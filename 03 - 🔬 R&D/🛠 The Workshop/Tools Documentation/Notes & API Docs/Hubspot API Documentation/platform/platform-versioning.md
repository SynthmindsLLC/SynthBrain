Projects platform versioning (BETA)
===================================

HubSpot developer projects include a `platformVersion` field that enables you to control which version of the projects platform you're developing on. This enables you to access updated functionalities, rollback to previous versions, and generally coordinate changes as needed. 

Below, learn how to set the `platformVersion` in a project, along with the available versions and their updates.

Manage versions[](https://developers.hubspot.com/docs/platform/platform-versioning#manage-versions)
---------------------------------------------------------------------------------------------------

To set which version of the developer platform your projects are running on, use the `platformVersion` field in your project's `hsproject.json` file.

After changing the version number, you'll need to upload the project to the HubSpot account to enable access to the version updates.

// Example project.json config file { "name": "my\_project", "srcDir": "src", "platformVersion": "2023.2" }

Available versions[](https://developers.hubspot.com/docs/platform/platform-versioning#available-versions)
---------------------------------------------------------------------------------------------------------

*   Latest version: `2023.2` (November 21, 2023)  
    
*   Initial release: `2023.1` (upcoming sunset on March 31, 2024)

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`2023.2`

 | 

Available as of November 21, 2023.

Changes primarily impact app functions, including:

*   Support for asynchronous functions (`async` / `await`)
*   Public URL support for app functions
*   `PRIVATE_APP_ACCESS_TOKEN` moved from `context.secrets` to `process.env`
*   Increased log size from 4KB to 256KB with logs now in order of execution
*   Support for Node 18

Learn more about working with these changes below.

 |
| 

`2023.1`

Upcoming sunset



 | 

Initial release of the developer platform.

This version will no longer be available after March 31, 2024. After this date, attempts to upload projects at this version will fail.

 |

Changes in 2023.2[](https://developers.hubspot.com/docs/platform/platform-versioning#changes-in-2023-2)
-------------------------------------------------------------------------------------------------------

Version `2023.2` of the developer platform includes the changes below.

### Serverless function configuration[](https://developers.hubspot.com/docs/platform/platform-versioning#serverless-function-configuration)

The following changes have been made for serverless function configuration (`serverless.json`):

*   Previously, serverless functions in projects supported two types of functions: app and API endpoint. App functions have been updated to support public URLs for making API requests, so you no longer need to build these as separate types.
*   With this update, the `runtime` and `version` fields have also been removed.
*   This version uses Node18, and lower versions cannot be specified.

Previous serverless function configuration

// serverless.json before update { "runtime": "nodejs18.x", "version": "1.0", "appFunctions": { "functionName": { "file": "function1.js" } }, "endpoints": { "path/to/endpoint": { "file": "githubUserFunction.js", "method": \["GET", "POST"\] } } }

Updated serverless function configuration

// serverless.json after update { "appFunctions": { "functionName": { "file": "function1.js", "endpoint": { "path": "path/to/endpoint", "method": \["GET"\], } } } }

### Async support[](https://developers.hubspot.com/docs/platform/platform-versioning#async-support)

Projects now support asynchronous functions. Callbacks are no longer supported in this version.

To update your serverless functions to use async:

*   Add `async` to the function definition.
*   Remove the callback (sometimes referred to as `sendResponse`), and use return statements to return response.
*   Use `await` and `try`/`catch` instead of promise chaining.
*   Return the desired response or throw an error.

#### Before[](https://developers.hubspot.com/docs/platform/platform-versioning#before)

const hubspot = require("@hubspot/api-client"); exports.main = myFunction = (context = {}, sendResponse) => { const { hs\_object\_id } = context.propertiesToSend; const userId = context.parameters.userId; const hubspotClient = new hubspot.Client({ accessToken: process.env\["PRIVATE\_APP\_ACCESS\_TOKEN"\], }); const properties = { "name":"newName", }; const SimplePublicObjectInput = { properties }; const objectType = "myObject"; const objectId = hs\_object\_id; const idProperty = undefined; hubspotClient.crm.objects.basicApi .update(objectType, objectId, SimplePublicObjectInput, idProperty) .then((res) => { sendResponse(res); }) .catch((err) => { console.error(err); sendResponse(err); }); };

#### After[](https://developers.hubspot.com/docs/platform/platform-versioning#after)

const hubspot = require("@hubspot/api-client"); exports.main = async (context = {}) => { const { hs\_object\_id } = context.propertiesToSend; const userId = context.parameters.userId; const hubspotClient = new hubspot.Client({ accessToken: process.env\["PRIVATE\_APP\_ACCESS\_TOKEN"\], }); const properties = { "name":"newName", }; const SimplePublicObjectInput = { properties }; const objectType = "myObject"; const objectId = hs\_object\_id; const idProperty = undefined; try { const res = await hubspotClient.crm.objects.basicApi .update(objectType, objectId, SimplePublicObjectInput, idProperty) return res } catch (err) { console.error(err); return err; } };

### Private app access token authentication[](https://developers.hubspot.com/docs/platform/platform-versioning#private-app-access-token-authentication)

Whereas previously you would refer to private app access tokens with `context.secrets.PRIVATE_APP_ACCESS_TOKEN`, you'll now use `process.env` rather than `context.secrets`. For example:

// Include HubSpot node API client const hubspot = require('@hubspot/api-client'); exports.main = async (context = {}) => { // instantiate HubSpot node API client const hubspotClient = new hubspot.Client({ accessToken: process.env\["PRIVATE\_APP\_ACCESS\_TOKEN"\] }); //your function return response; };

### Improved logging[](https://developers.hubspot.com/docs/platform/platform-versioning#improved-logging)

Version `2023.2` increases log size from 4KB to 256KB and guarantees logs to be in order of execution. You can also take advantage of improved in-app logging, such as [log tracing](/docs/platform/create-private-apps-with-projects#log-traces).

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/platform-versioning#page-feedback)
-----------------------------------------------------------------------------------------------------

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