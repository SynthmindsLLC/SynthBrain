---
title: "Goals in HubSpot CRM API"
description: "The goals API allows you to retrieve and manage user-specific quotas for sales and services teams based on templates provided by HubSpot. You can request all goals, individual goals, or filter goals using specific criteria."
type: "concept"
tags:
- "HubSpot"
- "CRM"
- "API"
- "Goals"
relationships:
- "#related_to [[Sales Quotas]]"
- "#used_by [[Sales and Services Teams]]"
- "#part_of [[HubSpot CRM API]]"
- "#enables [[User-Specific Goal Management]]"
---

Goals
=====

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, goals are used to create user-specific quotas for their sales and services teams based on templates provided by HubSpot. The goals API allow you to retrieve goals data in your HubSpot account. 

Learn more about [using goals in HubSpot](https://knowledge.hubspot.com/reports/create-goals).

Retrieve goals[](https://developers.hubspot.com/docs/api/crm/goals#retrieve-goals)
----------------------------------------------------------------------------------

You can retrieve an individual goal or all goals in your account.

*   To request all goals, make a `GET` request to `/crm/v3/objects/goal_targets`.
*   To retrieve an individual goal, make a `GET` request to `/crm/v3/objects/goal_targets/{goalTargetId}/`.
*   To retrieve goals that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. Learn more about [searching the CRM](https://developers.hubspot.com/docs/api/crm/search).

For example, to retrieve a goal with an ID of `44027423340`, the request URL would be the following:

`https://api.hubapi.com/crm/v3/objects/goal_targets/44027423340/`

The response will include a few default properties, including the create date, last modified date.

JSON

Copy all

    // Example response
    {
     "id":"87504620389",
     "properties":{
      "hs_createdate":"2021-11-30T22:18:49.923Z",
      "hs_lastmodifieddate":"2023-12-11T19:21:32.851Z",
      "hs_object_id":"87504620389"
      },
     "createdAt":"2021-11-30T22:18:49.923Z",
     "updatedAt":"2023-12-11T19:21:32.851Z",
     "archived":false
    }

To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. Learn more about [user properties below](#goal-properties).

For example, making a `GET` request to the following URL would result in the response below:

`crm/v3/objects/users?properties=hs_job_title,hs_additional_phone`

JSON

Copy all

    // Example response
    {
     "id":"87504620389",
     "properties":{
      "hs_createdate":"2021-11-30T22:18:49.923Z",
      "hs_lastmodifieddate":"2023-12-11T19:21:32.851Z",
      "hs_object_id":"87504620389"
      },
     "createdAt":"2021-11-30T22:18:49.923Z",
     "updatedAt":"2023-12-11T19:21:32.851Z",
     "archived":false
    }

Goals properties[](https://developers.hubspot.com/docs/api/crm/goals#goals-properties)
--------------------------------------------------------------------------------------

When making a `GET` request to the Goals API, you can also request specific goal properties:

*   hs\_goal\_name: This is a string that denotes the name of a goal.
*   hs\_target\_amount: Number that denotes the goal target value.
*   hs\_start\_datetime: Goal's start date as a UTC timestamp.
*   hs\_end\_datetime: Goal's end date as a UTC timestamp.
*   hs\_created\_by\_user\_id: HubSpot UserId of the person who created the goal, not the one assigned to a goal.

For example, if you wanted to include all properties listed above, the request URL may resemble the following:

`https://api.hubapi.com/crm/v3/objects/goal_targets/44027423340?properties=hs_goal_name,hs_target_amount,hs_start_datetime,hs_end_datetime,hs_created_by_user_id`

The response may look similar to the JSON excerpt below:

// Example response for GET request to /crm/v4/objects/goal\_targets/{goal\_target\_id}/ { "id": '44027423340', "properties": { "hs\_created\_by\_user\_id": '885536', "hs\_createdate": '2023-02-15T15:53:07.080Z', "hs\_end\_datetime": '2024-01-01T00:00:00Z', "hs\_goal\_name": 'Revenue Goal 2023', "hs\_lastmodifieddate": '2023-02-16T10:02:21.131Z', "hs\_object\_id": '44027423340', "hs\_start\_datetime": '2023-12-01T00:00:00Z', "hs\_target\_amount": '2000.00' }, "createdAt": '2023-02-15T15:53:07.080Z', "updatedAt": '2023-02-16T10:02:21.131Z', "archived": false }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/goals#page-feedback)
--------------------------------------------------------------------------------------

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