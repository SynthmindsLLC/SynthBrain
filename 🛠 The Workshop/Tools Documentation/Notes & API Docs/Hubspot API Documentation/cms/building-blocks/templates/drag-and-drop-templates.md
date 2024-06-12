---
title: "Drag and Drop Templates"
description: "Drag and drop templates are not recommended for new templates."
type: "concept"
tags:
- "Templating"
- "Design"
- "HubSpot_CMS"
- "Website_Building"
- "Drag_and_Drop"
relationships:
- "#differs_from [[HTML + HubL Templates]]"
- "#used_by [[Marketing Hub]], [[Content Hub]]"
- "#precedes [[Drag and Drop Areas]]"
- "#produces [[Website]]"
- "#influenced_by [[Bootstrap_2]]"
- "#replaced_by [[Drag and Drop Areas]]"
- "#requires [[Visual Template Builder]]"
---

Drag and drop templates


===========================

Last updated: January 12, 2023

**Drag and drop templates are not recommended for new templates.** These templates are not able to be part of a theme, and so they do not support theme functionality like theme fields, and theme modules. Drag and drop templates are **NOT** supported in CMS Hub Starter, use `dnd_area` instead. Drag and drop templates do not support several of the newer features of the CMS ([memberships](/docs/cms/features/memberships), [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas), [reusable sections](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections), GraphQL and many other features). They lack extensibility and do not provide as good of a content creator and developer experience as coded templates. **Instead, we recommend coded [HTML + HubL templates](/docs/cms/building-blocks/templates/html-hubl-templates) with [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas), which deliver a better experience for developers and marketers**. For a quick start on the CMS, we recommend checking out the [HubSpot Theme Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate) which is built using coded templates.

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

Drag and drop [templates](/docs/cms/building-blocks/templates) were designed for less technical users to be able to easily create a website on the HubSpot CMS. Drag and Drop templates take advantage of a visual template builder, which generates HTML + HubL under the hood. 

In order to make the visual builder work the HTML output is controlled by HubSpot and you do not have direct control over the structural portions of it. In-addition **a layout.css file is loaded onto the page which enables a basic 12 column grid** based on bootstrap 2. This makes all sites built with drag and drop templates responsive by default causing rows of content to stack vertically, for more complicated and custom responsiveness you'll want to add your own responsive styles.

Drag and Drop templates are built in the Design Manager, when interacting with them via the API or the [local development tools](/docs/cms/guides/getting-started-with-local-development) they are represented as JSON. Due to the nature of drag and drop templates the only recommended way to edit them is through the Design Manager interface. **If you prefer to code, use version control or simply want to be able to edit using your preferred tools locally, HTML + HubL coded templates offer the best experience for developers.** The [dnd\_area](/docs/cms/hubl/tags/dnd-areas) functionality for HTML + HubL templates also provides a better experience for content creators than the design manager drag and drop interface as it keeps them in the visual content editor. 

