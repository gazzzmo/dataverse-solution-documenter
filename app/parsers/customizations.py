"""
Parser: customizations.xml

Extracts entities (tables), attributes (columns), forms, views, relationships,
option sets, and other metadata from customizations.xml.
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any


def _text(el, tag: str) -> str:
    child = el.find(tag)
    return (child.text or "").strip() if child is not None else ""


def parse_customizations(zf: zipfile.ZipFile, namelist: list[str]) -> dict[str, Any]:
    """Parse customizations.xml and return structured metadata."""
    result: dict[str, Any] = {
        "entities": [],
        "global_option_sets": [],
    }

    cust_file = next(
        (n for n in namelist if n.lower() == "customizations.xml"), None
    )
    if not cust_file:
        return result

    xml_bytes = zf.read(cust_file)
    root = ET.fromstring(xml_bytes)

    # ---- Entities / Tables ----
    for entity in root.findall(".//Entity") + root.findall(".//entity"):
        name = entity.get("Name") or entity.get("name") or _text(entity, "Name")
        display_name_el = entity.find(".//displayname") or entity.find(".//DisplayName")
        display_name = (display_name_el.get("description") or "") if display_name_el is not None else name

        entity_data: dict[str, Any] = {
            "name": name,
            "display_name": display_name,
            "attributes": [],
            "forms": [],
            "views": [],
            "relationships": [],
        }

        # Attributes / columns
        for attr in entity.findall(".//attribute") + entity.findall(".//Attribute"):
            attr_name = attr.get("PhysicalName") or attr.get("physicalname") or _text(attr, "Name")
            attr_type = attr.get("Type") or attr.get("type") or _text(attr, "Type")
            attr_display = ""
            dn_el = attr.find(".//displayname") or attr.find(".//DisplayName")
            if dn_el is not None:
                attr_display = dn_el.get("description") or ""
            entity_data["attributes"].append({
                "name": attr_name,
                "type": attr_type,
                "display_name": attr_display,
            })

        # Forms
        for form in entity.findall(".//systemform") + entity.findall(".//SystemForm"):
            form_name = _text(form, "name") or _text(form, "Name")
            form_type = _text(form, "type") or _text(form, "Type")
            entity_data["forms"].append({"name": form_name, "type": form_type})

        # Views (saved queries)
        for view in entity.findall(".//savedquery") + entity.findall(".//SavedQuery"):
            view_name = _text(view, "name") or _text(view, "Name")
            entity_data["views"].append({"name": view_name})

        # Relationships
        for rel in entity.findall(".//EntityRelationship") + entity.findall(".//entityrelationship"):
            rel_name = rel.get("Name") or rel.get("name") or ""
            rel_type = rel.get("RelationshipType") or rel.get("relationshiptype") or ""
            entity_data["relationships"].append({"name": rel_name, "type": rel_type})

        result["entities"].append(entity_data)

    # ---- Global Option Sets ----
    for opt_set in root.findall(".//OptionSet") + root.findall(".//optionset"):
        os_name = opt_set.get("Name") or opt_set.get("name") or ""
        options = []
        for opt in opt_set.findall(".//Option") + opt_set.findall(".//option"):
            val = opt.get("Value") or opt.get("value") or ""
            label_el = opt.find(".//label") or opt.find(".//Label")
            label = (label_el.get("description") or "") if label_el is not None else ""
            options.append({"value": val, "label": label})
        result["global_option_sets"].append({"name": os_name, "options": options})

    return result
