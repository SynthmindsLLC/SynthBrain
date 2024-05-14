Custom event completions
========================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/operations_icon.svg) Operations Hub
    *   Enterprise

Custom events are account-defined events that store event details in event properties. There are three types of custom events that you can create in HubSpot:

*   [Clicked element](https://knowledge.hubspot.com/analytics-tools/create-clicked-element-events) and [visited URL](https://knowledge.hubspot.com/analytics-tools/create-visited-url-events) events are custom events that the tracking code automatically populates with data. You can further customize these events by updating your tracking code with the [trackCustomEvent](https://developers.hubspot.com/docs/api/events/tracking-code#events-js-api) function. 

*   [Manually tracked events](https://knowledge.hubspot.com/analytics-tools/create-custom-behavioral-events) are custom events that are unique to your business that are not captured automatically by HubSpot or by an integration. You can manually send data to these events through this API.

Below, learn how to create a manually tracked custom event, send event data through the API, and to use event data once captured.

Define the event[](https://developers.hubspot.com/docs/api/analytics/events#define-the-event)
---------------------------------------------------------------------------------------------

To send event completion data to HubSpot, you first need to define the event itself, including its metadata, CRM object associations, and properties. You can define events using the [custom event definition API](/docs/api/events/custom-events), or if you have a Marketing Hub Enterprise subscription you can [create the event in HubSpot](https://knowledge.hubspot.com/analytics-tools/create-custom-behavioral-events). When creating the event, HubSpot will include a set of default event properties that you can use to store event data. You can also create additional properties for the event. These properties can be created or edited at any time. 

Once you’ve set up your event, you can send data to it through the API.

Send event data[](https://developers.hubspot.com/docs/api/analytics/events#send-event-data)
-------------------------------------------------------------------------------------------

To send event data to HubSpot, make a `POST` request to `https://api.hubspot.com/events/v3/send`. There is a limit of 30 million custom behavioral events that can be logged per month in your account.

In the request body, you'll need to include event information as well as a contact to associate the event completion with. The following fields are required when triggering a custom behavioral event:

*   **Identifier:** Either the contact ID, email, or [utk](/docs/api/events/tracking-code) of the contact associated with the event. The event completion needs to be associated with a HubSpot Object. The identifier that can be used depends on the `primaryObject` type associated with the custom event. For `CONTACT`, the identifier can be any of `objectId` (contact record ID), `email` (email associated with the contact) or `utk` (HubSpot User Token). For other objects (like `DEAL`, `TICKET`, `COMPANY` and `Custom Object`), only the HubSpot `objectId` is supported.
*   **Event name:** the internal name of the event, which can be found in HubSpot. Learn how to [find an event's internal name](https://knowledge.hubspot.com/analytics-tools/create-custom-behavioral-events#define-the-api-call). ![custom-event-internal-name](https://developers.hubspot.com/hs-fs/hubfs/Imported%20sitepage%20images/custom-event-internal-name.png?width=1213&name=custom-event-internal-name.png)

### Send property data

To include specific properties in the request body, use the following format:

"properties": { "property1": "string", "property2": "string", "property3": "string" }

The values you send will depend on the type of event property. Most of the default event properties are single-line text (string). However, you can create custom properties of any type for each event. Review the table below when formatting property values.

Use this table to describe parameters / fields
| Property type | Description |
| --- | --- |
| 
`enumeration`

 | 

A string representing a set of options. When sending multiple values, separate them with a semicolon. In HubSpot, this type corresponds to dropdown select, radio select, and multiple checkbox properties.

 |
| 

`date`

 | 

A timestamp in the form of epoch milliseconds or ISO8601. In HubSpot, this type corresponds to date picker properties.

 |
| 

`string`

 | 

A plain text string limited to 65,536 characters. In HubSpot, this type corresponds to single-line and multi-line text properties.

 |
| 

`number`

 | 

A number value containing numeric digits and at most one decimal. In HubSpot, this type corresponds to number and calculation properties.

 |

To view an event's available properties:

*   In your HubSpot account, navigate to **Reporting** > **Data Management** > **Custom events**.
*   Click the **name** of the event.
*   Click the **Properties** tab.
*   In the properties table, view the property type under the name of the property. ![custom-event-properties-table](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-event-properties-table.png?width=457&name=custom-event-properties-table.png)  

### Set the time of an event

To specify the time of event completion, you can include a timestamp in an occurredAt field in your request. By default, if you do not include this field, HubSpot will set the completion time as the time of sending the request. The occurredAt field can be helpful if you want to store a different timestamp than when the API itself fired. For example, you have an event _Attended Partner Webinar_. The webinar took place two weeks ago, but you only received the data today. You could set the occuredAt property to include a timestamp from two weeks ago, which will set those dates in HubSpot accordingly.

### Example request body

Below is an example request body for a login event which sends city, country, page, and interaction source data to HubSpot. The contact that completed the event is represented by the objectId field. For more details on sending event data, click the Endpoints tab at the top of this article.

// POST to https://api/hubspot.com/events/v3/send { "eventName": "pe1234567\_login\_event", "properties": { "hs\_city": "Cambridge", "hs\_country": "United States", "hs\_page\_id": "53005768010", "hs\_page\_content\_type": "LANDING\_PAGE", "hs\_touchpoint\_source":"DIRECT\_TRAFFIC" }, "objectType": "contacts", "objectId": "608051" }

Exceeding any of the following limits will result in a failed request:

*   The property label and internal name are limited to 50 characters.
*   URL and referrer properties can receive up to 1024 characters, while all other properties can receive up to 256 characters.
*   Each event completion can contain data for up to 50 properties.
*   Property internal names must start with a letter and contain only lowercase letters a-z, numbers 0-9, and underscores.
*   Properties with the same internal name after lowercasing are considered duplicates, and only one of the properties will be used on completion. HubSpot will sort in ascending lexicographical order and keep the last property seen among the first 50 properties.
*   There is a limit of 500 unique event definitions per account.
*   There is a limit of 30 million event completions per month. 

Retrieve event data[](https://developers.hubspot.com/docs/api/analytics/events#retrieve-event-data)
---------------------------------------------------------------------------------------------------

To [retrieve a contact's event data](/docs/api/events/web-analytics), make a `GET` request to `/events/v3/events/eventType={EVENT_NAME}&objectType=contact&objectId={CONTACT_ID}`. 

The above request includes:

*   eventType: the internal name of the event.
*   objectType: the record's object type.
*   objectId: the contact's ID.

Attribution reporting[](https://developers.hubspot.com/docs/api/analytics/events#attribution-reporting)
-------------------------------------------------------------------------------------------------------

JavaScript events such as [clicked element](https://knowledge.hubspot.com/analytics-tools/create-clicked-element-events) and [visited URL](https://knowledge.hubspot.com/analytics-tools/create-visited-url-events) events are automatically populated with asset type and interaction data for attribution reporting. To include the same data for manually tracked events, you'll need to manually include the data in the request body using event properties. Learn more about [analyzing custom events](https://knowledge.hubspot.com/analytics-tools/analyze-custom-behavioral-events).

Below, learn about the available values for asset types and interaction sources, along with example requests. 

### Asset type[](https://developers.hubspot.com/docs/api/analytics/events#asset-type)

To attribute a specific asset type to a custom behavioral event request, include the `hs_page_content_type` property in the request body. For example:

// example request body { "eventName": "pe1234567\_manually\_tracked\_event", "properties": { "hs\_page\_id": "53005768010", "hs\_page\_content\_type": "LANDING\_PAGE" }, "objectType": "contacts", "objectId": "6091051" }

You can also use the **hs\_asset\_type** property. If both **hs\_page\_content\_type** and **hs\_asset\_type** are included in one request, **hs\_page\_content\_type** will override the **hs\_asset\_type** value.

HubSpot's standard content types, such as landing pages and blog posts, can be represented with the following values:

Use this table to describe parameters / fields
| Value | Description |
| --- | --- |
| 
`STANDARD_PAGE`

 | 

An interaction with a website page.

 |
| 

`LANDING_PAGE`

 | 

An interaction with a landing page.

 |
| 

`BLOG_POST`

 | 

An interaction with a blog post.

 |
| 

`KNOWLEDGE_ARTICLE`

 | 

An interaction with a knowledge base article.

 |

For all other types of assets, use the following values:

Use this table to describe parameters / fields
| Value | Description |
| --- | --- |
| 
`AD`

 | 

An interaction with an ad, such as a Facebook or Google ad.

 |
| 

`CALL`

 | 

An interaction with a call.

 |
| 

`CONTACT_IMPORT`

 | 

An interaction via a contact import.

 |
| 

`CONVERSATION`

 | 

An interaction related to a HubSpot conversation.

 |
| 

`CUSTOM_BEHAVIORAL_EVENT_NAME`

 | 

The internal name of a custom event, such as `pe123456_manually_tracked_event`.

 |
| 

`EMAIL`

 | 

An interaction with an email.

 |
| 

`EXTERNAL_PAGE`

 | 

An interaction with an external page.

 |
| 

`INTEGRATIONS`

 | 

An interaction via an integration.

 |
| 

`MARKETING_EVENT`

 | 

An interaction with a [marketing event](/docs/api/marketing/marketing-events).

 |
| 

`MEDIA_BRIDGE`

 | 

An interaction via the [media bridge](/docs/api/media-bridge/).

 |
| 

`MEETING`

 | 

An interaction with a meeting.

 |
| 

`SALES_EMAIL`

 | 

An interaction with a 1:1 sales email.

 |
| 

`SEQUENCE`

 | 

An interaction with a sequence.

 |
| 

`SOCIAL_POST`

 | 

An interaction with a social media post.

 |
| 

`OTHER`

 | 

An interaction with an asset not in one of the above categories.

 |

### Asset title[](https://developers.hubspot.com/docs/api/analytics/events#asset-title)

To attribute a custom event to an asset, include the `hs_page_title` or `hs_asset_title` property in your request with the name of the asset formatted as a string. For example:

`hs_page_title:`

JSON

Copy all

    // example request body
    {
      "eventName": "pe1234567_manually_tracked_event",
      "properties": {
        "hs_page_title": "Sweepstakes Sign Up",
        "hs_page_content_type": "LANDING_PAGE"
      },
     "objectType": "contacts",
     "objectId": "6091051"
    }

### Interaction sources[](https://developers.hubspot.com/docs/api/analytics/events#interaction-sources)

To attribute a custom behavioral event to a specific source, include the `hs_touchpoint_source` property in your request with one of the following values:

Use this table to describe parameters / fields
| Value | Description |
| --- | --- |
| 
`CONVERSATION`

 | 

The interaction source is a conversation.

 |
| 

`DIRECT_TRAFFIC`

 | 

The interaction source is direct traffic.

 |
| 

`EMAIL_MARKETING`

 | 

The interaction source is a marketing email.

 |
| 

`HUBSPOT_CRM`

 | 

The interaction source is the HubSpot CRM.

 |
| 

`INTEGRATION`

 | 

The interaction source is an integration.

 |
| 

`MARKETING_EVENT`

 | 

The interaction source is a [marketing event](/docs/api/marketing/marketing-events).

 |
| 

`OFFLINE`

 | 

The interaction source is offline.

 |
| 

`ORGANIC_SEARCH`

 | 

The interaction source is organic search.

 |
| 

`OTHER_CAMPAIGNS`

 | 

The interaction source is from an uncategorized campaign.

 |
| 

`PAID_SEARCH`

 | 

The interaction source is a paid search ad.

 |
| 

`PAID_SOCIAL`

 | 

The interaction source is a paid social ad.

 |
| 

`REFERRALS`

 | 

The interaction source is a referral.

 |
| 

`SALES`

 | 

The interaction source is sales.

 |
| 

`SOCIAL_MEDIA`

 | 

The interaction source is social media (not a paid social ad).

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/analytics/events#page-feedback)
---------------------------------------------------------------------------------------------

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