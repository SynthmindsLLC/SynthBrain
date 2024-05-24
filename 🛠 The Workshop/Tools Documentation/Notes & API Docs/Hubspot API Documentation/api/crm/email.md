Email
=====

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the email engagement API to log and manage emails on CRM records. You can log email activities either [in HubSpot](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or through the emails API. 

Below, learn the basic methods of managing emails through the API. To view all available endpoints and their requirements, click the Endpoints tab at the top of this article.

Create an email
---------------

To create an email engagement, make a `POST` request to `/crm/v3/objects/emails`.

In the request body, add email details in a properties object. You can also add an associations object to associate your new email with an existing record (e.g., contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/email#properties)

In the properties object, you can include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_timestamp`

 | 

Required. This field marks the email's time of creation and determines where the email sits on the record timeline. You can use either a Unix timestamp in milliseconds or UTC format. 

 |
| 

`hubspot_owner_id`

 | 

The [ID of the owner](/docs/api/crm/owners) associated with the email. This field determines the user listed as the email creator on the record timeline.

 |
| 

`hs_email_direction`

 | 

The direction the email was sent in. Possible values include:

`EMAIL`: the email was sent from the CRM or sent and logged to the CRM with the [BCC address.](https://knowledge.hubspot.com/settings/log-email-in-your-crm-with-the-bcc-or-forwarding-address)

`INCOMING_EMAIL`: the email was a reply to a logged outgoing email.

`FORWARDED_EMAIL`: the email was [forwarded to the CRM.](https://knowledge.hubspot.com/settings/log-email-in-your-crm-with-the-bcc-or-forwarding-address)

 |
| 

`hs_email_html`

 | 

The body of an email if it is sent from a CRM record.

 |
| 

`hs_email_status`

 | 

The send status of the email. The value can be `BOUNCED`, `FAILED`, `SCHEDULED`, `SENDING`, or `SENT`.

 |
| 

`hs_email_subject`

 | 

The subject line of the logged email. 

 |
| 

`hs_email_text`

 | 

The body of the email. 

 |
| 

`hs_attachment_ids`

 | 

The IDs of the email's attachments. Multiple attachment IDs are separated by a semi-colon.

 |
| 

`hs_email_headers`

 | 

The email's headers. The value for this property will automatically populate certain read only email properties. Learn how to [set email headers.](/docs/api/crm/email#set-email-headers)

 |

Learn more about batch creating email engagements by clicking the Endpoints tab at the top of this article.

### Read only properties

There are also some email properties that are read only, which are automatically populated by HubSpot. The properties in the table below are all automatically populated from the `hs_email_headers` value.

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_email_from_email`

 | 

The email address of the email's sender.

 |
| 

`hs_email_from_firstname`

 | 

The email sender's first name.

 |
| 

`hs_email_from_lastname`

 | 

The email sender's last name.

 |
| 

`hs_email_to_email`

 | 

The email addresses of the email's recipients.

 |
| 

`hs_email_to_firstname`

 | 

The first names of the email's recipients. 

 |
| 

`hs_email_to_lastname`

 | 

The last names of the email recipient.

 |

**Please note:** when retrieving an email header, you may notice there are values both for `From` and `Sender`. These are often the same, but because `Sender` identifies what actually submitted an email, there are scenarios where the values may differ. For example, if an email is sent from an email alias, the `From` value will refer to the user's actual email address, and the `Sender` value will refer to the email alias.

### Set email headers[](https://developers.hubspot.com/docs/api/crm/email#set-email-headers)

Since headers automatically populate the read only properties, you may want to manually set the email headers. To set the `hs_email_headers` value, you can use a JSON escaped string with the following data:

//Example data { "from": { "email": "from@domain.com", "firstName": "FromFirst", "lastName": "FromLast" }, "to": \[ { "email": "ToFirst ToLast<to@test.com>", "firstName": "ToFirst", "lastName": "ToLast" } \], "cc": \[\], "bcc": \[\] }

For example, your request to create an email may look like:

//Example request body { "properties":{ "hs\_timestamp":"2019-10-30T03:30:17.883Z", "hubspot\_owner\_id":"47550177", "hs\_email\_direction":"EMAIL", "hs\_email\_status":"SENT", "hs\_email\_subject":"Let's talk", "hs\_email\_text":"Thanks for youremail", "hs\_email\_headers":"{\\"from\\":{\\"email\\":\\"from@domain.com\\",\\"firstName\\":\\"FromFirst\\",\\"lastName\\":\\"FromLast\\"},\\"sender\\":{\\"email\\":\\"sender@domain.com\\",\\"firstName\\":\\"SenderFirst\\",\\"lastName\\":\\"SenderLast\\"},\\"to\\":\[{\\"email\\":\\"ToFirst+ToLast<to@test.com>\\",\\"firstName\\":\\"ToFirst\\",\\"lastName\\":\\"ToLast\\"}\],\\"cc\\":\[\],\\"bcc\\":\[\]}" } }

### Associations[](https://developers.hubspot.com/docs/api/crm/email#associations)

To create and associate an email with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the email with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the email and the other object. You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, to create an email and associate it with a deal and a contact, your request body might look like the following:

// Example request body { "properties": { "hs\_timestamp": "2019-10-30T03:30:17.883Z", "hubspot\_owner\_id": "11349275740", "hs\_email\_direction": "EMAIL", "hs\_email\_status": "SENT", "hs\_email\_subject": "Let's talk", "hs\_email\_text": "Thanks for your interest let's find a time to connect" }, "associations": \[ { "to": { "id": 601 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 210 } \] }, { "to": { "id": 602 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 198 } \] }\] }

Retrieve emails[](https://developers.hubspot.com/docs/api/crm/email#retrieve-emails)
------------------------------------------------------------------------------------

You can retrieve emails individually or in bulk. Learn more about batch retrieval by clicking the Endpoints tab at the top of this article.

To retrieve an individual email by its email ID, make a `GET` request to `/crm/v3/objects/emails/{emailId}`. You can also include the following parameters in the request URL: 

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

A comma separated list of object types to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](/docs/api/crm/associations)

 |

To request a list of all of emails, make a `GET` request to `crm/v3/objects/emails`. You can include the following parameters in the request URL: 

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

Update emails[](https://developers.hubspot.com/docs/api/crm/email#update-emails)
--------------------------------------------------------------------------------

You can update emails individually or in batches. To update an individual email by its email ID, make a `PATCH` request to `/crm/v3/objects/emails/{emailId}`. 

In the request body, include the email properties that you want to update. For example, your request body might look similar to the following:

// Example request body { "properties": { "hs\_timestamp": "2019-10-30T03:30:17.883Z", "hubspot\_owner\_id": "11349275740", "hs\_email\_direction": "EMAIL", "hs\_email\_status": "SENT", "hs\_email\_subject": "Let's talk tomorrow", "hs\_email\_text": "Thanks for your interest let's find a time to connect!" } }

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating by clicking the Endpoints tab at the top of this article.

### Associate existing emails with records[](https://developers.hubspot.com/docs/api/crm/email#associate-existing-emails-with-records)

To associate an email with records, such as a contact and its associated companies, make a `PUT` request to `/crm/v3/objects/emails/{emailId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL contains the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`emailId`

 | 

The ID of the email.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the email with (e.g., contact or company)

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the email with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the email and the other object. The ID can be represented numerically or in snake case (e.g., `email_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubspot.com/crm/v3/objects/emails/17691787884/associations/contact/104901/198`

### Remove an association

To remove an association between an email and a record, make a `DELETE` request to the same URL as above:

`/crm/v3/objects/emails/{emailId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin an email on a record[](https://developers.hubspot.com/docs/api/crm/email#pin-an-email-on-a-record)
------------------------------------------------------------------------------------------------------

You can [pin an email](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The email must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin an email, include the email's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete emails[](https://developers.hubspot.com/docs/api/crm/email#delete-emails)
--------------------------------------------------------------------------------

When you delete an email, it is permanently deleted and cannot be restored. You can delete emails individually or in batches.

To delete an individual email by its email ID, make a `DELETE` request to `/crm/v3/objects/emails/{emailId}`.

Learn more about batch deleting by clicking the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/email#page-feedback)
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