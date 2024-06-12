---
title: "Running code snippets in bots"
description: When creating or editing a bot, you can add a code snippet by clicking the "+" to add an action. From the action selection panel, click on "Run a code snippet."
type: "work"
tags:
- "Bot"
- "Code Snippet"
- "Node.js"
relationships:
- "#part_of [[Conversation]]"
- "#used_by [[Developer]]"
- "#related_to [[HubSpot Conversations API]]"
- "#requires [[Node.js 10.x]]"
- "#implements [[Code Snippet Action]]"
- "#produces [[Bot Response]]"
---

Running code snippets in bots
=============================

When [creating or editing a bot](https://knowledge.hubspot.com/articles/kcs_article/conversations/create-a-bot), you can add a code snippet by clicking the "+" to [add an action](https://knowledge.hubspot.com/articles/kcs_article/conversations/a-guide-to-bot-actions) as you normally would. From the action selection panel, click on "Run a code snippet."![run-a-code-snippet-2](https://developers.hubspot.com/hs-fs/hubfs/KB%20Team/run-a-code-snippet-2.png?width=322&name=run-a-code-snippet-2.png)

Next, give your action a nickname. Within the code editing pane, you'll see our default template for Node.js 10.x. The details of the "event" object and possible response object formats are detailed below.![run-a-code-snippet-editor](https://developers.hubspot.com/hs-fs/hubfs/KB%20Team/run-a-code-snippet-editor.png?width=388&name=run-a-code-snippet-editor.png)

The code will be triggered when the saved action is reached in a conversation.  

There are three main things to keep in mind when working with code snippets:

*   The `exports.main()` function is called when the code snippet action is executed.
*   The `event` argument is an object containing details for the visitor and chat session.
*   The `callback()` function is used to pass data back to the bot and user. It should be called in the `exports.main` function.

The `event` object will contain the following data:

//example payload { "userMessage": { // Details for the last message sent to your bot "message": "100-500", // The last message received by your bot, sent by the visitor "quickReply": { // If the visitor selected any quick reply options, this will be a list of the selected options. // Will be 'null' if no options were selected. "quickReplies":\[ // A list of quick reply options selected by the visitor { "value":"100-500", "label":"100-500" } \], }, "session": { "vid": 12345, // The contact VID of the visitor, if known. "properties": { // A list of properties collected by the bot in the current session. "CONTACT": { "firstname": { "value": "John", "syncedAt": 1534362540592 }, "email": { "value": "testing@domain.com", "syncedAt": 1534362541764 }, "lastname": { "value": "Smith", "syncedAt": 1534362540592 } } }, "customState":{myCustomCounter: 1, myCustomString:"someString"} // Only present if it customState was passed in from a previous callback payload } }

The `callback()` function is used to send data back to the bot. The argument should be an object with the following data:

//sample payload { "botMessage": "Thanks for checking out our website!", // This is the message your bot will display to the visitor. "quickReplies": \[{ value:'option', // Passed to the bot as the response on click label:'Option' // Gets displayed as the button label }\], // the quickReplies object is optional "nextModuleNickname": "SuggestAwesomeProduct", // The nickname of the next module the bot should execute. If undefined, the bot will follow the default configured behavior "responseExpected": false // If true, the bot will display the returned botMessage, wait for a response, then execute this code snippet again with that new response. "customState":{myCustomCounter: 1, myCustomString:"someString"} // Optional field to pass along to the next step. }

Limitations[](https://developers.hubspot.com/docs/api/conversations/code-snippets-in-bots#limitations)
------------------------------------------------------------------------------------------------------

Code snippets in bots must finish running within 20 seconds and only use 128 MB of memory. Exceeding either of these limits will result in an error.

Available libraries
-------------------

Several popular Node.js libraries are available for use within the code snippet.

*   [async](https://www.npmjs.com/package/async)
*   [lodash](https://www.npmjs.com/package/lodash)
*   [mongoose](https://www.npmjs.com/package/mongoose)
*   [mysql](https://www.npmjs.com/package/mysql)
*   [redis](https://www.npmjs.com/package/redis)
*   [request](https://www.npmjs.com/package/request)
*   [aws-sdk](https://www.npmjs.com/package/aws-sdk)

The libraries can be loaded using the normal `require()` function at the top of your code.

const request = require('request'); exports.main = (event, callback) => { request('http://time.jsontest.com/', function (error, response, body) { const responseJson = { "botMessage": "The current time in GMT is " + JSON.parse(body).time, "responseExpected": false } callback(responseJson); }); };

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/conversations/code-snippets-in-bots#page-feedback)
----------------------------------------------------------------------------------------------------------------

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