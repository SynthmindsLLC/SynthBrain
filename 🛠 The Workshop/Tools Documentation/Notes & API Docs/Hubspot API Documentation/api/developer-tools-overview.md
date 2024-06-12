---
title: "Building apps overview"
description: "Apps enable you to authenticate API calls to your HubSpot account, subscribe to events with webhooks, and extend the HubSpot UI, such as with custom cards. HubSpot offers several types of apps and extensions depending on your integration's needs. Below, learn more about the types of apps and extensions you can build with HubSpot, how to get started building them, and how to manage them in HubSpot."
type: "work"
tags:
- "HubSpot"
- "App_Development"
- "API_Integration"
relationships:
- "#related_to [[Private Apps]]"
- "#related_to [[Public Apps]]"
- "#related_to [[Projects (BETA)]]"
- "#related_to [[Supported Extensions by App Type]]"
- "#related_to [[Types of Accounts for App Development]]"
- "#related_to [[Authentication]]"
- "#related_to [[Developer Account API Keys]]"
- "#related_to [[Delete a Developer Account]]"
- "#related_to [[Share Feedback]]"
---

Building apps overview
======================

Apps enable you to authenticate API calls to your HubSpot account, subscribe to events with webhooks, and extend the HubSpot UI, such as with custom cards. HubSpot offers several types of apps and extensions depending on your integration's needs. Below, learn more about the types of apps and extensions you can build with HubSpot, how to get started building them, and how to manage them in HubSpot.

