---
Please provide me with more context! I need to know what kind of mission you are writing about. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, a community organization? "
* **What is the main purpose or objective?** What do you want to achieve?
* **What are the values or principles that guide the mission?** 

Once you give me more information, I can help you write a compelling and impactful mission statement.
---

Create private apps with projects (BETA)
========================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

Create private apps to access your HubSpot data through HubSpot's APIs. Private apps can only be installed into the account where they're defined. Serverless functions can [use a private app's access token](/docs/platform/serverless-functions#authenticate-hubspot-api-calls) to authenticate calls to access account data, similar to using an API key but with additional security and usability benefits.

When created as part of a [HubSpot project](/docs/platform/create-a-project), a private app is stored in a folder that contains an `app.json` file, and will also contain extension and serverless function files needed by the app. A project can contain multiple apps, and each app can contain multiple UI extensions.

In this guide, learn how to create a private app in a project and view it in HubSpot. Then, you can [create a UI extension within the app](/docs/platform/create-ui-extensions) to customize the CRM UI.

Create a private app within a project
-------------------------------------

To create a private app in a project, you'll first need to [install the HubSpot CLI](/docs/cms/guides/getting-started-with-local-development). To get started with HubSpot projects, you can also check out the [quickstart guide](/docs/platform/ui-extensions-quickstart).

**Please note:** you can create up to 20 private apps in a HubSpot account, and each app is subject to [HubSpot's API rate limits](/docs/api/usage-details#rate-limits).

To create a private app within your project:

*   Within the `src` folder of your project directory, create a folder for your app.
*   Within the app folder, create an `app.json` file. This file will contain your app definitions.
*   Copy the following code into your `app.json` file:

  

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="width: 100%; padding: 10px 4px;"><code>name</code>&nbsp; <strong>string</strong><p>A unique name for the app.</p></td></tr><tr><td style="width: 100%; padding: 10px 4px;"><code>description</code>&nbsp; <strong>string</strong><p>The app's description.</p></td></tr><tr><td style="width: 100%; padding: 10px 4px;"><code>scopes</code>&nbsp; <strong>array</strong><p>The app's allowed <a href="//developers.hubspot.com/docs/api/working-with-oauth#scopes" rel="noopener">scopes</a>. At least one scope is required.</p></td></tr><tr><td style="width: 100%; padding: 10px 4px;"><code>uid</code>&nbsp; <strong>string</strong><p>The app's uniquely identifying name. This can be any string, but should meaningfully identify the app. HubSpot will identify the app by this ID so that you can change the app's <code>name</code> locally or in HubSpot without removing historical or stateful data, such as logs.</p></td></tr><tr><td style="width: 100%; padding: 10px 4px;"><code>public</code>&nbsp; <strong>boolean</strong><p>Set to <code>false</code> for private apps.</p></td></tr><tr><td style="width: 100%; padding: 10px 4px;"><code>extensions</code>&nbsp; <strong>object</strong><p>Contains the extensions included in the app. For CRM cards, include a <code>crm</code> object, followed by a <code>cards</code> array that contains a <code style="font-size: inherit;">file</code> field that references the CRM card JSON definition file.</p><p>If you have not yet defined your extension, you can leave this object empty.</p></td></tr></tbody></table>

// Example app config file { "name": "Get started App with React", "description": "This is an example of private app that shows a custom card on the Contact record tab built with React-based frontend. This card demonstrates simple handshake with HubSpot's serverless backend.", "scopes": \["crm.objects.contacts.read", "crm.objects.contacts.write"\], "uid": "unique-app-name", "public": false, "extensions": { "crm": { "cards": \[ { "file": "extensions/example-card.json" } \] } } }

Add a serverless function to the app
------------------------------------

Within the private app, you'll add a [serverless function](/docs/platform/serverless-functions#create-a-serverless-function) to serve as your UI extension's back end. Serverless function files are stored in a separate folder within the app folder. 

In the app directory, create a `.functions` directory with the following files:

*   `serverless.json`
*   `package.json`
*   `example-function.js`

The example code below will get you started, but [check out the serverless functions guide](/docs/platform/serverless-functions#create-a-serverless-function) to learn more about authenticating calls, managing secrets, debugging, and more.

### serverless.json[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#serverless-json)

  

<table style="width: 100%; border-collapse: collapse; table-layout: fixed;"><tbody><tr><td style="width: 100%; padding: 10px 4px;"><code>appFunctions</code>&nbsp; <strong>object</strong><p>The object that contains definitions for each serverless function.</p></td></tr><tr><td style="width: 100%; padding: 10px 4px 10px 22px;"><span>⮑&nbsp;</span><code>myFunc</code><span>&nbsp;&nbsp;</span><strong>object</strong><br><p>The object containing the name of the serverless function<span>&nbsp;</span><code>file</code><span>&nbsp;</span>along with any secrets in the<span>&nbsp;</span><code>secrets</code><span>&nbsp;</span>array.</p><p><code>myFunc</code><span>&nbsp;</span>can be any name. You'll later reference this name when using the<span>&nbsp;</span><code>runServerless</code><span>&nbsp;</span>method in your React front end.</p></td></tr></tbody></table>

// Example serverless config file { "runtime": "nodejs18.x", "version": "1.0", "appFunctions": { "myFunc": { "file": "example-function.js", "secrets": \[\] } } }

### package.json[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#package-json)

// Example serverless function package.json { "name": "demo.functions", "version": "1.0.0", "description": "", "main": "index.js", "scripts": { "test": "echo \\"Error: no test specified\\" && exit 1" }, "author": "", "license": "ISC", "dependencies": { "@hubspot/api-client": "^7.0.1", "axios": "^0.27.2" } }

### example-function.js[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#example-function-js)

// Example serverless function exports.main = (context = {}, callback) => { const {text} = context.parameters const ret = \`This is coming from a serverless function! You entered: ${text}\` try { callback(ret); } catch (error) { callback(error); } };

![Screenshot 2023-08-31 at 4.23.46 PM](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/Screenshot%202023-08-31%20at%204.23.46%20PM.png?width=728&height=263&name=Screenshot%202023-08-31%20at%204.23.46%20PM.png)With your app defined and your serverless function configured, upload the project to HubSpot using the `hs project upload` command.  

On upload, the build will be triggered and HubSpot will validate your project files and provision any needed resources. By default, HubSpot will automatically deploy successful builds. Alternatively, you can [link a GitHub repository to the project](/docs/platform/link-a-github-repository-to-a-project) to automatically trigger a new build when you push a change to the project files in GitHub.

With your app uploaded, learn how to view it in HubSpot below. Then, [create a UI extension](/docs/platform/create-ui-extensions) in the app to customize CRM records with various UI components.

View the app in HubSpot[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#view-the-app-in-hubspot)
---------------------------------------------------------------------------------------------------------------------------------

If you're a [super admin](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#super-admin), you can access and manage private apps in your HubSpot account, including viewing your apps, their build history, and the access token required to [make API calls](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token). 

To view a private app's details in HubSpot:

*   In your HubSpot account, navigate to **CRM Development**.
*   In the left sidebar menu, navigate to **Private apps**.
*   Click the **name** of the private app.

You'll then be taken to the app's home page where you can view and manage its access token, view request logs and included extensions, and delete the app. Learn more about each tab below.

### Overview[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#overview)

On the _Overview_ tab, review high-level information about the app's API calls and extension requests and responses.

![private-app-overview-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-overview-tab.png?width=700&height=724&name=private-app-overview-tab.png)

### Auth[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#auth)

On the _Auth_ tab, view authentication-related information, such as the private app's access token and scopes. You can also delete the app from this page.

![private-app-auth-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-auth-tab.png?width=700&height=618&name=private-app-auth-tab.png)

### Logs[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#logs)

On the _Logs_ tab, view detailed information about the app's various calls and events. The tabs under the _Logs_ tab break down different types of events that occur while the app is running, and are helpful for debugging errors that your app might run into.

*   API calls: click the API calls tab to view logs for API calls made by the app.
*   Serverless functions: click the Serverless functions tab to view logs for serverless functions included in the app. Click an event row to view full the log details in the right panel. Log details will also include a _View log trace_ link that you can click to view the log trace, along with a _Trace ID_ that you can copy for use on the _Log Traces_ tab.
*   Extensions: click the Extensions tab to view React top-level event logs, such as a UI extension successfully loading. Click an event row to view log details, including the user who initialized the request. Log details will also include a _View log trace_ link that you can click to view the log trace, along with a _Trace ID_ that you can copy for use on the _Log Traces_ tab.
*   Security: click the Security tab to view security\-related events, such as private app access token viewing and rotating.

![private-app-logs-tab-serverless-functions](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-logs-tab-serverless-functions.png?width=700&height=566&name=private-app-logs-tab-serverless-functions.png)

As an example, say your app is running into an error when trying to retrieve company proximity information through a serverless function. You can click the Logs tab, then click the Serverless functions tab. Then, you can click the errored request to view the log output in the right panel. In the panel, you can then click View log trace for more information. 

![private-app-log-trace-method-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-log-trace-method-1.gif?width=600&height=536&name=private-app-log-trace-method-1.gif)

Alternatively, you can click Copy Trace ID in the log output panel, then use the ID in the _Log Traces_ tab.

![private-apps-log-traces-method-2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-apps-log-traces-method-2.gif?width=600&height=612&name=private-apps-log-traces-method-2.gif) 

### Log Traces[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#log-traces)

On the _Log Traces_ tab, view log traces by trace ID, which you can retrieve from log outputs on the [_Logs_](#logs) [tab](#logs). Log tracing enables you to trace front-end and back-end logs with a single ID, making it easier to debug issues happening in production.

You can also retrieve log IDs on CRM record pages where an extension has failed to load.  
![logger-debug-on-crm-record](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/logger-debug-on-crm-record.png?width=811&height=69&name=logger-debug-on-crm-record.png)

Please note: log tracing is not available for private apps built on [platform version](/docs/platform/platform-versioning) `2023.1`.

 ![private-app-log-traces-output](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-log-traces-output.png?width=700&height=590&name=private-app-log-traces-output.png)

### Extensions[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#extensions)

On the _Extensions_ tab, view information about the extensions that are included in the app.

![private-app-extensions-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-extensions-tab.png?width=700&height=607&name=private-app-extensions-tab.png) 

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/create-private-apps-with-projects#page-feedback)
-------------------------------------------------------------------------------------------------------------------

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