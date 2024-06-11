---
title: "FAQ about HubSpot's APIs"
description: "Get answers to frequently asked questions about HubSpot's APIs, including form manipulation with jQuery, timestamp formatting, API error messages, CORS / AJAX requests, email validation, contact record limits, transactional emails, subscribing to updates, and privacy compliance."
type: "group"
tags:
- "HubSpot"
- "APIs"
- "FAQ"
relationships:
- "#related_to [[CMS development]]"
- "#similar_to [[Documentation]]"
- "#contributed_to [[Developer community]]"
founded: "2014-05-08"
---

FAQ
===

Get answers to frequently asked questions about HubSpot's APIs. For CMS development questions, visit their [documentation](https://designers.hubspot.com/docs). If you can't find what you're looking for, you can ask on our [developer forum](https://developers.hubspot.com/forum). 

Below, learn more about the following commonly asked questions:

*   [How do I manipulate forms with jQuery?](#jQuerty)
*   [How should I format timestamps for HubSpot's APIs?](#timestamps)
*   [What do I need to know about API error messages?](#errors)
*   [Do the HubSpot APIs support CORS / AJAX requests?](#CORS_AJAX)
*   [How does HubSpot validate email addresses?](#validate_email)
*   [How do I set multiple values for checkbox properties?](#multiple_values_checkboxes)
*   [Are there limits on contact records?](#limits_contacts)
*   [How do I send transactional emails?](#transactional_emails)
*   [How do I subscribe to API updates?](#subscribe_updates)
*   [How do I handle privacy and legal compliance when working with the HubSpot platform?](#privacy_legal_compliance)

* * *

How do I manipulate forms using jQuery?
---------------------------------------

When you manipulate form input values using .`val()` or .`prop()`, you must trigger a change event using `change()`  or  `trigger('change')` for the change to register correctly.

Because HubSpot forms are rendered after the DOM builds, you must either trigger the manipulation after the window loads or modify the embed to use the `[onFormReady](https://developers.hubspot.com/docs/methods/forms/advanced_form_options)` parameter.

Update fields when page finishes loading: $(window).load(function(){ $('input\[value="checkbox\_1"\]').prop('checked', true).change(); $('input\[name="firstname"\]').val('Brian').change(); }); Modified embed code to update fields when form builds: hbspt.forms.create({ portalId: 'XXXXXX', formId: 'aa8b5b4a-62ac-461b-a387-XXXXXXXXXXX', onFormReady: function($form, ctx){ $('input\[value="checkbox\_1"\]').prop('checked', true).change(); $('input\[name="firstname"\]').val('Brian').change(); } });

* * *

How should I format timestamps for HubSpot's APIs?
--------------------------------------------------

Time values are represented in ISO 8601 format in responses, but the APIs will accept either of two formats for date and time values:  

*   **ISO 8601 formatted strings**: depending on the type of data, these will be one of two different formats:
    *   For values that represent a specific date, the complete date format will be used: YYYY-MM-DD (e.g. 2020-02-29)
    *   For values that represent a specific date and time, the complete date plus hours, minutes, seconds, and a decimal fraction of a second format will be used: YYYY-MM-DDThh:mm:ss.sTZD (e.g. 2020-02-29T03:30:17.000Z). All times are represented in UTC, so the values will always use the UTC designator "Z."
*   **UNIX-formatted timestamps in milliseconds**: timestamp values in milliseconds, which are represented in UTC time. For example, the timestamp value _1427997766000_ translates to _02 Apr 2015 18:02:46 UTC_, or _April 2nd, 2015, 2:02:46 PM EDT_ (Eastern Daylight Saving Time).

### Date and datetime properties in the HubSpot CRM

HubSpot has two types of CRM object properties for storing time: `date` and `datetime`.

*   **`date`** properties (including `date picker` properties created in HubSpot) store the date—not the time. `date` properties display the date they're set to, regardless of the time zone setting of the account or user. For `date` property values, it is recommended to use the ISO 8601 complete date format. If you use the UNIX timestamp format, you must use an EPOCH millisecond timestamp (i.e. the value must be set to midnight UTC for the date). For example, to represent May 1, 2015 in either format:
    *   **IOS 8601**: 2015-05-01
    *   **EPOCH-millisecond timestamp**: 1430438400000

**Please note**: if you're using a UNIX timestamp for a `date` property and try to set a value that isn't midnight UTC, you'll receive an error.

*   `datetime` properties store both the date and time. Either timestamp format will be accepted. In HubSpot, `datetime` properties are displayed based on the time zone of the user viewing the record, so the value will be converted to the local time zone of the user. Because `date picker` properties created in HubSpot are created as a `date` properties, the only way to create a `datetime` property is via API. If your integration needs to store specific times, you can create custom `datetime` properties using the [property endpoints.](/docs/api/crm/properties#tab-2)

* * *

What do I need to know about API error messages?
------------------------------------------------

Unless specified otherwise, most HubSpot endpoints will return a 200 OK response upon success. Any endpoints returning a different status code will specify the returned response in its documentation.

In addition, HubSpot has several error responses that are common to multiple APIs:

*   `401 Unauthorized` - Returned when the authentication provided is invalid. See our [Authentication Overview](https://developers.hubspot.com/docs/methods/auth/oauth-overview) for details on authenticating API requests.
*   `403 Forbidden` - Returned when the authentication provided does not have the proper permissions to access the specific URL. As an example, an OAuth token that only has content access would get a `403` when accessing the Deals API (which requires contacts access).
*   `429 Too many requests` - Returned when your account or app is over its API [rate limits](https://developers.hubspot.com/apps/api_guidelines). Find suggestions on working within those limits [here](https://developers.hubspot.com/docs/faq/working-within-the-hubspot-api-rate-limits).
*   `502/504 timeouts` - HubSpot has processing limits in place to prevent a single client from causing degraded performance, and these responses indicate that those limits have been hit. You'll normally only see these timeout responses when making a large number of requests over a sustained period. If you get one of these responses, you should pause your requests for a few seconds, then retry.

Aside from these general errors, HubSpot error responses are intended to be human-readable. Most endpoints don't return error codes, but return a JSON formatted response with details about the error. More details for endpoint-specific errors can be found on the documentation pages for the endpoint.

**Note:** The fields in the example response below should all be treated as optional in any error parsing. The specific fields included can vary between different APIs, so any error parsing should allow for specific fields to be missing from the response.

{"status":"error","message":"This will be a human readable message with details about the error.","errors":\[{"message":"This will be a message with additional details about the error","in":"name"}\],"category":"VALIDATION\_ERROR","correlationId":"a43683b0-5717-4ceb-80b4-104d02915d8c"}

* * *

Do the HubSpot APIs support CORS / AJAX requests?
-------------------------------------------------

For the most part, the HubSpot APIs do not support cross-origin (CORS) AJAX requests. Making the request client-side using JavaScript would expose any authentication you're using for the request. In order to use JavaScript/AJAX, you would need to make the request (excluding any authentication) to an external server that could then add the needed authentication and make requests to HubSpot's APIs server-side.

The exceptions to this rule are:

*   The [Submit form data (AJAX)](https://legacydocs.hubspot.com/docs/methods/forms/submit_form) endpoint, which accepts CORS AJAX form submissions.
*   Most `GET` requests for published HubDB tables. See the [HubDB API Overview](https://developers.hubspot.com/docs/methods/hubdb/hubdb_overview) for more details.

* * *

How does HubSpot validate email addresses?
------------------------------------------

HubSpot validates email addresses used for any process that would create or update a contact record. This includes using the [contacts endpoints](/docs-beta/crm/contacts) to create or update a contact as well as [form submissions](https://developers.hubspot.com/docs/methods/forms/submit_form) or [events](/docs/api/analytics/events).

These processes don't check the email address itself for validity (like an [embedded form would](https://knowledge.hubspot.com/articles/kcs_article/forms/why-is-my-form-telling-me-to-enter-a-valid-email-address)), but rather its format. In addition to being valid according to [RFC 2822](https://tools.ietf.org/html/rfc2822), HubSpot places the following restrictions on email addresses:

*   Local parts of the address cannot include quotation marks. (e.g. "Test Email"@hubspot.com isn't valid)
*   The domain part must end in a valid TLD, as listed at [https://data.iana.org/TLD/tlds-alpha-by-domain.txt](https://data.iana.org/TLD/tlds-alpha-by-domain.txt) (note that this is after handling unicode TLDs, so "user@email.삼성" is a valid email address).

* * *

How do I set multiple values for checkbox properties?
-----------------------------------------------------

When setting multiple values for a checkox property, the values should be separated with a semicolon (;).  
**Example:** `'value1;value2;value5'`

When updating a record through the CRM object endpoints, the property value should be a single string with all of the values separated by semicolons:

> `{     "properties":       {         "example_property": "value1;value3;value4"       }   }`

For the Forms endpoints, make sure that the semicolons are also URL encoded:

> `...&example_property=value1%3Bvalue2%3Bvalue4`  
>   

* * *

Are there limits on contact records?
------------------------------------

HubSpot has a few limits in place regarding merged contact records and form submissions for contact records:

1.  There's a limit of 250 linked identities per contact.
    *   If you try to merge two contacts, and the resulting contact would have more than 250 identities, you will get an error.
2.  Contacts are limited to 1000 form submissions. Submissions that would take a contact over this limit will be dropped completely:
    *   The form data will not update the contact record.
    *   The submission itself will not show up for the contact record, either in the `form-submissions` data from the contacts endpoints or in the contact's timeline.
    *   The submission won't be evaluated for list membership or workflows.
    *   The submission won't appear in the submissions list for viewing the form in HubSpot.

If you're exceeding either of these limits because of testing, we'd recommend deleting the test contacts and creating a new test record. Using the same email address in the new contact won't restore the deleted contact, and any form submissions with the email will be associated to the new record.

* * *

How do I send transactional emails?
-----------------------------------

HubSpot supports two methods of sending transactional emails: the SMTP API and the Single-send API.

### Using the SMTP API

The SMTP API doesn't directly send emails, but is only used to get login credentials for the HubSpot SMTP server. After you get a token and password using the [SMTP API](https://developers.hubspot.com/docs/methods/email/transactional_email/smtpapi_overview/list/create), you'll need to use those credentials to log into HubSpot's SMTP server and send the email over SMTP. The login details (hostname and port) for the SMTP server can be found on the [documentation page](https://developers.hubspot.com/docs/methods/email/transactional_email/smtpapi_overview/list/create). The email and links will be wrapped to support HubSpot's email tracking, but otherwise you will need to build the entirety of the email content.

### Using the Single-send API

The [Single-send API](https://developers.hubspot.com/docs/methods/email/transactional_email/single-send-overview) uses template emails created in the HubSpot email tool, along with a JSON formatted `POST` API to send emails. First, you'll need to create an email in HubSpot and select "Save for single-send API" when choosing the recipient.  After the email is created, you can use the API to send the email to a contact, setting the details for the recipient (including any contact or custom properties set up in the email) in the body of the API request.  More details for the format of that JSON request can be found on the [documentation page](https://developers.hubspot.com/docs/methods/email/transactional_email/single-send-overview).

* * *

How do I subscribe to API updates?
----------------------------------

Updates to HubSpot's APIs and developer tools are made through our [Developer Changelog](https://developers.hubspot.com/changelog).

You can use the form on the left to subscribe to updates. Select Instant for the frequency to get notifications as soon as they are announced. Otherwise, select one of the other frequencies to get a digest of updates at your chosen frequency.

* * *

How do I handle privacy and legal compliance when working with the HubSpot platform?
------------------------------------------------------------------------------------

### Tracking legal basis of processing in HubSpot

Under GDPR, companies need a legal reason to use and process contact data and must keep records of consent and evidence other legal purposes of processing.

The `Legal basis for processing contact's data` contact property allows you to collect, track, and store legal basis of processing via contract, legitimate interest, and/or consent for your HubSpot contacts.

When accessing contact data via the [contacts endpoints](/docs-beta/crm/contacts), this property uses the name `hs_legal_basis`. As with any other contact property, any contact with this property set would be accessible through the API. The property can also be set or [updated for contact records](/docs-beta/crm/contacts) through the API.

However, the property options can't be modified through the API. They can only be updated from inside HubSpot, but it's possible to pull any custom options that may have been set for the property through the contact properties endpoints. Since individual HubSpot accounts may not use the default settings, using these endpoints to get the property options is recommended.

For more details about this property and how it might be used in HubSpot, please see this  
[knowledge base article.](https://knowledge.hubspot.com/articles/kcs_article/contacts/how-can-i-track-lawful-basis-of-processing-in-hubspot)  

### Handling privacy compliant contact deletions

HubSpot users have the ability to permanently delete a contact record to comply with privacy laws. Please see [this knowledge base article](https://knowledge.hubspot.com/articles/kcs_article/contacts/how-do-i-perform-a-gdpr-compliant-delete-in-hubspot) for more information.

You can subscribe to the `contact.privacyDeletion` subscription type to receive webhook notifications when a user performs a privacy compliant contact deletion. Please see the [Webhooks Overview](/docs/methods/webhooks/webhooks-overview) for more details on webhooks and [handling these notifications](https://developers.hubspot.com/docs/methods/webhooks/webhooks-overview#privacy-deletions).

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/faq#page-feedback)
--------------------------------------------------------------------------------

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