Types of apps[](https://developers.hubspot.com/docs/api/developer-tools-overview#types-of-apps)
-----------------------------------------------------------------------------------------------

Depending on the type of integration you want to build, you’ll need to choose the right type of app. Below, learn more about the types of apps that you can build and the functionalities that they support.

For building extensions, [view the reference table below](#supported-extensions-by-app-type) for a quick overview of which extensions can be built with which types of apps.

### Private apps[](https://developers.hubspot.com/docs/api/developer-tools-overview#private-apps)

Private apps can be created for a single HubSpot account, and are best suited for one-off scripts or single-purpose extensions. For example, you might build a private app for your HubSpot account to:

*   Create a new custom object through the API.
*   Import CRM records from a CSV file.
*   Authenticate API requests in custom automation actions and chat bots.
*   [Create and edit webhook subscriptions](/docs/api/create-and-edit-webhook-subscriptions-in-private-apps).

In general, private apps are simpler to implement than public apps. Private apps authenticate with access tokens and cannot be listed on the HubSpot App Marketplace. Learn more about [when to build private apps](https://developers.hubspot.com/blog/hubspot-integration-choosing-private-public-hubspot-apps).

If this type of app fits your needs, [get started creating a private app in your HubSpot account](https://developers.hubspot.com/docs/api/private-apps).

#### Private apps in projects (BETA)[](https://developers.hubspot.com/docs/api/developer-tools-overview#private-apps-in-projects-beta-)

Private apps built with projects enable you to create UI extensions for CRM records. The difference when building a private app through this method is that projects only support creating UI extensions, which private apps outside of projects cannot create.

If this type of app fits your needs, check out the [projects quickstart guide](/docs/platform/projects-quick-start-guide) to get started creating a private app and project using the CLI.

### Public apps[](https://developers.hubspot.com/docs/api/developer-tools-overview#public-apps)

Public apps can be installed in multiple accounts. In addition to the types of extensions you can build with a private app, public apps support advanced functionality, such as:

*   Subscribing to account-wide events using the webhooks API.  
*   Creating custom timeline events on CRM records using the timeline events API. 
*   Creating custom app settings pages in HubSpot. 

Public apps authenticate with OAuth and can be listed on the HubSpot App Marketplace. Learn more about [when to build public apps](/blog/hubspot-integration-choosing-private-public-hubspot-apps).

If this type of app fits your needs, [get started creating a public app in your app developer account](/docs/api/creating-an-app).

### Supported extensions by app type[](https://developers.hubspot.com/docs/api/developer-tools-overview#supported-extensions-by-app-type)

| App type | Supported extensions |
| --- | --- |
| Private app | 
*   [Video conference extension](https://developers.hubspot.com/docs/api/crm/extensions/video-conferencing)

 |
| Public app | 

*   [Calling SDK](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk)
*   [CRM cards](https://developers.hubspot.com/docs/api/crm/extensions/custom-cards)\*
*   [Timeline events](https://developers.hubspot.com/docs/api/crm/timeline)
*   Video conference extension

 |
| Private app built with projects (BETA) | 

*   [UI extensions](/docs/platform/create-custom-crm-cards-with-projects)

 |

\* The CRM cards you can build with public apps are different from the custom cards you can create as [UI extensions with projects (BETA)](/docs/platform/create-ui-extensions). UI extensions offer more advanced functionality and customizable components.

Types of accounts for app development[](https://developers.hubspot.com/docs/api/developer-tools-overview#types-of-accounts-for-app-development)
-----------------------------------------------------------------------------------------------------------------------------------------------

While app developer and test accounts work together, they each serve a distinct purpose.

*   App developer accounts are intended for building and listing apps on the App Marketplace.
*   Test accounts intended for testing APIs and apps you’re building without impacting data in a real HubSpot account. This is separate from a sandbox account that you can create within standard HubSpot accounts.

Learn more about [HubSpot's account types](/docs/api/account-types).

Authentication[](https://developers.hubspot.com/docs/api/developer-tools-overview#authentication)
-------------------------------------------------------------------------------------------------

If you want to build a custom integration with a single HubSpot account, you can create a [private app](/docs/api/private-apps) and use its [access token](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token) to authenticate API calls, or you can use [OAuth](/docs/api/working-with-oauth) with a public app. Any app designed for installation by multiple HubSpot accounts or listing on the App Marketplace must use OAuth. 

**Please note:** as of November 30, 2022, HubSpot API Keys are being deprecated and are no longer supported. Continued use of HubSpot API Keys is a security risk to your account and data. During this deprecation phase, HubSpot may deactivate your key at any time.

You should instead authenticate using a private app access token or OAuth. Learn more about [this change](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) and how to [migrate an API key integration](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app) to use a private app instead.

If you want to subscribe to webhooks or set up [OAuth for your app](/docs/api/working-with-oauth?), you should [create a developer account](https://app.hubspot.com/signup/developers). With developer accounts, you can also [list your apps](/docs/api/listing-your-app) on the App Marketplace or [create a test account](/docs/api/creating-test-accounts).

### Developer account API keys

To manage your app settings through the API, you can use a developer API key. This API key is separate from standard API keys, which have been deprecated. Developer API keys can be used for managing subscriptions for the [Webhooks API](/docs/api/webhooks) and [creating or updating event types for the timeline events feature](/docs/api/crm/timeline). All other API calls need to be made using a [private app access token](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token) or OAuth.

To access your app developer account API key:

*   In your app developer account, navigate to **Apps** in the top navigation bar.
*   In the upper right, click **Get HubSpot API key**.
*   In the dialog box, click **Show key**. The key will be revealed, and you can then click **Copy** next tot he key.
*   You can also deactivate the previous API key and generate a new one by clicking **Regenerate key**.

![show_dev_api_key](https://428357.fs1.hubspotusercontent-na1.net/hubfs/428357/show_dev_api_key.webp)

Delete a developer account[](https://developers.hubspot.com/docs/api/developer-tools-overview#delete-a-developer-account)
-------------------------------------------------------------------------------------------------------------------------

You can delete app developer accounts if they don’t contain apps with installations or active marketplace listings. If your account has apps with installations or active marketplace listings and you’d like to delete your account, please reach out to support for assistance.

Once you delete your account, you will no longer be able to access that account. If you can switch between multiple HubSpot accounts, the deleted account will no longer appear.

In your HubSpot API developer account, click your account name in the top right corner, then click on **Account.**

![account](https://developers.hubspot.com/hs-fs/hubfs/account.jpeg?width=334&name=account.jpeg)

Click **Delete account.** If your account has any apps with installations or active marketplace listings this button will be disabled.

![Account2](https://developers.hubspot.com/hs-fs/hubfs/Account2.jpg?width=984&name=Account2.jpg)

In the dialog box, enter your account ID then click **Delete developer account**

![Confirm2](https://developers.hubspot.com/hs-fs/hubfs/Confirm2.jpg?width=603&name=Confirm2.jpg) 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/developer-tools-overview#page-feedback)
-----------------------------------------------------------------------------------------------------

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