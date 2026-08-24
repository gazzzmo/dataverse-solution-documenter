"""
Tests for solution parsers — verified against IDCT real solution structure.
"""
import io
import zipfile
import pytest
from app.parsers.solution import parse_solution
from app.parsers.customizations import parse_customizations
from app.parsers.workflows import parse_workflows
from app.parsers.webresources import parse_webresources
from app.parsers.env_vars import parse_env_vars


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SOLUTION_XML = b"""<?xml version="1.0" encoding="utf-8"?>
<ImportExportXml>
  <SolutionManifest>
    <UniqueName>TestSolution</UniqueName>
    <LocalizedNames>
      <LocalizedName description="Test Solution Display" languagecode="1033" />
    </LocalizedNames>
    <Descriptions>
      <Description description="A test solution" languagecode="1033" />
    </Descriptions>
    <Version>1.0.0.0</Version>
    <Managed>0</Managed>
    <Publisher>
      <UniqueName>TestPublisher</UniqueName>
      <LocalizedNames>
        <LocalizedName description="Test Publisher Name" languagecode="1033" />
      </LocalizedNames>
      <CustomizationPrefix>ts</CustomizationPrefix>
      <CustomizationOptionValuePrefix>10000</CustomizationOptionValuePrefix>
    </Publisher>
    <RootComponents>
      <RootComponent type="1" id="{aaa}" />
      <RootComponent type="20" id="{bbb}" />
    </RootComponents>
  </SolutionManifest>
</ImportExportXml>"""


CUSTOMIZATIONS_XML = b"""<?xml version="1.0" encoding="utf-8"?>
<ImportExportXml>
  <Entities>
    <Entity Name="ts_testentity">
      <EntityInfo>
        <entity>
          <LocalizedNames>
            <LocalizedName description="Test Entity" languagecode="1033" />
          </LocalizedNames>
          <LocalizedCollectionNames>
            <LocalizedName description="Test Entities" languagecode="1033" />
          </LocalizedCollectionNames>
          <attributes>
            <attribute PhysicalName="ts_name">
              <Type>nvarchar</Type>
              <RequiredLevel>required</RequiredLevel>
              <displaynames>
                <displayname description="Name" languagecode="1033" />
              </displaynames>
            </attribute>
            <attribute PhysicalName="ts_status">
              <Type>picklist</Type>
              <RequiredLevel>none</RequiredLevel>
              <displaynames>
                <displayname description="Status" languagecode="1033" />
              </displaynames>
            </attribute>
          </attributes>
        </entity>
      </EntityInfo>
      <FormXml>
        <forms>
          <systemform>
            <formid>{form-001}</formid>
            <IntroducedVersion>1.0.0.0</IntroducedVersion>
            <FormActivationState>1</FormActivationState>
            <LocalizedNames>
              <LocalizedName description="Main Form" languagecode="1033" />
            </LocalizedNames>
          </systemform>
        </forms>
      </FormXml>
      <SavedQueries>
        <savedqueries>
          <savedquery>
            <querytype>0</querytype>
            <LocalizedNames>
              <LocalizedName description="Active Test Entities" languagecode="1033" />
            </LocalizedNames>
          </savedquery>
        </savedqueries>
      </SavedQueries>
    </Entity>
  </Entities>
  <Roles>
    <Role name="TS-ReadOnly" id="{role-001}" />
  </Roles>
  <EntityRelationships>
    <EntityRelationship Name="ts_rel_one" />
  </EntityRelationships>
  <connectionreferences>
    <connectionreference connectionreferencelogicalname="ts_shared_cds" />
  </connectionreferences>
  <AppModules>
    <AppModule>
      <UniqueName>ts_testapp</UniqueName>
      <LocalizedNames>
        <LocalizedName description="Test App" languagecode="1033" />
      </LocalizedNames>
    </AppModule>
  </AppModules>
  <Workflows>
    <Workflow WorkflowId="{wf-001}" Name="My Cloud Flow">
      <Category>5</Category>
      <PrimaryEntity>ts_testentity</PrimaryEntity>
      <StateCode>1</StateCode>
      <IntroducedVersion>1.0.0.0</IntroducedVersion>
      <JsonFileName>/Workflows/MyCloudFlow-WF-001.json</JsonFileName>
    </Workflow>
  </Workflows>
  <WebResources>
    <WebResource>
      <Name>ts_myscript.js</Name>
      <DisplayName>My Script</DisplayName>
      <WebResourceType>3</WebResourceType>
      <IntroducedVersion>1.0.0.0</IntroducedVersion>
      <FileName>/WebResources/ts_myscriptjsWF001</FileName>
    </WebResource>
  </WebResources>
  <optionsets />
</ImportExportXml>"""


