---
Please provide me with more information about the mission you want to write about. I need to know what the mission is about in order to write it effectively. 

For example, tell me: "* **What is the purpose of this mission?** (What are you trying to achieve?)"
* **Who is involved?** (Who is this mission for?)
* **What are the key objectives?** (What are the specific goals you want to reach?)
* **What are the challenges?** (What obstacles will you need to overcome?)

Once I have a better understanding of the mission, I can help you write a strong and compelling mission statement.
---

Debugging methods and error types


=====================================

Last updated: November 17, 2022

Debugging code and understanding where and how to view errors is an important part of development on the HubSpot CMS. There are a number of tools you can use to increase efficiency when building and debugging and to make sure your website is optimized as you continue to build it out. 

Errors[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#errors)
-------------------------------------------------------------------------------------------------

The HubSpot CMS [developer file system](/docs/cms/key-concepts#developer-file-system) has many forms of validation to ensure your templates and modules render correctly on pages. 

### Fatal errors[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#fatal-errors)

Fatal errors are errors that would prevent a page from successfully rendering. To ensure live content renders correctly, the HubSpot CMS prevents publishing templates that have fatal errors. An example of a fatal error would be missing required HubL variables, such as `standard_header_includes`. This will cause errors when developing in the Design Manager or when uploading files through the CMS CLI. [The VS Code Extension](https://marketplace.visualstudio.com/items?itemName=hubspot.hubl) supports HubL linting, and can display the fatal errors in-context ahead of uploading the file.

![screenshot of a fatal error - design manager](https://developers.hubspot.com/hs-fs/hubfs/fatal%20error%20-%20design%20manager.png?width=580&height=245&name=fatal%20error%20-%20design%20manager.png "screenshot of a fatal error - design manager")

![screenshot of a fatal error - CMS CLI](https://developers.hubspot.com/hs-fs/hubfs/fatal%20error%20-%20CMS%20CLI.png?width=580&height=363&name=fatal%20error%20-%20CMS%20CLI.png "screenshot of a fatal error - CMS CLI")

Fatal errors must be resolved in order to publish files. 

### Warnings[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#warnings)

Warnings are errors or issues which do not prevent the publishing of files. Warnings are often suggestions in syntax or potential issues a developer might be missing. [The VS Code Extension](https://marketplace.visualstudio.com/items?itemName=hubspot.hubl) supports HubL linting, and can display the warnings in-context ahead of uploading the file. For example, if you try to include a file which does not exist, this throws a warning to alert the developer.

![warning - design manager](https://developers.hubspot.com/hs-fs/hubfs/warning%20-design%20manager.png?width=580&height=272&name=warning%20-design%20manager.png "warning - design manager")

Warnings will never prevent the publishing of files, however, it is recommended to investigate warnings. 

Debug mode on live pages[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#debug-mode-on-live-pages)
-------------------------------------------------------------------------------------------------------------------------------------

You can enable debug mode on a live page by loading the page with a `?hsDebug=true` query string in the URL.

**Please note:** debug mode isn't supported on [system pages](/docs/cms/building-blocks/templates#system-pages), such as 404 and password pages. 

When loading a live page with this query string, the page will be rendered:

*   with non-minified files.
*   with non-combined CSS files (individual CSS files served).
*   without serving cached files.

In addition, when you load a page with `?hsDebug=true`, debugging information will be added to the bottom of the page source code, including:

*   Whether the page can be [prerendered](/docs/cms/developer-reference/cdn/prerendering), and the reasons why if it cannot be prerendered.
*   A breakdown of rendering request timing, which can be helpful for knowing which page components take longer to render. This breakdown will also be added to the _Timing_ tab in your browser's developer console under _Doc_ requests.

![timing-tab-request-details](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/timing-tab-request-details.png?width=614&name=timing-tab-request-details.png)

*   Errors and warnings, such as HubL function limits or missing files.

![debug-page-source-elements-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/debug-page-source-elements-tab.png?width=614&name=debug-page-source-elements-tab.png)

Developer mode in the page editor[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#developer-mode-in-the-page-editor)
-------------------------------------------------------------------------------------------------------------------------------------------------------

You can also load the page editor in HubSpot with the query string to enable developer features, such as [copy sections as HubL](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#copy-section-hubl) and the ability to open specific modules in the design manager from the page editor.  

*   In the page editor, add the following parameter to the URL, then press **Enter**: `?developerMode=true`
*   With the page reloaded, you'll now be in developer mode. You can exit developer mode at any time by clicking **Exit developer mode** in the upper right.

![developer-mode-top-navigation-bar](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/developer-mode-top-navigation-bar.png?width=1148&name=developer-mode-top-navigation-bar.png)While you're in developer mode, you can navigate to the code for a specific module by clicking the associated module, then clicking Open in design manager in the sidebar editor.

![developer-mode-open-design-manager-for-module](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/developer-mode-open-design-manager-for-module.png?width=1138&name=developer-mode-open-design-manager-for-module.png)

You can also reset any unpublished changes back to the default content of the template:

*   Click the **Contents** tab.
*   To the right of template name, click **Reset content**.

![developer-mode-reset-contents](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/developer-mode-reset-contents.png?width=378&name=developer-mode-reset-contents.png)

*   In the dialog box, click **Yes, reset**.

View HubL output[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#view-hubl-output)
---------------------------------------------------------------------------------------------------------------------

Within the Design Manager, coded files have a “Show output” toggle which open up a second code editor panel, with a transpiled code of the file you are looking at. This is helpful to see how your HubL code will transpile into CSS, HTML or JavaScript, rather than reloading live pages the file is included on. It is also a helpful tool to use when exploring new features of HubL, or learning the basics of HubL as you can easily see what your HubL input will output to. 

![View HubL output](https://developers.hubspot.com/hs-fs/hubfs/View%20HubL%20output.png?width=580&height=109&name=View%20HubL%20output.png "View HubL output")

`|pprint` HubL filter[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#code-pprint-code-hubl-filter)
--------------------------------------------------------------------------------------------------------------------------------------

The `|pprint` HubL filter can be used on HubL variables to print valuable debugging information. It will print the type of HubL variable, which can be useful in understanding what expressions, filters, operators or functions it can be used with.

For example, `{{ local_dt }}` will print `2020-02-21 12:52:20`. If we pretty print this variable, we can see the value is a date `(PyishDate: 2020-02-21 12:52:20)`. This means we can use HubL filters that operate or format date objects, such as the `|datetimeformat` HubL filter.

{{ local\_dt }} {{ local\_dt|pprint }} {{ local\_dt|datetimeformat('%B %e, %Y') }}2020-02-21 12:55:13 (PyishDate: 2020-02-21 12:55:13) February 21, 2020

Developer info[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#developer-info)
-----------------------------------------------------------------------------------------------------------------

Much of the data found in developer info is used internally, and is subject to change if not otherwise documented.

The developer info for a page is the context of all data available when a page is being rendered. This rendering context is all accessible via HubL. To access the developer info for a page, select the **HubSpot sprocket icon in the top right hand corner of live pages > Developer Info.** 

![Developer info sprocket menu](https://developers.hubspot.com/hs-fs/hubfs/Developer%20info%20sprocket%20menu.png?width=580&height=239&name=Developer%20info%20sprocket%20menu.png "Developer info sprocket menu")

This will open up a new tab that returns the rendering context for a given page in the form of JSON. It is recommended to have a JSON formatter installed in your browser to make the developer info easier to read, such as this [JSON formatter Chrome extension](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en). While much of the information contained in the page's context is for internal purposes, this tool can be valuable to see what data is available via HubL when templating.

For example, the following image is of the developer info for [https://desigers.hubspot.com/docs/developer-reference/cdn](/docs/cms/developer-reference/cdn).

![Developer info example](https://developers.hubspot.com/hubfs/Developer%20info%20example.png "Developer info example")

The values of this data are being set through the Settings tab of the Content Editor:

![content editor - settings](https://developers.hubspot.com/hs-fs/hubfs/content%20editor%20-%20settings.png?width=580&height=380&name=content%20editor%20-%20settings.png "content editor - settings")

The values are then accessible to render on pages through HubL. To print the title and meta description in a [base template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/layouts/base.html), you would use the following HubL.

<title>{{ page\_meta.html\_title }}</title> <meta name="description" content="{{ page\_meta.meta\_description }}">

The data in the rendering context is available through HubL, and the JSON tree can be traversed using dot notation. Data in the developer info that developers frequently print out include module field values and tags that have been [exported to template context](/docs/cms/building-blocks/modules/export-to-template-context).

Review website performance and broken links[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#review-website-performance-and-broken-links)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It's important to verify that your site's visitors are not going to broken links. There are two tools you can use to help ensure your site visitors are getting to the correct place. You can use the [website performance API](/docs/api/cms/performance) to get HTTP Statuses like 404s and see your sites uptime.

If you're seeing 404 errors it's a good idea to redirect the visitor to a relevant URL.

You can also use the [SEO Recommendations tool](https://knowledge.hubspot.com/seo/view-seo-recommendations-in-hubspot) to identify broken links within your page content and quickly fix them.

Improving website speed[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#improving-website-speed)
-----------------------------------------------------------------------------------------------------------------------------------

There are a lot of factors that go into optimizing and testing website speed. For tools and tips to optimizing your site's speed see our guide.

[Optimize your CMS Hub site speed](https://developers.hubspot.com/cs/c/?cta_guid=0943ac91-eb91-4887-98cf-c3fa317b509e&signature=AAH58kFC2P-txIlKycNo_VgmAlJYWQXB6A&portal_id=53&pageId=29844694133&placement_guid=841bbe22-70a6-4222-a6f0-85dd019711ae&click=d61cbd17-b25f-498b-b886-0be3a3327769&redirect_url=APefjpEyz0QbNnUUwregT-v8eRTfYD952UKDn7Fcvz7SYT3zi5Bb0er1Ci07yqWR601ch6MQ5QBNppg5eP5jx1eDBgHEJvb6D52FdcAAtsdxCMck_SJSaE5Hla_rS2piQ6qwFjhVvUkHSQYdUimIVj87ipZtTO_Tfw&hsutk=ac257e7582a145e6027b0330a37eca62&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fdeveloper-reference%2Fdebugging-and-errors&__hstc=20629287.ac257e7582a145e6027b0330a37eca62.1715711134414.1715711134414.1715711134414.1&__hssc=20629287.1.1715711134414&__hsfp=1511885054&contentType=standard-page "Optimize your CMS Hub site speed") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, '841bbe22-70a6-4222-a6f0-85dd019711ae', {"useNewLoader":"true","region":"na1"});

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors#page-feedback)
---------------------------------------------------------------------------------------------------------------------

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