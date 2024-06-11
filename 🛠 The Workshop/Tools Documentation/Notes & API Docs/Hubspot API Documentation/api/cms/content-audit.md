---
title: "CMS Content Audit API"
description: "Allows filtering and sorting content object changes by type, time period, or HubSpot user ID. Available in accounts with a _CMS Hub Enterprise_ subscription. Example use case: find out which user most recently made changes to a list of pages."
type: "group"
tags:
- "Content Management System"
- "API"
- "HubSpot"
relationships:
- "#founded_by [[HubSpot]]"
- "#part_of [[CMS Hub Enterprise]]"
- "#related_to [[Content Audit API]]"
tags:
- "Event Type Listing"
- "Object Type Listing"
- "API Documentation"
founded: "N/A"
---

CMS Content Audit
=================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The CMS Content Audit API allows you to filter and sort content object changes by type, time period, or HubSpot user ID. This endpoint is only available in accounts with a _CMS Hub Enterprise_ subscription.  

**Example use case:** find out which user most recently made changes to a list of pages.

CMS Event Type Listing[](https://developers.hubspot.com/docs/api/cms/content-audit#cms-event-type-listing)
----------------------------------------------------------------------------------------------------------

Use this table to describe parameters / fields
| Event Type | Description |
| --- | --- |
| 
`CREATED`

 | 

An object has been created. 

 |
| 

`DELETED`

 | 

An object has been deleted or disconnected.

 |
| 

`PUBLISHED`

 | 

An object has been published.

 |
| 

`UNPUBLISHED`

 | 

An object has been unpublished.

 |
| 

`UPDATED`

 | 

An object has been updated.

 |

CMS Object Types Listing[](https://developers.hubspot.com/docs/api/cms/content-audit#cms-object-types-listing)
--------------------------------------------------------------------------------------------------------------

Use this table to describe parameters / fields
| Object Type | Description |
| --- | --- |
| 
`BLOG`

 | 

Changes made to your blog settings in your account settings.

 |
| 

`BLOG_POST`

 | 

Blog posts associated with your blog(s).

 |
| 

`CONTENT_SETTINGS`

 | 

Changes made to your website settings in your account settings. The values changed will appear in the `meta` JSON array.

 |
| 

`CTA`

 | 

Changes made to your [Calls-to-action (CTAs).](https://knowledge.hubspot.com/cta/get-started-with-calls-to-action-ctas)

 |
| 

`DOMAIN`

 | 

Changes made to the domains connected in your Domains & URLs settings in your account settings.

 |
| 

`EMAIL`

 | 

Changes made to emails in the email editor.

 |
| 

`FILE`

 | 

Changes made to files in the [files tool](https://knowledge.hubspot.com/cos-general/organize-edit-and-delete-files).

 |
| 

`GLOBAL_MODULE`

 | 

Changes made to [global modules.](https://knowledge.hubspot.com/cos-general/can-i-make-changes-to-a-global-module-in-only-one-template)

 |
| 

`HUBDB_TABLE`

 | 

Changes made to HubDB tables.

 |
| 

`KNOWLEDGE_BASE`

 | 

Changes made to your knowledge base settings in your account settings.

 |
| 

`KNOWLEDGE_BASE_ARTICLE`

 | 

Changes made to knowledge base articles in the content editor.

 |
| 

`LANDING_PAGE`

 | 

Changes made to landing pages in the content editor.

 |
| 

`MODULE`

 | 

Changes made to [modules](/docs/cms/building-blocks/modules).

 |
| 

`SERVERLESS_FUNCTION`

 | 

Changes made to [serverless functions](/docs/cms/features/serverless-functions).

 |
| 

`TEMPLATE`

 | 

Changes made to [templates](/docs/cms/building-blocks/templates).

 |
| 

`THEME`

 | 

Changes made to [Theme Settings](https://knowledge.hubspot.com/website-pages/edit-your-global-theme-settings) and when [Themes](https://knowledge.hubspot.com/website-pages/edit-your-global-theme-settings) are created.

 |
| 

`URL_MAPPING`

 | 

Changes made to your URL Redirects in URL Redirects settings in your account settings.

 |
| 

`WEBSITE_PAGE`

 | 

Changes made to website pages in the content editor.

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/cms/content-audit#page-feedback)
----------------------------------------------------------------------------------------------

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