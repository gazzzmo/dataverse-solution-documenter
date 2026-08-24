"""
Upload router — accepts a Dataverse solution .zip, orchestrates parsing,
and returns a ZIP of Markdown documentation files.
"""
import io
import zipfile

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse

from app.core import process_solution_zip

router = APIRouter(prefix="/api", tags=["upload"])

MAX_FILE_SIZE_MB = 100


@router.post("/upload", summary="Upload a Dataverse solution .zip")
async def upload_solution(file: UploadFile = File(...)):
    """
    Accepts a Dataverse solution export (.zip), parses its components,
    and returns a ZIP archive containing Markdown documentation files.
    """
    if not file.filename or not file.filename.lower().endswith(".zip"):
        raise HTTPException(status_code=400, detail="File must be a .zip archive.")

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail=f"File too large. Maximum size is {MAX_FILE_SIZE_MB} MB.",
        )

    if not zipfile.is_zipfile(io.BytesIO(contents)):
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid ZIP archive.")

    try:
        parsed, docs = process_solution_zip(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process solution: {e}")

    out_buffer = io.BytesIO()
    with zipfile.ZipFile(out_buffer, "w", zipfile.ZIP_DEFLATED) as out_zip:
        for filename, content in docs.items():
            out_zip.writestr(filename, content)
    out_buffer.seek(0)

    solution_name = parsed.get("solution", {}).get("unique_name", "solution").replace(" ", "_")
    zip_name = f"{solution_name}_docs.zip"

    return StreamingResponse(
        out_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f'attachment; filename="{zip_name}"'},
    )

