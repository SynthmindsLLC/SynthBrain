Orders
======

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the orders API to create and manage data related to ecommerce purchases in HubSpot. This can be especially useful for keeping HubSpot data synced with external ecommerce platforms, such as Shopify and NetSuite.

For example, when a buyer adds a set of products to their cart and makes a purchase, store that purchase as an individual order. You can then update that order with tracking information once the shipping label has been printed. Because this information is stored in a property, you can reference it in emails that you send to notify customers that their package is on the way. 

Create orders[](https://developers.hubspot.com/docs/api/commerce/orders#create-orders)
--------------------------------------------------------------------------------------

To create an order, make a `POST` request to `crm/v3/objects/order`.

In the request body, you can include the `properties` and `associations` objects to set property values and associate the order with other CRM objects (e.g., contacts and line items). Learn more about order properties and associations below.

### Properties[](https://developers.hubspot.com/docs/api/commerce/orders#properties)

Order details are stored in order properties. HubSpot provides a set of [default order properties](#order-properties), but you can also create your own custom properties using the [properties API](/docs/api/crm/properties).

To include properties when creating an order, add them as fields in a `properties` object in the request body. For example, the request body below would create an order with some basic order and shipping details based on the information provided by the buyer at checkout.

// Example POST request body { "properties": { "hs\_order\_name":"Camping supplies", "hs\_currency\_code": "USD", "hs\_source\_store": "REI - Portland", "hs\_fulfillment\_status":"Packing", "hs\_shipping\_address\_city":"Portland", "hs\_shipping\_address\_state":"Maine", "hs\_shipping\_address\_street":"123 Fake Street", } }

The response will include the information you provided during creation along with a few other default properties.

// Example response { "id":"54805205097", "properties":{ "hs\_created\_by\_user\_id":"959199", "hs\_createdate":"2024-03-27T18:04:11.823Z", "hs\_currency\_code":"USD", "hs\_exchange\_rate":"1.0", "hs\_fulfillment\_status":"Packing", "hs\_lastmodifieddate":"2024-03-27T18:04:11.823Z", "hs\_object\_id":"54805205097", "hs\_object\_source":"CRM\_UI", "hs\_object\_source\_id":"userId:959199", "hs\_object\_source\_label":"CRM\_UI", "hs\_object\_source\_user\_id":"959199", "hs\_order\_name":"Camping supplies", "hs\_shipping\_address\_city":"Portland", "hs\_shipping\_address\_state":"Maine", "hs\_shipping\_address\_street":"123 Fake Street", "hs\_source\_store":"REI - Portland", "hs\_updated\_by\_user\_id":"959199" }, "createdAt":"2024-03-27T18:04:11.823Z", "updatedAt":"2024-03-27T18:04:11.823Z", "archived":false }

### Associations[](https://developers.hubspot.com/docs/api/commerce/orders#associations)

You can associate the order with other HubSpot CRM objects at creation by including an `associations` array. You can also use the [associations API](/docs/api/crm/associations) to update existing orders after creation.

In the `associations` array, include an object for each associated record using the following fields:

Use this table to describe parameters / fields
| Fields | Type | Description |
| --- | --- | --- |
| 
`toObjectId`

 | String | 

The ID of the record that you want to associate the order with.

 |
| 

`associationTypeId`

 | String | 

A unique identifier to indicate the association type between the order and the other object. Below are the CRM objects that you can associate orders with, along with their `associationTypeId`:

*   [Carts](/docs/api/commerce/carts): `593`
*   [Contacts](/docs/api/crm/contacts): `507`
*   [Companies](/docs/api/crm/companies): `509`
*   [Deals](/docs/api/crm/deals): `512`
*   [Discounts](/docs/api/crm/discounts): `519`
*   [Discount codes](https://knowledge.hubspot.com/payments/create-and-use-payment-discount-codes): `521`
*   [Invoices](/docs/api/commerce/invoices): `518`
*   [Line items](/docs/api/crm/line-items): `513`
*   [Payments](/docs/api/commerce/payments): `523`
*   [Quotes](/docs/api/crm/quotes): `730`
*   [Subscriptions](/docs/api/crm/subscriptions): `516`
*   [Tasks](/docs/api/crm/tasks): `726`
*   [Tickets](/docs/api/crm/tickets): `525`

To see a list of all association types, check out the [associations API documentation](/docs/api/crm/associations#association-type-id-values). Or, you can retrieve each value by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

 |

For example, the `POST` request body below would create an order that's associated with a specific contact and two line items. Properties are also included below the associations for setting initial order information.

// Example request body { "associations": \[ { "to": { "id": 301 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 507 } \] }, { "to": { "id": 1243313490 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 513 } \] }, { "to": { "id": 1243557166 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 513 } \] } \], "properties": { "hs\_order\_name":"Associated order", "hs\_currency\_code": "USD", "hs\_source\_store": "REI - Portland", "hs\_fulfillment\_status":"Packing", "hs\_shipping\_address\_city":"Portland", "hs\_shipping\_address\_state":"Maine", "hs\_shipping\_address\_street":"123 Fake Street" } }

Retrieve orders[](https://developers.hubspot.com/docs/api/commerce/orders#retrieve-orders)
------------------------------------------------------------------------------------------

Depending on the information you need, there are a few ways to retrieve orders:

*   To retrieve all orders, make a `GET` request to `/crm/v3/objects/order`.
*   To retrieve a specific order, make a `GET` request to the above URL and specify an order ID. For example: `/crm/v3/objects/order/44446244097`.
*   To retrieve orders that meet a specific set of criteria, you can make a `POST` request to the search endpoint and include filters in the request body. Learn more about [searching the CRM](/docs/api/crm/search#make-a-search-request).

The response will include a few default properties, including the create date, last modified date.

// Example response { "results": \[ { "id": "54767113310", "properties": { "hs\_createdate": "2024-03-26T20:02:34.935Z", "hs\_lastmodifieddate": "2024-03-26T20:02:48.278Z", "hs\_object\_id": "54767113310" }, "createdAt": "2024-03-26T20:02:34.935Z", "updatedAt": "2024-03-26T20:02:48.278Z", "archived": false }, { "id": "54804869149", "properties": { "hs\_createdate": "2024-03-27T17:39:16.122Z", "hs\_lastmodifieddate": "2024-03-27T17:39:16.122Z", "hs\_object\_id": "54804869149" }, "createdAt": "2024-03-27T17:39:16.122Z", "updatedAt": "2024-03-27T17:39:16.122Z", "archived": false } \] }

To return specific properties, include a `properties` query parameter in the request URL along with comma-separated property names. For example, making a `GET` request to the following URL would result in the response below:

`/crm/v3/objects/order?properties=hs_order_name,hs_source_store`

// Example response { "id": "54767113310", "properties": { "hs\_createdate": "2024-03-26T20:02:34.935Z", "hs\_lastmodifieddate": "2024-03-27T18:50:07.678Z", "hs\_object\_id": "54767113310", "hs\_order\_name": "Test API order 2", "hs\_source\_store": "REI - Portland" }, "createdAt": "2024-03-26T20:02:34.935Z", "updatedAt": "2024-03-27T18:50:07.678Z", "archived": false }

To view all available order properties, you can query the [properties API](/docs/api/crm/properties) by making a `GET` request to `crm/v3/properties/order`.

Learn more about [order properties](#order-properties).

### Search for orders by properties[](https://developers.hubspot.com/docs/api/commerce/orders#search-for-orders-by-properties)

You can use the search endpoint to retrieve orders that meet a specific set of [filter criteria](/docs/api/crm/search#filter-search-results). This will be a `POST` request that includes your filter criteria in the request body.

For example, to search for all orders placed at a specific store, you would make a `POST` request to `crm/v3/objects/order/search` with the following request body:

// Example search request body { "filterGroups": \[ { "filters": \[ { "propertyName": "hs\_source\_store", "value": "REI - Portland", "operator": "EQ" } \] } \], "properties": \["hs\_order\_name","hs\_source\_store"\] }

### Retrieve an order with associations[](https://developers.hubspot.com/docs/api/commerce/orders#retrieve-an-order-with-associations)

To retrieve an order along with its associations, make a `GET` request to `crm/v3/objects/order/{orderId}/associations/{objectName}`

For example, to retrieve an order and its associated contacts, you would use the following URL: 

`crm/v3/objects/order/{orderId}/associations/contact`

This will return the IDs of the currently associated contacts, along with meta information about the association type.

// Example response { "results": \[ { "id": "301", "type": "order\_to\_contact" }, { "id": "1196316844", "type": "order\_to\_contact" } \] }

You could then use the returned IDs to request more information about the contacts through the [contacts API](/docs/api/crm/contacts). For example, you could retrieve the contact using its ID by making a `GET` request to `crm/v3/objects/contacts/{contactId}`.

// Example response { "id":"301", "properties":{ "createdate":"2022-09-27T13:13:31.004Z", "email":"tom.bombadil@oldforest.com", "firstname":"Tom", "hs\_object\_id":"301", "lastmodifieddate":"2023-11- 07T17:14:00.841Z", "lastname":"Bombadil" }, "createdAt":"2022-09-27T13:13:31.004Z", "updatedAt":"2023-11-07T17:14:00.841Z", "archived":false }

Note that the `filters` array specifies the search criteria, while the `properties` array specifies which properties to return.

Update orders[](https://developers.hubspot.com/docs/api/commerce/orders#update-orders)
--------------------------------------------------------------------------------------

To update an order, make a `PATCH` request to `/crm/v3/objects/order/{orderId}`. In the request body, include a `properties` object containing the properties that you want to update. 

For example, if you wanted to update an order with the shipping tracking number, you could send the following request body:

// Example request body { "properties": { "hs\_shipping\_tracking\_number": "123098521091" } }

The response will include a set of default properties along with the property that you just set.

// Example response { "id": "54767113310", "properties": { "hs\_created\_by\_user\_id": "959199", "hs\_createdate": "2024-03-26T20:02:34.935Z", "hs\_lastmodifieddate": "2024-03-27T20:03:05.890Z", "hs\_object\_id": "54767113310", "hs\_shipping\_tracking\_number": "123098521091", "hs\_updated\_by\_user\_id": "959199" }, "createdAt": "2024-03-26T20:02:34.935Z", "updatedAt": "2024-03-27T20:03:05.890Z", "archived": false }

To update the associations for an existing order, make a `PUT` request to `/crm/v3/objects/order/{orderId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. You can also use the [associations API](/docs/api/crm/associations).

See the [associations section](#associations) for `associationTypeId` values for order-to-object associations. You can also make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`.

To see all a list of all values, check out the [associations API documentation](/docs/api/crm/associations#association-type-id-values).

For example, to associate an existing order with an existing payment, you would make a `PUT` request to the following URL:

`/crm/v3/objects/order/{orderId}/associations/commerce_payments/{paymentId}/523`

The response will return a set of default properties along with an `associations` object containing information about the association that you set.

// Example response { "id": "54767113310", "properties": { "hs\_createdate": "2024-03-26T20:02:34.935Z", "hs\_lastmodifieddate": "2024-03-27T20:03:05.890Z", "hs\_object\_id": "54767113310" }, "createdAt": "2024-03-26T20:02:34.935Z", "updatedAt": "2024-03-27T20:03:05.890Z", "archived": false, "associations": { "payments": { "results": \[ { "id": "50927296322", "type": "order\_to\_commerce\_payment" } \] } } }

To remove an association from an existing order, make a `DELETE` request to the following URL:

`/crm/v3/objects/order/{orderId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

For example, if you wanted to remove an associated payment from an order, your request URL would be the following:

`/crm/v3/objects/order/{orderId}/associations/commerce_payments/{paymentId}/523`

Order properties[](https://developers.hubspot.com/docs/api/commerce/orders#order-properties)
--------------------------------------------------------------------------------------------

When managing your order data, you may want to use some of the common properties in the table below. To get all order properties, make a `GET` request to `/crm/v3/properties/order`. Learn more about using the [properties API](/docs/api/crm/properties).

| Property name | Label in UI | Description |
| --- | --- | --- |
| `hs_order_name` | Name | The name of the order. |
| `hs_currency_code` | Currency Code | The currency that the order was placed in. |
| `hs_source_store` | Source Store | The store that that the order came from.  |
| `hs_fulfillment_status` | Fulfillment Status | The current fulfillment / shipping status of the order. |
| `hs_shipping_status_url` | Shipping Status URL | A URL for tracking the shipment status. |
| `hs_shipping_tracking_number` | Shipping Tracking Number | The tracking number for shipping. |
| `hs_shipping_address_street   ` | Shipping Street | The street address for shipping. |
| `hs_shipping_address_city   ` | Shipping City | The city in the shipping address. |
| `hs_shipping_address_postal_code` | Shipping ZIP/Postal Code | The zip code of the shipping address. |
| `hs_pipeline` | Pipeline | The pipeline that the order is in. Pipelines contain stages for tracking the order's progress. Learn more about [pipelines and stages](#pipelines-and-stages) below. |
| `hs_pipeline_stage` | Stage | The order's progress within its current pipeline. Learn more about [pipelines and stages](#pipelines-and-stages) below. |

### Pipelines and stages[](https://developers.hubspot.com/docs/api/commerce/orders#pipelines-and-stages)

To track an order's progress, you can create pipelines with defined stages for each step of the fulfillment process. For example, you could create a pipeline for online orders with stages for when the order has been opened, paid, processed, shipped, cancelled, and refunded.

Using the [pipelines API](/crm/v3/pipelines/{objectType}), you can create an order pipeline by making a `POST` request to `crm/v3/pipelines/order`.  In the request body, you'll include a `label` for the pipeline, `displayOrder` for the display in HubSpot, and a `stages` array with objects for each stage.

// Example request body { "label":"Online orders", "displayOrder": 0, "stages": \[ { "label": "Open", "displayOrder": 0, "metadata": { "state":"OPEN" } }, { "label": "Paid", "displayOrder": 1, "metadata": { "state":"OPEN" } }, { "label": "Processed", "displayOrder": 2, "metadata": { "state":"OPEN" } }, { "label": "Shipped", "displayOrder": 3, "metadata": { "state":"CLOSED" } }, { "label": "Cancelled", "displayOrder": 4, "metadata": { "state":"CLOSED" } }, { "label": "Refunded", "displayOrder": 5, "metadata": { "state":"CLOSED" } } \] }

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`label`

 | String | 

The pipeline's label as it should appear in HubSpot.

 |
| 

`displayOrder`

 | Number | 

The order for displaying the pipeline in HubSpot. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label.

 |
| 

`stages`

 | Array | 

An array containing the pipeline stages. Each stage is an object containing the following fields:

*   `label`: the stage's label as it should appear in HubSpot.
*   `displayOrder`: the order in which the stage will appear in HubSpot.
*   `metadata`: configures whether the stage is in progress (`OPEN`) or complete (`CLOSED`) using the `state` field.

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/commerce/orders#page-feedback)
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