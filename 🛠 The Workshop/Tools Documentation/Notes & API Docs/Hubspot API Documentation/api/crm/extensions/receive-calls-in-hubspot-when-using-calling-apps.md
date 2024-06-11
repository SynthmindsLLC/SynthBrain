---
title: "Receive calls in HubSpot when using calling apps (BETA)"
description: "This article is for Calling App Marketplace Partners and Solutions Partners, detailing how to enable the Incoming Calls feature within HubSpot. It's currently in development and subject to change based on testing and feedback. To provide feedback, contact hubspot-calling-sdk-feedback@callingproductgroup.hs-inbox.com."
type: "group"
tags:
- "Calling App Marketplace"
- "Solutions Partners"
- "HubSpot SDK"
relationships:
- "#developed_by [[HubSpot]]"
founded: "N/A"
---

Receive calls in HubSpot when using calling apps (BETA)[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#receive-calls-in-hubspot-when-using-calling-apps-beta-)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Overview](#tab-1)

*   [Overview](#tab-1)

**Please note:**

*   This article is for **Calling App Marketplace Partners** and **Solutions Partners**.
*   **This functionality is currently in development**. It is subject to change based on testing and feedback. To provide feedback, contact [hubspot-calling-sdk-feedback@callingproductgroup.hs-inbox.com](mailto:hubspot-calling-sdk-feedback@callingproductgroup.hs-inbox.com). By using these instructions you agree to adhere to [HubSpot's Developer Terms](https://legal.hubspot.com/developer-terms?revisionPreview=true) & [HubSpot's Developer Beta Terms](https://legal.hubspot.com/developerbetaterms?revisionPreview=true).
*   Learn how to **ungate** your account for this beta [here](#ungate-your-account).

With the introduction of inbound calling in the [Calling SDK](/docs/api/crm/extensions/calling-sdk), calling apps that are using HubSpot's SDK or who can move the Calling SDK integration, can now enable the Incoming Calls feature within HubSpot. When you receive and answer inbound calls using your calling app in HubSpot, you can easily access records without the need to go back into your calling app. Inbound calls save to the [Call Index Page](https://knowledge.hubspot.com/calling/review-calls-in-the-call-index) once the call is answered for easy access to take real-time notes and review the call after it ends.

### Install the latest version of Calling SDK[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#install-the-latest-version-of-calling-sdk)

For npm, run:

npm i -s @hubspot/calling-extensions-sdk@latest

For yarn, run:

yarn add @hubspot/calling-extensions-sdk@latest

### 1\. Set user availability[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#set-user-availability)

You can set the user's availability using on of the following events:

*   Via the `initialized` event:

const payload = { // Optional: Whether a user is logged-in isLoggedIn: boolean, // Optional: Whether a user is available for inbound calling isAvailable: boolean, // Optional: The desired widget size sizeInfo: { height: number, width: number } } extensions.initialized(payload);

*   Via the `userAvailable` event:

extensions.userAvailable();

*   Via the `userUnavailable` event:

extensions.userUnavailable();

### 2\. Send message to notify HubSpot that an inbound call started[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#send-message-to-notify-hubspot-that-an-inbound-call-started)

You will be able to send calling lifecycle events, such as `callAnswered` and `callCompleted`, in the same way it is done for outgoing calls.

const callInfo = { fromNumber: string, // Required: The caller's number toNumber: string, // Required: The recipient's number createEngagement: boolean, // Whether HubSpot should create an engagement for this call }; extensions.incomingCall(callInfo);

*   If you’ve set `createEngagement` to true, you can subscribe to `onCreateEngagementSucceeded` and `onCreateEngagementFailed`. It is recommend you do this so that you can enable your calling app to support [custom objects](/docs/api/crm/crm-custom-objects). This will allow future integration into other areas of HubSpot. 

onCreateEngagementSucceeded(data) { const { /\* A HubSpot created engagement id. \*/ engagementId: number, } = data; ... } onCreateEngagementFailed(data) { const { error: { message: string } } = data; ... }

### 3\. Receive caller ID matches[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#receive-caller-id-matches)

*   You will be able to subscribe to `onCallerIdMatchSucceeded` and `onCalledIdMatchFailed`. This will enable you to receive contact matching data for the incoming call that previously had to be obtained via the [Search API](/docs/api/crm/search), and will solve its rate limitations. 

onCallerIdMatchSucceeded: data => { /\* HubSpot has fetched caller id matches for this call. \*/ const { callerIdMatches: (ContactIdMatch | CompanyIdMatch)\[\]; } = data; } onCallerIdMatchFailed: data => { /\* HubSpot has failed to fetch caller id matches for this call. \*/ const { error: { message: string } } = data; }

type ObjectCoordinates = { portalId: number; objectTypeId: string; objectId: number; } type ContactIdMatch = { callerIdType: 'CONTACT'; objectCoordinates: ObjectCoordinates; firstName: string; lastName: string; email: string; } type CompanyIdMatch = { callerIdType: 'COMPANY'; objectCoordinates: ObjectCoordinates; name: string; }

### 4\. Navigate to a record page[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#navigate-to-a-record-page)

Once you receive the caller ID matches, you can send HubSpot a message to navigate to a [contact or company record page](https://knowledge.hubspot.com/crm-setup/create-customize-and-manage-your-saved-views).

const data = { objectCoordinates: ObjectCoordinates // from onCallerIdMatchSucceeded }; extensions.navigateToRecord(data);

Once the call engagement is created, HubSpot will redirect to the contact page specified in the `navigateToRecord` payload and will sync with the SDK in the `onReady` event. You'll need to re-initialize the SDK using the engagement ID and show an incoming call within the iframe.

// Receive an engagementId for an existing inbound call type Payload = { engagementId: number | undefined } // Message indicating that HubSpot is ready to receive messages onReady(payload) { // Send initialized message to HubSpot to indicate that the call widget is also ready extensions.initialized(payload); if (payload.engagementId) { // Initialize calling state in the app for existing inbound call ... } ... }

In the following sections, preview how the incoming call feature will work in your calling app.

### Ungate your account[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#ungate-your-account)

To ungate your account for this beta, open your browser developer console from a HubSpot tab, and set the following:

localStorage\['LocalSettings:Calling:supportsInboundCalling'\] = true;

### Set the provider[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#set-the-provider)

Before logging in to your calling app, you will need to select the provider from your call settings:

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar menu, click **General**. Then, click the **Calling** tab at the top.
*   Click the **Receive calls through** dropdown menu, then select your calling app.

![choose-calling-app](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/choose-calling-app.png?width=522&height=368&name=choose-calling-app.png)Once the preferred provider is selected, incoming calls will only be received through the selected provider. HubSpot will not support receiving incoming calls from multiple providers in this version. 

If you wish to change the provider for receiving calls, you will have to go back to [your call settings](#call-settings) to make the change.

**Please note****:** for outbound calls, you can [continue to switch providers](https://knowledge.hubspot.com/calling/integrate-a-third-party-calling-provider-with-hubspot)from the contact record.

![select-calling-app](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/select-calling-app.png?width=646&height=444&name=select-calling-app.png)

### Receive incoming calls[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#receive-incoming-calls)

If you've not already set up an integration with any of the [calling apps](https://ecosystem.hubspot.com/marketplace/apps/sales/calling), click [here](https://knowledge.hubspot.com/calling/integrate-a-third-party-calling-provider-with-hubspot) to learn more.

*   Log in to your calling app through the call widget in HubSpot. The call widget can be accessed on the main navigation bar.

![open-calling-widget](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/open-calling-widget.png?width=683&height=349&name=open-calling-widget.png)

*   Set availability to enable HubSpot to start receiving calls.

![set-availability](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/set-availability.png?width=255&height=446&name=set-availability.png)

*   Answer inbound calls from the call remote.

**Please note:** the behavior may vary slightly based on each calling apps' implementation.

![answer-call-bananaphone](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/answer-call-bananaphone.png?width=396&height=655&name=answer-call-bananaphone.png)

Once the call is completed, the inbound call gets logged in the Call Index page. Missed calls will also get logged here.

**Please note:** if the call widget is minimized but you're set to _Available_, you will still receive calls. If the call tab is closed during an ongoing call, the call will get disconnected.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/receive-calls-in-hubspot-when-using-calling-apps#page-feedback)
--------------------------------------------------------------------------------------------------------------------------------------------

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