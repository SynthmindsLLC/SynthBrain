---
title: "Quotes API Overview and Usage"
description: "Use the quotes API to create, manage, and retrieve sales quotes for sharing pricing information with potential buyers. "
type: "concept"
tags:
- "Quote Management"
- "HubSpot CRM"
relationships:
- "#related_to [[Sales Quotes]]"
- "#enables [[Pricing Information Sharing]]"
birthdate: "N/A"
deathdate: "N/A"
---

Quotes
======

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the quotes API to create, manage, and retrieve sales quotes for sharing pricing information with potential buyers. Once configured, a quote can be shared with a buyer either at a specified URL or through PDF. Users can also [manage quotes in HubSpot](https://knowledge.hubspot.com/quotes/use-quotes#manage-quotes) to add details, update associations, and more.

If you’ve set up either [HubSpot payments](https://knowledge.hubspot.com/payments/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payments/connect-your-stripe-account-as-a-payment-processor-in-hubspot), you can configure a quote to be payable through this API. Learn more about [payable quotes](/docs/api/crm/quotes#enable-payments).  

![example-quote-api](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/example-quote-api.png?width=563&height=642&name=example-quote-api.png)

Example use case: You need to create a contract proposal for a customer who is interested in purchasing one of your annual SEO auditing service packages.

Below, learn how to create a quote through the API and configure its various properties, associations, states, and more.

Overview[](https://developers.hubspot.com/docs/api/crm/quotes#overview)
-----------------------------------------------------------------------

The quote creation process can be broken up into the following steps:

1.  **Create a quote:** create a quote with a few details, such as name and expiration date. You can also configure the quote to [enable e-signatures](/docs/api/crm/quotes#enable-e-signatures) and [payments](/docs/api/crm/quotes#enable-payments)[](https://knowledge.hubspot.com/quotes/use-e-signatures-with-quotes). 
2.  **Set up associations:** associate the quote with other types of CRM objects, such as line items, a quote template, a deal, and more. During the next step, the quote will inherit property values from some of these associated records as well as the account's settings.
3.  **Set the quote state:** set the quote's state to reflect its readiness to be shared with buyers. When you set the quote's state, such as making it an editable draft or fully published and publicly accessible quote, it will [inherit certain properties](#properties-set-by-quote-state) from its associated CRM records and account settings.
4.  **Share the quote:** once a quote has been published, you can share it with your buyers.

Create a quote[](https://developers.hubspot.com/docs/api/crm/quotes#create-a-quote)
-----------------------------------------------------------------------------------

To create a quote, you'll first configure its basic details by making a `POST` request to `/crm/v3/objects/quotes`. Later, you'll make a separate call to associate the quote with other objects, such as the quote template, line items, or a deal.

Depending on your preferred workflow, you can instead [create a quote with associations through one POST request](#create-a-quote-with-associations-single-request-).

In the post body, include the following required properties to configure its basic details.

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="width: 100.018%; padding: 10px 4px; height: 79.6719px;"><code>hs_title</code><span>&nbsp;&nbsp;</span><strong>string </strong><span style="font-weight: normal;">(required)</span><br><p>The name of the quote.</p></td></tr><tr><td style="width: 100.018%; padding: 10px 4px; height: 79.6719px;"><code>hs_expiration_date</code><span>&nbsp;&nbsp;</span><strong>string </strong><span style="font-weight: normal;">(required)</span><br><p>The date that the quote expires.</p></td></tr></tbody></table>

The above are just the minimum required properties to get a quote started but [other properties](/docs/api/crm/quotes#adding-associations) are required to publish a quote. To see all available quote properties, make a `GET` request to `crm/v3/properties/quotes`. Learn more about the [properties API](/docs/api/crm/properties).

// example POST request body { "properties": { "hs\_title": "CustomerName - annual SEO audit", "hs\_expiration\_date": "2023-12-10" } }

The response will include an `id`, which you'll use to continue configuring the quote. You can update quote properties at any time by making a `PATCH` request to `/crm/v3/objects/quotes/{quoteId}`.

### Enable e-signatures[](https://developers.hubspot.com/docs/api/crm/quotes#enable-e-signatures)

To enable e-signatures on the quote, include the `hs_esign_enabled` boolean property in your request body with a value of `true`. Note that you will not be able to add countersigners through the API, so those will need to be added in HubSpot before publishing the quote. You also cannot publish a quote with e-sign enabled if you've [exceeded your monthly e-signature limit](https://knowledge.hubspot.com/quotes/use-e-signatures-with-quotes#monitor-e-signature-usage). 

// example POST request body { "properties": { "hs\_title": "CustomerName - annual SEO audit", "hs\_expiration\_date": "2023-12-10", "hs\_esign\_enabled": "true" } }

Later, you'll need to associate the quote with the quote signers. While the contacts signing the quote exist as contacts in HubSpot, they're stored as a separate association type from contacts. Learn more about [associating quotes with quote signers](#associating-quote-signers).

### Enable payments[](https://developers.hubspot.com/docs/api/crm/quotes#enable-payments)

To turn on payments on a quote, include the `hs_payment_enabled` boolean property in your request body with a value of `true`. Depending on your payment processor and accepted payment methods, you’ll also need to set `hs_payment_type` and `hs_allowed_payment_methods`.

**Please note:** the HubSpot account must have either [HubSpot payments](https://knowledge.hubspot.com/payments/set-up-payments) or [Stripe payment processing](https://knowledge.hubspot.com/payments/connect-your-stripe-account-as-a-payment-processor-in-hubspot) set up before using this capability. 

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`hs_payment_enabled`

 | Boolean | 

When set to `true`, enables the quote to collect payment using either HubSpot payments or Stripe payment processing. Default is `false`.

 |
| 

`hs_payment_type`

 | Enumeration | 

Determines which payment processor to use. Value can be either `HUBSPOT` or `BYO_STRIPE`.

 |
| 

`hs_allowed_payment_methods`

 | Enumeration | 

The payment methods to be used (e.g., credit card).

 |
| 

`hs_collect_billing_address`

 | Boolean | 

When set to `true`, allows the buyer to enter their billing address during checkout.

 |
| 

`hs_collect_shipping_address`

 | Boolean | 

When set to `true`, allows the buyer to enter their shipping address during checkout.

 |

For example, to create a quote and enable HubSpot payments via credit/debit card or ACH, your request would look like:

// example POST request body { "properties": { "hs\_title": "CustomerName - annual SEO audit", "hs\_expiration\_date": "2023-12-10", "hs\_payment\_enabled": "true", "hs\_payment\_type": "HUBSPOT", "hs\_allowed\_payment\_methods": "CREDIT\_OR\_DEBIT\_CARD;ACH" } }

To track payment, HubSpot will automatically update the `hs_payment_status` and `hs_payment_date` properties:

*   When you publish a quote with payments enabled, HubSpot will automatically set the `hs_payment_status` property to PENDING.
*   If using ACH, when the payment is processed, HubSpot will automatically set the `hs_payment_status` property to PROCESSING.
*   When the payment is confirmed, HubSpot will automatically set the `hs_payment_status` property to PAID.
*   Once the quote is paid, HubSpot will automatically set `hs_payment_date` to the date and time that the payment was confirmed.
*   Once payment is confirmed, the payment is automatically associated to the quote. If you would like to retrieve more information about the payment, refer to the [Payments API](/docs/api/commerce/payments). 

Adding associations[](https://developers.hubspot.com/docs/api/crm/quotes#adding-associations)
---------------------------------------------------------------------------------------------

To create a complete quote, you'll need to associate it with other CRM records, such as line items, using the [associations API](/docs/api/crm/associations). The table below shows which CRM record associations are required for a complete quote, and which are optional. Continue reading to learn more about retrieving IDs and using them to create the needed associations.

| Object type | Required | Description |
| --- | --- | --- |
| **[Line items](/docs/api/crm/line-items)** | Yes | The goods and/or services being sold through the quote. You can create line items from [products in your product library](https://developers.hubspot.com/docs/api/crm/products) or create custom standalone line items. |
| [Quote template](https://knowledge.hubspot.com/quotes/create-custom-quote-templates) | Yes | The template that renders the quote, along with providing some default configuration settings for the quote, such as language. Each quote can be associated with one template. |
| [Deal](/docs/api/crm/deals) | Yes | The deal record for tracking revenue and sales lifecycle. A quote inherits values from the associated deal, including the owner and currency. Each quote can be associated with one deal. |
| [Contact](/docs/api/crm/contacts) | No | Specific buyers that you're addressing in the quote. |
| [Company](/docs/api/crm/companies) | No | A specific company that you're addressing in the quote. Each quote can be associated with one company. |
| [Discounts](/docs/api/crm/discounts), [fees](/docs/api/crm/fees), and [taxes](/docs/api/crm/taxes) | No | Any discounts, fees, and taxes to be applied at checkout. When determining the total quote amount, HubSpot first applies discounts, followed by fees, then taxes. You can use the `hs_sort_order` field to reorder objects of the same type. Can be set to fixed values or percentages by setting `hs_type` to either `FIXED` or `PERCENT`. |

### Retrieving IDs for associations[](https://developers.hubspot.com/docs/api/crm/quotes#retrieving-ids-for-associations)

To make each association, you'll first need to retrieve the ID of each object you want to associate. To retrieve each ID, you'll make a `GET` request to the relevant object endpoint, which follows the same pattern across each CRM object. When making each request, you can also include a `properties` query parameter to return specific properties when needed. Below are example `GET` requests for each type of object.

GET request for line items /crm/v3/objects/line\_items?properties=name GET request for quote templates /crm/v3/objects/quote\_template?properties=hs\_name GET request for deals /crm/v3/objects/deals?properties=dealname GET request for contacts /crm/v3/objects/contacts?properties=email GET request for companies /crm/v3/objects/companies?properties=name GET request for discounts crm/v3/objects/discounts?properties=hs\_type,hs\_value GET request for fees crm/v3/objects/fees?properties=hs\_type,hs\_value GET request for taxes crm/v3/objects/taxes?properties=hs\_type,hs\_value #GET request for line items curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/line\_items?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for quote templates curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/quote\_templates?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for deals curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/deals?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for contacts curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/contacts?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for companies curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/companies?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for discounts curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/discounts?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for fees curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/fees?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #GET request for taxes curl --request GET \\ --url 'https://api.hubapi.com/crm/v3/properties/taxes?archived=false' \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN'

Each successful call will return a `200` response with details for each fetched object type. You'll use the value in the `id` field to set associations in the next step.

// Example quote template GET response { "results": \[ { "id": "235425923863", "properties": { "hs\_createdate": "2023-06-12T16:27:32.794Z", "hs\_lastmodifieddate": "2023-06-12T16:27:32.794Z", "hs\_name": "Default Basic", "hs\_object\_id": "235425923863" }, "createdAt": "2023-06-12T16:27:32.794Z", "updatedAt": "2023-06-12T16:27:32.794Z", "archived": false }, { "id": "235425923864", "properties": { "hs\_createdate": "2023-06-12T16:27:32.794Z", "hs\_lastmodifieddate": "2023-06-12T16:27:32.794Z", "hs\_name": "Default Modern", "hs\_object\_id": "235425923864" }, "createdAt": "2023-06-12T16:27:32.794Z", "updatedAt": "2023-06-12T16:27:32.794Z", "archived": false }, { "id": "235425923865", "properties": { "hs\_createdate": "2023-06-12T16:27:32.794Z", "hs\_lastmodifieddate": "2023-06-12T16:27:32.794Z", "hs\_name": "Default Original", "hs\_object\_id": "235425923865" }, "createdAt": "2023-06-12T16:27:32.794Z", "updatedAt": "2023-06-12T16:27:32.794Z", "archived": false } \] }

### Creating associations[](https://developers.hubspot.com/docs/api/crm/quotes#creating-associations)

With your IDs retrieved, you can now make calls to the [associations API](/docs/api/crm/associations) to create associations.

For each type of object you want to associate with a quote, you'll need to make a separate call by making a `PUT` request using the URL structure below:

 `/crm/v4/objects/quotes/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}`

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`fromObjectId`

 | 

The ID of the quote.

 |
| 

`toObjectType`

 | 

The type of object you're associating with. For example, `line_items`, `deals`, and `quote_template`. 

 |
| 

`toObjectId`

 | 

The ID of the object you're associating the quote with. 

 |

Below are example `PUT` requests for each type of object.

PUT request to associate a line item /crm/v4/objects/quotes/{quoteId}/associations/default/line\_items/{lineItemId} PUT request to associate a quote template /crm/v4/objects/quotes/{quoteId}/associations/default/quote\_template/{quoteTemplateId} PUT request to associate a deal /crm/v4/objects/quotes/{quoteId}/associations/default/deals/{dealId} PUT request to associate contacts /crm/v4/objects/quotes/{quoteId}/associations/default/contacts/{contactId} PUT request to associate companies /crm/v4/objects/quotes/{quoteId}/associations/default/companies/{companyId} PUT request to associate discounts /crm/v4/objects/quotes/{quoteId}/associations/default/discounts/{discountId} PUT request to associate fees /crm/v4/objects/quotes/{quoteId}/associations/default/fees/{feeId} PUT request to associate taxes /crm/v4/objects/quotes/{quoteId}/associations/default/taxes/{taxId} #PUT request to associate line items curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/line\_items/{lineItemId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate a quote template curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quote\_ID}/associations/default/quote\_template/{quoteTemplateId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate a deal curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/deals/{dealId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate contacts curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/contacts/{contactId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate a company curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/companies/{companyId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate discounts curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/discounts/{discountId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate fees curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/fees/{feeId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN' #PUT request to associate taxes curl --request PUT \\ --url https://api.hubapi.com/crm/v4/objects/quotes/{quoteId}/associations/default/line\_items/{taxId} \\ --header 'authorization: Bearer YOUR\_ACCESS\_TOKEN'

As an example, if your quote has an ID of `123456`, the requests to associate the quote might include the following:

*   **Line items (IDs: `55555`, `66666`):** 
    *   `/crm/v4/objects/quotes/123456/associations/default/line_items/55555`
    *   `/crm/v4/objects/quotes/123456/associations/default/line_items/66666`
*   **Quote template (ID:** `987654`**):**  `/crm/v4/objects/quotes/123456/associations/default/quote_template/987654`
*   **Deal (ID: `345345`):** `/crm/v4/objects/quotes/123456/associations/default/deals/345345`

Each successful association will return a `200` response with details about the association. The above calls will associate the objects in both directions, with each direction have its own ID. For example, if you associate the quote with a quote template, the response will describe the association from both ends. In the example response below, `286` is the quote-to-quote-template association type ID, and `285` is the quote-template-to-quote association type ID.

// Example response { "status": "COMPLETE", "results": \[ { "from": { "id": "115045534742" }, "to": { "id": "102848290" }, "associationSpec": { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 285 } }, { "from": { "id": "102848290" }, "to": { "id": "115045534742" }, "associationSpec": { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 286 } } \], "startedAt": "2023-10-12T16:48:40.624Z", "completedAt": "2023-10-12T16:48:40.712Z" }

**Please note:** when associating a quote with a quote template, keep in mind the following limits:

*   Quote templates must be [created](https://knowledge.hubspot.com/quotes/create-custom-quote-templates) before they can be associated with a quote.
*   A quote can only be associated with on quote template.
*   This API does not support legacy or proposal quotes. Only the `CUSTOMIZABLE_QUOTE_TEMPLATE` template type can be used.  
    

### Associating quote signers[](https://developers.hubspot.com/docs/api/crm/quotes#associating-quote-signers)

If you're [enabling the quote for e-signatures](#enable-e-signatures), you'll also need to create an association between the quote and the contacts who are signing by using a specific quote-to-contact [association label](/docs/api/crm/associations#associate-records-with-a-label).

Rather than using the default association endpoints shown above, you'll need to make a `PUT` request to the following URL:

`/crm/v4/objects/quote/{quoteId}/associations/contact/{contactId}`

In the request body, you'll need to specify the `associationCategory` and `associationTypeId`, as shown below:

// Example request body \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 702 } \]

// Example request body \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 702 } \]

Create a quote with associations (single request)[](https://developers.hubspot.com/docs/api/crm/quotes#create-a-quote-with-associations-single-request-)
--------------------------------------------------------------------------------------------------------------------------------------------------------

The following request body will create a new quote with associations to a quote template, a deal, two line items, and a contact.

`POST` `/crm/v3/objects/quote` 

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%; height: 590.032px;"><tbody><tr style="height: 135.672px;"><td style="padding: 10px 4px; height: 135.672px;"><code>properties</code> &nbsp;<strong>object</strong>&nbsp;<p>Quote details, which can be retrieved through the <a href="/docs/api/crm/properties" rel="noopener" target="_blank">properties API</a>. Required properties are: <code>hs_title</code> and <code>hs_expiration_date</code>.</p></td></tr><tr style="height: 79.6719px;"><td style="width: 100%; padding: 10px 4px 10px 22px; height: 79.6719px;"><span>⮑&nbsp;</span><code>hs_title</code><span>&nbsp;&nbsp;</span><strong>string </strong><span style="font-weight: normal;">(required)</span><br><p>The name of the quote.</p></td></tr><tr style="height: 79.6719px;"><td style="width: 100%; padding: 10px 4px 10px 22px; height: 79.6719px;"><span>⮑&nbsp;</span><code>hs_expiration_date</code><span>&nbsp;&nbsp;</span><strong>string </strong><span style="font-weight: normal;">(required)</span><br><p style="padding-left: 40px;">The date that the quote expires.</p></td></tr><tr style="height: 135.672px;"><td style="width: 100%; padding: 10px 4px 10px 22px; height: 135.672px;"><span>⮑&nbsp;</span><code>hs_status</code><span>&nbsp;&nbsp;</span><strong>string</strong><br><p>The <a href="#update-quote-status" rel="noopener">quote status</a>. Omitting this property on create will prevent users from being able to edit the quote in HubSpot.</p></td></tr><tr style="height: 79.6719px;"><td style="padding: 10px 4px; height: 79.6719px;"><code>associations</code> &nbsp;<strong>array</strong><p>The quote's associated records. For a quote to be publishable, it must have an associated deal and quote template. The line items should be created separately from the line items on the associated deal.&nbsp;</p><p>To set each association, include a separate object in the associations array with the following fields:</p><ul><li>to: the ID of the record to associate with the quote.</li><li>associationCategory: the <a href="https://developers.hubspot.com/docs/api/crm/associations#retrieve-association-types" style="font-size: var(--cl-text-font-size, 1rem);">type of association</a><span style="font-size: var(--cl-text-font-size, 1rem); font-weight: var(--cl-text-font-weight, 300);">. Can be HUBSPOT_DEFINED or USER_DEFINED.</span></li><li>associationTypeId: the ID of the type of association being made:<ul><li>286: quote to quote template</li><li>64: quote to deal</li><li>67: quote to line item</li></ul></li></ul><p>Learn more about <a href="/docs/api/crm/associations#association-type-id-values" rel="noopener">association type IDs</a>.</p></td></tr></tbody></table> 

// POST request to https://api.hubapi.com/crm/v3/objects/quote { "properties": { "hs\_title": "CustomerName - annual SEO audit", "hs\_expiration\_date": "2023-09-30" }, "associations": \[ { "to": { "id": 115045534742 }, "types": \[{ "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 286 }\] }, { "to": { "id": 14795354663 }, "types": \[{ "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 64 }\] }, { "to": { "id": 75895447 }, "types": \[{ "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 67 }\] }, { "to": { "id": 256143985 }, "types": \[{ "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 67 }\] } \] }

**Please note:** these line items should be different to line items on other objects, even if they are associated (e.g., associating a quote to a deal). See the [line items API documentation](/docs/api/crm/line-items) for more information.

Update quote state[](https://developers.hubspot.com/docs/api/crm/quotes#update-quote-state)
-------------------------------------------------------------------------------------------

A quote's state describes how far along it is in the creation process, from initial set up to being published and publicly accessible. Quote state can also reflect the [quote approval process](https://knowledge.hubspot.com/quotes/approve-quotes), if quote approvals are enabled for the account. When setting a quote's state, HubSpot will [automatically fill in certain properties](#properties-set-by-quote-state).

You can update a quote's state by making a `PATCH` request to `/crm/v3/objects/quote/{quoteId}`.

A quote's state is based on the `hs_status` field. Certain quote states allow users to edit, publish, and use the quote in quote approval workflows. Below are the available quote states.

*   **No state:** if no value is provided for the `hs_status` field, the quote will be in a _Minimal_ state. The quote will appear on the index page of the quotes tool, but cannot be edited directly. Quotes in this state can still be used in automation, such as the sequences tool, and are also available to analyze within the reporting tool.
*   `DRAFT`: enables the quote to be edited in HubSpot. This state can be useful for when the quote isn't fully configured or if you'd rather enable sales reps to complete the quote configuration process in HubSpot. 
*   `APPROVAL_NOT_NEEDED`: publishes the quote at a publicly accessible URL (`hs_quote_link`) without needing to be [approved](https://knowledge.hubspot.com/quotes/approve-quotes).
*   `PENDING_APPROVAL`: indicates that the quote is [waiting to be approved](https://knowledge.hubspot.com/quotes/approve-quotes) before it can be published.
*   `APPROVED`: the quote has been [approved](https://knowledge.hubspot.com/quotes/approve-quotes) and is now published at a publicly accessible URL (`hs_quote_link`).
*   `REJECTED`: indicates that the quote has been set up but has not been [approved](https://knowledge.hubspot.com/quotes/approve-quotes) for publishing, and must be edited before it can be submitted for approval again.

**Please note:** if you're [enabling e-signatures](#enabling-e-signatures) on the quote, you won't be able to publish the quote if you've exceeded your [monthly e-signature limit](https://knowledge.hubspot.com/quotes/use-e-signatures-with-quotes#monitor-e-signature-usage).

For example, the following request would publish the quote at a publicly accessible URL.

// PATCH request to https://api.hubapi.com/crm/v3/objects/quote/{QUOTE\_ID} { "properties": { "hs\_status": "APPROVAL\_NOT\_NEEDED" } }

**Please note:** by default, HubSpot will set the quote's `hs_template_type` property to `CUSTOMIZABLE_QUOTE_TEMPLATE` after you [update the quote's state](/docs/api/crm/quotes#update-quote-state). This template type is supported by the v3 API, whereas the following template types are legacy templates that are no longer supported:

*   `QUOTE`
*   `PROPOSAL`

Retrieve quotes[](https://developers.hubspot.com/docs/api/crm/quotes#retrieve-quotes)
-------------------------------------------------------------------------------------

You can retrieve quotes individually or in batches.

*   To retrieve an individual quote, make a `GET` request to `/crm/v3/objects/quotes/{quoteID}`.
*   To request a list of all quotes, make a `GET` request to `/crm/v3/objects/quotes`.

For these endpoints, you can include the following query parameters in the request URL: 

 
| Parameter | Description |
| --- | --- |
| `properties` | A comma separated list of the properties to be returned in the response. If the requested quotecontact doesn't have a value for a property, it will not appear in the response. |
| `propertiesWithHistory` | A comma separated list of the current and historical properties to be returned in the response. If the requested quote doesn't have a value for a property, it will not appear in the response. |
| `associations` | A comma separated list of objects to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](/docs/api/crm/associations) |

To retrieve a batch of specific quotes by their IDs, make a `POST` request to `crm/v3/objects/quotes/batch/read` and include the IDs in the request body. You can also include a `properties` array to specify which properties to return. The batch endpoint cannot retrieve associations. Learn how to batch read associations with the [associations API](/docs/api/crm/associations).

JSON

Copy all

    // Example request body
    {
     "inputs": [
      {"id": "342007287"},
      {"id":"81204505203"}
     ],
     "properties": [
      "hs_content", "hs_sentiment", 
      "hs_submission_timestamp"

### Properties set by quote state[](https://developers.hubspot.com/docs/api/crm/quotes#properties-set-by-quote-state)

Updating the quote's state will update the following properties:

*   `hs_quote_amount`: calculated based on any associated line items, taxes, discounts, and fees.
*   `hs_domain`: set from the associated quote template.
*   `hs_slug`: randomly generated if one is not explicitly provided.
*   `hs_quote_total_preference`: set based on your account settings. If you haven't configured this setting, it will default to the value of the total\_first\_payment field.
*   `hs_timezone`: defaults to your HubSpot account's timezone.
*   `hs_locale`: set from the associated quote template.
*   `hs_quote_number`: set based on the current date and time, unless one is provided.
*   `hs_language`: set from the associated quote template.
*   `hs_currency`: set based on the associated deal. If you haven't associated a deal with the quote, it will default to your HubSpot account's default currency.

Additionally, the properties below will be calculated when the quote is set to a published state:

*   `hs_pdf_download_link`: populated with a URL of a PDF for the quote.
*   `hs_locked`: set to `true`. To modify any properties after you've published a quote, you must first update the `hs_status` of the quote back to `DRAFT`, `PENDING_APPROVAL`, or `REJECTED`.
*   `hs_quote_link`: the quote's publicly accessible URL. This is a read-only property and cannot be set through the API after publishing.
*   `hs_esign_num_signers_required`: if you've [enabled e-signatures](#enable-e-signatures), displays the number of signatures required.
*   `hs_payment_status`: the status of payment collection, if you’ve enabled payments. Upon publishing with payments enabled, this property will be set to PENDING. Once the buyer submits payment through the quote, the status will automatically update accordingly. Learn more about [enabling payments](/docs/api/crm/quotes#enable-payments). 

Scopes[](https://developers.hubspot.com/docs/api/crm/quotes#scopes)
-------------------------------------------------------------------

The following scopes are required for an app to create a valid publishable quote:

*   `crm.objects.quotes.write`, `crm.objects.quotes.read`, `crm.objects.line_items.write`, `crm.objects.line_items.read`, `crm.objects.owners.read`, `crm.objects.contacts.write`, `crm.objects.contacts.read`, `crm.objects.deals.write`, `crm.objects.deals.read`, `crm.objects.companies.write`, `crm.objects.companies.read`
*   `crm.schemas.quote.read`, `crm.schemas.line_items.read`, `crm.schemas.contacts.read`, `crm.schemas.deals.read`, `crm.schemas.companies.read`

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/quotes#page-feedback)
---------------------------------------------------------------------------------------

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