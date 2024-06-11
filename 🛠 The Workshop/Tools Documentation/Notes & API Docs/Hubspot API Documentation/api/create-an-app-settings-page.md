---
title: "Create a settings page for your app in HubSpot"
description: "A guide on creating an app settings page using the settings builder to give users more control over how they use your app within their HubSpot account."
type: "group"
tags:
- "HubSpot"
- "App Settings Page"
- "Developer Guide"
relationships:
- "#founded_by [[HubSpot]]"
- "#part_of [[Connected Apps]]"
created_date: "YYYY-MM-DD # Replace with actual creation date of the guide"
---

Create a settings page for your app
===================================

Create a settings page for your public app to give users more control over how they use your app in their HubSpot account. Developers can create a settings page for their app using the settings builder so that users can access the settings from the [_Connected Apps_](https://knowledge.hubspot.com/integrations/connect-apps-to-hubspot) page in HubSpot.

To create the app settings page:

*   In your [developer account](/docs/api/account-types), click **Apps**.
*   Click the **app** you want to create a settings page for. 
*   In the left sidebar menu, click **App settings**. 
*   To create a settings page from a template, click **Build from a template**.
*   To create a settings page from scratch, click **Start from scratch**. You'll then be brought to the app settings page builder.

![app-settings-intro](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/app-settings-intro.png?width=600&height=262&name=app-settings-intro.png "app-settings-intro")

**Please note:** if you select the _Build from a template_ option, ensure that all placeholder control component URLs are updated to your own API endpoints. 

There are two tabs on the settings page that you can customize:

*   On the _General settings_ tab, users can interact with selected components such as buttons and toggles to configure their app settings. 
*   On the _Feature discovery_ tab, add cards highlighting your app’s features, explain how the features work, and link to further documentation or resources.

The app settings builder is organized around three sections: accounts, controls, and feature cards.

Below, learn how to set up the following:

*   An account component to enable users to configure user-specific settings.
*   Control components to enable users to configure settings with buttons, dropdown menus, and more.
*   Feature cards to provide context to users as they configure their settings.

Set up the account component[](https://developers.hubspot.com/docs/api/create-an-app-settings-page#set-up-the-account-component)
--------------------------------------------------------------------------------------------------------------------------------

App settings can be uniquely configured for each user. The account component is a dropdown menu of all users in the connected HubSpot account. When viewing the settings page, a user can select any user in the account to view and set user-specific settings for the app. 

**Please note:** the account component is required and only one component can be added per app.

For an account component to work:

*   That account component must have a URL for fetching account data.
*   The account data fetched from the URL must include a list of connected users for the integration.
*   The `accountID` returned to HubSpot is what’s passed on to the control and feature card components so you’ll know which account HubSpot is interacting with.

![app-settings-accounts](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/app-settings-accounts.png?width=600&height=247&name=app-settings-accounts.png "app-settings-accounts")

The **account** **URL** is required to populate a list of user accounts on the customer’s app setting page. Users can then pick any of the accounts listed. Whichever account is selected will be sent on future action calls for toggles, buttons, and other action types. This allows the use of multiple account configurations in a single account that installs your app. You should use all the parameters HubSpot sends to determine which account you are making future changes for. 

HubSpot will send a `X-HubSpot-Signature` header to verify that the request came from HubSpot. Read more about [request signatures](https://developers.hubspot.com/docs/api/webhooks/validating-requests) for details.

![account-settings-url](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/account-settings-url.png "account-settings-url")

To add an account component:

*   Create an endpoint that’s configured to handle either a `GET` or `POST` request from HubSpot. This will be called to populate a list of user accounts on the customer’s app settings page. 
*   If you select `GET` as the HTTP method for your endpoint, the fields will be included as query params. For example:

https://api.hubapi.com/application/settings/test/v1/actions/accounts-fetch?actionType=ACCOUNTS\_FETCH&appId=999&portalId=1234&userId=1001&userEmail=test%40example.com

*   If you select `POST` as the HTTP method, the fields will be included in the request body as a JSON object. For example:

// Request body for POST request to /settings-account-fetch { “actionType”: “ACCOUNTS\_FETCH”, “appId”: 123, “portalId”: 456 “userId”: 1 “userEmail”: “test@example.com”, }

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot that includes a response field, which contains the `accountId`, `accountName` of the user, along with an optional `accountLogoUrl`. 

{ "response": { "accounts": \[ # Object\[\] REQUIRED { "accountId": "abc123", # String REQUIRED "accountName": "Joe Cool", # String REQUIRED "accountLogoUrl": # Url OPTIONAL } \] } }

Set up the control component
----------------------------

You can set up controls for users such as buttons, toggles, or a dropdown menu to manage general app settings and functions in the control component. Controls are optional. If you choose to add a control, each control must contain a short header and description describing its purpose or function. 

To add a component, populate the following fields:

*   **Header**: what the control does.
*   **Description**: a description of the control.
*   **Control type**: select from three control types: button, toggle, or dropdown menu. 

HubSpot will send a `X-HubSpot-Signature` header to verify that the request came from HubSpot. Read more about [request signatures](https://developers.hubspot.com/docs/api/webhooks/validating-requests) for details.

HubSpot will attempt to parse responses to actions as JSON and look for a message property. This message will be displayed to the user on either success or failure. Response status code of 2xx will show a success message and status codes of 4xx or 5xx will show an error message.

An example response may look similar to the following:

// Example GET to https://api.hubapi.com/application/settings/test/v1/actions/toggle-update { "message": "You have successfully enabled your data sync" }

![app-settings-control](https://developers.hubspot.com/hubfs/Knowledge_Base_2021/app-settings-control.png "app-settings-control")

### Add a button control type

Use a button to initiate an action via a call to your API endpoint. You will supply the API endpoint and choose the request method (either `PUT`, `POST` or `DELETE`). While no data is returned, HubSpot will communicate the resulting success, failure, or timeout status of the action to the customer. You should use all parameters HubSpot sends to determine which account you are making changes for.

To add a button control type:: 

*   Select a **button** control type.
*   Click **Configure button behavior**. 
*   Select **Hit an external endpoint**. 
*   In the **Button text** field, enter text for the button. This should tell the customer what it does.
*   Create an endpoint that’s configured to handle either a `PUT`, `POST` or `DELETE` request from HubSpot. HubSpot will provide the associated identifying fields for the customer based on the HTTP method you select when configuring your button.
*   The fields will be included in the request body as a JSON object. For example:

curl -i -X POST \\ -H 'Content-Type: application/json' \\ -d ' { "actionType": "BUTTON\_UPDATE", "appId": 999, "portalId": 1234, "userId": 1001, "userEmail": "jondoe@example.com", "accountId": "jondoe@example.com" } ' \\ 'https://api.hubapi.com/application/settings/test/v1/actions/button-update'

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot. This should include a response field along with an optional message to the user. For example:

{ "response": null, # Ignored for beta "message": "Custom message to user" # Optional }

### Open an iframe with a button control type

You can also use a button to open a modal displaying an iframe. To do so:

*   Select a **button** control type.
*   Click **Configure button behavior**. 
*   Select **Open an external URL within an iframe**.
*   In the **Button text** field, enter text for the button. This should tell the customer what it does.
*   Select the **HTTP Method** (`GET` or `POST`).
*   Enter the **Endpoint URL**. Do not input the iframe URL. 

*   If you select `GET` as the HTTP method for your endpoint, the fields will be included as query parameters. For example:

https://api.hubapi.com/application/settings/test/v1/actions/iframe-fetch?actionType=IFRAME\_FETCH&appId=999&portalId=1234&userId=1001&userEmail=test%40example.com&accountId=joedoe@example.com

*   If you select `POST` as the HTTP method, the fields will be included in the request body as a JSON object. For example:

curl -i -X POST \\ -H 'Content-Type: application/json' \\ -d ' { "actionType": "IFRAME\_FETCH", "appId": 999, "portalId": 1234, "userId": 1001, "userEmail": "jondoe@example.com", "accountId": "jondoe@example.com" } ' \\ 'https://api.hubapi.com/application/settings/test/v1/actions/iframe-fetch'

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot. This should include a response field containing the `iframeURL`:

{"response":{"iframeUrl":"https://en.wikipedia.org/wiki/Flywheel"}}

All iframe modals will open from within your app’s settings page. 

### Add a toggle control type

The toggle control type provides users with a toggle option that they can turn on or off. HubSpot retrieves a toggle’s current state from the `TOGGLE_FETCH` URL. When a user clicks the toggle, HubSpot calls the `TOGGLE_UPDATE` URL to send the toggle’s new state. Other identifiers such as `accountId` and `portalId` are also passed – this allows you to identify the user triggering the toggle. 

To add a toggle:

*   Select a **Toggle** control type.
*   Click **Configure toggle behavior**. 
*   In the _Toggle settings_ pop-up, set up the toggle status and update toggle sections.
*   If you’re fetching the toggle status:
    *   Create an endpoint that’s configured to handle either a `GET` or `POST` request from HubSpot, which will be called to fetch the existing toggle state for a customer when they visit the settings page for your app.
    *   If you select `GET` as the HTTP method for your endpoint, the fields will be included as query parameters. For example:

https://api.hubapi.com/application/settings/test/v1/actions/toggle-fetch?actionType=TOGGLE\_FETCH&appId=999&portalId=1234&userId=1001&userEmail=test%40example.com&accountId=jondoe%40example.com

*   If you select `POST` as the HTTP method, the fields will be included in the request body as a JSON object. For example:

curl -i -X POST \\ -H 'Content-Type: application/json' \\ -d ' { "actionType": "TOGGLE\_FETCH", "appId": 999, "portalId": 1234, "userId": 1001, "userEmail": "jondoe@example.com", "accountId": "jondoe@example.com", "enabled": false } ' \\ 'https://api.hubapi.com/application/settings/test/v1/actions/toggle-fetch'

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot that includes a response field, which contains the current enabled state of the toggle as a boolean, along with an optional message to the user. For example:

{"response":{"enabled":true},"message":"Optional custom message to user"}

*   To configure the toggle when it’s turned on or off:
    *   Create an endpoint that’s configured to handle either a `POST` or `PUT` request from HubSpot, which will be called when the toggle is turned on or off. 
    *   The fields will be included in the request body as a JSON object. For example:

curl -i -X POST \\ -H 'Content-Type: application/json' \\ -d ' { "actionType": "TOGGLE\_UPDATE", "appId": 999, "portalId": 1234, "userId": 1001, "userEmail": "jondoe@example.com", "accountId": "jondoe@example.com", "enabled": false } ' \\ 'https://api.hubapi.com/application/settings/test/v1/actions/toggle-update'

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot that includes a response field, which contains the current enabled state of the toggle as a boolean, along with an optional message to the user. For example:

{ "response": {"enabled": false}, # Boolean REQUIRED "message": "Custom message to user" # Optional }

### Add a dropdown control type

The dropdown control type provides the customer with a list of options they can select from. HubSpot retrieves the list from the `DROPDOWN_FETCH` URL. Your API may also return a `selectedOption` field to display which option the user has selected, as well as a placeholder field signifying what text to display when no option is selected. By passing the `accountId`, `portalId`, and other identifiers, you can identify which user triggered the control.

When a user clicks on an option in the dropdown menu, HubSpot calls the `DROPDOWN_UPDATE` URL to send the same identifiers along with the selected option.

To add a dropdown menu:

*   Select the **dropdown** control type.
*   Click **Configure dropdown behavior**.
*   In the _Dropdown settings_ pop-up box, configure the _Dropdown fetch_ and _Dropdown update_ sections.
*   To fetch the list of dropdown options:

*   Create an endpoint that’s configured to handle either a `GET` or `POST` request from HubSpot, which will be called to fetch the list of dropdown options from the app settings page.

*   If you select `GET` as the HTTP method for your endpoint, the fields will be included as query parameters. For example:

// GET request to /dropdown-fetch https://api.hubapi.com/application/settings/test/v1/actions/dropdown-fetch?actionType=DROPDOWN\_FETCH&appId=123&portalId=456&userId=1&userEmail=jkurien@hubspot.com&accountId=jkurien@hubspot.com

*   If you select `POST` as the HTTP method, the fields will be included in the request body as a JSON object. For example:

curl -i -X POST \\ -H 'Content-Type: application/json' \\ -d ' { "actionType": "DROPDOWN\_FETCH", "appId": 999, "portalId": 1234, "userId": 1001, "userEmail": "jondoe@example.com", "accountId": "jondoe@example.com", "enabled": false } ' \\ 'https://api.hubapi.com/application/settings/test/v1/actions/dropdown-fetch'

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot that includes a response field, which contains the current enabled state of the toggle as a boolean, along with an optional message to the user. For example:

{ "response": { "options": \[ { "text": "Option 1", "value": "option1" }, { "text": "Option 2", "value": "option2" } \], "selectedOption": "option2" # optional "placeholder": "Choose an Option" # optional }, }

*   To configure what happens when an option is selected from the dropdown menu:
    *   Create an endpoint that’s configured to handle either a `POST` or `PUT` request from HubSpot. The fields will be included in the body as a JSON object:

curl -i -X POST \\ -H 'Content-Type: application/json' \\ -d ' { "actionType": "DROPDOWN\_UPDATE", "appId": 999, "portalId": 1234, "userId": 1001, "userEmail": "jondoe@example.com", "accountId": "jondoe@example.com", "selectedOption": "option1" } ' \\ 'https://api.hubapi.com/application/settings/test/v1/actions/dropdown-update'

*   In the request handler for your app’s endpoint, you should return a JSON object to HubSpot that includes a response field, which contains the current enabled state of the toggle as a boolean, along with an optional message to the user. For example:

{ "response": { "actionType": "DROPDOWN\_UPDATE", "selectedOption": "option2" "message": "null" }, }

Set up feature cards
--------------------

Use feature cards to introduce, describe, and help users set up app features. You can add up to six feature cards per app. 

To add a feature card:

*   Set up the following fields for the card
    *   **Card header:** enter a **header** – this is the title of a feature.
    *   **Description**: enter a **description** for the feature.
    *   **CTA button text**: enter **text** for the CTA button.
    *   **CTA button URL**: enter a **URL.** It is recommended to have the CTA direct users to where the feature appears in HubSpot.
    *   **Illustration:** select an illustration for the feature card. 
    *   **Add image or video:** provide a preview carousel of the feature to your users.
        *   Upload an image or video file. You can upload up to six images or videos.
        *   Add a **description** of the image or video. 

*   Once you’ve set up all the fields, click **Add to settings.**

Once you’ve added all the components to the settings page builder, click **Deploy changes** in the upper-right to deploy the settings page to all users. 

Restore a previous version of an app settings page
--------------------------------------------------

The app settings builder supports versioning and allows you to restore previously deployed settings pages. To do so:

*   Click the **Version history** tab.
*   Next to the version you want to deploy, click **Restore**. The selected version of the app settings page will load in the builder. 
*   From there, you can make new edits to the settings page and deploy it. 

![app-settings-version](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/app-settings-version.png?width=600&height=475&name=app-settings-version.png "app-settings-version")

Test your app settings page
---------------------------

To test your app’s settings page, set up a [test account](https://developers.hubspot.com/docs/api/creating-test-accounts) from your developer account, then install the app on that test account. The app settings page will load on the test account’s connected app. 

HubSpot also logs all requests made to URLs in the app settings page. To view this request log:

*   In your developer account, click **Apps**.
*   Click the **app** you want to create a settings page for. 
*   In the left sidebar menu, click **Monitoring**. 
*   Click the **App settings** tab.

**Please note:** clicking buttons or toggles will make calls to the URLs you have configured, so ensure that you are using a true developer test account.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/create-an-app-settings-page#page-feedback)
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