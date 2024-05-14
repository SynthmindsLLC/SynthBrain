Getting started with modules


================================

Last updated: June 30, 2023

In this tutorial, you'll use the HubSpot CMS boilerplate theme to learn how to create a module and walk through how you can use it in templates and pages as part of a theme. By the end of the tutorial, you'll have created a customer testimonial module that includes a text field, an image field, and a rich text field. 

If this is your first experience with CMS Hub development we recommend:

[Quick start to CMS Hub development](https://developers.hubspot.com/cs/c/?cta_guid=c66b91fb-14b1-4c35-ab0d-7e4af8000592&signature=AAH58kGCK2nKjHn17XzlF09dw6f3mbLI6Q&portal_id=53&pageId=29844694137&placement_guid=28bfd0e9-ec05-48a5-b069-ce20015f54ac&click=58ade738-70ca-427a-a49b-de880e98b0e7&redirect_url=APefjpG2wzbkSMEfKfWOxIv8nHkYQRWKpcCLX6snVA-qDWWI9eAtFpiBBj-X_GQu_LYx9qms4svlGrQcnuasl8HSa6rDSBX-N8mw-1EaRYPAr-DVPm-c-gbop2mlQBV8f2Mdm-oqCVYuGTKBcSQJe9LU-lrVdXWNuQ&hsutk=83d64634269164cb28a107a450d84bfd&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fguides%2Fgetting-started-with-modules&__hstc=20629287.83d64634269164cb28a107a450d84bfd.1715711061876.1715711061876.1715711061876.1&__hssc=20629287.1.1715711061876&__hsfp=1511885054&contentType=standard-page "Quick start to CMS Hub development") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, '28bfd0e9-ec05-48a5-b069-ce20015f54ac', {"useNewLoader":"true","region":"na1"});

**Please note:** if you're looking to develop a module for use in a theme that you want to list on the HubSpot Asset Marketplace, check out the [Asset Marketplace module requirements](/docs/cms/marketplace-guidelines/module-requirements).

Before you get started[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#before-you-get-started)
----------------------------------------------------------------------------------------------------------------------------

Before getting started with this tutorial:

*   Set up a [HubSpot CMS Developer Sandbox](https://offers.hubspot.com/free-cms-developer-sandbox). You can use your existing account instead, but the sandbox will allow you to develop without impacting assets in your main account.
*   Install [Node.js](https://nodejs.org/en/), which enables HubSpot's local development tools. Versions 10 or higher are supported.

If you want to jump ahead, you can preview the finished [project files](https://github.com/HubSpot/cms-modules-getting-started/tree/3b9159334f8c6204c7d2d34d8945d71b6ba402ea). Because the CMS boilerplate theme's code may change over time, only the most critical files that developers will need to create or edit during the tutorial are included. These files include:

1.  **Testimonial.module:** the folder containing the files that make up the custom module you'll build as part of the tutorial.
2.  **homepage.html:** the template that you'll be editing to include the custom module.
3.  **images:** the folder containing the profile pictures you'll use in the module. 

Set up your local development environment[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#set-up-your-local-development-environment)
------------------------------------------------------------------------------------------------------------------------------------------------------------------

During this tutorial, you'll be developing the module locally. To interact with HubSpot in your command line interface, you'll need to install the [HubSpot CLI](/docs/cms/guides/getting-started-with-local-development) and configure it to access your account.

*   In the terminal, run the following command to install the CLI globally. To install the CLI only in your current directory instead, run `npm install @hubspot/cli`.

npm install -g @hubspot/cli

*   In the directory where you'll be storing your theme files, authenticate your HubSpot account so that you can interact with it via the CLI.

hs init

*   Press **Enter** to open the personal access key page in your browser.
*   Select the **account** that you want to deploy to, then click **Continue with this account**. You’ll then be redirected to the personal access key page of the account.
*   Next to _Personal Access Key_, click **Show** to reveal your key. Then click **Copy** to copy it to your clipboard.
*   Paste the copied key into the terminal, then press **Enter**.
*   Enter a unique **name** for the account. This name will only be seen and used by you when running commands. Then, press **Enter**.To connect the local development tools to your account:

You'll then see a success message confirming that the `hubspot.config.yml` file was created.

Add the CMS boilerplate to your account[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#add-the-cms-boilerplate-to-your-account)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Run the command below to create a new theme named `my-theme`. A theme folder named `my-theme` will then be created in your working directory containing the boilerplate assets.

hs create website-theme my-theme

*   Upload the files to your account. 

hs upload <src> <destination>

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`<src>`

 | 

The path to your local files, relative to your current working directory.

 |
| 

`<destination>`

 | 

The destination path in your HubSpot account. This can be a new folder.

 |

For example, `hs upload my-theme my-new-theme` would upload the `my-theme` folder from your machine to a `my-new-theme` folder in HubSpot

By default, HubSpot will upload to the default account in your `hubspot.config,yml` file. However, you can also specify an account by including a `--account=<accountNameOrId>` flag in the command. For example, `hs upload --portal=mainProd`.

Learn more in the [CLI command reference](/docs/cms/developer-reference/local-development-cli).

Create a module in HubSpot[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#create-a-module-in-hubspot)
------------------------------------------------------------------------------------------------------------------------------------

With the CMS boilerplate in your local environment, you'll now create a new module for the theme.

For the purposes of this tutorial, you'll create the module in HubSpot, then pull it down into the theme using the CLI. However, you can also create modules from scratch locally using the [hs create module](/docs/cms/developer-reference/local-development-cli#create-new-files) command.

*   Log in to your HubSpot account, then navigate to the design manager by navigating to **Marketing > Files and Templates > Design Tools**.
*   In the left sidebar of the design manager, open the **theme folder** that you just uploaded. 
*   In the theme folder, open the **modules folder**.
*   In the upper left, click **File > New file** to create a new module in this folder.
*   In the dialog box, click the **dropdown menu**, then select **Module**, then click **Next**.  
    ![new-module-dropdown-menu0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/new-module-dropdown-menu0.png?width=643&name=new-module-dropdown-menu0.png)
*   Select the **Pages** checkbox to make the module available for website and landing pages.
*   Name the module **Testimonial**, then click **Create**.

### Add fields to the module[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#add-fields-to-the-module)

Next, you'll add three fields to the module:

*   A text field to store the name of the customer giving the testimonial.
*   An image field that will store the customer's profile picture.
*   A rich text field that will store the customer's testimonial.

#### Add the text field for customer name

*   In the right sidebar of the module editor, click the Add field dropdown menu, then select Text.  
    ![testimonial-module-add-field](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/testimonial-module-add-field.png?width=344&height=255&name=testimonial-module-add-field.png)
*   In the right sidebar, click the **pencil icon** in the upper right to name the field. For this tutorial, enter the **Customer Name**. You'll then see the HubL variable name change to **customer\_name**.
*   Set the **Default text** to **Sally**.

![Text Field Example](https://developers.hubspot.com/hs-fs/hubfs/Text-Field-3.png?width=385&height=477&name=Text-Field-3.png "Text Field Example")

*   In the right sidebar, click the **breadcrumb** icon to return to the main module menu. ![module-breadcrumb-icon0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/module-breadcrumb-icon0.png?width=354&name=module-breadcrumb-icon0.png)

#### Add the image field for customer profile picture

*   Add another field using the same method, this time selecting the **Image** field type.
*   Label the image field **Profile Picture**, then set the **HubL variable name** to **profile\_pic**.
*   Under **Default image**, select the profile picture provided for Sally in the **images** folder of the completed [project files.](https://github.com/HubSpot/cms-modules-getting-started/tree/3b9159334f8c6204c7d2d34d8945d71b6ba402ea/images)
*   Set the **Alt text** to **Sally Profile Picture**.

![getting-started-with-modules-profile-pic](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/getting-started-with-modules-profile-pic.png?width=345&height=620&name=getting-started-with-modules-profile-pic.png "getting-started-with-modules-profile-pic")

#### Add the rich text field for Sally's testimony

*   Add another field using the same method, this time selecting the **Rich text** field type.
*   Label the rich text field **Testimonial**.
*   Click the **Default rich text** box, then enter "I've had nothing but wonderful experiences with this company."

![Rich Text Field Example](https://developers.hubspot.com/hs-fs/hubfs/Rich-Text-Field-5--.png?width=385&height=693&name=Rich-Text-Field-5--.png "Rich Text Field Example")

So far, you've added data into several module fields. At this point, though, the module doesn't contain any HTML to render that data. In the module editor, this is reflected by the empty state of the `module.html` section.   
![module-html-empty0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/module-html-empty0.png?width=1039&name=module-html-empty0.png)

Next, you'll add HubL to `module.html` to display the field data.

### Add HubL to display field data[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#add-hubl-to-display-field-data)

To display data from the previously created fields, add the following HubL to the `module.html` pane:

<!-- module.html --> {{module.customer\_name}} <img src={{module.profile\_pic.src}} alt="{{module.profile\_pic.alt}}"> {{module.testimonial}}

The above HubL tokens use dot notation to access data from each field. In this case, because we want to pull data from module fields, each token begins with `module`, followed by the field's HubL variable name. You can use dot notation to further access specific properties of a field, which you can see in the `profile_pic` tokens on line 3 above.

*   With the HubL added to your module, click Preview in the upper right to see what the module looks like so far.

![design-manager-previewer](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-manager-previewer.png?width=959&height=430&name=design-manager-previewer.png)

*   Then, in the upper right, click Publish changes.

Having created and published the module in HubSpot, you'll now use the CLI to pull the module down into your local environment so that you can view its contents and make further changes.

View and modify the module locally[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#view-and-modify-the-module-locally)
----------------------------------------------------------------------------------------------------------------------------------------------------

To view the module locally, you'll first need to pull it down to your local theme:

*   In the terminal, run the following command: `hs fetch <hs_src> <destination>`:
    *   `<hs_src>` represents the module's filepath in HubSpot. To get the filepath, you can right-click the module in the left sidebar of the design manager, then select **Copy path**.   
        ![design-manager-copy-path0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/design-manager-copy-path0.png?width=318&name=design-manager-copy-path0.png)
    *   `<destination>` represents the path to the local directory where your theme lives. If omitted, the command will default to the current working directory.

For example, if you're in the working directory already, your fetch command may look similar to the following:

hs fetch my-theme/modules/testimonial.module

### Open the module folder in your local environment[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#open-the-module-folder-in-your-local-environment)

In your preferred code editor, navigate to the module folder you’ve just pulled down from your HubSpot account. Within your module folder, you will see five different files:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`fields.json`

 | 

A JSON object that contains your module’s fields.

 |
| 

`meta.json`

 | 

A JSON object that contains meta information about your module.

 |
| 

`module.css`

 | 

The CSS file that styles your module.

 |
| 

`module.html`

 | 

The HTML and HubL for your module.

 |
| 

`module.js`

 | 

The JavaScript for your module.

 |

You can find more detailed information in our documentation about the [module file structure](//developers.hubspot.com/docs/cms/building-blocks/modules), especially concerning the `fields.json` and `meta.json` files. In this tutorial, we’ll focus on the `fields.json`, `module.css`, and `module.html` files and how they are generated by, downloaded from, and uploaded to the module editor in the Design Manager.

### View the module’s fields.json file[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#view-the-module-s-fields-json-file)

Open the module's `fields.json` file. Aside from some of the `id` numbers, the `src` attribute of the image field, and potentially the order of fields, the file should contain a JSON object similar to the following:

//fields.json \[ { "label": "Customer Name", "name": "customer\_name", "id": "2a025cd5-7357-007f-ae2f-25ace762588e", "type": "text", "required": true, "locked": false, "validation\_regex": "", "allow\_new\_line": false, "show\_emoji\_picker": false, "default": "Sally" }, { "label": "Profile Picture", "name": "profile\_pic", "id": "7877fb84-eb8a-d2c7-d939-77e6e9557d8f", "type": "image", "required": false, "locked": false, "responsive": true, "resizable": true, "default": { "src": "https://cdn2.hubspotqa.net/hubfs/101140939/profile-pic-sally.svg", "alt": "Sally Profile Picture", "width": 100, "height": 100, "max\_width": 100, "max\_height": 100 } }, { "label": "Testimonial", "name": "testimonial", "id": "c5524ece-1ab5-f92d-a5de-e2bf53199dfa", "type": "richtext", "required": false, "locked": false, "default": "<p>I’ve had nothing but wonderful experiences with this company.</p>" } \]

The values for the following fields will match the values you added in step 3:

*   `name`: the name of the field.
*   `label`: the field's label.
*   `default`: the field's default value.  

### View the module's module.html file[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#view-the-module-s-module-html-file)

The `module.html` file should contain the HubL and HTML that you wrote in the HubL + HTML module editor previously.

To make this code more interesting and ready for CSS styling, copy and paste the following code into the file:

<div class="testimonial"> <h1 class="testimonial\_\_header"> {{ module.customer\_name }} </h1> <img class="testimonial\_\_picture" src={{ module.profile\_pic.src }} alt={{ module.profile\_pic.alt }}> {{ module.testimonial }} </div>

Writing your HTML as above uses the [BEM class structure](https://css-tricks.com/bem-101/) in accordance with the HubSpot CMS boilerplate theme's [style guide](https://github.com/HubSpot/cms-theme-boilerplate/blob/master/STYLEGUIDE.md#css-code-formatting).

### View the module’s module.css file[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#view-the-module-s-module-css-file)

The `module.css` file should be empty at this point. To add styling, copy and paste the following code into the file:

.testimonial { text-align: center; } .testimonial\_\_header { font-weight: bold; } .testimonial\_\_picture { display: block; margin: auto; }

After adding the code, save the file.

Push local changes to your HubSpot account[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#push-local-changes-to-your-hubspot-account)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

After saving your local changes, push them back to your HubSpot account.

*   Navigate to your terminal and ensure that you're in the correct directory.
*   Run the watch command to push changes to HubSpot on save: `hs watch <src> <destination>`. 

hs watch my-theme my-theme

Preview your local changes in HubSpot[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#preview-your-local-changes-in-hubspot)
----------------------------------------------------------------------------------------------------------------------------------------------------------

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **Design Tools**.
*   In the left sidebar, navigate to the **theme** you've created, then open the **module** folder and select the **Testimonial** module.
*   With the module open, you should now see your changes in the `module.html` and `module.css` panes.
*   In the upper right, click **Preview**. A new tab will open to display the module preview. 

![Module Preview Example](https://developers.hubspot.com/hs-fs/hubfs/Module-Preview-7.png?width=630&height=537&name=Module-Preview-7.png "Module Preview Example")

To recap this tutorial so far, you have:

*   created a module in HubSpot.
*   pulled that module down to your local environment.
*   made changes to the HubL + HTML and CSS using your local development tools.

In the next part of this tutorial, learn how to use the module in a template.

Add the module to a template[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#add-the-module-to-a-template)
----------------------------------------------------------------------------------------------------------------------------------------

For this part of the tutorial, you'll be working mostly within the `modules` and `templates` folders within your local theme files.   
![theme-folder-structure-getting-started-with-modules0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/theme-folder-structure-getting-started-with-modules0.png?width=219&name=theme-folder-structure-getting-started-with-modules0.png) 

By their most basic definition, modules are editable areas of HubSpot templates and pages. You can insert modules into templates in HubSpot by using the design manager, but here you'll be using HubL to add the module to the template in your local environment.   

*   In your code editor, open the `templates` folder, then open the `home.html` file. 
*   In the `home.html` file, navigate to the final `dnd_section`, which starts around line 28. You'll be adding your new module to this section.  
    ![home-html-add-testimonial-module-to-section0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/home-html-add-testimonial-module-to-section0.png?width=694&name=home-html-add-testimonial-module-to-section0.png)
*   Within this `dnd_section` and above the other `dnd_modules`, copy and paste the following HubL module tag:

{% dnd\_module path= “../modules/Testimonial.module”, offset=0, width=4 %} {% end\_dnd\_module %}

This HubL tag references your new module by its relative file path. To get the module to fit evenly with the other two modules in the `dnd_section`, it also assigns a module `width` and `offset`:

*   HubSpot's CMS uses a [12-column grid system](/docs/cms/building-blocks/templates/drag-and-drop-areas#columns), so to space this module evenly with the other two, you'll need to update each module in the `dnd_section` to have a width of `4`.
*   Then, the first `dnd_module` in the group (`testimonial`) will have an offset of `0` to position it first.
*   The second `dnd_module` (`linked_image`) will have an offset of `4` to position it second.
*   The third `dnd_module` (`rich_text`) will have an offset of `8` to position it third.

After setting the `offset` and `width` of each `dnd_module`, your code will look similar to the following:

{% dnd\_section background\_color="#f8fafc", vertical\_alignment="MIDDLE" %} {% dnd\_module path= “../modules/Testimonial.module”, offset=0, width=4 %} {% end\_dnd\_module %} {% dnd\_module path="@hubspot/linked\_image", img={ "alt": "Stock placeholder image with grayscale geometrical mountain landscape", "loading": "lazy", "max\_height": 451, "max\_width": 605, "size\_type": "auto\_custom\_max", "src": get\_asset\_url("../images/grayscale-mountain.png") }, offset=4, width=4 %} {% end\_dnd\_module %} {% dnd\_module path="@hubspot/rich\_text", html="<h2>Provide more details here.</h2><p>Use text and images to tell your company’s story. Explain what makes your product or service extraordinary.</p>" offset=8, width=4 %} {% end\_dnd\_module %} {% end\_dnd\_section %}

When adding a module to a Drag and Drop area, the module tag does not require a unique name. However, when adding a module to a HTML file outside of Drag and Drop areas, you must assign the module a unique name. You would also use slightly different syntax, such as:

`{% module "testimonial_one" path="../modules/Testimonial.module" %}`

Learn more about [using modules in templates](/docs/cms/building-blocks/modules/using-modules-in-templates).

Preview your changes in HubSpot[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#preview-your-changes-in-hubspot)
----------------------------------------------------------------------------------------------------------------------------------------------

*   If you haven’t kept the watch command running to track your saved work automatically, run hs watch <src> <dest>. Ensure that this command keeps running as you complete the next steps. 
*   In your HubSpot account, open the design manager (**Marketing** > **Files and Templates** > **Design Tools**).
*   In the left sidebar of the design manager, select the **home.html** file.
*   In the upper right, click **Preview**, then select **Live preview with display options** to open the template preview in a new window.

![Live Preview Example](https://developers.hubspot.com/hs-fs/hubfs/Live-Preview-10.png?width=1701&height=951&name=Live-Preview-10.png "Live Preview Example")

*   In the new tab, view the template preview, which should contain your newly added testimonial module.

![testimonial-module-added-to-theme](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/testimonial-module-added-to-theme.png?width=1228&height=393&name=testimonial-module-added-to-theme.png "testimonial-module-added-to-theme")

Customize the module in the template locally[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#customize-the-module-in-the-template-locally)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To make the homepage template more interesting:

*   Navigate back to your code editor, then open the `home.html` file.
*   Add the following parameters to the testimonial module tag:

{% dnd\_module path='../modules/Testimonial.module', customer\_name = "Mary", profile\_pic = { src: "{{ get\_asset\_url('../images/profile-pic-mary.svg') }}", alt: "Mary Profile Picture" }, testimonial = "Wow, what a product! I can't wait to recommend this to all my family and friends!", offset=0, width=4 %} {% end\_dnd\_module %}

The above parameters override the default values that you originally assigned to the three fields. Each parameter uses the HubL variable name that you assigned to each field previously:

*   `customer_name`**:** this parameter passes the name `Mary` to the customer name field, overriding the original value of `Sally`.
*   `profile_pic`**:** this parameter is an object that contains two properties:
    *   The `src` property uses the `get_asset_url` HubL function to retrieve the URL for the new profile picture. Note that the image's file path is relative to your working directory. You'll first need to add this image to the `images` folder in your local theme files. You can find the image in the `images` folder of the completed [project files.](https://github.com/HubSpot/cms-modules-getting-started/tree/3b9159334f8c6204c7d2d34d8945d71b6ba402ea/images)
    *   The `alt` property assigns the image's alt text.
*   `testimonial`**:** this parameter passes new text into the testimonial field.

Alternatively, for the rich text field you could use HubL block syntax to write a large block of HTML or text:

{% dnd\_module path='../modules/Testimonial.module', customer\_name = "Mary", profile\_pic = { src: "{{ get\_asset\_url('../images/profile-pic-mary.svg') }}", alt: "Mary Profile Picture" }, offset=0, width=4 %} {% module\_attribute "testimonial" %} Wow, what a product! I can't wait to recommend this to all my family and friends! {% end\_module\_attribute %} {% end\_dnd\_module %}

Learn more about [module block syntax](/docs/cms/building-blocks/modules/using-modules-in-templates).

If you’ve kept the watch command running in your terminal, saving your changes will send them to HubSpot. You can then navigate back to the design manager to preview the template.

![Mary Module in Template](https://developers.hubspot.com/hs-fs/hubfs/Mary-Module-in-Template-12.png?width=2072&height=916&name=Mary-Module-in-Template-12.png "Mary Module in Template")

Add two more testimonial modules to the template[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#add-two-more-testimonial-modules-to-the-template)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this step, you'll add two more testimonial modules to the template using the same steps as before:

*   Navigate to your code editor, then open the `home.html` file.
*   Under the testimonial module you previous added, add another instance of the module by copying and pasting that module's code. In the new testimonial module, specify the following details using the same steps as above:
    *   The customer's name is `Ollie`.
    *   Ollie's testimonial reads: `I can't believe that I ever conducted business without the use of this product!`
    *   For Ollie's picture, add the relative file path for the file within the `images` folder. You can get the image itself from the finished [project files](https://github.com/HubSpot/cms-modules-getting-started/tree/3b9159334f8c6204c7d2d34d8945d71b6ba402ea). Then give Ollie's image the `alt` attribute of `Ollie Profile Picture`.
    *   To maintain spacing, set `offset` to `4` and `width` to `4`.
*   Underneath the second testimonial module, add a third with the following details:
    *   The customer's name is `Erin`.
    *   Erin's testimony reads: `My business has nearly tripled since I began to use this product! Don't wait, start now!`
    *   For Erin's picture, add the relative file path for the file within the `images` folder. Then give Erin's image the `alt` attribute of `Erin Profile Picture`.
    *   To maintain spacing, set `offset` to `8` and `width` to `4`.

*   Save your changes.

If you’ve kept the `watch` command running in your terminal, you can navigate back to the Design Manager to preview your changes to the template. The template preview should now contain all three testimonial modules.

![testimonial-modules-added-to-theme](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/testimonial-modules-added-to-theme.png "testimonial-modules-added-to-theme")

As a final step, you'll prepare the theme for use in a live page by modifying the `theme.json` file.

Modify the theme name[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#modify-the-theme-name)
--------------------------------------------------------------------------------------------------------------------------

If you'd like to modify the default name of the theme, you can do so by configuring the `name` and `label` fields in the `theme.json` file.

// example theme.json { "name": "my\_first\_theme", "label": "My first theme" }

After adding that code, save your changes so that the `watch` command sends your changes to HubSpot.

Next steps[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#next-steps)
----------------------------------------------------------------------------------------------------

Now that you've created a custom module, added it to the `home.html` template, and optionally customized the theme name, you're ready to create a live page from the theme. 

If you'd like to follow a similar tutorial that focuses on themes, check out the [Getting started with themes tutorial](/docs/cms/guides/getting-started-with-themes) next. Otherwise, you can learn more about [creating and customizing pages](https://knowledge.hubspot.com/website-pages/create-and-customize-pages) in HubSpot's Knowledge Base.

Or, if you'd like to learn more about modules, check out the following module guides:

*   [Configuring a module](/docs/cms/building-blocks/modules/configuration)
*   [Using modules in templates](/docs/cms/building-blocks/modules/using-modules-in-templates)
*   [Default modules](/docs/cms/building-blocks/modules/default-modules)

Other tutorials[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#other-tutorials)
--------------------------------------------------------------------------------------------------------------

*   [Getting started with themes](/docs/cms/guides/getting-started-with-themes)
*   [Getting started with serverless functions](/docs/cms/guides/getting-started-with-serverless-functions)
*   [Creating an efficient developer workflow](/docs/cms/guides/creating-an-efficient-development-workflow)
*   [Getting started with accessibility](/docs/cms/guides/accessibility)
*   [How to use JavaScript frameworks on CMS Hub](/docs/cms/guides/js-frameworks)
*   [How to use web components in custom modules](/blog/use-web-components-in-hubspot-cms-development)
*   [How to build a code block web component based module](/blog/how-to-build-a-code-block-web-component)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-modules#page-feedback)
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