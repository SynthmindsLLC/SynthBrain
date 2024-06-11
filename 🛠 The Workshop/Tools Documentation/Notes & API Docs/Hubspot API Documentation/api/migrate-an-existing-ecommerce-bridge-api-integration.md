---
title: "Migrate an existing Ecommerce Bridge API integration"
description: "Guide on migrating the Ecommerce Bridge API integration due to sunsetting of API keys and changes in HubSpot's ecommerce features."
type: "guide"
tags:
- "Ecommerce"
- "API Integration"
- "HubSpot"
relationships:
- "#related_to [[Migrating contact, product, deal & line items sync]]"
- "#related_to [[Learn about the different APIs you can use for the contact, product, deal and line items sync]]"
- "#related_to [[Establishing relationships between objects using Associations API]]"
- "#related_to [[Migrating external object id]]"
- "#related_to [[Creating unique identifiers]]"
- "#related_to [[Defining own properties with Properties API]]"
- "#related_to [[Import API]]"
- "#related_to [[Pipeline creation and usage]]"
- "#related_to [[VAST email templates sunsetting]]"
- "#related_to [[New customer, re-engaging, abandon cart email templates]]"
- "#related_to [[Ecommerce dashboard and template sunsetting for new users]]"
- "#related_to [[Migrating embedded workflows]]"
- "#related_to [[Creating settings page with Settings App API]]"
created: "2023-01-01"
---

Migrate an existing Ecommerce Bridge API integration
====================================================

[API keys will be sunsetted](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) on November 30th, 2022. If your Ecommerce Bridge integration uses API keys, you will need to update it to a [private app](/docs/api/migrate-an-api-key-integration-to-a-private-app), then implement the following API changes below. 

Migrating contact, product, deal & line items sync[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-contact-product-deal-line-items-sync)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Learn about the different APIs you can use for the contact, product, deal and line items sync. The respective API documentation includes details on relevant scope requirements.

*   For contact sync, you can instead use the [Contacts API](/docs/api/crm/contacts). Specifically, you can make `GET`, `POST`, `PATCH`, `DELETE` requests to `/crm/v3/objects/contacts`. 
*   For product sync, you can instead use the [Products API](/docs/api/crm/products?_ga=2.70552208.1464203463.1656084382-250228468.1656084382). Specifically, you can make `GET`, `POST`, `PATCH`, `DELETE` requests to `/crm/v3/objects/products`. 
*   For deal sync, you can instead use the [Deals API](/docs/api/crm/deals?_ga=2.70552208.1464203463.1656084382-250228468.1656084382). Specifically, you can use make `GET`, `POST`, `PATCH`, `DELETE` requests to `/crm/v3/objects/deals`.
*   For line item sync you can instead use the [Line Items API](/docs/api/crm/line-items?_ga=2.70552208.1464203463.1656084382-250228468.1656084382). Specifically, you can make `GET`, `POST`, `PATCH`, `DELETE` requests to `/crm/v3/objects/line_items`. 

In addition to creating and maintaining these objects, you will also need to establish the relationships between them using the [Associations API](/docs/api/crm/associations?_ga=2.70552208.1464203463.1656084382-250228468.1656084382). You can create associations by making a `PUT` request to `/crm/v3/objects/associations`. For example, you associate contacts to deals, or line items to deals and products.    

The above APIs do not automatically retry if they return errors. If your integration experiences errors interacting with the above APIs your system will need to retry API calls.

**Please note:** when using the products, deals, and line items API, deduplication will not happen automatically. When you create an object using one of these APIs, you should record the ID so you know when to update existing products, deals, or line items instead of creating new ones. 

Migrating the external object id[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-the-external-object-id)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The Ecommerce Bridge API used the `externalObjectId` field to sync objects. Moving forward, you should maintain the HubSpot record IDs for each record in your internal system.

For product, deals, and line items, you can also [create a unique identifier](/docs/api/crm/understanding-the-crm) for your records and use this identifier when creating and updating records. When creating this unique identifier, make sure to set the `hasUniqueValue` field to `true` so that any records created in the future will not have the same value. Learn more about [creating unique identifiers](/docs/api/crm/understanding-the-crm). 

Migrating ecommerce properties[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-ecommerce-properties)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Any properties prefixed with  _ip\_\_ecomm\_bridge\_\__ will remain in existing users' HubSpot accounts, but for net new integrations, developers will need to use the [Properties API](/docs/api/crm/properties)to define their own properties.

The following properties were created automatically in your account when using the Ecommerce Bridge API:

Contact

*   Ecommerce contact
*   Source store

Deal 

*   Abandoned cart URL
*   Discount savings
*   Ecommerce deal
*   Order number
*   Shipment IDs
*   Source store
*   Tax price

