---
title: "Website Settings"
description: "A single place where various global and system-level content settings can be configured for your website's blog, navigation, pages, and themes. Navigate to [Settings > Website](https://app.hubspot.com/l/settings/website/blogs/) and choose which content area you want to access your Content Settings for."
type: "group"
tags:
- "Website"
- "Configuration"
- "Blog"
- "Navigation"
- "Pages"
- "Themes"
relationships:
- "#contains [[Settings > Website]]"
birthdate: "N/A"
deathdate: "N/A"
---

Website Settings


====================

Last updated: April 12, 2022

Website settings is a single place where various global and system-level content settings can be configured for your website's blog, navigation, pages, and themes. Navigate to [Settings > Website](https://app.hubspot.com/l/settings/website/blogs/) and choose which content area you want to access your Content Settings for. 

Blog settings[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#blog-settings)
-------------------------------------------------------------------------------------------------------

In this area you will control the content settings for your sites blog(s). If you have multiple blogs, you can switch between them using the dropdown under the "Select a blog to modify" heading.

![Blog settings screen](https://developers.hubspot.com/hubfs/5Cdocs/website-settings/blog-settings-screen-4.jpg "Blog settings screen")

### General Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#general-tab)

#### Blog name[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#blog-name)

The HubL variables `{{ content.blog }}` and `{{ group.public_title }}` will render the name set here.

#### Blog header[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#blog-header)

The HubL variable `{{ group.header }}` will render the header set here.

#### Page Title[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#page-title)

The HubL variable `{{ group.html_title }}` will render the title set here.

#### Meta description[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#meta-description)

The HubL variable `{{ group.description }}` will render the description set here. This meta description will be used on blog listing pages.

#### Blog root URL[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#blog-root-url)

The blog root URL will precede individual blog post slugs. The HubL variable `{{ group.absolute_url }}` will render the URL set here.

#### Control audience access[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#control-audience-access)

You can control audience access to an entire blog via this setting. More on that [here](https://knowledge.hubspot.com/cms-pages-editor/control-audience-access-to-pages).

### Templates Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#templates-tab)

#### Current template[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#current-template)

This is the template used for all blog posts in a particular blog. The same template will be used for blog listing pages as well by default. Varying content for listing pages versus posts can be written within the Post Content module.

#### Template for listing pages (optional)[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#template-for-listing-pages-optional-)

This setting enables a different template for blog listing pages other than the template used for blog posts.

#### Number of posts per listing page[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#number-of-posts-per-listing-page)

This determines the number of post items that appear on a blog listing page by default. 

#### Header HTML[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#header-html)

Any code added to the blog listing header HTML will be added to all listing pages via the `{{ standard_header_includes }}` variable. Any code added to the blog post header HTML will be added to all blog posts via the `{{ standard_header_includes }}` variable. 

#### Footer HTML[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#footer-html)

Any code added to the blog listing footer HTML will be added to all listing pages via the `{{ standard_footer_includes }}` variable. Any code added to the blog post footer HTML will be added to all blog posts via the `{{ standard_footer_includes }}` variable. 

### Subscriptions Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#subscriptions-tab)

#### Blog subscriber notification emails[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#blog-subscriber-notification-emails)

Instant, Daily, Weekly, and Monthly blog notification emails can be enabled and edited via this setting. These emails go out automatically if new blog posts were published in the given timeframe. Read more [here](https://knowledge.hubspot.com/cos-blog/set-up-your-blog-subscription-features-in-hubspot).

#### RSS feed[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#rss-feed)

The number of post items in the blog RSS feed can be determined via this setting. There is a maximum of 50 posts.

### Date Formats Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#date-formats-tab)

#### Language for dates[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#language-for-dates)

This setting determines the language of months and days that appear in blog dates.

#### Publish date format[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#publish-date-format)

The format set here determines the order and pattern of publish dates in blogs. Using Local Data Markup Language, it is possible to specify a custom date format.

#### Posts by month format[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#posts-by-month-format)

The format set here determines the order and pattern of posts by month. Using Local Data Markup Language, it is possible to specify a custom date format.

### Comments Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#comments-tab)

#### Enable or disable blog comments[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#enable-or-disable-blog-comments)

It is possible to enable or disable blog comments via this setting. Comments can require moderation, or have an established timeframe after which comments are automatically closed.

#### Blog comment notifications[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#blog-comment-notifications)

Blog comments can trigger email notifications to specified users via this setting.

### Social Sharing Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#social-sharing-tab)

#### Default Twitter account[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#default-twitter-account)

The Twitter account specified here will be used for Twitter Cards when content is shared on Twitter.

#### Social sharing buttons[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#social-sharing-buttons)

Social sharing buttons for Twitter, LinkedIn, and Facebook can be automatically added to blog posts via this setting.

### Google AMP Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#google-amp-tab)

Accelerated Mobile Pages (AMP) load your content instantly. Read more [here](https://knowledge.hubspot.com/cos-general/how-to-use-accelerated-mobile-pages-amp-in-hubspot). In order to load content so quickly, a simplified page experience is required. AMP content has limited styling control for this reason.

#### Enable or disable Google AMP[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#enable-or-disable-google-amp)

Google AMP formatted pages can be enabled via this setting. AMP logo, font, and color settings

#### AMP-specific settings for a logo, header formatting[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#amp-specific-settings-for-a-logo-header-formatting)

In order to deliver AMP content, simplified styling is required. Determine AMP-specific styles for the logo, header formatting, fonts, and colors via these settings.

Navigation settings[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#navigation-settings)
-------------------------------------------------------------------------------------------------------------------

You can manage your menu links and labels in this area. You can switch between which menus you want to configure by choosing the dropdown and selecting your desired menu. [Learn more about setting up your sites navigation menus here.](https://knowledge.hubspot.com/cos-general/set-up-your-site-s-navigation-menus)

![Navigation settings screen](https://developers.hubspot.com/hubfs/5Cdocs/website-settings/navigation-settings-screen-4.jpg "Navigation settings screen")

Page settings[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#page-settings)
-------------------------------------------------------------------------------------------------------

Settings are broken down by domains, and default values for all domains can be set. The “_Default for all domains_” settings will be displayed when navigating to Pages Settings. There is a toggle at the top of the screen to view and modify settings for specific subdomains. Settings applied to specific subdomains will override the default for all domains settings.

Only users with the “[Edit website settings” Marketing permission](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide) can access and edit Content Settings.

![Page settings screen](https://developers.hubspot.com/hubfs/5Cdocs/website-settings/page-settings-screen-4.jpg "Page settings screen")

### Templates Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#templates-tab)

#### Site header HTML[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#site-header-html)

Any code added into the site header HTML field in Pages Settings will be included in the `{{ standard_header_includes }}` variable.

#### Site footer HTML[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#site-footer-html)

Any code added into the site footer HTML field in Pages Settings will be included in the `{{ standard_footer_includes }}` variable. Typically this is a good place for adding tracking codes and other scripts that are "non-essential" to your site functioning or looking good. That way it will not negatively impact any of your templates or pages.

#### jQuery[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#jquery)

You can modify the jQuery version loading on your page via Pages Settings. 

You can also opt to load jQuery from your footer via this setting. Appending `?hsMoveJQueryToFooter=True` to your page URL will allow you to test this change and ensure it does not impact your site’s appearance negatively.

The option to disable jQuery is also located within Pages Settings.

### Branding Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#branding-tab)

The logo image set for each domain here will automatically be used in the default “Logo” module.

#### Favicon[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#favicon)

#### Logo (alt text, dimensions, link)[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#logo-alt-text-dimensions-link-)

Your favicon image source URL can be pulled from the `site_settings` dictionary and used in your coded files:

{% if site\_settings.favicon\_src %}<link rel="icon" href="{{ site\_settings.favicon\_src }}" />{% endif %}

### Personalization Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#personalization-tab)

#### Contact & Company defaults[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#contact-company-defaults)

These are the default values used for personalization tokens used on pages when the visitor is unknown.

### Integrations Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#integrations-tab)

#### JS Integrations[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#js-integrations)

Enable JS Integrations (like Google Analytics or AdRoll) for all domains or select domains here. If using other tracking scripts or Google Tag Manager instead of Google Analytics that code should be added to the [site footer HTML](#site-footer-html).

### SEO & Crawlers Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#seo-crawlers-tab)

#### Canonical URLs[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#canonical-urls)

Select your default canonicalization setting for individual pages and posts, as well as listing pages, here.

#### Default File Hosting Domain[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#default-file-hosting-domain)

This controls the domain that assets from the file manager appear to be hosted at.

#### Robots.txt[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#robots-txt)

Modify your robots.txt file for each domain here.

### System Pages Tab[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#system-pages-tab)

For several system pages, you can select your templates in Pages Settings. No page editor exists for these pages, only templates in the Design Manager that are created with the “System” template type. **_Please note_**_: Email preferences and subscription templates are located in Email Settings, not Pages Settings._

404 and 500 error pages[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#and-500-error-pages)
-----------------------------------------------------------------------------------------------------------------------

These are the pages that are returned for 404 or 500 status codes. When creating a new template, select the [“Error page” template type](/docs/cms/building-blocks/templates#error-pages) in the Design Manager to make a template available for these system pages.

Password Prompt Page[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#password-prompt-page)
---------------------------------------------------------------------------------------------------------------------

This is the page that is returned for [password-protected pages](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages) when prompting a visitor to input a password. When creating a new template, select the [“Password prompt page” template type](/docs/cms/building-blocks/templates#password-prompt) in the Design Manager to make a template available for this kind of system page.

#### Search results page and URL[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#search-results-page-and-url)

This is the page that lists search results for queries input into HubSpot’s [Site Search](https://knowledge.hubspot.com/cos-general/how-do-i-set-up-a-results-page-for-my-search-field-in-hubspot) module. Read more on how to customize your search [here](https://developers.hubspot.com/docs/methods/content/search-for-content). When creating a new template, select the [“Search results page” template type](/docs/cms/building-blocks/templates#search-results-page) in the Design Manager to make a template for this kind of system page. You can also determine your search results page URL in Pages Settings.

Themes settings[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#themes-settings)
-----------------------------------------------------------------------------------------------------------

Here you can find all the themes added to your site. You can go into the themes editor by clicking on one of the themes available on your site.

![Theme settings screen](https://developers.hubspot.com/hubfs/5Cdocs/website-settings/theme-settings-screen-4.jpg "Theme settings screen")

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/website-settings#page-feedback)
-------------------------------------------------------------------------------------------------------------

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