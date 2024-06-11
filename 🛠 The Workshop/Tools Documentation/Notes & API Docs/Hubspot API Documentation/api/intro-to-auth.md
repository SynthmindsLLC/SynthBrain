---
title: "HubSpot API Key Deprecation Notice"
description: "As of November 30, 2022, HubSpot has deprecated the use of API Keys for authentication and recommends using private app access tokens or OAuth. Continued usage poses a security risk to your account and data. Learn more about this change and how to migrate from an API key integration to a private app at [HubSpot's documentation](https://developers.hubspot.com/changelog/upcoming-api-key-sunset)"
type: "notice"
tags:
- "API"
- "Authentication"
- "Security Risk"
relationships:
- "#caused_by [[HubSpot's Security Policy]]"
- "#replaced_with [[Private App Access Token]], [[OAuth]]"
founded: "2014-05-08"
---

**Please note:** as of November 30, 2022, HubSpot API Keys are being deprecated and are no longer supported. Continued use of HubSpot API Keys is a security risk to your account and data. During this deprecation phase, HubSpot may deactivate your key at any time.

You should instead authenticate using a private app access token or OAuth. Learn more about [this change](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) and how to [migrate an API key integration](/docs/api/migrate-an-api-key-integration-to-a-private-app) to use a private app instead.

Authentication methods on HubSpot
=================================

There are two ways to authenticate calls to HubSpot's APIs: [OAuth](https://developers.hubspot.com/docs-beta/working-with-oauth), and [private app](/docs/api/private-apps) access tokens. Below, learn more about each method and how to include it in your code for authorization.

If you were previously using an API key to authenticate, learn how to [migrate to using a private app access token](/docs/api/migrate-an-api-key-integration-to-a-private-app) instead.

**Please note:** integrations designed for multi-customer use or listing on the App Marketplace must be built as an app using HubSpot’s OAuth protocol

OAuth[](https://developers.hubspot.com/docs/api/intro-to-auth#oauth)
--------------------------------------------------------------------

To make a request using [OAuth](/docs/api/oauth/tokens), include the OAuth access token in the authorization header:

/~curl --header "Authorization: Bearer C4d\*\*\*sVq" https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false

Private app access tokens[](https://developers.hubspot.com/docs/api/intro-to-auth#private-app-access-tokens)
------------------------------------------------------------------------------------------------------------

Similar to OAuth, to make a request using a private app access token, include the token in the authorization header:

/~curl --header "Authorization: Bearer \*\*\*-\*\*\*-\*\*\*\*\*\*\*\*\*-\*\*\*\*-\*\*\*\*-\*\*\*\*-\*\*\*\*\*\*\*\*\*\*\*\*" https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false

* * *

#### Related docs

[Working with OAuth](/docs/api/working-with-oauth)

[OAuth Quickstart Guide](https://developers.hubspot.com/docs-beta/oauth-quickstart-guide)

[Private Apps](/docs/api/private-apps)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/intro-to-auth#page-feedback)
------------------------------------------------------------------------------------------

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