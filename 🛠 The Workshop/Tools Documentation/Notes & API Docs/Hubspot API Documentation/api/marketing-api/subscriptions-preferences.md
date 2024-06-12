---
title: "Subscription Preferences API Documentation"
description: "Overview of the subscription preferences API, including endpoints for managing contact email subscriptions and retrieving subscription statuses."
type: "documentation"
tags:
- "Email"
- "Subscriptions"
- "API"
relationships:
- "#related_to [[Contact Management]]"
- "#part_of [[HubSpot Marketing API]]"
- "#enables [[Managing Contact Email Preferences]]"
- "#used_by [[Marketers]]"
- "#contains [[Subscribe Contact Endpoint]]"
- "#contains [[Unsubscribe Contact Endpoint]]"
- "#contains [[Get Subscription Types Endpoint]]"
- "#part_of [[HubSpot API Documentation]]"
---

Subscription preferences
========================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Subscriptions types represent the legal basis to communicate with your contacts through email. Contacts can [manage their email preferences](https://knowledge.hubspot.com/articles/kcs_article/email/how-to-send-contacts-an-email-with-an-opt-out-link-so-they-can-manage-their-preferences) so that they're only opted into the emails they want to receive.

**Please note:** the subscription preferences API does not currently support retrieving or updating [WhatsApp](https://knowledge.hubspot.com/inbox/collect-consent-for-whatsapp-conversations) subscription information for a contact.

**Get contact subscription status**
-----------------------------------

The contact subscription status endpoint allows users to retrieve the subscription statuses for an email address in an account.

This endpoint is ideal for when you have an external preferences center or integration and need to know the subscription statuses for any given email address in your account.

* * *

**Subscribe contact**
---------------------

The subscribe contact endpoint allows you to subscribe an email address to any given subscription type in an account, but **will not allow you to resubscribe contacts who have opted out.** 

**Example use case:** This endpoint is ideal for when you have an integration or external form that needs to opt contacts into a subscription type. 

**Note**: The subscribe contact endpoint should only be used to honor requests from contacts who have given you permission to subscribe them. Please [review applicable laws and regulations](https://knowledge.hubspot.com/contacts/how-do-subscription-preferences-and-types-work) before subscribing a contact. 

* * *

**Unsubscribe contact**
-----------------------

The unsubscribe contact endpoint allows allows you to unsubscribe an email address in an account from any given subscription type. 

**Example use case:** This endpoint is ideal for when you have an integration or external form that needs to opt contacts out of a subscription type.

* * *

**Get subscription types**
--------------------------

The subscription info endpoint allows users to retrieve all subscription types in their account.

**Example use case:** This endpoint is ideal for when you have an external preferences center, integration, or form and need to know which subscription types exist in your account so you can update the subscription statuses for your contacts accordingly.

* * * 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/marketing-api/subscriptions-preferences#page-feedback)
--------------------------------------------------------------------------------------------------------------------

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