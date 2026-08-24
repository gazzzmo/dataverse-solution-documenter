# Security Roles

**Total security roles:** 2

| Level | Meaning |
|---|---|
| 🌐 Global | Entire organisation |
| 🔵 Deep | Business unit + child units |
| 🟡 Local | Own business unit only |
| 🟢 Basic | Records owned by the user |

---

## Cross-Role Comparison — Solution Entities

> Showing **Read** access level per role for entities defined in this solution.

| Entity | Field Service - Vendor Admin | Field Service - Vendor Resource |
|---|---|---|
| `BookableResource` | 🌐 Global | 🔵 Deep |
| `Characteristic` | 🌐 Global | 🟡 Local |
| `Contact` | 🌐 Global | 🟡 Local |
| `msdyn_organizationalunit` | 🌐 Global | 🌐 Global |
| `msdyn_warehouse` | 🌐 Global | 🔵 Deep |
| `o25fs_VendorCharacteristic` | 🔵 Deep | — |
| `RatingValue` | 🌐 Global | 🟡 Local |

---

## Field Service - Vendor Admin

### Solution Entities

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `BookableResource` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `Characteristic` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `Contact` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_organizationalunit` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_warehouse` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `o25fs_VendorCharacteristic` | 🔵 Deep | 🔵 Deep | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🔵 Deep |
| `RatingValue` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |

### All Entity Privileges

