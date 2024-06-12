---
title: "CMS Module Files"
description: "Overview of module files used in HubSpot CMS."
type: "concept"
tags:
- "CMS"
- "HubSpot"
- "Module Files"
- "Front-end Development"
- "Web Development"
relationships:
- "#explains [[HTML]] [[HubL]] [[CSS]] [[JavaScript]]"
- "#contributes_to [[CMS Hub Website]]"
- "#related_to [[Module Field Values]] [[Module Customization]]"
---

Module files


================

Last updated: December 14, 2021

When building a module for pages, blogs, and [quotes](/docs/cms/building-blocks/templates/quotes), the module will contain three front-end related files that control the content, styling, and functionality of the module:

*   module.html
*   module.css
*   module.js

Email modules don't support module.css and module.js. This is because email clients don't support JavaScript and support for linked CSS files is limited.

These files will always be rendered to the page when an instance of the module is on the page.

When a page includes multiple instances of the same module, HubSpot will only load `module.css` and `module.js` from that module once. By default, `module.css` and `module.js` do not load asynchronously, but you can change this by including [css\_render\_options and js\_render\_options](https://developers.hubspot.com/docs/cms/building-blocks/modules/configuration) in the module’s meta.json.

Modules can be built within the design manager or locally using [the HubSpot CLI](/docs/cms/developer-reference/local-development-cli). In the design manager, module files are displayed in a multi-pane editor.

![cms-dev-custom-module1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/cms-dev-custom-module1.png?width=1040&name=cms-dev-custom-module1.png)When viewing a module locally, the files are contained within module-name.module folders.

![cms-dev-custom-module0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/cms-dev-custom-module0.png?width=796&name=cms-dev-custom-module0.png)Whether you use the design manager or CLI to create and manage modules is based on your team’s preferences. See [creating an efficient developer workflow](https://designers.hubspot.com/tutorials/creating-an-efficient-development-workflow) for recommendations.

HTML + HubL (module.html)[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#html-hubl-module-html-)
-------------------------------------------------------------------------------------------------------------------------

The module.html file is intended for HTML and HubL. In general, wherever a module is placed in the page editor or template file determines where the contents of the module.html file are rendered. 

This file acts like a [HubL include](https://developers.hubspot.com/docs/cms/hubl#including-files-in-files) in the page wherever the module is placed. The module.html file [can access the module's field values through HubL](https://developers.hubspot.com/docs/cms/building-blocks/modules#using-module-field-data-to-render-html).

CSS (module.css)[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#css-module-css-)
---------------------------------------------------------------------------------------------------------

Use the `module.css` file to add CSS to a module.

In general, `module.css` supports a very limited subset of HubL. However, you can use [`module_asset_url("my-image.png")`](/docs/cms/hubl/functions#module-asset-url) for images added as module linked assets. This enables linking assets such as images, packaged with the module itself. For example:

.testimonial-module\_\_wrapper{ background: url("{{ module\_asset\_url("bg-pattern.png") }}"); background-repeat:repeat; min-height:200px; width:100%; display:block; }

Below, learn how to set up a module's CSS to change dynamically based on the module's fields.

### Styling based on module field values[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#styling-based-on-module-field-values)

There are a few ways you can influence the styling of your module based on the module’s fields. Choose the way that works best for your specific use case.

*   [CSS Classes](#css-classes)
*   [Require\_css block](#require-css-block)
*   [Inline styles](#inline-styles)

#### CSS Classes[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#css-classes)

To set up predefined styling for the module with the option for editors to select from those options, you can add a module field to set classes in your `module.htm`l file which correspond to CSS classes in your `module.css` file.

For example, you may have an image and text module. You want content creators to be able to position the image to the right or left of the text based on a choice field. To do this, you could set your `module.html` and `module.css` files as follows:

<!-- module.html --> <section class="img-text\_\_wrapper img-text--{{ module.positioning }}" aria-label="{{ module.heading }}"> {# module.position is a choice field with two values "img-left" or "img-right". This dictates the order they appear on desktop. Controlled by CSS #} <div class="img-text\_\_img"> <img src="{{ module.image.src }}" alt="{{ module.image.alt }}"> </div> <div class="img-text\_\_text"> <h2> {% inline\_text field="heading" value="{{ module.heading }}" %} </h2> {% inline\_rich\_text field="text" value="{{ module.text }}" %} </div> </section>

/\* module.css \*/ /\* CSS that makes the image show adjacent to the text, and positioned based on the positioning field.\*/ /\* The media query ensures that on mobile the image will always appear above the text for visual consistency. \*/ @media(min-width:768px){ .img-text\_\_wrapper{ display:flex; align-items:row; } .img-text\_\_img,.img-text\_\_text{ flex:1; padding:10px; } .img-text--img-right{ flex-direction:row-reverse; } }

### require\_css block[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#require-css-block)

When you need to give content creators direct control over specific properties and when classes are not ideal, style tags with `require_css` blocks are the best option. 

To give content creators direct control over specific properties without using classes, you can instead add styling to the `module.html` file within `require_css` tags. For example:

<div class="img\_\_wrapper"> {% if module.image.src %} {% set sizeAttrs = 'width="{{ module.image.width }}" height="{{ module.image.height }}"' %} {% if module.image.size\_type == 'auto' %} {% set sizeAttrs = 'style="max-width: 100%; height: auto;"' %} {% elif module.image.size\_type == 'auto\_custom\_max' %} {% set sizeAttrs = 'width="100%" height="auto" style="max-width: {{ module.image.max\_width }}px; max-height: {{ module.image.max\_height }}px"' %} {% endif %} <img src="{{ module.image.src }}" alt="{{ module.image.alt }}" {{ sizeAttrs }}> {% endif %} </div> {% require\_css %} <style> img { border-width:{{ module.border\_width }}px; border-color:rgba({{ module.border\_color.color|convert\_rgb}},{{ module.border\_color.opacity/100 }}); border-style: solid; } </style> {% end\_require\_css %}

Because `module.html` can render HubL, you can use module field values as CSS variables. When a content creator updates the field in the page editor, the CSS will update to match. These block move the `<style>` tags into the `<head>` of your page within the `standard_header_includes` statement.

You can also set the CSS to be scoped to only the module instance by wrapping the CSS with `scope_css` tags. For example, you could update the above module code as follows:

<div class="img\_\_wrapper"> {% if module.image.src %} {% set sizeAttrs = 'width="{{ module.image.width }}" height="{{ module.image.height }}"' %} {% if module.image.size\_type == 'auto' %} {% set sizeAttrs = 'style="max-width: 100%; height: auto;"' %} {% elif module.image.size\_type == 'auto\_custom\_max' %} {% set sizeAttrs = 'width="100%" height="auto" style="max-width: {{ module.image.max\_width }}px; max-height: {{ module.image.max\_height }}px"' %} {% endif %} <img src="{{ module.image.src }}" alt="{{ module.image.alt }}" {{ sizeAttrs }}> {% endif %} </div> {% require\_css %} <style> {% scope\_css %} img { border-width:{{ module.border\_width }}px; border-color:rgba({{ module.border\_color.color|convert\_rgb}},{{ module.border\_color.opacity/100 }}); border-style: solid; } {% end\_scope\_css %} </style> {% end\_require\_css %}

### Add inline styles[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#add-inline-styles)

When you need to give content creators granular control over only a few properties and when classes are not ideal, you can directly add the values to a style attribute in the HTML.

{# Module.html #} <div style="background: rgba({{ module.bg\_color.color|convert\_rgb }},{{ module.bg\_color.opacity/100 }});"> {% inline\_rich\_text field="richtext" value="{{ module.richtext }}" %} </div>

If you have many properties and the code becomes hard to read, consider switching to the `require_css` block method.

### Import specific CSS files[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#import-specific-css-files)

`require_css` is a HubL function that you can add to module.html which tells HubSpot that a particular module or template requires a particular CSS file to display. A link tag pointing to the css file is added to the page's `<head>` inside of the `standard_header_includes`. 

The `require_css` function will only load that CSS file once, regardless of how many times that same file is required by modules and templates on a particular page. This makes it great for situations where styles may be shared across multiple modules, but where adding the CSS directly to the main stylesheets used on every page for your site may not make sense.

`require_css` and linked CSS files fill the same purpose, but `require_css` can be used conditionally based on field values. This prevents loading unnecessary code.

<!-- module.html --> {{ require\_css(get\_asset\_url("/modules/shared\_layout\_styles.css")) }}

JavaScript (module.js)[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#javascript-module-js-)
---------------------------------------------------------------------------------------------------------------------

Use the `module.js` file to add JavaScript to a module.

Like the `module.css` file, the `module.js` file does not support HubL.

### Scripting based on field values[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#scripting-based-on-field-values)

There are a few ways you can build modules, where the JavaScript acts differently based on field values. Understanding which method to use and when can mean performance benefits on every page the module is used. 

For example, you have a custom image module, you want to give content creators the ability to make it so the image can open in a lightbox. Content creators only want that for specific images, and not all instances of the module.

### Data attributes[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#data-attributes)

Data attributes are HTML 5 standard custom attributes that developers add to elements. Just as all elements support `class="yourClassName"`, all elements support `data-your-attribute="yourValue"`.

<!-- module.html--> <div class="img-module img-module\_\_wrapper" data-lightbox="{{ module.is\_lightbox\_enabled }}" data-caption="above"> <!-- module.is\_lightbox\_enabled is a boolean field, module.caption\_position is a choice field. --> {% if module.image.src %} {% set sizeAttrs = 'width="{{ module.image.width }}" height="{{ module.image.height }}"' %} {% if module.image.size\_type == 'auto' %} {% set sizeAttrs = 'style="max-width: 100%; height: auto;"' %} {% elif module.image.size\_type == 'auto\_custom\_max' %} {% set sizeAttrs = 'width="100%" height="auto" style="max-width: {{ module.image.max\_width }}px; max-height: {{ module.image.max\_height }}px"' %} {% endif %} <img src="{{ module.image.src }}" alt="{{ module.image.alt }}" {{ sizeAttrs }}> {% endif %} </div>

You can use data attributes to pass the field values of your module instances to be handled by your module.js file.

To use the values in your module.js file, you will need to loop through all of the instances of your module. Adding a module-specific class name to the outermost wrapper element of your module will give you a target to use, so that you can loop through each of your module instances.

// module.js let imgModules = document.getElementsByClassName('img-module'); Array.from(imgModules).forEach(function(element) { // loop through each of the instances of the module // set data attributes to variables to make it easy to work with let isLightboxEnabled = element.dataset.lightbox; let captionStyle = element.dataset.caption; if(isLightboxEnabled){ element.addEventListener('click', function(){ showLightbox(captionStyle); // Execute your code for the action you want to take, you can pass your data attributes into functions from libraries. }); } });

The data attributes will allow you to retrieve the field values for each module instance in your module.js. 

### require\_js block[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#require-js-block)

In advanced situations, perhaps when using a JavaScript templating library or a reactive framework like Vue.js or React.js, you may prefer outputting just the data, while the framework handles rendering.

In this case, use a script tag surrounded by a [`require_js`](/docs/cms/hubl/functions#require-js) block to provide variables you can access from your templating script.

{% require\_js %} <script> let myArray = \[ {%- for item in module.repeating\_text\_field -%}"{{ item }}",{%- endfor -%} \]; </script> {% end\_require\_js %}

This technique can be useful for supplying advanced applications with an initial set of data from which to render. This eliminates an initial JavaScript call to retrieve data.

### require\_js[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#require-js)

`[require_js](/docs/cms/hubl/functions#require-js)` is a HubL function that tells HubSpot that a particular module or template requires a particular JavaScript file to load properly. The function takes two parameters: the path to the file and the location the file is to be added to ("head" or "footer"). 

In a module `require_js` can only be added to the module.html. The JavaScript file referred to in the `require_js` statement will only be loaded once per page, regardless of how many times it is required by modules and templates within the page. This reduces the number of HTTP requests and prevents duplicate code. 

Some situations where this becomes handy:

*   If you have multiple modules or templates that require the same JavaScript, you can use `require_js` to share that script across modules.
*   If you're working with a JavaScript bundler like webpack, it can be easier to output your js files to one specific location. Using `require_js`, you can associate the JavaScript with your module.

`require_js` and linked javascript files serve the same purpose, but `require_js` can be done conditionally based on field values. This prevents unnecessary code from being loaded. You also have the additional option of loading JavaScript in the head, should you need that.

Since JavaScript is render-blocking , the default location `[require_js](/docs/cms/hubl/functions#require-js)` places JavaScript is the "footer". [Learn more about optimizing for performance.](https://designers.hubspot.com/tutorials/speed)

Related Information[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#related-information)
----------------------------------------------------------------------------------------------------------------

*   [Optimize your CMS Hub site for speed](/docs/cms/guides/speed)
*   [Modules](/docs/cms/building-blocks/modules)
*   [Module fields](/docs/cms/building-blocks/module-theme-fields-overview)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules/files#page-feedback)
----------------------------------------------------------------------------------------------------------

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