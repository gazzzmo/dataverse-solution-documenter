"""
Parser: Web Resources

Metadata for web resources is in customizations.xml <WebResources/WebResource>,
not derivable from the ZIP filenames (which use GUID-based names with no extension).

This parser receives the already-parsed web_resources list from customizations.py
and enriches it with file size from the actual zip entry.
"""
import zipfile
from typing import Any

WEB_RESOURCE_TYPES = {
    "1": "HTML", "2": "CSS", "3": "JavaScript", "4": "XML",
    "5": "PNG Image", "6": "JPEG Image", "7": "GIF Image",
    "8": "XAP (Silverlight)", "9": "XSL Stylesheet", "10": "Icon",
    "11": "SVG Image", "12": "String Resource (RESX)",
}


def parse_webresources(
    zf: zipfile.ZipFile,
    namelist: list[str],
    web_resources_meta: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """
    Return a list of web resource metadata dicts.

    web_resources_meta: pre-parsed list from customizations.py.
    Falls back to scanning the WebResources/ folder if not provided.
    """
    resources: list[dict[str, Any]] = []

    if web_resources_meta:
        # Use metadata from customizations.xml, enrich with file size from zip
        for wr in web_resources_meta:
            file_path = wr.get("file", "").lstrip("/")
            size_bytes = 0
            if file_path and file_path in namelist:
                try:
                    size_bytes = zf.getinfo(file_path).file_size
                except KeyError:
                    # Try case-insensitive match
                    lower_map = {n.lower(): n for n in namelist}
                    actual = lower_map.get(file_path.lower())
                    if actual:
                        size_bytes = zf.getinfo(actual).file_size

            resources.append({
                "name": wr.get("name", ""),
                "display_name": wr.get("display_name", ""),
                "type": wr.get("type", "Unknown"),
                "type_code": wr.get("type_code", ""),
                "file": file_path,
                "size_bytes": size_bytes,
                "introduced_version": wr.get("introduced_version", ""),
            })
    else:
        # Fallback: scan WebResources/ folder — type derived from filename if it has an extension
        EXTENSION_TYPES = {
            ".js": "JavaScript", ".html": "HTML", ".htm": "HTML",
            ".css": "CSS", ".xml": "XML", ".png": "PNG Image",
            ".jpg": "JPEG Image", ".jpeg": "JPEG Image", ".gif": "GIF Image",
            ".svg": "SVG Image", ".ico": "Icon", ".resx": "String Resource (RESX)",
            ".xsl": "XSL Stylesheet",
        }
        for n in namelist:
            if not n.startswith("WebResources/") or n.endswith("/"):
                continue
            fname = n.split("/")[-1]
            suffix = ("." + fname.rsplit(".", 1)[-1].lower()) if "." in fname else ""
            file_type = EXTENSION_TYPES.get(suffix, "Unknown (no extension in ZIP)")
            try:
                size_bytes = zf.getinfo(n).file_size
            except KeyError:
                size_bytes = 0
            resources.append({
                "name": fname,
                "display_name": fname,
                "type": file_type,
                "type_code": "",
                "file": n,
                "size_bytes": size_bytes,
                "introduced_version": "",
            })

    return resources
