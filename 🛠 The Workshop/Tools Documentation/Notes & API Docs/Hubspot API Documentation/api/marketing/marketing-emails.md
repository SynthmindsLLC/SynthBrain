---
title: "Marketing Email API"
description: "Programmatically create, update, and get details about marketing emails using the Marketing Emails API. Query post-send statistics of a specific email or set of emails. Excludes sales emails created via contact record. Transactional emails use Single-send API. Requires _Marketing Hub_ Professional or Enterprise account for `/publish` and `/unpublish` endpoints."
type: "group"
tags:
- "Email"
- "API"
- "HubSpot"
relationships:
- "#related_to [[Single-send API]]"
- "#requires [[Marketing Hub Professional or Enterprise account]]"
- "#part_of [[Marketing Hub]]"
- "#used_for [[Creating Marketing Emails]], [[Updating Marketing Emails]], [[Retrieving Marketing Email Details]], [[Querying Post-send Statistics]]"
- "#used_by [[Developers]]"
- "#different_from [[Engagements API]]"
---

.interest-form { padding: 1em; display: none; height: 100%; } .interest-text { padding: 1em; } .hs-form>fieldset { max-width: 100% !important; }

**Access and test APIs in beta.** 
----------------------------------

**Please note**: This API is currently in beta and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to our [Developer Terms](https://legal.hubspot.com/hubspot-developer-terms)& [Developer Beta](https://legal.hubspot.com/developerbetaterms?)Terms. You also acknowledge and understand the risk associated with testing an unstable API. 

  

* * *

Marketing Email (BETA)
======================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

If you have a _**Marketing Hub** Professional_ or _Enterprise_ account, you can use the Marketing Emails API to programmatically create, update, and get details about marketing emails. You can also query details about the post-send statistics of a specific email or set of emails. These statistics should match what you can access in the app on the _Details_ section of a particular email and will be returned under the stats object in your JSON response.

The Marketing Email API cannot be used to create or retrieve data for sales emails that are created and sent via the contact record. To get details for sales emails, use the Engagements API.

**Please note:**

*   To programmatically send transactional emails to contacts, use the [Single-send API](/docs/api/marketing/transactional-emails#single-send-api).
*   To use the `/publish` and `/unpublish` endpoints, you must have a _**Marketing Hub**_ _Enterprise_ account or the [transactional email add-on](https://www.hubspot.com/products/marketing/transactional-email).

Create a marketing email[](https://developers.hubspot.com/docs/api/marketing/marketing-email#create-a-marketing-email)
----------------------------------------------------------------------------------------------------------------------

To create an email, make a `POST` request to `/marketing/v3/emails` and include the following fields in the body of your request:

// Example request body for POST request to /marketing/v3/emails { "name": "A new marketing email", "subject": "Behold the latest version of our newsletter!", "templatePath": "@hubspot/email/dnd/welcome.html" }

**Please note:** if you purchased the [business units add-on](https://knowledge.hubspot.com/account-settings/manage-brands-with-business-unit), you must include the `businessUnitId` field in the request body. You can get a list of business units in your account using the [business units API](/docs/api/settings/business-units-api).

Retrieve a marketing email[](https://developers.hubspot.com/docs/api/marketing/marketing-email#retrieve-a-marketing-email)
--------------------------------------------------------------------------------------------------------------------------

You can retrieve existing emails in your account individually or in batches:

*   To retrieve an individual email, make a `GET` request to `/marketing/v3/emails/{emailId}`
*   To retrieve a list of all emails, make a `GET` request to `/marketing/v3/emails`, and include any filters as query parameters in your request (e.g., add `createdAfter` and a date in ISO8601 format to get all emails created after a specific date).

Click the Endpoints tab at the top of this article for a full list of endpoints and the associated parameters available.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/marketing/marketing-email#page-feedback)
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