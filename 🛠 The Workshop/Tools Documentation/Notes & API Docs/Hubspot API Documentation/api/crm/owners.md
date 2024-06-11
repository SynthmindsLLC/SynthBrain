---
title: "Owners in HubSpot CRM"
description: "Users who can be assigned specific users to records, activities, or marketing tasks and used for personalization tokens. Automatically created when new users are added or existing owners synced from Salesforce. Read-only API endpoints available for retrieving owner details."
type: "group"
tags:
- "HubSpot"
- "CRM"
- "Ownership"
relationships:
- "#created_by [[Salesforce]]"
- "#used_for [[Assigning Owners to Records, Activities, Marketing Tasks]]"
founded: "2014-08-01"
---

Owners
======

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

HubSpot owners [assign](https://knowledge.hubspot.com/contacts/how-to-set-an-owner) specific users to records, activities, or marketing tasks, and can be used in personalization tokens for your content. Owners are automatically created and updated in HubSpot when new users are added or existing owners are synced from [Salesforce](https://knowledge.hubspot.com/articles/kcs_article/salesforce/how-will-a-salesforce-owner-will-be-recognized-by-hubspot).

The owners API endpoints are read-only, so you can use them to retrieve an owner's identifying details, including the owner ID. This identifier can then be used to assign ownership to CRM records in HubSpot, via an integration, or via property change API calls.

Retrieve a list of owners[](https://developers.hubspot.com/docs/api/crm/owners#retrieve-a-list-of-owners)
---------------------------------------------------------------------------------------------------------

To retrieve the owners in your account, make a `GET` request to `/crm/v3/owners`. The response will return each user's name, email, ID values, create/update dates, and if applicable, team information. Two ID values are returned, which are used for different purposes:

*   `id`: the ID of the owner. This value should be used when retrieving information about a specific owner, and when assigning an owner to a record or activity.
*   `userId`: the ID of the user. This value can be used to specify users in the [settings API](/docs/api/settings/user-provisioning), but will result in an error if it is used to assign ownership.

Retrieve information about an individual owner[](https://developers.hubspot.com/docs/api/crm/owners#retrieve-information-about-an-individual-owner)
---------------------------------------------------------------------------------------------------------------------------------------------------

To retrieve a specific owner, make a `GET` request to `/crm/v3/owners/{ownerId}`. You should use the `id` value to specify the owner for which you want more details.

**Please note**: the `updatedAt` value in the response changes based on updates to the Owner object itself. It will not be updated for changes to the User object. For example, changing a user's permissions will not update the `updatedAt` value.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/owners#page-feedback)
---------------------------------------------------------------------------------------

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