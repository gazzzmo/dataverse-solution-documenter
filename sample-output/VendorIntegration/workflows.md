# Workflows

**Total workflows:** 3

## Cloud Flow (Power Automate)

### On Create/Update of Contacts where Setup Technician is True -> Call...

| Field | Value |
|---|---|
| Category | Cloud Flow (Power Automate) |
| Primary Entity | none |
| State | Active |
| Introduced Version | 1.0.0.0 |

**Triggers:** `On_Create_or_Update_of_Contacts_where_Setup_Technician_is_True`  
**Actions:** `Call_Azure_Function_to_Invite_User`, `Call_Azure_Function_to_Assign_License_to_User`, `Allow_Time_for_Entra_to_Create_the_User_Record_Asynchronously_(1_Minute)`, `Call_Azure_Function_to_Add_User_to_Security_Group_for_Dataverse_Permissions`  
**Connection References:** `shared_commondataserviceforapps`  
**Source File:** `Workflows/OnCreateUpdateofContactswhereSetupTechnicianisTrue-6F35B8C3-34A2-EF11-8A69-000D3A59D659.json`  

### On Reactivate of Contacts where Setup Technician is True -> Call...

| Field | Value |
|---|---|
| Category | Cloud Flow (Power Automate) |
| Primary Entity | none |
| State | Active |
| Introduced Version | 1.0.0.0 |

**Triggers:** `On_Reactivation_of_Contacts_where_Setup_Technician_is_True`  
**Actions:** `Call_Azure_Function_to_Assign_License_to_User`  
**Connection References:** `shared_commondataserviceforapps`  
**Source File:** `Workflows/OnReactivateofContactswhereSetupTechnicianisTrue-C-242A38E3-DAB0-EF11-B8E8-000D3A59D659.json`  

### On Deactivate of Contacts where Setup Technician is True -> Unlicense User via Azure Function

| Field | Value |
|---|---|
| Category | Cloud Flow (Power Automate) |
| Primary Entity | none |
| State | Active |
| Introduced Version | 1.0.0.0 |

**Triggers:** `On_Deactivate_of_Contact`  
**Actions:** `Call_RemoveUserLicense_Azure_Function`  
**Connection References:** `shared_commondataserviceforapps`  
**Source File:** `Workflows/OnDeactivateofContactswhereSetupTechnicianisTrue-U-CFBCB0F9-80AB-EF11-B8E9-000D3A5CC0A9.json`  

---
