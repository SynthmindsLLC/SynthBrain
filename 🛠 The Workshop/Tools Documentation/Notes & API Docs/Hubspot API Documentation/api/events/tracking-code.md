---
title: "Tracking code API overview"
description: "This page has been updated for working with new custom behavioral events. For legacy custom events, please [see the legacy documentation](https://legacydocs.hubspot.com/docs/methods/tracking_code_api/tracking_code_overview). In addition to tracking page views, the HubSpot tracking code allows you to identify visitors, track events, and manually track page views without reloading the page. The tracking code API allows you to dynamically create events and track event data in HubSpot."
type: "work"
tags:
- "Tracking Code"
- "API Overview"
relationships:
- "#related_to [[HubSpot Analytics]]"
- "#enables [[Identifying Visitors]]"
- "#allows [[Manual Page View Tracking]]"
- "#facilitates [[Custom Behavioral Event Tracking]]"
birthdate: "deathdate: "
---

Tracking code API overview
==========================

This page has been updated for working with new custom behavioral events. For legacy custom events, please [see the legacy documentation](https://legacydocs.hubspot.com/docs/methods/tracking_code_api/tracking_code_overview).

In addition to tracking page views, the HubSpot tracking code allows you to identify visitors, track events, and manually track page views without reloading the page. The tracking code API allows you to dynamically create events and track event data in HubSpot.

If your site uses the [privacy consent banner](https://knowledge.hubspot.com/getting-started-with-hubspot-v2/how-to-enable-a-privacy-policy-alert-if-you-are-doing-business-in-europe), learn how to manage the cookies that are added to a visitor's browser with the [cookie banner API](/docs/api/events/cookie-banner).

Function calls are pushed into the `_hsq` array. For example:

var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', { path string }\])

In this article, learn about how you can add functions to the tracking code to identify visitors, track page views, send event data, and more.

Identifying contacts
--------------------

The HubSpot analytics tool identifies contacts using two pieces of data:

*   The usertoken, which is stored in the visitor's `hubspotutk` browser cookie.
*   The contact's email address.

When the HubSpot tracking code tracks a visitor's action, such as a page view, it automatically associates that action with the visitor's usertoken. When you use the tracking code API to identify a visitor by email address, the analytics system will tie that email to the usertoken, allowing HubSpot to update an existing contact record or create a new one. Analytics data associated with the usertoken, such as page views and original source, will then appear on the contact record.

When you know a visitor's identity (e.g., email address), you can use the [identify](#identify-a-visitor) function to set identities in the tracker. You can then send the identity to HubSpot by making a separate [trackPageView](#track-page-view) or [trackCustomBehavioralEvent](#events-js-api) call.

When using this function keep in mind:

*   Avoid using a placeholder email for unknown visitors, as HubSpot will create a contact record with that placeholder email, and the visitor's `usertoken` cookie will be associated with that record. This leads to all unknown visitors being associated with your placeholder contact.
*   If you set an identity to a contact record and have any properties that are unique, we will drop any properties from the identity that violate uniqueness.

Identify a visitor[](https://developers.hubspot.com/docs/api/events/tracking-code#identify-a-visitor)
-----------------------------------------------------------------------------------------------------

**Please note:** if your account was created before September 8, 2021 and is set up to [allow contact properties to be updated through the tracking code](https://knowledge.hubspot.com/prevent-contact-properties-update-through-tracking-code-api), you can also include other contact properties to be updated with this function. For accounts created after September 8, 2021, this functionality is deprecated.

`_hsq.push(["identify", { {identity details} }]);`

Use this endpoint to identify website visitors and contacts.

*   **Visitor:** refers to any website visitor, regardless of whether they’re a HubSpot contact. HubSpot does not create records for visitors like it does for contacts.
*   **Contact:** refers to a visitor or offline contact that has a record in HubSpot. A contact can be identified by its unique email address.

To manually identify a visitor or contact, you can use either an email address or unique external ID:

*   **email:** identify a visitor by email address when you want to update an existing contact or create a new one. If a contact with that email exists in HubSpot, their contact record will update with the analytics data. If no contact exists at that email address, a new record will be created.
*   **id:** a custom external ID that identifies the visitor. Identifying a visitor with this ID will associate analytics data to that visitor. However, using the ID alone will not create a contact in HubSpot. Analytics data can only be associated with an existing contact through this method when:
    *   the visitor was previously identified by both ID and email.
    *   the visitor was previously identified by ID and also has a form submission associated with their record.

**Please note:** this external ID can only be used with the HubSpot tracking code. This ID cannot be used to retrieve or update any records through any other HubSpot tools or APIs. If you know the visitor’s email address, it’s recommended to use that as the unique identifier. Similarly, you should only identify a visitor with by ID when you don’t know their email address.

If you’ve previously sent analytics data to HubSpot using the visitor’s ID only, you can later include both the ID and an email address to associate the data from that ID with a contact. The existing contact will then be updated or created if no contact currently exists.

/\* The below example gets the value of a query string parameter '?email=' and uses that to identify the visitor \*/ function getParameterByName(name) { var match = RegExp('\[?&\]' + name + '=(\[^&\]\*)').exec(window.location.search); return match && decodeURIComponent(match\[1\].replace(/\\+/g, ' ')); } var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\["identify",{ email: getParameterByName("email") }\]); /\* The below example sets the email, as well as a custom property favorite\_color \*/ var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\["identify",{ email: getParameterByName("email"), favorite\_color: 'orange' }\]); /\* The below example sets the email and a custom external ID for the visitor. This assumes that your site includes a variable named 'user' that includes that user's ID in an 'id' property, and their email in an 'email' property. \*/ var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\["identify",{ email: user.email, id: user.id }\]);

When using this function, keep the following in mind:  

*   This function call stores the data in the tracker, but the data is not actually passed to HubSpot with this call. The data will only be passed when tracking a page view or an event (with either the [trackPageView](#track-page-view) or [trackEvent](#events-js-api) functions).
*   A contact can only have one ID and/or email address associated with them. If you try to assign two IDs to one email, only the first ID will be associated with the email address.
*   You must include an email address to tie the data to a contact.
*   If your account was created before September 8, 2021 and is set up to [allow contact properties to be updated through the tracking code](https://knowledge.hubspot.com/account/prevent-contact-properties-update-through-tracking-code-api), you can also include other contact properties to be updated with this function.
*   This function will _not_ restore previously deleted contacts. These contacts must be [restored in HubSpot](https://knowledge.hubspot.com/articles/kcs_article/contacts/restore-deleted-contacts-companies-deals-or-tickets).

Tracking in single-page applications[](https://developers.hubspot.com/docs/api/events/tracking-code#tracking-in-single-page-applications)
-----------------------------------------------------------------------------------------------------------------------------------------

The HubSpot tracking code will automatically record a page view when the code is first loaded, but you can also manually track page views in a single-page application without reloading the tracking code. You can use the [setPath](#set-path) and [trackPageView](#track-page-view) functions to update and track the current page. For example:

<!-- Set up the path for the initial page view --> <script> var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/home'\]); </script> <!-- Load the HubSpot tracking code --> <!-- Start of HubSpot Embed Code --> <script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/{hubId}.js"> </script> <!-- End of HubSpot Embed Code --> <!-- Tracking subsequent page views --> <script> var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/about-us'\]); \_hsq.push(\['trackPageView'\]); </script>

### Set page path[](https://developers.hubspot.com/docs/api/events/tracking-code#set-page-path)

`hsq.push(['setPath', { path string }])`

Update the path of the current page stored in the tracker. This function should be used by single-page applications to update the current page whenever a page is loaded. After using this function to update the path, you'll need to call the [trackPageView function](#track-page-view) to track the view of the current page.

Single-page applications should push a `setPath` call into `_hsq` before the tracking code loads to set the URL that gets tracked for the first page view. See the [track page view](#track-page-view) section below for an example.

When calling `setPath`, you'll include the path of the current page. The set path will be treated as relative to the current domain being viewed. The path should always start with a slash. If your URL also contains parameters, these will need to be included in the path as well. View the above code for examples.

When using this function, keep the following in mind:

*   Any path set using the **setPath** function will override the data in the referrer header. If you call **setPath** once, you'll need to use **setPath** to update the path for each view you want to track.
*   Repeatedly calling **setPath** will override the referrer, which can impact a contact's original source, depending on when a tracking request is made. 
*   This function can only update the path of the URL. The domain is set automatically based on the URL of the page on load, and the path that is set using this function is always treated as relative to that detected domain.

Example usage: // These examples assume that the domain of the site is // www.mydomain.com // Set the path to '/' and track the page var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/'\]); \_hsq.push(\['trackPageView'\]); // This will result in a view being recorded for // http://www.mydomain.com/ // Set the path to '/contact-us' and track the page var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/contact-us'\]); \_hsq.push(\['trackPageView'\]); // This will result in a view being recorded for // http://www.mydomain.com/contact-us // Set the path to '/blog/post?utm\_campaign=my-campaign' and track the page var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/blog/post?utm\_campaign=my-campaign'\]); \_hsq.push(\['trackPageView'\]); // This will result in a view being recorded for // http://www.mydomain.com/blog/post?utm\_campaign=my-campaign // Set the path to '/#/about-us' and track the page var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/#/about-us'\]); \_hsq.push(\['trackPageView'\]); // This will result in a view being recorded for // http://www.mydomain.com/#/about-us

### Track page view[](https://developers.hubspot.com/docs/api/events/tracking-code#track-page-view)

`_hsq.push(['trackPageView']);`

Track the page view for the current page. This function is automatically called when the tracking code is loaded on a page, but you can manually call this function to track subsequent views in a single page application.

**Please note:** calling this function manually before or during the initial page load could lead to duplicate views being tracked.

This function does not support any arguments. The page title tracked will be the current value of `document.title`.

The URL that gets tracked is based on one of the following:

*   The path set using the [setPath function](https://developers.hubspot.com/docs/methods/tracking_code_api/set_page_path). If your site is built as a single-page application, this function is the preferred method of setting the tracked path. View the [setPath](https://developers.hubspot.com/docs/methods/tracking_code_api/set_page_path) section above for disclaimers about the function.
*   If `setPath` has never been called, the tracked URL will be the referrer HTTP header in the request being made by the visitor's browser to HubSpot's tracking servers ([modifying the browser history state](https://developer.mozilla.org/en-US/docs/Web/API/History_API#Adding_and_modifying_history_entries) would update the value used for that header). The referrer header will not support URL fragments (anything after the # in the URL), as fragments are not included in the referrer header.

Example usage: // Track a new page using setPath: // Update the path stored in the tracker: var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['setPath', '/#/new-page'\]); // Track the page view for the new page \_hsq.push(\['trackPageView'\]); // Track a new page by updating the browser state: // Update the browser state, showing "updated.html" in the browser address bar var stateObj = { foo: 'updated' }; history.pushState(stateObj, "updated page", "updated.html"); //Track the page view for the new page, '/updated.html' var \_hsq = window.\_hsq = window.\_hsq || \[\]; \_hsq.push(\['trackPageView'\]);

When using this function, keep in mind the following:

*   While you can't prevent this function from being automatically called when the tracking code loads, you can control the URL recorded for the page by pushing a `setPath` call into `_hsq` before the tracking code is loaded.
*   If your site is a single-page application, you should avoid including a `<link rel="canonical">` tag in your page. If your page uses `<link rel="canonical">` tags, you'll need to use the [setPath](https://developers.hubspot.com/docs/methods/tracking_code_api/set_page_path) function to update the path of your new pages, as the canonical URL set from the link tag will override any detected URL if you're only updating the browser history state.

Privacy policy in tracking[](https://developers.hubspot.com/docs/api/events/tracking-code#privacy-policy-in-tracking)
---------------------------------------------------------------------------------------------------------------------

If your site has a [privacy consent banner](https://knowledge.hubspot.com/getting-started-with-hubspot-v2/how-to-enable-a-privacy-policy-alert-if-you-are-doing-business-in-europe) you can use functions to check and manage cookies placed into the visitor's browser. Learn more about [managing privacy consent banner cookies](/docs/api/events/cookie-banner).

Get cross-domain linking parameters[](https://developers.hubspot.com/docs/api/events/tracking-code#get-cross-domain-linking-parameters)
---------------------------------------------------------------------------------------------------------------------------------------

`_hsq.push(['addIdentityListener', function(hstc, hssc, hsfp) {}])` 

The HubSpot tracking code can be used across multiple sites with separate domains. This function will allow you to get the query parameters required to create create links that will allow you to track your visitors [across those separate domains](https://knowledge.hubspot.com/reports/set-up-your-site-domains#track-multiple-domains-with-cross-domain-linking). These query parameters are used by the HubSpot tracking code to identify a visitor across domains by ensuring that the separate cookies for the separate domains are merged to a single tracked visitor. You can also use cross-domain query parameters in links that are dynamically added to the page after the tracking code is loaded.

Cross-domain links are only needed when linking to a distinct domain (e.g., domain-one_.com_ and _domain-two.com_) that is also being tracked for a single HubSpot account. You do not need cross-domain link parameters when tracking visits between subdomains (e.g., www._domain-one.com_ and _blog.domain-one.com_). 

// Get the cross-domain query parameters and store them in a string, //so that they can be appended to links as needed. \_hsq.push(\['addIdentityListener', function(hstc, hssc, hsfp) { // Add these query parameters to any links that point to a separate tracked domain crossDomainTrackingParams = '&\_\_hstc=' + hstc + '&\_\_hssc=' + hssc + '&\_\_hsfp=' + hsfp; }\]);

Reapply analytics event handlers[](https://developers.hubspot.com/docs/api/events/tracking-code#reapply-analytics-event-handlers)
---------------------------------------------------------------------------------------------------------------------------------

`_hsq.push(['refreshPageHandlers'])`

This function reapplies any analytics event handlers that are set up in the analytics settings for the HubSpot account.

This would include reapplying any [clicked element events](https://knowledge.hubspot.com/events/create-clicked-element-events) that have been set up.

 You can use this function to automatically reapply click handlers when content on the page is updated, such as updating a section of content or displaying a modal window on the page.

**Please note:** this functionality is automatically triggered as part of the [`setPath`](https://developers.hubspot.com/docs/methods/tracking_code_api/set_page_path) function, so you'll only need to use this function when updating the content without updating the tracked page URL.

// Reapply event handlers after updating the page content \_hsq.push(\['refreshPageHandlers'\]);

Tracking custom behavioral events (Marketing Hub Enterprise only)[](https://developers.hubspot.com/docs/api/events/tracking-code#tracking-custom-behavioral-events-marketing-hub-enterprise-only-)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using custom behavioral events, you can tie event completions to contacts records and populate event properties with metadata about the event. To retrieve custom behavioral events, use the [web analytics API](/docs/api/events/web-analytics).

Through the API, events can be triggered using the event's internal name, which is assigned automatically when you create the event. You can find an event's internal name either [in HubSpot](https://knowledge.hubspot.com/analytics-tools/create-custom-behavioral-events#define-the-api-call) or by [using the events API](https://legacydocs.hubspot.com/docs/methods/events/get_events). Learn how to [find the internal name for an event](https://knowledge.hubspot.com/analytics-tools/create-custom-behavioral-events#define-the-api-call). 

![custom-event-internal-name](https://developers.hubspot.com/hs-fs/hubfs/Imported%20sitepage%20images/custom-event-internal-name.png?width=851&name=custom-event-internal-name.png)

There are three types of events that you can create in HubSpot:

*   [Clicked element events](https://knowledge.hubspot.com/analytics-tools/create-clicked-element-events):events tied to clickable elements on a website page. Will automatically populate a set of default HubSpot event properties through the tracking code. You can further customize these events with the [trackCustomBehavioralEvent](#events-js-api) function.
*   [Visited URL events](https://knowledge.hubspot.com/analytics-tools/create-visited-url-events): events tied to page loads at specified URLs. Will automatically populate a set of default HubSpot event properties through the tracking code. You can further customize these events with the [trackCustomBehavioralEvent](#events-js-api) function.
*   [Manually tracked behavioral events](/docs/api/analytics/events): custom events that are unique to your business, as well as events that may not be automatically captured by HubSpot or by an integration. Manually send data to HubSpot events through the [HTTP API](/docs/api/analytics/events).

For each event type, HubSpot includes a set of standard properties that can capture certain metadata at the time of completion, including UTM parameters or device and operating system metadata.

 Since this function works alongside HubSpot's analytics tracking, any events triggered through the JavaScript API will automatically be associated with the visitor's _hubspotutk_ cookie, so the event would automatically be [tied to the contact associated with that usertoken](#identities-overview).

### trackCustomBehavioralEvent

`_hsq.push(["trackCustomBehavioralEvent", { {event details} }]);`

Use this function to track an [event](https://knowledge.hubspot.com/events-user-guide-v2/a-quick-tour-of-events) using JavaScript and HubSpot's tracking code. You can use events to track specific activities completed by visitors on your site. Tracked events can show up in contacts' timelines.

/\* Example code to fire a custom behavioral event using the name "clicked Buy Now button" when a visitor clicks an element with the 'buyNow' id. \*/ document.getElementById("buyNow").onclick = function() {\_hsq.push(\["trackCustomBehavioralEvent", { name: "pe123456\_course\_registration", properties: { course\_id: "Math101" } }\]);

Use this table to describe parameters / fields
| Arguments | How to use | Description |
| --- | --- | --- |
| 
`Name`

 | name:"internal\_name" | 

The event\_id or internal name of the event that you created in HubSpot.

 |
| 

`Properties`

 | property\_name: "property\_value" | 

A list of key-value pairs, with one key-value pair per property.

`property_name` is the internal name of the event property you’ve created for the event, and `property_value` is the value to add to the property. 

You can also track non-defined properties and go back to create them after event tracking.

 |

### Customize your tracking code to send custom behavioral event data

By default, HubSpot creates a set of properties for each event you create. For [clicked element](https://knowledge.hubspot.com/analytics-tools/create-clicked-element-events) or [visited URL](https://knowledge.hubspot.com/analytics-tools/create-visited-url-events) events, HubSpot will auto-populate some of those properties with data. But you can also customize your tracking code to send data to the event's properties.

*   In your HubSpot account, navigate to **Reports** \> **Analytics tools**.
*   Click **Custom Behavioral Events**.
*   Click the **name** of the event that you want to track.
*   Under _Properties_, copy the **internal name** of the event.![custom-clicked-element-event-internal-name0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-clicked-element-event-internal-name0.png?width=604&name=custom-clicked-element-event-internal-name0.png)
*   Then, in the properties table, click the **name** of the event property that you want to send data to.
*   In the right panel, click the **</> source icon** to view the property's internal name. You'll use this name when customizing the tracking code.  
    ![custom-behavioral-event-property-internal-name0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-behavioral-event-property-internal-name0.png?width=585&name=custom-behavioral-event-property-internal-name0.png)
*   Now that you have your event and event property data, click the **Settings** icon to navigate to your account settings. Then, in the left sidebar menu, navigate to **Tracking & Analytics** > **Tracking code.**
*   Click **Customize javascript**.  
    ![tracking-code-customize-javascript0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/tracking-code-customize-javascript0.png?width=420&name=tracking-code-customize-javascript0.png)
*   In the upper right, click **Add custom JavaScript**.
*   In the right sidebar, enter a **name** for your custom JavaScript, then enter the JavaScript, including the [trackCustomBehavioralEvent](#events-js-api) function. This JavaScript be executed after the tracking code loads for a page.

// example usage \_hsq.push(\['trackCustomBehavioralEvent',{ name: '((behavioral\_event\_internal\_name))”, properties: { internal\_property\_name: property\_value} } \]);

For example, if your event tracks a course registration when a button with the HTML ID `register_for_econ101` is clicked, your JavaScript might look like the following: ![customize-tracking-code0-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/customize-tracking-code0-1.png?width=680&name=customize-tracking-code0-1.png)

*   Click **Save** to save your JavaScript. Your tracking code will now load with your custom JavaScript.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/events/tracking-code#page-feedback)
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