Business Units
==============

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The following endpoint provides information about [business units](https://knowledge.hubspot.com/account-settings/manage-brands-with-business-unit) tied to a user. This may also include information about [logos](https://knowledge.hubspot.com/account-settings/edit-your-logo-favicon-and-brand-colors).

**Please note:** the business units API currently only supports retrieving business unit data and does not support associating assests with a business unit, nor creating a new business unit.

Get business units tied to a user
---------------------------------

To get the business units that a user has access to, you can make a `GET` request to

`/business-units/v3/business-units/user/{userId}`

The following is an example of what the response body should include:

// Example GET request to /business-units/v3/business-units/user/{userId} { "logoMetadata": { "logoAltText": "logo sample text", "resizedUrl": "sillystring", "logoUrl": "examplelogourl.com" }, "name": "sample business unit name", "id": "101" }

For more information on how to use the business units API, click the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/settings/business-units-api#page-feedback)
--------------------------------------------------------------------------------------------------------

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