Subscriptions
=============

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the subscriptions API to fetch information about an account's [commerce subscriptions](https://knowledge.hubspot.com/payments/manage-subscriptions-for-recurring-payments). This is a read-only API, so it cannot be used for creating new or managing existing subscriptions. If you're looking to manage marketing email subscriptions instead, check out the [subscription preferences API](/docs/api/marketing-api/subscriptions-preferences).

For example, use this API to [fetch all currently active subscriptions](#search-for-subscriptions-by-properties).

Requirements[](https://developers.hubspot.com/docs/api/commerce/subscriptions#requirements)
-------------------------------------------------------------------------------------------

To use this API, the account must be set up to collect payments through either [HubSpot payments](https://knowledge.hubspot.com/payments/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payments/connect-your-stripe-account-as-a-payment-processor-in-hubspot).

Retrieve subscriptions[](https://developers.hubspot.com/docs/api/commerce/subscriptions#retrieve-subscriptions)
---------------------------------------------------------------------------------------------------------------

Depending on the information you need, there are a few ways to retrieve subscriptions:

*   To retrieve all subscriptions, make a `GET` request to `crm/v3/objects/subscriptions`.
*   To retrieve a specific subscription, make a `GET` request to the above URL and specify a subscription ID. For example: `crm/v3/objects/subscriptions/41112146008`.
*   To retrieve subscriptions that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. See an example of using the [search endpoint below](#search-for-invoices-by-filter-criteria).

The response will include a few default properties, including the create date, last modified date.

// Example response { "id":"41112146008", "properties":{ "hs\_createdate":"2023-03-08T14:54:17.333Z", "hs\_lastmodifieddate":"2024-03-01T22:33:09.011Z", "hs\_object\_id":"44446244097" }, "createdAt":"2023-03-08T14:54:17.333Z", "updatedAt":"2024-03-01T22:33:09.011Z", "archived":false }

### Properties[](https://developers.hubspot.com/docs/api/commerce/subscriptions#properties)

To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below:

`crm/v3/objects/subscriptions?properties=hs_status,hs_last_payment_amount`

// Example response { "id":"41112146008", "properties":{ "hs\_createdate":"2022-09-02T15:03:40.828Z", "hs\_last\_payment\_amount":"200.00", "hs\_lastmodifieddate":"2024-02-27T15:03:53.620Z", "hs\_object\_id":"41112146008", "hs\_status":"active" }, "createdAt":"2022-09-02T15:03:40.828Z", "updatedAt":"2024-02-27T15:03:53.620Z", "archived":false }

To view all available subscription properties, make a `GET` request to `crm/v3/properties/subscriptions`. Learn more about using the [properties API](/docs/api/crm/properties).

Below are some common subscription properties that you may want to query. 

| Property name | Label in UI | Description |
| --- | --- | --- |
| `hs_status` | 
[Status](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=the%20status%20of%20the%20subscription)

 | 

The current status of the subscription. Values include:

*   `active`
*   `past_due`
*   `canceled`
*   `expired`
*   `scheduled`

 |
| `hs_recurring_billing_start_date` | 

[Start date](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=for%20the%20subscription.-,Start%20date%3A,-the%20date%20the)

 | 

The date that the subscription is scheduled to start.

 |
| `hs_last_payment_amount` | 

[Last payment amount](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=is%20updated%20automatically.-,Last%20payment%20amount,-%3A%C2%A0the%20amount)

 | 

The amount that was charged during the most recent billing period.

 |
| `hs_next_payment_amount` | 

[Next payment amount](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=of%20the%20subscription.-,Next%20payment%20amount,-%3A%20the%20amount)

 | 

The amount that will be charged at the start of the next billing period.

 |
| `hs_next_payment_due_date` | 

[Next payment due date](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#subscription-properties:~:text=Next%20payment%20due%20date)

 | 

The date that the next payment is due.

 |

### Search for subscriptions by properties[](https://developers.hubspot.com/docs/api/commerce/subscriptions#search-for-subscriptions-by-properties)

You can use the search endpoint to retrieve subscriptions that meet a specific set of [filter criteria](/docs/api/crm/search#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body.

For example, to search for all currently active subscriptions, you would make a `POST` request to `crm/v3/objects/subscriptions/search` with the following request body:

// Example search request body { "filterGroups": \[ { "filters": \[ { "propertyName": "hs\_status", "value" : "active", "operator": "EQ" } \] } \], "properties":\["hs\_status","hs\_last\_payment\_amount"\] }

Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

Associations[](https://developers.hubspot.com/docs/api/commerce/subscriptions#associations)
-------------------------------------------------------------------------------------------

While you cannot set associations using this API, you can retrieve association information by making a GET request to the following URL:

`crm/v3/objects/subscriptions/{subscriptionId}/associations/{associatedObjectName}`

Associated objects can include **[contacts](https://developers.hubspot.com/docs/api/crm/contacts)**, **[companies](https://developers.hubspot.com/docs/api/crm/companies)**, **[deals](https://developers.hubspot.com/docs/api/crm/deals)**, [quotes](/docs/api/crm/quotes), **[line items](https://developers.hubspot.com/docs/api/crm/line-items)**, [payments](/docs/api/commerce/payments), **[discounts](https://developers.hubspot.com/docs/api/crm/discounts)**, **[fees](https://developers.hubspot.com/docs/api/crm/fees)**, and **[taxes](https://developers.hubspot.com/docs/api/crm/taxes)**. These associations are typically set by the payment link or quote associated with the initial subscription payment. To manage these associations, you can [update the subscription in HubSpot](https://knowledge.hubspot.com/payments/manage-subscriptions-for-recurring-payments#edit-a-subscription).[](https://knowledge.hubspot.com/invoices/create-and-manage-invoices) 

Below is an example of how you might use this API combined with another API to get a specific set of association information.

**Please note:** line items belong to one single parent object. For example, if retrieving line items from a subscription, the line item ID’s will be different to those on a deal, or a quote.

### Retrieving a subscription with associated line items[](https://developers.hubspot.com/docs/api/commerce/subscriptions#retrieving-a-subscription-with-associated-line-items)

To retrieve a subscription and the line items associated with it, make a `GET` request to:

`crm/v3/objects/subscription/{subscriptionId}/associations/line_items`

This will return the IDs of the currently associated line items, along with meta information about the association type.

// Example response { "results":\[ { "id":"1459694380", "type":"subscription\_to\_line\_item" }, { "id":"1459694381", "type":"subscription\_to\_line\_item" } \] }

You can then use the returned IDs to request more information about the line items through the [line items API](/docs/api/crm/line-items). For example, you could batch retrieve line items by ID with the following `POST` request:

`crm/v3/objects/line_items/batch/read`

// Example request body { "inputs": \[ {"id": "1459694380"}, {"id": "1459694381"} \], "properties": \["name", "amount"\] }

The response would be formatted as follows:

// Example response { "status":"COMPLETE", "results":\[ { "id":"1459694381", "properties":{ "amount":"100.00", "createdate":"2023-11-08T18:23:06.361Z", "hs\_lastmodifieddate":"2023-11-08T18:23:06.361Z", "hs\_object\_id":"1459694381", "name":"Recurring line item 2" }, "createdAt":"2023-11-08T18:23:06.361Z", "updatedAt":"2023-11-08T18:23:06.361Z", "archived":false }, { "id":"1459694380", "properties":{ "amount":"100.00", "createdate":"2023-11-08T18:23:06.361Z", "hs\_lastmodifieddate":"2023-11-08T18:23:06.361Z", "hs\_object\_id":"1459694380", "name":"Recurring line item 1" }, "createdAt":"2023-11-08T18:23:06.361Z", "updatedAt":"2023-11-08T18:23:06.361Z", "archived":false } \], "startedAt":"2024-03-14T15:43:53.179Z", "completedAt":"2024-03-14T15:43:53.186Z" }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/commerce/subscriptions#page-feedback)
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