Product

*   Ecommerce product
*   Image URL
*   Source store

Migrating import API[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-import-api)
-----------------------------------------------------------------------------------------------------------------------------------------

For import, you can instead use the [Import API](https://developers.hubspot.com/docs/api/crm/imports). Specifically, you can make a `POST` request to `/crm/v3/imports/`. 

Migrating ecommerce pipeline[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-ecommerce-pipeline)
---------------------------------------------------------------------------------------------------------------------------------------------------------

Pipelines are a [paid feature](https://legal.hubspot.com/hubspot-product-and-services-catalog). With this sunset, there will no longer be an option to create a _free_ ecommerce pipeline in every account. Moving forward, ecommerce pipelines can only be created in accounts that have not reached its pipeline limit. If the ecommerce pipeline has already been created in a user's account, when the API is sunsetted that pipeline will **not be removed**. Developers should use the [Pipeline API](/docs/api/crm/pipelines?_ga=2.162876860.1464203463.1656084382-250228468.1656084382) to find all existing pipelines and continue to sync deals in that existing pipeline. Specifically, you can make a `GET` request to `/crm/v3/pipelines/deal`. 

Or, you can store the ecommerce tag or pipeline name in a property on the deal record. 

**Please note:** if you attempt to create a pipeline in a free account, you will receive the following error: `context:{maximum pipelines:["1" ]},category:"API_LIMIT"}.`

Migrating VAST email templates[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-vast-email-templates)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

HubSpot sunsetted VAST email templates in 2021. As a result, these templates will also be sunsetted for the Ecommerce Bridge API.  

### New customer email template[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#new-customer-email-template)

If you're a Marketing Hub Professional or Enterprise user, you can add the [product module in-app](https://knowledge.hubspot.com/email/add-a-product-module-to-your-marketing-email) to marketing emails. Or you can create a coded file with the email template type using the [Template overview documentation](https://developers.hubspot.com/docs/cms/building-blocks/templates#email). Make sure to publish the email template so it is available to use when creating emails. 

### Re-engaging email template[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#re-engaging-email-template)

You can create a coded file with the email template type using this [Template overview documentation](https://developers.hubspot.com/docs/cms/building-blocks/templates#email).

### Abandon cart email template[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#abandon-cart-email-template)

The [_Abandoned cart_ module](https://knowledge.hubspot.com/email/add-a-product-module-to-your-marketing-email#add-an-abandoned-cart-module) only works when using the [Shopify integration](https://knowledge.hubspot.com/integrations/connect-hubspot-and-shopify), and is not currently supported when building a custom integration.

Migrating the ecommerce dashboard[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-the-ecommerce-dashboard)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

The ecommerce dashboard and template will be sunsetted for **net new users**. Accounts that already have a ecommerce dashboard or the ecommerce dashboard template can still use it, but can no longer create an ecommerce template via open APIs. 

Moving forward, learn how to build [reports](https://knowledge.hubspot.com/reports/create-reports-with-the-custom-report-builder?_ga=2.137773616.1464203463.1656084382-250228468.1656084382) and [dashboards](https://knowledge.hubspot.com/dashboards/manage-your-dashboards?_ga=2.137773616.1464203463.1656084382-250228468.1656084382) in HubSpot.

Migrating embedded workflows[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#migrating-embedded-workflows)
---------------------------------------------------------------------------------------------------------------------------------------------------------

The _Customer welcome_, _Abandon cart_, and _Re-engaging customer_ embedded workflow, will also be sunsetted. 

To create workflows, you can instead use the [Create & Manage Workflows API](https://legacydocs.hubspot.com/docs/methods/workflows/v3/create_workflow?_ga=2.95759772.1464203463.1656084382-250228468.1656084382). Specifically, you can make a POST request to `/automation/v3/workflows`. 

**Please note:** you cannot recreate the abandon cart workflow using the workflows API because it does not support deal-based workflows. 

Ecommerce settings page in app[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#ecommerce-settings-page-in-app)
-------------------------------------------------------------------------------------------------------------------------------------------------------------

The _Ecommerce_ navigation item in the side menu and the ecommerce settings page will be sunsetted.   
![ecomm](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/ecomm.png?width=512&name=ecomm.png)As partners move their integrations to public apps, their apps will then be listed on the _Connected Apps_ page.

![list-of-apps](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/list-of-apps.png?width=512&name=list-of-apps.png)

If developers would like to have a settings page for their integration they can build one using the [Settings App API](/docs/api/create-an-app-settings-page?_ga=2.95759772.1464203463.1656084382-250228468.1656084382)**.** 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/migrate-an-existing-ecommerce-bridge-api-integration#page-feedback)
---------------------------------------------------------------------------------------------------------------------------------

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