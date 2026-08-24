"""
Parser: Web Resources

Indexes all web resources found in the WebResources/ folder.
"""
import zipfile
from typing import Any

WEB_RESOURCE_TYPES = {
    ".js": "JavaScript",
    ".html": "HTML",
    ".htm": "HTML",
    ".css": "CSS",
    ".xml": "XML",
    ".png": "PNG Image",
    ".jpg": "JPEG Image",
    ".jpeg": "JPEG Image",
    ".gif": "GIF Image",
    ".svg": "SVG Image",
    ".ico": "Icon",
    ".resx": "String Resource",
    ".xsl": "XSL Stylesheet",
}


def parse_webresources(zf: zipfile.ZipFile, namelist: list[str]) -> list[dict[str, Any]]:
    """Return a list of web resource metadata dicts."""
    resources = []

    wr_files = [
        n for n in namelist
        if n.startswith("WebResources/") and not n.endswith("/")
    ]

    for wr_file in wr_files:
        suffix = "." + wr_file.rsplit(".", 1)[-1].lower() if "." in wr_file else ""
        file_type = WEB_RESOURCE_TYPES.get(suffix, "Other")
        size_bytes = zf.getinfo(wr_file).file_size

        resources.append({
            "path": wr_file,
            "name": wr_file.split("/")[-1],
            "type": file_type,
            "size_bytes": size_bytes,
        })

    return resources
