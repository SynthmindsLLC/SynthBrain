HubL standard tags


======================

Last updated: March 20, 2024

This page is a comprehensive reference guide of the syntax and the available parameters for all standard HubL tags, including [tags for system pages](#system-page-tags), such as the email subscription page. Each tag below contains a sample of the basic syntax, as well as an example with parameters and code output.

If you're building drag and drop areas, learn more about [drag and drop area tags](/docs/cms/hubl/tags/dnd-areas). If you maintain an older website, you may also want to check out the [list of deprecated HubL tags](/docs/cms/hubl/tags/deprecated).

Most of the tags in this page have [default module equivalents.](/docs/cms/building-blocks/modules/default-modules) Modules can be used within **[dnd\_areas](/docs/cms/building-blocks/templates/drag-and-drop-areas)** and **[flexible columns](#flexible-column)**, making them more powerful and user friendly than the tags you see here.

Blog comments[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-comments)
--------------------------------------------------------------------------------

A blog comments tag renders the comments embed code on a blog template. This Javascript embed code loads the comments form and comments, based upon your configuration in your [website settings](/docs/cms/building-blocks/website-settings).

Blog Comment Form module: {% blog\_comments "blog\_comments" overrideable=False, label="Blog Comments" %} Blog Comment Count module: {% blog\_comments "blog\_comments" %} Blog Comment listing for specific blog: {% blog\_comments "default\_blog\_comments" select\_blog="359485112" %}Blog Commment Form Output: <span id="hs\_cos\_wrapper\_blog\_comments" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_blog\_comments" style="" data-hs-cos-general-type="widget" data-hs-cos-type="blog\_comments"> <div class="section post-footer"> <div id="comments-listing" class="new-comments no-comments"></div> <div id="hs-comment-embed" style="display:none;"></div> <div id="comment-form" class="new-comments"> <form novalidate="" accept-charset="UTF-8" action="https://api.hubapi.com/comments/v3/comment?portalId=311600" enctype="multipart/form-data" id="hsForm\_d30edada-82e4-4a69-aaf4-a9d0376f37e6" method="POST" class="hs-form stacked" data-form-id="d30edada-82e4-4a69-aaf4-a9d0376f37e6" data-portal-id="311600" data-reactid=".hbspt-forms-0"> <div data-reactid=".hbspt-forms-0.0:$0"> <div class="hs\_email field hs-form-field" data-reactid=".hbspt-forms-0.0:$0.$email"> <label class="" placeholder="Enter your Email" for="email-d30edada-82e4-4a69-aaf4-a9d0376f37e6" data-reactid=".hbspt-forms-0.0:$0.$email.0"> <span data-reactid=".hbspt-forms-0.0:$0.$email.0.0">Email</span><span class="hs-form-required" data-reactid=".hbspt-forms-0.0:$0.$email.0.1">\*</span> </label> <legend class="hs-field-desc" style="display:none;" data-reactid=".hbspt-forms-0.0:$0.$email.1"> </legend> <div class="input" data-reactid=".hbspt-forms-0.0:$0.$email.$email"> <input id="email-d30edada-82e4-4a69-aaf4-a9d0376f37e6" class="hs-input" type="email" name="email" required="" placeholder="" value="" data-reactid=".hbspt-forms-0.0:$0.$email.$email.0"> </div> </div> </div> <div data-reactid=".hbspt-forms-0.0:$1"> <div class="hs\_website field hs-form-field" data-reactid=".hbspt-forms-0.0:$1.$website"> <label class="" placeholder="Enter your Website" for="website-d30edada-82e4-4a69-aaf4-a9d0376f37e6" data-reactid=".hbspt-forms-0.0:$1.$website.0"> <span data-reactid=".hbspt-forms-0.0:$1.$website.0.0">Website</span> </label> <legend class="hs-field-desc" style="display:none;" data-reactid=".hbspt-forms-0.0:$1.$website.1"></legend> <div class="input" data-reactid=".hbspt-forms-0.0:$1.$website.$website"> <input id="website-d30edada-82e4-4a69-aaf4-a9d0376f37e6" class="hs-input" type="text" name="website" value="" placeholder="" data-reactid=".hbspt-forms-0.0:$1.$website.$website.0"> </div> </div> </div> <div data-reactid=".hbspt-forms-0.0:$2"> <div class="hs\_comment field hs-form-field" data-reactid=".hbspt-forms-0.0:$2.$comment"> <label class="" placeholder="Enter your Comment" for="comment-d30edada-82e4-4a69-aaf4-a9d0376f37e6" data-reactid=".hbspt-forms-0.0:$2.$comment.0"> <span data-reactid=".hbspt-forms-0.0:$2.$comment.0.0">Comment</span> <span class="hs-form-required" data-reactid=".hbspt-forms-0.0:$2.$comment.0.1">\*</span> </label> <legend class="hs-field-desc" style="display:none;" data-reactid=".hbspt-forms-0.0:$2.$comment.1"></legend> <div class="input" data-reactid=".hbspt-forms-0.0:$2.$comment.$comment"> <textarea id="comment-d30edada-82e4-4a69-aaf4-a9d0376f37e6" class="hs-input" name="comment" required="" placeholder="" data-reactid=".hbspt-forms-0.0:$2.$comment.$comment.0"></textarea> </div> </div> </div> <div data-reactid=".hbspt-forms-0.0:$3"> <div class="hs\_subscribe field hs-form-field" data-reactid=".hbspt-forms-0.0:$3.$subscribe"> <label class="" placeholder="Enter your Subscribe to follow-up comments for this post" for="subscribe-d30edada-82e4-4a69-aaf4-a9d0376f37e6" data-reactid=".hbspt-forms-0.0:$3.$subscribe.0"> <span data-reactid=".hbspt-forms-0.0:$3.$subscribe.0.0"></span> </label> <legend class="hs-field-desc" style="display:none;" data-reactid=".hbspt-forms-0.0:$3.$subscribe.1"></legend> <div class="input" data-reactid=".hbspt-forms-0.0:$3.$subscribe.$subscribe"> <ul class="inputs-list" data-reactid=".hbspt-forms-0.0:$3.$subscribe.$subscribe.0"> <li class="hs-form-booleancheckbox" data-reactid=".hbspt-forms-0.0:$3.$subscribe.$subscribe.0.0"> <label for="subscribe-d30edada-82e4-4a69-aaf4-a9d0376f37e6" class="hs-form-booleancheckbox-display" data-reactid=".hbspt-forms-0.0:$3.$subscribe.$subscribe.0.0.0"> <input id="subscribe-d30edada-82e4-4a69-aaf4-a9d0376f37e6" class="hs-input" type="checkbox" name="subscribe" value="true" data-reactid=".hbspt-forms-0.0:$3.$subscribe.$subscribe.0.0.0.0"> <span data-reactid=".hbspt-forms-0.0:$3.$subscribe.$subscribe.0.0.0.1">Subscribe to follow-up comments for this post</span> </label> </li> </ul> </div> </div> </div> <div data-reactid=".hbspt-forms-0.0:$4"> <div class="hs\_lifecyclestage field hs-form-field" style="display:none;" data-reactid=".hbspt-forms-0.0:$4.$lifecyclestage"> <label class="" placeholder="Enter your Lifecycle Stage" for="lifecyclestage-d30edada-82e4-4a69-aaf4-a9d0376f37e6" data-reactid=".hbspt-forms-0.0:$4.$lifecyclestage.0"> <span data-reactid=".hbspt-forms-0.0:$4.$lifecyclestage.0.0">Lifecycle Stage</span> </label> <legend class="hs-field-desc" style="display:none;" data-reactid=".hbspt-forms-0.0:$4.$lifecyclestage.1"></legend> <div class="input" data-reactid=".hbspt-forms-0.0:$4.$lifecyclestage.$lifecyclestage"> <input name="lifecyclestage" class="hs-input" type="hidden" value="subscriber" data-reactid=".hbspt-forms-0.0:$4.$lifecyclestage.$lifecyclestage.0"> </div> </div> </div> <div class="hs\_submit" data-reactid=".hbspt-forms-0.2"> <div class="hs-field-desc" style="display:none;" data-reactid=".hbspt-forms-0.2.0"></div> <div class="actions" data-reactid=".hbspt-forms-0.2.1"> <input type="submit" value="Submit Comment" class="hs-button primary" data-reactid=".hbspt-forms-0.2.1.0"> </div> </div> <input name="hs\_context" type="hidden" value="{&quot;rumScriptExecuteTime&quot;:1396.815,&quot;rumServiceResponseTime&quot;:7737.500000000001,&quot;rumFormRenderTime&quot;:187.17999999999938,&quot;rumTotalRenderTime&quot;:7738.14,&quot;rumTotalRequestTime&quot;:183.2549999999992,&quot;pageUrl&quot;:&quot;http://311600.hs-sites.com/-temporary-slug-5eccb1d9-1f1b-4bbd-8e19-00e198331b15?hs\_preview=ALicr-ma-4312320350&quot;,&quot;pageTitle&quot;:&quot;HubSpot Sales Professional User Guide: HubSpot Sales Professional Overview&quot;,&quot;source&quot;:&quot;FormsNext-static-1.390&quot;,&quot;isHostedOnHubspot&quot;:true,&quot;timestamp&quot;:1479135449193,&quot;userAgent&quot;:&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_11\_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36&quot;,&quot;referrer&quot;:&quot;&quot;,&quot;hutk&quot;:&quot;a525e671c25f6b108d25e08c892e359e&quot;,&quot;originalEmbedContext&quot;:{&quot;portalId&quot;:&quot;311600&quot;,&quot;formId&quot;:&quot;d30edada-82e4-4a69-aaf4-a9d0376f37e6&quot;,&quot;target&quot;:&quot;#comment-form&quot;,&quot;redirectUrl&quot;:&quot;http://www.hubspot.com/contact-sales/thanks/&quot;,&quot;pageId&quot;:&quot;23423&quot;,&quot;pageName&quot;:&quot;My great landing page&quot;,&quot;css&quot;:&quot;.your-custom-css {background-color: #fe7722}&quot;,&quot;requiredCss&quot;:&quot;.my-custom-error-msgs {border-radius: 3px;}&quot;,&quot;submitButtonClass&quot;:&quot;hs-button primary&quot;},&quot;recentFieldsCookie&quot;:{},&quot;pageId&quot;:&quot;23423&quot;,&quot;pageName&quot;:&quot;My great landing page&quot;,&quot;boolCheckBoxFields&quot;:&quot;subscribe&quot;,&quot;dateFields&quot;:&quot;&quot;,&quot;redirectUrl&quot;:&quot;http://www.hubspot.com/contact-sales/thanks/&quot;,&quot;smartFields&quot;:{},&quot;urlParams&quot;:{&quot;hs\_preview&quot;:&quot;ALicr-ma-4312320350&quot;},&quot;formValidity&quot;:{},&quot;correlationId&quot;:&quot;55d71532-ab6b-4415-98f5-f3a16d7741c9&quot;,&quot;disableCookieSubmission&quot;:false}" data-reactid=".hbspt-forms-0.3"> <input type="hidden" id="id\_portalId" name="portalId" value="311600"><input type="hidden" id="id\_contentId" name="contentId" value="4312320350"> <input type="hidden" id="id\_collectionId" name="collectionId" value="2224463151"> <input type="hidden" id="id\_contentAuthorEmail" name="contentAuthorEmail" value="cstone@hubspot.com"><input type="hidden" id="id\_contentAuthorName" name="contentAuthorName" value="Christopher Stone"> <input type="hidden" id="id\_comment\_verification\_text" name="comment\_verification\_text" value="Your comment has been received."> <input type="hidden" id="id\_contentTitle" name="contentTitle" value="HubSpot Sales Professional User Guide: HubSpot Sales Professional Overview"> <input type="hidden" id="id\_contentPermalink" name="contentPermalink" value="http://311600.hs-sites.com/-temporary-slug-5eccb1d9-1f1b-4bbd-8e19-00e198331b15"> <input type="hidden" id="id\_contentCreatedAt" name="contentCreatedAt" value="1479135208000"> <input type="hidden" id="id\_formGuid" name="formGuid" value="d30edada-82e4-4a69-aaf4-a9d0376f37e6"> </form> </div> </div> </span> Blog Comment Listing Module Output: (function ($) { var commentsEmbedContext = { portalId: 327485, collectionId: 359485112, contentId: 2684120609, target: '#comments-listing.new-comments', showComments: true, showForm: true, commentVerificationText: "Your comment has been received.", embedScriptEnv: "prod", apiEnv: "prod", contentTitle: "Post title", contentCreatedAt: "1427849160000", contentPermalink: "http:\\/\\/designers.hubspot.com\\/blog\\/post-name, contentAuthorEmail: "dhunt@hubspot.com", contentAuthorName: "David Hunt", captchaRequired: true, captchaKey: "6Lc3uMsSAAAAAMjk4NIvPQK9\_-ZLk2wBokFCo5Qt", maxThreadDepth: 3, formId: "8d42bb92-241b-4894-b853-1d5f6553daa0" }; function loadComments() { if (window.hubspot && typeof window.hubspot.loadCommentsEmbed === 'function') { hubspot.loadCommentsEmbed(commentsEmbedContext.embedScriptEnv, function () { if (typeof window.hsEmbedComments === 'function') { window.hsEmbedComments(commentsEmbedContext); } }); } else { setTimeout(loadComments, 50); } } loadComments(); })(window.hsjQuery || jQuery);

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`limit`

 | Number | 

Sets maximum number of comments.

 | `5000` |
| 

`select_blog`

 | "default" or blog ID | 

Specifies which blog is connected to the comments embed. This parameter accepts arguments of either `"default"` or a blog ID (available in the URL of the Blog dashboard). If want to use your default blog, this parameter is unnecessary.

 | `default` |
| 

`skip_css`

 | Boolean | 

Setting this option to True will stop the blog comments CSS from loading. 

 | `false` |
| 

`message`

 | String | 

The message to display when there are no comments. By default, appears as empty (no text displayed).

 | `""` |

Blog content[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-content)
------------------------------------------------------------------------------

While [drag and drop layouts](/docs/cms/building-blocks/templates/drag-and-drop-templates) include a blog content module, these modules are not created with a single tag. They instead use conditional logic to define how a blog post and a blog listing should render. [You can learn more about coding blog templates here.](/docs/cms/building-blocks/templates/blog-template-markup)

Blog post filter[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-post-filter)
--------------------------------------------------------------------------------------

Creates a linked listing of posts by topic, posts by month, or posts by author.

**Please note:** this module can only be used in blog post templates.

{% post\_filter "post\_filter" %} {% post\_filter "posts\_by\_topic" select\_blog="default", expand\_link\_text="see all", overrideable=False, list\_title="Posts by Topic", max\_links=5, filter\_type="topic", label="Posts by Topic" %}<span id="hs\_cos\_wrapper\_posts\_by\_topic" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_post\_filter" style="" data-hs-cos-general-type="widget" data-hs-cos-type="post\_filter"> <div class="block"> <h3>Posts by Topic</h3> <div class="widget-module"> <ul> <li><a href="http://www.hubspot.com/blog/topic/sales">Sales</a></li> <li><a href="http://www.hubspot.com/blog/topic/marketing">Marketing</a></li> <li><a href="http://www.hubspot.com/blog/topic/service">Service</a> </li> <li> <a href="http://www.hubspot.com/blog/topic/operations">Operations</a> </li> <li> <a href="http://www.hubspot.com/blog/topic/cms">CMS</a> </li> <li> <a href="http://www.hubspot.com/blog/topic/industry">Industry</a> </li> </ul> </div> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | "default" or blog ID | 

Selects the HubSpot blog to use. This parameter uses either an blog ID or "default" value.

 | `"default"` |
| 

`expand_link_text`

 | String | 

 Text link to display if more posts than max\_links number available. Exclude parameter to omit link.

 | `"see all"` |
| 

`list_title`

 | String | 

List title to display.

 | `""` |
| 

`list_tag`

 | String | 

Sets the tag used for the list. Value should generally be `"ul"` or `"ol"`.

 | `"ul"` |
| 

`title_tag`

 | String | 

Sets the tag used for the list title.

 | `"h3"` |
| 

`max_links`

 | Number | 

Maximum number of filter values to display. Excude parameter to show all.

 | `5` |
| 

`filter_type`

 | Enumeration | 

Selects the type of filter. Possible values include `"topic"`, `"month"`, and `"author"`.

 | `"topic"` |

Blog post Listing[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-post-listing)
----------------------------------------------------------------------------------------

Adds a listing of most popular or top posts.

**Please note:** this tag can only be used in blog post templates. The tag's content is loaded asynchronously on the client-side. As a result, if you want to manipulate the feed after it's loaded, you'll need to define a global JS function to handle that manipulation. Use the function `hsPostListingComplete(feeds)`, where `feeds` is the jQuery selector on all feeds that have been completed. You will want to directly manipulate the DOM object in that function.

{% post\_listing "post\_listing" %} {% post\_listing "top\_posts" select\_blog="default", label="Recent Posts", overrideable=False, list\_title="Recent Posts", listing\_type="recent", max\_links=5 %}<span id="hs\_cos\_wrapper\_module\_42751498763\_top\_posts" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_post\_listing" style="" data-hs-cos-general-type="widget" data-hs-cos-type="post\_listing"> <div class="block"> <h3>Recent Posts</h3> <div class="widget-module"> <ul class="hs-hash-1630637453-1678475653429"> <li class="hs-postlisting-item"> <a href="https://blog.hubspot.com/marketing/product-category-marketing">9 Product Category Marketing Examples to Inspire Your Own</a> </li> <li class="hs-postlisting-item"> <a href="https://blog.hubspot.com/marketing/increasing-mobile-conversion-rate">Mobile Conversion Rate: What It Is and How To Increase It</a> </li> <li class="hs-postlisting-item"> <a href="https://blog.hubspot.com/blog/tabid/6307/bid/33401/14-real-life-examples-of-cta-copy-you-should-copy.aspx">14 Real-Life Examples of CTA Copy YOU Should Copy</a> </li> </ul> </div> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | "default" or blog ID | 

 Selects the HubSpot blog to use for the listing. This parameter uses either an blog ID or `"default"` value.

 | `"default"` |
| 

`list_title`

 | String | 

List title to display.

 | `""` |
| 

`list_tag`

 | String | 

Sets the tag used for the list. Value should generally be `"ul"` or `"ol"`.

 | `"ul"` |
| 

`title_tag`

 | String | 

Sets the tag used for the list title.

 | `"h3"` |
| 

`listing_type`

 | String | 

List the blog posts by most recent or most popular in a time range. Possible values include recent, popular\_all\_time, popular\_past\_year, popular\_past\_six\_months, and popular\_past\_month.

 | `"recent"` |
| 

`max_links`

 | Number | 

 Maximum number of blog posts to list.

 | `5` |
| 

`include_featured_image`

 | Boolean | 

 Display featured image along with post link.

 | `False` |

Blog related posts[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-related-posts)
------------------------------------------------------------------------------------------

Adds a listing of blog posts based off of a set of parameters shared by posts across blogs. Posts are selected based off of their relevance to the set parameters.

This tag does not generate a page/post-level editable module, it is entirely configured with HubL.

{% related\_blog\_posts limit=2, blog\_ids="1,2", tags="Sales enablement,Marketing", blog\_authors="John Smith,Frank Smith", path\_prefixes="/business-blog", start\_date="2018-04-10", end\_date="2018-04-10", blog\_post\_override="2783035366" %}<span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_related\_blog\_posts" data-hs-cos-general-type="widget" data-hs-cos-type="related\_blog\_posts" id="hs\_cos\_wrapper\_" style=""><!--related-blog-entries--></span> <div class="hs-related-blog-module feedreader\_box"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_related\_blog\_posts" data-hs-cos-general-type="widget" data-hs-cos-type="related\_blog\_posts" id="hs\_cos\_wrapper\_" style=""></span> <div class="hs-related-blog-item"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_related\_blog\_posts" data-hs-cos-general-type="widget" data-hs-cos-type="related\_blog\_posts" id="hs\_cos\_wrapper\_" style=""></span> <div class="hs-related-blog-item-text"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_related\_blog\_posts" data-hs-cos-general-type="widget" data-hs-cos-type="related\_blog\_posts" id="hs\_cos\_wrapper\_" style=""><a class="hs-related-blog-title" href="//www.hubspot.com/business-blog/marketing-is-fun"><span>Marketing is fun</span></a></span> <div class="hs-related-blog-byline">by <span class="hs-related-blog-author">John Smith</span> <span class="hs-related-blog-posted-at">posted on</span> <span class="hs-related-blog-date">June 3, 2018</span> </div> <div class="hs-related-blog-byline"> <p class="hs-related-blog-description">Learn how to make marketing fun!<a href="//www.hubspot.com/business-blog/marketing-is-fun">Read more</a></p> </div> <div class="hs-related-blog-byline"> <span class="hs-related-blog-tags">Tags: Marketing</span> </div> </div> </div> <div class="hs-related-blog-item hs-with-featured-image"> <div class="hs-related-blog-item-text"> <a class="hs-related-blog-title" href="//www.hubspot.com/business-blog/sales-is-fun"><span>Sales is fun</span></a> <div class="hs-related-blog-byline">by <span class="hs-related-blog-author">Frank Smith</span> <span class="hs-related-blog-posted-at">posted on</span> <span class="hs-related-blog-date">June 7, 2018</span> </div> <div class="hs-related-blog-byline"> <p class="hs-related-blog-description">Learn how to make sales fun!<a href="//www.hubspot.com/business-blog/sales-is-fun">Read more</a></p> </div> <div class="hs-related-blog-byline"> <span class="hs-related-blog-tags">Tags: Sales enablement</span> </div> </div> <div class="hs-related-blog-item-image-wrapper"><img alt="" class="hs-related-blog-featured-image" src="//www.hubspot.com/hubfs/business-blog/sales-is-fun.jpg"></div> </div> </div>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`blog_ids`

 | Number | 

The IDs of the blogs to include posts from. If not specified, it will include posts from the default blog.

 |  |
| 

`blog_post_ids`

 | String | 

The IDs of the blog posts to use when finding relevant blog posts to list, separated by commas.

Use this parameter only when the widget is appearing on pages. When used on blog posts, it will look for relevant posts based on the currently displaying blog post.

 |  |
| 

`blog_post_override`

 | String | 

The IDs of the blog posts which should always show up in the returned listing, despite all other parameter values and filters (comma separated).

 |  |
| 

`limit`

 | Number | 

 The maximum number of blog posts to list.

 | `3` |
| 

`tags`

 | String | 

The blog tags that should be used to determine if a post is relevant (comma separated). Blog posts with the specified tags will rank higher for relevancy.

 |  |
| 

`tag_boost`

 | Number | 

Increases the weight given to the tags specified in the `tags` parameter to generate related posts. Include this parameter to pull in posts more closely related to the currently displaying or specified posts. Accepts positive numbers.

 |  |
| 

`start_date`

 | datetime | 

Earliest published date.

See an [example below](#examples).

 |  |
| 

`end_date`

 | datetime | 

Latest published date.

See an [example below](#examples).

 |  |
| 

`blog_authors`

 | String | 

 The names of authors to include posts from (comma separated).

See an [example below](#examples).

 |  |
| 

`path_prefixes`

 | String | 

URL paths or subdirectories to include posts from (comma separated). If a blog post has a similar prefix in its path, the post’s relevancy is increased, improving its ranking in the listing.

 |  |
| 

`callback`

 | String | 

The name of a JavaScript function to render returned blog posts. The function is passed an array of blog post objects to format. If neither the `callback` nor `post_formatter` parameter is specified, the tag will generate HTML in a default format.

See an [example below](#examples).

 | `none` |
| 

`post_formatter`

 | String | 

The name of a custom macro to render returned blog posts. The macro is passed three parameters which are the blogs blog post object to format, the count in the iteration of blog posts, and the total count of blog posts in the results. If not specified or set to `default`, the built-in formatter will be used to format each post.

 | `default` |
| 

`allow_any_language`

 | Boolean | 

When set to `false`, only posts in the same language as the page the tag is used on will appear. When set to `true`, the language restriction is ignored and all related posts are pulled in regardless of the page language. 

 | `False` |

We strongly recommend using the `callback` parameter instead of `post_formatter` to improve page loading speed.

### Examples[](https://developers.hubspot.com/docs/cms/hubl/tags#examples)

The following example generates a listing of posts written by one of the three specified `blog_authors` across two different blogs:

HubL

Copy all

    {% related_blog_posts blog_ids="3241539189,3261083894", limit=6, blog_authors="John Smith,Joe Smith,Frank Smith" %}

The following example generates a listing of 10 posts related to a specific blog post, with the blog tag "sales enablement," and restricted to a specific publish date time frame. This example specifies the `blog_post_ids` parameter, so it would be used on a page:

HubL

Copy all

    {% related_blog_posts blog_post_ids="3267910554", limit=10, tags="sales enablement", start_date="2018-02-05", end_date="2018-06-10" %}

The following example generates a listing of five posts using the `callback` parameter to control the HTML output of the post listing:

HubL

Copy all

    {% related_blog_posts limit=5, callback="blog_post_formatter" %}
    
    <script>
      var blog_post_formatter = function(blogposts) {
    
        var formatted = "<div>";
        for (var i = 0; i < blogposts.length; i++) {
          var blogpost = blogposts[i];
          formatted += '<div class="related-blog-item">';
          formatted += `<span>Related Post ${i + 1}/${blogposts.length}</span><br>`;
          formatted += `<a class="related-blog-title" href="${blogpost.url}"><span>${blogpost.name}</span></a>`;
          formatted += `<div class="hs-related-blog-byline">by <span class="related-blog-author">${blogpost.blogAuthor.fullName}</span><span class="related-blog-posted-at"> posted on </span><span class="related-blog-date">${new Date(blogpost.publishDate).toLocaleDateString()}</span></div>`;
          formatted += `<p class="related-blog-post-summary">${blogpost.postSummary}<a href="${blogpost.url}">Read more</a></p>`;
          formatted += '<div class="related-blog-tags">';
          if (blogpost.tagList.length > 0) {
            formatted += `Tags: ${blogpost.tagList.map(tag => tag.label).join(", ")}`;
          }
          formatted += '</div>';
          
          if (blogpost.featuredImage) {
            formatted += `<img src="${blogpost.featuredImage}" alt="${blogpost.featuredImageAltText}">`;
          }
          formatted += '</div>';
        }
        formatted += '</div>';
        return formatted;
      }
    </script>

Blog social sharing[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-social-sharing)
--------------------------------------------------------------------------------------------

Blog social sharing renders share counters on your blog posts (if enabled in Content Settings).

{% blog\_social\_sharing "blog\_social\_sharing" %} {% blog\_social\_sharing "blog\_social\_sharing" select\_blog="359485112" %}<span id="hs\_cos\_wrapper\_blog\_social\_sharing" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_blog\_social\_sharing" style="" data-hs-cos-general-type="widget" data-hs-cos-type="blog\_social\_sharing"> <div class="hs-blog-social-share"> <ul class="hs-blog-social-share-list"> <li class="hs-blog-social-share-item hs-blog-social-share-item-twitter"> <a href="https://twitter.com/share" class="twitter-share-button" data-lang="en" data-url="http://designers.hubspot.com/blog" data-size="medium" data-text="">Tweet</a> </li> <li class="hs-blog-social-share-item hs-blog-social-share-item-linkedin"> <script type="IN/Share" data-url="http://designers.hubspot.com/blog" data-showzero="true" data-counter="right"></script> </li> <li class="hs-blog-social-share-item hs-blog-social-share-item-facebook"> <div class="fb-like" data-href="http://designers.hubspot.com/blog" data-layout="button\_count" data-action="like" data-show-faces="false" data-share="true" data-width="120"></div> </li> <li class="hs-blog-social-share-item hs-blog-social-share-item-google-plus"> <div class="g-plusone" data-size="medium" data-href="http://designers.hubspot.com/blog"></div> </li> </ul> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | "default" or blog ID | 

Species which blog is connected to the share counters. This parameter accepts arguments of either `"default"` or a blog ID (available in the URL of the Blog dashboard). If you want to use your default blog, this parameter is unnecessary.

 | `default` |
| 

`downgrade_shared_url`

 | Boolean | 

Use HTTP in the url sent to the social media networks. Used to preserve counts when upgrading domains to HTTPS only.

 | `false` |

Blog subscription[](https://developers.hubspot.com/docs/cms/hubl/tags#blog-subscription)
----------------------------------------------------------------------------------------

A blog subscription tag renders the blog subscriber form for a particular blog. This form is automatically created whenever a blog is created in Content Settings, and there is always one subscription form per blog. Please note that the subscribe form's fields are configured within the Forms editor UI.

{% blog\_subscribe "blog\_subscribe" %} {% blog\_subscribe "subscribe\_designers\_blog" select\_blog="default", title="Subscribe to the Designers Blog", response\_message="Thanks for Subscribing!", label="Blog Email Subscription", overrideable=False %}<span id="hs\_cos\_wrapper\_blog\_subscription" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_blog\_subscribe" style="" data-hs-cos-general-type="widget" data-hs-cos-type="blog\_subscribe"> <h3 id="hs\_cos\_wrapper\_blog\_subscription\_title" class="hs\_cos\_wrapper form-title" data-hs-cos-general-type="widget\_field" data-hs-cos-type="text">Subscribe to Designers Blog</h3> <div id="hs\_form\_target\_blog\_subscription"></div> <script charset="utf-8" src="//js.hsforms.net/forms/current.js"></script> <script> hbspt.forms.create({ portalId: '327485', formId: 'a8d73dc6-0d3a-486d-8938-b19f28b69c3c', formInstanceId: '60', pageId: 2749976739, pageName: 'Apple, Google & Starbucks: Inside the Web Design Style Guides of 10 Famous Companies', redirectUrl: 'http://designers.hubspot.com/blog/web-design-style-guides-examples?hsFormKey=a56a754bc4c3465015935953363b8ff3#blog\_subscription', css: '', target: '#hs\_form\_target\_blog\_subscription', formData: { cssClass: 'hs-form stacked' } }); </script> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | "default" or blog ID | 

Selects which blog subscription form to render. This parameter accepts arguments of either `"default"` or a blog ID (available in the URL of the Blog dashboard). If want to use your default blog, this parameter is unnecessary.

 | `default` |
| 

`title`

 | String | 

Defines text in an h3 tag title above the subscribe form.

 | `"Subscribe Here!"` |
| 

`no_title`

 | Boolean | 

If True, the h3 tag above the title is removed.

 | `false` |
| 

`response_message`

 | String | 

Defines the inline thank-you message that is rendered when a user submits a form. Supports HTML.

 | `"Thanks for Subscribing!"` |
| 

`edit_form_link`

 | String | 

This parameter generates a link that allows users to click through to the corresponding Form editor screen. This option will only show in the editor UI if the modules has the parameter overrideable=True.

For example, to replace HubID and form ID with the information from the URL of your default blog subscriber form: `edit_form_link=" <ul>\n <li><a href="/forms/HubID/FormID/edit/" target="_blank">Default Blog</a></li> \n</ul> "`.

\\n drops the code onto a new line.

 |  |

Boolean[](https://developers.hubspot.com/docs/cms/hubl/tags#boolean)
--------------------------------------------------------------------

A boolean tag creates a checkbox in the UI that prints "true" or "false." In addition to printing the value, this module is useful for defining conditional template logic, when combined with the parameter [`export_to_template_context`](/docs/cms/building-blocks/modules/export-to-template-context). 

{% boolean "boolean" %} {% boolean "nav\_toggle" label="Hide navigation", value=False, no\_wrapper=True %}false

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`value`

 | Boolean | 

Determines whether the checkbox is checked or unchecked.

 | `False` |

Choice[](https://developers.hubspot.com/docs/cms/hubl/tags#choice)
------------------------------------------------------------------

A choice tag creates a dropdown in the content editor UI that prints the value selected by the user. Choice tags are great for giving your users a preset set of options, such as printing the type of page as a page header.  
  
In addition to printing the choice value, this tag is useful for defining conditional template logic, when combined with the parameter [`export_to_template_context`](/docs/cms/building-blocks/modules/export-to-template-context). 

{% choice "choice" %} {% choice "type\_of\_page" label="Choose the type of page", value="About", choices="About, Careers, Contact, Store" %}<span id="hs\_cos\_wrapper\_type\_of\_page" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_choice" style="" data-hs-cos-general-type="widget" data-hs-cos-type="choice"> About </span>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`value`

 | Boolean | 

The default field value for the dropdown

 |
| 

`choices`

 | Sequence | 

A comma-separated list of values, or list of value-label pairs. The syntax for value label pairs is as follows: `choices="[[\"value1\", \"Label 1\"], [\"value2\", \"Label 2\"]]"`. The editor will display the label, while it will print the value to the page.

 |

Color[](https://developers.hubspot.com/docs/cms/hubl/tags#color)
----------------------------------------------------------------

The color tag generates a color picker in the page editor UI that prints a HEX color value to a template. Please note that this module can only be used in templates, not CSS files. If using this tag in a `<style>` or inline CSS, you will want to use the `no_wrapper=True` parameter to remove the wrapper `<span>` wrapper.

{% color "color" %} {% color "my\_color\_picker" label="Choose a color", color="#000000", no\_wrapper=True %}#000000

| Parameter | Type | Description |
| --- | --- | --- |
| 
`color`

 | String | 

A default HEX color value for the color picker

 |

CTA[](https://developers.hubspot.com/docs/cms/hubl/tags#cta)
------------------------------------------------------------

A Call to Action or CTA tag allows users to add a HubSpot Call to Action button to a predefined area of a page.

{% cta "cta" %} {% cta "my\_cta" label="Select a CTA", guid="ccd39b7c-ae18-4c4e-98ee-547069bfbc5b", image\_src="https://no-cache.hubspot.com/cta/default/53/c7335b66-a0d4-4d19-82eb-75e1626d02d0.png" %}<span id="hs\_cos\_wrapper\_" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_cta" style="" data-hs-cos-general-type="widget" data-hs-cos-type="cta"> <!--HubSpot Call-to-Action Code --> <span class="hs-cta-wrapper" id="hs-cta-wrapper-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b"> <span class="hs-cta-node hs-cta-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b" id="hs-cta-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b" style="visibility: visible;"> <a id="cta\_button\_158015\_19a9097a-8dff-4181-b8f7-955a47f29826" class="cta\_button " href="//cta-service-cms2.hubspot.com/ctas/v2/public/cs/c/?cta\_guid=19a9097a-8dff-4181-b8f7-955a47f29826&placement\_guid=ccd39b7c-ae18-4c4e-98ee-547069bfbc5b&portal\_id=158015&redirect\_url=APefjpFSOqhysLBE-Yye5WFoP82Swxb2PVWpfI3VxlUjuOCHfiVMcxKic3yM28vuwu9UB8\_Jyhk6DGRCEN63hKqQOMtMTGmQZ1UNMK3LtNx0sRrAfQQYna2BfZ9RmgQOs8sKO\_PcKOP6G26L5wQ5vdcXXOiMCxFPJxzPzUCcl474iiHKbEo5H8LVtZf6e140VOSGJ37NTpxCcPHLDvH9iFaT6mR0BnKzFReaX0FXBj7Lx2rFLVCZcIC0bdaFEGI1uKOJBMNT9RDtEzeJzUHzFYN0b34uv-ZR4w&hsutk=683eeb5b499fdfdf469646f0014603b4&utm\_referrer=http%3A%2F%2Fwww.davidjosephhunt.com%2Fvariables%3Fhs\_preview%3D159bC1Cj-2863569740&canon=http%3A%2F%2Fwww.davidjosephhunt.com%2Fvariables" style="" cta\_dest\_link="http://www.hubspot.com/free-trial" title="Start a HubSpot trial"> Start a HubSpot trial </a> </span> <script charset="utf-8" src="//js.hscta.net/cta/current.js"></script> <script type="text/javascript"> hbspt.cta.load(158015, 'ccd39b7c-ae18-4c4e-98ee-547069bfbc5b'); </script> </span> <!-- end HubSpot Call-to-Action Code --> </span>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`embed_code`

 | String | 

The embed code for the CTA. \\n differentiates line breaks.

 |
| 

`full_html`

 | String | 

The embed code for the CTA (Same as embed\_code). \\n differentiates line breaks.

 |
| 

`image_src`

 | String | 

Image src url that defines the preview image in the content editor.

 |
| 

`image_editor`

 | String | 

Markup for the image editor preview

 |
| 

`guid`

 | String | 

The unique ID number of the CTA. This ID number is available in the URL of the Details screen of a particular CTA. This parameter is used to choose which CTA to display by default.

 |
| 

`image_html`

 | String | 

CTA image HTML without the CTA script.\*

 |
| 

`image_email`

 | String | 

Email-friendly version of the CTA code.\*

 |

\*While these parameters are included here for the sake of being comprehensive, the code generated by HubSpot to populate them is very specific. If you need a default CTA selected, rather than trying to develop the CTA parameters from scratch, it is recommended that set up the CTA on a template layout, and then [clone to file](https://knowledge.hubspot.com/cos-general/how-do-i-clone-my-blog-email-page-template). You can then copy the HubL CTA module of the CTA with all parameters set correctly for you.  
  
There is also a [CTA function](/docs/cms/hubl/functions#cta) that generates a CTA from the ID.

Custom HTML[](https://developers.hubspot.com/docs/cms/hubl/tags#custom-html)
----------------------------------------------------------------------------

A custom HTML module allows users to enter raw HTML into the content editor. If you need to add extensive default HTML to the tag, you may want to use [block syntax](/docs/cms/building-blocks/modules/using-modules-in-templates#block-syntax).

{% raw\_html "raw\_html" %} {% raw\_html "my\_custom\_html\_module" label="Enter HTML here" value="<div>My HTML Block</div>" %} Block Syntax Example: {% widget\_block raw\_html "my\_custom\_html\_module" overrideable=True, label="My custom HTML module" %} {% widget\_attribute "value" %} <div>Default HTML block</div> {% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_my\_custom\_html\_module" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_raw\_html" style="" data-hs-cos-general-type="widget" data-hs-cos-type="raw\_html"> <div>My HTML block</div> </span>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`value`

 | String | 

Sets the default content HTML of the module.

 |

Custom modules[](https://developers.hubspot.com/docs/cms/hubl/tags#custom-modules)
----------------------------------------------------------------------------------

Custom Modules allow HubSpot designers to create a custom group of editable content objects to be used across templates and pages on HubSpot’s CMS, while still allowing marketers to control the specific content appearing within those modules on a page-by-page basis. You can learn more about [custom modules and their simplified HubL syntax, here](/docs/cms/building-blocks/modules).  
  
Custom modules must be built in the Custom Module editor, but they can be included into coded templates and HubL modules. You will see a 'Usage Snippet' in the right sidebar of the Custom Module editor under 'Template Usage'.  
  
Custom modules require the ID of the module as a string as well as a path parameter in order to specify which module to load. The usage snippet will also include a label parameter. See the syntax below:

{% module "module\_15677217712485" path="/Custom/Test custom module" %} {% module "module\_25642219712432" path="/Assets/Custom calendar module" label="Custom calendar module" %}<div id="hs\_cos\_wrapper\_module\_15677217712485" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">content!</div> <style> @import "//cdn2.hubspotqa.net/qa/hub/126/file-613025667-css/custom\_widget\_example.css" </style> <div> <img class="persons-photo" src="//cdn2.hubspotqa.net/qa/hub/124/file-1360297556-jpeg/dharmesh.jpeg" alt="dharmesh.jpeg"> <div> <img class="company-logo with-background" src="//cdn2.hubspotqa.net/qa/hub/124/file-221882251-png/HubSpot\_Logo\_2x.png" width="60px" height="inherit" alt="HubSpot\_Logo\_2x.png"> </div> </div> <div> <p class="quote"> <span class="quotation-mark"><b>" </b></span>The Content Optimization System matches content with context to create a highly personalized, relevant and meaningful customer experience. <span class="quotation-mark"><b>" </b></span> </p> </div> <div class="name-and-company"> <span><b>Dharmesh Shah,</b></span> <span>HubSpot</span> </div>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`module_id`

 | String | 

The id of the module to render.

 |
| 

`path`

 | String | 

The path of the module to render. Include leading slash for absolute path, otherwise path is relative to template. Reference HubSpot default modules with paths corresponding to their HubL tags such as @hubspot/rich\_text, @hubspot/linked\_image, etc.

 |

Editor placeholders[](https://developers.hubspot.com/docs/cms/hubl/tags#editor-placeholders)
--------------------------------------------------------------------------------------------

When building a module, you can add either default content  to your fields or an `editor_placeholder` HubL tag to the HTML + HubL file to render placeholder content. This tag renders the module's icon and name as empty placeholders in the editor.

![module-placeholder-content0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/module-placeholder-content0.png?width=899&name=module-placeholder-content0.png)

This tag can be useful when the module doesn't have or need default content, or to streamline module building.

To add a placeholder to a custom module, you can add an [if statement](/docs/cms/hubl/if-statements) to the HTML + HubL file to render the placeholder when there's no content selected. For example:

{% if module.cta\_field.name %} {% cta guid="{{ module.cta\_field }}" %} {% elif is\_in\_editor %} {% editor\_placeholder %} {% endif %}

While you cannot edit the placeholder's styling, you can add the following properties to the module's `meta.json` file to customize its content:

| Parameter | Type | Description |
| --- | --- | --- |
| 
`show_module_icon`

 | Boolean | 

Whether to display the module's icon.

 |
| 

`title`

 | String | 

The title that appears in the placeholder.

 |
| 

`description`

 | String | 

The description that appears in the placeholder.

 |

For example, your `meta.json` file might look like the following:

// Module meta.json { "global" : false, "host\_template\_types" : \[ "PAGE" \], "module\_id" : 62170380654, "is\_available\_for\_new\_content" : true, "placeholder": { "show\_module\_icon": true, "title": "Call to action", "description": "Select a CTA" } }

Flexible column[](https://developers.hubspot.com/docs/cms/hubl/tags#flexible-column)
------------------------------------------------------------------------------------

Flexible columns are vertical columns in a template that enable content creators to insert and remove modules to the page using the [content editor](https://knowledge.hubspot.com/cos-pages-editor/how-to-use-flexible-columns-in-your-pages). When coding a flexible column with HubL, you can choose to wrap other HubL modules to make them appear in the flexible column by default. The sample code below shows the basic syntax and a sample flexible column with a rich text and form module contained as default content.

Please note that flexible columns can only be added to page templates, not blog or email templates. Modules cannot contain flexible columns, but they can instead contain [repeatable fields and groups](/docs/cms/building-blocks/module-theme-fields#repeaters), which provide a similar functionality. 

{% widget\_container "my\_flexible\_column" label="My flex column"%} {% module "rich\_text" path="@hubspot/rich\_text" %} {% module "linked\_image" path="@hubspot/linked\_image" %} {% end\_widget\_container %}<span id="hs\_cos\_wrapper\_my\_flexible\_column" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget\_container hs\_cos\_wrapper\_type\_widget\_container" style="" data-hs-cos-general-type="widget\_container" data-hs-cos-type="widget\_container"><div id="hs\_cos\_wrapper\_rich\_text" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module"><span id="hs\_cos\_wrapper\_rich\_text\_" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_rich\_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rich\_text"><h2>Something Powerful</h2> <h3>Tell The Reader More</h3> <p>The headline and subheader tells us what you're <a href="#">offering</a>, and the form header closes the deal. Over here you can explain why your offer is so great it's worth filling out a form for.</p> <p>Remember:</p> <ul> <li>Bullets are great</li> <li>For spelling out <a href="#">benefits</a> and</li> <li>Turning visitors into leads.</li> </ul></span></div> <div id="hs\_cos\_wrapper\_linked\_image" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module"> <span id="hs\_cos\_wrapper\_linked\_image\_" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_linked\_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked\_image"><img src="https://static.hubspot.com/final/img/content/email-template-images/placeholder\_200x200.png" class="hs-image-widget " style="width:200px;border-width:0px;border:0px;" width="200" alt="placeholder\_200x200" title="placeholder\_200x200"></span> </div></span>

**Please note:** when using this tag, the `label` must follow the `name` value for the flexible column to function in the content editor. For example, the following syntax is invalid:

`[% widget_container label="My label" "my_flexible_column" %}`

Form[](https://developers.hubspot.com/docs/cms/hubl/tags#form)
--------------------------------------------------------------

Allows users to select a HubSpot form to add to their page.

{% form "form" %} {% form "my\_form" form\_to\_use="08bd9f0d-3be9-41c2-93b6-231a3a71b143", title="Free Trial" %} Block Syntax Example: {% widget\_block form "my\_form" form\_follow\_ups\_follow\_up\_type="", response\_redirect\_id=306590405, form\_to\_use="08bd9f0d-3be9-41c2-93b6-231a3a71b143", title="Free Trial", notifications\_are\_overridden=True, sfdc\_campaign="", response\_message="Thanks for submitting the form.", response\_response\_type="redirect", response\_redirect\_url="", overrideable=True, gotowebinar\_webinar\_key="", response\_redirect\_name="Homepage (http://www.hubspot.com/)", label="Form", response={message="Thank you for submitting the form.", redirect\_url=""} %} {% widget\_attribute "notifications\_override\_email\_addresses" is\_json=True %}\["noreply@hubspot.com"\]{% end\_widget\_attribute %} {% end\_widget\_block %}<div id="hs\_cos\_wrapper\_my\_form" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_form" style="" data-hs-cos-general-type="widget" data-hs-cos-type="form"> <h3 id="hs\_cos\_wrapper\_module\_13885064832664947\_title" class="hs\_cos\_wrapper form-title" data-hs-cos-general-type="widget\_field" data-hs-cos-type="text">Free Trial</h3> <div id="hs\_form\_target\_module\_13885064832664947"> <form accept-charset="UTF-8" enctype="multipart/form-data" id="hsForm\_08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756" class="hs-form stacked hs-custom-form" action="https://forms.hubspot.com/uploads/form/v2/158015/08bd9f0d-3be9-41c2-93b6-231a3a71b143" method="POST" novalidate="novalidate"> <div class="hs\_lastname field hs-form-field"> <label placeholder="Enter your Last Name" for="lastname-08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756">Last Name</label> <div class="hs-field-desc" style="display: none;"></div> <div class="input"> <input class="hs-input" type="text" id="lastname-08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756" name="lastname" value="" placeholder=""> </div> </div> <div class="hs\_firstname field hs-form-field"> <label placeholder="Enter your First Name" for="firstname-08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756">First Name</label> <div class="hs-field-desc" style="display: none;"></div> <div class="input"> <input class="hs-input" type="text" id="firstname-08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756" name="firstname" value="" placeholder=""> </div> </div> <div class="hs\_email field hs-form-field"> <label placeholder="Enter your Email" for="email-08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756">Email<span class="hs-form-required"> \* </span></label> <div class="hs-field-desc" style="display: none;"></div> <div class="input"> <input class="hs-input" type="email" required="required" id="email-08bd9f0d-3be9-41c2-93b6-231a3a71b143\_6756" name="email" value="" placeholder=""> </div> </div> <div class="hs\_submit"> <div class="hs-field-desc" style="display: none;"></div> <div class="actions"> <input class="hs-button primary large" type="submit" value="Submit"> </div> </div> </form> </div> <script charset="utf-8" src="//js.hsforms.net/forms/current.js"></script> <script> hbspt.forms.create({ portalId: '158015', formId: '08bd9f0d-3be9-41c2-93b6-231a3a71b143', formInstanceId: '6756', pageId: 1, redirectUrl: "http:\\/\\/www.davidjosephhunt.com\\/404", deactivateSmartForm: true, css: '', target: '#hs\_form\_target\_module\_13885064832664947', contentType: "landing-page", formData: { cssClass: 'hs-form stacked hs-custom-form' } }); </script> </div>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`form_key`

 | String | 

Specifies a unique id for the form at the page level.

 |  |
| 

`form_to_use`

 | String | 

Specifies which form to load by default, based on the Form ID. This ID is available in the form editor URL of a each form.

 |  |
| 

`title`

 | String | 

Populates an h3 header tag above the form.

 |  |
| 

`no_title`

 | Boolean | 

 If `True`, the h3 tag above the title is removed.

 | `False` |
| 

`form_follow_ups_follow_up_type`

 | Enumeration | 

Specifies follow up actions such as enrolling a contact into a workflow or sending a simple follow up email. Possible values include: `no_action`, `simple`, and `automation`.

 |  |
| 

`simple_email_for_live_id`

 | Number | 

Specifies the ID of the simple follow-up email for the live page.

 |  |
| 

`simple_email_for_buffer_id`

 | Number | 

Specifies the ID of the simple follow-up email for the auto-save version of a page.

 |  |
| 

`follow_up_type_simple`

 | Boolean | 

If true, enables a simple follow-up email. Alternative to `form_follow_ups_follow_up_type`.

 |  |
| 

`follow_up_type_automation`

 | Boolean | 

If true, enrolls submissions in a workflow. Alternative to `form_follow_ups_follow_up_type`.

 |  |
| 

`simple_email_campaign_id`

 | Number | 

Specifies the ID of the simple follow-up email. Alternative to `simple_email_for_live_id`.

 |  |
| 

`form_follow_ups_workflow_id`

 | Number | 

Specifies the ID of the workflow in which to enroll submissions.

 |  |
| 

`response_redirect_url`

 | String | 

If redirecting to an external page, this parameter specifies the URL to redirect to.

 |  |
| 

`response_redirect_id`

 | Number | 

If redirecting to HubSpot hosted page, this parameter specifies the page ID of that page. The page ID is available in the page editor URL of each page.

 |  |
| 

`response_response_type`

 | Enumeration | 

Determines whether to redirect to another page or to display an inline thank you message on submission. The value of this parameter should either be `"redirect"` or `"inline"`.

 | `inline` |
| 

`response_message`

 | String | 

Sets an inline thank you message. This parameter supports HTML.

 |  |
| 

`notifications_are_overridden`

 | Boolean | 

If True, the form will send form notifications to specified email addresses selected in the `notifications_override_email_addresses`  
parameter, instead of the form defaults

 | `False` |
| 

`notifications_override_guid_buffer`

 | String | 

ID of override settings in auto-save version of page.

 |  |
| 

`notifications_override_guid`

 | String | 

ID of override settings in live version of page.

 |  |
| 

`notifications_override_email_addresses`

 | JSON | 

Block syntax supports a JSON list of email recipients that will be notified upon form submission. These email addresses will override the email notification settings set in the form.

 |  |
| 

`gotowebinar_webinar_key`

 | String | 

Specifies the GoToWebinar webinar to enroll contacts who submit the form into. Only available for portals using the [GoToWebinar integration](https://knowledge.hubspot.com/integrations/use-the-gotowebinar-integration-with-hubspot).

 |  |
| 

`sfdc_campaign`

 | String | 

Specifies the Salesforce campaign to enroll contacts who submit the form into. This parameter's value should be the SFDC campaign ID and is only available for portals that are [integrated with Salesforce](https://knowledge.hubspot.com/salesforce/install-the-hubspot-salesforce-integration).

 |  |

Footer[](https://developers.hubspot.com/docs/cms/hubl/tags#footer)
------------------------------------------------------------------

Renders copyright information with the year and company name specified in Content Settings (Email > Footer Information).

{% page\_footer "page\_footer" %}<span id="hs\_cos\_wrapper\_page\_footer" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_page\_footer" style="" data-hs-cos-general-type="widget" data-hs-cos-type="page\_footer"> <footer> <span class="hs-footer-company-copyright">© 2020 HubSpot</span> </footer> </span>

Gallery[](https://developers.hubspot.com/docs/cms/hubl/tags#gallery)
--------------------------------------------------------------------

Generates a HubSpot gallery tag. This gallery tag is based on [Slick](http://kenwheeler.github.io/slick/). While you can create a gallery module with standard module HubL syntax, If you want to predefine default slides using HubL, you must use block syntax. Both methods are shown below. Gallery images are lazy loaded using JavaScript.

{% gallery "crm\_gallery" %} <-- Block syntax --> {% widget\_block gallery "Gallery" display\_mode="standard" sizing="static", transition="slide", caption\_position="below", auto\_advance=True, overrideable=True, description\_text="", show\_pagination=True, label="Gallery", loop\_slides=True, num\_seconds=5 %} {% widget\_attribute "slides" is\_json=True %} \[{ "caption": "CRM Contacts App", "show\_caption": true, "link\_url": "http://www.hubspot.com/crm", "alt\_text": "Screenshot of CRM Contacts", "img\_src": "http://go.hubspot.com/hubfs/Contacts-View-1.png?t=1430860504240", "open\_in\_new\_tab": true }, { "caption": "HubSpot CRM Contact Profile", "show\_caption": true, "link\_url": "http://www.hubspot.com/", "alt\_text": "HubSpot CRM Contact Profile", "img\_src": "http://cdn2.hubspot.net/hubfs/53/Contact-Profile.png?t=1430860504240", "open\_in\_new\_tab": true }\] {% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_crm\_gallery" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_gallery" style="" data-hs-cos-general-type="widget" data-hs-cos-type="gallery"> <div id="hs\_cos\_flex\_gallery\_crm\_gallery" class="hs\_cos\_flex-gallery flex-gallery-main gallery-mode-gallery"> <div class="hs\_cos\_flex-viewport" style="overflow: hidden; position: relative;"> <ul class="hs\_cos\_flex-slides hs\_cos\_flex-slides-main " style="width: 800%; -webkit-transition-duration: 0s; transition-duration: 0s; -webkit-transform: translate3d(-1090px, 0px, 0px);"> <li class="hs\_cos\_flex-slide-main clone" aria-hidden="true" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/" target="\_blank"><img src="//cdn2.hubspot.net/hubfs/53/Contact-Profile.png?t=1430860504240&t=1430335520686" alt="HubSpot CRM Contact Profile" draggable="false"></a> <div class="caption"> HubSpot CRM Contact Profile </div> </li> <li class="hs\_cos\_flex-slide-main hs\_cos\_flex-active-slide" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/crm" target="\_blank"><img src="http://go.hubspot.com/hubfs/Contacts-View-1.png?t=1430860504240&t=1430335520686" alt="Screenshot of CRM Contacts" draggable="false"></a> <div class="caption"> CRM Contacts App </div> </li> <li class="hs\_cos\_flex-slide-main" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/" target="\_blank"><img src="//cdn2.hubspot.net/hubfs/53/Contact-Profile.png?t=1430860504240&t=1430335520686" alt="HubSpot CRM Contact Profile" draggable="false"></a> <div class="caption"> HubSpot CRM Contact Profile </div> </li> <li class="hs\_cos\_flex-slide-main clone" aria-hidden="true" style="width: 1090px; float: left; display: block;"> <a href="//www.hubspot.com/crm" target="\_blank"><img src="http://go.hubspot.com/hubfs/Contacts-View-1.png?t=1430860504240&t=1430335520686" alt="Screenshot of CRM Contacts" draggable="false"></a> <div class="caption"> CRM Contacts App </div> </li> </ul> </div> <ol class="hs\_cos\_flex-control-nav hs\_cos\_flex-control-paging"> <li><a class="hs\_cos\_flex-active">1</a></li> <li><a class="">2</a></li> </ol> <ul class="hs\_cos\_flex-direction-nav"> <li><a class="hs\_cos\_flex-prev" href="#">Previous</a></li> <li><a class="hs\_cos\_flex-next" href="#">Next</a></li> </ul> </div> <script> window.hsSliderConfig = window.hsSliderConfig || {}; window.hsSliderConfig\['crm\_gallery'\] = { mode: 'gallery', mainConfig: { "animationLoop": true, "direction": "horizontal", "slideshowSpeed": 5000.0, "controlNav": true, "smoothHeight": false, "namespace": "hs\_cos\_flex-", "slideshow": true, "selector": ".hs\_cos\_flex-slides > li", "animation": "slide" } }; </script>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`slides`

 | JSON | 

A JSON list of the default caption, the link url, the alt text, the image src, and whether to open in a new tab. See block syntax above.

 |  |
| 

`loop_slides`

 | Boolean | 

When True, continuously loop through slides.

 | `True` |
| 

`num_seconds`

 | Number | 

Time in seconds to pause between slides.

 | `5` |
| 

`show_pagination`

 | Boolean | 

Provide buttons below slider to navigate among slides.

 | `True` |
| 

`sizing`

 | Enumeration | 

Determines whether the slider changes sizes, based on the height of the slides. Possible values include: "static" or "resize".

 | `"static"` |
| 

`auto_advance`

 | Boolean | 

Automatically advance slides after the time set in num\_seconds.

 | `False` |
| 

`transition`

 | Enumeration | 

Sets the type of slide transition. Possible values include: "fade" or "slide".

 | `"slide"` |
| 

`caption_position`

 | Enumeration | 

Affects positioning of caption on or below the slide. Possible values include "below" or "superimpose".

 | `"below"` |
| 

`display_mode`

 | Enumeration | 

Determines how the image gallery will be displayed. Possible values include: "standard", "lightbox", "thumbnail".

 | `"standard"` |
| 

`lightboxRows`

 | Number | 

If "display\_mode" is set to "lightbox", this parameter will control the number of rows displayed within the lightbox.

 | `3` |

Header[](https://developers.hubspot.com/docs/cms/hubl/tags#header)
------------------------------------------------------------------

Generates a header module that will render text as an h1-h6 tag.

{% header "header" %} {% header "my\_header" header\_tag="h1", overrideable=True, value="A clear and bold header", label="Header" %}<span id="hs\_cos\_wrapper\_my\_header" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_header" style="" data-hs-cos-general-type="widget" data-hs-cos-type="header"> <h1>A clear and bold header</h1> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header_tag`

 | String | 

Select which heading tag to render. Possible values include: h1, h2, h3, h4, h5, h6.

 | `h1` |
| 

`value`

 | String | 

Renders default text within the heading module.

 | `"A clear bold header"` |

Icon[](https://developers.hubspot.com/docs/cms/hubl/tags#icon)
--------------------------------------------------------------

Adds an icon tag that allows users to select and icon for use. Supported icons sets are FontAwesome [5.0.10](https://github.com/FortAwesome/Font-Awesome/releases/tag/5.0.10), [5.14.0](https://github.com/FortAwesome/Font-Awesome/releases/tag/5.14.0), and [6.4.2](https://github.com/FortAwesome/Font-Awesome/releases/tag/6.4.2).

This tag cannot be used in modules enabled for email.

{% icon name="Accessible Icon" style="REGULAR" unicode="f368" icon\_set="fontawesome-5.14.0" purpose="decorative" title="Accessible Icon" %}<span id="hs\_cos\_wrapper\_module\_42549274798\_" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_icon" style="" data-hs-cos-general-type="widget" data-hs-cos-type="icon"> <svg version="1.0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" aria-hidden="true"> <g id="layer1"> <path d="M423.9 255.8L411 413.1c-3.3 40.7-63.9 35.1-60.6-4.9l10-122.5-41.1 2.3c10.1 20.7 15.8 43.9 15.8 68.5 0 41.2-16.1 78.7-42.3 106.5l-39.3-39.3c57.9-63.7 13.1-167.2-74-167.2-25.9 0-49.5 9.9-67.2 26L73 243.2c22-20.7 50.1-35.1 81.4-40.2l75.3-85.7-42.6-24.8-51.6 46c-30 26.8-70.6-18.5-40.5-45.4l68-60.7c9.8-8.8 24.1-10.2 35.5-3.6 0 0 139.3 80.9 139.5 81.1 16.2 10.1 20.7 36 6.1 52.6L285.7 229l106.1-5.9c18.5-1.1 33.6 14.4 32.1 32.7zm-64.9-154c28.1 0 50.9-22.8 50.9-50.9C409.9 22.8 387.1 0 359 0c-28.1 0-50.9 22.8-50.9 50.9 0 28.1 22.8 50.9 50.9 50.9zM179.6 456.5c-80.6 0-127.4-90.6-82.7-156.1l-39.7-39.7C36.4 287 24 320.3 24 356.4c0 130.7 150.7 201.4 251.4 122.5l-39.7-39.7c-16 10.9-35.3 17.3-56.1 17.3z"></path> </g> </svg> </span>

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`name`

 | String | 

Name of the icon.

 |  |
| 

`style`

 | String | 

Style of the icon. Possible values: `REGULAR` or `SOLID`

 | `REGULAR` |
| 

`unicode`

 | String | 

The Unicode character representation of the icon.

 |  |
| 

`icon_set`

 | String | 

The FontAwesome icon set to use. Possible values are:

*   `fontawesome-5.14.0` 
*   `fontawesome-5.0.10`
*   `fontawesome-6.4.2`

 |  |
| 

`purpose`

 | String | 

The purpose of the icon, used for [accessibility](https://fontawesome.com/v5.15/how-to-use/on-the-web/other-topics/accessibility). Possible values are `decorative` or `semantic`. If set to `decorative`, an additional attribute of `aria-hidden="true"` will be added to the icon.

 | `decorative` |
| 

`title`

 | String | 

The title element of the icon's svg, along with a  `labelledby` attribute that points to the title.

 |  |

Image[](https://developers.hubspot.com/docs/cms/hubl/tags#image)
----------------------------------------------------------------

Creates a image tag that allows users to select an image from the content editor. If you want the image to be linked to a destination URL, you should use linked\_image below.

{% image "image" %} {% image "executive\_image" label="Executive photo", alt="Photo of Brian Halligan", src="//cdn2.hubspot.net/hub/53/file-733888619-jpg/assets/hubspot.com/about/management/brian-home.jpg", width="300" %}<span id="hs\_cos\_wrapper\_executive\_image" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="image"> <img src="//cdn2.hubspot.net/hub/53/file-733888619-jpg/assets/hubspot.com/about/management/brian-home.jpg?width=300" class="hs-image-widget " width="300" alt="Photo of Brian Halligan" title="Photo of Brian Halligan"> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`alt`

 | String | 

Sets the default alt text for the image.

 |  |
| 

`src`

 | String | 

Populates the src attribute of the img tag.

 |  |
| 

`width`

 | Number | 

Sets the width attribute of the img tag.

 | `The width of the image` |
| 

`height`

 | Number | 

Sets a min-height in a style attribute of the img tag **for email templates only**.

 | `The height of the image` |
| 

`hspace`

 | Number | 

Sets the hspace attribute of the img tag.

 |  |
| 

`align`

 | String | 

Sets the align attribute of the img tag. Possible values include: left, right, & center.

 |  |
| 

`style`

 | String | 

Adds inline CSS declarations to the img tag. For example style="border:1px solid blue; margin:10px"

 |  |
| 

`loading`

 | String | 

Controls img element loading attribute. [Used for browser based lazy loading.](/docs/cms/guides/speed/lazy-loading)

 |  |

Image src[](https://developers.hubspot.com/docs/cms/hubl/tags#image-src)
------------------------------------------------------------------------

An image src module creates a image selector in the content editor, but rather than printing a img tag, it renders the URL of the image. This tag is generally used with `no_wrapper=True` parameter, so that the image src can be added to inline CSS or other markup. An alternative to using this tag is to use the [`export_to_template_context`](/docs/cms/building-blocks/modules/export-to-template-context) parameter.

{% image\_src "image\_src" %} {% image\_src "executve\_image\_src" src="//cdn2.hubspot.net/hub/53/file-733888614-jpg/assets/hubspot.com/about/management/dharmesh-home.jpg", no\_wrapper=True %}//cdn2.hubspot.net/hub/53/file-733888614-jpg/assets/hubspot.com/about/management/dharmesh-home.jpg

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`src`

 | String | 

 Specifies the default URL image src.

 |  |

Language switcher[](https://developers.hubspot.com/docs/cms/hubl/tags#language-switcher)
----------------------------------------------------------------------------------------

Adds a Globe Icon with links to the translated versions of a given CMS page. Learn more about [multi-language content here](https://knowledge.hubspot.com/cos-general/how-to-manage-multi-language-content-with-hubspots-cos).

{% language\_switcher "language\_switcher" overrideable=false, display\_mode="localized", label="Language Switcher" %}<span id="hs\_cos\_wrapper\_module\_1487954976079503" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_language\_switcher" style="" data-hs-cos-general-type="widget" data-hs-cos-type="language\_switcher"> <div class="lang\_switcher\_class"> <div class="globe\_class"> <ul class="lang\_list\_class"> <li> <a class="lang\_switcher\_link" href="http://www.hubspot.com">English</a> </li> <li> <a class="lang\_switcher\_link" href="http://www.hubspot.com/es">Spanish</a> </li> </ul> </div> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`display_mode`

 | Enumeration | 

The language of the text in the language switcher. Values are:

*   `Pagelang` means the names of languages will display in the language of the page the switcher is on.
*   `Localized` means the name of each language will display in that language.
*   `Hybrid` is a combination of the two.

 | `Localized` |

Linked image[](https://developers.hubspot.com/docs/cms/hubl/tags#linked-image)
------------------------------------------------------------------------------

Creates a user-selectable image that is wrapped in a link. This module has all of the parameters of an image module with two additional parameters that specify the link destination URL and whether the link opens in a new window.

{% linked\_image "linked\_image" %} {% linked\_image "executive\_image" label="Executive photo", link="https://twitter.com/bhalligan", \\ open\_in\_new\_tab=True, alt="Photo of Brian Halligan", src="//cdn2.hubspot.net/hub/53/file-733888619-jpg/assets/hubspot.com/about/management/brian-home.jpg", width="300" %}<span id="hs\_cos\_wrapper\_executive\_image" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_linked\_image" style="" data-hs-cos-general-type="widget" data-hs-cos-type="linked\_image"> <a href="https://twitter.com/bhalligan" target="\_blank" id="hs-link-executive\_image" style="border-width:0px;border:0px;"> <img src="//cdn2.hubspot.net/hub/53/file-733888619-jpg/assets/hubspot.com/about/management/brian-home.jpg?width=300" class="hs-image-widget " style="width:300px;border-width:0px;border:0px;" width="300" alt="Photo of Brian Halligan" title="Photo of Brian Halligan"> </a> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`alt`

 | String | 

Sets the default alt text for the image.

 |  |
| 

`src`

 | String | 

Populates the src attribute of the img tag.

 |  |
| 

`width`

 | Number | 

Sets the width attribute of the img tag.

 | `The width of the image` |
| 

`height`

 | Number | 

Sets a min-height in a style attribute of the img tag for **email templates only.**

 | `The height of the image` |
| 

`hspace`

 | Number | 

Sets the hspace attribute of the img tag.

 |  |
| 

`align`

 | String | 

Sets the align attribute of the img tag. Possible values include: left, right, & center.

 |  |
| 

`style`

 | String | 

Adds inline CSS declarations to the img tag. For example style="border:1px solid blue; margin:10px"

 |  |
| 

`open_in_new_tab`

 | Boolean | 

Selects whether or not to open the destination URL in another tab.

 | `False` |
| 

`link`

 | String | 

Sets the destination URL of the link that wraps the img tag.

 |  |
| 

`target`

 | String | 

Sets the target attribute of the link tag.

 |  |
| 

`loading`

 | String | 

Controls img element loading attribute. [Used for browser based lazy loading.](/docs/cms/guides/speed/lazy-loading)

 |  |

Logo[](https://developers.hubspot.com/docs/cms/hubl/tags#logo)
--------------------------------------------------------------

A logo module renders your company's logo image from Content Settings.

{% logo "logo" %} {% logo "my\_logo" width="200" %}<span id="hs\_cos\_wrapper\_my\_logo" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_logo" style="" data-hs-cos-general-type="widget" data-hs-cos-type="logo"> <a href="//www.hubspot.com" id="hs-link-my\_logo"> <img src="//cdn2.hubspot.net/hub/53/file-1237149549-png/assets/hubspot.com/V2-Global/hubspot-logo-dark.png?t=1430948896766&amp;width=200" class="hs-image-widget " width="200" alt="HubSpot logo" title="HubSpo logot"> </a> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`suppress_company_name`

 | Boolean | 

Hides company name if an image logo isn't set.

 | `False` |
| 

`alt`

 | String | 

Sets the default alt text for the image.

 | `Value in Content Settings` |
| 

`src`

 | String | 

Populates the src attribute of the img tag.

 | `Value in Content Settings` |
| 

`width`

 | Number | 

Sets the width attribute of the img tag.

 | `The width of the image` |
| 

`height`

 | Number | 

Sets a min-height in a style attribute of the img tag for **email templates only.**

 | `The height of the image` |
| 

`hspace`

 | Number | 

Sets the hspace attribute of the img tag.

 |  |
| 

`align`

 | String | 

Sets the align attribute of the img tag. Possible values include: left, right, & center.

 |  |
| 

`style`

 | String | 

Adds inline CSS declarations to the img tag. For example style="border:1px solid blue; margin:10px"

 |  |
| 

`open_in_new_tab`

 | Boolean | 

Selects whether or not to open the destination URL in another tab.

 | `False` |
| 

`link`

 | String | 

Sets the destination URL of the link that wraps the img tag.

 |  |
| 

`override_inherited_src`

 | Boolean | 

If true, use src from logo widget rather than src inherited from settings or template.

 | `True` |
| 

`heading_level`

 | String | 

When using non-linked text-based logos, this wraps the text-based logo in one of the following available options as an HTML tag: `h1`, `h2`, `h3`, `h4`. 

 | `h1` |
| 

`loading`

 | String | 

Controls img element loading attribute. [Used for browser based lazy loading.](/docs/cms/guides/speed/lazy-loading)

 |  |

Menu[](https://developers.hubspot.com/docs/cms/hubl/tags#menu)
--------------------------------------------------------------

Generates an advanced menu based on a menu tree in **Content Settings > Advanced Menus.**  See [menus and navigation](/docs/cms/building-blocks/menus-and-navigation) for more information on using menus in [templates](/docs/cms/building-blocks/templates) and [modules](/docs/cms/building-blocks/modules). If `id` is set to `null` the menu tag will render the default menu for the HubSpot account.

{% menu "menu" %} {% menu "my\_menu" id=456, site\_map\_name="Default", overrideable=False, root\_type="site\_root", flyouts="true", max\_levels="2", flow="horizontal", label="Advanced Menu" %}<div id="hs\_menu\_wrapper\_my\_menu" class="hs-menu-wrapper active-branch flyouts hs-menu-flow-horizontal" data-sitemap-name="Default"> <ul> <li class="hs-menu-item hs-menu-depth-1"><a href="http://www.husbpot.com/Software">Software</a></li> <li class="hs-menu-item hs-menu-depth-1"><a href="http://www.hubspot.com/pricing">Pricing</a></li> <li class="hs-menu-item hs-menu-depth-1"><a href="http://www.hubspot.com/resources">Resources</a></li> <li class="hs-menu-item hs-menu-depth-1"><a href="http://www.hubspot.com/contact">Contact</a></li> </ul> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`id`

 | Number | 

ID of Menu Tree from Advanced Menus in Content Settings.

 |  |
| 

`site_map_name`

 | String | 

Name of Menu Tree from Advanced Menus in Content Settings.

 | `"default"` |
| 

`root_type`

 | Enumeration | 

Specifies the type of advanced menus. Options include: "site\_root", "top\_parent", "parent", "page\_name", "page\_id", and "breadcrumb". These values correspond to static, dynamic by section, dynamic by page, and breadcrumb.

 | `"site_root"` |
| 

`flyouts`

 | String | 

When true, a class is added to the menu tree that can be styled to allow child menu items will appear when you hover over the parent. When false, child menu items will always appear.

 | `"true"` |
| 

`max_levels`

 | Number | 

Determines how many levels of nested menus render in the markup. This parameter dictates number of menu tree children that can be expanded in the menu.

 | `2` |
| 

`flow`

 | Enumeration | 

Sets orientation of menu items. This adds classes to menu tree, so that they can be styled accordingly. Possible values include "horizontal", "vertical" or "vertical\_flyouts". Horizontal menus display items side-by-side, and vertical menus are top-to-bottom.

 | `"horizontal"` |
| 

`root_key`

 | String | 

Used to find the menu root. When root\_type is set to page\_id or page\_name, this param should be the page ID or the label of the page, respectively.

 | `"horizontal"` |
| 

`label`

 | String | 

Some rich content to describe this entity

 | `False` |
| 

`label`

 | String | 

Some rich content to describe this entity

 | `False` |

Require\_css[](https://developers.hubspot.com/docs/cms/hubl/tags#require-css)
-----------------------------------------------------------------------------

A HubL tag that enqueues a style element to be rendered in the `<head>`.

This tag is similar to the [require\_css function](/docs/cms/hubl/functions#require-css), except that this tag inserts styling inline rather than from a stylesheet. This tag also does not deduplicate against other instances of the CSS on the same page. If you're building a module and want to insert a stylesheet, but you might use that module multiple times on a single page, you may want to use the `require_css` function instead. 

{{ standard\_header\_includes }} <!-- more html --> {% require\_css %} <style> body { color: red; } </style> {% end\_require\_css %} {{ standard\_footer\_includes }}<!-- other standard header html --> <style> body { color: red; } </style> <!-- more html --> <!-- other standard footer html -->

Require\_head[](https://developers.hubspot.com/docs/cms/hubl/tags#require-head)
-------------------------------------------------------------------------------

A HubL tag that enqueues anything placed inside of it into the `standard_header_includes` which is in the template's  `<head>`. For most Javascript and CSS see `require_js` and `require_css`.  Some use-cases for `require_head` include supplying meta tags, and special link tags (like prefetch and preconnect) from modules.

{% require\_head %} <meta name="third-party-app-verification-id" content="123456"> <link rel="prefetch" href="http://example.com/large-script.js"> <!-- these are purely examples, you could add anything that requires being in the head. require\_css and require\_js should be used instead of this when embedding a style tag or script tag.--> {% end\_require\_head %}

Require\_js[](https://developers.hubspot.com/docs/cms/hubl/tags#require-js)
---------------------------------------------------------------------------

A HubL tag that enqueues a script element to be rendered. To enqueue a script to render in the `<head />`from a different file via a `<script />` element (as opposed to inline as shown here), use the HubL function [require\_js(absolute\_url)](/docs/cms/hubl/functions#require-js) instead.

{{ standard\_header\_includes }} <!-- more html --> {% require\_js position="footer" %} <script> console.log("The CMS is awesome!"); </script> {% end\_require\_js %} {{ standard\_footer\_includes }}<!-- other standard header html --> <!-- more html --> <script> console.log("The CMS is awesome!"); </script> <!-- other standard footer html -->

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`position`

 | String | 

Set the position where the inline script will be rendered. Options include: `"head"` and `"footer"`.

 | `"footer"` |

Rich text[](https://developers.hubspot.com/docs/cms/hubl/tags#rich-text)
------------------------------------------------------------------------

Creates a WYSIWYG content editor.

{% rich\_text "rich\_text" %} {% rich\_text "left\_column" label="Enter HTML here" html="<div>My rich text default content</div>" %} Block Syntax Example: {% widget\_block rich\_text "right\_column" overrideable=True, label="Right Column" %} {% widget\_attribute "html" %} <h2>Something Powerful</h2> <h3>Tell The Reader More</h3> <p>The headline and subheader tells us what you're offering, and the form header closes the deal. Over here you can explain why your offer is so great it's worth filling out a form for.</p> <p>Remember:</p> <ul> <li>Bullets are great</li> <li>For spelling out <a href="#">benefits</a> and</li> <li>Turning visitors into leads.</li> </ul> {% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_right\_column" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_rich\_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rich\_text"> <h2>Something Powerful</h2> <h3>Tell The Reader More</h3> <p>The headline and subheader tells us what you're offering, and the form header closes the deal. Over here you can explain why your offer is so great it's worth filling out a form for.</p> <p>Remember:</p> <ul> <li>Bullets are great</li> <li>For spelling out benefits and</li> <li>Turning visitors into leads.</li> </ul> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`html`

 | String | 

Default rich text content for module.

 | `<h2>Something Powerful</h2> <h3>Tell The Reader More</h3> <p>The headline and subheader tells us what you're offering, and the form header closes the deal. Over here you can explain why your offer is so great it's worth filling out a form for.</p> <p>Remember:</p> <ul> <li>Bullets are great</li> <li>For spelling out <a href="#">benefits</a> and</li> <li>Turning visitors into leads.</li> </ul>` |

RSS listing[](https://developers.hubspot.com/docs/cms/hubl/tags#rss-listing)
----------------------------------------------------------------------------

Loads a list of content from an internal or external RSS feed.

**Please note:** this module loads asynchronously on the client-side. As a result, if you want to manipulate the feed after it's loaded, you'll need to define a global JS function to handle that manipulation. Use the function `hsRssFeedComplete(feeds)`, where `feeds` is the jQuery selector on all feeds that have been completed. You can directly manipulate the DOM object in that function.

{% rss\_listing "rss\_listing" %} {% rss\_listing "my\_rss\_listing" rss\_url="", publish\_date\_text="posted at", feed\_source={rss\_url="", is\_external=False, content\_group\_id="30808594297"}, click\_through\_text="Read more", show\_date=True, include\_featured\_image=True, overrideable=False, publish\_date\_format="short", show\_detail=True, show\_author=True, number\_of\_items="3", is\_external=False, title="", content\_group\_id="24732847", label="RSS Listing", limit\_to\_chars="200", attribution\_text="by" %}<span id="hs\_cos\_wrapper\_module\_70642123068\_my\_rss\_listing" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_rss\_listing" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rss\_listing"> <h3></h3> <div class="hs-rss-module feedreader\_box hs-hash-758735283"> <div class="hs-rss-item "> <div class="hs-rss-item-text"> <a class="hs-rss-title" href="https://developers.hubspot.com/blog/how-to-write-cron-jobs-in-hubspot-to-take-time-based-action-on-crm-data"> <span>How to Write Cron Jobs in HubSpot to take Time Based Action on CRM Data</span> </a> <div class="hs-rss-byline"> by <span class="hs-rss-author">Jon McLaren</span> <span class="hs-rss-posted-at"> posted at</span> <span class="hs-rss-date">3/8/23 10:42 AM</span> </div> <div class="hs-rss-description"> <p>First things first: Cron jobs are scripts that get executed based on time. Understanding where this shorthand name comes from may help you remember this: <a href="https://developers.hubspot.com/blog/how-to-write-cron-jobs-in-hubspot-to-take-time-based-action-on-crm-data">Read more</a> </p> </div> </div> </div> <div class="hs-rss-item "> <div class="hs-rss-item-text"> <a class="hs-rss-title" href="https://developers.hubspot.com/blog/implementing-semantic-search-into-a-hubspot-workflow"> <span>Using OpenAI Embeddings API to implement Semantic Search into a HubSpot Workflow</span> </a> <div class="hs-rss-byline"> by <span class="hs-rss-author">Roman Kozak</span> <span class="hs-rss-posted-at"> posted at</span> <span class="hs-rss-date">3/7/23 2:09 PM</span> </div> <div class="hs-rss-description"> <p>This article was authored by a member of the HubSpot developer community, Roman Kozak. <a href="https://developers.hubspot.com/blog/implementing-semantic-search-into-a-hubspot-workflow">Read more</a> </p> </div> </div> </div> <div class="hs-rss-item "> <div class="hs-rss-item-text"> <a class="hs-rss-title" href="https://developers.hubspot.com/blog/how-to-use-npm-packages-in-custom-code-workflow-actions"> <span>How to Use NPM Packages in Custom Code Workflow Actions</span> </a> <div class="hs-rss-byline"> by <span class="hs-rss-author">Joshua Beatty</span> <span class="hs-rss-posted-at"> posted at</span> <span class="hs-rss-date">2/28/23 10:30 AM</span> </div> <div class="hs-rss-description"> <p>This article was authored by a member of the HubSpot developer community, Joshua Beatty. <a href="https://developers.hubspot.com/blog/how-to-use-npm-packages-in-custom-code-workflow-actions">Read more</a> </p> </div> </div> </div> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`show_title`

 | Boolean | 

 Shows or hides RSS feed title.

 | `True` |
| 

`show_date`

 | Boolean | 

Displays post date.

 | `True` |
| 

`show_author`

 | Boolean | 

Displays author name.

 | `True` |
| 

`show_detail`

 | Boolean | 

Display post summary up to number of characters set by `limit_to_chars` parameter.

 | `True` |
| 

`title`

 | String | 

Populates a heading above the RSS feed listing.

 |  |
| 

`limit_to_chars`

 | Number | 

Maximum number of characters to display in summary.

 | `200` |
| 

`publish_date_format`

 | String | 

Format for the publish date. Possible values include `"short"`, `"medium"` and `"long"`. Also accepts custom formats including `"MMMM d, yyyy 'at' h:mm a"`.

 | `"short"` |
| 

`attribution_text`

 | String | 

The text which attributes an author to a post.

 | `"by"` |
| 

`click_through_text`

 | String | 

The text which will be displayed for the click through link at the end of a post summary.

 | `"Read more"` |
| 

`publish_date_text`

 | String | 

 The text which indicates when a post was published.

 | `"posted at"` |
| 

`include_featured_image`

 | Boolean | 

Displays featured image with post link for HubSpot generated RSS feeds.

 | `False` |
| 

`item_title_tag`

 | String | 

Specifies HTML tag of each post title.

 | `span` |
| 

`is_external`

 | Boolean | 

RSS feed is from an external blog.

 | `False` |
| 

`number_of_items`

 | Number | 

Maximum number of posts to display.

 | `5` |
| 

`publish_date_language`

 | String | 

Specifies the language of the publish date.

 | `en_US` |
| 

`rss_url`

 | String | 

 The URL where the RSS feed is located.

 |  |
| 

`content_group_id`

 | String | 

ID for blog when feed source is internal blog.

 |  |
| 

`select_blog`

 | String | 

Can be used to select an internal HubSpot blog feed.

 | `default` |
| 

`feed_source`

 | String | 

Set source for RSS feed. When internal, general format is `{rss_url="", is_external=False, content_group_id="2502431580"}`. When external, general format is `{rss_url="http://blog.hubspot.com/marketing/rss.xml", is_external=True}`.

 |  |
| 

`tag_id`

 | Number | 

ID for tag when feed source is internal blog.

 |  |

Section header[](https://developers.hubspot.com/docs/cms/hubl/tags#section-header)
----------------------------------------------------------------------------------

Generates an html heading and `<p>` subheader.

{% section\_header "section\_header" %} {% section\_header "my\_section\_header" subheader="A more subdued subheader", header="A clear and bold header", label="Section Header" %}<span id="hs\_cos\_wrapper\_my\_section\_header" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_section\_header" style="" data-hs-cos-general-type="widget" data-hs-cos-type="section\_header"> <div class="page-header section-header"> <h1>A clear and bold header</h1> <p class="secondary-header"><span id="hs\_cos\_wrapper\_subheader" class="section-subheader">A more subdued subheader</span></p> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | String | 

Text to display in header.

 | `"A clear and bold header"` |
| 

`subheader`

 | String | 

Text to display in subheader.

 | `"A more subdued subheader"` |
| 

`heading_level`

 | String | 

The semantic HTML heading level. h1 to h6 are supported.

 | `"h1"` |

Simple menu[](https://developers.hubspot.com/docs/cms/hubl/tags#simple-menu)
----------------------------------------------------------------------------

Simple menus allow you to create basic [navigation menus](/docs/cms/building-blocks/menus-and-navigation) that can be modified at the page level. Unlike regular menu modules, simple menus are not managed from the Navigation screen in Website Settings, but rather from the template and page editors. You can use [block syntax](/docs/cms/building-blocks/modules/using-modules-in-templates#block-syntax) to set up a default menu tree.

{% simple\_menu "simple\_menu" %} {% simple\_menu "my\_simple\_menu" orientation="horizontal", label="Simple Menu" %} Block Syntax Example: {% widget\_block simple\_menu "block\_simple\_menu" overrideable=True, orientation="horizontal", label="Simple Menu" %} {% widget\_attribute "menu\_tree" is\_json=True %}\[{"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "Home", "linkTarget": null, "linkUrl": "http://www.hubspot.com", "children": \[\], "isDeleted": false}, {"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "About", "linkTarget": null, "linkUrl": "http://www.hubspot.com/internet-marketing-company", "children": \[{"contentType": null, "subCategory": null, "pageLinkName": null, "linkUrl": "http://www.hubspot.com/company/management", "isPublished": false, "children": \[\], "linkParams": null, "linkLabel": "Our Team", "linkTarget": null, "pageLinkId": null, "categoryId": null, "isDeleted": false}\], "isDeleted": false}, {"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "Pricing", "linkTarget": null, "linkUrl": "http://www.hubspot.com/pricing", "children": \[\], "isDeleted": false}\]{% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_my\_simple\_menu" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_simple\_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="simple\_menu"> <ul></ul> </span> <span id="hs\_cos\_wrapper\_block\_simple\_menu" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_simple\_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="simple\_menu"> <div id="hs\_menu\_wrapper\_module\_143093417497114626" class="hs-menu-wrapper active-branch flyouts hs-menu-flow-horizontal" data-sitemap-name=""> <ul> <li class="hs-menu-item hs-menu-depth-1"><a href="//www.hubspot.com" target="\_self">Home</a></li> <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children"><a href="//www.hubspot.com/internet-marketing-company" target="\_self">About</a> <ul class="hs-menu-children-wrapper"> <li class="hs-menu-item hs-menu-depth-2"><a href="//www.hubspot.com/company/management" target="\_self">Our Team</a></li> </ul> </li> <li class="hs-menu-item hs-menu-depth-1"><a href="//www.hubspot.com/pricing" target="\_self">Pricing</a></li> </ul> </div> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`orientation`

 | Enumeration | 

Defines classes of menu markup to allow to style the orientation of menu items on the page. Possible values include `"horizontal"` and `"vertical"`.

 | `"horizontal"` |
| 

`menu_tree`

 | JSON | 

Menu structure including page link names and target URLs.

 | `[]` |

Social sharing[](https://developers.hubspot.com/docs/cms/hubl/tags#social-sharing)
----------------------------------------------------------------------------------

Social sharing tags generate social media icons that can be used to share a particular page. This module can be used with [block syntax](/docs/cms/building-blocks/modules/using-modules-in-templates#block-syntax) to customize the icon images and more.

{% social\_sharing "social\_sharing" %} {% social\_sharing "my\_social\_sharing" use\_page\_url=True %} Block Syntax Example: {% widget\_block social\_sharing "my\_social\_sharing" label="Social Sharing", use\_page\_url=True, overrideable=True %} {% widget\_attribute "pinterest" is\_json=True %}{"custom\_link\_format": "", "pinterest\_media": "http://cdn1.hubspot.com/hub/158015/305390\_10100548508246879\_837195\_59275782\_6882128\_n.jpg", "enabled": true, "network": "pinterest", "img\_src": "https://static.hubspot.com/final/img/common/icons/social/pinterest-24x24.png"}{% end\_widget\_attribute %} {% widget\_attribute "twitter" is\_json=True %}{"custom\_link\_format": "", "enabled": true, "network": "twitter", "img\_src": "https://static.hubspot.com/final/img/common/icons/social/twitter-24x24.png"}{% end\_widget\_attribute %} {% widget\_attribute "linkedin" is\_json=True %}{"custom\_link\_format": "", "enabled": true, "network": "linkedin", "img\_src": "https://static.hubspot.com/final/img/common/icons/social/linkedin-24x24.png"}{% end\_widget\_attribute %} {% widget\_attribute "facebook" is\_json=True %}{"custom\_link\_format": "", "enabled": true, "network": "facebook", "img\_src": "https://static.hubspot.com/final/img/common/icons/social/facebook-24x24.png"}{% end\_widget\_attribute %} {% widget\_attribute "email" is\_json=True %}{"custom\_link\_format": "", "enabled": true, "network": "email", "img\_src": "https://static.hubspot.com/final/img/common/icons/social/email-24x24.png"}{% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_social\_sharing" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_social\_sharing" style="" data-hs-cos-general-type="widget" data-hs-cos-type="social\_sharing"> <a href="http://www.facebook.com/share.php?u=http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Dfacebook" target="\_blank" style="width:24px;border-width:0px;border:0px;"> <img src="//static.hubspot.com/final/img/common/icons/social/facebook-24x24.png?width=24" class="hs-image-widget hs-image-social-sharing-24" style="max-height:24px;max-width:24px;border-width:0px;border:0px;" width="24" hspace="0" alt="Share on Facebook"> </a> <a href="http://www.linkedin.com/shareArticle?mini=true&url=http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Dlinkedin" target="\_blank" style="width:24px;border-width:0px;border:0px;"> <img src="//static.hubspot.com/final/img/common/icons/social/linkedin-24x24.png?width=24" class="hs-image-widget hs-image-social-sharing-24" style="max-height:24px;max-width:24px;border-width:0px;border:0px;" width="24" hspace="0" alt="Share on LinkedIn"> </a> <a href="https://twitter.com/intent/tweet?original\_referer=http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Dtwitter&url=http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Dtwitter&source=tweetbutton&text=" target="\_blank" style="width:24px;border-width:0px;border:0px;"> <img src="//static.hubspot.com/final/img/common/icons/social/twitter-24x24.png?width=24" class="hs-image-widget hs-image-social-sharing-24" style="max-height:24px;max-width:24px;border-width:0px;border:0px;" width="24" hspace="0" alt="Share on Twitter"> </a> <a href="http://pinterest.com/pin/create/button/?url=http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Dpinterest&media=http%3A%2F%2Fcdn1.hubspot.com%2Fhub%2F158015%2F305390\_10100548508246879\_837195\_59275782\_6882128\_n.jpg" target="\_blank" style="width:24px;border-width:0px;border:0px;"> <img src="//static.hubspot.com/final/img/common/icons/social/pinterest-24x24.png?width=24" class="hs-image-widget hs-image-social-sharing-24" style="max-height:24px;max-width:24px;border-width:0px;border:0px;" width="24" hspace="0" alt="Share on Pinterest"></a> <a href="mailto:?subject=Check out http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Demail &body=Check out http%3A%2F%2Fexample.com%2Fmy-page%3Futm\_medium%3Dsocial%26utm\_source%3Demail" target="\_blank" style="width:24px;border-width:0px;border:0px;"> <img src="//static.hubspot.com/final/img/common/icons/social/email-24x24.png?width=24" class="hs-image-widget hs-image-social-sharing-24" style="max-height:24px;max-width:24px;border-width:0px;border:0px;" width="24" hspace="0" alt="Share on Email"> </a> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`use_page_url`

 | Boolean | 

If true, the module shares the URL of the page by default.

 | `True` |
| 

`link`

 | String | 

Specifies a different URL to share, if `use_page_url` is false.

 |  |
| 

`pinterest`

 | JSON | 

Parameters for Pinterest link format and icon image source.

 | `See block syntax example, above` |
| 

`twitter`

 | JSON | 

Parameters for Twitter link format and icon image source.

 | `See block syntax example, above` |
| 

`linked_in`

 | JSON | 

Parameters for LinkedIn link format and icon image source.

 | `See block syntax example, above` |
| 

`facebook`

 | JSON | 

Parameters for Facebook link format and icon image source.

 | `See block syntax example, above` |
| 

`email`

 | JSON | 

Parameters for email sharing link format and icon image source.

 | `See block syntax example, above` |

Spacer[](https://developers.hubspot.com/docs/cms/hubl/tags#spacer)
------------------------------------------------------------------

A spacer tag generates an empty span tag. This tag can be styled to act as a spacer. In drag and drop layouts, the spacer module is wrapped in a container with a class of span1-span12 to determine how much space the module should take up in the twelve column responsive grid.

{% space "space" %} {% space "spacer" label="Horizontal Spacer" %}<span id="hs\_cos\_wrapper\_module\_spacer" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_space" style="" data-hs-cos-general-type="widget" data-hs-cos-type="space"></span>

System page tags[](https://developers.hubspot.com/docs/cms/hubl/tags#system-page-tags)
--------------------------------------------------------------------------------------

The following tags can be used on [system pages](/docs/cms/building-blocks/templates#system-pages), such as the password reset or email subscription pages.

### Email backup unsubscribe[](https://developers.hubspot.com/docs/cms/hubl/tags#email-backup-unsubscribe)

The backup unsubscribe tag renders for email recipients, if HubSpot is unable to determine their email address, when that recipient tries to unsubscribe. This tag renders a form for the contact to enter his or her email address to unsubscribe from email communications. It should be used on an [Unsubscribe Backup system template.](https://knowledge.hubspot.com/cos-general/use-system-templates-to-customize-error-subscription-and-password-prompt-pages)

{% email\_simple\_subscription "email\_simple\_subscription" %} {% email\_simple\_subscription "email\_simple\_subscription" header="Email Unsubscribe", input\_help\_text="Your email address:", input\_placeholder="email@example.com", button\_text="Unsubscribe", label="Backup Unsubscribe" %}<span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""></span> <div class="page-header"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""></span> <h1><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style="">Email Unsubscribe</span></h1><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""></span> </div> <form id="email-prefs-form" method="post" name="email-prefs-form" style="position: relative"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""></span> <div id="content"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""></span> <h3 style="font-weight: normal"><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style="">Your email address:</span></h3> <div style="padding-bottom: 10px"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""><input class="email-edit hs-input" name="email" placeholder="email@example.com" style="padding: 6px; font-size: 15px; width: 507px; margin-left: 0px" type="email" value=""></span> </div><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""><input class="hs-button primary" id="submitbutton" type="submit" value="Unsubscribe"></span> </div><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_simple\_subscription" data-hs-cos-general-type="widget" data-hs-cos-type="email\_simple\_subscription" id="hs\_cos\_wrapper\_email\_simple\_subscription" style=""></span> </form>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | String | 

Renders text in an h1 tag above the unsubscribe form.

 | `"Email Unsubscribe"` |
| 

`input_help_text`

 | String | 

Renders help text in an h3 tag above your email unsubscribe form field.

 | `"Your email address:"` |
| 

`input_placeholder`

 | String | 

Adds placeholder text within the email address form field.

 | `"email@example.com"` |
| 

`button_text`

 | String | 

Changes the text of the unsubscribe form submit button.

 | `"Unsubscribe"` |

### Email subscriptions[](https://developers.hubspot.com/docs/cms/hubl/tags#email-subscriptions)

This module renders when an email recipient goes to edit his or her subscription preferences. It should be used on a [Subscription Preference system template.](https://knowledge.hubspot.com/cos-general/use-system-templates-to-customize-error-subscription-and-password-prompt-pages)

{% email\_subscriptions "email\_subscriptions" %} {% email\_subscriptions "email\_subscriptions" resubscribe\_button\_text="Yes, resubscribe me!", unsubscribe\_single\_text="Uncheck the types of emails you do not want to receive:", subheader\_text="\\n If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you.\\n", unsubscribe\_all\_unsubbed\_text="You are presently unsubscribed from all of our emails. Would you like to receive our emails again?", button\_text="Update email preferences", label="Subscription Preferences", header="Communication Preferences", unsubscribe\_all\_option="Unsubscribe me from all mailing lists.", unsubscribe\_all\_text="Or check here to never receive any emails:" %}<span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""></span> <form id="email-prefs-form" method="post" name="email-prefs-form"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""></span> <div class="page-header"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""></span> <h1><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style="">Communication Preferences</span></h1> <h2><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style="">example@email.com</span></h2><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""><br></span> <p><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style="">If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you.</span></p> </div> <div class="email-prefs" id="content"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""></span> <p class="header"><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style="">Uncheck the types of emails you do not want to receive:</span></p><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""><input name="email" type="hidden" value="example@email.com"> <input name="unsub\_url" type="hidden" value=""> <input name="unsubed\_all" type="hidden" value="false"> <input name="subscription\_ids" type="hidden" value=""></span> <div class="item"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""></span> <div class="item-inner"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""></span> <div class="checkbox-row"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions" id="hs\_cos\_wrapper\_email\_subscriptions" style=""><span class="fakelabel"><input id="id\_0" name="id\_0" type="checkbox"> <span>Example Subscription #1</span></span></span> </div> <p>Your email type description</p> </div> </div> <div class="item"> <div class="item-inner"> <div class="checkbox-row"> <span class="fakelabel"><input id="id\_0" name="id\_0" type="checkbox"> <span>Example Subscription #2</span></span> </div> <p>Your email type description</p> </div> </div> <div class="subscribe-options" style="margin-right: 0"> <p class="header">Or check here to never receive any emails:</p> <p><label for="globalunsub"><input id="globalunsub" name="globalunsub" type="checkbox"> <span>Unsubscribe me from all mailing lists.</span></label></p> </div><input class="hs-button primary" id="submitbutton" type="submit" value="Update email preferences"> <div class="clearer"></div> </div> </form>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | String | 

Renders text in an h1 tag above the subscription preferences form.

 | `"Communication Preferences"` |
| 

`subheader_text`

 | String | 

Populates text below the heading above the unsubscribe preferences.

 | `"<p>\n If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you.\n</p>"` |
| 

`unsubscribe_single_text`

 | String | 

Renders text in a <p class="header"> above the subscription options.

 | `"Uncheck the types of emails you do not want to receive:"` |
| 

`unsubscribe_all_text`

 | String | 

Renders text in a <p class="header"> above the unsubscribe from all emails checkbox input.

 | `"Or check here to never receive any emails:"` |
| 

`unsubscribe_all_unsubbed_text`

 | String | 

Populates text within a <p> that renders, if a contact is currently unsubscribed from all emails.

 | `"You are presently unsubscribed from all of our emails. Would you like to receive our emails again?"` |
| 

`unsubscribe_all_option`

 | String | 

Sets the text next to the unsubscribe from all emails checkbox input.

 | `"Unsubscribe me from all mailing lists."` |
| 

`button_text`

 | String | 

Sets the text of the submit button that updates subscription preferences.

 | `"Update email preferences"` |
| 

`resubscribe_button_text`

 | String | 

Sets the text of the submit button for when contacts are resubscribing.

 | `"Yes, resubscribe me!"` |

### Email subscriptions confirmation[](https://developers.hubspot.com/docs/cms/hubl/tags#email-subscriptions-confirmation)

The email subscriptions update confirmation is a module that can be added to the thank you template for when a recipient updates his or her subscription preferences or unsubscribes. It should be used on a [Subscription Preference system template.](https://knowledge.hubspot.com/cos-general/use-system-templates-to-customize-error-subscription-and-password-prompt-pages)

{% email\_subscriptions\_confirmation "email\_subscriptions\_confirmation" %} {% email\_subscriptions\_confirmation "email\_subscriptions\_confirmation" label="Subscriptions Update Confirmation", unsubscribe\_all\_success="You have successfully unsubscribed from all email communications.", subscription\_update\_success="You have successfully updated your email preferences.", subheader\_text="\\n If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you.\\n" %}<span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions\_confirmation" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions\_confirmation" id="hs\_cos\_wrapper\_email\_subscriptions\_confirmation" style=""></span> <div class="page-header"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions\_confirmation" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions\_confirmation" id="hs\_cos\_wrapper\_email\_subscriptions\_confirmation" style=""></span> <h2><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions\_confirmation" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions\_confirmation" id="hs\_cos\_wrapper\_email\_subscriptions\_confirmation" style="">example@email.com</span></h2><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions\_confirmation" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions\_confirmation" id="hs\_cos\_wrapper\_email\_subscriptions\_confirmation" style=""><br></span> <p><span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions\_confirmation" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions\_confirmation" id="hs\_cos\_wrapper\_email\_subscriptions\_confirmation" style="">If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you.</span></p> </div> <div class="success" id="content"> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_email\_subscriptions\_confirmation" data-hs-cos-general-type="widget" data-hs-cos-type="email\_subscriptions\_confirmation" id="hs\_cos\_wrapper\_email\_subscriptions\_confirmation" style="">You have successfully updated your email preferences.</span> </div>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | String | 

Renders text in an h1 tag above the unsubscribe form.

 | `"Communication Preferences"` |
| 

`subheader_text`

 | String | 

Populates text above the confirmation message.

 | `"<p>\n If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you.\n</p>"` |
| 

`unsubscribe_all_success`

 | String | 

Sets the text that will display when someone unsubscribes from all email communications.

 | `"You have successfully unsubscribed from all email communications."` |
| 

`subscription_update_success`

 | String | 

Sets the text when a recipient updates his or her subscription preferences.

 | `"You have successfully updated your email preferences."` |

### Membership login[](https://developers.hubspot.com/docs/cms/hubl/tags#membership-login)

Creates a login form to provide access to [private content](https://knowledge.hubspot.com/website-pages/require-member-registration-to-access-private-content). 

{% member\_login "my\_login" %} {% member\_login "my\_login" email\_label="Email", password\_label="Password", remember\_me\_label="Remember Me", reset\_password\_text="Forgot your password?", submit\_button\_text="Login", show\_password="Show password" %}<span id="hs\_cos\_wrapper\_my\_login" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_member\_login" style="" data-hs-cos-general-type="widget" data-hs-cos-type="member\_login"><div class="hs-form-field"> <ul class="no-list hs-error-msgs" style="text-align:center"> <li> <label class="hs-membership-global-error hs-error-msg"></label> </li> </ul> </div> <form method="post" action="/\_hcms/mem/login?domain=default&amp;hs\_preview\_key=c4H4EEQCL-JSCFBlDzG4wg&amp;portalId=2272014&amp;tc\_deviceCategory=desktop&amp;template\_file\_path=my-test-theme%2Ftemplates%2Fsystem%2Fmembership-login.html&amp;updated=1644243124141&amp;redirect\_url=/" id="hs-membership-form" onsubmit="onFormSubmit()" data-hs-do-not-collect=""> <input name="csrf\_token" type="hidden" value=""> <input name="redirect\_url" type="hidden" value="/"> <input id="hs-membership-form-hubspotutk" name="hubspotutk" type="hidden" value=""> <div class="hs-form-field"> <label class="hs-login-widget-email-label" for="hs-login-widget-email">Email\*</label> <input class="hs-input" name="email" type="text" placeholder="Email" id="hs-login-widget-email" value=""> </div> <div class="hs-form-field"> <label class="hs-login-widget-password-label" for="hs-login-widget-password">Password\*</label> <a class="hs-login-widget-show-password" href="javascript:show\_password('hs-login-widget-password');">Show password</a> <input class="hs-input" name="password" type="password" placeholder="Password" id="hs-login-widget-password"> </div> <div class="hs-form-field"> <input class="hs-input" name="remember\_me" type="checkbox" id="hs-login-widget-remember" value="true" checked=""> <label for="hs-login-widget-remember">Remember Me</label> </div> <div> <a id="hs\_login\_reset" href="/\_hcms/mem/reset/request">Forgot your password?</a> </div> <div class="hs-membership-loader hs\_submit hs-submit"> <div class="actions"> <input type="submit" class="hs-button primary large" value="Login"> </div> </div> </form> <script type="text/javascript"> function onFormSubmit() { // document.querySelector('.hs-membership-loader').classList.add('active'); } document.onkeydown = function(e) { if (\['ArrowUp','ArrowDown'\].includes(e.code)) { var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input = children\[i\]; if (input === document.activeElement) { if (e.code =='ArrowDown' && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (e.code=='ArrowUp' && children\[i-1\]!==undefined) { children\[i-1\].focus(); break; } } else if (i + 1 === children.length) { children\[0\].focus(); } } } else if ('Enter' === e.code) { e.preventDefault(); var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input=children\[i\]; if (input === document.activeElement && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (input === document.activeElement && i + 1 === children.length) { // document.querySelector('.hs-membership-loader').classList.add('active'); document.getElementById('hs-membership-form').submit(); } else if (i + 1 === children.length) { children\[0\].focus(); } } } } </script> <div id="hs-membership-rate-limit-error-text" style="display:none"> You've made too many attempts at this request. Please try this action again in a few minutes. </div> <script type="text/javascript"> function show\_password(id) { var input = document.getElementById(id); input.type = input.type === 'password' ? 'text' : 'password'; } </script> <script> function getCookie(name) { var nameEQ = name + "="; var ca = document.cookie.split(';'); for(var i=0;i < ca.length;i++) { var c = ca\[i\]; while (c.charAt(0)==' ') c = c.substring(1,c.length); if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length); } return null; } document.getElementById('hs-membership-form-hubspotutk').value = getCookie("hubspotutk"); </script> </span>

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`email_label`

 | String | 

The label for the email entry field.

 | `"Email"` |
| 

`password_label`

 | String | 

The label for the password entry field.

 | `"Password"` |
| 

`remember_me_label`

 | String | 

The label for the "Remember Me" checkbox.

 | `"Remember Me"` |
| 

`reset_password_text`

 | String | 

The text for the password reset hyperlink.

 | `"Forgot your password?"` |
| 

`submit_button_text`

 | String | 

The text for the submit button.

 | `"Login"` |
| 

`show_password`

 | String | 

The text for the password reveal link.

 | `"Show password"` |

### Membership registration[](https://developers.hubspot.com/docs/cms/hubl/tags#membership-registration)

Creates a form to register for access to [private content](https://knowledge.hubspot.com/website-pages/require-member-registration-to-access-private-content). 

{% member\_register "my\_register" %} {% member\_register "my\_register" email\_label="Email", password\_label="Password", password\_confirm\_label="Confirm Password", submit\_button\_text="Save Password", show\_password="Show password" %}<span id="hs\_cos\_wrapper\_my\_register" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_member\_register" style="" data-hs-cos-general-type="widget" data-hs-cos-type="member\_register"><div class="hs-form-field"> <ul class="no-list hs-error-msgs" style="text-align:center"> <li> <label class="hs-membership-global-error hs-error-msg"></label> </li> </ul> </div> <form method="post" action="/\_hcms/mem/register?domain=default&amp;hs\_preview\_key=\_zUv\_TyY1BCRQ2RviUepiQ&amp;portalId=2272014&amp;tc\_deviceCategory=desktop&amp;template\_file\_path=my-test-theme%2Ftemplates%2Fsystem%2Fmembership-register.html&amp;updated=1644243124290&amp;redirect\_url=/\_hcms/mem/login?success%3Dtrue" id="hs-membership-form" onsubmit="onFormSubmit()" data-hs-do-not-collect=""> <input name="csrf\_token" type="hidden" value=""> <input name="redirect\_url" type="hidden" value="/\_hcms/mem/login?success=true"> <input id="hs-membership-form-hubspotutk" name="hubspotutk" type="hidden" value=""> <div class="hs-form-field"> <label for="hs-register-widget-email">Email\*</label> <input class="hs-input" name="email\_read\_only" type="email" value="" id="hs-register-widget-email" disabled=""> <input name="email" type="hidden" value=""> <input name="token" type="hidden" value=""> </div> <div class="hs-form-field"> <label for="hs-register-widget-password">Password\*</label> <a class="hs-register-widget-show-password" href="javascript:show\_password('hs-register-widget-password');">Show password</a> <input class="hs-input" name="password" type="password" placeholder="Password" id="hs-register-widget-password"> </div> <div class="form-input-validation-message" id="hs-membership-password-requirements"> <ul class="no-list hs-error-msgs"> <li> <label>Password must be at least 8 characters long and include lower and uppercase letters, a number, and a symbol</label> </li> </ul> </div> <div class="hs-form-field"> <label for="hs-register-widget-password-confirm">Confirm Password\*</label> <a class="hs-register-widget-show-password" href="javascript:show\_password('hs-register-widget-password-confirm');">Show password</a> <input class="hs-input" name="password\_confirm" type="password" placeholder="Confirm Password" id="hs-register-widget-password-confirm"> </div> <div class="hs-membership-loader hs\_submit hs-submit"> <div class="actions"> <input type="submit" class="hs-button primary large" value="Save Password"> </div> </div> </form> <script type="text/javascript"> function onFormSubmit() { // document.querySelector('.hs-membership-loader').classList.add('active'); } document.onkeydown = function(e) { if (\['ArrowUp','ArrowDown'\].includes(e.code)) { var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input = children\[i\]; if (input === document.activeElement) { if (e.code =='ArrowDown' && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (e.code=='ArrowUp' && children\[i-1\]!==undefined) { children\[i-1\].focus(); break; } } else if (i + 1 === children.length) { children\[0\].focus(); } } } else if ('Enter' === e.code) { e.preventDefault(); var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input=children\[i\]; if (input === document.activeElement && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (input === document.activeElement && i + 1 === children.length) { // document.querySelector('.hs-membership-loader').classList.add('active'); document.getElementById('hs-membership-form').submit(); } else if (i + 1 === children.length) { children\[0\].focus(); } } } } </script> <script type="text/javascript"> function show\_password (id) { var input = document.getElementById(id); input.type = input.type === 'password' ? 'text' : 'password'; } </script> <script> function getCookie(name) { var nameEQ = name + "="; var ca = document.cookie.split(';'); for(var i=0;i < ca.length;i++) { var c = ca\[i\]; while (c.charAt(0)==' ') c = c.substring(1,c.length); if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length); } return null; } document.getElementById('hs-membership-form-hubspotutk').value = getCookie("hubspotutk"); </script> </span>

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`email_label`

 | String | 

The label for the email entry field.

 | `"Email"` |
| 

`password_label`

 | String | 

The label for the password entry field.

 | `"Password"` |
| 

`password_confirm_label`

 | String | 

The label for the password confirmation field.

 | `"Confirm Password"` |
| 

`submit_button_text`

 | String | 

The text for the submit button.

 | `"Save Password"` |
| 

`show_password`

 | String | 

The text for the password reveal link.

 | `"Show password"` |

### Password reset request[](https://developers.hubspot.com/docs/cms/hubl/tags#password-reset-request)

Creates a form to send a password reset email for accessing password-protected pages. 

{% password\_reset\_request "my\_password\_reset\_request" %} {% password\_reset\_request "my\_password\_reset\_request" email\_label="Email", submit\_button\_text="Send Reset Email" %}<span id="hs\_cos\_wrapper\_my\_password\_reset\_request" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_password\_reset\_request" style="" data-hs-cos-general-type="widget" data-hs-cos-type="password\_reset\_request"><div class="hs-form-field"> <ul class="no-list hs-error-msgs" style="text-align:center"> <li> <label class="hs-membership-global-error hs-error-msg"></label> </li> </ul> </div> <div class="hs-form-field"> <ul class="no-list" style="text-align:center"> <li> <label class="hs-membership-global-message"></label> </li> </ul> </div> <form method="post" action="/\_hcms/mem/reset/request?domain=default&amp;hs\_preview\_key=x7aXsEAvlLtUOa1P5t89wQ&amp;portalId=2272014&amp;tc\_deviceCategory=desktop&amp;template\_file\_path=my-test-theme%2Ftemplates%2Fsystem%2Fmembership-reset-password-request.html&amp;updated=1644243124282&amp;redirect\_url=/" id="hs-membership-form" onsubmit="onFormSubmit()" data-hs-do-not-collect=""> <input name="csrf\_token" type="hidden" value=""> <input name="redirect\_url" type="hidden" value="/"> <div class="hs-form-field"> <label for="hs-reset-request-widget-email">Email\*</label> <input class="hs-input" name="email" type="text" placeholder="Email" id="hs-reset-request-widget-email"> </div> <div class="hs-membership-loader hs\_submit hs-submit"> <div class="actions"> <input type="submit" class="hs-button primary large" value="Send Reset Email"> </div> </div> </form> <script type="text/javascript"> function onFormSubmit() { // document.querySelector('.hs-membership-loader').classList.add('active'); } document.onkeydown = function(e) { if (\['ArrowUp','ArrowDown'\].includes(e.code)) { var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input = children\[i\]; if (input === document.activeElement) { if (e.code =='ArrowDown' && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (e.code=='ArrowUp' && children\[i-1\]!==undefined) { children\[i-1\].focus(); break; } } else if (i + 1 === children.length) { children\[0\].focus(); } } } else if ('Enter' === e.code) { e.preventDefault(); var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input=children\[i\]; if (input === document.activeElement && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (input === document.activeElement && i + 1 === children.length) { // document.querySelector('.hs-membership-loader').classList.add('active'); document.getElementById('hs-membership-form').submit(); } else if (i + 1 === children.length) { children\[0\].focus(); } } } } </script> </span>

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`email_label`

 | String | 

The label for the email entry field.

 | `"Email"` |
| 

`submit_button_text`

 | String | 

The text for the submit button.

 | `"Send Reset Email"` |
| 

`password_reset_message`

 | String | 

The message that displays after requesting the password reset email.

 | `False` |

### Password reset[](https://developers.hubspot.com/docs/cms/hubl/tags#password-reset)

Renders a password reset form for accessing password-protected pages. 

{% password\_reset "my\_password\_reset" password\_label="Password", password\_confirm\_label="Confirm Password", submit\_button\_text="Save password", show\_password="Show password" %}<span id="hs\_cos\_wrapper\_my\_password\_reset\_request" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_password\_reset\_request" style="" data-hs-cos-general-type="widget" data-hs-cos-type="password\_reset\_request"><div class="hs-form-field"> <ul class="no-list hs-error-msgs" style="text-align:center"> <li> <label class="hs-membership-global-error hs-error-msg"></label> </li> </ul> </div> <div class="hs-form-field"> <ul class="no-list" style="text-align:center"> <li> <label class="hs-membership-global-message"></label> </li> </ul> </div> <form method="post" action="/\_hcms/mem/reset/request?domain=default&amp;hs\_preview\_key=x7aXsEAvlLtUOa1P5t89wQ&amp;portalId=2272014&amp;tc\_deviceCategory=desktop&amp;template\_file\_path=my-test-theme%2Ftemplates%2Fsystem%2Fmembership-reset-password-request.html&amp;updated=1644243124282&amp;redirect\_url=/" id="hs-membership-form" onsubmit="onFormSubmit()" data-hs-do-not-collect=""> <input name="csrf\_token" type="hidden" value=""> <input name="redirect\_url" type="hidden" value="/"> <div class="hs-form-field"> <label for="hs-reset-request-widget-email">Email\*</label> <input class="hs-input" name="email" type="text" placeholder="Email" id="hs-reset-request-widget-email"> </div> <div class="hs-membership-loader hs\_submit hs-submit"> <div class="actions"> <input type="submit" class="hs-button primary large" value="Send Reset Email"> </div> </div> </form> <script type="text/javascript"> function onFormSubmit() { // document.querySelector('.hs-membership-loader').classList.add('active'); } document.onkeydown = function(e) { if (\['ArrowUp','ArrowDown'\].includes(e.code)) { var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input = children\[i\]; if (input === document.activeElement) { if (e.code =='ArrowDown' && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (e.code=='ArrowUp' && children\[i-1\]!==undefined) { children\[i-1\].focus(); break; } } else if (i + 1 === children.length) { children\[0\].focus(); } } } else if ('Enter' === e.code) { e.preventDefault(); var children = \[\].slice.call(document.querySelectorAll('#hs-membership-form input:not(\[type="hidden"\]):not(\[type="checkbox"\]):not(\[disabled\])')); for (i = 0; i < children.length; i++) { var input=children\[i\]; if (input === document.activeElement && children\[i+1\] !== undefined) { children\[i+1\].focus(); break; } else if (input === document.activeElement && i + 1 === children.length) { // document.querySelector('.hs-membership-loader').classList.add('active'); document.getElementById('hs-membership-form').submit(); } else if (i + 1 === children.length) { children\[0\].focus(); } } } } </script> </span>

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`password_label`

 | String | 

The text label for the password input field.

 | `"Email"` |
| 

`password_confirm_label`

 | String | 

The text label for the password confirmation input field.

 | `"Send Reset Email"` |
| 

`submit_button_text`

 | String | 

The text label for the form submit button.

 | `False` |
| 

`show_password`

 | String | 

The text label for the button to unhide the entered password value.

 | `False` |
| 

`password_requirements`

 | String | 

The text label that describes password requirements.

 | `False` |

### Password prompt[](https://developers.hubspot.com/docs/cms/hubl/tags#password-prompt)

Adds a password prompt to password-protected pages.

{% password\_prompt "password\_prompt" %} {% password\_prompt "my\_password\_prompt" submit\_button\_text="Submit", bad\_password\_message="Sorry, please try again.\\n", label="Password Prompt" %}<span id="hs\_cos\_wrapper\_password\_prompt" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_password\_prompt" style="" data-hs-cos-general-type="widget" data-hs-cos-type="password\_prompt"> <form method="post" action="/\_hcms/protected/auth"> <input name="content\_id" type="hidden" value="1"> <input name="redirect\_url" type="hidden" value="https://preview.hs-sites.com/content-rendering/v1/public/\_hcms/preview/template/multi"> <input name="password" type="password" id="hs-pwd-widget-password" style="height: 22px; margin-top: -5px"> <input type="submit" class="hs-button primary large" value="Submit"> </form> <script type="text/javascript"> document.getElementById("hs-pwd-widget-password").focus(); </script> </span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`submit_button_text`

 | String | 

 Label for button below password entry field.

 | `"Submit"` |
| 

`bad_password_message`

 | String | 

 Message displayed if incorrect password entered.

 | `"<p>Sorry, please try again.</p>"` |
| 

`password_placeholder`

 | String | 

 Defines placeholder text within the password field.

 | `"Password"` |

Text[](https://developers.hubspot.com/docs/cms/hubl/tags#text)
--------------------------------------------------------------

Creates a single line of text. This tag can be useful to be mixed into your markup, when used in conjunction with the `no_wrapper=True` parameter. For example, if you wanted your end users to be able to define a destination of a predefined anchor, you could populate the `href` with a text module with `**no_wrapper=True**`.

{% text "text" %} {% text "simple\_text\_field" label="Enter text here", value="This is the default value for this text field" %}<span id="hs\_cos\_wrapper\_simple\_text\_field" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="text">This is the default value for this text field</span>

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`value`

 | String | 

Sets the default text of the single line text field.

 |  |

Textarea[](https://developers.hubspot.com/docs/cms/hubl/tags#textarea)
----------------------------------------------------------------------

A textarea is similar to a text module in that it allows users to enter plain text, but it gives them a larger area to work in the content editor. This module does not support HTML. If you want to use directly within a predefined wrapping tag, add the `no_wrapper=true` parameter.

{% textarea "my\_textarea" %} {% textarea "my\_textarea" label="Enter plain text block", value="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean a urna quis lacus vehicula rutrum.", no\_wrapper=True %}Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean a urna quis lacus vehicula rutrum.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`value`

 | String | 

Sets the default text of the textarea.

 |  |

Video Player[](https://developers.hubspot.com/docs/cms/hubl/tags#video-player)
------------------------------------------------------------------------------

Render a video player for a video file from the file manager that has the _Allow embedding, sharing, and tracking_ setting turned on.

{% video\_player "embed\_player" %} {% video\_player "embed\_player" overrideable=False, type="scriptV4", hide\_playlist=True, viral\_sharing=False, embed\_button=False, width="600", height="375", player\_id="6178121750", style="", conversion\_asset="{"type":"FORM","id":"9a77c63f-bee6-4ff8-9202-b0af020ea4b2","position":"POST"}" %}

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`hide_playlist`

 | Boolean | 

Hide the video playlist.

 | `True` |
| 

`playlist_color`

 | String | 

A HEX color value for the playlist.

 |  |
| 

`play_button_color`

 | String | 

A HEX color value for the play and pause buttons.

 | `#2A2A2A` |
| 

`embed_button`

 | Boolean | 

Display embed button on the player

 | `False` |
| 

`viral_sharing`

 | Boolean | 

Display the social networks sharing button on the player.

 | `False` |
| 

`width`

 | Number | 

Width of the embedded video player.

 | `Auto` |
| 

`height`

 | Number | 

Height of the embedded video player.

 | `Auto` |
| 

`player_id`

 | Number | 

The `player_id` of the video to embed.

 |  |
| 

`style`

 | String | 

Additional style for player.

 |  |
| 

`conversion_asset`

 | JSON | 

Event setting for player. Can render CTA or Form before or after video plays. This parameter takes a JSON object with three parameters: type (FORM or CTA), id (The guid of the type object), position (POST or PRE).

 | `See above example` |
| 

`placeholder_alt_text`

 | String | 

The video's alt text.

 |  |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/tags#page-feedback)
--------------------------------------------------------------------------------------

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