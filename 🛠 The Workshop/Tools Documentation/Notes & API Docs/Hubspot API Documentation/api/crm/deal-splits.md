Deal splits (BETA)[](https://developers.hubspot.com/docs/api/crm/deal-splits#deal-splits-beta-)
-----------------------------------------------------------------------------------------------

.interest-form { padding: 1em; display: none; height: 100%; } .interest-text { padding: 1em; } .hs-form>fieldset { max-width: 100% !important; }

**Please note:** this API is currently in beta and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to our [Developer Terms](https://legal.hubspot.com/hubspot-developer-terms)& [Developer Beta Terms](https://legal.hubspot.com/developerbetaterms?). You also acknowledge and understand the risk associated with testing an unstable API.

  

Provide Feedback

hbspt.forms.create({ portalId: "428357", formId: "037350c3-535d-4755-82ca-53b73367754f", cssClass: "hs-form" });

First name

Last name

Email

How satisfied are you with this API beta\*

Please SelectVery satisfiedSatisfiedNeutralUnsatisfiedVery unsatisfied

Can we contact you with follow-up questions about this feedback?

*   Yes, HubSpot can contact me about this feedback 

By selecting “Yes,” you are allowing HubSpot to store any personal information submitted through this form. We respect your privacy and will only use it to contact you if we have follow-up questions about today’s feedback. You can unsubscribe from these communications at any time. For more information, check out our [Privacy Policy.](https://legal.hubspot.com/privacy-policy)

$(document).ready(() => { $("#interest-btn").click(() => { $(".interest-form").toggle(); }); });

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

If your HubSpot account has a _Sales Hub Enterprise_ subscription, you can set up [deal splits](https://knowledge.hubspot.com/records/split-deal-credit-among-users) to split credit for deal amounts between multiple users. Once [deal splits are turned on](https://knowledge.hubspot.com/records/split-deal-credit-among-users#turn-on-deal-splits) in your HubSpot account, you can use the deal splits API to create new deal splits or view and update existing splits.

Create or update deal splits[](https://developers.hubspot.com/docs/api/crm/deal-splits#create-or-update-deal-splits)
--------------------------------------------------------------------------------------------------------------------

To add new splits or update existing splits for deals, make a `POST` request to `crm/v3/objects/deals/splits/batch/upsert`.

In your request, include the following fields for each deal:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`id`

 | The ID of the deal. You can retrieve this via the [deals API](/docs/api/crm/deals#retrieve-deals). |
| 

`splits`

 | 

An array that contains the user to assign a split to, and the percentage of the deal amount to assign. In the array, include the following fields:

`ownerId`: the [owner ID](/docs/api/crm/owners) assigned to the HubSpot user.

`percentage`: the percentage of the deal amount to assign to the owner.

 |

When adding deal splits, the deal's owner must be included as a split owner, the split percentages must add up to 1.0, and you must meet the limits for the split user maximum and split percentage minimum set in your [deal split settings.](https://knowledge.hubspot.com/records/split-deal-credit-among-users#turn-on-deal-splits)If any deals included in the batch request fail validation for these requirements, the request will result in an error. 

For example, to assign even deal credit to two users on a deal, your request would look like:

///Example request body { "inputs": \[ { "id": 5315919905, "splits": \[ { "ownerId": 41629779, "percentage": 0.5 }, { "ownerId": 60158084, "percentage": 0.5 } \] } \] }

If a deal didn't have existing splits, the splits will appear on the deal record following your request. If the deal had existing splits, they will be replaced by the splits you created in your request.

Retrieve deal splits[](https://developers.hubspot.com/docs/api/crm/deal-splits#retrieve-deal-splits)
----------------------------------------------------------------------------------------------------

To view split information for deals, make a `POST` request to `crm/v3/objects/deals/splits/batch/read`. In your request, include the `id` values of the deals with splits you want to view. You can retrieve a deal's `id` via the [deals API](/docs/api/crm/deals#retrieve-deals).

For example, to retrieve deal splits for two deals, your request could look like:

///Example request body { "inputs": \[ { "id": "5315919905" }, { "id": "17137567105" } \] }

For each deal, the response will include the date and time the splits were created or updated, the IDs of users splitting the deal, and the percentage of the deal amount assigned to each user.

For two deals, the response would look similar to:

///Example response { "status": "COMPLETE", "results": \[ { "id": "17137567105", "splits": \[ { "id": "311226010924", "properties": { "hs\_deal\_split\_percentage": "0.5", "hubspot\_owner\_id": "41629779" }, "createdAt": "2024-03-11T19:55:26.219Z", "updatedAt": "2024-03-11T19:55:26.219Z", "archived": false }, { "id": "311226010925", "properties": { "hs\_deal\_split\_percentage": "0.25", "hubspot\_owner\_id": "60158084" }, "createdAt": "2024-03-11T19:55:26.219Z", "updatedAt": "2024-03-11T19:55:26.219Z", "archived": false }, { "id": "311226010926", "properties": { "hs\_deal\_split\_percentage": "0.25", "hubspot\_owner\_id": "61891281" }, "createdAt": "2024-03-11T19:55:26.219Z", "updatedAt": "2024-03-11T19:55:26.219Z", "archived": false } \] }, { "id": "5315919905", "splits": \[ { "id": "57675010822", "properties": { "hs\_deal\_split\_percentage": "0.3333", "hubspot\_owner\_id": "81538190" }, "createdAt": "2021-06-16T21:04:09.264Z", "updatedAt": "2021-06-16T21:04:09.264Z", "archived": false }, { "id": "57675010821", "properties": { "hs\_deal\_split\_percentage": "0.3333", "hubspot\_owner\_id": "81426347" }, "createdAt": "2021-06-16T21:04:09.264Z", "updatedAt": "2021-06-16T21:04:09.264Z", "archived": false }, { "id": "57675010820", "properties": { "hs\_deal\_split\_percentage": "0.3334", "hubspot\_owner\_id": "60158084" }, "createdAt": "2021-06-16T21:04:09.264Z", "updatedAt": "2021-06-16T21:04:09.264Z", "archived": false } \] } \], "startedAt": "2024-03-11T19:56:42.555Z", "completedAt": "2024-03-11T19:56:42.596Z" }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/deal-splits#page-feedback)
--------------------------------------------------------------------------------------------

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