---
title: "Idea Tracker Tutorial Part 3"
description: "This is Part 3 of a three-part tutorial for creating and integrating an app with a HubSpot account, focusing on building a custom UI within the HubSpot CRM."
type: "tutorial"
tags:
- "HubSpot"
- "CRM"
- "Custom_UI"
relationships:
- "#part_of [[Idea Tracker Tutorial]]"
- "#requires [[Authentication and Initial Sync (Part 1)]]"
- "#follows [[Creating a Two-Way Sync and Customizing CRM Experience (Part 2)]]"
founded: "N/A"
---

Idea Tracker Tutorial Part 3
============================

Introduction
------------

This is Part 3 of a three-part tutorial for creating and integrating an app with a HubSpot account. Part 1 focused on authentication and the initial sync. Part 2 was about creating a two-way sync and customizing parts of the CRM experience. Part 3 will focus on building a custom UI within the HubSpot CRM. 

### Making tradeoffs

Since this application uses a microservices architecture, you have to decide which services will handle the different functions of your applications. If you’ve completed Parts 1 and 2, you’ve put any function rendering the UI or communicating with the database in `web_service`, while any function calling HubSpot is in `hubspot_service`. This makes the app easier to maintain in the long run, but it also complicates the initial development.

As you build out your app to accommodate new use cases, new factors will influence the tradeoffs you make. For example, if you expanded the app to send emails through HubSpot’s transactional email offering, you might set up a separate service for it instead of expanding the existing `hubspot_service`. 

Further extending the CRM
-------------------------

In Part 2, you added custom events to a contact record’s timeline. Now you can extend the CRM even further by using CRM cards to add interactive elements. When a contact posts something in the idea forum, a card will be added to their contact record displaying this information. Just like with timeline events, you’ll need to make changes to both your developer account settings and your code when creating CRM cards.

### Developer account settings

1.  In your developer account, navigate to your app and go to “CRM cards” in the left-hand nav. 
2.  Click “Create CRM card” and enter a name for your card. 
3.  In the Data request tab, set the data fetch URL to `yourdomain.com/webhooks/platform`, with `yourdomain.com` representing the domain hosting your app. 
4.  In the same tab, go to “Target record types” and find the row that says “Contacts.” Turn the toggle in the “Appear on this type?” column on.
5.  Go to the Card properties tab and add the `title` and `date` properties. They should be a `string` and a `datetime` property, respectively. 

  
  

------ 

### Code

The code changes here are simple, requiring only a single function. Where you put that function is less straightforward. This part of the tutorial highlights the tradeoffs you make when developing. In this case, you should put the function in `./web_service/src/server.js`. Since the HubSpot UI is relying on data from the webhook, this will allow you to respond quickly. This breaks the earlier pattern where all HubSpot logic was in \`hubspot\_service\`, but you’ll deliver a better user experience.

// ./web\_service/src/server.js app.get("/webhook/platform", async (req, res, next) => { const { associatedObjectId } = req.query; try { const author = await Users.findOne({ hubspotContactId: associatedObjectId, }); const ideas = await Ideas.find({ author }); const cards = ideas.map((idea, i) => { const card = {}; card.id = i; card.title = idea.title; card.linkUrl = null; card.tokens = \[ { label: "Idea Title", dataType: "STRING", value: idea.title, name: "title", }, { label: "Created Date", dataType: "DATETIME", value: idea.date, name: "date", }, \]; card.actions = \[ { type: "IFRAME", width: 890, height: 748, url: \`${process.env.BASE\_URL}/idea/${idea.\_id}\`, label: "View Full Idea", }, \]; console.log(card); return card; }); const cardListing = { totalCount: cards.length, sections: cards, responseVersion: "v3", topLevelActions: { primary: { type: "IFRAME", width: 890, height: 748, url: \`${process.env.BASE\_URL}\`, label: "View Full Idea", }, }, }; res.send(cardListing); } catch (err) { next(err); } });

Conclusion
----------

That part of the tutorial was all about making tradeoffs when adding a new feature. Your users now have a way to access your app’s data inside the context of the CRM. This unlocks new power for them, but also makes things more complicated for you. 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/idea-tracker-tutorial-part-3#page-feedback)
---------------------------------------------------------------------------------------------------------

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