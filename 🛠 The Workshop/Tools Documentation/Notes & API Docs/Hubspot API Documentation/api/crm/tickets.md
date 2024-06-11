---
title: "Tickets in HubSpot CRM"
description: "Customer requests for help tracked through support process until closed, manage ticket records and sync data between HubSpot and other systems."
type: "group"
tags:
- "Customer Support"
- "CRM"
- "HubSpot"
relationships:
- "#part_of [[CRM]]"
- "#related_to [[Support Process]]"
founded: "N/A"
---

Tickets
=======

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, tickets represents customer requests for help. Tickets are tracked through your support process in [pipeline statuses](https://knowledge.hubspot.com/tickets/customize-ticket-pipelines-and-statuses) until they're closed. The tickets endpoints allow you to manage create and manage ticket records, as well as sync ticket data between HubSpot and other systems. 

Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs-beta/crm/understanding-the-crm?_ga=2.21847609.341006870.1586180142-500942594.1573763828) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.22901305.341006870.1586180142-500942594.1573763828)[.](//knowledge.hubspot.com/contacts-user-guide?utm_campaign=UserGuides&utm_source=Developers)

Create tickets[](https://developers.hubspot.com/docs/api/crm/tickets#create-tickets)
------------------------------------------------------------------------------------

To create new tickets, make a `POST` request to `/crm/v3/objects/tickets`.

In your request, include your ticket data in a properties object. You can also add an associations object to associate your new ticket with existing records (e.g., contacts, companies), or activities (e.g., meetings, notes).

### Properties[](https://developers.hubspot.com/docs/api/crm/tickets#properties)

Ticket details are stored in ticket properties. There are [default HubSpot ticket properties](https://knowledge.hubspot.com/tickets/hubspots-default-ticket-properties), but you can also [create custom properties](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.135700019.341006870.1586180142-500942594.1573763828#create-custom-properties).

When creating a new ticket, you should include the following properties in your request: `subject` (the ticket's name), `hs_pipeline_stage` (the ticket's status) and if you have multiple pipelines, `hs_pipeline`. If a pipeline isn't specified, the default pipeline will be used.

To view all available properties, you can retrieve a list of your account's ticket properties by making a `GET` request to `/crm/v3/properties/tickets`. Learn more about the the [properties API](/docs/api/crm/properties).

**Please note**: you must use the internal ID of a ticket status or pipeline when creating a ticket via the API. The internal ID is a number, which will also be returned when you retrieve tickets via the API. You can find a ticket status or pipeline's internal ID in your [ticket pipeline settings.](https://knowledge.hubspot.com/tickets/customize-ticket-pipelines-and-statuses)

For example, to create a new ticket, your request may look similar to the following:

///Example request body { "properties": { "hs\_pipeline": "0", "hs\_pipeline\_stage": "1", "hs\_ticket\_priority": "HIGH", "subject": "troubleshoot report" } }

### Associations[](https://developers.hubspot.com/docs/api/crm/tickets#associations)

When creating a new ticket, you can also associate the ticket with [existing records](https://knowledge.hubspot.com/crm-setup/associate-records) or [activities](https://knowledge.hubspot.com/crm-setup/associate-activities-with-records). In the associations object, include the following fields:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record or activity that you want to associate the ticket with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the ticket and the other object or activity. Default association types are listed [here](https://developers.hubspot.com/docs/api/crm/associations#association-type-id-values), or you can retrieve the value by making by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. Learn more about the [associations API](/docs/api/crm/associations).

 |

You can also include the `label` field to assign a [defined association label](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) that describes the association. Learn more about associating records via the [associations API](/docs/api/crm/associations).

For example, to associate a new ticket with an existing contact and company, your request would look like the following:

///Example request body { "properties": { "hs\_pipeline": "0", "hs\_pipeline\_stage": "1", "hs\_ticket\_priority": "HIGH", "subject": "troubleshoot report" }, "associations": \[ { "to": { "id": 201 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 16 } \] }, { "to": { "id": 301 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 26 } \] }\] }

Retrieve tickets[](https://developers.hubspot.com/docs/api/crm/tickets#retrieve-tickets)
----------------------------------------------------------------------------------------

You can retrieve tickets individually or in batches.

*   To retrieve an individual ticket, make a `GET` request to `/crm/v3/objects/tickets/{ticketId}`.
*   To request a list of all tickets, make a `GET` request to `/crm/v3/objects/tickets`.

For these endpoints, you can include the following query parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If the requested ticket doesn't have a value for a property, it will not appear in the response.

 |
| 

`propertiesWithHistory`

 | 

A comma separated list of the current and historical properties to be returned in the response. If the requested ticket doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of objects to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](https://developers.hubspot.com/docs/api/crm/associations)

 |

*   To retrieve a batch of specific tickets by record ID or a [custom unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties), make a `POST` request to `crm/v3/objects/tickets/batch/read`. The batch endpoint cannot retrieve associations. Learn how to batch read associations with the [associations API](/docs/api/crm/associations).

For the batch read endpoint, you can also use the optional `idProperty` parameter to retrieve tickets by a custom [unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID (`hs_object_id`), so the `idProperty` parameter is not required when retrieving by record ID. To use a custom unique value property to retrieve tickets, you must include the `idProperty` parameter.

For example, to retrieve a batch of tickets, your request could look like either of the following:

///Example request body with record ID { "properties": \[ "subject", "hs\_pipeline\_stage", "hs\_pipeline" \], "inputs": \[ { "id": "4444888856" }, { "id": "666699988" } \] }

///Example request body with a unique value property { "properties": \[ "subject", "hs\_pipeline\_stage", "hs\_pipeline" \], "idProperty": "uniquepropertyexample", "inputs": \[ { "id": "abc" }, { "id": "def" } \] }

To retrieve tickets with current and historical values for a property, your request could look like:

///Example request body with record ID (current and historical values) { "propertiesWithHistory": \[ "hs\_pipeline\_stage" \], "inputs": \[ { "id": "4444888856" }, { "id": "666699988" } \] }

Update tickets[](https://developers.hubspot.com/docs/api/crm/tickets#update-tickets)
------------------------------------------------------------------------------------

You can update tickets individually or in batches. For existing tickets, the ticket ID is a unique value that you can use to update the ticket via API.

To update an individual ticket by its ticket ID, make a `PATCH` request to `/crm/v3/objects/tickets/{ticketId}`, and include the data you want to update.

### Associate existing tickets with records or activities[](https://developers.hubspot.com/docs/api/crm/tickets#associate-existing-tickets-with-records-or-activities)

To associate a ticket with other CRM records or an activity, make a `PUT` request to  `/crm/v3/objects/tickets/{ticketId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

To retrieve the `associationTypeId` value, refer to [this list](https://developers.hubspot.com/docs/api/crm/associations#association-type-id-values) of default values, or make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. 

Learn more about the [associations API.](/docs/api/crm/associations)

### Remove an association[](https://developers.hubspot.com/docs/api/crm/tickets#remove-an-association)

To remove an association between a ticket and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/tickets/{ticketId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

Pin an activity on a ticket record[](https://developers.hubspot.com/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record)
----------------------------------------------------------------------------------------------------------------------------

**Please note:** pinning activities to ticket records via API requires OAuth authentication through a public app. Private apps cannot be used for pinning activities to ticket records.

You can pin an activity on a ticket record via API by including the `hs_pinned_engagement_id` field in your request. In the field, include the `id` of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api/crm/engagements). You can pin one activity per record, and the activity must already be associated with the ticket prior to pinning.

To set or update a ticket's pinned activity, your request could look like:

///Example request body PATCH /crm/v3/objects/tickets/{ticketId} { "properties": { "hs\_pinned\_engagement\_id": 123456789 } }

You can also create a ticket, associate it with an existing activity, and pin the activity in the same request. For example:

///Example request body POST /crm/v3/objects/tickets { "properties": { "hs\_pipeline": "0", "hs\_pipeline\_stage": "1", "hs\_ticket\_priority": "HIGH", "subject": "troubleshoot report", "hs\_pinned\_engagement\_id": 123456789 }, "associations": \[ { "to": { "id": 123456789 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 227 }\] }\] }

Delete tickets[](https://developers.hubspot.com/docs/api/crm/tickets#delete-tickets)
------------------------------------------------------------------------------------

You can delete tickets individually or in batches, which will add the ticket to the recycling bin in HubSpot. You can later [restore the ticket within HubSpot](https://knowledge.hubspot.com/contacts/restore-deleted-contacts-companies-deals-or-tickets).

To delete an individual ticket by its ID, make a `DELETE` request to `/crm/v3/objects/tickets/{ticketId}`.

Learn more about batch deleting tickets on the _Endpoints_ tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/tickets#page-feedback)
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