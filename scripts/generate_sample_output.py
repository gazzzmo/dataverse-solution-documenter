"""
generate_sample_output.py

Runs the full documentation pipeline against every zip in sample-solutions/
and writes the resulting Markdown files to sample-output/<SolutionName>/.

Usage (from repo root, with venv active):
    python scripts/generate_sample_output.py
"""
import sys
import os
import zipfile
import glob

# Make sure the repo root is on the path when running as a script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.parsers.solution import parse_solution
from app.parsers.customizations import parse_customizations
from app.parsers.workflows import parse_workflows
from app.parsers.webresources import parse_webresources
from app.parsers.env_vars import parse_env_vars
from app.parsers.plugins import parse_plugins
from app.parsers.controls import parse_controls
from app.generators.markdown import generate_docs
from app.core import process_solution_zip

SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "..", "sample-solutions")
OUTPUT_DIR  = os.path.join(os.path.dirname(__file__), "..", "sample-output")


def process_zip(zip_path: str) -> None:
    zip_name = os.path.basename(zip_path)
    # Derive a clean folder name — strip version suffix and extension
    # e.g. "MySolution_1_1_0_0.zip" -> "MySolution"
    base = os.path.splitext(zip_name)[0]
    parts = base.split("_")
    # Drop trailing numeric version segments
    while parts and parts[-1].isdigit():
        parts.pop()
    folder_name = "_".join(parts) if parts else base

    out_dir = os.path.join(OUTPUT_DIR, folder_name)
    os.makedirs(out_dir, exist_ok=True)

    print(f"\n📦 Processing: {zip_name}")
    print(f"   Output → sample-output/{folder_name}/")

    parsed, docs = process_solution_zip(zip_path)

    for filename, content in docs.items():
        out_path = os.path.join(out_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   ✅ {filename}  ({len(content):,} chars)")

    print(f"   → {len(docs)} documents written.")


if __name__ == "__main__":
    zip_files = sorted(glob.glob(os.path.join(SAMPLES_DIR, "*.zip")))
    if not zip_files:
        print("No zip files found in sample-solutions/")
        sys.exit(1)

    print(f"Found {len(zip_files)} sample solution(s) to process.")
    for zp in zip_files:
        process_zip(zp)

    print("\n✨ Done. Documentation written to sample-output/")
