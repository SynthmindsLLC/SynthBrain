---
Please provide me with the rest of the mission statement so I can help you complete it! 

For example, tell me: "* **What is the mission for?** (A company, a project, a personal goal?)"
* **What are the key values or goals?** (What does this mission aim to achieve?) 
* **Who is the target audience?** (Who will benefit from this mission?)

Once you give me more information, I can help you craft a compelling and impactful mission statement.
---

HubL variables


==================

Last updated: April 6, 2023

HubSpot templates can use a host of predefined variables that can be used to render useful website and email elements. This page is a reference listing of those variables.  [Learn more about creating your own variables](/docs/cms/hubl/variables-macros-syntax) in a [HubL template](/docs/cms/building-blocks/templates/html-hubl-templates) or [module](/docs/cms/building-blocks/modules).

While most of the variables listed on this page are optional, there are a few variables that are required, in order to create emails and pages from your templates.

The variables listed below can be used individually by wrapping them in the `}}` delimiter as noted on our [Variables and Macros page](/docs/cms/hubl/variables-macros-syntax). You can optionally use these variables with other parts of the HubL Templating Language such as [loops](/docs/cms/hubl/for-loops), [filters](/docs/cms/hubl/filters), [functions](/docs/cms/hubl/functions), [tags](/docs/cms/hubl/tags), and more.

