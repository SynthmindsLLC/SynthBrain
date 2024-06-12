---
title: "Using Modules in Templates"
description: "Guide on adding and using modules in templates in HubSpot CMS"
type: "document"
tags:
- "HubL"
- "modules"
- "CMS"
relationships:
- "#part_of [[HubSpot CMS documentation]]"
- "#similar_to [[Using Widgets in Templates]]"
- "#related_to [[Creating and Editing Templates]]"
- "#explains [[Block Syntax]]"
- "#discusses [[Content Attribute]]"
---

Using Modules in Templates


==============================

Last updated: May 4, 2023

Modules can either be added directly to a template or added to individual pages with [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas) and flexible columns. When a module is added to a template, the module will appear in that location by default. Modules in drag and drop areas and flexible columns can be moved and removed, and other modules can be added around them. These are module instances.

After a module has been defined, you can get its field values at the template level through the [content.widgets dict](/docs/cms/building-blocks/modules/export-to-template-context#retrieving-parameters-from-modules-already-rendered-on-the-template).

Basic module syntax[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#basic-module-syntax)
-------------------------------------------------------------------------------------------------------------------------------------

HubL module tags are delimited by `{% %}` , and must specify `module`, a unique name, and the module's design manager path. A module can also include parameters for additional settings.

*   **Module name:** gives the module a unique identity in the context of the template. 
    *   The name must be in quotes following the type of module, and must use underscores instead of spaces or dashes.
    *   This name is used to match the content set within the page/email editor with the corresponding HubL module tag. For example, if you code a HubL module tag with the same name in two different areas of a template, users will only have one module to edit in the editor, but changes to that module will apply in both locations. 
*   **Path:** depending on the tag, defines the location of where the module is in the design manager.
    *   `/` means the root of the current drive;
    *   `./` means the current directory;
    *   `../` means the parent of the current directory.

The path for [HubSpot default modules](/docs/cms/building-blocks/modules/default-modules) always start with `@hubspot/` followed by the type of module.

*   **Parameters:** additional settings for the module instance, specifying its behavior and how it renders. Includes template-level default values for module fields.
    *   Parameters are comma-separated key-value pairs.
    *   Parameters have different types, including: string, boolean, integer, enumeration, and JSON list object. String parameters values must be in single or double quotes, while boolean parameters do not require quotes around their `True` or `False` values. Learn more about the [parameters that are available for all modules](/docs/cms/building-blocks/modules/using-modules-in-templates#parameters-available-for-all-modules).
    *   Note that there is no in-editor validation for field values compared to the module's field settings. For example, if module has a number field that has a minimum value set to `1`, and you pass into the parameter a `0`, you will not see a warning that the value is invalid.

{# Basic syntax #} {% module "unique\_module\_name" path="@hubspot/module\_type", parameterString='String parameter value', parameterBoolean=True %} {# Sample of a default HubSpot text module #} {% module "job\_title" path="@hubspot/text", label="Job Title", value="Chief Morale Officer" %} {# Sample of a custom module #} {% module "faqs" path="/myWebsite/modules/faq\_module", label="Custom FAQ Module" faq\_group\_title="Commonly Asked Questions" %}

Passing dicts to module parameters[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#passing-dicts-to-module-parameters)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

For modules with fields that expect dicts, you can pass them like you would other parameters. If it's cleaner to you or you plan to re-use the values, you can set the dict to a variable, and pass the variable to the parameter instead.

{% module "social\_buttons", path="@hubspot/social\_sharing", email={ "default": true, "enabled": false, "img\_src": "https://..." } %}

### Passing fields that have dnd associated parameters[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#passing-fields-that-have-dnd-associated-parameters)

[Drag and drop tags](/docs/cms/hubl/tags/dnd-areas), such as `dnd_area`, come with a set of default parameters, such as `width`. While the design manager will prevent you from creating new fields that use one of these reserved parameters, modules created before drag and drop tags were introduced may already use a reserved parameter. 

To fix this, you can use the `fields` parameter. Just like you would pass field data to a group, you can pass the field name as a key on the `fields` object. Its value must be consistent with the format the field type expects.

{% dnd\_area "main\_content"%} {% dnd\_section %} {% dnd\_column %} {% dnd\_row %} {% dnd\_module path="@hubspot/divider", fields={width: "90"} %} {% end\_dnd\_module %} {% end\_dnd\_row %} {%end\_dnd\_column%} {% end\_dnd\_section %} {% end\_dnd\_area %}

Setting template-level default values for fields[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#setting-template-level-default-values-for-fields)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can set default values for module fields at the template level by including parameters in the `dnd_module` tags. Below, learn how to set default field values in nested field groups, repeating fields, repeating field groups, and style fields.

### Setting default values for nested field groups[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#setting-default-values-for-nested-field-groups)

Below is an example of a custom drag and drop module with a custom  `style` field group containing other nested field groups. Compare its template-level configuration with how this same grouping would appear in the design manager.

{% dnd\_module path="/Nested\_Module.module" style={ "group":{ "section":{ "color\_field":{ "color" : "#000", "opacity" : 100 } } } } %} {% end\_dnd\_module %}

![multi-level field nesting ](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/multi-level%20field%20nesting%20.png "multi-level field nesting ")

### Setting default values for repeating fields[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#setting-default-values-for-repeating-fields)

You can set template level default values for repeating fields by passing an array to the field's parameter. The array's items must be in the format expected based on the [field type](#field-based-parameters). For example:

*   A simple text field only expects a string
*   An image repeater field expects an image field object. This applies to [all of the other field types](#field-based-parameters).

{% module path='../modules/recipe\_card.module', ingredients=\["Eggs","Ham","Cheese"\] %} {% module "my\_repeater\_module" path="/img\_repeater\_module", label="img\_repeater\_module", image=\[ { "src" : "https://cdn2.hubspot.net/hubfs/428357/Developer%20Site/assets/logo/Developers-LOGO.svg", "alt" : "HubSpot Developers", "width" : 254, "height" : 31 },{ "src" : "https://www.hubspot.com/hs-fs/hub/53/file-733888614-jpg/assets/hubspot.com/about/management/dharmesh-home.jpg", "alt" : "Dharmesh", "width" : 394, "height" : 394 } \] %}

### Setting default values for repeating field groups[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#setting-default-values-for-repeating-field-groups)

Modules that contain repeating groups of fields - like you might see in a slideshow module or FAQ module - can have a template level default set for those groups. To do this you pass an array of objects to your field group's parameter.  The key and value pairs of the object are the field names and their values.

{% module path='../modules/slideshow.module', slides=\[ { "caption":"Cute dog looking up", "image\_url":"http://example.com/image.jpg", }, { "caption":"Cuter cat not looking amused", "image\_url":"http://example.com/image2.jpg", } \] %}

### Setting default values for style fields[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#setting-default-values-for-style-fields)

you can explicitly set default values for [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields) using the `styles` parameter.

This works just like other groups do, where the parameter is the name of the group. You pass an object to that parameter with all of the fields you wish to set.

{% dnd\_module path="./path/to/module", styles={ "background\_color":{ "color":"#123", "opacity":50 } } %}

Block Syntax[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#block-syntax)
-----------------------------------------------------------------------------------------------------------------------

While most modules have parameters that control default content, there may be situations where you need to add large code blocks to the default content of a module. For example, you may want to include a large block of HTML as the default content for a rich text or HTML module. Rather than trying to write that code into a value parameter, you can use HubL block syntax.

{% module\_block module "my\_rich\_text\_module" path="/My Rich Text Field Module", label="My Rich Text Field Module" %} {% module\_attribute "rich\_text\_field\_variable" %} <div>My HTML block</div> {% end\_module\_attribute %} {% end\_module\_block %}

Prior to the `module_block` syntax, `widget_block` was used. It follows the same pattern but the opening tags were `widget_block`, and `widget_attribute`. Closing tags were `end_widget_attribute`, `end_widget_block`.

The `widget_block` syntax is deprecated but you don't need to update old code.

The parameter that immediately follows `module_block` or `widget_block`(deprecated) is the `type_of_module` parameter.

In nearly all of our documentation you will find we use `module`. [V2 HubSpot Modules](/docs/cms/hubl/tags) are normal modules, like what you can create. Therefore there's no longer a need to use a different `type_of_module`.

While `widget_block` is deprecated, and you should use `module_block`. If inheriting a website from another developer it may contain old code using `widget_block` and `type_of_module`.

The `type_of_module` supports V1 HubSpot module names for example: `rich_text` or `raw_html`. Additional parameters can be added to the first line of HubL. The second line defines which parameter the contents of the block will be applied to. For example, for a `rich_text` module this should be the html parameter. For a `raw_html` module, this would be the value parameter (see both examples below). 

{# widget\_block is deprecated, use module\_block instead. This example is only to explain what type\_of\_module was used for, for those with legacy code. #} {% widget\_block rich\_text "my\_rich\_text\_module" overrideable=True, label='My rich-text module' %} {% widget\_attribute "html" %} <h2>New Module</h2> <p>Add content here.</p> {% end\_widget\_attribute %} {% end\_widget\_block %}<span id="hs\_cos\_wrapper\_my\_rich\_text\_module" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_rich\_text" style="" data-hs-cos-general-type="widget" data-hs-cos-type="rich\_text"> <h2>New Module</h2> <p>Add content here.</p> </span>

content\_attribute[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#content-attribute)
----------------------------------------------------------------------------------------------------------------------------------

In addition to regular and block syntax, there are certain instances where you may want to specify a large block default content for a predefined content variable. The most common example of this proves to be the **[content.email\_body](/docs/cms/hubl/variables#email-variables)** variable. This variable prints a standard email body that can be altered in the content editor. Since this isn't a standard HubL module, we use a **content\_attribute** tag to specify a block of default content. The example below shows the email body variable populated with a default content code block.

{% content\_attribute "email\_body" %} <p>Hi {{ contact.firstname }},</p> <p>Describe what you have to offer the customer. Why should they read? What did you promise them in the subject line? Tell them something cool. Make them laugh. Make them cry. Well, maybe don't do that...</p> <p>Use a list to:</p> <ul> <li>Explain the value of your offer</li> <li>Remind the reader what they’ll get out of taking action</li> <li>Show off your skill with bullet points</li> <li>Make your content easy to scan</li> </ul> <p><a href="http://hubspot.com">LINK TO A LANDING PAGE ON YOUR SITE</a> (This is the really important part.)</p> <p>Now wrap it all up with a pithy little reminder of how much you love them.</p> <p>Aw. You silver-tongued devil, you.</p> <p>Sincerely,</p> <p>Your name</p> {% end\_content\_attribute %}

Parameters available for all modules[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#parameters-available-for-all-modules)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

While some modules have certain [special parameters](/docs/cms/hubl/tags), below is a list of parameters supported by all modules.

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`label`

 | String | 

The name of the module displayed in the content editor. This parameter can also be used to give users additional instructions.

 |  |
| 

`overrideable`

 | Boolean | 

Controls whether or not the module can be edited in the content editor, equivalent to the _Prevent editing in content editors_ setting in the design manager.

 | `True` |
| 

`no_wrapper`

 | Boolean | 

When set to `True`, removes the wrapping markup from around the content of a module.

On pages, modules are always wrapped in a `<div>` with special classes. This wrapping markup makes it so when you click the module in the preview pane, the editor scrolls to that module. There may be instances where you want to remove the wrapper, such as if you want to use a text module to populate the destination of an anchor tag `href` attribute.

 | `False` |
| 

`extra_classes`

 | String | 

Adds classes to the module wrapper. You can add multiple classes by separating the classes with spaces. For example:

`extra_classes='full-width panel'`

 |  |
| 

`export_to_template_context`

 | Boolean | 

When set to `True`, instead of rendering the HTML, the parameters from this widget will be available in the template context. [Learn how to use this parameter and the widget\_data tag.](/docs/cms/building-blocks/modules/export-to-template-context)

 | `False` |
| 

`unique_in_loop`

 | Boolean | 

When the module is defined within a loop, appends the module name with the loop.index. When set to `True`, a different version of the module will print within each iteration of the loop. Appends the module name with the loop.index.

 | `False` |

To see a complete list of all module types and their parameters, [click here.](/docs/cms/hubl/tags)

Field-based parameters[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#field-based-parameters)
-------------------------------------------------------------------------------------------------------------------------------------------

Below, learn about the field-based module parameters you can use.

| Field | Type | Example | Keys |
| --- | --- | --- | --- |
| Blog | Integer (blog ID) | `1234567890` |   |
| Boolean | True/false | `false` |   |
| Choice | String | `"option_1"` |   |
| Color | Object | 
    {
      "color" : "#ffffff",
      "opacity" : 100
    }

 | 

color

6 character hexidecimal format

opacity

integer 0 - 100



 |
| CTA | String (CTA ID) | 

    "fb9c0055-6beb-489d-8dda-3e1222458750"

 |   |
| Date | Timestamp | 

    1566360000000

 |   |
| Datetime | Timestamp | 

    1566360000000

 |   |
| Email address | Array (email address strings) | 

    ["develop@hubspot.com", "design@hubspot.com"]

 |   |
| File | String (URL of file) | 

    "https://cdn2.hubspot.net/hubfs/file.pdf"

 |   |
| Follow Up Email | Integer (follow up email ID) | 

    1234567890

 |   |
| Font | Object | 

    {
      "size" : 12,
      "size_unit" : "px",
      "color" : "#000",
      "styles" :{
        "text-decoration" : "underline"
      },
      "font" : "Alegreya",
      "fallback" : "serif",
      "variant" : "regular",
      "font_set" : "GOOGLE"
    }

 | 

size

font size without unit type

size\_unit

font size unit string

*   "px"
*   "pt"
*   "em"
*   "rem"
*   "%"
*   "ex"
*   "ch"

color

hex color code string

styles

supported properties

"font-weight"

"normal" / "bold"

"font-style"

"normal" / "italic"

"font-style"

"none" / "underline"







 |
| Form | Object | 

    {
      "form_id" : "9aa2e5f3-a46d-4774-897e-0bc37478521c",
      "response_type" : "redirect",
      "redirect_url" : "http://www.hubspot.com",
      "redirect_id" : null,
      "form_type" : "HUBSPOT"
    }

 | 

form\_id

The form's ID. [How to get a form's id.](https://knowledge.hubspot.com/forms/find-your-form-guid)

response\_type

"redirect" / "inline"

message

Message displayed if using response\_type "inline". String supporting html.

redirect\_url

String, absolute URL to a webpage

redirect\_id

Page/Post id to redirect to

form\_type

"HUBSPOT" / "TICKET\_FORM"



 |
| HubDB Table | Integer (HubDB table ID) | `123456789` |   |
| Icon | Object | 

    { 
      "name" : "align-center",
      "unicode" : "f037",
      "type" : "SOLID"
    }

 | 

name

The icon's name

unicode

The unicode symbol for the font the icon is from

type

Symbol style. "SOLID" / "REGULAR"

It is recommended you set an icon field and view the values that way, to set the parameters properly. |
| Image | Object | 

    {
      "src" : "https://cdn2.hubspot.net/hubfs/image.jpeg",
      "alt" : "an_image",
      "width" : 100,
      "height" : 100
    }

 | 

src

Image URL

alt

Image alt text, used by screen readers and search engines

width

The width at which the image is to be displayed

height

The height at which the image is to be displayed



 |
| Link | Object | 

    { 
      "url" : { 
        "type" : "EXTERNAL",
        "href" : "www.hubspot.com",
        "content_id" : null 
      },
      "open_in_new_tab" : false,
      "no_follow" : false 
    }

 | 

url

object storing URL data.

type

*   "EXTERNAL" for non HubSpot non-email URLs
*   "CONTENT" for pages, blog posts, and landing pages
*   "FILE" for files uploaded to the file manager
*   "EMAIL\_ADDRESS" for email addresses
*   "BLOG" for blog listing pages

href

The URL you are linking to.

open\_in\_new\_tab

"true"/"false", determines if `target="_blank"` should be added

no\_follow

"true"/"false", determines if `rel="nofollow"` should be used



 |
| Logo | Object | 

    {
      "override_inherited_src" : true,
      "src" : "https://cdn2.hubspot.net/hubfs/logo.png",
      "alt" : "best_logo_ever",
      "width" : 100,
      "height" : 100
    }

 | 

override\_inherited\_src

true/false overide the portal defaults

src

Image URL

alt

Alt text, used for screen readers and search engines.

width

width the image is to be displayed at

height

height the image is to be displayed at



 |
| Meeting | String (meeting link) | `"https://app.hubspot.com/meetings/developers-r-kewl"` |   |
| Menu | Integer (menu ID) | `123456789` |   |
| Number | Integer | `1` |   |
| Page | Integer (page ID) | `1234567890` |   |
| richtext | String (can contain HTML) | `"<h1>Hello, world!</h1>"` |   |
| Salesforce Campaign | String  (Salesforce campaign ID) | `"7016A0000005S0tQAE"` |   |
| Simple Menu | Array of menu item objects | 

    [ 
      { 
        "isPublished" : true,
        "pageLinkId" : 123456789,
        "pageLinkName" : "My page",
        "isDeleted" : false,
        "categoryId" : 1,
        "subCategory" : "site_page",
        "contentType" : "site_page",
        "state" : "PUBLISHED_OR_SCHEDULED",
        "linkLabel" : "This is a page",
        "linkUrl" : null,
        "linkParams" : null,
        "linkTarget" : null,
        "type" : "PAGE_LINK",
        "children" : [ ]
      } 
    ]

 | 

isPublished

true/false is the menu item's page published?

pageLinkId

Page id in the CMS

pageLinkName

The page's actual name in the CMS

isDeleted

true/false

categoryId

*   1 - Site Page
*   3 - Blog post

subCategory

*   site\_page
*   landing\_page
*   blog
*   normal\_blog\_post

contentType

*   site\_page
*   landing\_page
*   blog

state

*   DRAFT
*   DRAFT\_AB
*   PUBLISHED
*   PUBLISHED\_OR\_SCHEDULED
*   PUBLISHED\_AB
*   SCHEDULED

linkLabel

text the user reads and clicks

linkUrl

actual URL the user is sent to upon clicking

linkParams

\# links or ? query parameters

linkTarget

if open in new tab is enabled "\_blank" otherwise "null"

type

*   "PAGE\_LINK"
*   "PAGE\_LINK\_WITH\_PARAMS"
*   "NO\_LINK"

children

array of menu item objects, identical to individual menu items.



 |
| Tag | Integer (tag ID or slug, ID is recommended) | `1234567890` |   |
| Text | String | `"it's like any other string"` |   |
| URL | Object | 

    { 
      "type" : "CONTENT",
      "href" : null,
      "content_id" : 123456789
    }

 | 

type

*   "EXTERNAL" for non HubSpot non-email URLs
*   "CONTENT" for pages, blog posts, and landing pages
*   "FILE" for files uploaded to the file manager
*   "EMAIL\_ADDRESS" for email addresses
*   "BLOG" for blog listing pages

href

String, the URL you are linking to.



 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates#page-feedback)
-------------------------------------------------------------------------------------------------------------------------------

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