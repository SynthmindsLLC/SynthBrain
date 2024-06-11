---
title: "Working with webhooks from bots"
description: "A guide on creating and editing a bot, adding actions including triggering a webhook, inputting the endpoint URL for the webhook, and understanding request and response payloads."
type: "work"
tags:
- "Bot"
- "Webhooks"
- "HubSpot"
relationships:
- "#part_of [[Conversation]]"
- "#used_by [[Developers]]"
created_date: "YYYY-MM-DD // Replace with actual creation date if known"
---

Working with webhooks from bots
===============================

When [creating or editing a bot](https://knowledge.hubspot.com/articles/kcs_article/conversations/create-a-bot), you can add a webhook by clicking the "+" to [add an action](https://knowledge.hubspot.com/articles/kcs_article/conversations/a-guide-to-bot-actions) as you normally would. From the action selection panel, click on "Trigger a webhook."![trigger-a-webhook](https://developers.hubspot.com/hs-fs/hubfs/KB%20Team/trigger-a-webhook.png?width=334&name=trigger-a-webhook.png)

Next, give your action a nickname and input the endpoint URL for the webhook. If your webhook will be sending data to HubSpot in response to the request, check the "Wait for webhook feedback" box. (Read more on this below.) Save your action. ![trigger-a-webhook-editor](https://2832391.fs1.hubspotusercontent-na1.net/hub/2832391/hubfs/Settings/Website/Blog/trigger-a-webhook-editor.png?width=469&name=trigger-a-webhook-editor.png)When this action has been reached in a conversation, HubSpot will send a JSON payload to the **Webhook URL** you’ve defined. The payload will contain information relevant to the chat session, including the visitors' responses to any questions asked, their contact ID, and information about the bot.

##### Example request payload:

//sample payload { "userMessage": { // Details for the last message sent to your bot "message": "100-500", // The last message received by your bot, sent by the visitor "quickReply": { // If the visitor selected any quick reply options, this will be a list of the selected options. // Will be 'null' if no options were selected. "quickReplies":\[ // A list of quick reply options selected by the visitor { "value":"100-500", "label":"100-500" } \], }, "session": { "vid": 12345, // The contact VID of the visitor, if known. "properties": { // A list of properties collected by the bot in the current session. "CONTACT": { "firstname": { "value": "John", "syncedAt": 1534362540592 }, "email": { "value": "testing@domain.com", "syncedAt": 1534362541764 }, "lastname": { "value": "Smith", "syncedAt": 1534362540592 } } } } }

Advanced users also have the option of including JSON in your webhook's response. By doing this, you can impact the flow of conversation or send a custom message.

##### Example response payload:

//sample payload { "botMessage": null, // This is the message your bot will display to the visitor. "nextModuleNickname": "PromptForCollectUserInput", // If defined, this will be the next module your bot will go to. If undefined, the default configured behavior will be observed. "responseExpected": false // If true, the webhook will be triggered again with the visitor's next reply. If false, the default configured behavior will be observed. }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/conversations/webhooks-in-bots#page-feedback)
-----------------------------------------------------------------------------------------------------------

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