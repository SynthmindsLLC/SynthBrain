Creating a related blog post listing with the blog related posts HubL tag


=============================================================================

Last updated: April 1, 2021

The [related\_blog\_posts](/docs/cms/hubl/tags#blog-related-posts) HubL tag can be used to create dynamic and related blog post listing based on a variety of parameters. It allows for generating listings of posts across blogs, with the ability to filter by tags, authors, post paths and publish dates. Developers can also specify the HTML output of the module using a macro. This HubL tag can be used on both blog posts and pages. This tutorial will walk through the parameters and usage options for the blog related posts HubL tag.

Please note that the `related_blog_posts` HubL tag does not generate an editable module on the post/page level, it is configured in its entirety with HubL.

Parameters[](https://developers.hubspot.com/docs/cms/guides/creating-a-related-post-listing#parameters)
-------------------------------------------------------------------------------------------------------

The list of posts is generated from a relevancy score based on a comparison of the set parameter values against posts matching these parameters, or relating to the post the HubL tag appears on. None of the parameters are required, however, specifying parameters will allow you to further control which posts are returned. For comma-separated parameters, the more values you set, the more diverse the returned listing will be. The `post_formatter` parameter allows you to specify a [macro](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#macros) to generate the HTML output of the module. For a full list of parameters and example default HTML output, please see the [related\_blog\_posts](/docs/cms/hubl/tags#blog-related-posts) spec.

Parameters for the related blog posts function
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`limit`

 | number | 

 The max number of blog posts to list.

 | `3` |
| 

`blog_ids`

 | 'default' or blog id | 

The ID(s) of a blogs to include posts from.

 | `none` |
| 

`tags`

 | String | 

The tag(s) that should be used to determine if a post is relevant (comma separated). If a blog post has one of these tags or a similar tag, the post’s relevancy is increased, improving its ranking in the listing.

 | `none` |
| 

`blog_authors`

 | String | 

The names of authors to include posts from (comma separated)

 | `none` |
| 

`blog_post_ids`

 | String | 

The ID(s) of a blog posts to use when finding relevant blog posts to list (comma separated). This parameter should only be used when the widget is appearing on pages, as on blog posts, it will default to the post the widget is appearing on.

 | `none` |
| 

`post_formatter`

 | String | 

The name of a custom macro to render returned blog posts. The macro is passed three parameters which are the blog post object to format, the count in the iteration of blog posts, and the total count of blog posts in the results. If not specified or set to “default”, the built-in formatter will be used to format each post.  
  
**Note: It is recommended to use the callback parameter below in place of the ‘post\_formatter’ parameter as the HTML of the tag will render more quickly, decreasing page load times.**

 | `none` |
| 

`callback`

 | String | 

The name of a javascript function to render returned blog posts. The function is passed an array of blog post objects to format. If neither the callback, or post\_formatter parameters are specified, the tag will generate HTML in a default format.

 | `none` |
| 

`path_prefixes`

 | String | 

URL paths or subdirectories to include posts from (comma separated). If a blog post has a similar prefix in its path, the post’s relevancy is increased, improving its ranking in the listing.

 | `none` |
| 

`start_date`

 | date/time | 

Allows for filtering of posts published after a date/time.

 | `none` |
| 

`end_date`

 | Date/Time | 

Allows for filtering of posts published before a date/time.

 | `False` |
| 

`blog_post_override`

 | String | 

The ID(s) of a blog posts which should always show up in the returned listing, despite all other parameter values and filters (comma separated).

 | `none` |

We strongly recommend using the `callback` parameter instead of the `post_formatter` parameter to ensure faster page load times.

Please note that if the `related_blog_posts` HubL tag is being used on a post, the `blog_post_ids` parameter should not be specified, as on blog posts, it will default to the post the widget is appearing on.

Example usages of the related\_blog\_posts HubL tag[](https://developers.hubspot.com/docs/cms/guides/creating-a-related-post-listing#example-usages-of-the-related-blog-posts-hubl-tag)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Below are some example ways to use this tag to enhance your website.

### Display posts from a specific author across multiple blogs[](https://developers.hubspot.com/docs/cms/guides/creating-a-related-post-listing#display-posts-from-a-specific-author-across-multiple-blogs)

In this example, we generate a listing of posts written by one of the three specified `blog_authors` across two different blogs. 

{% related\_blog\_posts blog\_ids="3241539189,3261083894", limit=6, blog\_authors="John Smith,Joe Smith,Frank Smith" %}

### Display posts with the tag "sales enablement", restricted to a specific publish date time frame[](https://developers.hubspot.com/docs/cms/guides/creating-a-related-post-listing#display-posts-with-the-tag-sales-enablement-restricted-to-a-specific-publish-date-time-frame)

In this example, we generate a listing of 10 posts related to a specific blog post, with the tag "sales enablement", and restricted to a specific publish date time frame. This example specifies the `blog_post_ids` parameter, so it would be used on a page.  

{% related\_blog\_posts blog\_post\_ids="3267910554", limit=10, tags="sales enablement", start\_date="2018-02-05", end\_date="2018-06-10" %}

### Display posts using a JS callback to control HTML output[](https://developers.hubspot.com/docs/cms/guides/creating-a-related-post-listing#display-posts-using-a-js-callback-to-control-html-output)

In this example, we generate a listing of 5 posts  using the `callback` parameter to control the HTML output of the post listing. (Instead of the `post_formatter` parameter using a [macro](/docs/cms/hubl/variables-macros-syntax#macros).)

{% related\_blog\_posts limit=5, callback="blog\_post\_formatter" %} <script> var blog\_post\_formatter = function(blogposts) { var formatted = "<div>"; for (var i = 0; i < blogposts.length; i++) { var blogpost = blogposts\[i\]; formatted += '<div class="related-blog-item">'; formatted += \`<span>Related Post ${i + 1}/${blogposts.length}</span><br>\`; formatted += \`<a class="related-blog-title" href="${blogpost.url}"><span>${blogpost.name}</span></a>\`; formatted += \`<div class="hs-related-blog-byline">by <span class="related-blog-author">${blogpost.blogAuthor.fullName}</span><span class="related-blog-posted-at"> posted on </span><span class="related-blog-date">${new Date(blogpost.publishDate).toLocaleDateString()}</span></div>\`; formatted += \`<p class="related-blog-post-summary">${blogpost.postSummary}<a href="${blogpost.url}">Read more</a></p>\`; formatted += '<div class="related-blog-tags">'; if (blogpost.tagList.length > 0) { formatted += \`Tags: ${blogpost.tagList.map(tag => tag.label).join(", ")}\`; } formatted += '</div>'; if (blogpost.featuredImage) { formatted += \`<img src="${blogpost.featuredImage}" alt="${blogpost.featuredImageAltText}">\`; } formatted += '</div>'; } formatted += '</div>'; return formatted; } </script>

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/creating-a-related-post-listing#page-feedback)
-------------------------------------------------------------------------------------------------------------------

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