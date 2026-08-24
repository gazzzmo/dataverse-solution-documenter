"""
Dataverse Solution Documenter — FastAPI application entry point.
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routers import upload

app = FastAPI(
    title="Dataverse Solution Documenter",
    description="Upload a Dataverse solution .zip and receive structured Markdown documentation.",
    version="0.1.0",
)

app.include_router(upload.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", include_in_schema=False)
async def root():
    return FileResponse("app/static/index.html")
