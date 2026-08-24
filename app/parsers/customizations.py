"""
Parser: customizations.xml

Extracts entities, attributes, forms, views, roles, entity relationships,
connection references, app modules, and option sets.

Real-world structure (from a real Dataverse solution):
  <ImportExportXml>
    <Entities>
      <Entity Name="ebp_Branch">
        <EntityInfo>
          <entity>
            <LocalizedNames><LocalizedName description="Branch" .../></LocalizedNames>
            <attributes>
              <attribute>
                <PhysicalName>ebp_Name</PhysicalName>
                <Type>nvarchar</Type>
                <RequiredLevel>required</RequiredLevel>
                <displaynames><displayname description="Name" .../></displaynames>
              </attribute>
            </attributes>
          </entity>
        </EntityInfo>
        <FormXml>
          <forms><systemform>
            <formid>...</formid>
            <LocalizedNames><LocalizedName description="Information" .../></LocalizedNames>
          </systemform></forms>
        </FormXml>
        <SavedQueries>
          <savedqueries>
            <savedquery>
              <querytype>0</querytype>
              <LocalizedNames><LocalizedName description="Active Branches" .../></LocalizedNames>
            </savedquery>
          </savedqueries>
        </SavedQueries>
      </Entity>
    </Entities>
    <Roles>
      <Role name="bcc_MarketingManager" .../>
    </Roles>
    <EntityRelationships>
      <EntityRelationship Name="bcc_contact_branch_ebp_branch" RelationshipType="..."/>
    </EntityRelationships>
    <connectionreferences>
      <connectionreference connectionreferencelogicalname="..." connectorid="..." />
    </connectionreferences>
    <AppModules>
      <AppModule><UniqueName>bcc_myapp</UniqueName></AppModule>
    </AppModules>
  </ImportExportXml>

Workflow metadata is in <Workflows/Workflow> but parsed by workflows.py.
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any

# Dataverse query type codes → human labels
QUERY_TYPES = {
    "0": "Public View",
    "1": "Advanced Find",
    "2": "Associated View",
    "4": "Quick Find",
    "8": "Reporting",
    "16": "Offline",
    "32": "Lookup View",
    "64": "Lookup View",
    "128": "Email Templates",
    "256": "Mail Merge",
    "512": "Adv. Find (Quick)",
    "1024": "Reporting",
    "2048": "Offline",
}


def _localized_name(el: ET.Element | None, lang: str = "1033") -> str:
    """Get the @description from a LocalizedName with preference for given languagecode."""
    if el is None:
        return ""
    best = ""
    for ln in el.findall(".//LocalizedName"):
        best = ln.get("description", "")
        if ln.get("languagecode") == lang:
            return best
    return best


def _attr_default(el: ET.Element | None, child_tag: str) -> str:
    """Get @default attribute from a child element."""
    if el is None:
        return ""
    child = el.find(child_tag)
    return (child.get("default") or "").strip() if child is not None else ""


def parse_customizations(zf: zipfile.ZipFile, namelist: list[str]) -> dict[str, Any]:
    """Parse customizations.xml and return structured metadata."""
    result: dict[str, Any] = {
        "entities": [],
        "roles": [],
        "entity_relationships": [],
        "connection_references": [],
        "app_modules": [],
        "global_option_sets": [],
        "web_resources": [],
        "workflows_meta": [],  # workflow metadata cross-ref for workflows parser
    }

    cust_file = next((n for n in namelist if n.lower() == "customizations.xml"), None)
    if not cust_file:
        return result

    root = ET.fromstring(zf.read(cust_file))

    # ---- Entities -----------------------------------------------------------
    for entity in root.findall("Entities/Entity"):
        name = entity.get("Name") or entity.findtext("Name") or ""

        entity_info_el = entity.find("EntityInfo/entity")
        display_name = _localized_name(
            entity_info_el.find("LocalizedNames") if entity_info_el is not None else None
        ) or name
        collection_name = _localized_name(
            entity_info_el.find("LocalizedCollectionNames") if entity_info_el is not None else None
        )
        description = _localized_name(
            entity_info_el.find("Descriptions") if entity_info_el is not None else None
        ) if entity_info_el is not None else ""

        entity_data: dict[str, Any] = {
            "name": name,
            "display_name": display_name,
            "collection_name": collection_name,
            "description": description,
            "attributes": [],
            "forms": [],
            "views": [],
        }

        # Attributes
        attrs_el = entity_info_el.find("attributes") if entity_info_el is not None else None
        if attrs_el is not None:
            for attr in attrs_el.findall("attribute"):
                # PhysicalName is an XML attribute on the <attribute> element
                # but may also appear as a child text element
                phys_name = (
                    attr.get("PhysicalName")
                    or attr.findtext("PhysicalName")
                    or attr.findtext("Name")
                    or attr.findtext("LogicalName")
                    or ""
                ).strip()
                attr_type = (attr.findtext("Type") or "").strip()
                required = (attr.findtext("RequiredLevel") or "").strip()

                # Display name: <displaynames><displayname description="..."/>
                display_el = attr.find(".//displaynames/displayname")
                if display_el is not None:
                    attr_display = display_el.get("description") or ""
                else:
                    ln_el = attr.find(".//LocalizedNames/LocalizedName")
                    attr_display = (ln_el.get("description") or "") if ln_el is not None else ""

                # Option set values (picklist, state, status, boolean)
                options = []
                for opt in attr.findall(".//optionset/Options/Option"):
                    val = opt.get("Value", "")
                    lbl_el = opt.find(".//LocalizedLabels/LocalizedLabel")
                    lbl = (lbl_el.get("description") or "") if lbl_el is not None else ""
                    if val or lbl:
                        options.append({"value": val, "label": lbl})

                attr_data: dict[str, Any] = {
                    "name": phys_name,
                    "display_name": attr_display,
                    "type": attr_type,
                    "required": required,
                }
                if options:
                    attr_data["options"] = options

                entity_data["attributes"].append(attr_data)

        # Forms — FormXml contains multiple <forms> elements, each with a <systemform>
        form_xml_el = entity.find("FormXml")
        if form_xml_el is not None:
            for forms_container in form_xml_el.findall("forms"):
                for sf in forms_container.findall("systemform"):
                    form_id = (sf.findtext("formid") or "").strip()
                    form_version = (sf.findtext("IntroducedVersion") or "").strip()
                    form_state = (sf.findtext("FormActivationState") or "1").strip()
                    form_name = _localized_name(sf.find("LocalizedNames"))
                    entity_data["forms"].append({
                        "name": form_name or "Unnamed Form",
                        "id": form_id,
                        "version": form_version,
                        "active": form_state == "1",
                    })

        # Views — SavedQueries/savedqueries/savedquery
        sq_el = entity.find("SavedQueries")
        if sq_el is not None:
            savedqueries_inner = sq_el.find("savedqueries")
            if savedqueries_inner is not None:
                for sq in savedqueries_inner.findall("savedquery"):
                    q_type_raw = (sq.findtext("querytype") or "0").strip()
                    q_type_label = QUERY_TYPES.get(q_type_raw, f"Type {q_type_raw}")
                    view_name = _localized_name(sq.find("LocalizedNames"))
                    entity_data["views"].append({
                        "name": view_name or "Unnamed View",
                        "type": q_type_label,
                        "type_code": q_type_raw,
                    })

        result["entities"].append(entity_data)

    # ---- Roles --------------------------------------------------------------
    # Standard CRUD+misc actions — order matters (AppendTo before Append)
    _PRIV_ACTIONS = [
        "AppendTo", "Append", "Create", "Delete",
        "Read", "Write", "Assign", "Share",
    ]

    def _parse_priv(name: str) -> tuple[str | None, str]:
        """Split a privilege name into (action, entity). Returns (None, name) for misc."""
        raw = name[3:] if name.startswith("prv") else name
        for action in _PRIV_ACTIONS:
            if raw.startswith(action):
                return action, raw[len(action):]
        return None, raw

    for role in root.findall("Roles/Role"):
        # Entity privileges: {entity_name: {action: level}}
        entity_privs: dict[str, dict[str, str]] = {}
        # Misc privileges (non-entity): {raw_name: level}
        misc_privs: dict[str, str] = {}

        for rp in role.findall("RolePrivileges/RolePrivilege"):
            priv_name = rp.get("name", "")
            level = rp.get("level", "")
            action, entity = _parse_priv(priv_name)
            if action and entity:
                entity_privs.setdefault(entity, {})[action] = level
            else:
                misc_privs[entity] = level  # entity holds the raw remainder

        result["roles"].append({
            "name": role.get("name") or role.get("Name") or "",
            "id": role.get("id") or "",
            "entity_privileges": entity_privs,
            "misc_privileges": misc_privs,
        })

    # ---- Entity Relationships (top-level, cross-entity) --------------------
    for rel in root.findall("EntityRelationships/EntityRelationship"):
        rel_type_raw = rel.get("RelationshipType") or ""
        result["entity_relationships"].append({
            "name": rel.get("Name") or "",
            "type": rel_type_raw,
            "entity1": rel.get("Entity1LogicalName") or "",
            "entity2": rel.get("Entity2LogicalName") or "",
            "entity1_nav": rel.get("Entity1NavigationPropertyName") or "",
            "entity2_nav": rel.get("Entity2NavigationPropertyName") or "",
        })

    # ---- Connection References ---------------------------------------------
    for cr in root.findall("connectionreferences/connectionreference"):
        result["connection_references"].append({
            "logical_name": cr.get("connectionreferencelogicalname") or "",
            "connector_id": cr.get("connectorid") or "",
            "display_name": _localized_name(cr.find("LocalizedNames")) or cr.get("connectionreferencelogicalname") or "",
        })

    # ---- App Modules -------------------------------------------------------
    for app in root.findall("AppModules/AppModule"):
        app_name = _localized_name(app.find("LocalizedNames"))
        result["app_modules"].append({
            "unique_name": (app.findtext("UniqueName") or "").strip(),
            "display_name": app_name or (app.findtext("UniqueName") or "").strip(),
            "description": _localized_name(app.find("Descriptions")),
        })

    # ---- Global Option Sets ------------------------------------------------
    for opt_set in root.findall("optionsets/optionset"):
        os_name = opt_set.get("Name") or opt_set.get("name") or ""
        os_display = _localized_name(opt_set.find("LocalizedNames"))
        options = []
        for opt in opt_set.findall(".//Options/Option"):
            val = opt.get("Value", "")
            lbl_el = opt.find(".//LocalizedLabels/LocalizedLabel")
            lbl = (lbl_el.get("description") or "") if lbl_el is not None else ""
            options.append({"value": val, "label": lbl})
        result["global_option_sets"].append({
            "name": os_name,
            "display_name": os_display or os_name,
            "options": options,
        })

    # ---- Web Resources (metadata from customizations.xml) ------------------
    WR_TYPES = {
        "1": "HTML", "2": "CSS", "3": "JavaScript", "4": "XML",
        "5": "PNG Image", "6": "JPEG Image", "7": "GIF Image",
        "8": "XAP (Silverlight)", "9": "XSL Stylesheet", "10": "Icon",
        "11": "SVG Image", "12": "String Resource (RESX)",
    }
    for wr in root.findall("WebResources/WebResource"):
        wr_type_code = (wr.findtext("WebResourceType") or "").strip()
        result["web_resources"].append({
            "name": (wr.findtext("Name") or "").strip(),
            "display_name": (wr.findtext("DisplayName") or "").strip(),
            "type": WR_TYPES.get(wr_type_code, f"Type {wr_type_code}"),
            "type_code": wr_type_code,
            "file": (wr.findtext("FileName") or "").strip(),
            "introduced_version": (wr.findtext("IntroducedVersion") or "").strip(),
        })

    # ---- Workflow metadata (for workflows.py cross-reference) --------------
    for wf_el in root.findall("Workflows/Workflow"):
        CATEGORY_LABELS = {
            "0": "Classic Workflow", "1": "Dialog",
            "2": "Business Rule", "3": "Action",
            "4": "Business Process Flow", "5": "Cloud Flow (Power Automate)",
        }
        cat = (wf_el.findtext("Category") or "").strip()
        result["workflows_meta"].append({
            "id": (wf_el.get("WorkflowId") or "").strip("{}").lower(),
            "name": wf_el.get("Name") or "",
            "description": wf_el.get("Description") or "",
            "category": CATEGORY_LABELS.get(cat, f"Category {cat}"),
            "category_code": cat,
            "primary_entity": (wf_el.findtext("PrimaryEntity") or "").strip(),
            "state": (wf_el.findtext("StateCode") or "").strip(),
            "on_demand": (wf_el.findtext("OnDemand") or "0").strip() == "1",
            "trigger_on_create": (wf_el.findtext("TriggerOnCreate") or "0").strip() == "1",
            "trigger_on_delete": (wf_el.findtext("TriggerOnDelete") or "0").strip() == "1",
            "json_file": (wf_el.findtext("JsonFileName") or "").strip("/"),
            "xaml_file": (wf_el.findtext("XamlFileName") or "").strip("/"),
            "introduced_version": (wf_el.findtext("IntroducedVersion") or "").strip(),
        })

    return result
