---
title: "Exports API Overview and Usage"
description: "The exports API allows you to export records, property data, or logs from your HubSpot account in various formats. It supports both view and list exports with customizable parameters such as file format, object type, associated objects, and properties. You can also filter the exported data based on specific criteria."
type: "concept"
tags:
- "HubSpot"
- "API"
- "Exporting Data"
relationships:
- "#related_to [[CRM]]"
- "#used_for [[Data Management]]"
start_date: "N/A"
end_date: "N/A"
---

Exports
=======

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the exports API to export records and property data from your HubSpot account, retrieve a URL to download an export file, or see the status of an export. Within HubSpot, you can also [export records](https://knowledge.hubspot.com/crm-setup/export-contacts-companies-deals-or-tickets) or [view a log of past exports in your account.](https://knowledge.hubspot.com/crm-setup/view-a-log-of-your-users-exports-in-your-account)

Start an export[](https://developers.hubspot.com/docs/api/crm/exports#start-an-export)
--------------------------------------------------------------------------------------

To start an export, make a `POST` request to `/crm/v3/exports/export/async`. Your request body should specify information such as the file format, the object and properties you want to export, and the type of export you're completing (e.g., exporting an object view or a list). You can also filter the property data to be exported based on specific operators.

For both view and list exports, you can include the following fields in your request:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`exportType`

 | 

The type of export, either `VIEW` (exports a view from an object index page) or `LIST` (exports a list).

 |
| 

`format`

 | 

The file format. Options include `XLSX`, `CSV`, or `XLS`.

 |
| 

`exportName`

 | 

The name of the export.

 |
| 

`language`

 | 

The language of the export file. Options include `DE`, `EN`, `ES`, `FI`, `FR`, `IT`, `JA`, `NL`, `PL`, `PT`, or `SV`. Learn more about [supported languages.](https://knowledge.hubspot.com/account/hubspot-language-offerings)

 |
| 

`objectType`

 | 

The name or ID of the object you're exporting. For standard objects, you can use the object's name (e.g., `CONTACT`), but for custom objects, you must use the `objectTypeId` value. You can retrieve this value by making a `GET` request to `/crm/v3/schemas`.

 |
| 

`associatedObjectType`

 | 

The name or ID of an associated object to include in the export. If you include an associated object, the export will contain the associated record IDs of that object and the records' primary display property value (e.g., name). You can export only one associated object per request.

 |
| 

`objectProperties`

 | 

A list of the properties you want included in your export.

 |

### Export a view[](https://developers.hubspot.com/docs/api/crm/exports#export-a-view)

If you're exporting an [index page view](https://knowledge.hubspot.com/crm-setup/create-customize-and-manage-your-saved-views), your `exportType` value should be `VIEW`, and you can include the following field to filter and sort the records you're exporting:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`publicCrmSearchRequest`

 | 

Indicates which data should be exported based on certain property values and search queries. You can include the following within the object:

`filters`: the properties and property values to filter records by.  
`sorts`: the sort order of a property's values, either ascending, `ASC`, or descending, `DES`.  
`query`: a string to search the records' values for.

 |

For example, to export a view of contacts and associated company records, filtered by the `email` property, your request may look like the following:

///Example request body { "exportType": "VIEW", "exportName": "All contacts", "format": "xlsx", "language": "DE", "objectType": "CONTACT", "objectProperties": \[ "email, firstname, lastname" \], "associatedObjectType": "COMPANY", "publicCrmSearchRequest": { "filters": \[ { "value": "hello@test.com", "propertyName": "email", "operator": "EQ" } \], "query": "hello", "sorts": \[ { "propertyName": "email", "order": "ASC" } \] } }

### Export a list[](https://developers.hubspot.com/docs/api/crm/exports#export-a-list)

If you're exporting a [list](https://knowledge.hubspot.com/lists/create-active-or-static-lists), your `exportType` value should be `LIST`, but you also need to specify the list you're exporting with the following field:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`listId`

 | 

The [ILS List ID](https://knowledge.hubspot.com/lists/lists-faq#ils-list) of the list to export. You can find the ILS List ID value via the list details in HubSpot. Navigate to **Contacts** > **Lists**, hover over the **list** in the table, then click **Details**. In the right panel, click **Copy** **List ID** next to the ILS List ID value. Contact lists have two different ID values, but you must use the ILS List ID value in your request.

 |

For example, to export a list with the contacts' emails, your request may look like the following:

///Example request body { "exportType": "LIST", "listId": 1234567, "exportName": "Marketing email contacts", "format": "xlsx", "language": "EN", "objectType": "CONTACT", "objectProperties": \[ "email" \] }

Retrieve exports[](https://developers.hubspot.com/docs/api/crm/exports#retrieve-exports)
----------------------------------------------------------------------------------------

When you successfully complete an export, the export's `id` will be returned in the response. To retrieve an export from your HubSpot account, make a `GET` request to `/crm/v3/exports/export/async/tasks/{exportId}/status`.

When retrieving exports, the `status` of the export will also be returned. Possible statuses include `COMPLETE`, `PENDING`, `PROCESSING`, or `CANCELED`. For exports with a `COMPLETE` status, a URL is returned that you can use to download the exported file. The download URL will expire five minutes after the completed request. Once expired, you can perform another `GET` request to generate a new unique URL.

**Please note**: prior to expiration, an export's download URL can be accessed without any additional authorization. To protect your data, proceed with caution when sharing a URL or integrating with HubSpot via this API.

Limits[](https://developers.hubspot.com/docs/api/crm/exports#limits)
--------------------------------------------------------------------

The following limits apply to the export endpoints:

*   When setting filters for your export, you can include a maximum of three `filterGroups` with up to three `filters` in each group.

*   You can complete up to thirty exports within a rolling 24 hour window, and one export at a time. Additional exports will be queued until the previous export is completed.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/exports#page-feedback)
----------------------------------------------------------------------------------------

Was this article helpful? Yes No

Thanks for letting us know. How would you describe this article?

 Inaccurate: it doesn’t reflect what I see in the product

 Unclear: it’s difficult to understand

 Missing information: it’s not comprehensive enough

 Irrelevant: it doesn’t match what I searched for

Great! Is there anything we could change to make it even more helpful? Is there anything we could change to make this article helpful?

 Allow HubSpot to contact me about my documentation feedback.

Email address

Only used if we need clarification on your feedback.

 

Thank you for your feedback, it means a lot to us.

Sorry this feedback form requires JavaScript to function.

This form is used for documentation feedback only. Learn how to [get help with HubSpot](https://knowledge.hubspot.com/account/get-help-with-hubspot).