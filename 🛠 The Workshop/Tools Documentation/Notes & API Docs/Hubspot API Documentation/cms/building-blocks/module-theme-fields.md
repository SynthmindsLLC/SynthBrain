---
title: "Module and theme fields"
description: "Last updated: April 11, 2024. Add fields to modules and themes to allow content creators to control various aspects of a page within the page editor. Below, learn about all of the fields available for modules and themes, along with their available properties. For more information about implementing module and theme fields, including field groups and repeating fields, view the [module and theme fields overview](/docs/cms/building-blocks/module-theme-fields-overview)."
type: "document"
tags:
- "Module"
- "Theme"
- "Fields"
relationships:
- "#related_to [[Page Editor]]"
---

Module and theme fields


===========================

Last updated: April 11, 2024

Add fields to modules and themes to allow content creators to control various aspects of a page within the page editor. Below, learn about all of the fields available for modules and themes, along with their available properties.

For more information about implementing module and theme fields, including field groups and repeating fields, view the [module and theme fields overview](/docs/cms/building-blocks/module-theme-fields-overview).

Properties used by all fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#properties-used-by-all-fields)
------------------------------------------------------------------------------------------------------------------------------------------

All fields share a set of common properties. These are general fields, such as the field's name or the help text that displays for content creators using the field in the module or theme. 

// Boolean field { "name" : "is\_teaser\_img", "label" : "Enable Teaser Image", "required" : false, "locked" : false, "type" : "boolean", "inline\_help\_text" : "Shows Teaser image when toggled on", "help\_text" : "Teaser images are used to help provide visual context to the post.", "default" : false }

Properties used by all fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`name`

 | String | 

The field's name, which you'll reference when incorporating the field and its values in the module or theme. Cannot contain spaces or special characters.

 | `richtext_field, date_field, etc.` |
| 

`label`

 | String | 

The text the content creator sees describing the field. May contain spaces.

 | `Rich text field, Date field, etc.` |
| 

`required`

 | Boolean | 

Sets whether the field can be left blank in the editor. If `true`, content cannot be published without a value in the field.

 | `false` |
| 

`locked`

 | Boolean | 

Sets whether the field is editable in the content editor. If `true`, the field will not appear in the content editor.

 | `false` |
| 

`type`

 | String | 

The type of field. Field types are unique per field and can be found within the documentation for each field below.

 |  |
| 

`inline_help_text`

 | String | 

Text that displays inline below field's label (limit 400 characters). Best used for information required to use the field.

You can include the following HTML tags (other tags will be ignored on render):

`a`, `b`, `br`, `em`, `i`, `p`, `small`, `strong`, `span`.

 |  |
| 

`help_text`

 | String | 

Text that displays in the editor within a tooltip on hover to assist the content creator (limit 300 characters). Best used for information that is supplementary but not required to use the field.

You can include the following HTML tags (other tags will be ignored on render):

`a`, `b`, `br`, `em`, `i`, `p`, `small`, `strong`, `span`.

 |  |
| 

`id`

 | String | 

The field's unique ID, which is set by HubSpot. When building locally you do not need to specify this ID.

 |  |
| 

`visibility`

 | Array | 

Sets the field's display conditions. For example, you can set a field to only display when another checkbox field has been selected. Learn more about [visibility](/docs/cms/building-blocks/module-theme-fields-overview#field-visibility).

 |  |
| 

`display_width`

 | String | 

By default, fields are full-width in the editor. When two consecutive fields in the `fields.json` file are set to `half_width`, they will instead appear next to each other in the editor.

 |  |

