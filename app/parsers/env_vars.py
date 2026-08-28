"""
Parser: Environment Variables

Files are at: environmentvariabledefinitions/<schemaname>/environmentvariabledefinition.xml

Real-world structure (from a real Dataverse solution):
  <environmentvariabledefinition schemaname="bcc_targetenvironment">
    <description default="URL of the target environment">
      <label description="URL of the target environment" languagecode="1033" />
    </description>
    <displayname default="Target Environment URL">
      <label description="Target Environment URL" languagecode="1033" />
    </displayname>
    <introducedversion>0.0.0.1</introducedversion>
    <iscustomizable>1</iscustomizable>
    <isrequired>0</isrequired>
    <secretstore>0</secretstore>
    <type>100000000</type>
  </environmentvariabledefinition>
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any

# Dataverse environment variable type codes
EV_TYPES = {
    "100000000": "String",
    "100000001": "Decimal Number",
    "100000002": "Boolean",
    "100000003": "JSON",
    "100000004": "Data Source",
}


def _localized_value(el: ET.Element | None) -> str:
    """
    Extract value from an env var field element.
    Tries @default attribute first, then <label @description> for lang=1033.
    """
    if el is None:
        return ""
    # @default is the most reliable
    default = el.get("default", "").strip()
    if default:
        return default
    # Fall back to first label
    for label in el.findall("label"):
        desc = label.get("description", "").strip()
        if desc:
            return desc
    return (el.text or "").strip()


def parse_env_vars(
    zf: zipfile.ZipFile,
    namelist: list[str],
    warnings: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Return a list of environment variable metadata dicts."""
    env_vars: list[dict[str, Any]] = []

    ev_files = [
        n for n in namelist
        if n.startswith("environmentvariabledefinitions/")
        and n.endswith("/environmentvariabledefinition.xml")
    ]

    for ev_file in ev_files:
        try:
            root = ET.fromstring(zf.read(ev_file))
        except Exception as e:
            if warnings is not None:
                warnings.append(f"Could not parse environment variable definition '{ev_file}': {e}")
            continue

        # Schema name from element attribute
        schema_name = (root.get("schemaname") or "").strip()

        type_code = (root.findtext("type") or "").strip()
        is_required = (root.findtext("isrequired") or "0").strip() == "1"
        is_secret = (root.findtext("secretstore") or "0").strip() != "0"
        introduced = (root.findtext("introducedversion") or "").strip()

        env_vars.append({
            "schema_name": schema_name,
            "display_name": _localized_value(root.find("displayname")),
            "description": _localized_value(root.find("description")),
            "type": EV_TYPES.get(type_code, f"Unknown ({type_code})"),
            "type_code": type_code,
            "is_required": is_required,
            "is_secret": is_secret,
            "introduced_version": introduced,
        })

    return env_vars
