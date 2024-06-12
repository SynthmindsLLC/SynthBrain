---
Please provide me with the rest of the mission statement. I need more information to understand the context and purpose of the mission. 

For example, tell me: "* **Who is the mission for?** (A company, a team, an organization, an individual?)"
* **What is the overall goal or purpose?** (To achieve something, to improve something, to create something?)
* **What are the values or principles that guide the mission?** (Innovation, sustainability, social impact, etc.)

Once I have this information, I can help you complete the mission statement and make it clear, concise, and impactful.
---

Optimize your HubSpot development workflow


==============================================

Last updated: April 25, 2024

Setting up an efficient developer workflow will help you work more effectively when building websites on the HubSpot CMS. Depending on the nature of your web development team, or the nature of a specific project, your workflow may differ. 

For example, a single developer building out a new site in a new HubSpot CMS account needs to worry less about testing and collaboration. On the other hand, a team of developers working on a larger website will need a clearer dev and staging process, a deployment workflow, and code living in source control in order to work efficiently.

This guide is designed to walk you through setting up an efficient developer workflow, which you can adapt to fit your needs.

This guide assumes you build websites using the [CMS CLI](/docs/cms/developer-reference/local-development-cms-cli), follow the [getting started with local development](/docs/cms/guides/getting-started-with-local-development) tutorial to get set up. This guide also assumes you've gone through the [quick start guide to developing on the HubSpot CMS](/docs/cms/guides/getting-started#quick_start).

