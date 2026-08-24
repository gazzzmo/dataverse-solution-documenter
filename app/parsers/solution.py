"""
Parser: solution.xml

Extracts top-level solution metadata — name, version, publisher, description.

Real-world structure (from a real Dataverse solution):
  <SolutionManifest>
    <UniqueName>MySolution</UniqueName>
    <LocalizedNames>
      <LocalizedName description="My Solution" languagecode="1033" />
    </LocalizedNames>
    <Descriptions>
      <Description description="Example solution description" languagecode="1033" />
    </Descriptions>
    <Version>1.0.0.0</Version>
    <Managed>0</Managed>
    <Publisher>
      <UniqueName>bccdefaultpublisher</UniqueName>
      <LocalizedNames>
        <LocalizedName description="BCC Default Publisher" languagecode="1033" />
      </LocalizedNames>
      <CustomizationPrefix>bcc</CustomizationPrefix>
    </Publisher>
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def _attr_desc(el, path: str, fallback: str = "") -> str:
    """Find element at path and return its 'description' attribute."""
    found = el.find(path) if el is not None else None
    return (found.get("description") or fallback).strip() if found is not None else fallback


def parse_solution(zf: zipfile.ZipFile, namelist: list[str]) -> dict[str, Any]:
    """Parse solution.xml and return a flat dict of solution metadata."""
    result: dict[str, Any] = {}

    solution_file = next((n for n in namelist if n.lower() == "solution.xml"), None)
    if not solution_file:
        return result

    root = ET.fromstring(zf.read(solution_file))
    manifest = root.find("SolutionManifest") or root

    result["unique_name"] = (manifest.findtext("UniqueName") or "").strip()

    # Display name comes from LocalizedName @description attribute (language 1033 preferred)
    display_name = ""
    for ln in manifest.findall(".//LocalizedNames/LocalizedName"):
        display_name = ln.get("description", "")
        if ln.get("languagecode") == "1033":
            break
    result["display_name"] = display_name or result["unique_name"]

    # Description — same pattern
    description = ""
    for d in manifest.findall(".//Descriptions/Description"):
        description = d.get("description", "")
        if d.get("languagecode") == "1033":
            break
    result["description"] = description

    result["version"] = (manifest.findtext("Version") or "").strip()

    managed_el = manifest.find("Managed")
    result["is_managed"] = (managed_el.text or "0").strip() if managed_el is not None else "0"

    # Publisher
    pub = manifest.find("Publisher")
    if pub is not None:
        result["publisher_unique_name"] = (pub.findtext("UniqueName") or "").strip()
        # Publisher display name is also in LocalizedName @description
        pub_display = ""
        for ln in pub.findall(".//LocalizedNames/LocalizedName"):
            pub_display = ln.get("description", "")
            if ln.get("languagecode") == "1033":
                break
        result["publisher_name"] = pub_display or result["publisher_unique_name"]
        result["publisher_prefix"] = (pub.findtext("CustomizationPrefix") or "").strip()
        result["publisher_option_prefix"] = (pub.findtext("CustomizationOptionValuePrefix") or "").strip()

        # Publisher description
        pub_desc = ""
        for d in pub.findall(".//Descriptions/Description"):
            pub_desc = d.get("description", "")
            if d.get("languagecode") == "1033":
                break
        result["publisher_description"] = pub_desc
    else:
        result["publisher_unique_name"] = ""
        result["publisher_name"] = ""
        result["publisher_prefix"] = ""
        result["publisher_option_prefix"] = ""
        result["publisher_description"] = ""

    # Root component type counts
    comps = root.findall(".//RootComponents/RootComponent")
    result["component_count"] = len(comps)

    # Component type breakdown (Dataverse type codes)
    COMPONENT_TYPES = {
        "1": "Entity", "2": "Attribute", "3": "Relationship",
        "4": "AttributePicklistValue", "5": "AttributeLookupValue",
        "6": "ViewAttribute", "7": "LocalizedLabel", "8": "RelationshipExtraCondition",
        "9": "OptionSet", "10": "EntityRelationship", "11": "EntityRelationshipRole",
        "12": "EntityRelationshipRelationships", "13": "ManagedProperty",
        "14": "EntityKey", "20": "Role", "21": "RolePrivilege",
        "22": "DisplayString", "23": "DisplayStringMap", "24": "Form",
        "25": "Organization", "26": "SavedQuery", "27": "Workflow",
        "28": "Report", "29": "ReportEntity", "30": "ReportCategory",
        "31": "ReportVisibility", "32": "Attachment", "33": "EmailTemplate",
        "34": "ContractTemplate", "35": "KBArticleTemplate",
        "36": "MailMergeTemplate", "37": "DuplicateRule",
        "38": "DuplicateRuleCondition", "39": "EntityMap", "40": "AttributeMap",
        "41": "RibbonCommand", "42": "RibbonContextGroup",
        "43": "RibbonCustomization", "44": "RibbonRule", "45": "RibbonTabToCommandMap",
        "46": "RibbonDiff", "47": "RibbonMetadataToProcess",
        "48": "SiteMap", "49": "WebResource", "50": "SystemForm",
        "51": "AppModule", "52": "AppModuleRoles", "53": "AppModuleRoleLite",
        "55": "Role", "59": "ChannelProperty", "60": "ChannelPropertyGroup",
        "61": "EnvironmentVariableDefinition", "62": "EnvironmentVariableValue",
        "65": "MobileOfflineProfile", "66": "MobileOfflineProfileItem",
        "70": "SimilarityRule", "71": "DataSourceMapping",
        "80": "ConnectionReference", "81": "AIModel",
        "90": "CanvasApp", "92": "Connector", "95": "AIConfiguration",
    }
    type_breakdown = {}
    for c in comps:
        t = c.get("type", "unknown")
        label = COMPONENT_TYPES.get(t, f"Type{t}")
        type_breakdown[label] = type_breakdown.get(label, 0) + 1
    result["component_types"] = type_breakdown

    return result
