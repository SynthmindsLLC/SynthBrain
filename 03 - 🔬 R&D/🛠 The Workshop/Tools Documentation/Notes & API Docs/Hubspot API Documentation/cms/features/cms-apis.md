CMS APIs


============

Last updated: April 18, 2024

The HubSpot CMS is powerful and can be extended through APIs. This page is an aggregation of our APIs that are most relevant to developers building with the CMS. **This is not our** [**full list of APIs**](/docs/api/overview)**.** Our APIs are subject to [rate limits](/docs/api/usage-details#rate-limits) and support [OAuth](/docs/api/working-with-oauth). We encourage reviewing our [API Usage Guidelines](/docs/api/usage-details) for best practices. To test your integrations you will need to [create a developer account](https://app.hubspot.com/signup/developers), which will enable you to [create test accounts](/docs/api/creating-test-accounts) or an [application](/docs/api/creating-an-app) to get started with OAuth. This is different from your CMS developer sandbox portal.

Analytics API[](https://developers.hubspot.com/docs/cms/features/cms-apis#analytics-api)
----------------------------------------------------------------------------------------

The [Analytics API](/docs/api/analytics/reporting) allows you to export analytics and reporting data from HubSpot. It’s primarily used to connect metrics tracked in HubSpot to those stored in other business intelligence tools. You could use this API to display traffic and leads tracked in another CRM or analytics tool.

Conversations API[](https://developers.hubspot.com/docs/cms/features/cms-apis#conversations-api)
------------------------------------------------------------------------------------------------

The Conversations Live Chat widget allows you to directly engage in conversations on your website. The [Conversations API](/docs/api/conversation/chat-widget-sdk) helps you provide a more tailored visitor experience by giving you more control over this widget.

You can use this to customize how and when the conversations widget appears on your website.

CMS Blog API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-blog-api)
--------------------------------------------------------------------------------------

The [CMS Blog APIs](/docs/api/cms/blogs) enable you to sync your blog data with external applications and tools as well as modify blog content.

### CMS Blog Authors API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-blog-authors-api)

The [CMS Blog Authors API](/docs/api/cms/blog-authors) enables you to list, search, create, delete, and get information for blog authors.

### CMS Blog Comments API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-blog-comments-api)

The [CMS Blog Comments API](https://developers.hubspot.com/docs/methods/comments/get_comments) can be used to list, get, create, and delete comments as well as restore deleted comments.

### CMS Blog Post API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-blog-post-api)

The [CMS Blog Post API](/docs/api/cms/blog-post) can be used to list, get, create, update, delete, clone, and control publishing of blog posts. The API can also be used to manage revisions of a post.

### CMS Blog Topics API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-blog-topics-api)

The [CMS Blog Topics API](/docs/api/cms/blog-tags) can be used to list, search, get, create, update, delete and merge blog topics.

CMS Domains API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-domains-api)
--------------------------------------------------------------------------------------------

The [CMS Domains API](https://developers.hubspot.com/docs/methods/domains/get_domains) can be used to get a list of all the domains and their associated properties for a HubSpot account.

CMS Files API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-files-api)
----------------------------------------------------------------------------------------

You can use the [CMS Files API](https://developers.hubspot.com/docs/methods/files/post_files) to upload, delete, organize and manage files in the [File Manager](/docs/cms/features/file-manager).

Forms API[](https://developers.hubspot.com/docs/cms/features/cms-apis#forms-api)
--------------------------------------------------------------------------------

You can use the [Forms API](https://developers.hubspot.com/docs/methods/forms/forms_overview) to deliver heavily customized forms to users by directly submitting form data to our forms API. This API can also be used to get form information, create, update and delete forms, and their associated fields. Note: when using the Forms API to submit forms data, the [accessibility](/docs/cms/developer-reference/accessibility) and validation of your forms is your responsibility.

CMS HubDB API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-hubdb-api)
----------------------------------------------------------------------------------------

You can use the [HubDB API](/docs/api/cms/hubdb) to create, modify and delete HubDB tables, and their rows of data. The HubDB API also supports [importing a CSV file](https://developers.hubspot.com/docs/methods/hubdb/v2/import_csv) into an existing HubDB table. This API is useful for those storing and displaying complex information.

CMS Page Publishing API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-page-publishing-api)
------------------------------------------------------------------------------------------------------------

You can use the [CMS Page Publishing API](https://developers.hubspot.com/docs/methods/pages/get_pages) to create, clone, list, update, and delete pages on the CMS. This API can also be used to manage the publishing state and view and revert to revisions of a page.

CMS Site Search API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-site-search-api)
----------------------------------------------------------------------------------------------------

You can use the [Site Search API](https://developers.hubspot.com/docs/methods/content/search-for-content) to search the content (site pages, blog posts, landing pages, blog listing pages, and knowledge articles) of a HubSpot hosted site. This can be used to build a custom [site search](/docs/cms/features/content-search). You can also use the API to access all of the indexed data for a document.

CMS Templates API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-templates-api)
------------------------------------------------------------------------------------------------

You can use the [CMS Templates API](https://developers.hubspot.com/docs/methods/templates/get_templates) to list, create, update, delete, and publish coded HTML+HubL templates. This API can also be used to get and restore previous revisions of a template as well as restore deleted templates.

CMS URL Mappings API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-url-mappings-api)
------------------------------------------------------------------------------------------------------

You can use the [CMS URL Mappings API](/docs/api/cms/url-redirects) to list, create, update, delete, and get URL mappings from a HubSpot account. URL Mappings are used for redirects and proxy pages.

CMS Content Audit API[](https://developers.hubspot.com/docs/cms/features/cms-apis#cms-content-audit-api)
--------------------------------------------------------------------------------------------------------

The [CMS Content Audit API](https://developers.hubspot.com/docs/api/cms/content-audit) allows you to filter and sort on content object changes by type, time period, or HubSpot user ID, so you’re never left wondering what happened. This API is currently in public beta.

Get Privacy Consent Status[](https://developers.hubspot.com/docs/cms/features/cms-apis#get-privacy-consent-status)
------------------------------------------------------------------------------------------------------------------

The [GDPR privacy consent banner](https://knowledge.hubspot.com/reports/customize-your-cookie-tracking-settings-and-privacy-policy-alert) which can control whether different analytics scripts are run. To control script loading you'll need to [get the consent status](/docs/api/events/cookie-banner). 

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/features/cms-apis#page-feedback)
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