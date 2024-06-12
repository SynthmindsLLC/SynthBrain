---
title: "HubSpot Forms"
description: "Use HubSpot forms to capture information from website visitors, which you can then access throughout HubSpot."
type: "group"
tags:
- "Website Tools"
- "Customer Conversion"
- "Data Collection"
relationships:
- "#part_of [[HubSpot]]"
- "#used_for [[Capturing Visitor Information]]"
- "#enables [[Accessing Form Data in HubSpot Tools and Assets]]"
last_updated: "2024-03-28"
---

HubSpot forms


=================

Last updated: March 28, 2024

Use HubSpot forms to capture information from website visitors, which you can then access throughout HubSpot. You can share links to forms directly with users, [submit form data via the API](https://legacydocs.hubspot.com/docs/methods/forms/forms_overview), and embed them on your website pages using the CMS.

Forms are a core part of the HubSpot and can be created in HubSpot accounts of any subscription level. Not only are forms important for customer conversion, but also because form data can be used in other HubSpot tools and assets, such as smart content, lists, workflows, content personalization, and more.

After [creating a HubSpot form](https://knowledge.hubspot.com/forms/create-forms), you can add it to your templates and pages. There are a few ways to add a form to a template, depending on your use case:

*   [Using the default form module](#the-default-form-module)
*   [Adding a form field to a custom module](#form-fields-in-custom-modules)[](#using-the-form-hubl-tag)
*   [Embedding using the form embed code](#embedding-forms-with-the-form-embed-code)

The default form module[](https://developers.hubspot.com/docs/cms/building-blocks/forms#the-default-form-module)
----------------------------------------------------------------------------------------------------------------

If your template has [drag and drop areas](/docs/cms/hubl/tags/dnd-areas), content creators can add the [default form module](/docs/cms/building-blocks/modules/default-modules#form) to a page from the page editor, then configure the form options in the left sidebar.

To code a form module directly into a template with drag and drop areas, reference it as a `dnd_module`. 

{% dnd\_area "dnd\_area" class='body-container body-container\_\_landing', label='Main section' %} {% dnd\_section vertical\_alignment='MIDDLE' %} {% dnd\_column width=6, offset=6 %} {% dnd\_row %} <!-- Form module tag for use in templates --> {% dnd\_module path='@hubspot/form' %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% end\_dnd\_column %} {% end\_dnd\_section %} {% end\_dnd\_area %}

To add a form module to a template outside of a drag and drop area, you'll instead reference it as a standard `module`. 

{% module "form" path="@hubspot/form" form={ "form\_id": "9e633e9f-0634-498e-917c-f01e355e83c6", "response\_type": "redirect", "message": "Thanks for submitting the form.", "redirect\_id": null, "redirect\_url": "http://www.google.com" } %}

With either implementation, you can add parameters to the module tag to specify settings such as the form to use and redirect options, as shown in the code example above. See the [default modules documentation](/docs/cms/building-blocks/modules/default-modules#form) for more information on available parameters.

### Cloning the default module

In addition to using the default module as-is, you can clone it to make it editable, enabling you to customize it as needed. For example, you could clone the default form module, add a color field, then wrap the module's HTML in a `<section>` tag with styling to add the color as a background:

*   In the left sidebar design manager, navigate to the **@hubspot** folder, then right click **form.module** and select **Clone module**.

![clone-form-module](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/clone-form-module.png?width=400&height=279&name=clone-form-module.png)

*   In the right sidebar, click **Add field**, then select **Color**.
*   Add a `<section>` tag around the HTML content, then include styling to reference the color field, such as:

`<section style="background:">`

![default-form-module-clone-section](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/default-form-module-clone-section.png?width=700&height=384&name=default-form-module-clone-section.png)

Form fields in custom modules[](https://developers.hubspot.com/docs/cms/building-blocks/forms#form-fields-in-custom-modules)
----------------------------------------------------------------------------------------------------------------------------

When creating a custom module, you can include a form in it by adding a [form field](/docs/cms/building-blocks/module-theme-fields#form), along with adding the field's code snippet to the module HTML. For example, you may want to add a consultation request form to a module that contains an image of a product and a descriptive value proposition.

To add a form field to a custom module from the design manager:

*   In the right sidebar of the module editor, click Add field, then select Form.

![design-manager-select-form-field](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-manager-select-form-field.png?width=400&height=284&name=design-manager-select-form-field.png)

*   After adding the field, hover over the field in the right sidebar, then click Actions and select Copy snippet.

![module-field-copy-snippet](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/module-field-copy-snippet.png?width=400&height=495&name=module-field-copy-snippet.png)

*   Paste the snippet into the module's HTML field.

![module-field-paste-snippet](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/module-field-paste-snippet.png?width=1748&height=664&name=module-field-paste-snippet.png)

### Limit form options in the editor[](https://developers.hubspot.com/docs/cms/building-blocks/forms#limit-form-options-in-the-editor)

Once added to a page, content creators typically have control over many aspects of the form, including which form to use and the form fields themselves. However, you can limit the amount of control given in the page editor by modifying the form module’s `fields.json` file [locally](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development) to include the following fields:

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`disable_inline_form_editing`

 | String | 

Set the `disable_inline_form_editing` property to `true`to hide all inline form editing controls in the form module. This includes the form fields, submit button text, data privacy and consent options, and CAPTCHA.

 |
| 

`required_property_types`

 | Array | 

An array that specifies which forms can be selected based on the property types of the form fields. Values include: `"CONTACT"`, `"COMPANY"`, and `"TICKET"`.

 |

For example, if you’ve built out a module that should only be used for forms that enable visitors to contact your company’s various services departments, you could allow content creators to only be able to select forms that use ticket properties.

// Form field { "id" : "843b4f0f-0ed7-5b10-e86a-5cc8a0f11a0c", "name" : "form\_field\_1", "display\_width" : null, "label" : "Form", "required" : false, "locked" : false, "type" : "form", "disable\_inline\_form\_editing": true, "required\_property\_types": \["TICKET"\], "default" : { "response\_type" : "inline", "message" : "Thanks for submitting the form." } }

Form styling[](https://developers.hubspot.com/docs/cms/building-blocks/forms#form-styling)
------------------------------------------------------------------------------------------

While HubSpot offers [form styling from a global setting](https://knowledge.hubspot.com/forms/set-global-form-colors-and-fonts) and [form specific setting level](https://knowledge.hubspot.com/forms/create-forms#style-and-preview-your-form), you can also style a form depending on how it's added to your CMS pages.

**Please note:** all forms generated on the HubSpot CMS (excluding using the form embed code) will ignore any styling that is configured via the global form settings or the form's individual settings. 

### Styling forms via the default form module or HubL tag[](https://developers.hubspot.com/docs/cms/building-blocks/forms#styling-forms-via-the-default-form-module-or-hubl-tag)

HubSpot forms added to HubSpot pages can be styled using your website's CSS. HubSpot includes a number of different classes and attributes on forms that are generated where you can apply styling. As a starting point, refer to the [HubSpot Boilerplate's form CSS](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/css/elements/_forms.css), which represents the best practices for how to style forms.

### Styling forms via a custom module[](https://developers.hubspot.com/docs/cms/building-blocks/forms#styling-forms-via-a-custom-module)

Forms inside custom modules can be styled by CSS in the module's CSS pane within the design manager. By keeping CSS scoped to the module, you can ensure that whenever the module is added to a page, the styling comes with it. It's recommended to add a wrapper to the form, then using that wrapper as the top-level selector for the CSS. This will prevent your custom module's form styling from being overwritten by additional styles in your websites main stylesheet. Below is a screenshot of the custom module from above with form styling added to the CSS Pane.

![Custom Module with CSS](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/forms/form-module-css-pane-4.jpg?width=800&height=460&name=form-module-css-pane-4.jpg)

### Styling forms added via the form embed code

When using the form embed code, you can style the form using the [global form styling settings](https://knowledge.hubspot.com/forms/set-global-form-colors-and-fonts) or using your website's CSS.

Using the global form styling settings enables you to configure default settings for every form in the account. You can also [override these styles on an individual form within the form editor](https://knowledge.hubspot.com/forms/create-forms#style-and-preview-your-form).

![Global Form Styles](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/forms/global-form-styling-options-4.png?width=800&height=561&name=global-form-styling-options-4.png)

If you have a _Marketing Hub_ or _CMS Hub_ _Professional_ or _Enterprise_ subscription, you can select the Set as raw HTML form option when creating a form. This setting makes the form render as HTML instead of an iframe, which makes it easier to style the embedded form with CSS. 

Learn more about [styling embedded forms on the Knowledge Base](https://knowledge.hubspot.com/forms/how-can-i-share-a-hubspot-form-if-im-using-an-external-site).

![Set as raw HTML form setting](https://developers.hubspot.com/hs-fs/hubfs/5Cdocs/forms/set-as-raw-html-form-4.jpg?width=800&height=198&name=set-as-raw-html-form-4.jpg)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/forms#page-feedback)
--------------------------------------------------------------------------------------------------

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