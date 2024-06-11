---
title: "API usage guidelines"
description: "Guidelines on using HubSpot's public APIs, including authentication and security measures, rate limits, error responses, service limits, and best practices for private and OAuth apps."
type: "guide"
tags:
- "HubSpot"
- "API"
- "Usage"
relationships:
- "#related_to [[OAuth protocol]]"
- "#part_of [[Public APIs]]"
- "#similar_to [[Private Apps]]"
founded: "N/A"
---

API usage guidelines
====================

HubSpot closely monitors usage of our public APIs to ensure a quality experience for every user. All app and integration developers must comply with the [HubSpot Acceptable Use Policy](https://legal.hubspot.com/acceptable-use?_ga=2.160640372.814749580.1584984850-500942594.1573763828) and [API Terms](https://legal.hubspot.com/developer-terms). While HubSpot reserves the right to change or deprecate the APIs over time, updates will always be provided in advance through the [Developer Changelog](/changelog?_ga=2.36526632.929165764.1583254459-500942594.1573763828).

Authentication and security
---------------------------

For optimal security, all apps must use HubSpot’s [OAuth protocol](https://developers.hubspot.com/docs-beta/working-with-oauth) directly, or use your app's access token if you're building a [private app](/docs/api/private-apps). Apps are responsible for storing time-to-live (TTL) data and refreshing user access tokens in accordance with this protocol. When an access token is generated, it will include an `expires_in` parameter indicating how long it can be used to make API calls before refreshing. `Unauthorized (401)` requests are not a valid indicator that a new access token must be retrieved.

Checking API usage[](https://developers.hubspot.com/docs/api/usage-details#checking-api-usage)
----------------------------------------------------------------------------------------------

### **Private apps**

To view API usage for a private app:

*   In your HubSpot account, click the **settings icon** in the main navigation bar.
*   In the left sidebar menu, navigate to **Integrations** \> **Private Apps**.
*   Click the **name** of the private app.
*   On the app details page, click the **Logs** tab.
*   Review the API calls listed in the table. You can also use the **search bar**, **filters**, and **date pickers** to further refine the displayed API calls.

![Screenshot 2023-08-31 at 5.28.03 PM](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/Screenshot%202023-08-31%20at%205.28.03%20PM.png?width=988&height=513&name=Screenshot%202023-08-31%20at%205.28.03%20PM.png)

Learn more about [checking API usage in private apps](/docs/api/private-apps#view-api-call-logs).

### **Public apps using OAuth**

To view API usage for a public app using OAuth:

*   In your developer account, navigate to **Apps** in the main navigation bar.
*   Click the **name** of the app.
*   In the left sidebar menu, navigate to **Monitoring**.
*   Use the **tabs** to view different types of requests being made to or from the app. While viewing these logs, you can click an **individual request** to view more information.

![6-request_details](https://developers.hubspot.com/hs-fs/hubfs/6-request_details.png?width=486&height=549&name=6-request_details.png)Learn more about [monitoring API usage for public apps](/docs/api/creating-an-app#monitor-app-behavior).

Rate Limits[](https://developers.hubspot.com/docs/api/usage-details#rate-limits)
--------------------------------------------------------------------------------

#### **Apps using OAuth**

For OAuth apps, each HubSpot account that installs your app is limited to 100 requests every 10 seconds. This excludes the [Search API](/docs/api/crm/search), as noted in the [Other Limits](#other-limits) section below. Limits related to the API Add-on don't apply.

#### **Private apps**

Each private app is subject to [HubSpot's API usage guidelines](/docs/api/usage-details). The number of calls your private app can make is based on your account subscription and whether you've purchased the API add-on:

|   | **Product Tier** | **Per 10 Seconds** | **Per Day** |
| --- | --- | --- | --- |
| Private Apps | 
(Any Hub)

Free and Starter

 | 100 / private app | 250,000 / account |
|   | 

(Any Hub)

Pro and Enterprise

 | 150 / private app | 500,000 / account |
| Private Apps with API Add-on | 

(Any Hub)

Free, Starter, Professional, and Enterprise

 | 200 / private app | 1,000,000 / account |

Other limits[](https://developers.hubspot.com/docs/api/usage-details#other-limits)
----------------------------------------------------------------------------------

*   You can create up to 100 apps per developer account.
*   You can create up to 20 private apps per HubSpot account.
*   You can create up to 1,000 webhook subscriptions per app.
*   You can create up to 25 CRM extension settings per app.
*   You can create up to 750 timeline event types per app.
*   You can create up to 500 properties per timeline event type.
*   The [Search API](/docs/api/crm/search) endpoints are rate limited to four requests per second per authentication token.
*   API requests that are exempt from daily or secondary limits will not be logged in HubSpot. If you want to store these exempted requests, you'll need to log these requests externally.

Service Limits[](https://developers.hubspot.com/docs/api/usage-details#service-limits)
--------------------------------------------------------------------------------------

Learn more about service limits and pricing [here](https://www.hubspot.com/pricing/service-limits?_ga=2.67496408.814749580.1584984850-500942594.1573763828).

Error Responses[](https://developers.hubspot.com/docs/api/usage-details#error-responses)
----------------------------------------------------------------------------------------

Any app or integration exceeding its rate limits will receive a `429` error response for all subsequent API calls. Requests resulting in an error response shouldn’t exceed 5% of your total daily requests. If you plan on listing your app in the [HubSpot App Marketplace](https://ecosystem.hubspot.com/marketplace/apps), it must stay under this 5% limit to be certified. 

The `429` response will have the following format: 

//Example { "status": "error", "message": "You have reached your daily limit.", "errorType": "RATE\_LIMIT", "correlationId": "c033cdaa-2c40-4a64-ae48-b4cec88dad24", "policyName": "DAILY", "requestId": "3d3e35b7-0dae-4b9f-a6e3-9c230cbcf8dd" }

The `message` and `policyName` will indicate which limit you hit (either daily or secondly).

The **daily** limit resets at midnight based on your [time zone setting](https://knowledge.hubspot.com/getting-started-with-hubspot-v2/how-to-set-your-time-zone-in-hubspot).

The following table details the rate limit headers included in the response of each API request to HubSpot, subject to the exceptions listed below the table.

| **Header** | **Description** |
| --- | --- |
| `X-HubSpot-RateLimit-Daily` | The number of API requests that are allowed per day. Note that this header is not included in the response to API requests authorized using [OAuth](/docs/api/working-with-oauth). |
| `X-HubSpot-RateLimit-Daily-Remaining` | The number of API requests still allowed for the current day. Note that this header is not included in the response to API requests authorized using [OAuth](/docs/api/working-with-oauth). |
| `X-HubSpot-RateLimit-Interval-Milliseconds` | The window of time that the `X-HubSpot-RateLimit-Max` and `X-HubSpot-RateLimit-Remaining` headers apply to.  
  
For example, a value of 10000 would be a window of 10 seconds. |
| `X-HubSpot-RateLimit-Max` | The number of requests allowed in the window specified in `X-HubSpot-RateLimit-Interval-Milliseconds`.  
  
For example, if this header had a value of 100, and the `X-HubSpot-RateLimit-Interval-Milliseconds` header was 10000, the enforced limit would be 100 requests per 10 seconds. |
| `X-HubSpot-RateLimit-Remaining` |  The number of API requests still allowed for the window specified in `X-HubSpot-RateLimit-Interval-Milliseconds` |

**Please note:**

*   The `X-HubSpot-RateLimit-Secondly` and `X-HubSpot-RateLimit-Secondly-Remaining` headers are still included and will still have accurate data, but the limit referenced by these headers is no longer enforced and these two headers should be considered deprecated.
*   Responses from the [search API endpoints](/docs/api/crm/search) will not include any of the rate limit headers listed above.

You can also check the number of calls used during the current day using [this endpoint](/docs/api/settings/account-information-api).

If you're running into the `TEN_SECONDLY_ROLLING` limit, you should throttle the requests that your app is making to stay under that limit. In addition to throttling the requests, or if you're running into the daily limit, check out the suggestions below.

If you find that you're still hitting the call limits after looking through these suggestions, please post on HubSpot's [developer forums](https://integrate.hubspot.com/?_ga=2.234851102.1802613489.1576611619-500942594.1573763828). You should include as many details as possible about the APIs you're using, how you're using them, and which limit you're hitting.

### Use batch APIs and cache results when possible[](https://developers.hubspot.com/docs/api/usage-details#use-batch-apis-and-cache-results-when-possible)

If your site or app uses data from HubSpot on each page load, that data should be cached and loaded from that cache instead of being requested from the HubSpot APIs each time. If you're making repeated calls to get settings from your account for a batch job (such as getting your object properties, owners, or settings for a form), those settings should also be cached when possible.

### Use webhooks to get updated data from HubSpot[](https://developers.hubspot.com/docs/api/usage-details#use-webhooks-to-get-updated-data-from-hubspot)

If you have a HubSpot Marketing Enterprise subscription, you can use webhook actions in workflows to have data for contact records sent to your system. Webhooks can be triggered as an action in any workflow, so you can use any workflow [starting conditions](https://knowledge.hubspot.com/workflows-user-guide-v2/how-to-choose-the-workflow-type-and-the-starting-condition-best-suited-for-your-goal) as the criteria to have contact data sent to your system. More details about using webhooks can be found [here](https://knowledge.hubspot.com/articles/kcs_article/workflows/how-do-i-use-webhooks-with-hubspot-workflows) and example webhooks data is [here](https://developers.hubspot.com/docs/methods/workflows/webhook_information). Webhook calls made via workflows do not count towards the API rate limit. 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/usage-details#page-feedback)
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