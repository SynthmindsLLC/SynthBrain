Default email modules


=========================

Last updated: August 28, 2023

Below, learn about the modules that you can use when building email templates.

These modules are separate from [default web modules](/docs/cms/building-blocks/modules/default-modules), which can be used to build website pages, blog posts, and blog listing pages. Many of the modules below were released to replace usage of default web modules in emails, such as the `email_logo` module replacing the `logo` module. If your email templates are still using the web versions of these modules, learn how to [update your email templates to use email-specific modules instead](/docs/cms/update-email-templates-to-use-default-email-modules).

To view a default module's code, you can view and clone the module within the `@hubspot` folder of the design manager, or [fetch it](/docs/cms/developer-reference/local-development-cli#fetch-files) by its path locally using the HubSpot CLI.

![design-manager-default-modules](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/design-manager-default-modules.png?width=401&name=design-manager-default-modules.png)

Email blog post filter[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-blog-post-filter)
--------------------------------------------------------------------------------------------------------------------------------------

A version of the [blog post filter](#blog-post-filter) module for emails.

{% module "post\_filter" path="@hubspot/email\_post\_filter" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | Blog | 

The blog to display posts from.

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

Email blog post listing[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-blog-post-listing)
----------------------------------------------------------------------------------------------------------------------------------------

A version of the [blog post listing](#blog-post-listing) module for emails.

{% module "post\_listing" path="@hubspot/email\_post\_listing" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`select_blog`

 | Blog | 

The blog to display posts from.

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

Email Call-to-Action[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-call-to-action)
----------------------------------------------------------------------------------------------------------------------------------

A version of the [Call-to-Action](#call-to-action) module for emails.

{% module "cta" path="@hubspot/email\_cta" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`guid`

 | String | 

Globally Unique Identifier of the CTA. 

 |  |

Email header[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-header)
------------------------------------------------------------------------------------------------------------------

A version of the [header](#header) module for emails.

{% module "email\_header" path="@hubspot/email\_header" %}

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

Email HTML[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-html)
--------------------------------------------------------------------------------------------------------------

Raw HTML module for emails.

{% module "raw\_html\_email" path="@hubspot/raw\_html\_email" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`html`

 | HTML | 

HTML block.

 | `<p>\n Add custom HTML to your email.\n</p>` |

Email image[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-image)
----------------------------------------------------------------------------------------------------------------

Image module for emails.

{% module "image\_email" path="@hubspot/image\_email" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`img`

 | Image | 

Image to be used for the email. 

 |  |
| 

`link`

 | Text | 

Optional link for the image.

 |  |
| 

`alignment`

 | Choice | 

Alignment of the image. Choice include:

*   `left`
*   `center`
*   `right`

 | `center` |

Email linked image[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-linked-image)
------------------------------------------------------------------------------------------------------------------------------

A version of the [image](#image) module for emails.

{% module "email\_linked\_image" path="@hubspot/email\_linked\_image" %}

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

Email logo[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-logo)
--------------------------------------------------------------------------------------------------------------

A version of the [logo](#logo) module for emails.

{% module "logo" path="@hubspot/email\_logo" %}

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

Optional link for the logo. If no url is specified, your logo will link to your primary domain.

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

Main email body[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#main-email-body)
------------------------------------------------------------------------------------------------------------------------

The main body module for emails.

{% module "email\_body" path="@hubspot/email\_body" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`html`

 | Rich Text | 

Default content for the email body. Supports HTML. See below for this field's default value.

 |  |

<!-- Default html field value --> <p>Hi&nbsp;{{contact.firstname}},</p>\\n<p>Describe what you have to offer the customer. Why should they read? What did you promise them in the subject line? Tell them something cool. Make them laugh. Make them cry. Well, maybe don't do that...</p>\\n<p>Use a list to:</p>\\n<ul>\\n<li>Explain the value of your offer</li>\\n<li>Remind the reader what they’ll get out of taking action</li>\\n<li>Show off your skill with bullet points</li>\\n<li>Make your content easy to scan</li>\\n</ul>\\n<p><a href=\\"http://hubspot.com\\">LINK TO A LANDING PAGE ON YOUR SITE</a> (This is the really important part.)</p>\\n<p>Now wrap it all up with a pithy little reminder of how much you love them.</p>\\n<p>Aw. You silver-tongued devil, you.</p>\\n<p>Sincerely,</p>\\n<p>Your name</p>

Office location information[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#office-location-information)
------------------------------------------------------------------------------------------------------------------------------------------------

Office location information footer for emails (CAN-SPAM compliant).

{% module "email\_can\_spam" path="@hubspot/email\_can\_spam" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`html`

 | Rich Text | 

Populates required CAN-SPAM information for emails including business address and unsubscribe/preferences links.

See below for this field's default value.

 |  |

<!-- Default html field value --> <p id=\\"footer\\" style=\\"font-family: Geneva, Verdana, Arial, Helvetica, sans-serif; text-align: center; font-size: 12px; line-height: 1.34em; color: {{ secondary\_font\_color }}; display: block;\\">{{ site\_settings.company\_name }} &nbsp;&nbsp;{{ site\_settings.company\_street\_address\_1 }} &nbsp;{{ site\_settings.company\_street\_address\_2 }} &nbsp;{{ site\_settings.company\_city }} &nbsp;{{ site\_settings.company\_state }} &nbsp;&nbsp;{{ site\_settings.company\_zip }} &nbsp;&nbsp;{{ site\_settings.company\_country }} <br><br> You received this email because you are subscribed to {{ subscription\_name }} from {{ site\_settings.company\_name }} . <br><br> Update your <a target=\\"\_blank\\" href=\\"{{ unsubscribe\_link }}\\" style=\\"text-decoration: underline; whitespace: nowrap; color: {{ secondary\_font\_color }};\\" data-unsubscribe=\\"true\\">email preferences</a> to choose the types of emails you receive. <br><br> &nbsp;<a target=\\"\_blank\\" href=\\"{{ unsubscribe\_link\_all }}\\" style=\\"text-decoration: underline; whitespace: nowrap; color: {{ secondary\_font\_color }};\\" data-unsubscribe=\\"true\\">Unsubscribe from all future emails</a> &nbsp;</p>

Email one line of text[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-one-line-of-text)
--------------------------------------------------------------------------------------------------------------------------------------

A version of the [text](#one-line-of-text) module for emails.

{% module "text" path="@hubspot/email\_text" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`value`

 | Text | 

Add your text to this parameter.

 | `"Some additional information in one line"` |

Email section header[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-section-header)
----------------------------------------------------------------------------------------------------------------------------------

A version of the [section header](#section-header) module for emails.

{% module "section\_header" path="@hubspot/email\_section\_header" %}

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

Email social sharing[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-social-sharing)
----------------------------------------------------------------------------------------------------------------------------------

A version of the [social sharing](#social-sharing) module for emails.

{% module "social\_sharing" path="@hubspot/email\_social\_sharing" %}

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

Email subscription preferences[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-subscription-preferences)
------------------------------------------------------------------------------------------------------------------------------------------------------

Module for displaying email subscription preferences.

{% module "email\_subscriptions" path="@hubspot/email\_subscriptions" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | Text | 

H1 heading.

 | `header` |
| 

`subheader_text`

 | Rich Text | 

Supplemental text for your H1 heading.

 | `"If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you."` |
| 

`unsubscribe_single_text`

 | Text | 

Preference selection help text.

 | `"Uncheck the types of emails you do not want to receive:"` |
| 

`unsubscribe_all_text`

 | Text | 

Unsubscribe all help text. 

 | `"Or check here to never receive any emails:"` |
| 

`unsubscribe_all_unsubbed_text`

 | Text | 

Unsubscribe all help text for a currently unsubbed user.

 | `"You are presently unsubscribed from all of our emails. Would you like to receive our emails again?"` |
| 

`unsubscribe_all_option`

 | Text | 

Label for unsubscribe all option.

 | `"Unsubscribe me from all mailing lists."` |
| 

`button_text`

 | Text | 

Update preferences button text.

 | `"Update email preferences"` |
| 

`resubscribe_button_text`

 | Text | 

Resubscribe button text.

 | `"Yes, resubscribe me!"` |

Email subscriptions confirmation message[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-subscriptions-confirmation-message)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Confirmation of email subscription changes.

{% module "email\_subscriptions\_confirmation" path="@hubspot/email\_subscriptions\_confirmation" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | Text | 

H1 heading.

 |  |
| 

`subheader_text`

 | Rich Text | 

Supplemental text for your H1 heading.

 | `"If this is not your email address, please ignore this page since the email associated with this page was most likely forwarded to you."` |
| 

`unsubscribe_all_success`

 | Text | 

Message on unsubscribe.

 | `"You have successfully unsubscribed from all email communications."` |
| 

`subscription_update_success`

 | Text | 

Message on subscription update.

 | `"You have successfully updated your email preferences."` |

Email unsubscribe (backup)[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-unsubscribe-backup-)
---------------------------------------------------------------------------------------------------------------------------------------------

Supported in pages, blog posts, and blog listings.

{% module "email\_simple\_subscription" path="@hubspot/email\_simple\_subscription" %}

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`header`

 | Text | 

H1 heading.

 | `"Email Unsubscribe"` |
| 

`input_help_text`

 | Text | 

H3 heading for help text.

 | `"Your email address:"` |
| 

`input_placeholder`

 | Text | 

Placeholder content for the input field.

 | `"email@example.com"` |
| 

`button_text`

 | Text | 

Text to display on the unsubscribe button.

 | `"Unsubscribe"` |

Email video[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#email-video)
----------------------------------------------------------------------------------------------------------------

A video module for emails.

{% module "video\_email" path="@hubspot/video\_email" %}

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

`embed`

 | Object | 

Object containing `source_type`. Only value of `oembed` is available. 

 | `{ "source_type": "oembed" }` |
| 

`oembed_thumbnail`

 | Image | 

Override oembed thumbnail image when `video_type` equals `embed` and `embed_field` equals `oembed`.

 | `{"size_type": "exact"}` |
| 

`style_options`

 | Object | 

Object containing:

*   `play_button_color`: color hex code.
*   `play_button_scale`: number 0-100

 | `{ {"play_button_color":{ "color":"#2f4254", "opacity":100},"play_button_scale" : 30} }` |
| 

`alignment`

 | Choice | 

Alignment of video. Choices include:

*   `left`
*   `center`
*   `right`

 | `center` |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules/default-email-modules#page-feedback)
--------------------------------------------------------------------------------------------------------------------------

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