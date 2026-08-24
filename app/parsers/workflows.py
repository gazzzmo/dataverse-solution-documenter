"""
Parser: Workflows

Lists workflow definitions from the Workflows/ folder inside the solution zip.
Extracts name, description, trigger, and primary entity from XAML/JSON.
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def parse_workflows(zf: zipfile.ZipFile, namelist: list[str]) -> list[dict[str, Any]]:
    """Return a list of workflow metadata dicts."""
    workflows = []

    wf_files = [
        n for n in namelist
        if n.startswith("Workflows/") and (n.endswith(".xaml") or n.endswith(".json") or n.endswith(".xml"))
    ]

    for wf_file in wf_files:
        try:
            content = zf.read(wf_file).decode("utf-8", errors="replace")
        except Exception:
            continue

        wf: dict[str, Any] = {
            "file": wf_file,
            "name": wf_file.split("/")[-1].rsplit(".", 1)[0],
            "description": "",
            "primary_entity": "",
            "trigger": "",
            "category": "",
        }

        # Try XML parse for classic workflows
        if wf_file.endswith(".xaml") or wf_file.endswith(".xml"):
            try:
                root = ET.fromstring(content)
                # Common locations for workflow metadata
                wf["name"] = root.get("Name") or root.get("DisplayName") or wf["name"]
                wf["description"] = root.get("Description") or ""
                wf["primary_entity"] = root.get("PrimaryEntity") or root.get("Entity") or ""
                wf["trigger"] = root.get("TriggerOnCreate") or root.get("Category") or ""
            except ET.ParseError:
                pass

        workflows.append(wf)

    return workflows