Building with portability in mind[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#building-with-portability-in-mind)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Before we begin setting up our developer workflow, it is important to recognize portability as a key concept in having an efficient developer workflow. The portability of your project ensures it is easy to move between environments with little friction and explanation, making it easy to test and stage changes before taking them live. 

The [CMS Theme Boilerplate](https://github.com/HubSpot/cms-theme-boilerplate) is an example project that is portable, utilizing features like relative file paths, and true file format for all assets in the project using the [CMS CLI](/docs/cms/developer-reference/local-development-cms-cli), which allows it to live in source control and work in any HubSpot account. This project is a great starting or reference point for developers working on a new project. All of the HubSpot default Themes are built using this boilerplate, and can also be used as a portable and effective starting point.

Setting up your development environment[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#setting-up-your-development-environment)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For your individual development environment, each developer on your team should create a free [CMS Developer Sandbox account](https://offers.hubspot.com/free-cms-developer-sandbox). These accounts never expire and have all of the functionality of paid HubSpot CMS accounts (except being able to connect custom domains). 

The CMS CLI makes it easy to interact with multiple HubSpot CMS accounts. Create a new [configuration entry](/docs/cms/developer-reference/local-development-cms-cli) for your CMS Developer Sandbox account. Set the name of the entry for your sandbox to be along the lines of “DEV” or “SANDBOX” so it is clear this account is a development environment. Additionally, set the `defaultPortal` to be your sandbox account, so when you run commands using the CMS CLI, it will automatically interact with your sandbox, and reduce accidental production deploys. At this point, your configuration file will look something like this:

defaultPortal: DEV portals: - name: PROD portalId: 123 authType: personalaccesskey personalAccessKey: >- xxxxx-xxxxxx-xxxxxxx-xxxxxx-xxxxx-xxxxxxx-xxxxxxxx auth: tokenInfo: accessToken: >- xxxxx-xxxxxx-xxxxxxx-xxxxxx-xxxxx-xxxxxxx-xxxxxxxx expiresAt: '2020-01-01T00:00:00.000Z' - name: DEV portalId: 456 authType: personalaccesskey personalAccessKey: >- xxxxx-xxxxxx-xxxxxxx-xxxxxx-xxxxx-xxxxxxx-xxxxxxxx auth: tokenInfo: accessToken: >- xxxxx-xxxxxx-xxxxxxx-xxxxxx-xxxxx-xxxxxxx-xxxxxxxx expiresAt: '2020-01-01T00:00:00.000Z'

Now, when running commands in the CMS CLI, like [`hs upload`](/docs/cms/developer-reference/local-development-cms-cli#upload), if you do not specify a portal, the files will be uploaded to your “DEV” account.

### Setting up your code editor[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#setting-up-your-code-editor)

You can use your preferred code editor when building on HubSpot, whether you prefer [VS Code](#vs-code), or [other code editors and IDEs](#other-code-editors-and-ides).

#### VS Code[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#vs-code)

A significant amount of developers building on HubSpot use [Visual Studio Code](https://code.visualstudio.com/). That inspired the HubSpot VS Code Extension. The extension adds handy intellisense snippets, HubL code completion, HubL syntax highlighting HubL Linting.  The project is [open source](https://github.com/HubSpot/hubspot-cms-vscode) and [contributions are welcome](https://github.com/HubSpot/hubspot-cms-vscode/blob/master/CONTRIBUTING.md). If you have feedback, please [file an issue on the repository](https://github.com/HubSpot/hubspot-cms-vscode/issues).

[Get VS Code Extension](https://developers.hubspot.com/cs/c/?cta_guid=44d37c82-0784-4f60-827f-830acb3cf0b2&signature=AAH58kG04eBTI2fRp4XOMYZbKRFJLmT1Xg&portal_id=53&pageId=29837710042&placement_guid=c0ab15c7-27f7-4f4d-a884-5468e852577a&click=6010fff9-5680-4893-b7ee-197a7bec11ef&redirect_url=APefjpEnumdUXlYaC9T0pbA3ufj9yLS5WNlDf3ZaDixcOMhTW45L49KZzMYrcFiyxJejnYZyV0-TvC4ezJfP_X4PgW9T5prlnGBCOCtO8A_16w0cYFMw1V8bhkfovkGUMfmoLIvggPYG3AjSnjRkggyasXOaENEGueJaBqbEiSHdmwqCyOQOqFY&hsutk=9a7b340a2a160b4a15bf969998da2b21&canon=https%3A%2F%2Fdevelopers.hubspot.com%2Fdocs%2Fcms%2Fguides%2Fcreating-an-efficient-development-workflow&__hstc=20629287.9a7b340a2a160b4a15bf969998da2b21.1715711068441.1715711068441.1715711068441.1&__hssc=20629287.1.1715711068441&__hsfp=1511885054&contentType=standard-page "Get VS Code Extension") hbspt.cta.\_relativeUrls=true;hbspt.cta.load(53, 'c0ab15c7-27f7-4f4d-a884-5468e852577a', {"useNewLoader":"true","region":"na1"});

![vs code extension animated screen capture showing hubl variable suggestion](https://developers.hubspot.com/hubfs/vs%20code%20extension%20-%20hubl%20variable%20suggestion.gif "vs code extension animated screen capture showing hubl variable suggestion")

#### Other code editors and IDEs[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#other-code-editors-and-ides)

While there is an official VS Code extension, there is no reason you can't use a different preferred editor.  HubL is HubSpot's private fork of Jinjava, which is based on Jinja. Because of the similarities in syntax, Jinja syntax highlighting extensions tend to work well. Extensions and add-on tooling vary by editor.

Testing[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#testing)
------------------------------------------------------------------------------------------------------------

There are two main methods for testing changes:

*   **Testing with watch/upload:** When working in your development environment, it is safe to use the [watch](/docs/cms/developer-reference/local-development-cms-cli#watch) command to automatically upload changes when you save files in your text editor to rapidly develop. If you use the Design Manager “Live preview with display options” tool for a template, as you save changes, you will automatically see them reflected in the rendered output of the template preview. To view the live preview of a template, select **Preview > Live Preview** with display options within the template editor of the Design Manager. 
*   **Testing locally:** to preview your changes locally without uploading to the account, you can run the `hs theme preview` command in the theme's root directory. This command will run a local proxy server at [https://hslocal.net:3000/](https://hslocal.net:3000/) which you can then use to preview the theme's templates and modules. Learn more about the [hs theme preview command](/docs/cms/developer-reference/local-development-cli#locally-preview-theme).

#### Editor[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#editor)

Another critical piece of the development phase is testing your changes in the content creation tools. If you are building modules, or templates designed to be manipulated in the content editor, create pages in your development environment to ensure the content editing experience is as you intend it to be. Drag modules around into odd configurations and enter dummy content to make sure marketers can not “break” your modules when building pages. Using the content editors will help illustrate what guardrails you want to build into your templates and modules. Currently, it is not possible to move content, such as pages or blog posts, between HubSpot accounts.

#### Module Preview[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#module-preview)

When in the module editor within the Design Manager, select the “Preview” button. This will open up a preview editor for how the module and its fields will behave in the content editors. This allows you to test the fields, groups, and repeaters in your module with dummy content in a safe environment.

![module preview](https://developers.hubspot.com/hs-fs/hubfs/module-preview.gif?width=1228&height=760&name=module-preview.gif "module preview")

#### Debugging[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#debugging)

Knowing how to debug and troubleshoot issues with your website is critical in the ongoing health and success of your website. Familiarize yourself with [debugging techniques when developing on the HubSpot CMS](/docs/cms/developer-reference/debugging-and-errors).

#### Sandboxes[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#sandboxes)

As noted above in the section about setting up your development environment, you can create free [CMS Developer Sandbox](https://offers.hubspot.com/free-cms-developer-sandbox) accounts to use for testing and as a safe development environment.

Deploying[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#deploying)
----------------------------------------------------------------------------------------------------------------

Once you have tested your changes and are ready to take them live, it is time to deploy your changes to your production portal. Based on your local configuration, you will need to run the CMS CLI command with the `--portal` argument to interact with your production account, such as `hs upload my-theme/src my-theme --portal=PROD`. When uploading files to your production account, pay attention if there were any errors to diagnose, and make sure to briefly browse your live website to make sure there were not any unintended consequences of the deploy. 

If you work as part of a web development team, it is recommended to have your entire production codebase source of truth in version control, and to deploy to your product portal when changes are merged in master. This way, your team of developers can use your favorite version control system to collaborate, track changes and easily roll-back changes. 

To learn more about setting up continuous integration with git repositories, follow this guide on [utilizing GitHub actions to deploy to your production account when changes are merged into master](/docs/cms/guides/github-integration).

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/creating-an-efficient-development-workflow#page-feedback)
------------------------------------------------------------------------------------------------------------------------------

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