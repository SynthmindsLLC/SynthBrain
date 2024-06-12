---
Please provide me with more context!  To help me create a compelling mission statement, I need to know: "* **What is the purpose of this mission?**  Is it for a company, a project, a team, or something else?"
* **What are the goals and objectives?** What do you want to achieve?
* **What are the values and beliefs?** What are your guiding principles?
* **Who is the target audience?** Who are you trying to reach with this mission?

Once you give me some more information, I can create a strong and effective mission statement that will inspire and motivate your team.
---

Getting started with serverless functions


=============================================

Last updated: November 21, 2023

**Please note:** if you're building a serverless function as a part of a [developer project](/platform/create-a-project-for-ui-extensions), visit the [developer projects serverless function documentation](/docs/platform/serverless-functions) instead. The documentation below is for building serverless functions outside of the developer project platform.

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

Serverless functions provide a way to write server-side code that interacts with HubSpot and third-party services through [APIs](https://developers.hubspot.com/docs/overview).  APIs requiring authentication are not safe for the front-end of a website, as your credentials would be exposed.

 Serverless functions can act as an intermediary between your front-end and back-end services that require authentication. With serverless functions, developers don’t need to spin up and manage new servers. Serverless functions require less overhead and as a result they are easier to scale as a business grows. We have a [high level overview of what HubSpot serverless functions are and how they work](https://developers.hubspot.com/docs/cms/features/serverless-functions), we recommend reading through before doing this tutorial.

**This tutorial will guide you through the creation of your first serverless function.**

You will create a serverless function folder, set up your configuration folder, create a function and get a response from it.

**What you should do before taking this tutorial:**

*   Have access to a CMS Hub Enterprise account or a [CMS Developer Sandbox account](https://app.hubspot.com/signup/standalone-cms-developer?userType=developer).
*   Ensure you have at least a basic understanding of the [concept of what a serverless function is](https://developers.hubspot.com/docs/cms/features/serverless-functions).
*   Become familiar with the [HubSpot local development tools](https://developers.hubspot.com/docs/cms/guides/getting-started-with-local-development), as they are required for working with serverless functions.
*   Ensure you have the [latest version of the HubSpot local development tools](/docs/cms/developer-reference/local-development-cms-cli#install-or-upgrade).
*   You should already have the local development tools [authenticated with your HubSpot account](https://developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli#auth).

1\. Create a project folder[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#create-a-project-folder)
-----------------------------------------------------------------------------------------------------------------------------------------------

Open your `hubspot.config.yml` file, and make sure your [`defaultPortal`](/docs/cms/developer-reference/local-development-cms-cli#authentication) is set to either your [CMS Developer Sandbox](https://app.hubspot.com/signup/standalone-cms-developer?userType=developer) account or an account with CMS Hub Enterprise.

On your computer, in the folder that contains your [`hubspot.config.yml`](/docs/cms/developer-reference/local-development-cms-cli#authentication) file, **create a** `serverless-tutorial` **folder.** This folder will contain all of our files, both the functions themselves and a template which will use the function. 

In your terminal run the [watch command](//developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli#watch):

hs watch serverless-tutorial serverless-tutorial

This will cause any edits to this folder to result in uploads to the design manager. Since the folder currently has no content, this command will simply state Watcher is ready and watching.

2\. Create a functions folder[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#create-a-functions-folder)
---------------------------------------------------------------------------------------------------------------------------------------------------

Inside of the `serverless-tutorial` folder **create a** `**my-first-function.functions**` **folder.**  
This is similar to custom modules folders which end in `.module`, `.functions` serves to communicate that folder contains serverless functions. Files stored in this folder are not publicly accessible.

Because this folder is currently empty the [`watch`](/docs/cms/developer-reference/local-development-cms-cli#watch) command you have running will not create this folder in the Design Manager yet.

3\. Create a configuration file[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#create-a-configuration-file)
-------------------------------------------------------------------------------------------------------------------------------------------------------

**Create a new file in your** `**my-first-function.functions**` **folder, name it** **`serverless.json`.** `serverless.json` is a required file contained within a `.functions` folder. It serves as a configuration file for serverless functions. Defining the runtime environment, serverless function version, and available endpoints. For a rundown of everything that gets defined in this file, see our [serverless reference](https://developers.hubspot.com/docs/cms/features/serverless-functions/reference).

If you created and saved the file empty, you'll receive an error message in your terminal stating you can't upload an empty `serverless.json` file. That's okay, to ignore because you're going to add that code and then save it - triggering a new upload that will suceed.

**Paste the code below into your serverless.json:**

// place this in your serverless.json file, without this comment { "runtime": "nodejs18.x", "version": "1.0", "endpoints": { } }

**Save the file.**

Keep this file open in your code editor, we will be coming back to it.

Because [`watch`](/docs/cms/developer-reference/local-development-cms-cli#watch) is running, if you refresh your design manager you will now see your `serverless-tutorial` and `my-first-function.functions` folders and your new `serverless.json` file. 

4\. Create a function file[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#create-a-function-file)
---------------------------------------------------------------------------------------------------------------------------------------------

**Create a new file in your** **my-first-function.functions** **folder, name it** **congratulation.js**

This is the actual function file, the file that will execute and perform a task.

**Paste in the code below:**

exports.main = (context, sendResponse) => { // your code called when the function is executed const functionResponse = "Congrats! You've just deployed a Serverless Function." // sendResponse is a callback function you call to send your response. sendResponse({body: functionResponse, statusCode: 200}); };

This serverless function when executed returns a string `"Congrats! You just deployed a Serverless Function."` and a status code of `200`, indicating success.

In a real world scenario it is likely you might use APIs or perform some calculations you don't want public. You would return the result of those calculations or, a simple status code based on how the success of your API transactions.

You are not done yet, there is no way to execute this function just yet.

5\. Register your function in your serverless.json[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#register-your-function-in-your-serverless-json)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Open your `serverless.json` file again. In your file find your `"endpoints"` object.

Update the object to look like this:

// update the endpoints object in your serverless.json to reflect this object. "endpoints": { "congratulation": { "method": "GET", "file": "congratulation.js" } }

The endpoints object contains a `"congratulation"` object. `"congratulation"` is the endpoint you're creating. The endpoint's name is what defines the path that you will use to call your serverless function.

Serverless functions are exposed through **a path at your HubSpot CMS account’s domain.**

These functions can be accessed  at: 

`<https://www.example.com>/_hcms/api/<endpoint-name/path>`

In the case of this "congratulation" endpoint you've created, it will be 

`<https://www.example.com>/_hcms/api/congratulation`

Because of this it is generally a good idea to name your endpoint similarly to your function file's name, and both should be named based on the information they act against, not the action taken against that information. You should use the [HTTP method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) or methods for communicating the type of action you are making against that information. The "method" parameter defines the HTTP method's your function supports. It can be a single string or an array of strings denoting the methods the function supports.

6\. Test your function[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#test-your-function)
-------------------------------------------------------------------------------------------------------------------------------------

The simplest way to test a `GET` request to your serverless function is to go to your endpoint's URL directly in the browser.  
[https://your-domain.com/\_hcms/api/congratulation](https://your-domain.com/_hcms/api/congratulation)

Replacing your-domain.com with your HubSpot site's domain.  
  
You should see `"Congrats! You just deployed a serverless function"`.

Success, you did it!

_If you do not get that response, start from the top of this tutorial carefully reading each step and verifying the code. It is likely instructions in step 4 or 5 were not followed correctly._

For more complicated requests it's helpful to use a tool like [Postman.](https://www.postman.com/downloads/) Postman makes it easier to test and debug APIs. A handy feature for front-end developers is it's [code generation](https://learning.postman.com/docs/postman/sending-api-requests/generate-code-snippets/) which can generate a starting point for your javascript call to your function.

7\. Create a basic template calling your function[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#create-a-basic-template-calling-your-function)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using a new terminal window navigate into your `serverless-tutorial` folder using `cd`.

**Run the following command in your terminal:**

hs create template "test-function"

This creates a `test-function.html` file. **Open this file in your code editor.**

Above the `</head>` tag **add `<script></script>`.**

**Copy the javascript below:**

var requestOptions = { 'method': 'GET', 'headers': { 'Content-Type': 'application/json', } }; fetch("https://www.example.com/\_hcms/api/congratulation", requestOptions) .then(response => response.text()) .then(result => console.log(result)) .catch(error => console.log('error', error));

HubSpot serverless functions only support the content type `application/json`. Leaving it out will result in an "Unsupported Media Type" error.

Inside of the script tag you created earlier, **paste your copied JavaScript code**.

**Change `www.example.com` to your account's domain.**

**Save the file.**

8\. Create a page using the test-function.html template[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#create-a-page-using-the-test-function-html-template)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In the design manager find your `test-function.html` file (you may need to refresh)

**Right click the file, choose "create page"**.

Name your page "Test Function". **Create page**.

**Click preview, preview in new window**. 

Inspect the page by **right clicking anywhere** on the page and **selecting "inspect".**

If you did everything correctly you should see in your console the congratulations message.

**Congratulations, you've called your serverless function from within a HubSpot CMS page.** 

While this tutorial has you call the serverless function at the template level, you can call serverless functions anywhere that you can add JavaScript on your CMS hosted site. The most common place you might do this is within your custom modules.

Debugging your serverless function[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#debugging-your-serverless-function)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

At this stage your serverless function should work fine. The more complicated your function gets, the harder it is to troubleshoot. Just like the console in your browser is useful for debugging javascript on your front-end, you can get similar logs for your serverless functions using [`hs logs`](/docs/cms/developer-reference/local-development-cms-cli#logs). Check out the [local development reference](//developers.hubspot.com/docs/cms/developer-reference/local-development-cms-cli#logs) for more information on this command.

hs logs <endpoint-name> --follow

What did you do?
----------------

You created a serverless function folder, with a serverless.json configuration file, and function file named `congratulation.js`. You used "GET" to get congratulations text from the serverless function. You used javascript to make a call to your serverless function from a page on the HubSpot CMS.

Now that you understand how the configuration file, function file, and `.functions` folder relate, the CLI has a handy command you can use to create your functions faster next time.

hs create function <function name>

This function creates a `.functions` folder, `serverless.json` file and a function file with the names you provide.

Where to go from here?[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#where-to-go-from-here-)
-----------------------------------------------------------------------------------------------------------------------------------------

*   [High level overview of serverless functions](//developers.hubspot.com/docs/cms/features/serverless-functions) on the HubSpot CMS.
*   [Serverless Reference](https://developers.hubspot.com/docs/cms/features/serverless-functions/reference) breaking down the parts of a serverless function
*   [Introduction to HubSpot APIs academy course.](https://academy.hubspot.com/courses/introduction-to-hubspot-apis)
*   [Continuous integration with GitHub](/docs/cms/guides/github-integration)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/guides/getting-started-with-serverless-functions#page-feedback)
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