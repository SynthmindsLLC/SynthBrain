---
title: "Products in HubSpot CRM"
description: "Products represent the goods or services you sell, allowing sales reps to easily add them to deals and quotes. Manage product data through products endpoints and sync with other systems. Learn more about object properties, associations, relationships, etc., in our Understanding the CRM Objects guide."
type: "group"
tags:
- "CRM"
- "HubSpot"
- "Products"
relationships:
- "#part_of [[Sales]]"
- "#related_to [[Deals]]"
- "#related_to [[Quotes]]"
- "#used_by [[Sales Reps]]"
---

Products
========

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, products represent the goods or services you sell. Building a [product library](https://knowledge.hubspot.com/deals/how-do-i-use-products) allows you to quickly add products to deals, generate quotes, and report on product performance. The products endpoints allow you to manage this data and sync it between HubSpot and other systems.

Products, along with companies, contacts, deals, tickets, line items, and quotes, are objects in the HubSpot CRM. Learn more about object properties, associations, relationships, and more in our [Understanding the CRM Objects](https://developers.hubspot.com/docs-beta/crm/understanding-the-crm) guide.

**Example use case:** so that sales reps can easily add goods and services to deals, quotes, and more, use the products API to import your product catalog into HubSpot.

Create a product[](https://developers.hubspot.com/docs/api/crm/products#create-a-product)
-----------------------------------------------------------------------------------------

To create a product make a `POST` request to `crm/v3/objects/products`. In the request body, include any product properties that you'd like to set on create. You can later update a product's properties through a `PATCH` request to the same endpoint.

To see all available product properties, make a `GET` request to the [properties API](/docs/api/crm/properties). To retrieve product properties, the request URL will be `/crm/v3/properties/products`.

// POST request to crm/v3/objects/products { "name": "Implementation Service", "price": "6000.00", "hs\_sku": "123456", "description": "Onboarding service for data product", "hs\_cost\_of\_goods\_sold": "600.00", "hs\_recurring\_billing\_period": "P12M" }

Note that the value for `hs_recurring_billing_period` is formatted as `P#M`, where # is the number of months.

Associate products[](https://developers.hubspot.com/docs/api/crm/products#associate-products)
---------------------------------------------------------------------------------------------

Products themselves can't be associated with other CRM objects. However, to associate a product's information with a deal or a quote, you can create a [line item](/docs/api/crm/line-items) based on that product. Line items are individual instances of products, and are a separate object from products so that you can tailor the goods and services on a deal or quote as needed without needing to update the product itself.

For example, if you're putting together a deal where one of your products is being sold, you'd first create a line item from the product, then associate it with the deal. You can either do this with two separate calls, or with one call that creates and associates the line item. Both options are shown below.

**Please note:** line items belong to one single parent object. If associating objects, line items should be individual to each object. For example, if you're creating a deal and a quote, you should create one set of line items for the deal, and another set for the quote. This will help streamline CRM data across objects and prevent unexpected data loss when needing to modify line items. For example, deleting a quote will also delete the quote's line items. If those line items are also assocatied with a deal, the deal's line items will also be deleted.

### Create and associate a line item (multiple calls)[](https://developers.hubspot.com/docs/api/crm/products#create-and-associate-a-line-item-multiple-calls-)

First, you'll create a line item based on a product with the ID of `1234567`. For a full list of available line item properties, make a `GET` request to the [properties API](/docs/api/crm/properties). The URL for line items would be `crm/v3/properties/line_items`. Because you're create the line item from an existing product, it will inherit property values from the product, such as price.

// POST request to https://api.hubapi.com/crm/v3/objects/line\_item { "properties": { "quantity": 1, "hs\_product\_id": "1234567", "name": "New line item (product-based)" } }

The response will return a line item ID which you can use to associate it with a deal using the [associations API](/docs/api/crm/associations). For this example, assume that the returned line item ID is `7791176460`.

To associate the line item with an existing deal (ID: `14795354663`), you'll make a `PUT` request to `/crm/v4/objects/line_items/7791176460/associations/default/deals/14795354663`. This request uses the default association type. 

A `200` response will return information similar to the following:

// PUT request to crm/v4/objects/line\_items/7791176460/associations/default/deals/14795354663 { "status": "COMPLETE", "results": \[ { "from": { "id": "14795354663" }, "to": { "id": "7791176460" }, "associationSpec": { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 19 } }, { "from": { "id": "7791176460" }, "to": { "id": "14795354663" }, "associationSpec": { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 20 } } \], "startedAt": "2023-12-21T20:06:52.083Z", "completedAt": "2023-12-21T20:06:52.192Z" }

In HubSpot, the deal record will display the line item in the _Line items_ card.

![deal-record-line-item-association](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/deal-record-line-item-association.png?width=400&height=155&name=deal-record-line-item-association.png)

### Create and associate a line item (single call)[](https://developers.hubspot.com/docs/api/crm/products#create-and-associate-a-line-item-single-call-)

To create a line item from an existing product and associate it with a deal using a single call, you can include an `associations` array in the line item create request. 

To create the line item, make a `POST` request to `crm/v3/objects/line_item`. Your request body will look similar to the following. Note that the `associationTypeId` for the line item-deal association is `20`. Learn more about [association types between different types of CRM records](/docs/api/crm/associations#association-type-id-values).

// POST request to https://api.hubapi.com/crm/v3/objects/line\_item { "properties": { "quantity": 1, "hs\_product\_id": "1234567", "name": "New line item (product-based)" }, "associations": \[ { "to": { "id": "14795354663" }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 20 } \] } \] }

A `200` response will return details about the new line item. In HubSpot, the deal record will display the line item in the _Line items_ card.

![deal-record-line-item-association](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/deal-record-line-item-association.png?width=400&height=155&name=deal-record-line-item-association.png)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/products#page-feedback)
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