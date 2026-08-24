"""
Core documentation engine for Dataverse solutions.
Extracts parsing and document generation into a reusable pipeline
used by both the CLI, Web app, and CI/CD tasks.
"""
import io
import zipfile
from pathlib import Path
from typing import Dict, Any, Union

from app.parsers.solution import parse_solution
from app.parsers.customizations import parse_customizations
from app.parsers.workflows import parse_workflows
from app.parsers.webresources import parse_webresources
from app.parsers.env_vars import parse_env_vars
from app.parsers.plugins import parse_plugins
from app.parsers.controls import parse_controls
from app.generators.markdown import generate_docs


def process_solution_zip(zip_source: Union[str, Path, bytes, io.BytesIO]) -> tuple[Dict[str, Any], Dict[str, str]]:
    """
    Parse a Dataverse solution zip archive and generate Markdown documentation.

    Args:
        zip_source: Path to zip file, bytes, or file-like object.

    Returns:
        tuple of (parsed_data, docs_dict) where docs_dict maps filenames to Markdown strings.
    """
    if isinstance(zip_source, (str, Path)):
        zf = zipfile.ZipFile(str(zip_source), "r")
    elif isinstance(zip_source, bytes):
        zf = zipfile.ZipFile(io.BytesIO(zip_source), "r")
    else:
        zf = zipfile.ZipFile(zip_source, "r")

    try:
        namelist = zf.namelist()

        solution_data = parse_solution(zf, namelist)
        cust = parse_customizations(zf, namelist)
        workflows_data = parse_workflows(
            zf, namelist,
            workflows_meta=cust.get("workflows_meta", []),
        )
        webresources_data = parse_webresources(
            zf, namelist,
            web_resources_meta=cust.get("web_resources", []),
        )
        env_vars_data = parse_env_vars(zf, namelist)
        plugins_data = parse_plugins(
            zf, namelist,
            plugins_meta=cust.get("plugin_assemblies", []),
            steps_meta=cust.get("plugin_steps", []),
        )
        controls_data = parse_controls(
            zf, namelist,
            controls_meta=cust.get("custom_controls_meta", []),
        )

        parsed = {
            "solution": solution_data,
            "entities": cust.get("entities", []),
            "roles": cust.get("roles", []),
            "entity_relationships": cust.get("entity_relationships", []),
            "connection_references": cust.get("connection_references", []),
            "app_modules": cust.get("app_modules", []),
            "global_option_sets": cust.get("global_option_sets", []),
            "workflows": workflows_data,
            "webresources": webresources_data,
            "env_vars": env_vars_data,
            "plugins": plugins_data,
            "controls": controls_data,
        }

        docs = generate_docs(parsed)
        return parsed, docs
    finally:
        zf.close()
