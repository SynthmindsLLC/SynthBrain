---
title: "Conversations inbox and messages APIs (BETA)"
description: "The conversations APIs enable you to manage and interact with the conversations inbox, channels, threads, and messages. For example, you can use these APIs to get and sort conversations inboxes, update thread statuses, delete and restore threads, send outbound messages via existing conversations channels, retrieve conversation data for advanced reports and analytics, integrate existing channels with other apps like Slack or Microsoft Teams, etc."
type: "group"
tags:
- "HubSpot"
- "APIs"
- "Conversations"
relationships:
- "#part_of [[Official HubSpot Documentation]]"
- "#related_to [[Slack]], [[Microsoft Teams]]"
- "#related_to [[Webhooks]]"
- "#related_to [[Files API]]"
- "#related_to [[Developer Terms]], [[Developer Beta Terms]]"
---

.hidden { display: none; } .interest-form { padding: 1em; height: 100%; } .interest-text { padding: 1em; } .hs-form>fieldset { max-width: 100% !important; }

**Please note:** this API is currently in beta and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to HubSpot's [Developer Terms](https://legal.hubspot.com/hubspot-developer-terms) and[Developer Beta Terms](https://legal.hubspot.com/developerbetaterms?). You also acknowledge and understand the risk associated with testing an unstable API.

  
Provide feedback

hbspt.forms.create({ region: "na1", portalId: "428357", formId: "037350c3-535d-4755-82ca-53b73367754f" });

First name

Last name

Email

How satisfied are you with this API beta\*

Please SelectVery satisfiedSatisfiedNeutralUnsatisfiedVery unsatisfied

Can we contact you with follow-up questions about this feedback?

*   Yes, HubSpot can contact me about this feedback 

