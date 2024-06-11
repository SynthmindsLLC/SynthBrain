---
title: "Private Apps in HubSpot"
description: "Allows you to use HubSpot's APIs to access specific data from your account, requiring super admin permissions for access and management."
type: "group"
tags:
- "HubSpot"
- "API"
- "Private Applications"
relationships:
- "#requires [[Super Admin]]"
- "#part_of [[Integration Settings]]"
founded: "N/A"
---

Private apps
============

Private apps allow you to use HubSpot's APIs to access specific data from your HubSpot account. You can authorize what each private app can request or change in your account, which will generate an access token that's unique to your app. 

You must be a [super admin](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#super-admin) to access private apps in your HubSpot account.

**Please note:** private apps do not support custom timeline events. Webhooks are [supported in private apps](/docs/api/create-and-edit-webhook-subscriptions-in-private-apps), but subscriptions cannot be edited programmatically via an API, and must instead be edited in your private app settings.  
  
If you plan on building an app using custom timeline events, you should create a public app instead. Learn more about the [differences between private and public apps](/docs/api/developer-tools-overview).

Create a private app[](https://developers.hubspot.com/docs/api/private-apps#create-a-private-app)
-------------------------------------------------------------------------------------------------

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar menu, navigate to **Integrations** > **Private Apps**.
*   Click **Create private app**.
*   On the _Basic Info_ tab, configure the details of your app:
    *   Enter your app's **name**.
    *   Hover over the placeholder logo and click the **upload icon** to upload a square image that will serve as the logo for your app.
    *   Enter a **description** for your app.
*   Click the **Scopes** tab.
*   Select the **Read** or **Write** checkbox for each scope you want your private app to be able to access. You can also search for a specific scope using the _Find a scope_ search bar. You can review a full list of available scopes in [this reference article](/docs/api/scopes).
*   After you're done configuring your app, click **Create app** in the top right.

![updated-read-write-scope-config-private-apps](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/updated-read-write-scope-config-private-apps.png?width=746&name=updated-read-write-scope-config-private-apps.png)

*   In the dialog box, review the info about your app's access token, then click **Continue creating**.

Once you've created your app, you can start making API calls using the app's access token. If you need to edit your app's info or change its scopes, click Edit details.

![edit-details-of-private-app](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/edit-details-of-private-app.png?width=476&name=edit-details-of-private-app.png) 

Make API calls with your app's access token[](https://developers.hubspot.com/docs/api/private-apps#make-api-calls-with-your-app-s-access-token)
-----------------------------------------------------------------------------------------------------------------------------------------------

**Please note:** private apps will lose access to scopes when your HubSpot account is downgraded and loses access to functionality. For example, if your account does not have access to HubDB, your private app will not have access to the HubDB scope.

Private app access tokens will be updated to reflect available scopes in your HubSpot account and what you configured for the private app, but the token string itself will not change. 

To start making API calls, navigate to the details page of your app.

*   On the _Access_ _token_ card, click **Show token** to reveal your access token. Click **Copy** to copy the token to your clipboard.

![show-private-app-access-token-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/show-private-app-access-token-1.png?width=746&name=show-private-app-access-token-1.png)

*   You can then paste the access token to provide it to your developers, or use it yourself as you develop your app. When making a call to one of the HubSpot API endpoints, set the value of the _Authorization_ field to **Bearer \[YOUR\_TOKEN\]**. For example, if you're making a call to the [Contacts API](/docs/api/crm/contacts) using Node.js and [axios](https://www.npmjs.com/package/axios), the request would look like the following:

axios.get('https://api.hubapi.com/crm/v3/objects/contacts', { headers: { 'Authorization': \`Bearer ${YOUR\_TOKEN}\`, 'Content-Type': 'application/json' } }, (err, data) => { // Handle the API response } );

*   Private app access tokens are implemented on top of OAuth, so you can also make authenticated calls with your access token using one of HubSpot's client libraries. For example, if you're using the [Node.js client library](https://github.com/HubSpot/hubspot-api-nodejs), you can instantiate an OAuth client by passing in your app's access token:

const hubspotClient = new hubspot.Client({ accessToken: YOUR\_ACCESS\_TOKEN });

View private app access token information[](https://developers.hubspot.com/docs/api/private-apps#view-private-app-access-token-information)
-------------------------------------------------------------------------------------------------------------------------------------------

To view information about a private app's access token, such as the Hub ID and scopes associated with the token, make a `POST` request to `/oauth/v2/private-apps/get/access-token-info`. In the request body, include your access token:

// POST request response body { "tokenKey": {{accessToken}} }

The response will include information about the user who created the token, the Hub ID of the account, the private app ID, and the scopes associated with the token.

// Example response body { userId:123456, hubId:1020304, appId:2011410, scopes:\[ "oauth", "crm.schemas.companies.write"\] }

Rotate your access token[](https://developers.hubspot.com/docs/api/private-apps#rotate-your-access-token)
---------------------------------------------------------------------------------------------------------

If you access token is lost or otherwise compromised, you can rotate the token. A new access token will be created and the original access token will expire.

*   In your HubSpot account, click the **Settings** page in the main navigation bar.
*   Navigate to **Integrations** > **Private Apps**.
*   Click the **name** of your private app.
*   Next to your access token, click **Rotate**:
    *   If your token is compromised and you want to immediately revoke access, click **Rotate and expire now**.
    *   If there's no imminent threat to your token, it's still recommended that you rotate your token every six months. If you're ready to initiate a regular rotation of your token, click **Rotate and expire later**, which will trigger an expiration of the token in 7 days.
        *   If your app is ready to transition earlier, you can click **Expire now**.
        *   If you decide you need more time, you can click **Cancel rotation**, which will cancel the expiration of the original token and revoke the new access token.

![rotate-private-app-access-token](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/rotate-private-app-access-token.png?width=959&name=rotate-private-app-access-token.png)

HubSpot will also send email notifications to [super admins](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#super-admin) with reminders about access token rotation status, as well as other related alerts. Super admins in your HubSpot account will receive notifications for the following events and reminders:

*   A super admin initiated a rotation (either immediately or scheduled for 7 days from now).
*   A super admin canceled a pending rotation.
*   A super admin opted to expire an access token immediately by clicking **Expire now** instead of waiting 7 days for the token to expire.
*   The app's access token is about to expire in 24 hours.
*   The app's access token has been rotated and expired after 7 days.
*   If you haven't rotated your access token in over 180 days, super admins will also receive a reminder email to rotate your app's access token.

View API call logs[](https://developers.hubspot.com/docs/api/private-apps#view-api-call-logs)
---------------------------------------------------------------------------------------------

To review the API calls your app has made in the past 30 days:

*   On the details page of your app, click the **Logs** tab.
*   Review and filter your private app API calls:
    *   Click the **Method** and **Response** dropdown menus to filter your historical API calls by request method or response code.
    *   Click the **start date** or **end date** dropdown menus to narrow your call logs to a specific time range.
    *   You can also search for specific calls by URL in the _Search by request URL_ search box.

![private-app-logs-tab-updated](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/private-app-logs-tab-updated.png?width=746&height=378&name=private-app-logs-tab-updated.png)

*   To export the API call logs, click **Export logs (CSV)**. Then, specify a **date range** (up to the past 30 days) and click **Export**.
*   In the pop-up box, select the **date range** of API calls you want to export and click **Export**. You will receive an email with a download link when the export is ready. 

Private app limits[](https://developers.hubspot.com/docs/api/private-apps#private-app-limits)
---------------------------------------------------------------------------------------------

You can create up to 20 private apps in your HubSpot account. Each private app is subject to [HubSpot's API usage guidelines](/docs/api/usage-details). The number of calls your private app can make is based on your account subscription and whether you've purchased the API add-on:

|   | Product Tier | Per 10 Seconds | Per Day |
| --- | --- | --- | --- |
| Private Apps | 
(Any Hub)

Free and Starter

 | 100 / private app | 250,000 / account |
|   | 

(Any Hub)

Pro and Enterprise

 | 150 / private app | 500,000 / account |
| Private Apps with API Add-on | 

(Any Hub)

Free, Starter, Professional, and Enterprise

 | 200 / private app | 1,000,000 / account |

If you have both a Starter and Professional plan, limits for the higher tier (Professional) apply to your account.

You can make a `GET` request to `/account-info/v3/api-usage/daily/private-apps` to review the daily API usage for all private apps in your HubSpot account. Learn more about using the [account information API](/docs/api/settings/account-information-api).

Delete a private app[](https://developers.hubspot.com/docs/api/private-apps#delete-a-private-app)
-------------------------------------------------------------------------------------------------

When you delete one of your private apps, its access token will be permanently revoked and you'll no longer be able to use it to make API calls.

To delete an app:

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   Click the **name** of your private app.
*   At the top of the page, click the **Auth** tab.
*   At the bottom of the page, click **Delete \[name of your app\]**.
*   In the dialog box, type the name of your app to confirm its deletion, then click **Delete**.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/private-apps#page-feedback)
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