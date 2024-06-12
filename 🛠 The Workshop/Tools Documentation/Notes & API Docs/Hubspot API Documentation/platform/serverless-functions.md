---
Please provide me with more information about the mission you want to create. I need context to write a compelling mission statement. 

For example, tell me: "* **What is the mission for?**  (e.g., a company, a project, a team, a personal goal)"
* **What are the core values or goals of this mission?** (e.g., innovation, sustainability, community impact)
* **What are the key activities or outcomes you hope to achieve?** (e.g., develop new technology, improve customer satisfaction, build a stronger community)

The more information you give me, the better I can help you write a powerful and meaningful mission statement.
---

**Please note:** the serverless function features described in this article are specifically for developer projects. This includes both UI extensions and [JavaScript rendered modules and partials built with projects](https://github.hubspot.com/cms-js-building-block-examples/). For information about building serverless functions for websites outside of developer projects, visit the [CMS documentation](/docs/cms/data/serverless-functions).

Include serverless functions in projects (BETA)
===============================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Serverless functions allow you to write server-side code in JavaScript that runs on HubSpot. Because HubSpot runs the function, you don't need to manage your own server. 

In the context of HubSpot projects, serverless functions provide the core functionality for your UI extensions.

Within your project file structure, serverless functions live in the `src/app` directory within a `<AnyName>.functions` folder. At the most basic level, this folder should include:

*   One or more JavaScript files that export a `main` function.
*   A `serverless.json` file that registers and configures your functions. 

![example-project-serverless-structure-simple](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/example-project-serverless-structure-simple.png?width=263&height=243&name=example-project-serverless-structure-simple.png)

Create a serverless function[](https://developers.hubspot.com/docs/platform/serverless-functions#create-a-serverless-function)
------------------------------------------------------------------------------------------------------------------------------

**Please note:** serverless functions have been updated as of [platform version](/docs/platform/platform-versioning) `2023.2`, which was released on November 21, 2023. The documentation below reflects the most up to date serverless function configuration and best practices. Serverless functions created before this will need to be updated to be compatible with the new platform version.

To create a serverless function that provides functionality for your app or extension, you'll first need to create the JavaScript file that provides the functionality.

Each serverless function exports a `main` function that gets called when HubSpot executes it. The function receives the `context` argument, which is an object that contains data based on how the function is being used. This includes context about where the card is loaded as well as the authenticated user and account.

Learn more about [fetching user, account, and card location context](/docs/platform/create-ui-extensions#fetch-account-user-and-extension-context).

Below is an example of data included in `context`:

// example context object data { "user": { "userId": 12345678, "email": "user@example.com", "locale": "en" }, "portalId": 12345, "propertiesToSend": { "city": "Somerville", "hs\_lead\_status": "OPEN\_DEAL" }, "parameters": { "form\_data": { "attending": true, "meal\_choice": "vegetarian" } } }

Below is an example of a function that returns a 200 status code and a _Hello World_ message:

//helloWorld.js exports.main = async (context) => { return ({ statusCode: 200, body: { message: 'Hello World' }, }); };

**Please note:** serverless functions cannot import other functions. You'll need to include all the code the serverless function needs to execute within the serverless function file. 

### Configuration[](https://developers.hubspot.com/docs/platform/serverless-functions#configuration)

In the serverless functions directory, configure the serverless function by including a `serverless.json` file. In this file, you'll configure your serverless function to reference the `.js` function file to execute or the public URL to request. 

**Please note:**

*   To call an endpoint in a serverless function, your account must have either a _**Content Hub**_ _Enterprise_ subscription, a _**Sales Hub** Enterprise_ subscription, or a _**Service Hub**_ _Enterprise_ subscription.
*   Due to system limitations, logs will not be surfaced in HubSpot or the CLI for project-based serverless functions with endpoints. If you want to use serverless functions for CMS use cases and be able to view logs, learn more about [building serverless functions in HubSpot's CMS documentation](/docs/cms/data/serverless-functions).

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>file</code> &nbsp;<strong>string</strong><p>The <code>.js</code> file to execute.</p></td></tr><tr><td style="padding: 10px 4px;"><code>secrets</code> &nbsp;<strong>array</strong><p>If needing to authenticate requests, you can include secrets in this array. Learn more about <a href="#managing-secrets" rel="noopener">managing secrets</a>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>endpoint</code> &nbsp;<strong>object</strong><p>An object containing configuration when you want to hit a public URL. Requires:</p><ul><li><code>path</code>: the endpoint path. See below for more information about URLs for endpoint calls.</li><li><code>method</code>: the request method.</li></ul></td></tr></tbody></table>

// Example serverless.json { "appFunctions": { "functionName": { "file": "function1.js", "secrets": \["SOME\_SECRET"\], "endpoint": { "path": "path/to/endpoint", "method": \["GET"\], } } } }

When calling an endpoint, you can call the function using any [domain connected to your account](https://knowledge.hubspot.com/domains-and-urls/connect-a-domain-to-hubspot) with the following URL structure: `https://<domain>/hs/serverless/<endpoint-path-from-config>`. For example, if both website.com and subdomain.brand.com are connected to the account, you could call the function using `https://website.com/hs/serverless/path/to/endpoint` or `https://subdomain.brand.com/hs/serverless/path/to/endpoint`.

In the URL to call the function, the endpoint path is global rather than scoped to the app or project. If you have identical endpoint paths across multiple apps or projects, the most recently deployed endpoint function will take precedence. 

**Please note:** serverless functions have a response limit of 15 seconds. Functions that take longer to execute will fail. 

Authenticate calls[](https://developers.hubspot.com/docs/platform/serverless-functions#authenticate-calls)
----------------------------------------------------------------------------------------------------------

When developing a private app with projects, each private app comes with a private access token that you can use to authenticate calls to HubSpot's APIs. Calls authenticated with private app access tokens count against your [API call limits](/docs/api/usage-details). You can also authenticate calls using secrets, which you'll [manage through the CLI](#managing-secrets).

For example, when [creating a UI extension](/docs/platform/create-ui-extensions) with [Node.js](/docs/api/client-libraries), you'll first include the HubSpot node API client, then instantiate it within `exports.main` within the CRM card JavaScript file, including the private app access token:

// Include HubSpot node API client const hubspot = require('@hubspot/api-client'); exports.main = async (context = {}) => { // instantiate HubSpot node API client const hubspotClient = new hubspot.Client({ accessToken: process.env\['PRIVATE\_APP\_ACCESS\_TOKEN'\], }); //your function return response; };

You can then configure the rest of the function using Node.js. For example, the following code would create a serverless function that retrieves a specific contact by ID using the [contacts API](/docs/api/crm/contacts):

// Example crm-card.js file // Include HubSpot node API client const hubspot = require('@hubspot/api-client'); exports.main = async (context = {}) => { // Get hs\_object\_id of the record in context const { hs\_object\_id } = context.propertiesToSend; console.log(\`Looking up contact by ID \[${hs\_object\_id}\]\`); // instantiate HubSpot Node API client const hsClient = new hubspot.Client({ accessToken: process.env\["PRIVATE\_APP\_ACCESS\_TOKEN"\] }); try { // Look up contact from the API const response = await hsClient.crm.contacts.basicApi .getById(hs\_object\_id, \['email'\]); // Pass the contact properties back return ({ results: response.properties }); } catch (err) { // Handle API call error console.error(err); // Option 1: Return no result return ({ results: null }); // Option 2: Rethrow the error, which will result in an ERROR status for the function call throw err; } };

To get started, you can find Node.js code snippets on the _Endpoints_ tabs of [HubSpot's API docs.](/docs/api/overview)

### Managing secrets[](https://developers.hubspot.com/docs/platform/serverless-functions#managing-secrets)

If your serverless function requires secrets, include a `secrets` field in the `serverless.json` configuration file. Follow the steps below to make them accessible when the function is deployed and when running the local development server.

*   Create your secrets by running `hs secrets add <secret name>`. HubSpot will securely store this secret on its backend and inject them into the runtime environment when a function is invoked in production.
*   In your `serverless.json` file, list the names of the secrets needed by each function. Do not include `PRIVATE_APP_ACCESS_TOKEN`, as this is automatically created for you and already available in the serverless function.

// serverless.json { "appFunctions": { "functionName": { "file": "function1.js", "secrets": \["GITHUB\_ACCESS\_TOKEN"\], "endpoint": { "path": "path/to/endpoint", "method": \["GET"\] } } } }

*   To make secrets available for local development, create a `.env` file in the `app.functions` directory. HubSpot will never retrieve your secrets outside of its protected infrastructure, so you'll need to specify the secret values that you want to use when the function is executed locally. If your function uses `PRIVATE_APP_ACCESS_TOKEN`, you'll need to copy the private app's access token from HubSpot and store it in the `.env` file for local access. The following snippet demonstrates what an example `.env` file might look like:

PRIVATE\_APP\_ACCESS\_TOKEN=pat-na1-\*\*\*\*\*\* ANOTHER\_SECRET=my-secret-value

*   After saving secrets to the `.env` file, you can access them in your function using `process.env["your-secret-key"]`.

export const main = async (context) => { const secret = process.env\["ANOTHER\_SECRET"\]; const token = process.env\["PRIVATE\_APP\_ACCESS\_TOKEN"\]; ... }

*   To update a secret's value, you can run the `hs secrets update` command. If you're using a Node runtime of 14 or higher, updated secret values will  automatically be updated in your deployed function within one minute, meaning you won't have to build and deploy to get the updated secret.

**Please note:** 

*   To limit exposure of a secret, it's strongly recommended to never include it in console statements to prevent it from being recorded in logs.
*   If your project is [linked to a GitHub repository](https://developers.hubspot.com/docs/platform/link-a-github-repository-to-a-project), be sure to never commit the `.env` file when uploading to GitHub. You can include an entry for `.env` in your `.gitignore` file to ensure that it is omitted from your commits.

Best practices[](https://developers.hubspot.com/docs/platform/serverless-functions#best-practices)
--------------------------------------------------------------------------------------------------

Keep the following recommendations in mind while you develop and test your serverless function:

#### Variable assignment inside functions[](https://developers.hubspot.com/docs/platform/serverless-functions#variable-assignment-inside-functions)

To ensure that variables are correctly assigned and initialized with every function invocation, you should opt to assign variables within the function itself. This practice prevents potential issues related to stale or persistent variable states, which can lead to unexpected behaviors. See the example below for additional context:

// Preferred exports.myHandler = async (event, context) => { const myDynamicVariable = process.env\['SOME\_KEY'\]; // The rest of your handler logic }; // Discouraged const myDynamicVariable = process.env\['SOME\_KEY'\]; exports.myHandler = async (event, context) => { // The rest of your handler logic };

#### Stay up to date with the latest platform version[](https://developers.hubspot.com/docs/platform/serverless-functions#stay-up-to-date-with-the-latest-platform-version)

The `hsprojects.json` configuration file includes a `platformVersion` field which specifies which [platform version](/docs/platform/platform-versioning) to run the project on. It's strongly encouraged to use the latest platform version to ensure that your project and its assets are up to date with the latest improvements, optimizations, and feature enhancements. In addition, some previously available features may not be available in older versions due to deprecation.

The platform version also dictates which version of Node the project runs on. The latest version, `2023.2`, uses Node18, and doesn't support older versions of Node.

Including dependencies[](https://developers.hubspot.com/docs/platform/serverless-functions#including-dependencies)
------------------------------------------------------------------------------------------------------------------

By default, HubSpot provides a small number of [NPM](https://www.npmjs.com/) dependencies in addition to the [Node.js](https://nodejs.org/en/download/) standard library. To add your own dependencies, you can list the package in `dependencies` within the `package.json` file. When the app is built, dependencies will be bundled with your function code. All dependencies must be published to NPM and be public.

For example, if you wanted to add the [lodash](https://www.npmjs.com/package/lodash) library in a serverless function, you would first update `package.json` to include the dependency:

// package.json { "name": "app.functions", "version": "1.0.0", "description": "", "dependencies": { "lodash": "^4.17.21", } }

Then, at the top of your serverless function JavaScript file, you would require the lodash dependency:

// myFunction.js const \_ = require('lodash'); exports.main = async (context) => { const objectA = {}; const objectB = {}; const equal = \_.isEqual(objectA, objectB); return ({ statusCode: 200, body: { isEqual: equal, }, }); };

Debug a serverless function[](https://developers.hubspot.com/docs/platform/serverless-functions#debug-a-serverless-function)
----------------------------------------------------------------------------------------------------------------------------

Log messages are produced every time HubSpot executes a serverless function. Below, learn how to access logs in HubSpot and locally using the CLI.

### In-app debugging[](https://developers.hubspot.com/docs/platform/serverless-functions#in-app-debugging)

In HubSpot, you can view a serverless function's log history, including both successful requests and errors. When a CRM card fails to load, HubSpot will also display an error message in the card on the CRM record that links to that app's CRM card logs. 

![custom-card-error-message](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-card-error-message.png?width=574&name=custom-card-error-message.png)

To access a serverless function's logs in HubSpot:

*   In your HubSpot account, navigate to **CRM Development**.
*   In the left sidebar menu, navigate to **Private apps**.
*   Select the **private app** that contains the serverless function.
*   Click the **Logs** tab, then the **Serverless functions** tab to view serverless function logs.
*   To view logs for a specific request, use the search bar to search by request ID, or click a **request**. 
*   In the right panel, you can also click **View log trace** for a more in-depth breakdown of the request.

![private-app-log-trace-method-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-log-trace-method-1.gif?width=591&height=528&name=private-app-log-trace-method-1.gif)

You can also include `console.log()` in your serverless function code for debugging purposes, then view its output in the function log details sidebar.

![custom-card-error-message-logs-console-log](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-card-error-message-logs-console-log.png?width=1019&name=custom-card-error-message-logs-console-log.png)

### Local debugging[](https://developers.hubspot.com/docs/platform/serverless-functions#local-debugging)

Log messages are produced every time HubSpot executes a serverless function. To view a serverless function's logs for both API endpoint and app functions in the CLI, run the `hs project logs` command. This guide you through selecting the project, app, and function name or endpoint to get logs for. Learn more about using the [hs project logs command](/docs/platform/project-cli-commands#view-logs).

There are two types of log messages produced:

*   Log messages that record the execution of a function, along with its status and timing. For example: `2021-04-28T19:19:21.666Z - SUCCESS - Execution Time: 279ms`
*   Log messages that are produced through console statements in the function code. For example, your serverless function JavaScript might include:

// helloWorld.js exports.main = async (context) => { console.log('Log some debug info'); console.error('An error occurred'); return ({ statusCode: 200, body: { message: 'Hello World' }, }); };

A log output for the above code would then produce the following:

`2021-04-28T19:15:13.200Z    INFO   Log some debug info`

`2021-04-28T19:15:14.200Z    ERROR    An error occurred`

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/serverless-functions#page-feedback)
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