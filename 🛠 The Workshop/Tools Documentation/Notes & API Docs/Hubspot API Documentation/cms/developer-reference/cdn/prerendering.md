---
Please provide me with more information about the mission you want to describe. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, or something else?"
* **What is the main objective?** What are you trying to achieve? 
* **What are the key values and principles?** What are the guiding factors for the mission?
* **What is the target audience?** Who is the mission intended to inspire and motivate?

Once you provide more details, I can help you write a compelling mission statement.
---

Prerendering


================

Last updated: April 4, 2023

To improve page load speed and security, HubSpot automatically creates static versions of pages, blog posts, and knowledge base articles when possible. This means that, rather than assembling the page's data and layout for each request, HubSpot will render the page ahead of time and push it to the [CDN](/docs/cms/developer-reference/cdn). Local copies of prerendered pages are stored around the globe so that users across the world can access pages faster based on their location.

This is separate from the concept of caching. All prerendered pages are cacheable on HubSpot's CDN. Prerendering is the process by which the HubSpot CMS generates the static version of a page. Even if the CDN doesn't have a page cached, requests will be faster because the page is already in its final rendered form.

Not all pages are eligible for prerendering, depending on the type of content it serves. When a page is not eligible, HubSpot will continue to serve that page dynamically. Below, learn more about prerendering.