Required email template variables[](https://developers.hubspot.com/docs/cms/hubl/variables#required-email-template-variables)
-----------------------------------------------------------------------------------------------------------------------------

To be [CAN-SPAM](https://knowledge.hubspot.com/email/can-i-customize-my-can-spam-email-footer) compliant, all emails sent through HubSpot require certain company and opt-out information; therefore, HubSpot email templates require certain variables. There are additional email variables that are optional which are listed [further down this page](#email-variables).

| Variable | Type | Description |
| --- | --- | --- |
| 
`site_settings.company_city`

 | String | 

Prints the company city (set in **Settings > Marketing > Email > Configuration > Footer**).

 |
| 

`site_settings.company_name`

 | String | 

Prints the company name (set in **Settings > Marketing > Email > Configuration > Footer**).

 |
| 

`site_settings.company_state`

 | String | 

Prints the company state (set in **Settings > Marketing > Email > Configuration > Footer**).

 |
| 

`site_settings.company_street_address_1`

 | String | 

Prints the company address (set in **Settings > Marketing > Email > Configuration > Footer**).

 |
| 

`unsubscribe_link`

 | String | 

Prints the URL of the page that allows recipients to manage subscription preferences or unsubscribe from email communications. This variable should be used in the href attribute of an <a>.

 |

Required page template variables[](https://developers.hubspot.com/docs/cms/hubl/variables#required-page-template-variables)
---------------------------------------------------------------------------------------------------------------------------

To publish a coded file as an editable page or blog template, the following variables must be included. If you want to publish an HTML file without these variables, to use within another template, you can do so by unchecking the option "Make this template available for new content". 

| Variable | Type | Description |
| --- | --- | --- |
| 
`standard_footer_includes`

 | String | 

Renders the [HubSpot tracking code](/docs/cms/building-blocks/templates#hubspot-tracking-code) and any other code included in your Footer HTML in [**Content Settings**](https://app.hubspot.com/l/settings/website/pages/all-domains/page-templates) or the options of a particular page. This tag should be inserted directly before the closing body tag.

 |
| 

`standard_header_includes`

 | String | 

Adds [jQuery, layout.css](/docs/cms/building-blocks/templates#included-cms-files), any attached stylesheets, a meta viewport tag, Google Analytics tracking code, other page meta information, and code added to the head tag at the domain/template/page level. This variable should be added to the <head> of HTML templates.

 |

Variables available in all templates[](https://developers.hubspot.com/docs/cms/hubl/variables#variables-available-in-all-templates)
-----------------------------------------------------------------------------------------------------------------------------------

Many predefined HubSpot variables can be used in email, page, or blog templates. Below is a list of these variables.

_(Note: If you want to see additional information what these variables can output, [try using the pprint parameter](/docs/cms/hubl/filters#pprint))_

### General variables[](https://developers.hubspot.com/docs/cms/hubl/variables#general-variables)

The following variables will render on any type of content.

| Variable | Type | Description |
| --- | --- | --- |
| 
`account`

 | Dict | 

This variable is a dictionary that stores company personalization properties for a known contact. Properties can be accessed from this dict, by adding a period and the property name. For example, `account.name` would print the company name of a contact.  
_Use of this variable will disable page caching._ 

 |
| 

`company_domain`

 | String | 

Prints the company domain from **Website** **> Pages > Branding > Logo Link**.

 |
| 

`contact`

 | Dict | 

This variable is a dictionary that stores contact personalization properties for a known contact. Properties can be accessed from this dict, by adding a period and the property name. For example, `contact.firstname` would print the first name of a contact.  
_Use of this variable will disable page caching._ 

 |
| 

`content`

 | Dict | 

This variable is a dictionary that stores various properties pertaining to a specific piece of content such as an email, a page, or a post.

 |
| 

`content.absolute_url`

 | String | 

Prints the full URL of a page, post, or web page version of an email.

 |
| 

`content.archived`

 | Boolean | 

This variable evaluates to True, if the page or email was marked as archived by the user.

 |
| 

`content.author_email`

 | String | 

The email address of the content creator.

 |
| 

`content.author_name`

 | String | 

The first and last name of the content creator.

 |
| 

`content.author_username`

 | String | 

The HubSpot username of the content creator.

 |
| 

`content.campaign`

 | String | 

The GUID for the marketing campaign that this page or email is associated with. This unique ID can be found in the URL of a particular campaign in the Campaign's tool.

 |
| 

`content.campaign_name`

 | String | 

The name of the marketing campaign that this page, this post, or this email is associated with.

 |
| 

`content.created`

 | Datetime | 

A datetime object for when the content was originally created, in UTC time. This variable can be formatted with the [datetime filter](/docs/cms/hubl/filters#datetimeformat).

 |
| 

`content.meta_description`

 | String | 

When pulling the meta description of a page, it is better to use the variable `page_meta.meta_description`.

 |
| 

`content.name`

 | String | 

The name of a post, email, or page. For pages and emails this will print the internal content name, while for posts this will print the post title. For blog posts, this is the post title that displays. For other types of content, this is generally an internal name. This variable includes a wrapper so that it is editable via the UI, when included in blog posts. If you want to print the content name without a wrapper, use page\_meta.name.

 |
| 

`content.publish_date`

 | Datetime | 

A datetime object representing when the content was published, in UTC time. This variable can be formatted with the [format\_datetime filter](/docs/cms/hubl/filters#format-datetime).

 |
| 

`content.publish_date_localized`

 | String | 

A string representing the datetime when the content was published using the time zone defined in the account's [default settings](https://knowledge.hubspot.com/account/change-your-language-and-region-settings). This variable is also subject to the language and  date format settings in **Settings > Website > Blog > Date Formats**.

 |
| 

`content.template_path`

 | String | 

The Design Manager file path to your template (ie `custom/page/web_page_basic/my_template.html`).

 |
| 

`content.updated`

 | Datetime | 

A datetime object for when the user last updated the content, in UTC time. This variable can be formatted with the datetime filter. _Does not equal_ `content.publish_date` _on initial publish. Use_ [`|between_times`](/docs/cms/hubl/filters#between-times) _filter to test if a post has been updated after publishing._

 |
| 

`content_id`

 | String | 

Prints the unique ID for a page, post, or email. This ID can be found in the URL of the editor. You can use this variable as an alias for content.id.

 |
| 

`favicon_link`

 | String | 

Prints the source URL of the favicon. This image is set in **Settings > Website > Pages > Branding**.

 |
| 

`hub_id`

 | String | 

The portal ID of your HubSpot account.

 |
| 

`hubspot_analytics_tracking_code`

 | String | 

Includes the analytics tracking code. This tag is not necessary, because `standard_footer_includes`, already renders the tracking code.

 |
| 

`local_dt`

 | Datetime | 

A datetime object of the current time in the time zone defined in your Report Settings. _Usage of this variable will disable page caching in order to return the current time. May hurt page performance. Use JavaScript instead to get current date and time in a cacheable way._

 |
| 

`local_time_zone`

 | String | 

The time zone, as configured in your HubSpot Report Settings.

 |
| 

`page_meta.canonical_url`

 | String | 

The official URL that this page should be accessed at. Usually does not include any query string parameters. Use this for the `rel="canonical"` tag. HubSpot automatically canonicalizes URLs.

 |
| 

`page_meta.html_title`

 | String | 

The title of the page. This variable should be used in the `<title>` tag of HTML templates.  

 |
| 

`page_meta.meta_description`

 | String | 

The meta description of a page. This variable should be used in the "description" `<meta>` tag of HTML templates.

 |
| 

`page_meta.name`

 | String | 

An alias for `content.name`.

 |
| 

`portal_id`

 | String | 

An alias for hub\_id

 |
| 

`request_contact`

 | Dict | 

A dictionary containing data about the requested contact.  
_Use of this variable will disable page caching._ _Not available in email templates._

 |
| 

`site_settings`

 | Dict | 

The site\_settings dict contains various settings from such as colors and fonts (see below).

 |
| 

`year`

 | String | 

Prints the current year.

 |

Color and font settings[](https://developers.hubspot.com/docs/cms/hubl/variables#color-and-font-settings)
---------------------------------------------------------------------------------------------------------

There are several basic color and font controls in **Settings > Marketing > Configuration > Color** that can be printed to templates and files. Please note that if you use these variables in CSS files, you will need to republish/recompile your CSS file when you change one of the settings, for the new color to apply.

| Variable | Type | Description |
| --- | --- | --- |
| 
`site_settings.background_color`

 | Dict | 

Background color setting from **Settings > Marketing > Email > Configuration > Color**. Prints a HEX value.

 |
| 

`site_settings.body_border_color`

 | String | 

Body border color setting from **Settings > Marketing > Email > Configuration > Color**. This option becomes available when you select "Manually set email border color" under the "Border Color Options" dropdown. Prints a HEX value.

 |
| 

`site_settings.body_border_color_choice`

 | Enumeration | 

The variable is used in HubSpot's default email templates to determine whether or not a border should be added. The setting is controlled in **Content Settings > Colors and Fonts**. It prints values: BORDER\_AUTOMATIC, BORDER\_MANUAL, BORDER\_NONE

 |
| 

`site_settings.body_color`

 | String | 

Body color setting from **Settings > Marketing > Email > Configuration > Color**. Prints a HEX value.

 |
| 

`site_settings.color_picker_favorite_1`

 | String | 

Favorite color 1 setting from **Settings > Marketing > Email > Configuration > Color.** Prints a HEX value. Replace 1 with 2-6 to modify the tag for other favorite color settings.

 |
| 

`site_settings.primary_accent_color`

 | String | 

Primary accent color setting from **Settings > Marketing > Email > Configuration > Color**. Prints a HEX value.

 |
| 

`site_settings.primary_font`

 | Enumeration | 

Primary font setting from **Settings > Marketing > Email > Configuration > Font**. Prints value from dropdown.

 |
| 

`site_settings.primary_font_color`

 | String | 

Primary font color setting from **Settings > Marketing > Email > Configuration > Font**. Prints a HEX value.

 |
| 

`site_settings.primary_font_size`

 | String | 

Primary font size setting from **Settings > Marketing > Email > Configuration > Font**. Includes "px".

 |
| 

`site_settings.secondary_accent_color`

 | String | 

Secondary font color setting from **Settings > Marketing > Email > Configuration > Color** Prints a HEX value.

 |
| 

`site_settings.secondary_font`

 | Enumeration | 

Secondary font setting from **Settings > Marketing > Email > Configuration > Font**. Prints value from dropdown.

 |
| 

`site_settings.secondary_font_color`

 | String | 

Secondary font color setting from **Settings > Marketing > Email > Configuration > Font** Prints a HEX value.

 |
| 

`site_settings.secondary_font_size`

 | String | 

Primary font size setting from **Settings > Marketing > Email > Configuration > Font**. Includes "px".

 |

Email variables[](https://developers.hubspot.com/docs/cms/hubl/variables#email-variables)
-----------------------------------------------------------------------------------------

The following variables are specifically for HTML email templates or HubL template modules in email layouts.

| Variable | Type | Description |
| --- | --- | --- |
| 
`background_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`body_border_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`body_border_color_choice`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`body_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`content.create_page`

 | Boolean | 

This variable is True, if there is a web page version of the email.

 |
| 

`content.email_body`

 | Richtext | 

The main body of the email. This variable renders a rich text module.

 |
| 

`content.emailbody_plaintext`

 | String | 

The optional override of the plain text email body

 |
| 

`content.from_name`

 | String | 

The from name of the email sender

 |
| 

`content.reply_to`

 | String | 

The reply to address for the email

 |
| 

`content.subject`

 | String | 

The subject of the email

 |
| 

`email_body_border_css`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`email_body_padding`

 | string | 

The email body padding setting. This setting is located in **Settings > Marketing > Email > Configuration > Size.**

 |
| 

`email_body_width`

 | String | 

The email body width setting. This setting is located in **Settings > Marketing > Email > Configuration > Size**.

 |
| 

`primary_accent_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`primary_font`

 | Enumeration | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`primary_font_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`primary_font_size`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`primary_font_size_num`

 | String | 

Prints the font size number from **Settings > Marketing > Email > Configuration > Font**. Excludes "px".

 |
| 

`secondary_accent_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`secondary_font`

 | Enumeration | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`secondary_font_color`

 | String | 

Email-template only alias for the [color and font setting described above](#color-and-font-settings).

 |
| 

`secondary_font_size_num`

 | String | 

Prints the font size number from **Settings > Marketing > Email > Configuration > Font**. Excludes "px".

 |
| 

`site_settings.company_street_address_2`

 | String | 

Prints the address line 2 from **Settings > Marketing > Email > Configuration > Footer**.

 |
| 

`site_settings.office_location_name`

 | String | 

Prints the office location name from **Settings > Marketing > Email > Configuration > Footer**.

 |
| 

`subscription_confirmation_url`

 | String | 

Prints the URL of the subscription preferences confirmation page. This URL is dynamically generated on send.

 |
| 

`subscription_name`

 | String | 

Prints the name of the Email Type specified for that email.

 |
| 

`unsubscribe_anchor`

 | String | 

Generates an anchor tag with the work "unsubscribe" linked to your unsubscribe page.

 |
| 

`unsubscribe_link_all`

 | String | 

Renders a link to unsubscribe from all email communications, as opposed to a link to manage subscription preferences.

 |
| 

`unsubscribe_section`

 | String | 

Renders an unsubscribe section that includes an unsubscribe link, as well as help text.

 |
| 

`view_as_page_section`

 | String | 

Generates a link with help text that leads to a webpage version of an email.

 |
| 

`view_as_page_url`

 | String | 

Generates a link that leads to a webpage version of an email.

 |

### Email Variables for Private Content Emails[](https://developers.hubspot.com/docs/cms/hubl/variables#email-variables-for-private-content-emails)

The following list of variables are only available inside of email templates that are used for [Private Content Email Templates.](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages#customize-your-membership-registration-page-and-email-templates)

Use this table to describe parameters / fields
| Variable | Type | Description |
| --- | --- | --- |
| 
`membership_company_name`

 | String | 

This is the company name listed in [**Private Content > General Settings**](https://app.hubspot.com/l/settings/content-membership/all-domains/general).

 |
| 

`membership_domain`

 | URL | 

This is the domain of the private content website.

 |
| 

`membership_registration_link`

 | URL | 

Link to the registration page for the private content website.

 |
| 

`membership_website_admin`

 | String | 

This is the website admin listed in [**Private Content > General Settings**](https://app.hubspot.com/l/settings/content-membership/all-domains/general).

 |
| 

`membership_password_saved_link`

 | URL | 

Link to the password saved page. The link will redirect the visitor to a random restricted page that they have access to.

 |
| 

`membership_password_reset_link`

 | URL | 

Link to the reset password page for the private content website.

 |

Website pages variables[](https://developers.hubspot.com/docs/cms/hubl/variables#website-pages-variables)
---------------------------------------------------------------------------------------------------------

The following variables are available for site pages, landing pages, system pages, and blogs. 

| Variable | Type | Description |
| --- | --- | --- |
| 
`builtin_body_classes`

 | String | 

This variable dynamicaly prints helpful classes that help differentiate the markup of content created with that template (ie type of content, content name, etc). This makes styling different types of content or particular pages easier. This variable should be used in the class attribute of the body tag on coded templates.

 |
| 

`request_contact.is_logged_in`

 | String | 

This variable defines whether or not the requesting contact is logged in to a website's gated content (see [control audience access documentation](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages) for further information). The value of this variable will return true if the requesting contact is logged in, and false if the requesting contact has logged out. A contact can be logged out by directing them to the URL `https://www.yourdomain.com/_hcms/mem/logout`.  
_Use of this variable will disable page caching._ 

 |
| 

`request_contact.list_memberships`

 | String | 

This variable returns a dict of ids that represents the lists of which the contact is a member.  
_Use of this variable will disable page caching._ 

 |
| 

`content.language`

 | Dict | 

This variable returns a dict of information about the language settings of a page. `{{ content.language.languageTag }}` returns the language identifier of a page (i.e. "en" or "es"). `{{ content.language.textDirection.value }}` returns the text direction of the language of the page (i.e. "rtl" or "ltr").

 |

HTTP request variables[](https://developers.hubspot.com/docs/cms/hubl/variables#http-request-variables)
-------------------------------------------------------------------------------------------------------

The following variables print information about the HTTP page request.

| Variable | Type | Description |
| --- | --- | --- |
| 
`request.cookies`

 | Dict | 

A dictionary of cookie names mapped to cookie values.  
_Use of this variable will disable page caching._ 

 |
| 

`request.domain`

 | String | 

The domain used to access this page

 |
| 

`request.full_url`

 | String | 

The URL used to access this page.

 |
| 

`request.path`

 | String | 

The path component of the URL

 |
| 

`request.path_and_query`

 | String | 

The path and query component of the URL

 |
| 

`request.query`

 | String | 

The query string component of the URL. request.query\_dict automatically splits the query strings into key value pairs, and is recommended over the raw query for most use-cases.

 |
| 

`request.query_dict`

 | Dict | 

The query string converted into a name->value dictionary.  


 |
| 

`request.referrer`

 | String | 

The HTTP referrer, the url of the page that linked to the current page.  
_Use of this variable will disable page caching._ 

 |
| 

`request.remote_ip`

 | String | 

The IP address of the visitor.  
_Use of this variable will disable page caching._

 |
| 

`request.scheme`

 | String | 

The protocol of the request (either http or https)

 |
| 

`request.search_engine`

 | String | 

The search engine used to find this page, if applicable. Ex: google, aol, live, yahoo, images.google, etc

 |
| 

`request.search_keyword`

 | String | 

The keyword phrase used to find this page, if applicable

 |
| 

`request.headers`

 | String | 

A dictionary of available request headers.

_Usage of this variable will disable page caching in order to interpret individualized headers for each request. May hurt page performance._

 |

Blog variables[](https://developers.hubspot.com/docs/cms/hubl/variables#blog-variables)
---------------------------------------------------------------------------------------

The following variables are available for blog templates. Some variables are only available for post listings, while others may only be available for blog posts.

| Variable | Type | Description |
| --- | --- | --- |
| 
`blog_author`

 | String | 

This variable contains blog author information for blog author listing pages. It can be used to create conditional logic to >[render markup for blog author listings](/docs/cms/building-blocks/templates/blog-template-markup#if-blog-author-statement). It also contains the following properties:

*   `blog_author.avatar`
*   `blog_author.bio`
*   `blog_author.display_name`
*   `blog_author.email`
*   `blog_author.facebook`
*   `blog_author.google_plus`
*   `blog_author.has_social_profiles`
*   `blog_author.linkedin`
*   `blog_author.twitter`
*   `blog_author.website`

 |
| 

`content.blog_post_author`

 | String | 

This variable contains individual blog post author information for a given post. It contains the following properties:

*   `content.blog_post_author.avatar`
*   `content.blog_post_author.bio`
*   `content.blog_post_author.display_name`
*   `content.blog_post_author.email`
*   `content.blog_post_author.facebook`
*   `content.blog_post_author.google_plus`
*   `content.blog_post_author.has_social_profiles`
*   `content.blog_post_author.linkedin`
*   `content.blog_post_author.slug`
*   `content.blog_post_author.twitter`
*   `content.blog_post_author.website`

 |
| 

`blog`

 | String | 

An alias for group.

 |
| 

`content.comment_count`

 | Integer | 

The number of comments for the current blog post. 

 |
| 

`content.comment_list`

 | String | 

A list of the comments for the current blog post.

 |
| 

`current_page_num`

 | Integer | 

The integer index of the current page of blog posts in the view. 

 |
| 

`content.featured_image`

 | String | 

The source URL of the featured image, selected when the blog was published.

 |
| 

`content.featured_image_alt_text`

 | String | 

The alt text of the featured image.

 |
| 

`last_page_num`

 | Integer | 

The integer index of the last page of blog posts in the view.

 |
| 

`next_page_num`

 | Integer | 

The integer index of the next page of blog posts in the view.

 |
| 

`content.next_post_featured_image`

 | String | 

The URL of the featured image of the next blog post, if one exists.

 |
| 

`content.next_post_featured_image_alt_text`

 | String | 

Alt text for the next post's featured image if alt text exists.

 |
| 

`content.next_post_name`

 | String | 

The name of the next blog post, if one exists.

 |
| 

`content.next_post_slug`

 | String | 

The URL slug of the next blog post, if one exists.

 |
| 

`content.post_body`

 | String | 

The body of the blog post.

 |
| 

`content.post_list_content`

 | String | 

The body blog post content, modified for the listing page. The final output is affected by summary settings in **Settings > Website > Blog**. If featured images are enabled in settings, this variable will remove any images above the read more separator automatically.

 |
| 

`content.post_list_summary_featured_image`

 | String | 

The featured image of post summaries to be used in listing templates. This variable is affected by the settings in **Settings > Website > Blog**.

 |
| 

`content.post_summary`

 | String | 

The blog post summary. This content is determined by the read more separator in the blog editor.

 |
| 

`content.previous_post_featured_image`

 | String | 

The URL of the featured image of the previous blog post, if one exists.

 |
| 

`content.previous_post_featured_image_alt_text`

 | String | 

Alt text for the previous post's featured image if alt text exists.

 |
| 

`content.previous_post_name`

 | String | 

The name of the previous blog post, if one exists.

 |
| 

`content.previous_post_slug`

 | String | 

The URL slug of the previous blog post, if one exists.

 |
| 

`content.publish_date_localized`

 | String | 

A string representing the date/time when the blog post was published, formatted according to the blog's language and date formatting settings.

 |
| 

`simple_list_page`

 | Boolean | 

A boolean to indicate whether the requested page is the 'all posts' page containing links to all blog posts.

 |
| 

`content.topic_list`

 | Dict | 

Can be used to render markup for a topic listing by looping through it. `{% for topic in content.topic_list %}` The items within contain the properties: `name` and `slug`.

 |
| 

`contents`

 | String | 

Contents is a sequence of your blog posts that are iterated through using a for loop, available on [blog listing pages (is\_listing\_view)](/docs/cms/building-blocks/templates/blog-template-markup#if-is-listing-view-statement). 

 |
| 

`contents.total_count`

 | Integer | 

Total number of posts in a listing (regular, topics, authors, etc.).

 |
| 

`contents.total_page_count`

 | Integer | 

Total number of pages of posts based on your number of posts per page.

 |
| 

`contents_topics`

 | String | 

Get a list of all blog topics in the contents sequence of posts.

 |
| 

`group`

 | Dict | 

The dictionary containing variables that pertain to an entire blog.

 |
| 

`group.absolute_url`

 | String | 

The base URL of a blog.

 |
| 

`group.allow_comments`

 | Boolean | 

Evaluates to True, if comments are allowed.

 |
| 

`group.description`

 | String | 

The meta description of the blog from **Settings > Website > Blog**. Used for the meta description on certain listing pages.

 |
| 

`group.header`

 | String | 

The header of the blog.

 |
| 

`group.html_title`

 | String | 

The title of this blog as it should appear in the `<title>` tag.

 |
| 

`group.id`

 | String | 

The unique ID of a blog. This ID can be found in the URL of the Blog Dashboard for a particular blog.

 |
| 

`group.language`

 | Dict | 

A dictionary containing information about a blog's language. `{{ group.language.languageTag }}`can be used in conditionals to render different content on the different language variations of a multi-language blog.

 |
| 

`group.public_title`

 | String | 

The title of this blog as it should appear at the top of rendered pages.

 |
| 

`group.show_summary_in_listing`

 | Boolean | 

A boolean from **Settings > Website > Blog** to indicate whether to show summaries in post listings.

 |
| 

`group.slug`

 | String | 

The path to this blog.

 |
| 

`group.use_featured_image_in_summary`

 | Boolean | 

A boolean from **Settings > Website > Blog** to indicate whether featured images are shown in post summaries.

 |
| 

`archive_list_page`

 | Boolean | 

Returns true if page is a blog archive page. Ex: `https://www.example.com/blog/archive/2020/02` would return `true`.

 |

CRM object dynamic pages[](https://developers.hubspot.com/docs/cms/hubl/variables#crm-object-dynamic-pages)
-----------------------------------------------------------------------------------------------------------

The following variables are used to [build dynamic pages with CRM objects](/docs/cms/data/dynamic-pages#crm-object-dynamic-pages). These variables are only available for CRM object dynamic pages.

| Variable | Type | Description |
| --- | --- | --- |
| 
`dynamic_page_crm_object`

 | Dict | 

The CRM object of the dynamic page that matches with the page request path. If the request is to the listing page, this value will be `null`.

 |
| 

`dynamic_page_crm_object_type_fqn`

 | String | 

The fully qualified name (FQN) of the crm object. The FQN is an assigned unique ID for the object, including portal ID and object name.  
  
The fqn can be used in the [`crm_objects` function.](/docs/cms/hubl/functions#crm-objects)

 |

HubDB variables[](https://developers.hubspot.com/docs/cms/hubl/variables#hubdb-variables)
-----------------------------------------------------------------------------------------

The following variables are used to build dynamic pages with [HubDB](/docs/cms/data/hubdb). These variables are only available for [HubDB dynamic pages](/docs/cms/data/dynamic-pages#hubdb-dynamic-pages).

| Variable | Type | Description |
| --- | --- | --- |
| 
`dynamic_page_hubdb_table_id`

 | Long | 

The ID of the table selected in the 'Advanced Settings\` tab of the page editor.

 |
| 

`dynamic_page_hubdb_row`

 | Dict | 

The HubDB row of the dynamic page that matches with the page request path. If the request is to the listing page, this value will be `null`.

 |
| 

`row.hs_id`

 | Long | 

The internal ID of a HubDB row.

 |
| 

`row.hs_name`

 | String | 

The name of the HubDB row.

 |
| 

`row.hs_path`

 | String | 

The path of the HubDB row. Used to resolve a request to one row in the table specified by `dynamic_page_hubdb_table_id`.

 |
| 

`row.hs_child_table_id`

 | Long | 

The child table ID of the HubDB row. Can be used to build nested templates.

 |
| 

`row.hs_parent_row`

 | Dict | 

The parent row of the HubDB row. Can only be used when using child tables for nested templates.

 |
| 

`dynamic_page_route_level`

 | Integer | 

Current depth of a page in a multi-level dynamic template. The value starts at `0` and increments with each additional table layer.

 |

Menu node variables[](https://developers.hubspot.com/docs/cms/hubl/variables#menu-node-variables)
-------------------------------------------------------------------------------------------------

The following variables are available to use on the object returned by the [HubL menu function](/docs/cms/hubl/functions#menu).

| Variable | Type | Description |
| --- | --- | --- |
| 
`node.label`

 | String | 

The menu label of the page.

 |
| 

`node.url`

 | String | 

URL of the page.

 |
| 

`node.pageId`

 | Number | 

ID of the page if within HubSpot.

 |
| 

`node.contentGroupId`

 | Number | 

Blog ID of the page if it is a HubSpot blog post.

 |
| 

`node.parentNode`

 | Object | 

The parent node of the current node. The parent node will have the current node in its `children` property.

 |
| 

`node.children`

 | List | 

The list of child nodes for the current node.

 |
| 

`node.activeBranch`

 | Boolean | 

True if the node is in the top-level branch that the current page is in.

 |
| 

`node.activeNode`

 | Boolean | 

True if the node is the current page.

 |
| 

`node.level`

 | Number | 

The number of levels deep the current node is from the top-level nodes.

 |
| 

`node.pageTitle`

 | String | 

Name of the content page if within HubSpot.

 |
| 

`node.slug`

 | String | 

Path slug of the page.

 |
| 

`node.linkTarget`

 | String | 

Link target of the page.

 |

In-app editor and preview variables[](https://developers.hubspot.com/docs/cms/hubl/variables#in-app-editor-and-preview-variables)
---------------------------------------------------------------------------------------------------------------------------------

You can use the following variables to check if the content is being rendered in the content editor or previewer. For example, you may want to use these to prevent running code in the editor while still running the code on live pages.

{% if is\_in\_page\_editor %} Display something different within the page editor. {% endif %}

| Variable | Type | Description |
| --- | --- | --- |
| 
`is_in_hs_app`

 | String | 

Returns `true` if content is being rendered within the HubSpot app.

 |
| 

`is_in_editor`

 | String | 

Returns `true` if content is being rendered within any content editor.

 |
| 

`is_in_global_content_editor`

 | String | 

Returns `true` if content is being rendered within the global content editor.

 |
| 

`is_in_theme_editor`

 | Number | 

Returns `true` if content is being rendered within the theme editor.

 |
| 

`is_in_page_editor`

 | String | 

Returns `true` if content is being rendered within the page editor.

 |
| 

`is_in_blog_post_editor`

 | String | 

Returns `true` if content is being rendered within the blog post editor.

 |
| 

`is_in_email_editor`

 | String | 

Returns `true` if content is being rendered within the email editor.

 |
| 

`is_in_previewer`

 | Number | 

Returns `true` if content is being rendered within any preview context.

 |
| 

`is_in_theme_previewer`

 | Object | 

Returns `true` if content is being rendered within the theme previewer.

 |
| 

`is_in_template_previewer`

 | String | 

Returns `true` if content is being rendered within the template previewer.

 |
| 

`is_in_page_previewer`

 | String | 

Returns `true` if content is being rendered within the page previewer.

 |
| 

`is_in_blog_post_previewer`

 | String | 

Returns `true` if content is being rendered within the blog post previewer.

 |
| 

`is_in_email_previewer`

 | String | 

Returns `true` if content is being rendered within the email previewer.

 |
| 

`is_in_module_previewer`

 | String | 

Returns `true` if content is being rendered within the module previewer.

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/variables#page-feedback)
-------------------------------------------------------------------------------------------

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