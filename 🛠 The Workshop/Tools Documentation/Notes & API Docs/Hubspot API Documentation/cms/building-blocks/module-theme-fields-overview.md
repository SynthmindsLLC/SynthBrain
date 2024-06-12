---
title: "Module and theme fields overview"
description: "Within modules and themes, fields are used to enable content creators to control module and theme styling and functionality on your website. When developing a module or a theme, you'll include fields in a `fields.json` file, which will then translate to the theme and content editors. To learn more about specific field types, check out the [module and field types reference guide](/docs/cms/building-blocks/module-theme-fields)."
type: "concept"
tags:
- "Modules"
- "Themes"
- "Fields"
relationships:
- "#related_to [[Module]]"
- "#related_to [[Theme]]"
- "#used_for [[Content Creation]]"
last_updated: "2023-06-27"
---

Module and theme fields overview


====================================

Last updated: June 27, 2023

Within [modules](/docs/cms/building-blocks/modules) and [themes](/docs/cms/building-blocks/themes), fields are used to enable content creators to control module and theme styling and functionality on your website. When developing a module or a theme, you'll include fields in a `fields.json` file, which will then translate to the theme and content editors.

![theme-settings-fields](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/theme-settings-fields.png?width=409&height=607&name=theme-settings-fields.png)

Below, learn more about how to create and manage options for module and theme fields. To learn more about specific field types, check out the [module and field types reference guide](/docs/cms/building-blocks/module-theme-fields). 

Creating and managing fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#creating-and-managing-fields)
-------------------------------------------------------------------------------------------------------------------------------------------------