The Drag and Drop Template Builder[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#the-drag-and-drop-template-builder)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

To create a drag and drop template, open the Design Manager and in the finder, create a new file, choose a template, and the [type of template](/docs/cms/building-blocks/templates#template-types) you're creating.

Drag and drop templates are made up of building blocks, these blocks are modules, groups, global groups, and flexible columns.

[Learn how to use the Drag and Drop template builder.](https://knowledge.hubspot.com/structure-and-customize-template-layouts)

### Modules[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#modules)

Modules are reusable components that are editable portions of a page. Modules are made up of an HTML + HubL template fragment, CSS, JS, and fields. Modules can be placed inside of flexible columns and dnd\_areas by content editors, and are the primary way that content editors manage the content of their website. You can build modules to handle any number of functions, search, image galleries, menus, complex marketing animations, calculators, product comparisons, the possibilities are down to your imagination and what you think provides a good experience for content creators. The fields are how the content editor controls their output. Modules are not unique to drag and drop templates, they are a very important core building block for the HubSpot CMS. In Drag and Drop templates the default values for module fields can be configured in the [inspector](https://knowledge.hubspot.com/cos-general/use-the-inspector-to-style-your-template). [Learn more about Modules.](/docs/cms/building-blocks/modules)

![Design Manager interface with modules highlighted](https://developers.hubspot.com/hs-fs/hubfs/image2-3.png?width=816&height=672&name=image2-3.png "Design Manager interface with modules highlighted")

### Groups[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#groups)

Groups are wrappers for other groups and modules, they can have CSS classes, and wrapping HTML. Groups manifest themselves as wrapping HTML with layout classes to facilitate placement and sizing of the groups. Groups can also have an internal-only name. With this, you can [group modules](https://knowledge.hubspot.com/structure-and-customize-template-layouts#group-modules) in the Design Manager making it easier to visually identify parts of a page. An example of this might be for sidebars or banners.

Being that [HTML + HubL](/docs/cms/building-blocks/templates/html-hubl-templates) files are the recommended path for new sites, columns, sections, and rows of [Drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas) largely replace the purposes of groups.

Additionally a developer can create partials, and [global partials](/docs/cms/building-blocks/global-content), which can contain freeform code in-addition to drag and drop areas.

Drag and drop areas, partials, and global partials are not supported in drag and drop templates.

![Design manager screenshot with sidebar group selected](https://designers.hubspot.com/hs-fs/hubfs/image4-1.png?width=816&height=363&name=image4-1.png "Design manager screenshot with sidebar group selected")

### Global Groups[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#global-groups)

Global groups are groups that when edited affect the entire website and not just the page they are on. Global groups can exist in multiple templates and most commonly are used for site headers and footers. Global groups are similar to partials but are limited to the structure that drag and drop templates enforce. They can be embedded into HTML + HubL files if needed, but most of the time it makes more sense to use a global partial instead.

![Design Manager interface with header and footer global groups highlighted](https://developers.hubspot.com/hubfs/image1-3.png "Design Manager interface with header and footer global groups highlighted")

### Flexible columns[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#flexible-columns)

Flexible columns are a special type of group. They can contain a default set of modules, but content editors can add, remove, and move modules within them. Flexible columns allow reordering of modules in a one dimensional way, vertically up and down. [Unlike dnd\_area tags](/docs/cms/building-blocks/templates/drag-and-drop-areas), flexible columns do not support sections, or the styling capabilities, afforded to modules within them. Flexible columns are not unique to drag and drop templates, there is a [HubL tag](/docs/cms/hubl/tags#flexible-column) which can be used in [HTML + HubL](/docs/cms/building-blocks/templates/html-hubl-templates) templates. [Learn how to add a flexible column to a drag and drop template.](https://knowledge.hubspot.com/structure-and-customize-template-layouts#add-a-flexible-column)

It is generally recommended to use drag and drop areas, as most of the time they are more useful and provide all of the capabilities flexible columns provide.  
  
There may still be useful times to use a flexible column, for something like a sidebar. For main content areas drag and drop areas are much more flexible.

![Design manager screenshot with Main content group selected](https://designers.hubspot.com/hubfs/image3-2.png "Design manager screenshot with Main content group selected")

Why use flexible columns? Websites are not usually rigid. They are built and maintained over long periods of time. A homepage for example for a business may show off featured products, and may frequently change as the business's marketing needs change over time. Since content within a flex column can be added/removed and modified by content editors, the experience is less painful for marketers and enables developers to focus on what they enjoy, building cool stuff instead of making minor page adjustments.

Similarly, pages throughout a site may have different structural needs. Flex columns give the marketers control to create those pages using custom modules.

### Add custom code to your drag and drop templates[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#add-custom-code-to-your-drag-and-drop-templates)

There are a handful of ways to add custom code to your drag and drop templates. The primary method is through custom modules. Sometimes though you may need to add code that wraps around modules or groups. In order to do this, click on the module or group to view it in the inspector and find the wrapping HTML field. Add your HTML there.

Sometimes you may need to add code to the head of your HTML or code right above the `</body>`. With your template open make sure you don't have anything selected. The inspector will show fields for the template itself. Here you can link Stylesheets, and javascript files while also adding additional HTML in the head or just before the `</body>` tag.

For this you'll use the [inspector](https://knowledge.hubspot.com/cos-general/use-the-inspector-to-style-your-template). The inspector has fields at the template level for [stylesheets, javascript](https://knowledge.hubspot.com/cos-general/use-the-inspector-to-style-your-template##attach-stylesheets-and-javascript-files), [`<head>` markup](https://knowledge.hubspot.com/cos-general/use-the-inspector-to-style-your-template#customize-your-template-s-head-and-body-options), etc.

![custom code inspector panel of Design Manager](https://designers.hubspot.com/hs-fs/hubfs/image5.png?width=334&height=791&name=image5.png "custom code inspector panel of Design Manager")

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-templates#page-feedback)
------------------------------------------------------------------------------------------------------------------------------

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