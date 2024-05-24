API developer guides & resources
================================

HubSpot's APIs, which you can find the [reference documentation here](/docs/api/overview), allow you to build a functional app or integration quickly and easily. Here's an overview of what you'll need to use them.

Building apps
-------------

Before you get started, you should decide what type of app you want to build.

### Public apps

If you're looking to create an app that other HubSpot users outside of your organization will install, such as an app listed on the [app marketplace](https://ecosystem.hubspot.com/marketplace/apps), you should create a public app.

If you're building a public app, you'll need to create an app developer account:

*   First, navigate to [this page](/get-started).
*   Click **Create App Developer Account**.
*   Authenticate using your Google or Microsoft account, or enter your email.
*   Continue following the setup instructions to create your developer account.

From there, you can create a new app, configure OAuth, and create a test environment. [Start building now.](/docs/api/developer-tools-overview)

### Private apps

If your goal is to create an integration that will only be leveraged by other users in your HubSpot account, such as internal app that can access or modify contact data from your account, you can create a private app.

Learn more about creating a [private app](/docs/api/private-apps) in this article.

Authentication
--------------

Most HubSpot API endpoints support both [OAuth](/docs/api/working-with-oauth) and [private app access tokens](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token).

**Please note:** as of November 30, 2022, HubSpot API Keys are being deprecated and are no longer supported. Continued use of HubSpot API Keys is a security risk to your account and data. During this deprecation phase, HubSpot may deactivate your key at any time.

You should instead authenticate using a private app access token or OAuth. Learn more about [this change](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) and how to [migrate an API key integration](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app) to use a private app instead.

*   If you want to list your app in the HubSpot App Marketplace or have multiple users install it, you must use OAuth.
*   If you're building a [private app](/docs/api/private-apps), you can make calls using your app's access token, which also implements OAuth.

Usage and limits
----------------

Learn about our [usage guidelines](/docs/api/usage-details), rate limits, and how to check your API call usage.

App Partners and the App Marketplace
------------------------------------

Review [app listing requirements](/docs/api/app-marketplace-listing-requirements) and [create your app listing](/docs/api/listing-your-app).

Learn to use APIs and build apps on HubSpot Academy
---------------------------------------------------

Learn more about the HubSpot APIs, developer accounts, and how to start making calls using both OAuth and API keys with these short (and free!) HubSpot Academy [videos](https://academy.hubspot.com/courses/integrating-with-hubspot-foundations).

 * * *

#### Quick links

*    [Create a developer account](https://app.hubspot.com/signup-v2/developers/step/join-hubspot?hubs_signup-url=developers.hubspot.com/get-started&hubs_signup-cta=developers-getstarted-app)
*    [Set up a developer test account](/docs/api/account-types#developer-test-accounts) to install your app and test API calls
*    Stay up-to-date by subscribing to the [Changelog](/changelog?_ga=2.18393149.544057971.1579020362-1635676776.1568129882)
*    Join the conversation or ask questions in HubSpot’s [developer community forums](https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers?_ga=2.141401138.1430331704.1585575540-500942594.1573763828)
*    Become a member of our developer [Slack community](https://designers.hubspot.com/slack?_ga=2.141401138.1430331704.1585575540-500942594.1573763828)  
      
    
    * * *
    

#### Related docs

[API reference docs](/docs/api/overview)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/developer-guides-resources#page-feedback)
-------------------------------------------------------------------------------------------------------

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