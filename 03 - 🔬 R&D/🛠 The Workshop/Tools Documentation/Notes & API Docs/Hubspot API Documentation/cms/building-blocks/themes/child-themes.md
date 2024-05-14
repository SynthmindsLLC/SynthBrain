Child Themes


================

Last updated: August 12, 2022

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Starter, Professional, or Enterprise

A **child theme** is a copy of an original **parent theme**. You can edit the child theme without altering the parent theme. You can create child themes from default HubSpot themes, Asset Marketplace themes, and custom themes.

**Please note:** creating a child theme lets you customize its theme settings without impacting the parent theme settings. However, it won't create clones of each template. If you want to create a copy of all the parent theme assets, including templates, you need to clone the theme. 

Create a child theme in the Design Manager[](https://developers.hubspot.com/docs/cms/building-blocks/themes/child-themes#create-a-child-theme-in-the-design-manager)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can create a child theme in the Design Manager. You will be able to edit the child theme even if the original theme is not editable. The following files will be added to your child theme:

*   `theme.json` - this will include an extends statement for linking to the parent theme.
*   `child.css` and `child.js` - these are empty CSS and JS files. Code added to these files will only affect the child theme. 
*   Any files that contain the [`standard_header_includes` HubL variable](/docs/cms/hubl/variables#required-page-template-variables). This usually includes a "base" or "main" template file. You can [view an example of this on our boilerplate](https://github.com/HubSpot/cms-theme-boilerplate/tree/main/src/templates/layouts).

Learn how to create a child theme from an Asset Marketplace or default HubSpot theme in the [Knowledge Base](https://knowledge.hubspot.com/website-pages/use-themes#create-a-child-theme).

To create a child theme from a custom theme: 

*   In your HubSpot account, navigate to **Marketing > Files and Templates > Design Tools.**
*   In the finder, click the **File** dropdown menu and select **New theme.**
*   Click the **Theme Starting Point** dropdown menu and select **Blank Theme**. 
*   Enter a **name** in the _Theme Label_ field. 
*   To change where the child theme will be saved, click **Change** in the _File location_ section. Click a **folder**, then click **Select**.
*   In the _theme.json_ file, enter a **comma** at the end of line 5, then add a new line below line 5. 
*   On line 6, add an `extends` statement, using a value of the path of the parent theme. 

"extends": "path/to/theme"

*   By default, the child theme will inherit **fields.json** from the parent theme, so you do not need to create a separate **fields.json** for the child theme if you don't plan on updating it.

Create a child theme with the CLI[](https://developers.hubspot.com/docs/cms/building-blocks/themes/child-themes#create-a-child-theme-with-the-cli)
--------------------------------------------------------------------------------------------------------------------------------------------------

You can create a child theme with the CLI. You must complete [the setup process for the CLI](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development) before creating a child theme. Your child theme will inherit the templates and files from the parent theme. You will be able to edit the new theme within the CLI and in the Design Manager.

*   Create a new directory for your theme. 

mkdir cms-project

*   In the new directory, create a copy of the **theme.json** file of the parent theme. 

cd cms-project cp ~/src/cms-sprout-theme/src/theme.json

*   In the copied _theme.json_ file, add a comma to the end of line 5 and a new line below line 5 (or below the final line of the `responsive_breakpoints`, if they are present). 
*   Add an `extends` statement to line 6 (or 14, or the appropriate line for your theme), using a value of the path of the parent theme. 

"extends": "@hubspot/barricade"

*   By default, the child theme will inherit **fields.json** from the parent theme. Consequently, you don't need to create a separate **fields.json** for the child theme if you don't plan on updating it.
*   Upload your new theme and files to your HubSpot account. 

hs upload cms-project cms-project

Limitations[](https://developers.hubspot.com/docs/cms/building-blocks/themes/child-themes#limitations)
------------------------------------------------------------------------------------------------------

The total number of child themes you can have is based on your subscription: 

*   _**Marketing Hub** Professional_ or _**CMS Hub** Professional_: five child themes
*   _**Marketing Hub** Enterprise_ or _**CMS Hub** Enterprise:_ 10 child themes
*   HubSpot's free tools and _**CMS Hub**_ _Starter_: one child theme 

FAQs[](https://developers.hubspot.com/docs/cms/building-blocks/themes/child-themes#faqs)
----------------------------------------------------------------------------------------

1.  **Can I copy a child theme to another HubSpot account if the parent theme is from the Asset Marketplace?**  
    Yes, as long as the “extends” path is the same in the other HubSpot account.
2.  **What assets are inherited from the parent theme?**  
    All files are inherited from the parent theme unless they are overwritten in the child theme.
3.  **How can I override a particular asset from the parent theme?**  
    A file in the same relative path of a child theme will overwrite the equivalent file from the parent theme. So, for instance, to overwrite `@marketplace/parent/theme/templates/about.html` you can create `/child/theme/templates/about.html` and make your edits to the new file. The new file will take effect instead of the inherited file. This applies to your **fields.json** file as well as other files in the theme.
4.  **How can I create new pages using the child theme?**  
    When you create a new page, your child theme will appear as an option under **Your Themes** on the theme selection screen. Learn more about creating pages using themes in the [Knowledge Base.](https://knowledge.hubspot.com/website-pages/create-website-content-using-a-theme)
5.  **How can I edit an existing page to use a child theme instead of the parent theme?**  
    You can replace your page template with the equivalent template from the new theme. For instance, [replace the template](https://knowledge.hubspot.com/cos-general/how-do-i-edit-my-blog-email-page-template#use-a-different-template) `landing-page.html` (in the parent theme) with the template `landing-page.html` (in the new theme).
6.  **How can I edit a template’s label on the page creation screen?**  
    You can change the label of your template by editing the HTML file. The label is located in a comment at the top of your theme file.
7.  **Can I create a child theme from a child theme?**  
    Currently you cannot create a child theme from a child theme.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/building-blocks/themes/child-themes#page-feedback)
----------------------------------------------------------------------------------------------------------------

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