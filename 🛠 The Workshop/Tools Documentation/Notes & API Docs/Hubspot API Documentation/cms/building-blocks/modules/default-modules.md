Default web modules


=======================

Last updated: March 11, 2024

Below, learn about the default modules that HubSpot provides for building templates for website pages, blog posts, and blog listing pages. You'll also find default modules that can be used to build quote templates.

When developing locally, you can [fetch](/docs/cms/developer-reference/local-development-cli#fetch-files) a specific default module using the module path (e.g. `hs fetch @hubspot/linked_image.module`).

To view a default module's code, you can view and clone the module within the `@hubspot` folder of the design manager.

![design-manager-default-modules](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/design-manager-default-modules.png?width=401&name=design-manager-default-modules.png)

**Please note:** default web modules are separate from [default email modules](/docs/cms/building-blocks/modules/default-email-modules), which are for email templates. If your email templates include any of the following default web modules, you should [replace them with the corresponding email-specific module](/docs/cms/update-email-templates-to-use-default-email-modules):

*   `cta`
*   `header`
*   `linked_image`
*   `logo`
*   `post_filter`
*   `post_listing`
*   `section_header`
*   `social_sharing`
*   `text`

Blog comments[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#blog-comments)
--------------------------------------------------------------------------------------------------------------

Supported in blog posts and blog listings.

{% module "blog\_comments" path="@hubspot/blog\_comments" %}

Blog email subscription[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#blog-email-subscription)
----------------------------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "blog\_subscribe" path="@hubspot/blog\_subscribe" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | Blog | 

The blog to use for the module.

 |  |
| 

`title`

 | String | 

Title for the module (wrapped in a h3 tag)

 | `"Subscribe Here!"` |
| 

`response_message`

 | Rich Text | 

The message that is shown upon submitting the form.

 | `Thanks for subscribing!` |

Blog posts[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#blog-posts)
--------------------------------------------------------------------------------------------------------

Add this module to blog listing pages to display blog post previews containing each post's title, featured image, author, publish date, and more with a clickable button that navigates to the post.

This default module has built using React, and you can [view its source code on GitHub](https://github.com/HubSpot/cms-react/tree/main/default-react-modules/src/components/modules/BlogPosts-V0). 

**Please note:**

*   This module cannot be accessed from the design manager. The module can be referenced with HubL in coded templates and added within the [blog listing page editor](https://knowledge.hubspot.com/blog/edit-a-blog-listing-page?revisionPreview=true).
*   This module replaces the previous `blog_listing` module, which has been deprecated.

{% module "blog\_posts" path="@hubspot/blog\_posts" layout="grid", columns=4, displayForEachListItem=\[ "image", "title", "authorName", "tags", "publishDate", "description", "button" \] %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`layout`

Required



 | Choice | 

The content layout for each blog post preview.

*   `grid` (default): aligns posts in a basic grid.
*   `singleColumn`: aligns posts in a single column. with featured images on their own row above the rest of the post content.
*   `sideBySide`: aligns posts in a column with featured images aligned horizontally with the post content.

 | `grid` |
| 

`columns`

 | Number | 

When using the `grid` layout, the number of posts per row. Can be `2`, `3`, or `4`.

 | `3` |
| 

`alternateImage`

 | Boolean | 

When using the `sideBySide` layout, set to `true` to align the featured image on the right and left side of the post preview, alternating.

 | `false` |
| 

`fullImage`

 | Boolean | 

When using the `grid` or `singleColumn` layouts, set this field to `true` to make the featured image the background of the post preview.

 | `false` |
| 

`displayForEachListItem`

 | Array | 

The content to include in each blog post preview. Choices include:

*   `image`: the post's featured image.
*   `title`: the post's title.
*   `authorImage`: the post author's image.
*   `authorName`: the post author's name.
*   `tags`: the post's blog tags.
*   `publishDate`: the post's publish date.
*   `description`: the post's meta description.
*   `button`: the read more button that links to the blog post.

 | `[ 'image', 'title', 'authorImage', 'authorName', 'tags', 'publishDate', 'description', 'button' ]` |
| 

`buttonText`

 | String | 

The text that displays on the read more button, if included.

 | `Read more` |

Blog post filter[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#blog-post-filter)
--------------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "post\_filter" path="@hubspot/post\_filter" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | Blog | 

Select a blog to display. Default will use the current blog when used in a blog template or the primary blog when used elsewhere.

 |  |
| 

`filter_type`

 | Choice | 

Type of filtering links to show. Choices include:

*   `tag`
*   `month`
*   `author`

 | `tag` |
| 

`order_by`

 | Choice | 

Ordering for the values of filter links. Choices include:

*   `post_count`
*   `name`

 | `post_count` |
| 

`list_title`

 | Text | 

An H3 heading.

 | `"Posts by Tag"` |
| 

`max_links`

 | Number | 

Number of filter links to show. Leave blank to show all.

 | `5` |
| 

`expand_link_text`

 | Text | 

Text to display if more than the `max_links` value to display are available. 

 | `"See all"` |

Blog post listing[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#blog-post-listing)
----------------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

**Please note:** a new version of this module will be available by the end of March 2024. Learn more about the [new default post listing module](/docs/cms/building-blocks/default-asset-versioning#post-listing).

{% module "post\_listing" path="@hubspot/post\_listing" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | Blog | 

Select a blog to display. Default will use the current blog when used in a blog template or the primary blog when used elsewhere.

 |  |
| 

`listing_type`

 | Choice | 

The type of listing for your posts. Choices include:

*   `recent`: most recent.
*   `popular_all_time`: most popular of all time.
*   `popular_past_year`: most popular the past year.
*   `popular_past_six_months`: most popular the past six months.
*   `popular_past_month`: most popular the past month.

 | `recent` |
| 

`list_title`

 | Text | 

An H3 heading. 

 | `"Recent Posts"` |
| 

`max_links`

 | Number | 

Maximum number of posts to display. 

 | `5` |

Button[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#button)
------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "button" path="@hubspot/button" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`link`

 | Link | 

The URL that the button redirects to.

 | `{ "url": { "type": "EXTERNAL", "href": "www.hubspot.com", "content_id": null }, "open_in_new_tab": false, "no_follow": false }` |
| 

`button_text`

 | Text | 

Text that will be displayed on the button.

 | `"Add a button link here"` |
| 

`style`

 | Object | 

*   `override_default_style` (Boolean)
*   `button_font` (Font)
*   `button_color` (Color)
*   `text_hover_color` (Color)
*   `button_hover_color` (Color)

 | `{ "override_default_style": false, "button_font": { "color": "#FFFFFF", "size_unit": "px" }, "button_color": { "color": "#000000", "opacity": 100 }, "text_hover_color": { "color": "#000000", "opacity": 100 }, "button_hover_color": { "color": "#CCCCCC", "opacity": 100 } }` |

Call-to-Action[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#call-to-action)
----------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "cta" path="@hubspot/cta" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`guid`

 | String | 

Globally Unique Identifier of the CTA. 

 |  |

Delete data[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#delete-data)
----------------------------------------------------------------------------------------------------------

You can add this module to your subscription preferences page to allow contacts to request that their data be deleted. This function is required under certain data privacy laws. Once a contact requests that their data be deleted, they have 30 minutes to confirm in an email that will automatically be sent.

Users with [super admin permissions](/settings/hubspot-user-permissions-guide) will receive a notification email about these requests. Learn how to [allow contacts to request a download of their data](#download-data).

{% module "delete\_data" path="@hubspot/delete\_data", label="delete\_data.module" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`content`

 | Rich Text | 

Message displayed above the button.

 | `<h3>Delete Data</h3> <p>Permanently delete your personal data stored by {{ site_settings.company_name}}. Personal data is information that can be used to identify you and doesn't include anonymized data.<p/> <p>You'll get a follow-up email where you'll need to verify your request.</p>` |
| 

`button_text`

 | Text | 

Button text.

 | `Request data deletion` |
| 

`group_alerts`

 | Field group | The success and fail alert field group. Including the following field groups:  

*   `group_success_alert`:
    *   `content`: rich text content of success alert.
*   `group_fail_alert`:
    *   `content`: rich text content of fail alert.
*   `group_close_icon`:
    *   `icon`: the icon to close the alert.

 |  |

Divider[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#divider)
--------------------------------------------------------------------------------------------------

Supported in pages. There's a [new version of this module](/docs/cms/building-blocks/default-asset-versioning#divider) available in accounts created after August 25th, 2022. [Learn more about this change](/changelog/divider-module-v1).

{% module "divider" path="@hubspot/divider" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`height`

 | Number | 

Pixel (px) height of the divider line.

 | `1` |
| 

`width`

 | Number | 

Percentage (%) width of the divider line.

 | `50` |
| 

`color`

 | Color | 

Color (hex) and opacity (number) of the divider line.

 | `{ "color": "#000000", "opacity": 100 }` |
| 

`line_type`

 | Choice | 

Line type. Choices include:

*   `solid`
*   `dotted`
*   `dashed`

 | `solid` |
| 

`alignment`

 | Choice | 

Horizontal alignment of divider line. Choices include:

*   `left`
*   `center`
*   `right`

 | `center` |
| 

`show_padding`

 | Boolean | 

Show/hide top and bottom margining on the divider.

 | `false` |
| 

`padding`

 | Number | 

Pixel (px) value for the margining on top and bottom of divider line. 

Option available when `show_padding` equals `true`.

 | `5` |

Download data[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#download-data)
--------------------------------------------------------------------------------------------------------------

You can add this module to your subscription preferences page to allow contacts to request a copy of their data. This function is required under certain data privacy laws. Users with [super admin permissions](/settings/hubspot-user-permissions-guide) will receive a notification email about these requests. Learn how  to [allow contacts to request that their data be deleted](#delete-data).

{% module "download\_data" path="@hubspot/download\_data", label="download\_data.module" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`content`

 | Rich Text | 

Message displayed above the button.

 | `<h3>Download Data</h3> <p>Download your personal data stored by {{ site_settings.company_name}}.</p> <p>Personal data is information that can be used to identify you and doesn't include anonymized data. </p>` |
| 

`button_text`

 | Text | 

Button text.

 | `Request data download` |
| 

`group_alerts`

 | Field group | The success and fail alert field group. Including the following field groups:  

*   `group_success_alert`:
    *   `content`: rich text content of success alert.
*   `group_fail_alert`:
    *   `content`: rich text content of fail alert.
*   `group_close_icon`:
    *   `icon`: the icon to close the alert.

 |  |

Follow me[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#follow-me)
------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts. Uses the [follow\_me\_links function](/docs/cms/hubl/functions#follow-me-links) to return the [social media account links set in account settings](https://knowledge.hubspot.com/design-manager/add-social-links-to-hubspot-templates#add-social-accounts-to-the-follow-me-module)

{% module "follow\_me" path="@hubspot/follow\_me" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`title`

 | Text | 

H3 heading.

 |  |
| 

`links`

 | Boolean | 

Open links in new window.

 | `true` |

Follow me (landing page)[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#follow-me-landing-page-)
-----------------------------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "follow\_me\_lp" path="@hubspot/follow\_me\_lp" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`social`

 | Object | 

Social network selection. Options include:

*   `network` (Choice)
*   `link` (Link)
*   `network_image` (Image)
*   `supporting_text` (Text)

 | `[ { "network": "facebook" } ]` |
| 

`display`

 | Choice | 

Display options for showing social networks. Choices include:

*   `icon`
*   `icon_text`
*   `text_only`

 | `icon` |
| 

`scale`

 | Number | 

Size of the icon (px).

 | `25` |
| 

`spacing`

 | Number | 

Left and Right Padding (px) for items.

 | `5` |
| 

`alignment`

 | Choice | 

The alignment of the items on the page. Choice include:

*   `left`
*   `center`
*   `right`

 | `center` |
| 

`color_scheme`

 | Choice | 

Color scheme to use for icons. Choices include:

*   `color`
*   `black` (black and white)
*   `grey`
*   `white`
*   `custom`

 | `color` |
| 

`custom_color`

 | Color | 

Custom color to use when `color_scheme` equals `custom`.

 | `#000000` |
| 

`icon_shape`

 | Choice | 

Shape of the social icons. Choices include:

*   `circle`
*   `square`
*   `original`

 | `circle` |
| 

`font_style`

 | Object | 

Font object for social network text. Available when `display` does not equal `icon`.

Font object contains: 

*   `size`
    *   `value`: number
    *   `units`: unit of Measure
*   `color`: hex value
*   `styles`
    *   `bold`: boolean
    *   `italic`: boolean
    *   `underline`: boolean
*   `font`: text

 | `{ "size": { "value": 14, "units": "px" }, "color": "#2696be", "styles": { "bold": false, "italic": false, "underline": false }, "font": "helvetica" }` |

Form[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#form)
--------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "form" path="@hubspot/form" form={ "form\_id": "9e633e9f-0634-498e-917c-f01e355e83c6", "response\_type": "redirect", "message": "Thanks for submitting the form.", "redirect\_id": null, "redirect\_url": "http://www.google.com" } %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`title`

 | Text | 

H3 heading

 |  |
| 

`form`

 | Object | 

Form object including:

*   `form_id`: ID for form to use
*   `response_type`: what the visitor will see after submitting the form:
    *   `inline`
    *   `redirect`
*   `message`: inline message if `response_type` is set to `inline`
*   `redirect_id`: ID of page to be redirected to if `response_type` is set to `redirect`.
*   `redirect_url`: URL to be redirected to if `response_type` is set to `redirect`

 | `{ "form_id": "", "response_type": "redirect", "message": "Thanks for submitting the form.", "redirect_id": null, "redirect_url": "http://www.google.com" }` |
| 

`notifications_are_overridden`

 | Boolean | 

Email to send form notification to instead of form defaults.

 | `false` |
| 

`notifications_override_email_addresses`

 | Email | 

Comma-separated list of emails to send to when `notifications_are_overridden` equals `true`.

 |  |
| 

`follow_up_type_simple`

 | Boolean | 

Enabled sending a follow up email.

 | `false` |
| 

`simple_email_for_live_id`

 | Followupemail | 

ID of the follow-up email. Available when `follow_up_type_simple` equals `true`.

 |  |
| 

`sfdc_campaign`

 | Salesforcecampaign | 

When Salesforce integration is active, the campaign ID.

 |  |

Header[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#header)
------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "header" path="@hubspot/header" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`value`

 | Text | 

Text for the heading.

 | `"A clear and bold header"` |
| 

`header_tag`

 | Choice | 

Choose a heading level. Choice include `h1` through `h6`.

 | `h1` |

Horizontal spacer[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#horizontal-spacer)
----------------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, blog posts, and emails.

{% module "horizontal\_spacer" path="@hubspot/horizontal\_spacer" %}

Icon[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#icon)
--------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts. Icons can be pulled from the Font Awesome 5.0.10 and 5.14.0 icon sets.

{% module "icon" path="@hubspot/icon" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`name`

 | String | 

The name of the icon.

 | `"hubspot"` |
| 

`purpose`

 | Choice | 

An accessibility option that categorizes the purpose of the icon for screen readers. Available values are:

*   `decorative:` ignored by the screen reader.
*   `semantic:` read by the screen reader.

 | `"decorative"` |
| 

`title`

 | String | 

An accessibility option that assigns the icon a title.

 |  |
| 

`style`

 | String | The type of icon. Can be one of `solid`, `regular`, `light`, `thin`, or `duotone`. | `"solid"` |
| 

`unicode`

 | String | 

The icon's unicode value.

 | `f3b2` |

Image[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#image)
----------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "linked\_image" path="@hubspot/linked\_image" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`img`

 | Image | 

Image object containing:

*   `src`: image url
*   `alt`: alt text for image
*   `loading`: lazy loading options include:
    *   `disabled`
    *   `lazy`
*   `width`: px value
*   `height`: px value

 | `{ "src": "https://static.hubspot.com/final/img/content/email-template-images/placeholder_200x200.png", "alt": "placeholder_200x200", "loading": "disabled", "width": 200, "height": 200 }` |
| 

`link`

 | Text | 

Optional link for the image.

 |  |
| 

`target`

 | Boolean | 

Opens link in a new tab.

 | `false` |

Image grid[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#image-grid)
--------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "image\_grid" path="@hubspot/image\_grid", label="image\_grid.module" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`slides`

 | Object | 

Object containing information for each slide. Object contains:

*   `img`: image URL.
*   `link_url`: URL where the slide should link.
*   `hover_messages`: text that overlays on the image on hover.

 | `[ { "show_caption": false, "open_in_new_tab": false } ]` |
| 

`display_mode`

 | Choice | 

Display mode of the Image Gallery. Choices include:

*   `standard`: standard slider.
*   `thumbnail`: thumbnail navigator.
*   `lightbox`: lightbox gallery.

 | `standard` |
| 

`lightboxRows`

 | Number | 

Number of rows in the Lightbox gallery when `display_mode` equals `lightbox`.

 | `3` |
| 

`loop_slides`

 | Boolean | 

Enables looping through the slides with next/prev when `display_mode` equals `standard` or `thumbnail`.

 | `true` |
| 

`auto_advance`

 | Boolean | 

Automatically advances to the next slide when `display_mode` equals `standard` or `thumbnail`.

 | `true` |
| 

`num_seconds`

 | Number | 

Amount of time (seconds) between advancing to the next slide when `display_mode` equals `standard` or `thumbnail`.

 | `5` |
| 

`show_pagination`

 | Boolean | 

Show navigation buttons when  `display_mode` equals `standard` or `thumbnail`.

 | `true` |
| 

`sizing`

 | Choice | 

Sets the height of the slides when `display_mode` equals `standard` or `thumbnail`. Choices include:

*   `static`: fixed height.
*   `resize`: variable height.

 | `static` |
| 

`transition`

 | Choice | 

Slide transition styles when `display_mode` equals `standard` or `thumbnail`. Choices include:

*   `slide`: slide transition.
*   `fade`: fade transition.

 | `slide` |
| 

`caption_position`

 | Choice | 

Position of the slide captions when `display_mode` equals `standard` or `thumbnail`. Choices include:

*   `below`: always keep captions below the image.
*   `superimpose`: superimpose captions on top of images.

 | `below` |

Image gallery[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#image-gallery)
--------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "gallery" path="@hubspot/gallery" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`slides`

 | Object | 

Object containing information for each slide. Object contains:

*   `img`: image URL.
*   `show_caption`: boolean to show slide caption.
*   `caption`: rich text for caption.
*   `link_url`: URL where the slide should link.
*   `open_in_new_tab`: boolean to direct if the link should open in a new tab.

 | `[ { "show_caption": false, "open_in_new_tab": false } ]` |
| 

`display_mode`

 | Choice | 

Display mode of the Image Gallery. Choices include:

*   `standard`: standard slider.
*   `thumbnail`: thumbnail navigator.
*   `lightbox`: lightbox gallery.

 | `standard` |
| 

`lightboxRows`

 | Number | 

Number of rows in the Lightbox gallery when `display_mode` equals `lightbox`.

 | `3` |
| 

`loop_slides`

 | Boolean | 

Enables looping through the slides with next/prev when `display_mode` equals `standard` or `thumbnail`.

 | `true` |
| 

`auto_advance`

 | Boolean | 

Automatically advances to the next slide when `display_mode` equals `standard` or `thumbnail`.

 | `true` |
| 

`num_seconds`

 | Number | 

Amount of time (seconds) between advancing to the next slide when `display_mode` equals `standard` or `thumbnail`.

 | `5` |
| 

`show_pagination`

 | Boolean | 

Show navigation buttons when  `display_mode` equals `standard` or `thumbnail`.

 | `true` |
| 

`sizing`

 | Choice | 

Sets the height of the slides when `display_mode` equals `standard` or `thumbnail`. Choices include:

*   `static`: fixed height.
*   `resize`: variable height.

 | `static` |
| 

`transition`

 | Choice | 

Slide transition styles when `display_mode` equals `standard` or `thumbnail`. Choices include:

*   `slide`: slide transition.
*   `fade`: fade transition.

 | `slide` |
| 

`caption_position`

 | Choice | 

Position of the slide captions when `display_mode` equals `standard` or `thumbnail`. Choices include:

*   `below`: always keep captions below the image.
*   `superimpose`: superimpose captions on top of images.

 | `below` |

Image slider gallery[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#image-slider-gallery)
----------------------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "unique\_name" path="@hubspot/image\_slider\_gallery", slides=\[ { "img": { "src": "", "alt": "Default image alt text" }, "caption": "<strong>1</strong> An optional caption for the image that will be added to the gallery. Enter any descriptive text for this image that you would like visitors to be able to read.", "link\_url": "" }, { "img": { "src": "", "alt": "Default image alt text" }, "caption": "<strong>2</strong> An optional caption for the image that will be added to the gallery. Enter any descriptive text for this image that you would like visitors to be able to read.", "link\_url": "" } \] slideshow\_settings={ "slides": { "per\_page": 1, "sizing": "natural", "aspect\_ratio": "16/9", "show\_captions": true, "caption\_position": "below" }, "movement": { "transition": "slide", "loop\_slides": false, "auto\_advance": false, "auto\_advance\_speed\_seconds": 5 }, "navigation": { "show\_main\_arrows": true, "show\_thumbnails": false, "show\_dots": false } } %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`slides`

 | Field group | 

A field group containing the following fields:

*   `img`: image URL.
*   `caption`: rich text for image caption.
*   `link_url`: URL that the slide links to.

 |  |
| 

`slideshow_settings`

 | Field group | 

The image slider settings field group. Includes the following field groups:

*   `slides`: slide settings, including:
    *   `per_page`: number of slides per page.
    *   `sizing`: image sizing.
    *   `aspect_ratio`: image aspect ratio.
    *   `show_captions`: a boolean
*   `movement`: image sliding behavior settings.
*   `navigation`: image navigation settings.

 |  |
| 

`default_text`

 | Field group | 

The module's default text elements, including:

*   `default_caption`: image caption.
*   `default_image_alt_text`: image text.
*   `slider_aria_label`: the module's default aria label.
*   `arial_label_thumbnails`: the module's default aria thumbnail.
*   `slider_nav_aria_label`: the module navigation's default aria label.
*   `prev`: previous slide text.
*   `next`: next slide text.
*   `first`: go to first slide text.
*   `slideX`: go to X slide text.
*   `pageX`: go to X page text.
*   `play`: start autoplay text.
*   `pause`: pause autoplay text.
*   `carousel`: carousel text.
*   `select`: text for selecting a slide to show.
*   `slide`: slide text.
*   `slidelabel`: slide label.

 |  |

Language switcher[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#language-switcher)
----------------------------------------------------------------------------------------------------------------------

Supported in pages.

{% module "language\_switcher" path="@hubspot/language\_switcher" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`display_mode`

 | Choice | 

The language of the text in the language switcher. Options include:

*   `pagelang`: the names of languages will display in the language of the page the switcher is on.
*   `localized`: the name of each language will display in that language.
*   `hybrid`: a combination of the two.

 | `localized` |

Logo [](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#logo-nbsp-)
---------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "logo" path="@hubspot/logo" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`img`

 | Image | 

Image object containing:

*   `override_inherited_src`: override the default logo from settings
*   `src`: image url
*   `alt`: alt-text for logo

 | `{ "override_inherited_src": false, "src": null, "alt": null }` |
| 

`link`

 | Text | 

Optional link for the logo. If no URL is specified, your logo will link to the _Logo URL_ set in your [brand settings](https://knowledge.hubspot.com/branding/edit-your-logo-favicon-and-brand-colors#edit-your-logo).

 |  |
| 

`open_in_new_tab`

 | Boolean | 

Opens link in a new tab.

 | `false` |
| 

`suppress_company_name`

 | Boolean | 

Hide the company name when an image is not selected.

 | `true` |
| 

`heading_level`

 | Choice | 

Choose a heading level when no image is selected and `suppress_company_name` equals `false`. Choices include `h1` through `h6`.

 | `h1` |

Logo grid[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#logo-grid)
------------------------------------------------------------------------------------------------------

A customizable grid of containers to display logos uniformly. Supported in pages, blog listings, and blog posts.

{% module "logo grid" path="@hubspot/logo\_grid" group\_logos=\[ { "logo": { "loading": "lazy", "alt": "company\_logo", "src": "https://www.example.com/Logos/color/logo.png" } }, { "logo": { "loading": "lazy", "alt": "company2\_logo", "src": "https://www.example.com/Logos/color/logo2.png" } }, { "logo": { "alt": "lorem-logo", "height": 40, "loading": "lazy", "max\_height": 40, "max\_width": 175, "src": "https://www.example.com/Logos/color/logo3.png", "width": 175 } } \], styles={ "group\_logo": { "group\_background": { "aspect\_ratio": "1/1", "background\_color": { "color": "#8E7CC3", "opacity": 100 } }, "group\_spacing": { "padding": { "padding": { "bottom": { "units": "px", "value": 75 }, "left": { "units": "px", "value": 75 }, "right": { "units": "px", "value": 75 }, "top": { "units": "px", "value": 75 } } } }, "max\_logo\_height": 85 }, "group\_logo\_grid": { "column\_count": 3, "grid\_gap": 54 } } %}

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`group_logos`

 | Array | 

An array containing an object for each logo in the grid.

 |
| 

`logo`

 | Object | 

In `group_logos`, an object for each logo in the grid. Each logo can include the following parameters:

*   `src`: the file path of the logo.
*   `loading`: the [lazy load](/docs/cms/lazy-loading) behavior of the logo.
*   `alt`: the logo's alt-text.
*   `height`: the logo's height.
*   `width`: the logo's width.
*   `max_height`: the logo's maximum height.
*   `max_width`: the logo's maximum width.

 |
| 

`styles`

 | Array | 

An array containing the style fields that affect the grid layout, logo containers, and logo images. This array contains the following style groups:

*   `group_logo`: styles that affect the logo containers and logo images. Contains the following:
    *   `group_background`: styles that set the aspect ratio and background color of the grid containers. Aspect ratios include: `1/1`, `4/3`, `16/9`.
    *   `group_spacing`: styles that set the inner padding of the logo container. For wider logos, higher padding value may decrease logo width.
    *   `max_logo_height`: the maximum height of each logo.
*   `group_logo_grid`: styles that set the grid layout, including:
    *   `column_count`: the number of columns in the grid.
    *   `grid_gap`: the spacing between grid items.

 |

Meetings[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#meetings)
----------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "meetings" path="@hubspot/meetings" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`meeting`

 | Meeting | 

Select a meeting link.

 |  |

Membership social logins[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#membership-social-logins)
------------------------------------------------------------------------------------------------------------------------------------

This module provides Google and Facebook login capability to memberships sites. The user must sign-in with an account linked to the email for the contact in the CRM. You can choose which social logins to enable.

**Supported in membership login pages.**

{% module "social" path="@hubspot/membership\_social\_logins", clientid="" appid="" facebook\_enabled=true google\_enabled=true %}

Facebook requires having a [Facebook developer account](https://developers.facebook.com/docs/development/register), and a [facebook app created](https://developers.facebook.com/docs/development/create-an-app), with basic settings. Once you've done that your app id is what you pass to the module.

Google requires a Google account, and [authorization credentials created](https://developers.google.com/identity/sign-in/web/sign-in#create_authorization_credentials), once you have that your app's client id is what you pass to the module.

Membership social logins parameters
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`facebook_appid`

 | String | 

Your facebook app ID.

 |  |
| 

`facebook_enabled`

 | boolean | 

Enable the button for Facebook login. `facebook_appid` is required**.**

 | `False` |
| 

`google_clientid`

 | String | 

Your Google client ID.

 |  |
| 

`google_enabled`

 | Boolean | 

Enable the button for Google login. `google_clientid` is required**.**

 | `False` |

Menu[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#menu)
--------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

Looking to build your own custom menu? Try our [menu() function](https://developers.hubspot.com/docs/cms/hubl/functions#menu).

{% module "menu" path="@hubspot/menu" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`id`

 | Menu | 

ID of the menu.

 |  |
| 

`root_type`

 | Choice | 

Advanced menu type. Choices include:

*   `site_root`: always show top-level pages in menu.
*   `top_parent`: show pages in menu that are related to section being viewed.
*   `parent`: show pages in menu that are related to page being viewed.
*   `breadcrumb`: breadcrumb style path menu (uses horizontal flow).

 | `site_root` |
| 

`max_levels`

 | Choice | 

Determines the number of menu tree children that can be expanded in the menu. Choices include `1` through `10`

 | `2` |
| 

`flow`

 | Choice | 

Orientation of the menu. Choices include:

*   `horizontal`
*   `vertical`

 | `horizontal` |
| 

`flyouts`

 | Boolean | 

Enabled hover over functionality for child menu items.

 | `true` |

Page footer[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#page-footer)
----------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "page\_footer" path="@hubspot/page\_footer" %}

Password prompt[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#password-prompt)
------------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "password\_prompt" path="@hubspot/password\_prompt" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`submit_button_text`

 | Text | 

Text that appears on the submit button.

 | `"Submit"` |
| 

`password_placeholder`

 | Text | 

Placeholder text for the password field.

 | `"Password"` |
| 

`bad_password_message`

 | Rich Text | 

Message to show when a password is entered incorrectly. 

 | `"Sorry, please try again. "` |

Payments[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#payments)
----------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "payments" path="@hubspot/payments" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`payment`

 | String | 

To set the module to use a specific payment link, include the ID of the payment link. You can [find the ID](/docs/cms/building-blocks/module-theme-fields/payment-links#find-a-payment-link-s-id) in the URL while editing the payment link.  

 |  |
| 

`checkout_location`

 | String | 

Set whether the payment form opens in a new tab or in an overlay. Available values are:

*   `new_tab`: opens the payment form in a new tab.
*   `overlay`: opens the payment form in a sliding overlay.

 | `"new_tab"` |
| 

`button_text`

 | String | 

Sets the text of the checkout button.

 | `"Checkout"` |
| 

`button_target`

 | Choice | 

Whether the button uses a HubSpot payment link or an external link. Choices include:

*   `payment_link`
*   `custom_link`

 | `"payment_link"` |
| 

`button_link`

 | Link | 

When `button_target` is set to `custom_link`, sets the destination of the external link. Supported link types include:

*   `EXTERNAL`
*   `CONTENT`

 | `EXTERNAL` |

Product[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#product)
--------------------------------------------------------------------------------------------------

Displays a product from the account's [product library](https://knowledge.hubspot.com/products/how-do-i-use-products). Supported in pages, blog posts, and blog listings.

{% module path="@hubspot/product", product={ "id" : 2124070179 }, group\_button={ "button\_text" : "Buy", "override\_product\_button" : true, "button\_override" : { "no\_follow" : false, "open\_in\_new\_tab" : false, "sponsored" : false, "url" : { "href" : "https://www.test.com", "type" : "EXTERNAL" } }, group\_description={ "description\_override" : "Monthly gym membership with access to shared locker facilities.", "override\_product\_description" : true }, group\_name={ "heading\_level" : "h3", "name\_override" : "Gym membership", "override\_product\_name" : true }, group\_image={ "image\_override" : { "alt" : "360\_F\_317724775\_qHtWjnT8YbRdFNIuq5PWsSYypRhOmalS", "height" : 360, "loading" : "lazy", "src" : "https://2272014.fs1.hubspotusercontent-na1.net/hubfs/2272014/360\_F\_317724775\_qHtWjnT8YbRdFNIuq5PWsSYypRhOmalS.jpg", "width" : 640 }, "override\_product\_image" : true } %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`product`

 | Product | 

The product to display, specified by product ID.

 |  |
| 

`group_button`

 | Field group | 

By default, the module includes a button that directs users to the product's set URL. To customize the button destination, include this optional field group along with the following fields:

*   `button_text`: a string that sets the button's text.
*   `override_product_button`: set to `true` to override the default button link settings. Then, include a `button_override` object. Learn more about `button_override` below.

 |  |
| 

`button_override`

 | Object | 

In the `group_button` field group, this sets the button's URL behavior when `override_product_button` is set to `true`.

Includes the following fields:

*   `no_follow`: boolean field for the link's [no\_follow](https://ahrefs.com/blog/nofollow-links) behavior.
*   `open_link_in_new_tab`: boolean field for the link's open behavior.
*   `url`: an object that specifies the button's destination.

In the `url` field, you can set the type of destination through the `type` field, which supports the following content types:

*   `EXTERNAL`: a standard URL. Include the URL in an `href` field.
*   `CONTENT`: a HubSpot page. Include the page ID in a `content_id` field.
*   `PAYMENT`: a payment link. Include the payment link in an `href` field.
*   `EMAIL_ADDRESS`: an email address. Include the address in an `href` field.

 |  |
| 

`group_name`

 | Field group | 

By default, the module will display the product name at the top of the module as an h3. To customize the name, include this optional field group along with the following fields:

*   `heading_level`: the heading size. Can be `h1` - `h6`.
*   `override_product_name`: set to `true` to specify text rather than the product name.
*   `name_override`: the string that you want to display at the top of the module.

 |  |
| 

`group_description`

 | Field group | 

By default, the module will display the product's set description. To customize the description, include this optional field group along with the following fields:

*   `override_product_description`: set to `true` to customize the product description.
*   `description_override`: a string containing your new description.

 |  |
| 

`group_image`

 | Field group | 

By default, the module will display the product's set image. To customize this image, include this optional field group with the following fields:

*   `override_product_image`: set to `true` to specify a new image. 
*   `image_override`: an object that specifies the new image, including the following properties:
    *   `alt`
    *   `height`
    *   `loading`
    *   `src`
    *   `width`

 |  |

Quote download[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#quote-download)
----------------------------------------------------------------------------------------------------------------

Supported in quote templates.

{% module "download" path="@hubspot/quote\_download" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`button_text`

 | String | 

The text displayed on the download button.

 | `Download` |
| 

`download_error`

 | String | 

Error message displayed if the download fails.

 | `There was a problem downloading the quote. Please try again.` |

Quote payment[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#quote-payment)
--------------------------------------------------------------------------------------------------------------

Supported in quote templates.

{% module "payment" path="@hubspot/quote\_payment" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`heading_text`

 | String | 

The heading displayed above the payment section of a quote template.

 | `Payment` |
| 

`heading_tag`

 | Choice | 

The type of heading used to display `heading_text`. Values include `h1`, `h2`, `h3`, `h4`, `h5`, `h6`.

 | `h3` |
| 

`checkout`

 | String | 

The payment button text.

 | `Pay now` |
| 

`needs_signature`

 | String | 

Button text when a signature is required.

 | `Payment can't be made because the quote isn't fully signed.` |
| 

`checkout_error`

 | Rich text | 

Message that displays when there's an error during checkout.

 | `There was a problem setting up checkout. Please contact the person who sent you this quote.` |
| 

`payment_status_error`

 | Rich text | 

Message that displays when there's an error when trying to make a payment.

 | `There was a problem loading the payment status for this quote. Please try refreshing the page.` |
| 

`paid`

 | String | 

A successful payment status indicator.

 | `Paid` |
| 

`payment_processing`

 | String | 

A payment processing status indicator.

 | `Payment processing` |

Quote signature[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#quote-signature)
------------------------------------------------------------------------------------------------------------------

Supported in quote templates.

{% module "signature" path="@hubspot/quote\_signature" %}

When a quote requires an e-signature, the following fields are available within an `esignature` object:

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`pretext`

 | Rich text | 

E-signature explanation text.

 | `Before you sign this quote, an email must be sent to you to verify your identity. Find your profile below to request a verification email.` |
| 

`verify_button`

 | String | 

Text that displays on the verification button.

 | `Verify to sign` |
| 

`failure`

 | String | 

Alert text that displays when the signature information can't be retrieved.

 | `There was a problem retrieving the signature information. Please reload the page.` |
| 

`verification_sent`

 | String | 

A status indicator that appears when the verification request has been successfully sent to the quote signer.

 | `Verification sent` |
| 

`signed`

 | String | 

Text that displays when the quote has been successfully signed.

 | `Signed` |

When a quote requires a printed signature, the following fields are available within a `print_signature` object:

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | Rich text | 

Text displayed at the top of the signature section.

 | `Signature` |
| 

`signature`

 | String | 

Text that displays next to the signature field.

 | `Signature` |
| 

`date`

 | String | 

Text that displays next to the date field.

 | `Date` |
| 

`printed_name`

 | String | 

Text that displays next to the printed name field.

 | `Printed name` |
| 

`countersignature`

 | Object | 

An object containing content for the countersignature section. This object can contain the following fields:

*   `header`: text that displays at the top of the countersignature section.
*   `countersignature`: Text that displays next to the countersignature field.
*   `date`: text that displays next to the date field.
*   `printed_name`: text that displays next to the printed name field.

 | `Signed` |

Line items[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#line-items)
--------------------------------------------------------------------------------------------------------

Supported in quote templates. This module also includes the default text used on custom quotes. 

{% module "module\_165350106057652" path="@hubspot/line\_items", label="line\_items.module" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`title`

 | Text | 

The title of the line item column. 

 | `Column description` |
| 

`use_additional_product_property`

 | Boolean | 

Display checkbox to allow users to select additional line item columns from product properties. 

 | `False` |
| 

`additional_product_properties`

 | Choice | 

A product property. Choices include: 

*   `price`: price of line item. 
*   `item_description`: description of line item. 
*   `quantity`: number of line items. 
*   `amount`: total cost of line items. 
*   `hs_recurring_billing_start_date`: billing start date for recurring line items. 
*   `discount`: discount amount applies to the line item. 

 |  |
| 

`crm_product_property`

 | CRM object property | 

Select any product property to appear as a line item column header. 

 |  |

Rich text[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#rich-text)
------------------------------------------------------------------------------------------------------

Supported in all template types.

{% module "rich\_text" path="@hubspot/rich\_text" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`html`

 | Rich Text | 

HTML block.

 | `<h2>Something Powerful</h2>\n<h3>Tell The Reader More</h3>\n<p>The headline and subheader tells us what you're <a href=\"#\">offering</a>, and the form header closes the deal. Over here you can explain why your offer is so great it's worth filling out a form for.</p>\n<p>Remember:</p>\n<ul>\n<li>Bullets are great</li>\n<li>For spelling out <a href=\"#\">benefits</a> and</li>\n<li>Turning visitors into leads.</li>\n</ul>` |

RSS listing[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#rss-listing)
----------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "rss\_listing" path="@hubspot/rss\_listing" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`title`

 | Text | 

An H3 heading.

 | `"Test"` |
| 

`rss_feed_type`

 | Choice | 

Type of RSS feed. Choices include:

*   `blog` - HubSpot hosted blog.
*   `external` - An external RSS feed.

 | `blog` |
| 

`rss_url`

 | Text | 

RSS URL to use when `rss_feed_type` equals `external`.

 |  |
| 

`content_group_id`

 | Blog | 

Id of the blog to use when `rss_feed_type` equals `blog`.

 |  |
| 

`topic_id`

 | Tag | 

(optional) Id of the tag to filter by when `rss_feed_type` equals `blog`.

 |  |
| 

`number_of_items`

 | Number | 

Maximum number of posts to display.

 | `5` |
| 

`include_featured_image`

 | Boolean | 

Include the featured image.

 | `false` |
| 

`show_author`

 | Boolean | 

Show the author name.

 | `true` |
| 

`attribution_text`

 | Text | 

Text that attributes an author to a post. Displayed when `show_author` equals `true`.

 | `"by"` |
| 

`show_detail`

 | Boolean | 

Show post summary text.

 | `true` |
| 

`limit_to_chars`

 | Number | 

Limits the length of the summary text when `show_detail` equals `true`.

 | `200` |
| 

`click_through_text`

 | Text | 

The text which will be displayed for the clickthrough link at the end of a post summary when `show_detail` equals `true`.

 | `"Read more"` |
| 

`show_date`

 | Boolean | 

Show publish date.

 | `true` |
| 

`publish_date_format`

 | Choice | 

Format for the publish date when `show_date` equals `true`. Choices include:

*   `short` (ex: 06/11/06 12:00PM)
*   `medium` (ex: Jun 6, 2006 12:00:00 pm)
*   `long` (ex: June 6, 2017 12:00:00 pm EDT)
*   `MMMM d, yyyy 'at' h:mm a` (ex: June 6, 2006 at 12:00 pm)
*   `h:mm a 'on' MMMM d, yyyy` (ex: 12:00 pm on June 6, 2006)

 | `short` |
| 

`publish_date_text`

 | Text | 

The text that indicates when a post was published when `show_date` equals `true`.

 | `"posted at"` |

Site search input[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#site-search-input)
----------------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "search\_input" path="./local-search\_input" placeholder="Search" include\_search\_button=true results={ "use\_custom\_search\_results\_template": "true", "path\_id": "77977569400" } %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`field_label`

 | Text | 

Search input label text

 |  |
| 

`placeholder`

 | Text | 

Placeholder text for the input field.

 | `"Search"` |
| 

`include_search_button`

 | Boolean | 

Include a search button.

 | `false` |
| 

`content_types`

 | Object | 

Which content types to include in search results. Object contains the following keys with boolean values:

*   `website_pages`
*   `landing_pages`
*   `blog_posts`
*   `knowledge_articles`

 | `{ "website_pages": true, "landing_pages": false, "blog_posts": true, "knowledge_articles": false }` |
| 

`results`

 | Object | An object that enables controls for using a custom search results page. Includes the following properties:  

*   `use_custom_search_results_template` **(boolean):** when set to `true`, users can select a custom search results page. Default is `false`.
*   `path_id` **(string):** the ID of the page that will be used for search results. The referenced page must contain the search results module.

 |  |

Search results[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#search-results)
----------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "search\_results" path="@hubspot/search\_results" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`display_featured_images`

 | Boolean | 

Display featured images for items.

 | `false` |

Section header[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#section-header)
----------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "section\_header" path="@hubspot/section\_header" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | Text | 

Section header content.

 | `"A clear and bold header"` |
| 

`heading_level`

 | Choice | 

Heading level for the `header`. Choices include `h1` through `h6`.

 | `h1` |
| 

`subheader`

 | Text | 

Subheading paragraph text for the section.

 | `"A more subdued subheader"` |

Simple menu[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#simple-menu)
----------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "simple\_menu" path="@hubspot/simple\_menu" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`menu_tree`

 | Simple Menu | 

Simple menu object.

 | `[]` |
| 

`orientation`

 | Choice | 

Orientation of the menu. Choices include:

*   `horizontal`
*   `vertical`

 | `horizontal` |

Social sharing[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#social-sharing)
----------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "social\_sharing" path="@hubspot/social\_sharing" %}

Note: The variable `social_link_url` in the default column below is the same value as the `link` parameter.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`link`

 | Text | 

This is the destination link that will be shortened for easier sharing on social networks.

 |  |
| 

`facebook`

 | Object | 

Object containing:

*   `enabled`: boolean to enable social item
*   `custom_link_format`: custom URL for socials sharer URL

 | `{ "enabled": false, "custom_link_format": "http://www.facebook.com/share.php?u={{ social_link_url }}" }` |
| 

`twitter`

 | Object | 

Object containing:

*   `enabled`: boolean to enable social item
*   `custom_link_format`: custom URL for socials sharer URL

 | `{ "enabled": false, "custom_link_format": "https://twitter.com/intent/tweet?original_referer={{ social_link_url }}&url={{ social_link_url }}&source=tweetbutton&text={{ social_page_title|urlencode }}" }` |
| 

`linkedin`

 | Object | 

Object containing:

*   `enabled`: boolean to enable social item
*   `custom_link_format`: custom URL for socials sharer URL

 | `{ "enabled": false, "custom_link_format": "http://www.linkedin.com/shareArticle?mini=true&url={{ social_link_url }}" }` |
| 

`pinterest`

 | Object | 

Object containing:

*   `enabled`: boolean to enable social item.
*   `custom_link_format`: custom URL for socials sharer URL.
*   `pinterest_media`: image object including:
    *   `src`: image URL.
    *   `alt`: alt-text for the image.

 | `{ "enabled": false, "custom_link_format": "http://pinterest.com/pin/create/button/?url={{ social_link_url }}&media={{ pinterest_media }}", "pinterest_media": { "src": "", "alt": null } }` |
| 

`email`

 | Object | 

Object containing:

*   `enabled`: boolean to enable social item
*   `custom_link_format`: custom URL for socials sharer URL

 | `{ "enabled": false, "custom_link_format": "mailto:?subject=Check out {{ social_link_url }} &body=Check out {{ social_link_url }}" }` |

One line of text[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#one-line-of-text)
--------------------------------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "text" path="@hubspot/text" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`value`

 | Text | 

Add your text to this parameter.

 | `"Some additional information in one line"` |

Video[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#video)
----------------------------------------------------------------------------------------------

Supported in pages, blog listings, and blog posts.

{% module "video" path="@hubspot/video" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`video_type`

 | Choice | 

Type of video. Choices include:

*   `embed`: embed code from an external source.
*   `hubspot_video`: HubSpot hosted video.

 | `embed` |
| 

`hubspot_video`

 | Video Player | 

HubSpot hosted video. Used when `video_type` equals `hubspot_video`.

 |  |
| 

`embed_field`

 | Embed | 

Supports embed types:

*   `oembed`
    *   `video`: URL for video.
*   `html`: embed code for video.

 |  |
| 

`oembed_thumbnail`

 | Image | 

Override oembed thumbnail image when `video_type` equals `embed` and `embed_field` equals `oembed`.

 |  |
| 

`style_options`

 | Object | 

Object containing `oembed_thumbnail_play_button_color` - Color field.

 | `{"oembed_thumbnail_play_button_color":"#ffffff"}` |
| 

`placeholder_fields`

 | Object | 

Object containing:

*   `placeholder_title`: text field.
*   `placeholder_description`: text field.

 | `{"placeholder_title":"No video selected", "placeholder_description":"Select a video type in the sidebar."}` |

Video embed (landing page)[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#video-embed-landing-page-)
---------------------------------------------------------------------------------------------------------------------------------------

Supported in pages.

{% module "video\_embed\_lp" path="@hubspot/video\_embed\_lp" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`url`

 | Text | 

URL for video. URLs from Vimeo and YouTube are supported.

 | `"https://www.youtube.com/watch?v=X1Rr5BFO5rg"` |
| 

`is_full_width`

 | Boolean | 

Sets the video to full width (`true`) or manually set width and height (`false`).

 | `true` |
| 

`max_width`

 | Number | 

Max width (px)

 | `800` |
| 

`max_height`

 | Number | 

Max height (px)

 | `450` |

WhatsApp link[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#whatsapp-link)
--------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listing pages. Requires a [connected WhatsApp channel](https://knowledge.hubspot.com/inbox/connect-whatsapp-to-the-conversations-inbox).

{% module "whatsapp\_link" path="@hubspot/whatsapp\_link", label="whatsapp\_link" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`whatsapp_number`

 | URL | 

Select from the [WhatsApp channels connected to the account](https://knowledge.hubspot.com/inbox/connect-whatsapp-to-the-conversations-inbox).

 |  |
| 

`optin_text`

 | Choice | The [opt-in and opt-out text](https://knowledge.hubspot.com/inbox/collect-consent-for-whatsapp-conversations#subscribe-a-contact-using-opt-in-keywords-in-a-whatsapp-thread). |  |
| 

`whatsapp_display`

 | Choice | 

Select whether the button displays text, a WhatsApp icon, or both. Choices include:

*   `text_and_icon`
*   `text`
*   `icon`

 | `text_and_icon` |
| 

`icon_position`

 | Choice | 

The position of the icon on the button. Choices include `left` and `right`.

 | `left` |
| 

`button_text`

 | String | 

The button's text.

 | `Chat on WhatsApp` |
| 

`whatsapp_icon_title`

 | String | 

The icon text for screen readers.

 | `WhatsApp Icon` |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-modules#page-feedback)
--------------------------------------------------------------------------------------------------------------------

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