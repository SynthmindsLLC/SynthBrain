---
title: "Call Recording and Transcription Integration in HubSpot"
description: "If you want to make call recordings playable in your HubSpot account, or build on top of HubSpot's Conversation Intelligence functionality, use the endpoints to automatically transcribe calls and log them within HubSpot. Requirements include only .WAV, .FLAC, and .MP4 audio files being transcribed by splitting the audio file into different channels for each speaker. Create an endpoint to provide authenticated recording URLs for a call with parameters like externalId, externalAccountId, and appId. Register your app's endpoint using HubSpot's calling settings API. Log calls using the engagements API and associate them with records to ensure transcripts appear on the record timeline. Mark call recordings as ready for transcription before September 2024 when unauthenticated approach will no longer be supported."
type: "integration"
tags:
- "HubSpot"
- "Call Recording"
- "Transcription"
relationships:
- "#requires [[Conversation Intelligence]]"
- "#uses_endpoint [[Create an endpoint to provide an authenticated recording URL for a call]]"
- "#creates [[Log a call with your app's endpoint using the engagements API]]"
- "#associates [[Associate calls with records]]"
- "#marks [[Mark a call recording as ready]]"
---

Recordings and transcripts
==========================

If you want to make call recordings playable in your HubSpot account, or you want to build on top of HubSpot's [Conversation Intelligence](https://knowledge.hubspot.com/calling/manage-phone-numbers-registered-for-calling#turn-on-conversation-intelligence-sales-hub-or-service-hub-enterprise-only) functionality, you can use the endpoints to automatically transcribe calls and log them within HubSpot. 

