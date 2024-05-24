Module and theme fields best practices


==========================================

Last updated: October 27, 2023

When incorporating fields into your module or theme, there are a few best practices to keep in mind, including:

*   Grouping fields together
*   Organizing fields logically across modules
*   Providing a consistent styling experience with style fields

In this article, learn about some recommended best practices to create an efficient and consistent module and theme field editing experience for content creators. 

Style fields vs. content fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#style-fields-vs-content-fields)
------------------------------------------------------------------------------------------------------------------------------------------------------------

You can add [style fields](/docs/cms/building-blocks/module-theme-fields-overview#style-fields) to both modules and themes, and they enable the content creator to adjust the module's appearance, such as borders or background images behind text. Style fields should not communicate meaning or be required to understand the page's content. For example, if you have a text and image module and the image is required to understand the text content, the image should be a content field rather than a style field.

When added to a module, the style options will appear in the _Styles_ tab of the page editor. When added to a theme, style options will appear in the left sidebar of the theme editor.

![style-field-module-editor0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/style-field-module-editor0.png?width=377&name=style-field-module-editor0.png)

Keep accessibility in mind when deciding between using an image or background image field. If the content creator should have the ability to add alt text, use an image field rather than a background image field.

Organizing fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#organizing-fields)
---------------------------------------------------------------------------------------------------------------------------------

How you organize fields plays a significant role in the content creator’s ability to quickly make changes. Below are recommended best practices for organizing fields:

*   Group style fields based on the component they control rather than the stylistic element. 
*   Leave only the highest-level, most important fields outside of groups.

*   Favor creating a component group over unnested groups. If you ever need to add functionality to your module later, you can't move your modules to a group later without manually updating all of the instances of the module on pages.

*   Order field groups in the order in which the components appear based on the primary language of the majority of the content creators that will be maintaining the site. Example: English is read from left to right, top to bottom. If the users maintaining the site typically read right to left in their language, you should provide it in that order. When in doubt, base this off of the primary language of the content for your site.

Learn more about [field groups](/docs/cms/building-blocks/module-theme-fields-overview#field-groups).

### Example[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#example)

Below is an example card module.

![A typical card layout containing an icon, text, and a button. Styling options are shown grouped on the right into Icon, Button, and Card categories.](https://developers.hubspot.com/hs-fs/hubfs/card%20and%20style%20settings.png?width=800&height=595&name=card%20and%20style%20settings.png "A typical card layout containing an icon, text, and a button. Styling options are shown grouped on the right into Icon, Button, and Card categories.")

The styles panel groups the module fields into 3 groups based on components in the card that can be styled.

*   Icon
*   Button
*   Card

When viewing the card, the icon is seen first, then the text and button. The Icon group and its styling options appear before the button group and its styling options. Therefor, the color field for the icon would be found in the _Icon_ group, while the color field for the button's background color would be found within the _Button_ group.

Required fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#required-fields)
-----------------------------------------------------------------------------------------------------------------------------

Required fields are fields that the content creator must set in order to display the module and publish the page. 

*   Only require fields to have a value if it breaks the module to not have a value.
*   If you need to have a required field, provide a default value if possible. 

For example, you're building an image carousel module which allows you to configure how many slides to display at the same time. A minimum value of 1 is needed, and without a value, you don't know how to display the image carousel. This is a situation where requiring a value, but setting a default value of one or two, might make sense.

Typography[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#typography)
-------------------------------------------------------------------------------------------------------------------

Because rich text fields provide more typographical control, it's recommended to use rich text fields over a combination of text field and font field when possible.

There may be cases where you need to be able to provide typographic styles that apply across multiple pieces of content within the same module, such as a [text field](/docs/cms/building-blocks/module-theme-fields#text) intended for headers. In that case, you may be able to make the content creator's work more efficient by providing [font](/docs/cms/building-blocks/module-theme-fields#font) and [color](/docs/cms/building-blocks/module-theme-fields#color) style fields in the text field.

When including rich text fields, it's recommended to allow the field's typographic controls to override manually added style fields. If a style field does control a rich text field, it may be worthwhile setting help text, to ensure the content creator is aware.

Toggle vs checkbox in boolean fields[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#toggle-vs-checkbox-in-boolean-fields)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

When including a [boolean field](/docs/cms/building-blocks/module-theme-fields#boolean), you can set it to display as either a toggle or a checkbox. 

*   Set the boolean to a toggle when the field controls a major design or layout option. For example, converting the layout of a card from vertical to a horizontal orientation.
*   Set the boolean to a checkbox when the change is less drastic. For example, hiding or showing a publish date for a blog post in a featured blog posts module.

Related articles[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#related-articles)
-------------------------------------------------------------------------------------------------------------------------------

*   [Module and theme field types](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields)
*   [Module and theme fields overview](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields-overview)
*   [Modules overview](https://developers.hubspot.com/docs/cms/building-blocks/modules)
*   [Themes overview](https://developers.hubspot.com/docs/cms/building-blocks/themes)

#### Tutorials[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#tutorials)

*   [Getting started with modules](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules)
*   [Getting started with themes](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields/best-practices#page-feedback)
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