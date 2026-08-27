"""
Parser: Workflows

Metadata comes from customizations.xml (parsed by customizations.py) cross-referenced
with the actual workflow files in the Workflows/ folder.

Cloud flows (JSON, Category=5): extract triggers, actions, connection references
Classic workflows (XAML, Category=0/2/3/4): metadata only from customizations.xml
"""
import zipfile
import json
import xml.etree.ElementTree as ET
from typing import Any


def _extract_cloud_flow_details(content: bytes) -> dict[str, Any]:
    """Parse a Power Automate JSON flow file for trigger, action, and dependency metadata."""
    try:
        data = json.loads(content)
    except Exception:
        return {}

    props = data.get("properties", {})
    defn = props.get("definition", {})

    triggers = list(defn.get("triggers", {}).keys())
    actions_dict = defn.get("actions", {})
    actions = list(actions_dict.keys())
    conn_refs = list(props.get("connectionReferences", {}).keys())

    # Extract detailed connection reference logical names
    detailed_conn_refs = []
    for ref_key, ref_val in props.get("connectionReferences", {}).items():
        logical_name = ref_val.get("connection", {}).get("connectionReferenceLogicalName") or ref_key
        if logical_name not in detailed_conn_refs:
            detailed_conn_refs.append(logical_name)

    # Extract environment variables referenced in flow parameters or actions
    env_vars = []
    for param_name, param_val in defn.get("parameters", {}).items():
        if isinstance(param_val, dict):
            schema_name = param_val.get("metadata", {}).get("schemaName")
            if schema_name and schema_name not in env_vars:
                env_vars.append(schema_name)

    # Extract Dataverse entities accessed across triggers and actions
    dataverse_entities = []

    def _scan_for_entities(obj: Any):
        if isinstance(obj, dict):
            entity_name = obj.get("entityName") or obj.get("item/entityName")
            if entity_name and isinstance(entity_name, str) and entity_name not in dataverse_entities:
                dataverse_entities.append(entity_name)
            for v in obj.values():
                _scan_for_entities(v)
        elif isinstance(obj, list):
            for item in obj:
                _scan_for_entities(item)

    _scan_for_entities(defn.get("triggers", {}))
    _scan_for_entities(actions_dict)

    return {
        "triggers": triggers,
        "actions": actions,
        "connection_refs": detailed_conn_refs or conn_refs,
        "env_vars": env_vars,
        "dataverse_entities": dataverse_entities,
        "schema_version": defn.get("$schema", ""),
    }


def parse_workflows(
    zf: zipfile.ZipFile,
    namelist: list[str],
    workflows_meta: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """
    Return a list of workflow metadata dicts.

    workflows_meta: pre-parsed list from customizations.py (avoids re-parsing customizations.xml).
    If not supplied, falls back to scanning files only.
    """
    workflows: list[dict[str, Any]] = []
    meta_by_id: dict[str, dict[str, Any]] = {}

    if workflows_meta:
        for m in workflows_meta:
            wf_id = m.get("id", "").lower().strip("{}")
            if wf_id:
                meta_by_id[wf_id] = m

    # Build a map of zip path (lower) → actual zip path for case-insensitive lookup
    namelist_lower = {n.lower(): n for n in namelist}

    # Build a map of GUID → zip path for flow files (fallback when metadata has no file path)
    flow_files_by_guid: dict[str, str] = {}
    for n in namelist:
        if n.startswith("Workflows/") and not n.endswith("/"):
            # Filename format: DisplayName-GUID.json / DisplayName-GUID.xaml
            fname = n.split("/")[-1]
            base = fname.rsplit(".", 1)[0]  # strip extension
            # GUID is the last 36 chars (with hyphens) of the base name
            parts = base.rsplit("-", 5)  # GUID is 5 dash-separated groups
            if len(parts) >= 6:  # need name + 5 GUID segments
                # Reconstruct the GUID from the last 5 segments
                guid_parts = parts[-5:]
                guid = "-".join(guid_parts).lower()
                flow_files_by_guid[guid] = n

    # Track which zip paths were covered by metadata
    processed_zip_paths: set[str] = set()
    processed_guids: set[str] = set()

    # First pass: use customizations.xml metadata as the authoritative source
    for meta in (workflows_meta or []):
        wf_id = meta.get("id", "").lower()
        processed_guids.add(wf_id)

        wf: dict[str, Any] = {
            "name": meta.get("name", ""),
            "description": meta.get("description", ""),
            "category": meta.get("category", ""),
            "primary_entity": meta.get("primary_entity", ""),
            "state": "Active" if meta.get("state") == "1" else "Inactive",
            "on_demand": meta.get("on_demand", False),
            "trigger_on_create": meta.get("trigger_on_create", False),
            "trigger_on_delete": meta.get("trigger_on_delete", False),
            "introduced_version": meta.get("introduced_version", ""),
            "file": meta.get("json_file") or meta.get("xaml_file") or "",
            # Cloud flow extras (populated below if JSON)
            "triggers": [],
            "actions": [],
            "connection_refs": [],
            "env_vars": [],
            "dataverse_entities": [],
        }

        # Find matching file: prefer the path declared in metadata, fall back to GUID match
        zip_path = None
        declared_path = (meta.get("json_file") or meta.get("xaml_file") or "").lstrip("/")
        if declared_path:
            # Try exact, then case-insensitive
            if declared_path in namelist:
                zip_path = declared_path
            else:
                zip_path = namelist_lower.get(declared_path.lower())
        if zip_path is None:
            zip_path = flow_files_by_guid.get(wf_id)
        if zip_path and zip_path in namelist:
            wf["file"] = zip_path
            try:
                content = zf.read(zip_path)
                if zip_path.endswith(".json"):
                    details = _extract_cloud_flow_details(content)
                    wf.update({
                        "triggers": details.get("triggers", []),
                        "actions": details.get("actions", []),
                        "connection_refs": details.get("connection_refs", []),
                        "env_vars": details.get("env_vars", []),
                        "dataverse_entities": details.get("dataverse_entities", []),
                    })
            except Exception:
                pass

        if zip_path:
            processed_zip_paths.add(zip_path)
        workflows.append(wf)

    # Second pass: any files in the zip NOT covered by metadata
    for n in namelist:
        if not n.startswith("Workflows/") or n.endswith("/"):
            continue
        if n in processed_zip_paths:
            continue

        fname = n.split("/")[-1]
        base = fname.rsplit(".", 1)[0]
        wf = {
            "name": base,
            "description": "",
            "category": "Unknown",
            "primary_entity": "",
            "state": "Unknown",
            "on_demand": False,
            "trigger_on_create": False,
            "trigger_on_delete": False,
            "introduced_version": "",
            "file": n,
            "triggers": [],
            "actions": [],
            "connection_refs": [],
            "env_vars": [],
            "dataverse_entities": [],
        }
        try:
            content = zf.read(n)
            if n.endswith(".json"):
                details = _extract_cloud_flow_details(content)
                wf.update({
                    "triggers": details.get("triggers", []),
                    "actions": details.get("actions", []),
                    "connection_refs": details.get("connection_refs", []),
                    "env_vars": details.get("env_vars", []),
                    "dataverse_entities": details.get("dataverse_entities", []),
                })
        except Exception:
            pass
        workflows.append(wf)

    return workflows
