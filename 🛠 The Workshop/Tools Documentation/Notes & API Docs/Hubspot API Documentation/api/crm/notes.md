---
title: "CRM Notes Management in HubSpot API"
description: "A guide on creating, retrieving, updating, associating, pinning, and deleting notes within the HubSpot CRM system using its API."
type: "group"
tags:
- "CRM"
- "HubSpot"
- "API"
- "Notes Management"
relationships:
- "#created_by [[User]]"
- "#associated_with [[Contacts]], [[Companies]], [[Deals]], [[Tickets]], [[Custom Objects]]"
founded: "2014-03-05"
---

Notes
=====

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

You can log notes on CRM records to add information to the record timeline or associate an attachment with a record. For example, if you need to keep track of an offline conversation you had with a contact, you can add a note to their contact record with details and documents related to the conversation. Other users in the account will then be able to view and reference that note.

You can manage notes either [in HubSpot](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or through the notes API. Below, learn the basic methods of managing notes through the API. You can review all available endpoints on the _Endpoints_ tab at the top of this article.

Create a note
-------------

To create a note, make a `POST` request to `/crm/v3/objects/notes`.

In the request body, add note details in a properties object. You can also add an associations object to associate your new note with an existing record (e.g., contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/notes#properties)

In the properties object, you can include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_timestamp`

 | 

Required. This field marks the note's time of creation and determines where the note sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 

 |
| 

`hs_note_body`

 | 

The note's text content, limited to 65,536 characters.

 |
| 

`hubspot_owner_id`

 | 

The [ID of the owner](/docs/api/crm/owners) associated with the note. This field determines the user listed as the note creator on the record timeline in HubSpot.

 |
| 

`hs_attachment_ids`

 | 

The IDs of the note's attachments. Multiple attachment IDs are separated by a semi-colon.

 |

### Associations[](https://developers.hubspot.com/docs/api/crm/notes#associations)

To create and associate a note with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the note with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the note and the other object. You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, to create a note and associate it with a company and deal, your request body might look similar to the following:

// Example POST request to https://api.hubspot.com/crm/v3/objects/notes { "properties": { "hs\_timestamp": "2021-11-12T15:48:22Z", "hs\_note\_body": "Spoke with decision maker Carla. Attached the proposal and draft of contract.", "hubspot\_owner\_id": "14240720", "hs\_attachment\_ids": "24332474034;24332474044" }, "associations": \[ { "to": { "id": 301 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 190 } \] }, { "to": { "id": 401 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 214 } \] }\] }

Learn more about batch creating notes on the _Endpoints_ tab at the top of this article.

Retrieve notes[](https://developers.hubspot.com/docs/api/crm/notes#retrieve-notes)
----------------------------------------------------------------------------------

You can retrieve notes individually or in batches. To retrieve an individual note, make a `GET` request to `/crm/v3/objects/notes/{noteId}`.

To request a list of all notes, make a `GET` request to `/crm/v3/objects/notes`.

For both endpoints, you can include the following query parameters in the request URL:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If the requested note doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of object types to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](/docs/api/crm/associations)

 |

For example, to retrieve notes with their text content and any associated contact IDs, your request URL might look similar to the following:

`https://api.hubapi.com/crm/v3/objects/notes?limit=10&properties=hs_note_body&associations=contact&archived=false&hapikey=YOUR_HUBSPOT_API_KEY`.

Learn more about retrieving a batch of notes by internal ID or unique property value on the _Endpoints_ tab at the top of this article.

Update notes[](https://developers.hubspot.com/docs/api/crm/notes#update-notes)
------------------------------------------------------------------------------

You can update notes individually or in batches. To update an individual note by its note ID, make a `PATCH` request to `/crm/v3/objects/notes/{noteId}`. 

In the request body, include the note properties that you want to update:

// Example PATCH request to https://api.hubspot.com/crm/v3/objects/notes/{noteID} { "properties": { "hs\_note\_body": "Spoke with decision maker Carla.", "hs\_attachment\_ids": "24332474034;24332474044" } }

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating notes on the _Endpoints_ tab at the top of this article.

### Associate existing notes with records[](https://developers.hubspot.com/docs/api/crm/notes#associate-existing-notes-with-records)

To associate a note with other CRM records, such as a contact, make a `PUT` request to `/crm/v3/objects/notes/{noteId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL contains the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`noteId`

 | 

The ID of the note.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the note with (e.g., contact or company)

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the note with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the note and the other object. The ID can be represented numerically or in snake case (e.g., `note_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubspot.com/crm/v3/objects/notes/17147287858/associations/contact/581751/202`

### Remove an association

To remove an association between a note and a record, make a `DELETE` request to the same URL as above:

`/crm/v3/objects/notes/{noteId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin a note on a record[](https://developers.hubspot.com/docs/api/crm/notes#pin-a-note-on-a-record)
--------------------------------------------------------------------------------------------------

You can [pin a note](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The note must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin a note, include the note's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete notes[](https://developers.hubspot.com/docs/api/crm/notes#delete-notes)
------------------------------------------------------------------------------

You can delete notes individually or in batches, which will add the note to the recycling bin in HubSpot. You can later [restore the note from the record timeline](https://knowledge.hubspot.com/crm-setup/restore-deleted-activity-in-a-record).

To delete an individual note by its note ID, make a `DELETE` request to `/crm/v3/objects/notes/{noteId}`.

Learn more about batch deleting notes on the _Endpoints_ tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/notes#page-feedback)
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