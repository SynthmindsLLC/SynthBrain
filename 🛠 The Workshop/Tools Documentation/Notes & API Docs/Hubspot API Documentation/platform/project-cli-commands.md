---
Please provide me with more context. What is the mission about? 

For example, you could tell me: "* **What is the subject of the mission?** (e.g., a company, a team, a project, a personal goal)"
* **What is the goal of the mission?** (e.g., to improve customer satisfaction, to launch a new product, to achieve a personal fitness goal)
* **What are the specific objectives of the mission?** (e.g., increase sales by 10%, reduce production costs by 5%, run a marathon)

Once you give me more information, I can help you craft a compelling mission statement.
---

Developer projects CLI commands (BETA)
======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The HubSpot CLI connects your local development tools to HubSpot, allowing you to develop on HubSpot with version control, your favorite text editor, and various web development technologies. 

Below, learn about the CLI commands available while you're developing with HubSpot projects. You can also refer to the [standard CLI commands](/docs/cms/developer-reference/local-development-cli) reference for general commands such as `hs auth`.

Update the CLI[](https://developers.hubspot.com/docs/platform/project-cli-commands#update-the-cli)
--------------------------------------------------------------------------------------------------

Update your CLI to the latest version.

npm i -g @hubspot/cli@latest

View all commands[](https://developers.hubspot.com/docs/platform/project-cli-commands#view-all-commands)
--------------------------------------------------------------------------------------------------------

List all project-specific CLI commands.

hs project help

To learn more about a specific command, enter the command followed by `--help`.

Create a new project[](https://developers.hubspot.com/docs/platform/project-cli-commands#create-a-new-project)
--------------------------------------------------------------------------------------------------------------

Create a project in a specified directory. You'll be prompted to give the project a name, as well as confirm the local location. You'll then select whether to start the project from scratch or from a sample template.

A new folder will be created in the specified directory containing an `hsproject.json` file and an `src` folder where you'll build out your [project components](/docs/platform/ui-extension-components). 

Once you've created a project, you can run other project commands inside your project directory and HubSpot will automatically recognize your project.

hs project create

Upload to HubSpot[](https://developers.hubspot.com/docs/platform/project-cli-commands#upload-to-hubspot)
--------------------------------------------------------------------------------------------------------

Upload the project to your HubSpot account and create a build. If the project hasn't been created in the account yet, you'll be asked whether you want to create it.

If the project is configured to auto-deploy, this command will automatically deploy after the build is successful. By default, new projects are set to auto-deploy.

hs project upload

You can upload a project to a specific account in your `hubspot.config.yml` file by adding `--account=accountName` to the command. For example, `hs project upload --account=main`. This can be useful when switching between uploading to a sandbox account and then uploading to the main account. For example, your workflow might look like:

*   When developing your project in a sandbox, you upload changes with `hs project upload--account=sandbox`.
*   Then when uploading the project to a main account, you upload the project with `hs project upload--account=main`.

You can use the same configuration when using the [watch](#watch-for-changes) command.

Deploy to HubSpot[](https://developers.hubspot.com/docs/platform/project-cli-commands#deploy-to-hubspot)
--------------------------------------------------------------------------------------------------------

Manually deploy the most recent build if the project is not set to auto-deploy. 

hs project deploy

You can deploy any build by adding `--buildId=buildID`. For example, `hs project deploy --buildId=123`.

Start a local development server[](https://developers.hubspot.com/docs/platform/project-cli-commands#start-a-local-development-server)
--------------------------------------------------------------------------------------------------------------------------------------

Start a local development server to view extension changes in the browser without needing to refresh. With the server running, saving changes to your extension's front end files and serverless function files will cause the extension to automatically refresh. This does not include changes made to the `.json` config files, which need to be manually uploaded instead.

When a project has multiple extensions, you'll be prompted to select which extensions to run. You can run multiple extensions from the same app, but not multiple extensions across multiple apps.

hs project dev

Open project in HubSpot[](https://developers.hubspot.com/docs/platform/project-cli-commands#open-project-in-hubspot)
--------------------------------------------------------------------------------------------------------------------

Opens the project in HubSpot where you can view the project's settings, build history, and more. By default, will attempt to open the project in the default account set in `hubspot.config.yml`. Specify an account by adding the `--account=accountName` flag.

hs project open

Watch for changes[](https://developers.hubspot.com/docs/platform/project-cli-commands#watch-for-changes)
--------------------------------------------------------------------------------------------------------

Watches the project directory and uploads to HubSpot upon saving, including deleting files. Each upload will result in a new build with a new build ID. A successful build will deploy automatically if the project’s [auto-deploy setting](/docs/platform/build-and-deploy-using-hubspot-projects#builds-and-deploying) is turned on.

hs project watch

You can further configure watch to send changes to a specific account with `---account=accountName`. For example, `hs project watch --account=main`.

View logs[](https://developers.hubspot.com/docs/platform/project-cli-commands#view-logs)
----------------------------------------------------------------------------------------

Get logs for a specific function within a project.

hs project logs

Running this command will guide you through selecting the project, app, and serverless function to get logs for. However, you can also manually specify this information by including the following flags in the command:

Use this table to describe parameters / fields
| Flag | Description |
| --- | --- |
| 
`--project=projectName`

 | 

The name of the project as set in the `hsproject.json` file.

 |
| 

`--app=appName`

 | 

The name of the app as set in the `app.json` file.

 |
| 

`--function=functionName`

 | 

For app functions, the name of the serverless function as set in the `serverless.json` file.

 |
| 

`--endpoint`

 | 

For endpoint functions, the public endpoint path.

 |

Sandbox commands[](https://developers.hubspot.com/docs/platform/project-cli-commands#sandbox-commands)
------------------------------------------------------------------------------------------------------

Interact with [standard sandboxes](https://knowledge.hubspot.com/account/set-up-a-hubspot-standard-sandbox-account) and  [development sandboxes](/docs/platform/developer-projects-setup#create-and-use-development-sandboxes) using the commands below.

### Create a sandbox[](https://developers.hubspot.com/docs/platform/project-cli-commands#create-a-sandbox)

Creates a new sandbox in a production account. When running this command, you can select whether you want to create a standard sandbox or a development sandbox.

A production account can only have one standard sandbox and two development sandboxes at a time. Learn more about [development sandbox limits](/docs/platform/developer-projects-setup#create-and-use-development-sandboxes).

hs sandbox create

### Delete a sandbox[](https://developers.hubspot.com/docs/platform/project-cli-commands#delete-a-sandbox)

Deletes a sandbox connected to the production account. Follow the prompts to select the sandbox account to delete, then confirm the permanent deletion.

hs sandbox delete

### Sync[](https://developers.hubspot.com/docs/platform/project-cli-commands#sync)

Resync CRM object definitions, including properties and property groups, in a standard or development sandbox. 

hs sandbox sync

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/project-cli-commands#page-feedback)
------------------------------------------------------------------------------------------------------

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