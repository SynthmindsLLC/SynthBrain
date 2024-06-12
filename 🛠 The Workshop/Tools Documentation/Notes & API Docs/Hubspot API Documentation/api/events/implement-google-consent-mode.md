---
title: "Google Consent Mode v2"
description: "A framework designed to integrate website visitor consent preferences with Google's advertising and analytics tools, allowing websites to adjust how these tools behave based on the consent status of website visitors."
type: "concept"
tags:
- "Google_Consent_Mode"
- "Privacy"
- "Advertising"
- "Analytics"
relationships:
- "#related_to [[Website_Visitor_Consent]]"
- "#enables [[Compliance_with_Privacy_Regulations]]"
- "#used_for [[Google_Analytics_4]], [[Google_Tag_Manager]]"
- "#requires [[HubSpot_Cookie_Banner]]"
- "#developed_by [[Google]]"
---

Implement Google consent mode
=============================

[Google Consent Mode v2](https://support.google.com/google-ads/answer/10000067?hl=en) is a framework designed to integrate website visitor consent preferences with Google's advertising and analytics tools. With it, websites can adjust how these tools behave based on the consent status of website visitors, particularly regarding cookies and data collection. When visitors don’t consent to cookies, with [advanced consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#basic-vs-advanced), Google services can operate in a limited mode and collect basic interactions without breaching privacy expectations. With [basic consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#basic-vs-advanced), without consent, cookielesss pings and basic interactions will not replace tracking. 

Implement Google consent mode v2 manually[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#implement-google-consent-mode-v2-manually)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you use HubSpot's native [Google Analytics 4](https://knowledge.hubspot.com/website-pages/integrate-google-analytics-with-hubspot-content) or [Google Tag Manager](https://knowledge.hubspot.com/website-pages/add-the-google-tag-manager-code-to-your-pages) integrations, learn how to [support Google consent mode v2](https://knowledge.hubspot.com/privacy-and-consent/support-google-consent-mode-v2). 

You will need to manually integrate Google consent mode v2 if either of the following scenarios are true:

*   You use a HubSpot cookie banner on an externally-hosted website or CMS.
*   You use a HubSpot cookie banner on the HubSpot CMS, and you use a code snippet to integrate with either Google Analytics or Google Tag Manager. 

### Integrate Google consent mode v2 with Google Analytics 4[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#integrate-google-consent-mode-v2-with-google-analytics-4)

*   [In HubSpot, set up a cookie consent banner](https://knowledge.hubspot.com/privacy-and-consent/customize-your-cookie-tracking-settings-and-consent-banner#set-up-and-edit-your-cookie-consent-banner) with an opt-in policy type targeting EEA, EU, and UK visitors.
*   On your website, configure on-page consent default, configure consent updates, and install Google Analytics (see below for an example).
    *   Add your manual implementation immediately after the `<head>` element of your HTML. 

// Step 2: This snippet sets a default consent state, instructing Google's technologies how to behave if no consent is present. <script> window.dataLayer = window.dataLayer || \[\]; function gtag() { dataLayer.push(arguments); } // Determine actual values based on your own requirements, gtag('consent', 'default', { 'analytics\_storage': 'denied', 'ad\_storage': 'denied', 'ad\_user\_data': 'denied', 'ad\_personalization': 'denied', // Use region, to specifiy where this default should be applied. 'region': \["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IS", "IE", "IT", "LV", "LI", "LT", "LU", "MT", "NL", "NO", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "UK", "CH" \] }); // Step 3: This snippet sends consent updates from the HubSpot cookie banner to Google's tags using Consent Mode v2 var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', function(consent) { var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics)); var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement)); gtag('consent', 'update', { 'ad\_storage': hasAdsConsent ? 'granted' : 'denied', 'analytics\_storage': hasAnalyticsConsent ? 'granted' : 'denied', 'ad\_user\_data': hasAdsConsent ? 'granted' : 'denied', 'ad\_personalization': hasAdsConsent ? 'granted' : 'denied' }); }\]); </script> // Step 4: This snippet installs Google Analytics 4 <!-- Google tag (gtag.js) --> <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script> <script> window.dataLayer = window.dataLayer || \[\]; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'G-XXXXXXXXXX'); </script>

Follow [Google’s instructions for installing Google Analytics 4](https://support.google.com/analytics/answer/9304153#zippy=%2Cadd-the-tag-to-a-website-builder-or-cms-hosted-website-eg-hubspot-shopify-etc)when installing Google Analytics. Remember to replace G-XXXXXXXXXX with your Google Measurement ID.

### Integrate Google consent mode v2 with Google Tag Manager[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#integrate-google-consent-mode-v2-with-google-tag-manager)

*   [In HubSpot, set up a cookie consent banner](https://knowledge.hubspot.com/privacy-and-consent/customize-your-cookie-tracking-settings-and-consent-banner#set-up-and-edit-your-cookie-consent-banner) with an opt-in policy type targeting EEA, EU, and UK visitors.
*   On your website, configure on-page consent default, configure consent updates, and install Google Tag Manager (see below for an example).
    *    Add this code as high in the `<head>` of the page as possible.

// Step 2: This snippet sets a default consent state, instructing Google's technologies how to behave if no consent is present. window.dataLayer = window.dataLayer || \[\]; function gtag() { dataLayer.push(arguments); } gtag('consent', 'default', { 'analytics\_storage': 'denied', 'ad\_storage': 'denied', 'ad\_user\_data': 'denied', 'ad\_personalization': 'denied', 'region': \["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IS", "IE", "IT", "LV", "LI", "LT", "LU", "MT", "NL", "NO", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "UK", "CH" \] }); // Step 3: This snippet sends consent updates from the HubSpot cookie banner to Google's tags using Consent Mode v2 var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', function(consent) { var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics)); var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement)); gtag('consent', 'update', { 'ad\_storage': hasAdsConsent ? 'granted' : 'denied', 'analytics\_storage': hasAnalyticsConsent ? 'granted' : 'denied', 'ad\_user\_data': hasAdsConsent ? 'granted' : 'denied', 'ad\_personalization': hasAdsConsent ? 'granted' : 'denied' }); }\]); // Step 4: This snippet installs Google Tag Manager <!-- Google Tag Manager --> <script>(function(w,d,s,l,i){w\[l\]=w\[l\]||\[\];w\[l\].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)\[0\], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-XXXXXXXX');</script> <!-- End Google Tag Manager -->

*   Add this code immediately after the opening `<body>` tag

// Step 4 continued: This snippet installs Google Tag Manager <!-- Google Tag Manager (noscript) --> <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXXX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript> <!-- End Google Tag Manager (noscript) -->

Follow [Google’s instructions for installing Google Tag Manager](https://support.google.com/tagmanager/answer/6103696?hl=en)when installing Google Tag Manager. Remember to replace `G-XXXXXXXXXX` with your Google Measurement ID.

Implement advanced Google consent mode v2 manually[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#implement-advanced-google-consent-mode-v2-manually)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This article provides an overview of how Advanced Google Consent Mode works, and how to implement it for Google Tag Manager or Google Analytics 4 using the HubSpot Cookie Banner.  
Note that this article assumes you’re familiar with writing HTML and JavaScript. 

When you implement consent mode on your website or app in advanced mode, Google tags are always loaded. Default consent is set (typically to denied) using the Consent Mode API. While consent is denied, Google tags will send [cookieless pings](https://support.google.com/google-ads/answer/10000067#Pings). When the user interacts with the HubSpot cookie banner, the consent state updates. If consent is granted, Google tags send full measurement data. 

To implement advanced consent mode via the HubSpot cookie banner, you must write a consent mode configuration script and install it along with the base installation code. This script will: 

*   Set up the default consent state.
*   Update the consent state when the user interacts with the HubSpot cookie banner. 

Learn more about the [types of Google consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#advanced_consent_mode).

### Integrate Google consent mode v2 with Google Tag Manager[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#integrate-google-consent-mode-v2-with-google-tag-manager)

The example code below provides one possible way you could implement advanced consent mode on your website. The code consists of two parts: 

**1\. Setting up the default consent state:** this snippet configures the default consent state for consent mode. Each consent category can be set to _granted_ or _denied_. The default can also be targeted to specific regions (identified by their region code). Learn more about [setting up consent mode](https://developers.google.com/tag-platform/security/guides/consent?consentmode=advanced). Make sure to configure the categories used and the regions based on your specific requirements.

2\. Updating consent when the user interacts with your cookie consent banner: this snippet sends consent updates from the HubSpot cookie banner to Google. This code extracts the consent state from the HubSpot cookie banner consent object and updates the corresponding categories in consent mode. These mappings are a suggestion, so make sure to update them to include the categories you require. Learn more about the [categories available for the HubSpot cookie banner](/docs/api/events/cookie-banner)and [consent mode categories.](https://support.google.com/tagmanager/answer/10718549?hl=en)

**Please note:** The code below is a recommendation and may not meet your regulatory requirements. Make sure to review and update the code to ensure it meets your needs.

<script> // 1. Set up default denied consent window.dataLayer = window.dataLayer || \[\]; function gtag() { dataLayer.push(arguments); } gtag('consent', 'default', { 'analytics\_storage': 'denied', 'ad\_storage': 'denied', 'ad\_user\_data': 'denied', 'ad\_personalization': 'denied', 'region': \["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IS", "IE", "IT", "LV", "LI", "LT", "LU", "MT", "NL", "NO", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "UK", "CH"\] }); // 2. Send consent updates from the cookie banner to google tags var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', function(consent) { var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics)); var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement)); gtag('consent', 'update', { 'ad\_storage': hasAdsConsent ? 'granted' : 'denied', 'analytics\_storage': hasAnalyticsConsent ? 'granted' : 'denied', 'ad\_user\_data': hasAdsConsent ? 'granted' : 'denied', 'ad\_personalization': hasAdsConsent ? 'granted' : 'denied' }); }\]); </script>

### Implement advanced Google consent mode for Google Analytics 4[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#implement-advanced-google-consent-mode-for-google-analytics-4)

First, you need to [find the installation code for Google Analytics 4 in your Google Analytics account](https://support.google.com/analytics/answer/9304153#zippy=%2Cadd-the-google-tag-directly-to-your-web-pages).  

This code may change as Google updates its product. Typically, you must paste two scripts in the page’s `<head>` html (similar to the scripts below). If copying these scripts, replace `MEASUREMENT_ID` with [your measurement ID](https://support.google.com/analytics/answer/12270356?hl=en).

To implement Advanced Consent Mode, add your consent mode configuration script before the installation code in your `<head>` html.

<script> // 1. Set up default denied consent window.dataLayer = window.dataLayer || \[\]; function gtag() { dataLayer.push(arguments); } gtag('consent', 'default', { 'analytics\_storage': 'denied', 'ad\_storage': 'denied', 'ad\_user\_data': 'denied', 'ad\_personalization': 'denied', 'region': \["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IS", "IE", "IT", "LV", "LI", "LT", "LU", "MT", "NL", "NO", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "UK", "CH"\] }); // 2. Send consent updates from the cookie banner to google tags var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', function(consent) { var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics)); var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement)); gtag('consent', 'update', { 'ad\_storage': hasAdsConsent ? 'granted' : 'denied', 'analytics\_storage': hasAnalyticsConsent ? 'granted' : 'denied', 'ad\_user\_data': hasAdsConsent ? 'granted' : 'denied', 'ad\_personalization': hasAdsConsent ? 'granted' : 'denied' }); }\]); </script> // GA4 installation code <script async src="https://www.googletagmanager.com/gtag/js?id=MEASUREMENT\_ID>"></script> <script> window.dataLayer = window.dataLayer || \[\]; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'MEASUREMENT\_ID'); </script>

### Implement advanced Google consent mode for Google Tag Manager[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#implement-advanced-google-consent-mode-for-google-tag-manager)

The base installation code for Google Tag Manager can be found in your [Google Tag Manager account](https://support.google.com/tagmanager/answer/6103696). 

The Google Tag Manager installation code can change as Google updates its products. Typically, you must install Google Tag Manager with two snippets. If copying these scripts, replace `CONTAINER_ID` with [your container ID](https://support.google.com/tagmanager/answer/6103696?hl=en#:~:text=2.%20Install%20the%20container).

1\. Head code: Google instructs that this code be pasted into the `<head>` tag.

<!-- Google Tag Manager --> <script>(function(w,d,s,l,i){w\[l\]=w\[l\]||\[\];w\[l\].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)\[0\], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= 'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','CONTAINER\_ID');</script> <!-- End Google Tag Manager -->

2\. Body code: Google instructs that this code be pasted into the `<body>` tag.

<!-- Google Tag Manager (noscript) --> <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=CONTAINER\_ID" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript> <!-- End Google Tag Manager (noscript) -->

#### Support basic consent mode for tags without built-in consent checks[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#support-basic-consent-mode-for-tags-without-built-in-consent-checks)

If a tag does not feature built-in consent checks, it is not compatible with advanced consent mode, and you must use basic consent mode instead. Under [basic consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode#advanced_consent_mode), tags only fire when they have consent. If a tag does not have consent, it is blocked. You can implement this functionality using Google Tag Manager’s [_Additional Consent Checks_](https://support.google.com/tagmanager/answer/10718549?hl=en#:~:text=Select%20Additional%20Consent%20Checks) feature, which allows you to specify consent mode categories that must be granted for the tag to fire.

This implementation requires you to:

1.  **Send events when consent is updated**: To properly configure your tags to work with the _Additional Consent Checks_ feature, you need to fire [a custom event](https://support.google.com/tagmanager/answer/7679219?hl=en) when consent updates. In the next step, you will use this event as a trigger for your tags, ensuring that they fire when consent is updated by the user. To send this custom event, you need to add a new line to your consent mode configuration script, in the consent update section (see below for an example).
2.  **Configure additional consent checks**: For each of the tags you identified as requiring consent but lacking built-in consent checks, make the following updates to that tag’s settings:
    1.  [Configure additional consent checks for that tag](https://support.google.com/tagmanager/answer/10718549?hl=en#:~:text=Tag%20consent%20settings). Select all the consent categories that apply to your tag.
    2.  [Add a custom event trigger to your tag](https://support.google.com/tagmanager/answer/7679219?hl=en). Make sure the event name matches the event name in your consent mode configuration script.

var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', function(consent) { var hasAnalyticsConsent = consent && (consent.allowed || (consent.categories && consent.categories.analytics)); var hasAdsConsent = consent && (consent.allowed || (consent.categories && consent.categories.advertisement)); gtag('consent', 'update', { 'ad\_storage': hasAdsConsent ? 'granted' : 'denied', 'analytics\_storage': hasAnalyticsConsent ? 'granted' : 'denied', 'ad\_user\_data': hasAdsConsent ? 'granted' : 'denied', 'ad\_personalization': hasAdsConsent ? 'granted' : 'denied' }); // Send a custom event when consent updates gtag('event', 'hubspotConsentUpdate') }\]);

The Cookie Banner Consent Listener API, allows scripts running on a webpage to receive consent updates from the Cookie Banner. Learn more about [how to get privacy consent status](/docs/api/events/cookie-banner#:~:text=Get%20privacy%20consent%20status). 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/events/implement-google-consent-mode#page-feedback)
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