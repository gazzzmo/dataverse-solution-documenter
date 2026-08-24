"""
Parser: solution.xml

Extracts top-level solution metadata — name, version, publisher, description.
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def parse_solution(zf: zipfile.ZipFile, namelist: list[str]) -> dict[str, Any]:
    """Parse solution.xml and return a flat dict of solution metadata."""
    result: dict[str, Any] = {}

    solution_file = next(
        (n for n in namelist if n.lower() == "solution.xml"), None
    )
    if not solution_file:
        return result

    xml_bytes = zf.read(solution_file)
    root = ET.fromstring(xml_bytes)

    ns = {"s": root.tag.split("}")[0].lstrip("{") if "}" in root.tag else ""}

    def find_text(path: str) -> str:
        """XPath helper that gracefully returns empty string if not found."""
        # Try with namespace, then without
        el = root.find(path)
        return (el.text or "").strip() if el is not None else ""

    # Unique name / display name / version
    result["unique_name"] = find_text(".//UniqueName") or find_text(".//uniquename")
    result["version"] = find_text(".//Version") or find_text(".//version")
    result["description"] = find_text(".//Description") or find_text(".//description")

    # Publisher
    pub = root.find(".//Publisher")
    if pub is not None:
        result["publisher_name"] = (pub.findtext("UniqueName") or pub.findtext("uniquename") or "").strip()
        result["publisher_prefix"] = (pub.findtext("CustomizationPrefix") or pub.findtext("customizationprefix") or "").strip()
    else:
        result["publisher_name"] = ""
        result["publisher_prefix"] = ""

    # Managed / unmanaged — search recursively through all elements
    managed_el = None
    for tag in ("Managed", "managed", "ismanaged", "IsManaged"):
        managed_el = root.find(f".//{tag}")
        if managed_el is not None:
            break
    result["is_managed"] = (managed_el.text or "0").strip() if managed_el is not None else "unknown"

    # Component counts — just raw list of component type IDs for now
    components = root.findall(".//RootComponents/RootComponent")
    result["component_count"] = len(components)

    return result
