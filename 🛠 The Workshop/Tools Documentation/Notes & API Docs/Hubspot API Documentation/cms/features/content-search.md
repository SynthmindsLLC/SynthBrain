Content Search


==================

Last updated: August 30, 2023

HubSpot CMS has built-in site search functionality to allow your visitors to easily find the content they are looking for. All of your HubSpot content is automatically indexed in HubSpot’s native search engine, taking the hassle out of setting up a third-party search tool for your website.

Searching Content[](https://developers.hubspot.com/docs/cms/features/content-search#searching-content)
------------------------------------------------------------------------------------------------------

The search engine is accessible through the [site search API](/docs/api/cms/site-search). This API supports numerous filtering options to allow you to create a highly customized and powerful search experience on your website. For example, if you wanted to build a search into your blog, you can query for `type=BLOG_POST` to only return blog posts. Or, if you wanted to build search into the Spanish version of your website, you could query `_language=es_` to only return Spanish pages.

The API returns JSON that can be parsed with JavaScript to display the results on your website. All content types will return the page domain, title, url and language. The description returned is a sample of text from the content which best matches the search term. A `<span class="hs-search-highlight hs-highlight-html">` element will wrap perfectly matching text, allowing you to highlight matching text with CSS. 

Depending on the type of content searched, the results return slightly different information, so you can display results for unique content types differently. For example, blog posts will return information on which tags the post has, who the author is, and when it was published.

// json { "total": 850, "offset": 0, "limit": 10, "results": \[ { "id": 3761238962, "score": 0.30858153, "type": "SITE\_PAGE", "domain": "designers.hubspot.com", "url": "https://developers.hubspot.com/docs/cms/search", "language": "en", "title": "Content Search", "description": "Using HubSpot’s native search engine, content search, to implement <span class="hs-search-highlight hs-highlight-html">search on your website</span>" }, { "id": 3254581958, "score": 0.30858153, "type": "BLOG\_POST", "domain": "designers.hubspot.com", "url": "https://designers.hubspot.com/blog/getting-started-with-local-development", "featuredImageUrl":"https://designers.hubspot.com/hubfs/local-development.jpg" "title": "Getting Started with Local Development", "description":"The beta Local Development Tooling connects your local workflow to HubSpot, allowing you to utilize <span class="hs-search-highlight hs-highlight-html">version control</span>, your favorite text editor and various web development technologies when developing on the HubSpot CMS." "authorFullName": "William Spiro", "tags": \[ "Website Development", "Local Development" \], "publishedDate": 1447938000000 } }

Implementing search on your website[](https://developers.hubspot.com/docs/cms/features/content-search#implementing-search-on-your-website)
------------------------------------------------------------------------------------------------------------------------------------------

There are two default modules you can use to easily implement search on your website, which use the [site search API](/docs/api/cms/site-search): `search_input` and `search_results`.

### Site Search Input[](https://developers.hubspot.com/docs/cms/features/content-search#site-search-input)

An input field for visitors to enter search terms into. This module can exist anywhere on your website. This module can be included in a template with `{% module "search_input" path="@hubspot/search_input" %}`.

{% module "search\_input" path="@hubspot/search\_input" %}

### Site Search Results[](https://developers.hubspot.com/docs/cms/features/content-search#site-search-results)

Returns a listing of content based on the search term. This module can exist anywhere on your website. This module can be included in a template with

{% module "search\_results" path="@hubspot/search\_results" %}

If the functionality of these modules is not how you want search to work on your website, you can build your own search modules or functionality. The default search modules are designed to be extended based on your search needs. You can view and clone these modules in the Design Manager by searching for their names in the Finder, or, you can fetch them to your local environment using the [CMS CLI](/docs/cms/developer-reference/local-development-cms-cli) by running `hs fetch @hubspot/search_input.module` or `hs fetch @hubspot/search_results.module`.

![default search module](https://developers.hubspot.com/hs-fs/hubfs/default%20search%20module.png?width=1999&name=default%20search%20module.png)

Search Results Template[](https://developers.hubspot.com/docs/cms/features/content-search#search-results-template)
------------------------------------------------------------------------------------------------------------------

Every domain has its own search results page by default. The template and path for this page are set at **Settings > Website > Pages** under the [System Pages tab](https://app.hubspot.com/l/settings/website/pages/all-domains/system-pages) for specific domains. See the [CMS theme boilerplate search results template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/search-results.html) as an example. The domain set for the search results page is automatically connected to the default search modules. However, you can use the [site search API](/docs/api/cms/site-search) to build our your search results as you'd like on any pages of your website.

How is the search precedence determined?[](https://developers.hubspot.com/docs/cms/features/content-search#how-is-the-search-precedence-determined-)
----------------------------------------------------------------------------------------------------------------------------------------------------

The order of search results is determined by a series of weighted comparisons of page content to the visitor's search term. Page content is separated into comparison fields with varying weight based on where the content lives within the HTML of your pages. Comparison fields are grouped in order of weight:

1.  HTML title
2.  Meta description
3.  H1 HTML elements
4.  H2 HTML elements
5.  H3 HTML elements
6.  Other HTML elements

Please note that this list is subject to change. 

If you wish to tell our indexer to specifically boost certain elements on a page, you can wrap the content in a `hs-search-keyword` class.

Control indexing during development[](https://developers.hubspot.com/docs/cms/features/content-search#control-indexing-during-development)
------------------------------------------------------------------------------------------------------------------------------------------

While developing a new site, it's useful to be able to test site search without worrying about the site being indexed by search engines such as Google.

In your `[robots.txt](https://knowledge.hubspot.com/cos-general/customize-your-robots-txt-file)` you can tell HubSpot to crawl everything, while blocking other bots.

\# Block all bots User-agent: \* Disallow: / # Allow HubSpot Site Search Indexing User-agent: HubSpotContentSearchBot Allow: /

If any of your pages have a meta tag specifying no index, the page will still not be indexed, even if allowed in the `robots.txt`.

Also remember to review your `robots.txt` prior to launch to ensure everything indexes how you want it to.

Default indexing behavior[](https://developers.hubspot.com/docs/cms/features/content-search#default-indexing-behavior)
----------------------------------------------------------------------------------------------------------------------

Because the CMS knows the intent of certain types of pages, content search is able to safely limit indexing to allow indexing of content type pages. Examples of content type pages:

*   Site Pages
*   Landing Pages
*   Knowledge articles
*   blog posts

**System pages and password protected pages are not indexed.** CMS Membership restricted pages will only display in hubspot content search for users that are signed in and have access to the pages.

How can I exclude pages from being returned in search results?[](https://developers.hubspot.com/docs/cms/features/content-search#how-can-i-exclude-pages-from-being-returned-in-search-results-)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you block a page from being indexed to search engines via your websites [`robots.txt`](https://knowledge.hubspot.com/cos-general/customize-your-robots-txt-file) file or via `meta` tags, they will not be indexed for site search. 

In your `robots.txt` add a `disallow`.

\# Block all bots User-agent: \* Disallow: /path-to-page # Block just HubSpot Site Search Indexing User-agent: HubSpotContentSearchBot Disallow: /path-to-page

You can also add a `NOINDEX, NOFOLLOW` meta tag in the `<head>` at the page or template level.

<meta name="ROBOTS" content="NOINDEX, NOFOLLOW">

You don't need to block robots using both `robots.txt` and the meta tag. Doing so can make it confusing later if you decide to allow indexing of a page.

How to exclude sections of a page from being indexed in search[](https://developers.hubspot.com/docs/cms/features/content-search#how-to-exclude-sections-of-a-page-from-being-indexed-in-search)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes there are regions of a page that are not useful to return in search results. This might be content from a header, a footer, sidebar, etc. When this is the case, you can add the class `hs-search-hidden` to your HTML for those regions to have search ignore the content inside.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/features/content-search#page-feedback)
----------------------------------------------------------------------------------------------------

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