Alignment[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#alignment)
--------------------------------------------------------------------------------------------------

Enables content creators to position an element within a container. To enable text alignment, use the [text alignment field](/docs/cms/building-blocks/module-theme-fields#text-alignment) instead. 

Alignment fields are supported in [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules) and can only be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Alignment field](https://developers.hubspot.com/hs-fs/hubfs/Alignment-field.png?width=113&height=110&name=Alignment-field.png "Alignment field")

// alignment field { "name": "img\_position", "label": "Position Image", "help\_text":"Position the image within it's container.", "required": false, "type": "alignment", "default": { "horizontal\_align": "CENTER", "vertical\_align": "TOP", } }

Blog field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Object containing `horizontal_align` and `vertical_align`.

 |  |
| 

`alignment_direction`

 | String | 

Determines if only horizontal, only vertical, or both alignment controls should be shown. Can be:

*   `HORIZONTAL`
*   `VERTICAL`
*   `BOTH`

 | `BOTH` |

Background image[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#background-image)
----------------------------------------------------------------------------------------------------------------

This field provides a background image field which has subfields for background position and background size. Background image fields have a `.css` property that returns CSS based on the field's value. [Learn more about the generated CSS property.](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#generated-css)

Background Image fields are supported in [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules) and can only be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Background image field](https://developers.hubspot.com/hs-fs/hubfs/bg_field.png?width=349&height=246&name=bg_field.png "Background image field")

// background image field { "name": "bg\_image", "label": "Background image", "required": false, "type": "backgroundimage", "default": { "src": "https://example.com/img.png", "background\_position": "MIDDLE\_CENTER", "background\_size": "cover" } }

Blog field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Object containing the image src, background position and background size.

 | `null` |

Blog[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#blog)
----------------------------------------------------------------------------------------

This field provides a way for content editors to select a blog, providing you, the developer the blog's id. This is useful for situations like pulling teaser information for featured blogs in modules. You can use the blog id in blog-related [HubL functions](/docs/cms/hubl/functions) to get information like [blog authors](/docs/cms/hubl/functions#blog-authors), [recent blog posts](/docs/cms/hubl/functions#blog-recent-posts), [recent blog posts with a specific tag](/docs/cms/hubl/functions#blog-recent-tag-posts), and more.

Blog fields are supported in modules.

![Screenshot of Blog field](https://developers.hubspot.com/hubfs/Blog%20field.png "Screenshot of Blog field")

// blog field { "name" : "blog", "label" : "Blog", "required" : false, "locked" : false, "type" : "blog", "default" : 1234567890 }

Blog field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | "default" / blog id | 

Specifies which blog is selected by default. This parameter accepts arguments of either 'default' or a blog ID (available in the URL of the Blog dashboard).

 | `null` |

Boolean[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#boolean)
----------------------------------------------------------------------------------------------

This field provides a way for content editors to enable/disable functionality. Booleans can only be `true` or `false`. Often it makes sense to make groups or fields conditional based on boolean fields. If you think you might need to provide more than two states down the road, a Choice field may be a better option as you can grow into that with less effort should needs change later.

Boolean fields are supported in both themes and modules.  
Boolean fields can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Screenshot of Boolean field](https://developers.hubspot.com/hs-fs/hubfs/Boolean.png?width=209&height=45&name=Boolean.png "Screenshot of Boolean field")

// Boolean field { "name" : "is\_teaser\_img", "label" : "Enable Teaser Image", "required" : false, "locked" : false, "type" : "boolean", "display":"checkbox", "inline\_help\_text" : "Shows Teaser image when toggled on", "help\_text" : "Teaser images are used to help provide visual context to the post.", "default" : false }

Blog field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Boolean | 

Set's whether the default state of this field is `true` or `false`.

 | `false` |
| 

`display`

 | String | 

Choose the visual display style for the field. Can appear as either a `toggle` or a `checkbox`.

 | `checkbox` |

A toggle switch can make sense when the value of the field enables/disables other fields conditionally being shown. Another time a toggle may be useful is when the field represents a major design change for the module.

Checkboxes make sense for smaller changes that may not have as drastic of an effect on the module's display, such as hiding or showing individual small elements.

Border[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#border)
--------------------------------------------------------------------------------------------

This field provides content creators a user interface for creating a border around an element. Border fields have a `.css` property that returns CSS based on the field's value. [Learn more about the generated CSS property.](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#generated-css)

Border fields are supported in [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules).  
Border fields can only be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Screenshot of border module field in page editor](https://developers.hubspot.com/hs-fs/hubfs/border-module-field.png?quality=low&width=327&height=281&name=border-module-field.png "Screenshot of border module field in page editor")

// Border field { "id" : "styles.border", "name" : "border", "label" : "border", "required" : false, "locked" : false, "allow\_custom\_border\_sides" : false, "type" : "border", "default" : { "top": { "width": { "value": 1, "units": "px" }, "opacity": 100, "style": "solid", "color": "#ffffff" }, "bottom": { "width": { "value": 1, "units": "px" }, "opacity": 100, "style": "solid", "color": "#ffffff" }, "left": null, "right": null } }

Blog field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Boolean | 

object with keys for border radius, top, bottom, left, and right sides.

 | `{}` |

Choice[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#choice)
--------------------------------------------------------------------------------------------

Choice fields allow a content creator to select one or more items from a list of options. Using the `display` property, you can set display the options in a dropdown menu, radio select, or checkboxes, or a range of buttons. Learn more about [choice field display options below](#choice-button-presets).

Choice fields are supported in both themes and modules. Choice fields can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![choice-field-dropdown](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/choice-field-dropdown-4.jpg?width=766&height=522&name=choice-field-dropdown-4.jpg "choice-field-dropdown")

// Choice field { "name" : "img\_position", "label" : "Image Position", "required" : false, "locked" : false, "multiple":"true", "display" : "select", "choices" : \[ \[ "img--left", "Image Left - Text Right" \], \[ "img--right", "Text Left - Image Right" \] \], "type" : "choice", "default" : "img--left" }

Boolean field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`choices`

 | Array | 

Array containing the selectable options, formatted as unique internal value followed by label.

 | `[ [ "value 1", "Label 1" ], [ "value 2", "Label 2" ] ]` |
| 

`default`

 | Value | 

Sets the default selected value from the choice array.

 |  |
| 

`multiple`

 | Boolean | 

Optional field that enables multiple options to be selected when set to `true`.

Set `display` to `checkbox` or `select` to configure whether the field displays as a list of checkboxes or a dropdown menu.

 | `false` |
| 

`display`

 | String | 

Set the field's appearance using one of the following values:

*   `select`: renders a dropdown menu. Allows for selecting multiple options when `multiple` is set to `true`. 
*   `checkbox`: renders a list of selectable checkboxes. Allows for selecting multiple options when `multiple` is set to `true` and `reordering_enabled` is set to `false`.
*   `radio`: renders a list of radio button options. Does not allow for selecting multiple options.
*   `buttons`: renders a set of buttons based on the specified `preset`. Does not allow for selecting multiple options.

 | `"select"` |
| 

`reordering_enabled`

 | Boolean | 

When set to `true`, allows content creators to reorder the field's options in the editor. To enable this, `multiple` must also be set to `true`.



 | `false` |
| 

`preset`

 | String | 

Configures the button preset to use when `display` is set to `buttons`. For each preset, you'll need to configure the `choices` labels to match a specific set of values. Learn more about these [preset options](#choice-button-presets) below.

 |  |

### Choice button presets[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#choice-button-presets)

To configure a choice field to display buttons instead of a dropdown menu, checkboxes, or radio selects, you can use any of the presets below. Each preset allows for a specific set of option labels, which you'll need to include in the `choices` array. These labels cannot be customized.

// Layout choice button { "name" : "layout", "type" : "choice", "label" : "Layout", "required" : false, "locked" : false, "display" : "buttons", "preset" : "layout", "choices" : \[ \[ "cards\_value", "cards" \], \[ "tiles\_value", "tiles" \], \["minimal\_value", "minimal"\] \] }

| Preset | Choice labels | Example |
| --- | --- | --- |
| `expand_icon` | `caret` | `plus` | ![choice-button-presets_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/choice-button-presets_1.png?width=217&height=129&name=choice-button-presets_1.png)
 |
| `layout` | `cards` | `tiles` | `minimal` | ![choice-button-presets_6](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/choice-button-presets_6.png?width=374&height=156&name=choice-button-presets_6.png)

 |
| `icon_size` | `small` | `medium` | `large` | ![choice-button-presets_5](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/choice-button-presets_5.png?width=374&height=163&name=choice-button-presets_5.png)

 |
| `social_icon_size` | `small` | `medium` | `large` | ![choice-button-presets_4](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/choice-button-presets_4.png?width=374&height=166&name=choice-button-presets_4.png)

 |
| `icon_background_shape` | `none` | `square` | `rounded` | `circle` | ![choice-button-presets_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/choice-button-presets_3.png?width=374&height=291&name=choice-button-presets_3.png)

 |
| `social_icon_background_shape` | `none` | `square` | `rounded` | `circle` | ![choice-button-presets_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/choice-button-presets_2.png?width=371&height=291&name=choice-button-presets_2.png)

 |

Color[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#color)
------------------------------------------------------------------------------------------

Color fields provide a color picker interface for content creators. They support solid colors as well as transparency. They are a perfect choice for when you want to give content creators full control over colors within a module.

By default, the opacity input of a color field is hidden for email modules, as some email clients don't respect opacity rules. You can reveal the opacity field for email modules by setting `show_opacity` to `true`.

Color fields are supported in both themes and modules.Color fields can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields)

![Color field](https://developers.hubspot.com/hs-fs/hubfs/colorfield.png?width=800&height=446&name=colorfield.png "Color field")

// color field { "name" : "bg\_color", "label" : "Background color", "required" : false, "locked" : false, "type" : "color", "default" : { "color" : "#ff0000", "opacity" : 100 } }

Color field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Sets the default selected color and opacity.

 | `{ "color" : "#ffffff", "opacity" : 100 }` |
| 

`show_opacity`

 | Boolean | 

Sets whether opacity input is shown.

*   `true`: the opacity input is shown.
*   `false`: the opacity input is hidden.
*   If left undefined, opacity input will not display in email modules, but will display in other module types.

 | `undefined` |

CTA[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#cta)
--------------------------------------------------------------------------------------

Call-To-Action (CTA) fields provide a way for users to pick a CTA to display. CTA's are essentially trackable buttons or links. Content creators [create CTAs](https://knowledge.hubspot.com/ctas/create-calls-to-action-ctas) that can be used throughout a site. 

CTA fields are supported in modules.  
CTA fields are available in CMS Hub _Professional_ and _Enterprise_.

![Call To Action Field](https://developers.hubspot.com/hubfs/Screen%20Shot%202020-02-26%20at%2010.24.18%20PM.png "Call To Action Field")

// CTA field { "name" : "cta", "label" : "CTA", "required" : false, "locked" : false, "type" : "cta", "default" : null }

CTA field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

The default selected CTA. Expects a CTA id which can be found in the URL when editing a CTA in the [CTA manager](https://app.hubspot.com/l/ctas).

 | `null` |

CRM object[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#crm-object)
----------------------------------------------------------------------------------------------------

CRM object fields provide a way for users to pick an individual instance of a CRM object to display. 

`module.fieldname.properties` returns the properties fetched from this object instance. This makes it so you don't need to use the `crm_object()` function to get the data for the selected object instance.

`module.fieldname.id` returns the object instance id.

CRM object fields are supported in modules.  
CRM object fields are available in CMS Hub _Professional_ and _Enterprise_.

![CRM Object Field](https://developers.hubspot.com/hs-fs/hubfs/CRM%20Object%20Field.png?width=372&height=317&name=CRM%20Object%20Field.png "CRM Object Field")

// fields.json { "name" : "crmobject\_field", "label" : "CRM object", "required" : false, "locked" : false, "object\_type" : "CONTACT", "properties\_to\_fetch" : \[ \], "type" : "crmobject", "default" : { "id" : 1 } }

CRM object field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`object_type`

Required



 | String | 

Type of CRM Object the user can pick from. [Supported CRM Object Types](https://developers.hubspot.com/docs/cms/features/custom-objects#supported-crm-object-types)

 |  |
| 

`properties_to_fetch`

 | Array | 

Array of property names associated with the object type in string form. Ex: `"date_of_birth"` is a property associated with a contact. Use this to limit the information available to the page to just what you need.

 |  |
| 

`default`

 | Object | 

Object with id of default selected object instance. Contact ID, Company ID etc

 | `null` |

CRM object property[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#crm-object-property)
----------------------------------------------------------------------------------------------------------------------

Use the CRM object property field to access property metadata, such as the label and property name, from a specified object type. This enables content creators to select from object properties when needing to display property details on a page.

For example, you could add this field to a custom table module to populate table headings based on the selected properties.

CRM object fields are supported in modules. 

![crm-object-property-dropdown-menu0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/crm-object-property-dropdown-menu0.png?width=361&height=375&name=crm-object-property-dropdown-menu0.png "crm-object-property-dropdown-menu0")

// fields.json { "name" : "crmobjectproperty\_field", "label" : "CRM object property", "required" : true, "locked" : false, "object\_type" : "contact", "type" : "crmobjectproperty", "default" : { "property" : "field\_of\_study" } }

CRM object field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`object_type`

Required



 | String | 

Type of CRM Object the user can pick from. Learn more about [supported CRM object types](https://developers.hubspot.com/docs/cms/features/custom-objects#supported-crm-object-types).

 |  |
| 

`default`

 | Object | 

Contains the default property to display.

 |  |

In addition, you can use the following snippets to return other property details:  

*   `{{ module.fieldname.property }}`: returns the property's internal name.
*   `{{ module.fieldname.property_definition.label }}`: returns the property's label.
*   `{{ module.fieldname.property_definition.type }}`: returns the property type (e.g., string).

Date[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#date)
----------------------------------------------------------------------------------------

Date fields provide a date picker interface to make it easy for content creators to select a date. Returns a timestamp you can use in your code.

Date fields are supported in modules.

![Date field with calendar picker open](https://developers.hubspot.com/hs-fs/hubfs/date%20field.png?width=376&height=442&name=date%20field.png "Date field with calendar picker open")

// Date field { "name" : "event\_start\_date", "label" : "Event Date", "required" : false, "locked" : false, "type" : "date", "default" : 1577854800000 }

Date field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Timestamp | 

The Unix Epoch timestamp for the date and time you want to default to. Leave this null to allow the date and time picker to start the content creator at the current date and time in the picker.

 | `null` |

Date and time[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#date-and-time)
----------------------------------------------------------------------------------------------------------

Date and time fields provide a date picker interface just like the date field, as well as a time picker to make it easy for content creators to select a date and time of day. Returns a timestamp you can use in your code.

Date and time fields are supported in modules.

![Event Start](https://developers.hubspot.com/hs-fs/hubfs/Event%20Start.png?width=376&height=390&name=Event%20Start.png "Event Start")

// Date and time field { "name" : "event\_start", "label" : "Event Start", "required" : false, "locked" : false, "type" : "datetime", "default" : 1577854800000 }

Date and time field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Timestamp | 

The Unix Epoch timestamp for the date and time you want to default to. Leave this null to allow the date and time picker to start the content creator at the current date and time in the picker.

 | `null` |

Email Address[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#email-address)
----------------------------------------------------------------------------------------------------------

Email address fields allow a user to select multiple email addresses. This could be used for displaying contact information. The email field returns an array of selected email addresses you can loop through.

Email fields are supported in modules.

![email-field](https://developers.hubspot.com/hubfs/email-field.png "email-field")

// Email address field { "name" : "emails", "label" : "Email address", "required" : false, "locked" : false, "type" : "email", "default" : null }

Email address field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Array | 

Array of email address strings `["bob@example.com", "dennis@example.com"]`

 | `null` |

Embed[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#embed)
------------------------------------------------------------------------------------------

Embed fields allow the user to add a URL from an [oEmbed-enabled site](https://oembed.com/#section7) or paste in an embed code from another site. To learn more about oEmbed usage on HubSpot, and see use cases, visit our [oEmbed document](/docs/cms/building-blocks/module-theme-fields/oembed).

![Embed field ](https://developers.hubspot.com/hs-fs/hubfs/Developer%20Site/assets/images/module-theme-fields/embed-field.jpg?width=756&height=482&name=embed-field.jpg "Embed field ")

// embed field { "name" : "embed\_field", "label" : "Embed", "required" : false, "locked" : false, "supported\_source\_types" : \[ "oembed", "html" \], "supported\_oembed\_types" : \[ "photo", "video", "link", "rich" \], "type" : "embed", "default" : { "source\_type" : "oembed" } }

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`supported_source_types`

 | Array | 

Supported source types for either oEmbed URLs (`oembed`), HTML embed code (`html`), or Media Bridge (`media_bridge`).

 | `["oembed", "html"]` |
| 

`supported_oembed_types`

 | Array | 

Supported oEmbed type including `"photo"`, `"video"`, `"link"`, and `"rich"`. Does not apply to the supported\_source\_types of html

 | `[ "photo", "video", "link", "rich" ]` |
| 

`supported_media_bridge_providers`

 | Array | 

Array of provider IDs that determine which Media Bridge providers are available to select content from.

Note: This param will also be populated when installing a [Media Bridge Provider Application](https://ecosystem.hubspot.com/marketplace/apps/apps-for-media). 

 |  |
| 

`type`

 | String | 

This parameter is always set to `"embed"`

 | `"embed"` |
| 

`default`

 | Dict | 

An array containing the `"source_type"` parameter. This parameter has one string based value from the options provided in the `"supported_source_types"` parameter.

 | `oembed` |

File[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#file)
----------------------------------------------------------------------------------------

File fields allow the user to upload a file to the file manager, or document manager, and make it easy to attach items that are in those locations. This can be useful for linking out to PDF files or files of other formats. For displaying images on a page you should use the image field.

File fields are supported in modules.

![File field](https://developers.hubspot.com/hs-fs/hubfs/File%20field.png?width=376&height=263&name=File%20field.png "File field")

// Email address field { "name" : "file\_field", "label" : "File", "required" : false, "locked" : false, "type" : "file", "picker" : "file", "default" : null }

File field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

File URL.

 | `null` |
| 

`picker`

 | String | 

Acceptable values: "file", "document", "image".  
The picker shows assets uploaded to either the file manager, or the document manager depending on this parameter.

 | `file` |

Followup email[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#followup-email)
------------------------------------------------------------------------------------------------------------

Followup email fields allow a content creator to designate an email that will be sent in response to a form submission. This works in tandem with the [HubL form tag](/docs/cms/hubl/tags#form), through the `simple_email_campaign_id` parameter.

Followup email fields are supported in modules.

![followup email field](https://developers.hubspot.com/hs-fs/hubfs/followup%20email%20field.png?width=377&height=131&name=followup%20email%20field.png "followup email field")

// Followup email field { "name" : "followup\_email", "label" : "Followup email", "required" : false, "locked" : false, "type" : "followupemail", "default" : null }

Email address field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

Email id

 | `null` |

Font[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#font)
----------------------------------------------------------------------------------------

Font fields provide content creators basic font styling controls. Content creators can choose the size, color, font family, and the format (bold, italic, and underlined). The listed fonts are all standard web-safe fonts. These fonts are sourced from [Google Fonts](https://fonts.google.com/) but served by HubSpot directly on the  domain that the page loads on.

Font fields are supported in both themes and modules. Font fields can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Font field](https://developers.hubspot.com/hubfs/font%20field.png "Font field")

**Please note:**

*   Font family is determined by the combination of the `font` and `font_set` properties. You must include both to load the font. When [inheriting fields](/docs/cms/building-blocks/module-theme-fields-overview#inherited-fields), this means you need to inherit both values.
*   Hiding CSS-related sub fields with `visibility` will not prevent that CSS from being output in the styling returned in the field object. You'll still need to manually include the CSS in the `styles` object.

// Font field { "name" : "font", "label" : "Font", "required" : false, "locked" : false, "load\_external\_fonts" : true, "type" : "font", "default" : { "size" : 12, "font":"Merriweather", "font\_set":"GOOGLE", "size\_unit" : "px", "color" : "#000", "styles" : { } }, "visibility" : { "hidden\_subfields" : { "font": true, "size": true } } }

Font field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Font object with settings for size, sizing unit, color, and styles for bold, italic, and underline.

 | `{ "size" : 12, "size_unit" : "px", "color" : "#000", "styles" : { } }` |
| 

`load_external_fonts`

 | Boolean | 

HubSpot automatically loads the selected web font to the page if the font is selected and referenced by HubL in a stylesheet or in a module. Set this to false, if you are already loading the font to the page, that way the font won't load twice.

 | `true` |
| 

`visibility`

 | Object | 

Using the `hidden_subfields` nested object, you can set a boolean for which controls of the Font field to hide. Subfields include: `font`, `size`, `bold`, `italic`, `underline`, and `color`.

 |  |
| 

`variant`

 | String | 

If using a web font, the variant of the font you want to use. For example, to use the 700-weight version of a font, set this to `"700"`. To use the 400-weight italic version of a font, set this to `"400i"`.

 |  |

Form[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#form)
----------------------------------------------------------------------------------------

Form fields allow a content creator to designate a form in their account. You can then use this to render a form to a page using the [HubL form tag](/docs/cms/hubl/tags#form). 

Form fields are supported in modules.

![form field-Aug-21-2020-08-09-55-35-PM](https://developers.hubspot.com/hubfs/form%20field-Aug-21-2020-08-09-55-35-PM.png "form field-Aug-21-2020-08-09-55-35-PM")

// Form field { "id" : "idNumber", "name" : "form\_field\_name", "display\_width" : null, "label" : "Form", "required" : false, "locked" : false, "type" : "form", "disable\_inline\_form\_editing": true, "required\_property\_types": \["TICKET"\], "default" : { "response\_type" : "inline", "message" : "Thanks for submitting the form." } }

Email address field
| Parameter | Type | Description |
| --- | --- | --- |
| 
`default`

 | Object | 

An object containing the form submission response details. Includes the following parameters:

*   `response_type`, which can be one of:
    *   `inline:` an inline text message. 
    *   `redirect`: redirect the visitor after submission.
*   `message`: the text to display after form submit.

*   `redirect_id`: for redirected forms, set to a HubSpot content ID to redirect submitters to a HubSpot page.
*   `redirect_url`: for redirected forms, set to a specific URL to redirect submitters to a page.

 |
| 

`disable_inline_form_editing`

 | String | 

Set the `disable_inline_form_editing` property to `true` to hide all inline form editing controls in the form module. This includes the form fields, submit button text, data privacy and consent options, and CAPTCHA.

 |
| 

`required_property_types`

 | Array | 

An array that specifies which forms can be selected based on the property types of the form fields. Values include: `"CONTACT"`, `"COMPANY"`, and `"TICKET"`).

 |

Gradient[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#gradient)
------------------------------------------------------------------------------------------------

This field provides a way for content creators to create and configure gradients. At this time linear gradients support up to 5 color stops. Gradient fields have a `.css` property that returns CSS based on the field's value. [Learn more about the generated CSS property.](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#generated-css)

Gradient fields are supported in [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules). Gradient fields can only be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Gradient Field](https://developers.hubspot.com/hs-fs/hubfs/gradient_field.png?quality=low&width=349&height=310&name=gradient_field.png "Gradient Field")

// Gradient field { "name": "bg\_gradient", "label": "Background gradient", "help\_text": "Sets a gradient behind the content", "required": false, "type": "gradient", "default": { "colors": \[{ "color": { "r": 0, "g": 0, "b": 0, "a": 1 } }, { "color": { "r": 255, "g": 255, "b": 255, "a": 1 } }\], "side\_or\_corner": { "verticalSide": "BOTTOM", "horizontalSide": null } } }

Email address field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Object containing directional settings for a gradient ("side\_or\_corner") and color stops for the gradient as an array of objects.

 |  |

HubDB Row[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#hubdb-row)
--------------------------------------------------------------------------------------------------

HubDB Row fields allow a content creator to select an individual row (or rows if using repeater fields) from a defined table. You can then use this field to create user-defined lists, tables, resources, and more.

HubDB Row fields are supported in modules.  
HubDB Row fields are available in CMS Hub _Professional_ and _Enterprise_.

![hubdb-row-field](https://developers.hubspot.com/hubfs/Developer%20Site/assets/images/module-theme-fields/hubdb-row-field.png "hubdb-row-field")

// HubDB Row field { "name" : "hubdbrow\_field", "label" : "HubDB row", "required" : false, "locked" : false, "table\_name\_or\_id" : "3096859", "columns\_to\_fetch" : \[ "name", "price", "desc" \], "display\_columns" : \[ "name", "price", "desc" \], "display\_format" : "%0 - %1 :::: %2", "type" : "hubdbrow", "default" : { "id" : 4450468943 } }

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`table_name_or_id`

 | String | 

The name or ID of the HubDB table. This field is required.

 |  |
| 

`columns_to_fetch`

 | Array | 

An array of column names to fetch from the table. If left blank, will return all columns in the table.

 | `[]` |
| 

`display_columns`

 | Array | 

An array of column names to use in choice label. If left blank, will return only the first column in the table.

 | `[]` |
| 

`display_format`

 | String | 

The format you would like the column data to display in the HubDB row selector using the percent symbol and number to designate a column.  
**Ex:** _%0 (%1) would appear as Column0Value (Column1Value)_

 | `""` |
| 

`default`

 | Object | 

Object containing “id” for setting the default hubdb row.

 | `{ “id” : null }` |

HubDB Table[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#hubdb-table)
------------------------------------------------------------------------------------------------------

HubDB Table fields allow a content creator to designate a HubDB  in their account. You can then use this to render a form to a page using the [HubL form tag](/docs/cms/hubl/tags#form). Returns the table id, which you can use with the [HubDB HubL functions](/docs/cms/features/hubdb#access-hubdb-data-using-hubl).

HubDB Table fields are supported in modules. HubDB Table fields are available in **CMS Hub**_Professional_ and _Enterprise_.

![HubDB field](https://developers.hubspot.com/hubfs/HubDB%20field.png "HubDB field")

// HubDB Table field { "name" : "recipe\_table", "label" : "Recipe Table", "required" : false, "locked" : false, "type" : "hubdbtable", "default" : 2010782 }

Email address field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

HubDB table id

 | `null` |

Icon[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#icon)
----------------------------------------------------------------------------------------

Icon fields provide an icon picker UI to make it easier for content creators to add icons to your modules. The Icon field is preloaded with FontAwesome Icons.

Icon fields are supported in modules. Icon fields can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![icon field](https://developers.hubspot.com/hubfs/icon%20field.png "icon field")

// Icon field { "name" : "icon\_field", "label" : "Icon", "required" : false, "locked" : false, "icon\_set" : "fontawesome-6.4.2", "type" : "icon", "default" : { "name" : "accessible-icon", "unicode" : "f368", "type" : "REGULAR" } }

Icon field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Icon object

 |  |
| 

`icon_set`

 | String | 

The FontAwesome icon set to use. Possible values are:

*   `fontawesome-6.4.2`
*   `fontawesome-5.14.0`
*   `fontawesome-5.0.10`

 | `fontawesome-5.0.10` |

Image [](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#image-nbsp-)
-------------------------------------------------------------------------------------------------

Image fields provide an easy interface for content creators to add images to a module or theme. Image fields provide a file picker interface that lists images from the File Manager. Since images can be used and displayed in different ways, developers can limit the sizing options available to the content creator in the UI as well as allow for [lazy-loading of images](/docs/cms/guides/speed/lazy-loading).

![Image Field](https://developers.hubspot.com/hubfs/Image%20Field.png "Image Field")

Image fields are supported in modules.  
Images can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields). You should only use Image fields as style fields, if the image will be purely presentational, not convey meaning and not a [background image](#background-image). This is to follow best practices for [accessibility](https://developers.hubspot.com/docs/cms/guides/accessibility).

// Image field { "name" : "image\_field", "label" : "Image", "required" : false, "locked" : false, "responsive" : true, "resizable" : true, "show\_loading" : false, "type" : "image", "default" : { "size\_type" : "exact", "src" : "", "alt" : "image-alt-text", "loading" : "lazy", "width" : 128, "height" : 128, "max\_width" : 128, "max\_height" : 128 } }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Sets properties for image sizing, alt-text, and more. Can contain the following properties: 

*   `size_type`: whether the image is automatically or manually sized:
    *   `"auto"`: HubSpot will automatically adjust the size of the image based on its original dimensions.
    *   `"auto_custom_max"`: HubSpot will automatically adjust the size of the image with maximum dimensions set using the `"max_height"` and `"max_width"` properties.
    *   `"exact":` HubSpot will size the image based on the dimensions set using the `"height"` and `"width"` properties.
*   `src`: the URL of the default image. Must be an absolute path to an image.
*   `alt`: the image's default alt-text.
*   `loading`: the image's [lazy loading options](/docs/cms/guides/speed/lazy-loading). Can be set as `"disabled"` (default), `"eager"`, or `"lazy"`.

 | `{ "size_type" : "auto", "src" : "", "alt" : null, "loading": "disabled" }` |
| 

`responsive`

 | Boolean | 

determines if the image is to act responsively or have a fixed height and width.

 | `true` |
| 

`show_loading`

 | Boolean | 

Determines if the controls for choosing to [lazy load](/docs/cms/guides/speed/lazy-loading) the image are shown in the page editor.

 | `false` |

Link[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#link)
----------------------------------------------------------------------------------------

Link fields provide an easy interface for content creators to provide links to URLs and email addresses. For external links, content creators choose "external". For email links "email address". Finally for content hosted on the HubSpot CMS they can use "content" which shows a list of all pages and blog posts in the account, file showing file assets, and blog, showing all of the blog listings in the account. Link fields are very similar to URL fields except for the key difference that they provide a UI for "open in new window" and "tell search engines not to follow". If you do not want content creators to have that control use the [URL field](#url).

Link fields are supported in modules.

![link field](https://developers.hubspot.com/hubfs/link%20field.png "link field")

// Link field { "name" : "link\_field", "display\_width" : null, "label" : "Link", "required" : false, "locked" : false, "supported\_types" : \[ "EXTERNAL", "CONTENT", "FILE", "EMAIL\_ADDRESS", "BLOG", "CALL\_TO\_ACTION", "PHONE\_NUMBER", "WHATSAPP\_NUMBER", "PAYMENT" \], "show\_advanced\_rel\_options" : true, "type" : "link", "default" : { "url" : { "content\_id" : null, "type" : "EXTERNAL", "href" : "" }, "open\_in\_new\_tab" : false, "no\_follow" : false } }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

The default URL and link open behavior. This object includes:

*   A `url` object which contains:
    *   `content_id`: if linking to HubSpot content, the ID of that content. Set to `null` if linking to external content.
    *   `type`: the type of URL. Learn more about supported types below.
    *   `href`: the URL of the content. When linking to HubSpot content, set this to `null` and use `content_id` instead.

 | `{ "url" : { "content_id" : null, "type" : "EXTERNAL", "href" : "" }, "open_in_new_tab" : false, "no_follow" : false, "sponsored" : false, "user_generated_content" : false }` |
| 

`supported_types`

 | Array | 

The types of links that content creators can select. Remove types from the list that you don't want content creators to have access to set. Valid types include:

*   `EXTERNAL`
*   `CONTENT`
*   `FILE`
*   `EMAIL_ADDRESS`
*   `BLOG`
*   `CALL_TO_ACTION`
*   `PHONE_NUMBER`
*   `WHATSAPP_NUMBER`
*   `PAYMENT`



 | `[ "EXTERNAL", "CONTENT", "FILE", "EMAIL_ADDRESS", "BLOG", "CALL_TO_ACTION", "PHONE_NUMBER", "WHATSAPP_NUMBER", "PAYMENT" ]` |
| 

`show_advanced_rel_options`

 | Boolean | 

By default, content creators will only be able to select the `no_follow` option.

When set to `true`, content creators can also select:

*   `sponsored`: a sponsored link, such as a paid ad link. 
*   `user_generated_content`: content generated by users, such as forums.

Learn more about [link attributes](https://moz.com/blog/nofollow-sponsored-ugc).

 | `false` |

Logo[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#logo)
----------------------------------------------------------------------------------------

Logo fields provide a way for content creators to specify logo images to use in a page, defaulting to the domain's logo. This is useful for site headers and footers that may contain the company logo. Logo fields also allow for [lazy loading](/docs/cms/guides/speed/lazy-loading).

Logo fields are supported in modules.

![logo field](https://developers.hubspot.com/hs-fs/hubfs/logo%20field.png?width=377&name=logo%20field.png "logo field")

// Logo field { "name" : "logo", "label" : "Logo", "required" : false, "locked" : false, "type" : "logo", "show\_loading": true, "default" : { "override\_inherited\_src" : false, "src" : null, "alt" : null, "loading": "lazy" } }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`show_loading`

 | String | 

Determines if the controls for choosing to [lazy load](https://developers.hubspot.com/docs/cms/guides/speed/lazy-loading) the image are shown in the page editor.

 | `false` |
| 

`default`

 | Object | 

Logo object. 

If `show_loading` is set to `true`, you can include a `loading` property to set the image's [lazy loading options](https://developers.hubspot.com/docs/cms/guides/speed/lazy-loading). Options include:

*   `"disabled"` (default)
*   `"eager"`
*   `"lazy"`

 | `{ override_inherited_src: false, src: "", alt: null, width: null, height: null, loading: "disabled" suppress_company_name: false }` |

Menu[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#menu)
----------------------------------------------------------------------------------------

Menu fields provide an easy interface for content creators to create, edit and select a [navigation menu](/docs/cms/building-blocks/menus-and-navigation) that is re-usable on other pages. This field is great for use in menus that are used across multiple pages like main navigation and footer navigation and other [global content](/docs/cms/building-blocks/global-content).  Use this field in tandem with the [menu tag](/docs/cms/hubl/tags#menu) or [menu() function](/docs/cms/hubl/functions#menu), to render a menu inside of your module.  
  
For menus that don't make sense to re-use on other pages, like a table of contents menu, use the [simple menu field](#simple-menu).

Menu fields are supported in modules.

![menu field](https://developers.hubspot.com/hubfs/menu%20field.png "menu field")

// Menu field { "name" : "menu", "label" : "Menu", "required" : false, "locked" : false, "type" : "menu", "default" : 12345678911 }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Integer | 

The [menu ID](/docs/cms/building-blocks/menus-and-navigation#get-your-menu-id) for the menu. The default value of `null`, defaults to the default menu under navigation.

 | `null` |

Number[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#number)
--------------------------------------------------------------------------------------------

Number fields provide an easy interface for content creators to enter in or adjust numerical values and options. This can be used for creating percentage based items or anything where numbers are needed for input.

Number fields are supported in modules. Number fields can be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Number field](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/number-field-example-4.jpg?width=774&name=number-field-example-4.jpg "Number field")

// Number field { "name" : "number\_field", "label" : "Number", "required" : false, "locked" : false, "display" : "slider", "min" : 1, "max" : 10, "step" : 1, "type" : "number", "prefix": "", "suffix" : "", "default" : null, "placeholder": "50" }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Number | 

A default number to be used.

 | `null` |
| 

`prefix`

 | String | 

Added as a prefix to the number field.

 |  |
| 

`suffix`

 | String | 

Added as a suffix to the number field.

 |  |
| 

`placeholder`

 | String | 

Adds a placeholder value to the field.

 |  |

Suffix and prefix parameters are for display purposes in the content editor and have no effect on the numerical value of the field. 

Page[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#page)
----------------------------------------------------------------------------------------

Page fields provide an interface for content creators to select site pages and landing pages.

The value returned by a page field is the page id of the selected page. When used in tandem with the [content\_by\_id](/docs/cms/hubl/functions#content-by-id) or [content\_by\_ids](/docs/cms/hubl/functions#content-by-ids) functions, you can use data from the selected pages in the current page.

Page fields are supported in modules.

![Page field](https://developers.hubspot.com/hubfs/Page%20field.png "Page field")

// Page field { "name" : "page\_field", "label" : "Page", "help\_text" : "Pulls data from the selected page.", "required" : false, "locked" : false, "placeholder" : "Page to pull from", "type" : "page", "default" : null }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Integer | 

A default page id to be selected.

 | `null` |

Rich text[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#rich-text)
--------------------------------------------------------------------------------------------------

Rich Text fields provide content creators with a WYSIWYG text editor experience. When a rich text field's value is printed it is printed as HTML. When you do not want content creators to have formatting capabilities use [text fields](#text).

Rich text fields are supported in modules.

![Rich Text field](https://developers.hubspot.com/hs-fs/hubfs/Rich%20Text%20field.png?width=377&height=358&name=Rich%20Text%20field.png "Rich Text field")

// Rich text field { "name" : "description", "label" : "Description", "required" : false, "locked" : false, "type" : "richtext", "default" : null }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

string of content to be displayed supports HTML. 

Note: You cannot use the `get_asset_url` [function](/docs/cms/hubl/functions#get-asset-url) within this default property. 

 | `""` |
| 

`enabled_features`

Optional



 | Array | 

An array of items that allows you to [configure the Rich Text Editor Toolbar](/docs/cms/building-blocks/module-theme-fields/rich-text-editor) and what options are available for content editors. 

 |  |

Simple menu[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#simple-menu)
------------------------------------------------------------------------------------------------------

Simple menu fields provide an easy interface for content creators to create a [navigation menu](/docs/cms/building-blocks/menus-and-navigation) that is not re-usable on other pages. For menus that should be reusable, use the [menu field](#menu). A time you may want this is for a table of contents menu that links to headings on very long pages, or a list of links to content that only makes sense to have on the current page.

Simple menu fields are supported in modules.

![Simple menu field](https://developers.hubspot.com/hs-fs/hubfs/Screen%20Shot%202020-02-28%20at%207.33.17%20AM.png?width=179&height=90&name=Screen%20Shot%202020-02-28%20at%207.33.17%20AM.png "Simple menu field")

// Simple menu field { "name" : "toc\_menu", "label" : "Table of Contents", "required" : false, "locked" : false, "type" : "simplemenu", "default" : \[ { "isPublished" : false, "pageLinkId" : null, "pageLinkName" : null, "isDeleted" : null, "categoryId" : null, "subCategory" : null, "contentType" : null, "state" : null, "linkLabel" : "Why is product marketing important?", "linkUrl" : null, "linkParams" : null, "linkTarget" : null, "type" : "NO\_LINK", "children" : \[ { "isPublished" : false, "pageLinkId" : null, "pageLinkName" : null, "isDeleted" : null, "categoryId" : null, "subCategory" : null, "contentType" : null, "state" : null, "linkLabel" : "Product Marketing Responsibilities", "linkUrl" : "#product-marketing-responsibilities", "linkParams" : null, "linkTarget" : null, "type" : "URL\_LINK", "children" : \[ \] }, { "isPublished" : false, "pageLinkId" : null, "pageLinkName" : null, "isDeleted" : null, "categoryId" : null, "subCategory" : null, "contentType" : null, "state" : null, "linkLabel" : "1. Identify the buyer personas and target audience for your product.", "linkUrl" : "#step1", "linkParams" : null, "linkTarget" : null, "type" : "URL\_LINK", "children" : \[ \] }, { "isPublished" : false, "pageLinkId" : null, "pageLinkName" : null, "isDeleted" : null, "categoryId" : null, "subCategory" : null, "contentType" : null, "state" : null, "linkLabel" : "2. Successfully create, manage and carry out your product marketing strategy.", "linkUrl" : "#step2", "linkParams" : null, "linkTarget" : null, "type" : "URL\_LINK", "children" : \[ \] } \] }, { "isPublished" : false, "pageLinkId" : null, "pageLinkName" : null, "isDeleted" : null, "categoryId" : null, "subCategory" : null, "contentType" : null, "state" : null, "linkLabel" : "How HubSpot can help", "linkUrl" : "https://hubspot.com", "linkParams" : null, "linkTarget" : null, "type" : "URL\_LINK", "children" : \[ \] } \] }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Array of objects | 

JSON structure for menu and menu children.

 | `[]` |

Spacing[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#spacing)
----------------------------------------------------------------------------------------------

This field provides a user interface (UI) for content creators to set padding and margin. Spacing fields have a `.css` property that returns CSS based on the field's value. [Learn more about the generated CSS property.](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#generated-css)

Spacing fields are supported in [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules).  
Spacing fields can only be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![screenshot of spacing style field expanded in page editor](https://developers.hubspot.com/hs-fs/hubfs/spacing%20style%20field%20expanded.png?quality=low&width=321&height=361&name=spacing%20style%20field%20expanded.png "screenshot of spacing style field expanded in page editor")

// Spacing field { "name": "img\_spacing", "label": "Spacing around image", "required": false, "type": "spacing", "limits": { "padding": { "top": { "max": 50, "min": 25, "units": \["px", "pt", "em"\] }, "left": { "max": 50, "units": \["px", "pt", "em"\] }, "bottom": { "max": 50, "units": \["px", "pt", "em"\] } }, "margin": { "top": { "max": 50, "min": 25, "units": \["px", "pt", "em"\] }, "bottom": { "max": 25, "units": \["Q", "rem", "em"\] } } }, "default": { "padding": { "top": { "value": 25, "units": \["px", "pt", "em"\] }, "bottom": { "value": 25 "units": \["px", "pt", "em"\] }, "left": { "value": 25, "units": \["px", "pt", "em"\]}, "right": { "value": 25, "units": \["px", "pt", "em"\] } }, "margin": { "top": { "value": 20, "units": \["px", "pt", "em"\] }, "bottom": { "value": 20, "units": \["px", "pt", "em"\] } } } }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Sets the default spacing values.

Contains `padding` and `margin` objects:

*   `padding`: can contain `top`, `right`, `bottom`, `left` objects
*   `margin`: can contain `top` and `bottom` objects

Use `units` to set the units that a content creator can use in HubSpot. Learn more about units below.

 | `{}` |
| 

`limits`

 | Object | 

Sets the guidelines for `min` and `max` amount of spacing. 

Contains `padding` and `margin` objects:

*   `padding`: can contain `top`, `right`, `bottom`, `left` objects
*   `margin`: can contain `top` and `bottom` objects

Use `units` to set the units that a content creator can use in HubSpot. Learn more about units below.

 |  |

When using the spacing field, please note the following:

*   You must include a `units` list when setting a `min` or `max`. 
*   The `units` property supports the following unit types: `%`, `ch`, `em`, `ex`, `in`, `lh`, `pc`, `pt`, `px`, `Q`, `rem`, `vh`, `vmax`, `vmin`, and `vw`.  
    
*   When a content creator edits all padding together, HubSpot will use the highest `min` value and the lowest `max` value. In addition, only the units shared by all sides will be available to the content creator.

Tag[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#tag)
--------------------------------------------------------------------------------------

Tag fields provide  a blog tag picker for content creators. This tag picker returns a blog tag id which can then be used in blog tag related functions such as [Blog Tag URL](/docs/cms/hubl/functions#blog-tag-url) and [Blog Recent Tag Posts](/docs/cms/hubl/functions#blog-recent-tag-posts).

Tag fields are supported in modules.

![tag field](https://developers.hubspot.com/hs-fs/hubfs/tag%20field.png?width=377&name=tag%20field.png "tag field")

// Tag field { "id" : "c3395cd3-8e60-7e47-2f1b-b7ccf4d669c9", "name" : "blog\_tag", "label" : "Blog Tag", "required" : false, "locked" : false, "tag\_value" : "SLUG", "type" : "tag", "default" : null }

Tag field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

Blog tag id

 | `null` |

Text[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#text)
----------------------------------------------------------------------------------------

Text fields provide content creators a simple text editing experience with no rich text functionality. Text fields initially show as a single line, but can actually expand to be textareas, supporting multiple lines. Use these when you do not want content creators to have control over formatting. If you do want to provide formatting controls use [rich text fields](#rich-text).

Text fields are supported in modules.

![text field](https://developers.hubspot.com/hs-fs/hubfs/text%20field.png?width=377&height=98&name=text%20field.png "text field")

// Text field { "name" : "product\_name", "label" : "Product Name", "required" : false, "locked" : false, "validation\_regex" : "", "allow\_new\_line" : false, "show\_emoji\_picker" : false, "type" : "text", "default" : "" }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | String | 

Text string.

 | `""` |

Text Alignment[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#text-alignment)
------------------------------------------------------------------------------------------------------------

This field provides content creators a way to align text content within a container. This should not be used for aligning other assets as there is a [field type specifically for that](#alignment).

Text alignment fields are supported in [modules](https://developers.hubspot.com/docs/cms/building-blocks/modules). Text alignment fields can only be used as [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields).

![Text Alignment field](https://developers.hubspot.com/hs-fs/hubfs/Text%20Alignment%20field.png?width=144&height=74&name=Text%20Alignment%20field.png "Text Alignment field")

// text alignment field { "name": "heading\_align", "label": "Heading alignment", "required": false, "type": "textalignment", "default": { "text\_align": "LEFT" } }

Blog field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Object containing `horizontal_align` and `vertical_align`.

 |  |
| 

`alignment_direction`

 | String | 

Determines if only horizontal, only vertical, or both alignment controls should be shown. Can be:

*   `HORIZONTAL`
*   `VERTICAL`
*   `BOTH`

 | `BOTH` |

URL[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#url)
--------------------------------------------------------------------------------------

URL fields provide a similar experience to link fields. Providing a UI for content creators to add links. URL fields, however, do not show a UI for open in a new window, nor tell search engines not to follow. Use this field when you as a developer want to dictate the values for that. If you want the user to have control, use [link fields](#link) instead.

URL fields are supported in modules.

![URL field](https://developers.hubspot.com/hs-fs/hubfs/URL%20field.png?width=377&name=URL%20field.png "URL field")

// URL field { "name" : "url", "label" : "URL", "required" : false, "locked" : false, "supported\_types" : \[ "EXTERNAL", "CONTENT", "FILE", "EMAIL\_ADDRESS", "BLOG", "PHONE\_NUMBER", "WHATSAPP\_NUMBER" \], "type" : "url", "default" : { "content\_id" : null, "href" : "http://example.com", "type" : "EXTERNAL" } }

Link field
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

URL object, with type, href and content id (if content is a page or post on HubSpot)

 | `{ "content_id" : null, "href" : "", "type" : "EXTERNAL" }` |
| 

`supported_types`

 | Array | 

list of the types of links this field allows content creators to select. Remove types from the list that you don't want content creators to have access to set. Types include:

*   `EXTERNAL`: renders a text input field for an external URL.
*   `CONTENT`: renders a dropdown menu containing the account's website and landing pages.
*   `FILE`: renders a file selector.
*   `EMAIL_ADDRESS`: renders a text input field for an email address.
*   `BLOG`: renders a dropdown menu containing the account's blog listing pages.
*   `PHONE_NUMBER`: renders a text input field for a phone number. The number must start with `+` and contain 7-15 digits (excluding the country code).
*   `WHATSAPP_NUMBER`: renders a dropdown menu containing the account's [connected WhatsApp numbers](https://knowledge.hubspot.com/inbox/connect-whatsapp-to-the-conversations-inbox).

 | `[ "EXTERNAL", "CONTENT", "FILE", "EMAIL_ADDRESS", "BLOG" ]` |

Video[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#video)
------------------------------------------------------------------------------------------

Video fields provide content editors with a place to add HubSpot Video to their module content without the need of using rich text fields.

![Video Field](https://developers.hubspot.com/hs-fs/hubfs/Developer%20Site/assets/images/module-theme-fields/video-field.png?width=377&height=315&name=video-field.png "Video Field")

//Video field { "id" : "ca4a319e-5b58-422e-47ac-49ce1b51b507", "name" : "videoplayer\_field", "label" : "Video", "required" : false, "locked" : false, "type" : "videoplayer", "show\_advanced\_options" : false, "default" : { "player\_id" : 32173842991, "height" : 1224, "width" : 1872, "conversion\_asset" : { "type" : "CTA", "id" : "c3e4fa03-2c69-461d-b9af-22b2fde86bc7", "position" : "POST" }, "loop\_video" : false, "mute\_by\_default" : false, "autoplay" : false, "hide\_control" : false } }

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`default`

 | Object | 

Video object with settings for `player_id`, `height`, `width`, `size_type`, `conversion_asset`, `loop_video`, `mute_by_default`, `autoplay`, and `hide_control`.

 | `[]` |
| 

`show_advanced_options`

 | Boolean | 

Whether content creators can see advanced default options.

 | `false` |

### conversion\_asset object parameters[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#conversion-asset-object-parameters)

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`type`

 | String | 

Accepts either `"FORM"`, `"CTA"`, or `""`

 | `""` |
| 

`id`

 | String | 

The id of the Form or CTA type

 | `""` |
| 

`position`

 | String | 

Whether the conversion asset should be shown before the video starts or after it ends. Accepts either "PRE" or "POST".

 | `""` |

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#page-feedback)
----------------------------------------------------------------------------------------------------------------

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