Requirements[](https://developers.hubspot.com/docs/api/crm/extensions/recordings-and-transcriptions#requirements)
-----------------------------------------------------------------------------------------------------------------

*   HubSpot will only transcribe calls associated with [users with a paid _Sales_ or _Services_ hub seat](https://knowledge.hubspot.com/account/manage-sales-hub-and-service-hub-paid-users).
*   Only .WAV, .FLAC, and .MP4 audio files will be transcribed.
*   In the transcription system, HubSpot splits the audio file into its different channels and treats each channel as a separate speaker. If all of the speakers are on the same audio channel, or if the caller or recipient are on an unexpected channel, HubSpot will not be able to transcribe the audio recording. Therefore, each speaker in an audio file should be on a separate channel. For calls with two channels, the caller should be on channel 1, and the call recipient should be on channel 2, regardless of whether the call is inbound or outbound. 

Create an endpoint to provide an authenticated recording URL for a call[](https://developers.hubspot.com/docs/api/crm/extensions/recordings-and-transcriptions#create-an-endpoint-to-provide-an-authenticated-recording-url-for-a-call)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To list and transcribe calls on a [record's timeline](https://knowledge.hubspot.com/crm-setup/view-the-history-of-an-activity-in-a-timeline) in HubSpot, create an endpoint that will be invoked to retrieve the authenticated call URLs associated with each engagement.

Your endpoint should accept the following parameters:

*   **externalId:** the unique ID associated with a call URL, provided as a path parameter. This will correspond to the same parameter you include in the metadata of your `POST` request to the engagements API, which you can then use in your app's backend to associate with the recording URL.
*   **externalAccountId:** a unique ID associated with the HubSpot account that made the call engagement, provided as a query parameter. You can use this parameter along with the externalId to identify the call recording.
*   **appId:** the [ID of your app](https://legacydocs.hubspot.com/docs/faq/how-do-i-find-the-app-id), provided as a query parameter.

Your endpoint should return a JSON response with a `authenticatedUrl` field that provides the recording URL.

// Response to GET request to your app's endpoint { "authenticatedUrl": "https://app-test.com/retrieve/authenticated/recordings/test-call-01" }

Register your app's endpoint with HubSpot using the calling settings API[](https://developers.hubspot.com/docs/api/crm/extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Once your endpoint is ready, make a `POST` request using your app's ID to `/crm/v3/extensions/calling/{appId}/settings/recording` and provide the URL of your endpoint with the `urlToRetrieveAuthedRecording` parameter in the body of your request.

*   Your endpoint's URL must contain the _%s_ character sequence, which HubSpot will substitute with the `externalId` of the engagement when calling your endpoint. The _%s_ character sequence can be located anywhere in your URL.
*   Provide the full path of your endpoint URL in your `POST` request, including the _https://_ prefix.

For example:

// Example POST request to configure your app's endpoint { "urlToRetrieveAuthedRecording": "https://app-test.com/retrieve/authenticated/recordings/%s" }

If you change the location of your endpoint, you can make a `PATCH` request to the same HubSpot endpoint above and provide an updated value for `urlToRetrieveAuthedRecording`.

Log a call with your app's endpoint using the engagements API[](https://developers.hubspot.com/docs/api/crm/extensions/recordings-and-transcriptions#log-a-call-with-your-app-s-endpoint-using-the-engagements-api)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After you've registered your calling app's endpoint with HubSpot, you can log a call by making a `POST` request to the `/crm/v3/objects/calls` [endpoint](/docs/api/crm/calls), and including the engagement data within the properties field in the body of your request.

 The `hs_call_external_id`, `hs_call_external_account_id`, `hs_call_app_id`, and `hs_call_source` properties are required to ensure that HubSpot can fetch the authenticated recording URL.  
  
The body of an example request is shown below:

// POST request to https://api.hubapi.com/crm/v3/objects/calls { "properties": { "hs\_timestamp": "2021-03-17T01:32:44.872Z", "hs\_call\_title": "Test v3 API", "hubspot\_owner\_id": "11526487", "hs\_call\_body": "Decision maker out, will call back tomorrow", "hs\_call\_duration": "3800", "hs\_call\_from\_number": "(555) 555 5555", "hs\_call\_to\_number": "(555) 555 5555", "hs\_call\_source" : "INTEGRATIONS\_PLATFORM", // this has to be INTEGRATIONS\_PLATFORM "hs\_call\_status": "COMPLETED", "hs\_call\_app\_id": "test-app-01", "hs\_call\_external\_id": "test-call-01", "hs\_call\_external\_account\_id": "test-account-01" } }

Next, you'll need to [associate the call with a record type](/docs/api/crm/calls#associate-calls-with-records) to ensure the transcript appears on the record timeline.

*   To make this association, make a `PUT` request to `/crm/v3/objects/calls/{callId}/associations/{toObjectType}/{toObjectId}/{associationType}`.
*   For example, if the ID of the logged call you created above is _17591596434_, the ID of the contact you wanted to associate it with is _104901_, and the ID of the associationType is _194_, your request URL would be:

`https://api.hubspot.com/crm/v3/objects/calls/17591596434/associations/contacts/104901/194`

When one of your app's users navigates to the associated record timeline to view the engagement, HubSpot will call the endpoint you configured to serve the authenticated recording URL. For example, to retrieve the recording URL associated with the example engagement above, HubSpot would make a `GET` request to:

`https://app-test.com/retrieve/authenticated/recordings/test-call-01?appId=app-101&externalAccountId=test-account-01`

Mark a call recording as ready[](https://developers.hubspot.com/docs/api/crm/extensions/recordings-and-transcriptions#mark-a-call-recording-as-ready)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Create the call object as shown [above](#log-a-call-with-your-app-s-endpoint), and then do the following:

Make a `POST` request to `/crm/v3/extensions/calling/recordings/ready` with the `engagementId` for the call that was created. This will notify HubSpot that the recording is ready and transcription can begin.

The body of an example request is shown below: 

// Example POST request to log a recording as being ready for a call { "engagementId": 17591596434 }

**Please note:** if you're using the legacy approach of logging call recordings without authentication, please update to the authenticated approach before September 2024. After this time, the unauthenticated approach will no longer be supported.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/recordings-and-transcriptions#page-feedback)
-------------------------------------------------------------------------------------------------------------------------

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