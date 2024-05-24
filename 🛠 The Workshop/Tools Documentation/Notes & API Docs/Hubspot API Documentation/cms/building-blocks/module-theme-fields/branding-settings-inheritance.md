Brand settings inheritance


==============================

Last updated: September 14, 2023

With [brand settings](https://knowledge.hubspot.com/settings/customize-branding-for-your-hubspot-content#customize-your-company-logo-and-colors), users can set up the company's brand colors, logos, and favicons to be used across HubSpot content. This enables you to access those brand settings with tokens in a theme's `fields.json` file and within HTML/HubL and CSS files. You can also access brand colors within a module's `fields.json` file.

After adding these tokens within a `fields.json` file, content creators can edit their values within the theme settings editor. When adding these tokens in a HTML, HubL, or CSS, the values will be hardcoded and cannot be modified in the page editor by content creators. 

Below, learn about the available brand setting variables along with examples of implementation.

Brand Setting Variables[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance#brand-setting-variables)
------------------------------------------------------------------------------------------------------------------------------------------------------------

The following is a list of options that can be accessed from the brand settings area within the value of the `property_value_paths` object or within HTML/HubL and CSS files.

### Colors[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance#colors)

Brand colors can be accessed both within a theme or module's `fields.json` file, and within HTML/HubL and CSS files.

In a HTML/HubL or CSS file, you can use the following tokens to access the primary brand color:

*   `{{brand_settings.primaryColor}}`
*   `{{brand_settings.colors[0]}}`![branding-color-primary-color](https://developers.hubspot.com/hs-fs/hubfs/Developer%20Site/assets/images/branding-inheritance/branding-color-primary-color.jpg?width=403&name=branding-color-primary-color.jpg)

All additional colors can be accessed with `{{brand_settings.colors[1-19]}}`. For example, if there are four brand colors, you can access the third one with `{{brand_settings.colors[2]}}`. ![branding-color-additional-colors](https://developers.hubspot.com/hs-fs/hubfs/Developer%20Site/assets/images/branding-inheritance/branding-color-additional-colors.jpg?width=417&name=branding-color-additional-colors.jpg)

You can access the hex code of the color directly by including a `hex` filter in the token. For example: `{{brand_settings.PrimaryColor.hex}}`.

To include brand settings colors in a theme or module's `fields.json` file, use the following format: 

//Example of using the primary color in within a theme's // field.json file { "name": "branding\_color", "label": "branding\_color", "type": "color", "default": { "color": "#26ff55", "opacity": 60 }, "inherited\_value": { "property\_value\_paths": { "color": "brand\_settings.primaryColor" } } }

There are times when accounts may not have any additional colors configured in its brand settings. If your code is referencing an inherited color that does not exist in brand settings (ex: `brand_settings.colors[3]`), the `default` property value will be used as a fallback. If there is no default property color set, the primary color from your brand setting will be used as a fallback instead (`brand_settings.primaryColor`).

### Logos[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance#logos)

Brand logos can be accessed within a module's `fields.json` file, and within HTML/HubL and CSS files.

You can use the following tokens to access the primary logo set within brand settings:

*   `{{brand_settings.primaryLogo}}`
*   `{{brand_settings.logos[0]}}`

![brand-settings-logo0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/brand-settings-logo0.png?width=958&name=brand-settings-logo0.png)

All additional logos can be accessed by using `{{brand_settings.logos[1-19]}}`.

In addition, you can access the following logo attributes:

*   **Logo URL:** `{{brand_settings.primaryLogo.link}}`
*   **Logo alt text:** `{{brand_settings.primaryLogo.alt}}`
*   **Logo height:** `{{brand_settings.primaryLogo.height}}`
*   **Logo width:** `{{brand_settings.primaryLogo.width}}`
*   **Link to the logo's image:** `{{brand_settings.primaryLogo.src}}`

### Favicons[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance#favicons)

Brand favicons can be accessed only within HTML/HubL and CSS files.

You can use the following tokens to access the primary logo set within brand settings:

*   `{{brand_settings.primaryFavicon}}`
*   `{{brand_settings.favicons[0]}}`

![brand-settings-favicon0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/brand-settings-favicon0.png?width=954&name=brand-settings-favicon0.png)

All additional favicons can be accessed by using `{{brand_settings.favicons[1-19]}}`.

You can access the URL of the logo directly by including an `src` filter. For example: `{{brand_settings.primaryFavicon.src}}`.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/branding-settings-inheritance#page-feedback)
----------------------------------------------------------------------------------------------------------------------------------------------

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