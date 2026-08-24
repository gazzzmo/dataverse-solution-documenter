"""
Parser: Plugin Assemblies & SDK Message Processing Steps

Data lives entirely in customizations.xml — NOT in separate XML files.

Real-world structure:

  <SolutionPluginAssemblies>
    <PluginAssembly
        FullName="FieldService.Optimize25.SetupVendorUser, Version=1.0.0.0, ..."
        PluginAssemblyId="2468dab7-..."
        CustomizationLevel="1">
      <IsolationMode>2</IsolationMode>   <!-- 1=None, 2=Sandbox -->
      <SourceType>0</SourceType>
      <IntroducedVersion>1.0</IntroducedVersion>
      <FileName>/PluginAssemblies/...</FileName>
      <PluginTypes>
        <PluginType
            AssemblyQualifiedName="..."
            PluginTypeId="..."
            Name="FieldService.Optimize25.SetupVendorUser.SetupVendorUser">
          <FriendlyName>3a280edd-...</FriendlyName>
        </PluginType>
      </PluginTypes>
    </PluginAssembly>
  </SolutionPluginAssemblies>

  <SdkMessageProcessingSteps>
    <SdkMessageProcessingStep
        Name="FieldService.Optimize25.SetupVendorUser.SetupVendorUser: Create of systemuser"
        SdkMessageProcessingStepId="{bc8d80e0-...}">
      <PrimaryEntity>systemuser</PrimaryEntity>
      <Stage>40</Stage>       <!-- 10=PreValidation, 20=PreOp, 40=PostOp -->
      <Mode>1</Mode>          <!-- 0=Sync, 1=Async -->
      <Rank>1</Rank>
      <PluginTypeName>FieldService.Optimize25.SetupVendorUser.SetupVendorUser, ...</PluginTypeName>
      <Description>...</Description>
      <FilteringAttributes></FilteringAttributes>
      <SupportedDeployment>0</SupportedDeployment>
    </SdkMessageProcessingStep>
  </SdkMessageProcessingSteps>
"""
import zipfile
import xml.etree.ElementTree as ET
from typing import Any

ISOLATION_MODES = {"1": "None", "2": "Sandbox", "3": "External Isolation"}
STAGES = {
    "10": "PreValidation",
    "20": "PreOperation",
    "40": "PostOperation",
    "45": "PostOperation (Deprecated)",
}
MODES = {"0": "Synchronous", "1": "Asynchronous"}
DEPLOYMENTS = {"0": "Server Only", "1": "Offline Only", "2": "Both"}


def parse_plugins(
    zf: zipfile.ZipFile,
    namelist: list[str],
    plugins_meta: list[dict[str, Any]] | None = None,
    steps_meta: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """
    Return plugin assembly and step registration data.

    plugins_meta / steps_meta: pre-parsed from customizations.py (avoids re-parsing).
    Falls back to scanning customizations.xml directly if not supplied.
    """
    if plugins_meta is not None and steps_meta is not None:
        assemblies = plugins_meta
        steps = steps_meta
    else:
        # Parse directly from customizations.xml
        cust_file = next((n for n in namelist if n.lower() == "customizations.xml"), None)
        if not cust_file:
            return {"assemblies": [], "steps": []}
        root = ET.fromstring(zf.read(cust_file))
        assemblies = _parse_assemblies(root)
        steps = _parse_steps(root)

    # Cross-reference steps onto their assemblies by plugin type name
    type_to_assembly: dict[str, str] = {}
    for asm in assemblies:
        for pt in asm.get("plugin_types", []):
            type_to_assembly[pt["name"]] = asm["name"]

    for step in steps:
        plugin_type = step.get("plugin_type_name", "")
        # Match on the class portion before the first comma
        class_name = plugin_type.split(",")[0].strip()
        step["assembly_name"] = type_to_assembly.get(class_name, "")

    return {"assemblies": assemblies, "steps": steps}


def _parse_assemblies(root: ET.Element) -> list[dict[str, Any]]:
    assemblies = []
    for asm in root.findall("SolutionPluginAssemblies/PluginAssembly"):
        full_name = asm.get("FullName", "")
        # Parse assembly name from FullName (everything before first comma)
        asm_name = full_name.split(",")[0].strip() if full_name else ""

        # Parse version from FullName "Name, Version=x.x.x.x, ..."
        version = ""
        for part in full_name.split(","):
            part = part.strip()
            if part.startswith("Version="):
                version = part[len("Version="):]
                break

        iso_code = (asm.findtext("IsolationMode") or "").strip()
        file_path = (asm.findtext("FileName") or "").strip().lstrip("/")

        plugin_types = []
        for pt in asm.findall("PluginTypes/PluginType"):
            pt_name = pt.get("Name") or pt.get("AssemblyQualifiedName", "").split(",")[0].strip()
            plugin_types.append({
                "name": pt.get("AssemblyQualifiedName", "").split(",")[0].strip(),
                "display_name": pt_name,
                "id": pt.get("PluginTypeId", ""),
            })

        assemblies.append({
            "name": asm_name,
            "full_name": full_name,
            "version": version,
            "id": asm.get("PluginAssemblyId", ""),
            "isolation_mode": ISOLATION_MODES.get(iso_code, iso_code),
            "introduced_version": (asm.findtext("IntroducedVersion") or "").strip(),
            "file": file_path,
            "plugin_types": plugin_types,
        })
    return assemblies


def _parse_steps(root: ET.Element) -> list[dict[str, Any]]:
    steps = []
    for step in root.findall("SdkMessageProcessingSteps/SdkMessageProcessingStep"):
        stage_code = (step.findtext("Stage") or "").strip()
        mode_code = (step.findtext("Mode") or "").strip()
        deploy_code = (step.findtext("SupportedDeployment") or "").strip()
        filtering = (step.findtext("FilteringAttributes") or "").strip()

        steps.append({
            "name": step.get("Name", ""),
            "id": step.get("SdkMessageProcessingStepId", "").strip("{}"),
            "plugin_type_name": (step.findtext("PluginTypeName") or "").strip(),
            "primary_entity": (step.findtext("PrimaryEntity") or "").strip(),
            "stage": STAGES.get(stage_code, stage_code),
            "mode": MODES.get(mode_code, mode_code),
            "rank": (step.findtext("Rank") or "").strip(),
            "description": (step.findtext("Description") or "").strip(),
            "filtering_attributes": filtering,
            "deployment": DEPLOYMENTS.get(deploy_code, deploy_code),
            "introduced_version": (step.findtext("IntroducedVersion") or "").strip(),
            "assembly_name": "",  # filled in by parse_plugins
        })
    return steps
