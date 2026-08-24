"""
Basic tests for the solution parsers.
"""
import io
import zipfile
import pytest
from app.parsers.solution import parse_solution
from app.parsers.customizations import parse_customizations
from app.parsers.workflows import parse_workflows
from app.parsers.webresources import parse_webresources
from app.parsers.env_vars import parse_env_vars
from app.parsers.plugins import parse_plugins


SOLUTION_XML = b"""<?xml version="1.0"?>
<ImportExportXml>
  <SolutionManifest>
    <UniqueName>TestSolution</UniqueName>
    <Version>1.0.0.0</Version>
    <Managed>0</Managed>
    <Publisher>
      <UniqueName>TestPublisher</UniqueName>
      <CustomizationPrefix>ts</CustomizationPrefix>
    </Publisher>
    <Description/>
    <RootComponents>
      <RootComponent type="1" id="{aaa}" />
      <RootComponent type="2" id="{bbb}" />
    </RootComponents>
  </SolutionManifest>
</ImportExportXml>"""


def _make_zip(files: dict) -> zipfile.ZipFile:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, content in files.items():
            zf.writestr(name, content)
    buf.seek(0)
    return zipfile.ZipFile(buf)


def test_parse_solution_basic():
    zf = _make_zip({"solution.xml": SOLUTION_XML})
    result = parse_solution(zf, zf.namelist())
    assert result["unique_name"] == "TestSolution"
    assert result["version"] == "1.0.0.0"
    assert result["publisher_name"] == "TestPublisher"
    assert result["publisher_prefix"] == "ts"
    assert result["component_count"] == 2
    assert result["is_managed"] == "0"


def test_parse_solution_missing():
    zf = _make_zip({"other.xml": b"<root/>"})
    result = parse_solution(zf, zf.namelist())
    assert result == {}


def test_parse_workflows_empty():
    zf = _make_zip({"solution.xml": SOLUTION_XML})
    result = parse_workflows(zf, zf.namelist())
    assert result == []


def test_parse_webresources():
    zf = _make_zip({
        "WebResources/ts_script.js": b"console.log('hello');",
        "WebResources/ts_style.css": b"body { margin: 0; }",
    })
    result = parse_webresources(zf, zf.namelist())
    assert len(result) == 2
    types = {r["name"]: r["type"] for r in result}
    assert types["ts_script.js"] == "JavaScript"
    assert types["ts_style.css"] == "CSS"


def test_parse_env_vars_empty():
    zf = _make_zip({"solution.xml": SOLUTION_XML})
    result = parse_env_vars(zf, zf.namelist())
    assert result == []
