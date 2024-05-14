Getting started from the CMS quotes theme 


==============================================

Last updated: June 17, 2022

With a CMS quotes theme, you can create a custom quote theme for sales reps to use during the buying process. This guide will walk you through cloning the default CMS quotes theme locally using the CLI, uploading the clone to your account, then making adjustments as needed.  You'll then create a quote using the template to view your work.

Prerequisites[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#prerequisites)
-----------------------------------------------------------------------------------------------------------------------

*   You should feel confident writing HTML and CSS.
*   You should have the latest version of the [HubSpot CLI installed and configured for your portal](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development). 

**Please note:** while this tutorial uses the HubSpot CLI, you can do all of this in HubSpot using the design manager if preferred. To complete this process in HubSpot, you'll just need to clone the `cms-quotes-theme` in the `@hubspot` folder instead of running the `fetch` command. shown in step 1.

1\. Fetching the theme to your local directory[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#fetching-the-theme-to-your-local-directory)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Open your terminal, navigate to the directory you want to download the files to. This will be your main working directory for the remainder of this tutorial. 

To download the default quotes theme, run the following in your terminal:

hs fetch @hubspot/cms-quotes-theme "my-quotes-theme"

You should now see a folder named `my-quotes-theme` in your local file system. This folder contains all of the assets needed for the quote theme, including mock data and module defaults within the `imports` folder.

2\. Upload and watch changes[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#upload-and-watch-changes)
-------------------------------------------------------------------------------------------------------------------------------------------------

With the folder downloaded, upload it to HubSpot. While you can use the [hs upload](/docs/cms/developer-reference/local-development-cli#upload) command to perform a single upload, you can instead use the `watch` command to trigger automatic uploads on each file save:

hs watch "my-quotes-theme" "my-quotes-theme" --initial-upload

After upload, you can now view the `my-quotes-theme` folder in the [design manager](https://app.hubspot.com/l/design-manager/). To open the design manager from the terminal, open a new terminal tab or window and run the `hs open dm` command.

A new terminal tab or window is needed because you cannot run commands while the `hs watch` process is running. You can also press `q` to end the watch, run another command, then rerun `hs watch`.

3\. Open a template preview[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#open-a-template-preview)
-----------------------------------------------------------------------------------------------------------------------------------------------

To preview the quote template:

*   In the design manager, navigate to **my-quotes-theme > templates > bold.html.**
*   In the top right of the code editor, click **Preview**, then select **Live preview with display options**.

With the template preview open, you'll then make a change locally, which will be automatically uploaded on save due to `hs watch` running.

4\. Make a change locally[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#make-a-change-locally)
-------------------------------------------------------------------------------------------------------------------------------------------

*   In your local code editor, open **my-quotes-theme > css > bold.css.**
*   Add the code below to **bold.css**, then save your changes:

.line-items\_\_table tbody tr:nth-child(odd){ background-color: #d6d6d6; }

*   Refresh the template preview in your browser to view your CSS changes. You should now see that every odd row in the table body has a gray background. 

As you build your custom quote theme, you can repeat this workflow to quickly confirm the changes that you're making locally.

**Please note:** because of the complexity of the signature system, signatures will not display in previews.

5\. Change the template label[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#change-the-template-label)
---------------------------------------------------------------------------------------------------------------------------------------------------

As you prepare a custom quotes theme for real life use, you should be mindful of the template label so that sales reps can easily find it among HubSpot's default quote options.

To change a quote template's label:

*   In your code editor, open **my-quotes-theme > templates > bold.html**.
*   At the top of the file, view the template annotation:

<!-- templateType: quote isAvailableForNewContent: true label: Bold -->

*   Update the `label` parameter from `Bold` to a name of your choosing, such as **`My custom quote template`**.
*   Save the file to upload it to HubSpot.

6\. Customize the quote template in HubSpot[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#customize-the-quote-template-in-hubspot)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Before a sales rep can use your quote template, it must be customized in HubSpot. This would typically be done by a sales manager so that they can [create ready-made quotes for their sales team](https://knowledge.hubspot.com/deals/create-custom-quote-templates). However, in this tutorial, you'll walk through this process yourself so that you can understand what the content creation experience is like.

To customize the quote template and make it available for sales reps:

*   In your HubSpot account, click the settings **settings icon** in the main navigation bar.
*   In the left sidebar menu, navigate to **Objects > Quotes**.
*   Click the **Quote templates** tab.
*   In the upper right, click **Customize quote template.**
*   Hover over your new **template**, then select **Choose**.
*   Using the left panel, you can edit the modules included in the template. For example, you can click a **module** to edit its properties or toggle visibility.

![quote-template-toggle-visibility](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/quote-template-toggle-visibility.png?width=528&name=quote-template-toggle-visibility.png)

*   In the upper right, click **Save** when you're done making changes.

7\. Create a quote using your new template[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#create-a-quote-using-your-new-template)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With your changes saved, you can now create a quote with the template, simulating the sales rep experience.

*   In your HubSpot account, navigate to **Sales > Quotes**. 
*   In the upper right, click **Create quote**. You'll then be redirected to a quote creation wizard. 
*   On the first screen, click the **Associate with a deal** dropdown menu, then either select an existing deal or select **Create a new deal** if you want to use a test deal instead.
*   In the bottom right, click **Next**.
*   On the next screen, click the **Quote** dropdown menu, then select your custom quote template.
*   Proceed through the rest of the quote wizard to create your quote.
*   After publishing the quote, a dialog box will appear with a link to view the quote. Click **Copy** to copy the URL, then paste it into your browser to view the completed quote.

![copy-quote-url](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/copy-quote-url.png?width=527&name=copy-quote-url.png)

Next steps[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#next-steps)
-----------------------------------------------------------------------------------------------------------------

With your quote template created, uploaded, and customized, you should now have a better understanding of the quote template editing process and the content creator experience.

As you create quote templates to fit your business needs, you may want to try adding your own custom modules to the quote along with HubSpot's default modules. 

**Please note:** it's recommended to not edit the JavaScript of the payment, signature, and download modules, as this could lead to breaking the modules. If broken, the end-user might not be able to sign it, download it, or even make a payment.

Related Resources[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#related-resources)
-------------------------------------------------------------------------------------------------------------------------------

*   [Custom quote templates](/docs/cms/building-blocks/templates/quotes)
*   [Custom quote variable reference](/docs/cms/hubl/variables/quotes)
*   [Create and use custom quote templates (from the sales, sales ops/manager perspective)](https://knowledge.hubspot.com/deals/create-custom-quote-templates-beta)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/getting-started-from-the-cms-quotes-theme#page-feedback)
-----------------------------------------------------------------------------------------------------------------------------

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