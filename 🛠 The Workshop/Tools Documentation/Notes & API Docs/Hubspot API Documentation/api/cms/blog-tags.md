---
title: "Blog Tags API Documentation"
description: "Manage tags for your blog posts using the blog tags API."
type: "concept"
tags:
- "Blog"
- "Tags"
- "API"
relationships:
- "#related_to [[HubSpot Knowledge Base]]"
- "#similar_to [[Endpoints]], [[Filtering]], [[Sorting and Paginating]], [[Create blog tags]], [[Edit blog tags]], [[Multi-language management]], [[Create a new language variant]], [[Attach a blog tag to an existing multi-language group]], [[Detach a blog tag from a multi-language group]]"
createdAt: "2023-01-01"
updatedAt: "2023-04-01"
---

.interest-form { padding: 1em; display: none; height: 100%; } .interest-text { padding: 1em; } .hs-form>fieldset { max-width: 100% !important; }

**Access and test APIs in beta.** 
----------------------------------

**Please note**: This API is currently under development and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to our [Developer Terms](https://legal.hubspot.com/hubspot-developer-terms)& [Developer Beta](https://legal.hubspot.com/developerbetaterms?)Terms. You also acknowledge and understand the risk associated with testing an unstable API. 

  
Provide Feedback

hbspt.forms.create({ portalId: "428357", formId: "037350c3-535d-4755-82ca-53b73367754f", cssClass: "hs-form" });

First name

Last name

Email

How satisfied are you with this API beta\*

Please SelectVery satisfiedSatisfiedNeutralUnsatisfiedVery unsatisfied

Can we contact you with follow-up questions about this feedback?

*   Yes, HubSpot can contact me about this feedback 

By selecting “Yes,” you are allowing HubSpot to store any personal information submitted through this form. We respect your privacy and will only use it to contact you if we have follow-up questions about today’s feedback. You can unsubscribe from these communications at any time. For more information, check out our [Privacy Policy.](https://legal.hubspot.com/privacy-policy)

$(document).ready(() => { $("#interest-btn").click(() => { $(".interest-form").toggle(); }); });

Blog Tags
=========

*   [
    
    Overview
    
    ](#tab-1)
*   [
    
    Endpoints
    
    ](#tab-2)

Use the blog tags API to manage tags for your blog posts. Learn more about how to create and maintain your blog on the [HubSpot Knowledge Base.](https://knowledge.hubspot.com/website/topics#blog)

Changes in V3[](https://developers.hubspot.com/docs/api/cms/blog-tags#changes-in-v3)
------------------------------------------------------------------------------------

The `description` property has been deprecated and will not be included in the response of any of the V3 endpoints.

Search blog tags[](https://developers.hubspot.com/docs/api/cms/blog-tags#search-blog-tags)
------------------------------------------------------------------------------------------

To retrieve blog tags, make a `GET` request to `/cms/v3/blogs/tags`. You can filter and sort the tags returned in the response using the operators and properties below. You can also use the standard filters using the `createdAt` and `updatedAt` dates.

### Filtering[](https://developers.hubspot.com/docs/api/cms/blog-tags#filtering)

Provide any filters as query parameters in your request by adding the property name, followed by two underscore characters, then include the associated operator as a suffix. For example, you can filter the results to only include blog tags where the `name` property contains the word _marketing_ using the parameter: `&name__icontains=marketing`.

You can include any number of filters as query parameters in the request URL. All filters are ANDed together. ORing filters is not currently supported.

The available filter types are listed below:

Use this table to describe parameters / fields
| Operator | Description |
| --- | --- |
| 
`eq`

 | 

Equal to

 |
| 

`ne`

 | 

Not equal to

 |
| 

`contains`

 | 

Contains

 |
| 

`icontains`

 | 

Contains (case sensitive)

 |
| 

`lt`

 | 

Less than

 |
| 

`lte`

 | 

Less than or equal to

 |
| 

`gt`

 | 

Greater than

 |
| 

`gte`

 | 

Greater than or equal to

 |
| 

`is_null`

 | 

Null

 |
| 

`not_null`

 | 

Not null

 |
| 

`like`

 | 

Like

 |
| 

`not_like`

 | 

Not like

 |
| 

`startswith`

 | 

Value starts with

 |
| 

`in`

 | 

In

 |

The table below lists the properties that can be filtered on, along with their supported filter types.

Use this table to describe parameters / fields
| Property | Supported filters |
| --- | --- |
| 
`id`

 | 

eq, in

 |
| 

`name`

 | 

eq, contains

 |
| 

`slug`

 | 

eq

 |
| 

`createdAt`

 | 

eq, gt, gte, lt, lte

 |
| 

`deletedAt`

 | 

eq, gt, gte, lt, lte

 |
| 

`createdById`

 | 

eq

 |
| 

`updatedById`

 | 

eq

 |
| 

`language`

 | 

in, not\_null

 |
| 

`translatedFromId`

 | 

null, not\_null

 |

To filter blog tags based on a multi-language group, you can include one of the query parameters from the table below. For example, to get blog tags from the German variation of your blog, you'd include `language__in=de` as a query parameter.

**Please note:** languages with locales (e.g., `en-us`) are not supported with the `language` filter.

### Sorting and paginating[](https://developers.hubspot.com/docs/api/cms/blog-tags#sorting-and-paginating)

You can provide sorting and pagination options as query parameters. Specify the property name as the value to the sort query parameter to return the blog tags in the natural order of that property. You can reverse the sorting order by including a dash character before the property name (e.g., `sort=-createdAt`).

By combining query parameters for filtering, sorting, and paging, you can retrieve blog tags that match more advanced search criteria. For example, the request below fetches blog tags that have a language assigned, ordered by the most recently updated. Including the `limit` and `offset` parameters below returns the second page of results.

curl https://api.hubapi.com/cms/v3/blogs/tags?sort=-updatedAt&&language\_\_not\_null&limit=10&offset=10 \\ --request POST \\ --header "Content-Type: application/json"

Create blog tags[](https://developers.hubspot.com/docs/api/cms/blog-tags#create-blog-tags)
------------------------------------------------------------------------------------------

To create a blog tag, make a `POST` request to `/cms/v3/blog/posts` and include a JSON payload that represents the blog tag model, as shown in the Endpoints tab at the top of this article. The `name` field is required when creating a blog tag. To set the URL of a blog tag listing page, you must include the `slug` field in your request.

Edit blog tags[](https://developers.hubspot.com/docs/api/cms/blog-tags#edit-blog-tags)
--------------------------------------------------------------------------------------

To update a blog tag, make a `PATCH` request to `/cms/v3/blog/posts/{objectId}` where `objectId` is the ID of the tag you want to update. In your request, include a JSON payload should include the blog tag model, as shown in the Endpoints tab at the top of this article.

Multi-language management[](https://developers.hubspot.com/docs/api/cms/blog-tags#multi-language-management)
------------------------------------------------------------------------------------------------------------

To help you maintain blog tags across multiple languages, HubSpot's CMS allows you to group together blog tags of language variants of the same content. A tag with a language set may only be used on blog posts of the same language. Tags that do not have a language set are considered global and may be used on all blog posts.

To learn more about working with multi-language blog tags, check out [this Knowledge Base article](https://knowledge.hubspot.com/blog/create-a-multi-language-blog#create-blog-authors-in-multiple-languages).

### Create a new language variant[](https://developers.hubspot.com/docs/api/cms/blog-tags#create-a-new-language-variant)

To create a new language variant for an existing blog tag, make a `POST` request to `/multi-language/create-language-variant` and include a JSON payload containing the ID of the blog tag to clone and the language identifier of the new variant.

### Attach a blog tag to an existing mutli-language group[](https://developers.hubspot.com/docs/api/cms/blog-tags#attach-a-blog-tag-to-an-existing-mutli-language-group)

To add a blog tag to an existing multi-language group, make a `POST` request to the `/multi-language/attach-to-lang-group` and include a JSON payload containing the ID of the target blog tag, the language identifier of the blog tag being added, and the `primaryId` of the blog tag designated as the primary blog tag in the target multi-language group.

### Detach a blog tag from a multi-language group[](https://developers.hubspot.com/docs/api/cms/blog-tags#detach-a-blog-tag-from-a-multi-language-group)

To remove a blog tag from a multi-language group, make a `POST` request to `/multi-language/detach-from-lang-group` and include a JSON payload containing the ID of the target blog tag.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/cms/blog-tags#page-feedback)
------------------------------------------------------------------------------------------

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