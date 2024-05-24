Serverless functions


========================

Last updated: November 21, 2023

**Please note:** if you're building a serverless function as a part of a [developer project](/platform/create-a-project-for-ui-extensions), visit the [developer projects serverless function documentation](/docs/platform/serverless-functions) instead. The documentation below is for building serverless functions outside of the developer project platform.

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Serverless functions provide a way to write server-side code that interacts with HubSpot and third-party services through [APIs](https://developers.hubspot.com/docs/overview). APIs requiring authentication are not safe for the front-end of a website, as your credentials would be exposed. Serverless functions can act as an intermediary, enabling you to keep credentials secret. 

With serverless functions, you don’t need to spin up and manage new servers. Serverless functions require less overhead and as a result they are easier to scale as a business grows.

You can experiment with serverless functions using a [CMS developer sandbox account](https://app.hubspot.com/signup/standalone-cms-developer?userType=developer). To build your first serverless function, check out the [getting started with serverless functions guide](/docs/cms/guides/getting-started-with-serverless-functions).

Examples[](https://developers.hubspot.com/docs/cms/data/serverless-functions#examples)
--------------------------------------------------------------------------------------

The list of things you can use HubSpot serverless functions for is up to your imagination. You could use them for:

*   Collecting data and storing it in HubDB or the HubSpot CRM
*   Complex data calculators
*   Dynamically displaying data from other systems
*   [Event registration systems](/docs/cms/features/serverless-functions/event-registration-app)
*   Form submissions that send data to other systems

![](https://play.vidyard.com/cTGrp5cXoNrQBrZupnsr2S.jpg)

Using the event registration system example, you could use serverless functions to handle registration and update how many open slots there are for an event. The flow would work as follows:

1.  The website visitor navigates to your event registration page, showing there is room for 15 more people to attend. The visitor fills out a custom form to sign up for the event, and submits.
2.  That submission we've set to send a `POST` request to `yourwebsite.com/_hcms/api/event/participants`. `event/participants` is your serverless function.
3.  Your serverless function receives the user submitted data and takes a few actions before returning a response to the browser:
4.  Submits the form field data to the HubSpot submit form API to add this form submission information to the HubSpot CRM.
5.  Uses the HubDB api, to subtract 1 from the participant count for this event which is stored in HubDB.
6.  Sends a response back to the web browser.
7.  Javascript in the page receives the response from the serverless function and displays a confirmation message to the end-user, and adjusting the count of how many slots are left for participants.

HubSpot’s serverless functions are written in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and use the [NodeJS](https://nodejs.org/en/about/) runtime. HubSpot's serverless functions are intended to be used to add functionality to your HubSpot site, such as supporting advanced form submissions and pulling in data from other APIs. It’s not intended as a generic computing platform where you would run code unrelated to HubSpot.

Limits[](https://developers.hubspot.com/docs/cms/data/serverless-functions#limits)
----------------------------------------------------------------------------------

Serverless functions are intended to be fast and have a narrow focus. That speed enables them to be perfect companions to the front-end of websites and apps, enabling a quick call and response. To maintain performance, HubSpot serverless functions are limited to:

*   50 secrets per account.
*   128MB of memory.
*   no more than 100 endpoints per HubSpot account.
*   the contentType `application/json` when calling a function.
*   6MB per invocation payload, which you might encounter when trying to upload a file with a serverless function, for example.
*   4KB for the amount of data that can be logged. When hitting this limit, it's recommended to log after individual actions, rather than the final output.

### Execution limits

*   Each function has a maximum of 10 seconds of execution time.
*   Each account is limited to 600 total execution seconds per minute.

This means either of these scenarios can happen within one minute:

*   Up to 60 function executions that take 10 seconds each to complete.
*   Up to 6,000 function executions that take 100 milliseconds to complete.

Functions that exceed those limits will throw an error. Execution count and time limits will return a `429` response. The execution time of each function is included in the [serverless function logs](#viewing-serverless-function-logs).

### Split dependencies

Serverless functions don't support splitting JavaScript between multiple files when deployed. Instead, your serverless function must include one JavaScript file to execute the function. If you're building a serverless function with multiple JavaScript files, you should instead copy the shared code into the one JavaScript file, or use [webpack](https://webpack.js.org/) to bundle your code. Learn more about using webpack as a solution on [HubSpot's Community](https://community.hubspot.com/t5/APIs-Integrations/Import-packages-in-serverless-functions/m-p/346620).

Accessing serverless functions[](https://developers.hubspot.com/docs/cms/data/serverless-functions#accessing-serverless-functions)
----------------------------------------------------------------------------------------------------------------------------------

In HubSpot, serverless functions is stored in the [developer file system](/docs/cms/key-concepts#developer-file-system), visible in the [design manager](https://knowledge.hubspot.com/cos-general/a-quick-tour-of-the-design-manager). You can access and edit your serverless functions locally through the CLI. 

For including serverless functions in a developer project, see the [JavaScript building blocks documentation](https://github.hubspot.com/cms-js-building-block-examples/).

### Serverless function folders[](https://developers.hubspot.com/docs/cms/data/serverless-functions#serverless-function-folders)

HubSpot Serverless functions live inside a functions folder. This folder can be named anything, but must contain the suffix `.functions`. Files stored in this folder are not publicly accessible.

Within the functions folder, include your `serverless.json` file along with a [`.js`](#function-js) file which contains your functions. You might consider adding a [README](#readme-md) markdown file to communicate what the functions are for, how they work, and if you have a build process to author them.

![Serverless .functions folder](https://developers.hubspot.com/hubfs/Screen%20Shot%202020-04-03%20at%208.24.31%20AM.png "Serverless .functions folder")

To prevent accidental edits from within the design manager, you can lock your folder. To lock a folder, navigate to the design manager, then right-click the **folder** and select **Lock folder**.

### Serverless.json[](https://developers.hubspot.com/docs/cms/data/serverless-functions#serverless-json)

**Please note:** serverless functions included in [developer projects](/docs/platform/serverless-functions) have been updated as of platform version `2023.2`, including a new `serverless.json` schema. Learn more about [project platform versioning](/docs/platform/platform-versioning).

[`serverless.json`](/docs/cms/features/serverless-functions/reference#serverless-json) is the serverless function's config file which specifies the runtime environment and any [environment variables](https://nodejs.org/docs/latest-v10.x/api/process.html#process_process_env) you plan to use in your functions.

This file also handles the routing of your endpoints. You specify the [endpoint](/docs/cms/features/serverless-functions/reference#endpoints) paths you want to map to your [`function.js`](#function-js) files. For an example of what your `serverless.json` file should look like, view the [serverless functions reference guide](/docs/cms/features/serverless-functions/reference#serverless-json).

### Function.js[](https://developers.hubspot.com/docs/cms/data/serverless-functions#function-js)

Your actual serverless function can be named anything as long as it is a [`.js` file](/docs/cms/features/serverless-functions/reference#function-file). For your serverless function to work, it must be mapped to an endpoint [defined in the `serverless.json` file](/docs/cms/features/serverless-functions/reference#serverless-json). For troubleshooting purposes, it's recommended to name the `.js` file similarly to your endpoint name in your `serverless.json` configuration file. 

Secrets[](https://developers.hubspot.com/docs/cms/data/serverless-functions#secrets)
------------------------------------------------------------------------------------

When authenticating a call made by a serverless function, you should use secrets to store API keys, private app access tokens, and other authentication information for security. This will allow for authentication without exposing your key or access token.

To create and manage secrets, you can use [HubSpot CLI commands](/docs/cms/developer-reference/local-development-cli#serverless-function-commands), such as:

*   `hs secrets add` to create a new secret.
*   `hs secrets list` to view your currently available secrets by name.
*   `hs secrets update` to update an existing secret.

Once added through the CLI, they can be made available to functions by including a `secrets` array containing the name of the secret. This enables you to store your function code in [version control](/docs/cms/guides/github-integration) and use secrets without exposing them. However, you should never return your secret's value through console logging or as a response, as this will expose the secret in logs or in front-end pages that call your serverless function.

**Please note:** due to caching, it can take about one minute to see updated secret values. If you've just updated a secret but are still seeing the old value, check again after about a minute.

Viewing serverless function logs[](https://developers.hubspot.com/docs/cms/data/serverless-functions#viewing-serverless-function-logs)
--------------------------------------------------------------------------------------------------------------------------------------

To help with troubleshooting your serverless functions, the [CLI](/docs/cms/developer-reference/local-development-cms-cli) has an [`hs logs` command](/docs/cms/developer-reference/local-development-cms-cli#logs) which gives you the ability to view your function’s logs. In addition to individual function invocation responses, time of execution, and execution time, any `console.log` statement will also appear in function logs. Do not `console.log` secrets like API keys.

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/serverless-functions#page-feedback)
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