---
Please provide me with more context! I need to know what your mission is about in order to help you write it. 

For example, tell me: "* **What is the purpose of this mission?** What are you trying to achieve?"
* **Who is this mission for?** Who is the target audience?
* **What are the key goals of this mission?** What specific objectives will you accomplish?
* **What is the tone you want to convey?** Do you want it to be inspiring, informative, or something else?

Once you give me this information, I can help you write a compelling and effective mission statement.
---

SSO for Memberships


=======================

Last updated: October 24, 2022

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Manage all of your businesses access permission and authentication needs in a single system with single sign-on (SSO) for [memberships](https://developers.hubspot.com/docs/cms/features/memberships). This system allows you to manage access to your company’s applications across your stack, giving your end-users a single username and password combo for all of the applications and content they should have access to.

**Please note:** this setup process must be done by an IT administrator with experience creating applications in your identity provider account. At this time, we only support SAML-based applications.

Initial Setup[](https://developers.hubspot.com/docs/cms/features/memberships/sso#initial-setup)
-----------------------------------------------------------------------------------------------

Follow the steps below to begin setting up your SSO for memberships.

The navigation instructions and field names described below may differ across identity providers. You can find more specific instructions for setting up applications in commonly used identity providers below:

• [Okta](#okta)

• [OneLogin](#onelogin)

### 1\. Login to your identity provider.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#login-to-your-identity-provider-)

### 2\. Navigate to your applications.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#navigate-to-your-applications-)

### 3\. Create a new SAML application specifically for HubSpot content access.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#create-a-new-saml-application-specifically-for-hubspot-content-access-)

To get the Audience URI and Sign on URL, ACS, Recipient, or Redirect values:

*   In your HubSpot account, click the settings icon settings in the main navigation bar.
*   In the left sidebar menu, select Private Content.
*   Select a domain from the “choose a domain to edit” picklist to open the settings for that domain.  Note\* SSO must be enabled on a per-subdomain basis at this time.

![Select a domain from the dropdown](https://developers.hubspot.com/hubfs/Developer%20Site/assets/images/sso-memberships/sso-for-memberships-sub-domain-select.png "Select a domain from the dropdown")

*   In the _Single sign-on (SSO)_ section, click Set up.
*   In the right pane, click Copy next to the values as needed. If you are using Microsoft AD FS, click the Microsoft AD FS tab to copy the values needed.
*   Paste them into your identity provider account where required.

### 4\. Copy the identifier or issuer URL, the single-sign on URL, and the certificate from your identity provider, and paste them into the corresponding fields in the SSO setup panel in HubSpot.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#copy-the-identifier-or-issuer-url-the-single-sign-on-url-and-the-certificate-from-your-identity-provider-and-paste-them-into-the-corresponding-fields-in-the-sso-setup-panel-in-hubspot-)

### 5\. Click Verify.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#click-verify-)

Once verification is complete, a “single sign on is enabled” notification will appear at the top of the General & Templates tabs for that domain and all template and email settings options that are no longer managed through HubSpot (because they are now managed through your IaP) will be disabled.

SSO Enablement for Blogs[](https://developers.hubspot.com/docs/cms/features/memberships/sso#sso-enablement-for-blogs)
---------------------------------------------------------------------------------------------------------------------

### 1\. Navigate to settings > CMS > Blog in the Settings UI.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#navigate-to-settings-cms-blog-in-the-settings-ui-)

### 2\. Select a blog that is currently hosted on an SSO enabled subdomain from the “select a blog to modify” list.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#select-a-blog-that-is-currently-hosted-on-an-sso-enabled-subdomain-from-the-select-a-blog-to-modify-list-)

### 3\. Locate the control audience access settings at the bottom of your blog’s general tab.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#locate-the-control-audience-access-settings-at-the-bottom-of-your-blog-s-general-tab-)

Visit the [control audience access option settings section](/docs/cms/features/memberships/sso-for-memberships#control-audience-access-option-settings) for more information on these choices.

SSO Enablement for Pages / Landing Pages[](https://developers.hubspot.com/docs/cms/features/memberships/sso#sso-enablement-for-pages-landing-pages)
---------------------------------------------------------------------------------------------------------------------------------------------------

### 1\. Navigate to marketing > website > website pages or landing pages.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#navigate-to-marketing-website-website-pages-or-landing-pages-)

### 2\. Select a single page or landing page on an SSO enabled domain, or select multiple pages or landing pages on an SSO enabled domain using the checkbox option in the listing’s area, and click the “control audience access” option at the top of the table.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#select-a-single-page-or-landing-page-on-an-sso-enabled-domain-or-select-multiple-pages-or-landing-pages-on-an-sso-enabled-domain-using-the-checkbox-option-in-the-listing-s-area-and-click-the-control-audience-access-option-at-the-top-of-the-table-)

These options are also available in the page and landing page editor > settings tab.

![Page and landing page listing in app](https://developers.hubspot.com/hubfs/Developer%20Site/assets/images/sso-memberships/page-landing-page-editor.png "Page and landing page listing in app")

Visit the [control audience access option settings section](/docs/cms/features/memberships/sso-for-memberships#control-audience-access-option-settings) for more information on these choices.

SSO Enablement for Knowledge Articles[](https://developers.hubspot.com/docs/cms/features/memberships/sso#sso-enablement-for-knowledge-articles)
-----------------------------------------------------------------------------------------------------------------------------------------------

**Note:** Articles must be set at the article level at this time.  We will address global SSO settings options for the knowledge base at a later time.

### 1\. Navigate to settings > knowledge base > articles[](https://developers.hubspot.com/docs/cms/features/memberships/sso#navigate-to-settings-knowledge-base-articles)

### 2\. Select a single article on an SSO enabled domain or select multiple articles on an SSO enabled domain using the checkbox option in the listing’s area, and click the “control audience access” option at the top of the table.[](https://developers.hubspot.com/docs/cms/features/memberships/sso#select-a-single-article-on-an-sso-enabled-domain-or-select-multiple-articles-on-an-sso-enabled-domain-using-the-checkbox-option-in-the-listing-s-area-and-click-the-control-audience-access-option-at-the-top-of-the-table-)

**Note:** These options are also available in the article editor > settings tab.

![Knowledge base article listing in app](https://developers.hubspot.com/hubfs/Developer%20Site/assets/images/sso-memberships/kb-article-editor.png "Knowledge base article listing in app")

Visit the [control audience access option settings section](/docs/cms/features/memberships/sso-for-memberships#control-audience-access-option-settings) for more information on these choices.

Control Audience Access Option Settings[](https://developers.hubspot.com/docs/cms/features/memberships/sso#control-audience-access-option-settings)
---------------------------------------------------------------------------------------------------------------------------------------------------

If you would like all users in your IaP that have HubSpot as an assigned app to be able to see your private content, **select the Private - Single sign on(SSO) required** option.

If you would like to segment users with the assigned HubSpot app in your IaP into smaller tiered groups, **select the Private - Single sign on (SSO) required with list filtering** option.

*   This option requires users to be both a member of your IaP with the assigned app AND a member of a contact list within HubSpot in order to view pages. The benefit of this option is that it allows you to further refine access if your business operates on a tiered subscription model, for example members get access to different content materials depending on their bronze, gold, or platinum subscription levels.
*   **Note:** This is also the default option for content previously marked as “Private - registration required”. If you have content previously marked as "Private - registration required" and would like to transition fully to SSO, please verify that all contacts currently in those assigned lists are added to your IaP before switching over to unfiltered SSO management. Failure to do so will result in contacts losing access to that content.

Instructions for specific identity providers[](https://developers.hubspot.com/docs/cms/features/memberships/sso#instructions-for-specific-identity-providers)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

### Okta[](https://developers.hubspot.com/docs/cms/features/memberships/sso#okta)

**Please note:** you need administrative access in your Okta instance. This process is only accessible in the Classic UI in Okta.

*   Log in to Okta. Make sure you are in the administrative instance of your Okta developer account.
*   Click **Applications** in the top navigation bar.
*   Click **Add application**.
*   Click **Create new app.**
*   Select **Web** as your platform and **SAML 2.0** as your Sign On method then click **Create.**
*   Fill out the General Settings screen as desired then click **Next**.
*   On the Configure SAML screen, copy and paste the **Sign on URL** and **Audience URI** from HubSpot into Okta, then click **Next** and finish the app creation process.
*   Navigate to the **Assignments** tab. Assign the new app to any users that will have access to private content, including yourself.
*   Navigate to the **Sign On** tab. Click the **View setup instructions** button.
*   Copy the Identity Provider **Single Sign-On URL**, **Identity Provider Issuer** and **X.509 Certificate** from Okta into HubSpot.
*   Click **Verify**. You'll be prompted to log in with your Okta account to finish the configuration and save your settings.

### OneLogin[](https://developers.hubspot.com/docs/cms/features/memberships/sso#onelogin)

**Please note:** you need administrative access in your OneLogin instance to create a new SAML 2.0 application in OneLogin, as required.

*   Log in to **OneLogin**.
*   Navigate to **Applications**.
*   Click **Add App**.
*   Search for **SAML Test Connector (Advanced)** and select the app.
*   Click **Save**.
*   Click the **Configuration** tab.
*   Copy and paste the **Audience** and **Recipient** from HubSpot into the corresponding fields in OneLogin.
*   In the upper right, click **Save**.
*   Click the **SSO** tab.
*   Copy the **Issuer URL** and **SAML 2.0 Endpoint** (Single Sign-on URL) into HubSpot.
*   Click **View Details** under the X.509 Certificate then copy and paste the certificate into HubSpot.
*   Click the **Users** tab in the top left and add yourself and any other users that should have access to private content to the OneLogin application you created.
*   Click **Verify**. You'll be prompted to log in with your OneLogin account to finish the configuration and save your settings.

Frequently Asked Questions[](https://developers.hubspot.com/docs/cms/features/memberships/sso#frequently-asked-questions)
-------------------------------------------------------------------------------------------------------------------------

### What happens to my content if I disable SSO for a domain?[](https://developers.hubspot.com/docs/cms/features/memberships/sso#what-happens-to-my-content-if-i-disable-sso-for-a-domain-)

If you disable SSO for a domain that has published private content on it today, any Private - Single sign on (SSO) required pages will become fully public. Any content marked Private - Single sign on (SSO) required with list filtering will remain private and will be inaccessible to all users.

### Can I go back to the old Private - registration required option? How[](https://developers.hubspot.com/docs/cms/features/memberships/sso#can-i-go-back-to-the-old-private-registration-required-option-how)

To go back to simple registration through HubSpot, our recommendation is to first change all sensitive content over to Private - Single sign on (SSO) required with list filtering, then disable SSO for that domain, and then to change all private content over to Private - registration required.  During this switch we recommend reviewing any lists or workflows used to populate lists for registration purposes to ensure things are correct before saving the changes.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/features/memberships/sso#page-feedback)
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