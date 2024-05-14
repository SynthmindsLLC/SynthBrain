HubSpot Template Marketplace module requirements


====================================================

Last updated: May 6, 2024

Learn about the requirements to submit a module to the Template Marketplace. These requirements apply to both modules in a theme and independent modules. 

Module restrictions[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#module-restrictions)
-----------------------------------------------------------------------------------------------------------------------------

Modules must not contain [HubDB](/docs/cms/features/hubdb), calls to [serverless functions](/docs/cms/features/serverless-functions), or the [CRM object field](/docs/cms/building-blocks/module-theme-fields#crm-object).

The following module types should not be built as independent modules

*   HTML
*   Full-width modules
*   Forms and multi-step forms
*   Spacer modules or modules that create non-UI page structure
*   Modules that duplicate default module functionality
*   Commerce-specific modules
*   Email-specific modules

Module content[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#module-content)
-------------------------------------------------------------------------------------------------------------------

Learn about the requirements for module labels and help text, fields, and default content.

### Module labels & help text[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#module-labels-help-text)

*   Modules must have descriptive labels that convey the purpose of the module. The label _Hero Banner with Parallax Scrolling_ is descriptive, whereas the labels _Hero Banner_ and _Gallery_ are not.   
    
*   Module labels must not contain numbers, such as _Hero Banner 01_.  
    
*   Module labels must not contain underscores. 
*   Module labels must not contain abbreviations, such as _Col_ instead of _Column_.
*   Modules must contain [inline help text](https://developers.hubspot.com/docs/cms/building-blocks/modules/configuration#meta-json) where applicable to further convey how to use the module.
*   Modules should not be named the same as a [default module](/docs/cms/building-blocks/modules/default-modules).
*   For independent modules, the module label should match the name on the template listing. For example, if your template listing is _SuperAwesome Banner with Scrolling_, your module label should be the same. 

![listing-name](https://developers.hubspot.com/hubfs/Knowledge_Base_2023_2024/listing-name.png "listing-name")

![module-label](https://developers.hubspot.com/hubfs/Knowledge_Base_2023_2024/module-label.png "module-label")

### Default content[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#default-content)

*   Default field cannot include _Lorem ipsum_ text. 
*   Default field content should represent the field’s purpose:
    *   When including menu fields, modules must use _Select a menu_ as the default content option.
    *   When including form fields, modules must use _Select a form_ as the default content option.
    *   When including blog selector fields, modules must use _Select a blog_ as the default content option.
*   If adding default content to a module doesn't make sense, use a [module placeholder](/docs/cms/hubl/tags#editor-placeholders) instead to help the content creator visualize the space that they'll fill with content.

### Module icons[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#module-icons)

Modules must include a custom icon assigned to the module (replacing the default icon). Do not use company logos as icons, such as Apple or Amazon logos. Learn more about [module icons](https://developers.hubspot.com/docs/cms/building-blocks/modules/configuration#adding-an-icon).

### Modules that require 3rd party accounts[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#modules-that-require-3rd-party-accounts)

For individual modules, if the module requires a 3rd party account, it must be noted in the template description. For example, if your module makes use of the Google Maps Platform, you need to include a note, _"The use of this module requires a Google Cloud (Google Maps Platform) account."_

Module fields[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#module-fields)
-----------------------------------------------------------------------------------------------------------------

Review specific requirements for modules in a theme and independent modules below:  

*   For modules in a theme:
    *   Must contain inline help text and specific default content for certain fields.
    *   A part of the theme's [color](/docs/cms/building-blocks/module-theme-fields#color) and [logo](/docs/cms/building-blocks/module-theme-fields#logo) must inherit from the account's [brand settings](/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance).
        *   At a minimum, three color fields must inherit colors from the account's brand settings. Extra color fields can default to other colors, including black and white.
        *   At least one logo field must inherit from the account's brand settings. If using an image field to render a logo, the image field does not have to inherit from the brand settings. 
*   For both modules in a theme and independent modules:
    *   Module field names should describe the field’s intent. For example, if a text field is meant to include a person’s job title, _Job Title_ would be a proper description whereas _Title_ would not.
    *   All of HubSpot's default modules must be styled and must display properly on all templates submitted.

### fields.json and module.html configuration[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#fields-json-and-module-html-configuration)

To ensure compatible functionality between themes and independent modules, modules must [inherit](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview#inherited-fields) the color and font fields either by defining `default_value_path` or `property_value_paths`, or both in their `fields.json` file and add a reference to the theme fields in the `module.html` file. [Learn more about these requirements.](/docs/cms/marketplace-guidelines/general-requirements)

Module code quality[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#module-code-quality)
-----------------------------------------------------------------------------------------------------------------------------

### Modules must be self-contained[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#modules-must-be-self-contained)

#### Theme modules[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#theme-modules)

Any files needed for your theme module, such as CSS or JavaScript, must be contained in the theme folder and included in the theme directory. You can use the Linked Files feature in the Design Manager. Or, include the files using the [require\_js()](/docs/cms/hubl/functions#require-js) or [require\_css()](/docs/cms/hubl/functions#require-css) functions with a relative path to the file.

For common libraries, such as slick.js, you can include them using the `require_js()` or `require_css()` functions with an absolute URL to the CDN where it's hosted. 

**Please note:** do not use absolute URLs to assets contained within your development portal as cross-portal references will not resolve. 

#### Independent modules[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#independent-modules)

For independent modules, all CSS and Javascript files should be contained in either the `module.css` or `module.js`. Alternatively, include the files using the `require_js()` or `require_css()` functions with an absolute URL to the CDN where it’s hosted. It is not possible to use the Linked Files feature in the Design Manager as that is only available for theme modules. 

Since `module.js` is included in the DOM before any `require_js` or `require_css` files, Javascript contained in the `module.js` section should be deferred using the annotation below:

JavaScript

Copy all

    document.addEventListener("DOMContentLoaded", function(){
    // Put Javascript here
    });

All scripts and files should be rendered in the head of the module's [HTML](/docs/cms/hubl/functions#require-js). 

### Code restrictions for independent modules[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#code-restrictions-for-independent-modules)

The following restrictions apply to only independent modules:

*   It is recommended to use [vanilla JS](http://vanilla-js.com/) where possible. Adding a jQuery library to a site that is not using jQuery can potentially cause conflicts and slow down the website page.
*   If using a jQuery library, use the [require\_js()](/docs/cms/hubl/functions#require-js) function to include the library in the event that jQuery is turned off with the checkbox (Boolean) in account settings to avoid conflicts from multiple jQuery libraries. 

{% if not site\_settings.include\_jquery %} {{ require\_js("https://code.jquery.com/jquery-3.7.0.min.js", "footer") }} {% endif %}

### Categories[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#categories)

*   All independent modules must have at least one category. Modules submitted as part of a theme are not required to have categories, but it's best practice to include at least one. Learn more about [adding categories to modules](/docs/cms/building-blocks/modules/add-categories). 

### Class name selectors[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#class-name-selectors)

*   Any class name selectors must be prefixed with the module name, replacing spaces with hyphens. For example, below is the `module.html` file for a button named `example-button`, with each class name and CSS selector reflecting its name.

<style> {% scope\_css %} {# Button wrapper #} {% if module.styles.group\_alignment.alignment %} .example-button-wrapper { text-align: {{ module.styles.group\_alignment.alignment.horizontal\_align }}; } {% endif %} {# Button #} .example-button { {% if module.styles.group\_background.color.color %} background-color: rgba({{ module.styles.group\_background.color.color|convert\_rgb }}, {{ module.styles.group\_background.color.opacity / 100 }}); {% endif %} } {% end\_scope\_css %} </style> {% end\_require\_css %} {##### Module HTML #####} <div class="example-button-wrapper"> <a href="{{ href }}" class="example-button" {% if module.button\_link.open\_in\_new\_tab %}target="\_blank"{% endif %} {% if rel %}rel="{{ rel|join(" ") }}"{% endif %} > {{ module.button\_text }} </a> </div>

### Styles and Javascript[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#styles-and-javascript)

*   Styles:
    *   Modules must have a non-empty style group.
    *   Hardcoding inline styles within modules is not recommended. Instead, use dynamic inline styles by enabling fields to control styling.
*   JavaScript:  
    *   JavaScript must be able to represent multiple instances of a module. JavaScript in the JS Pane will only load once per page, regardless of the number of module occurrences.
    *   JavaScript should reference DOM elements by module-specific class names to ensure elements outside of the module are not unintentionally affected.

When creating modules, you can use a built-in variable called `Template Marketplace | Module requirements`. This variable pulls in the module's instance ID (which can be used in the HTML+HubL panel only) to help in CSS and JS markup for complex modules. [Learn more about this in our developer documentation.](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#require-css-block)

Field organization[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#field-organization)
---------------------------------------------------------------------------------------------------------------------------

The following field organization and grouping requirements must be met.

### Content tab

*   Where there is at least one control within a field group, all controls must be grouped into categories labeled by their function.
*   Module fields added to the _Content_ tab must give ways to customize the content of a module. For example, controls for image, icon, alt text, and link controls.

### Styles tab

Module style field groups must be consistent and follow a pattern. Below is a recommended order for your style field groups. These groups can either be at the top level or [nested one group deep](#multi-level-grouping). Empty groups may also be removed:

*   [Presets](#presets)
*   Text
*   Background
*   Border
*   Hover
*   Corner
*   Spacing
*   Alignment
*   Custom style groups that don't fit the above
*   Advanced

The following field types must be contained in the _Styles_ tab if present:

*   [Alignment](/docs/cms/building-blocks/module-theme-fields#alignment)
*   [Background image](/docs/cms/building-blocks/module-theme-fields#background-image)
*   [Border](/docs/cms/building-blocks/module-theme-fields#border)
*   [Color](/docs/cms/building-blocks/module-theme-fields#color)
*   [Font](/docs/cms/building-blocks/module-theme-fields#font)
*   [Gradient](/docs/cms/building-blocks/module-theme-fields#gradient)
*   [Spacing](/docs/cms/building-blocks/module-theme-fields#spacing) 
*   [Text alignment](/docs/cms/building-blocks/module-theme-fields#text-alignment)

When moving fields from the _Content_ tab to the _Styles_ tab, learn how to [use alias mapping](#aliases) to preserve styling for modules that are already in use on live pages.

*   Animation options should always be positioned near the bottom of the field group list.
*   Options that allow content creators to add code snippets or CSS should be grouped at the end of the field group list under a field labeled _Advanced_. 
*   Controls should be standardized across all modules. For example, all elements that can have a border radius control should offer that control. Avoid offering controls on some modules that are absent on others.

*   Module fields added to the _Style_ tab must provide ways to style the module. For example:
    *   Style options such as color, text styling, alignment, spacing, border, and corner radius.
    *   Animations such as hover and slide-in effects.
    *   Presets such as dark and light themes that are meant to change many styles at the same time.

### Examples of field organization

#### Presets

Presets can be used when wanting to give content creators a limited set of options, often tying back to theme settings. For example, the _Icon_ module included in the Growth theme contains presents for _Dark_ and _Light_ colors, which enables consistency when used across the website. 

#### Multi-level grouping

When deciding whether to keep style fields at the top level or nest them, consider the following example.

The _Icon_ module included in the Growth theme lists all its styles at the top level because it's one component, and therefore its style options all impact the one component. 

![growth-theme-icon-module](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/Developer/growth-theme-icon-module.png "growth-theme-icon-module")

The _Speaker card_ module included in the Growth theme contains multiple components: the card's image and its text contents. Module styles are therefore grouped by component so that the content creator has a more clear process for styling each component.

![growth-theme-speaker-card](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/Developer/growth-theme-speaker-card.png "growth-theme-speaker-card")

#### Grouping individual fields

The button module below contains groupings for _Presets_, _Text_, _Background_, and more. Although the _Corner_ field group contains only the corner radius control, it’s still grouped to create a uniform content creation experience.

![module-requirements-2_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/module-requirements-2_1.png?width=228&name=module-requirements-2_1.png)![button-styles](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/button-styles.png?width=375&height=641&name=button-styles.png) 

Aliases[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#aliases)
-----------------------------------------------------------------------------------------------------

Alias mapping enables you to create field mappings in a module so that you can move, rename, or replace its fields without impacting pages that are using the module. 

For example, a module is being used on a live page. You want to move some fields into the [_Styles_ tab](/docs/cms/building-blocks/module-theme-fields-overview#style-fields), such as color or font, but a content creator has already selected values for those fields in the editor. If you were to move those fields without setting up alias mapping, HubSpot would not be able to relocate those fields and they would revert to their default values, which would undo the styling on the live page.

Instead, you can add an `aliases_mapping` property to a field to map it to another one. Then, when a value has not been set for the original field, HubSpot will check if a value exists in the mapped field. If no value exists in the mapped field either, it will use the default value instead. This property can be used to map field values between different versions of a module only when the stored data type of the old field is the same as the new field's stored data type.

For a visual walkthrough of this feature, check out the video below.

To migrate existing fields to aliases:

1.  Create new fields and map them to old fields using the `aliases_mapping` property.
2.  Remove the old field definition.
3.  Update the `module.html` file to use the new fields definition.

**Please note:**

*   You cannot map fields that are of a different data type to each other. For example, you can't map a background gradient field to an image field. The stored value has to be a valid value for the new field's type.
*   When creating a new field with an alias mapping to an old field, the default values and required properties of both fields should be the same.

Below are examples of implementing this for both simple and complex changes:

*   [Simple implementation](#simple-implementation): mapping a color field to another new color field.
*   [Complex implementation](#complex-implementation): mapping a number field to a font field's `size` subfield to control font size.

### Simple implementation[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#simple-implementation)

In simple situations, the field type of the old field and the field type of the new field should be the same. For example:

*   Old color field to new color field. 
*   Old text field to new text field.
*   Old spacing field to new spacing field.

Below is an example of using `aliases_mapping` when moving a color field from the module's Content tab to the _Styles_ tab.

#### Example of a v0 module

\[ { "label": "Button Color", "name": "old\_button\_color\_field", "type": "color", "required": true, "default": { "color": "#FFFFFF", "opacity": 100 } } \]

#### Example of a v1 module

\[ { "label": "Styles", "name": "styles", "type": "group", "tab": "STYLE", "children": \[ { "label": "Button Color", "name": "new\_button\_color\_field", "type": "color", "required": true, "aliases\_mapping": { "property\_aliases\_paths": { "new\_button\_color\_field": \["old\_button\_color\_field"\] } }, "default": { "color": "#FFFFFF", "opacity": 100 } } \] } \]

### Complex implementation

In more complex situations, you can also map fields to subfields or other module field types as long as the data type is the same, and the new field's subfield type matches. Subfields are the properties within the field's stored value object. For example:

*   Mapping a _Rich text_ field to a _Text_ field, as the values in both fields are stored as strings.
*   Consolidating typography fields, such as changing from a number field for font size, to use a font field (which has a font size sub field). You can add an alias for the `size` subfield to map it to the old number field by using dot notation.

Below is an example of changing the font sizing option from a number field to a font field which has a font size sub field.

#### Example of a v0 module

\[ { "name": "my\_number\_field", "label": "Number field", "required": false, "locked": false, "display": "text", "step": 1, "type": "number", "min": null, "max": null, "inline\_help\_text": "", "help\_text": "", "default": null } \]

#### Example of a v1 module

\[ { "name": "my\_font\_field", "label": "font\_field", "required": false, "locked": false, "inline\_help\_text": "", "help\_text": "", "load\_external\_fonts": true, "type": "font", "aliases\_mapping": { "property\_aliases\_paths": { "my\_font\_field.size": \["my\_number\_field"\] } }, "default": { "size": 12, "font": "Merriweather", "font\_set": "GOOGLE", "size\_unit": "px", "color": "#000", "styles": {} } } \]

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/marketplace-guidelines/module-requirements#page-feedback)
-----------------------------------------------------------------------------------------------------------------------

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