---
Please provide me with more context! I need to know what kind of mission you're writing about in order to help you. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, or something else?"
* **What is the overall purpose?** What are you trying to achieve?
* **What are the key objectives?** What specific goals need to be accomplished?

Once I have this information, I can help you write a compelling and impactful mission statement.
---

How to add social login for membership pages


================================================

Last updated: August 27, 2021

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Remembering your password across the hundreds of sites we interact with day to day can be hard. Especially if you follow best practices and have separate passwords for all of your accounts. You can make it easier on users who have memberships with your website by providing the ability to login using social accounts like Facebook and Google.

In this guide you will add social login capability to your login template

What you need before you begin[](https://developers.hubspot.com/docs/cms/guides/membership/social#what-you-need-before-you-begin)
---------------------------------------------------------------------------------------------------------------------------------

*   Memberships functionality (requires CMS Enterprise)
*   A membership login template
*   A website page you wish to restrict access to
*   A contact list you will give page access to (a list which just contains your email would be good for testing before using a real list)

1\. Open your login template[](https://developers.hubspot.com/docs/cms/guides/membership/social#open-your-login-template)
-------------------------------------------------------------------------------------------------------------------------

In your theme, find and open your login template. Membership login templates are required to have the template annotation `templateType: membership_login_page`

2\. Add the membership social login module[](https://developers.hubspot.com/docs/cms/guides/membership/social#add-the-membership-social-login-module)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Add the code for the `membership_social_logins` module to your template where you want the button(s) to appear.

{% module "social" path="@hubspot/membership\_social\_logins" %}

The module supports both Google and Facebook login. You can add both, or just one of them to your login page.

The module supports both Google and Facebook login. You can add both, or just one of them to your login page.

### Add Google login button[](https://developers.hubspot.com/docs/cms/guides/membership/social#add-google-login-button)

You will create credentials in the Google developer console. You will be given a client ID which you will then use in your module tag.

1.  Go to the [Credentials page](https://console.developers.google.com/apis/credentials).
2.  Select **"Create credentials > OAuth client ID"**
3.  Select **"Web application"** application type.
4.  Name your application something that communicates what your users will be logging into on your HubSpot site. 
5.  Click **"Create"**
6.  Copy the **Client ID** of your newly created OAuth client.
7.  In your template file, find the social login module, add the parameter `google_clientid="YourAppID"` replace "YourAppID" with the app ID you just copied.
8.  Add the parameter `google_enabled=true`. This will make the Google login button appear.

### Add Facebook login button[](https://developers.hubspot.com/docs/cms/guides/membership/social#add-facebook-login-button)

To add the facebook login button you will create an app in Facebook's developer dashboard. The app will be given a Facebook App Id.

1.  [Log into your Facebook developer account](https://developers.facebook.com/apps/) ([Register a new account](https://developers.facebook.com/docs/development/register) if you don't have one)
2.  Use the **"Create App"** button.
3.  Select **"Build connected experiences"**, then **"continue"**.
4.  Name your app something that communicates what your users will be logging into on your HubSpot site. Select **"Create app"**.
5.  You should now see a screen that says "add products to your app".
6.  Select **"Facebook Login"**
7.  Open **"Settings"** in the left side navigation panel and under Client OAuth Settings, enter your redirect URL in the **"Valid OAuth Redirect URIs"** field.
8.  In the top bar you will see your **app id**. Copy it to your clipboard.
9.  In your template file, find the social login module, add the parameter `facebook_appid="YourAppID"` replace "YourAppID" with the app ID you just copied.
10.  Add the parameter `facebook_enabled=true`. This will make the facebook login button appear.

HubSpot does not have control over the UI that Google and Facebook provide. Should their UI change these instructions may become confusing or no longer work. The most important part is that you create a client/app, then get it's ID. Provide that id through the default module's parameter for that provider and their respective "enabled" parameter.

Below is an example of what your code may look like. If you are only adding one of the providers, you would not need to include an id, and the enabled parameter for services you are not supporting.

{% module "social" path="@hubspot/membership\_social\_logins", clientid="1234567890-abc123def456.apps.googleusercontent.com" appid="12345678" facebook\_enabled=true google\_enabled=true %}

3\. Test the social login[](https://developers.hubspot.com/docs/cms/guides/membership/social#test-the-social-login)
-------------------------------------------------------------------------------------------------------------------

1.  [Create a contact list](https://knowledge.hubspot.com/lists/create-active-or-static-lists#set-up-a-new-list) with just your email address in it. _Email address must also be used for your Google or Facebook account._
2.  [Set a page to "Private registration required",](https://knowledge.hubspot.com/website-pages/require-member-registration-to-access-private-content#set-up-membership-registration-for-pages) choose your newly created test list.
3.  Visit one of these pages using incognito mode so you are not signed in. You should see your login template with the social login functionality. 
4.  Attempt to log in using the social login buttons.

If you're seeing any issues, look back through the instructions, ensure your client ID or app ID is entered correctly and passed to the module. Ensure if you have security set up for it that your site's domain is set as a trusted domain in the app settings.

You're done![](https://developers.hubspot.com/docs/cms/guides/membership/social#you-re-done-)
---------------------------------------------------------------------------------------------

Congratulations you successfully added social login functionality to your login template! Your users can now use their Google and/or Facebook to log in.

Related resources[](https://developers.hubspot.com/docs/cms/guides/membership/social#related-resources)
-------------------------------------------------------------------------------------------------------

*   [Memberships](https://developers.hubspot.com/docs/cms/features/memberships)
*   [Memberships SSO](https://developers.hubspot.com/docs/cms/features/memberships/sso)
*   [CRM Objects in CMS Hub](https://developers.hubspot.com/docs/cms/features/custom-objects)
*   Membership social logins module reference

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/membership/social#page-feedback)
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