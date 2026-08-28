"""
Parser: PCF Custom Controls

Metadata sources:
  1. customizations.xml <CustomControls/CustomControl> — name + manifest file path
  2. Controls/<namespace.name>/ControlManifest.xml — full control detail

Real-world structure:

  customizations.xml:
    <CustomControls>
      <CustomControl>
        <Name>mycompany_MyControl.MyControl</Name>
        <FileName>/Controls/mycompany_MyControl.MyControl/ControlManifest.xml</FileName>
      </CustomControl>
    </CustomControls>

  ControlManifest.xml:
    <manifest>
      <control namespace="MyCompany"
               constructor="MyControl"
               version="1.0.0"
               display-name-key="MyControl"
               description-key="Example custom control"
               control-type="standard"
               api-version="1.3.15">
        <property name="MyProperty"
                  of-type="SingleLine.Text"
                  usage="output"
                  required="false" />
        <resources>
          <!-- bundle.js, css, resx files listed here -->
        </resources>
        <built-by name="pac" version="1.34.3" />
      </control>
    </manifest>
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def parse_controls(
    zf: zipfile.ZipFile,
    namelist: list[str],
    controls_meta: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """
    Return a list of PCF custom control metadata dicts.

    controls_meta: pre-parsed list from customizations.py (name + manifest path).
    Falls back to scanning customizations.xml if not supplied.
    """
    controls: list[dict[str, Any]] = []
    namelist_lower = {n.lower(): n for n in namelist}

    # Get base metadata list (name + manifest file path)
    if controls_meta is None:
        cust_file = next((n for n in namelist if n.lower() == "customizations.xml"), None)
        if not cust_file:
            return []
        root = ET.fromstring(zf.read(cust_file))
        controls_meta = _parse_controls_meta(root)

    for meta in controls_meta:
        control_name = meta.get("name", "")
        manifest_path = meta.get("manifest_file", "").lstrip("/")

        # Resolve manifest path (case-insensitive)
        actual_manifest = None
        if manifest_path in namelist:
            actual_manifest = manifest_path
        else:
            actual_manifest = namelist_lower.get(manifest_path.lower())

        control: dict[str, Any] = {
            "name": control_name,
            "namespace": "",
            "constructor": "",
            "display_name": "",
            "description": "",
            "version": "",
            "control_type": "",
            "api_version": "",
            "properties": [],
            "resources": [],
            "built_by": "",
            "manifest_file": manifest_path,
            "folder": "/".join(manifest_path.split("/")[:2]) if manifest_path else "",
        }

        if actual_manifest:
            try:
                mfst_root = ET.fromstring(zf.read(actual_manifest))
                ctrl_el = mfst_root.find("control")
                if ctrl_el is not None:
                    control["namespace"] = ctrl_el.get("namespace", "")
                    control["constructor"] = ctrl_el.get("constructor", "")
                    control["display_name"] = (
                        ctrl_el.get("display-name-key", "")
                        or f"{control['namespace']}.{control['constructor']}"
                    )
                    control["description"] = ctrl_el.get("description-key", "")
                    control["version"] = ctrl_el.get("version", "")
                    control["control_type"] = ctrl_el.get("control-type", "")
                    control["api_version"] = ctrl_el.get("api-version", "")

                    # Properties (inputs/outputs)
                    for prop in ctrl_el.findall("property"):
                        control["properties"].append({
                            "name": prop.get("name", ""),
                            "display_name": prop.get("display-name-key", ""),
                            "description": prop.get("description-key", ""),
                            "type": prop.get("of-type", ""),
                            "usage": prop.get("usage", ""),  # bound/input/output
                            "required": prop.get("required", "false") == "true",
                        })

                    # Resources (files bundled with control)
                    res_el = ctrl_el.find("resources")
                    if res_el is not None:
                        for res in res_el:
                            path = res.get("path", "")
                            if path:
                                control["resources"].append(path)

                    # Built-by tool info
                    built_el = ctrl_el.find("built-by")
                    if built_el is not None:
                        control["built_by"] = (
                            f"{built_el.get('name', '')} v{built_el.get('version', '')}"
                        )
            except ET.ParseError:
                pass

        # Enrich with file sizes from zip
        control_folder = "/".join(manifest_path.split("/")[:2]) if "/" in manifest_path else ""
        folder_files = [n for n in namelist if n.startswith(control_folder + "/") and not n.endswith("/")]
        control["files"] = [
            {
                "path": f,
                "size_bytes": zf.getinfo(f).file_size,
            }
            for f in folder_files
        ]
        total_size = sum(zf.getinfo(f).file_size for f in folder_files)
        control["total_size_bytes"] = total_size

        controls.append(control)

    return controls


def _parse_controls_meta(root: ET.Element) -> list[dict[str, Any]]:
    """Extract CustomControl name + manifest path from customizations.xml."""
    meta = []
    for cc in root.findall("CustomControls/CustomControl"):
        name = (cc.findtext("Name") or "").strip()
        file_path = (cc.findtext("FileName") or "").strip().lstrip("/")
        if name:
            meta.append({"name": name, "manifest_file": file_path})
    return meta
