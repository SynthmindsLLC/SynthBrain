App Marketplace listing requirements
====================================

App listing submissions are manually reviewed by the HubSpot Ecosystem Quality team and will be rejected if they do not meet the criteria outlined below. Once your app meets these requirements, you can [build your app listing](/docs/api/listing-your-app) from within your app developer account by navigating to **App Marketplace > Listings > Create listing**.

Minimum requirements
--------------------

*   **Single HubSpot app ID:** your app must authorize API requests with the public HubSpot app ID (and [OAuth client ID](/docs/api/working-with-oauth)) associated with your app listing.
    *   A listing must not redirect to a different public or private app.
    *   Your listed public app must not require another public or private app to function. 
    *   Your listed public app must be unique. If you have already listed an app and you want to replace it, you should update the existing app instead of listing a new one. 
    *   Do not create multiple apps that solve for the same use case. Apps with similar functionality and use the same APIs should be consolidated into a single app.

*   **OAuth:** your app must use OAuth as its sole authorization method. Learn more about [working with OAuth](/docs/api/working-with-oauth?_ga=2.22892857.341006870.1586180142-500942594.1573763828).
*   **Installs:** your app must have at least three [active, unique installs](/docs/api/certification-requirements#:~:text=Active%20installs%20are%20the%20number%20of%20unique%20HubSpot%20production%20accounts%2C%20unaffiliated%20with%20your%20organization%2C%20showing%20successful%20app%20activity%20within%20the%20past%2030%20days.). You won’t be able to submit your app listing without this.
*   **Scopes:** you must only request scopes your app needs. [Review your scopes](/docs/api/working-with-oauth#scopes) and make sure you’re not asking for unnecessary access. Apps that do this tend to have better conversion rates.
    *   Your app must have [advanced scope settings](/docs/api/creating-an-app#configure-scopes) turned on. All required, conditionally required, and optional scopes should be selected to prevent errors. These settings can be found in the [developer account](/docs/api/account-types#app-developer-accounts) that manages your app. 
*   **Terms:** you must review and agree to the terms in [HubSpot's App Partner Program Agreement](https://legal.hubspot.com/app-program-agreement). This protects you, HubSpot, and our shared customers. You won’t be able to submit your app listing without completing this step. 
*   **Restricted industries:** your app must not fit or deliver functionality that would exclusively serve customers within any of HubSpot's [restricted industries](https://legal.hubspot.com/acceptable-use#Restricted-Industries). 

### Brand requirements[](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#brand-requirements)

*   Your app and its associated collateral (documentation, landing pages, etc.) must meet [HubSpot’s Branding Guidelines](https://www.hubspot.com/partners/app/branding-guidelines). For example, capitalize the “S” in “HubSpot” any time you’re referring to HubSpot.
*   Your app and its associated collateral (documentation, landing pages, etc.) must not infringe [HubSpot’s Trademark Usage Guidelines](https://legal.hubspot.com/tm-usage-guidelines). For example, do not combine HubSpot's name (including “Hub” and “HubSpot”) with your app name or logo.

### Listing requirements[](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#listing-requirements)

Once you’ve met the minimum requirements, you can submit your app listing. When submitting your app listing, you must completely and accurately fill out all information. These fields are particularly important and failure to meet these requirements will cause your listing to be set to Draft mode only:

*   The content of your listing should be specific to the integration as opposed to general product information. It should contain information about the value customers can expect specifically from downloading and using this integration. Good examples include: [Aircall](https://ecosystem.hubspot.com/marketplace/apps/sales/calling/aircall), [CloudFiles](https://ecosystem.hubspot.com/marketplace/apps/sales/sales-enablement/cloudfiles), [Reveal](https://ecosystem.hubspot.com/marketplace/apps/sales/partner-relationship-management/reveal-191193).
*   A link to a publicly available (no sign-in, no paywall) Setup Documentation specific to your HubSpot integration. 
    *   Your Setup Guide cannot simply be your homepage or a general knowledge base.
    *   Instead, it must contain the steps to install and configure the integration.
    *   For an example, check out the [OrgChartHub setup guide](https://orgcharthub.com/guides/setup).
*   Include a relevant Install button URL that brings customers to a page where they can easily connect your app with HubSpot.
*   URLs for your app’s support resources (support website, HubSpot community forum, case study) must be live, up-to-date, and publicly available.
*   URLs for your app’s Terms of Service and Privacy Policy must be live and up-to-date.
*   All URL fields have a limit of 250 characters.
*   Shared data, which lets users know how information will flow between your app and HubSpot, must be accurate, up-to-date, and reflect the [scopes](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#:~:text=Webhooks%20API.-,Scopes,-%3A%20You%20must) your app requests.
    *   All objects selected in your OAuth scopes should be documented in the _Shared data_ table.
    *   If your app is requesting both read and write object scopes, the data sync should be advertised as bi-directional for these specific objects.
*   Your App Marketplace listing must contain clear and accurate pricing information.
    *   At least one pricing plan relevant to your HubSpot integration, which needs to match the information published on your website.
    *   Free pricing plans should only be used for Free forever or Freemium pricing models.
*   You must include at least one support contact method.
*   Follow the guidelines listed [here](/docs/api/provide-testing-credentials-for-your-app) for providing testing credentials for your app listing. 

Review, feedback, and approval[](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#review-feedback-and-approval)
-------------------------------------------------------------------------------------------------------------------------------------------

Once you submit your listing, the HubSpot Ecosystem Quality team will complete an initial review within 10 business days. If any of the information provided is incorrect, misleading, or incomplete, we’ll contact you with that feedback. The entire app review and feedback process should take no more than 6o days from the time feedback is shared. As stated in the [App Marketplace Terms](https://legal.hubspot.com/app-program-agreement), HubSpot reserves the right to unpublish or refuse publication of your app listing at any time.

Rewards for Listed App Partners[](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#rewards-for-listed-app-partners)
-----------------------------------------------------------------------------------------------------------------------------------------------

*   Dedicated HubSpot App Marketplace listing
*   Priority access to developer support through a dedicated support alias
*   Developer community resources, including webinars, forums, and more
*   Curated marketing resources, including PR templates and launch guides
*   Discounted INBOUND event sponsorship, booths, and tickets
*   Discounted software through the HubSpot for Startups seed-stage program
*   Monthly newsletter with marketing updates, product releases, and more

Related resources[](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#related-resources)
-------------------------------------------------------------------------------------------------------------------

*   [How to list your app](/docs/api/listing-your-app)
*   [App certification requirements](/docs/api/certification-requirements)
*   [API reference documentation](https://developers.hubspot.com/docs/api/overview)
*   [How to use the HubSpot APIs](https://developers.hubspot.com/docs/api/how-to-use-hubspot-api)
*   [Developer community forum](https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations?_ga=2.21920313.341006870.1586180142-500942594.1573763828)
*   [Contact the App Partner team](/contact-our-partnerships-team?_ga=2.21920313.341006870.1586180142-500942594.1573763828)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/app-marketplace-listing-requirements#page-feedback)
-----------------------------------------------------------------------------------------------------------------

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