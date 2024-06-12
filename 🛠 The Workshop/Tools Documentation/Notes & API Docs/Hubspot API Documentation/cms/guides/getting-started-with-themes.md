---
Please provide me with the context or topic for the mission! 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a team, a personal goal, etc.?"
* **What is the overall goal?** What are you trying to achieve?
* **What are the key objectives?** What specific steps need to be taken to achieve the goal?
* **What are the values and principles guiding the mission?** What are the core beliefs and behaviors that will shape the actions taken?

Once I have this information, I can help you write a compelling and effective mission statement.
---

Getting started with themes


===============================

Last updated: February 10, 2023

A theme is a portable and self-contained package of developer assets designed to work together to enable a flexible content editing experience. These assets might include templates, modules, CSS files, JavaScript files, images, and more. Themes allow developers to create a set of theme fields, similar to module fields, which allow content creators to control global website styles without having to edit CSS.

You can use HubL to access the values of theme fields throughout the theme's CSS. Content creators can then use the theme editor to modify theme fields, preview those changes against existing templates within a theme, and publish their changes.

![Theme settings edit UI animation showing selecting a color for elements of a theme.](https://developers.hubspot.com/hs-fs/hubfs/cms-themes-animation.gif?width=550&height=309&name=cms-themes-animation.gif "Theme settings edit UI animation showing selecting a color for elements of a theme.")

This document walks through creating your first theme based on the [HubSpot CMS Boilerplate](//developers.hubspot.com/docs/cms/building-blocks/themes/hubspot-cms-boilerplate). For more on themes, see the [themes reference documentation.](//developers.hubspot.com/docs/cms/building-blocks/themes)

If this is your first experience with CMS Hub development it's recommended you go through:

[Quick start to CMS Hub development](https://developers.hubspot.com/cs/c/?cta_guid=c66b91fb-14b1-4c35-ab0d-7e4af8000592&signature=AAH58kE9z4MMG8VPrNfwhg9fnKylBmRp7Q&portal_id=53&pageId=29844694130&placement_guid=28bfd0e9-ec05-48a5-b069-ce20015f54ac&click=33c621a6-481b-49d1-b9f5-dc0abed30a90&redirect_url=APefjpFqMoA87-6lU6_mLPlwrog2Jf4TjhsVhNaNuEMwYbZj_l08KMXY7UGxwRncg_ZQK0Wapzl2LH-KZ0ERYGAHUU0GEFGuWLBoA98OImhruv4EgGZ7BYD7pNT8wGwQbtwgPax8EOFg2ZmpuqjK1fWVKw2UDLVJ3A&hsutk=9c736650bec299a05d7df59038e6b735&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fguides%2Fgetting-started-with-themes&__hstc=20629287.9c736650bec299a05d7df59038e6b735.1715711064655.1715711064655.1715711064655.1&__hssc=20629287.1.1715711064655&__hsfp=1511885054&contentType=standard-page "Quick start to CMS Hub development") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, '28bfd0e9-ec05-48a5-b069-ce20015f54ac', {"useNewLoader":"true","region":"na1"});

**Please note:** before you begin, you'll need to install the [HubSpot CLI](/docs/cms/guides/getting-started-with-local-development).

1\. Start a boilerplate theme project[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#start-a-boilerplate-theme-project)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Run hs create website-theme my-website-theme to create a my-website-theme directory populated with files from the [CMS theme boilerplate](https://github.com/HubSpot/cms-theme-boilerplate).

2\. Upload the CMS Boilerplate to your HubSpot account[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#upload-the-cms-boilerplate-to-your-hubspot-account)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Run `hs upload my-website-theme my-website-theme`. This will upload the boilerplate to your account’s design manager, in a folder titled _my-website-theme_.

3\. Create a page[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#create-a-page)
-------------------------------------------------------------------------------------------------------------

To create a page from the uploaded theme:

*   In your HubSpot account, navigate to **Marketing** > **Website** > **Website Pages.**
*   In the upper right, click **Create**, then select **Website page**. 
*   In the dialog box, select the **domain** that the page will be published to, then enter a **page name**. Then, click **Create page**.

![create-page-from-dashboard](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/create-page-from-dashboard.gif?width=1280&height=1232&name=create-page-from-dashboard.gif)

*   On the template selection screen, templates from your [active theme](https://knowledge.hubspot.com/website-pages/use-themes#use-an-active-theme) will appear at the top of the page.
    *   If you haven’t selected an active theme, hover over **CMS theme boilerplate** and click **Set as active theme**. 
    *   If you've already set an active theme, select your new theme by clicking the **theme selector** dropdown menu, then selecting **Change theme**. Then, hover over **CMS theme boilerplate** and click **Set as active theme**. On the next screen, select a **template**.

![theme-selector](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/theme-selector.gif?width=1249&height=835&name=theme-selector.gif "theme-selector")

You'll then be brought to the page editor where you can edit the theme's fields.

4\. Edit theme fields[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#edit-theme-fields)
---------------------------------------------------------------------------------------------------------------------

*   In the left sidebar of the page editor, click the **Themes** tab.
*   On the _Themes_ tab, click **Edit theme settings**. This is where you can modify your existing theme settings. Publishing changes to theme settings will update the styles across your pages using this theme that was updated. 

![edit-theme-settings](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/edit-theme-settings.gif?width=660&height=497&name=edit-theme-settings.gif "edit-theme-settings")

5\. Prepare to make local changes[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#prepare-to-make-local-changes)
---------------------------------------------------------------------------------------------------------------------------------------------

Return to your terminal, then run `hs watch my-website-theme my-website-theme`. This [command](/docs/cms/guides/getting-started-with-local-development) watches your local directory and automatically uploads the following changes to your HubSpot account on file saves.

6\. Add a theme field[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#add-a-theme-field)
---------------------------------------------------------------------------------------------------------------------

Now that we're listening for local changes, add a new theme field:

*   Open `fields.json` file in your editor. This file controls the available fields in the theme editor sidebar. We’ll be adding a new [field](/docs/cms/building-blocks/themes#fields-json) to specify the height of the footer.
*   Near the bottom of the file, locate the `footer` group. 
*   Copy the code below and paste the JSON into the file above the first item in the children array for the footer group. 

// fields.json { "id" : "", "name" : "height", "label" : "Footer height", "required" : false, "locked" : false, "display" : "text", "step" : 1, "type" : "number", "min" : 10, "max" : 900, "help\_text":"This footer will expand in height to accomodate any content added to the footer. You are setting the minimum height in px", "default" : 100 },

 *    Save `fields.json`, and refresh the theme previewer in HubSpot. Your new field should display in the left-hand sidebar.

7\. Reference the field in your CSS[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#reference-the-field-in-your-css)
-------------------------------------------------------------------------------------------------------------------------------------------------

*   In your code editor, open the `theme-overrides.css` file. Then locate the css selector for `.footer`. We're now going to add a `min-height` to this selector.
*   To access a value in a theme, use the `theme` object. For example, you would use `{{ theme.footer.height }}` to access the height value set in our height field.
*   Replace the `.footer` declaration in theme-overrides.css with the following:

.footer { background-color: {{ footer\_bg\_color }}; min-height: {{theme.footer.height}}px; }

*   Save `theme-overrides.css` to upload it to your HubSpot account.

8\. Test changes[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#test-changes)
-----------------------------------------------------------------------------------------------------------

Return to the theme editor, and refresh the page to see your new field appear under footer. Update the height value to have it reflected immediately in the preview. It might be helpful to set a background color for the footer so you can see the change more easily.

Next Steps[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#next-steps)
---------------------------------------------------------------------------------------------------

Now that you've created and updated your theme, you can now create more theme fields and customize them for your projects. For more customization options, check out the [themes overview](/docs/cms/building-blocks/themes). While building out your theme, it might be helpful to view the best practices for [optimizing websites on the HubSpot CMS](/docs/cms/guides/speed). 

HubSpot has several [default themes](/docs/cms/building-blocks/themes/default-themes) that come with CMS Hub. These themes are available for you to view, clone, and update, to learn how you might use a theme in a real-world scenario.

Once you've got a handle on themes, [learn how to build your first custom module](/docs/cms/guides/getting-started-with-modules). 

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-themes#page-feedback)
---------------------------------------------------------------------------------------------------------------

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