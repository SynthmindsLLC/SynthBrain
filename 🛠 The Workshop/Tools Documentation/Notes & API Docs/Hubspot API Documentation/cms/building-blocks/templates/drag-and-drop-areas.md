---
title: "Drag and Drop Areas Overview"
description: "Drag and drop areas enable you to create areas of pages and global partials where content creators can place modules, change layout, and add styling within the content editor."
type: "concept"
tags:
- "Drag_and_Drop"
- "Content_Management"
- "Layout"
relationships:
- "#used_for [[Creating Layouts]]"
- "#enables [[Content Creators]]"
- "#differs_from [[Fixed Layouts]]"
---

Drag and Drop areas overview


================================

Last updated: December 5, 2022

Drag and drop areas enable you to create areas of pages and global partials where content creators can place modules, change layout, and add styling within the content editor. Using drag and drop areas, you can create fewer templates, as content creators are able to create layouts on their own. 

Below, learn more about the `dnd_area` experience and concepts. Once you're ready to build, see [getting started with dnd\_area](/docs/cms/guides/creating-a-drag-and-drop-area?_ga=2.125877323.719400123.1583936069-816758351.1565959634), and the [dnd\_area reference](/docs/cms/hubl/tags/dnd-areas).

**Please note:** drag and drop areas can't be used in [blog post](/docs/cms/building-blocks/templates/blog-template-markup) and [email templates](/docs/cms/building-blocks/templates#email).

