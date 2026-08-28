"""
Dataverse Solution Documenter — FastAPI application entry point.
"""
from importlib.metadata import PackageNotFoundError, version as pkg_version

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers import upload


def _get_version() -> str:
    try:
        return pkg_version("dataverse-solution-documenter")
    except PackageNotFoundError:
        return "0.0.0.dev0"


app = FastAPI(
    title="Dataverse Solution Documenter",
    description="Upload a Dataverse solution .zip and receive structured Markdown documentation.",
    version=_get_version(),
)

app.include_router(upload.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("app/static/index.html")
