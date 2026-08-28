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
_CHUNK_SIZE = 1024 * 1024  # 1 MB


async def _read_upload_limited(file: UploadFile, max_bytes: int) -> bytes:
    """
    Stream the upload in chunks, enforcing the size limit as data arrives
    instead of buffering the whole file first.
    """
    buffer = io.BytesIO()
    total = 0
    while chunk := await file.read(_CHUNK_SIZE):
        total += len(chunk)
        if total > max_bytes:
            raise HTTPException(
                status_code=413,
                detail=f"File too large. Maximum size is {MAX_FILE_SIZE_MB} MB.",
            )
        buffer.write(chunk)
    return buffer.getvalue()


@router.post("/upload", summary="Upload a Dataverse solution .zip")
async def upload_solution(file: UploadFile = File(...)):
    """
    Accepts a Dataverse solution export (.zip), parses its components,
    and returns a ZIP archive containing Markdown documentation files.
    """
    if not file.filename or not file.filename.lower().endswith(".zip"):
        raise HTTPException(status_code=400, detail="File must be a .zip archive.")

    max_bytes = MAX_FILE_SIZE_MB * 1024 * 1024
    contents = await _read_upload_limited(file, max_bytes)

    if not zipfile.is_zipfile(io.BytesIO(contents)):
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid ZIP archive.")

    warnings: list[str] = []
    try:
        parsed, docs = process_solution_zip(contents, warnings=warnings)
    except zipfile.BadZipFile:
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid ZIP archive.")
    except KeyError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Solution archive is missing a required component: {e}.",
        )
    except Exception:
        # Do not leak internal error details to clients; log server-side instead.
        import logging

        logging.getLogger("uvicorn.error").exception("Solution processing failed")
        raise HTTPException(
            status_code=500,
            detail="Failed to process solution. Check the archive structure and try again.",
        )

    out_buffer = io.BytesIO()
    with zipfile.ZipFile(out_buffer, "w", zipfile.ZIP_DEFLATED) as out_zip:
        for filename, content in docs.items():
            out_zip.writestr(filename, content)
    out_buffer.seek(0)

    solution_name = parsed.get("solution", {}).get("unique_name", "solution").replace(" ", "_")
    zip_name = f"{solution_name}_docs.zip"

    headers = {"Content-Disposition": f'attachment; filename="{zip_name}"'}
    if warnings:
        headers["X-Parse-Warnings"] = str(len(warnings))

    return StreamingResponse(
        out_buffer,
        media_type="application/zip",
        headers=headers,
    )
