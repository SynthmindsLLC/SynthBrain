---
title: "Deals in HubSpot CRM"
description: "Transactions with contacts or companies tracked through the sales process until won or lost, managed and synced via deals endpoints."
type: "group"
tags:
- "CRM"
- "Sales Process"
- "HubSpot"
relationships:
- "#part_of [[Pipeline Stages]]"
- "#managed_by [[HubSpot CRM]]"
founded: "N/A"
---

Deals
=====

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, deals represent transactions with contacts or companies. Deals are tracked through your sales process in [pipeline stages](https://knowledge.hubspot.com/crm-deals/set-up-and-customize-your-deal-pipelines-and-deal-stages) until they're won or lost. The deals endpoints allow you to manage create and manage deal records, as well as sync deal data between HubSpot and other systems. 

Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs-beta/crm/understanding-the-crm?_ga=2.21847609.341006870.1586180142-500942594.1573763828) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.22901305.341006870.1586180142-500942594.1573763828)[.](//knowledge.hubspot.com/contacts-user-guide?utm_campaign=UserGuides&utm_source=Developers)

Create deals[](https://developers.hubspot.com/docs/api/crm/deals#create-deals)
------------------------------------------------------------------------------

To create new deals, make a `POST` request to `/crm/v3/objects/deals`.

In your request, include your deal data in a properties object. You can also add an associations object to associate your new deal with existing records (e.g., contacts, companies), or activities (e.g., meetings, notes).

### Properties[](https://developers.hubspot.com/docs/api/crm/deals#properties)

Deal details are stored in deal properties. There are [default HubSpot deal properties](https://knowledge.hubspot.com/crm-deals/hubspots-default-deal-properties), but you can also [create custom properties](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.135700019.341006870.1586180142-500942594.1573763828#create-custom-properties).

When creating a new deal, you should include the following properties in your request: `dealname`, `dealstage` and if you have multiple pipelines, `pipeline`. If a pipeline isn't specified, the default pipeline will be used. 

To view all available properties, you can retrieve a list of your account's deal properties by making a `GET` request to `/crm/v3/properties/deals`. Learn more about the the [properties API](/docs/api/crm/properties).

**Please note**: you must use the internal ID of a deal stage or pipeline when creating a deal via the API. The internal ID will also be returned when you retrieve deals via the API. You can find a deal stage's or pipeline's internal ID in your [deal pipeline settings.](https://knowledge.hubspot.com/crm-deals/set-up-and-customize-your-deal-pipelines-and-deal-stages#to-customize-your-deal-stages:~:text=To%20view%20the%20internal%20name%20for%20a%20deal%20stage%2C%20hover%20over%20the%20stage%20and%20click%20the%20code%20code%20icon.%20The%20internal%20name%20is%20used%20by%20integrations%20and%20the%20API.)

For example, to create a new deal, your request may look similar to the following:

///Example request body { "properties": { "amount": "1500.00", "closedate": "2019-12-07T16:50:06.678Z", "dealname": "New deal", "pipeline": "default", "dealstage": "contractsent", "hubspot\_owner\_id": "910901" } }

### Associations[](https://developers.hubspot.com/docs/api/crm/deals#associations)

When creating a new deal, you can also associate the deal with [existing records](https://knowledge.hubspot.com/crm-setup/associate-records) or [activities](https://knowledge.hubspot.com/crm-setup/associate-activities-with-records). In the associations object, include the following fields:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record or activity that you want to associate the deal with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the deal and the other object or activity. Default association types are listed [here](/docs/api/crm/associations#association-type-id-values), or you can retrieve the value by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. Learn more about the [associations API](/docs/api/crm/associations).

 |

You can also include the `label` field to assign a [defined association label](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) that describes the association. Learn more about associating records via the [associations API](/docs/api/crm/associations).

For example, to associate a new deal with an existing contact and company, your request would look like the following:

///Example request body { "properties": { "amount": "1500.00", "closedate": "2019-12-07T16:50:06.678Z", "dealname": "New deal", "pipeline": "default", "dealstage": "contractsent", "hubspot\_owner\_id": "910901" }, "associations": \[ { "to": { "id": 201 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 5 } \] }, { "to": { "id": 301 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 3 } \] }\] }

Retrieve deals[](https://developers.hubspot.com/docs/api/crm/deals#retrieve-deals)
----------------------------------------------------------------------------------

You can retrieve deals individually or in batches.

*   To retrieve an individual deal, make a `GET` request to `/crm/v3/objects/deals/{dealId}`.
*   To request a list of all deals, make a `GET` request to `/crm/v3/objects/deals`.

For these endpoints, you can include the following query parameters in the request URL:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | A comma separated list of the properties to be returned in the response. If the requested deal doesn't have a value for a property, it will not appear in the response. |
| 

`propertiesWithHistory`

 | 

A comma separated list of the current and historical properties to be returned in the response. If the requested deal doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of objects to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](https://developers.hubspot.com/docs/api/crm/associations)

 |

*   To retrieve a batch of specific deals by record ID or a [custom unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties), make a `POST` request to `crm/v3/objects/deals/batch/read`. The batch endpoint cannot retrieve associations. Learn how to batch read associations with the [associations API](/docs/api/crm/associations).

For the batch read endpoint, you can also use the optional `idProperty` parameter to retrieve deals by a custom [unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID (`hs_object_id`), so the `idProperty` parameter is not required when retrieving by record ID. To use a custom unique value property to retrieve deals, you must include the `idProperty` parameter.

For example, to retrieve a batch of deals, your request could look like either of the following:

///Example request body with record ID { "properties": \[ "dealname", "dealstage", "pipeline" \], "inputs": \[ { "id": "7891023" }, { "id": "987654" } \] }

///Example request body with a unique value property { "properties": \[ "dealname", "dealstage", "pipeline" \], "idProperty": "uniqueordernumber", "inputs": \[ { "id": "0001111" }, { "id": "0001112" } \] }

To retrieve deals with current and historical values for a property, your request could look like:

///Example request body with record ID (current and historical values) { "propertiesWithHistory": \[ "dealstage" \], "inputs": \[ { "id": "7891023" }, { "id": "987654" } \] }

Update deals[](https://developers.hubspot.com/docs/api/crm/deals#update-deals)
------------------------------------------------------------------------------

You can update deals individually or in batches. For existing deals, the deal ID is a unique value that you can use to update the deal via API.

To update an individual deal by its deal ID, make a `PATCH` request to `/crm/v3/objects/deals/{dealId}`, and include the data you want to update.

### Associate existing deals with records or activities[](https://developers.hubspot.com/docs/api/crm/deals#associate-existing-deals-with-records-or-activities)

To associate a deal with other CRM records or an activity, make a `PUT` request to  `/crm/v3/objects/deals/{dealId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. 

To retrieve the `associationTypeId` value, refer to [this list](/docs/api/crm/associations#association-type-id-values) of default values, or make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

Learn more about associating records with the [associations API](/docs/api/crm/associations).

### Remove an association[](https://developers.hubspot.com/docs/api/crm/deals#remove-an-association)

To remove an association between a deal and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/deals/{dealId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

Pin an activity on a deal record[](https://developers.hubspot.com/docs/api/crm/deals#pin-an-activity-on-a-deal-record)
----------------------------------------------------------------------------------------------------------------------

You can pin an activity on a deal record via API by including the `hs_pinned_engagement_id` field in your request. In the field, include the `id` of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api/crm/engagements). You can pin one activity per record, and the activity must already be associated with the deal prior to pinning.

To set or update a deal's pinned activity, your request could look like:

///Example request body PATCH /crm/v3/objects/deals/{dealId} { "properties": { "hs\_pinned\_engagement\_id": 123456789 } }

You can also create a deal, associate it with an existing activity, and pin the activity in the same request. For example:

///Example request body POST /crm/v3/objects/deals { "properties": { "dealname": "New deal", "pipelines": "default", "dealstage": "contractsent", "hs\_pinned\_engagement\_id": 123456789 }, "associations": \[ { "to": { "id": 123456789 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 213 }\] }\] }

Delete deals[](https://developers.hubspot.com/docs/api/crm/deals#delete-deals)
------------------------------------------------------------------------------

You can delete deals individually or in batches, which will add the deal to the recycling bin in HubSpot. You can later [restore the deal within HubSpot](https://knowledge.hubspot.com/contacts/restore-deleted-contacts-companies-deals-or-tickets).

To delete an individual deal by its ID, make a `DELETE` request to `/crm/v3/objects/deals/{dealId}`.

Learn more about batch deleting deals on the _Endpoints_ tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/deals#page-feedback)
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