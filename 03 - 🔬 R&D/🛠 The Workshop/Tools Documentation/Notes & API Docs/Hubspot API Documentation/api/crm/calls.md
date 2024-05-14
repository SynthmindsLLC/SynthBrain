Calls
=====

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the calls engagement API to log and manage calls on CRM records and on the [calls index page](https://knowledge.hubspot.com/crm-setup/create-customize-and-manage-your-saved-views). You can log calls either [in HubSpot](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or through the calls API. Below, learn the basic methods of managing calls through the API. To view all available endpoints and their requirements, click the Endpoints tab at the top of this article.

Create a call engagement[](https://developers.hubspot.com/docs/api/crm/calls#create-a-call-engagement)
------------------------------------------------------------------------------------------------------

To create a call engagement, make a `POST` request to `/crm/v3/objects/calls`.

In the request body, add call details in a properties object. You can also add an associations object to associate your new call with an existing record (e.g.,contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/calls#properties)

Below is a list of HubSpot default calling properties that you can include in the properties object. You can also create custom properties using the [properties API](/beta-docs/guides/api/crm/properties). 

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_timestamp`

 | 

Required. This field marks the call's time of creation and determines where the call sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 

 |
| 

`hs_call_body`

 | 

The description of the call, including any notes that you want to add.

 |
| 

`hs_call_callee_object_id`

 | 

The ID of the HubSpot record associated with the call. This will be the recipient of the call for `OUTBOUND` calls, or the dialer of the call for `INBOUND` calls.

 |
| 

`hs_call_callee_object_type_id`

 | 

The ID of the object to which the call's associated record belongs (e.g., specifies if the record is a contact or company). This will be the object of the recipient for `OUTBOUND` calls, or the object of the dialer for `INBOUND` calls.

 |
| 

`hs_call_direction`

 | 

The direction of the call from the perspective of the HubSpot user. If the user is the call recipient, the direction should be set to `INBOUND`. If the user initiated the call, the direction should be set to `OUTBOUND`.

 |
| 

`hs_call_disposition`

 | 

The outcome of the call. To set the call disposition, you need to use the internal GUID value. If your account has set up [custom call outcomes](https://knowledge.hubspot.com/calling/create-custom-call-and-meeting-outcomes), you can find their disposition GUIDs using [this API](https://legacydocs.hubspot.com/docs/methods/engagements/get-call-dispositions). The default HubSpot outcome labels and their internal values are:

*   Busy: `9d9162e7-6cf3-4944-bf63-4dff82258764`
*   Connected: `f240bbac-87c9-4f6e-bf70-924b57d47db7`
*   Left live message: `a4c4c377-d246-4b32-a13b-75a56a4cd0ff`
*   Left voicemail: `b2cf5968-551e-4856-9783-52b3da59a7d0`
*   No answer: `73a0d17f-1163-4015-bdd5-ec830791da20`
*   Wrong number: `17b47fee-58de-441e-a44c-c6300d46f273`

 |
| 

`hs_call_duration`

 | 

The duration of the call in milliseconds.

 |
| 

`hs_call_from_number`

 | 

The phone number that the call was made from.

 |
| 

`hs_call_recording_url`

 | 

The URL that stores the call recording. URLS to .mp3 or .wav files can be played back on CRM records. Only HTTPS,  secure URLs will be accepted.

 |
| 

`hs_call_status`

 | 

The status of the call. The statuses are `BUSY`, `CALLING_CRM_USER`, `CANCELED`, `COMPLETED`, `CONNECTING`, `FAILED`, `IN_PROGRESS`, `NO_ANSWER`, `QUEUED`, and `RINGING`.

 |
| 

`hs_call_title`

 | 

The title of the call.

 |
| 

`hs_call_source`

 | 

The source of the call. This is not required, but it is required to leverage the [recording and transcriptions pipeline](/docs/api/crm/extensions/recordings-and-transcriptions#log-a-call-with-your-app-s-endpoint-using-the-engagements-api). If the property is set, it must be set to `INTEGRATIONS_PLATFORM`.

 |
| 

`hs_call_to_number`

 | 

The phone number that received the call.

 |
| 

`hubspot_owner_id`

 | 

The [ID of the owner](/docs/api/crm/owners) associated with the call. This field determines the user listed as the call creator on the record timeline.

 |
| 

`hs_activity_type`

 | 

The type of call. The options are based on the [call types set in your HubSpot account.](https://knowledge.hubspot.com/meetings-tool/how-do-i-create-and-use-call-and-meeting-types)

 |
| 

`hs_attachment_ids`

 | 

The IDs of the call's attachments. Multiple attachment IDs are separated by a semi-colon.

 |

### Associations[](https://developers.hubspot.com/docs/api/crm/calls#associations)

To create and associate a call with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the call with.

 |
| 

`associationType`

 | 

A unique identifier to indicate the association type between the call and the other object. The ID can be represented numerically or in snake case (e.g., `call_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, to create a call and associate it with a contact and a ticket, your request body might look similar to the following:

// Example request body { "properties": { "hs\_timestamp": "2021-03-17T01:32:44.872Z", "hs\_call\_title": "Support call", "hubspot\_owner\_id": "11349275740", "hs\_call\_body": "Resolved issue", "hs\_call\_duration": "3800", "hs\_call\_from\_number": "(857) 829 5489", "hs\_call\_to\_number": "(509) 999 9999", "hs\_call\_recording\_url": "https://api.twilio.com/2010-04-01/Accounts/AC890b8e6fbe0d989bb9158e26046a8dde/Recordings/RE3079ac919116b2d22", "hs\_call\_status": "COMPLETED" }, "associations": \[ { "to": { "id": 500 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 194 } \] }, { "to": { "id": 1234 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 220 } \] }\] }

Learn more about batch creating calls by clicking the Endpoints tab at the top of this article.

Retrieve calls[](https://developers.hubspot.com/docs/api/crm/calls#retrieve-calls)
----------------------------------------------------------------------------------

You can retrieve calls individually or in bulk. Learn more about batch retrieval by clicking the Endpoints tab at the top of this article.

To retrieve an individual call by its call ID, make a `GET` request to `/crm/v3/objects/calls/{callId}`. You can include the following parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the [properties](#call-properties-1) to be returned. 

 |
| 

`associations`

 | 

A comma separated list of object types to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](/docs/api/crm/associations)

 |

To request a list of all of calls, make a `GET` request to `/crm/v3/objects/calls`. You can include the following parameters in the request URL: 

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

A comma separated list of the [properties](#call-properties-1) to be returned. 

 |

When you make a successful request, the response will include the `callId` which you can use to retrieve, update, and delete the call. 

### Identify voicemails vs. recorded calls

For recorded calls and voicemails, a recording is stored in the `hs_call_recording_url` property. If your account has access to [inbound calling](https://knowledge.hubspot.com/calling/receive-calls-in-hubspot), to differentiate between calls that were completed and recorded vs. inbound calls with a voicemail, include the following properties in your request: `hs_call_status` and `hs_call_has_voicemail`. 

If a call has a voicemail, the `hs_call_status` value will be `missed`, and the `hs_call_has_voicemail` value will be `true`. The `hs_call_has_voicemail` value will be `false` for an inbound call where no voicemail was left, or `null` if the call has a status other than missed.

Update calls[](https://developers.hubspot.com/docs/api/crm/calls#update-calls)
------------------------------------------------------------------------------

You can update calls individually or in batches. To update an individual call by its call ID, make a `PATCH` request to `/crm/v3/objects/calls/{callId}`. 

In the request body, include the call properties that you want to update:

//Example PATCH request to https://api.hubspot.com/crm/v3/objects/calls/{callID} { "properties": { "hs\_timestamp": "2021-03-17T01:32:44.872Z", "hs\_call\_title": "Discovery call", "hubspot\_owner\_id": "11349275740", "hs\_call\_body": " Decision maker out, will call back tomorrow", "hs\_call\_duration": "3800", "hs\_call\_from\_number": "(857) 829 5489", "hs\_call\_to\_number": "(509) 999 9999", "hs\_call\_recording\_url": "https://api.twilio.com/2010-04-01/Accounts/AC890b8e6fbe0d989bb9158e26046a8dde/Recordings/RE3079ac919116b2d22", "hs\_call\_status": "COMPLETED" } }'

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating by clicking the Endpoints tab at the top of this article.

### Associate existing calls with records[](https://developers.hubspot.com/docs/api/crm/calls#associate-existing-calls-with-records)

To associate a call with records, such as a contact and its associated companies, make a `PUT` request to `/crm/v3/objects/calls/{callId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL contains the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`callId`

 | 

The ID of the call.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the call with (e.g., contact or company)

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the call with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the call and the other object. The ID can be represented numerically or in snake case (e.g., `call_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubspot.com/crm/v3/objects/calls/17591596434/associations/contact/104901/194`

### Remove an association

To remove an association between a call and a record, make a `DELETE` request to the same URL as above:

`/crm/v3/objects/calls/{callId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin a call on a record[](https://developers.hubspot.com/docs/api/crm/calls#pin-a-call-on-a-record)
--------------------------------------------------------------------------------------------------

You can [pin a call](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The call must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin a call, include the call's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete calls[](https://developers.hubspot.com/docs/api/crm/calls#delete-calls)
------------------------------------------------------------------------------

You can delete calls individually or in batches, which will add the call to the recycling bin in HubSpot. You can later [restore the call from the record timeline](https://knowledge.hubspot.com/crm-setup/restore-deleted-activity-in-a-record).

To delete an individual call by its call ID, make a `DELETE` request to `/crm/v3/objects/calls/{callId}`.

Learn more about batch deleting by clicking the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/calls#page-feedback)
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