ENV_VAR_XML = b"""<environmentvariabledefinition schemaname="ts_myenvvar">
  <displayname default="My Env Var">
    <label description="My Env Var" languagecode="1033" />
  </displayname>
  <description default="A test environment variable">
    <label description="A test environment variable" languagecode="1033" />
  </description>
  <type>100000000</type>
  <isrequired>1</isrequired>
  <secretstore>0</secretstore>
  <introducedversion>1.0.0.0</introducedversion>
</environmentvariabledefinition>"""


def _make_zip(files: dict) -> zipfile.ZipFile:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, content in files.items():
            if isinstance(content, str):
                content = content.encode("utf-8")
            zf.writestr(name, content)
    buf.seek(0)
    return zipfile.ZipFile(buf)


# ---------------------------------------------------------------------------
# Solution Parser
# ---------------------------------------------------------------------------

def test_parse_solution_basic():
    zf = _make_zip({"solution.xml": SOLUTION_XML})
    result = parse_solution(zf, zf.namelist())
    assert result["unique_name"] == "TestSolution"
    assert result["display_name"] == "Test Solution Display"
    assert result["description"] == "A test solution"
    assert result["version"] == "1.0.0.0"
    assert result["publisher_name"] == "Test Publisher Name"
    assert result["publisher_unique_name"] == "TestPublisher"
    assert result["publisher_prefix"] == "ts"
    assert result["component_count"] == 2
    assert result["is_managed"] == "0"
    assert "Entity" in result["component_types"]
    assert "Role" in result["component_types"]


def test_parse_solution_missing():
    zf = _make_zip({"other.xml": b"<root/>"})
    result = parse_solution(zf, zf.namelist())
    assert result == {}


# ---------------------------------------------------------------------------
# Customizations Parser
# ---------------------------------------------------------------------------

def test_parse_customizations_entities():
    zf = _make_zip({"customizations.xml": CUSTOMIZATIONS_XML})
    result = parse_customizations(zf, zf.namelist())

    assert len(result["entities"]) == 1
    entity = result["entities"][0]
    assert entity["name"] == "ts_testentity"
    assert entity["display_name"] == "Test Entity"
    assert entity["collection_name"] == "Test Entities"

    # Attributes — PhysicalName is an XML attribute on <attribute>
    assert len(entity["attributes"]) == 2
    attr = entity["attributes"][0]
    assert attr["name"] == "ts_name"
    assert attr["type"] == "nvarchar"
    assert attr["required"] == "required"
    assert attr["display_name"] == "Name"

    # Forms
    assert len(entity["forms"]) == 1
    assert entity["forms"][0]["name"] == "Main Form"
    assert entity["forms"][0]["active"] is True

    # Views
    assert len(entity["views"]) == 1
    assert entity["views"][0]["name"] == "Active Test Entities"
    assert entity["views"][0]["type"] == "Public View"


def test_parse_customizations_roles():
    zf = _make_zip({"customizations.xml": CUSTOMIZATIONS_XML})
    result = parse_customizations(zf, zf.namelist())
    assert len(result["roles"]) == 1
    assert result["roles"][0]["name"] == "TS-ReadOnly"


def test_parse_customizations_connection_refs():
    zf = _make_zip({"customizations.xml": CUSTOMIZATIONS_XML})
    result = parse_customizations(zf, zf.namelist())
    assert len(result["connection_references"]) == 1
    assert result["connection_references"][0]["logical_name"] == "ts_shared_cds"


