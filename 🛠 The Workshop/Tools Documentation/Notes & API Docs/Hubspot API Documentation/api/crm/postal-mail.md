Postal Mail
===========

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the postal mail engagement API to log and manage postal mail on CRM records. You can log the mail you've sent or received [in HubSpot](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or through the postal mail API. You can also retrieve, update, or delete existing postal mail engagements. 

Below, learn the basic methods of managing postal mail through the API. To view all available endpoints and their requirements, click the Endpoints tab at the top of this article.

Create a postal mail engagement[](https://developers.hubspot.com/docs/api/crm/postal-mail#create-a-postal-mail-engagement)
--------------------------------------------------------------------------------------------------------------------------

To create a postal mail engagement, make a `POST` request to `/crm/v3/objects/postal_mail`.

In the request body, add postal mail details in a properties object. You can also add an associations object to associate your new postal mail with an existing record (e.g., contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/postal-mail#properties)

In the properties object, you can include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_timestamp`

 | 

The date that the postal mail was sent or received.

 |
| 

`hs_postal_mail_body`

 | 

The body text of the postal mail engagement.

 |
| 

`hubspot_owner_id`

 | 

The ID of the user that created the postal mail engagement.

 |
| 

`hs_attachment_ids`

 | 

The IDs of any attachments to the postal mail engagement. Multiple attachment IDs are separated by a semi-colon.

 |

### Associations[](https://developers.hubspot.com/docs/api/crm/postal-mail#associations)

To create and associate a postal mail engagement with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the postal mail with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the postal mail and the other object. You can retrieve the value through the [associations API](https://developers.hubspot.com/docs/api/crm/associations/v4).

 |

For example, to create postal mail and associate it with two contacts, your request body might look similar to the following:

//Example request body { "properties": { "hs\_timestamp": "2021-11-12", "hs\_postal\_mail\_body": "Sent copy of contract to decision maker John", "hubspot\_owner\_id": "9274996", "hs\_attachment\_ids": "24332474034" }, "associations": \[ { "to": { "id": 501 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 453 } \] }, { "to": { "id": 502 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 453 } \] }\] }

Retrieve postal mail engagements[](https://developers.hubspot.com/docs/api/crm/postal-mail#retrieve-postal-mail-engagements)
----------------------------------------------------------------------------------------------------------------------------

You can retrieve postal mail engagements individually or in bulk.

To retrieve an individual postal mail engagement, make a `GET` request to `/crm/v3/objects/postal_mail/{postalMail}`. You can include the following parameters in the request: 

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

A comma separated list of object types to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](https://developers.hubspot.com/docs/api/crm/associations)

 |

To retrieve a list of the postal mail engagements in your account, make a `GET` request to `crm/v3/objects/postal_mail`. You can include the following parameters in the request:

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

When you make a successful batch request, the response will include the ID of each postal mail engagement, which you can use to retrieve, update, and delete postal mail engagements.

Update postal mail engagements[](https://developers.hubspot.com/docs/api/crm/postal-mail#update-postal-mail-engagements)
------------------------------------------------------------------------------------------------------------------------

You can update postal mail engagements individually or in batches. To update an individual engagement by its ID, make a `PATCH` request to `/crm/v3/objects/postal_mail/{postalMail}`. 

In the request body, include the properties that you want to update. For example, to update the body of the engagement, your request body might look similar to the following:

//Example request body { "properties": { "hs\_postal\_mail\_body": "Sent copy of contract to decision maker John. Received a call in response." } }

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating by clicking the Endpoints tab at the top of this article.

### Associate existing postal mail with records[](https://developers.hubspot.com/docs/api/crm/postal-mail#associate-existing-postal-mail-with-records)

You can associate postal mail engagements with contact, company, deal, or ticket records. To associate postal mail with records, make a `PUT` request to `/crm/v3/objects/postal_mail/{postalMail}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`postalMail`

 | 

The unique ID of the postal mail engagement.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the postal mail with (e.g., `contact` or `company`).

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the postal mail with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the postal mail and the other object. The ID can be represented numerically or in snake case (e.g., `POSTAL_MAIL_TO_CONTACT`). You can retrieve the value through the [associations API](https://developers.hubspot.com/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubspot.com/crm/v3/objects/postal_mail/25727582880/associations/contact/104901/POSTAL_MAIL_TO_CONTACT`

### Remove an association

To remove an association between a postal mail engagement and a record, make a `DELETE` request to:

`/crm/v3/objects/postal_mail/{postalMail}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin a postal mail engagement on a record[](https://developers.hubspot.com/docs/api/crm/postal-mail#pin-a-postal-mail-engagement-on-a-record)
--------------------------------------------------------------------------------------------------------------------------------------------

You can [pin a postal mail engagement](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The postal mail must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin postal mail, include the postal mail's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete postal mail engagements[](https://developers.hubspot.com/docs/api/crm/postal-mail#delete-postal-mail-engagements)
------------------------------------------------------------------------------------------------------------------------

You can delete a postal mail engagement individually or in bulk, which will add the engagement to the recycling bin in HubSpot. You can later [restore the engagement from the record timeline](https://knowledge.hubspot.com/crm-setup/restore-deleted-activity-in-a-record).

To delete an individual postal mail engagement by its ID, make a `DELETE` request to `/crm/v3/objects/postal_mail/{postalMail}`.

Learn more about batch deleting postal mail engagements on the _Endpoints_ tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/postal-mail#page-feedback)
--------------------------------------------------------------------------------------------

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