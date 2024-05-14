Create UI extensions with React (BETA)
======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

After creating a [project](/docs/platform/create-a-project) and a [private app](/docs/platform/create-private-apps-with-projects) within it, you can create a UI extension to customize your HubSpot CRM UI. In this guide, you'll learn how UI extensions work and how to build them.

To learn more about configuring UI extensions, check out the [UI extensions SDK reference](/docs/platform/ui-extensions-sdk).

You can also [follow the quickstart guide](/docs/platform/ui-extensions-quickstart) to build and deploy an example UI extension to your account. Or, check out HubSpot's other [sample projects](https://github.com/HubSpot/ui-extensions-examples).

In this guide:

*   [Prerequisites](#prerequisites)
*   [Set up extension files](#set-up-extension-files)
*   [Start local development](#start-local-development)

Prerequisites[](https://developers.hubspot.com/docs/platform/create-ui-extensions#prerequisites)
------------------------------------------------------------------------------------------------

*   This guide assumes that you're familiar with the general steps to set up your local environment with the CLI and configure a development sandbox, if needed. If you haven't done so, [check out the projects setup guide](/docs/platform/developer-projects-setup) before proceeding.
*   Before getting started, [check out the UI extensions overview](/docs/platform/ui-extensions-overview) for general information, best practices, and limitations.
*   You should also ensure you've updated to the latest version of the CLI by running `npm install -g @hubspot/cli@next`.
*   This guide assumes that you've already created a [project](/docs/platform/create-a-project) and a [private app](/docs/platform/create-private-apps-with-projects) within it.

Set up extension files[](https://developers.hubspot.com/docs/platform/create-ui-extensions#set-up-extension-files)
------------------------------------------------------------------------------------------------------------------

Below, learn more about each file along with example code. You can also [follow the quickstart guide](https://developers.hubspot.com/docs/platform/ui-extensions-quickstart) to create these files from an example project, or view HubSpot's other [sample projects](https://github.com/HubSpot/ui-extensions-examples).

Within your project's app directory, create an `/extensions` directory with the following files:

*   `example-card.json`: the custom card configuration.
*   `Example.jsx`: the React file that serves as the front end. You can learn more about how to customize your UI extension front end in the UI extension SDK reference below.
*   `package.json:` metadata about the extension's front end. This file is required and can be used to include dependencies for your React front end.

In the `extensions` directory, you'll also need to install the [HubSpot UI extensions npm package](https://www.npmjs.com/package/@hubspot/ui-extensions) by running `npm i` `@hubspot/ui-extensions`.

#### example-card.json[](https://developers.hubspot.com/docs/platform/create-ui-extensions#example-card-json)

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto;"><tbody><tr><td style="padding: 10px 4px;"><code>type</code> &nbsp; <strong>string</strong><p>The type of extension. Must be <code>crm-card</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>data</code> &nbsp; <strong>object</strong><p>Custom card metadata, including:</p><ul><li><code>title</code> (string): the name of the card.</li><li><code>location</code> (string): where the card appears on the CRM record. Learn more about <a href="#extension-location" rel="noopener">extension location</a>.<ul><li><code>crm.record.tab</code>: places the card on a tab of the middle pane.</li><li><code>crm.record.sidebar</code>: places the card in the right sidebar.</li><li><code>crm.preview</code>: places the card in the right side preview panel that you can access from record pages, index pages, board views, and segments pages.</li></ul></li></ul><ul><li><code>uid</code> (string): the extension's unique identifier. This can be any string, but should meaningfully identify the extension. HubSpot will identify the extension by this ID so that you can change the extension's title without removing historical or stateful data, such as the card's position on the CRM record.</li><li><code>module</code> (object): where the custom card font end React code lives.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>objectTypes</code> &nbsp; <strong>array</strong><p>Defines which types of CRM object records the extension will appear on. This will also enable you to pull data from those records when using the <code>fetchCrmObjectProperties</code> method. Learn more about <a href="#compatible-objects" rel="noopener">compatible objects</a>.</p></td></tr></tbody></table>

// Example extension config file { "type": "crm-card", "data": { "title": "Example Card", "location": "crm.record.tab", "uid": "unique-extension-name", "module": { "file": "Example.jsx" }, "objectTypes": \[{ "name": "contacts" }\] } }

#### Example.jsx[](https://developers.hubspot.com/docs/platform/create-ui-extensions#example-jsx)

// Example React front end import React, { useState } from 'react'; import { Button, Text, Input, Stack, hubspot, } from '@hubspot/ui-extensions'; hubspot.extend(({ context, runServerlessFunction, actions }) => ( <Extension context={context} runServerless={runServerlessFunction} sendAlert={actions.addAlert} /> )); const Extension = ({ context, runServerless, sendAlert }) => { const \[text, setText\] = useState(''); const run = () => { runServerless({ name: 'myFunc', parameters: { text: text } }).then((resp) => sendAlert({ message: resp.response }) ); }; return ( <> <Text> <Text format={{ fontWeight: 'bold' }}> Your first UI Extension is ready! </Text> Congratulations {context.user.firstName}! You just deployed your first HubSpot UI extension. This example demonstrates how you would send parameters from your React frontned to the serverless function and get response back. </Text> <Stack> <Input name="text" label="Send to serverless" onInput={(t) => setText(t)} /> <Button type="submit" onClick={run}> Click me </Button> </Stack> </> ); };

#### package.json[](https://developers.hubspot.com/docs/platform/create-ui-extensions#package-json)

// Example package.json { "name": "example-extension", "version": "0.1.0", "description": "", "license": "MIT", "main": "Example.jsx", "scripts": { "dev": "hs-ui-extensions-dev-server dev", "build": "hs-ui-extensions-dev-server build" }, "repository": { "type": "git", "url": "https://github.com/HubSpot/ui-extensions-react-examples" }, "dependencies": { "@hubspot/ui-extensions": "latest", "react": "^18.2.0" } }

### Compatible objects[](https://developers.hubspot.com/docs/platform/create-ui-extensions#compatible-objects)

You can create extensions for both [standard object](/docs/api/crm/understanding-the-crm) and custom object records. In the [card's JSON configuration file](#example-card-json), you'll define this within the `objectTypes` array. 

When building an extension for custom objects, you'll reference the object as `p_objectName` (case sensitive). To get this value, make a `GET` request to the [custom object schema API](/docs/api/crm/crm-custom-objects), then look for the `fullyQualifiedName` in the response. Take the `fullyQualifiedName`, then remove the HubID number, and use the resulting value for the configuration file.

// example card.json "objectTypes": \[ { "name": "p\_Cats" } \]

For example, for a custom object with the `fullyQualifiedName` of `p123456_Cats`, the correct value to use for the configuration file would be `p_Cats`.

### Extension location[](https://developers.hubspot.com/docs/platform/create-ui-extensions#extension-location)

You can configure where the extension appears in the CRM using the `location` property in the extension's [JSON config file](#example-card-json). Location values include:

*   `crm.record.tab`: places the extension in the middle column of CRM record pages, either in one of HubSpot's default tabs or in a custom tab. If you've customized the middle column previously, you'll need to [customize the middle column view](https://knowledge.hubspot.com/object-settings/customize-the-middle-column-of-records) to make any newly created extensions visible.  
    ![middle-column-example-card](https://developers.hubspot.com/hubfs/Knowledge_Base_2023_2024/middle-column-example-card.png)
*   `crm.record.sidebar`: places the extension in the right sidebar of CRM record pages. Extensions in the sidebar cannot use [CRM data components](/docs/platform/ui-components/crm-data-components).

![right-sidebar-example-card](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/right-sidebar-example-card.png?width=342&height=488&name=right-sidebar-example-card.png)

*   `crm.preview`: places the extension in the preview panel that you can access throughout the CRM. When using this location, the extension will be available when previewing the `objectTypes` specified in the [JSON config file](#example-card-json). This includes previewing records from within CRM record pages, index pages, board views, and the lists tool. Learn more about [customizing previews](https://knowledge.hubspot.com/object-settings/customize-record-previews).  
    ![preview-example-card](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/preview-example-card.png?width=1285&height=1017&name=preview-example-card.png)

Start local development[](https://developers.hubspot.com/docs/platform/create-ui-extensions#start-local-development)
--------------------------------------------------------------------------------------------------------------------

With your project files created locally, you can now use `hs project dev` to upload the files to HubSpot and start a local development server to view the extension in HubSpot.

If your project includes multiple extensions, you can select which extensions you'd like to run locally. The local development server supports running multiple extensions from the same app simultaneously, but you cannot run multiple extensions across different apps at the same time.

hs project dev

*   After running `hs project dev`, select the account you want to work in:  
    *   To create your extension in an existing sandbox, use the **arrow keys** to select the **sandbox**, then press **Enter**.
    *   To create and test your extension in a new development sandbox, select **< Test on a new development sandbox >**. Then, name the sandbox and press **Enter**. HubSpot will then create the new development sandbox in the production account. This sandbox will sync with the production account's data, including CRM object definitions and up to 100 of the most recently created contacts and their associated deals, tickets, and companies (up to 100 each).

**Please note:** when creating a new development sandbox, if you receive the error `The personal access key you provided doesn't include sandbox permissions`, you'll need to deactivate the account's Personal Access Key, then create a new one with sandbox permissions. To do so, run `hs auth`, then follow the prompts to select your account. Then, click **Deactivate** next to the personal access key, and generate a new one with the proper scopes.

*   To create and test your extension in the production account, select `< ! Test on this production account ! >`.
*   If your project has multiple extensions, you'll be prompted to select which extension to run. You can run multiple extensions from the same app, but not multiple extensions across multiple apps.

Once the project is created, built, and deployed in the selected account, the local development server will start and you can begin building and modifying your extension. 

*   The browser will automatically refresh to pick up the latest saved front end code (updates made to the React files).
*   Changes made to configuration files, such as `app.json` and `hsproject.json`, require a manual upload before you can continue development. To upload those changes, first stop the local development server with `q`, then run `hs project upload`. After your changes are uploaded, run `hs project dev` again to restart the server.

Add the card to the record view[](https://developers.hubspot.com/docs/platform/create-ui-extensions#add-the-card-to-the-record-view)
------------------------------------------------------------------------------------------------------------------------------------

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

![ui-ext-card-quickstart-result](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-card-quickstart-result.png?width=586&height=375&name=ui-ext-card-quickstart-result.png)Learn more about configuring UI extensions using the [UI extensions SDK](/docs/platform/ui-extensions-sdk).

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/create-ui-extensions#page-feedback)
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