def test_parse_customizations_app_modules():
    zf = _make_zip({"customizations.xml": CUSTOMIZATIONS_XML})
    result = parse_customizations(zf, zf.namelist())
    assert len(result["app_modules"]) == 1
    assert result["app_modules"][0]["unique_name"] == "ts_testapp"
    assert result["app_modules"][0]["display_name"] == "Test App"


def test_parse_customizations_workflows_meta():
    zf = _make_zip({"customizations.xml": CUSTOMIZATIONS_XML})
    result = parse_customizations(zf, zf.namelist())
    assert len(result["workflows_meta"]) == 1
    wf = result["workflows_meta"][0]
    assert wf["name"] == "My Cloud Flow"
    assert wf["category"] == "Cloud Flow (Power Automate)"


def test_parse_customizations_web_resources_meta():
    zf = _make_zip({"customizations.xml": CUSTOMIZATIONS_XML})
    result = parse_customizations(zf, zf.namelist())
    assert len(result["web_resources"]) == 1
    wr = result["web_resources"][0]
    assert wr["name"] == "ts_myscript.js"
    assert wr["type"] == "JavaScript"


# ---------------------------------------------------------------------------
# Workflow Parser
# ---------------------------------------------------------------------------

def test_parse_workflows_from_meta():
    flow_json = b'{"properties": {"definition": {"triggers": {"MyTrigger": {}}, "actions": {"Step1": {}}}, "connectionReferences": {"shared_cds": {}}}}'
    zf = _make_zip({
        "customizations.xml": CUSTOMIZATIONS_XML,
        "Workflows/MyCloudFlow-WF-001.json": flow_json,
    })
    cust = parse_customizations(zf, zf.namelist())
    wfs = parse_workflows(zf, zf.namelist(), workflows_meta=cust["workflows_meta"])
    assert len(wfs) == 1
    assert wfs[0]["name"] == "My Cloud Flow"
    assert wfs[0]["category"] == "Cloud Flow (Power Automate)"


def test_parse_workflows_empty():
    zf = _make_zip({"solution.xml": SOLUTION_XML})
    result = parse_workflows(zf, zf.namelist())
    assert result == []


# ---------------------------------------------------------------------------
# Web Resources Parser
# ---------------------------------------------------------------------------

def test_parse_webresources_from_meta():
    zf = _make_zip({
        "customizations.xml": CUSTOMIZATIONS_XML,
        "WebResources/ts_myscriptjsWF001": b"console.log('hello');",
    })
    cust = parse_customizations(zf, zf.namelist())
    wrs = parse_webresources(zf, zf.namelist(), web_resources_meta=cust["web_resources"])
    assert len(wrs) == 1
    assert wrs[0]["name"] == "ts_myscript.js"
    assert wrs[0]["type"] == "JavaScript"


def test_parse_webresources_fallback():
    """When no metadata provided, fall back to scanning WebResources/ folder."""
    zf = _make_zip({
        "WebResources/ts_script.js": b"console.log('hello');",
        "WebResources/ts_style.css": b"body { margin: 0; }",
    })
    result = parse_webresources(zf, zf.namelist())
    assert len(result) == 2
    types = {r["name"]: r["type"] for r in result}
    assert types["ts_script.js"] == "JavaScript"
    assert types["ts_style.css"] == "CSS"


# ---------------------------------------------------------------------------
# Environment Variables Parser
# ---------------------------------------------------------------------------

def test_parse_env_vars_basic():
    zf = _make_zip({
        "environmentvariabledefinitions/ts_myenvvar/environmentvariabledefinition.xml": ENV_VAR_XML,
    })
    result = parse_env_vars(zf, zf.namelist())
    assert len(result) == 1
    ev = result[0]
    assert ev["schema_name"] == "ts_myenvvar"
    assert ev["display_name"] == "My Env Var"
    assert ev["description"] == "A test environment variable"
    assert ev["type"] == "String"
    assert ev["is_required"] is True
    assert ev["is_secret"] is False
    assert ev["introduced_version"] == "1.0.0.0"


def test_parse_env_vars_empty():
    zf = _make_zip({"solution.xml": SOLUTION_XML})
    result = parse_env_vars(zf, zf.namelist())
    assert result == []
