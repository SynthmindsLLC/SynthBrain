Listing your app
================

After you’ve created an app in your developer account that meets the [App Marketplace listing requirements](/docs/api/app-marketplace-listing-requirements), you can submit a listing to add it to the [HubSpot App Marketplace](https://ecosystem.hubspot.com/marketplace/apps). The HubSpot Ecosystem Quality team will review your submission and follow up via email if the app has been approved or rejected.

**Please note:** you must be a [super admin](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#super-admin) to update and submit an app listing. 

In this article:

*   [Create and submit an app listing](#How_app_listing)
*   [Create and update a localized listing for an existing app listing](#edit-localized-listing)
*   [Add points of contact for the App Partner Program](#contacts)
*   [Edit a live app listing](#edit-localized-listing)
*   [Unpublish a live app listing](#unpublish-listing)

Create and submit an app listing[](https://developers.hubspot.com/docs/api/listing-your-app#create-and-submit-an-app-listing)
-----------------------------------------------------------------------------------------------------------------------------

**Please note:** before submitting an app listing, review the [App listing requirements page](/docs/api/app-marketplace-listing-requirements) to understand how to fill your listing.

*   In your [app developer account](/docs/api/developer-tools-overview), navigate to **App Marketplace** \> **Listings**.
*   In the upper right, click **Create listing**. If this button is grayed out, listings have already been created for all your existing apps.
*   Select the **app** you want to create a listing for and click **Next**. Apps that are already listed on the App Marketplace will not appear here.
*   On the next screen, click the **Select the languages your app is available in** dropdown menu and select the **languages** your app software is offered in. The App Marketplace is available in eight languages: English, Spanish, French, German, Portuguese, Japanese, Dutch, and Italian. You can create app listings in as many of these languages as you want, as long your app's software is available in them.
*   Click the **Select the primary listing language for \[app name\]** dropdown menu and select the **default language** users will see when browsing the App Marketplace.
*   Click **Next**

The app listing submission form is broken up into five tabs:

*   On the _Listing info_ tab:
    *   In the _App information_ section, add your public app name, company name, app tagline, and connect button URL. 
    *   In the _App icon_ section, upload an 800px by 800px icon for your app. This will appear in the App Marketplace and in connected users’ accounts. Best practices for icons are:
        *   **Do**: use a JPG, JPEG, or PNG file, fill the entire space (800px by 800px) - your image should touch at least two edges, and use a high-resolution, unpixellated image.
        *   **Do not**: include text in your icon, use a wordmark, or leave extra whitespace around your icon.

![dev-doc-logo](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/dev-doc-logo.png?width=835&name=dev-doc-logo.png)

*   In the _Categorize your app_ section, select a category for your app and any search terms that can be used to find your app in the App Marketplace.

*   Next, click the **App details** tab.
    *   In the _Demo video_ section, upload a video to show how your app works. Refer to the [How to Make a Great App Demo Video](https://www.hubspot.com/partners/apps/resources/how-to-make-a-great-app-demo-video) page for best practices and examples of how to create a demo video. 
    *   In the _Screenshots_ section, add images showing how your app works.
    *   In the _App Overview_ section, give a brief description of how your app can help users carry out their goals.
    *   In the _Features_ section, you can highlight your app’s key features and context for how it works in a real-life scenario. To add additional features, click **Add another feature**.
    *   In the _Shared data_ section, let users know how data will flow between your app and HubSpot. 
        *   Click **Add shared data**.
        *   In the right panel, select which app object syncs with which HubSpot object, and the direction of the sync. 
        *   To add another object sync, click **Add another object**. 
    *   In the _HubSpot features your app works with_ section, add up to 10 HubSpot tools and features your app works with. 
    *   In the _Other tools your software integrates with_ section, select up to six other tools or apps that your software integrates with. 
    *   In the _Languages your app is available in_ section, select all languages available for your app. You can only create additional App Marketplace listings in these languages.  
*   Next, click the **Pricing** tab.
    *   In the top section, select the currency you want to list the app in. You can select from over 100 currencies. 
    *   You can also set up pricing plans for your app by adding the plan name, tagline, features list, and pricing model. 
        *   Depending on the pricing model selected, you may need to add more information, such as the frequency of payment, one-time fees, or monthly prices. Hover over the **information icon** to learn more about each pricing model. 
        *   You can add up to five pricing plans. To add additional pricing plans, click **Add another plan.**
    *   In the _Link to your software’s pricing plan_ section, enter the URL where users can find more information on your pricing plans.
    *   In the _Agency pricing plans_, enter the URL where users can learn more about pricing for partner or consulting services. 
*   Next, click the **Support info** tab.
    *   In the _Contact info_ section, add a support contact method for users who have questions while using your app. Add your support email, company website and languages that customer support is offered in.
    *   In the _Support resources_ section, include links to your app’s setup documentation.
    *   In the _Terms of Service and Privacy Policy_ section, add links to your privacy documentation.
*   Lastly, click the **Review info** tab.
    *   In the _App review instructions_ section, include any information that the HubSpot Ecosystem Quality team requires to test and review your app.
    *   In the _App Partner Program points of contact_ section, include the contact information of any people who need to be communicated with regarding the app listing, and the developer of the app. You must include the person's role, first and last name, email, and country where they are based. 
    *   To add another point of contact, click **Add another point of contact**.

To submit the listing for review, click Submit for review in the upper right corner. If the _Submit for review_ button is grayed out, check that you’ve filled out all the required fields and have _Super admin_ permissions. If you’ve missed any required fields, you will see a number in the tab heading indicating the number of missed fields. Click each tab to enter the missing information, then return to the _Review info_ tab and click Submit for review.

![dev-doc-missing-field](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/dev-doc-missing-field.png?width=1144&name=dev-doc-missing-field.png)

Create and update a localized listing for an existing app listing[](https://developers.hubspot.com/docs/api/listing-your-app#create-and-update-a-localized-listing-for-an-existing-app-listing)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You will need to set a primary language on your existing app listing and have your primary listing already published in the HubSpot Marketplace in order to create listings in other languages.

*   In your HubSpot app developer account, click **App Marketplace** > **Listings**. 
*   If you already have an app listed in the Marketplace, you’ll see a yellow banner above the listed app asking you to set your primary listing language. Click **Set it now**. You will need to set the primary listing language for the app listing before you're able to create new language listings.

*   In the dialog box, click the **Select the languages your app is available in** dropdown menu and select the **languages** your app software is available in.
*   Click the **Select the primary listing language for \[app name\]** dropdown menu and select the **default language** users will see when browsing the App Marketplace. 
*   Click **Save.** 

Once you have set a primary language, you will be able to add a new localized listing:

*   Hover over the **app listing** and click **More** > **Create listing in another language**. 
*   Click the **Language for this listing** dropdown menu and select the **language** you want to create this listing in. 
*   Click **Create**.
*   Follow the steps to create and submit a listing in the selected language.

**Please note:** 

*   All parts of your localized listing should be in the same language, including product screenshots and demo videos.
*   Updating your primary listing does not automatically update your localized listings. Each must be updated independently.

Edit a live app listing[](https://developers.hubspot.com/docs/api/listing-your-app#edit-a-live-app-listing)
-----------------------------------------------------------------------------------------------------------

Once an app listing is live on the App Marketplace, to edit the listing: 

*   In your developer account, click **App Marketplace > Listings**. 
*   Hover over the listing you’d like to edit and click **More** > **Edit**. 
*   Make your changes then click **Submit for review**. 

Unpublish a live app listing[](https://developers.hubspot.com/docs/api/listing-your-app#unpublish-a-live-app-listing)
---------------------------------------------------------------------------------------------------------------------

*   In your developer account, click **App Marketplace** \> **Listings**. 
*   Hover over the listing you want to unpublish and click **More** > **Unpublish live listing**. 
*   In the dialog box, enter the reason for unpublishing the app, the click **Submit unpublish request**. 

Unpublish requests are processed by the HubSpot Marketplace team within 10 business days of submission. 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/listing-your-app#page-feedback)
---------------------------------------------------------------------------------------------

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