---
title: "Hide Modules and Sections"
description: "Overview of module and section visibility settings in HubSpot themes and templates."
type: "concept"
tags:
- "Themes"
- "Templates"
- "Modules"
- "Sections"
- "Content_Management"
relationships:
- "#applies_to [[Themes]], [[Templates]]"
- "#related_to [[Content_Editing]]"
- "#prevents [[Users]] from accessing certain [[Modules]] and [[Sections]]"
---

Hide modules and sections from the editor


=============================================

When developing a theme, you can set which modules and sections appear in the editor. This enables you to curate the list of modules and sections available to content creators when building pages, blogs, and global content, rather than having all modules and sections appear for all content types. Using this feature, you can also hide [HubSpot default modules](/docs/cms/building-blocks/modules/default-modules) in favor of your own versions.

You can hide modules and sections in the following ways:

*   **Within themes:** you can hide default modules, but not custom modules. Similarly, you cannot hide custom sections in a theme. To exclude a custom module or section from a theme, you should instead delete the module or section from the theme.
*   **Within templates:** you can hide default modules, custom modules, and sections.

When hiding modules and sections, keep the following in mind:

*   When hiding HubSpot default modules in a template, ensure that the module is wrapped in single quotes (`'`). For example, `'@hubSpot/follow_me'`. This complies with YAML, which template annotations are based on.
*   You must use the relative path when specifying a hidden module. Using an absolute path will result in the module not being hidden. 

Hide default modules in a theme[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hide-modules-and-sections#hide-default-modules-in-a-theme)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

To hide all default modules, set `hide_all_default_modules: true"` in the `theme.json` file

To hide specific default modules in a theme, you'll need to add a list of hidden modules to a `hidden_modules` array in the `theme.json` file.

For example, if you wanted to hide HubSpot's default button and form modules from a theme, your code would look like the following:

// example theme.json { "label": "CMS Theme Boilerplate", "preview\_path": "./templates/home.html", "screenshot\_path": "./images/template-previews/home.png", "enable\_domain\_stylesheets": false, "license": "./license.txt", "responsive\_breakpoints": \[ { "name": "mobile", "mediaQuery": "@media (max-width: 767px)", "previewWidth": {"value": 477} } \], "hidden\_modules": \[ "@hubspot/button", "@hubspot/form" \] }

To hide all default modules, set `_hide_all_default_modules_: true"`  in _`theme.json`_.

Hide modules and sections in a template[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hide-modules-and-sections#hide-modules-and-sections-in-a-template)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To hide modules and sections in a specific template, you'll need to add a list of `hiddenModules` and `hiddenSections` in the template annotations. For example:

// example template file <!-- templateType: page isAvailableForNewContent: true label: Ticket listing screenshotPath: ../images/template-previews/ticket-listing.png hiddenModules: - '@hubSpot/follow\_me' - ../modules/form hiddenSections: - ../sections/card -->

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hide-modules-and-sections#page-feedback)
-----------------------------------------------------------------------------------------------------------------------------

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