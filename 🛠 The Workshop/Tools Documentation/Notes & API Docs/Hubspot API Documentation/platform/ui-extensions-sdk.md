---
Please provide me with more context! I need to know what kind of mission you are referring to. For example, is it: "* **A personal mission statement?**  "
* **A mission for a company or organization?** 
* **A mission for a specific project?** 
* **A mission for a fictional story?**

Once you tell me what kind of mission you are working on, I can help you with ideas and suggestions.
---

UI extensions SDK (BETA)
========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The UI extensions SDK is the foundation for [building UI extensions in HubSpot](/docs/platform/create-ui-extensions), containing an assortment of methods, functionalities, tools, and [UI components](/docs/platform/ui-components) to customize your extensions.

Below, learn about what's offered in the SDK along with usage examples and boilerplate code.

*   [Registering the extension](#registering-the-extension)
*   [Display success and error banners](#display-alert-banners)
*   [Fetch CRM property data](#fetch-crm-property-data)
*   [Refresh properties on the CRM record](#refresh-properties-on-the-crm-record)
*   [Listen for property updates](#listen-for-property-updates)
*   [Open a panel](#open-a-panel)
*   [Open an iframe in a modal](#open-an-iframe-in-a-modal)
*   [Fetch account, user, and extension context](#fetch-account-user-and-extension-context)
*   [Send custom log messages for debugging](#send-custom-log-messages-for-debugging)

Registering the extension[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#registering-the-extension)
---------------------------------------------------------------------------------------------------------------------

UI extensions, like any React front-end, are written as React components. However, unlike usual react components, you must register them with HubSpot by including `hubspot.extend()` inside the component file instead of exporting them. This is not required when you create a sub-component. For better code, reuse and include them inside your extension.

The `hubspot.extend()` function receives the following arguments:

*   `context`: the context object that includes information about the account and user.
*   `runServerlessFunction`: the serverless functions to run in the component.
*   `actions`: the actions to include in the component.

If you followed the steps above to create your UI extension from scratch, you'll have already copied the code below into your React front end `Example.jsx` file. 

hubspot.extend(({ context, runServerlessFunction, actions }) => ( <HelloWorld context={context} runServerless={runServerlessFunction} onAlertClick={actions.addAlert} /> ));

### runServerlessFunction[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#runserverlessfunction)

View the full API for the `runServerlessFunction` call below. Note that `propertiesToSend` in the call is another way to fetch CRM properties on the serverless function side, rather than using `fetchCromObjectProperties` on the React client side. Making this call on the server side will fetch property data when the serverless function is called, versus only when the extension loads. Learn more about [fetching CRM data](#fetch-crm-property-data).

runServerlessFunction(params: ServerlessRunnerParams): Promise<ServerlessExecutionResult> type ServerlessRunnerParams = { /\*\* \* Name of the serverless function that is configured as a key for the function in serverless.json file. \*/ name: string; /\*\* \* Names of CRM object properties to be retrieved and supplied to \* the function as \`context.propertiesToSend\` (Optional) \*/ propertiesToSend?: string\[\]; /\*\* \* Additional parameters to be supplied to the function as \* \`context.parameters\` (Optional) \*/ parameters?: JsonValue; } Response body type ServerlessExecutionResult = | { status: 'SUCCESS'; response: JsonValue; } | { status: 'ERROR'; message: string; };

**Please note:** the `status` returned by `runServerlessFunction` is automatically determined by HubSpot and cannot be set manually using `sendResponse()`. If the serverless function runs successfully, it will automatically return a `status` of `SUCCESS`. To trigger an error status, you'll need to build it into your serverless function.

Display alert banners[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#display-alert-banners)
-------------------------------------------------------------------------------------------------------------

Use the `addAlert` method to send alert banners as a feedback for any actions to indicate success or failure. `addAlert` is a part of the `actions` object that can be passed to extension via `hubspot.extend`. If you want to render an alert within a card, check out the [`Alert` component](/docs/platform/ui-components/alert).

Use the `addAlert` method to send alert banners as a feedback for any actions to indicate success or failure. `addAlert` is a part of the `actions` object that can be passed to extension via `hubspot.extend`.

The `AddAlert` method accepts the following props:

*   `title`: the bolded title text of the alert.
*   `message`: the alert text.
*   `type`: the alert color variant. Can be one of:
    *   `info`: a blue alert to provide general information.
    *   `success`: a green alert indicating a positive outcome.
    *   `warning`: a yellow alert indicating caution.
    *   `danger`: a red alert indicating a negative outcome.
    *   `tip`: a white alert to provide guidance.

![ui-extension-alert-example (1)](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-alert-example%20(1).png?width=850&height=812&name=ui-extension-alert-example%20(1).png)

![alert-row](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/alert-row.png?height=110&name=alert-row.png)

// Snippet from app/extensions/HelloWorld.jsx hubspot.extend(({ context, runServerlessFunction, actions }) => ( <HelloWorld context={context} runServerless={runServerlessFunction} onAlertClick={actions.addAlert} /> )); // the following method executes a serverless function // and displays an alert based on the response const HelloWorld = ({ context, runServerless, onAlertClick }) => { const \[inputValue, setInputValue\] = useState(""); const executeServerless = async () => { const serverlessResult = await runServerless({ name: "get-data", parameters: { inputValue }, }); if (serverlessResult.status === 'SUCCESS') { onAlertClick({title: "Heads up", message: serverlessResult.response.alertMessage, type: "success"}); } else { console.error("Error executing serverless: ", serverlessResult.message); } }; return ( // components );

In line 21 above, the `alertMessage` value can be passed by the serverless function by including it in `sendResponse`.

// Snippet from app/app.functions/get-data.js \*/ export.main = async (context = {}, callback) => { const message = context.parameters\['inputValue'\]; callback({alertMessage: \`You typed "${message}".\`}); }

Fetch CRM property data[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#fetch-crm-property-data)
-----------------------------------------------------------------------------------------------------------------

There are three ways to fetch CRM property data:

*   `fetchCrmObjectProperties`, which can be included in your React files to fetch property data client side at extension load time.
*   `propertiesToSend`, which can be included in your [serverless functions](#runserverlessfunction) to fetch property data on the back end at function invocation time.
*   Use GraphQL to query CRM data through the `/collector/graphql` endpoint. Learn more about [querying CRM data using GraphQL](/docs/cms/data/query-hubspot-data-using-graphql). To see an example of using GraphQL to fetch data, check out [HubSpot's contact duplicator sample project](/docs/platform/sample-projects#contact-duplicator).

**Please note:** to make GraphQL requests, your app must include the following scopes:

*   `collector.graphql_schema.read`
*   `collector.graphql_query.execute`

### fetchCrmObjectProperties[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#fetchcrmobjectproperties)

Using the `fetchCrmObjectProperties` method, you can get property values from the currently displaying CRM record without having to use HubSpot's APIs. This method is a part of the `actions` object that can be passed to the extension via `hubspot.extend`. You'll first need to add the object to `objectTypes` inside the card's `.json` config file. The objects you specify in `objectTypes` will also set which CRM objects will display the extension.

hubspot.extend(({ actions }) => ( <HelloWorld fetchProperties={actions.fetchCrmObjectProperties} /> )); const HelloWorld = ({ runServerless, fetchProperties }) => { const \[firstName, setFirstName\] = useState(""); const \[lastName, setLastName\] = useState(""); useEffect(() => { fetchProperties(\["firstname", "lastname"\]) .then(properties => { setFirstName(properties.firstname); setLastName(properties.lastname); }); }, \[fetchProperties\]); return ( <Text>Hello {firstName} {lastName}</Text> ); }

You can specify individual properties or fetch all properties with an asterisk:

fetchCrmObjectProperties('\*').then(properties => console.log(properties))

The response for `fetchCrmObjectProperties` is formatted as:

// example fetchCrmObjectProperties response { "property1Name": "property1Value", "property2Name": "property2Value" }

Refresh properties on the CRM record[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#refresh-properties-on-the-crm-record)
-------------------------------------------------------------------------------------------------------------------------------------------

Use `refreshObjectProperties` to refresh the property data on the CRM record, and any CRM data components on the record without needing to refresh the page. This includes [cards added to the record through HubSpot's UI](https://knowledge.hubspot.com/crm-setup/customize-the-middle-column-of-records#manage-cards-in-the-middle-column). This method will work for the CRM objects that you include in the extension's `.json` file in the `objectTypes` array. 

**Please note:** this method will not refresh property values in custom cards that are fetched using HubSpot's APIs. Only HubSpot's built-in property fields and properties in CRM data components will be refreshed.

import React, { useState } from 'react'; import { Divider, Button, Input, Flex, hubspot } from '@hubspot/ui-extensions'; hubspot.extend(({ runServerlessFunction, actions }) => ( <Extension runServerless={runServerlessFunction} refreshObjectProperties={actions.refreshObjectProperties} /> )); const Extension = ({ runServerless, refreshObjectProperties, }) => { // Your extension logic goes here // Refresh all properties of the object on the page refreshObjectProperties(); } }); }; return ( // Your extension body )

Listen for property updates[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#listen-for-property-updates)
-------------------------------------------------------------------------------------------------------------------------

Use the `onCrmPropertiesUpdate` to subscribe to changes made to properties on the CRM record and run functions based on those changes. This action is intended to be used like a react hook.

The full API for this method is as follows:

export type onCrmPropertiesUpdateAction = ( properties: string\[\] | '\*', callback: ( properties: Record<string, string>, error?: { message: string } ) => void ) => void;

As an example, the following function subscribes to updates made to the contact's first and last name properties, then logs those properties to the console. 

onCrmPropertiesUpdate(\['firstname','lastname'\], (properties) => console.log(properties))

You can subscribe to all properties by using an asterisk.

onCrmPropertiesUpdate('\*', (properties) => console.log(properties))

### Error handling[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#error-handling)

You can handle potential errors by passing the error argument to the callback.

onCrmPropertiesUpdate(\['firstname','lastname'\], (properties, error) => { if(error) { console.log(error.message} } else { console.log(properties) } })

Open a panel[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#open-a-panel)
-------------------------------------------------------------------------------------------

Using a [`Panel` component](/docs/platform/ui-components/panel), you can add a side panel to your UI extension which can be opened by click events in other components. Only one panel can be open at a time. Opening a panel while another is already open will cause the first one to close. To see an example of incorporating a panel into an extension, check out HubSpot's [Build a multi-step flow sample project](/docs/platform/sample-projects#build-a-multi-step-flow).

![panel-example-gif](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/panel-example-gif.gif?width=700&height=595&name=panel-example-gif.gif)

The `Panel` component can be opened and closed through an event triggered by an `onClick` event in [Button](/docs/platform/ui-components/button), [Link](/docs/platform/ui-components/link), [Tag](/docs/platform/ui-components/tag), and [Image](/docs/platform/ui-components/image) components. In the `onClick` handles, two actions are passed in the callback:

*   `ExtensionEvent`: contains information about the actual DOM event created by the user.
*   `reactions`: contains two functions: `openPanel` and `closePanel`.

The example code below shows how to use separate buttons to open and close a panel:

<Panel id="my-panel"> Test </Panel> <Button onClick={(\_\_,reactions) => reactions.openPanel('panel-id')}> Open Panel</Button> <Button onClick={(\_\_,reactions) => reactions.closePanel('panel-id')}> Close Panel</Button>

**Please note:** if your `onClick` function is asynchronous, make sure that it returns a promise.

Panels consist of three subcomponents, which arrange the panel content:

*   `<PanelBody>`: the container that wraps the panel's content and makes it scrollable. Use only one `PanelBody` per `Panel`.
*   `<PanelSection>`: a container that adds padding and bottom margin to provide spacing between content. You can use [Flex](/docs/platform/ui-components/flex) and [Box](/docs/platform/ui-components/box) to further customize content layout.
*   `<PanelFooter>`: a sticky footer component at the bottom of the panel. Include only one `PanelFooter` per `Panel`.

<> <Panel title="Welcome to my Panel" id="my-panel"> <Form> <PanelBody> <PanelSection> <Select name="test" label="Test" options={\[ {label: 'foo', value: 'foo'}, {label:"bar", value: "bar"}\]} /> </PanelSection> <PanelSection> lorem ipsum... </PanelSection> </PanelBody> <PanelFooter><Button type="submit">Click me</Button></PanelFooter> </Form> </Panel> <Button onClick={(event, reactions) => { reactions.openPanel('my-panel')}}> Open Panel </Button> </>

Open an iframe in a modal[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#open-an-iframe-in-a-modal)
---------------------------------------------------------------------------------------------------------------------

Similar to `addAlert` and `fetchCrmObjectProperties`, you can pass `openIframeModal` to the extension through the `actions` object.

Learn more by checking out HubSpot's [Display an iframe modal sample project](/docs/platform/sample-projects#display-an-iframe-modal).

hubspot.extend(({ context, runServerlessFunction, actions }) => ( <HelloWorld context={context} runServerless={runServerlessFunction} openIframe={actions.openIframeModal} /> ));

`openIframeModal` takes the following payload:

interface OpenIframeActionPayload { uri: string; height: number; width: number; title?: string; flush?: boolean; associatedObjectProperties?: string\[\]; }

For example, the following code would result in an extension that opens an iframe on button click. The iframe is configured to contain the Wikipedia homepage with a height and width of 1000px an no padding.

import { Link, Button, Text, Box, Flex, hubspot } from "@hubspot/ui-extensions"; // Define the extension to be run within the Hubspot CRM hubspot.extend(( { actions } // serverless function is not required for simply displaying an iframe ) => <Extension openIframe={actions.openIframeModal} />); // Define the Extension component, taking in openIframe as a prop const Extension = ({ openIframe }) => { const handleClick = () => { openIframe({ uri: "https://wikipedia.org/", // this is a relative link. Some links will be blocked since they don't allow iframing height: 1000, width: 1000, title: 'Wikipedia in an iframe', flush: true }); }; return ( <> <Flex direction="column" align="start" gap="medium"> <Text> Clicking the button will open a modal dialog with an iframe that displays the content at the provided URL. Get more info on how to do this {" "}. <Link href="https://developers.hubspot.com/docs/platform/create-ui-extensions#open-an-iframe-in-a-modal"> here </Link> </Text> <Box> <Button type="submit" onClick={handleClick}> Click me </Button> </Box> </Flex> </> ); };

Fetch account, user, and extension context[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#fetch-account-user-and-extension-context)
-----------------------------------------------------------------------------------------------------------------------------------------------------

The `context` object, which is passed to the extension component via `hubspot.extend`, contains information related to the authenticated user and HubSpot account, along with information about where the extension is loading. The following is an example of the information you can retrieve via `context`.

{ location: 'crm.record.tab' | 'crm.record.sidebar', crm: { objectId: number, // the current CRM record's ID objectTypeId: string, // the current CRM record's object type }, user: { id: number, // logged in user's ID email: string; // primary email emails: string\[\]; // all associated emails firstName: string; lastName: string; roles: string\[\]; // role names teams: Team\[ { id: number; name: string; teammates: number\[\]; // IDs of the user's teammates \]; locale: string; }, portal: { id: number; timezone: string; } }

Send custom log messages for debugging[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#send-custom-log-messages-for-debugging)
-----------------------------------------------------------------------------------------------------------------------------------------------

Using `logger` methods, you can send custom log messages to HubSpot for more in-depth troubleshooting of deployed extensions. Custom log messages will appear in the [app's logs in HubSpot](/docs/platform/create-private-apps-with-projects#logs), searchable by trace ID. Check out [HubSpot's custom logger sample project](/docs/platform/sample-projects#custom-logger-example) to see an implementation example.

The following methods are available:

*   `logger.info`
*   `logger.debug`
*   `logger.warn`
*   `logger.error`

Each method accepts a single string argument.

For example, the following extension code includes few different log messages to help better identify where an error has occurred:

import { logger } from '@hubspot/ui-extensions'; logger.debug('Information before my extension') hubspot.extend(({ runServerlessFunction }) => { logger.warn('Logging a warning inside extension'); useEffect(() => { runServerlessFunction('customers') .then(result => { if (result.status === 'ERROR') { logger.error(\`Customer fetch failed\`); return; } logger.info(JSON.stringify(result)); }) .catch(error => { logger.error(\`Customer fetch failed: ${error.message}\`); }); }, \[\]) return <Text>Hello</Text> });

When an extension fails to load on a CRM record, an error message will display. This error message will contain a trace ID, which you can copy.

![logger-debug-on-crm-record](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/logger-debug-on-crm-record.png?width=811&height=69&name=logger-debug-on-crm-record.png)Using that trace ID, you can then locate the custom log messages [within the app's logs](/docs/platform/create-private-apps-with-projects#log-traces).

### ![log-trace-example-screenshot](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/log-trace-example-screenshot.png?width=632&height=672&name=log-trace-example-screenshot.png)

### Notes and limitations[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#notes-and-limitations)

*   Custom log messages are not sent while in local development mode. They are logged to the browser console instead.
*   All logs are sent as batches with a maximum of 100 logs per batch.
*   Each HubSpot account is rate limited to 1,000 logs per minute. After exceeding that limit, all logging is stopped until the page is reloaded.
*   The logger will queue a maximum of 10,000 pending messages. Any subsequent logs will be dropped until the queue is below the maximum.
*   Queued logs are processed at a rate of five seconds per log batch.
*   Queued logs are dropped when the page or is refreshed or closed.

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-extensions-sdk#page-feedback)
---------------------------------------------------------------------------------------------------

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