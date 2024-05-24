What to build
=============

There are several different development routes possible with HubSpot, depending on your goals. You’ll find a high-level overview of each route on this page, along with the tooling and accounts you’ll need for each. You'll also find links to detailed docs to give you more context, as well as relevant quickstart guides.

*   [Use APIs and build integrations](#use-apis-and-build-integrations)
    *   [Get started authenticating calls with a private app](#get-started-authenticating-calls-with-a-private-app)
    *   [Build for the app marketplace](#build-for-the-app-marketplace)
*   [Customize the HubSpot UI](#customize-the-hubspot-ui)
*   [Build custom websites](#build-custom-websites)

Use APIs and build integrations[](https://developers.hubspot.com/docs/getting-started/what-to-build#use-apis-and-build-integrations)
------------------------------------------------------------------------------------------------------------------------------------

Use HubSpot's APIs to build custom solutions, such as sharing data between HubSpot and external systems, using webhooks to listen for changes in the account, and creating custom objects to store data specific to your business.

**Example use cases:** 

*   Use custom objects to customize how the CRM stores data so it best represents your business.
*   Sync data from external systems to provide a richer picture of go-to-market activities.
*   Extend the capabilities of the CRM UI to best fit your processes.

**Two ways to build apps**

There are two [types of apps](/docs/api/developer-tools-overview), depending on what you’re building. If you’re getting started with APIs and integrations, it's recommended to start with a private app, as they're faster to set up and use for authentication. Once you’re familiar with building apps, you may want to learn more about [public apps](#build-for-the-app-marketplace), which can be installed in multiple accounts and enable you to build other types of extensions.

**Example use case for private apps:** _“I want to build an application for my company/team.”_

### Get started authenticating calls with a private app[](https://developers.hubspot.com/docs/getting-started/what-to-build#get-started-authenticating-calls-with-a-private-app)

Most API calls require authentication to interact with the data in your HubSpot account. To get started making calls to your account, create a private app and use its access token for authentication.

**Please note:** [Super Admin](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#super-admin) permissions are required to build private apps in your HubSpot account.

How to get started:

*   Create a [private app](/docs/api/private-apps)
*   Learn more about [making authenticated API calls with private apps](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token)
*   You can also use [client libraries](/docs/api/client-libraries) to make API calls

### Build for the app marketplace[](https://developers.hubspot.com/docs/getting-started/what-to-build#build-for-the-app-marketplace)

Develop integrations for HubSpot's App Marketplace with a public app, to enable HubSpot users to install your integration into their account. Building public apps for the marketplace requires adherence to HubSpot's App Marketplace guidelines, and an app developer account.

Public apps authenticate with OAuth. Public apps can be installed on multiple accounts and can be distributed on the marketplace.

**Example use cases for public apps:**

_“I’m a HubSpot partner who wants to build a reusable app that I can adapt for my clients.”_

_“I’m a HubSpot partner who wants to make an app available on the marketplace to promote our capabilities to as many HubSpot customers as possible.”_  
  

How to get started:

*   [Create an app developer account](https://app.hubspot.com/signup-hubspot/developers)
*   Quickstart: [Create a public app](https://developers.hubspot.com/docs/api/creating-an-app)
*   [Follow the OAuth quickstart guide](https://developers.hubspot.com/docs/api/oauth-quickstart-guide)

*   [Review the App Marketplace listing requirements](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements)
*   [Submit your app to the App Marketplace](https://developers.hubspot.com/docs/api/listing-your-app)

Customize the HubSpot UI[](https://developers.hubspot.com/docs/getting-started/what-to-build#customize-the-hubspot-ui)
----------------------------------------------------------------------------------------------------------------------

**Please note:** creating UI extensions requires a **_Sales Hub_** or **_Service Hub_** _Enterprise_ subscription. However, you can get started building them for free in [developer test accounts](https://developers.hubspot.com/docs/api/account-types#developer-test-accounts).

In addition to the UI elements that HubSpot provides for CRM records, you can also customize the CRM with UI extensions. These extensions are built locally using the developer projects tool, which enables you to build and deploy to HubSpot using the CLI. The UI extensions SDK provides a toolbox of methods, functionalities, tools, and components to customize your extension. If you're not sure where to start with UI extensions, check out [HubSpot's sample projects](/docs/platform/sample-projects).

Projects enable you to locally build and deploy private apps, UI extensions, and serverless functions using the HubSpot CLI. 

**Example use cases for UI extensions:** 

_“I want to add a custom form to contact and company records that enables our customer support team to create Jira tickets while on customer calls.”_

_“I need to surface detailed sales pipeline summaries across deal records so that our managing partners can find the information they need at a glance.”_

How to get started:

*   If you don't have a _**Sales Hub**_ or _**Service Hub** Enterprise_ subscription, [create a developer test account](/docs/api/account-types#developer-test-accounts)
*   Join the [developer projects beta](https://developers.hubspot.com/docs/platform/crm-development-tools-overview#get-started)
*   **Quickstart:** [UI extensions quickstart guide](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart)
*   Learn more about the [UI extensions SDK](https://developers.hubspot.com/docs/platform/ui-extensions-sdk)

Build custom websites[](https://developers.hubspot.com/docs/getting-started/what-to-build#build-custom-websites)
----------------------------------------------------------------------------------------------------------------

Using HubSpot's CMS (Content Management System) software, you can create powerful websites and landing pages that adapt and tailor themselves to the individuals coming to your site. By building on the CMS, every website visitor interaction is directly connected to the account’s CRM, the same tool that the Sales, Marketing, Services, and RevOps teams are using to do their jobs more efficiently.

Build HubSpot websites locally in your preferred environment with the HubSpot CLI, using technologies such as:

*   HTML, CSS, and JavaScript
*   HubL, which is HubSpot's Jinjava-based templating language
*   React, which can be used to build JavaScript-rendered modules and partials
*   GraphQL, which you can use to query HubSpot data

And if you prefer to use GitHub for version control, you can [set up an integration using GitHub Actions](https://developers.hubspot.com/docs/cms/guides/github-integration). 

The CMS enables you to build websites locally with the HubSpot CLI. You’ll have access to an array of versatile and adaptable tools, such as multi-language support, CTAs, forms, memberships, and more. HubSpot also handles security, server-side performance, CDN, hosting, and uptime assurance for you.

**Example use cases for the CMS:** 

_“I want to build out product listing pages that pull information directly from inventory maintained in the CRM.”_

_“I need a website that features a public blog and a members-only blog.”_

*   Create a [CMS Sandbox account](https://app.hubspot.com/signup-hubspot/cms-developers)
*   Install the [HubSpot CLI](/docs/cms/guides/getting-started-with-local-development).
*   Install the [HubSpot Visual Studio Code extension](https://developers.hubspot.com/docs/cms/guides/install-and-use-hubspot-code-extension)
*   **Quickstart:** [HubSpot CMS quickstart guide](https://developers.hubspot.com/docs/cms/guides/getting-started)
*   Check out the [CMS guides](/docs/cms/guides) and [reference docs](/docs/cms)

* * *

Share your feedback[](https://developers.hubspot.com/docs/getting-started/what-to-build#page-feedback)
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