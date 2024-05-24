Lists
=====

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

 Lists are a collection of records of the same object type that can be used for record segmentation, filtering, and grouping to serve your business needs. You can create contact, company, deal, or custom object lists. The v3 Lists API allows you to create, edit, and fetch lists. 

A list consists of a list definition and list memberships:

*   List definition: stores essential information about the list. 
*   List memberships: mappings between the list and object record.

Starting May 30, 2025, the [legacy v1 Lists API](https://legacydocs.hubspot.com/docs/methods/lists/contact-lists-overview) will be sunset. If you were previously using the v1 Lists API, review the [guide below](#migrate-from-v1-to-v3-api-endpoints) to transition to the v3 API.

List Processing Types[](https://developers.hubspot.com/docs/api/crm/lists#list-processing-types)
------------------------------------------------------------------------------------------------

There are three types of list processing types: `MANUAL`, `DYNAMIC`, and `SNAPSHOT`. 

`MANUAL`: this processing type indicates that object records can only be added to or removed from the list via manual actions by the user or API call. There is no list processing or list membership management done in the background by HubSpot's systems.

`DYNAMIC`: this processing type gives the possibility to specify filters to match records that will become list members. This type of list is processed in the background by HubSpot systems to ensure that the list only contains records that match the list's filters. Whenever a record changes, it is reevaluated against the list's filters and either added to or removed from it. 

`SNAPSHOT`: filters are specified at the time of list creation. After initial processing is completed, records can only be added to or removed from the list by manual actions.

**Please note:** use the [ILS List ID](https://knowledge.hubspot.com/lists/lists-faq?_gl=1*143kakg*_ga*OTkwNTMxMzkxLjE2OTc1OTQ1OTc.*_ga_LXTM6CQ0XK*MTY5NzU5NDU5Ni4xLjEuMTY5NzU5NzI5NC42MC4wLjA.#ils-list) when making requests to the v3 lists API to ensure the correct lists are selected.  

*   You can find the ILS list ID in app by hovering over a list in the Lists tool and clicking **Details**.

*   You can also make a `POST` request to `/crm/v3/lists/search` and omit the `query` parameter in the body of your request. The response will include all of your lists, each of which will include its associated ILS List ID.

Filter definitions[](https://developers.hubspot.com/docs/api/crm/lists#filter-definitions)
------------------------------------------------------------------------------------------

Filters are used together with filter branches to define the list criteria. This criteria determines how records will be added to either a `SNAPSHOT` or `DYNAMIC` list. Learn more about filters and how to define them [here](/docs/api/crm/list-filters-definitions). 

Create a list[](https://developers.hubspot.com/docs/api/crm/lists#create-a-list)
--------------------------------------------------------------------------------

To create a list, make a `POST` request to `/v3/lists`.

In your request, you must include the following parameters: `name`, `objectTypeId`, and `processingType`. The `filterBranch` parameter is optional. Once created, a `listID` (the ILD list ID) will be generated. This ID is used for future updates and modifications.

Retrieve a list[](https://developers.hubspot.com/docs/api/crm/lists#retrieve-a-list)
------------------------------------------------------------------------------------

A list can be retrieved by using either the ILS list ID or the name and object type for the list.

To retrieve a list using the ILS list ID, make a `GET` request to `/v3/lists/{listId}`.

To retrieve a list using a list name, make a `GET` request to `/v3/lists/object-type-id/{objectTypeId}/name/{listName}`. The `objectTypeId` is the ID that corresponds to the type of object stored by the list. Review the list of `objectTypeID`s [here](/docs/api/crm/understanding-the-crm). 

When retrieving a list, an optional query param flag, `includeFilters`, can be set to true if the list definitions in the response should include the filter branch definition.

### Retrieve multiple lists[](https://developers.hubspot.com/docs/api/crm/lists#retrieve-multiple-lists)

Multiple lists can be fetched in a single request by sending a `GET` request to `/v3/lists` with the list IDs to fetch as the `listIDs` parameter.

An optional query param flag, `includeFilters`, can be set to `true` if the list definitions in the response should include the filter branch definition.

Update a list name[](https://developers.hubspot.com/docs/api/crm/lists#update-a-list-name)
------------------------------------------------------------------------------------------

To update a list name, make a `PUT` request to `/v3/lists/{listId}/update-list-name` with the `listName` query parameter. If the list with the provided ILS list ID exists, then its name will be updated to the provided `listName`. The `listName` must be unique amongst all other public lists in the portal.

An optional query param flag, `includeFilters`, can be set to `true` if the list definitions in the response should include the filter branch definition.

### Update a list filter branch[](https://developers.hubspot.com/docs/api/crm/lists#update-a-list-filter-branch)

This endpoint can only be used for lists with a `DYNAMIC` processing type. 

A list filter branch can be updated by sending a `PUT` request to `/v3/lists/{listId}/update-list-filters` with a request body containing the new filter branch definition. If the list with the provided ILS list ID exists, then its filter branch definition will be updated to the provided filter branch. Oncethe filter branch is updated, the list will begin processing its new memberships. 

Search for a list[](https://developers.hubspot.com/docs/api/crm/lists#search-for-a-list)
----------------------------------------------------------------------------------------

Lists can be searched by list name by sending a `POST` request to `/v3/lists/search`.  If no `name` is provided, then the endpoint will provide all lists in the portal up to the count provided in the request.

Delete and restore a list[](https://developers.hubspot.com/docs/api/crm/lists#delete-and-restore-a-list)
--------------------------------------------------------------------------------------------------------

To delete a list, make a `DELETE` request to `/v3/lists/{listId}`.

Once deleted, lists can be restored within 90 days of deletion by making a `PUT` request to `/v3/lists/{listID}/restore`. Lists deleted more than 90 days ago cannot be restored.

List membership endpoints[](https://developers.hubspot.com/docs/api/crm/lists#list-membership-endpoints)
--------------------------------------------------------------------------------------------------------

List membership endpoints can only be used on `MANUAL` or `SNAPSHOT` list processing types. `DYNAMIC` lists will add and remove records based on the filter criteria set. 

### Add records to an existing list[](https://developers.hubspot.com/docs/api/crm/lists#add-records-to-an-existing-list)

To add records to an existing list, make a `PUT` request to `/v3/lists/{listId}/memberships/add` with a list of `recordID`s in the request body. 

To add records from one list to another, make a `PUT` request to ​`/v3​/lists/{listId}/memberships​/add-from​/{sourceListId}`, where the `sourceListId` is the list you're retrieving the records from. 

### View records in an existing list[](https://developers.hubspot.com/docs/api/crm/lists#view-records-in-an-existing-list)

To view all records in an existing list, make a `GET` request to `/v3/lists/{listId}/memberships`. This returns all members of a list ordered by `recordId`.

### Delete records from an existing list[](https://developers.hubspot.com/docs/api/crm/lists#delete-records-from-an-existing-list)

To remove all records from an existing list, make a `DELETE` request to `/v3/lists/{listId}/memberships`. This will not delete the list from your account. 

To remove specific records from an existing list, make a `PUT` request to `/v3/lists/{listId}/memberships/remove` with a list of `recordID`s in the request body. 

Migrate from v1 to v3 API endpoints[](https://developers.hubspot.com/docs/api/crm/lists#migrate-from-v1-to-v3-api-endpoints)
----------------------------------------------------------------------------------------------------------------------------

If you were previously using any of the v1 list endpoints, you can migrate over to the equivalent endpoints detailed in the sections below. 

### Get static lists[](https://developers.hubspot.com/docs/api/crm/lists#get-static-lists)

To get a static list, make a `POST` request to `/crm/v3/lists/search` and include `SNAPSHOT` and `MANUAL` within an array provided as the `processingTypes` parameter in your request body. 

// Example request body for POST request to /crm/v3/lists/search { "additionalProperties": \[ "hs\_is\_public", "hs\_is\_read\_only", "hs\_is\_limit\_exempt", "hs\_all\_team\_ids", "hs\_folder\_id", "hs\_folder\_name" \], "offset": 0, "processingTypes": \["MANUAL", "SNAPSHOT"\] }

### Get dynamic lists[](https://developers.hubspot.com/docs/api/crm/lists#get-dynamic-lists)

To get a dynamic list, make a `POST` request to `/crm/v3/lists/search` and include `DYNAMIC` within an array provided as the processingTypes parameter in your request body. 

// Example request body for POST request to /crm/v3/lists/search { "additionalProperties": \[ "hs\_is\_public", "hs\_is\_read\_only", "hs\_is\_limit\_exempt", "hs\_all\_team\_ids", "hs\_folder\_id", "hs\_folder\_name" \], "offset": 0, "processingTypes": \["DYNAMIC"\] }

### Get a batch of lists by list ID[](https://developers.hubspot.com/docs/api/crm/lists#get-a-batch-of-lists-by-list-id)

To get a batch of lists by the listIds, make a `POST` request to `/crm/v3/lists/search`. In the request, include the desired list IDs in the `listIds` parameter and specify any additional properties. The response will not include any filter branches.

// Example request body for POST request to /crm/v3/lists/search { "additionalProperties": \[ "hs\_is\_public", "hs\_is\_read\_only", "hs\_is\_limit\_exempt", "hs\_all\_team\_ids", "hs\_folder\_id", "hs\_folder\_name" \], "offset": 0, "listIds": \["42", "51"\] }

To include filters in your response, make a `GET` request to `/crm/v3/lists`. In the request, append the query parameters `includeListFilters=true` and the desired list IDs as the `listIds` parameter. E.g. `/crm/v3/lists?includeFilters=true&listIds=42&listIds=51`

### Get recent list members with properties[](https://developers.hubspot.com/docs/api/crm/lists#get-recent-list-members-with-properties)

First, make a `GET` request to  `/crm/v3/lists/{listId}/memberships/join-order` to get the record IDs of the list members. Then, make a `POST` request to `/crm/v3/objects/{object}/search` for the specific `objectTypeId` and include the record IDs in the `values` parameter.

// Example request body for POST request to /crm/v3/objects/{object}/search { "properties": \[ "firstname", "lastname", "email" , "hs\_object\_id", "createdate", "lastmodifieddate", "hs\_all\_accessible\_team\_ids" \], "filterGroups": \[ { "filters": \[ { "propertyName": "hs\_object\_id", "operator": "IN", "values": \["808431983", "802539655", "101"\] } \] } \] }

### Get all/recently modified records with properties[](https://developers.hubspot.com/docs/api/crm/lists#get-all-recently-modified-records-with-properties)

Use the CRM search endpoint to search for records in your HubSpot account. To get all records, make a `POST` request to `/crm/v3/objects/{object}/search` with the object you want to search for. 

// Example POST request to /crm/v3/objects/contacts/search { "properties": \[ "firstname", "lastname", "email" , "hs\_object\_id", "createdate", "lastmodifieddate", "hs\_all\_accessible\_team\_ids" \] }

// Example POST request to /crm/v3/objects/deals/search { "properties": \[ "hs\_object\_id", "createdate", "dealstage", "lastmodifieddate" \] }

To get recently modified records, make a `POST` request to `/crm/v3/objects/{object}/search` and filter by `lastmodifieddate`. 

// Example POST request to /crm/v3/objects/contacts/search { "properties": \[ "firstname", "lastname", "email" , "hs\_object\_id", "createdate", "lastmodifieddate" \], "filterGroups": \[ { "filters": \[ { "propertyName": "lastmodifieddate", "operator": "GT", "value": "2024-02-22" } \] } \] }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/lists#page-feedback)
--------------------------------------------------------------------------------------

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