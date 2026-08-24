"""
Parser: Plugin Assemblies

Extracts plugin assembly and step registration metadata.
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def parse_plugins(zf: zipfile.ZipFile, namelist: list[str]) -> list[dict[str, Any]]:
    """Return a list of plugin assembly metadata dicts."""
    plugins = []

    plugin_files = [
        n for n in namelist
        if "pluginassembly" in n.lower() and n.endswith(".xml")
    ]

    for pf in plugin_files:
        try:
            root = ET.fromstring(zf.read(pf))
        except Exception:
            continue

        for row in root.iter("pluginassembly"):
            assembly: dict[str, Any] = {
                "name": row.findtext("name") or "",
                "version": row.findtext("version") or "",
                "description": row.findtext("description") or "",
                "isolation_mode": row.findtext("isolationmode") or "",
                "steps": [],
            }

            for step in row.iter("sdkmessageprocessingstep"):
                assembly["steps"].append({
                    "name": step.findtext("name") or "",
                    "message": step.findtext("sdkmessageid") or "",
                    "stage": step.findtext("stage") or "",
                    "mode": step.findtext("mode") or "",
                    "primary_entity": step.findtext("primaryobjecttypecode") or "",
                })

            plugins.append(assembly)

    return plugins