**🌐 Global access** (274 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `Account` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `ActionCard` | — | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `Activity` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `AppModule` | — | 🌐 Global | — | — | — | — | — | — |
| `ApplicationFile` | — | 🌐 Global | — | — | — | — | — | — |
| `Attribute` | — | 🌐 Global | — | — | — | — | — | — |
| `AttributeMap` | — | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | — | — |
| `AuditSummary` | — | 🌐 Global | — | — | — | — | — | — |
| `BookableResourceBooking` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | 🌐 Global |
| `BookableResourceBookingHeader` | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `BookableResourceCategory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `BookableResourceCategoryAssn` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `BookableResourceCharacteristic` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `BookableResourceGroup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `BookingStatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `BusinessClosureCalendar` | — | — | 🌐 Global | — | — | — | — | — |
| `BusinessUnit` | — | 🌐 Global | — | — | 🔵 Deep | 🔵 Deep | — | — |
| `Calendar` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `Competitor` | — | 🌐 Global | — | — | — | — | — | — |
| `ComplexControl` | — | 🌐 Global | — | — | — | — | — | — |
| `Connection` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `ConnectionRole` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `CustomerOpportunityRole` | — | 🌐 Global | — | — | — | — | — | — |
| `Customization` | — | 🌐 Global | — | — | — | — | — | — |
| `DuplicateRule` | — | 🌐 Global | — | — | — | — | — | — |
| `DynamicProperty` | — | 🌐 Global | — | — | — | — | — | — |
| `DynamicPropertyAssociation` | — | 🌐 Global | — | — | — | — | — | — |
| `DynamicPropertyInstance` | — | 🌐 Global | — | — | — | — | — | — |
| `DynamicPropertyOptionSetItem` | — | 🌐 Global | — | — | — | — | — | — |
| `Entitlement` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `EntitlementEntityAllocationTypeMapping` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `Entity` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `EntityKey` | — | 🌐 Global | — | — | — | — | — | — |
| `EntityMap` | — | 🌐 Global | 🌐 Global | — | — | 🌐 Global | — | — |
| `ExpiredProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `FieldSecurityProfile` | — | 🌐 Global | — | — | — | — | — | — |
| `GoalRollupQuery` | — | 🌐 Global | — | — | — | — | — | — |
| `HierarchicalSecurityConfiguration` | — | — | 🌐 Global | — | — | — | — | — |
| `HierarchyRule` | — | 🌐 Global | — | — | — | — | — | — |
| `HolidayScheduleCalendar` | — | — | 🌐 Global | — | — | — | — | — |
| `ImportJob` | — | 🌐 Global | — | — | — | — | — | — |
| `Incident` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `Invoice` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `KnowledgeArticle` | 🔵 Deep | 🌐 Global | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🌐 Global |
| `KnowledgeArticleViews` | 🌐 Global | 🌐 Global | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🌐 Global |
| `KnowledgeBaseRecord` | — | 🌐 Global | — | — | — | — | — | — |
| `LanguageLocale` | — | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `Lead` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `LeadToOpportunitySalesProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `Mailbox` | — | 🌐 Global | — | — | — | — | — | — |
| `MobileOfflineProfile` | — | 🌐 Global | — | — | — | — | — | — |
| `NewProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `Note` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `Opportunity` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `OpportunitySalesProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `OptionSet` | — | 🌐 Global | — | — | — | — | — | — |
| `Order` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `Organization` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `OrganizationSetting` | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `OwnCalendar` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `PhoneToCaseProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `PlannerSyncAction` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `PluginAssembly` | — | 🌐 Global | — | — | — | — | — | — |
| `PluginTraceLog` | — | 🌐 Global | — | — | — | — | — | — |
| `PluginType` | — | 🌐 Global | — | — | — | — | — | — |
| `Post` | — | 🌐 Global | — | — | — | — | — | — |
| `Product` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `Publisher` | — | 🌐 Global | — | — | — | — | — | — |
| `Query` | — | 🌐 Global | — | — | — | — | — | — |
| `Quote` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `RatingModel` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `RecordAuditHistory` | — | 🌐 Global | — | — | — | — | — | — |
| `Relationship` | — | 🌐 Global | — | — | — | — | — | — |
| `ResourceBookingDetail` | — | — | — | — | 🌐 Global | — | — | — |
| `ResourceBookingHeader` | — | — | — | 🌐 Global | — | — | — | — |
| `Role` | — | 🌐 Global | — | — | — | — | — | — |
| `SLA` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `SLAKPIInstance` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `SavedQueryVisualizations` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `SdkMessage` | — | 🌐 Global | — | — | — | — | — | — |
| `SdkMessageProcessingStep` | — | 🌐 Global | — | — | — | — | — | — |
| `SdkMessageProcessingStepImage` | — | 🌐 Global | — | — | — | — | — | — |
| `SdkMessageProcessingStepSecureConfig` | — | 🌐 Global | — | — | — | — | — | — |
| `Service` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `ServiceEndpoint` | — | 🌐 Global | — | — | — | — | — | — |
| `SettingDefinition` | — | 🌐 Global | — | — | — | — | — | — |
| `SharePointData` | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `SharePointDocument` | — | 🌐 Global | — | — | — | — | — | — |
| `SharePointDocumentLocation` | — | 🌐 Global | — | — | — | — | — | — |
| `Site` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | — | — |
| `Solution` | — | 🌐 Global | — | — | — | — | — | — |
| `Subject` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `SystemApplicationMetadata` | — | 🌐 Global | — | — | — | — | — | — |
| `SystemForm` | — | 🌐 Global | — | — | — | — | — | — |
| `Team` | — | 🌐 Global | — | — | — | — | — | — |
| `Territory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — |
| `Theme` | — | 🌐 Global | — | — | — | — | — | — |
| `TransactionCurrency` | — | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `TranslationProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `User` | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | — | — |
| `UserSettings` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | — | — |
| `WebResource` | — | 🌐 Global | — | — | — | — | — | — |
| `Workflow` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `WorkflowSession` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_Configuration` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_FieldServiceSummaryConfiguration` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_FunctionalLocation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_FunctionalLocationType` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_MobileSource` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_PostAlbum` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_PostConfig` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_PostRuleConfig` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_Warranty` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_actual` | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreement` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementbookingdate` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementbookingincident` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementbookingproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementbookingservice` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementbookingservicetask` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementbookingsetup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementinvoicedate` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementinvoiceproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementinvoicesetup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_agreementsubstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_assetcategorytemplateassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_assetsuggestionssetting` | — | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `msdyn_assettemplateassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookableresourceassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookableresourcebookingquicknote` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookingalertstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookingchange` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookingjournal` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookingrule` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookingsetupmetadata` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bookingtimestamp` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_bpf_2c5fe86acc8b414b8322ae571000c799` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_bpf_989e9b1857e24af18787d5143b67523b` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_bpf_baa0a411a239410cb8bded8b5fdd88e3` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_bpf_d3d97bac8c294105840e99e37a9d1c39` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_customerasset` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_customerassetcategory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_dataanalyticsreport_fs` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_dataanalyticsreport_fspredictrs` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_dataanalyticsreport_fspredictwhd` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_datainsightsandanalyticsfeature` | — | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `msdyn_entitlementapplication` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_entityconfiguration` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `msdyn_federatedarticle` | 🔵 Deep | 🌐 Global | — | 🔵 Deep | 🌐 Global | 🌐 Global | — | — |
| `msdyn_federatedarticleincident` | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | — | — |
| `msdyn_fieldservicepricelistitem` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_fieldservicesetting` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_fieldserviceslaconfiguration` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_fieldservicesystemjob` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_flwconfiguration` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_geofence` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `msdyn_geofenceevent` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `msdyn_geofencingsettings` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — |
| `msdyn_geolocationsettings` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_geolocationtracking` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_incidenttype` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttype_requirementgroup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttypecharacteristic` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttypeproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttyperecommendationresult` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttyperecommendationrunhistory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttyperesolution` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttypeservice` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_incidenttypeservicetask` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inspection` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inspectionattachment` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inspectiondefinition` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inspectioninstance` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inspectionresponse` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_insurance` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inventoryadjustment` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inventoryadjustmentproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inventoryjournal` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_inventorytransfer` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_kbattachment` | 🔵 Deep | 🌐 Global | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🌐 Global |
| `msdyn_kmfederatedsearchconfig` | 🔵 Deep | 🌐 Global | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🌐 Global |
| `msdyn_knowledgearticleimage` | 🔵 Deep | 🌐 Global | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🌐 Global |
| `msdyn_knowledgearticletemplate` | 🔵 Deep | 🌐 Global | 🔵 Deep | 🔵 Deep | 🌐 Global | 🌐 Global | 🔵 Deep | 🌐 Global |
| `msdyn_knowledgeinteractioninsight` | 🔵 Deep | 🌐 Global | — | — | — | — | — | — |
| `msdyn_knowledgesearchinsight` | 🔵 Deep | 🌐 Global | — | — | — | — | — | — |
| `msdyn_locationtemplateassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_locationtypetemplateassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_nottoexceed` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_orderinvoicingdate` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_orderinvoicingproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_orderinvoicingsetup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_orderinvoicingsetupdate` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_payment` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_paymentdetail` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_paymentmethod` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_paymentterm` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_postalcode` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_priority` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_productinventory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_property` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_propertyassetassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_propertylocationassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_propertylog` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_propertytemplateassociation` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_purchaseorder` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_purchaseorderbill` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_purchaseorderproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_purchaseorderreceipt` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_purchaseorderreceiptproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_purchaseordersubstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quotebookingincident` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quotebookingproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quotebookingservice` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quotebookingservicetask` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quotebookingsetup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quoteinvoicingproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_quoteinvoicingsetup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementchange` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementcharacteristic` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementgroup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementorganizationunit` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementrelationship` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementresourcecategory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementresourcepreference` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_requirementstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_resolution` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_resourcepaytype` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_resourcerequirement` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_resourcerequirementdetail` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_resourceterritory` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rma` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rmaproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rmareceipt` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rmareceiptproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rmasubstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rtv` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rtvproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_rtvsubstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_scheduleboardsetting` | 🟢 Basic | 🌐 Global | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic |
| `msdyn_schedulingfeatureflag` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_schedulingparameter` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_servicetasktype` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_shipvia` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_solutioncomponentsummary` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_systemuserschedulersetting` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_taxcode` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_taxcodedetail` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_templateforproperties` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_timeentry` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_timeentrysetting` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_timegroup` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_timegroupdetail` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_timeoffrequest` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_tour` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_trade` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_tradecoverage` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_transactionorigin` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_uniquenumber` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_wallsavedquery` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_wallsavedqueryusersettings` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workhourtemplate` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorder` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workordercharacteristic` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorderdetailsgenerationqueue` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_workorderincident` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workordernte` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorderproduct` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorderresolution` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorderresourcerestriction` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorderservice` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workorderservicetask` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workordersubstatus` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_workordertype` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `plannerbusinessscenario` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |

</details>

**🔵 Deep access** (1 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `Campaign` | — | — | — | — | — | 🔵 Deep | — | — |

</details>

**🟢 Basic access** (10 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `ActionCardUserSettings` | — | 🟢 Basic | — | — | — | — | — | — |
| `AsyncOperation` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `ExchangeSyncIdMapping` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — |
| `Queue` | — | 🟢 Basic | — | — | — | — | — | — |
| `UserApplicationMetadata` | — | 🟢 Basic | 🟢 Basic | — | — | — | — | — |
| `UserEntityInstanceData` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | 🟢 Basic | 🟢 Basic |
| `UserEntityUISettings` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | 🟢 Basic |
| `UserForm` | — | 🟢 Basic | — | — | — | — | — | — |
| `UserQuery` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | 🟢 Basic | 🟢 Basic |
| `UserQueryVisualizations` | — | 🟢 Basic | — | — | — | — | — | — |

</details>

### Miscellaneous Privileges

**13 non-entity privileges** (feature access, system actions)

| Privilege | Level |
|---|---|
| AdminFilter | 🌐 Global |
| BrowseAvailability | 🌐 Global |
| BulkEdit | 🌐 Global |
| DisableUser | 🌐 Global |
| ExportToExcel | 🌐 Global |
| ISVExtensions | 🌐 Global |
| OverridePriceEngineOpportunity | 🌐 Global |
| OverridePriceEngineQuote | 🌐 Global |
| PublishKnowledgeArticle | 🌐 Global |
| SearchAvailability | 🌐 Global |
| SyncToOutlook | 🌐 Global |
| UseTabletApp | 🌐 Global |
| WorkflowExecution | 🌐 Global |

### Summary

| Metric | Count |
|---|---|
| Entities with privileges | 292 |
| Total entity privilege grants | 1703 |
| Miscellaneous privilege grants | 13 |

---

## Field Service - Vendor Resource

### Solution Entities

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `BookableResource` | — | 🔵 Deep | — | — | 🔵 Deep | 🔵 Deep | 🔵 Deep | — |
| `Characteristic` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `Contact` | — | 🟡 Local | 🟢 Basic | — | — | 🟡 Local | — | — |
| `msdyn_organizationalunit` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_warehouse` | — | 🔵 Deep | 🟡 Local | — | 🟡 Local | 🟡 Local | 🟡 Local | 🟡 Local |
| `o25fs_VendorCharacteristic` | — | — | — | — | — | — | — | — |
| `RatingValue` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |

### All Entity Privileges

**🌐 Global access** (88 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `AppModule` | — | 🌐 Global | — | — | — | — | — | — |
| `ApplicationFile` | — | 🌐 Global | — | — | — | — | — | — |
| `Attribute` | — | 🌐 Global | — | — | — | — | — | — |
| `AttributeMap` | — | 🌐 Global | — | — | — | — | — | — |
| `ComplexControl` | — | 🌐 Global | — | — | — | — | — | — |
| `ConnectionRole` | — | 🌐 Global | — | — | — | — | — | — |
| `Customization` | — | 🌐 Global | — | — | — | — | — | — |
| `EntitlementEntityAllocationTypeMapping` | — | 🌐 Global | — | — | — | 🟡 Local | — | — |
| `Entity` | — | 🌐 Global | — | — | — | — | — | — |
| `EntityMap` | — | 🌐 Global | — | — | — | — | — | — |
| `ExpiredProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `HierarchyRule` | — | 🌐 Global | — | — | — | — | — | — |
| `KnowledgeArticle` | — | 🌐 Global | — | — | 🔵 Deep | 🔵 Deep | — | — |
| `KnowledgeArticleViews` | — | 🌐 Global | — | — | — | — | — | — |
| `LanguageLocale` | — | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `LeadToOpportunitySalesProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `MobileOfflineProfile` | — | 🌐 Global | — | — | — | — | — | — |
| `NewProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `OpportunitySalesProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `OptionSet` | — | 🌐 Global | — | — | — | — | — | — |
| `Organization` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `OrganizationSetting` | — | 🌐 Global | — | — | — | — | — | — |
| `PhoneToCaseProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `PlannerSyncAction` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — |
| `PluginAssembly` | — | 🌐 Global | — | — | — | — | — | — |
| `PluginType` | — | 🌐 Global | — | — | — | — | — | — |
| `Product` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `Query` | — | 🌐 Global | — | — | — | — | — | — |
| `Relationship` | — | 🌐 Global | — | — | — | — | — | — |
| `SavedQueryVisualizations` | — | 🌐 Global | — | — | — | — | — | — |
| `SdkMessage` | — | 🌐 Global | — | — | — | — | — | — |
| `SdkMessageProcessingStep` | — | 🌐 Global | — | — | — | — | — | — |
| `SdkMessageProcessingStepImage` | — | 🌐 Global | — | — | — | — | — | — |
| `ServiceEndpoint` | — | 🌐 Global | — | — | — | — | — | — |
| `SettingDefinition` | — | 🌐 Global | — | — | — | — | — | — |
| `SharePointData` | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `SharePointDocument` | — | 🌐 Global | — | — | — | — | — | — |
| `Solution` | — | 🌐 Global | — | — | — | — | — | — |
| `Subject` | — | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `SystemApplicationMetadata` | — | 🌐 Global | — | — | — | — | — | — |
| `SystemForm` | — | 🌐 Global | — | — | — | — | — | — |
| `Territory` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `TransactionCurrency` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `TranslationProcess` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `WebResource` | — | 🌐 Global | — | — | — | — | — | — |
| `Workflow` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `msdyn_FieldServiceSummaryConfiguration` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_FunctionalLocationType` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `msdyn_MobileSource` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_PostConfig` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_assetcategorytemplateassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_assettemplateassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_bookingsetupmetadata` | — | 🌐 Global | — | — | 🔵 Deep | 🔵 Deep | — | — |
| `msdyn_bpf_2c5fe86acc8b414b8322ae571000c799` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_bpf_989e9b1857e24af18787d5143b67523b` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_bpf_baa0a411a239410cb8bded8b5fdd88e3` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_bpf_d3d97bac8c294105840e99e37a9d1c39` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | — | — |
| `msdyn_customerassetcategory` | — | 🌐 Global | — | — | — | 🌐 Global | — | — |
| `msdyn_entityconfiguration` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_federatedarticle` | 🔵 Deep | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `msdyn_federatedarticleincident` | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | — | — |
| `msdyn_fieldservicepricelistitem` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_fieldservicesetting` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_fieldserviceslaconfiguration` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_fieldservicesystemjob` | 🌐 Global | 🌐 Global | 🌐 Global | — | — | — | — | — |
| `msdyn_flwconfiguration` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_geolocationsettings` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_kbattachment` | — | 🌐 Global | — | — | 🔵 Deep | 🔵 Deep | — | — |
| `msdyn_kbenrichment` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_kmfederatedsearchconfig` | — | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `msdyn_knowledgearticleimage` | — | 🌐 Global | — | — | 🌐 Global | 🌐 Global | — | — |
| `msdyn_knowledgearticlesuggestion` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_knowledgearticletemplate` | — | 🌐 Global | — | — | — | 🟡 Local | — | — |
| `msdyn_locationtemplateassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_locationtypetemplateassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_productinventory` | 🌐 Global | 🌐 Global | 🌐 Global | — | 🌐 Global | 🌐 Global | — | — |
| `msdyn_property` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_propertyassetassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_propertylocationassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_propertylog` | 🟢 Basic | 🌐 Global | 🟢 Basic | — | 🟢 Basic | 🔵 Deep | — | — |
| `msdyn_propertytemplateassociation` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_schedulingparameter` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_solutioncomponentsummary` | — | 🌐 Global | — | — | — | — | — | — |
| `msdyn_systemuserschedulersetting` | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global | 🌐 Global |
| `msdyn_templateforproperties` | — | 🌐 Global | — | — | — | 🔵 Deep | — | — |
| `msdyn_timeentrysetting` | 🟢 Basic | 🌐 Global | 🟢 Basic | — | 🟢 Basic | 🌐 Global | — | — |
| `msdyn_tour` | — | 🌐 Global | — | — | — | — | — | — |
| `plannerbusinessscenario` | — | 🌐 Global | 🌐 Global | — | — | 🌐 Global | — | — |

</details>

**🔵 Deep access** (4 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `BookingStatus` | — | 🔵 Deep | — | — | 🔵 Deep | 🔵 Deep | — | — |
| `msdyn_bookingrule` | — | 🔵 Deep | — | — | — | — | — | — |
| `msdyn_postalcode` | — | 🔵 Deep | — | — | — | — | — | — |
| `msdyn_requirementstatus` | — | 🔵 Deep | — | — | 🔵 Deep | 🔵 Deep | — | — |

</details>

**🟡 Local access** (62 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `Account` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `BookableResourceCategory` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `BookableResourceCategoryAssn` | — | 🟡 Local | — | — | — | — | — | — |
| `BookableResourceCharacteristic` | — | 🟡 Local | — | — | — | — | — | — |
| `BusinessUnit` | — | 🟡 Local | — | — | — | — | — | — |
| `Calendar` | 🟡 Local | 🟡 Local | 🟡 Local | — | — | — | — | — |
| `Connection` | 🟡 Local | 🟡 Local | 🟡 Local | — | — | — | — | — |
| `Entitlement` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `Equipment` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `RatingModel` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `Role` | — | 🟡 Local | — | — | — | — | — | — |
| `SLA` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `SLAKPIInstance` | 🟢 Basic | 🟡 Local | 🟡 Local | — | 🟡 Local | 🟡 Local | — | — |
| `Team` | — | 🟡 Local | — | — | — | — | — | — |
| `User` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `UserSettings` | — | 🟡 Local | 🟡 Local | — | — | — | — | — |
| `msdyn_FunctionalLocation` | 🟡 Local | 🟡 Local | 🟡 Local | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_Warranty` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_customerasset` | 🟡 Local | 🟡 Local | 🟡 Local | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_entitlementapplication` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_incidenttype` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_incidenttype_requirementgroup` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttypecharacteristic` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttypeproduct` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttyperecommendationresult` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttyperecommendationrunhistory` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttyperesolution` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttypeservice` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_incidenttypeservicetask` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_inspection` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_inspectiondefinition` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_insurance` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotalert` | 🟡 Local | 🟡 Local | 🟡 Local | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdevice` | 🟡 Local | 🟡 Local | 🟡 Local | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdevicecategory` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdevicecommand` | 🟡 Local | 🟡 Local | 🟡 Local | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdevicecommanddefinition` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdevicedatahistory` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdeviceproperty` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdeviceregistrationhistory` | 🟡 Local | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotdevicevisualizationconfiguration` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotfieldmapping` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotpropertydefinition` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotprovider` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotproviderinstance` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_iotsettings` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_nottoexceed` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_paymentmethod` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_paymentterm` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_priority` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_resolution` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_resourcepaytype` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_resourceterritory` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_servicetasktype` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_taxcode` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_taxcodedetail` | — | 🟡 Local | — | — | — | — | — | — |
| `msdyn_timegroup` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_timegroupdetail` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_trade` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_tradecoverage` | — | 🟡 Local | — | — | 🟡 Local | 🟡 Local | — | — |
| `msdyn_workordersubstatus` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |
| `msdyn_workordertype` | — | 🟡 Local | — | — | — | 🟡 Local | — | — |

</details>

**🟢 Basic access** (52 entities)

<details><summary>Expand</summary>

| Entity | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|---|---|---|---|---|---|---|---|---|
| `ActionCard` | — | 🟢 Basic | 🟢 Basic | — | — | — | — | — |
| `ActionCardUserSettings` | — | 🟢 Basic | — | — | — | — | — | — |
| `Activity` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | 🟢 Basic |
| `AsyncOperation` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `BookableResourceBooking` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | 🟢 Basic | — | 🟢 Basic |
| `BookableResourceBookingHeader` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | 🟢 Basic |
| `BookableResourceGroup` | — | 🟢 Basic | — | — | — | — | — | — |
| `ExchangeSyncIdMapping` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — |
| `Note` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic |
| `Queue` | — | 🟢 Basic | — | — | — | — | — | — |
| `ResourceBookingDetail` | — | — | — | — | 🟢 Basic | — | — | — |
| `SyncError` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic |
| `UserApplicationMetadata` | — | 🟢 Basic | 🟢 Basic | — | — | — | — | — |
| `UserEntityInstanceData` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — | — |
| `UserEntityUISettings` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — | — |
| `UserForm` | — | 🟢 Basic | — | — | — | — | — | — |
| `UserQuery` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | 🟢 Basic | 🟢 Basic |
| `UserQueryVisualizations` | — | 🟢 Basic | — | — | — | — | — | — |
| `msdyn_actual` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | — | 🟢 Basic | — |
| `msdyn_bookableresourceassociation` | — | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_bookableresourcebookingquicknote` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic |
| `msdyn_bookingalertstatus` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic |
| `msdyn_bookingchange` | 🟢 Basic | 🟢 Basic | — | — | — | — | — | — |
| `msdyn_bookingjournal` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — |
| `msdyn_bookingtimestamp` | 🟢 Basic | 🟢 Basic | — | — | 🟢 Basic | — | — | — |
| `msdyn_geofence` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — |
| `msdyn_geofenceevent` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — |
| `msdyn_inspectionattachment` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_inspectioninstance` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_inspectionresponse` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_inventoryjournal` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🔵 Deep | 🟢 Basic | 🟢 Basic |
| `msdyn_payment` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_paymentdetail` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_requirementchange` | 🟢 Basic | 🟢 Basic | — | — | — | — | — | — |
| `msdyn_requirementcharacteristic` | 🟢 Basic | 🟢 Basic | — | — | 🟢 Basic | — | — | — |
| `msdyn_requirementgroup` | — | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_requirementrelationship` | — | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_requirementresourcepreference` | — | 🟢 Basic | — | — | — | — | — | — |
| `msdyn_resourcerequirement` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_richtextfile` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — | — | — |
| `msdyn_scheduleboardsetting` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic |
| `msdyn_timeentry` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🌐 Global | — | — |
| `msdyn_timeoffrequest` | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | 🟢 Basic | — |
| `msdyn_workorder` | — | 🟢 Basic | 🟢 Basic | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workordercharacteristic` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workorderincident` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workordernte` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workorderproduct` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workorderresolution` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workorderresourcerestriction` | — | 🟢 Basic | — | — | 🟢 Basic | 🟢 Basic | — | — |
| `msdyn_workorderservice` | 🟢 Basic | 🟢 Basic | 🟡 Local | 🟢 Basic | 🟡 Local | 🟢 Basic | — | — |
| `msdyn_workorderservicetask` | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | 🟢 Basic | — | — |

</details>

### Miscellaneous Privileges

**6 non-entity privileges** (feature access, system actions)

| Privilege | Level |
|---|---|
| BulkEdit | 🌐 Global |
| GoOffline | 🌐 Global |
| ISVExtensions | 🌐 Global |
| SyncToOutlook | 🌐 Global |
| UseTabletApp | 🌐 Global |
| WorkflowExecution | 🌐 Global |

### Summary

| Metric | Count |
|---|---|
| Entities with privileges | 212 |
| Total entity privilege grants | 617 |
| Miscellaneous privilege grants | 6 |

---