You can add fields to a [module's](/docs/cms/building-blocks/modules) `fields.json` file locally through the [HubSpot CLI](/docs/cms/developer-reference/local-development-cli) and in the in-app module editor. To add fields to a [theme](/docs/cms/building-blocks/themes), you must update the theme's `fields.json` file locally using the CLI. 

### HubSpot CLI[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#hubspot-cli)

When [building locally](/docs/cms/guides/getting-started-with-local-development), module and theme fields can be edited through a `fields.json` file inside of the module or theme's folder. For modules, this file will automatically be created when using the [`hs create module`](/docs/cms/developer-reference/local-development-cms-cli) command. All of the field options available in the module editor are available as properties you can add or edit in the `fields.json` file. This includes repeater fields, groups, and conditions. One of the benefits of editing locally is that it makes it easier to [include your modules in version control systems like git](/docs/cms/guides/github-integration).

### Module editor[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#module-editor)

The [design manager](/docs/cms/developer-reference/design-manager) has a built-in module editor UI that enables you to [create](https://knowledge.hubspot.com/cos-general/create-and-edit-modules), group, and [edit](https://knowledge.hubspot.com/cos-general/create-and-edit-modules) module fields. The module editor contains a module preview which enables you to see what the module looks like on its own, as well as test your fields. Since modules do not live in a vacuum you should always test them on a template you plan to use, to see what template level styles may affect it. Be aware if a module is contained in a locked folder it cannot be edited this way.

![Design Manager Module Editor](https://developers.hubspot.com/hubfs/Module%20Editor-1-1.png "Design Manager Module Editor")

**Please note:** if you are working mostly locally but want to use the module editor to configure fields, make sure to [fetch](/docs/cms/developer-reference/local-development-cms-cli#fetch) your changes. This is especially important for those using version control systems like git.

Side by side fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#side-by-side-fields)
-------------------------------------------------------------------------------------------------------------------------------

By default, module fields in content editors stack vertically. However, you can place module fields side by side by adding a `display_width` property to fields in the `fields.json` file with a value of `half_width`. 

![side-by-side-modules0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/side-by-side-modules0.png?width=361&name=side-by-side-modules0.png)

A single field with a `display_width` of `half_width` will appear as half-width in the content editor. When the field above or below that field in the `fields.json` file is set to `half_width`, they'll be placed side by side.

// Example module fields.json file \[ { "name": "number\_field", "label": "Number", "required": false, "locked": false, "display": "slider", "min": 1, "max": 10, "step": 1, "type": "number", "prefix": "", "suffix": "", "default": null, "display\_width":"half\_width" }, { "label": "Description", "name": "description", "type": "text", "required": true, "default": "Add a description", "display\_width": "half\_width" } \]

Field groups[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#field-groups)
-----------------------------------------------------------------------------------------------------------------

When fields are related to each other often it makes sense for them to be displayed visually grouped. Modules and Themes support grouping multiple fields together. 

![Field group without nested field groups](https://developers.hubspot.com/hs-fs/hubfs/Screen%20Shot%202020-02-26%20at%201.16.28%20PM.png?width=332&height=398&name=Screen%20Shot%202020-02-26%20at%201.16.28%20PM.png "Field group without nested field groups")

Field groups without nested field groups display simply with dividers above and below the group, and the group's label is displayed at the top of the group.

![Nested field group](https://developers.hubspot.com/hubfs/Nested%20field%20group.png "Nested field group")

Field Groups can be nested. A field group that contains another field group will display as a button. Clicking the button to view the group will show the contents of that group.

Field groups can be nested 3 levels deep, meaning module fields, can have 4 levels of depth. Making it easy to create user interfaces that convey field relationships and more granular depth.

### Field groups in fields.json[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#field-groups-in-fields-json)

Field group objects can be listed as children of other field groups, their structure is very similar to field's themselves with the only special parameter being the "children" parameter, which is an array of fields and groups they contain.

// Field group example { "type": "group", "name": "typography", "label": "Typography", "expanded": true, "children": \[ { "type": "font", "name": "h1\_font", "label": "Heading 1", "load\_external\_fonts": true, "default": { "color": "#000", "font": "Merriweather", "font\_set": "GOOGLE", "variant": "700", "size": "48" } } \] } // Field group inside of a field group { "type": "group", "name": "header", "label": "Header", "children": \[ { "type": "font", "name": "h1\_font", "label": "Heading 1", "load\_external\_fonts": true, "default": { "color": "#000", "font": "Merriweather", "font\_set": "GOOGLE", "variant": "700", "size": "48" } { "type": "group", "name": "navigation", "label": "Navigation", "expanded": false, "children": \[ { "name" : "bg\_color", "label" : "Background color", "sortable" : false, "required" : false, "locked" : false, "type" : "color", "default" : { "color" : "#ff0000", "opacity" : 100 } } \] } } \] }

#### Expanding field groups by default[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#expanding-field-groups-by-default)

Field groups can be set to be expanded by default by setting the `expanded` boolean property to `true` in the fields.json group properties as shown in the example code above. Field groups are not expanded by default and when using nested field groups, the parent group cannot make use of this property.

#### Outputting field values within Field Groups[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#outputting-field-values-within-field-groups)

Field groups create dicts that contain the field values you want to output. If you nest field groups the nested field group is a dict inside of the outside field group dict. To access that data you will traverse the tree from either the root theme or module variable depending on your context.

<div> {# printing a value from a field group \`recipe\_summary\` is the field group, \`title\` is the text field. #} {{module.recipe\_summary.title}} </div>/\* Printing a Font field's color value, when the font field is within a field group. \`typography\` is the field group, \`h1\_font\` is the field \*/ h1{ color: {{ theme.typography.h1\_font.color }}; }

Style fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#style-fields)
-----------------------------------------------------------------------------------------------------------------

Style fields are a special field group type in a module or theme's `fields.json` file that give content creators control over a module or theme's styling in the page and theme editor. Below, learn how to add style fields to a module or theme. Learn about [best practices for using and organizing style fields](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices).

### Module style fields

Style fields added to a module will appear on the _Styles_ tab of the page editor when editing the module: 

![style-field-module-editor0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/style-field-module-editor0.png?width=377&name=style-field-module-editor0.png)

When adding style fields to a module's `fields.json` file, you add them within one styles group. That group, however, can contain multiple groups within it, as shown below:

// Module style fields \[ { "type": "group", "name": "styles", "tab": "STYLE", "children": \[{ "name": "img\_spacing", "label": "Spacing around image", "required": false, "type": "spacing", "default": { "padding": { "top": { "value": 10, "units": "px" }, "bottom": { "value": 10, "units": "px" }, "left": { "value": 10, "units": "px" }, "right": { "value": 10, "units": "px" } }, "margin": { "top": { "value": 10, "units": "px" }, "bottom": { "value": 10, "units": "px" } } } }\] } \]

The following fields can be used as style fields in modules. Learn about each of the field types in the [module and field types guide](/en/docs/cms/building-blocks/module-theme-fields).

*   [Alignment](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#alignment)
*   [Gradient](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#gradient)
*   [Spacing](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#spacing)
*   [Background Image](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#background-image)
*   [Border](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#border)
*   [Boolean](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#boolean)
*   [Choice](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#choice)
*   [Number](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#number)
*   [Color](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#color)
*   [Icon](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#icon)
*   [Image](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#image)
*   [Font](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#font)
*   [Text Alignment](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#text-alignment) 

Learn more about [module and theme field types](/en/docs/cms/building-blocks/module-theme-fields).

View the [CMS boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/main/src/modules/card.module/fields.json) for an example of a style fields within a module's `fields.json` file.

### Theme style fields

Style fields added to a theme will appear in the left sidebar of the theme editor:

![style-field-theme-editor0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/style-field-theme-editor0.png?width=371&name=style-field-theme-editor0.png)

All style fields within a theme's `fields.json` file will be added to the left sidebar of the theme editor, as opposed to needing to put them under a styles group, as shown below:

// Theme style fields \[ { "label": "Global colors", "name": "global\_colors", "type": "group", "children": \[ { "label": "Primary", "name": "primary", "type": "color", "visibility": { "hidden\_subfields": { "opacity": true } }, "default": { "color": "#494A52" } }, { "label": "Secondary", "name": "secondary", "type": "color", "visibility": { "hidden\_subfields": { "opacity": true } }, "default": { "color": "#F8FAFC" } } \] }, { "label": "Global fonts", "name": "global\_fonts", "type": "group", "children": \[ { "label": "Primary", "name": "primary", "type": "font", "visibility": { "hidden\_subfields": { "size": true, "styles": true } }, "inherited\_value": { "property\_value\_paths": { "color": "theme.global\_colors.primary.color" } }, "default": { "fallback": "sans-serif", "font": "Lato", "font\_set": "GOOGLE" } }, { "label": "Secondary", "name": "secondary", "type": "font", "visibility": { "hidden\_subfields": { "size": true, "styles": true } }, "inherited\_value": { "property\_value\_paths": { "color": "theme.global\_colors.primary.color" } }, "default": { "fallback": "serif", "font": "Merriweather", "font\_set": "GOOGLE" } } \] }, { "name": "branding\_color", "label": "branding\_color", "type": "color", "default": { "color": "#3b7bc0", "opacity": 60 }, "inherited\_value": { "property\_value\_paths": { "color": "brand\_settings.primaryColor" } } }, { "name": "secondary\_branding\_color", "label": "Secondary Branding color", "type": "color", "default": { "color": "#ff6b6b", "opacity": 60 }, "inherited\_value": { "property\_value\_paths": { "color": "brand\_settings.colors\[2\]" } } } \] } \]

The following fields can be used as style fields in modules. Learn about each of the field types in the [module and field types guide](/en/docs/cms/building-blocks/module-theme-fields).

*   [Boolean](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#boolean)
*   [Border](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#border)
*   [Choice](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#choice)
*   [Color](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#color)
*   [Font](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#font)
*   [Image](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#image)
*   [Number](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#number)
*   [Spacing](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#spacing)

Learn more about [module and theme field types](/en/docs/cms/building-blocks/module-theme-fields).

View the [CMS boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/main/src/fields.json) for an example of a style fields within a theme's `fields.json` file. 

**Please note:** if you're a marketplace provider, you should not replace existing content fields with style fields in existing modules. Changing the hierarchy of fields in a `fields.json` file can result in existing module instances losing their data. Instead, you should add new style fields, or create a new listing that has the fields appropriately grouped. This will prevent your updates from being breaking changes for customers relying on your themes. To advocate for migration paths for old modules, [check out the HubSpot Ideas forum](https://community.hubspot.com/t5/HubSpot-Ideas/Create-a-path-to-make-it-possible-to-migrate-existing-fields-to/idi-p/450311#M85938).

### Generated CSS[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#generated-css)

Some style fields provide a way to output css directly based on the field's value. This is especially helpful with fields that can control more complicated styling like gradients. The following style fields have a generated `.css` property:

*   [Background Image](/docs/cms/building-blocks/module-theme-fields/#background-image) 
*   [Border](/docs/cms/building-blocks/module-theme-fields#border)
*   [Color](/docs/cms/building-blocks/module-theme-fields#color)
*   [Font](/docs/cms/building-blocks/module-theme-fields#font)
*   [Gradient](/docs/cms/building-blocks/module-theme-fields/#gradient)
*   [Spacing](/docs/cms/building-blocks/module-theme-fields#spacing) 
*   [Text alignment](/docs/cms/building-blocks/module-theme-fields#text-alignment) 

{% require\_css %} <style> {% scope\_css %} .team-member { {% if module.style.gradient.css %} background: {{ module.style.gradient.css }}; {% endif %} {{ module.style.bg\_img.css }} {{ module.style.spacing.css }} {{ module.style.border.css }} } {% end\_scope\_css %} </style> {% end\_require\_css %}

Repeaters[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#repeaters)
-----------------------------------------------------------------------------------------------------------

When creating modules that format information, often there are types of information that repeat. A recipe module for example, might have a field for "Ingredient". Well, most recipes have more than 1 ingredient. You could give them a rich text field, but then you lose your ability to force consistent styling and add functionality around each ingredient. That's where repeaters come in, HubSpot has two forms of repeaters: Repeating fields, and Repeating groups.

### Repeating fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#repeating-fields)

Repeating fields are normal fields but content creators can add, remove, and re-arrange instances of the field. Using the recipe module example above, each ingredient could be a repeating text field. 

![repeater field](https://developers.hubspot.com/hubfs/repeater%20field.png "repeater field")

This makes it so the content creator can add as many ingredients as they wish. From the developer perspective, you get an array that you can loop through to print out that list of ingredients, applying the formatting and functionality you want. 

Repeating fields are best used for very simple situations. Often times [repeating groups](#repeating-groups) make more sense.

**Please note:** it's not currently possible to set the default order of repeating fields.

#### Repeating fields in fields.json[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#repeating-fields-in-fields-json)

// Repeating field example { "name" : "ingredient", "label" : "Ingredient", "required" : false, "locked" : false, "occurrence" : { "min" : 1, "max" : null, "sorting\_label\_field" : null, "default" : 1 }, "allow\_new\_line" : false, "show\_emoji\_picker" : true, "type" : "text", "default" : \[ "1 cup water" \] }

#### Loop through items in module HTML+HubL[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#loop-through-items-in-module-html-hubl)

<!--Looping through a repeating field--> <ul> {% for item in module.ingredient %} <li>{{ item }}</li> {% endfor %} </ul>

### Repeating groups[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#repeating-groups)

Repeating groups are field groups with the repeating option enabled. Repeating groups allow content creators to add, remove, and re-arrange groups of fields. Using the recipe module example, say that you want to integrate your ingredients list with a shopping list functionality.

![Repeating group of fields](https://developers.hubspot.com/hubfs/Screen%20Shot%202020-02-26%20at%205.19.14%20PM.png "Repeating group of fields")

The quantity of an ingredient would be critical to the shopping list. While someone could provide that in the text field, the module would then need to parse the text field and hope we are successfully separating the quantity from the ingredient. This is where repeating groups come in handy. The output of these fields is an object that can be looped through.

#### Repeating groups in fields.json[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#repeating-groups-in-fields-json)

// Repeating field group example { "id" : "ingredients", "name" : "ingredients", "label" : "Ingredients", "required" : false, "locked" : false, "occurrence" : { "min" : 1, "max" : null, "sorting\_label\_field" : "ingredients.ingredient", "default" : null }, "children" : \[ { "id" : "ingredients.ingredient", "name" : "ingredient", "label" : "Ingredient", "required" : false, "locked" : false, "validation\_regex" : "", "allow\_new\_line" : false, "show\_emoji\_picker" : false, "type" : "text", "default" : "Water" }, { "id" : "ingredients.quantity", "name" : "quantity", "label" : "Quantity", "required" : false, "locked" : false, "display" : "text", "min" : 0, "step" : 1, "type" : "number", "default" : 1 }, { "id" : "ingredients.measurement", "name" : "measurement", "label" : "Measurement", "help\_text" : "Unit of measurement (cups, tbsp, etc.)", "required" : false, "locked" : false, "allow\_new\_line" : false, "show\_emoji\_picker" : false, "type" : "text", "default" : "cups" } \], "type" : "group", "default" : \[ { "ingredient" : "Water", "quantity" : 1, "measurement" : "cups" } \] }

#### Looping through repeating fields in modules[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#looping-through-repeating-fields-in-modules)

<h2>Ingredients</h2> <ul> {% for ingredient in module.ingredients %} <li> <button data-quantity="{{ ingredient.quantity }}" data-unit="{{ ingredient.measurement }}" data-ingredient="{{ ingredient.ingredient }}"> Add to cart </button> {{ ingredient.quantity }} {{ ingredient.measurement }} {{ ingredient.ingredient }} </li> {% endfor %} </ul>

### Repeater options[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#repeater-options)

To make the editing experience better and prevent content editors from providing values that you have not programmatically accommodated for, we allow you to set minimum and maximum values for how many items content creators can add to a repeating field or repeating group. 

For repeating groups you can also set which field acts as the label for that item when viewing the repeater.

![Max number of occurences](https://developers.hubspot.com/hubfs/Screen%20Shot%202020-02-26%20at%205.35.29%20PM.png "Max number of occurences")

"occurrence" : { "min" : 1, "max" : 4, "sorting\_label\_field" : "ingredients.ingredient", }

Repeater Options
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`max`

 | Integer | 

Maximum number of occurrences of this group. Prevents the content creator from adding more than this number of items in the UI.

 | `null` |
| 

`min`

 | Integer | 

Minimum number of occurrences of this field group. Prevents users from having less than this number of items in the UI.

 | `null` |
| 

`sorting_label_field`

 | String | 

This is the field id, of the field to pull text from to show in the UI on the draggable cards. The default for this is the first field in the group.

 |  |

Inherited fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#inherited-fields)
-------------------------------------------------------------------------------------------------------------------------

The `inherited_value` property can be configured to make a field inherit its default value from other fields. To set a field's entire default value from another field's value, set the `default_value_path` to the field name path of the target field. When `default_value_path` is set, it'll ignore any `default` set on the field.

To access other fields' values, paths must include `module.` at the beginning as if you were accessing the value in the module's HubL code.

// Inherited fields { "name": "body\_font", "type": "font", "default": { "font": "Helvetica", "color": "#C27BA0" } }, { "name": "h1\_font", "type": "font", "default": {}, "inherited\_value": { "default\_value\_path": "module.body\_font" } }

For complex fields (fields whose values are objects), users can have more granularity over which properties get inherited through `property_value_path`. Any paths referred in `inherited_value` can also include keys from a field's value for complex fields - for example, color fields have object values that contain the color itself as well as opacity. So to get a color's actual color value without the opacity, the path would end in `.color`. For example, a font field can inherit just its color from a separate color field:

// Inherited fields with objects { "name": "secondary\_color", "type": "color", "default": { "color": "#C27BA0", "opacity": 100 } }, { "name": "h1\_font", "type": "font", "default": { "font": "Helvetica", "size": 12, "size\_unit": "px" }, "inherited\_value": { "property\_value\_paths": { "color": "module.secondary\_color.color" } } }

You can also combine the effects of `default_value_path` and `property_value_paths` to inherit a default value from one field while inheriting a specific property value from a different field:

// combining the effects of default\_value\_path and property\_value\_paths { "name": "body\_font", "type": "font", "default": { "font": "Helvetica", "color": "#000000" } }, { "name": "secondary\_color", "type": "color", "default": { "color": "#C27BA0", "opacity": 100 } }, { "name": "h1\_font", "type": "font", "default": {}, "inherited\_value": { "default\_value\_path": "module.body\_font", "property\_value\_paths": { "color": "module.secondary\_color.color" } } }

If a field inherits from another field but then gets directly overridden at the page level or in theme settings, its connection to the controlling field gets severed. Any other fields attached via `default_value_path` or `property_value_paths` will no longer affect the value of the field.

Field visibility[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#field-visibility)
-------------------------------------------------------------------------------------------------------------------------

When defining custom module and theme fields, you can configure when a field appears by adding the `visibility` object to the field in the `fields.json` file. For example, you can set a form module to display a rich text area when the thank you message is selected, but a page selector when a redirect is selected.

You can set visibility based on the value of a `controlling_field_path`, or based on a specific property within that field using the `property` parameter.  
  
You can also apply visibility to an individual field, or to a group of fields to control visibility for all elements in the group.

"visibility" : { "controlling\_field\_path" : "field\_name", "controlling\_value\_regex" : "regular\_expression\_in\_controlling\_field", "property": "src", "operator" : "EQUAL" }

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`controlling_field_path`

 | String | 

The doth path of the field that controls the display condition.

*   If the field is not nested inside a field group, use the field's name (i.e. `field_name`).
*   For fields nested in groups, the path should match its grouping structure, separated by a period. For example:
    *   `field_group_name.field_name`
    *   `parent_group.child_group.field_name`

 |
| 

`controlling_value_regex`

 | String | 

The regular expression in the controlling field that needs to be present for the field to display. The regex must match the entire string (not a subset) and is run case-sensitively. 

 |
| 

`operator`

 | String | 

The operator that defines how the `controlling_value_regex` value needs to be met. Operators can be one of: 

*   `NOT_EQUAL`
*   `EQUAL`
*   `EMPTY`
*   `NOT_EMPTY`
*   `MATCHES_REGEX`

 |
| 

`property`

 | String | 

Sets visibility based on a specific property of the target field. For example, you can enable visibility when an image field's `src` property is equal to a specific value. By default, if no value is provided for this field, visibility is based on the stringified value of `controlling_value_regex`.

 |

The visibility attribute can support only one criteria at a time. To include multiple criteria with multiple operators, as well as order of operations, you can use `advanced_visibility`.

"visibility\_rules" : "ADVANCED", "advanced\_visibility" : { "boolean\_operator" : "AND", "criteria" : \[{ "controlling\_field\_path" : "field\_name", "controlling\_value\_regex" : "regular\_expression\_in\_controlling\_field", "operator" : "MATCHES\_REGEX" }, { "controlling\_field\_path" : "field\_name", "controlling\_value\_regex" : "regular\_expression\_in\_controlling\_field", "operator" : "EQUAL" }\] }

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`visibility_rules`

 | String | 

By default, this value is set to `SIMPLE`. To use `advanced_visibility`, set to `ADVANCED`.

 |
| 

`boolean_operator`

 | String | 

The boolean operator for the conditional criteria. Can be `AND` or `OR`.

 |
| 

`criteria`

 | Array | 

An array of visibility objects that defines the conditional criteria that needs to be met for the field to display.

 |
| 

`controlling_field_path`

 | String | 

The dot path of the field that controls the display condition.

*   If the field is not nested inside a field group, use the field's name (i.e. `field_name`).
*   For fields nested in groups, the path should match its grouping structure, separated by a period. For example:
    *   `field_group_name.field_name`
    *   `parent_group.child_group.field_name`

 |
| 

`controlling_value_regex`

 | String | 

The value in the controlling field that needs to be met to display the field. When using the `MATCHES_REGEX` operator, the regex must match the entire string (not a subset) and is run case-sensitively.

A field with a `controlling_field_path` but no `controlling_value_regex` is visible if the controlling field has any non-null, non-blank value.

 |
| 

`operator`

 | String | 

The operator that defines how the `controlling_value_regex` value needs to be met. Operators can be one of: 

*   `NOT_EQUAL`
*   `EQUAL`
*   `EMPTY`
*   `NOT_EMPTY`
*   `MATCHES_REGEX`

Regex syntax is required when using `MATCHES_REGEX`.

 |

As an example, below is the first portion of code from the [default payments module](/docs/cms/building-blocks/modules/default-modules). To review the full code, you can clone the module in HubSpot, then download into your local environment to view the module's `fields.json` file.

\[ { "id" : "payment", "name" : "payment", "display\_width" : null, "label" : "Payment", "required" : true, "locked" : false, "type" : "payment", "default" : { "id" : null, "properties" : { } } }, { "id" : "checkout\_location", "name" : "checkout\_location", "display\_width" : null, "label" : "Checkout behavior", "required" : false, "locked" : false, "visibility" : { "controlling\_field\_path" : "payment", "controlling\_value\_regex" : "id\\":\\\\d+", "operator" : "MATCHES\_REGEX" }, "display" : "radio", "choices" : \[ \[ "new\_tab", "Open in a new tab" \], \[ "overlay", "Sliding overlay" \] \], "type" : "choice", "default" : "new\_tab" }, { "id" : "button\_text", "name" : "button\_text", "display\_width" : null, "label" : "Button text", "required" : true, "locked" : false, "validation\_regex" : "", "visibility" : { "controlling\_field\_path" : "payment", "controlling\_value\_regex" : "id\\":\\\\d+", "operator" : "MATCHES\_REGEX" }, "allow\_new\_line" : false, "show\_emoji\_picker" : false, "type" : "text", "default" : "Checkout" }, { "id" : "icon", "name" : "icon", "display\_width" : null, "label" : "Icon", "required" : false, "locked" : false, "visibility\_rules" : "ADVANCED", "advanced\_visibility" : { "boolean\_operator" : "AND", "criteria" : \[ { "controlling\_field\_path" : "payment", "controlling\_value\_regex" : "id\\":\\\\d+", "operator" : "MATCHES\_REGEX" }, { "controlling\_field\_path" : "add\_icon", "controlling\_value\_regex" : "true", "operator" : "EQUAL" } \], "children" : \[ \] }, "children" : \[ { "id" : "icon.icon", "name" : "icon", "display\_width" : null, "label" : "Icon", "required" : true, "locked" : false, "icon\_set" : "fontawesome-5.0.10", "type" : "icon", "default" : { "name" : "hubspot", "type" : "SOLID", "unicode" : "f3b2" } }, { "id" : "icon.position", "name" : "position", "display\_width" : null, "label" : "Position", "required" : true, "locked" : false, "display" : "select", "choices" : \[ \[ "left", "Left" \], \[ "right", "Right" \] \], "type" : "choice", "default" : "left" } \], "tab" : "CONTENT", "expanded" : false, "type" : "group" }, // rest of fields.json code \]

The above code results in the following behavior:

*   The first field (`payment`) is a required field (dropdown menu) that lets the content creator select a specific payment link. In HubSpot, a content creator will see the following when first adding the module to the page:

![payment-link-selector](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/payment-link-selector.png?width=375&name=payment-link-selector.png)

*   Once a payment link is selected, the three fields that follow (`checkout_location`, `button_text`, and `icon`) will appear. This is because the fields have a `visibility` attribute which is controlled by the `payment` field and requires an ID value in the payment field's `id` parameter.

The `icon` field itself uses `advanced_visibility` to appear only when there's a payment link present in the `payment` field AND when the `add_icon` checkbox is selected.

In addition to setting visibility within `fields.json`, You can also set visibility in the design manager by editing a field's _Display conditions_ options.  
![display-conditions-property](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/display-conditions-property.png?width=357&height=332&name=display-conditions-property.png)

After setting visibility in the design manager, you can [fetch](/docs/cms/developer-reference/local-development-cli#fetch) the module [using the CLI](/docs/cms/guides/getting-started-with-local-development) to view the `visibility` attribute in the module's `fields.json` file.

Conditional field disabling[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#conditional-field-disabling)
-----------------------------------------------------------------------------------------------------------------------------------------------

You can add conditions to a field to prevent editing when the specified conditions are met. You can also set a message to display above the field  when disabled to provide context in the content editor. 

![Screenshot 2023-05-23 at 4.10.28 PM](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/Screenshot%202023-05-23%20at%204.10.28%20PM.png?width=321&height=148&name=Screenshot%202023-05-23%20at%204.10.28%20PM.png)

The conditions and message are set in the field's `disabled_controls` object. The conditions for making a field editable are set within the `rules` object, which follows the same format as [advanced\_visibility](#field-visibility).

The code below shows both a simple and advanced implementation of `rules` criteria:

*   The `simple_page` field includes logic to disable the field if the `text_field` is set to `testing`.
*   The `fancy_page` field includes logic to disable the field if either `text_field` or `text_field_2` is set to any value not equal to `testing` and `testing2` respectively.

// example fields.json \[ { "type": "text", "name": "text\_field", "label": "Text field", }, { "type": "text", "name": "text\_field\_2", "label": "Text field 2", }, { "type": "page", "label": "Simple Page", "name": "simple\_page", "disabled\_controls": { "message": "This field is disabled", "rules": { "criteria": \[ { "controlling\_field\_path": "text\_field", "operator" :"EQUAL", "controlling\_value\_regex": "testing" } \] } } }, { "type": "page", "label": "Fancy Page", "name": "fancy\_page", "disabled\_controls": { "message": "This field is disabled", "rules": { "boolean\_operator": "OR", "criteria": \[ { "controlling\_field\_path": "text\_field", "operator" :"NOT\_EQUAL", "controlling\_value\_regex": "testing" }, { "controlling\_field\_path": "text\_field\_2", "operator" :"NOT\_EQUAL", "controlling\_value\_regex": "testing2" }, \] } } } \]

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`message`

 | String | 

The message to display in the content editor when the field is disabled.

 |
| 

`rules`

 | Object | 

The conditions for enabling the field for editing.

 |
| 

`criteria`

 | Array | 

An array of condition objects that defines the criteria that needs to be met for the field to display. This array can contain multiple condition objects separated by `AND` or`OR` logic through the `boolean_operator` parameter.

 |
| 

`boolean_operator`

 | String | 

The boolean operator for the conditional criteria. Can be `AND` or `OR`. When not specified, defaults to `AND`.

 |
| 

`controlling_field_path`

 | String | 

The dot path of the field that controls the display condition.

*   If the field is not nested inside a field group, use the field's name (i.e. `field_name`).
*   For fields nested in groups, the path should match its grouping structure, separated by a period. For example:
    *   `field_group_name.field_name`
    *   `parent_group.child_group.field_name`

 |
| 

`controlling_value_regex`

 | String | 

The value in the controlling field that needs to be met to display the field. When using the `MATCHES_REGEX` operator, the regex must match the entire string (not a subset) and is run case-sensitively.

A field with a `controlling_field_path` but no `controlling_value_regex` is visible if the controlling field has any non-null, non-blank value.

 |
| 

`operator`

 | String | 

The operator that defines how the `controlling_value_regex` value needs to be met. Operators can be one of: 

*   `NOT_EQUAL`
*   `EQUAL`
*   `EMPTY`
*   `NOT_EMPTY`
*   `MATCHES_REGEX`

Regex syntax is required when using `MATCHES_REGEX`.

 |

Theme editor field highlighting[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#theme-editor-field-highlighting)
-------------------------------------------------------------------------------------------------------------------------------------------------------

When in the theme editor, preview highlighting can help content creators understand which fields are controlling which page elements. Preview highlighting works by mapping the theme fields to the CSS selectors that they affect, adding a box around those elements when hovering over the field in the theme editor.

To configure preview highlighting for theme fields, you'll include an `editor-preview.json` file in the root directory of the theme to map theme fields to a list of CSS selectors. In the file, you'll include an array for each style field you want to highlight containing the relevant CSS selectors, using the following format:

// editor-preview.json { "selectors": { "theme.settings.path.1": \[ <CSS selectors> \], "theme.settings.path.2": \[ <CSS selectors> \], } }

For example, the code below will highlight which page elements are controlled by the primary font field. You can view the full example in the `editor-preview.json` file of the default Growth theme.

// editor-preview.json { "selectors": { "fonts.primary": \[ "button, .button, .hs-button", "form input\[type='submit'\], form .hs-button", ".error-page:before", "p", "blockquote > footer", "form td.is-today .pika-button", "form .is-selected .pika-button", "th, td", ".blog-listing\_\_post-tag", ".blog-listing\_\_post-author-name, .blog-post\_\_author-name", ".pagination\_\_link-icon svg", ".tabs\_\_tab", "a", ".button.button--simple", ".pagination\_\_link .pagination\_\_link-icon svg", ".card--dark", ".card--light", ".card--light summary, .card--light p, .card--light h1, .card--light h2, .card--light h3, .card--light h4, .card--light h5, .card--light h6, .card--light a:not(.button), .card--light span, .card--light div, .card--light li, .card--light blockquote", ".card--light .accordion\_\_summary:before", "tfoot th, tfoot td", ".header\_\_language-switcher-current-label > span", ".header\_\_language-switcher-child-toggle svg", ".header\_\_language-switcher .lang\_list\_class a:not(.button)", ".header\_\_menu-link", ".header\_\_menu-item--depth-1 > .header\_\_menu-link:not(.button)", ".header\_\_menu-item--depth-1 .header\_\_menu-child-toggle svg", ".header\_\_menu-toggle svg", ".header\_\_language-switcher .header\_\_language-switcher-current-label > span", ".header p, .header h1, .header h2, .header h3, .header h4, .header h5, .header h6, .header a:not(.button), .header span, .header li, .header blockquote, .header .tabs\_\_tab, .header .tabs\_\_tab, .header .tabs\_\_tab, .header .tabs\_\_tab", ".footer .hs-menu-wrapper a", ".footer h1, .footer h2, .footer h3, .footer h4, .footer h5, .footer h6, .footer p, .footer a:not(.button), .footer span, .footer div, .footer li, .footer blockquote, .footer .tabs\_\_tab, .footer .tabs\_\_tab, .footer .tabs\_\_tab, .footer .tabs\_\_tab", ".footer hr", "form label", "#email-prefs-form, #email-prefs-form h1, #email-prefs-form h2", "form legend", "form input\[type='text'\], form input\[type='email'\], form input\[type='password'\], form input\[type='tel'\], form input\[type='number'\], form input\[type='search'\], form select, form textarea", ".backup-unsubscribe input\[type='email'\]", "form .legal-consent-container, form .legal-consent-container .hs-richtext, form .legal-consent-container .hs-richtext p", "form .hs-richtext, form .hs-richtext \*, form .hs-richtext p, form .hs-richtext h1, form .hs-richtext h2, form .hs-richtext h3, form .hs-richtext h4, form .hs-richtext h5, form .hs-richtext h6", "button, button, button, .button, .button, .button, .hs-button, .hs-button, .hs-button", "button, .button, .hs-button", ".button.button--secondary, .button.button--secondary, .button.button--secondary", ".button.button--secondary", ".header\_\_menu-item--depth-1 > .header\_\_menu-link, .header\_\_menu-item--depth-1 > .header\_\_menu-link", ".header\_\_menu-item--depth-1 > .header\_\_menu-link", ".header\_\_menu-submenu .header\_\_menu-link, .header\_\_menu-submenu .header\_\_menu-link", ".header\_\_language-switcher .lang\_list\_class a, .header\_\_language-switcher .lang\_list\_class a", ".header\_\_menu-submenu .header\_\_menu-link:not(.button)", ".footer .hs-menu-wrapper a, .footer .hs-menu-wrapper a", ".footer .hs-menu-wrapper a", "form .hs-richtext a", ".header\_\_menu-item--depth-1 > .header\_\_menu-link--active-link:not(.button)", ".footer .hs-menu-wrapper .active > a" \] } }

![growth-theme-hover](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/growth-theme-hover.png?width=800&height=456&name=growth-theme-hover.png)

To get started generating this file, run the following [CLI command](/docs/cms/developer-reference/local-development-cli#generate-theme-field-selectors-for-in-app-highlighting) to create the file. During file creation, a script will run to set up the initial field-selectors mappings.

hs theme generate-selectors <theme-directory-path>

| Parameter | Description |
| --- | --- |
| 
`theme-directory-path`

 | 

The path to the theme directory.

 |

After running the command, you'll need to review and refine the `editor-preview.json` file to ensure that fields and selectors are mapped properly. While the [generate-selectors](/docs/cms/developer-reference/local-development-cli#generate-theme-field-selectors-for-in-app-highlighting) command will make a rudimentary guess about which fields affect which selectors, you'll need to make corrections based on how your theme is built. For example, this command cannot detect when modules are overriding styling or when you're using macros.

To test these mappings, upload the theme to an account, then view the theme editor in that account (Settings \> Website > Themes \> View theme). 

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#page-feedback)
-------------------------------------------------------------------------------------------------------------------------

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