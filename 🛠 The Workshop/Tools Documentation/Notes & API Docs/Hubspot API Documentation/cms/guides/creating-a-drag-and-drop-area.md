---
Please provide me with the rest of the mission statement! I need more information to understand the context and help you complete it. 

For example, tell me: "* **What is the mission for?** Is it for a company, a non-profit, a project, a personal goal?"
* **What are the core values or goals of this mission?** What do you want to achieve?
* **Who is the target audience?** Who are you trying to reach with this mission?

Once you provide me with more information, I can help you craft a compelling and effective mission statement.
---

Getting started with drag and drop areas


============================================

Last updated: February 9, 2022

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

[Drag and drop areas](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas) allow developers to create sections of pages that support layout, stylistic and content changes directly within the content editors. This allows developers to create few templates with global structure, that support content creators making a multitude of pages with various purposes and layouts, without ever fumbling with code or requiring new templates for small layout changes.

![Animation of modules being dragged onto a page, with columns and rows being adjusted](https://developers.hubspot.com/hubfs/a%20new%20approach.gif "Animation of modules being dragged onto a page, with columns and rows being adjusted")

Developers can specify empty drop zones for drag and drop areas, where content creators build their own page content and layout, or, developers can pre-populate drag and drop areas with various modules, layouts, styles and content to act as a starting point for content creators to work with.

This tutorial will take you through setting up a simple drag and drop area. For more developer resources on drag and drop areas, see the [boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/home.html) for best practices on implementation as well as the [drag and drop area HubL tag reference documentation](//developers.hubspot.com/docs/cms/hubl/tags/dnd-areas).

**Please note:** a content creator can swap a page's template for another template of the same type, depending on whether it has _[dnd\_area](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas)_ tags.

*   Drag and drop templates built with the visual layout editor can be swapped for other drag and drop templates or coded templates with or without _dnd\_area_ tags.
*   Coded templates with _dnd\_area_ tags can only be swapped for other coded templates with _dnd\_area_ tags.
*   Coded templates without _dnd\_area_ tags can only be swapped for other coded templates without _dnd\_area_ tags.

1\. Create a new HTML template[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#create-a-new-html-template)
-----------------------------------------------------------------------------------------------------------------------------------------

Create a new html template to house the HubL and HTML which will make up your drag and drop section.

Drag and drop areas are based on a 12 column responsive grid. Drag and drop tags render markup with class names designating columns and rows.  You are responsible for adding a stylesheet to target those class names. An example of layout styles you could implement can be found in: [CMS-Theme-Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/css/objects/_layout.css). Your stylesheet can be added to the template using [`{{ require_css() }}`](/docs/cms/hubl/tags#require-css).

2\. Create a drag and drop area[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#create-a-drag-and-drop-area)
-------------------------------------------------------------------------------------------------------------------------------------------

A dnd\_area is the container that makes a portion of the web page editable in terms of its structure, design, and content. The body of a dnd\_area tag supplies the default content for the drag-and-drop area. 

This tag on its own will generate a drop zone for content creators to drag modules into within the content creator. 

{% dnd\_area "body\_dnd\_area" %} <!-- generates an empty drag and drop area drop-section --> {% end\_dnd\_area %}

3\. Create a section with a module[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#create-a-section-with-a-module)
-------------------------------------------------------------------------------------------------------------------------------------------------

A dnd\_section is a top-level row, and can only be a direct child of a dnd\_area. Sections support a variety of parameters that control default values for stylistic controls content creators have for sections within the content creators.

Let's set a background image, and set a centered vertical alignment and 1000px max-width for child content. For a full list of supported parameters on the drag and drop HubL tags, see the drag and drop area HubL tag reference documentation. 

To prepopulate the section with content, we can use the dnd\_module tag to include a module by referencing its path. In this example, we are referencing a default HubSpot module, but you can additionally include modules you have built, specifying their path within your Design Tools file tree.

To specify a default value for our dnd\_module, we can use the module\_attribute tag.

{% dnd\_area "body\_dnd\_area" %} {% dnd\_section background\_image = { 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': 'https://www.dragndrop.com/bg-image.jpg' }, max\_width=1000, vertical\_alignment='MIDDLE' %} {% dnd\_module path='@hubspot/rich\_text' %} {% module\_attribute "html"%} This is your main headline. Use this space to tell everyone about what you have to offer. {% end\_module\_attribute %} {% end\_dnd\_module %} {% end\_dnd\_section %} {% end\_dnd\_area %}

Now, we can see our drag and drop area contains a module content creators can edit within the content editor. We can also see how setting a max\_width on the dnd\_section is affecting our content. 

![screenshot of the page editor with the module toolbar displaying](https://developers.hubspot.com/hs-fs/hubfs/dnd_rich_text.png?width=580&height=134&name=dnd_rich_text.png "screenshot of the page editor with the module toolbar displaying")

4\. Include multiple modules[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#include-multiple-modules)
-------------------------------------------------------------------------------------------------------------------------------------

To include more than one module, we can use multiple dnd\_module tags. By setting the offset and width parameters, which are based off of a 12 column grid, we can place an image module next to our rich text module. 

{% dnd\_area "body\_dnd\_area" %} {% dnd\_section background\_image={ 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': 'https://www.dragndrop.com/bg-image.jpg' }, max\_width=1000, vertical\_alignment='MIDDLE' %} {% dnd\_module path='@hubspot/rich\_text', width=8, offset=0, label="Rich Text" %} {% module\_attribute "html"%} <h1>This is your main headline.</h1> <p>Use this space to tell everyone about what you have to offer.</p> {% end\_module\_attribute %} {% end\_dnd\_module %} {% dnd\_module path='@hubspot/linked\_image', width=4, offset=8, img={ "src": "https://www.dragndrop.com/placeholder-image.jpg", "alt": "Stock placeholder image" } %} {% end\_dnd\_module %} {% end\_dnd\_section %} {% end\_dnd\_area %}

Now, we also have an editable image module, as well as a drag handle, allowing content creators to change the width and offset of the modules. We can also see how setting a vertical\_alignment on the dnd\_section is vertically centering our content. 

![screenshot of page editor showing an image module added to a section](https://developers.hubspot.com/hs-fs/hubfs/dnd_rich_image.png?width=690&height=246&name=dnd_rich_image.png "screenshot of page editor showing an image module added to a section")

5\. Incorporate columns and rows[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#incorporate-columns-and-rows)
---------------------------------------------------------------------------------------------------------------------------------------------

To make our drag and drop area more complex, we can incorporate rows and columns using the dnd\_row and dnd\_column tags. Rows and columns act similarly to sections in the content editor, where content creators can drag them around, as well as clone, delete and style the rows and columns. 

{% dnd\_area "body\_dnd\_area" %} {% dnd\_section background\_image={ 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': 'https://www.dragndrop.com/bg-image.jpg' }, max\_width=1000, vertical\_alignment='MIDDLE' %} {% dnd\_module path='@hubspot/linked\_image', width=6, img={ "src": "https://www.dragndrop.com/placeholder-image.jpg", "alt": "Stock placeholder image" } %} {% end\_dnd\_module %} {% dnd\_column width=6, offset=6 %} {% dnd\_row padding={ 'bottom': 15 } %} {% dnd\_module path='@hubspot/rich\_text' %} {% module\_attribute "html"%} <h1>This is your main headline.</h1> <p>Use this space to tell everyone about what you have to offer.</p> {% end\_module\_attribute %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% dnd\_row %} {% dnd\_module path='@hubspot/form' %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% end\_dnd\_column %} {% end\_dnd\_section %} {% end\_dnd\_area %}

Now, our content creators will have further stylistic and layout control over specific rows and columns, in addition to modules and sections. 

![screenshot of page editor showing a row with two columns, an image module left, rich text module and form module on right.](https://developers.hubspot.com/hs-fs/hubfs/dnd_area_full.png?width=700&height=393&name=dnd_area_full.png "screenshot of page editor showing a row with two columns, an image module left, rich text module and form module on right.")

6\. Set generic drag and drop component styles[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#set-generic-drag-and-drop-component-styles)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The various components of drag and drop areas, sections, columns, rows and modules all have classes which can be styled using CSS. The editable styles and options for these components can be set using CSS rather than HubL. For example, default padding can be set on dnd\_sections with the CSS:

.dnd-section { padding: 80px 20px; }

The generic CSS selectors for the drag and drop area components are .dnd-section, .dnd-column, .dnd-row and .dnd-module. Aside from these dnd prefixed classes the actual grid class names in the markup are based on bootstrap 2 names. This does not mean you need to use bootstrap 2 with drag and drop areas. When you add a `dnd_area` to your page, you are responsible for providing the styles that make the grid work. An example of layout styles you could implement can be found in: [CMS-Theme-Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/tree/master/src/css/objects). Your stylesheet can be added to the template using [`{{ require_css() }}`](/docs/hubl/tags#require-css).

For more developer resources on drag and drop areas, see [the boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/tree/master/src/templates) for best practices on implementation as well as the [drag and drop area HubL tag reference documentation](//developers.hubspot.com/docs/cms/hubl/tags/dnd-areas).  

Related tutorials[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#related-tutorials)
-------------------------------------------------------------------------------------------------------------------

*   [Getting started with themes](/docs/cms/guides/getting-started-with-themes)
*   [Getting started with custom modules](/docs/cms/guides/getting-started-with-modules)
*   [How to add theme capabilities to an existing site](/docs/cms/guides/add-theme-features-to-existing-sites)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area#page-feedback)
-----------------------------------------------------------------------------------------------------------------

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