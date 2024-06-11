---
title: "OAuth Quickstart Guide"
description: "A guide on using OAuth 2.0 Authorization Code grant type for authenticating with HubSpot's APIs."
type: "work"
tags:
- "OAuth"
- "HubSpot"
- "API Authentication"
relationships:
- "#developed_by [[HubSpot]]"
- "#related_to [[Authorization Code Grant Type]]"]]
- "#used_for [[API Access]]"
tags:
- "OAuth"
- "HubSpot"
- "API Authentication"
birthdate: "N/A"
deathdate: "N/A"
---

OAuth Quickstart Guide
======================

Before you get started
----------------------

Before you can start using OAuth with HubSpot, you'll need to have:

*   [A developer account](https://app.hubspot.com/signup/developers?_ga=2.207664146.1651439249.1582052738-500942594.1573763828)
*   [An app](https://developers.hubspot.com/docs/api/creating-an-app) associated with your developer account
*   A HubSpot account\* to install your app in (you can use an existing account or [create a test account](/docs-beta/creating-test-accounts))

**\*You must be a Super Admin to install an app in a HubSpot account**

* * *

### How it works

HubSpot supports the [OAuth 2.0 Authorization Code grant type](https://developer.okta.com/blog/2018/04/10/oauth-authorization-code-grant-type), which can be broken down into four basic steps:

1.  Your app opens a browser window to send the user to the HubSpot OAuth 2.0 server
2.  The user reviews the requested permissions and grants the app access
3.  The user is redirected back to the app with an authorization code in the query string
4.  The app sends a request to the OAuth 2.0 server to exchange the authorization code for an access token

### In this guide

*   [Quickstart App](#quick-start-app): A Node.js demo app that authenticates with HubSpot's OAuth 2.0 server
*   [Getting OAuth 2.0 tokens](#getting_tokens): How to authorize your app with users
*   [Using OAuth 2.0 tokens](#using_tokens): How to make queries with a token
*   [Refreshing OAuth 2.0 tokens](#refreshing_tokens): How to use the refresh token provided by HubSpot

**Note:** All code examples in this guide are written in JavaScript (Node.js)

Quickstart app
--------------

If this is your first time using OAuth authentication with HubSpot's APIs, we strongly recommend checking out the [OAuth 2.0 Quickstart App](https://github.com/HubSpot/oauth-quickstart-nodejs), written in Node.js. This sample app is designed to get you started using OAuth 2.0 as quickly as possible by demonstrating all the steps outlined below in [Getting OAuth 2.0 tokens](/docs-beta/oauth/tokens). 

*   [Get the app on Github](https://github.com/HubSpot/oauth-quickstart-nodejs)

Getting OAuth 2.0 tokens
------------------------

### Step 1: Create the authorization URL and direct the user to HubSpot's OAuth 2.0 server

When sending a user to HubSpot's OAuth 2.0 server, the first step is creating the authorization URL. This will identify your app and define the resources (scopes) it's requesting access to on behalf of the user. The query parameters you can pass as part of an authorization URL are shown below. For more detailed information on this step, read the [reference doc](https://developers.hubspot.com/docs-beta/working-with-oauth).

Authorization URL query parameters
| Parameter | Required? | Description | Example |
| --- | --- | --- | --- |
| `client_id` | Yes | The client ID identifies your app. Find it on your app's settings page. | 
`7fff1e36-2d40-4ae1-bbb1-5266d59564fb`

 |
| `scope` | Yes | The [scopes](/docs-beta/working-with-oauth#scopes) your application is requesting, separated by URL-encoded spaces. | 

`contacts%20social`

 |
| `redirect_uri` | Yes | The URL that the user will be redirected to after they authorize your app for the requested scopes. **For production applications, https is required.** | 

`https://www.example.com/auth-callback`

 |
| `optional_scope` | No | The scopes that are optional for your app, and will be dropped if the selected HubSpot portal does not have access to those products | 

`automation`

 |
| `state` | No | A unique string value that can be used to maintain the user's state when they're redirected back to your app. | 

`WeHH_yy2irpl8UYAvv-my`

 |

Once you've created your URL, start the OAuth 2.0 process by sending the user to it.

##### Examples

Using a server-side redirect:

// Build the auth URL const authUrl = 'https://app.hubspot.com/oauth/authorize' + \`?client\_id=${encodeURIComponent(CLIENT\_ID)}\` + \`&scope=${encodeURIComponent(SCOPES)}\` + \`&redirect\_uri=${encodeURIComponent(REDIRECT\_URI)}\`; + \`&state=${encodeURIComponent(STATE)}\`; // Redirect the user return res.redirect(authUrl);

Using an HTML link:

<a href="https://app.hubspot.com/oauth/authorize?scope=contacts%20social&redirect\_uri=https://www.example.com/auth-callback&client\_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx&state=xxxxxxxx">Install</a>

##### Encoding an additional redirect user state

Some apps may need to redirect the user to different locations. For example, an app may wish to redirect users to different subdomains of their integration (e.g. userA.integration.com and userB.integration.com). To do so, use the `state` parameter to encode more information about the user state: 

1\. Generate and store a nonce value for the state parameter.

2\. Store the user's state in a local datastore using the nonce as its key.

3\. Include the nonce value as the state parameter in the authorization URL. 

4\. When the user authenticates and is redirected to your redirect URL, validate the state parameter and use it as the key to retrieve the user state that was stored. 

5\. From there, redirect the user as needed (e.g. redirecting again to a user specific URL).

### Step 2: HubSpot prompts user for consent

HubSpot displays a consent window to the user showing the name of your app and a short description of the HubSpot API services it's requesting permission to access. The user can then grant access to your app.

![[Example] Install Screen](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/%5BExample%5D%20Install%20Screen.png?width=600&height=678&name=%5BExample%5D%20Install%20Screen.png)

**Note:** The user installing the app must have access to all requested scopes. If they don't have the required access, the installation will fail and they will be directed to an error page. If a user sees this permissions error page, they'll need to have a Super Admin install the app.

Your application doesn't do anything at this stage. Once access is granted, the HubSpot OAuth 2.0 server will send a request to the callback URI defined in the authorization URL.

### Step 3: Handle the OAuth 2.0 server response

When the user has completed the consent prompt from Step 2, the OAuth 2.0 server sends a `GET` request to the redirect URI specified in your authentication URL. If there are no issues and the user approves the access request, the request to the redirect URI will be returned with a `code` query parameter attached. If the user doesn't grant access, no request will be sent.

##### Example:

app.get('/oauth-callback', async (req, res) => { if (req.query.code) { // Handle the received code } });

### Step 4: Exchange authorization code for tokens

After your app receives an authorization code from the OAuth 2.0 server, it can exchange that code for an access and refresh token by sending a URL-form encoded `POST` request to `https://api.hubapi.com/oauth/v1/token` with the values shown below. For more detailed information on this step, take a minute to read this [reference doc](/docs-beta/oauth/tokens).

| Parameter | Description | Example |
| --- | --- | --- |
| `grant_type` | Must be `authorization_code` | `authorization_code` |
| `client_id` | Your app's client ID | `7fff1e36-2d40-4ae1-bbb1-5266d59564fb` |
| `client_secret` | Your app's client secret | `7c3ce02c-0f0c-4c9f-9700-92440c9bdf2d` |
| `redirect_uri` | The redirect URI from when the user authorized your app | `https://www.example.com/auth-callback` |
| `code` | The authorization code received from the OAuth 2.0 server | `5771f587-2fe7-40e8-8784-042fb4bc2c31` |

##### Example:

const formData = { grant\_type: 'authorization\_code', client\_id: CLIENT\_ID, client\_secret: CLIENT\_SECRET, redirect\_uri: REDIRECT\_URI, code: req.query.code }; request.post('https://api.hubapi.com/oauth/v1/token', { form: formData }, (err, data) => { // Handle the returned tokens }

The body of the token response will be JSON data with the form:

{"refresh\_token":"6f18f21e-a743-4509-b7fd-1a5e632fffa1","access\_token":"CN2zlYnmLBICAQIYgZXFLyCWp1Yoy\_9GMhkAgddk-zDc-H\_rOad1X2s6Qv3fmG1spSY0Og0ACgJBAAADAIADAAABQhkAgddk-03q2qdkwdXbYWCoB9g3LA97OJ9I","expires\_in":1800}

**Note:** The access token will expire after the number of seconds given in the `expires_in` field of the response, currently 30 minutes. For information on getting a new access token, see Refreshing OAuth 2.0 tokens.

Using OAuth 2.0 tokens
----------------------

Once the authorization code flow is completed, your app is authorized to make requests on behalf of the user. To do this, provide the token as a bearer token in the `Authorization` HTTP header. Specific details can be found in the [reference doc](/docs-beta/oauth/tokens).

##### Example:

request.get('https://api.hubapi.com/contacts/v1/lists/all/contacts/all?count=1', { headers: { 'Authorization': \`Bearer ${ACCESS\_TOKEN}\`, 'Content-Type': 'application/json' } }, (err, data) => { // Handle the API response } );

**Please note:**access tokens reflect the scopes requested from the app and do not reflect the permissions or limitations of what a user can do in their HubSpot account. For example, if a user has permissions to view only owned contacts but authorizes a request for the  `crm.objects.contacts.read` scope, the resulting access token can view all contacts in the account and not only those owned by the authorizing user. 

Refreshing OAuth 2.0 tokens
---------------------------

OAuth access tokens expire periodically. This is to make sure that if they're compromised, attackers will only have access for a short time. The token's lifespan in seconds is specified in the `expires_in` field when an authorization code is exchanged for an access token.

Your app can exchange the received refresh token for a new access token by sending a URL-form encoded `POST` request to `https://api.hubapi.com/oauth/v1/token` with the values below. For more detailed information on this step, check out the [reference doc](/docs-beta/oauth/tokens).

| Parameter | Description | Example |
| --- | --- | --- |
| `grant_type` | Must be `refresh_token` | `refresh_token` |
| `client_id` | Your app's client ID | `7fff1e36-2d40-4ae1-bbb1-5266d59564fb` |
| `client_secret` | Your app's client secret | `7c3ce02c-0f0c-4c9f-9700-92440c9bdf2d` |
| `redirect_uri` | The redirect URI from when the user authorized your app | `https://www.example.com/auth-callback` |
| `refresh_token` | The refresh token received when the user authorized your app | `b9443019-30fe-4df1-a67e-3d75cbd0f726` |

##### Example:

const formData = { grant\_type: 'refresh\_token', client\_id: CLIENT\_ID, client\_secret: CLIENT\_SECRET, redirect\_uri: REDIRECT\_URI, refresh\_token: REFRESH\_TOKEN }; request.post('https://api.hubapi.com/oauth/v1/token', { form: formData }, (err, data) => { // Handle the returned tokens }

The body of the token response will be JSON data with the form:

// Sample response { "refresh\_token": "6f18f21e-a743-4509-b7fd-1a5e632fffa1", "access\_token": "CN2zlYnmLBICAQIYgZXFLyCWp1Yoy\_9GMhkAgddk-zDc-H\_rOad1X2s6Qv3fmG1spSY0Og0ACgJBAAADAIADAAABQhkAgddk-03q2qdkwdXbYWCoB9g3LA97OJ9I", "expires\_in": 1800 }

The new access token can then be used to make calls on behalf of the user. When the new token expires, you can follow the same steps again to retrieve a new one.

* * *

#### Related docs

[Auth methods on HubSpot](/docs-beta/intro-to-auth)

[Working with OAuth](/docs-beta/working-with-oauth)

[Manage tokens](/docs-beta/oauth/tokens)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/oauth-quickstart-guide#page-feedback)
---------------------------------------------------------------------------------------------------

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