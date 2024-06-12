---
Please provide me with more context! I need to know what kind of mission you're writing about.  

For example, tell me: "* **What is the mission for?**  (A company, a team, a personal goal, a fictional story, etc.)"
* **What is the overall purpose or objective?**
* **What are the key elements or values that guide the mission?**

Once I have this information, I can help you craft a compelling and impactful mission statement.
---

UI Extensions quickstart guide (BETA)
=====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

This quickstart guide walks through the basic UI extension CRM card sample project, which includes a minimal custom card that sends data from the React front end to the serverless function back end, then displays that data in a success alert. You’ll then customize the card by adding a new component. By the end of this guide, you'll be familiar with the basic processes of developing UI extensions locally with React.

Prerequisites[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#prerequisites)
----------------------------------------------------------------------------------------------------

Before proceeding, ensure that you've [opted in to the CRM development tools beta](/docs/platform/crm-development-tools-overview#get-started).

This guides assumes that you're already familiar with:

*   The basics of React and JavaScript (or optionally Typescript)
*   Using the [HubSpot CLI for local development](/docs/cms/guides/getting-started-with-local-development)
*   [Using a development sandbox](/docs/platform/developer-projects-setup)

1\. Set up your local environment[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#set-up-your-local-environment)
----------------------------------------------------------------------------------------------------------------------------------------

Because UI extensions are developed locally, you'll first need to set up your environment:

*   Install [Node.js](https://nodejs.org/en/download/) which enables HubSpot’s local development tools. Versions 16 or higher are supported.
*   Navigate to the directory where you'll be storing your project, app, and extension files.
*   Run `npm install -g @hubspot/cli@latest` to update the HubSpot CLI to the latest version. 
*   Run `hs init`, then follow the prompts to initialize the HubSpot configuration file to connect the CLI to your HubSpot account. 

After setting up your environment, proceed to the next steps where you'll create your project.

2\. Create a new project[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#create-a-new-project)
----------------------------------------------------------------------------------------------------------------------

*   Create a new project in your working directory. 

hs project create

*   After running the command, you'll be prompted to name the new project, select its location, then select a template. For this guide, select the `Use basic CRM extension card sample project (files only)` template. A new directory will then be created using the project name you assigned.
*   Navigate into the new directory by running `cd <project-directory>`, then run `npm install` to load the dependencies required to start local development server.

cd <project-template-directory> npm install

**Please note:**

*   This sample project automatically includes some of the local dependencies specified in the `package.json` file. If you're modifying these dependencies in other projects, you may need to run `npm install` in both the `src/app/extensions` and `src/app/app.functions` directories.
*   This sample project uses a free API which doesn't require any secret handling. Learn more about [how to include secrets](/docs/platform/serverless-functions#managing-secrets) so that they're accessible during local development and when deployed.

3\. Start local development[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#start-local-development)
----------------------------------------------------------------------------------------------------------------------------

To start local development, you'll use the `hs project dev` command. This command will walk you through setting up a development sandbox and allow you to test changes locally before uploading to your development sandbox or production account.

hs project dev

*   After running `hs project dev`, select the account you want to work in:  
    *   To create your extension in an existing sandbox, use the **arrow keys** to select the **sandbox**, then press **Enter**.
    *   To create and test your extension in a new development sandbox, select **< Test on a new development sandbox >**. Then, name the sandbox and press **Enter**. HubSpot will then create the new development sandbox in the production account. This sandbox will sync with the production account's data, including CRM object definitions and up to 100 of the most recently created contacts and their associated deals, tickets, and companies (up to 100 each).

**Please note:** if you receive the error `The personal access key you provided doesn't include sandbox permissions`, you'll need to deactivate the account's Personal Access Key, then create a new one with sandbox permissions. To do so, run `hs auth`, then follow the prompts to select your account. Then, click **Deactivate** next to the personal access key, and generate a new one with the proper scopes.

*   To create and test your extension in the production account, select `< ! Test on this production account ! >`.

If a project has multiple extensions, you'll be prompted to select which extension to run. You can run multiple extensions from the same app, but not multiple extensions across multiple apps.

Once the project is created, built, and deployed in the selected account, the local development server will start and you can begin building and modifying your extension. 

*   The browser will automatically refresh to pick up the latest saved front end code. This includes changes made to React files and serverless functions. Note that changes to serverless functions will be picked up at invocation time.
*   Changes made to configuration files, such as `app.json` and `hsproject.json`, require a manual upload before you can continue development. To upload those changes, first stop the local development server with `q`, then run `hs project upload`. After your changes are uploaded, run `hs project dev` again to restart the server.

4\. View the extension in HubSpot[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#view-the-extension-in-hubspot)
----------------------------------------------------------------------------------------------------------------------------------------

With the local development server running, you can add the card to the contact record view, then view the custom card:

*   Log in to your HubSpot account.
*   In your HubSpot account, navigate to **Contacts** > **Contacts**. Then, click the **name** of a contact to view its record.
*   At the top of the contact record, click **Customize tabs**. A new tab will open showing the record editor sidebar.  
    ![crm-recrd-customize-tabs](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/crm-recrd-customize-tabs.png?width=588&height=239&name=crm-recrd-customize-tabs.png)
*   In the right sidebar, click **Default view** to edit the default contact record view.
*   For the purposes of this tutorial, click the **\+ plus icon tab** at the top of the editor to add a new tab.  
    ![crm-record-page-editor-add-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/crm-record-page-editor-add-tab.png?width=648&height=308&name=crm-record-page-editor-add-tab.png)
*   In the dialog box, enter a **name** for your new tab, then click **Done**.
*   With the new tab added, click the **Add cards** dropdown menu, then select your **new card**.
*   In the top right, click **Save and exit**.
*   Navigate back to the contact record, then refresh the page. You should now see your new tab, which will contain your new card. With the local development server running, you'll see a _Developing locally_ tag displayed at the top of the card.

![ui-ext-card-quickstart-result](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-card-quickstart-result.png?width=586&height=375&name=ui-ext-card-quickstart-result.png)Learn more about [customizing record views on HubSpot's Knowledge Base](https://knowledge.hubspot.com/crm-setup/customize-the-record-middle-column).

5\. Add a new component to the card[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#add-a-new-component-to-the-card)
--------------------------------------------------------------------------------------------------------------------------------------------

With the card uploaded and local development server running, you'll now add a new [UI component](/docs/platform/ui-components) to the card and refresh the page to see your changes.

Because the React file serves as the extension's front end, you'll find the UI extension components in the `Example.jsx` file in the `app/extensions` directory. For the purposes of this guide, you'll add a `Link` component to link out to the UI extension components reference document.

*   First, add `Link` to the import at the top of the file to make the component available for use.

import { Tile, Button, Text, Input, Stack, hubspot, Link } from '@hubspot/ui-extensions';

*   Then add the `Link` component beneath the `Button` component.

return ( <> <Text> <Text format={{ fontWeight: 'bold' }}> Your first UI Extension is ready! </Text> Congratulations {context.user.firstName}! You just deployed your first HubSpot UI extension. This example demonstrates how you would send parameters from your React frontned to the serverless function and get response back. </Text> <Input name="text" label="Send to serverless" onInput={(t) => setText(t)} /> <Button type="submit" onClick={run}> Click me </Button> <Link href="https://developers.hubspot.com/docs/platform/ui-extension-components"> See all UI extension components </Link> </> );

*   Save your local changes. This will trigger the local development server to update and reload the extension.
*   The CRM record page should now show the new component without requiring a refresh.

![ui-ext-card-quickstart-step-5](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-card-quickstart-step-5.png?width=590&height=422&name=ui-ext-card-quickstart-step-5.png)

Next steps[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#next-steps)
----------------------------------------------------------------------------------------------

Now that you're familiar with the basics of creating, uploading, and updating a UI extension, you can continue customizing the example card with [other UI components](/docs/platform/ui-components), updating the serverless function to [fetch different data](/docs/platform/ui-extensions-overview#fetch-hubspot-crm-data), or [create a new card from scratch](/docs/platform/create-ui-extensions). 

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart#page-feedback)
----------------------------------------------------------------------------------------------------------

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