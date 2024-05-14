HubSpot CMS quickstart guide


================================

Last updated: April 24, 2024

HubSpot's CMS is a powerful, flexible platform for creating HubSpot websites, including website pages, blogs, and lightweight apps. It features built-in security and reliability features, along with a globally distributed Content Delivery Network (CDN) that ensures fast page load times.

When developing on the HubSpot CMS, you can use your preferred tools, technologies, and workflows, such as [GitHub](/docs/cms/guides/github-integration), while developing websites. Content creators can then create pages and publish content using drag and drop editors. And because the CMS is integrated with the CRM, you can [create dynamic website experiences](/docs/cms/data/dynamic-pages) for your visitors based on the data you already have.

Before you begin[](https://developers.hubspot.com/docs/cms/guides/getting-started#before-you-begin)
---------------------------------------------------------------------------------------------------

You'll need to do a few things before you start building:

*   Create a free [Developer Sandbox Account](https://app.hubspot.com/signup-hubspot/cms-developers?__hstc=233546881.4c0237b809748eb299763d55eb580290.1632322469269.1632322469269.1634846075686.2&__hssc=233546881.2.1636644675828&__hsfp=163831543) and keep it open in a browser window as you go through this guide.
*   Install [Node.js](https://nodejs.org/en/), which enables HubSpot's local development tools. Versions 10 or higher are supported.

1\. Install the HubSpot CLI[](https://developers.hubspot.com/docs/cms/guides/getting-started#install-the-hubspot-cli)
---------------------------------------------------------------------------------------------------------------------

Once you're ready to begin, open a terminal window and create or navigate to the directory where you want your local HubSpot files to live. This working directory is where the theme and its associated files will be placed.

Next, run `npm install -g @hubspot/cli` to install the HubSpot CLI, which introduces an `hs` command that allows you to easily interact with your HubSpot account.

2\. Configure the local development tools[](https://developers.hubspot.com/docs/cms/guides/getting-started#configure-the-local-development-tools)
-------------------------------------------------------------------------------------------------------------------------------------------------

Run `hs init` to connect the tools to your HubSpot account. This command will walk you through the following steps:

1.  First you’ll be guided to create a personal access key to enable authenticated access to your account via the local development tools. You’ll be prompted to press "Enter" when you’re ready to open the [Personal Access Key page](https://app.hubspot.com/l/personal-access-key) in your default browser. This page will allow you to view or generate your personal access key, if necessary. (Note: You’ll need to select at least the "Design Manager" permission in order to complete this tutorial.) Copy your access key and paste it in the terminal.
2.  Next, you’ll enter a name for the account. This name is only seen and used by you, For example, you might use "sandbox" if you're using a developer sandbox or "company.com" if you’re using a full customer account. This name will be used when running commands.

Once you've completed this simple `init` flow, you'll see a success message confirming that a configuration file, [hubspot.config.yml](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli#authentication), has been created in your current directory.

3\. Create a theme[](https://developers.hubspot.com/docs/cms/guides/getting-started#create-a-theme)
---------------------------------------------------------------------------------------------------

Run `hs create website-theme my-website-theme` to create a `my-website-theme` directory populated with files from the [CMS theme boilerplate](https://github.com/HubSpot/cms-theme-boilerplate).  
  

&nbsp;

![](https://play.vidyard.com/GU2G3DtsUsSEnRM7G5gzM3.jpg)

4\. Upload your theme to HubSpot[](https://developers.hubspot.com/docs/cms/guides/getting-started#upload-your-theme-to-hubspot)
-------------------------------------------------------------------------------------------------------------------------------

Run `hs upload my-website-theme my-website-theme` to upload your new theme to a `my-website-theme` folder in your HubSpot account.

Once this task has completed, you can view these files in the design manager of your HubSpot account. The design manager is an in-app code editor that displays the developer file system, and can be found by navigating to [**Marketing > Files and Templates > Design Tools**](https://app.hubspot.com/l/design-manager/) in the top navigation bar of your account.  
  

&nbsp;

![](https://play.vidyard.com/cVvngaRf4YaufZzmvxSVT1.jpg)

5\. Create a website page[](https://developers.hubspot.com/docs/cms/guides/getting-started#create-a-website-page)
-----------------------------------------------------------------------------------------------------------------

To experience how content creators will use your templates and modules, create a website page using the theme you just uploaded.

*   In your HubSpot account, navigate to [Marketing > Content > Website pages](https://app.hubspot.com/l/website)
*   In the upper right, click **Create**, then select **Website page**.
*   In the dialog box, enter a **name** for your page, then click **Create page**.
*   On the next page, select the **my-website-theme** theme if it's not already selected. Then, hover over the **Homepage** template and click **Select template**.
*   You'll then be brought to the website page editor where you can explore all of the options that content creators will have when working with the template. Learn more about using the editor to build and customize pages on [HubSpot's Knowledge Base](https://knowledge.hubspot.com/website-pages/create-and-customize-pages).  
*   Click the Settings tab in the editor, then select General. Enter a Page title, then set a Content slug to finalize the page's URL. Then, close out the dialog box by clicking **X** or pressing the **Escape key**.
*   In the upper right, click **Publish** to take your page live.

&nbsp;

![](https://play.vidyard.com/nVZcAdpRxY5EB4mV1g8ZBw.jpg)

6\. Edit a CSS file[](https://developers.hubspot.com/docs/cms/guides/getting-started#edit-a-css-file)
-----------------------------------------------------------------------------------------------------

Run `hs watch my-website-theme my-website-theme`. While `watch` is running, every time you save a file, it’ll be automatically uploaded. Open your theme's `/css/components/_footer.css` file in your editor, make a change (such as updating the `.footer__copyright` selector to have `color: red;`), and save your changes. Your terminal will show that the saved file has been uploaded.

Reload your published page to see the CSS change reflected on your website.

What's next?[](https://developers.hubspot.com/docs/cms/guides/getting-started#what-s-next-)
-------------------------------------------------------------------------------------------

You're encouraged to continue to explore and experiment with the boilerplate theme and the page-building experience. The sandbox account you created is yours to play around in and experiment with.

You can checkout [HubSpot's Inspire gallery](https://designers.hubspot.com/inspire/) to see websites, landing pages, and web apps built on HubSpot.

You might also want to check out the following documentation:

*   [CMS developer tutorials](/docs/cms/guides)
*   [HubSpot CMS overview](/docs/cms/key-concepts)

Join the HubSpot CMS developer community[](https://developers.hubspot.com/docs/cms/guides/getting-started#join-the-hubspot-cms-developer-community)
---------------------------------------------------------------------------------------------------------------------------------------------------

Learning is easier when you can learn from those who came before you.

HubSpot is driven by its [Culture Code](https://blog.hubspot.com/blog/tabid/6307/bid/34234/the-hubspot-culture-code-creating-a-company-we-love.aspx), embodied by the attributes in HEART: **H**umble, **E**mpathetic, **A**daptable, **R**emarkable, and **T**ransparent. This culture extends to our ever-growing developer community, with thousands of brilliant and helpful developers around the world. 

### Developer Slack community[](https://developers.hubspot.com/docs/cms/guides/getting-started#developer-slack-community)

Join the [Developer Slack](/slack?__hstc=233546881.1bf222aafec726db12f4514b2e292479.1617243690927.1617243690927.1617243690927.1&__hssc=233546881.1.1617243690928&__hsfp=796281768&_ga=2.856050.2120622895.1617243688-689024450.1617243688) to collaborate with 9,000+ developers and members of the HubSpot product team.

### Developer forums[](https://developers.hubspot.com/docs/cms/guides/getting-started#developer-forums)

Ask questions, learn from fellow developers, and submit ideas in the [CMS developer forums](https://community.hubspot.com/t5/CMS-Development/bd-p/designers_support).

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/getting-started#page-feedback)
---------------------------------------------------------------------------------------------------

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