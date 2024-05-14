Code alerts


===============

Last updated: November 17, 2022

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Code alerts provide a centralized location for developers and IT managers to see an overview listing of issues that are identified inside of your HubSpot CMS. By fixing the issues that are identified in Code Alerts it can help to optimize your website by helping to improve your customers experience and your sites performance as a whole.

To see other ways HubSpot helps to maximize your site's potential, check out [our reference page on CDN, Security, and Performance.](/docs/cms/developer-reference/cdn)

 ![Dashboard for code alerts](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/code-alerts/code-alerts-dashboard.jpg?width=1361&name=code-alerts-dashboard.jpg)

How to view code alerts[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#how-to-view-code-alerts)
-----------------------------------------------------------------------------------------------------------------------------------------------

View your code alerts for your entire portal by clicking on the Sprocket Menu from any published CMS page you are authenticated to and choosing **View Code Alerts** or go directly to [Code Alerts](https://app.hubspot.com/l/code-alerts).

![View Code Alerts from the Sprocket Menu](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/code-alerts/view-code-alerts-menu.png?width=155&name=view-code-alerts-menu.png)

Asset types and issues[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#asset-types-and-issues)
---------------------------------------------------------------------------------------------------------------------------------------------

### Asset types[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#asset-types)

There are multiple types of assets that code alerts can scan within your HubSpot CMS website. These are listed below.

Use this table to describe parameters / fields
| Asset type | Description |
| --- | --- |
| 
`Blog Post`

 | 

A blog post from one of your HubSpot blogs.

 |
| 

`Site Page`

 | 

A website page on the HubSpot CMS.

 |
| 

`Landing Page`

 | 

A website page with a specific purpose — the objective of a landing page is to convert visitors into leads.

 |
| 

`Blog`

 | 

Your HubSpot blog listing page.

 |
| 

`Module`

 | 

Reusable components that can be used in templates or added to pages.

 |
| 

`Template`

 | 

Templates are reusable page or email wrappers that generally place modules and partials into a layout.

 |
| 

`CSS`

 | 

A Cascading Style Sheet file.

 |
| 

`Knowledge Article`

 | 

An article from your HubSpot Knowledge Base.

 |
| 

`Unknown`

 | 

When an asset type is unknown.

 |

### Issues[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#issues)

There are multiple types of issues that your assets can have. If your asset has more than one issue it will be listed multiple times inside of your code alert dashboard.

Use this table to describe parameters / fields
| Issue | Example | Description |
| --- | --- | --- |
| 
`HubL limit`

 | The HubL function **blog\_recent\_tag\_posts** is used **11** times on this page. **blog\_recent\_tag\_posts** has a limit of **5** uses per page. | 

[Certain HubL functions have limits](https://designers.hubspot.com/docs/hubl/hubl-function-limits) to their usage. If your function exceeds its limits, you will be shown this issue.

 |
| 

`CSS combining`

 | There is a syntax error in a line of code that is preventing the CSS files from being combined. | 

Identifies CSS files that contain issues that would prevent the minification/combining of the file. There is also an option to **Show syntax errors** that are related to this asset.

 |
| 

`Output too big`

 | This page is **10446 Kilobytes**. The size limit is **9765 Kilobytes**. | 

The generated HTML for the page has reached more than the limit. This may result in seeing a blank or partial page.

 |
| 

`Template error`

 | There is an error in the code that is preventing this template from being rendered. | 

Identifies errors in your template code that prevent the template from being rendered.

 |
| 

`Unknown`

 | Unknown issue | 

When the system has a hard time identifying the error in the asset, an unknown issue will be assigned.

 |

How to view the issues identified for your assets[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#how-to-view-the-issues-identified-for-your-assets)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Code alerts include deep linking to assets where alerts are detected. When hovering over a row, you will be provided with the following options per asset type.

### Template, page, and module assets[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#template-page-and-module-assets)

The actions button will provide you with a link to open the corresponding template or module in the design manager. 

![Template and Module Issues](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/code-alerts/my-template-open-in-dm.jpg?width=802&name=my-template-open-in-dm.jpg) 

### CSS assets[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#css-assets)

The actions button will provide you with a link to open the corresponding stylesheet in the design manager, view your file with debugging info, or show you the syntax errors. 

![CSS Issues](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/code-alerts/code-alerts-css-options.jpg?width=802&name=code-alerts-css-options.jpg)

When choosing “Show syntax error” you will be shown a modal window with additional details about the syntax error along with the line number where the error exists.

![Syntax errors details modal](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/code-alerts/code-alert-syntax-error-details.png?width=1600&name=code-alert-syntax-error-details.png)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/developer-reference/debugging-and-errors/code-alerts#page-feedback)
---------------------------------------------------------------------------------------------------------------------------------

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