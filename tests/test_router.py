"""
Tests for the FastAPI upload router and parse-warning plumbing.
"""
import io
import json
import zipfile

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.core import process_solution_zip


client = TestClient(app)


def _make_zip(files: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, content in files.items():
            z.writestr(name, content)
    return buf.getvalue()


SOLUTION_XML = b"""<?xml version="1.0" encoding="utf-8"?>
<ImportExportXml>
  <SolutionManifest>
    <UniqueName>ApiTestSolution</UniqueName>
    <LocalizedNames>
      <LocalizedName description="Api Test Solution" languagecode="1033" />
    </LocalizedNames>
    <Version>1.0.0.0</Version>
    <Managed>0</Managed>
  </SolutionManifest>
</ImportExportXml>"""

GOOD_FLOW = json.dumps({
    "properties": {
        "definition": {
            "triggers": {"When_a_row_is_added": {}},
            "actions": {"Create_row": {}},
        },
    },
}).encode()


# ---------------------------------------------------------------------------
# Upload router
# ---------------------------------------------------------------------------

def test_upload_rejects_non_zip_filename():
    r = client.post(
        "/api/upload",
        files={"file": ("notazip.txt", b"hello", "text/plain")},
    )
    assert r.status_code == 400
    assert "zip" in r.json()["detail"].lower()


def test_upload_rejects_invalid_zip():
    r = client.post(
        "/api/upload",
        files={"file": ("fake.zip", b"this is not a zip", "application/zip")},
    )
    assert r.status_code in (400, 413, 500)


def test_upload_happy_path_returns_zip():
    zip_bytes = _make_zip({
        "solution.xml": SOLUTION_XML,
        "Workflows/TestFlow-GUID1.json": GOOD_FLOW,
    })
    r = client.post(
        "/api/upload",
        files={"file": ("solution.zip", zip_bytes, "application/zip")},
    )
    assert r.status_code == 200
    assert r.headers["content-type"] == "application/zip"
    assert "ApiTestSolution_docs.zip" in r.headers["content-disposition"]
    out = zipfile.ZipFile(io.BytesIO(r.content))
    assert "README.md" in out.namelist()
    assert "solution-overview.md" in out.namelist()


def test_upload_reports_parse_warnings_header():
    # A workflow JSON that is invalid — the flow file can't be parsed.
    zip_bytes = _make_zip({
        "solution.xml": SOLUTION_XML,
        "Workflows/BadFlow-GUID1.json": b"{not valid json",
    })
    r = client.post(
        "/api/upload",
        files={"file": ("solution.zip", zip_bytes, "application/zip")},
    )
    assert r.status_code == 200
    # Warning surfaced via header (no silent failure)
    assert "X-Parse-Warnings" in r.headers or "BadFlow" in r.content.decode("utf-8", "ignore")


# ---------------------------------------------------------------------------
# Parse-warning plumbing
# ---------------------------------------------------------------------------

def test_process_solution_zip_collects_warnings_for_bad_flow():
    zip_bytes = _make_zip({
        "solution.xml": SOLUTION_XML,
        "Workflows/BrokenFlow-GUID1.json": b"{invalid json",
    })
    warnings: list[str] = []
    parsed, docs = process_solution_zip(zip_bytes, warnings=warnings)

    # The broken flow should not crash the pipeline…
    assert any(w["name"] == "BrokenFlow-GUID1" for w in parsed["workflows"])
    # …and the failure should be reported, not swallowed.
    assert warnings, "expected at least one parse warning for the broken flow"
    assert any("BrokenFlow" in w or "Workflows/" in w for w in warnings)

    # Warnings appear in the generated README index.
    assert "Parse Warnings" in docs["README.md"]


def test_process_solution_zip_no_warnings_on_clean_solution():
    zip_bytes = _make_zip({
        "solution.xml": SOLUTION_XML,
        "Workflows/GoodFlow-GUID1.json": GOOD_FLOW,
    })
    warnings: list[str] = []
    _, docs = process_solution_zip(zip_bytes, warnings=warnings)
    assert warnings == []
    assert "Parse Warnings" not in docs["README.md"]
