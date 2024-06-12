---
title: "Visitor Identification API Integration Guide"
description: "A guide on integrating the Visitor Identification API into your web application for identifying authenticated visitors in HubSpot's chat widget."
type: "work"
tags:
- "HubSpot"
- "API"
- "Integration"
- "Authentication"
relationships:
- "#part_of [[Marketing Hub]]"
- "#part_of [[Sales Hub]]"
- "#part_of [[Service Hub]]"
- "#part_of [[Content Hub]]"
- "#requires [[Private App Setup]]"
- "#related_to [[HubSpot Conversations API]]"
- "#related_to [[Documentation Feedback Form]]"
applicable_products: "-title: Marketing Hub"
    description: "Professional or Enterprise level marketing platform."
    type: "group"
    tags:
- "Marketing"
- "HubSpot Platform"
-title: "Sales Hub"
    description: "Professional or Enterprise level sales platform."
    type: "group"
    tags:
- "Sales"
- "HubSpot Platform"
-title: "Service Hub"
    description: "Professional or Enterprise level service management platform."
    type: "group"
    tags:
- "Service Management"
- "HubSpot Platform"
-title: "Content Hub"
    description: "Professional or Enterprise level content creation and publishing platform."
    type: "group"
    tags:
- "Content Creation"
- "HubSpot Platform"
integration_flow: "title: Integration Flow Example"
  description: "Steps to integrate the Visitor Identification API with your web application."
  type: "work"
  tags:
- "Integration Process"
- "API Usage"
  relationships:
- "#has_part [[Chat Widget SDK primer]]"
- "#uses [[Visitor Identification Token Generation]]"
- "#enables [[Personalized Messages]]"
- "#has_part [[Verify Integration Process]]"
- "#related_to [[Chat Widget SDK primer]]"
- "#requires [[HubSpot Conversations API]]"
- "#uses [[Token Refresh Mechanism]]"
- "#enables [[Accurate Visitor Identification]]"
- "#has_part [[Feedback Collection]]"
- "#requires [[JavaScript]]"
- "#uses [[Email Address for Clarifications]]"
---

Visitor identification
======================

