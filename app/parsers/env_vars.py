"""
Parser: Environment Variables

Extracts environment variable definitions and (where present) default values
from environmentvariabledefinition XML files.
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def parse_env_vars(zf: zipfile.ZipFile, namelist: list[str]) -> list[dict[str, Any]]:
    """Return a list of environment variable metadata dicts."""
    env_vars = []

    ev_files = [
        n for n in namelist
        if "environmentvariabledefinition" in n.lower() and n.endswith(".xml")
    ]

    for ev_file in ev_files:
        try:
            content = zf.read(ev_file)
            root = ET.fromstring(content)
        except Exception:
            continue

        for row in root.iter("environmentvariabledefinition"):
            env_vars.append({
                "schema_name": row.findtext("schemaname") or "",
                "display_name": row.findtext("displayname") or "",
                "description": row.findtext("description") or "",
                "type": row.findtext("type") or "",
                "default_value": row.findtext("defaultvalue") or "(none)",
            })

        # Also handle single-record files
        if not list(root.iter("environmentvariabledefinition")):
            env_vars.append({
                "schema_name": root.findtext("schemaname") or ev_file,
                "display_name": root.findtext("displayname") or "",
                "description": root.findtext("description") or "",
                "type": root.findtext("type") or "",
                "default_value": root.findtext("defaultvalue") or "(none)",
            })

    return env_vars
