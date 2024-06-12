---
title: "Responsive Breakpoints for Themes"
description: "Set responsive breakpoints for themes to optimize styling for mobile and desktop using HubL in dnd\_area tags."
type: "concept"
tags:
- "Web_Design"
- "Themes"
- "HubSpot"
relationships:
- "#part_of [[HubSpot CMS]]"
- "#applies_to [[Drag and Drop Areas]]"
- "#uses [[HubL]]"
- "#prevents [[Non-Responsive Websites]]"
- "#enables [[Responsive Styling]]"
---

Set responsive breakpoints for themes


=========================================

Last updated: November 28, 2022

While developing a theme, you can define responsive breakpoints to optimize styling for mobile and desktop. Below, learn more about how to set breakpoints and define responsive styles in [dnd\_area tags](/docs/cms/hubl/tags/dnd-areas) using HubL.

You can use these breakpoints to define the following styling for specific asset types:

*   `dnd_section`, `dnd_column`, and `dnd_row` support margin and padding across breakpoints.
*   Default modules in a `dnd_area` support margin, padding, and visibility.
*   Default modules outside a `dnd_area` support only margin and padding.
*   Custom modules in a `dnd_area` support visibility.
*   Custom modules outside a `dnd_area` don't support breakpoint based customizations.

In addition, only two breakpoints are possible at this time: `mobile` and `default` (optional for desktop).

Define breakpoints in a theme[](https://developers.hubspot.com/docs/cms/building-blocks/themes/responsive-breakpoints#define-breakpoints-in-a-theme)
----------------------------------------------------------------------------------------------------------------------------------------------------

You can define a set of breakpoints in your theme by adding the `responsive_breakpoints` object to your `themes.json` file. Inside of this object is a set of key/value pairs that will contain information about your breakpoint.

JSON

Copy all

    // themes.json
    {
      "label": "My Theme",
      "preview_path": "./path/to/preview.html",
      "screenshot_path": "./images/template-previews/home.png",
      "responsive_breakpoints": [
        {
          "name": "mobile",
          "mediaQuery": "@media (max-width: 767px)",
          "previewWidth": {
            "value": 520
          }
        }
      ]
    }

Below are the properties you can include within `responsive_breakpoints`:

Use this table to describe parameters / fields
| Key | Type | Description |
| --- | --- | --- |
| 
`name`

 | String | 

The name of the breakpoint. At this time only `"mobile"` is available for use.

 |
| 

`mediaQuery`

 | String | 

A media query string for the renderer/editors to use when generating responsive CSS. 

e.g. `"@media (max-width: 767px)"`

 |
| 

`previewWidth`

 | Key/Value Pair | 

To give clues to the editor as to what size we should show our preview iframe at.

e.g. `{"value": 520}`

 |

Define responsive styles in dnd\_area tags[](https://developers.hubspot.com/docs/cms/building-blocks/themes/responsive-breakpoints#define-responsive-styles-in-dnd-area-tags)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While building [drag and drop areas](/docs/cms/hubl/tags/dnd-areas), you can including responsive styling  using HubL. This functionality currently works in the `dnd_section`, `dnd_row`, and `dnd_column` tags.

Take the following example of a [dnd\_section](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#drag-and-drop-section-code-dnd-section-code-):

{% dnd\_section padding={ 'top': 100, 'bottom': 100 } %} {% end\_dnd\_section %}

To change the padding for the mobile breakpoint, you can include values for both the `default` (desktop view) and `mobile` breakpoints as illustrated below.

{% dnd\_section padding={ 'default': { 'top': 100, 'bottom': 100 }, 'mobile': { 'top': 20, 'bottom': 20 } } %} {% end\_dnd\_section %}

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/themes/responsive-breakpoints#page-feedback)
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