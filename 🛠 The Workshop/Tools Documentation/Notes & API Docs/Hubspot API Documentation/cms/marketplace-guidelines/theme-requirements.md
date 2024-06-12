---
Please provide me with more context!  "MISSION" is a very broad term. To help me write a compelling mission statement, I need to know: "* **What is the subject of the mission?** Is it for a company, a project, a team, an individual, or something else?"
* **What are the goals or objectives?** What do you want to achieve?
* **What are the values or principles?** What are the guiding beliefs behind the mission?

Once I have a better understanding of the context, I can help you create a clear, concise, and inspiring mission statement.
---

HubSpot Template Marketplace theme requirements


===================================================

Last updated: May 13, 2024

Learn more about the requirements a theme must meet for submission to the HubSpot Template Marketplace. 

If you are just starting out on your theme creation journey, we highly recommend using our free CMS theme boilerplate, which can be downloaded from our [Git Repository](https://github.com/HubSpot/cms-theme-boilerplate) or [imported within your account’s design manager UI](https://www.youtube.com/watch?v=9Ez3ntetA4A&list=PLTGNq2fWP3b1g0PCXqPAuKZJHUdk_Z_ua).

Theme limits[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#theme-limits)
--------------------------------------------------------------------------------------------------------------

Keep in mind the following limits per theme:

*   Free **_CMS Hub_** accounts cannot use site search, CTA functionality, or native HubSpot video. Learn more about what's included with **_CMS Hub_** subscriptions in [HubSpot's Product & Services catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog).
*   Themes cannot contain more than:
    *   50 templates
    *   50 modules
    *   50 sections

*   Themes **must not** contain:
    *   Email templates
    *   HubDB functionality
    *   Serverless functions
    *   CRM object fields
    *   Membership templates
    *   [Flexible columns in templates](/docs/cms/building-blocks/templates/drag-and-drop-templates#flexible-columns)

**Modules vs. Sections**

Sections are helpful because content creators can only drop them in full-width drop zones on the page, which helps you as a developer guarantee a great finished product.

In particular, fixed-layout sections, where the content creator cannot move elements within the section around, are a great tool to provide creative formatting and layout that couldn’t otherwise be achieved using the drag-and-drop editor.

Sections also offer extra usability benefits for the content creator because they can select individual modules inside the section, making it so that their module forms are shorter and more targeted to the element they’re editing.

Overall theme requirements[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#overall-theme-requirements)
------------------------------------------------------------------------------------------------------------------------------------------

*   All submitted themes must be distinct and original. For example, the same theme with different copy or placeholder content does not count as a distinct theme. [Learn more about HubSpot Template Marketplace compliance](/docs/cms/marketplace-guidelines/template-marketplace-policies#template-marketplace-compliance). 
*   A theme must be built with HTML and HubL templates, and [dnd\_area](/docs/cms/hubl/tags/dnd-areas) tags.
*   Themes must respect a 12-column grid. 

### Theme file structure[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#theme-file-structure)

All themes should contain a proper folder structure and be grouped under one parent folder, which should describe your product listing. For example, if you build a theme named “SuperAwesome” for the marketplace, your structure should look similar to the image below. Learn more about [theme file structure](/docs/cms/building-blocks/themes#theme-file-structure). 

![template-name](https://developers.hubspot.com/hubfs/Knowledge_Base_2023_2024/template-name.png "template-name")

![file-structure](https://developers.hubspot.com/hubfs/Knowledge_Base_2023_2024/file-structure.png "file-structure")

### Relative local file paths for templates[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#relative-local-file-paths-for-templates)

You must use relative local file paths when referring to theme assets. The best way to include these is to use the [get\_asset\_url function](https://developers.hubspot.com/docs/cms/hubl/functions#get-asset-url), which returns the public URL of an asset, file, or template. You can also [generate this function](https://developers.hubspot.com/docs/cms/hubl/functions#get-asset-url) by either right-clicking a **file** and selecting **Copy public URL**, or by clicking **Actions**, then selecting **Copy public URL**. 

For example, a stylesheet referenced by `require_css` and `get_asset_url` must be formatted as follows:

{{require\_css(get\_asset\_url('../../css/main.css')) }//cdn2.hubspot.net/hub/1234567/hub\_generated/template\_assets/1565970767575/custom/styles/style.min.css

In the video below, review the differences in file structure in your developer account versus files delivered to a marketplace customer: 

Theme performance[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#theme-performance)
------------------------------------------------------------------------------------------------------------------------

Using Google Lighthouse, a theme must score higher than the following thresholds:

*   **Desktop accessibility:** 65
*   **Desktop best practices:** 80
*   **Desktop performance:** 70
*   **Mobile performance:** 40

Learn how to [generate a Google Lighthouse report for your theme using the CLI](/docs/cms/developer-reference/local-development-cli#evaluate-themes-and-templates-for-seo-and-accessibility).

*   Theme files should be able to be minified.
*   All image files should be under 1MB in size.
*   All image tags should have an `alt` attribute (a value of `""` is acceptable).
*   All image tags should have a `loading` attribute (a value of `""` is acceptable).

### Preview URLs for themes[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#preview-urls-for-themes)

You must use your own domain name when creating preview URLs. You cannot use the HubSpot-provided domain with this URL structure: `[AccountID].hs-sites.com`

A live website and not an image of the demo site must be used. 

If at any point your live demo becomes inaccessible, HubSpot reserves the right, with notification to the provider, to delist/remove your theme until the live demo becomes accessible again.

Using jQuery[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#using-jquery)
--------------------------------------------------------------------------------------------------------------

jQuery is [not enabled by default](https://knowledge.hubspot.com/website-pages/include-jquery-across-your-hubspot-pages) in a customer's HubSpot account. If your theme relies on jQuery, a version of the jQuery must be included to ensure the theme works as expected. 

For example, if you include a module that requires jQuery when the rest of the site doesn’t, you need to use the following code to load jQuery:

{# this checks if the "Include jQuery" option in Settings > CMS > Pages is checked #} {% if not site\_settings.include\_jquery %} {{ require\_js("../jquery-3.4.1.js", "footer") }} {% endif %}

Theme configuration (Theme.json)[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#theme-configuration-theme-json-)
-----------------------------------------------------------------------------------------------------------------------------------------------------

The `theme.json` file must include the following parameters:

// theme.json { "label": "Cool Theme", "preview\_path": "./templates/home-page.html", "screenshot\_path":"./images/templates/homepage.jpg", "enable\_domain\_stylesheets": false, "version":"1.0", "author":{ "name":"Jon McLaren", "email":"noreply@hubspot.com", "url":"https://theme-provider.com/" }, "documentation\_url":"https://theme-provider.com/cool-theme/documentation", "license":"./license.txt", "example\_url":"https://theme-provider.com/cool-theme/demo", "is\_available\_for\_new\_content":true }

Please check your `theme.json` file and ensure the following:

*   The label name matches the name in your theme listing.
*   If you're using HubSpot's free CMS theme boilerplate, boilerplate values must not be present. This includes author information, documentation URL, example URL, etc.
*   The documentation URL resolves and has documentation on how to use your theme.
*   The preview path is a valid file in your theme.
*   The screenshot path is a valid file and is related to your theme.
*   The example URL resolves and leads to a demo of your theme. Do not use `preview.hs-sites.com` or `[AccountID].hs-sites.com` subdomains for the example URL. 

Learn more about [theme.json parameters](/docs/cms/building-blocks/themes#theme-json).

Theme settings (Fields.json)[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#theme-settings-fields-json-)
---------------------------------------------------------------------------------------------------------------------------------------------

The `fields.json` file controls the available fields and fields groups in the theme editor, including style fields. The fields you include will depend on how much control you want content creators to have in the page editor. 

*   The `fields.json` file must contain at least three color fields.
*   To ensure compatibility between themes and independent modules, themes must include the following font and color standard naming conventions: `primary_color`, `secondary_color`, `heading_font`, and `body_font`. 

If theme fields do not have `primary_color`, `secondary_color`, `heading_font`, or `body_font` fields, they can use the `alternate_names` field.

Learn more about these [fields.json parameters](/docs/cms/building-blocks/themes#fields-json) and [review an example fields.json file](https://github.com/HubSpot/cms-theme-boilerplate/blob/main/src/fields.json) from the HubSpot CMS boilerplate. 

Theme settings must also:

*   Not conflict with your editor styles or styles set through a module. For example, do not use `!important` in your CSS stylesheet as it makes it difficult for end users to override and would cause a conflict.
*   Use descriptive labels for each setting so that content creators know what they're updating. 
*   Apply to all templates in a theme, unless there's a specific use case for additional styles. For example, changes to the style and size of `h1` headings in theme settings must apply across all `h1` tags in the theme. 

At a minimum, a theme must include the following theme fields:

**Typography fields:**

*   Body text font fields (`p` tags)
*   `h1` through `h6` font fields
*   Hyperlink color (`a` tags), including hover styling 

**Form fields:**  

*   Form title background
*   Form title text, including at least font color styles
*   Form background color
*   Form border color
*   Form label color
*   Form field border color
*   Form button -  this includes settings for button text, background color, and hover styling. 

In addition:

*   Fields inside of your theme must be grouped logically where appropriate. For example, multiple fields related to typography should be grouped under a `Typography` group.
*   Theme fields should have separate color and font controls for buttons and forms, as well as separate color, logo, and font controls for the header and footer. 
*   A portion of the theme's color and logo fields must inherit from the account's [brand settings](/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance):
    *   At a minimum, two color fields must inherit colors from the account's brand settings. Additional color fields can default to other colors, including black and white.
    *   If modules within a theme are using logos, at least one logo field must inherit from the account's brand settings. If using an image field to render a logo, the image field does not have to inherit from the brand settings.

How brand colors impact your theme's aesthetics 

Templates (CSS, Sections, Page Templates, etc.)[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#templates-css-sections-page-templates-etc-)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Sections[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#sections)

*   You must use [sections](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#reusable-sections) wherever applicable. There **must** be a minimum of five sections in a theme. 
*   Sections must have unique and working screenshots.
*   Sections and modules should not be redundant.

### Page templates[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#page-templates)

At a minimum, a theme must include the following template types:

*   A website page template or landing page template.
    *   When including multiple-page templates, each template must have a distinct purpose. For example, a home page, an _About Us_ page, a full-width landing page, and a landing page with a right sidebar.
    *   It is recommended to include at least eight page templates in a theme. 

*   Separate blog listing and blog post templates.
    *   **Blog listing template:** the page that shows all blog posts in a listing format (known as the blogroll). The template title must reflect that it's for the listing page.
    *   **Blog post template:** the blog post detail page that displays individual blog posts. The template title must reflect that it's for the blog post page.
    *   In addition, blog comments and blog author boxes must be styled to match the theme.

*   The following system page templates:
    *   **404 error template:** shown when visitors hit a page that doesn't exist.
    *   **500 error template:** shown when the site encounters an internal error.
    *   **Password prompt template:** shown when a page is password protected.
    *   **Subscription template:** a subscription preferences page where email recipients can manage the types of emails they're subscribed to.
    *   **Subscriptions update template:** a confirmation page that appears when an email recipient updates their email subscription preferences.
    *   **Backup unsubscribe template:** the page that appears for email recipients who are trying to unsubscribe if HubSpot is unable to determine their email address.
    *   Search results template: displays search results returned when using the [site search](https://developers.hubspot.com/docs/cms/features/content-search). Available for paid **_CMS Hub_** accounts only.

### Page template naming[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#page-template-naming)

*   If you have templates with similar names, add descriptive words that denote the difference between them.
*   Keep capitalization consistent, remove hyphens, and avoid using shorthand (e.g. spell out background instead of using bg). 
*   Your company name or theme name does not need to be included in the template name. 

Modules[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#modules)
----------------------------------------------------------------------------------------------------

Learn more about the requirements for theme modules and individual modules [here](/docs/cms/marketplace-guidelines/module-requirements). 

Global content[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#global-content)
------------------------------------------------------------------------------------------------------------------

### Global partials[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#global-partials)

[Global partials](/docs/cms/building-blocks/global-content) are a type of template built using HTML and HubL to can be reused across your entire website. The most common type of partials are website headers, page sidebars, and website footers. Learn how to [create global partials](/docs/cms/building-blocks/global-content#creating-a-global-content-partial-template-using-local-development-tools).

*   Themes must include global partials.
*   Global partials must include usable [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas). For example, you cannot hide the drag and drop area with a "hide" class.
*   You must incorporate usable drag-and-drop areas in headers and footers. 
*   For menus that are used globally throughout a site, users must also be able to [select a HubSpot navigation menu](/docs/cms/building-blocks/menus-and-navigation) they've created in their account settings.

**Please note**: avoid including global modules within global partials, as it can create a negative end-user experience.

Multi-Language support[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#multi-language-support)
----------------------------------------------------------------------------------------------------------------------------------

Themes must be able to support multiple language versions and should specify the languages that they support. This can be done by adding the language switcher module in a global header, which allows customers to easily locate the language options and choose their desired language.

*   You must only display one language at a time. For example, avoid having both English and Spanish in the UI at the same time.
*   Avoid using hard-coded text. For example, rather than hard-coding a blog listing button’s text as _Read More_, set the text within a field so that the end user can update the text without having to go into the code.

Mobile and responsive elements[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#mobile-and-responsive-elements)
--------------------------------------------------------------------------------------------------------------------------------------------------

Themes should be capable of adapting their content to the device it is being viewed on. They should also provide a good user experience across various devices. This includes, but is not limited to:

*   Main navigation
*   Sliders and tabs
*   Large images
*   Avoiding horizontal scrolling (unless intentional) 

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/theme-requirements#page-feedback)
----------------------------------------------------------------------------------------------------------------------

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