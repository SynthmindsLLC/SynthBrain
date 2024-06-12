---
title: "HubSpot CMS Boilerplate"
description: "The HubSpot CMS Boilerplate provides developers with a clean, performant, and easy-to-modify website that saves them a significant amount of developmental time."
type: "code"
tags:
- "HubSpot"
- "CMS"
- "Boilerplate"
- "Web Development"
relationships:
- "#related_to [[Optimizing CMS Hub Site Performance]], [[Accessibility on CMS Hub]]"
- "#recommended_for [[HubSpot CMS Developers]]"
- "#used_by [[Developers]]"
- "#requires [[jQuery]]"
- "#derived_from [[Best Practices]]"
- "#influences [[Speed]], [[Performance]]", [[Development Time]]"
- "#includes [[Header]], [[Footer]]"
- "#contains [[CSS]], [[JS]], [[Assets]]"
- "#part_of [[HubSpot CMS]], [[Design Manager]]"
language: "version: "
---

The HubSpot CMS Boilerplate


===============================

Last updated: January 10, 2023

[The HubSpot CMS Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate) serves as a starting point for helping developers get a website up and running quickly on the HubSpot CMS while illustrating best practices developers can use when building on the HubSpot CMS Platform. The boilerplate is an open-source GitHub project where all are welcome to suggest changes and fork for their own use. If you are new to the HubSpot CMS, and want to get started on a new project based off of the boilerplate, follow the [quick start guide to developing on the HubSpot CMS](/docs/cms/guides/getting-started).

  
  

Why should developers use the HubSpot CMS Boilerplate?[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate#why-should-developers-use-the-hubspot-cms-boilerplate-)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The HubSpot CMS Boilerplate is built and actively maintained by HubSpot. When building the boilerplate, we incorporated best practices that were influenced by how developers created the best website building experience and then applied those to building a website on the HubSpot CMS. This provides developers with a clean, [performant](/docs/cms/guides/speed), and ready to modify website that saves developers a significant amount of developmental time. The boilerplate also provides comprehensive CSS for HubSpot related assets such as forms, menu modules, base classes and more. You can view a live demo of the boilerplate in action by visiting [https://boilerplate.hubspotcms.com/](https://boilerplate.hubspotcms.com/)

How to get started using the HubSpot CMS Boilerplate[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate#how-to-get-started-using-the-hubspot-cms-boilerplate)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To get started with using the boilerplate in your local development environment, simply follow our [Getting Started Developing Websites on the HubSpot CMS guide.](/docs/cms/guides/getting-started)

HubSpot CMS Boilerplate structure[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate#hubspot-cms-boilerplate-structure)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Developers can work with the boilerplate using [local development tools](/docs/cms/guides/getting-started-with-local-development) or directly inside of the [Design Manager](https://knowledge.hubspot.com/cos-general/get-started-with-the-design-manager). The boilerplate uses relative path references for all of the assets which makes it easy to adapt to whatever your project may be. This also allows for the boilerplate to be completely portable between accounts on the HubSpot Platform. Below is a screenshot of the folder structure of the boilerplate’s assets. The boilerplate silos its assets into multiple directories for easy identification of where they reside.

![](https://play.vidyard.com/dqjsowJjeD4SdKTh8J6wb5.jpg)

[View in HubSpot Academy](https://app.hubspot.com/academy/l/lessons/673/3415 "View HubSpot Academy lesson")

![Folder Structure of the HubSpot CMS Boilerplate](https://developers.hubspot.com/hubfs/5Cdocs/boilerplate/boilerplate-structure-tree-view-4.png "Folder Structure of the HubSpot CMS Boilerplate")

The HubSpot CMS Boilerplate’s underlying template structure revolves around a [common base layout](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/layouts/base.html), located in the templates > layouts folder, that is then `{% extends %}` tag and referencing the `{% block body %}` block for its main content. A sample of how the extend tag and blocks are being used can be seen in [any of the html files inside of the templates directory.](https://github.com/HubSpot/cms-theme-boilerplate/tree/master/src/templates) Learn more about [blocks and extends](/docs/cms/hubl#blocks-and-extends).

This is a common method of developing on CMS systems where you have a base (sometimes called a main/parent) template that contains all the main common structural pieces of content on your site. These are often items that are inside of the <head> element on your site such as common meta properties (ex: Title and Meta Description), Favicon links, CSS links, and 3rd party scripts

<!doctype html> <html lang="{{ html\_lang }}" {{ html\_lang\_dir }}> <head> <meta charset="utf-8"> <title>{{ page\_meta.html\_title }}</title> {% if site\_settings.favicon\_src %}<link rel="shortcut icon" href="{{ site\_settings.favicon\_src }}" />{% endif %} <meta name="description" content="{{ page\_meta.meta\_description }}"> {{ require\_css(get\_asset\_url("../../css/layout.css")) }} {{ require\_css(get\_asset\_url("../../css/main.css")) }} {{ require\_css("https://fonts.googleapis.com/css?family=Merriweather:400,700|Lato:400,700&display=swap") }} {{ require\_js(get\_asset\_url("../../js/main.js")) }} {{ standard\_header\_includes }} </head> <body> <div class="body-wrapper {{ builtin\_body\_classes }}"> {% block header %} {% global\_partial path="../partials/header.html" %} {% endblock header %} {% block body %} <!-- Nothing to see here --> {% endblock body %} {% global\_partial path="../partials/footer.html" %} </div> {{ standard\_footer\_includes }} </body> </html>

Inside of this base layout, there are also calls to our global header and footer partials. This allows us to be able to keep the code for these partials in their own separate files for modularity and, because they are global partials, can then be easily edited using our [Global Content Editor](/docs/cms/building-blocks/global-content) by your content creators.

For more depth into the assets included in the boilerplate [check out the boilerplate's wiki on GitHub](https://github.com/HubSpot/cms-theme-boilerplate/wiki).

jQuery[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate#jquery)
-------------------------------------------------------------------------------------------------------

**The HubSpot Theme boilerplate doesn't require jQuery in order to function**. For older HubSpot accounts jQuery is loaded by default. Newer HubSpot accounts have jQuery disabled by default.

Historically HubSpot scripts required jQuery to function properly, so the domain-wide setting was there to help ensure compatibility. HubSpot scripts no longer use jQuery. Because JQuery is not required, and there are better ways for developers to include libraries that also work with source control. It is advised to disable the jQuery settings for new websites. 

Be aware if disabling jQuery on a domain that has an existing website - any landing pages or existing web pages you may have could break if they depend on jQuery.  
  
**If you wish to use jQuery on your new website it is recommended that you use the latest version of jQuery.** There are two easy ways to do that:

*   Upload the latest version of jQuery to your developer file system and use [`require_js`](/docs/cms/hubl/functions#require-js) to load it where and when you need it.
*   Use a CDN you trust, and use [`require_js`](/docs/cms/hubl/functions#require-js) to load jQuery where and when you need it.

Related resources[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate#related-resources)
-----------------------------------------------------------------------------------------------------------------------------

*   [Getting started with themes](/docs/cms/guides/getting-started-with-themes)
*   [How to optimize your CMS Hub site for performance](/docs/cms/guides/speed)
*   [Getting started with accessibility](/docs/cms/guides/accessibility)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate#page-feedback)
---------------------------------------------------------------------------------------------------------------------------

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