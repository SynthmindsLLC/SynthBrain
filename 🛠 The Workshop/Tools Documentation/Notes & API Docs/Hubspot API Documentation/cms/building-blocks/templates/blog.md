---
title: "Blog Template Documentation"
description: "Guide for using HubSpot's blog templates."
type: "concept"
tags:
- "HubSpot"
- "Marketing"
- "Content Management"
relationships:
- "#part_of [[HubSpot Documentation]]"
- "#explains [[HubSpot Blog Templates]]"
- "#used_by [[Blog Creators]]"
- "#related_to [[Content Strategy]]"
published_date: "2022-11-18"
---

Blog templates


==================

Last updated: November 18, 2022

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Starter, Professional, or Enterprise

HubSpot blogs consist of blog listing pages and the individual blog posts. In addition to listing the individual blog posts, the blog listing template is also used for rendering the author and tag listing pages. You can either create a single template to render all listing and blog post pages, or you can create two separate templates. 

Below, learn about blog template markup, template components, and customization options.

Create a shared template for the listing and post pages[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#create-a-shared-template-for-the-listing-and-post-pages)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To create one template that renders the listing and post pages, add the `templateType: blog` [annotation](/docs/cms/building-blocks/templates/html-hubl-templates#template-annotations) to the top of your template file. When using one template to render both, you'll use an [if statement](/docs/cms/hubl/if-statements) that evaluates whether the user is looking at a listing page or an individual post. If you are using the [drag and drop design manager layouts](/docs/cms/building-blocks/templates/drag-and-drop-templates), this `if` statement is built into the UI of blog content module buttons.

By using the `if is_listing_view` statement, you can write your post and listing code separately.

{% if is\_listing\_view %} Markup for blog listing template {% else %} Markup for blog post template {% endif %}

Create separate listing and post templates[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#create-separate-listing-and-post-templates)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Alternatively, you can choose to have separate templates for [blog post](/docs/cms/building-blocks/templates#blog-post) and [listing pages](/docs/cms/building-blocks/templates#blog-listing) which can help make your code cleaner and easier to read as a developer, while making the templates easier to select for content creators. Rather than using the `templateType: blog` annotation at the top of the one template, include the following [annotations](/docs/cms/building-blocks/templates#template-types) at the top of your two templates:

*   Blog post template: `templateType: blog_post`
*   Blog listing template: `templateType: blog_listing`

![template-annotation-blog-listing](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/template-annotation-blog-listing.png?width=511&height=179&name=template-annotation-blog-listing.png)

When building separate post and listing templates, the `is_listing_view` check is not required. Instead, you'll manually [select separate templates](https://knowledge.hubspot.com/blog/manage-your-blog-template-and-settings#select-your-blog-templates) within the account's blog settings.

You can also [migrate an existing unified blog template to be either a blog post template or blog listing template](/docs/cms/guides/migrate/blog-to-blog_listing).

### Listing page templates[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#listing-page-templates)

The `templateType: blog_listing` annotation makes the template available for [selection under blog settings](https://knowledge.hubspot.com/blog/manage-your-blog-template-and-settings?__hstc=45788219.de9b5c05d5e30dacc446959817befb15.1626110695319.1626110695319.1626110695319.1&__hssc=45788219.1.1626110695320&__hsfp=939966733&_ga=2.135248759.797241302.1626110695-1964912082.1626110695#select-your-blog-templates) specifically for the listing view. With this template type, content creators can also edit the listing page within the page editor. By also including [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas) in the template, modules can be added and removed in the page editor like they can for other CMS pages. Check out the [CMS boilerplate blog templates](https://github.com/HubSpot/cms-theme-boilerplate/pull/349) to see examples of including drag and drop areas.

The listing of posts is generated by a [for loop](/docs/cms/hubl/for-loops) that iterates through your blog posts. `contents` is a predefined sequence of content that contains all the posts contained in that blog.

{% for content in contents %} <div class="post-item"> Post item markup that renders with each iteration. </div> {% endfor %}

It's recommended to make all text strings on your blog listing template controlled by fields. This makes it easier to create [multilingual](/docs/cms/features/multi-language-content) blogs and gives content creators more control.

Create a blog listing module[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#create-a-blog-listing-module)
-----------------------------------------------------------------------------------------------------------------------------------

You can enable content creators to place modules on the perimeter of the blog listing content, such as on the sides, or above and below. To enable this, it's recommended to create a blog listing module that uses a [blog listing for loop](/docs/cms/building-blocks/templates/blog#blog-listing-for-loop). Check out the [CMS boilerplate blog listing module](https://github.com/HubSpot/cms-theme-boilerplate/tree/main/src/modules/blog-listings.module) for an example. [](https://github.com/HubSpot/cms-theme-boilerplate/tree/main/src/modules/blog-listings.module)

While HubSpot provides [blog settings](https://knowledge.hubspot.com/blog/manage-your-blog-template-and-settings#select-your-blog-templates) for showing summaries and using featured images, you can also build these features into your module. This enables content creators to set these features within the page editor, rather than blog settings.

Blog author, tag, and simple listing pages[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#blog-author-tag-and-simple-listing-pages)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

In additional to the blog post and blog listing pages, HubSpot blogs also have pages for blog authors, blog post tags, and simple listing pages. These additional pages use the same template as the blog listing page to render their content.

Because the listing page template is also shared by the blog author, tag, and simple listing page, updates published to the template will also apply to those pages.

To configure the layout of these pages individually, you can use `if` statements to conditionally render content for each type of page.

### If blog\_author[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#if-blog-author)

Within the standard HubSpot blog listing markup, there is an `if blog_author` statement. This statement evaluates as true when viewing an author's page, which lists the posts published by the author. The boilerplate template includes the author's name, bio, and social media accounts.

{% if blog\_author %} <div class="blog-header"> <div class="blog-header\_\_inner"> {% if blog\_author.avatar %} <div class="blog-header\_\_author-avatar" style="background-image: url('{{ blog\_author.avatar }}');"></div> {% endif %} <h1 class="blog-header\_\_title">{{ blog\_author.display\_name }}</h1> <h4 class="blog-header\_\_subtitle">{{ blog\_author.bio }}</h4> {% if blog\_author.has\_social\_profiles %} <div class="blog-header\_\_author-social-links"> {% if blog\_author.website %} <a href="{{ blog\_author.website }}" target="\_blank"> {% icon name="link" style="SOLID" width="10" %} </a> {% endif %} {% if blog\_author.facebook %} <a href="{{ blog\_author.facebook }}" target="\_blank"> {% icon name="facebook-f" style="SOLID" width="10" %} </a> {% endif %} {% if blog\_author.linkedin %} <a href="{{ blog\_author.linkedin }}" target="\_blank"> {% icon name="linkedin-in" style="SOLID" width="10" %} </a> {% endif %} {% if blog\_author.twitter %} <a href="{{ blog\_author.twitter }}" target="\_blank"> {% icon name="twitter" style="SOLID" width="10" %} </a> {% endif %} </div> {% endif %} </div> </div> {% else %}

### If tag[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#if-tag)

You can use an `if tag` statement to only render code on a blog topic listing page, which visitors can see when clicking a blog topic on your site. The example below is a snippet that uses the page title variable to automatically print the tag name at the top of a tag listing page.

{% if tag %} <h3>Posts about {{ page\_meta.html\_title|split(" | ")|last }}</h3> {% endif %}

### If not simple\_list\_page[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#if-not-simple-list-page)

There are two types of blog listing pages that can be rendered to display blog post listings: the regular listing page, and a simple listing page:

*   The regular listing iterates through the number of posts specified by the post listing blog setting and paginates accordingly.
*   A simple listing is a listing of all your posts and does not support pagination. The simple listing is not affected by the [post limit blog setting](/docs/cms/building-blocks/website-settings#number-of-posts-per-listing-page) and generally just contains links to the most recent 200 blog posts. The address of your simple listing page is the URL for your blog with `/all` added to the end of the path.

You can use an `if not simple_list_page` statement to determine what to render in a simple versus regular listing. A simplified version of this statement is shown below.

Note that the `if` statement uses reverse logic, which means that the `else` defines the simple listing view. Optionally, you could use an [unless statement](/docs/cms/hubl/if-statements#unless-statements) instead.

{% if not simple\_list\_page %} Iterated post markup for regular listing {% else %} <h2 class="post-listing-simple"><a href="{{content.absolute\_url}}">{{ content.name }}</a></h2> {% endif %}

Listing pagination[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#listing-pagination)
---------------------------------------------------------------------------------------------------------------

Blog listing pages have auto-generated pagination. Your listing template can include logic to allow visitors to easily pages through your blog posts. The [boilerplate blog](https://boilerplate.hubspotcms.com/blog) accomplishes simple, number pagination through the [following markup](https://github.com/HubSpot/cms-theme-boilerplate/blob/main/src/modules/blog-pagination.module/module.html):

{% if contents.total\_page\_count > 1 %} <div class="blog-pagination"> {% set page\_list = \[-2, -1, 0, 1, 2\] %} {% if contents.total\_page\_count - current\_page\_num == 1 %}{% set offset = -1 %} {% elif contents.total\_page\_count - current\_page\_num == 0 %}{% set offset = -2 %} {% elif current\_page\_num == 2 %}{% set offset = 1 %} {% elif current\_page\_num == 1 %}{% set offset = 2 %} {% else %}{% set offset = 0 %}{% endif %} <a class="blog-pagination\_\_link blog-pagination\_\_prev-link {{ "blog-pagination\_\_prev-link--disabled" if !last\_page\_num }}" href="{{ blog\_page\_link(last\_page\_num) }}"> {% icon name="chevron-left" style="SOLID", width="13", no\_wrapper=True %} Prev </a> {% for page in page\_list %} {% set this\_page = current\_page\_num + page + offset %} {% if this\_page > 0 and this\_page <= contents.total\_page\_count %} <a class="blog-pagination\_\_link blog-pagination\_\_number-link {{ "blog-pagination\_\_link--active" if this\_page == current\_page\_num }}" href="{{ blog\_page\_link(this\_page) }}">{{ this\_page }}</a> {% endif %} {% endfor %} <a class="blog-pagination\_\_link blog-pagination\_\_next-link {{ "blog-pagination\_\_next-link--disabled" if !next\_page\_num }}" href="{{ blog\_page\_link(current\_page\_num + 1) }}"> Next {% icon name="chevron-right" style="SOLID", width="13", no\_wrapper=True %} </a> </div> {% endif %}

Boilerplate markup[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#boilerplate-markup)
---------------------------------------------------------------------------------------------------------------

Below, view the boilerplate markup for the blog post and blog listing page templates. You can also view this markup in the CMS boilerplate on GitHub, as listed in each section.

### Post template markup[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#post-template-markup)

All blog posts in a blog are generated by a single blog template. `Content` is a predefined object of data that contains information about the requested blog post. [Boilerplate posts](https://boilerplate.hubspotcms.com/blog) are rendered with the [following markup](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/blog-post.html):

<div class="content-wrapper"> <div class="blog-post"> <h1>{{ content.name }}</h1> <div class="blog-post\_\_meta"> <a href="{{ blog\_author\_url(group.id, content.blog\_post\_author.slug) }}"> {{ content.blog\_post\_author.display\_name }} </a> <div class="blog-post\_\_timestamp"> {{ content.publish\_date\_localized }} </div> </div> <div class="blog-post\_\_body"> {{ content.post\_body }} </div> {% if content.tag\_list %} <div class="blog-post\_\_tags"> {% icon name="tag" style="SOLID" %} {% for tag in content.tag\_list %} <a class="blog-post\_\_tag-link" href="{{ blog\_tag\_url(group.id, tag.slug) }}">{{ tag.name }}</a>{% if not loop.last %},{% endif %} {% endfor %} </div> {% endif %} </div> <div class="blog-comments"> {% module "blog\_comments" path="@hubspot/blog\_comments", label="Blog Comments" %} </div> </div>

Blog post author information is also available within the `content` data.

<img alt="{{ content.blog\_post\_author.display\_name }}" src="{{ content.blog\_post\_author.avatar }}"> <h3>Written by <a class="author-link" href="{{ blog\_author\_url(group.id, content.blog\_post\_author.slug) }}">{{ content.blog\_post\_author.display\_name }}</a></h3> <p>{{ content.blog\_post\_author.bio }}</p> {% if content.blog\_post\_author.has\_social\_profiles %} <div class="hs-author-social-section"> <div class="hs-author-social-links"> {% if content.blog\_post\_author.facebook %} <a href="{{ content.blog\_post\_author.facebook }}" target="\_blank" class="hs-author-social-link hs-social-facebook">Facebook</a> {% endif %} {% if content.blog\_post\_author.linkedin %} <a href="{{ content.blog\_post\_author.linkedin }}" target="\_blank" class="hs-author-social-link hs-social-linkedin">LinkedIn</a> {% endif %} {% if content.blog\_post\_author.twitter %} <a href="{{ content.blog\_post\_author.twitter }}" target="\_blank" class="hs-author-social-link hs-social-twitter">Twitter</a> {% endif %} {% if content.blog\_post\_author.google\_plus %} <a href="{{ content.blog\_post\_author.google\_plus }}?rel=author" target="\_blank" class="hs-author-social-link hs-social-google-plus">Google+</a> {% endif %} </div> </div> {% endif %}

### Listing template markup[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#listing-template-markup)

The [boilerplate blog listing page](https://boilerplate.hubspotcms.com/blog) contents for loop is rendered with the [following markup](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/blog-index.html):

{% for content in contents %} {# On the blog homepage the first post will be featured above older posts #} {% if (loop.first && current\_page\_num == 1 && !topic) %} <div class="blog-index\_\_post blog-index\_\_post--large"> <a class="blog-index\_\_post-image blog-index\_\_post-image--large" {% if content.featured\_image %} style="background-image: url('{{ content.featured\_image }}')"; {% endif %} href="{{ content.absolute\_url }}"></a> <div class="blog-index\_\_post-content blog-index\_\_post-content--large"> <h2><a href="{{ content.absolute\_url }}">{{ content.name }}</a></h2> {{ content.post\_list\_content }} </div> </div> {% else %} <div class="blog-index\_\_post blog-index\_\_post--small"> <a class="blog-index\_\_post-image blog-index\_\_post-image--small" {% if content.featured\_image %} style="background-image: url('{{ content.featured\_image }}')"; {% endif %} href="{{ content.absolute\_url }}"></a> <div class="blog-index\_\_post-content blog-index\_\_post-content--small"> <h2><a href="{{ content.absolute\_url }}">{{ content.name }}</a></h2> {{ content.post\_list\_content|truncatehtml(100) }} </div> </div> {% endif %} {% endfor %}

Related resources[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#related-resources)
-------------------------------------------------------------------------------------------------------------

*   [Blog variables](https://developers.hubspot.com/docs/cms/hubl/variables#blog-variables)
*   [Blog templates](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog-template-markup)
*   [HubSpot Theme Boilerplate](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate)
*   [How to create a blog](https://knowledge.hubspot.com/blog/create-a-new-blog)
*   [Import your blog into HubSpot](https://knowledge.hubspot.com/blog/import-a-blog-into-hubspot)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/templates/blog#page-feedback)
-----------------------------------------------------------------------------------------------------------

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