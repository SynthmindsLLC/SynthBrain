**Video Conference Extension**
==============================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The Video Conference API gives integrators the ability to plug into the meeting creation flow within HubSpot and add video conference information. Using this API will involve the following steps: 

1.  Set up your app with Video Conference Extensions webhooks. You will provide URIs to HubSpot that HubSpot will use to notify you when customers are creating or updating meetings. 
2.  Handle the meeting creation webhooks and, optionally, the meeting update webhooks. 
3.  Handle user identity verification webhooks, if necessary. 

Settings API 
-------------

Developers will use this Settings API to set up an existing application. You can use the access token from your [private app](/docs/api/private-apps) to authenticate the request. 

### Settings object definition 

The settings object has the following fields: 

`createMeetingUrl`: The URL where we'll send requests for new video conferences. This must use the `https` protocol. 

`updateMeetingUrl:` (optional) The URL where we'll send updates to existing meetings. Typically called when the user changes the topic or times of a meeting. This must use the https protocol. 

`deleteMeetingUrl:` (optional) The URL where we'll notify you of meetings that have been deleted in HubSpot. 

`userVerifyUrl:` (optional) The URL we will use to verify that a user exists in your system.   
  

### Create or update video conference extension settings 

**Example request:**

`PUT /crm/v3/extensions/videoconferencing/settings/{appId}`

JSON

Copy all

    //example request
    
    {
    "createMeetingUrl": "https://example.com/create-meeting",
    "updateMeetingUrl": "https://example.com/update-meeting",
    "deleteMeetingUrl": "https://example.com/delete-meeting"
    }

**Example Response:** 

JSON

Copy all

    // example 200 response
    {
    "createMeetingUrl": "https://example.com/create-meeting",
    "updateMeetingUrl": "https://example.com/update-meeting",
    "deleteMeetingUrl": "https://example.com/delete-meeting"
    }

**Example Response:**

Optional values should be excluded from the request; providing empty strings or other values will likely result in undesired behavior.

### Fetch video conference extension settings

**Example request:**

`GET /crm/v3/extensions/videoconferencing/settings/{appId}   `

**Example response:**

JSON

Copy all

    // example 200 response
    {
    "createMeetingUrl": "https://example.com/create-meeting",
    "updateMeetingUrl": "https://example.com/update-meeting"
    "deleteMeetingUrl": "https://example.com/delete-meeting"
    "userVerifyUrl": "https://example.com/user-verify"
    }

### Create Meeting webhook

When a meeting is created HubSpot will send a request to the `createMeetingUri` 

**Example request:**

JSON

Copy all

    // example request
    {
    "portalId": 123123,
    "userId": 123,
    "userEmail": "test.user@example.com",
    "topic": "A Test Meeting",
    "source": "MEETINGS"
    "startTime": 1534197600000,
    "endTime": 1534201200000
    }

The fields in this request are:

*   `portalId`: The ID of the HubSpot account (called a portal).
*   `userId`: The unique ID for the HubSpot user that owns the meeting.
*   `userEmail`: The email address for the HubSpot user that owns the meeting.
*   `topic`: The topic/title of the meeting.
*   `source`: Either MEETINGS or MANUAL , indicating the meeting feature within  
    the HubSpot app where the meeting has been created; MEETINGS corresponds to  
    the "meeting link" function, and MANUAL corresponds to a meeting created in  
    the CRM Communicator.
*   `startTime`: The start time of the meeting (in epoch milliseconds)
*   `endTime`: The end time of the meeting (in epoch milliseconds)  
      
    

To successfully handle this webhook, the developer should generate a video conference for this meeting (or link it to an existing conference line), and respond with information about this conference.

  
**Example response:**

JSON

Copy all

    //example response
    {
    "conferenceId": "some-unique-id",
    "conferenceUrl": "https://example.com/join",
    "conferenceDetails": "Click here to join: https://example.com/join"
    }

The fields expected in this response are:

*   `conferenceId`: A unique ID associated with the conference on this event.  
    This ID needs to be globally unique within your system. We'll return this ID  
    back to you in the update webhook.
*   `conferenceUrl:` The join link for the created conference. This may be  
    placed in the "location" field of events.
*   `conferenceDetails`: Plain text "invitation" information. This should describe  
    how attendees of the event can access the video conference for this  
    event. Newlines will be maintained in representations of this text within our  
    system, but no other formatting is supported.

### Update Meeting Webhook

If you've specified a `updateMeetingUri` , HubSpot will send this URI a request whenever a meeting's relevant details have changed. This notification is necessary if you need to maintain the most up-to date topic or times for a video conference.

  
**Example request:**

JSON

Copy all

    //example request
    {
    "conferenceId": "some-unique-id",
    "userId": 123,
    "userEmail": "test.user@example.com",
    "portalId": 123123,
    "topic": "A Test Meeting (updated)",
    "startTime": 1534197600000,
    "endTime": 1534201200000
    }

The fields expected in this response are:

*   `conferenceId`: The unique ID for the conference provided by your integration in the response to the create meeting webhook.
*   `userId`: The unique ID for the HubSpot user that owns the meeting. This will always be the same userId as the create meeting request.
*   `userEmail`: The email address for the HubSpot user that owns the meeting. This will always be the same userEmail as the create meeting request.
*   `topic`: The topic/title of the meeting.
*   `startTime`: The start time of the meeting (in epoch milliseconds)

`endTime`: The end time of the meeting (in epoch milliseconds)  
  
No response body is required when responding to these requests. We require only  
a 200 or 204 response code to let us know that this webhook has been received  
successfully.

### Delete Meeting Webhook

When a meeting is deleted in HubSpot we'll send a request to the `deleteMeetingUri.`  
**Example request:**

JSON

Copy all

    //example request
    {
    "conferenceId": "some-unique-id"
    }

This request just contains the conferenceId of the meeting that was deleted.  
No response body is required when responding to these requests. We require only  
a 200 or 204 response code to let us know that this webhook has been received  
successfully.

### User Verify Webhook

HubSpot's systems will always communicate with you about its users in terms of their HubSpot user ID and their HubSpot account email address. There is a chance that a user in HubSpot's system may exist in your system with a different email address or identifier.

Before we make a call to your system to create, update, or delete a web conference link, we will first check your settings for a `userVerifyUri` , and, if that URI has been set, we will make a call to it to retrieve your native user identifier. We will then send that identifier as the user's email address in the  
subsequent call.

There are places in the HubSpot application where we may make this call to you to validate that the user exists in your system before we display UI components that they can interact with, as a kind of pre-verification. If you do not configure this URI, we will always assume that the user's identity is verified.  
  
It is up to you whether you support this feature. If you need to maintain a user mapping within your system, you may wish to simply map the HubSpot user ID or email to your internal user ID on each call.

  
**The request will look like this:**

JSON

Copy all

    //example request
    {
    "portalId": 123123,
    "userEmail": "test.user@example.com"
    }

You can return a 200 or any error code (404 would be appropriate). If you return a 200, you should return a payload containing the new ID that we should use in place of "email":

JSON

Copy all

    //example response
    {
    "id": "any-string-id"
    }

### Webhook signing

All of the Webhooks sent by HubSpot are HMAC signed using your application's "app secret". See the "Security" section on [this page](/docs-beta/webhooks): (The rest of this Webhooks Overview page does not apply to these video conference extension webhooks.)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/video-conferencing#page-feedback)
--------------------------------------------------------------------------------------------------------------

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