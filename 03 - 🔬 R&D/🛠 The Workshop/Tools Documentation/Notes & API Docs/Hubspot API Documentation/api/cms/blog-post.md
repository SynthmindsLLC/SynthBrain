Blog Posts 
=========== 

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

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

*   [
    
    Overview
    
    ](#tab-1)
*   [
    
    Endpoints
    
    ](#tab-2)

You can use the blog post API to publish and manage blog posts. Learn more about how to create and maintain your blog on the [HubSpot Knowledge Base.](https://knowledge.hubspot.com/website/topics#blog)

Changes in V3[](https://developers.hubspot.com/docs/api/cms/blog-post#changes-in-v3)
------------------------------------------------------------------------------------

*   The following properties are deprecated and will not be included in the response of any of the V3 endpoints:
    *   _campaign\_name_
    *   _is\_draft_
    *   _keywords_
*   The _topicIds_ property has been renamed to _tagIds_.

Limits[](https://developers.hubspot.com/docs/api/cms/blog-post#limits)
----------------------------------------------------------------------

The blog post API endpoints are subject to the limits defined in [HubSpot's API usage guidelines](/docs/api/usage-details). Any limits specific to a certain endpoint will be listed with the associated endpoint in the Endpoints tab above.

Search blog posts[](https://developers.hubspot.com/docs/api/cms/blog-post#search-blog-posts)
--------------------------------------------------------------------------------------------

When you make a `GET` request to `/cms/v3/blogs/posts`, you can filter and sort the posts returned in the response using the operators and properties below. You can also use the standard filters using the `createdAt` and `updatedAt` dates.

### Filtering[](https://developers.hubspot.com/docs/api/cms/blog-post#filtering)

Provide any filters as query parameters in your request, by adding the property name, followed by two underscore characters, then include the associated operator as a suffix. For example, you can filter the results to only include blog posts where the _name_ property contains the word _marketing_ using the parameter: `&name__contains=marketing`.

You can include any number of filters as query parameters in the request URL. All specified filters will be applied to narrow down results.  

The available filter types are listed below:

| Filter | Operator |
| --- | --- |
| Equals | `eq (or none)` |
| Not equal | `ne` |
| Contains | `contains` |
| Less than | `lt` |
| Less than or equal | `lte` |
| Greater than | `gt` |
| Greater than or equal | `gte` |
| Null | `is_null` |
| Not null | `not_null` |
| Like | `like` |
| Not like | `not_like` |
| Contains (case insensitive) | `icontains` |
| Starts with | `startswith` |
| In | `in` |

The table below lists the properties that can be filtered on, along with their supported filter types.

| Property | Supported filters |
| --- | --- |
| id | `Equal`, `In` |
| slug | `Equal`, `In`, `Not in`, `Contains (case insensitive)` |
| campaign | `Equal`, `In` |
| state | `Equal`, `Not equal`, `In`, `Not in`, `Contains` |
| publishDate | `Equal`, `Greater than`, `Greater than or equal` , `Less than` ,`Less than or equal` |
| createdAt | `Equal`, `Greater than`, `Greater than or equal` , `Less than` ,`Less than or equal` |
| updatedAt | `Equal`, `Greater than`, `Greater than or equal` , `Less than` ,`Less than or equal` |
| name | `Equal`, `In`, `Contains (case insensitive)` |
| archivedAt | `Equal`, `Greater than`, `Greater than or equal`, `Less than` ,`Less than or equal` |
| createdById | `Equal` |
| updatedById | `Equal` |
| blogAuthorId | `Equal`, `In` |
| translatedFromId | `Null`, `Not null` |
| contentGroupId | `Equal`, `In` |
| tagId | `Equal`, `In` |

The table below lists the query parameters you can use to filter by publish state.

| Publish State | Query parameters |
| --- | --- |
| Draft | `state=DRAFT` |
| Scheduled | `state=SCHEDULED` |
| Published | `state=PUBLISHED` |

**Please note:** the _currentState_ field on the blog post object is a generated field which also reflects the blog's publish state, but you cannot use it as a property to filter against in your requests.

To filter blog posts based on a multi-language group, you can include one of the query parameters in the table below. For example, to get blog posts associated with a German variation of your blog, you'd include `contentGroupId__eq={germanBlogId}` as a query parameter.

| Description | Query parameters |
| --- | --- |
| Primary blog post in a multi-language group | `translatedFromId__is_null` |
| Variation blog post in a multi-language group | `translatedFromId__not_null` |
| Blog post with specific language | `contentGroupId__eq` |

### Sorting and paginating[](https://developers.hubspot.com/docs/api/cms/blog-post#sorting-and-paginating)

You can provide sorting and pagination options as query parameters. Specify the property name as the value to the sort query parameter to return the blog posts in the natural order of that property. You can reverse the sorting order by including a dash character before the property name (e.g., `sort=-createdAt`).

By combining query parameters for filtering, sorting, and paging, you can retrieve blog posts that match more advanced search criteria. For example, the request below fetches blog posts that don't have a language assigned, ordered by the most recently updated. Including the _limit_ and _offset_ parameters below returns the second page of results.

curl https://api.hubapi.com/cms/v3/blogs/posts?sort=-updatedAt&&language\_\_not\_null&limit=10&offset=10 \\ --request POST \\ --header "Content-Type: application/json"

Create blog posts[](https://developers.hubspot.com/docs/api/cms/blog-post#create-blog-posts)
--------------------------------------------------------------------------------------------

You can create a blog post by making a `POST` request to the `/cms/v3/blogs/posts` endpoint, and including a JSON payload that represents the blog post model. The _name_ and _contentGroupId_ fields are required when creating a blog post. To set the URL of a blog post, you must provide the _slug_ field in your request. The _url_ field is auto-generated by HubSpot and cannot be updated. Review the required parameters and the structure of the blog post model in the Endpoints tab at the top of this article.

Learn more about [creating blog posts in the HubSpot content editor](https://knowledge.hubspot.com/blog/create-and-publish-blog-posts?_ga=2.178469028.1635574580.1657805127-616104167.1657805127#create-a-new-blog-post).

Edit and publish blog posts[](https://developers.hubspot.com/docs/api/cms/blog-post#edit-and-publish-blog-posts)
----------------------------------------------------------------------------------------------------------------

Blog posts in HubSpot have both draft and live versions. The draft version can be updated without affecting the live blog post content. Drafts can be reviewed and published by a user in your HubSpot account. You can also schedule your post to be published at a future time via the _/schedule_ endpoint. Draft changes can also be discarded using the _/reset_ endpoint, which allows a user in your account to revert back to the current live version of the blog post without disruption.

### Edit a draft[](https://developers.hubspot.com/docs/api/cms/blog-post#edit-a-draft)

You can update the draft version of a blog post by making a `PATCH` request to the `/cms/v3/blogs/posts/{objectId}` endpoint and providing the associated ID of the post as the _objectId_. You must include a JSON payload that represents the blog post model.  
  
You can modify the _widgets_, _widgetContainers_, and _layoutSections_ properties of the blog post model. Each property stores module data for the post.

*   **widgets:** contains data from the blog post's template.
*   **widgetContainers:** contains data from the module's flex columns.
*   **layoutSections:** contains data from the module's drag and drop areas.

Properties you provide in the payload of your request will override existing draft properties without any complex merging logic. As a result, if you're updating any nested properties within the three properties listed above, you should provide the full definition of the object. Partial updates are not supported.

**Please note:** editing your blog post drafts directly in your HubSpot account is the simplest way to modify content managed by the HubSpot CMS. While you can use the edit endpoint described above, it's not recommended over using the editor.

### Publish draft blog post[](https://developers.hubspot.com/docs/api/cms/blog-post#publish-draft-blog-post)

You can publish an unpublished blog post by making a `PATCH` request to the `api.hubspot.com/cms/v3/blogs/posts/{objectId}` endpoint and supplying the _objectID_ of the blog post. In your request, include a JSON payload that sets the _state_ to _Published_. 

### Publish changes to live blog post[](https://developers.hubspot.com/docs/api/cms/blog-post#publish-changes-to-live-blog-post)

You can push live unpublished changes to a published blog post by making a `POST` request to the `/cms/v3/blogs/posts/{objectId}/draft/push-live` endpoint and supplying the _objectID_ of the blog post. This endpoint does not require a payload and will only update an already published blog post, not publish a drafted blog post.

### Schedule draft to be published a future time[](https://developers.hubspot.com/docs/api/cms/blog-post#schedule-draft-to-be-published-a-future-time)

You can schedule the draft version of your blog post to be published later by making a `POST` request to the `/cms/v3/blogs/posts/schedule` endpoint. In your request, include a JSON payload that contains the _id_ of the target blog post and a _publishDate_.

### Reset draft[](https://developers.hubspot.com/docs/api/cms/blog-post#reset-draft)

You can reset the draft version of a blog post back to its current live version by making a `POST` request to the `/cms/v3/blogs/posts/{objectId}/draft/reset` endpoint, and supplying the _objectId_ of the associated post you want to reset. This endpoint does not require you to supply a payload.

Review the required parameters and available endpoints for editing and publishing a blog post in the Endpoints tab at the top of this article.

Multi-language management[](https://developers.hubspot.com/docs/api/cms/blog-post#multi-language-management)
------------------------------------------------------------------------------------------------------------

To help you maintain blog posts across multiple languages, HubSpot's CMS allows you to group together language variants of the same content. You can learn more about working with multi-language blog posts in [this Knowledge Base article](https://knowledge.hubspot.com/blog/create-a-multi-language-blog#create-a-blog-post-in-multiple-languages).

### Create a new language variant[](https://developers.hubspot.com/docs/api/cms/blog-post#create-a-new-language-variant)

You can create a new language variant for an existing blog post by making a `POST` request to the `/multi-language/create-language-variant` endpoint. The endpoint accepts a JSON payload containing the _id_ of the blog post to clone and the _language_ identifier of the new variant.

### Attach a blog post to an existing multi-language group[](https://developers.hubspot.com/docs/api/cms/blog-post#attach-a-blog-post-to-an-existing-multi-language-group)

You can add a blog post to an existing multi-language group by making a `POST` request to the `/multi-language/attach-to-lang-group` endpoint. The endpoint accepts a JSON payload containing the _id_ of the target blog post, the _language_ identifier of the blog post being added, and the _primaryId_ of the blog post designated as the primary blog post in the target multi-language group.

### Detach a blog post from a multi-language group[](https://developers.hubspot.com/docs/api/cms/blog-post#detach-a-blog-post-from-a-multi-language-group)

To detach a blog post from a multi-language group, make a `POST` request to the `/multi-language/detach-from-lang-group` endpoint. The endpoint accepts a JSON payload containing the _id_ of the target blog post.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/cms/blog-post#page-feedback)
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