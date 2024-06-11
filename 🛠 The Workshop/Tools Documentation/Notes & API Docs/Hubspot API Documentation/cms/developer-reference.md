---
title: "HubSpot CMS overview"
description: "This section is designed to help you understand key aspects of HubSpot's **_CMS_** and build great websites on it. To get the most out of this, a professional-level understanding of web development basics, including HTML, JavaScript, and CSS, is expected."
type: "group"
tags:
- "Web Development"
- "HubSpot CMS"
relationships:
- "#related_to [[Content Creation]]"
- "#enables [[Marketing Automation]]"
- "#used_by [[Developers, Content Creators]]"
founded: "N/A"
---

HubSpot CMS overview


========================

This section is designed to help you understand key aspects of HubSpot's **_CMS_** and build great websites on it. To get the most out of this, a professional-level understanding of web development basics, including HTML, JavaScript, and CSS, is expected.

If you’re new to building on the CMS, check out the [quickstart tutorial](/docs/cms/guides/getting-started) first, then consult this overview as needed.

Content enablement[](https://developers.hubspot.com/docs/cms/key-concepts#content-enablement)
---------------------------------------------------------------------------------------------

HubSpot's CMS is designed to help businesses grow their web presence with an emphasis on enabling marketers to create and manage content. The website's content, lead collection, and analytics are integrated with the [HubSpot CRM](https://www.hubspot.com/products/crm), making it easy to create personalized experiences for visitors and integrate those experiences with the rest of the business.

As a HubSpot CMS developer, you'll not only be building assets like themes, templates, and modules, but you'll be building them in a way that enables content creators to customize them with content as needed. In this way, **_you'll need to_** balance the needs of developers with the needs of content creators through its [theme](/docs/cms/building-blocks/themes) and [module](/docs/cms/building-blocks/modules) system and [drag-and-drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas).

![Templates and modules are at the intersection between developers and marketers](https://developers.hubspot.com/hs-fs/hubfs/code-no-code-graphic.png?width=780&height=439&name=code-no-code-graphic.png "Templates and modules are at the intersection between developers and marketers")

A well-crafted website should be developed in close collaboration with your content creators to understand their needs, and will then require less ongoing support and maintenance from a developer. To that end, it's recommended that you [preview how the page building experience looks and feels for content creators](/docs/cms/guides/creating-an-efficient-development-workflow#testing) while you build. This ensures they can work independently with the site as much as possible.

![Animated showing user creating a drag-and-drop page](https://developers.hubspot.com/hs-fs/hubfs/making%20a%20page.gif?width=780&height=407&name=making%20a%20page.gif "Animated showing user creating a drag-and-drop page")

HubSpot takes care of hosting and maintaining your pages, so you don’t have to worry about plugin management, updates, hosting, scaling, or security. The tradeoff is that the system puts a few more restrictions on what you can do compared to self-hosted CMS's. For example, you can’t alter or extend system fundamentals manually or via plugins, manipulate low-level rendering, or access and alter database content directly.

Developer-built content (e.g., [themes](/docs/cms/building-blocks/themes), [templates](/docs/cms/building-blocks/templates), [modules](/docs/cms/building-blocks/modules), JavaScript, and CSS) is created in a developer file system, while page content (pages, blog posts) is laid out and built in a powerful block-based what you see is what you get (WYSIWYG) editor, and media files (content creator-built images, PDFs, etc.) are stored in a web app-based file manager.

When a page is rendered, HubSpot routes the request to one of many servers based on domain, renders the page on our servers, and caches it to a content delivery network (CDN) if possible.

Types of content[](https://developers.hubspot.com/docs/cms/key-concepts#types-of-content)
-----------------------------------------------------------------------------------------

There are many types of content that you create using HubSpot's CMS. The user interface for content creators is slightly different depending on content type, which has implications that you as a developer need to be aware of.

### Website pages and landing pages[](https://developers.hubspot.com/docs/cms/key-concepts#website-pages-and-landing-pages)

Website and landing pages are built independent of one another, but all pages are based on templates. For content creators, the process of building a landing page or a website page is nearly identical. The distinction between them is that website pages are made to present information that’s part of your website and designed to be found organically, while a landing page is [generally associated with a specific marketing offer or campaign](https://blog.hubspot.com/marketing/landing-page-best-practices) (e.g., linked from a marketing email sent to a specific list of contacts). 

In the UI for marketers, the analytics and organization of these page types are also organized separately since landing pages often have specific conversion goals.

### Blogs[](https://developers.hubspot.com/docs/cms/key-concepts#blogs)

HubSpot blogs have two views—one for the listing page and one for the individual post page, then each blog post is populated into each of them. You can set a blog to share the same template for blog posts and listing pages, or have separate templates for the listing page and for blog posts. Blog posts must share the same template. Learn more about [blog template markup](/docs/cms/building-blocks/templates/blog) and [how to create and manage blogs in HubSpot](https://knowledge.hubspot.com/blog/manage-your-blog-template-and-settings).

### Emails[](https://developers.hubspot.com/docs/cms/key-concepts#emails)

Emails can be built in a few ways in HubSpot:

*   Classic email: build email templates and modules in a similar way to website and landing pages. You can also build [coded email templates](/docs/cms/building-blocks/templates/email-template-markup) to have full control of the markup.
*   **Drag and drop emails:** build customizable [drag and drop](https://knowledge.hubspot.com/email/create-marketing-emails-in-the-drag-and-drop-email-editor) email templates that enable content creators to build email layout and content using HubSpot's drag and drop interface.

Structured content[](https://developers.hubspot.com/docs/cms/key-concepts#structured-content)
---------------------------------------------------------------------------------------------

In addition to creating page content through the in-app editors or hard-coding in templates, you can also use structured data sources to populate [dynamic page content](/docs/cms/data/dynamic-pages) with HubL. You can use the following data sources to populate pages:

*   **[HubDB](/docs/cms/data/dynamic-pages#hubdb-dynamic-pages):** store data in cells of HubDB tables.
*   **[CRM records](/docs/cms/data/dynamic-pages#crm-object-dynamic-pages):** store data in CRM records, such as contacts, companies, or custom objects.

Building dynamic pages using structured content means that you can create, edit, and remove website pages and page content by updating the data sources directly. Similar to a HubSpot blog, a set of dynamic pages will include a single listing page to display the instances of your data source, then a separate page for each individual instance. Using HubL, you can fully configure the data that the pages display.

For example, you can create a HubDB table that stores a row of information for each member of a sales team. Using that HubDB table, HubSpot can then generate a listing page to display key details from each table row (such as a name and image for each sales rep), along with a separate page per sales rep to display more information (such as their bio and phone number). Should a sales rep later be promoted to a different team, you can delete their row from the HubDB table, and HubSpot will automatically delete their detail page and remove them from the listing page. 

Developer file system[](https://developers.hubspot.com/docs/cms/key-concepts#developer-file-system)
---------------------------------------------------------------------------------------------------

The core assets—templates, [themes](/docs/cms/building-blocks/themes), and [modules](/docs/cms/building-blocks/modules), as well as the JavaScript, CSS files, and images that support them—are created in a developer file system. You can view this file system either in the left panel of the [design manager](/docs/cms/developer-reference/design-manager) or in folders synchronized locally using the local development tools. Within the file system, assets can refer to each other with absolute or relative paths.

Behind the scenes, these files are mapped to entries in a database. This is why access to the developer file system is through the HubSpot [CLI](/docs/cms/developer-reference/local-development-cms-cli) tools rather than direct SSH or FTP access, and some file system features you may expect, like permissions and symlinks, are not offered in the developer filesystem.

This differs from the approach of traditional CMS's, but means that broken references between file or syntax errors are caught at publish time rather than at runtime, providing you with extra insulation against accidental failures when live traffic is hitting a website.

Templates in the file system will be automatically detected and will be presented to content creators as they’re making new pages, so the structure of the file system is up to you. There’s no requirement that modules live in a `/modules/` folder or JavaScript lives in a `/js/` folder. However, it's recommended to organize your assets in a similar way to the [boilerplate example code for the CMS](https://github.com/HubSpot/cms-theme-boilerplate). 

**Please note:** by default, HubSpot automatically minifies JavaScript and CSS included in the design manager to remove unnecessary spaces, line breaks, and comments. This also applies to JavaScript and CSS [uploaded to the design manager through the CLI](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development). This means that you should not add already minified code directly to the design manager.

Learn more about [JavaScript and CSS minification](/docs/cms/developer-reference/cdn#javascript-and-css-minification).

Themes, templates, modules, and fields[](https://developers.hubspot.com/docs/cms/key-concepts#themes-templates-modules-and-fields)
----------------------------------------------------------------------------------------------------------------------------------

[Themes](/docs/cms/building-blocks/themes), [templates](/docs/cms/building-blocks/templates), [modules](/docs/cms/building-blocks/modules), and [fields](/docs/cms/building-blocks/module-theme-fields) are the objects you’ll work with most. Using these different objects effectively lets you give content creators the freedom to work and iterate on websites independently while staying inside style and layout guardrails you set.

Themes and modules contain fields, which are settings of specific data types, such as numbers, strings, rich text, and images. You can control how these are used in rendering these objects, as well as how they should be organized and appear in the WYSIWYG editor. Content creators can set values for fields in the WYSIWYG editor, which are applied to the theme or module at render time.

### Themes[](https://developers.hubspot.com/docs/cms/key-concepts#themes)

[Themes](/docs/cms/building-blocks/themes) are the top-level objects that define the look and feel of a website and create a friendly content editing experience. These assets might include templates, modules, CSS files, JavaScript files, images, and more.

*   [
    
    ### Theme
    
    ](https://developers.hubspot.com/docs/cms/building-blocks/themes)
    *   [
        
        #### Theme Fields
        
        ](/docs/cms/building-blocks/themes#theme-fields)
        
        Inputs for content creators to control style settings for themes
        
    *   [
        
        #### Templates
        
        ](https://developers.hubspot.com/docs/cms/building-blocks/templates)
        
        Files that define the markup and style of various page types
        
        *   [
            
            ##### Global Partials
            
            ](/docs/cms/building-blocks/templates/html-hubl-templates#global-partials)
            
        *   [
            
            ##### Drag and Drop Areas
            
            ](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas)
            
        *   [
            
            ##### Modules
            
            ](https://developers.hubspot.com/docs/cms/building-blocks/modules)
            
        *   ##### Markup, CSS, JS
            
    *   [
        
        #### Modules
        
        ](https://developers.hubspot.com/docs/cms/building-blocks/modules)
        
        Reusable objects that can be placed as instances on pages, partials, and drag and drop areas
        
        *   [
            
            ##### Module Fields
            
            ](/docs/cms/building-blocks/modules#fields-json)
            
        *   ##### Markup, CSS, JS
            

Using themes, you can create a set of fields that content creators use to gain global stylistic control over a website without having to edit CSS. You can specify in CSS where these controls are applied, arrange controls to inherit from others, and manage how they are presented and organized to marketers in the Theme Editor. Content creators use the [theme editor](/docs/cms/building-blocks/themes#theme-fields) to modify theme fields, preview those changes against existing templates within a theme, and publish their changes.

These theme fields can be set either globally across a site or overridden at a page level.

![Theme Editor](https://developers.hubspot.com/hs-fs/hubfs/Vitality%20Theme%20Editor.png?width=780&height=425&name=Vitality%20Theme%20Editor.png "Theme Editor")

### Templates[](https://developers.hubspot.com/docs/cms/key-concepts#templates)

[Templates](/docs/cms/building-blocks/templates) define the base markup and style of a set of pages that use a template. They can contain HubL, HTML, and links to JavaScript and CSS files, and can be restricted to use with specific content types. You have full flexibility in the markup and style you can include in a template, but you’re encouraged to adhere to a few best practices and use some key features of Content Hub to ensure marketers can edit pages easily. Some best practices include:

*   Building [templates](/docs/cms/building-blocks/templates) as part of a theme and using theme-level CSS, including theme fields, to do the majority of styling within a template. This’ll make it easy for content creators to make global and local style changes in a consistent way without needing to get into editing CSS.
*   Using [modules](/docs/cms/building-blocks/modules) for the majority of components on your page, which allows them to be rearranged and reused across a website. Learn more about modules below.
*   Using [drag-and-drop areas](/docs/cms/templates/drag-and-drop-areas) where possible for core page content, especially on internal pages. Drag-and-drop areas let you set a default layout for the modules that comprise a page but give marketers flexibility to edit layout and style independently.
*   Using [global partials](/docs/cms/building-blocks/templates/html-hubl-templates#global-partials) to contain shared content like headers and footers that you want to look consistent across a website.

Templates can be built either with [HTML + HubL](/docs/cms/building-blocks/templates/html-hubl-templates) or with a [drag and drop](/docs/cms/building-blocks/templates/drag-and-drop-templates) interface in the [Design Manager](/docs/cms/developer-reference/design-manager). However, it's recommended to coded templates as they provide more control and functionality than drag and drop templates do, such as supporting [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas).

![VS Code with HTML and HubL template open](https://developers.hubspot.com/hs-fs/hubfs/Vitality%20Homepage%20Template%20html.png?width=780&height=452&name=Vitality%20Homepage%20Template%20html.png "VS Code with HTML and HubL template open")

### Modules[](https://developers.hubspot.com/docs/cms/key-concepts#modules)

[Modules](/docs/cms/building-blocks/modules) are reusable components that you can place on templates and pages. They include controls for marketers and contain HubL/HTML markup, CSS, and JavaScript that together build reusable and editable components of a website.

The controls for a module are defined in fields, so building a great module means considering both the resulting appearance on a page, as well as the editing experience for content editors.

**_HubSpot provides a set of_** [default modules](/docs/cms/building-blocks/modules/default-modules) like headers, rich text, images, buttons, and CTAs that you’ll use as fundamental components. You’ll also likely want to build out elements that can have more interesting layouts that fit into your theme and templates. Some common examples of modules you might want to build are accordions, sliders, and tabbers.

![Module form in editor](https://developers.hubspot.com/hs-fs/hubfs/Module%20form%20in%20editor.png?width=780&height=430&name=Module%20form%20in%20editor.png "Module form in editor")

You can think of a module as an object and modules on pages as instances of that object, meaning updates to the [HubL](/docs/cms/hubl), CSS, or JavaScript of a module are applied across all instances of that module inside pages or templates in a given portal. Modules are also portable across portals, whether you’re using the copy tool built into [design manager](/docs/cms/developer-reference/design-manager), selling them in the Marketplace, or sharing the code directly with local development tools. This means you can implement a design solution once and use it across pages and portals, and when you need to update it, those changes can be applied across pages without having to edit multiple pages or multiple templates.

Modules may also be included in themes, which allows you to use theme fields to manipulate the look of modules and ensure they’re prominently displayed in the page editor so content creators can have easy access to modules that’ll look great with the designs you’ve built.

Learn more in the [modules overview guide](/docs/cms/building-blocks/modules).

### Fields[](https://developers.hubspot.com/docs/cms/key-concepts#fields)

[Fields](/docs/cms/building-blocks/module-theme-fields) are the controls that content creators use to adjust the parameters passed into your themes and modules. Fields are typed, including simple types like boolean, text, URL, choice, and file, but also have more complex fields like font with styling as well as HubSpot-specific fields like links to other pieces of content or forms in the HubSpot system.

Fields can also be placed inside repeaters that’ll pass an array to the module—an example of this could be an image carousel where you want a set of images with associated \`alt\` text passed in. Rather than creating a number of image and text fields, you can create one of each and put them in a repeating group.

Fields of a module are specified either inside the design manager or with [this syntax in a fields.json file.](/docs/cms/building-blocks/modules#the-user-interface-for-editing)  Fields for a theme must be specified in the `fields.json` file at the root of the theme.

The HubL Language[](https://developers.hubspot.com/docs/cms/key-concepts#the-hubl-language)
-------------------------------------------------------------------------------------------

The main language that you'll use to build website assets on HubSpot's CMS is the HubSpot Markup Language or [HubL](/docs/cms/hubl) (pronounced “Hubble”). HubL is HubSpot’s extension of [Jinjava](https://github.com/HubSpot/jinjava), a templating engine based on [Jinja](https://palletsprojects.com/p/jinja/). HubL uses a fair amount of markup that is unique to HubSpot and does not support all features of Jinja. It’s executed completely on the server-side when a page is rendered.

HubL has the features you’d expect of a simple templating language like [variables](/docs/cms/hubl/variables), [for loops](/docs/cms/hubl/for-loops), and [if statements](/docs/cms/hubl/if-statements), but also supports more complex rendering [macros](/docs/cms/hubl/variables-macros-syntax#macros), data fetching, and mapping with [tags](/docs/cms/hubl/tags), [functions](/docs/cms/hubl/functions), and [filters](/docs/cms/hubl/filters). 

If you reach the limits of what's possible with HubL, HubSpot provides APIs for creating more customized solutions. Content Hub Enterprise accounts can use [serverless functions](/docs/cms/features/serverless-functions), enabling more sophisticated server side programming. 

You can refer to the [HubL language reference](/docs/cms/hubl) for more details on specific language features.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/key-concepts#page-feedback)
-----------------------------------------------------------------------------------------

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