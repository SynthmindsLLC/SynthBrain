Custom Workflow Actions
=======================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use [HubSpot's workflows tool](https://knowledge.hubspot.com/workflows/create-workflows) to automate business processes and allow your team to be more efficient. You can create custom workflow actions to integrate your service with HubSpot's workflows.

After setting up your custom action, when users install your application, they can add the custom action to their workflows. 

When those workflows execute, HTTPS requests will send to the configured URL with the payload that you set up. Requests made for your custom action will use the v2 version of the _X-HubSpot-Signature_. Learn more about [validating requests from HubSpot](https://developers.hubspot.com/docs/api/webhooks/validating-requests).  
[](#add)

You can also skip forward to the following sections:

*   [Before you get started](#before)
*   [Define your custom action](#define)
*   [Functions](#functions)
*   [Input fields](#input)
*   [Fetch external data fields](#fetch)
*   [Output fields](#output)
*   [Labels](#label)
*   [Execution](#execution)
*   [Asynchronous custom action execution](/docs/api/automation/custom-workflow-actions#asynchronous-execution)
*   [Add custom execution messages with execution rules](#executionmessage)
*   [Test and publish your custom action](#publish)

The final section in this article provides [several custom action examples](#custom-action-examples).

Before you get started[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#before-you-get-started)
---------------------------------------------------------------------------------------------------------------------------

*   You'll need a [HubSpot developer account](https://app.hubspot.com/signup/developers) with a [HubSpot app](https://developers.hubspot.com/docs/api/creating-an-app). Your app logo will be used as the icon for the custom action.
*   When making requests to the custom workflow action endpoints, you must include your [HubSpot developer account key](https://legacydocs.hubspot.com/docs/faq/developer-api-keys) in the request URL. For example:

`https://api.hubspot.com/automation/v4/actions/{appId}?hapikey={developer_API_key}`

Define your custom action[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#define-your-custom-action)
---------------------------------------------------------------------------------------------------------------------------------

To create a custom workflow action, you'll need to define the action using the following fields. This also specifies the request format for requests coming from HubSpot, as well as the handling of responses from your service.

*   `**actionUrl**`: the URL where an HTTPS request is sent when the action is executed. The request body will contain information about which user the action is executing on behalf of, and what values were entered for the input fields.
*   **`objectTypes`:** which CRM objects this action can be used with.
*   **`published`:** by default, custom actions are created in an unpublished state. Unpublished actions are only visible in the developer portal associated with your HubSpot application. To make a custom action visible to users, update the published flag on your action definition to true.
*   `**inputFields**`: the inputs that the action receives. These will be filled by the user.
*   **`inputFieldDependencies`:** these rules allow fields to be grayed out until other fields meet specific conditions.
*   `outputFields`: the values that the action will output that can be used by later actions in the workflow. A custom action can have zero, one, or many outputs.
*   `objectRequestOptions`**:**  properties of the enrolled object included in the payload to the actionUrl.
*   `labels`: copy that describes to the user what the action's fields represent and what the action does. English labels are required, but labels can be specified in any of the following supported languages as well: French (`fr`), German (`de`), Japanese (`ja`), Spanish (`es`), Brazilian Portuguese (`pt-br`), and Dutch (`nl`).
*   `**executionRules**`: a list of definitions you can specify to surface errors from your service to the user creating the workflow.
*   **`functions`:** code snippets that are run in order to transform the payload being sent to a url and/or transform the response from that url.

### Example custom action definition

// { "actionUrl":"https://webhook.site/94d09471-6f4c-4a7f-bae2-c9a585dd41e0", "objectTypes":\[ "CONTACT" \], "inputFields":\[ { "typeDefinition":{ "name":"staticInput", "type":"string", "fieldType":"text" }, "supportedValueTypes":\[ "STATIC\_VALUE" \], "isRequired":true }, { "typeDefinition":{ "name":"objectInput", "type":"string", "fieldType":"text" }, "supportedValueTypes":\[ "OBJECT\_PROPERTY" \], "isRequired":true }, { "typeDefinition":{ "name":"optionsInput", "type":"enumeration", "fieldType":"select", "optionsUrl":"https://webhook.site/94d09471-6f4c-4a7f-bae2-c9a585dd41e0" }, "supportedValueTypes":\[ "STATIC\_VALUE" \] } \], "inputFieldDependencies":\[ { "dependencyType":"SINGLE\_FIELD", "dependentFieldNames":\[ "objectInput" \], "controllingFieldName":"staticInput" } \], "outputFields":\[ { "typeDefinition":{ "name":"myOutput", "type":"string", "fieldType":"text" }, "supportedValueTypes":\[ "STATIC\_VALUE" \] } \], "objectRequestOptions":{ "properties":\[ "email" \] }, "labels":{ "en":{ "inputFieldLabels":{ "staticInput":"Static Input", "objectInput":"Object Property Input", "optionsInput":"External Options Input" }, "actionName":"My Extension", "actionDescription":"My Extension Description", "appDisplayName":"My App Display Name", "actionCardContent":"My Action Card Content" } }, "functions":\[ { "functionType":"POST\_ACTION\_EXECUTION", "functionSource":"exports.main = (event, callback) => {\\r\\n callback({\\r\\n outputFields: {\\r\\n myOutput: \\"example output value\\"\\r\\n }\\r\\n });\\r\\n}" }, { "functionType":"POST\_FETCH\_OPTIONS", "functionSource":"exports.main = (event, callback) => {\\r\\n callback({\\r\\n \\"options\\": \[{\\r\\n \\"label\\": \\"Big Widget\\",\\r\\n \\"description\\": \\"Big Widget\\",\\r\\n \\"value\\": \\"10\\"\\r\\n },\\r\\n {\\r\\n \\"label\\": \\"Small Widget\\",\\r\\n \\"description\\": \\"Small Widget\\",\\r\\n \\"value\\": \\"1\\"\\r\\n }\\r\\n \]\\r\\n });\\r\\n}" } \] }

The above definition will render the following in the workflows tool:

![](https://lh5.googleusercontent.com/mX9MJ1Mh6YbxqbnGHHdF2acsI0RU4uHE7eRQij6Dc9yddUxGOKV0IVVa0vhxrwL23s_6cJdS2ogNBW6lBMclAxGqozZ-lkJIPHDDUkxmwUCLeFb5WdxfhtDRTddGvvxkYwjndmDl)

There are two types of calls made for custom workflow actions:

*   **Field option fetches:** populate a list of valid options when a user is configuring a field. Learn more about using field option fetches to fetch external data fields. 
*   **Action execution requests:** made when an action is being executed by a workflow that includes your custom action. 

Functions[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#functions)
-------------------------------------------------------------------------------------------------

Functions are snippets of code used to modify payloads before sending them to an API. You can also use functions to parse results from an API. HubSpot's functions are backed by [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/nodejs-handler.html). In the following code:

*   `event` contains the data that is passed to the function 
*   `exports.main` is the method that will be called when the function is run. 
*   The `callback` function can be used to return a result.

The code should be formatted as follows:

exports.main = (event, callback) => { callback({ "data": { "field": "email", "phone": "1234567890" } }); }

When setting up a function, the `functionSource` format will be in string. Ensure that the characters in the code have been escaped.

Generally, the definition of a function will follow the format: 

// { "functionType":"PRE\_ACTION\_EXECUTION", "functionSource":"exports.main = (event, callback) => {\\r\\n callback({\\r\\n \\"data\\": {\\r\\n \\"field\\": \\"email\\",\\r\\n \\"phone\\": \\"1234567890\\" \\r\\n }\\r\\n });\\r\\n" }

### Example function[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#example-function)

In the example below, examine the input code, the function used, and the output produced.  

Function input: 

// { "callbackId": "ap-102670506-56777914962-11-0", "origin": { "portalId": 102670506, "actionDefinitionId": 10860211, "actionDefinitionVersion": 1, "extensionDefinitionId": 10860211, "extensionDefinitionVersionId": 1 }, "context": { "source": "WORKFLOWS", "workflowId": 192814114 }, "object": { "objectId": 614, "objectType": "CONTACT" }, "inputFields": { "widgetOwner": "10887165", "widgetName": "My Widget Name" } }

Function used: 

// exports.main = (event, callback) => { callback({ "data": { "myObjectId": event\["object"\]\["objectId"\], "myField": event\["inputFields"\]\["widgetName"\] } }); }

Output expected:

// { "data":{ "myObjectId":614, "myField":"My Widget Name" } }

Input fields[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#input-fields)
-------------------------------------------------------------------------------------------------------

Input field definitions will adhere to the following format:

*   `name`**:** the internal name of the input field, separate from its label. The label displayed in the UI must be defined using the [labels section](#labels) of the custom action definition.
*   **`type`:** the type of value required by the input.
*   `fieldType`: how the input field should be rendered in the UI.  Input fields mimic CRM properties, learn more about [valid `type` and `fieldType` combinations](/docs/api/crm/properties#property-type-and-fieldtype-values)
*   `supportedValueTypes` have two valid values:
    *   `OBJECT_PROPERTY`**:** the user can select a property from the enrolled object or an output from a previous action to use as the value of the field.
    *   `STATIC_VALUE`**:** this should be used in all other cases. It denotes that the user must enter a value themselves. 
*   `isRequired`**:** this determines whether the user must give a value for this input or not

Input field definitions should be formatted as follows: 

// { "typeDefinition":{ "name":"staticInput", "type":"string", "fieldType":"text" }, "supportedValueTypes":\[ "STATIC\_VALUE" \], "isRequired":true }

You can also hard code options for the user to select: 

// { "typeDefinition":{ "name":"widgetColor", "type":"enumeration", "fieldType":"select", "options":\[ { "value":"red", "label":"Red" }, { "value":"blue", "label":"Blue" }, { "value":"green", "label":"Green" } \] }, "supportedValueTypes":\[ "STATIC\_VALUE" \] }

### Using external data[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#using-external-data)

Instead of hard coding field options, you can also fetch external data with external data fields. For example, you can retrieve a list of meeting projects or a list of products to serve as inputs. The input field should be formatted as follows: 

// { "typeDefinition":{ "name":"optionsInput", "type":"enumeration", "fieldType":"select", "optionsUrl":"https://your-url-here.com" }, "supportedValueTypes":\[ "STATIC\_VALUE" \] }

The payload sent to the `optionsURL` will be formatted as follows:

// { "origin": { // The customer's portal ID "portalId": 1, // Your custom action definition ID "actionDefinitionId": 2, // Your custom action definition version "actionDefinitionVersion": 3 }, // The workflow object type the action is being used in "objectTypeId" : "0-1" // The input field you are fetching options for "inputFieldName": "optionsInput", // The values for the fields that have already been filled out by the workflow user "inputFields": { "widgetName": { "type": "OBJECT\_PROPERTY", "propertyName": "widget\_name" }, "widgetColor": { "type": "STATIC\_VALUE", "value": "blue" } }, "fetchOptions": { // The search query provided by the user. This should be used to filter the returned // options. This will only be included if the previous option fetch returned // \`searchable: true\` and the user has entered a search query. "q": "option label", // The pagination cursor. This will be the same pagination cursor that was returned by // the previous option fetch; it can be used to keep track of which options have already // been fetched. "after": "1234=" } }

The expected response should be formatted as follows: 

// { "options": \[ { "label": "Big Widget", "description": "Big Widget", "value": "10" }, { "label": "Small Widget", "description": "Small Widget", "value": "1" } \], // Optional. The pagination cursor. If this is provided, the Workflows app will render // a button to load more results at the bottom of the list of options when a user is // selecting an option, and when the next page is loaded this value will be included in // the request payload under \`fetchOptions.after\`. "after": "1234=", // Optional. Default is false. If this is true, the Workflows app will render a search // field to allow a user to filter the available options by a search query, and when // a search query is entered by the user, options will be re-fetched with that search // term in the request payload under \`fetchOptions.q\`. "searchable": true }

In the code above, note that there's pagination being set to limit the number of returned options. This instructs the workflow that more options can be loaded.

In addition, the list of options is made searchable by including `searchable:true`.

### Modify external data[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#modify-external-data)

To manage external data, you can include two hooks to customize the field option fetch lifecycle:

*   `PRE_FETCH_OPTIONS`: a function that configures the payload sent from HubSpot.
*   `POST_FETCH_OPTIONS`: a function that transforms the response from your service into a format that's understood by HubSpot. 

#### PRE\_FETCH\_OPTIONS[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#pre-fetch-options)

When included, this function will apply to each input field. You can apply it to a specific input field by specifying an `id` in the function definition.

// { "functionType":"PRE\_FETCH\_OPTIONS", "functionSource":"...", id: "inputField" }

The payload sent from HubSpot will be formatted as follows:

// { "origin": { // The customer's portal ID "portalId": 1, // Your custom action definition ID "actionDefinitionId": 2, // Your custom action definition version "actionDefinitionVersion": 3 }, // The input field you are fetching options for "inputFieldName": "optionsInput", // Your configured external data field webhook URL "webhookUrl": "https://myapi.com/hubspot/widget-sizes", // The values for the fields that have already been filled out by the workflow user "inputFields": { "widgetName": { "type": "OBJECT\_PROPERTY", "propertyName": "widget\_name" }, "widgetColor": { "type": "STATIC\_VALUE", "value": "blue" }, "fetchOptions": { // The search query provided by the user. This should be used to filter the returned // options. This will only be included if the previous option fetch returned // \`searchable: true\` and the user has entered a search query. "q": "option label", // The pagination cursor. This will be the same pagination cursor that was returned by // the previous option fetch; it can be used to keep track of which options have already // been fetched. "after": "1234=" } } }

The response should then be formatted as follows:

// { // The webhook URL for HubSpot to call "webhookUrl": "https://myapi.com/hubspot", // Optional. The request body. "body": "{\\"widgetName\\": \\"My new widget\\", \\"widgetColor\\": \\"blue\\"}", // Optional. A map of custom request headers to add. "httpHeaders": { "My-Custom-Header": "header value" }, // Optional. The Content-Type of the request. Default is application/json. "contentType": "application/json", // Optional. The Accept type of the request. Default is application/json. "accept": "application/json", // Optional. The HTTP method with which to make the request. // Valid values are GET, POST, PUT, PATCH, and DELETE. // Default is POST. "httpMethod": "POST" }

#### POST\_FETCH\_OPTIONS[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#post-fetch-options)

To parse the response into an expected format, per the external data fields, use a `POST_FETCH_OPTIONS` function. The definition for a `POST_FETCH_OPTIONS` function is the same as a `PRE_FETCH_OPTIONS` function.  When external external data fetch options are defined, a dropdown menu will be rendered in the input options for the action. 

// { "functionType":"POST\_FETCH\_OPTIONS", "functionSource":"...", id: "inputField" }

The function input will be formatted as follows:

// { // The requested field key "fieldKey": "widgetSize", // The webhook response body from your service "responseBody": "{\\"widgetSizes\\": \[10, 1\]}" }

The function output will be formatted as follows:

// { "options": \[ { "label": "Big Widget", "description": "Big Widget", "value": "10" }, { "label": "Small Widget", "description": "Small Widget", "value": "1" } \] }

Output fields[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#output-fields)
---------------------------------------------------------------------------------------------------------

Use output fields to output values from your custom action to use in other actions. The definition for output fields is similar to the definition for input fields: 

*   **name:** how this field is referenced in other parts of the Custom Action. The label displayed in the UI must be defined using the \`labels\` section of the Custom Action 
*   **type:** the type of value required by the input.
*   **fieldType:** is how the input field should be rendered in the UI. Input fields mimic CRM properties, learn more about [valid `type` and `fieldType` combinations](/docs/api/crm/properties#property-type-and-fieldtype-values)  
      
    

The output field should be formatted as follows: 

// { "outputFields":\[ { "typeDefinition":{ "name":"myOutput", "type":"string", "fieldType":"text" } } \] }

When using an output field, values are parsed from the response from the `actionURL`. For example, you can copy output fields to an existing property in HubSpot.  

**![](https://lh3.googleusercontent.com/UJmic1rLacFsz3lUbPw96xZFf0s9_yx82ISp41Qcv_uJ_i70u-G10ZtPb1Wj5lkmQillB-GNbdRwqc-XW0EchJKBxFtpdtW8UB-ClVefswvoJUV0vxIxmGUaiFoAP6CPR3jmgYzG)**  

Labels[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#labels)
-------------------------------------------------------------------------------------------

Use labels to add text to your outputs or inputs in the workflow editor. Labels are loaded into HubSpot's language service and may take a few minutes to display. Portals [set to different regions or languages](https://knowledge.hubspot.com/account/change-your-language-and-region-settings#customize-default-user-language-date-and-number-format) will display the label in the corresponding language, if available. 

*   **`labels`:** copy describing what the action's fields represent and what the action does. English labels are required, but labels can be specified in any of the following supported languages as well:  French (`fr`), German (`de`), Japanese (`ja`), Spanish (`es`), Brazilian Portuguese (`pt-br`), and Dutch (`nl`).
*   **`actionName`:** the action's name shown in the Choose an action panel in the workflow editor.
*   **`actionDescription`:** a detailed description for the action shown when the user is configuring the custom action.
*   **`actionCardContent`:** a summarized description shown in the action's card.
*   **`appDisplayName`:** The name of the section in the “Choose an Action” panel where all the actions for the app are displayed. If appDisplayName is defined for multiple actions, the first one found is used.  
*   **`inputFieldLabels`:** an object that maps the definitions from inputFields to the corresponding labels the user will see when configuring the action.
*   **`outputFieldLabels`:** an object that maps the definitions from outputFields to the corresponding labels shown in the workflows tool.
*   **`inputFieldDescriptions`:** an object that maps the definitions from inputFields to the descriptions below the corresponding labels.
*   **`executionRules`:** an object that maps the definitions from your executionRules to messages that will be shown for action execution results on the workflow history. There is a separate section in these docs for execution rules. 

Label definitions should be formatted as follows:

// { "labels":{ "en":{ "actionName":"Create Widget", "actionDescription":"This action will create a new widget in our system. So cool!", "actionCardContent":"Create widget {{widgetName}}", "appDisplayName":"My App Display Name", "inputFieldLabels":{ "widgetName":"Widget Name", "widgetOwner":"Widget Owner" }, "outputFieldLabels":{ "outputOne":"First Output" }, "inputFieldDescriptions":{ "widgetName":"Enter the full widget name. I support <a href=\\"https://hubspot.com\\">links</a> too." }, "executionRules":{ "alreadyExists":"The widget with name {{ widgetName }} already exists" } } } }

Execution[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#execution)
-------------------------------------------------------------------------------------------------

When an execution executes, a https request is sent to the `actionUrl`.

*   `callbackId`**:** a unique ID for the specific execution. If the custom action execution is [blocking](#block), use this ID. 
*   **`object`:** the values of the properties requested in `objectRequestOptions`.
*   **`InputFields`:** the values for the inputs that the user has filled out. 

The execution payload will be formatted as follows: 

// { "callbackId": "ap-102670506-56776413549-7-0", "origin": { "portalId": 102670506, "actionDefinitionId": 10646377, "actionDefinitionVersion": 1 }, "context": { "source": "WORKFLOWS", "workflowId": 192814114 }, "object": { "objectId": 904, "properties": { "email": "ajenkenbb@gnu.org" }, "objectType": "CONTACT" }, "inputFields": { "staticInput": "My Static Input", "objectInput": "995", "optionsInput": "1" } }

The expected response should be formatted as follows: 

// { "outputFields":{ "myOutput":"Some value", "hs\_execution\_state": "SUCCESS" } }

When looking at the execution response: 

*   **`outputFields`:** the values of the output fields defined earlier. These values can be used in later actions. 
*   **`hs_execution_state`:** an optional special value that can added to outputFields.  It is not possible to specify a retry, only the following values can be added:
    *   SUCCESS
    *   FAIL\_CONTINUE
    *   BLOCK
    *   ASYNC

`SUCCESS` and `FAIL_CONTINUE` indicate that the action has completed and the workflow should move on to the next action to execute. If no execution state is specified, status codes will be used to determine the result of an action: 

*   **2xx status codes:** the action has completed successfully.
*   **4xx status codes:** the action has failed. The exception is 429 Rate Limited status codes, which are re-treated as retries, and the Retry-After header is respected.
*   **5xx status codes:** there was a temporary problem with the service, and the action will be retried at a later time. An exponential backoff system is used for retries, retries will continue for up to 3 days before failing. 

Execution functions[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#execution-functions)
---------------------------------------------------------------------------------------------------------------------

Use execution functions to format data before sending to the `actionURL` and parse data from the `actionURL`. There are two types of execution functions:

*   `PRE_ACTION_EXECUTION`
*   `POST_ACTION_EXECUTION`

#### PRE\_ACTION\_EXECUTION function

Use `PRE_ACTION_EXECUTION` functions to format data before sending it to the `actionURL`

The function definition will be formatted as follows:

// { "functionType":"PRE\_ACTION\_EXECUTION", "functionSource":"..." }

The function input should be formatted as follows:

// { "webhookUrl": "https://actionurl.com/", "callbackId": "ap-102670506-56776413549-7-0", "origin": { "portalId": 102670506, "actionDefinitionId": 10646377, "actionDefinitionVersion": 1 }, "context": { "source": "WORKFLOWS", "workflowId": 192814114 }, "object": { "objectId": 904, "properties": { "email": "ajenkenbb@gnu.org" }, "objectType": "CONTACT" }, "inputFields": { "staticInput": "My Static Input", "objectInput": "995", "optionsInput": "1" } }

The function output should be formatted as follows:

// { // The webhook URL for HubSpot to call "webhookUrl": "https://myapi.com/hubspot", // Optional. The request body. "body": "{\\"widgetName\\": \\"My new widget\\", \\"widgetColor\\": \\"blue\\"}", // Optional. A map of custom request headers to add. "httpHeaders": { "My-Custom-Header": "header value" }, // Optional. The Content-Type of the request. Default is application/json. "contentType": "application/json", // Optional. The Accept type of the request. Default is application/json. "accept": "application/json", // Optional. The HTTP method with which to make the request. // Valid values are GET, POST, PUT, PATCH, and DELETE. // Default is POST. "httpMethod": "POST" }

#### POST\_ACTION\_EXECUTION function 

After receiving a response from the `actionURL`, use a `POST_ACTION_EXECUTION` function to format data for HubSpot.

The function definition will be formatted as follows:

// { "functionType":"POST\_ACTION\_EXECUTION", "functionSource":"..." }

The function input should be formatted as follows:

// { "responseBody": "{\\r\\n \\"returnValue\\":\\"Hello World!\\"\\r\\n}" }

The function output should be formatted as follows:

// { "outputFields":{ "myOutput":"Some value", "hs\_execution\_state": "SUCCESS" } }

Asynchronous execution[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#asynchronous-execution)
---------------------------------------------------------------------------------------------------------------------------

Execute custom workflow actions asynchronously by blocking and later completing the action.

### Blocking action execution[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#blocking-action-execution)

Use custom actions to block workflow execution. Instead of executing the next action in the workflow after your custom action after receiving a `completed (2xx or 4xx status code)` response from your service, the workflow will stop executing ("block") that enrollment until you tell the workflow to continue.

When blocking, you can specify a value for the `hs_default_expiration` field, after which your custom action will be considered expired. The execution of the workflow will then resume and the action following your custom action will be executed, even if the action is not completed. 

To block a custom action, your action execution response must have the following format:

// { "outputFields": { // Required. Must be BLOCK for your custom action to block execution. "hs\_execution\_state": "BLOCK", // Optional. If not provided, a default expiration of 1 week is used. // Must be specified in ISO 8601 Duration format. // See https://en.wikipedia.org/wiki/ISO\_8601#Durations "hs\_expiration\_duration": "P1WT1H" } }

### Complete a blocked execution[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#complete-a-blocked-execution)

To complete a blocked custom action execution, use the following endpoint: `/callbacks/{callbackId}/complete`

Format the request body as follows:

// { "outputFields": { // Required. The final execution state. Valid values are SUCCESS // (to indicate that your custom action completed successfully) or // FAIL\_CONTINUE (to indicate that there was a problem with your // custom action execution) "hs\_execution\_state": "SUCCESS" } }

Add custom execution messages with rules[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#add-custom-execution-messages-with-rules)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Specify rules on your action to determine which message displays on the workflow's history page when the action executes.

The rules will be matched against the output values from your action.  These output values should be provided in the `actionURL`'s response body, in the following format:

// { "outputFields": { "errorCode": "ALREADY\_EXISTS", "widgetName": "Test widget" } }

The actual messages can be specified in the labels section of the custom action:

// { "labels": { "executionRules": { "alreadyExists": "The widget with name {{ widgetName }} already exists", "widgetWrongSize": "Wrong widget size", "widgetInvalidSize": "Invalid widget size" } } } }

The `executionRules` will be tested in the order provided. If there are multiple matches, only the message from the first rule that matches is displayed to the user.

The rule matches when the execution output corresponds to a specified value in the rule. For example, consider this set of `executionRules`:

// \[ { // This matches the key of a label on the action's \`labels.LANGUAGE.executionRules\` map "labelName": "alreadyExists", "conditions": { "errorCode": "ALREADY\_EXISTS" } }, { "labelName": "widgetWrongSize", "conditions": { "errorCode": "WIDGET\_SIZE", "sizeError": \["TOO\_SMALL", "TOO\_BIG"\] } }, { "labelName": "widgetInvalidSize", "conditions": { "errorCode": "WIDGET\_SIZE" } } \]

With the above, the following matches would occur:

*   `{"errorCode": "ALREADY_EXISTS", "widgetName": "Test widget"}`: This would match the first rule, since `errorCode` is equal to `ALREADY_EXISTS`. In this instance, even though there is a `widgetName` output, it isn't used in the rule definition so any value is allowed.
*   `{"errorCode": "WIDGET_SIZE", "sizeError": "TOO_SMALL"}`: This would match the second rule, since `TOO_SMALL` is one of the matching `sizeError`s, and `errorCode` is `WIDGET_SIZE`.
*   `{"errorCode": "WIDGET_SIZE", "sizeError": "NOT_A_NUMBER"}`: This would match the third rule, since even though the `errorCode` is `WIDGET_SIZE`, the `sizeError` does not match any of the values specified by the second rule (`TOO_SMALL` or `TOO_BIG`).

This matching mechanism allows you to specify fallback errors, so that you can have specific errors for important error cases, but fall back to more generic error messages for less common errors. Here is an example of how the custom message would display:

![](https://developers.hubspot.com/hubfs/image-png-Feb-25-2022-07-04-17-38-AM.png)

Test and publish your custom action[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#test-and-publish-your-custom-action)
-----------------------------------------------------------------------------------------------------------------------------------------------------

After creating your new custom action, you can test and publish it. 

### Testing custom actions before publishing 

Before publishing your custom action, you can test action execution and fetching options by pointing the URL to [webhook.site](https://webhook.site/). This allows you to inspect the payload and return a specific response. 

You can also test the action in your developer portal by creating a workflow in the workflows tool. Then, [adding your new action](https://knowledge.hubspot.com/workflows/choose-your-workflow-actions#add-actions).

When you've complete your testing, it is recommended to archive your test actions. Learn more about archiving actions in the _Archive a custom action_ section in the _Endpoints_ tab at the top of this article._._

### Publishing custom actions 

By default, custom actions are created in an unpublished state. Unpublished custom actions are only visible in the developer portal associated with the corresponding HubSpot application. To make a custom action visible to users, update the `published` flag on your action definition to `true`. If an action is unpublished, portals that have already added the action to their workflow will still be able to edit and execute already added actions. But, they won't be able to add the action again. 

Custom action examples[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#custom-action-examples)
---------------------------------------------------------------------------------------------------------------------------

The code snippets below provide examples of several common use-cases for custom actions, such as defining a widget or invoking a serverless function.

### Example #1[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#example-1)

This example features the following input fields, created for contact and deal workflows:

*   `widgetName`: a static input field
*   `widgetColor`: a dropdown field with options
*   `widgetOwner`:  a field representing a HubSpot owner.
*   `widgetQuantity`: a field whose derived from a property (that the user creating the workflow selects) on the enrolled object.

// { "actionUrl": "https://example.com/hubspot", "inputFields": \[ { "typeDefinition": { "name": "widgetName", "type": "string", "fieldType": "text" }, "supportedValueTypes": \["STATIC\_VALUE"\], "isRequired": true }, { "typeDefinition": { "name": "widgetColor", "type": "enumeration", "fieldType": "select", "options": \[ { "value": "red", "label": "Red" }, { "value": "blue", "label": "Blue" }, { "value": "green", "label": "Green" } \] }, "supportedValueTypes": \["STATIC\_VALUE"\] }, { "typeDefinition": { "name": "widgetOwner", "type": "enumeration", "referencedObjectType": "OWNER" }, "supportedValueTypes": \["STATIC\_VALUE"\] }, { "typeDefinition": { "name": "widgetQuantity", "type": "number" }, "supportedValueTypes": \["OBJECT\_PROPERTY"\] } \], "labels": { "en": { "actionName": "Create Widget - Example 1", "actionDescription": "This action will create a new widget in our system. So cool!", "actionCardContent": "Create widget {{widgetName}}", "inputFieldLabels": { "widgetName": "Widget Name", "widgetColor": "Widget Color", "widgetOwner": "Widget Owner", "widgetQuantity": "Widget Quantity" }, "inputFieldDescriptions": { "widgetName": "Enter the full widget name. I support <a href=\\"https://hubspot.com\\">links</a> too.", "widgetColor": "This is the color that will be used to paint the widget." } } }, "objectTypes": \["CONTACT", "DEAL"\] }

### Example #2[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#example-2)

The following custom action uses a serverless function to transform the payload that is sent to the configured actionUrl. Since the `objectTypes` field isn't specified in the custom action definition, this action will be available in all workflows types.

// { "actionUrl": "https://example.com", "inputFields": \[ { "typeDefinition": { "name": "widgetName", "type": "string", "fieldType": "text" }, "supportedValueTypes": \["STATIC\_VALUE"\], "isRequired": true } \], "labels": { "en": { "actionName": "Create Widget - Example 2", "actionCardContent": "Create widget {{widgetName}}", "inputFieldLabels": { "widgetName": "Widget Name" } } }, "functions": \[ { "functionType": "PRE\_ACTION\_EXECUTION", "functionSource": "exports.main = function(event, callback) { return callback(transformRequest(event)); }\\nfunction transformRequest(request) { return { webhookUrl: request.webhookUrl, body: JSON.stringify(request.fields), contentType: 'application/x-www-form-urlencoded', accept: 'application/json', httpMethod: 'POST' }; }" } \] }

### Example #3[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#example-3)

The following custom action has field dependencies and options that are fetched from an external API. Because the widget size depends on the widget color, the user won't be able to input a value for the widget size until a widget color is chosen.  
  
The widget cost is also dependent on the widget color, but it is conditional on the value that the user selects for the widget color; the user won't be able to input a value for the widget cost unless Red is selected as the widget color.

// { "actionUrl": "https://example.com/hubspot", "inputFields": \[ { "typeDefinition": { "name": "widgetName", "type": "string", "fieldType": "text" }, "supportedValueTypes": \["STATIC\_VALUE"\], "isRequired": true }, { "typeDefinition": { "name": "widgetColor", "type": "enumeration", "fieldType": "select", "options": \[ { "value": "red", "description": "red", "label": "Red" }, { "value": "blue", "description": "blue", "label": "Blue" }, { "value": "green", "description": "green", "label": "Green" } \] }, "supportedValueTypes": \["STATIC\_VALUE"\], }, { "typeDefinition": { "name": "widgetSize", "type": "enumeration", "fieldType": "select", "optionsUrl": "https://api.example.com/v1/widget-sizes" }, "supportedValueTypes": \["STATIC\_VALUE"\] }, { "typeDefinition": { "name": "widgetCost", "type": "number", "fieldType": "number" }, "supportedValueTypes": \["OBJECT\_PROPERTY"\] } \], "inputFieldDependencies": \[ { "dependencyType": "SINGLE\_FIELD", "controllingFieldName": "widgetColor", "dependentFieldNames": \["widgetSize"\] }, { "dependencyType": "CONDITIONAL\_SINGLE\_FIELD", "controllingFieldName": "widgetColor", "controllingFieldValue": "red", "dependentFieldNames": \["widgetCost"\] } \], "labels": { "en": { "actionName": "Create Widget - Example 3", "actionCardContent": "Create widget {{widgetName}}", "inputFieldLabels": { "widgetName": "Widget Name", "widgetColor": "Widget Color", "widgetSize": "Widget Size", "widgetCost": "Widget Cost" } } }, "objectTypes": \["CONTACT", "DEAL"\], "functions": \[ { "functionType": "PRE\_FETCH\_OPTIONS", "id": "widgetSize", "functionSource": "exports.main = function(event, callback) { return callback(transformRequest(event)); }\\nfunction transformRequest(request) { return { webhookUrl: request.webhookUrl + '?color=' + request.fields.widgetColor.value, body: JSON.stringify(request.fields), httpMethod: 'GET' }; }" } \] }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions#page-feedback)
---------------------------------------------------------------------------------------------------------------

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