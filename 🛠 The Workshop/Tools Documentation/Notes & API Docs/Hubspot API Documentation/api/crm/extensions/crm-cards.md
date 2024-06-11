---
title: "CRM cards"
description: "Within a public app, you can create custom CRM cards to display information from other systems on HubSpot contact, company, deal, and ticket records. Each app can include up to 25 CRM cards."
type: "work"
tags:
- "CRM"
- "HubSpot"
- "Integration"
relationships:
- "#part_of [[Public App]]"
- "#used_for [[Displaying Information on CRM Records]]"
- "#related_to [[UI Extensions]]"
---

CRM cards
=========

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Within a [public app](/docs/api/creating-an-app), you can create custom CRM cards to display information from other systems on HubSpot contact, company, deal, and ticket records. Each app can include up to 25 CRM cards.

**Please note:** the CRM cards referenced in this article are different from the custom cards you can [create as UI extensions with projects](/docs/platform/create-ui-extensions). The CRM cards included in this article are intended for use with public apps, while UI extensions offer more flexibility, customizability, and interactivity using a more modern toolset.

If you're not building a public app, check out the check out the [CRM development tools overview](https://developers.hubspot.com/docs/platform/crm-development-tools-overview) to see if React-based UI extensions will work better for your use case.

**Example use case:** you're building an integration for the App Marketplace for your bug tracking software. You want to be able to surface tracked bugs on contact records so that support reps can reference them when working with customers. Your app can define a custom card that displays this info right on the HubSpot contact record.  
![CRM_Card_1](https://developers.hubspot.com/hs-fs/hubfs/CRM_Card_1.png?width=467&name=CRM_Card_1.png)Cards can be defined as part of your app’s feature settings. Once the app is installed and a user views the target CRM records, HubSpot makes an outbound request to the app, retrieves the relevant data, and displays it in a card on the record page. Apps can also specify custom actions the user can take based on this information. For example, your app could include an action to open a modal for displaying the app's own UI in HubSpot.  

![CRM_card_diagram](https://developers.hubspot.com/hs-fs/hubfs/CRM_card_diagram.png?width=1326&name=CRM_card_diagram.png)

Scope requirements[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#scope-requirements)
---------------------------------------------------------------------------------------------------------

To create custom CRM cards, your app has to request the OAuth scopes needed to modify the CRM records where your card will appear. For example, for a CRM card to appear on contact records, the app must have the `crm.objects.contacts.read` and `crm.objects.contacts.write` scopes. If you later need to remove CRM object scopes from your app, you'll first need to delete all existing cards for those object types.

See the OAuth documentation for [more details about scopes](https://developers.hubspot.com/docs-beta/working-with-oauth) and setting up the authorization URL for your app.

Create a CRM card[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#create-a-crm-card)
-------------------------------------------------------------------------------------------------------

You can create CRM cards for your app either through the API or by editing your app in your developer account. To learn more about configuring a card through the API, check out the Endpoints tab at the top of the article.

To create a CRM card using HubSpot's UI:

*   In your HubSpot developer account, navigate to **Apps** in the main navigation.
*   Select the **app** where you want to add a card.
*   In the left sidebar menu, select **CRM cards**.
*   In the upper right, click **Create CRM card**.  
    ![private-app-create-crm-card](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-create-crm-card.png?width=1209&height=521&name=private-app-create-crm-card.png)

Below, learn more about the configuration options in each tab.

UI extensions built using developer projects offer more flexible ways to display data and allow user interaction, including displaying external content in frames. If using a private app is feasible for your integration, check out the [UI extensions quickstart guide](/docs/platform/ui-extensions-quickstart) to get started, or [view HubSpot's example projects](/docs/platform/sample-projects) to see examples of what's possible.

Data request[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#data-request)
---------------------------------------------------------------------------------------------

When a user HubSpot views a CRM record that the CRM card is on, HubSpot will make a data fetch request to the integration. This request is made to the specified target URL, which includes a set of default query parameters, along with extra parameters containing property data as specified in the card's settings. 

![private-app-create-crm-card-data-request-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-create-crm-card-data-request-tab.png?width=973&height=737&name=private-app-create-crm-card-data-request-tab.png)

*   In the _Data fetch URL_ field, enter the **URL** that you'll be fetching data from. In the API, this URL is added to the `targetUrl` field. 
    
*   In the _Target record types_ section, click to toggle the **switches** on to select which CRM records the card will appear on. Then, Use the **Properties sent from HubSpot** dropdown menus to select the **HubSpot properties** that will be included as query parameters in the request URL. In the API, each record type and its corresponding properties are added as objects in the `objectTypes` array.

// Example data fetch configuration { "title": "New CRM Card", "fetch": { "targetUrl": "https://www.example.com/demo-fetch", "objectTypes": \[ { "name": "contacts", "propertiesToSend": \[ "firstname", "email", "lastname" \] } \] } ... }

### Example request[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#example-request)

The above configuration would result in HubSpot sending its `GET` request as follows.

https://www.example.com/demo-fetch?userId=12345&userEmail=loggedinuser@hubspot.com&associatedObjectId=53701&associatedObjectType=CONTACT&portalId=987654&firstname=Tim&email=timrobinson@itysl.com&lastname=Robinson

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`userId`

 | Default | 

The ID of the HubSpot user that loaded the CRM record.

 |
| 

`userEmail`

 | Default | 

The email address of the user that loaded the CRM record.

 |
| 

`associatedObjectId`

 | Default | 

The ID of the CRM record that loaded.

 |
| 

`associatedObjectType`

 | Default | 

The type of CRM record that loaded (e.g., contact, company, deal).

 |
| 

`portalId`

 | Default | 

The ID of the HubSpot account where the CRM record loaded.

 |
| 

`firstname`

 | Custom | 

The contact's first name, as specified in the _Properties sent from HubSpot_ dropdown menu (in-app) and `propertiesToSend` array (API).

 |
| 

`email`

 | Custom | 

The contact's email address, as specified in the _Properties sent from HubSpot_ dropdown menu (in-app) and `propertiesToSend` array (API).

 |
| 

`lastname`

 | Custom | 

The contact's last name, as specified in the _Properties sent from HubSpot_ dropdown menu (in-app) and `propertiesToSend` array (API).

 |

**Please note:** requests will timeout after five seconds. Within that, a connection must be made within three seconds. 

### Example response[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#example-response)

Below is an example response that the integrator might provide to the above request.

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%; height: 510.688px;"><tbody><tr><td style="padding: 10px 4px;"><code>results</code> &nbsp;<strong>array</strong><p>An array of up to five valid <a href="#card-properties" rel="noopener">card properties</a>. If more card properties are available for a specific CRM object, your app can link to them.</p></td></tr><tr><td style="padding: 10px 4px;"><code>objectId</code> &nbsp;<strong>number</strong> (required)<p>A unique ID for this object.</p></td></tr><tr><td style="padding: 10px 4px;"><code>title</code> &nbsp;<strong>string&nbsp;</strong><span style="font-weight: normal;">(required)</span><p>The title of this object.</p></td></tr><tr><td style="padding: 10px 4px;"><code>link</code> &nbsp;<strong>string</strong><p>The URL that the user can follow to get more details about the object. This property is optional, but if no objects have a link, you should provide a value of <code>null</code>.</p></td></tr><tr><td style="padding: 10px 4px;"><code>created</code> &nbsp;<strong>string&nbsp;</strong><span style="font-weight: normal;">(required)</span><p>A <a href="#card-properties" rel="noopener">custom property</a> as defined in the card's settings that denotes the date of the object's creation.</p></td></tr><tr><td style="padding: 10px 4px;"><code>priority</code> &nbsp;<strong>string&nbsp;</strong><span style="font-weight: normal;">(required)</span><p>A <a href="#card-properties" rel="noopener">custom property</a> as defined in the card's settings that denotes external ticket's priority level.</p></td></tr><tr><td style="padding: 10px 4px;"><code>actions</code> &nbsp;<strong>array</strong><p>A list of available <a href="#action-types" rel="noopener">actions</a> a user can take.</p></td></tr><tr><td style="padding: 10px 4px;"><code>properties</code> &nbsp;<strong>string</strong><p>A list of custom properties that aren't defined in the card settings. You can use this list to display a specific object's unique properties. These properties will be shown in the order they're provided, but after the properties defined in the card settings.</p></td></tr><tr><td style="padding: 10px 4px;"><code>settingsAction</code> &nbsp;<strong>object</strong><p>An iframe action that enables users to update the app's settings.&nbsp;</p></td></tr><tr><td style="padding: 10px 4px;"><code>primaryAction</code> &nbsp;<strong>object&nbsp;</strong><p>The primary action for a record type, typically a creation action.</p></td></tr><tr><td style="padding: 10px 4px;"><code>secondaryActions</code> &nbsp;<strong>array</strong><p>A list of actions displayed on the card.</p></td></tr></tbody></table>

// Example response { "results": \[ { "objectId": 245, "title": "API-22: APIs working too fast", "link": "http://example.com/1", "created": "2016-09-15", "priority": "HIGH", "project": "API", "description": "Customer reported that the APIs are just running too fast. This is causing a problem in that they're so happy.", "reporter\_type": "Account Manager", "status": "In Progress", "ticket\_type": "Bug", "updated": "2016-09-28", "actions": \[ { "type": "IFRAME", "width": 890, "height": 748, "uri": "https://example.com/edit-iframe-contents", "label": "Edit", "associatedObjectProperties": \[\] }, { "type": "IFRAME", "width": 890, "height": 748, "uri": "https://example.com/reassign-iframe-contents", "label": "Reassign", "associatedObjectProperties": \[\] }, { "type": "ACTION\_HOOK", "httpMethod": "PUT", "associatedObjectProperties": \[\], "uri": "https://example.com/tickets/245/resolve", "label": "Resolve" }, { "type": "CONFIRMATION\_ACTION\_HOOK", "confirmationMessage": "Are you sure you want to delete this ticket?", "confirmButtonText": "Yes", "cancelButtonText": "No", "httpMethod": "DELETE", "associatedObjectProperties": \[ "protected\_account" \], "uri": "https://example.com/tickets/245", "label": "Delete" } \] }, { "objectId": 988, "title": "API-54: Question about bulk APIs", "link": "http://example.com/2", "created": "2016-08-04", "priority": "HIGH", "project": "API", "reported\_by": "ksmith@hubspot.com", "description": "Customer is not able to find documentation about our bulk Contacts APIs.", "reporter\_type": "Support Rep", "status": "Resolved", "ticket\_type": "Bug", "updated": "2016-09-23", "properties": \[ { "label": "Resolved by", "dataType": "EMAIL", "value": "ijones@hubspot.com" }, { "label": "Resolution type", "dataType": "STRING", "value": "Referred to documentation" }, { "label": "Resolution impact", "dataType": "CURRENCY", "value": "94.34", "currencyCode": "GBP" } \], "actions": \[ { "type": "IFRAME", "width": 890, "height": 748, "uri": "https://example.com/edit-iframe-contents", "label": "Edit" }, { "type": "CONFIRMATION\_ACTION\_HOOK", "confirmationMessage": "Are you sure you want to delete this ticket?", "confirmButtonText": "Yes", "cancelButtonText": "No", "httpMethod": "DELETE", "associatedObjectProperties": \[ "protected\_account" \], "uri": "https://example.com/tickets/245", "label": "Delete" } \] } \], "settingsAction": { "type": "IFRAME", "width": 890, "height": 748, "uri": "https://example.com/settings-iframe-contents", "label": "Settings" }, "primaryAction": { "type": "IFRAME", "width": 890, "height": 748, "uri": "https://example.com/create-iframe-contents", "label": "Create Ticket" } }

### Request signatures[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#request-signatures)

To ensure that the requests are actually coming from HubSpot, the following request header is included. This header will contain a hash of the of the app secret for your application and the details of the request. 

`X-HubSpot-Signature: <some base64 string>`

To verify this signature, perform the following steps:

1.  Create a string that concatenates together the following: `<app secret>` + `<HTTP method>` \+ `<URL>` + `<request body> (if present)`.
2.  Create a SHA-256 hash of the resulting string.
3.  Compare the hash value to the signature. If they're equal, the request passed validation. If the values do not match, the request may have been tampered with in transit or someone may be spoofing requests to your endpoint.

Learn more about [validating requests from HubSpot](/docs/api/webhooks/validating-requests).

Card properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#card-properties)
---------------------------------------------------------------------------------------------------

On the _Card Properties_ tab, define any custom properties that you want HubSpot to display on the CRM card. Once defined, the integration can fill these properties by including them in its response.

*   *   Click **Add property** to add a new property for the card to display. The payload you provide in response to the data fetch call should contain values for all of these properties.
    *   In the right panel, set the property's unique name, display label, and data type. You can select from the following types: _Currency_, _Date_, _Datetime_, _Email_, _Link_, _Numeric_, _Status_, and _String**.**_ Learn more about [using extension property types](https://legacydocs.hubspot.com/docs/methods/crm-extensions/property-types).
    *   Click **Add** to save the property.  
        ![private-app-create-crm-card-card-properties-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-create-crm-card-card-properties-tab.png?width=968&height=351&name=private-app-create-crm-card-card-properties-tab.png)

When HubSpot sends its data request, the integration can provide values for these properties in its response alongside other values in each object in `results`. In addition to the properties configured on this tab, the integration can also include its own custom properties without needing them to be defined in the card's settings.

For example, in the response below, `created` and `priority` are both defined in the _Card properties_ tab, while the `properties` array sends its own property definitions and values. These object-specific properties must be defined per object.

// Example object within a response { "objectId": 988, "title": "API-54: Question about bulk APIs", "link": "http://example.com/2", "created": "2016-08-04", "priority": "HIGH", "properties": \[ { "label": "Resolved by", "dataType": "EMAIL", "value": "ijones@hubspot.com" }, { "label": "Resolution type", "dataType": "STRING", "value": "Referred to documentation" }, { "label": "Resolution impact", "dataType": "CURRENCY", "value": "94.34", "currencyCode": "GBP" } \], "actions": \[ ... \] }

When sending custom properties, the `dataType` field for each property can be set to one of: `CURRENCY`, `DATE`, `DATETIME`, `EMAIL`, `LINK`, `NUMERIC`, `STATUS`, `STRING`. Depending on the property type, the integration may need to provide additional fields. Below, learn more about each property type.

### Currency properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#currency-properties)

`CURRENCY` properties must include a `currencyCode`, which needs to be a valid [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) code. This will ensure the user sees the correct currency symbol and number formatting.

// Example custom currency property { "results": \[ { "properties": \[ { "label": "Resolution impact", "dataType": "CURRENCY", "value": "94.34", "currencyCode": "GBP" } \] } \] }

### Date properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#date-properties)

`DATE` properties should be in the format `yyyy-mm-dd`. These properties will be displayed in a format appropriate to the user's locale. If you need to include a timestamp, you should instead use a `DATETIME` property.

// Example custom date property { "results": \[ { "properties": \[ { "label": "Date", "dataType": "DATE", "value": "2023-10-13" } \] } \] }

### Datetime properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#datetime-properties)

`DATETIME` properties indicate a specific time and must be provided as milliseconds since epoch. These properties will be displayed in a format appropriate to the user's locale.

// Example custom datetime property { "results": \[ { "properties": \[ { "label": "Timestamp", "dataType": "DATETIME", "value": "1697233678777" } \] } \] }

### Email properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#email-properties)

`EMAIL` properties are for values that contain an email address. These properties will be displayed as mailto links.

// Example custom email property { "results": \[ { "properties": \[ { "label": "Email address", "dataType": "EMAIL", "value": "hobbes.baron@gmail.com" } \] } \] }

### Link properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#link-properties)

`LINK` properties display hyperlinks and open in a new window. You can specify a `linkLabel`, otherwise the URL itself will be displayed. 

// Example custom link property { "results": \[ { "properties": \[ { "label": "Link property", "dataType": "LINK", "value": "https://www.hubspot.com", "linkLabel": "Test link" } \] } \] }

### Numeric properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#numeric-properties)

`NUMERIC` properties display numbers. 

// Example custom datetime property { "results": \[ { "properties": \[ { "label": "Number", "dataType": "NUMERIC", "value": "123.45" } \] } \] }

### Status properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#status-properties)

`STATUS` properties display as colored indicators. To define a status property, the integration must provide an `optionType` that describes the possible statuses. Statuses include:

*   `DEFAULT`: Grey
*   `SUCCESS`: Green
*   `WARNING`: Yellow
*   `DANGER`: Red
*   `INFO`: Blue

// Example custom datetime property { "results": \[ { "properties": \[ { "label": "Status", "dataType": "STATUS", "value": "Errors occurring", "optionType": "DANGER" } \] } \] }

### String properties[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#string-properties)

`STRING` properties display text.

// Example custom datetime property { "results": \[ { "properties": \[ { "label": "First name", "dataType": "STRING", "value": "Tim Robinson" } \] } \] }

Custom actions[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#custom-actions)
-------------------------------------------------------------------------------------------------

On the _Custom actions_ tab, you can define the base URLs that will be requested when a user clicks an action button.. You can include multiple action URLs for various actions in your CRM card. Card actions must call an endpoint specified on this tab.  
![private-app-create-crm-card-custom-actions-tab](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/private-app-create-crm-card-custom-actions-tab.png?width=649&height=295&name=private-app-create-crm-card-custom-actions-tab.png)Action hooks and confirmation hook requests will include a `X-HubSpot-Signature` header for verifying the request. Iframe action requests will not include a request signature. See [request signatures](#request-signatures) for more information.  

Action URLs are accessed in the `uri` field in an action. Similar to the [data fetch request,](#data-request) action hooks will include a default set of query parameters. You can include other query parameters by including an `associatedObjectProperties` field in the action.

The response will vary depending on type of action. Below, learn more about action types.

### Action types[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#action-types)

#### Iframe actions[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#iframe-actions)

`IFRAME` actions will open a modal containing an iframe pointing at the provided URL. No request signature is sent when the iframe is opened from the CRM UI. This is because the iframe URL is returned in the original data fetch request, and no additional proxy requests are needed.

// Example iframe action { "type": "IFRAME", "width": 890, "height": 748, "uri": "https://example.com/iframe-contents", "label": "Edit", "associatedObjectProperties": \[ "some\_crm\_property" \] }

When the user is done completing an action inside the iframe, the modal should close and return the user to the CRM record they started from. To close the modal, the integration can use `window.postMessage` to signal to the CRM that the user is done. The following messages are accepted:

*   `{"action": "DONE"}`: the user has successfully competed the action.
*   `{"action": "CANCEL"}`: the user has canceled the action.

// Example iframe close message window.parent.postMessage(JSON.stringify({"action": "DONE"}), "\*");

#### Action hook actions[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#action-hook-actions)

`ACTION_HOOK` actions send a server-side request to the integrator. The only UI a users sees for this action is a success or error message. This type of action is useful for simple operations that require no further input from the user. An `X-HubSpot-Signature` header will be included in the request for verification. Learn more about [request signatures](#request-signatures).

// Example action hook action { "type": "ACTION\_HOOK", "httpMethod": "POST", "uri": "https://example.com/action-hook", "label": "Example action", "associatedObjectProperties": \[ "some\_crm\_property" \] }

The `httpMethod` can be set to  `GET`, `POST`, `PUT`, `DELETE`, or `PATCH`.  If using `GET` or `DELETE`, the `associatedObjectProperties` values will be appended to the request URL as query parameters. Otherwise, the properties will be sent in the request body.

// Example iframe close message window.parent.postMessage(JSON.stringify({"action": "DONE"}), "\*");

#### Confirmation actions[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#confirmation-actions)

`CONFIRMATION_ACTION_HOOK` actions behave the same as `ACTION_HOOK` actions, except that a confirmation dialog is shown to the user before running the server-side request. An `X-HubSpot-Signature` header will be included in the request for verification. Learn more about [request signatures](#request-signatures).

// Example action hook action { "type": "CONFIRMATION\_ACTION\_HOOK", "httpMethod": "POST", "uri": "https://example.com/action-hook", "label": "Example action", "associatedObjectProperties": \[ "some\_crm\_property" \], "confirmationMessage": "Are you sure you want to run example action?", "confirmButtonText": "Yes", "cancelButtonText": "No" }

The `httpMethod` can be set to  `GET`, `POST`, `PUT`, `DELETE`, or `PATCH`.  If using `GET` or `DELETE`, the `associatedObjectProperties` values will be appended to the request URL as query parameters. Otherwise, the properties will be sent in the request body.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/crm-cards#page-feedback)
-----------------------------------------------------------------------------------------------------

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