[Overview](#tab-1)[Endpoint](#tab-2)

*   [Overview](#tab-1)
*   [Endpoint](#tab-2)

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Professional or Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

Use the Visitor Identification API to identify visitors to your site that were authenticated using your own external authentication system.

An identification token returned from this API can be used to pass information about your already-authenticated visitor to the chat widget, so that it treats the visitor as a known contact. Agents in the inbox can then have confidence about who they are talking to, and visitors can access previous thread history across devices. For example:

**Please note:**

*   The Visitor Identification API is for telling HubSpot who the visitor is. You should not rely on this to authenticate users in your platform.
*   Access to the Visitor Identification API requires a _Professional_ or _Enterprise_ level subscription. If the account does not have a qualifying subscription, you will receive a `403` error response from the API.

Example integration flow[](https://developers.hubspot.com/docs/api/conversation/visitor-identification#example-integration-flow)
--------------------------------------------------------------------------------------------------------------------------------

In order to integrate with this feature, you must have an existing web application with an authentication system. 

Before getting started, make sure you have a [private app](/docs/api/private-apps)set up and the account that you are trying to integrate has a qualifying _Professional_ or _Enterprise_ subscription.

Here’s an example of a possible integration flow:

![Possible User Identification Flow](https://developers.hubspot.com/hs-fs/hubfs/Possible%20User%20Identification%20Flow.png?width=932&name=Possible%20User%20Identification%20Flow.png)

Once your customer is logged in and verified in your system, take the following steps to identify them within live chat:

**1.** On your front end, set loadImmediately to false on the hsConversationsSettings object on the window. If you do not do this, the chat widget may load before the identification information is passed through. See the [Chat Widget SDK primer below](#chat-widget-sdk-primer) for more information.

*   Set the `hsConversationsSettings` properties outside the `isConversationsAPIReady` function.
*   In addition, the `hsConversationsSettings` needs to be set prior to the call, otherwise you may experience a race condition that interferes with widget load.

window.hsConversationsSettings = { loadImmediately: false };

**2.** Generate a token from the Visitor Identification API by passing in the email address of your authenticated visitor. This should be done on the back end of your web application. See the _Endpoints_ tab for an example request.

curl --request POST \\ --url 'https://api.hubspot.com/conversations/v3/visitor-identification/tokens/create \\ --data '{ "email": "gob@bluth.com", "firstName": "Gob", "lastName": "Bluth" }'

The provided first and last name will be set on the contact record in HubSpot after the chat begins if:  

*   it's a new contact created by the Visitor Identification API.
*   it's an existing contact where the name is not already known.

This can be useful when personalizing messages to identified visitors when your external system already has name information, but it does not yet exist in HubSpot. These are optional parameters and not required. 

**3.** Using the token Step 2, set the following properties on the `hsConversationsSettings` object on the window.

window.hsConversationsSettings = { identificationEmail: "visitor-email@example.com", identificationToken: "<TOKEN FROM STEP 1>" };

4. Load the widget.

window.HubSpotConversations.widget.load();

The token and email must be set on the `hsConversationsSettings` object on the window every time the page loads for an authenticated visitor. This context will not be carried across page loads automatically if these parameters are no longer set. Tokens are temporary and will expire after 12 hours. Tokens can be cached to avoid re-fetching the token on every page load, as long as they are refreshed at least every 12 hours. 

Verify the integration[](https://developers.hubspot.com/docs/api/conversation/visitor-identification#verify-the-integration)
----------------------------------------------------------------------------------------------------------------------------

Once you've completed your integration of the Visitor Identification feature, you can verify that it’s working as expected. This can be done in a couple ways, depending on your implementation, so you may need to tailor the examples below to your specific requirements.

*   If you've added the chat widget to one or more public pages as well as behind an authentication system:
    *   Navigate to a page where the chat widget should not be identifying visitors and start a conversation.
    *   In HubSpot, open the inbox and verify that the chat that just came in belongs to an _Unknown Visitor_. If this is not the case, try following these steps in a private browsing window:  
        *   Navigate to a page where the chat widget should be identifying visitors via the Visitor Identification API and start a conversation.
        *   In HubSpot, open the inbox and verify that the chat is correctly attributed to the contact that you’re logged in as. You should see a badge next to the contact’s name, indicating that this contact was successfully identified through this API.  
              
            ![visitor_identity_badge](https://developers.hubspot.com/hs-fs/hubfs/visitor_identity_badge.png?width=437&name=visitor_identity_badge.png)

*   If you've only added the chat widget to pages behind an authentication system, and you have access to multiple test user accounts:
    *   Log in to HubSpot as the first test user, then navigate to a page where the chat widget loads, and start a conversation.
    *   Log out of HubSpot, then log back in as the second test user. Navigate to a page where the chat widget loads, and start a conversation.
    *   In HubSpot, open the inbox and verify that the chats that came in were from the first and second test accounts, respectively, and that you see the badge next to the contact names for both records.

**Please note:** for visitors identified with this API, HubSpot will not drop the `messagesUtk` cookie. HubSpot will also skip any email capture questions since email address is already known. Because the `messagesUtk` cookie and email capture do not apply to these chats, the associated settings in the chatflow will not show for visitors identified through the Visitor Identification API.

Chat widget SDK primer[](https://developers.hubspot.com/docs/api/conversation/visitor-identification#chat-widget-sdk-primer)
----------------------------------------------------------------------------------------------------------------------------

The API is housed in the `window.HubSpotConversations` object. All available methods can be accessed via this object. The HubSpot script loader on your page will create this object for you, but it may not be available immediately. To defer accessing the API until it's initialized, you may use the `window.hsConversationsOnReady` helper. For example:

<script type="text/javascript"> function onConversationsAPIReady() { console.log(\`HubSpot Conversations API: ${window.HubSpotConversations}\`); } /\* configure window.hsConversationsSettings if needed. \*/ window.hsConversationsSettings = {}; /\* If external API methods are already available, use them. \*/ if (window.HubSpotConversations) { onConversationsAPIReady(); } else { /\* Otherwise, callbacks can be added to the hsConversationsOnReady on the window object. These callbacks will be called once the external API has been initialized. \*/ window.hsConversationsOnReady = \[onConversationsAPIReady\]; } </script>

### SDK reference[](https://developers.hubspot.com/docs/api/conversation/visitor-identification#sdk-reference)

`window.hsConversationsOnReady` array

This is an optional field you can define on the window object that enables you to specify code to be executed as soon as the widget becomes available. Once the API has been initialized, it will check for the existence of this array and execute its functions in series.

if (window.HubSpotConversations) { console.log('The api is ready already'); } else { window.hsConversationsOnReady = \[ () => { console.log('Now the api is ready'); }, \]; }

`hsConversationsSettings` object

This object enables you to provide some configuration options to the widget before it initializes. In order to use the Visitor Identification feature, you must set the following fields:

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`loadImmediately`

 | boolean | 

Whether the widget should implicitly load or wait until the `widget.load` method is called

 | `true` |
| 

`identificationToken`

 | string | 

Used to integrate with the Visitor Identification API. This is the token provided by the token generation endpoint on the Visitor Identification API that is used as proof that this visitor has been identified.

 | `""` |
| 

`identificationEmail`

 | string | 

The email address of the visitor that you’ve identified as loading the widget.

 | `""` |

window.hsConversationsSettings = { loadImmediately: false, identificationEmail: "visitor-email@example.com", identificationToken: "<TOKEN FROM STEP 1>" };

Learn more about the [conversations SDK](/docs/api/conversation/chat-widget-sdk).

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/conversation/visitor-identification#page-feedback)
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