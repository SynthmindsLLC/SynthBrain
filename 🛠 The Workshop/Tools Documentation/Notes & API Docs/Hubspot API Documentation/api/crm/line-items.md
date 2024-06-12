---
title: "Line Items in HubSpot CRM API"
description: "Individual instances of products attached to deals, quotes, etc., managed through the line items endpoints for data syncing and customization."
type: "group"
tags:
- "HubSpot"
- "CRM"
- "API"
- "Line_Items"
relationships:
- "#part_of [[Sales Operations]]"
- "#associated_with [[Deals]], [[Quotes]], [[Invoices]], [[Payment Links]], [[Subscriptions]]"
founded: "2014-08-01"
---

Line Items
==========

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, line items are individual instances of [products](/docs-beta/crm/products). When a product is attached to a deal, it becomes a line item. You can create line items that are unique to an individual quote, but they will not be added to your product library. The line items endpoints allow you to manage this data and sync it between HubSpot and other systems.

**Example use case:** when creating a set of [quotes](/docs/api/crm/quotes) for sales reps to send to potential buyers, you can use this API to create standalone line items per quote, as well as line items that are attached to existing products.

Create a line item[](https://developers.hubspot.com/docs/api/crm/line-items#create-a-line-item)
-----------------------------------------------------------------------------------------------

To create a line item, make a `POST` request to `/crm/v3/objects/line_items`. In the post body, include the line item's details, such as name, quantity, and price.

To create a line item based on an existing product (created through the [products API](/docs/api/crm/products) or [in HubSpot](https://knowledge.hubspot.com/products/how-do-i-use-products)), include `hs_product_id` in the post body. 

You can also associate the line item with deals, quotes, invoices, payment links or subscriptions, by including an `associations` array in the post body. For example, the post body below would create a line item named "New standalone line item" that's associated with a deal (ID: `12345`).

// POST request to https://api.hubapi.com/crm/v3/objects/line\_item { "properties": { "price": 10, "quantity": 1, "name": "New standalone line item" }, "associations": \[ { "to": { "id": 12345 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 20 } \]

**Please note:** 

*   Line items belong to one single parent object. If associating objects, line items should be individual to each object. For example, if you're creating a deal and a quote, you should create one set of line items for the deal, and another set for the quote. This will help streamline CRM data across objects and prevent unexpected data loss when needing to modify line items (e.g., deleting a quote will delete the quote's line items, and if those line items are associated with a deal, the deals line items will also be deleted).
*   The `price` specified within the `properties` field cannot be negative.
*   The line items _Term_ property (`hs_recurring_billing_period`) accepts [ISO-8601 period formats](https://docs.oracle.com/javase/8/docs/api/java/time/Period.html#:~:text=exceeds%20an%20int-,parse,-public%20static%C2%A0) of PnYnMnD and PnW.

Retrieve a line item[](https://developers.hubspot.com/docs/api/crm/line-items#retrieve-a-line-item)
---------------------------------------------------------------------------------------------------

You can retrieve line items individually or in bulk.

*   To retrieve a specific line item, make a `GET` request to `/crm/v3/objects/line_items/{lineItemId}` where `lineItemId` is the ID of the line item.
*   To retrieve all line items, make a `GET` request to `/crm/v3/objects/line_items`. 

In the request URL, you can include the following parameters:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.

 |
| 

`propertiesWithHistory`

 | 

A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.

 |

Update a line item[](https://developers.hubspot.com/docs/api/crm/line-items#update-a-line-item)
-----------------------------------------------------------------------------------------------

To update a line item, make a `PATCH` request to `/crm/v3/objects/line_items/{lineItemId}`, where `lineItemId` is the ID of the line item.

In the post body, include the property values that you want to update. You cannot update associations through this method. Instead you'll need to use the [associations API](/docs/api/crm/associations).

For example, your request body might look similar to the following:

// PATCH request to https://api.hubapi.com/crm/v3/objects/line\_item/{lineItemId} { "properties": { "price": 25, "quantity": 3, "name": "Updated line item" }

Delete a line item[](https://developers.hubspot.com/docs/api/crm/line-items#delete-a-line-item)
-----------------------------------------------------------------------------------------------

To delete a line item, make a `DELETE` request to `/crm/v3/objects/line_items/{lineItemId}`, where `lineItemId` is the ID of the line item.

Line item properties[](https://developers.hubspot.com/docs/api/crm/line-items#line-item-properties)
---------------------------------------------------------------------------------------------------

When managing your line item data, you may want to use some of the common properties in the table below. To get all line item properties, make a `GET` request to `/crm/v3/properties/line_item`. Learn more about using the [properties API](/docs/api/crm/properties).

| Property name | Label in UI | Description |
| --- | --- | --- |
| `name` | Name | The name of the line item. |
| `description` | Description | Full description of the product |
| `hs_sku` | SKU | Unique product identifier |
| `hs_billing_period_start_date` | Billing start date | Start date of a fixed billing period |
| `hs_billing_period_end_date` | Billing end date | End date of a fixed billing period |
| `recurringbillingfrequency` | Billing frequency | How often a line item with recurring billing is billed. It informs the pricing calculation for deals and quotes. Line items with one-time billing aren't included. |
| `quantity   ` | Quantity | How many units of a product are included in this line item |
| `price   ` | Unit price | The cost of the product |
| `amount` | Net price | The total cost of the line item (i.e., the quantity times the unit price). |
| `currency` | Currency | Currency code for the line item |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/line-items#page-feedback)
-------------------------------------------------------------------------------------------

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