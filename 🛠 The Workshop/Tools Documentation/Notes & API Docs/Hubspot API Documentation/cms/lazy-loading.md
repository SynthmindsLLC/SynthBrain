Lazy loading assets for performance


=======================================

Last updated: November 30, 2022

Lazy loading assets allows you to defer the loading of the assets until the time when they are actually needed. On the web, this often means downloading the designated content only once the user has gotten sufficiently close to where in the HTML document the asset displays. This technique is one of many suggested for [optimizing page performance](/docs/cms/guides/speed).

Lazy loading images[](https://developers.hubspot.com/docs/cms/lazy-loading#lazy-loading-images)
-----------------------------------------------------------------------------------------------

Lazy loading options are available for the [image and logo fields](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#image) in custom modules for use in HubL tags and also available in the [default image module.](https://knowledge.hubspot.com/cos-general/use-default-modules-in-your-template#image)

When building custom modules, you have the option to enable [browser built-in lazy loading](https://web.dev/browser-level-image-lazy-loading/) on image fields. When enabled, you can choose whether to show or hide controls to the content editor enabling them to change the loading behavior in the page editor.

### Browser Compatibility[](https://developers.hubspot.com/docs/cms/lazy-loading#browser-compatibility)

Lazy loading of images via the `loading` attribute is supported by most of the popular Chromium-powered browsers (Chrome, Edge, Opera) and Firefox. To learn more about what browsers are supported you can visit [caniuse.com](https://caniuse.com/#feat=loading-lazy-attr). Browsers that do not support the `loading` attribute will simply ignore it without side-effects.

### Add lazy loading to Image fields using the CLI[](https://developers.hubspot.com/docs/cms/lazy-loading#add-lazy-loading-to-image-fields-using-the-cli)

To enable lazy loading of images while building with the CMS CLI, add the `show_loading` and `loading` keys to the [image](/docs/cms/building-blocks/module-theme-fields#image) or [logo](/docs/cms/building-blocks/module-theme-fields#logo) field in the module's `fields.json` file.

// fields.json file { "id" : "357bacfa-2bb8-e996-4589-f55e10d4f1d4", "name" : "image\_field", "label" : "Image", "required" : false, "locked" : false, "responsive" : true, "resizable" : true, "show\_loading" : false, "type" : "image", "default" : { "size\_type" : "auto", "src" : "", "alt" : null, "loading" : "disabled" } }

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`show_loading`

 | Boolean | 

Controls showing/hiding lazy load controls to the content editor.

 | `False` |
| 

`loading`

 | String | 

Determines whether to use lazy loading. Options include: `"disabled"` or `"lazy"`

 | `"disabled"` |

You can then reference these variables in your `module.html` file using the following syntax:

{% set loadingAttr = module.image\_field.loading != 'disabled' ? 'loading="{{ module.image\_field.loading }}"' : '' %} <img src="{{ module.image\_field.src }}" alt="{{ module.image\_field.alt }}" {{ loadingAttr }}>

### Add lazy loading to image and logo fields in HubSpot[](https://developers.hubspot.com/docs/cms/lazy-loading#add-lazy-loading-to-image-and-logo-fields-in-hubspot)

To enable lazy loading, add an image or logo field to your custom module, then navigate to the **Content options** section in the [Inspector pane](https://knowledge.hubspot.com/cos-general/a-quick-tour-of-the-design-manager#inspector). Then use the **Image loading** and **Available loading options** dropdown menus to configure the image loading behavior.

![Lazy loading controls in the Design Manager](https://developers.hubspot.com/hubfs/Developer%20Site/assets/images/lazy-loading/lazy-loading-image-controls-dm.png "Lazy loading controls in the Design Manager")

#### Image loading[](https://developers.hubspot.com/docs/cms/lazy-loading#image-loading)

The **Image loading** option will set the value of the `loading` attribute in the browser. Options for this include "Default" (default option) which is the default browser loading behavior for the asset. When enabling lazy loading, the image will load once the image reaches a certain distance from the viewport as defined in the [distance-from-viewport threshold](https://web.dev/browser-level-image-lazy-loading/#distance-from-viewport-thresholds).

#### Available loading options[](https://developers.hubspot.com/docs/cms/lazy-loading#available-loading-options)

The **Available loading options** will determine if content editors will be able to see and set the **Image loading** option while inside of the page, global, and theme content editor panes. Options for this include _Do Not Show Controls_ (default) or _Show all controls_.  Below is a sample of what the page editor would look like with _Show all controls_ selected:

![Lazy loading controls on the page editor](https://developers.hubspot.com/hs-fs/hubfs/Developer%20Site/assets/images/lazy-loading/lazy-loading-image-controls-page-editor.png?width=450&height=668&name=lazy-loading-image-controls-page-editor.png "Lazy loading controls on the page editor")

You can then reference these variables in the `module.html` file using the following syntax:

{% set loadingAttr = module.image\_field.loading != 'disabled' ? 'loading="{{ module.image\_field.loading }}"' : '' %} <img src="{{ module.image\_field.src }}" alt="{{ module.image\_field.alt }}" {{ loadingAttr }}>

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/lazy-loading#page-feedback)
-----------------------------------------------------------------------------------------

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