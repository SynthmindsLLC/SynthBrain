Create a project (BETA)
=======================

Using projects, you can package, build, and deploy to HubSpot locally using the CLI. Depending on your HubSpot subscription, you can use projects to build the following:

*   **CRM UI extensions:** if you have a _**Sales Hub**_ or **_Service_** **_Hub_** _Enterprise_ subscription, you can [build UI extensions to customize CRM records](/docs/platform/create-ui-extensions).
*   **CMS Javascript rendered modules and partials:** all accounts can create projects to [build JavaScript rendered modules and partials for the CMS](https://github.hubspot.com/cms-js-building-block-examples/). However, to include serverless functions that hit public URLs, you'll need a _**Content Hub**_ _Enterprise_ subscription and a _**Sales Hub**_ or _**Service Hub**_ _Enterprise_ subscription.

Once deployed to HubSpot, you can view a project within your HubSpot account to see its build and deploy history, manage its settings, and monitor the private app’s usage. 

This guide walks through how to create a project from scratch. After creating and uploading the project, you'll then [create a private app](/docs/platform/create-private-apps-with-projects) within it, followed by a [custom card UI extension](/docs/platform/create-ui-extensions) or [JavaScript modules and partials](https://github.hubspot.com/cms-js-building-block-examples/).

To get started developing a project, app, and UI extension from a template, check out the [quickstart guide](/docs/platform/ui-extensions-quickstart) instead. You can also view example projects that contain private apps and UI extensions in [HubSpot's example extension library on GitHub](https://github.com/hubspot/ui-extensions-examples).

Create a project[](https://developers.hubspot.com/docs/platform/create-a-project#create-a-project)
--------------------------------------------------------------------------------------------------

To create a project from scratch:

*   In the terminal, navigate to the folder where you'll be storing the project locally. A project can live anywhere locally, but will be stored in HubSpot as a root-level directory in the developer file system.
*   Run `hs project create`.
*   Enter a **name** for your project, then hit **Enter**.
*   Hit **Enter** to create the project with the suggested directory. Or enter a new directory path, then hit **Enter**.
*   Select No template to create a project with no template. You can learn more about getting started with sample projects in the [quickstart guide](/docs/platform/ui-extensions-quickstart). 

A project directory will then be created with the following assets:

*   An `hsproject.json` file in the root directory to configure the project.

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><span style="color: #2e475d; font-family: Lexend Deca, Helvetica Neue, Helvetica, Arial, sans-serif;"><code>name</code> &nbsp;<span style="font-weight: bold;">string</span>&nbsp;</span><p>The project's description.</p></td></tr><tr><td style="padding: 10px 4px;"><span style="color: #2e475d; font-family: Lexend Deca, Helvetica Neue, Helvetica, Arial, sans-serif;"><code>srcDir</code> &nbsp;<span style="font-weight: bold;">string</span></span><p>The name of the directory that contains the rest of your project files.</p></td></tr><tr><td style="padding: 10px 4px;"><span style="color: #2e475d; font-family: Lexend Deca, Helvetica Neue, Helvetica, Arial, sans-serif;"><code>platformVersion</code> &nbsp;<span style="font-weight: bold;">string</span></span><p><span>The <a href="/docs/platform/platform-versioning" rel="noopener">version of the developer project platform</a> you're developing on. As improvements are made and features are added to the projects platform, some might include breaking changes. By specifying a version, you can control which features are accessible in your project. If not specified, the project will fall back to the current version.&nbsp;</span></p></td></tr></tbody></table> 

// Example project config file { "name": "my\_project", "srcDir": "src", "platformVersion": "2023.2" }

*   An `src` folder where you'll store your app's files. This folder can have any name as long as it matches the `srcDir` value in the `hsproject.json` file.

![project-from-scratch](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/project-from-scratch.png?width=490&height=199&name=project-from-scratch.png)

Next, upload the project to HubSpot by running `hs project upload`. This will upload the empty project to your account where you can then view it.

**Please note:** the source directory cannot be greater than 50MB uncompressed, otherwise it will fail to upload.

View the project in HubSpot[](https://developers.hubspot.com/docs/platform/create-a-project#view-the-project-in-hubspot)
------------------------------------------------------------------------------------------------------------------------

To view your deployed project in HubSpot:

*   In your HubSpot account, navigate to **CRM Development**.
*   In the left sidebar menu, navigate to **Projects**. The project card will display a _This project is empty_ message, which is expected because you've uploaded a project without a private app.
*   Click the **name** of the project. The project details page will display information about build history once a private app is added to the project.

From the project details page, you can also manage auto-deploy settings:

*   On the project page, click the **Settings** tab.
*   Click to toggle the **Auto-deploy successful builds** switch off. 

![project-private-app-settings-tab0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/project-private-app-settings-tab0.png?width=748&name=project-private-app-settings-tab0.png)

Next, [create a private app](/docs/platform/create-private-apps-with-projects) in the project to start building out the project's functionality.

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/create-a-project#page-feedback)
--------------------------------------------------------------------------------------------------

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