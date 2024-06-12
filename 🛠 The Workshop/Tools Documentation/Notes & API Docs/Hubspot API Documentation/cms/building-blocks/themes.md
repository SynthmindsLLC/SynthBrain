---
title: "Themes overview"
description: "A theme is a portable and contained collection of developer assets designed to enable a flexible content editing experience. You can build themes locally using the HubSpot CLI, and they are also portable between environments and accounts. For more information on getting started with local development, view the HubSpot Academy video below."
type: "concept"
tags:
- "Developer Assets"
- "Content Editing Experience"
- "Local Development"
relationships:
- "#related_to [[HubSpot CLI]]"
- "#enables [[Flexible Content Creation]]"
last_updated: "2024-01-04"
---

Themes overview


===================

Last updated: January 4, 2024

A theme is a portable and contained collection of developer assets designed to enable a flexible content editing experience.  You can [build themes locally using the HubSpot CLI](/docs/cms/guides/getting-started-with-local-development) using the tools, technologies, and workflows that you prefer. Themes and all of their files are also portable between environments and accounts. For a video walkthrough of getting started developing themes, view the HubSpot Academy video below:

![](https://play.vidyard.com/9bGj5nULvUK2fcjX2fZxpz.jpg)

[View in HubSpot Academy](https://app.hubspot.com/academy/l/lessons/673/3414 "View HubSpot Academy lesson")

Themes as a package[](https://developers.hubspot.com/docs/cms/building-blocks/themes#themes-as-a-package)
---------------------------------------------------------------------------------------------------------

Themes being a package cascades throughout the HubSpot app in various places to enable an efficient content creation experience. Developers can use themes to build a design system for content creators to work within. Whatever amount of flexibility, or guardrails can be built into a theme to meet the needs of your business. 

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
            

### Page creation[](https://developers.hubspot.com/docs/cms/building-blocks/themes#page-creation)

When content creators start building new pages, they are prompted to start by selecting which theme they are building a page from, followed by selecting which template within the theme to use.

![Theme selection inside of HubSpot](https://developers.hubspot.com/hs-fs/hubfs/theme%20selection.gif?width=1240&name=theme%20selection.gif)The theme preview image, as well as other configurations for a theme, are set in the [theme.json file](#theme-json). 

### Theme fields[](https://developers.hubspot.com/docs/cms/building-blocks/themes#theme-fields)

Themes allow developers to create a set of [Theme Fields](#fields-json), similar to Module Fields, which allow content creators to tweak various knobs and dials designed by a developer to allow global stylistic control over a website without having to edit CSS. Developers [use HubL to access the values of Theme Fields](#using-theme-field-values) throughout their CSS. Content creators use the Theme Editor to modify Theme Fields, preview those changes against existing templates within a Theme, and publish their changes.

![themes](https://developers.hubspot.com/hs-fs/hubfs/themes.gif?width=1000&name=themes.gif)

Theme fields are dictated by the [fields.json file of a theme](#fields-json). 

When editing a theme in [test mode](/docs/cms/building-blocks/themes#test-mode), you can also copy the theme's settings JSON. This allows you to paste any updates into the theme's local `fields.json` file.![copy-theme-settings-test-mode](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/copy-theme-settings-test-mode.png?width=451&name=copy-theme-settings-test-mode.png) 

### Theme modules[](https://developers.hubspot.com/docs/cms/building-blocks/themes#theme-modules)

The modules within a theme should be designed specifically for use within templates in that theme. The content editor will emphasize these theme modules, making it quick and easy for content creators to add modules to the pages they are building that are designed to work well in the context of that page. Default modules and the rest of the modules in your HubSpot account will still be available.

![Theme modules inside of a theme](https://developers.hubspot.com/hs-fs/hubfs/theme%20modules.png?width=3132&name=theme%20modules.png)

When developing a theme, you can [hide modules and sections from the page editor](/docs/cms/building-blocks/themes/hide-modules-and-sections) to create a more streamlined content creation experience.

Theme file structure[](https://developers.hubspot.com/docs/cms/building-blocks/themes#theme-file-structure)
-----------------------------------------------------------------------------------------------------------

A theme is a single directory of files. You can include HTML, CSS, and Javascript files, modules and additional files that can be organized in any manner within subdirectories of the parent theme folder. Two JSON files are necessary to build a theme: `theme.json` and `fields.json`. These files should be included at the root theme folder.

To start from an example, see the [HubSpot CMS Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate).

![theme file structure](https://designers.hubspot.com/hs-fs/hubfs/theme%20file%20structure.png?width=599&height=452&name=theme%20file%20structure.png)

At this time .json files can only be created and uploaded to a HubSpot account through the [local development tools](/docs/cms/guides/getting-started-with-local-development).

### theme.json[](https://developers.hubspot.com/docs/cms/building-blocks/themes#theme-json)

The `theme.json` file contains the meta-information for your theme directory, such as the themes readable label, its preview screenshot and various configurations for how the theme should behave. Your `theme.json` file will look similar to the following:

// theme.json { "label": "Cool Theme", "preview\_path": "./templates/home-page.html", "screenshot\_path":"./images/templates/homepage.jpg", "enable\_domain\_stylesheets": false, "version":"1.0", "author":{ "name":"Jon McLaren", "email":"noreply@hubspot.com", "url":"https://theme-provider.com/" }, "documentation\_url":"https://theme-provider.com/cool-theme/documentation", "license":"./license.txt", "example\_url":"https://theme-provider.com/cool-theme/demo", "is\_available\_for\_new\_content":true }

theme.json
| Parameter | Type | Description |
| --- | --- | --- |
| 
`label`

 | String | 

The readable label of the theme, used in various places the theme is shown throughout the HubSpot app, like the template selection screen and the theme editor. 

 |
| 

`preview_path`

 | String | 

A relative path to a template file in the theme which should be the default template, used when previewing a theme in the theme editor. 

 |
| 

`screenshot_path`

 | String | 

A relative path to an image file that is used to give a snapshot of what the theme looks like in various places theme selection occurs, such as in the template selection screen. 

 |
| 

`enable_domain_stylesheets`

 | Boolean | 

Enabling or disabling stylesheets attached to domains in Website Settings getting included on templates within the theme. The default value is `false`.

 |
| 

`version`

 | String | 

Integer version number supporting `.` versions.

 |
| 

`Author`

 | object | 

Object to provide information about yourself as the theme provider.

`name`

The provider's name.

`email`

The provider's support email address.

`url`

The provider's website.



 |
| 

`documentation_url`

 | String | 

The theme documentation link.

 |
| 

`example_url`

 | String | 

The theme live example link.

 |
| 

`license`

 | String | 

A valid [SPDX Identifier](https://spdx.org/licenses/) or the relative path to the license within your theme.

This license dictates what use and modification is permitted by the creator of the theme. Useful when submitting to the marketplace.

 |
| 

`is_available_for_new_content`

 | Boolean | 

Boolean that determines if a theme shows up in the content creator page for selection. The default value is `true`.

 |

### fields.json[](https://developers.hubspot.com/docs/cms/building-blocks/themes#fields-json)

The `fields.json` file controls the available fields and field groups in the theme editor, including [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields). The fields you include will depend on how much control you want content creators to have in the page editor. The number of fields available for themes is more limited than for modules, as theme fields are best for styling options, while [global content](/docs/cms/building-blocks/global-content) is better for theme content.

For example, rather than adding a text field to the theme's `field.json` for your site's tagline, it should add it as a global module so that content creators can update the tagline from the page editor rather than the theme editor.

The fields that are available for use in themes are:

*   [Boolean](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#boolean)
*   [Border](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#border)
*   [Choice](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#choice)
*   [Color](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#color)
*   [Font](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#font)
*   [Image](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#image)
*   [Number](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#number)
*   [Spacing](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#spacing)

For comprehensive documentation on the possible options for theme fields, see the [module and theme fields documentation](/docs/cms/building-blocks/module-theme-fields). 

#### Using theme field values[](https://developers.hubspot.com/docs/cms/building-blocks/themes#using-theme-field-values)

To access field values, use dot notation and prefix the path to the value in `fields.json` with theme. You can use a themes fields value in your stylesheets using syntax like {{ theme.path.to.value }}. For example, the font field outlined below:

// fields.json \[{ "type": "group", "name": "typography", "label": "Typography", "children": \[ { "type": "font", "name": "h1\_font", "label": "Heading 1", "load\_external\_fonts": true, "default": { "color": "#000", "font": "Merriweather", "font\_set": "GOOGLE", "variant": "700", "size": "48" } } \] }\]

Would be referenced in CSS with:

h1 { font-size: {{ theme.typography.h1\_font.size }}px; font-family: {{ theme.typography.h1\_font.font }}; color: {{ theme.typography.h1\_font.color }}; text-decoration: {{ theme.typography.h1\_font.styles.text-decoration }}; font-style: {{ theme.typography.h1\_font.styles.font-style }}; font-weight: {{ theme.typography.h1\_font.styles.font-weight }}; }

Previewing themes[](https://developers.hubspot.com/docs/cms/building-blocks/themes#previewing-themes)
-----------------------------------------------------------------------------------------------------

For developers sometimes you need to be able to test out that your theme fields are working properly but don't want to impact real pages. That's where theme test mode comes in.

### Test mode[](https://developers.hubspot.com/docs/cms/building-blocks/themes#test-mode)

Test mode gives you a safe environment to be able to play with your theme's fields and ensure they are working as you expect. The interface looks exactly like the [theme preview/editor that content creators can see](https://knowledge.hubspot.com/website-pages/edit-your-global-theme-settings#edit-theme-settings), however you can rest assured that you are not changing your actual website's settings. To protect against accidental theme setting updates, publishing is blocked in test mode. You can tell if you are in test mode as `?testmode=true` appears in your address bar, and a test mode icon will display in the header of the theme editor.

![Theme Test/Preview Mode](https://developers.hubspot.com/hubfs/theme-test-mode.png "Theme Test/Preview Mode")

There are two ways to enable test mode:

*   To activate test mode from the design manager:
    *   In the design manager, select your **theme** in the finder.
    *   At the top of the left sidebar, click the **Preview** button.  
        ![copy-theme-settings-test-mode-design-manager (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/copy-theme-settings-test-mode-design-manager%20(1).png?width=306&name=copy-theme-settings-test-mode-design-manager%20(1).png)

*   To activate test mode from the page editor:
    *   In the page editor, click the **Design** tab in the left sidebar, then click **Edit theme settings**.  
        ![page-editor-edit-theme](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/page-editor-edit-theme.png?width=369&name=page-editor-edit-theme.png)
    *   Add `?testmode=true` to the URL, then hit **enter**. You'll then be in test mode.

 Another method is to open your theme settings from within the page editor. Then once inside add the query parameter `?testmode=true` to the URL in your address bar.

Related resources[](https://developers.hubspot.com/docs/cms/building-blocks/themes#related-resources)
-----------------------------------------------------------------------------------------------------

*   [Getting started with themes](/docs/cms/guides/getting-started-with-themes)
*   [How to add theme capabilities to existing sites](/docs/cms/guides/add-theme-features-to-existing-sites)
*   [HubSpot theme boilerplate](/docs/cms/building-blocks/themes/hubspot-cms-boilerplate)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/themes#page-feedback)
---------------------------------------------------------------------------------------------------

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