By selecting “Yes,” you are allowing HubSpot to store any personal information submitted through this form. We respect your privacy and will only use it to contact you if we have follow-up questions about today’s feedback. You can unsubscribe from these communications at any time. For more information, check out our [Privacy Policy.](https://legal.hubspot.com/privacy-policy)

document.addEventListener('DOMContentLoaded', function() { var button = document.getElementById('toggleButton'); var hiddenDiv = document.getElementById('hiddenDiv'); button.addEventListener('click', function() { if (hiddenDiv.classList.contains('hidden')) { hiddenDiv.classList.remove('hidden'); } else { hiddenDiv.classList.add('hidden'); } }); });

Conversations inbox and messages APIs (BETA)
============================================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The conversations APIs enable you to manage and interact with the conversations inbox, channels, and messages. For example, you can use these APIs to:

*   Get and sort conversations inboxes, channels, threads, and messages.
*   Update thread statuses.
*   Delete and restore threads.
*   Send outbound messages via existing conversations channels.
*   Send an internal comment to an agent. 
*   Retrieve conversation data to create advanced reports and analytics in external tools.

You could also use these APIs to integrate existing channels with other apps such as [Slack](https://knowledge.hubspot.com/integrations/how-do-i-use-the-slack-integration) or Microsoft Teams to send replies or receive notifications. 

To get started with the conversations APIs, make sure you have [set up a HubSpot developer account](/get-started) and [created an app](/docs/api/creating-an-app). You will need a developer account ID and app ID to get access to these APIs. 

**Please note:** with these APIs, you cannot add net new channels, such as a WhatsApp channel, to the inbox. You also cannot start a new thread in an existing channel or connect a 3rd party chat provider to the inbox. 

To view all available endpoints and their requirements, click the Endpoints tab at the top of this article.

Webhooks for conversations are also supported and can be used in tandem with the conversations API. You can use webhooks to subscribe to events about conversations, including thread creation, thread status and assignment changes, and new messages on threads. Learn more about using [webhooks](/docs/api/webhooks). 

**Please note:** to make a `GET` request to any endpoints, or `POST` batch read request to the get actors endpoint, you must have `conversations.read` access. All other endpoints require `conversations.write` access.

Filter and sort results[](https://developers.hubspot.com/docs/api/conversations/conversations#filter-and-sort-results)
----------------------------------------------------------------------------------------------------------------------

When retrieving inboxes, channels, channel accounts, threads, and messages using the endpoints outlined in this article, you can use different query parameters to filter and sort your responses. 

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`sort`

 | String | 

Set the sort order of the response. You can sort by multiple properties. 

 |
| 

`after`

 | String | 

The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results. 

 |
| 

`limit`

 | Integer | 

The maximum number of results to display per page.

 |

You can also sort your results by any field on the channel, channel accounts, or inbox objects. For example, you could sort inboxes by name, or channel accounts by both channel ID and name. 

Inboxes[](https://developers.hubspot.com/docs/api/conversations/conversations#inboxes)
--------------------------------------------------------------------------------------

To retrieve a list of inboxes set up in your account, make a `GET` request to `conversations/v3/conversations/inboxes`.

When you make a successful request, the response will include the inbox IDs of the different inboxes set up in your account. To retrieve details about a specific inbox, use the inbox ID to make a `GET` request to `conversations/v3/conversations/inboxes/{inboxId}`.

Channels[](https://developers.hubspot.com/docs/api/conversations/conversations#channels)
----------------------------------------------------------------------------------------

You can retrieve a list of the channels connected to your inboxes by making a `GET` request to `conversations/v3/conversations/channels`. 

When you make a successful request, the response will include the channel IDs for the different channels connected to your inbox. To retrieve a specific channel, use the channel ID to make a `GET` request to `conversations/v3/conversations/channels/{channelId}`. 

You can also retrieve channel accounts, which are instances of a channel that are used to send and receive messages, like a specific chatflow created for one of your chat channels or a team email address connected as an email channel. 

To retrieve a list of channel accounts, make a `GET` request to `conversations/v3/conversations/channel-accounts`. You can limit the results by including the following parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`channelId`

 | 

The ID of the channel type for which you're retrieving a channel instance. 

 |
| 

`inboxId`

 | 

The ID of the inbox that the channel is connected to. 

 |

For example, your request may look similar to the following:  
`https://api.hubspot.com/conversations/v3/conversations/channel-accounts?channelId=1000&inboxId=448`.

When you make a successful request, the response will include an ID number, which is the channel account ID.![channel-account-id-in-response-headers](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/channel-account-id-in-response-headers.png?width=476&name=channel-account-id-in-response-headers.png)

You can use the channel account ID to retrieve a single channel account, such as a specific chatflow. To retrieve a specific channel account, make a `GET` request to `conversations/v3/conversations/channel-accounts/{channelAccountId}`. 

Threads & messages[](https://developers.hubspot.com/docs/api/conversations/conversations#threads-messages)
----------------------------------------------------------------------------------------------------------

### Retrieve threads[](https://developers.hubspot.com/docs/api/conversations/conversations#retrieve-threads)

Threads are a group of related messages that make up a conversation in the inbox. To retrieve a list of all threads in your conversations inbox, make a `GET` request to `conversations/v3/conversations/threads`. To filter and search your results, you can use the following parameters in your request:

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`archived`

 | Boolean | 

To retrieve archived threads, use the value `true`. 

 |
| 

`sort`

 | String | 

Set the sort order of the response. Valid options include `id` , which is the default,  and `latestMessageTimestamp` , which requires the `latestMessageTimestampAfter` field to also be set. Results are always returned in ascending order.

 |
| 

`after`

 | String | 

The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results. Use this parameter when sorting by ID. 

 |
| 

`latestMessageTimestampAfter`

 | String | 

The minimum `latestMessageTimestamp`. This is required only when sorting by `latestMessageTimestamp`.

 |
| 

`limit`

 | Integer | 

The maximum number of results to display per page.

 |

When you make a successful request, the response will include the thread ID, which you can use to retrieve, update, or create a new message in a thread. 

To retrieve a specific thread by thread ID, make a `GET` request to `conversations/v3/conversations/threads/{threadId}`. 

### Retrieve messages[](https://developers.hubspot.com/docs/api/conversations/conversations#retrieve-messages)

To get the entire message history, make a `GET` request to `conversations/v3/conversations/threads/{threadId}/messages`.

When you make a successful request, the response will include the message ID, which you can use to retrieve a specific message. To do so, make a `GET` request to `conversations/v3/conversations/threads/{threadId}/messages/{messageId}`. 

For email messages, HubSpot cuts off the reply history section of an email. This is similar to how common mail clients handle reply history and longer emails. When you retrieve a message, the response will include a `truncationStatus` field. The value will either be `NOT_TRUNCATED`, `TRUNCATED_TO_MOST_RECENT_REPLY,` or `TRUNCATED`.

If a message is truncated, you can make a `GET` request to `conversations/v3/conversations/threads/{threadId}/messages/{messageId}/original-content`. This will retrieve the full original version of the message. 

### Retrieve a subset of messages associated with a specific contact[](https://developers.hubspot.com/docs/api/conversations/conversations#retrieve-a-subset-of-messages-associated-with-a-specific-contact)

You can also fetch messages associated with a single contact, which can be helpful if you're creating a view where a customer can review the conversations they've had with your business.

To filter for messages associated with a contact, provide the ID of the contact as the `associatedContactId` as a query parameter in the URL of your request, along with a `threadStatus` parameter, which can be either `OPEN` or `CLOSED`.

For example, to retrieve open threads associated with a contact whose ID is `53701`, you'd make a `GET` request to the following URL:

`https://api.hubapi.com/conversations/v3/conversations/threads?associatedContactId=53701&threadStatus=OPEN`

### Get actors[](https://developers.hubspot.com/docs/api/conversations/conversations#get-actors)

Actors are entities that interact with conversations, like a HubSpot user responding to a message or a visitor sending a message. When you make a request to retrieve threads or messages, the response will include actor IDs.

All actor IDs are a single letter representing the actor type, followed by a hyphen, followed by an identifier for the actor. The identifier could be a number, a string, etc. depending on the actor type. In the table below, learn more about the different actor IDs: 

Use this table to describe parameters / fields
| Actor Type | Identifier | Description |
| --- | --- | --- |
| 
`A-`

 | HubSpot user ID (number) | 

Agent actor, i.e. a user in the account. 

 |
| 

`E-`

 | Email address (string) | 

Email actor. This is used for email addresses that HubSpot didn't try to resolve to an agent actor or a visitor actor. For example, HubSpot will generally resolve the from email address to a contact, but if an incoming email has any additional email addresses included in the _To_ field, _CC_ field, etc., HubSpot won't try to resolve those email addresses to contacts. 

 |
| 

`I-`

 | App ID (number) | 

Integration actor. This is used for actions taken by an integration. 

 |
| 

`S-`

 | S-hubspot (string) | 

System actor. This is used for actions taken by the HubSpot system itself. 

 |
| 

`V-`

 | Contact ID (number) | 

Visitor actor. Keep in mind that it's possible the visitor isn't a contact yet. 

 |

For example, if you make a `GET` request to `conversations/v3/conversations/threads/{threadId}/messages`, the response will include a `sender` and `recipient` fields. These fields will include the actor IDs for the visitor or agent. For example, your response may look similar to the following: ![actorID-response-headers](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/actorID-response-headers.png?width=600&name=actorID-response-headers.png)To retrieve a single actor, make a `GET` request to `conversations/v3/conversations/actors/{actorId}`. You will need the `actorId`, which is included in the response to a request to get a message or thread. The response will return details like the actor name, email address, avatar, and actor type. 

### Update or restore threads[](https://developers.hubspot.com/docs/api/conversations/conversations#update-or-restore-threads)

You can update a thread's status by making a `PATCH` request to `conversations/v3/conversations/threads/{threadId}`. In the request body, include the thread properties to update. 

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`status`

 | 

The status of the thread, which can be `OPEN` or `CLOSED`. 

 |

To restore any soft-deleted threads, make a `PATCH` request to `conversations/v3/conversations/threads/{threadId}?archived=true` to retrieve the archived thread, then in the request body set the archived property to `false`. 

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`archived`

 | 

Set to `false` to restore a thread. 

 |

**Please note:** at this time you can only update the thread's status or restore a thread when making a `PATCH` request to this endpoint. 

### Archive threads[](https://developers.hubspot.com/docs/api/conversations/conversations#archive-threads)

You can archive a thread by making a `DELETE` request to `conversations/v3/conversations/threads/{threadId}`. 

If you use this endpoint to archive a thread, the thread will be moved to the trash and will be permanently deleted after 30 days. In the section above, learn how to restore a thread before it is permanently deleted. 

### Add comments to threads[](https://developers.hubspot.com/docs/api/conversations/conversations#add-comments-to-threads)

To add a comment to an existing thread, make a `POST` request to `conversations/v3/conversations/threads/{threadId}/messages`. Comments only appear in the inbox and are not sent to visitors.

You can include the following fields in the request body when sending a comment: 

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`type`

 | 

The type of message you're sending. This value can either be `MESSAGE` or `COMMENT`. 

 |
| 

`text`

 | 

The content of the message. 

 |
| 

`richText`

 | 

The content of the message in HTML format. This is optional. 

 |
| 

`attachments`

 | 

Any attachments to attach to the comment, specified as an object containing a `fileId`. If you want to include a specific attachment, you can upload it using the [Files API](https://developers.hubspot.com/docs/api/files/files) before making the call to add the comment. 

 |

For example, your request body may look similar to the following:

// POST request to conversations/v3/conversations/threads/{threadId}/messages { "type": "COMMENT", "text": "Can you follow up?", "richText": "<p>Can you follow up?</p>" }

### Send messages to threads[](https://developers.hubspot.com/docs/api/conversations/conversations#send-messages-to-threads)

Using this endpoint, an integration can send outgoing messages as a user in a HubSpot account. These messages are sent from the channel, just like if a user typed and sent a response in the inbox. To send a message to an existing thread, make a `POST` request to `conversations/v3/conversations/threads/{threadId}/messages`. 

When sending a message to a thread, you can include the following fields. You can include both the message details, as well as recipient information, in the request body. 

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`type`

 | 

The type of message you're sending. This value can either be `MESSAGE` or `COMMENT`. 

 |
| 

`text`

 | 

The content of the message. 

 |
| 

`richText`

 | 

The content of the message in HTML format. This is optional. 

 |
| 

`recipients`

 | 

An object representing the recipients of the message. This is the most important for email, where you can specify multiple recipients. This object includes the following fields:

`actorID`: the ID associated with the message recipient.

`name`: the name of the recipient.

`recipientField`: for email messages, this is the type of recipient. Available values are `TO`, `CC`, or `BCC`.

`deliveryIdentifiers`: for email messages, this indicates the email addresses used for the visitor and agent.

 |
| 

`senderActorId`

 | 

This must be an agent actor ID that is associated to the HubSpot user in the account who is sending the message. 

 |
| 

`channelId`

 | 

The ID of a generic channel returned from the channels endpoint, like `1000` for live chat, `1001` for Facebook Messenger, `1002` for email, etc.

 |
| 

`channelAccountId`

 | 

The ID of an account that is part of the `channelId` channel. On an existing thread, it is recommended to copy the `channelId` and `channelAccountId` of the most recent message on the thread. 

 |
| 

`subject`

 | 

The subject line of the email. This is ignored when sending a message to a non-email channel. 

 |
| 

`attachments`

 | 

Any attachments to attach to the message, which can be specified as an object that contains a URL to a file hosted in your HubSpot account, or a list of quick replies if you're sending a message via Facebook Messenger or LiveChat. Learn more about how to include attachments [in the section below.](#include-attachments-in-messages)

 |

For example, your request body may look similar to the following: 

// POST request to conversations/v3/conversations/threads/{threadId}/messages { "type": "MESSAGE", "text": "Hey there, following up", "richText": "<p>Hey there, following up</p>", "recipients": \[ { "actorId": "E-user@hubspot.com", "name": "Leslie Knope", "recipientField": "TO", "deliveryIdentifiers": \[ { "type": "HS\_EMAIL\_ADDRESS", "value": "lknope@hubspot.com" } \] } \], "senderActorId": "A-3892666", "channelId": "1002", "channelAccountId": "42423411", "subject": "Follow up" }

If you make a successful request, the new message will be sent to the visitor. This can appear as a message in the chat widget, an email in the thread, a message in Facebook Messenger, etc. 

### Include attachments in messages

Attachments can be links to a file hosted in the HubSpot files tool, or a set of quick replies if you're sending a message using Facebook Messenger or LiveChat.

To include an attachment from a file in your HubSpot account, provide the absolute URL as the `fileId` in the `attachments` field of the request body. For example, the corresponding part of the request body is shown in lines `10-12` below:

// POST request to conversations/v3/conversations/threads/{threadId}/messages { "type": "MESSAGE", "text": "Hey there, following up", "recipients": { "actorID": "E-user@hubspot.com", "name": "Leslie Knope", "recipientField": "TO", "deliveryIdentifiers": \[{"type": "HS\_EMAIL\_ADDRESS", "value": "lknope@hubspot.com"}\]}, "senderActorId": "A-3892666", "channelId": "1002", "channelAccountId": "424232411", "subject": "Follow up", "attachments": { "fileId": "https://12345678.fs1.hubspotusercontent-na1.net/hubfs/12345678/doggo\_video.mp4" } }

If you connected Facebook Messenger or LiveChat as a channel, you can also specify a set of quick replies within the `attachments` field, which prompt the recipient with certain options that appear as tappable buttons below a message. Once tapped, the corresponding value of that option will be recorded.

Quick replies should be provided as a list of objects that each contain the following fields:

*   `label`: the visible text that appears to the recipient (e.g., _Red_)
*   `value`: the associated value of the button that you want to record  (e.g., `RED`)
*   `valueType`: the type of the quick reply option, which can be either `TEXT` or `URL`.

The example request body below demonstrates how to specify two quick reply options, _Yes_ and _No_, on lines `10-23`:

// POST request to conversations/v3/conversations/threads/{threadId}/messages { "type": "MESSAGE", "text": "Did that answer your question?", "recipients": { "actorID": "E-user@hubspot.com", "name": "Leslie Knope", "recipientField": "TO", "deliveryIdentifiers": \[{"type": "HS\_EMAIL\_ADDRESS", "value": "lknope@hubspot.com"}\]}, "senderActorId": "A-3892666", "channelId": "1002", "channelAccountId": "424232411", "subject": "Follow up", "attachments": \[ "type": "QUICK\_REPLIES", "quickReplies": \[ { "label": "Yes", "value": "Yes", "valueType": "URL" }, { "label": "No", "value": "No", "valueType": "TEXT" } \] \] }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/conversations/conversations#page-feedback)
--------------------------------------------------------------------------------------------------------

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