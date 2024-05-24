Sections


============

Last updated: December 8, 2022

The outermost container in a [drag and drop area](/docs/cms/building-blocks/templates/drag-and-drop-areas) is called a section. Sections can't be nested within any other [dnd element](/docs/cms/building-blocks/templates/drag-and-drop-areas#drag-and-drop-areas-and-their-elements), but can contain modules, [rows](/docs/cms/building-blocks/templates/drag-and-drop-areas#row), and [columns](/docs/cms/building-blocks/templates/drag-and-drop-areas#column). In the page editor, content creators can add sections to the page, then modify and style them as needed. Content creators can also create and save sections to use on other pages within the same theme, making content creation more efficient.

In this article, learn more about sections and how to use them in the page editor. If you're developing a theme, check out the guide on [hiding modules and sections](/docs/cms/building-blocks/themes/hide-modules-and-sections) from the page editor to create a more streamlined content creation experience.

![page editor add reusable section UI](https://developers.hubspot.com/hs-fs/hubfs/page%20editor%20add%20reusable%20section%20UI.gif?width=700&height=454&name=page%20editor%20add%20reusable%20section%20UI.gif "page editor add reusable section UI")

Overview[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#overview)
-------------------------------------------------------------------------------------------------------------------

Sections can be created either [in the content editor by a content creator](https://knowledge.hubspot.com/website-pages/edit-page-content-in-a-drag-and-drop-area#create-a-section) or built by a developer into a `[dnd_area](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas)`, with the `[dnd_section](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas#drag-and-drop-section-code-dnd-section-code-)` tag.

The styling options available in the editor are available when coding a template as well. For example:

<main class="body-container-wrapper"> {% dnd\_area 'dnd\_area' label='Main section', %} {% dnd\_section background\_image={ 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': 'https://example.com/path/to/image.jpg' }, margin={ 'top': 32, 'bottom': 32 }, padding={ 'top': '1em', 'bottom': '1em', 'left': '1em', 'right': '1em' }, max\_width=1200, vertical\_alignment='MIDDLE' %} {% end\_dnd\_section %} {% end\_dnd\_area %} </main>

For full documentation of all available drag and drop element parameters and usage examples, learn more about [dnd\_area tags](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas).

You can use sections to quickly scaffold out templates that are easy to read. Since you are only specifying in context where the template specific instances are different, you can still go back and modify that section template. 

**Please note:** modifying a section will update it across all instances of that section, except for existing pages that use a template that references the section. Pages previously created with a template that had an included section in it will instead need to be manually updated to use the new version of the section. This prevents accidentally making breaking changes. To update a section to the latest version, a content creator can navigate to the page editor, add the new section to the page, then delete the old version.

Create reusable sections[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#create-reusable-sections)
---------------------------------------------------------------------------------------------------------------------------------------------------

Within a theme, you can include preconfigured sections that content creators can add to pages using that theme within the page editor. These reusable sections are built as section template files and are coded within the same syntax that you would use inside a `dnd_area`.

**Please note:** to make a section available for multiple themes, you'll need to add the section template file to each theme. Similarly, sections created by content creators in the content editor will only be available within that theme.

Below, learn how to create section template files and then reference them in other template files.

### Section template files[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#section-template-files)

Section templates are denoted with `templateType: section` in their [template annotation](https://developers.hubspot.com/docs/cms/building-blocks/templates/html-hubl-templates#template-annotations).

<!-- templateType: section label: Banner description: "A banner typically used at the top of a page highlighting a product or main topic." isAvailableForNewContent: true screenshotPath: ../images/section-previews/banner.png -->

Section Template Annotations
| Parameter | Type | Description | Value |
| --- | --- | --- | --- |
| 
`templateType`

 | String | 

Sets the template type used to determine where the template can be used and what data is available to it.

 | `section` |
| 

`label`

 | String | 

Used in the page editor to provide a human readable name of the section.

 |  |
| 

`description`

 | String | 

Further description of the section beyond what you can do with a label. Displays in the page editor. 255 characters maximum.

 |  |
| 

`screenshotPath`

 | String/path | 

Path to a screenshot of the section. This is used to give content creators an easy visual reference for what the section looks like.

 |  |

A section template must begin and end with a `dnd_section` tag. Only one `dnd_section` can exist within a section template. Inside of that section, you can place modules, rows and columns, following the same `dnd_area` rules that apply when [adding a dnd\_area to a page template](/docs/cms/hubl/tags/dnd-areas#dnd-area). The exception is that you are defining the content for just a section and its child drag and drop elements.

<!-- templateType: section label: Banner description: "A banner typically used at the top of a page highlighting a product or main topic." isAvailableForNewContent: true screenshotPath: ../images/section-previews/banner.png --> {% dnd\_section padding={ 'top': 200, 'right': 20, 'bottom': 200, 'left': 20 }, background\_image={ 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': context.backgroundImage || get\_asset\_url('../images/blank-page-banner.png') }, max\_width=778, vertical\_alignment='MIDDLE' %} {% dnd\_column %} {% dnd\_row %} {% dnd\_module path='@hubspot/rich\_text' %} {% module\_attribute 'html' %} <div style="text-align: center"> {{ context.content || '<h1 style="color: #fff;">Communicate <span style="font-weight: 400;">Your Way</span></h1><p style="color: #fff;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dapibus posuere mi, in pretium ante posuere a. Aliquam a risus at eros molestie pretium.</p>' }} </div> {% end\_module\_attribute %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% dnd\_row %} {% dnd\_module path='../modules/button', button\_text={{ context.buttonText || 'Subscribe' }} horizontal\_alignment='CENTER' %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% end\_dnd\_column %} {% end\_dnd\_section %}

### Add a section partial to a template[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#add-a-section-partial-to-a-template)

After creating a section, you can reference it within a `dnd_area` by using a  `include_dnd_partial` tag. This tag provides the path pointing to the section file, as shown below:

{% dnd\_area 'dnd\_area' class='body-container body-container--home-page', label='Main section' %} {# Banner Section #} {% include\_dnd\_partial path='../sections/banner.html' context={} %} {# End Banner Section #} {% end\_dnd\_area %}

In the above example, note the context argument in the `include_dnd_partial` tag. This allows you to pass instance specific variables from the page template to the section, overriding the default values in the section file. [See section context](#section-context) for more information.

### Section context[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#section-context)

You can use section context variables to override section level and module level default values. Section context variables are defined by you and are not associated directly with the modules and their fields.

In your page template you can set these context variables through the `context` parameter in the `include_dnd_partial` tag.

{% dnd\_area 'dnd\_area' class='body-container body-container--home-page', label='Main section' %} {# Banner Section #} {% include\_dnd\_partial path='../sections/banner.html' context={ 'content': '<h1 style="color: #fff;">Home Page</h1><p style="color: #fff;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dapibus posuere mi, in pretium ante posuere a. Aliquam a risus at eros molestie pretium.</p>', 'buttonText': 'Buy Now' } %} {# End Banner Section #} {% end\_dnd\_area %}

Any variables you add to your `context` parameter will become available to reference within your section template. The following example shows how to set the image URL and rich text area and button content set in context if it exists.

<!-- templateType: section label: Banner description: "A banner typically used at the top of a page highlighting a product or main topic." isAvailableForNewContent: true screenshotPath: ../images/section-previews/banner.png --> {% dnd\_section background\_image={ 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': context.backgroundImage || get\_asset\_url('../images/blank-page-banner.png') }, max\_width=778 %} {% dnd\_column %} {% dnd\_row %} {% dnd\_module path='@hubspot/rich\_text' %} {% module\_attribute 'html' %} <div style="text-align: center"> {{ context.content || '<h1 style="color: #fff;">Communicate <span style="font-weight: 400;">Your Way</span></h1><p style="color: #fff;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dapibus posuere mi, in pretium ante posuere a. Aliquam a risus at eros molestie pretium.</p>' }} </div> {% end\_module\_attribute %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% dnd\_row %} {% dnd\_module path='../modules/button', button\_text={{ context.buttonText || 'Subscribe' }} horizontal\_alignment='CENTER' %} {% end\_dnd\_module %} {% end\_dnd\_row %} {% end\_dnd\_column %} {% end\_dnd\_section %}

Notice everywhere context variables are used, there is an `||` _OR_ filter to provide fallback default content if none is provided. For example, in the button module, if `context.buttonText` has a value, the page will use it. Otherwise, the text is set to `Subscribe`. 

### Section classes[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#section-classes)

In section templates, you can add classes to the section wrapper using the class parameter. This will add the class you specify to the class field of the dnd section's html element. It's recommended wherever possible that you use styling controls built into sections to enable content creators to be able to modify them. 

**Please note:** section classes are only supported in section templates.

{% dnd\_section class='my-hero-section' padding={ 'top': 200, 'right': 20, 'bottom': 200, 'left': 20 }, background\_image={ 'backgroundPosition': 'MIDDLE\_CENTER', 'backgroundSize': 'cover', 'imageUrl': context.backgroundImage || get\_asset\_url('../images/blank-page-banner.png') }, max\_width=778, vertical\_alignment='MIDDLE' %} ...

Content creators can't edit, add, or remove classes. They can only be "removed" by recreating a section manually in the editor.

Additionally you should avoid changing the layout of section children using CSS or JavaScript. Doing so can create an unpleasant page editor experience for the content creator. 

### Previewing your section[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#previewing-your-section)

The easiest way to preview your section while developing, is to use the Design Manager. Open a template containing a [`dnd_area`](/docs/cms/hubl/tags/dnd-areas) which calls your section template using a `include_dnd_partial` tag. In the top right corner click preview. This way you can keep updating your section and see your changes reflected right away. This is much more efficient than having to create a new page for each change you make.

Copy section HubL[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#copy-section-hubl)
-------------------------------------------------------------------------------------------------------------------------------------

In the page editor, you can copy the HubL markup for a section to reuse the code as needed. This can be helpful when wanting to recreate drag and drop sections in a coded file.

To copy a section's HubL markup:

*   Navigate to your content:
    *   **Website Pages**: In your HubSpot account, navigate to **Marketing** \> **Website** \> **Website Pages**.
    *   **Landing Pages**: In your HubSpot account, navigate to **Marketing** \> **Landing Pages**.
*   Hover over a page and click **Edit**.
*   In the page editor, add the following parameter to the URL, then press **Enter**: `?developerMode=true`.
*   With the page reloaded, you'll now be in developer mode.  You can exit developer mode any time by clicking **Exit developer mode** in the upper right.

![exit-developer-mode0](https://developers.hubspot.com/hs-fs/hubfs/exit-developer-mode0.png?width=916&name=exit-developer-mode0.png)

*   Hover over the section you want to copy, then click the **down arrow icon**. Select **Copy as HubL**. The HubL markup will then be copied to your clipboard.

![copy-section-hubl-menu](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/copy-section-hubl-menu.png?width=698&name=copy-section-hubl-menu.png)

Related resources[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#related-resources)
-------------------------------------------------------------------------------------------------------------------------------------

*   [Drag and Drop Areas overview](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas)
*   [Drag and Drop Areas HubL tags](https://developers.hubspot.com/docs/cms/hubl/tags/dnd-areas)
*   [Using modules in templates](https://developers.hubspot.com/docs/cms/building-blocks/modules/using-modules-in-templates)
*   [Getting started with drag and drop areas](https://developers.hubspot.com/docs/cms/guides/creating-a-drag-and-drop-area?_ga=2.260863950.2135406090.1621313928-1048867954.1621313928)
*   [How to enable Developer Mode in CMS Hub's page editor - YouTube](https://www.youtube.com/watch?v=51gH2faFmfA)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#page-feedback)
-----------------------------------------------------------------------------------------------------------------------------------

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