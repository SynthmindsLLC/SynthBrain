---
title: "Global Content in HubSpot CMS"
description: "Shared content across portions of a website, such as headers, footers, and sidebars. Developers specify global components using partials or modules for easy editing and previewing changes. Learn more about [global content](https://knowledge.hubspot.com/cms-general/use-global-content-across-multiple-templates)."
type: "concept"
tags:
- "HubSpot"
- "CMS"
- "Global Content"
relationships:
- "#related_to [[Website Templates]]"
- "#used_for [[Headers]], [[Footers]], [[Sidebars]]"
- "#part_of [[Content Management System]]"
last_updated: "2023-01-10"
---

Global content


==================

Last updated: January 10, 2023

Global content is content that is shared across portions of a website. Common examples are website headers, footers, and sidebars. As a developer, you'll specify which components should be global by using global partials or by making modules global. HubSpot provides a different editing experience for content editors that makes it easy to edit the global content and preview the changes across pages before publishing. To learn more about how to edit your global content, check out [how to use global content across multiple templates](https://knowledge.hubspot.com/cms-general/use-global-content-across-multiple-templates) on HubSpot Knowledge Base.

![Global content editor](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/global-content/global-content-editor-4.png?width=800&height=452&name=global-content-editor-4.png "Global content editor")

Overview[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#overview)
-------------------------------------------------------------------------------------------

Global content is best used to display the same information across multiple pages. For example, your website's header and footer, such as the header at the top of this page.

![hubspot-developers-header](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hubspot-developers-header.png?width=800&height=101&name=hubspot-developers-header.png)

Below are some additional examples of areas where you can use global content:

*   Secondary navigation for different sections of your website
*   Copyright footers (or sub footers)
*   Blog post sidebars (for showing recent posts, author listings, and more)

Because global content is used in multiple places throughout a website, it is even more crucial to [design and build your global partials and modules for accessibility](/docs/cms/developer-reference/accessibility).

### Global partials vs global modules[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#global-partials-vs-global-modules)

As a developer, you can create global partials and global modules, with a few key differences between them:

*   Global partials are a type of template built using HTML & HubL that can be reused across your entire website. The most common types of partials are website headers, sidebars, and footers.
*   Global modules are modules that are made up of single or multiple pieces of content that can be used across multiple pages on your site. Some common types of global modules can be items such as blog subscribe forms, secondary navigation elements, and calls-to-action.

You should avoid including global modules within global partials, as it can create a negative content editing experience.

All modules and fields inside of your global partials and global modules are easily editable inside of the [global content editor](https://knowledge.hubspot.com/cms-general/use-global-content-across-multiple-templates).

Global partials[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#global-partials)
---------------------------------------------------------------------------------------------------------

### Create a global partial[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#create-a-global-partial)

A global partial is a type of template, which you can create locally through the HubSpot CLI by using the [create command](/docs/cms/developer-reference/local-development-cms-cli#create), as shown below.

hs create template <partial-file-name>

When prompted to pick a type of template, select `global partial`.

This will create your template in the desired directory with the following template annotations included in the HTML file.

<!-- templateType: global\_partial label: Page Header -->

To see a sample of a global content partial, [please reference our boilerplate on GitHub.](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/partials/header.html)

### Add drag and drop areas to global partials[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#add-drag-and-drop-areas-to-global-partials)

You can enable drag and drop content capabilities inside of your global partials by adding in `dnd_area` tags similar to enabling them in page templates. View our [Drag and Drop Area documentation](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas) for more information. 

### Include a global partial in your existing template[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#include-a-global-partial-in-your-existing-template)

To add a global partial into one of your existing templates, use the global\_partial HubL tag while referencing the path to your partial. Below is an example from [the CMS boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/layouts/base.html#L21) using this tag.

{% global\_partial path="../partials/header.html" %}

When global partials are output, they contain a wrapping `<div>` around the global partial. This is used by the page editor to identify that the piece of content is a global partial.

<div data-global-resource-path="cms-theme-boilerplate/templates/partials/header.html"> <!-- Your header.html code is output here --> </div>

**Please note:** do not use `global_partial` within the `<head>` of a template. Doing so would result in invalid HTML.

In most situations where you'd want to use a global partial in the header, it may make more sense to use a global module instead with a [`{%require_head%}`](/docs/cms/hubl/tags#require-head) to insert custom code into the head, and still provide module fields.

Global modules[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#global-modules)
-------------------------------------------------------------------------------------------------------

You can create global modules like any other module using the CLI by running the `hs create` command, as shown below.

hs create module <module\_name>

A global module is differentiated by the global flag in the module's `meta.json` file.

// meta.json file { "css\_assets": \[\], "external\_js": \[\], "global": true, "help\_text": "", "host\_template\_types": \["PAGE"\], "js\_assets": \[\], "other\_assets": \[\], "smart\_type": "NOT\_SMART", "tags": \[\], "is\_available\_for\_new\_content": false }

You can also [create global modules in HubSpot by using the design Manager](https://knowledge.hubspot.com/cos-general/create-and-edit-modules).

Learn more about working with modules in the following related resources:

*   [Modules overview](/docs/cms/building-blocks/modules)
*   [HubSpot's default modules](/docs/cms/building-blocks/modules/default-modules)
*   [Configuring modules](/docs/cms/building-blocks/modules/configuration)
*   [Using modules in templates](/docs/cms/building-blocks/modules/using-modules-in-templates)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/global-content#page-feedback)
-----------------------------------------------------------------------------------------------------------

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