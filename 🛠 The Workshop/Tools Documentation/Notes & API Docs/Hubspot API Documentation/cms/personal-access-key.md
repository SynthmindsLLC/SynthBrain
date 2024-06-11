---
title: "Personal Access Key"
description: "A method of authenticating with local development tools, tied to a specific user in an account and limited by the permissions that individual user has. Provides security for accounts as it only affects the individual portals associated with that user. Similar to OAuth2 behind the scenes."
type: "group"
tags:
- "HubSpot"
- "Local Development Tools"
- "Authentication"
relationships:
- "#similar_to [[API Keys]]"
- "#used_for [[Development Tools]]"]]
updated_date: "2022-07-21"
---

Personal Access Key


=======================

Last updated: July 21, 2022

**Personal access keys are the recommended way of authenticating with local development tools.** Personal access keys work in a similar fashion to API Keys but are tied to a specific user in an account. Personal access keys only work with local development tools.

### Personal access keys compared to other Auth methods[](https://developers.hubspot.com/docs/cms/personal-access-key#personal-access-keys-compared-to-other-auth-methods)

The advantage of personal access keys over implementations like API keys is that API keys effectively have super admin permissions. Personal access keys are limited to the permissions that the individual user in the portal has. If the user has Super Admin, they see no difference in their functionality, but the advantage is that if say an individual developer needs to be removed from an account, the act of disabling their user on the account will disable their local development capabilities.

Because personal access keys are tied to the individual user in an account we are able to display more useful information, for example, if a developer changes or uploads a file using the local development tools while using a personal access key, we can attribute the change in-app to that user. This makes it easier to work with teams and understand who did what.

Personal access keys are tied to the individual user in the specific HubSpot account, and not the user directly. What this means is that using the local development tools you will need to generate a new personal access key for each account you wish to use the development tools with. This provides a layer of security for accounts, as a malicious actor obtaining your access key would then only be able to affect the individual portals and as that individual user.

#### Similarity to OAuth2[](https://developers.hubspot.com/docs/cms/personal-access-key#similarity-to-oauth2)

Behind the scenes, personal access keys actually act like OAuth2. When you generate a personal access key, you choose the permissions you want this key to have. You may only have 1 access key per user per HubSpot account. Once you've generated your access key, an app will be connected to your HubSpot account called "HubSpot Local Development Tools". This first-party HubSpot app facilitates authentication for the local development tools when using a personal access key. Disconnecting this app will delete any access key you previously generated, instantly making it so your local development tools will no longer be able to connect through those access keys. You will need to generate a new key and update your `hubspot.config.yml` file.

![personalcmsaccesskey](https://developers.hubspot.com/hubfs/personalcmsaccesskey.png "personalcmsaccesskey")

### Protect your credentials[](https://developers.hubspot.com/docs/cms/personal-access-key#protect-your-credentials)

Guard your personal access keys as if they are your account password, share them with no-one. They enable whoever has them to authenticate as if they are you and take any action you personally can take.

### Using personal access keys with the local development tools[](https://developers.hubspot.com/docs/cms/personal-access-key#using-personal-access-keys-with-the-local-development-tools)

Personal access keys were built to be used with local development tools.

[Get started with the local development tools](/docs/cms/guides/getting-started-with-local-development).

[View your personal CMS access key.](https://app.hubspot.com/l/personal-access-key)

When used for auth in the local development tools, your `hubspot.config.yml` file will resemble this:

defaultPortal: production portals: - name: production portalId: <portalId> authType: personalaccesskey personalAccessKey: >- CJDVnLanLRICEQIYyLu8LyDh9E4opf1GMhkAxGuU5XN\_O2O2QhX0khw7cwIkPkBRHye-OfIADgLBAAADAIADAAAAAAAAAAJCGQC8a5TlhtSU8T-2mVLxOBpxS18aM42oGKk auth: tokenInfo: accessToken: >- CJDVnLanLRICEQIYyLu8LyDh9E4opf1GMhkAxGuU5XN\_O2O2QhX0khw7cwIkPkBRHye-OfIADgLBAAADAIADAAAAAAAAAAJCGQC8a5TlhtSU8T-2mVLxOBpxS18aM42oGKk expiresAt: '2020-01-01T00:00:00.000Z'

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/personal-access-key#page-feedback)
------------------------------------------------------------------------------------------------

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