Overview[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#overview)
-------------------------------------------------------------------------------------------------

Updating data that affects your page will automatically trigger a render. For example, publishing an edit to a page's template will re-render it. Changes to other shared data, such as CMS settings, may cause pages pages to be re-rendered.

Generally, the prerendering process takes seconds to complete. If a large change is made, such as updating a module that’s included in many templates and pages, it may be minutes before all pages are updated.

CSS, JavaScript and images files have always been statically generated on HubSpot, so they have effectively always been prerendered. 

HubL in JS or CSS files is evaluated only once when the asset is published.

Check if a page is prerendered[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#check-if-a-page-is-prerendered)
---------------------------------------------------------------------------------------------------------------------------------------------

The easiest way to tell if a page is prerendered is by looking at the HTTP response headers of the request. If it includes a `X-HS-Prerendered` header, the page is prerendered. The value of the header is the last time the page was prerendered. 

[![chrome network tab showing prerendered header](https://developers.hubspot.com/hs-fs/hubfs/chrome-network-tab-prerendered.png?width=800&height=288&name=chrome-network-tab-prerendered.png "chrome network tab showing prerendered header")](https://cdn2.hubspot.net/hub/53/hubfs/chrome-network-tab-prerendered.png)

The other way to tell is to load the page with a `?hsDebugOnly=true` query param. This will include an indication if the page can be prerendered. If it can't be prerendered, a list of issues that prevent prerendering will be listed. If the formatting of the debug information is hard to read you can use the parameter `?hsDebug=true` instead, then inspect your page the same debug information will appear in a formatted HTML comment near the bottom of your page.

[![Screenshot of HTML comment showing that page can be prerendered](https://developers.hubspot.com/hs-fs/hubfs/hsDebugTrue-prerender.png?width=300&height=416&name=hsDebugTrue-prerender.png "Screenshot of HTML comment showing that page can be prerendered")](https://cdn2.hubspot.net/hub/53/hubfs/hsDebugTrue-prerender.png)

Incompatible features[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#incompatible-features)
---------------------------------------------------------------------------------------------------------------------------

The use of the features below prevents the same response from being served to every user, so they prevent the serving of a static prerendered page. Pages using some of these features may be served using partial prerendering.

### Incompatible HubL variables[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#incompatible-hubl-variables)

*   `account` 
*   `company`
*   `contact`
*   `local_dt`
*   `owner`
*   `query`
*   `request_contact`
*   `request.cookies`
*   `request.full_url`
*   `request.geoip*` (deprecated)
*   `request.headers`
*   `request.path_and_query`
*   `request.query`
*   `request.query_dict`
*   `request.referrer`
*   `request.remote_ip`
*   `year`

The HubL request variables generally have JavaScript based alternatives you can use. Enabling you to avoid using those variables.

### Incompatible HubL functions[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#incompatible-hubl-functions)

*   `personalization_token`
*   `today`
*   `unixtimestamp`

### Incompatible functionalities[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#incompatible-functionalities)

*   Password-protected pages
*   Pages that use [adaptive tests](https://knowledge.hubspot.com/website-pages/create-an-adaptive-test-for-a-page)

Pages that include [smart content](https://knowledge.hubspot.com/website-pages/create-and-manage-smart-content-rules) are supported via [partial pre-rendering](#what-is-partial-prerendering-).

How can I make my pages compatible with prerendering?[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#how-can-i-make-my-pages-compatible-with-prerendering-)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Load the page with a `?hsDebugOnly=true` query param, and there will be additional output that can help point to specific features that prevent pre-rendering. This additional output includes:

*   A list of specific features that may be causing issues
*   Specific files and line numbers of templates that use uncacheable variables

When possible, move all dynamic rendering of content to JavaScript executed in the user’s browser. You may also use Serverless Functions to pull in dynamic data.

What is partial prerendering?[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#what-is-partial-prerendering-)
-------------------------------------------------------------------------------------------------------------------------------------------

Partial prerendering allows HubSpot to serve “mostly” prerendered pages. For example, a page may be entirely static except for a contact’s name displayed on the page. The page can be prerendered except for that contact name. Just before returning the page to the user, HubSpot will perform a render of just those dynamic values.

Pages that use partial prerendering can't be cached at the CDN or the browser. However, partially prerendered pages are faster to deliver than pages that can't be partially prerendered. Partially prerendered pages also have the ability to fall back to an unpersonalized state in case of an outage or an attack.

While partial prerendering may help the speed and reliability of your site, removing the HubL features that make pages non-prerenderable will have a much greater positive effect on your overall page performance.

How can I tell if my page uses partial prerendering?[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#how-can-i-tell-if-my-page-uses-partial-prerendering-)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Load the page with a `?hsPrcDebug=true` query param, and there will be additional output about the pre-rendered content for that page. If the page is prerendered, the `X-HS-Prerendered` header will  be present and contain `partial` before the time the page was partially prerendered.

The features below _are currently supported_ with partial prerendering. The page will be partially pre-rendered and expressions using these will be instead be evaluated at serve-time.

### HubL variables[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#hubl-variables)

*   `account`
*   `company`
*   `contact`
*   `local_dt`
*   `owner`
*   `query`
*   `request`
*   `request_contact`
*   `year`

### HubL filters[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#hubl-filters)

*   `|random`
*   `|shuffle`

How does prerendering affect CSS combining?[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#how-does-prerendering-affect-css-combining-)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

With page prerendering, HubSpot no longer automatically combines CSS at the page-level. There’s several reasons for this:

1.  CSS combining may optimize a single page view, but it hurts subsequent page views because all the CSS has to be re-downloaded for each page.
2.  HTTP/2 (all HubSpot sites served over SSL use HTTP/2) [solves a lot of the problems](https://developers.google.com/web/fundamentals/performance/http2#request_and_response_multiplexing) with many CSS files, so combining CSS doesn’t provide as much benefit as it used to.
3.  To verify that the combined CSS doesn’t break anything on a page, HubSpot runs an automated visual check on the page with the combined CSS. The visual checker isn’t 100% effective (consider elements that only appear or scroll, JavaScript animations, etc.) so sometimes it will miss problems.
4.  Prerendering pages is much more important than CSS combining for site availability and speed. Since it’s required to verify combined CSS after every renderer, it’s not feasible to also combine and visually verify CSS on every change.

This is referring to functionality that historically combined module and page styles into one monolithic file per page.

This has no effect on CSS files that are combined using the `include` tag. 

Without page-level automatic CSS combining, how can I optimize delivery of CSS?[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#without-page-level-automatic-css-combining-how-can-i-optimize-delivery-of-css-)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Take advantage of modules. If your CSS is unique to the module, put it in the module's CSS or a CSS file you are tying to the module with require\_css. This means the small css file specific to just this module will only load on pages where that module is used. For subsequent page loads, the CSS for modules already seen by the user will be cached and they only need to download the CSS for assets they haven't yet seen.
*   If you share styles like layout or utility classes etc in multiple modules or modules are visually similar so they share a lot of CSS, consider creating a CSS file that you require\_css in each of the modules that need it. This enables you to avoid repeating CSS in each module, while also getting the caching benefits. 

*   Another way to consider this is also modules that are used everywhere on your site - for example if your header and footer modules don't change per page, consider using this approach for their CSS styles.

Related resources[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#related-resources)
-------------------------------------------------------------------------------------------------------------------

*   [Optimizing CMS Hub site performance](https://developers.hubspot.com/docs/cms/guides/speed)
*   [Using JavaScript frameworks and libraries on HubSpot](//developers.hubspot.com/docs/cms/guides/js-frameworks)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering#page-feedback)
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