The content creator experience[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#the-content-creator-experience)
------------------------------------------------------------------------------------------------------------------------------------------------------

When a content creator creates a page using a template that has drag and drop areas, they first see the page with predefined modules in the layout that you've defined as the developer. This initial layout sets the precedent for how pages using this template might look. Using drag and drop areas, the content creator can then build the page, including:

*   Adding modules, sections, rows, and columns.
*   Resizing modules and updating their content and styling, such as adjusting alignment and adding backgrounds.

This gives content creators enough flexibility to make simple page changes without needing a developer for small tweaks.

**Please note:** a content creator can swap a page's template for another template of the same type, depending on whether it has [dnd\_area](/docs/cms/hubl/tags/dnd-areas) tags.

*   Templates built with the visual drag and drop layout editor can be swapped for other drag and drop templates or coded templates with or without `dnd_area` tags.
*   Coded templates with _dnd\_area_ tags can only be swapped for other coded templates with `dnd_area` tags.
*   Coded templates without `dnd_area` tags can only be swapped for other coded templates without `dnd_area` tags.

![The page editor experience for dnd_areas](https://developers.hubspot.com/hubfs/drag-and-drop.gif "The page editor experience for dnd_areas")

The developer experience[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#the-developer-experience)
------------------------------------------------------------------------------------------------------------------------------------------

Developing with drag and drop areas is similar to working with common CSS frameworks and their grids. First you'll lay out the page using containers, called [sections](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections), which contain rows. Inside of those rows are modules and columns. Learn more about these [elements](#drag-and-drop-area-elements) below.

While you could hard-code nearly everything into the template, the goal of developing with drag and drop areas is that you instead build the default page content which can later be edited by a content creator. 

View the [HubSpot CMS Boilerplate templates](https://github.com/HubSpot/cms-theme-boilerplate/tree/master/src/templates) to see `dnd_area` tags in use.

![dnd_area coded in VS Code](https://developers.hubspot.com/hubfs/dnd%20coded.png "dnd_area coded in VS Code")

Drag and drop area elements[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#drag-and-drop-area-elements)
------------------------------------------------------------------------------------------------------------------------------------------------

When building a page with drag and drop areas, you'll include the following elements: 

*   [**dnd\_area**](/docs/cms/hubl/tags/dnd-areas#dnd-area): the highest-level drag and drop element which enables dragging and dropping modules in the content editor. You cannot nest drag and drop areas. For example, a `dnd_section` cannot contain a `dnd_area` tag.
*   [**dnd\_section**](/docs/cms/hubl/tags/dnd-areas#dnd-section): the outermost container in a `dnd_area`. Can contain `dnd_row`, `dnd_column`, and `dnd_module`. You cannot nest a `dnd_section` within other drag and drop elements.
*   [**dnd\_column**](/docs/cms/hubl/tags/dnd-areas#dnd-column): can contain `dnd_row`. Multiple columns within a `dnd_row` will align the row's contents horizontally.
*   [dnd\_row](/docs/cms/hubl/tags/dnd-areas#dnd-row)**:** can contain `dnd_module` and `dnd_column`.
*   [dnd\_module](/docs/cms/hubl/tags/dnd-areas#dnd-module): a module wrapper where module layout, styles, and content can be added. 

Learn more about each of these tags below. In addition, you may want to walk through the [Getting started with drag and drop areas guide](/docs/cms/guides/creating-a-drag-and-drop-area) for a hands-on approach.

![Drag and Drop relationships](https://developers.hubspot.com/hs-fs/hubfs/Drag%20and%20Drop%20relationships.png?width=1013&height=221&name=Drag%20and%20Drop%20relationships.png)

The diagram below further breaks down the hierarchy of the various drag and drop elements.

[![Example structure](https://developers.hubspot.com/hubfs/Example%20structure.png "Example structure")](https://designdev.hubspot.com/hubfs/Example%20structure.png)

For a video walkthrough of how to visualize drag and drop areas, check out the video below:

Continue reading to learn more about drag and drop sections, rows, columns, and modules.

### Sections[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#sections)

Sections are a special type of row which are created using the [`dnd_section`](/docs/cms/hubl/tags/dnd-areas#drag-and-drop-section-code-dnd-section-code-) tag. They are the only drag and drop element that can be a direct descendant of a `dnd_area`. You can think of sections like an outer wrapping container. They can enable content to be full width or have a confined center max-width. Because sections wrap around columns and modules, it makes it easy to rearrange and implement large portions of content. The `dnd_section` tag does not render an HTML `<section>` element.

Below is a screenshot of how a section appears in the page editor.

![Section in page editor](https://developers.hubspot.com/hubfs/Section%20in%20page%20editor.png "Section in page editor")

In addition to the `dnd_section` tag, you can also create [section templates](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#create-reusable-sections) which are pre-defined reusable sections that content creators can access in the page editor. For example, you could build the section shown in the screenshot above as a section template so that a content creator could quickly add it to pages as needed. Section templates have some unique capabilities, including being able to use them similar to a standard hubL template partial.

### Columns[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#columns)

Columns are wrappers for rows and modules and can be placed inside of a row or section. Columns are created using the [`dnd_column`](/docs/cms/hubl/tags/dnd-areas#drag-and-drop-column-code-dnd-column-code-) tag.

Use multiple columns inside of a row to place rows and the modules they contain horizontally. 

Columns are vertical regions that can contain rows. You can make columns of different sizes by changing their width. A row’s size is 12 "columns" wide, this refers to the CSS grid. The columns inside of a row can be any size smaller than 12 but cannot add up to more than 12.

When multiple rows are placed inside of a column the modules inside of those rows will appear vertically stacked. Since modules are columns themselves, a module cannot be a direct descendant of a column, they must be contained within a row.

![dnd_area column in page editor](https://developers.hubspot.com/hubfs/dnd_area%20column%20in%20page%20editor.png "dnd_area column in page editor")

The appearance of a column in the page editor.

### Rows[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#rows)

Rows are wrappers for columns. Rows are created in templates using the `[dnd_row](/docs/cms/hubl/tags/dnd-areas#drag-and-drop-row-code-dnd-row-code-)` tag. Since modules are columns you can place them directly inside of a row. This will cause the modules to appear horizontally adjacent to each other.

Modules can be organized vertically by placing them inside of rows. If you want to place a module above another you would place that module inside a row. You would then add another module in a row above or below that first row. 

![dnd_area row in page editor](https://developers.hubspot.com/hubfs/dnd_area%20row%20in%20page%20editor.png "dnd_area row in page editor")

The appearance of a row in the page editor.

### Modules[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#modules)

[Modules](/docs/cms/building-blocks/modules) are a fundamental part of the HubSpot CMS, acting as reusable building blocks that you use to piece together a site, and display content. When building a template you place modules inside of drag and drop rows and sections using the [`dnd_module`](/docs/cms/hubl/tags/dnd-areas#drag-and-drop-module-code-dnd-module-code-) tag. Modules are also columns. Meaning if you place two module tags, or a module and a column directly next to each other, they will appear side-by-side horizontally. 

No drag and drop elements can be placed within a module. Modules cannot be direct children of a [`dnd_area`](/docs/cms/hubl/tags/dnd-areas#drag-and-drop-area-code-dnd-area-code-).

HTML structure and styling[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#html-structure-and-styling)
----------------------------------------------------------------------------------------------------------------------------------------------

Drag and drop areas and their elements when rendered have class names for a 12 column grid based on bootstrap 2. To make it easy to get up and running, you can use the [\_layout.css](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/css/objects/_layout.css) file from the [HubSpot CMS Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/). This provides default styles for those class names. 

You are not required to use this stylesheet and can provide your own styles instead. If you're building your site based off of the CMS Theme Boilerplate and want to use your own CSS, you will want to [remove layout.css from being called in base.html](https://github.com/HubSpot/cms-theme-boilerplate/blob/5abaf2a4c45a95dbed1d459f7f0f6407350752ac/src/templates/layouts/base.html#L8). For your own CSS grid you will need to target those same grid class names, but the styling is up to you.

Drag and drop areas when rendered create divs with classes that are used by the page editor. Examples would be `widget-span` and `widget-type-cell`. You should not directly target these classes as they are used by page-editor and could change down the road.  
  
Instead in your `[dnd_area](/docs/cms/hubl/tags/dnd-areas#drag-and-drop-area-code-dnd-area-code-)` HubL add a class parameter with a class name you would like to use

<div class="container-fluid my-custom-class"> <div class="row-fluid-wrapper"> <div class="row-fluid"> <div class="span12 widget-span widget-type-cell " style="" data-widget-type="cell" data-x="0" data-w="12"> </div> <!--end widget-span --> </div> </div> </div>

### Editor and attribute styling[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#editor-and-attribute-styling)

With drag and drop areas content creators can have some effect on styling of the page. For example they can set a section to have a background. Developers can pass default values for those settings through attributes.

When the page is actually rendered, the styles that are generated based on those settings is added to the `standard_header_includes`.

At launch of `dnd_area` those styles were loaded from `standard_footer_includes`. That was [changed recently](/changelog/drag-and-drop-area-styles-moved-from-footer-to-header) to `standard_header_includes` and is rolling out to all HubSpot accounts with the HubSpot CMS.

Migrating flexible columns[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#migrating-flexible-columns)
----------------------------------------------------------------------------------------------------------------------------------------------

If you are changing templates built with flexible columns to now use drag and drop areas, keep the following in mind about flexible columns.

Flexible columns are not the same as drag and drop areas, and you can't swap from a template that only has a flexible column to one that only has a drag and drop area. This limitation was put in place because the content would not map from the flexible column to the drag and drop area. To illustrate why this is, suppose you built your new template so you have a sidebar and a main content area. Your sidebar is a flexible column, your main content is a drag and drop area. The swapping tool would map the flexible column to the flexible column.

Learn more about [adding drag and drop areas to existing pages](/docs/cms/guides/add-theme-features-to-existing-sites#drag-and-drop-areas).

Related resources[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#related-resources)
----------------------------------------------------------------------------------------------------------------------------

*   [Adding drag and drop areas to existing websites](/docs/cms/guides/add-theme-features-to-existing-sites#drag-and-drop-areas)
*   [Creating a drop area](/docs/cms/guides/creating-a-drag-and-drop-area)
*   [Visualizing Drag and Drop Areas - YouTube](https://youtu.be/RUs24n8DfzA)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas#page-feedback)
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