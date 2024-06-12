---
title: "Use HubSpot Owned Engagements to create and update call engagements"
description: "A guide on how calling app partners can leverage the Calling Extensions SDK for creating and updating call engagements with HubSpot."
type: "article"
tags:
- "HubSpot"
- "Calling App Partners"
- "Owned Engagements"
relationships:
- "#uses_calling_extensions_sdk"
- "#requires_upgrade_to_version_0.2.0"
- "#opt_in_to_hubspot_owned_engagements"
- "#sends_successful_and_failure_events"
- "#deprecating_onEngagementCreated_event_in_2024"
created: "2023-01-01"
---

Use HubSpot Owned Engagements to create and update call engagements
===================================================================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)

*   [Overview](#tab-1)

**Please note:** to access HubSpot Owned Engagements, you must upgrade to the new calling SDK version 0.2.0 and opt in to HubSpot Owned Engagements.

When using the [Calling Extensions SDK](https://github.com/HubSpot/calling-extensions-sdk), calling app partners no longer have to create and update call engagements because HubSpot will do it for them.

*   When a calling app partner logs a call, they no longer have to make any additional API calls to update call information like notes, call direction, and outcome. They can simply send HubSpot this information with an API call for logging a call and HubSpot will get this information updated for them. This includes call properties from the [Call Engagements API](https://53.hubspotpreview-na1.com/docs/api/crm/calls#properties).
*   Previously only successful events were sent for creating and updating engagements. With this change, HubSpot will start sending failure notifications so calling app partners have information on engagements that failed, and can take action accordingly.

**Please note:** to install the demo app or the Calling Extensions SDK on your calling app, click [here](/docs/api/crm/extensions/calling-sdk).

Create a call engagement[](https://developers.hubspot.com/docs/api/crm/extensions/use-hubspot-owned-engagements-to-create-and-update-call-engagements#create-a-call-engagement)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the `outgoingCall` event to create an engagement.

// Sends a message to notify HubSpot that an outgoing call has started. const callInfo = { phoneNumber: string, // optional unless call is initiated by the widget createEngagement: true, // whether HubSpot should create an engagement for this call callStartTime: number // optional unless call is initiated by the widget };

HubSpot sends the success or failure events to the third-party calling app and the app receives the event via the `onCreateEngagementSucceeded` or `onCreateEngagementFailed` handler.

onCreateEngagementSucceeded: event => { /\* HubSpot has created an engagement for this call. \*/ }, onCreateEngagementFailed: event => { /\* HubSpot has failed to create an engagement for this call. \*/ }

**Please note:** HubSpot is deprecating the `onEngagementCreated` event in 2024.

Update a call engagement[](https://developers.hubspot.com/docs/api/crm/extensions/use-hubspot-owned-engagements-to-create-and-update-call-engagements#update-a-call-engagement)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the `callCompleted` event to update an engagement with the `engagementProperties` object in the [Call Engagements API](/docs/api/crm/calls#properties).

// Sends a message to notify HubSpot that the call has completed. // After receiving the call completed event, HubSpot will // 1) insert the engagement into the timeline // 2) set the default associations on the engagement // 3) closes the widget unless \`hideWidget\` is set to false. // 4) update the engagement with any engagement properties const data = { engagementId: number, hideWidget: boolean, // (optional) defaults to true engagementProperties?: { \[key: string\]: string } // opt in to hs owned engagements by adding properties in https://developers.hubspot.com/docs/api/crm/calls#properties }; extensions.callCompleted(data);

HubSpot sends the success or failure events to the third-party calling app and the app receives the event via the `onUpdateEngagementSucceeded` or `onUpdateEngagementFailed` handler.

onUpdateEngagementSucceeded: event => { /\* HubSpot has updated an engagement for this call. \*/ }, onUpdateEngagementFailed: event => { /\* HubSpot has failed to update an engagement for this call. \*/ }

If you need further assistance, visit the [HubSpot developer support forum](https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations).

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/use-hubspot-owned-engagements-to-create-and-update-call-engagements#page-feedback)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

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