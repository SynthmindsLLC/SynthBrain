---
title: "Menus and Navigation"
description: "Include navigation menus on your website to help users find the information they need. "
type: "guide"
tags:
- "Website Design"
- "User Experience"
- "Navigation"
relationships:
- "#related_to [[HubSpot]]"
- "#used_for [[Improving User Navigation]]"
last_updated: "2024-03-28"
---

Menus and Navigation


========================

Last updated: March 28, 2024

Include navigation menus on your website to help users find the information that the need. Navigation menus are often located in the headers, sidebars, and footers of a website. HubSpot provides a few built-in solutions for adding menus to your pages, depending on your use case, but you can also create your own menus when needed. Your account also includes a [settings page for creating and managing menus](#navigation-settings), which the various menu methods can reference.

*   **Default menus:** HubSpot provides two default menu types that can be used as needed out of the box. These menus can be added as modules in the page editor in [drag and drop areas](/docs/cms/building-blocks/templates/drag-and-drop-areas) or in templates, or you can add them to custom modules using [HubL tags](#menu-hubl-tags).
    *   **Menu:** commonly used for global navigation, such as in the website header or footer, the default standard menu enables you to select a menu that you've configured in your navigation settings, then configure it further with options such as maximum levels, display settings, and orientation.
    *   **Simple menu:** commonly used for page-specific navigation, such as pillar pages, the simple menu module enables you to create menus at the page level. Rather than reference a menu that you've built in your navigation settings, simple menu items are managed in the content editor and have fewer configuration options than the standard menu. This enables content creators to update menus on specific pages as needed without impacting global navigation.

*   **Custom menus:** when the default menu options don't fit your needs, you can create your own custom solutions. This can range from building custom modules that include default menus using the standard [menu and simple\_menu HubL tags](#menu-hubl-tags), to using the [menu() HubL function](#menu-hubl-function) to build out a completely custom solution using repeater groups or HubDB. That being said, when building a complicated custom menu, you should keep in mind the editor experience. In many cases, it may make more sense to use the `menu` and `simple_menu` fields in tandem with the `menu()` function so that there's a balance between custom solution and intuitive editing experience.

Below, learn more about the different ways to include menus on pages and how to manage navigation settings in HubSpot.

Navigation Settings[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#navigation-settings)
-----------------------------------------------------------------------------------------------------------------------

In each account, HubSpot includes [navigation settings](https://knowledge.hubspot.com/cos-general/set-up-your-site-s-navigation-menus) so that you can create multi-level menus to reference in menu modules and tags. This creates a single source of truth for a set of menu items, so you'll only need to update a menu once to update all pages referencing that menu. You can create as many menus as needed, and each menu comes with options for cloning, deleting, renaming, and displaying revision history.

To create and manage menus in HubSpot, navigate to Settings > Website > Navigation menus. Learn more about navigation settings in [HubSpot's Knowledge Base](https://knowledge.hubspot.com/website-pages/set-up-your-site-s-navigation-menus).

![Navigation settings area](https://developers.hubspot.com/hs-fs/hubfs/image2-4.png?width=600&height=552&name=image2-4.png "Navigation settings area")

When working with menus in HubL, you may need to reference the menu's ID. This does not apply to simple menus, as their menu items are set in the editor.

When building a custom module, the easiest way to get the menu ID is by creating a menu field. This field enables the content creator to select a menu from a dropdown menu, and returns the menu ID. If you need to hardcode the menu ID, you can retrieve it from the URL when viewing the menu in the navigation settings page. 

![menu-id-in-url](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/menu-id-in-url.png?width=401&height=342&name=menu-id-in-url.png)Note that, when you first arrive at the page, the default menu ID will not display in the URL. To get the ID for that default menu, you'll need to select a different menu, then select the default menu again.

A best practice for site headers, which often contain the lengthy main navigation, is to provide a ["skip to content" link](/docs/cms/developer-reference/accessibility#adding-a-skip-to-content-link). This helps users navigating by keyboard, skipping over lengthy menus.

HubL menu tags[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#hubl-menu-tags)
-------------------------------------------------------------------------------------------------------------

Use the `menu` and `simple_menu` HubL tags to add menu functionality to custom modules. Adding the tag to a module will render the menu on the page. To enable content creators to configure the menu's options in the page editor, you'll need to include the [menu](/docs/cms/building-blocks/module-theme-fields#form) or [simple menu field](/docs/cms/building-blocks/module-theme-fields#simple-menu) in the module as well.

Below, learn more about each type of menu tag.

### Standard menu[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#standard-menu)

The [HubL Menu tag](/docs/cms/hubl/tags#menu) generates standard menu HTML with class names already provided for depth levels, active states, and if the item has children. The menu tag can be used within [custom modules](/docs/cms/building-blocks/modules) making it an easy way to create navigation menus for main nav's and sidebar navigation. This tag expects you to provide the [menu ID](#menu-id).

{% menu "menu" %} {% menu "my\_menu" id=456, site\_map\_name='Default', overrideable=False, root\_type='site\_root', flyouts='true', max\_levels='2', flow='horizontal', label='Advanced Menu' %}

### Simple menu[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#simple-menu)

The [simple menu](/docs/cms/hubl/tags#simple-menu) tag functions just like the menu tag by generating [standard menu HTML](https://developers.hubspot.com/docs/cms/hubspot-menu-markup) with class names for depth levels, active states, and if the item has children. The difference is that this tag expects you to provide a dict of the menu structure instead of a menu ID. This is useful for when you want a module's fields to determine the structure of a menu instead of using the navigation settings. For example, you may want to use this type of module for the table of contents of a pillar page.

{% simple\_menu menu\_tree=\[{"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "Home", "linkTarget": null, "linkUrl": "http://www.hubspot.com", "children": \[\], "isDeleted": false}, {"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "About", "linkTarget": null, "linkUrl": "http://www.hubspot.com/internet-marketing-company", "children": \[{"contentType": null, "subCategory": null, "pageLinkName": null, "linkUrl": "http://www.hubspot.com/company/management", "isPublished": false, "children": \[\], "linkParams": null, "linkLabel": "Our Team", "linkTarget": null, "pageLinkId": null, "categoryId": null, "isDeleted": false}\], "isDeleted": false}, {"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "Pricing", "linkTarget": null, "linkUrl": "http://www.hubspot.com/pricing", "children": \[\], "isDeleted": false}\] %}

Default menu modules[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#default-menu-modules)
-------------------------------------------------------------------------------------------------------------------------

HubSpot provides default modules that you can add to coded templates, as well as pages through the page editor when a template includes [drag and drop areas](/docs/cms/hubl/tags/dnd-areas). Each module will have a different editing experience, with the standard menu having more configuration options than the simple menu.

Because modules cannot be nested, you cannot place these modules inside of other modules. Instead, you should use the [menu or simple menu tags](#hubl-menu-tags).

{% module "main\_nav" path="@hubspot/menu", label="Menu" id="123456" %} {% module "menu" path="@hubspot/simple\_menu", label="Simple Menu" menu\_tree=\[{"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "Home", "linkTarget": null, "linkUrl": "http://www.hubspot.com", "children": \[\], "isDeleted": false}, {"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "About", "linkTarget": null, "linkUrl": "http://www.hubspot.com/internet-marketing-company", "children": \[{"contentType": null, "subCategory": null, "pageLinkName": null, "linkUrl": "http://www.hubspot.com/company/management", "isPublished": false, "children": \[\], "linkParams": null, "linkLabel": "Our Team", "linkTarget": null, "pageLinkId": null, "categoryId": null, "isDeleted": false}\], "isDeleted": false}, {"contentType": null, "subCategory": null, "pageLinkName": null, "pageLinkId": null, "isPublished": false, "categoryId": null, "linkParams": null, "linkLabel": "Pricing", "linkTarget": null, "linkUrl": "http://www.hubspot.com/pricing", "children": \[\], "isDeleted": false}\] %}

### Standard menu markup[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#standard-menu-markup)

Default menu modules are powered by their respective HubL menu tags (`menu` and `simple_menu`) to generate standard menu HTML. Like other HubSpot modules, menu modules are wrapped in module wrapper markup. These `div` and `span` tags make the module editable with the content editor. The menu markup of both the menu and simple menu modules is the same, with the exception of some of the classes applied to the wrapper and menu containers.

<div id="hs\_cos\_wrapper\_widget\_1711642118872" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_module widget-type-menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module"> <span id="hs\_cos\_wrapper\_widget\_1711642118872\_" class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_menu" style="" data-hs-cos-general-type="widget" data-hs-cos-type="menu"> <div id="hs\_menu\_wrapper\_widget\_1711642118872\_" class="hs-menu-wrapper active-branch flyouts hs-menu-flow-horizontal" role="navigation" data-sitemap-name="default" data-menu-id="162449947934" aria-label="Navigation Menu"> <ul role="menu"> <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none"> <a href="javascript:;" aria-haspopup="true" aria-expanded="false" role="menuitem">Menu item 1</a> <ul role="menu" class="hs-menu-children-wrapper"> <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="//freecrmtest.hubspotpagebuilder.com/test" role="menuitem">A</a></li> <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.wikipedia.org/" role="menuitem">B</a></li> </ul> </li> <li class="hs-menu-item hs-menu-depth-1 hs-item-has-children" role="none"> <a href="javascript:;" aria-haspopup="true" aria-expanded="false" role="menuitem">Menu item 2</a> <ul role="menu" class="hs-menu-children-wrapper"> <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="//freecrmtest.hubspotpagebuilder.com/test" role="menuitem">A</a></li> <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.hubspot.com/new-page" role="menuitem">B</a></li> <li class="hs-menu-item hs-menu-depth-2" role="none"><a href="https://www.hubspot.com/blah" role="menuitem">C</a></li> </ul> </li> </ul> </div> </span> </div>

As shown above, the actual menu renders as a `ul` wrapped in a `div` with the `hs-menu-wrapper` class. This wrapper will have additional classes based on how the module is configured in the page editor, such as enabling flyouts. Learn more about [classes added by these settings](#classes-added-by-settings) below.

Within the `ul`, each menu item is an `a` tag wrapped in a `li`. The `li` tag has a class that indicates the depth of the item in the menu tree (e.g., `hs-menu-depth-1`). When a menu item contains a nested child item, the corresponding `li` will have the additional class of `hs-item-has-children`. The child menu renders as a nested `ul` with the class `hs-menu-children-wrapper`.

When you visit a page that is included in your menu tree, the class `active-branch` is added to the parent `li` items and a class of **`active`** is added to that page's particular `li` item.

### Standard menu styling[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#standard-menu-styling)

At the module level, whether editing a menu module in the page editor or editing a menu field in a custom module, you'll have a few configuration options. The _Menu_, _Advanced menu type_, and _Max levels_ fields enable you to control the menu items are rendered as `li` in the page markup. But the orientation and flyouts options will impact the CSS selectors added to the menu wrapper `div`. You can then target these selectors in your CSS.

![menu-options-in-editor](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/menu-options-in-editor.png?width=376&height=166&name=menu-options-in-editor.png)

Below, learn more about the classes that are added to the menu wrapper `div` depending on these field settings.

Use this table to describe parameters / fields
| Class | Description |
| --- | --- |
| 
`hs-menu-flow-horizontal`

 | 

Added to the wrapper `div` when the menu is set to horizontal orientation.

 |
| 

`hs-menu-flow-vertical`

 | 

Added to the wrapper `div` when the menu is set to vertical orientation.

 |
| 

`flyouts`

 | 

Added to the wrapper `div` when _Enable flyouts_ is selected.

 |
| 

`no-flyouts`

 | 

Added to the wrapper `div` when _Enable flyouts_ is not selected.

 |

To get you started styling menus, below are some example CSS selectors that can be used to style the menu tag and default menu module.

/\* Menus \*/ .hs-menu-wrapper ul { /\* Targets all unordered lists within HubSpot menus \*/ } /\* Horizontal Menu ========================================================================== \*/ .hs-menu-wrapper.hs-menu-flow-horizontal ul { /\* Targets all unordered lists within horizontal menus \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal ul li{ /\* Targets all list items within horizontal menus \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal ul li a{ /\* Targets all links within horizontal menus \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul { /\* Targets the top-level unordered list within horizontal menus \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul li.hs-menu-depth-1 { /\* Targets top-level list items within the top-level unordered list \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul li a { /\* Targets top-level list links within the top-level unordered list \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul li.hs-item-has-children { /\* Targets list items with children with the top-level unordered list \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal.flyouts > ul li.hs-item-has-children ul.hs-menu-children-wrapper { /\* Targets second-level unordered lists when flyouts are enabled (for styling dropdowns) \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul li.hs-item-has-children ul.hs-menu-children-wrapper li a { /\* Targets links within second-level unordered lists \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal.flyouts > ul li.hs-item-has-children ul.hs-menu-children-wrapper li.hs-item-has-children ul.hs-menu-children-wrapper { /\* Targets third-level unordered lists (for styling dropdowns)\*/ } .hs-menu-wrapper.hs-menu-flow-horizontal.flyouts > ul li.hs-item-has-children:hover > ul.hs-menu-children-wrapper { /\* Targets second-level unordered list when top-level menu item is hovered (use to reveal dropdowns) \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul li.hs-item-has-children.active-branch{ /\* Targets top-level active branch unordered list \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal > ul li.hs-item-has-children.active-branch > ul.hs-menu-children-wrapper { /\* Targets second-level unordered list within active branch \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal li.active a{ /\* Targets the link within the active list item \*/ } /\* Vertical Menu ========================================================================== \*/ .hs-menu-wrapper.hs-menu-flow-vertical ul { /\* Targets all unordered lists within vertical menus \*/ } .hs-menu-wrapper.hs-menu-flow-vertical ul li a { /\* Targets all list items within vertical menus \*/ } .hs-menu-wrapper.hs-menu-flow-vertical ul li a { /\* Targets all links within vertical menus \*/ } .hs-menu-wrapper.hs-menu-flow-vertical > ul { /\* Targets the top-level unordered list within vertical menus \*/ } .hs-menu-wrapper.hs-menu-flow-vertical > ul li.hs-menu-depth-1 > a { /\* Targets top-level links in vertical menus \*/ } .hs-menu-wrapper.hs-menu-flow-vertical > ul li.hs-item-has-children { /\* Targets top-level list items with children \*/ } /\* No flyouts ========================================================================== \*/ .hs-menu-wrapper.hs-menu-flow-vertical.no-flyouts .hs-menu-children-wrapper { /\* Targets child menus when flyouts are disabled \*/ } .hs-menu-wrapper.hs-menu-flow-horizontal.no-flyouts > ul li.hs-item-has-children ul.hs-menu-children-wrapper { /\* Targets second-level child menus when flyouts are disabled \*/ }

HubL menu() function[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#hubl-menu-function)
-----------------------------------------------------------------------------------------------------------------------

The [menu()](/docs/cms/hubl/functions#menu) function exists to enable you to create fully custom menu structures. It returns an object that you can iterate through to generate a menu, there are many [provided properties for the menu items](/docs/cms/hubl/variables#menu-node-variables). Be aware when you use the menu function [you are fully responsible for the accessibility of your menu](/docs/cms/guides/accessibility), the structure, and the styling.

{% set node = menu(987) %} {% for child in node.children %} {{ child.label }}<br> {% endfor %} {% set default\_node = menu("default") %} {% for child in default\_node.children %} {{ child.label }}<br> {% endfor %}

The [HubSpot CMS Theme Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate) contains an [example menu module built with the menu() function](https://github.com/HubSpot/cms-theme-boilerplate/blob/main/src/modules/menu.module/module.html). You can modify that to meet your needs to make complicated menus.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/menus-and-navigation#page-feedback)
-----------------------------------------------------------------------------------------------------------------

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