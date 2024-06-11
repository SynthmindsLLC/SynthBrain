---
title: "Communications"
description: "Logging external communications via WhatsApp, LinkedIn, or SMS messages on CRM records to add information about the message to the record timeline."
type: "group"
tags:
- "CRM"
- "Communication"
- "Messaging"
relationships:
- "#part_of [[HubSpot]]"
- "#related_to [[WhatsApp]], [[LinkedIn]], [[SMS Messages]]"
founded: "N/A"
---

Communications
==============

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

You can log external communications via WhatsApp, LinkedIn, or SMS messages on CRM records to add information about the message to the record timeline. 

You can [log a message directly in your HubSpot account](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or using the API endpoints below. You can review all available endpoints on the **_Endpoints_** tab at the top of this article.

**Please note**: the Communications API does not apply to marketing SMS messages. Learn how to create and view [marketing SMS messages in HubSpot](https://knowledge.hubspot.com/sms/create-and-send-sms-messages).

Create a WhatsApp, LinkedIn, or SMS message
-------------------------------------------

To create a message, make a `POST` request to `/crm/v3/objects/communications`.

In the request body, add message details in a properties object. You can also add an associations object to associate your new message with an existing record (e.g., contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/communications#properties)

In the properties object, you can include the following fields:

| Field | Description |
| --- | --- |
| `hs_communication_channel_type` | The channel type of the message that you sent or received from the contact. Supported values are `WHATS_APP`, `LINKEDIN_MESSAGE`, or `SMS`. |
| `hs_communication_logged_from` | Enum used to differentiate between conversations objects. This must be set to `CRM` in your request. |
| `hs_communication_body` | The text body of the engagement. |
| `hs_timestamp` | This field marks the message's time of creation and determines where the message appears on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. |

### Associations[](https://developers.hubspot.com/docs/api/crm/communications#associations)

To create and associate a postal mail engagement with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the message with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the message and the other object. The ID can be represented numerically or in snake case (e.g., `communication_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, if you want to log an SMS message and associate it with a contact and company, your request body might resemble the following:

// Example POST request to https://api.hubapi.com/crm/v3/objects/communications { "properties": { "hs\_communication\_channel\_type": "SMS", "hs\_communication\_logged\_from": "CRM", "hs\_communication\_body": "Texted Linda to confirm that we're ready to move forward with the contract.", "hs\_timestamp": "2022-11-12T15:48:22Z" }, "associations": \[ { "to": { "id": 9001 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 87 } \] }, { "to": { "id": 1234 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 81 } \] }\] }

The response to your request will include an ID that you can use to update or associate the message with a record:

// Example response from POST request to https://api.hubapi.com/crm/v3/objects/communications { "id": '12021896773', "properties": { "hs\_communication\_channel\_type": "SMS ", "hs\_communication\_logged\_from": "CRM", "hs\_communication\_body": "Texted John to confirm that we're ready to move forward with the contract.", "hs\_timestamp": "2022-11-12T15:48:22Z", "hs\_createdate": '2022-11-29T18:35:00.484Z', "hs\_lastmodifieddate": '2022-11-29T18:35:00.484Z', "hs\_object\_id": '12021896773', }, "createdAt": '2022-11-29T18:35:00.484Z', "updatedAt": '2022-11-29T18:35:00.484Z', "archived": false }

Retrieve messages[](https://developers.hubspot.com/docs/api/crm/communications#retrieve-messages)
-------------------------------------------------------------------------------------------------

You can retrieve messages individually or in batches. To retrieve an individual messages, make a `GET` request to `/crm/v3/objects/communication/{communicationId}`.

To request a list of all of logged WhatsApp, LinkedIn, and SMS messages, make a `GET` request to `/crm/v3/objects/communications`.

For both endpoints, you can include the following query parameters in the request URL:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If the requested message doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of object types to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](/docs/api/crm/associations)

 |

For example, to retrieve messages with their text content and any associated contact IDs, your request URL might look similar to the following:

`https://api.hubapi.com/crm/v3/objects/communications?limit=10&properties=hs_communication_body&associations=contact&archived=false`.

Learn more about retrieving a batch of messages by internal ID or unique property value on the **_Endpoints_** tab at the top of this article.

Update messages[](https://developers.hubspot.com/docs/api/crm/communications#update-messages)
---------------------------------------------------------------------------------------------

You can update messages individually or in batches. To update an individual message by its communication ID, make a `PATCH` request to `/crm/v3/objects/communications/{communicationId}`. 

In the request body, include the message properties that you want to update:

// Example PATCH request to https://api.hubapi.com/crm/v3/objects/communications/{communicationId} { "properties": { "hs\_communication\_body": "Sent a follow-up message to Carla." } }

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating messages on the **_Endpoints_** tab at the top of this article.

### Associate an existing message with a record[](https://developers.hubspot.com/docs/api/crm/communications#associate-an-existing-message-with-a-record)

To associate a message with other CRM records, such as a contact, make a `PUT` request to `/crm/v3/objects/communications/{communicationId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL contains the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`communicationId`

 | 

The ID of your WhatsApp, LinkedIn, or SMS message.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the message with (e.g., contact or company)

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the message with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the message and the other object. The ID can be represented numerically or in snake case (e.g., `communication_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubapi.com/crm/v3/objects/communications/12021896773/associations/contact/581751/communication_to_contact`

### Remove an association

To remove an association between a message and a record, make a `DELETE` request to the same URL as above:

`/crm/v3/objects/communications/{communicationId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin a message on a record[](https://developers.hubspot.com/docs/api/crm/communications#pin-a-message-on-a-record)
-----------------------------------------------------------------------------------------------------------------

You can [pin a message](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The message must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin a message, include the message's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete messages[](https://developers.hubspot.com/docs/api/crm/communications#delete-messages)
---------------------------------------------------------------------------------------------

You can delete messages individually or in batches, which will add the message to the recycling bin in HubSpot. You can later [restore the message from the record timeline](https://knowledge.hubspot.com/crm-setup/restore-deleted-activity-in-a-record).

To delete an individual message by its ID, make a `DELETE` request to `/crm/v3/objects/communications/{communicationId}`.

Learn more about batch deleting messages on the **_Endpoints_** tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/communications#page-feedback)
-----------------------------------------------------------------------------------------------

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