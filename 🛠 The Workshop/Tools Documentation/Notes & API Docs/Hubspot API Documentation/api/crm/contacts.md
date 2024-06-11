---
title: "Contacts in HubSpot CRM"
description: "Contacts store information about the individual people that interact with your business, allowing you to create and manage contact records in your HubSpot account, as well as sync contact data between HubSpot and other systems."
type: "group"
tags:
- "CRM"
- "HubSpot"
- "Contacts Management"
relationships:
- "#part_of [[Customer Relationship Management]]"
- "#related_to [[Data Syncing]]"
founded: "N/A"
---

Contacts
========

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, contacts store information about the individual people that interact with your business. The contacts endpoints allow you to create and manage contact records in your HubSpot account, as well as sync contact data between HubSpot and other systems.

Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs-beta/crm/understanding-the-crm?_ga=2.21847609.341006870.1586180142-500942594.1573763828) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](//knowledge.hubspot.com/contacts-user-guide?utm_campaign=UserGuides&utm_source=Developers&_ga=2.22901305.341006870.1586180142-500942594.1573763828).

Create contacts[](https://developers.hubspot.com/docs/api/crm/contacts#create-contacts)
---------------------------------------------------------------------------------------

To create new contacts, make a `POST` request to `/crm/v3/objects/contacts`.

In your request, include your contact data in a properties object. You can also add an associations object to associate your new contact with existing records (e.g., companies, deals), or activities (e.g., meetings, notes).

### Properties[](https://developers.hubspot.com/docs/api/crm/contacts#properties)

Contact details are stored in contact properties. There are [default HubSpot contact properties](https://knowledge.hubspot.com/articles/kcs_article/contacts/hubspots-default-contact-properties?_ga=2.135700019.341006870.1586180142-500942594.1573763828), but you can also [create custom contact properties](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.135700019.341006870.1586180142-500942594.1573763828#create-custom-properties).

When creating a new contact, you should include at least one of the following properties in your request: `email`, `firstname`, or `lastname`. It is recommended to always include `email`, because email address is the [primary unique identifier](https://knowledge.hubspot.com/crm-setup/deduplication-of-contacts-companies-deals-tickets#automatic-deduplication-in-hubspot)  to avoid duplicate contacts in HubSpot.

To view all available properties, you can retrieve a list of your account's contact properties by making a `GET` request to `/crm/v3/properties/contacts`. Learn more about the the [properties API](/docs/api/crm/properties).

**Please note**: if you've included `lifecyclestage` in your request, values must refer to the lifecycle stage's internal name. The internal names of default stages are text values, and do not change even if you edit the stage's [label](https://knowledge.hubspot.com/crm-setup/manage-your-properties#:~:text=the%20properties%20settings.-,Label/Name%3A,-enter%20a%20unique)(e.g., `subscriber` or `marketingqualifiedlead`). The internal names of [custom stages](https://knowledge.hubspot.com/crm-setup/create-and-customize-lifecycle-stages)are numeric values. You can find a stage's internal ID in your [lifecycle stage settings,](https://knowledge.hubspot.com/crm-setup/create-and-customize-lifecycle-stages#:~:text=To%20edit%20a%20lifecycle%20stage%2C%20hover%20over%20the%20stage%20and%20click%20Edit.%20In%20the%20right%20panel%2C%20edit%20the%20Stage%20name%2C%20then%20click%20Edit%20lifecycle%20stage%20to%20confirm.%20Click%20the%20code%20codcode%20icon%20to%20view%20the%20stage%27s%20internal%20ID%2C%20which%20is%20used%20by%20integrations%20and%20APIs.)or by retrieving the lifecycle stage property via API.

For example, to create a new contact, your request may look similar to the following:

///Example request body { "properties": { "email": "example@hubspot.com", "firstname": "Jane", "lastname": "Doe", "phone": "(555) 555-5555", "company": "HubSpot", "website": "hubspot.com", "lifecyclestage": "marketingqualifiedlead" } }

### Associations[](https://developers.hubspot.com/docs/api/crm/contacts#associations)

When creating a new contact, you can also associate the contact with [existing records](https://knowledge.hubspot.com/crm-setup/associate-records) or [activities](https://knowledge.hubspot.com/crm-setup/associate-activities-with-records). In the associations object, include the following fields:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record or activity that you want to associate the contact with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the contact and the other object or activity. Default association types are listed [here](https://developers.hubspot.com/docs/api/crm/associations#association-type-id-values), or you can retrieve the value by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. Learn more about the [associations API](https://developers.hubspot.com/docs/api/crm/associations).

 |

You can also include the `label` field to assign a [defined association label](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) that describes the association. Learn more about associating records via the [associations API](https://developers.hubspot.com/docs/api/crm/associations).

For example, to associate a new contact with an existing company and email, your request would look like the following:

///Example request body { "properties": { "email": "example@hubspot.com", "firstname": "Jane", "lastname": "Doe", "phone": "(555) 555-5555", "company": "HubSpot", "website": "hubspot.com", "lifecyclestage": "marketingqualifiedlead" }, "associations": \[ { "to": { "id": 123456 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 279 } \] }, { "to": { "id": 556677 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 197 } \] }\] }

Retrieve contacts[](https://developers.hubspot.com/docs/api/crm/contacts#retrieve-contacts)
-------------------------------------------------------------------------------------------

You can retrieve contacts individually or in batches.

*   To retrieve an individual contact, make a `GET` request to `/crm/v3/objects/contacts/{contactId}`. 
*   To request a list of all contacts, make a `GET` request to `/crm/v3/objects/contacts`.

For these endpoints, you can include the following query parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If the requested contact doesn't have a value for a property, it will not appear in the response.

 |
| 

`propertiesWithHistory`

 | 

A comma separated list of the current and historical properties to be returned in the response. If the requested contact doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of objects to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](https://developers.hubspot.com/docs/api/crm/associations)

 |

*   To retrieve a batch of specific contacts by record ID, email address, or a [custom unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties), make a `POST` request to `crm/v3/objects/contacts/batch/read`. The batch endpoint cannot retrieve associations. Learn how to batch read associations with the [associations API](/docs/api/crm/associations).

For the batch read endpoint, you can use the optional `idProperty` parameter to retrieve contacts by `email` or a custom [unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID (`hs_object_id`), so the `idProperty` parameter is not required when retrieving by record ID. If you're using `email` or a custom unique value property to retrieve contacts, you must include the `idProperty` parameter.  

For example, to retrieve a batch of contacts based on their record ID values, your request could look like the following (current values only, or current and historical values):

///Example request body with record ID (current values) { "properties": \[ "email", "lifecyclestage", "jobtitle" \], "inputs": \[ { "id": "1234567" }, { "id": "987456" } \] }

///Example request body with record ID (current and historical values) { "propertiesWithHistory": \[ "lifecyclestage", "hs\_lead\_status" \], "inputs": \[ { "id": "1234567" }, { "id": "987456" } \] }

To retrieve contacts based on email address or a custom unique identifier property (e.g., a customer ID number unique for your business), your request would look like:

///Example request body with email { "properties": \[ "email", "lifecyclestage", "jobtitle" \], "idProperty": "email", "inputs": \[ { "id": "lgilmore@thedragonfly.com" }, { "id": "sstjames@thedragonfly.com" } \] }

///Example request body with a unique value property { "properties": \[ "email", "lifecyclestage", "jobtitle" \], "idProperty": "internalcustomerid", "inputs": \[ { "id": "12345" }, { "id": "67891" } \] }

Update contacts[](https://developers.hubspot.com/docs/api/crm/contacts#update-contacts)
---------------------------------------------------------------------------------------

You can update contacts individually or in batches. For existing contacts, email and record ID are both unique values, so you can use `id` or `email` to update contacts via API.

To update an individual contact by its contact ID, make a `PATCH` request to `/crm/v3/objects/contacts/{contactId}`, and include the data you want to update.

### Associate existing contacts with records or activities[](https://developers.hubspot.com/docs/api/crm/contacts#associate-existing-contacts-with-records-or-activities)

To associate a contact with other CRM records or an activity, make a `PUT` request to  `/crm/v3/objects/contacts/{contactId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

To retrieve the `associationTypeId` value, refer to [this list](https://developers.hubspot.com/docs/api/crm/associations#association-type-id-values) of default values, or make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. 

Learn more about the [associations API.](/docs/api/crm/associations)

### Remove an association[](https://developers.hubspot.com/docs/api/crm/contacts#remove-an-association)

To remove an association between a contact and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/contacts/{contactID}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

Pin an activity on a contact record[](https://developers.hubspot.com/docs/api/crm/contacts#pin-an-activity-on-a-contact-record)
-------------------------------------------------------------------------------------------------------------------------------

You can [pin an activity](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a contact record by including the `hs_pinned_engagement_id` field in your request. In the field, include the `id` of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api/crm/engagements). You can pin one activity per record, and the activity must already be associated with the contact prior to pinning.

To set or update a contact's pinned activity, your request could look like:

///Example request body PATCH /crm/v3/objects/contacts/{contactId} { "properties": { "hs\_pinned\_engagement\_id": 123456789 } }

You can also create a contact, associate it with an existing activity, and pin the activity in the same request. For example:

///Example request body POST /crm/v3/objects/contacts { "properties": { "email": "example@hubspot.com", "firstname": "Jane", "lastname": "Doe", "phone": "(555) 555-5555", "hs\_pinned\_engagement\_id": 123456789 }, "associations": \[ { "to": { "id": 123456789 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 201 }\] }\] }

Delete contacts[](https://developers.hubspot.com/docs/api/crm/contacts#delete-contacts)
---------------------------------------------------------------------------------------

You can delete contacts individually or in batches, which will add the contact to the recycling bin in HubSpot. You can later [restore the contact within HubSpot](https://knowledge.hubspot.com/contacts/restore-deleted-contacts-companies-deals-or-tickets).

To delete an individual contact by its ID, make a `DELETE` request to `/crm/v3/objects/contacts/{contactId}`.

Learn more about batch deleting contacts on the _Endpoints_ tab at the top of this article.

Limits[](https://developers.hubspot.com/docs/api/crm/contacts#limits)
---------------------------------------------------------------------

Batch operations for creating, updating, and archiving are limited to batches of 100. There are also limits for [contacts and form submissions](/docs/api/faq#limits_contacts).

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/contacts#page-feedback)
-----------------------------------------------------------------------------------------

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