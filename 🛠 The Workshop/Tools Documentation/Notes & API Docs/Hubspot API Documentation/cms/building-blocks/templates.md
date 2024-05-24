Templates overview


======================

Last updated: May 4, 2023

Templates define the layout of your HubSpot pages, emails, and themes. A template consists of modules and partials, and can reference other assets such as stylesheets and JavaScript files. Templates can be created either using the [HubSpot CLI](/docs/cms/guides/getting-started) or in [HubSpot's design manager](https://knowledge.hubspot.com/design-manager/create-page-email-and-blog-templates-in-the-layout-editor). For content creators, the template is the first thing they'll select when creating a page or email.

Below, learn how to create a template, the different types of templates, and what's included with your templates.

Create a template[](https://developers.hubspot.com/docs/cms/building-blocks/templates#create-a-template)
--------------------------------------------------------------------------------------------------------

You can create a template either [in HubSpot](https://knowledge.hubspot.com/design-manager/create-page-email-and-blog-templates-in-the-layout-editor) or by [using the CLI](/docs/cms/guides/getting-started).

*   To create a template using the CLI, run the following command:

hs create template <name> \[dest\]

hs create template parameters
| Parameter | Description |
| --- | --- |
| 
`name`

 | 

The template's name

 |
| 

`dest`

 | 

The path of the local directory that you want to create the template in. If not included, the template will be created in the directory you're currently in.

 |

*   Using the arrow keys, navigate to the [type of template](#template-types) you want to create, then hit enter.  

The template will then be created locally. When you want to make the template available for use in your HubSpot account, [upload](/docs/cms/developer-reference/local-development-cms-cli#upload) the template to your account. You can also use the [watch](/docs/cms/developer-reference/local-development-cms-cli#watch) command to automatically upload all new files and edits to existing files in the current working directory and child directories.

Preview a template[](https://developers.hubspot.com/docs/cms/building-blocks/templates#preview-a-template)
----------------------------------------------------------------------------------------------------------

After updating a template, you can preview it to ensure it looks and acts as you expect. There are a few ways in HubSpot to preview a template, such as:

*   **Previewing a template in the design manager:** best for quick visual checks or when needing to preview a blog post/listing/combined template.
*   **Creating a new asset from a template:** best for testing the drag and drop editor and content creation experience.

### Preview with the design manager

Previewing templates using the design manager can be especially helpful for quick visual checks. The template previewer also enables you to configure display options, such as viewport dimensions.

To preview a template in the design manager:

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **Design Tools**
*   Using the left sidebar file explorer, click the **template** you'd like to preview.
*   In the upper right, click **Preview**. 
    *   Select **Live preview with display options** to preview the template with options to test responsiveness and domain settings such as stylesheets. This option displays the page within an iframe. This also enables you to select between blogs and the blog post or listing view for blog templates.
    *   Select **Preview without display options** to preview the template without additional options.

![template-preview-options](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/template-preview-options.png?width=653&height=186&name=template-preview-options.png)

### Preview with a new page

When changing drag and drop areas, default parameter values on modules, or other significant changes, it’s best to [create a website page](https://knowledge.hubspot.com/website-pages/create-and-customize-pages), [blog](https://knowledge.hubspot.com/blog/create-a-new-blog), [blog post](https://knowledge.hubspot.com/blog/create-and-publish-blog-posts) or [email](https://knowledge.hubspot.com/email/create-marketing-emails-in-the-drag-and-drop-email-editor) using the template. You can then try out different module field values and test what your template will look like in the real world and optimize for the best content creator experience. You can either publish these assets or leave them in draft mode for testing purposes.

In addition, you can use [content staging](https://knowledge.hubspot.com/cms-general/redesign-and-relaunch-your-site-with-content-staging#new) or a [developer sandbox account](https://offers.hubspot.com/free-cms-developer-sandbox) to create and view assets without impacting a production account.

Template types[](https://developers.hubspot.com/docs/cms/building-blocks/templates#template-types)
--------------------------------------------------------------------------------------------------

Templates can be used for different types of content, such as website pages and blog posts. In coded templates, you designate the type of template by adding an annotation at the top of the file.

Below, learn about the different types of templates and annotations you can use to designate each type.

**Please note:** a content creator can swap a page's template for another template of the same type, depending on whether it has [dnd\_area](/docs/cms/hubl/tags/dnd-areas) tags.

*   Templates built with the visual drag and drop layout editor can be swapped for other drag and drop templates or coded templates with or without `dnd_area` tags.
*   Coded templates with _dnd\_area_ tags can only be swapped for other coded templates with `dnd_area` tags.
*   Coded templates without `dnd_area` tags can only be swapped for other coded templates without `dnd_area` tags.

### Page[](https://developers.hubspot.com/docs/cms/building-blocks/templates#page)

templateType: page

Page templates are the most open-ended template type. They can serve as any flavor of web page or [landing page](https://blog.hubspot.com/blog/tabid/6307/bid/7177/what-is-a-landing-page-and-why-should-you-care.aspx). Page [Layouts](#layout-css) are not pre-populated with any components. Coded page templates come pre-populated with sparse markup including suggested HubL tags for meta info, title, and required header/footer [includes](#included-cms-files). Examples of pages that would typically use a page template would include but are not limited to:

*   [Homepage](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/home.html)
*   [About us](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/about.html)
*   [Contact](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/contact.html)

### Email[](https://developers.hubspot.com/docs/cms/building-blocks/templates#email)

templateType: email

Email templates are used by the [email tool](https://www.hubspot.com/products/marketing/email). They have the most stringent set of requirements since they need to be viewed in many different email clients and conform to best practices to ensure proper deliverability. Both [HTML + HubL](/docs/cms/building-blocks/templates/html-hubl-templates) and design manager drag and drop email templates come pre-populated with baseline components upon creation. Templates with this `templateType` are only visible for template selection when [creating an email](https://knowledge.hubspot.com/email/create-and-send-marketing-emails).

In order to stay [CAN-SPAM](https://knowledge.hubspot.com/email/can-i-customize-my-can-spam-email-footer) compliant, email templates have a set of [required variables](/docs/cms/hubl/variables#required-email-template-variables) that must be included.

Email templates also have a built-in functionality to [inline-css](/docs/cms/building-blocks/templates/email-template-markup#hs-inline-css-and-data-hse-inline-css) added to `<style>` elements with a special class name or data attribute. Inlining CSS in emails is a method used to get better support across email clients. Fortunately, [most of the popular email clients now support embedded css](https://litmus.com/blog/do-email-marketers-and-designers-still-need-to-inline-css), that however is not representative of your specific recipients. Use good judgment to do what is right by your recipients.

[Learn more about building email templates.](/docs/cms/building-blocks/templates/email-template-markup)

### Partial[](https://developers.hubspot.com/docs/cms/building-blocks/templates#partial)

templateType: page isAvailableForNewContent: false

Partials are template files that can be included in other coded files. Unlike global partials, partials can be edited individually without impacting other instances of the partial. 

Learn more about [partials](/docs/cms/building-blocks/templates/html-hubl-templates#partials).

### Global partial[](https://developers.hubspot.com/docs/cms/building-blocks/templates#global-partial)

templateType: global\_partial

Global partials are a type of template built using HTML & HubL that can be reused across your entire website. The most common types of partials are website headers, sidebars, and footers. Updating a global partial will update all instances of the global partial.  

Learn more about [global partials](/docs/cms/building-blocks/templates/html-hubl-templates#global-partials) and [global content](/docs/cms/building-blocks/global-content).

### Blog[](https://developers.hubspot.com/docs/cms/building-blocks/templates#blog)

When [creating a blog](https://knowledge.hubspot.com/cos-blog/cos-blog-how-do-i-create-a-cos-blog), [blog templates](/docs/cms/building-blocks/templates/blog) are similar in structure to standard [page templates](#page-templates). The crucial difference is that they can be selected in [content settings](https://app.hubspot.com/l/settings/website/pages/all-domains/system-pages) as blog templates whereas page templates cannot. Templates created with `blog_listing`, `blog_post`, or `blog`, `templateType` do not appear when a user is creating a web page, in the template selection screen. Blog templates actually have two forms, blog listing pages and blog post detail pages. 

### Blog listing[](https://developers.hubspot.com/docs/cms/building-blocks/templates#blog-listing)

templateType: blog\_listing

The [blog listing template](/docs/cms/building-blocks/templates/blog/listing) is the template users will see when navigating to the blog's URL. Typically this template is used to list summaries, titles and featured images of all of the posts on the blog, additionally typically displays pagination to get to older posts.

### Blog post[](https://developers.hubspot.com/docs/cms/building-blocks/templates#blog-post)

templateType: blog\_post

The blog post template, is the template users will see when viewing an individual post in the blog. These templates typically show the full post content.

#### Combined blog post and listing template[](https://developers.hubspot.com/docs/cms/building-blocks/templates#combined-blog-post-and-listing-template)

A single blog template can handle the layout for [both listing and detail pages](/docs/cms/building-blocks/templates/blog-template-markup#if-is-listing-view-statement) but more typically these are separated into separate templates. Combined templates will show in the blog settings as selectable for both listing and blog post options. If you are creating a template that is intended to only be used for posts, or listings, you should use `blog_post`, or `blog_listing`, instead.

templateType: blog

For a simpler development and content creator experience it is recommended to use the separate `blog_post`, and `blog_listing` `templateTypes` instead of combined templates.

### System pages[](https://developers.hubspot.com/docs/cms/building-blocks/templates#system-pages)

System page templates are flagged internally for their specific purpose. In your account's [content settings](https://app.hubspot.com/l/settings/website/pages/all-domains/system-pages), you can select these templates for their specified purpose in the system tab.

**Please note:** the only type of system page template that can be created through the CLI is the search results page template.

#### Error pages[](https://developers.hubspot.com/docs/cms/building-blocks/templates#error-pages)

Error pages can be set in [Content Settings](https://app.hubspot.com/l/settings/website/pages/all-domains/system-pages) as either [404](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/404.html) or [500](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/500.html) pages. Both templates use the same templateType. Templates created with this templateType do not appear when a user is creating a web page, in the template selection screen.

templateType: error\_page

#### Email subscription preferences[](https://developers.hubspot.com/docs/cms/building-blocks/templates#email-subscription-preferences)

The email subscription preferences page. Lists all of the available subscription types a user can opt into or out of. Required to contain the `{% email_subscriptions "email_subscriptions"  %}` HubL Tag. [See the subscription preferences template in the cms-theme-boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/subscription-preferences.html).

templateType: email\_subscription\_preferences\_page

#### Email backup unsubscribe[](https://developers.hubspot.com/docs/cms/building-blocks/templates#email-backup-unsubscribe)

A system template for email unsubscribe pages. Required to contain the `{% email_simple_subscription "email_simple_subscription" %}` HubL tag. [See the email backup unsubscribe template in the cms-theme-boilerplate.](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/backup-unsubscribe.html)

templateType: email\_backup\_unsubscribe\_page

#### Email unsubscribe confirmation[](https://developers.hubspot.com/docs/cms/building-blocks/templates#email-unsubscribe-confirmation)

A system template for email unsubscribe confirmation pages. This is where users are sent when they go to the URL generated by the [`{{ unsubscribe_link_all }}`](/docs/cms/hubl/variables#email-variables) variable.  [See the subscription confirmation template in the cms-theme-boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/subscriptions-confirmation.html).

templateType: email\_subscriptions\_confirmation\_page

#### Password prompt[](https://developers.hubspot.com/docs/cms/building-blocks/templates#password-prompt)

Password prompt templates provide a branded page content creators can display to require a password before a visitor can view the page’s actual content. Password prompt templates are set via [Content Settings](https://app.hubspot.com/l/settings/website/pages/all-domains/system-pages). [How to make a page on HubSpot password protected](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages). See the [password protected page prompt](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/password-prompt.html) in the boilerplate.

templateType: password\_prompt\_page

#### Search results page[](https://developers.hubspot.com/docs/cms/building-blocks/templates#search-results-page)

A system template for the built-in CMS site search listing functionality. See the [search results page template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/search-results.html) in the boilerplate.

templateType: search\_results\_page

### Membership[](https://developers.hubspot.com/docs/cms/building-blocks/templates#membership)

HubSpot accounts with the [memberships functionality](/docs/cms/features/memberships) (CMS Hub Enterprise _only_) can [create pages on their sites that only users apart of specific lists in the CRM can access](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages). This enables site visitors to have accounts with login credentials. These templates give you control over the appearance of these pages.

Only [HTML + HubL templates](/docs/cms/building-blocks/templates/html-hubl-templates) can be membership templates.

#### Membership login[](https://developers.hubspot.com/docs/cms/building-blocks/templates#membership-login)

This is the login page that displays when a user tries to access content that is access controlled through the memberships functionality. Typically contains the `{% member_login "member_login" %}` module. See the example [membership login template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/membership-login.html) in the boilerplate.

templateType: membership\_login\_page

#### Membership register[](https://developers.hubspot.com/docs/cms/building-blocks/templates#membership-register)

This is the user registration page that allows users to create an account to view the content that users of this list can access. Typically contains the `{% member_register "member_register" %}` HubL Tag. See the example [membership registration template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/membership-register.html) in the boilerplate.

templateType: membership\_register\_page

#### Membership password reset[](https://developers.hubspot.com/docs/cms/building-blocks/templates#membership-password-reset)

This is the password reset page. Users provide their new password on this page. Typically contains the `{% password_reset "password_reset" %}` HubL Tag. See the example [membership password reset template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/membership-reset-password.html) in the boilerplate.

templateType: membership\_reset\_page

#### Membership reset request[](https://developers.hubspot.com/docs/cms/building-blocks/templates#membership-reset-request)

This is the request a password reset page. Displaying a form to request a password reset email. Typically contains the `{% password_reset_request "password_reset_request" %}` HubL Tag. See the example [membership password reset request template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/system/membership-reset-password-request.html) in the boilerplate.

templateType: membership\_reset\_request\_page

Included CMS files[](https://developers.hubspot.com/docs/cms/building-blocks/templates#included-cms-files)
----------------------------------------------------------------------------------------------------------

There are certain JavaScript and CSS files that are attached to CMS templates. Some files are automatically included and cannot be removed, while others can be optionally included. To learn more about the order in which stylesheets are attached to CMS content, [check out this article](https://knowledge.hubspot.com/cos-general/create-edit-and-attach-css-files-to-style-your-site).

### jQuery[](https://developers.hubspot.com/docs/cms/building-blocks/templates#jquery)

[jQuery](https://jquery.com/) is optionally included in the head tag of HubSpot templates. If included, it is rendered as part of the `[standard_header_includes](/docs/cms/hubl/variables#required-page-template-variables)` HubL variable.

In **Settings > Website > Pages**, you can change the jQuery version to 1.11.x, version 1.7.1, or disable it completely. You can also choose to include a jQuery migrate script for backward compatibility with older browsers. You can move jQuery to the footer to improve page performance, but moving jQuery can break JavaScript relying on it. It's recommended to test this out before moving it by adding `?hsMoveJQueryToFooter=True` to the end of your website page URLs.

While jQuery was historically included by default, currently CMS Hub does not require jQuery. Most of jQuery's functionality now has [modern vanilla javascript equivalents](http://youmightnotneedjquery.com/), and it's recommended to use them instead. If you need to use jQuery, we encourage disabling the default version in settings and using the latest version loaded above the `</body>` tag.

To test if removing jQuery on your site will break anything, add `?hsNoJQuery=true` to the end of the URL while viewing your site, especially pages with heavy interactivity.

### layout.css[](https://developers.hubspot.com/docs/cms/building-blocks/templates#layout-css)

Formerly known as `required_base.css`, this file is responsible for styling HubSpot's responsive grid. This file is automatically included in any drag and drop template, but is not included by default in custom coded templates. When using [dnd\_area](/docs/cms/hubl/tags/dnd-areas) tags in coded HTML + HubL templates, you don't need to load the `layout.css` file, but a version of it is [included in the CMS boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/css/objects/_layout.css) to make it easier to get up and running quickly.

In addition to the responsive grid CSS, the file includes some classes that can be used to show and hide elements at different viewports. To learn more,  [view the file directly](https://cdn2.hubspot.net/hubfs/327485/Designers_Docs_2015/layout.css).

### HubSpot tracking code[](https://developers.hubspot.com/docs/cms/building-blocks/templates#hubspot-tracking-code)

The [HubSpot tracking code](https://knowledge.hubspot.com/account/how-does-hubspot-track-visitors) is automatically added to any HubSpot template, excluding email templates, with the [**standard\_footer\_includes**](/docs/cms/hubl/variables) HubL variable. The tracking code loads an analytics JavaScript file named `your_HubID.js` (example: `158015.js`). This tracking code is directly integrated with [HubSpot's GDPR functionality](https://knowledge.hubspot.com/account/how-do-i-turn-on-gdpr-functionality-in-my-hubspot-account).

Related resources[](https://developers.hubspot.com/docs/cms/building-blocks/templates#related-resources)
--------------------------------------------------------------------------------------------------------

*   [Drag and Drop Areas](/docs/cms/building-blocks/templates/drag-and-drop-areas)
*   [Section templates](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections)
*   [How to use web components in templates, and modules](/blog/use-web-components-in-hubspot-cms-development)
*   [Build headers footers and more using global content](/docs/cms/building-blocks/global-content)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/templates#page-feedback)
------------------------------------------------------------------------------------------------------

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