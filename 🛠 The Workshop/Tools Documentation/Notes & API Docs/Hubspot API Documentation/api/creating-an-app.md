---
title: "Public Apps in HubSpot"
description: "A type of integration that can be installed on customer accounts or listed on the App Marketplace, requiring authentication via OAuth."
type: "group"
tags:
- "HubSpot"
- "Integration"
- "OAuth Authentication"
relationships:
- "#part_of [[HubSpot]]"
- "#requires [[Authentication]]"]]
- "#enables [[API Calls]]"
founded: "N/A"
---

Public apps
===========

In HubSpot, a public app is a type of integration that can be installed on customer accounts or listed on the App Marketplace. It requires authentication via **[OAuth](https://developers.hubspot.com/docs-beta/working-with-oauth)**. Once a user [installs](#installing-apps) your app on their HubSpot account, you’ll be able to make API calls to that account using an [OAuth access token](/docs/api/oauth/tokens). Your app will also appear in the account’s Connected Apps settings.

Connected apps are also able to take advantage of [subscribing to changes using webhooks](https://developers.hubspot.com/docs-beta/webhooks) and creating custom [timeline events](/docs/api/crm/timeline). 

Below, learn how to:

*   [Create a public app](#create-a-public-app)
*   [Install a public app in an account](#install-an-app)
*   [Manage the app, including monitoring usage](#manage-public-apps-in-hubspot)
*   [Add a verified domain to the app](#add-a-verified-domain)

Create a public app[](https://developers.hubspot.com/docs/api/creating-an-app#create-a-public-app)
--------------------------------------------------------------------------------------------------

When you create an app in HubSpot, you're essentially associating an app you've built with an [app developer account](https://app.hubspot.com/signup/developers). To get started creating your HubSpot app:

*   In your app developer account, navigate to **Apps** in the main navigation bar. 
*   In the upper right, click **Create app**.
*   Next, fill out some basic information and settings for your app. When users authenticate your app with their HubSpot account, they’ll see the name, description, logo, and any support contact info you provide on this page.

**Please note**: the app name will be used wherever your app displays in HubSpot. This includes when installing the app as well as the _Powered by_ footer for [CRM cards](/docs/api/crm/extensions/custom-cards) and [timeline events](/docs/api/crm/timeline).

![](https://developers.hubspot.com/hs-fs/hubfs/new_app_setup.png?width=600&name=new_app_setup.png)

*   Click the Auth tab to view your client ID and client secret, as well as the app's assigned scopes. You'll need this information when [initiating an OAuth connection](https://developers.hubspot.com/docs-beta/working-with-oauth) between your app and HubSpot.

![](https://developers.hubspot.com/hs-fs/hubfs/app_auth_settings.png?width=600&name=app_auth_settings.png) 

### Configure scopes[](https://developers.hubspot.com/docs/api/creating-an-app#configure-scopes)

Scopes determine your app's permissions to access data sources or tools in an account that's installed your app. The scopes you configure will appear as the `scope` and `optional_scope` query parameters in an install URL that you can then provide to users.

#### Scope types

On the _Auth_ tab, there are three different scope types available for you to configure. You must specify the scopes your app will require for installation, but you can also specify two other scope types: conditionally required scopes and optional scopes.

*   **Required scopes:** scopes that must be authorized by the user and must be present in the `scope` query parameter in your app's install URL for successful installation.
*   **Conditionally required scopes:** scopes that must be authorized by the user only if they're present in the `scope` query parameter in your app's install URL for successful installation.
    *   This scope type allows you to be flexible and provide a separate install URL for tiered features or scopes that are only required when users enable certain features in your app. For example, you could offer two install URLs to your users: one install URL could include the conditionally required scope in the `scope` query parameter for users with access to a feature, while another install URL omits that scope in the `scope` query parameter for users without access.
    *   If a conditionally required scope is present in your app install URL and a user without access to the associated feature attempts to install your app using that URL, the installation will fail.
*   **Optional scopes:** scopes that are not required to successfully install your app. These scopes are specified in the `optional_scope` query parameter in your app's install URL. For example, if you want your app to be able to fetch [custom object](/docs/api/crm/crm-custom-objects) data (which is only available to _Enterprise_ HubSpot accounts), you could add the `crm.objects.custom.read` scope as an optional scope. Then, if an account has access to the custom objects, the scope will be authorized. Otherwise, they’ll still be able to install the app without the custom objects scope.

#### Configure your public app scopes

To customize your scope settings and add new scopes:

*   To configure conditionally required or optional scopes, click to the toggle the **Turn on advanced scope settings** switch on.

![turn-on-advanced-scope-settings-toggle-in-public-app-auth-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/turn-on-advanced-scope-settings-toggle-in-public-app-auth-tab.png?width=700&height=89&name=turn-on-advanced-scope-settings-toggle-in-public-app-auth-tab.png)

**Please note:** starting October 21, 2024, advanced scope settings will be required for all apps. Learn more on [HubSpot's Developer Changelog](/changelog/advanced-auth-and-scope-settings-for-public-apps).

*   In the _Scopes_ section, click **Add new scope**.
*   In the right panel, use the **search bar** to search for a scope, then select the **checkbox** next to any scope you want the user to authorize. If you turned on advanced scope settings, click the **dropdown menu** next to the scope and select a **scope type**.
*   Click **Update**.

![add-new-scope-panel-in-public-app-setup](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/add-new-scope-panel-in-public-app-setup.png?width=550&height=764&name=add-new-scope-panel-in-public-app-setup.png)

*   Review your configured scopes. If you turned on advanced scope settings, you can switch the scope type of any scope by clicking the **dropdown menu** next to the scope. You can also click **Delete** to remove one of your app's scopes.

![review-new-scope-settings-in-public-app-setup](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/review-new-scope-settings-in-public-app-setup.png?width=700&height=515&name=review-new-scope-settings-in-public-app-setup.png)

*   Once you've finished setting up your app settings, click **Create app** in the bottom left.

With your app created, you can now walk through the installation process.

**Please note:** it's recommended to [add a verified domain](#add-a-verified-domain) to the app to add another level of trust for users installing your app. Otherwise, the app will display a banner stating that the app is not verified.

Install an app[](https://developers.hubspot.com/docs/api/creating-an-app#install-an-app)
----------------------------------------------------------------------------------------

**Please note:** before installing your app, keep in mind the following:

*   An app won’t appear on an account’s _Connected Apps_ page until the initial access and refresh tokens are created.
*   Only users with with access to an app’s required or conditionally required scopes can install an app.
*   Apps can’t be installed on developer accounts. To test your app, you’ll need to create a [test account](https://developers.hubspot.com/docs-beta/creating-test-accounts) in your app developer account and install it there.

App installation can be broken down into two steps: authorization and token generation.

### Authorize your app with a customer account 

*   To authorize your app with a HubSpot account, you’ll need to create an authorization URL. Do this by getting the client ID for your app and [initiating the OAuth process](https://developers.hubspot.com/docs-beta/working-with-oauth).
*   Once your URL is ready, open it in your browser to see a list of all your HubSpot accounts. This is also what users will see once you begin directing them to this URL.
*   Select the **account** where you want to install your app.

![select_account-1](https://428357.fs1.hubspotusercontent-na1.net/hubfs/428357/select_account-1.webp)

*   After choosing an account, you'll be presented with a list of scopes based on the `&scope=` and `&optional_scope=` parameters you set for the authorization URL.

**Please note:** if you include an `optional_scope` and the selected account doesn't have access to it (such as the content scope for a CRM-only account), it will not be listed.

*   Click **Grant access** to authorize the connection.

![approve_scopes-1](https://428357.fs1.hubspotusercontent-na1.net/hubfs/428357/approve_scopes-1.webp)

*   After granting access, you'll be redirected based on the `&redirect_uri=` parameter in the original authorization URL, and a `?code=` parameter will be appended to the URL. Use that code in the next step to generate an access token.

### Generate the initial OAuth tokens 

To generate your refresh and initial access tokens, you’ll need the code from the `?code=` parameter of the authorization URL, `redirect_url`, client ID, and client secret. Detailed instructions are [here](https://developers.hubspot.com/docs-beta/working-with-oauth). 

Once you’ve authorized your app and generated the initial tokens, installation is complete. It’ll be listed on your [Connected Apps](https://app.hubspot.com/l/integrations-beta?_ga=2.4127344.1956280234.1584921781-1635676776.1568129882) page, and you’ll start getting [webhook](/docs-beta/webhooks) and [CRM Cards](https://developers.hubspot.com/docs-beta/crm/extensions) fetch requests.

![connected_apps-1](https://428357.fs1.hubspotusercontent-na1.net/hubfs/428357/connected_apps-1.webp) 

Manage public apps in HubSpot[](https://developers.hubspot.com/docs/api/creating-an-app#manage-public-apps-in-hubspot)
----------------------------------------------------------------------------------------------------------------------

### Find an app's ID[](https://developers.hubspot.com/docs/api/creating-an-app#find-an-app-s-id)

You can find a public app's ID in your app developer account using either of the methods below:

*   In your developer account, navigate to **Apps** in the main navigation bar, then view the _App ID_ listed below the name of your app.

![find-app-id](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/find-app-id.png?width=654&height=227&name=find-app-id.png)

*   In your developer account, navigate to **Apps** in the main navigation bar, then click the **name** of the app. On the _Basic info_ page, click the **Auth** tab, then view the _App ID_.

![find-app-id-auth-settings](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/find-app-id-auth-settings.png?width=654&height=233&name=find-app-id-auth-settings.png)

### Monitor app behavior[](https://developers.hubspot.com/docs/api/creating-an-app#monitor-app-behavior)

HubSpot logs all requests made to or from a connected app, including incoming requests using an [OAuth access token](/docs/api/oauth/tokens) or outgoing requests for webhooks or CRM cards. 

To view this request log:

*   In your developer account, navigate to **Apps** in the main navigation bar.
*   Click the **name** of the app.
*   In the left sidebar menu, navigate to **Monitoring**. 
*   Use the tabs to view different types of requests being made to or from the app. While viewing these logs, you can click an individual request to view more information about it, including:
    *   for successful requests, the request method, path, and time of request.
    *   for unsuccessful requests, additional error information such as response headers and body.

![request_details](https://428357.fs1.hubspotusercontent-na1.net/hubfs/428357/request_details.webp)

Below, learn more about each tab of the _Monitoring_ page.

*   **API calls:** the _API calls_ tab shows all requests made to your app using an OAuth access token. It can be filtered by HTTP method, response code, timeframe, or request URL.
*   **Webhooks:** the Webhooks tab shows HubSpot requests for any of your app’s [webhook subscriptions](https://developers.hubspot.com/docs-beta/webhooks). Filter by response (including timeouts and connection failures), status (success, will retry, or failure), subscription type, time frame, attempt, batch, event, or account ID. 

**Please note:** the attempt ID is a combination of the `subscriptionId`, `eventId`, and `attemptNumber` from a specific request.

*   **CRM extensions:** the CRM extensions tab shows requests for your app’s [CRM cards](https://developers.hubspot.com/docs/api/crm/extensions/custom-cards). Filter by extension object type, CRM object type (contact, company, ticket, or deal), error or warning type, time frame, request ID, or CRM record ID (i.e. a specific contact ID).
*   **App settings:** the _App settings_ tab enables you to configure the [settings page](/docs/api/create-an-app-settings-page) that comes with your app.

On each tab, if any associated events occurred in the last 30 days (e.g., a webhook trigger occurred or an API call was made), you can click Export logs to export the associated event data to a CSV:

*   In the dialog box, configure how many days' worth of data to export (up to 30 days).
*   Click **Export**. An email notification will be sent to the email address associated with your user in your HubSpot settings.

Add a verified domain[](https://developers.hubspot.com/docs/api/creating-an-app#add-a-verified-domain)
------------------------------------------------------------------------------------------------------

When HubSpot users install an app, they consent to give the app’s developer access to their account data. The developer’s identity and reputation each play an important role in a user’s decision to continue with the install. To ensure full user consent when installing an app, HubSpot will display a message on the app install screen to indicate the app's level of verification and App Marketplace listing:

*   When an app doesn't have a verified domain, HubSpot will display a banner on the install screen that says the app has not been verified.  
    ![not-verified](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/not-verified.png?width=705&height=335&name=not-verified.png)
*   When app has a verified domain but is not [listed on the App Marketplace](/docs/api/listing-your-app), HubSpot will display the verified domain along with a banner on the install screen that says the app has not been reviewed or approved by HubSpot. ![verified-not-listed](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/verified-not-listed.png?width=705&height=354&name=verified-not-listed.png)
*   When an app has been listed on the marketplace, passing HubSpot's app review process, HubSpot will not display either of the above banners. You're not required to verify the domain if your app has been listed on the App Marketplace.  
    ![verified-and-listed](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/verified-and-listed.png?width=705&height=243&name=verified-and-listed.png)

### Add a verified domain

To add a verified domain to the app, you'll need to first add the domain to the app's settings, then add a TXT record to the domain's DNS settings:

*   In your app developer account, navigate to **Apps**.
*   Click the **name** of the app.
*   In the left sidebar, navigate to **Contact & support**.
*   In the _Company domain_ field, enter your domain, then click **Save**. A message will appear below the _Company domain_ stating that the domain has not yet been verified.
*   Click **Verify it now** to begin the verification process.

![domain-verification-for-app](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/domain-verification-for-app.png?width=667&height=399&name=domain-verification-for-app.png)

  

*   In the right panel, confirm that the domain has been entered correctly, then click **Next**.
*   Copy the required TXT record value by clicking **Copy** in the _Value_ column.  
    ![verify-app-domain-copy-value](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/verify-app-domain-copy-value.png?width=694&height=514&name=verify-app-domain-copy-value.png)
*   In your DNS provider, create a TXT record with the copied value. Below are instructions for some common DNS providers:
    *   [GoDaddy](https://www.godaddy.com/help/add-a-txt-record-19232)
    *   [BlueHost](https://my.bluehost.com/hosting/help/559#add)
    *   [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237)
    *   [Cloudflare](https://support.cloudflare.com/hc/en-us/articles/360019093151-Managing-DNS-records-in-Cloudflare#h_60566325041543261564371)
    *   [Hover](https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-AAAA-CNAME-MX-TXT-SRV-)
    *   [Name](https://www.name.com/support/articles/115004972547-Adding-a-TXT-Record)
    *   [United Domains](https://help.uniteddomains.com/hc/en-us/articles/115000887125-How-to-set-up-a-TXT-record-on-a-domain-name)
*   After updating your DNS settings, navigate back to HubSpot, then click **Next** in the right panel. DNS records can take up to 48 hours to update, so HubSpot might not recognize the change immediately. You can get back to this screen any time by selecting **Verify it now** again from the _Company info_ settings page.
*   Once verified, you'll see a success status indicator under the _Company domain_ field.

![Domain verified__export](https://developers.hubspot.com/hubfs/Domain%20verified__export.png)

#### Additional Notes

*   To ensure continued ownership of the domain, HubSpot will continue to verify that the TXT record is present on a regular basis. The install warning will return if the TXT record is removed or modified.
*   Currently, you can only have one verified domain per developer account. All apps in an account share the verified domain. The domain on the install page will link to your root domain.
*   If you delete your verified domain, all apps in your developer account will get the install warning again. You can verify another domain, but the process will take a couple hours. 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/creating-an-app#page-feedback)
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