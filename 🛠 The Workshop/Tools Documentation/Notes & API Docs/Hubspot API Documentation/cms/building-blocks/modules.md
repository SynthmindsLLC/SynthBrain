---
title: "Modules overview"
description: "Understanding modules is key to understanding the HubSpot CMS and its power. Modules are reusable components that can be used in templates or added to pages through [drag and drop areas](/docs/cms/guides/creating-a-drag-and-drop-area) and [flexible columns](/docs/cms/hubl/tags#flexible-column). In addition to using the modules that HubSpot provides, developers can create their own modules for everything from testimonials to photo galleries. Modules are created [using the local development tools](/docs/cms/guides/getting-started-with-modules) or [using the Design Manager](https://knowledge.hubspot.com/cos-general/create-and-edit-modules). A module has two parts: 1. A user interface created through a list of fields that users will see when editing a module instance. 2. An HTML+HubL template fragment with associated CSS and JS that defines how HTML will be generated"
type: "concept"
tags:
- "Modules"
- "HubSpot CMS"
- "Reusable Components"
relationships:
- "#part_of [[CMS]]"
- "#used_for [[Templates]], [[Pages]]"
last_updated: "2022-11-17"
---

Modules overview


====================

Last updated: November 17, 2022

Understanding modules is key to understanding the HubSpot CMS and its power. Modules are reusable components that can be used in templates or added to pages through [drag and drop areas](/docs/cms/guides/creating-a-drag-and-drop-area) and [flexible columns](/docs/cms/hubl/tags#flexible-column). In addition to using the modules that HubSpot provides, developers can create their own modules for everything from testimonials to photo galleries. Modules are created [using the local development tools](/docs/cms/guides/getting-started-with-modules) or [using the Design Manager](https://knowledge.hubspot.com/cos-general/create-and-edit-modules).

A module has two parts:

1.  A [user interface](#the-user-interface-for-editing) created through a list of fields that users will see when editing a module instance.
2.  An HTML+HubL template fragment with associated CSS and JS that defines how HTML will be generated

An Example[](https://developers.hubspot.com/docs/cms/building-blocks/modules#an-example)
----------------------------------------------------------------------------------------

To better understand what a module is, let's take a look at a simple "Team Member" module. The module consists of a photo, the team member's name, their title, and a short bio and when part of a CMS web page looks like:

![Team member module instance](https://developers.hubspot.com/hs-fs/hubfs/team-member-module-instance.png?width=257&height=635&name=team-member-module-instance.png "Team member module instance")

### The User Interface for Editing[](https://developers.hubspot.com/docs/cms/building-blocks/modules#the-user-interface-for-editing)

The developer builds the user interface (UI) for modules using fields. The developer then chooses which fields to use based on the kind of module being built, the data that is needed, and the editing experience. In this case, the module includes:

1.  an image field, for a team member photo
2.  two text fields, for the team member's name and position
3.  and a rich text field, for a short bio.

When a content creator edits a module, the UI is constructed based on the fields that the developer has added to the module and how each field is configured.

![Team member module editor](https://developers.hubspot.com/hubfs/team-member-editor.png "Team member module editor")

Module vs module instance[](https://developers.hubspot.com/docs/cms/building-blocks/modules#module-vs-module-instance)
----------------------------------------------------------------------------------------------------------------------

There are two terms frequently used regarding modules. It's important to understand the difference between them.

*   **Module** - reusable building blocks that can be added to templates and pages.
*   **Module instance** - the individual rendered modules on the page. They can have separate field values and as a result look different from other module instances that are for the same module.

Fields.json[](https://developers.hubspot.com/docs/cms/building-blocks/modules#fields-json)
------------------------------------------------------------------------------------------

The fields for a module are defined in JSON as an array of objects. Each field has a name, type, and default value. Other properties are also available depending on the type of field that controls the editing experience.

// fields.json \[ { "name": "team\_member\_photo", "label": "Team Member Photo", "required": true, "responsive": true, "resizable": true, "type": "image", "default": { "src": "", "alt": "" } }, { "name": "team\_member\_name", "label": "Team member name", "required": true, "type": "text", "default": "Joshua Beck" }, { "name": "team\_member\_position", "label": "Team member position", "required": true, "type": "text", "default": "CEO, Co-Founder" }, { "name": "team\_member\_bio", "label": "Team member bio", "required": true, "type": "richtext", "default": "<p>Joshua has over 20 years of experience in the tech industry. He helped start this company in 2015 with the mission of helping people grow. In his spare time he loves hanging out with his kids, going to the beach, and cooking.</p>" } \]

To learn more about all of the fields that are available, see [Module and Theme Fields](/docs/cms/building-blocks/module-theme-fields).

### Using module field data to render HTML[](https://developers.hubspot.com/docs/cms/building-blocks/modules#using-module-field-data-to-render-html)

The values for each field are available in the HTML+HubL fragment for a module via a `module` variable. The data for each field can be accessed via the properties of the module variable. Using the team member module as an example, the team member name can be accessed via `{{ module.team_member_name }}`.

<section class="team-member"> <img class="team-member\_\_image" src="{{ module.team\_member\_image.src }}" alt="{{ module.team\_member\_image.alt }}"> <h3 class="team-member\_\_name">{{ module.team\_member\_name }}</h3> <p class="team-member\_\_position">{{ module.team\_member\_position }}</p> <div class="team-member\_\_bio">{{ module.team\_member\_bio }}</div> </section>

Using Modules in Templates[](https://developers.hubspot.com/docs/cms/building-blocks/modules#using-modules-in-templates)
------------------------------------------------------------------------------------------------------------------------

Modules are added to templates using the [module](/docs/cms/building-blocks/modules/using-modules-in-templates#basic-module-syntax), [module\_block](/docs/cms/building-blocks/modules/using-modules-in-templates#block-syntax), or [dnd\_module](/docs/cms/hubl/tags/dnd-areas) tag and specifying the path to the module as a parameter. The default values for fields in a module can also be overridden at the template level through adding parameters to the module tag that corresponds to the field name as shown in the second part of the example below.

{% module "unique\_identifier" path="/modules/team-member.module" %} {# override default values in a module instance #} {% module "unique\_identifier" path="/modules/team-member.module", team\_member\_name="Brian Halligan", team\_member\_position="CEO" %}

Modules can't be nested inside of each other. The majority of the time you would want to do this, it is usually for layout reasons. Sections in [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas), are often the better course of action.

Modules are a great tool in the accessibility toolbox[](https://developers.hubspot.com/docs/cms/building-blocks/modules#modules-are-a-great-tool-in-the-accessibility-toolbox)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Modules are used throughout a website, some times on multiple pages, even multiple times on a page. Because of this [building your module's HTML, CSS, and JS, with accessibility in mind](/docs/cms/developer-reference/accessibility) can have a profound effect on how usable your site is to those both with and without disabilities or impairments.

Modules can make localization easier[](https://developers.hubspot.com/docs/cms/building-blocks/modules#modules-can-make-localization-easier)
--------------------------------------------------------------------------------------------------------------------------------------------

In a similar sense to accessibility, building modules so that all content in the module is based on fields, makes it possible to localize later. For example you may have a "Featured articles" module. Instead of hard-coding the text "Featured Articles" use a text or rich text field. Then the text can be changed for other languages. To learn more about localization on the CMS see [multi-language](/docs/cms/features/multi-language-content).

Getting Started[](https://developers.hubspot.com/docs/cms/building-blocks/modules#getting-started)
--------------------------------------------------------------------------------------------------

To get started, check out our [Getting started with modules](/docs/cms/guides/getting-started-with-modules) tutorial.

Going Further[](https://developers.hubspot.com/docs/cms/building-blocks/modules#going-further)
----------------------------------------------------------------------------------------------

*   [Configuring a module](/docs/cms/building-blocks/modules/configuration)
*   [Using modules in templates](/docs/cms/building-blocks/modules/using-modules-in-templates)
*   [Default modules](/docs/cms/building-blocks/modules/default-modules)
*   [The module editor](/docs/cms/building-blocks/modules)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules#page-feedback)
----------------------------------------------------------------------------------------------------

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