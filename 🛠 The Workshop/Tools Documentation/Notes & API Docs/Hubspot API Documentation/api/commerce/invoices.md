---
title: "Invoices API Overview"
description: "Use the invoices API to fetch information about an account's invoices, including retrieving all open invoices and specific properties or associations. This is a read-only API that cannot be used for creating new or managing existing invoices."
type: "group"
tags:
- "Invoice"
- "API"
- "HubSpot"
relationships:
- "#founded_by [[HubSpot]]"
- "#related_to [[Commerce API]]"
createdAt: "YYYY-MM-DD"
updatedAt: "YYYY-MM-DD"
---

Invoices
========

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the invoices API to fetch information about an account's [invoices](https://knowledge.hubspot.com/invoices/create-and-manage-invoices). This is a read-only API, so it cannot be used for creating new or managing existing invoices. 

For example, use this API to [fetch all currently open invoices](#search-for-invoices-by-properties).

Retrieve invoices[](https://developers.hubspot.com/docs/api/commerce/invoices#retrieve-invoices)
------------------------------------------------------------------------------------------------

Depending on the information you need, there are a few ways to retrieve invoices:

*   To retrieve all invoices, make a `GET` request to `crm/v3/objects/invoices`.
*   To retrieve a specific invoice, make a `GET` request to the above URL and specify an invoice ID. For example: `crm/v3/objects/invoices/44446244097`.
*   To retrieve invoices that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. See an example of using the [search endpoint below](#search-for-invoices-by-filter-criteria).

The response will include a few default properties, including the create date, last modified date.

// Example response { "id":"44446244097", "properties":{ "hs\_createdate":"2023-03-08T14:54:17.333Z", "hs\_lastmodifieddate":"2024-03-01T22:33:09.011Z", "hs\_object\_id":"44446244097" }, "createdAt":"2023-03-08T14:54:17.333Z", "updatedAt":"2024-03-01T22:33:09.011Z", "archived":false }

### Properties[](https://developers.hubspot.com/docs/api/commerce/invoices#properties)

To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below:

`crm/v3/objects/invoices?properties=hs_invoice_status,hs_amount_billed`

// Example response { "id":"44446244097", "properties":{ "hs\_amount\_billed":"20.00", "hs\_createdate":"2023-03-08T14:54:17.333Z", "hs\_invoice\_status":"open", "hs\_lastmodifieddate":"2024-03-01T22:33:09.011Z", "hs\_object\_id":"44446244097" }, "createdAt":"2023-03-08T14:54:17.333Z", "updatedAt":"2024-03-01T22:33:09.011Z", "archived":false }

To view all available invoice properties, make a `GET` request to `crm/v3/properties/invoices`. Learn more about using the [properties API](/docs/api/crm/properties).

Below are some common invoice properties that you may want to query. 

| Property name | Label in UI | Description |
| --- | --- | --- |
| `hs_invoice_status` | 
[Invoice status](https://knowledge.hubspot.com/invoices/hubspots-default-invoice-properties#:~:text=Legacy%20Quickbooks%20integration.-,Invoice%20Status,-%3A%20the%20current)

 | 

The current status of the invoice. Values include:

*   `draft`
*   `open`
*   `paid`
*   `voided`

 |
| `hs_amount_billed` | 

[Amount billed](https://knowledge.hubspot.com/invoices/hubspots-default-invoice-properties#:~:text=creating%20the%20invoice.-,Amount%20billed,-%3A%20the%20total)

 | 

The amount billed on the invoice.

 |
| `hs_balance_due` | 

[Balance due](https://knowledge.hubspot.com/invoices/hubspots-default-invoice-properties#:~:text=on%20the%20invoice.-,Balance%20due,-%3A%20the%20current)

 | 

The balance due on the invoice.

 |
| `hs_due_date` | 

[Due date](https://knowledge.hubspot.com/invoices/hubspots-default-invoice-properties#:~:text=USD%20is%20supported.-,Due%20date,-%3A%20the%20invoice%E2%80%99s)

 | 

The date the invoice is due.

 |
| `hs_number` | 

[Number](https://knowledge.hubspot.com/invoices/hubspots-default-invoice-properties#:~:text=creating%20the%20invoice.-,Number,-%3A%20the%20unique)

 | 

The invoice number (e.g., `INV_1003`)

 |

### Search for invoices by properties[](https://developers.hubspot.com/docs/api/commerce/invoices#search-for-invoices-by-properties)

You can use the search [endpoint](/docs/api/crm/search) to retrieve invoices that meet a specific set of [filter criteria](/docs/api/crm/search#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body.

For example, to search for all open invoices, you would make a `POST` request to `crm/v3/objects/invoices/search` with the following request body:

// Example search request body { "filterGroups": \[ { "filters": \[ { "propertyName": "hs\_invoice\_status", "value" : "open", "operator": "EQ" } \] } \], "properties": \[ "hs\_invoice\_status", "hs\_due\_date"\] }

Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

Associations[](https://developers.hubspot.com/docs/api/commerce/invoices#associations)
--------------------------------------------------------------------------------------

While you cannot set associations using this API, you can retrieve association information by making a GET request to the following URL:

`crm/v3/objects/invoice/{invoiceId}/associations/{associatedObjectName}`

Associated objects can include **[contacts](https://developers.hubspot.com/docs/api/crm/contacts)**, **[companies](https://developers.hubspot.com/docs/api/crm/companies)**, **[deals](https://developers.hubspot.com/docs/api/crm/deals)**, **[line items](https://developers.hubspot.com/docs/api/crm/line-items)**, **[discounts](https://developers.hubspot.com/docs/api/crm/discounts)**, **[fees](https://developers.hubspot.com/docs/api/crm/fees)**, and **[taxes](https://developers.hubspot.com/docs/api/crm/taxes)**. To create associations between an invoice and these objects, you can [update the invoice in HubSpot](https://knowledge.hubspot.com/invoices/create-and-manage-invoices).

Below is an example of how you might use this API combined with another API to get a specific set of association information.

**Please note:** line items belong to one single parent object. For example, if retrieving line items from an invoice, the line item ID’s will be different to those on a deal, or a quote.

### Retrieving an invoice with associated line items[](https://developers.hubspot.com/docs/api/commerce/invoices#retrieving-an-invoice-with-associated-line-items)

To retrieve an invoice and the line items associated with it, make a `GET` request to:

`crm/v3/objects/invoice/{invoiceId}/associations/line_items`

This will return the IDs of the currently associated line items, along with meta information about the association type.

// Example response { "results":\[ { "id":"1526712436", "type":"invoice\_to\_line\_item" }, { "id":"1526712437", "type":"invoice\_to\_line\_item" } \] }

You can then use the returned IDs to request more information about the line items through the [line items API](/docs/api/crm/line-items). For example, you could batch retrieve line items by ID by making a `POST` request to the following URL with the request body below:

`crm/v3/objects/line_items/batch/read`

// Example request body { "inputs": \[ {"id": "1526712436"}, {"id": "1526712437"} \], "properties": \["name", "amount"\] }

The response would be formatted as follows:

// Example response { "status":"COMPLETE", "results":\[ { "id":"1359205183", "properties":{ "amount":"123.00", "createdate":"2023-04-26T14:52:35.885Z" "hs\_lastmodifieddate":"2023-04-26T14:52:35.885Z", "hs\_object\_id":"1359205183", "name":"itemname" }, "createdAt":"2023-04-26T14:52:35.885Z", "updatedAt":"2023-04-26T14:52:35.885Z", "archived":false } \], "startedAt":"2024-03-11T20:09:44.151Z", "completedAt":"2024-03-11T20:09:44.195Z" }

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/commerce/invoices#page-feedback)
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