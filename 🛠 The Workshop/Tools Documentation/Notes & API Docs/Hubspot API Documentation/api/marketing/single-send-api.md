Marketing Single Send API
=========================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The single-send API allows you to send template emails created in the HubSpot [marketing email tool](https://knowledge.hubspot.com/email/create-marketing-emails-in-the-drag-and-drop-email-editor) using a JSON-formatted POST request.

All contacts receiving marketing content must be [set as marketing](https://knowledge.hubspot.com/contacts/set-contacts-as-marketing). Any marketing emails sent through the single-send API will automatically be associated with contact records based on their email address, and update non-marketing contacts and set them to marketing contacts . If there's no contact with a matching email address, a new contact record with that email will be created, and the contact will be set as marketing.

Requirements[](https://developers.hubspot.com/docs/api/marketing/single-send-api#requirements)
----------------------------------------------------------------------------------------------

To use the marketing single send API, the following requirements must be met:

*   You must have a _**Marketing Hub** Enterprise_ account.
*   The [private app](/docs/api/private-apps) or [public app](/docs/api/creating-an-app) you're using to make API requests has been granted the `marketing-email` scope.

Create an email and send it via the single-send API
---------------------------------------------------

First, [set up your email in HubSpot](https://knowledge.hubspot.com/email/how-to-use-transactional-email-in-hubspot). After you create the email, you can set the recipient details, including any contact or custom properties set up in the email template, in the body of the API request. Before you can make the API request, you'll need the ID of the email:

*   If you leave the email drafted without publishing it, you can get the email ID from the URL when you're in the email editor. The ID is the final numeric value before the final slash character (`/`) in the URL (e.g., `https://app.hubspot.com/email/{PORTAL_ID}/edit/{EMAIL_ID}/settings`).

![email-id-for-drafted-single-send-api-email](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/email-id-for-drafted-single-send-api-email.png?width=800&height=133&name=email-id-for-drafted-single-send-api-email.png)

*   If you publish your email, you can copy the email ID from the email details page.

![Screen Shot 2020-04-15 at 1.00.37 PM](https://developers.hubspot.com/hs-fs/hubfs/Screen%20Shot%202020-04-15%20at%201.00.37%20PM.png?width=872&name=Screen%20Shot%202020-04-15%20at%201.00.37%20PM.png)

**Please note:** HubSpot does not save the HTML/JSON sent through this API. You can review the email template from the recipient contact's timeline, but if you want to keep a record of the email's contents, it's recommended to add a BCC to the email.

To send an email with the Single-Send API, make a `POST` request to `/marketing/v4/email/single-send`.

The response contains the following fields:

*   `requestedAt`: the timestamp of when the send was requested.

*   `statusId`: an identifier that can be used to [query the status of the send](#query-the-status-of-an-email-send).

*   `status`: the status of the send request. Includes `PENDING`, `PROCESSING`, `CANCELED`, and `COMPLETE`.

### Request properties

The request body must be a JSON-formatted object with the following properties:

*   `emailId`
*   `message`
*   `contactProperties`
*   `customProperties`

#### emailId

The `emailId` field contains the email's content ID, which can be found in HubSpot's email tool.

#### message

The message field is a JSON object containing anything that you want to override. At the minimum, you must include the `to` field.

Message object fields:

*   `to`: the recipient of the email
*   `from`: the "From" header for the email. You can define a from name with the following format: `"from":"Sender Name <sender@hubspot.com>"`
*   `sendId`: the ID of a particular send. Only one email with a given `sendId` will be sent per account, so you can include this field to prevent duplicate email sends.
*   `replyTo`:  a JSON list of "Reply-To" header values for the email.
*   `cc`: a JSON list of email addresses to send as Cc.
*   `bcc`: a JSON list of email addresses to send as Bcc.

#### contactProperties

The `contactProperties` field is a JSON map of contact property values. Each contact property value contains a `name` and `value`. Each property will be set on the contact record and will be visible in the template under:

![name-token-in-template-for-transactional-email](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/name-token-in-template-for-transactional-email.png?width=88&height=29&name=name-token-in-template-for-transactional-email.png)

Use these properties when you want to set a contact property while you’re sending the email. For example, when sending a receipt you may want to set a `last_paid_date` property, as the sending of the receipt will have information about the last payment.

{ "emailId": 4126643121, "message": { "to": "jdoe@hubspot.com" "sendId": "6" }, "contactProperties": { "last\_paid\_date": "2022-03-01", "firstname": "jane" } }

#### customProperties

The `customProperties` field is a JSON map of key-value properties. These properties are generally related to the email itself, not the contact receiving the email. They will not appear in the [web page version of the email](https://knowledge.hubspot.com/email/create-a-web-version-of-your-marketing-email), or in the view of the email from the contact's timeline. These properties are also not stored in HubSpot and will only be included in the sent email.

Each key in the `customProperties` field can be referenced in the template using a [HubL expression](/docs/cms/hubl) for fields contained within the `custom` variable (e.g., `{{custom.NAME_OF_PROPERTY}}` ).

For example, if your email template references two properties, `purchaseUrl` and `productName`, you could provide the associated values for these properties with the following request body:

{ "emailId": 4126643121, "message": { "to": "jdoe@hubspot.com" "sendId": "6" }, "customProperties": { "purchaseUrl": "https://example.com/link-to-product", "productName": "vanilla" } }

You can then reference these properties in your email template:

<!doctype html> <html> <p> Congrats on purchasing some of the best ice cream around. </p> <a href={{custom.purchaseUrl}}>{{custom.productName}}</a> </html>

The `customProperties` field only supports arrays when used with [programmable email content](/docs/cms/guides/email/hubdb-crm-objects). In your email template, you can reference the items defined in your `customProperties` field by using a [HubL expression](/docs/cms/hubl) (e.g., using a [for loop](/docs/cms/hubl/for-loops) to render each item in a list). For example, if the `customProperties` you included in your request body was structured like the following JSON snippet below:

{ "emailId": 4126643122, "message": { "to": "jdoe@hubspot.com" "sendId": "7" }, "customProperties": { "exampleArray": \[ {"firstKey": "someValue", "secondKey": "anotherValue"}, {"firstKey": "value1", "secondKey": "value2" } \] } }

You could then reference the values for each item in `exampleArray` with the following HubL code:

<!doctype html> <html> <p> Thanks for your recent purchase! Here are the details of the items you'll be receiving: </p> <ul> {% for item in custom.exampleArray %} <li>First key: {{ item.firstKey }}, Second key: {{item.secondKey}}</li> {% endfor %} </ul> </html>

Once sent, the email would render the contents of the associated programmable email template as follows:

![example-transactional-email-with-customProperties-array](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/example-transactional-email-with-customProperties-array.png?width=568&height=114&name=example-transactional-email-with-customProperties-array.png)

### Query the status of an email send

To get the status of the email send, make a `GET` request to `https://api.hubapi.com/marketing/v3/email/send-statuses/{statusId}`. 

The response contains the following fields:

*   `sendResult`: an enumeration that represents the email's send status. The possible values are [listed below](#sendresult-values).
*   `requestedAt`: the timestamp from when the send was requested.

*   `startedAt`: the timestamp when the send began processing.

*   `completedAt`: the timestamp when the send completed.

*   `statusId`: an identifier that can be used to query the status of the send.

*   `status`: the status of the send request. Includes `PENDING`, `PROCESSING`, `CANCELED`, and `COMPLETE`.

*   `eventId`: if sent, the ID and created timestamp of the sent event.

#### sendResult

The `sendResult` is an enumeration that reflects the result of an email send attempt. Its possible values are:

*   `SENT`: the email was sent successfully.
*   `QUEUED`: the email was queued and will send as the queue gets processed.
*   `PORTAL_SUSPENDED`: due to [Acceptable Use Policy](https://legal.hubspot.com/acceptable-use) violations, the HubSpot customer's email has been suspended.
*   `INVALID_TO_ADDRESS`: the recipient address is invalid. This error will also occur if you attempt to send an email with any of the following role-based prefixes in the email address: `abuse`, `no-reply`, `noreply`, `root`, `spam`, `security`, `undisclosed-recipients`, `unsubscribe`, `inoc`, `postmaster`, or `privacy`.
*   `BLOCKED_DOMAIN`: the domain cannot receive emails from HubSpot at this time.
*   `PREVIOUSLY_BOUNCED`: the recipient has previously bounced, and the sending logic resulted in no send.
*   `PREVIOUS_SPAM`: the recipient has previously marked similar email as spam.
*   `INVALID_FROM_ADDRESS`: the _From_ address is invalid.
*   `MISSING_CONTENT`: the `emailId` is invalid, or the `emailId` corresponds to an email that wasn't set up for Single-Send.
*   `MISSING_TEMPLATE_PROPERTIES`: there are properties set up in the template that have not been included in the `customProperties` sent in the request.

For a full list of the endpoints available with this API, click the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/marketing/single-send-api#page-feedback)
------------------------------------------------------------------------------------------------------

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