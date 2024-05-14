Calling Extensions SDK
======================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

**Please note:** Our calling app partners no longer need to create and update call engagements manually; HubSpot will do it for them. Learn more [here](/docs/api/crm/extensions/use-hubspot-owned-engagements-to-create-and-update-call-engagements).

The [Calling Extensions SDK](https://github.com/HubSpot/calling-extensions-sdk) allows apps to provide a custom calling option to HubSpot users directly from a record in the CRM. 

A calling extension consists of three main components:

1.  The [Calling Extensions SDK](https://github.com/HubSpot/calling-extensions-sdk), a JavaScript SDK that enables communication between your app and HubSpot.
2.  The **calling settings endpoints**, which are used to set the calling settings for your app. Each HubSpot account that connects to your app will use these settings.
3.  The **calling iframe**, which is where your app appears to HubSpot users and is configured using the calling settings endpoints.

For more information on the in-app calling experience, review [this knowledge base article](https://knowledge.hubspot.com/calling/use-the-calling-tool#call-from-your-phone). Once your calling extension-enabled app is connected to HubSpot, it will appear as an option in the call switcher whenever a user [makes a call from HubSpot](https://knowledge.hubspot.com/calling/use-the-calling-tool).

If you don't have an app, you can [create one from your HubSpot developer account](/docs/api/account-types#app-developer-accounts). If you don't already have a HubSpot developer account, sign up for one [here](https://app.hubspot.com/signup/developers).

**Please note:** only outgoing calls are currently supported.

Run the demo calling app[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#run-the-demo-calling-app)
-----------------------------------------------------------------------------------------------------------------------

You have the option to test the Calling Extensions SDK on two different demo apps:

*   The [demo-minimal-js](https://github.com/HubSpot/calling-extensions-sdk/tree/master/demos/demo-minimal-js) features a minimal implementation of the SDK using JavaScript, HTML, and CSS. View how the SDK is instantiated in [index.js](https://github.com/HubSpot/calling-extensions-sdk/blob/project-demo-v1/demos/demo-minimal-js/index.js).
*   The [demo-react-ts](https://github.com/HubSpot/calling-extensions-sdk/tree/master/demos/demo-react-ts) features a real-life implementation of the SDK using React, TypeScript, and Styled Components to act as a blueprint for your app. View how the SDK is instantiated in [useCti.ts](https://github.com/HubSpot/calling-extensions-sdk/blob/master/demos/demo-react-ts/src/hooks/useCti.ts).

**Please note:** these demo apps aren't fully functional calling apps and use mock data to provide a more realistic experience.

### Install the demo calling app[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#install-the-demo-calling-app)

You can run the demo apps with or without installation. To install the demo on your local environment:

1.  Install [Node.js](https://nodejs.org/en) on your environment.
2.  Clone, fork, or [download the ZIP](https://github.com/HubSpot/calling-extensions-sdk/archive/refs/heads/master.zip) of this repository.
3.  Open your terminal, and navigate to the root directory of the project.
4.  Run one of the following commands:
    
    *   For the `demo-minimal-js`:
    

cd demos/demo-minimal-js && npm i && npm start

*   For the `demo-react-ts`:

cd demos/demo-react-ts && npm i && npm start

These will switch to the desired demo directory, install the [Node.js](https://nodejs.org/en/) dependencies required for the project using the [npm CLI](https://docs.npmjs.com/cli/v9), and start the app. 

**Please note:** the `npm start` command will automatically open a new tab in your browser at [https://localhost:9025/](https://localhost:9025/), and you may need to bypass a "Your connection is not secure" warning in order to access the application.

### Launch the demo calling app from HubSpot[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#launch-the-demo-calling-app-from-hubspot)

1.  Navigate to your records:.
    *   **Contacts:** In your HubSpot account, navigate to **Contacts > Contacts**.
    *   **Company:** In your HubSpot account, navigate to **Contacts > Companies**.
2.  Open your browser's developer console, and run the following command:
    *   If you've completed the installation steps, for the `demo-minimal-js` or the `demo-react-ts`:

localStorage.setItem("LocalSettings:Calling:installDemoWidget", "local");

*   If you've skipped the installation steps:
    *   For the `demo-minimal-js`:

localStorage.setItem("LocalSettings:Calling:installDemoWidget", "app:js");

*   For the `demo-react-ts`:

localStorage.setItem("LocalSettings:Calling:installDemoWidget", "app");

1.  Refresh the page, and click the **Call** icon in the left sidebar. Click the **Call from** dropdown menu, and select the **name** of the demo app from step 2 (e.g. Demo App Local, Demo App JS, Demo App React).   
    ![call-app-in-record](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/call-app-in-record.png?width=780&height=392&name=call-app-in-record.png)
2.  Click **Call** to see how the demo app integrates with HubSpot via the Calling Extensions SDK. You can also see the events logged to your browser's developer console.

![calling-sdk-in-app](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/calling-sdk-in-app.png?width=244&height=414&name=calling-sdk-in-app.png) 

Install the Calling Extensions SDK on your calling app[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#install-the-calling-extensions-sdk-on-your-calling-app)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To add the Calling Extensions SDK as a [Node.js](https://nodejs.org/en/) dependency to your calling app:

*   For npm, run:

npm i --save @hubspot/calling-extensions-sdk

*   For yarn, run:

yarn add @hubspot/calling-extensions-sdk

Typical message flow between the calling app and HubSpot[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#typical-message-flow-between-the-calling-app-and-hubspot)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Calling Extensions SDK exposes a simple API for HubSpot and a calling app to exchange messages. The messages are sent through methods exposed by the SDK and received through `eventHandlers`.

The following is a description of the events:

1.  **Dial number:** HubSpot sends the dial number event.
2.  **Outbound call started:** App notifies HubSpot when the call is started.
3.  **Create engagement:** HubSpot creates [a call engagement](/docs/api/crm/calls) with minimal information if requested by the app.
4.  **Engagement created:** HubSpot created an engagement.
5.  **EngagementId sent to App:** HubSpot sends the `engagementId` to the app.
6.  **Call ended:** App notifies when the call is ended.
7.  **Call completed:** App notifies when the user is done with the app user experience.
8.  **Update engagement:** App fetches the engagement by the `engagementId`, then merges and updates the engagement with additional call details. Learn more about [updating a call engagement via the API](/docs/api/crm/calls#update-calls)or [via the SDK](/docs/api/crm/extensions/use-hubspot-owned-engagements-to-create-and-update-call-engagements).

Using the Calling Extensions SDK[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#using-the-calling-extensions-sdk)
---------------------------------------------------------------------------------------------------------------------------------------

### Create an instance[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#create-an-instance)

To begin, create an instance of the `CallingExtensions` object. You can define the behavior of your extension by providing an option's object when you create your extensions instance. This option's object provides an `eventHandlers` field where you can specify the behavior of your extension. The following code block illustrates the available options and event handlers you can define:

import CallingExtensions from "@hubspot/calling-extensions-sdk"; const options = { /\*\* @property {boolean} debugMode - Whether to log various inbound/outbound debug messages to the console. If false, console.debug will be used instead of console.log \*/ debugMode: true | false, // eventHandlers handle inbound messages eventHandlers: { onReady: () => { /\* HubSpot is ready to receive messages. \*/ }, onDialNumber: event => { /\* HubSpot sends a dial number from the contact \*/ }, /\*\* onEngagementCreated will be @deprecated in 2024 \*/ onEngagementCreated: event => { /\* HubSpot has created an engagement for this call. \*/ }, onCreateEngagementSucceeded: event => { /\* HubSpot has created an engagement for this call. \*/ } onEngagementCreatedFailed: event => { /\* HubSpot has failed to create an engagement for this call. \*/ } onUpdateEngagementSucceeded: event => { /\* HubSpot has updated an engagement for this call. \*/ }, onUpdateEngagementFailed: event => { /\* HubSpot has failed to update an engagement for this call. \*/ } onVisibilityChanged: event => { /\* Call widget's visibility is changed. \*/ } } }; const extensions = new CallingExtensions(options);

### Sending messages to HubSpot[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#sending-messages-to-hubspot)

The `extensions` object provides the following event handlers that you can invoke to send messages to HubSpot or to specify other associated behavior. See examples below.

*   `initialized`: send a message indicating that the soft phone is ready for interaction. 

// The initialized call allows you to send a message indicating that the soft phone is ready for interaction. const payload = { // Whether a user is logged-in isLoggedIn: true|false, // Optionally send the desired widget size sizeInfo: { height: number, width: number } } extensions.initialized(payload);

*   `userLoggedIn`: sends a message indicating that the user has logged in.

// Sends a message indicating that user has logged in // This message is only needed when user isn't loged in when initialized extensions.userLoggedIn();

*   `userLoggedOut`: sends a message indicating that the user has logged out.

// Sends a message indicating that user has logged out extensions.userLoggedOut();

*   `outgoingCall`: sends a message to notify HubSpot that an outgoing call has started. 

// Sends a message to notify HubSpot that an outgoing call has started. const callInfo = { phoneNumber: string, /\*\* @deprecated Use toNumber instead \*\*/ callStartTime: number, // in milliseconds createEngagement: true, // whether HubSpot should create an engagement for this call toNumber: // Required: The recipient's number fromNumber: string, // Required: The caller's number }; extensions.outgoingCall(callInfo);

*   `callAnswered`: sends a message to notify HubSpot that an outgoing call is being answered.

extensions.callAnswered();

*   `callEnded`: sends a message to notify HubSpot that the call has ended.

// Sends a message to notify HubSpot that the call has ended. // After receiving the call ended event, the user can navigate away, can close the call widget. extensions.callEnded();

*   `callCompleted`: sends a message to notify HubSpot that the call has completed. Engagement properties are [owned by HubSpot](/docs/api/crm/extensions/use-hubspot-owned-engagements-to-create-and-update-call-engagements), and no longer need to be created or updated manually (see highlighted).

**Please note:** the `hideWidget` property will be ignored when the user is in a task queue with the `Call` task type.

// Sends a message to notify HubSpot that the call has completed. // After receiving the call completed event, HubSpot will // 1) insert the engagement into the timeline // 2) set the default associations on the engagement // 3) closes the widget unless \`hideWidget\` is set to false. // 4) update the engagement with any engagement properties const data = { engagementId: number, hideWidget: boolean, // (optional) defaults to true engagementProperties?: { \[key: string\]: string } // opt in to hs owned engagements by adding properties in https://developers.hubspot.com/docs/api/crm/calls#properties extensions.callCompleted(data);

*   `sendError`: sends a message to notify HubSpot that the calling app has encountered an error.

// Sends a message to notify HubSpot that the call widget has encountered an error. // After receiving the sendError event, HubSpot will display an alert popup to the user with the error message provided. const data = { message: string // error message to be displayed in the alert popup }; extensions.sendError(data);

*   `resizeWidget`: sends a message to notify HubSpot that the calling app needs to be resized.

// Sends a message to notify HubSpot that the call widget needs to be resized. // After receiving the resizeWidget event, HubSpot will use the provided height and width to resize the call widget. const data = { height: boolean // desired height of the call widget width: number, // desired width of the call widget }; extensions.resizeWidget(data);

### Receive messages from HubSpot[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#receive-messages-from-hubspot)

The `extensions` object provides the following event handlers that you can invoke when receiving messages in HubSpot or to specify other associated behavior. See examples below.

*   `onReady`: message indicating that HubSpot is ready to receive messages.

// Message indicating that HubSpot is ready to receive messages onReady() { // Send initialized message to HubSpot to indicate that the call widget is also ready extensions.initialized(payload); ... }

*   `onDial`: message indicating that the user has triggered an outbound call.

// Message indicating that user has triggered an outbound call onDialNumber(data) { const { /\* The phone nubmer to dial \*/ phoneNumber: string, /\* The id of the logged in user. \*/ ownerId: number, /\* The id of the hubspot account \*/ portalId: number, /\* HubSpot object Id of the phoneNumber \*/ objectId: number, /\* HubSpot object type of the phoneNumber \*/ objectType: CONTACT | COMPANY } = data; ... }

*   `onEngagementCreated`: message indicating that HubSpot has created `onEngagementCreated` data.

**Please note:** HubSpot is deprecating the `onEngagementCreated` event in favor of `onCreateEngagementSucceeded` in 2024.

/\*\* @deprecated \*/ // Message indicating that HubSpot has created onEngagementCreated(data) { const { /\* A HubSpot created engagement id. \*/ engagementId: number, } = data; ... }

*   `onCreateEngagementSucceeded` or `onCreateEngagementFailed` **(NEW)**: HubSpot sends a message to notify the calling app partner that the engagement update succeeded or failed.

onCreateEngagementSucceeded: event => { /\* HubSpot has created an engagement for this call. \*/ }, onCreateEngagementFailed: event => { /\* HubSpot has failed to create an engagement for this call. \*/ }

*   `onUpdateEngagementSucceeded` or `onUpdateEngagementFailed` **(NEW)**: HubSpot sends a message to notify the calling app partner that the engagement creation succeeded or failed.

onUpdateEngagementSucceeded: event => { /\* HubSpot has updated an engagement for this call. \*/ }, onUpdateEngagementFailed: event => { /\* HubSpot has failed to update an engagement for this call. \*/ }

*   `onVisibilityChanged`: message indicating if the user has minimized or hidden the calling app.

// Message indicating if user has minimized/hide the call widget onVisibilityChanged(data) { const { isMinimized, isHidden } = data; ... }

*   `defaultEventHandler`: default handler for events.

// Default handler for events. defaultEventHandler(event) { console.info("Event received. Do you need to handle it?", event); }

Test your app[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#test-your-app)
-------------------------------------------------------------------------------------------------

In order to launch the calling extensions iFrame for end users, HubSpot requires the following iFrame parameters.

{ name: string /\* The name of your calling app to display to users. \*/, url: string /\* The URL of your calling app, built with the Calling Extensions SDK \*/, width: number /\* The iFrame's width \*/, height: number /\* The iFrame's height \*/, isReady: boolean /\* Whether the widget is ready for production (defaults to true) \*/, supportsCustomObjects : true /\* Whether calls can be placed from a custom object \*/ }

### Using the calling settings endpoint[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#using-the-calling-settings-endpoint)

Using your API tool (e.g. Postman), send the following payload to HubSpot's settings API. Ensure you get the APP\_ID of your calling app and your app [DEVELOPER\_ACCOUNT\_API\_KEY](/docs/api/developer-tools-overview#authentication).

**Please note:** the `isReady` flag indicates whether the app is ready for production. This flag should be set to false during testing.

\# Example payload to add the call widget app settings curl --request POST \\ --url 'https://api.hubapi.com/crm/v3/extensions/calling/APP\_ID/settings?hapikey=DEVELOPER\_ACCOUNT\_API\_KEY' \\ --header 'accept: application/json' \\ --header 'content-type: application/json' \\ --data '{"name":"demo widget","url":"https://mywidget.com/widget","height":600,"width":400,"isReady":false}' # Note that this endpoint also supports PATCH, GET and DELETE

### Override your extension settings using localStorage[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#override-your-extension-settings-using-localstorage)

You can override any of your extension settings for testing purposes. Open your browser developer console from a HubSpot tab, edit the settings below, and run the command:

const myExtensionSettings = { isReady: true, name: "My app name", url: "My local/qa/prod URL", }; localStorage.setItem( "LocalSettings:Calling:CallingExtensions", JSON.stringify(myExtensionSettings), );

Get your app ready for production[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#get-your-app-ready-for-production)
-----------------------------------------------------------------------------------------------------------------------------------------

If you’ve already used the POST endpoint when testing your app, you can use the PATCH endpoint to change `isReady` to true. Otherwise, using your API tool (e.g. Postman), send this payload to HubSpot's settings API. Ensure you get the APP\_ID of your calling app and your app [DEVELOPER\_ACCOUNT\_API\_KEY](/docs/api/developer-tools-overview#authentication).

\# Example payload to add the call widget app settings curl --request POST \\ --url 'https://api.hubapi.com/crm/v3/extensions/calling/APP\_ID/settings?hapikey=DEVELOPER\_ACCOUNT\_API\_KEY' \\ --header 'accept: application/json' \\ --header 'content-type: application/json' \\ --data '{"name":"demo widget","url":"https://mywidget.com/widget","height":600,"width":400,"isReady":true}' # Note that this endpoint also supports PATCH, GET and DELETE

Publish your calling app to the HubSpot marketplace[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#publish-your-calling-app-to-the-hubspot-marketplace)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The final step once your app is setup is to list your calling app in the HubSpot marketplace. You can find more details [here](/submit-an-application-to-the-marketplace) . You can also choose not to list it in the marketplace if this application is for internal use only.

Calling SDK | Frequently Asked Questions[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#calling-sdk-frequently-asked-questions)
-----------------------------------------------------------------------------------------------------------------------------------------------------

### How is user authentication handled?

The calling app should handle authentication.

### Is Calling Extensions hosted on a CDN?

Yes. You can install the Calling Extensions SDK via [jsDeliver](https://www.jsdelivr.com/). For example, to install calling-extensions-sdk@0.2.2, you can use [https://cdn.jsdelivr.net/npm/@hubspot/calling-extensions-sdk@0.2.2/dist/main.js](https://cdn.jsdelivr.net/npm/@hubspot/calling-extensions-sdk@0.2.2/dist/main.js).

### When should an engagement be created versus updated?

A user can initiate a call from inside the HubSpot UI and outside the HubSpot UI (e.g. mobile app, redirected number, etc.) If a call is initiated from within HubSpot UI, HubSpot will create a call engagement and send the engagement to the calling app. Once the call finishes, the call app can update this engagement with additional call details. If a call is initiated outside of HubSpot UI, the app should create the call engagement.

### What scopes are required as a part of the integration?

Add contacts and timeline scopes are required. These scopes ensure your application has access to contacts and the ability to create and update call engagements in the CRM.

### Can this functionality be added to an already existing application in the marketplace or do I create a new app?

If you already have an existing app that serves the calling use case then you can directly add this functionality to your existing app. All customers who already have your app installed will get access to this new functionality without having to install the app again.

### Can I integrate my existing soft phone application in the SDK?

Yes, integrating your existing soft phone application should be very easy. Just follow the steps in the documentation above to have your application up and running.

### Can users use multiple integrations at the same time?

Yes, users can use multiple third-party calling integrations at the same time. They can use the provider switcher presented after clicking on the call button to seamlessly switch between providers.

### Can free users install app integrations?

Yes, all users can install the app.

### If a user already has my app installed, does the integration automatically show up?

Yes, if a user already has installed your app, and you are updating the same app with the calling extensions, the integration will automatically show up. Currently, there is no way for the developer to enable the calling app only to a subset of customers.

### Can any user install or uninstall an app?

No, only users who have necessary permissions can install and uninstall an app. Learn more about how to [review a user's permissions](https://knowledge.hubspot.com/settings/edit-user-permissions). 

### Can I create a custom calling property?

Yes, you can create a custom calling property using the [properties API](/docs/api/crm/properties).

### Can I place a call from a custom object?

Yes, calling integrations can place calls from custom objects as long as they only use the SDK to create the call. Each integration will need to verify that they only use the Calling SDK to create calls and to notify HubSpot in the `outgoingCall` event.

First, verify that the integration is using the Calling SDK to create engagements in the outgoingCall event:

outgoingCall({ createEngagement: true })

If `createEngagement` is true, learn how to update your app information [here](#get-your-app-ready-for-production).

Here is the example for the entire `outgoingCall` event:

const callInfo = { phoneNumber: string, // optional unless call is initiated by the widget createEngagement: true // whether HubSpot should create an engagement for this call callStartTime: number // optional unless call is initiated by the widget }; extensions.outgoingCall(callInfo);

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk#page-feedback)
-------------------------------------------------------------------------------------------------------

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