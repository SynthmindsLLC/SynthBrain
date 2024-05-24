Cookie consent banner API
=========================

Super admins and users with [permission to edit website settings](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#marketing) can customize visitor cookie tracking and consent banners to comply with EU cookie laws and the [General Data Protection Regulation (GDPR)](https://www.hubspot.com/data-privacy/gdpr).

A cookie consent banner allows visitors to opt in or opt out of being tracked in your HubSpot account with cookies. This feature works for all HubSpot pages as well as any external pages with your [HubSpot tracking code](https://knowledge.hubspot.com/articles/kcs_article/reports/install-the-hubspot-tracking-code) installed. [Customize the cookie tracking settings and cookie consent banner.](https://knowledge.hubspot.com/reports/customize-your-cookie-tracking-settings-and-privacy-policy-alert)

In this article, learn how to manage the cookies that are added to a visitor's browser through the cookie consent banner.

* * *

Remove cookies
--------------

`_hsp.push(['revokeCookieConsent']);`

Remove the cookies created by the HubSpot tracking code that are included in the consent banner under GDPR, include the HubSpot cookies related to tracking the visitor. As a result of the cookies being removed, the visitor would see the [cookie consent banner](https://knowledge.hubspot.com/getting-started-with-hubspot-v2/how-to-enable-a-privacy-policy-alert-if-you-are-doing-business-in-europe) on their next page load, as they would appear as a new visitor.

This function does not remove cookies placed by non-HubSpot banners. You can find the specific list of cookies that will be removed on [HubSpot's Knowledge Base](https://knowledge.hubspot.com/articles/kcs_article/reports/what-cookies-does-hubspot-set-in-a-visitor-s-browser#consent-banner-cookies). 

If cookie blocking is turned on, this function will revoke consent so any third-party cookies will not be updated or dropped during future visits to the website. 

/\* Example code to remove the consent banner cookies when a visitor clicks an element with the 'removeCookies' id. \*/ var \_hsp = window.\_hsp = window.\_hsp || \[\]; document.getElementById("removeCookies").onclick = function() { \_hsp.push(\['revokeCookieConsent'\]); };

Place do not track cookie
-------------------------

`_hsq.push(['doNotTrack']);`

Places the `__hs_do_not_track` cookie in the visitors browser, which will prevent the HubSpot tracking code from sending any information for the visitor.

You can remove the cookie by calling the function again and including the `{track: true}` argument:  
`_hsq.push(['doNotTrack', {track: true}]);`

**Please note:** this function prevents all information from being collected by the tracking code, including anonymized traffic and [custom event](#events-js-api) data.

/\* Example code to place the \_\_hs\_do\_not\_track cookie for the visitor when they click an element with the 'doNotTrack' id. \*/ document.getElementById("doNotTrack").onclick = function() { \_hsq.push(\['doNotTrack'\]); };

Get privacy consent status
--------------------------

`_hsp.push(['addPrivacyConsentListener', callbackFunction]);`

Get the privacy consent status of the current visitor. There are 3 categories of consent that can be used to provide more granular control to the user. These each have their own keys within the `consent.categories` object:

*   `consent.categories.analytics`
*   `consent.categories.advertisement`
*   `consent.categories.functionality`

The _callbackFunction_ will be called, depending on the state of the page:

*   If the banner is not enabled, or if the visitor has previously seen the banner and clicked accept or decline:
    *   the _callbackFunction_ will be called immediately if the banner code is already loaded.
    *   the _callbackFunction_ will be called after the tracking code loads if the function is pushed to **\_hsp** before the tracking code loads.

*   If the banner is enabled, the callback function will be called when the visitor clicks on the accept or decline button.  

// Log the analytics category consent status of the current visitor to the console var \_hsp = window.\_hsp = window.\_hsp || \[\]; // analytics \_hsp.push(\['addPrivacyConsentListener', function(consent) { console.log(consent.categories.analytics); }\]); // advertisement \_hsp.push(\['addPrivacyConsentListener', function(consent) { console.log(consent.categories.advertisement); }\]); // functionality \_hsp.push(\['addPrivacyConsentListener', function(consent) { console.log(consent.categories.functionality); }\]); // or it can all be done in one call \_hsp.push(\['addPrivacyConsentListener', function(consent) { console.log(\`analytics: ${consent.categories.analytics}\`); console.log(\`advertisement: ${consent.categories.advertisement}\`); console.log(\`functionality: ${consent.categories.functionality}\`); }\]);

Cookies not by category[](https://developers.hubspot.com/docs/api/events/cookie-banner#cookies-not-by-category)
---------------------------------------------------------------------------------------------------------------

**Please note:** This is provided for backward compatibility with older scripts. For all new websites you should use the cookies by category method, giving more granular control over cookie activation.

`_hsp.push(['addPrivacyConsentListener', callbackFunction]);`

Allows you to get the _true_ or _false_ privacy consent status of the current visitor.

The _callbackFunction_ will be called, depending on the state of the page:

*   If the banner is not enabled, or if the visitor has previously seen the banner and clicked accept or decline:
    *   the _callbackFunction_ will be called immediately if the banner code is already loaded.
    *   the _callbackFunction_ will be called after the tracking code loads if the function is pushed to **\_hsp** before the tracking code loads.

*   If the banner is enabled, the callback function will be called when the visitor clicks on the accept or decline button.  

// Log the consent status of the current visitor to the console var \_hsp = (window.\_hsp = window.\_hsp || \[\]); \_hsp.push(\["addPrivacyConsentListener", function (consent) { if (consent.allowed) { console.log('something') } }\])

The `callbackFunction` accepts a `consent` object as its only argument.

The `consent` object has a single `allowed` property that will be `true` if:

*   The [cookie consent banner](https://knowledge.hubspot.com/getting-started-with-hubspot-v2/how-to-enable-a-privacy-policy-alert-if-you-are-doing-business-in-europe) is not enabled, or is enabled in notify-only mode.
*   The visitor clicks accept on the banner when opt-in mode is enabled.
*   The visitor has previously clicked accept on the banner when opt-in mode is enabled.

The property will be false if the consent banner is enabled in opt-in mode and the visitor clicks or has previously clicked the decline button.

​​Enable website visitors to manage their consent[](https://developers.hubspot.com/docs/api/events/cookie-banner#enable-website-visitors-to-manage-their-consent)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Call the `showBanner` function to resurface the banner, enabling website visitors to make changes to their consent preferences. For example:

​​var \_hsp = window.\_hsp = window.\_hsp || \[\]; ​​\_hsp.push(\['showBanner'\]);

The behavior of`showBanner`varies by policy and is only available for Opt-In and Cookie-By-Category policies. 

For Opt-In policies, calling `showBanner`  will cause the banner to reappear, as shown in the video below:

![HubSpot Video](https://api-na1.hubapi.com/video/v1/public/40218050953/poster?portalId=53)

 For Cookies-By-Category policies, calling `showBanner` will cause the modal for selecting each category to reappear, as shown in the video below:

![HubSpot Video](https://api-na1.hubapi.com/video/v1/public/40218140317/poster?portalId=53)

UI Examples[](https://developers.hubspot.com/docs/api/events/cookie-banner#ui-examples)
---------------------------------------------------------------------------------------

This functionality can be made available to visitors in the form of buttons/links on your website that they can use to re-open the banner and edit their preferences. The following are examples with code. 

### Button[](https://developers.hubspot.com/docs/api/events/cookie-banner#button)

A button, often placed in the website footer.

<button type="button" id="hs\_show\_banner\_button" onClick="(function(){ var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['showBanner'\]); })()" > Cookie Settings </button>#hs\_show\_banner\_button { display: inline-block; text-align: center; height: 50px; background-color: #425b76; border: 1px solid #425b76; border-radius: 3px; padding: 10px 16px; text-decoration: none; color: #fff; font-family: inherit; font-size: inherit; font-weight: normal; line-height: inherit; text-shadow: none; }

 ![HubSpot Video](https://api-na1.hubapi.com/video/v1/public/40220919441/poster?portalId=53)

### Fixed position button[](https://developers.hubspot.com/docs/api/events/cookie-banner#fixed-position-button)

A button with fixed positioning on the bottom of the screen. This kind of button has the advantage of being readily available and easy to find, while being somewhat obtrusive UX.

<button id='hs-hud-cookie-settings' onClick="(function(){ var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['showBanner'\]); })()"> Cookie Settings </button> button#hs-hud-cookie-settings { position: fixed !important; bottom: 0px; right: 10px; color: white; background-color: #425b76; padding: 5px; border-top-right-radius: 5px; border-top-left-radius: 5px; border-width:0; appearance:none; }

 ![HubSpot Video](https://api-na1.hubapi.com/video/v1/public/40220919737/poster?portalId=53)

### Link[](https://developers.hubspot.com/docs/api/events/cookie-banner#link)

A link or highlighted text.

<a id="hs-cookie-settings-link" onClick="(function(){ var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['showBanner'\]); })()"> Cookie Settings </a>#hs-cookie-settings-link { cursor: pointer; }

 ![HubSpot Video](https://api-na1.hubapi.com/video/v1/public/40220920222/poster?portalId=53)

Block third party cookies manually[](https://developers.hubspot.com/docs/api/events/cookie-banner#block-third-party-cookies-manually)
-------------------------------------------------------------------------------------------------------------------------------------

The HubSpot Consent Banner supports manual handling of third party tracking technologies and cookies. It's recommended to use manual handling if you have a complicated website and/or a dedicated web developer. If auto-blocking does not work for your site, manual blocking is also a good option.  
  
Manual blocking is implemented through the [Cookie Banner Consent Listener API](https://developers.hubspot.com/docs/api/events/cookie-banner). This API is used to prevent tracking technologies from running until they have consent. To get started, take a look at the examples below.

### General usage[](https://developers.hubspot.com/docs/api/events/cookie-banner#general-usage)

If you want to install a tracking script onto your website to display targeted ads to visitors. You could use something like the below:

`<script src=”https://my.advertisement.script.com/ads”></script>`

When this script is pasted into the head HTML of a page on a website it would run anytime someone visits that page, regardless of their consent status. Visitors will have cookies placed on their browser without consent.  
  
To prevent the script from running without consent, you can use the HubSpot Cookie Banner Consent Listener API to install the script when the visitor has consented to its cookies. Consent listeners are functions that run whenever the visitor submits their consent. To use this functionality, a consent listener needs to be created that adds the script to the page if the visitor has consented to advertisement cookies.

<script> var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', (consent) => { if (consent.categories.advertisement) { const script = document.createElement('script'); script.src = "https://my.advertisement.script.com/ads"; document.head.appendChild(script) } }\]) </script>

This script will register the consent listener with the cookie banner. When consent to cookies is submitted, the consent listener will run, adding HubSpot's third party ads script to the page.

### Example: Google Tag[](https://developers.hubspot.com/docs/api/events/cookie-banner#example-google-tag)

[Google Tag or gtag.js](https://developers.google.com/tag-platform/gtagjs) can be used to add Google Analytics. For example:

<!-- Google tag (gtag.js) --> <script async src="https://www.googletagmanager.com/gtag/js?id=GA\_TRACKING\_ID"></script> <script> window.dataLayer = window.dataLayer || \[\]; function gtag(){window.dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'GA\_TRACKING\_ID'); </script>

To load Google Analytics when analytics consent has been given, the gtag script needs to be added when consent is given:

<!-- Google tag (gtag.js) --> <script> var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', (consent) => { if (consent.categories.analytics) { const script = document.createElement('script'); script.src = "https://www.googletagmanager.com/gtag/js?id=GA\_TRACKING\_ID"; script.async = 'true' document.head.appendChild(script) } }\]) </script> <script> window.dataLayer = window.dataLayer || \[\]; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'GA\_TRACKING\_ID'); </script>

### Example: HotJar[](https://developers.hubspot.com/docs/api/events/cookie-banner#example-hotjar)

[HotJar](https://help.hotjar.com/hc/en-us/articles/115009336727-How-to-Install-Your-Hotjar-Tracking-Code#manually) is another example of analytics tracking. For example:

[HotJar](https://help.hotjar.com/hc/en-us/articles/115009336727-How-to-Install-Your-Hotjar-Tracking-Code#manually) is another example of analytics tracking. For example:

<!-- Hotjar Tracking Code --> <script> (function(h,o,t,j,a,r){ h.hj=h.hj||function(){(h.hj.q=h.hj.q||\[\]).push(arguments)}; h.\_hjSettings={hjid:HOT\_JAR\_ID,hjsv:6}; a=o.getElementsByTagName('head')\[0\]; r=o.createElement('script');r.async=1; r.src=t+h.\_hjSettings.hjid+j+h.\_hjSettings.hjsv; a.appendChild(r); })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv='); </script>

To ensure Hotjar runs when analytics consent is given, the consent listener can be added.

<!-- Hotjar Tracking Code --> <script> var \_hsp = window.\_hsp = window.\_hsp || \[\]; \_hsp.push(\['addPrivacyConsentListener', (consent) => { if (consent.categories.analytics){ (function(h,o,t,j,a,r){ h.hj=h.hj||function(){(h.hj.q=h.hj.q||\[\]).push(arguments)}; h.\_hjSettings={hjid:HOT\_JAR\_ID,hjsv:6}; a=o.getElementsByTagName('head')\[0\]; r=o.createElement('script');r.async=1; r.src=t+h.\_hjSettings.hjid+j+h.\_hjSettings.hjsv; a.appendChild(r); })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv='); } }\]) </script>

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/events/cookie-banner#page-feedback)
-------------------------------------------------------------------------------------------------

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