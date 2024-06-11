---
title: "Managing tokens"
description: "Overview of OAuth 2.0 access and refresh tokens, including obtaining, using, and deleting them for HubSpot data management."
type: "work"
tags:
- "OAuth"
- "HubSpot API"
- "Authentication"
relationships:
- "#related_to [[API Integration]]"
- "#used_by [[Developers]]"]]
- "#part_of [[Web Development]]"
birthdate: "2023-01-01 # Assuming the article was created on January 1, 2023."
deathdate: "null"
---

Managing tokens
===============

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

*   [
    
    Overview
    
    ](#tab-1)
*   [
    
    Endpoints
    
    ](#tab-2)

Get OAuth 2.0 access and refresh tokens:
----------------------------------------

Use the code you get after a user authorizes your app to get an access token and refresh token. The access token will be used to authenticate requests that your app makes. Access tokens are short lived; you can check the `expires_in` parameter when generating an access token to determine its lifetime (in seconds). You can use the refresh token endpoint to get a new access token when the current access token expires..

Use a previously obtained refresh token to generate a new access token. If you need offline access to HubSpot data, store the refresh token you get when initiating your OAuth integration and use it to generate a new access token once the initial one expires

**Note**: HubSpot access tokens will fluctuate in size as we change the information that is encoded. We recommend allowing for tokens to be up to 300 characters to account for any changes.

Get Information for OAuth 2.0 access or refresh token:
------------------------------------------------------

Get the meta data for an access or refresh token. This can be used to get the email address of the HubSpot user that the token was created for, as well as the Hub ID that the token is associated with.

Delete OAuth 2.0 Refresh Token:
-------------------------------

Deletes a refresh token. You can use this to delete your refresh token if a user uninstalls your app.

**Note:** This will only delete the refresh token. Access tokens generated with the refresh token will not be affected. Additionally, this will not uninstall an application from a HubSpot account or inhibit data syncing between an account and a connected application.

Using OAuth 2.0 access tokens:
------------------------------

`// Authorization: Bearer {token}`

`curl --request GET \`

  `--url 'https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false' \`

  `--header 'authorization: Bearer CJSP5qf1KhICAQEYs-gDIIGOBii1hQIyGQAf3xBKmlwHjX7OIpuIFEavB2-qYAGQsF4'`

`{contacts: .....}`

  In this example, the access token is:

 `CJSP5qf1KhICAQEYs-gDIIGOBii1hQIyGQAf3xBKmlwHjX7OIpuIFEavB2-qYAGQsF4`

**Notes:** If you're using OAuth 2.0 access tokens, you should **not** include `hapikey=` in the request URL. The Authorization header is used in place of that query parameter.

  
  

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/oauth/tokens#page-feedback)
-----------------------------------------------------------------------------------------

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