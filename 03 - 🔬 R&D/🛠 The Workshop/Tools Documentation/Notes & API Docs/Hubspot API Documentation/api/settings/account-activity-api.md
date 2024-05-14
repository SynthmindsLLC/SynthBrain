Account activity
================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The following endpoints provide information about [login](https://knowledge.hubspot.com/account/export-account-activity-history#account-login-history) and [security activity](https://knowledge.hubspot.com/account/export-account-activity-history#security-activity-history) in your HubSpot account.

Get a centralized audit log of user actions
-------------------------------------------

Use this endpoint to export of a [centralized audit log](https://knowledge.hubspot.com/view-and-export-account-activity-history-in-a-centralized-audit-log) of user actions across your account (Enterprise subscriptions only). In order to utilize this endpoint, you must first follow the documentation on [making API calls with your app's access token](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token).

For each centralized audit log, the response body will show:

*   user action category (e.g. CRM object, login)
*   user action subcategory (e.g. playbook, login succeeded)
*   user action (e.g. create, update, perform)
*   the ID of the affected object
*   the time and date the action occurred
*   the user's email address

Get login activity for your HubSpot account
-------------------------------------------

Use this endpoint to retrieve the previous 90 days of user login history. This includes login attempts to app.hubspot.com and the HubSpot mobile app. Login history exports contain the following information about each login attempt:

*   login timestamp
*   user email address
*   IP address
*   location
*   type of login
*   user agent (information about the device used for logging in)

Get security activity for your HubSpot account
----------------------------------------------

Use this endpoint to export security activity history to see a list of security-related actions that users have taken in the account. For each user action, the response body will show:

*   the time of the action
*   the type of action
*   the user's email address
*   the ID of the affected object
*   the approximate location
*   a link to the URL where the action was taken in the account 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/settings/account-activity-api#page-feedback)
----------------------------------------------------------------------------------------------------------

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