---
title: "Payments API Overview"
description: "Use the payments API to fetch information about an account's payments, which is a read-only API and cannot be used for creating new or managing existing payments. This includes retrieving all refunded payments in an account. Requirements include setting up HubSpot payments or Stripe payment processing."
type: "group"
tags:
- "Payment"
- "API"
- "HubSpot"
relationships:
- "#founded_by [[HubSpot]]"
- "#part_of [[Commerce API]]"
- "#related_to [[Stripe payment processing]]"
founded: "2014-05-08"
---

Payments
========

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the payments API to fetch information about an account's [payments](https://knowledge.hubspot.com/payments/manage-payments). This is a read-only API, so it cannot be used for creating new or managing existing payments. 

For example, use this API to [fetch all refunded payments](#search-for-payments-by-properties) in an account.

Requirements[](https://developers.hubspot.com/docs/api/commerce/payments#requirements)
--------------------------------------------------------------------------------------

To use this API, the account must be set up to collect payments through either [HubSpot payments](https://knowledge.hubspot.com/payments/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payments/connect-your-stripe-account-as-a-payment-processor-in-hubspot).

Retrieve payments[](https://developers.hubspot.com/docs/api/commerce/payments#retrieve-payments)
------------------------------------------------------------------------------------------------

Depending on the information you need, there are a few ways to retrieve payments:

*   To retrieve all payments, make a `GET` request to `crm/v3/objects/commerce_payments`.
*   To retrieve a payment, make a `GET` request to the above URL and specify an payment ID. For example: `crm/v3/objects/commerce_payments/44446244097`.
*   To retrieve payments that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. See an example of using the [search endpoint below](#search-for-invoices-by-filter-criteria).

The response will include a few default properties, including the create date, last modified date.

// Example response { "id":"44446244097", "properties":{ "hs\_createdate":"2023-03-08T14:54:17.333Z", "hs\_lastmodifieddate":"2024-03-01T22:33:09.011Z", "hs\_object\_id":"44446244097" }, "createdAt":"2023-03-08T14:54:17.333Z", "updatedAt":"2024-03-01T22:33:09.011Z", "archived":false }

### Properties[](https://developers.hubspot.com/docs/api/commerce/payments#properties)

To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below:

`crm/v3/objects/commerce_payments?properties=hs_customer_email,hs_latest_status`

// Example response { "id":"40744976671", "properties":{ "hs\_createdate":"2022-09-02T15:03:40.828Z", "hs\_customer\_email": "name@emailaddress.com", "hs\_lastmodifieddate":"2024-02-27T15:03:53.620Z", "hs\_object\_id":"40744976671", "hs\_latest\_status":"succeeded" }, "createdAt":"2022-09-02T15:03:40.828Z", "updatedAt":"2024-02-27T15:03:53.620Z", "archived":false }

To view all available payment properties, make a `GET` request to `crm/v3/properties/commerce_payments`. Learn more about using the [properties API](/docs/api/crm/properties).

Below are some common payment properties that you may want to query. 

| Property name | Label in UI | Description |
| --- | --- | --- |
| `hs_latest_status` | 
[Status](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#payment-properties:~:text=created%20the%20payment.-,Status,-%3A%C2%A0the%20current)

 | 

The current status of the payment. Values include:

*   `succeeded`
*   `refunded`
*   `processing`
*   `failed`

 |
| `hs_initial_amount` | 

[Gross amount](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#payment-properties:~:text=made%20the%20payment.-,Gross%20amount,-%3A%C2%A0the%20total)

 | 

The total amount that the buyer was charged.

 |
| `hs_customer_email` | 

[Customer](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#payment-properties:~:text=be%20in%20USD.-,Customer,-%3A%C2%A0the%20email)

 | 

The buyer's email address.

 |
| `hs_initiated_date` | 

[Payment date](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#payment-properties:~:text=can%27t%20be%20changed.-,Payment%20date,-%3A%C2%A0the%20date)

 | 

The date that the payment was created.

 |
| `hs_payment_id` | 

[Payment ID](https://knowledge.hubspot.com/payments/hubspots-payments-and-subscriptions-properties#payment-properties:~:text=is%20updated%20automatically.-,Payment%20ID,-%3A%C2%A0the%20unique)

 | 

The payment's unique ID.

 |

### Search for payments by properties[](https://developers.hubspot.com/docs/api/commerce/payments#search-for-payments-by-properties)

You can use the search endpoint to retrieve payments that meet a specific set of [filter criteria](/docs/api/crm/search#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body.

For example, to search for all refunded payments, you would make a `POST` request to `crm/v3/objects/commerce_payments/search` with the following request body:

// Example search request body { "filterGroups": \[ { "filters": \[ { "propertyName": "hs\_latest\_status", "value": "refunded", "operator": "EQ" } \] } \], "properties": \["hs\_latest\_status","hs\_customer\_email"\] }

Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

Associations[](https://developers.hubspot.com/docs/api/commerce/payments#associations)
--------------------------------------------------------------------------------------

While you cannot set associations using this API, you can retrieve association information by making a GET request to the following URL:

`crm/v3/objects/commerce_payments/{paymentId}/associations/{associatedObjectName}`

Associated objects can include **[contacts](https://developers.hubspot.com/docs/api/crm/contacts)**, **[companies](https://developers.hubspot.com/docs/api/crm/companies)**, **[deals](https://developers.hubspot.com/docs/api/crm/deals)**, [invoices](/docs/api/commerce/invoices), [quotes](/docs/api/crm/quotes), **[line items](https://developers.hubspot.com/docs/api/crm/line-items)**, [subscriptions](/docs/api/commerce/subscriptions), **[discounts](https://developers.hubspot.com/docs/api/crm/discounts)**, **[fees](https://developers.hubspot.com/docs/api/crm/fees)**, and **[taxes](https://developers.hubspot.com/docs/api/crm/taxes)**. These associates are based on the associations set on the invoice, payment link, or quote used for transaction. To manage these associations, you can [update the payment in HubSpot](https://knowledge.hubspot.com/payments/manage-payments#view-payment-records).

Below is an example of how you might use this API combined with another API to get a specific set of association information.

**Please note:** when retrieving line items from different objects created in HubSpot, you should expect to receive different IDs. This is because line items should only be associated with one object, which HubSpot handles automatically by creating copies of line items rather than using the same line item across multiple objects.

### Retrieving a payment with associated contact[](https://developers.hubspot.com/docs/api/commerce/payments#retrieving-a-payment-with-associated-contact)

To retrieve a payment and contact associated with it, make a `GET` request to:

`crm/v3/objects/commerce_payments/{paymentId}/associations/contact`

This will return the IDs of the currently associated contact, along with meta information about the association type.

// Example response { "results":\[ { "id":"301", "type":"commerce\_payment\_to\_contact" } \] }

You can then use the returned IDs to request more information about the line items through the [contacts API](/docs/api/crm/contacts). For example, you could retrieve the contact using its ID by making a `GET` request to `crm/v3/objects/contacts/{contactId}`

// Example response { "id":"301", "properties":{ "createdate":"2022-09-27T13:13:31.004Z", "email":"tom.bombadil@oldforest.com", "firstname":"Tom", "hs\_object\_id":"301", "lastmodifieddate":"2023-11- 07T17:14:00.841Z", "lastname":"Bombadil" }, "createdAt":"2022-09-27T13:13:31.004Z", "updatedAt":"2023-11-07T17:14:00.841Z", "archived":false }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/commerce/payments#page-feedback)
----------------------------------------------------------------------------------------------

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