# Entities & Tables

**Total entities:** 7

## Summary

| Display Name | Schema Name | Attributes | Forms | Views |
|---|---|---|---|---|
| [BookableResource](#bookableresource) | `BookableResource` | 0 | 1 | 0 |
| [Characteristic](#characteristic) | `Characteristic` | 0 | 0 | 0 |
| [Contact](#contact) | `Contact` | 11 | 1 | 0 |
| [Organizational Unit](#organizational-unit) | `msdyn_organizationalunit` | 0 | 0 | 0 |
| [msdyn_warehouse](#msdyn-warehouse) | `msdyn_warehouse` | 0 | 0 | 0 |
| [Technician Characteristic](#technician-characteristic) | `o25fs_VendorCharacteristic` | 21 | 4 | 8 |
| [RatingValue](#ratingvalue) | `RatingValue` | 0 | 0 | 0 |

---

## BookableResource

| Field | Value |
|---|---|
| Schema Name | `BookableResource` |
| Display Name | BookableResource |
| Collection Name |  |
| Description |  |

### Forms

| Name | ID | Version | Active |
|---|---|---|---|
| Work Hours Form | `{be117c6f-55ab-ef11-b8e8-000d3a59d659}` | 1.0.0.0 | ✅ |

---

## Characteristic

| Field | Value |
|---|---|
| Schema Name | `Characteristic` |
| Display Name | Characteristic |
| Collection Name |  |
| Description |  |

---

## Contact

| Field | Value |
|---|---|
| Schema Name | `Contact` |
| Display Name | Contact |
| Collection Name |  |
| Description |  |

### Attributes

| Schema Name | Display Name | Type | Required | Options |
|---|---|---|---|---|
| `o25fs_BookableResourceId` | Bookable Resource | lookup | none |  |
| `o25fs_DisplayOnScheduleBoard` | Display On Schedule Board | bit | none |  |
| `o25fs_EnableforAvailabilitySearch` | Enable for Availability Search | bit | none |  |
| `o25fs_EndLocation` | End Location | picklist | none |  |
| `o25fs_HourlyRate` | Hourly Rate | money | none |  |
| `o25fs_hourlyrate_Base` | Hourly Rate (Base) | money | none |  |
| `o25fs_OrganizationalUnitId` | Organizational Unit | lookup | none |  |
| `o25fs_SetupTechnician` | Setup Technician | bit | none |  |
| `o25fs_StartLocation` | Start Location | picklist | none |  |
| `o25fs_TimeOffApprovalRequired` | Time Off Approval Required | bit | none |  |
| `o25fs_WarehouseId` | Warehouse | lookup | none |  |

### Forms

| Name | ID | Version | Active |
|---|---|---|---|
| Vendor Admin Form | `{60fdd8d9-21a2-ef11-8a6a-000d3a5cc0a9}` | 1.0.0.0 | ✅ |

---

## Organizational Unit

| Field | Value |
|---|---|
| Schema Name | `msdyn_organizationalunit` |
| Display Name | Organizational Unit |
| Collection Name |  |
| Description |  |

---

## msdyn_warehouse

| Field | Value |
|---|---|
| Schema Name | `msdyn_warehouse` |
| Display Name | msdyn_warehouse |
| Collection Name |  |
| Description |  |

---

## Technician Characteristic

| Field | Value |
|---|---|
| Schema Name | `o25fs_VendorCharacteristic` |
| Display Name | Technician Characteristic |
| Collection Name |  |
| Description |  |

### Attributes

| Schema Name | Display Name | Type | Required | Options |
|---|---|---|---|---|
| `CreatedBy` | Created By | lookup | none |  |
| `CreatedOn` | Created On | datetime | none |  |
| `CreatedOnBehalfBy` | Created By (Delegate) | lookup | none |  |
| `ImportSequenceNumber` | Import Sequence Number | int | none |  |
| `ModifiedBy` | Modified By | lookup | none |  |
| `ModifiedOn` | Modified On | datetime | none |  |
| `ModifiedOnBehalfBy` | Modified By (Delegate) | lookup | none |  |
| `o25fs_CharacteristicId` | Characteristic | lookup | ✅ |  |
| `o25fs_RatingValueId` | Rating Value | lookup | none |  |
| `o25fs_VendorCharacteristicId` | Technician Characteristic | primarykey | ⚠️ |  |
| `o25fs_VendorCharacteristicName` | Technician Characteristic Name | nvarchar | none |  |
| `o25fs_VendorContactId` | Technician Contact | lookup | ✅ |  |
| `OverriddenCreatedOn` | Record Created On | datetime | none |  |
| `OwnerId` | Owner | owner | ⚠️ |  |
| `OwningBusinessUnit` | Owning Business Unit | lookup | ⚠️ |  |
| `OwningTeam` | Owning Team | lookup | none |  |
| `OwningUser` | Owning User | lookup | none |  |
| `statecode` | Status | state | ⚠️ |  |
| `statuscode` | Status Reason | status | none |  |
| `TimeZoneRuleVersionNumber` | Time Zone Rule Version Number | int | none |  |
| `UTCConversionTimeZoneCode` | UTC Conversion Time Zone Code | int | none |  |

### Forms

| Name | ID | Version | Active |
|---|---|---|---|
| Information | `{7e665938-c676-4c43-8501-e99779043b31}` | 1.0 | ✅ |
| Information | `{9bd7a5e1-3814-46eb-b986-e101aca860b2}` | 1.0 | ✅ |
| Vendor Characteristic quick create form | `{b671a30a-60a7-ef11-8a69-000d3a59d659}` | 1.0.0.0 | ✅ |
| Information | `{15a95fd5-b40e-4914-9b8e-e492089f3086}` | 1.0 | ✅ |

### Views

| Name | Type |
|---|---|
| Active Vendor Characteristics | Public View |
| Inactive Vendor Characteristics | Public View |
| My Vendor Characteristics | Type 8192 |
| Quick Find Active Vendor Characteristics | Quick Find |
| Vendor Characteristic Advanced Find View | Advanced Find |
| Vendor Characteristic Associated View | Associated View |
| Vendor Characteristic Lookup View | Lookup View |
| Vendor Characteristics Subgrid | Public View |

---

## RatingValue

| Field | Value |
|---|---|
| Schema Name | `RatingValue` |
| Display Name | RatingValue |
| Collection Name |  |
| Description |  |

---
