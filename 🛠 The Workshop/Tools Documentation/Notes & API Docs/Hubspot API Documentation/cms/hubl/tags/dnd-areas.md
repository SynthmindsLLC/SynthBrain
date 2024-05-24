Drag and Drop Area HubL tags


================================

Last updated: March 15, 2023

[Drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas) allow developers to create sections of pages and global partials that support layout, stylistic and content changes directly within the content editors. See the [creating a drag and drop area tutorial](/docs/cms/guides/creating-a-drag-and-drop-area) for an introduction to setting up drag and drop areas. 

Drag and drop areas are based on a 12 column responsive grid. Drag and drop tags render markup with class names designating columns and rows.  You'll need to add a stylesheet to target those class names. An example of layout styles you could implement can be found in the [HubSpot CMS Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/css/objects/_layout.css). Your stylesheet can be added to the template using [`{{ require_css() }}`](/docs/cms/hubl/tags#require-css).

![](https://play.vidyard.com/g5kieAUP2d4wmUgcAe2oCo.jpg)

[View in HubSpot Academy](https://app.hubspot.com/academy/l/lessons/673/3417 "View HubSpot Academy lesson")

**Please note:** drag and drop areas can't be used in [blog post](/docs/cms/building-blocks/templates/blog-template-markup) and [email templates](/docs/cms/building-blocks/templates#email) at this time.

dnd\_area[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#dnd-area)
---------------------------------------------------------------------------------

A [drag and drop area](/docs/cms/building-blocks/templates/drag-and-drop-areas) is a container that makes a portion of the web page editable in terms of its structure, design, and content. The body of a {% dnd\_area %} tag supplies the default content for the drag and drop area.

Modules themselves cannot contain drag and drop areas. To provide content creators an interface for adding uniform content within a module, use [repeatable fields and groups](/docs/cms/building-blocks/module-theme-fields#repeaters) instead.

A `dnd_area` tag can contain the following parameters:

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`class`

 | String | 

A class added to the wrapping div of a dnd\_area

 |  |
| 

`label`

 | String | 

Used in the editor to label the area in the sidebar.

 |  |

{% dnd\_area "unique\_name", class="main" %} {% end\_dnd\_area %}<div class="container-fluid main"> <div class="row-wrapper"> <div class="row-fluid"> <div class="span12 widget-span widget-type-cell " style="" data-widget-type="cell" data-x="0" data-w="12"> </div> </div> </div> </div>

`dnd_area` tags can also contain `dnd_section` tags.

**Please note:** a content creator can swap a page's template for another template of the same type, depending on whether it has [dnd\_area](/docs/cms/hubl/tags/dnd-areas) tags.

*   Templates built with the visual drag and drop layout editor can be swapped for other drag and drop templates or coded templates with or without `dnd_area` tags.
*   Coded templates with _dnd\_area_ tags can only be swapped for other coded templates with `dnd_area` tags.
*   Coded templates without `dnd_area` tags can only be swapped for other coded templates without `dnd_area` tags.

dnd\_section[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#dnd-section)
---------------------------------------------------------------------------------------

A [{% dnd\_section %}](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections) is a top-level row, and must be nested within a {% dnd\_area %} tag. [Sections can also be defined as a template](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#section-templates), and then [included](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#section-context) into a `dnd_area`, making them ideal for quickly scaffolding out a template.

A `dnd_section` tag can contain the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| 
`background_color`

 | Dict | 

A dict which supports specifying a [background color](#background-color). Can also be provided as a string.

 |
| 

`background_image`

 | Dict | 

A dict which supports specifying a [background image](#background-image).

 |
| 

`background_linear_gradient`

 | Dict | 

A dict which supports specifying a [linear gradient background](#background-linear-gradient).

 |
| 

`full_width`

 | Boolean | 

A boolean which determines if the section is intended to be full width or constrained by an inner container.

 |
| 

`margin`

 | Dict | 

A dict which supports specifying margin values in `cm`, `mm`, `Q`, `in`, `pc`, `pt`, `px`, `em`, `ex`, `ch`, `rem`, `lh`, `vw`, `vh`, `vmin`, `vmax`, and `%`. When no unit of measure is provided, the default of `px` is applied.

 |
| 

`max_width`

 | Integer | 

A pixel value which sets a content max-width on a wrapping dict.

 |
| 

`padding`

 | Dict | 

A dict which supports specifying padding values in `cm`, `mm`, `Q`, `in`, `pc`, `pt`, `px`, `em`, `ex`, `ch`, `rem`, `lh`, `vw`, `vh`, `vmin`, `vmax`, and `%`. When no unit of measure is provided, the default of `px` is applied.

 |
| 

`vertical_alignment`

 | String | Vertical alignment of child content. Available options include:  

*   `TOP`
*   `MIDDLE`
*   `BOTTOM`

 |

**Please note:** you can only use one background parameter per `dnd_section` tag.

{% dnd\_section background\_image={ "backgroundPosition": "MIDDLE\_CENTER", "backgroundSize": "cover", "imageUrl": "https://example.com/path/to/image.jpg" }, margin={ "top": 32, "bottom": 32 }, padding={ "top": "1em", "bottom": "1em", "left": "1em", "right": "1em" }, max\_width=1200, vertical\_alignment="MIDDLE" %} {% end\_dnd\_section %}<div class="row-fluid-wrapper row-depth-1 row-number-1 unique\_name-row-0-background-image dnd-section unique\_name-row-0-max-width-section-centering unique\_name-row-0-margin unique\_name-row-0-padding"> <div class="row-fluid "> </div><!--end row--> </div><!--end row-wrapper -->

`dnd_section` tags can also contain the following tags:

*   dnd\_column
*   dnd\_module

dnd\_column[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#dnd-column)
-------------------------------------------------------------------------------------

A [{% dnd\_column %}](/docs/cms/building-blocks/templates/drag-and-drop-areas#column) is a vertical structural building block that occupies one or more layout columns defined by its parent row.

This HubL tag must be nested within a {% dnd\_area %} tag.

A `dnd_column` tag can contain the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| 
`background_color`

 | Dict | 

A dict which supports specifying a [background color](#background-color).

 |
| 

`background_image`

 | Dict | 

A dict which supports specifying a [background image](#background-image).

 |
| 

`background_linear_gradient`

 | Dict | 

A dict which supports specifying a [linear gradient background](#background-linear-gradient).

 |
| 

`margin`

 | Dict | 

A dict which supports specifying margin values in `cm`, `mm`, `Q`, `in`, `pc`, `pt`, `px`, `em`, `ex`, `ch`, `rem`, `lh`, `vw`, `vh`, `vmin`, `vmax`, and `%`. When no unit of measure is provided, the default of `px` is applied.

 |
| 

`max_width`

 | Integer | 

A pixel value which sets a content max-width on a wrapping dict.

 |
| 

`padding`

 | Dict | 

A dict which supports specifying padding values in `cm`, `mm`, `Q`, `in`, `pc`, `pt`, `px`, `em`, `ex`, `ch`, `rem`, `lh`, `vw`, `vh`, `vmin`, `vmax`, and `%`. When no unit of measure is provided, the default of `px` is applied.

 |
| 

`vertical_alignment`

 | String | Vertical alignment of child content. Available options include:  

*   `TOP`
*   `MIDDLE`
*   `BOTTOM`

 |

**Please note:** you can only use one background parameter per `dnd_column` tag.

{% dnd\_column offset=0, width=12, background\_color={ r: 255, g: 0, b: 0, a: 1 }, margin={ "top": "1em", "bottom": "1em" }, %} {% end\_dnd\_column %}<div class="span12 widget-span widget-type-cell unique\_name-column-1-margin unique\_name-column-1-background-color unique\_name-column-1-vertical-alignment dnd-column" style="" data-widget-type="cell" data-x="0" data-w="12"> </div><!--end widget-span -->

A `dnd_column` tag can also contain `dnd_row`.

dnd\_row[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#dnd-row)
-------------------------------------------------------------------------------

A [{% dnd\_row %}](/docs/cms/building-blocks/templates/drag-and-drop-areas#row) is a horizontal structural building block that creates a nested 12-column layout grid in which columns and modules can be placed.

This HubL tag must be nested within a {% dnd\_area %} tag.

A `dnd_row` tag can include the following parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| 
`background_color`

 | Dict | 

A dict which supports specifying a [background color](#background-color).

 |
| 

`background_image`

 | Dict | 

A dict which supports specifying a [background image](#background-image).

 |
| 

`background_linear_gradient`

 | Dict | 

A dict which supports specifying a [linear gradient background](#background-linear-gradient).

 |
| 

`margin`

 | Dict | 

A dict which supports specifying margin values in `cm`, `mm`, `Q`, `in`, `pc`, `pt`, `px`, `em`, `ex`, `ch`, `rem`, `lh`, `vw`, `vh`, `vmin`, `vmax`, and `%`. When no unit of measure is provided, the default of `px` is applied.

 |
| 

`max_width`

 | Integer | 

A pixel value which sets a content max-width on a wrapping dict.

 |
| 

`padding`

 | Dict | 

A dict which supports specifying padding values in `cm`, `mm`, `Q`, `in`, `pc`, `pt`, `px`, `em`, `ex`, `ch`, `rem`, `lh`, `vw`, `vh`, `vmin`, `vmax`, and `%`. When no unit of measure is provided, the default of `px` is applied.

 |
| 

`vertical_alignment`

 | String | Vertical alignment of child content. Available options include:  

*   `TOP`
*   `MIDDLE`
*   `BOTTOM`

 |

**Please note:** you can only use one background parameter per `dnd_row` tag.

{% dnd\_row background\_color={ r: 123, g: 123, b: 123, a: 1.0 }, margin={ "top": 20, "bottom": 200 }, padding={ "top": 20, "bottom": 200, "left": 20, "right": 20 } %} {% end\_dnd\_row %}<div class="row-fluid-wrapper row-depth-1 row-number-1 main-row-0-padding main-row-0-background-color main-row-0-margin"> <div class="row-fluid "> </div> </div>

A dnd\_row can also contain the following tags:

*   dnd\_column
*   dnd\_module

dnd\_module[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#dnd-module)
-------------------------------------------------------------------------------------

A [{% dnd\_module %}](/docs/cms/building-blocks/templates/drag-and-drop-areas#module) is a [module](/docs/cms/building-blocks/modules) wrapped within a div where layout, styles and content can be added. The module is specified by referencing its path, which can either be a HubSpot default module (using the @hubspot/ namespace), or modules you have built, specifying their path within the design manager file tree.

This HubL tag must be nested within a {% dnd\_area %} tag.

A `dnd_module` tag can contain the following parameters:

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`path`

Required



 | String | 

The path to a module.

 |
| 

`horizontal_alignment`

 | String | 

Horizontal positioning, supports:

`LEFT`, `CENTER`, `RIGHT`

 |
| 

`offset`

 | Integer | 

The offset from 0 in the 12 column grid.

 |
| 

`width`

 | Integer | 

The number of columns occupying the 12 column grid.

 |
| 

`flexbox_positioning`

Deprecated



 | String | 

**Deprecated do not use.** Instead, use `horizontal_alignment` in tandem with the row or section's `vertical_alignment` instead.

  
Flexbox position value for the module. Supported a string indicating vertical position followed by horizontal:

*   `TOP_LEFT`
*   `TOP_CENTER`
*   `TOP_RIGHT`
*   `MIDDLE_LEFT`
*   `MIDDLE_CENTER`
*   `MIDDLE_RIGHT`
*   `BOTTOM_LEFT`
*   `BOTTOM_CENTER`
*   `BOTTOM_RIGHT`

 |

Have an old module which has a field name that matches one of the `dnd_module` parameters above? You can [pass default values through a fields parameter](/docs/cms/building-blocks/modules/using-modules-in-templates#passing-fields-that-have-dnd-associated-parameters), much like you would a field group.

{% dnd\_module path="@hubspot/rich\_text", offset=0, width=8, %} {% module\_attribute "html" %} <h1>Hello, world!</h1> {% end\_module\_attribute %} {% end\_dnd\_module %}<div class="span8 widget-span widget-type-custom\_widget" style="" data-widget-type="custom\_widget" data-x="0" data-w="12"> <div id="hs\_cos\_wrapper\_main-module-1" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module" > <span id="hs\_cos\_wrapper\_module-1\_" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_rich\_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rich\_text"> <h1>Hello, world!</h1> </span> </div> </div>

Background[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#background)
------------------------------------------------------------------------------------

There are a few ways to set backgrounds on column, section and row dnd elements, [`background_image`](#background-image), [`background_linear_gradient`](#background-linear-gradient), and [`background_color`](#background-color). 

### background\_color[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#background-color)

The column, section, and row dnd tags support background colors. You can set the default background color for a drag and drop element using `background_color`. This parameter is a string based parameter and can include the following formats outlined in the example below. 

{% dnd\_section %} // Hex Value (both 3 and 6 char length) {% dnd\_column background\_color="#F7F7F7" %} {% end\_dnd\_column %} {% dnd\_column background\_color="#FFF" %} {% end\_dnd\_column %} // Both RGB and RGBA {% dnd\_column background\_color="rgb(255,255,255)" %} {% end\_dnd\_column %} {% dnd\_column background\_color="rgba(0,0,0,.25)" %} {% end\_dnd\_column %} {% end\_dnd\_section %}

### background\_linear\_gradient[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#background-linear-gradient)

The column, section and row dnd elements support background linear gradients. You can set a default gradient using the `background_linear_gradient` parameter. The parameter expects a dict. Currently only supports two color stops.

| Parameter | Type | Description |
| --- | --- | --- |
| 
`direction`

 | String | 

The direction of the gradient.

*   `to bottom`
*   `to top`
*   `to left`
*   `to right`

 |
| 

`colors`

 | array | 

Array of color strings. Currently supports 2 values, the start and end. Values are provided as strings, and the following formats are supported:

*   `RGB`
*   `RGBA`
*   `3 char hex`
*   `6 char hex`
*   `8 char hex`

 |

{% dnd\_section background\_linear\_gradient={ "direction": "to bottom", "colors": \[ "#1EB6C3", "#2A2859" \] } %} {% dnd\_module path="@hubspot/rich\_text" width="6" %} {% end\_dnd\_module %} {% end\_dnd\_section %}

### background\_image[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#background-image)

The column, section and row dnd elements support background images. You can provide a default background image by using the `background_image` parameter which expects a dict.

Use this table to describe parameters / fields
| Key | Type | Description |
| --- | --- | --- |
| 
`backgroundPosition`

 | String | 

The background position of the image. Supports a string indicating vertical position followed by horizontal.

*   `TOP_LEFT`
*   `TOP_CENTER`
*   `TOP_RIGHT`
*   `MIDDLE_LEFT`
*   `MIDDLE_CENTER`
*   `MIDDLE_RIGHT`
*   `BOTTOM_LEFT`
*   `BOTTOM_CENTER`
*   `BOTTOM_RIGHT`

 |
| 

`backgroundSize`

 | String | 

The CSS background size property used for the image.  
Supported values are:

*   `cover`
*   `contain`
*   `auto`

 |
| 

`imageUrl`

 | String | 

Absolute URL to the image.

 |

{% dnd\_section background\_image = { "backgroundPosition": "MIDDLE\_CENTER", "backgroundSize": "cover", "imageUrl": "https://www.example.com/bg-image.jpg" }, %} {% dnd\_module path="@hubspot/rich\_text" width="6" %} {% end\_dnd\_module %} {% end\_dnd\_section %}

How dnd style parameters translate to the page[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#how-dnd-style-parameters-translate-to-the-page)
------------------------------------------------------------------------------------------------------------------------------------------------------------

When you are using style based parameters such as [backgrounds](#background), margins, or padding, the class names are automatically computed for your sections, columns, rows, and modules. The property values you have assigned are then added to those automatically created class names and the resulting CSS code is then placed before the closing `</body>` tag on the page in a `<style>` tag. 

[Drag and drop styles can also be different at different breakpoints](/docs/cms/building-blocks/themes/responsive-breakpoints) to offer a responsive look.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#page-feedback)
------------------------------------------------------------------------------------------------

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