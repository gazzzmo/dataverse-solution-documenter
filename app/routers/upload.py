"""
Upload router — accepts a Dataverse solution .zip, orchestrates parsing,
and returns a ZIP of Markdown documentation files.
"""
import io
import zipfile
import tempfile
import os
from pathlib import Path

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

from app.parsers.solution import parse_solution
from app.parsers.customizations import parse_customizations
from app.parsers.workflows import parse_workflows
from app.parsers.webresources import parse_webresources
from app.parsers.env_vars import parse_env_vars
from app.parsers.plugins import parse_plugins
from app.generators.markdown import generate_docs

router = APIRouter(prefix="/api", tags=["upload"])

ALLOWED_CONTENT_TYPES = {
    "application/zip",
    "application/x-zip-compressed",
    "application/octet-stream",
}
MAX_FILE_SIZE_MB = 100


@router.post("/upload", summary="Upload a Dataverse solution .zip")
async def upload_solution(file: UploadFile = File(...)):
    """
    Accepts a Dataverse solution export (.zip), parses its components,
    and returns a ZIP archive containing Markdown documentation files.
    """
    # Basic validation
    if not file.filename or not file.filename.lower().endswith(".zip"):
        raise HTTPException(status_code=400, detail="File must be a .zip archive.")

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size is {MAX_FILE_SIZE_MB} MB.",
        )

    # Validate it's actually a zip
    if not zipfile.is_zipfile(io.BytesIO(contents)):
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid ZIP archive.")

    solution_zip = zipfile.ZipFile(io.BytesIO(contents))
    namelist = solution_zip.namelist()

    # Parse each component
    solution_data = parse_solution(solution_zip, namelist)
    customizations_data = parse_customizations(solution_zip, namelist)
    workflows_data = parse_workflows(solution_zip, namelist)
    webresources_data = parse_webresources(solution_zip, namelist)
    env_vars_data = parse_env_vars(solution_zip, namelist)
    plugins_data = parse_plugins(solution_zip, namelist)

    # Bundle all parsed data
    parsed = {
        "solution": solution_data,
        "customizations": customizations_data,
        "workflows": workflows_data,
        "webresources": webresources_data,
        "env_vars": env_vars_data,
        "plugins": plugins_data,
    }

    # Generate Markdown documents
    docs = generate_docs(parsed)

    # Pack docs into a ZIP response
    out_buffer = io.BytesIO()
    with zipfile.ZipFile(out_buffer, "w", zipfile.ZIP_DEFLATED) as out_zip:
        for filename, content in docs.items():
            out_zip.writestr(filename, content)
    out_buffer.seek(0)

    solution_name = solution_data.get("unique_name", "solution").replace(" ", "_")
    zip_name = f"{solution_name}_docs.zip"

    return StreamingResponse(
        out_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{zip_name}"'},
    )
