---
title: "export_to_template_context"
description: "A HubL parameter that allows HubL tag parameters to be available in the template environment without rendering the tag."
type: "concept"
tags:
- "HubL"
- "CMS"
- "Templates"
relationships:
- "#used_for [[Conditionally Rendering Content]]"
- "#enables [[User Interactivity]], [[Content Customization]]"
- "#related_to [[Widget Data]], [[Template Variables]]"
- "#part_of [[HubSpot CMS]]"
---

export\_to\_template\_context


=================================

Last updated: January 25, 2024

`export_to_template_context` is a parameter that makes a HubL tag's parameters available to the template environment without actually rendering the HubL tag. This parameter can be used with all [HubL tags](/docs/cms/hubl/tags). The `widget_data` dict is used to retrieve these parameters, store them in [variables](/docs/cms/hubl/variables-macros-syntax), and/or incorporate them into your template's logic.

By making a HubL tag's parameters available in the template context, without actually rendering the HubL tag, you can allow users to make decisions in the content editor that affect how the template renders. For example, let's say that you want to only render a certain code block when the user gives a value to a field. This becomes possible with this parameter.

First you must add `export_to_template_context=True` to the HubL tag. Then you must use a `widget_data.module.parameter_you_want_to_retreive`.

{% module "job\_title" path="@hubspot/text", label="Enter a Job Title", value="Chief Morale Officer", export\_to\_template\_context=True %} {# Makes the parameters available to be stored and used in template logic #} {{ widget\_data.job\_title.body.value }} {# Prints the value of the HubL tag but can also be used in template logic #}

Below are a few applications of this concept.

Usage within custom modules[](https://developers.hubspot.com/docs/cms/building-blocks/modules/export-to-template-context#usage-within-custom-modules)
-----------------------------------------------------------------------------------------------------------------------------------------------------

`export_to_template_context=True` is not supported in custom modules, as it serves no real purpose for them. You do not need to use `export_to_template_context` to get the value of a module within a template, [you can already access it](#retrieving-parameters-from-modules-already-rendered-on-the-template). If you need to visually hide the module's output you could build the module to not output anything, or include a boolean field that enables or disables whether the module renders anything.

User selectable background images[](https://developers.hubspot.com/docs/cms/building-blocks/modules/export-to-template-context#user-selectable-background-images)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

In this example, an image HubL tag is created but then exported to the context of the template rather than rendered. The `src` parameter is retrieved with the `widget_data` tag and rendered as the source of a background image in a style tag.

{% module "background\_image" path="@hubspot/image" label='Select a background image', src='http://cdn2.hubspot.net/hub/428357/file-2117441560-jpg/img/dev-bg-compressed.jpg', export\_to\_template\_context=True %} <!--Sample markup --> <div class="bg-image-section" style="background:url('{{ widget\_data.background\_image.src }}'); background-size:cover; min-height: 500px;"> <h1>Supercharge your app with HubSpot</h1> <h3>Build powerful integrations for a global community of users</h3> </div>

While this is possible to do in coded templates, generally it is better to build a custom module to give users in the page editor the best experience. HubL tags like this show up as individual fields, whereas you may have multiple related fields. Using a custom module all of its fields display grouped in the page editor.

Choice field to render pre-defined markup[](https://developers.hubspot.com/docs/cms/building-blocks/modules/export-to-template-context#choice-field-to-render-pre-defined-markup)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following example uses the `export_to_template_context` parameter in conjunction with a [choice module](/docs/cms/hubl/tags#choice) to change a banner message on a careers page. The user selects a department via the UI and the heading changes without the user having to actually edit content.

{% module "department" path="@hubspot/choice", label="Choose department", value="Marketing", choices="Marketing, Sales, Dev, Services" export\_to\_template\_context=True %} {% if widget\_data.department.value == "Marketing" %} <h3>Want to join our amazing Marketing team?!</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% elif widget\_data.department.value == "Sales" %} <h3>Are you a Sales superstar?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% elif widget\_data.department.value == "Dev" %} <h3>Do you love to ship code?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% else %} <h3>Want to work with our awesome customers?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% endif %}

This same functionality can actually be reproduced using a choice field inside of a custom module. The custom module UI actually makes choice options with both a value and a label pretty easy.

Retrieving parameters from modules already rendered on the template[](https://developers.hubspot.com/docs/cms/building-blocks/modules/export-to-template-context#retrieving-parameters-from-modules-already-rendered-on-the-template)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you want to retrieve a parameter from a module or tag that is already rendering on a page, the module can be accessed within a dict named `widgets`. The `export_to_template_context` parameter is not required. The syntax is as follows:

// HubL {{ content.widgets.name\_of\_module.body.parameter }} {{ content.widgets.my\_text.body.value }}

**Please note:** the above method does not support retrieving values from fields in global modules, as `content.widgets` won't access global modules.

Because different fields store data in different formats it is often handy to make use of [developer Info](/docs/cms/developer-reference/debugging-and-errors#developer-info) to see how you access the specific data you want to display.

Printing HubL module info on blog listing[](https://developers.hubspot.com/docs/cms/building-blocks/modules/export-to-template-context#printing-hubl-module-info-on-blog-listing)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While blog templates are generally used for blogs, they can also be repurposed to create various other types of listings. You can use the techniques described above to achieve this.

For example, you may want to create a listing layout of press that your company has received, but rather than linking to posts, you want the listing to link to another page.

You can see this concept in action at [academy.hubspot.com/projects](https://academy.hubspot.com/projects). The projects listing page is a blog listing template, but each post links to a regular HubSpot page. The content creator specifies the destination link in the editor.

Within the head of the individual blog post's code, you would define a text field. If you don't want  the text to render on the post, you would use `export_to_template_context`.

{% module "custom\_blog\_link" path="@hubspot/text", label="Link to external press item", export\_to\_template\_context=True %}

This text field is editable in each blog post. Next, we would need to define a link in our listing. But because the widget\_data only exists in the context of the post, we need to use different syntax to fetch the widget data to populate the link. In this case, we would use `content.widgets.custom_blog_link.body.value`. While the `widget_data` is not available to the blog listing, the value of that field is still stored within the context of the individual content's widgets.

A basic blog listing loop that renders this custom link with each post is shown below. If using this technique, you would want to ensure that you add the subdirectory automatically created for each blog post to your robots.txt file to prevent those empty posts from being crawled by Google and other crawlers.

{% for content in contents %} <a href="{{ content.widgets.custom\_blog\_link.body.value }}"> Click here to see this press feature! </a> {% endfor %}

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/modules/export-to-template-context#page-feedback)
-------------------------------------------------------------------------------------------------------------------------------

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