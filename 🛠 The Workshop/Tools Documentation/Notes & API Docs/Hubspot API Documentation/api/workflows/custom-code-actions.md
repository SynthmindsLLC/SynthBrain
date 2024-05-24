Custom code workflow actions
============================

In workflows, use the _Custom code_ action to write and execute JavaScript or Python (_in beta_). With custom code actions, you can extend workflow functionality within and outside of HubSpot. To learn more about HubSpot's APIs, you can refer to either the [developer documentation](https://developers.hubspot.com/docs/api/developer-guides-resources) for the latest versions or the [legacy developer documentation](https://legacydocs.hubspot.com/) for our older APIs. To see examples of common custom code actions, view [HubSpot's Programmable Automation Use Cases](https://www.hubspot.com/programmable-automation-use-cases).

Custom code actions support JavaScript using the [Node 16.x runtime framework](https://aws.amazon.com/blogs/compute/node-js-16-x-runtime-now-available-in-aws-lambda/). If you're using Python for your custom code action, the custom code action will use [Python 3.9 runtime framework](https://www.python.org/downloads/release/python-390/). When an action executes, the runtime compute is managed through a serverless function by HubSpot and [AWS Lambda](https://aws.amazon.com/lambda/features/#:~:text=AWS%20Lambda%20is%20a%20serverless,scale%2C%20performance%2C%20and%20security.).

If you encounter any general issues implementing your custom code action, you can reach out to [HubSpot support](https://knowledge.hubspot.com/account/get-help-with-hubspot). However, if you're facing any issues with your written custom code, it's recommended to search and post on the [HubSpot Developer's Forum](https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers) to get tips, advice, or help with troubleshooting your code.

Node.js supported libraries
---------------------------

If you're using Node.js, the following libraries are available for use within the code action. These libraries can be loaded using the normal `require()` function at the top of your code.

*   @hubspot/api-client ^10
*   async ^3.2.0
*   aws-sdk ^2.744.0
*   axios ^1.2.0
*   lodash ^4.17.20
*   mongoose ^6.8.0
*   mysql ^2.18.1
*   redis" ^4.5.1
*   request" ^2.88.2
*   bluebird ^3.7.2
*   random-number-csprng ^1.0.2
*   googleapis ^67.0.0

**Please note:** the v4 Associations API is supported in Version 9.0.0 or later of the NodeJS HubSpot Client and in Version 8 of the NodeJS HubSpot Client.

Python supported libraries
--------------------------

If you're using Python, you can load the following libraries with an import statement at the top of your code. The import statement should be formatted as `from [libraryname] import [item]`, such as  `from redis.client import redis`.

*   requests 2.28.2
*   @hubspot/api-client ^8
*   google-api-python-client 2.74.0
*   mysql-connector-python 8.0.32
*   redis 4.4.2
*   nltk 3.8.1

If you're using anything from the standard library, you can use `import`, such as  `import os`.

Get started
-----------

Use the code samples below to begin using custom code workflow actions. 

### Code samples

NODE16X, v8

const hubspot = require('@hubspot/api-client'); exports.main = async (event, callback) => { /\*\*\*\*\* How to use secrets Secrets are a way for you to save API keys or private apps and set them as a variable to use anywhere in your code Each secret needs to be defined like the example below \*\*\*\*\*/ const hubspotClient = new hubspot.Client({ accessToken: process.env.SECRET\_NAME }); let phone; try { const ApiResponse = await hubspotClient.crm.contacts.basicApi.getById(event.object.objectId, \["phone"\]); phone = ApiResponse.properties.phone; } catch (err) { console.error(err); // We will automatically retry when the code fails because of a rate limiting error from the HubSpot API. throw err; } /\*\*\*\*\* How to use inputs Inputs are a way for you to take data from any actions in your workflow and use it in your code instead of having to call the HubSpot API to get that same data. Each input needs to be defined like the example below \*\*\*\*\*/ const email = event.inputFields\['email'\]; /\*\*\*\*\* How to use outputs Outputs are a way for you to take data from your code and use it in later workflows actions Use the callback function to return data that can be used in later actions. Data won't be returned until after the event loop is empty, so any code after this will still execute. \*\*\*\*\*/ callback({ outputFields: { email: email, phone: phone } }); } /\* A sample event may look like: { "origin": { // Your portal ID "portalId": 1, // Your custom action definition ID "actionDefinitionId": 2, }, "object": { // The type of CRM object that is enrolled in the workflow "objectType": "CONTACT", // The ID of the CRM object that is enrolled in the workflow "objectId": 4, }, "inputFields": { // The property name for defined inputs }, // A unique ID for this execution "callbackId": "ap-123-456-7-8" } \*/

NODE16X, v3

const hubspot = require('@hubspot/api-client'); exports.main = async (event, callback) => { /\*\*\*\*\* How to use secrets Secrets are a way for you to save API keys or private apps and set them as a variable to use anywhere in your code Each secret needs to be defined like the example below \*\*\*\*\*/ const hubspotClient = new hubspot.Client({ apiKey: process.env.SECRET\_NAME }); let phone; try { const ApiResponse = await hubspotClient.crm.contacts.basicApi.getById(event.object.objectId, \["phone"\]); phone = ApiResponse.body.properties.phone; } catch (err) { console.error(err); // We will automatically retry when the code fails because of a rate limiting error from the HubSpot API. throw err; } /\*\*\*\*\* How to use inputs Inputs are a way for you to take data from any actions in your workflow and use it in your code instead of having to call the HubSpot API to get that same data. Each input needs to be defined like the example below \*\*\*\*\*/ const email = event.inputFields\['email'\]; /\*\*\*\*\* How to use outputs Outputs are a way for you to take data from your code and use it in later workflows actions Use the callback function to return data that can be used in later actions. Data won't be returned until after the event loop is empty, so any code after this will still execute. \*\*\*\*\*/ callback({ outputFields: { email: email, phone: phone } }); } /\* A sample event may look like: { "origin": { // Your portal ID "portalId": 1, // Your custom action definition ID "actionDefinitionId": 2, }, "object": { // The type of CRM object that is enrolled in the workflow "objectType": "CONTACT", // The ID of the CRM object that is enrolled in the workflow "objectId": 4, }, "inputFields": { // The property name for defined inputs }, // A unique ID for this execution "callbackId": "ap-123-456-7-8" } \*/

PYTHON (same for all versions)

import os from hubspot import HubSpot from hubspot.crm.contacts import ApiException def main(event): # How to use secrets # Secrets are a way for you to save API keys or private apps and set them as a variable to use anywhere in your code # Each secret needs to be defined like the example below hubspot = HubSpot(access\_token=os.getenv('SECRET\_NAME')) phone = '' try: ApiResponse = hubspot.crm.contacts.basic\_api.get\_by\_id(event.get('object').get('objectId'), properties=\["phone"\]) phone = ApiResponse.properties.get('phone') except ApiException as e: print(e) # We will automatically retry when the code fails because of a rate limiting error from the HubSpot API. raise # How to use inputs # Inputs are a way for you to take data from any actions in your workflow and use it in your code instead of having to call the HubSpot API to get that same data. # Each input needs to be defined like the example below email = event.get('inputFields').get('email') # How to use outputs # Outputs are a way for you to take data from your code and use it in later workflows actions # Use the callback function to return data that can be used in later actions. # Data won't be returned until after the event loop is empty, so any code after this will still execute. return { "outputFields": { "email": email, "phone": phone } } # A sample event may look like: # { # "origin": { # # Your portal ID # "portalId": 1, # # Your custom action definition ID # "actionDefinitionId": 2, # }, # "object": { # # The type of CRM object that is enrolled in the workflow # "objectType": "CONTACT", # # The ID of the CRM object that is enrolled in the workflow # "objectId": 4, # }, # "inputFields": { # # The property name for defined inputs # }, # # A unique ID for this execution # "callbackId": "ap-123-456-7-8" # }

Create a custom code action[](https://developers.hubspot.com/docs/api/workflows/custom-code-actions#create-a-custom-code-action)
--------------------------------------------------------------------------------------------------------------------------------

To add a custom code action to a workflow:

*   In your HubSpot account, navigate to **Automation** \> **Workflows**.
*   Click the **name** of a workflow, or [create a new workflow](https://knowledge.hubspot.com/workflows/create-workflows). 
*   Click the **\+** **plus** **icon** to add a workflow action.
*   In the right panel, select **Custom code**.

   

![custom-code-action-select](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/custom-code-action-select.png?width=420&name=custom-code-action-select.png)

*   In the right panel, set up your action:
    *   By default, custom code actions will use **Node.js 16.x**. If you’re in the Python beta and want to build your action with Python, click the **Language** dropdown menu, then select **Python**.
    *   To add a new [secret](#secret), such as a [private app access token](/docs/api/private-apps), click **Add secret**. The app must include the respective scopes of any data that you're trying to pull from HubSpot, such as `contacts` or `forms`.  Learn more about [HubSpot private apps](/docs/api/private-apps).
    *   In the dialog box, enter the **Secret name** and **Secret value**.
    *   Click **Save**. You can now select this secret in future custom code actions.
    *   To edit or delete existing secrets, click **Manage secrets**.
*   To include properties in your custom code, click the **Choose property** dropdown menu, then select a **property**. You can use existing properties or [previously formatted property values](https://knowledge.hubspot.com/workflows/format-your-data-with-workflows) in the workflow. After selecting your property, enter a Property **name** to use in your code. Learn how to [reference a property in your custom code](#add-hubspot-properties-to-your-custom-code).
*   To add another property, click **Add property**. Each property can only be added once and must have a unique _Variable ID_.  You can use up to 50 properties with your custom code. 
*   To delete a property,  click the **delete** icon.
*   In the **code field**, enter your JavaScript or Python.
*   To define data outputs that can be used as inputs later in the workflow, for example with a [_Copy property value_](https://knowledge.hubspot.com/workflows/choose-your-workflow-actions#copy-a-property-value) action:
    *   Under _Data outputs_, click the **Data type** dropdown menu, and select a type of data.
    *   In the **Name** field, enter a name for the data output.
    *   To add multiple outputs, click **Add output**.
*   Click **Save**.

![workflow-custom-code](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/workflow-custom-code.png?width=707&height=405&name=workflow-custom-code.png)

**Please note:** the code field will not display lint errors when using Python. 

When building custom code actions, keep the following in mind: 

*   The `def main(event):` function is called when the code snippet action is executed.
*   The event argument is an object containing details for the workflow execution.
*   The `callback()` function is used to pass data back to the workflow. It should be called in the `exports.main` function. This can only be used with Node.js.   
      
    

The `event` object will contain the following data:

//example payload { "origin": { // Your portal ID "portalId": 1, // Your custom action definition ID "actionDefinitionId": 2, }, "object": { // The type of CRM object that is enrolled in the workflow "objectType": "CONTACT", // The ID of the CRM object that is enrolled in the workflow "objectId": 4, }, // A unique ID for this execution. "callbackId": "ap-123-456-7-8" }

Test the action
---------------

When adding a custom code action to a workflow, you can test the action to ensure that your code runs as expected before turning the workflow on.

When testing a custom code action, you'll start by selecting a record to test the code with, then run the code. This test will run only the code in your custom action, not any of the other actions in the workflow. When the code is finished running, you'll be able to view the code outputs and the log of your test.

**Please note:** when testing your custom code, the code will run and any changes will apply to the selected test record. It's recommended to create a dedicated test record if you want to avoid updating your live records. 

To test a custom code action:

*   In the workflow timeline, click the **custom code action**.
*   At the bottom of the right sidebar, click **Test action** to expand the testing section.  
    ![workflow-custom-code-test-expand](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/workflow-custom-code-test-expand.png?width=453&name=workflow-custom-code-test-expand.png)
*   Select a record to test your code with by clicking the **\[Object\]** dropdown menu, then selecting a **record**.  
    ![workflow-custom-code-action-test2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/workflow-custom-code-action-test2.png?width=444&name=workflow-custom-code-action-test2.png)
*   If you're using [previously formatted property values](/workflows/format-your-data-with-workflows) in the workflow, enter a test value for the formatted data.   

![](https://developers.hubspot.com/hubfs/image-png-Oct-22-2021-04-16-00-53-AM.png)

*   To run the code, click **Test**.
*   In the dialog box, confirm that you want to test your code against the selected record by clicking **Test**.
*   Once your code is done running, the sidebar will display the results of your test:
    *   **Status:** the success or failure status of your custom code action.
    *   **Data outputs:** the values that resulted for your defined data outputs. An alert will display next to any outputs that the code generated which weren't defined either in the _Data outputs_ section or in the code editor. You'll need to add those outputs in order to use them later in the workflow.
    *   **Logs:** information about the test itself, such as how much memory the action took to execute and the total runtime.   
          
        ![workflow-custom-code-action-test0results0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/workflow-custom-code-action-test0results0.png?width=451&name=workflow-custom-code-action-test0results0.png)
*   To update your custom code action, click **Create** **action** to expand the action editor. Continue to update and test your code as needed.
*   When you're done testing the action, click **Save** to save your changes.

Secrets[](https://developers.hubspot.com/docs/api/workflows/custom-code-actions#secrets)
----------------------------------------------------------------------------------------

There are times you will want your code to reference something that shouldn't be widely shared. Most often, this is a means of authentication, like a [private app access token](/docs/api/private-apps). You can manage the secrets your function has access to directly in the workflow action definition. When using multiple secrets within a custom code, the total length of all secret values must not exceed 1000 characters.

![workflow-custom-code-secrets](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/workflow-custom-code-secrets.png?width=440&height=473&name=workflow-custom-code-secrets.png)

Once added, the secrets will be available as environment variables, which you can access in the custom code, as shown below:

const hubspot = require('@hubspot/api-client'); exports.main = (event, callback) => { return callback(processEvent(event)); };function processEvent(event) { // secrets can be accessed via environment variables const hubspotClient = new hubspot.Client({ accessToken: process.env.secretName }); hubspotClient.crm.contacts.basicApi.getById(event\["object"\]\["objectId"\], \["email", "phone"\]) .then(results => { let email = results.body\["properties"\]\["email"\] let phone = results.body\["properties"\]\["phone"\] // ... }) .catch(err => { console.error(err) }) }

Add HubSpot properties to your custom code[](https://developers.hubspot.com/docs/api/workflows/custom-code-actions#add-hubspot-properties-to-your-custom-code)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

At times, you may need to fetch object properties in your custom code action. Rather than using HubSpot's APIs, you can add these properties directly in the workflow action definition. Add properties and set property names to reference properties in your code. You can add up to 50 properties in each custom code action.  

![](https://developers.hubspot.com/hubfs/image-png-Oct-21-2021-07-28-35-75-AM.png)

Once added, the property can be referenced in the custom code. 

const email = event.inputFields\['email'\]; email = event.get('inputFields').get('email')

Logging
-------

An important tool for developers is ability to print outputs from their code. It helps you debug issues and provide better support for your end users. To see the output of the logs, you can find them in the "History" tab of the workflow.  

![custom_code_logs](https://developers.hubspot.com/hubfs/custom_code_logs.png "custom_code_logs")

How to Define Outputs
---------------------

In the function, define the output fields you want to use later in the workflow. Then, in the right sidebar, select the data output type (e.g., number, string, boolean, datetime, enum, date phone number) and input the field you want to output.  
  
The output fields should be part of a json object formatted accordingly, depending on the language used:

callback({ outputFields: { email: email, phone: phone } }); return { "outputFields": { "email": email, "phone": phone } }

![custom-code-output](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/custom-code-output.png "custom-code-output")

You can then use the output from your code action as in input to the _Copy property value_ action. This removes the need to make another API call to store the value as a property on your object.

Do take note of the following when defining your output:

*   If your data output type is in string format, the limit for string output values is 65,000  characters. Exceeding this limit will result in an `OUTPUT_VALUES_TOO_LARGE` error. 
*   If you're using the _Copy property value_ action, please also take note of [compatible source and target properties](https://knowledge.hubspot.com/workflows/compatible-source-and-target-properties-for-copying-property-values-in-workflows).
*   Do also note that if you're copying an output to a datetime property, the output will need to be in [UNIX millisecond format](https://legacydocs.hubspot.com/docs/faq/how-should-timestamps-be-formatted-for-hubspots-apis).

![custom_code_actions_output_usage](https://developers.hubspot.com/hubfs/custom_code_actions_output_usage.png "custom_code_actions_output_usage")

Limitations
-----------

Custom code actions must finish running within 20 seconds and can only use up to 128 MB of memory. Exceeding either of these limits will result in an error. 

Retries
-------

You may need to fetch object properties using the HubSpot API or to call other HubSpot API endpoints in your custom code action. Like any other API call, you'll still need to comply with [HubSpot API rate limits](/docs/api/usage-details).

*   If you're using Node.js and encounter a rate limiting error but you want HubSpot to retry your call, you'll need to throw the error in the `catch` block of your custom code action.

![](https://developers.hubspot.com/hubfs/image-png-Dec-10-2021-11-39-45-62-AM.png)

*   If you're using Python and encounter a rate limiting error but you want HubSpot to retry your call, you'll need to raise the error in the `except` block of your custom code action.

![](https://developers.hubspot.com/hubfs/image-png-Dec-10-2021-11-41-06-77-AM.png)

**Please note:** if the call fails due to a rate limiting error, or a 429 or 5XX error from [axios](https://www.npmjs.com/package/axios) or [@hubspot/api-client](https://www.npmjs.com/package/@hubspot/api-client), HubSpot will reattempt to execute your action for up to three days, starting one minute after failure. Subsequent failures will be retried at increasing intervals, with a maximum gap of eight hours between tries.

Caveats
-------

If you're using Node.js for your custom code, take note of the following caveats:

*   Generating random numbers: it's common to use [Math.random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) to generate random numbers but users may see the same numbers generated across different executions. This is because Math.random is seeded by the current time. Since HubSpot may enroll many objects into a workflow at the same time and clear the state on every execution, different executions end up seeding Math.random in the same way. Instead, you can use of [random-number-csprng 1.0.2](https://www.npmjs.com/package/random-number-csprng) library which guarantees cryptographically secure pseudo-random number generation.
*   Variable re-use: to save memory, any variables declared outside the `exports.main` function may be re-used for future executions of the custom code action. This is useful when connecting to external services like a database, but any logic or information that needs to be unique to each execution of the custom code action should be inside the `exports.main` function.

If you're using Python for your custom code, take note of the following caveats:

*   Variable re-use: similar to the above, any variables declared outside the `def main` function may be re-used for future executions of the custom code action.
    *   If you've declared a variable outside the `def main` function but do not plan on altering it, you can reference the variable directly.
    *   If you plan on altering a variable, you can declare the variable within the `def main` function with a global keyword before referencing it.

a = 1 def main(event): global a a += 1

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/workflows/custom-code-actions#page-feedback)
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