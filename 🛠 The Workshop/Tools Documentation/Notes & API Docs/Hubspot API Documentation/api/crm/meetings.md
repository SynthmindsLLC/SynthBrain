---
title: "Meetings Engagement API"
description: "Use the meetings engagement API to log and manage meetings on CRM records, including creating, retrieving, updating, deleting, associating with existing records, pinning, and batch operations."
type: "group"
tags:
- "CRM"
- "Meetings"
- "HubSpot"
relationships:
- "#used_for [[Logging Meeting Activities]]"
- "#related_to [[Contacts]], [[Companies]], [[Deals]], [[Tickets]], [[Custom Objects]]"
founded: "2014-03-06"
---

Meetings
========

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the meetings engagement API to log and manage meetings on CRM records. You can log meeting activities either [in HubSpot](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or through the meetings API. You can retrieve, update, or delete meeting engagements that are manually logged on a record, scheduled using the [meetings tool](https://knowledge.hubspot.com/meetings-tool/use-meetings), or [scheduled using the Google Calendar or Office 365 calendar integration](https://knowledge.hubspot.com/integrations/schedule-a-meeting-with-a-contact-in-a-record).

Below, learn the basic methods of managing meetings through the API. To view all available endpoints and their requirements, click the Endpoints tab at the top of this article.

Create a meeting
----------------

To create a meeting engagement, make a `POST` request to `/crm/v3/objects/meetings`.

In the request body, add meeting details in a properties object. You can also add an associations object to associate your new meeting with an existing record (e.g., contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/meetings#properties)

In the properties object, you can include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_timestamp`

 | 

Required. This field marks the date and time that the meeting occurred. You can use either a Unix timestamp in milliseconds or UTC format.

(BETA) When the property value is missing, the value will  default to `hs_meeting_start_time.`

 |
| 

`hs_meeting_title`

 | 

The title of the meeting.

 |
| 

`hubspot_owner_id`

 | 

The [ID of the owner](/docs/api/crm/owners) associated with the meeting. This field determines the user listed as the meeting creator on the record timeline.

 |
| 

`hs_meeting_body`

 | 

The meeting description. 

 |
| 

`hs_internal_meeting_notes`

 | 

The internal notes you take for your team during a meeting that are not included in the attendee meeting description. 

 |
| 

`hs_meeting_external_URL`

 | 

The external URL for the calendar event. For example, this could be a Google calendar link or a Microsoft Outlook calendar link.

 |
| 

`hs_meeting_location`

 | 

Where the meeting takes place. The value could be a physical address, a conference room, a videoconference link, or a phone number. This appears on the calendar invite on the attendee's calendar. 

 |
| 

`hs_meeting_start_time`

 | 

The date and time when the meeting starts. The value for this property should match the value for `hs_timestamp`.

 |
| 

`hs_meeting_end_time`

 | 

The date and time when the meeting ends. 

 |
| 

`hs_meeting_outcome`

 | 

The outcome of the meeting. The outcome values are scheduled, completed, rescheduled, no show, and canceled. 

 |
| 

`hs_activity_type`

 | 

The type of meeting. The options are based on the [meeting types set in your HubSpot account.](https://knowledge.hubspot.com/meetings-tool/how-do-i-create-and-use-call-and-meeting-types)

 |
| 

`hs_attachment_ids`

 | 

The IDs of the meeting's attachments. Multiple attachment IDs are separated by a semi-colon.

 |

### Associations[](https://developers.hubspot.com/docs/api/crm/meetings#associations)

To create and associate a meeting with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the meeting with.

 |
| 

`associationTypeId`

 | 

The ID of the association type between the meeting and the other object type. You can retrieve this value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, to create and associate a meeting with contacts, your request may look similar to the following:

// Example request body { "properties": { "hs\_timestamp": "2021-03-23T01:02:44.872Z", "hubspot\_owner\_id": "11349275740", "hs\_meeting\_title": "Intro meeting", "hs\_meeting\_body": "The first meeting to discuss options", "hs\_internal\_meeting\_notes": "These are the meeting notes", "hs\_meeting\_external\_url": "https://Zoom.com/0000", "hs\_meeting\_location": "Remote", "hs\_meeting\_start\_time": "2021-03-23T01:02:44.872Z", "hs\_meeting\_end\_time": "2021-03-23T01:52:44.872Z", "hs\_meeting\_outcome": "SCHEDULED" }, "associations": \[ { "to": { "id": 101 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 200 } \] }, { "to": { "id": 102 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 200 } \] }\] }

Learn more about batch creating meetings by clicking the Endpoints tab at the top of this article.

Retrieve meetings[](https://developers.hubspot.com/docs/api/crm/meetings#retrieve-meetings)
-------------------------------------------------------------------------------------------

You can retrieve meetings individually or in bulk. Learn more about batch retrieval by clicking the Endpoints tab at the top of this article.

To retrieve an individual meeting by its meeting ID, make a `GET` request to `/crm/v3/objects/meetings/{meetingId}`. You can also include the following parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned. 

 |
| 

`associations`

 | 

A comma separated list of objects to you want to retrieve associated record IDs from. 

 |

To request a list of all of meetings, make a `GET` request to `crm/v3/objects/meetings`. You can include the following parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`limit`

 | 

The maximum number of results to display per page.

 |
| 

`properties`

 | 

A comma separated list of the properties to be returned. 

 |

Update meetings[](https://developers.hubspot.com/docs/api/crm/meetings#update-meetings)
---------------------------------------------------------------------------------------

You can update meetings individually or in batches. To update an individual meeting by its meeting ID, make a `PATCH` request to `/crm/v3/objects/meetings/{meetingId}`. 

In the request body, include the meeting properties that you want to update. For example, your request body might look similar to the following:

//Example PATCH request to https://api.hubspot.com/crm/v3/objects/meetings/{meetingId} { "properties": { "hs\_timestamp": "2019-10-30T03:30:17.883Z", "hubspot\_owner\_id": "11349275740", "hs\_meeting\_title": "Intro meeting", "hs\_meeting\_body": "The first meeting to discuss options", "hs\_internal\_meeting\_notes": "These are the meeting notes", "hs\_meeting\_external\_url": "https://Zoom.com/0000", "hs\_meeting\_location": "Remote", "hs\_meeting\_start\_time": "2021-03-23T01:02:44.872Z", "hs\_meeting\_end\_time": "2021-03-23T01:52:44.872Z", "hs\_meeting\_outcome": "SCHEDULED" } }'

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating by clicking the Endpoints tab at the top of this article.

### Associate existing meetings with records[](https://developers.hubspot.com/docs/api/crm/meetings#associate-existing-meetings-with-records)

To associate a meeting with records, such as a contact and its associated companies, make a `PUT` request to `/crm/v3/objects/meetings/{meetingId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL contains the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`meetingId`

 | 

The ID of the meeting.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the meeting with (e.g., contact or company)

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the meeting with.

 |
| 

`associationTypeId`

 | 

The ID of the association type between the meeting and the other object type. You can retrieve this value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubspot.com/crm/v3/objects/meetings/17612479134/associations/contact/104901/200`

### Remove an association

To remove an association between a meeting and a record, make a `DELETE` request to the same URL as above:

`/crm/v3/objects/meetings/{meetingId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin a meeting on a record[](https://developers.hubspot.com/docs/api/crm/meetings#pin-a-meeting-on-a-record)
-----------------------------------------------------------------------------------------------------------

You can [pin a meeting](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The meeting must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin a meeting, include the meeting's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete meetings[](https://developers.hubspot.com/docs/api/crm/meetings#delete-meetings)
---------------------------------------------------------------------------------------

You can delete meetings individually or in batches, which will add the meeting to the recycling bin in HubSpot. You can later [restore the meeting from the record timeline](https://knowledge.hubspot.com/crm-setup/restore-deleted-activity-in-a-record).

To delete an individual meeting by its meeting ID, make a `DELETE` request to `/crm/v3/objects/meetings/{meetingId}`.

Learn more about batch deleting by clicking the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/meetings#page-feedback)
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