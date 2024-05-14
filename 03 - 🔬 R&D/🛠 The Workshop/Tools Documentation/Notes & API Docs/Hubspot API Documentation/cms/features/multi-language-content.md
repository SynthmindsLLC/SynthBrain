Multi-language Content


==========================

Last updated: March 10, 2022

Any company which does business across regions or with a customer-base that speaks multiple languages needs to be able to connect with their audience in the audience’s language. With HubSpot’s CMS, users are able to [create multi-language variations](https://knowledge.hubspot.com/cos-general/how-to-manage-multi-language-content-with-hubspots-cos) of their content that enable the end-user to view the content in the language with which they are most comfortable.

HubSpot sets a number of facets of a multi-language website up for you automatically, but there is also a number steps developers should take to ensure their website is multi-language ready. 

HubSpot's default multi-language functionalities[](https://developers.hubspot.com/docs/cms/features/multi-language-content#hubspot-s-default-multi-language-functionalities)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Whenever a multi-language variant is created for a page in HubSpot, we will automatically: 

*   Create a new entry in the XML sitemap indicating the translated page’s name and URL.
*   Specify the language of the content within the page `<head>` for templates built using drag and drop functionality.
*   Identify other pages within the multi-language content group following the appropriate standardized format, which marks the other pages as alternates to avoid duplicate content errors and also identifies the [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) code associated with the language translation(s):
    
    `<link rel="alternate" hreflang="lang_code" href="url_of_page" />`
    
*   Re-write links on language pages to navigate to intra-language versions of the linked page to help visitors stay in-language, and prevent the need for you to have to update every single link on every page translation. For a given element, you can disable this rewrite by adding the class "hs-skip-lang-url-rewrite" to the element. 

### What HubSpot does not do[](https://developers.hubspot.com/docs/cms/features/multi-language-content#what-hubspot-does-not-do)

With the HubSpot CMS, HubSpot does not automatically:

*   translate the content of the page for you.
*   direct users to a multi-language variation based upon their GeoIP.
*   include a language-switcher module within your header or website.
*   specify the language of a page for coded files.
*   set the content directional attribute for translations using a language that reads right-to-left as opposed to left-to-right for coded files.

Set language variables[](https://developers.hubspot.com/docs/cms/features/multi-language-content#set-language-variables)
------------------------------------------------------------------------------------------------------------------------

Because coded files do not automatically include language declarations or content language directional attributes, this will need to be manually set up for coded templates. Language variables can be set in HTML or populated via HubL, such as in the [CMS Boilerplate template](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/src/templates/layouts/base.html#L2). 

Setting these properties using HubL will allow this data to populate dynamically within a page’s HTML based upon the language set for the page within the HubSpot CMS.

<html lang="{{ html\_lang }}" {{ html\_lang\_dir }}>

Use page-editable modules[](https://developers.hubspot.com/docs/cms/features/multi-language-content#use-page-editable-modules)
------------------------------------------------------------------------------------------------------------------------------

In order to ensure that content can be localized across each instance of a template’s use, leverage [custom modules](/docs/cms/building-blocks/modules) in place of hard-coded HTML content whenever possible. Creating modules that can be edited at the page level will enable content creators to set the specific content that should appear on each page without having the adjust template code. It also allows for unique content to be used across pages which share a template. 

Include field translations in custom modules and themes[](https://developers.hubspot.com/docs/cms/features/multi-language-content#include-field-translations-in-custom-modules-and-themes)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To support your global team, you can publish translations of modules you've created in HubSpot.

After you've translated the content in the module and published in the languages of your team members, users will see the field labels for that module in their account default language. The content in a translated module will not be translated automatically; you will need to do this. You can create translations of your module in any supported language.  

You can set translations using the [local development tools](/docs/cms/building-blocks/modules#local-module-file-structure) or through the Design Manager.

### Local development[](https://developers.hubspot.com/docs/cms/features/multi-language-content#local-development)

To set translations using local development tooling, every module folder and every theme folder can contain a `_locales` folder, with language locale subfolders, each with a `messages.json` file, containing module field translations.

![Screenshot of editing module translations locally in VS Code](https://developers.hubspot.com/hs-fs/hubfs/local%20module%20translations.png?width=580&height=290&name=local%20module%20translations.png "Screenshot of editing module translations locally in VS Code")

### Design Manager[](https://developers.hubspot.com/docs/cms/features/multi-language-content#design-manager)

To set field translations through the [Design Manager](/docs/cms/developer-reference/design-manager), when viewing the module, navigate to the “Add Translations” option on the right hand side of the screen. Select the languages in which your team works from the dropdown menu. From there, you are able to select each language and specify the labeling conventions for each field in each language.

![Screenshot of field translations in the design manager](https://developers.hubspot.com/hs-fs/hubfs/field_translations.gif?width=580&height=289&name=field_translations.gif "Screenshot of field translations in the design manager")

Theme field translations do not have an interface in the design manager and need to be edited through the `.json` files.

Translate system pages[](https://developers.hubspot.com/docs/cms/features/multi-language-content#translate-system-pages)
------------------------------------------------------------------------------------------------------------------------

To set up translations for system pages, including password reset and email subscription pages, you can customize module and HubL tag fields with your translated content. Learn more about the available fields for [modules](/docs/cms/building-blocks/modules/default-modules) and [system page HubL tags](/docs/cms/hubl/tags#system-page-tags).

Include a language switcher[](https://developers.hubspot.com/docs/cms/features/multi-language-content#include-a-language-switcher)
----------------------------------------------------------------------------------------------------------------------------------

To enable end-users to toggle between available translations, it is advised that a language-switcher module be added to your website. 

An [example of of how to implement a language switcher](https://github.com/HubSpot/cms-theme-boilerplate/blob/09ad0b2c3bbc8400e64c5617268cb0504392e8e5/src/templates/partials/header.html#L26-L47) can be found in the [CMS Theme Boilerplate](/docs/cms/building-blocks/themes/hubspot-cms-boilerplate). 

{# Header navigation row one #} <div class="header\_\_row-1"> {% if content.translated\_content.values()|selectattr('published')|length || is\_listing\_view && group.translations %} <div class="header\_\_language-switcher header--element"> <div class="header\_\_language-switcher--label"> {% module 'language-switcher' path='@hubspot/language\_switcher', label='Language switcher', display\_mode='localized' %} <div class="header\_\_language-switcher--label-current"> {{ locale\_name(locale) }}</div> </div> </div> {% endif %} <div class="header\_\_search header--element"> {% module 'site\_search' path='@hubspot/search\_input', label='Search', field\_label='Search', placeholder='' %} </div> </div> {# End header navigation row one #}

Implementing search on multi-language websites[](https://developers.hubspot.com/docs/cms/features/multi-language-content#implementing-search-on-multi-language-websites)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Content Search](/docs/cms/features/content-search) supports querying for content across the various languages on your website. The language filter parameter can be used when hitting the [/contentsearch/v2/search](https://developers.hubspot.com/docs/methods/content/search-for-content) to return only specified languages, which allows you to create search experiences for each language on your website, or let visitors search across multiple languages on your website. 

Use global partials and modules[](https://developers.hubspot.com/docs/cms/features/multi-language-content#use-global-partials-and-modules)
------------------------------------------------------------------------------------------------------------------------------------------

Use module fields to make text in headers, footers, and sidebars editable. Place these modules into global partials. Not only will content creators benefit from ease of editing, global partials support [configuring their settings for each language](https://knowledge.hubspot.com/cos-general/how-to-manage-multi-language-content-with-hubspots-cos#edit-global-content-in-a-multi-language-page). 

![Screenshot of page editor showing header partial](https://developers.hubspot.com/hs-fs/hubfs/edit-multilanguage-global-content.png?width=580&height=166&name=edit-multilanguage-global-content.png "Screenshot of page editor showing header partial")

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/features/multi-language-content#page-feedback)
------------------------------------------------------------------------------------------------------------

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