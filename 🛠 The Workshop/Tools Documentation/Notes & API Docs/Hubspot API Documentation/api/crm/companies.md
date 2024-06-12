---
title: "Companies in HubSpot CRM"
description: "Companies store information about organizations that interact with your business, allowing you to manage company records and sync data between HubSpot and other systems. Learn more about objects, records, properties, and associations APIs in the Understanding the CRM guide. For general information on managing your CRM database, refer to the Contacts User Guide."
type: "group"
tags:
- "CRM"
- "HubSpot"
- "Companies"
relationships:
- "#founded_by [[HubSpot]]"
- "#located_in [[United States]]"
created_date: "YYYY-MM-DD"
---

Companies 
========== 

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, companies store information about the organizations that interact with your business. The companies endpoints allow you to manage create and manage company records, as well as sync company data between HubSpot and other systems. 

Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](/docs-beta/crm/understanding-the-crm?_ga=2.21847609.341006870.1586180142-500942594.1573763828) guide. For more general information about objects and records in HubSpot, [learn how to manage your CRM database](https://knowledge.hubspot.com/contacts/a-guide-to-using-records?_ga=2.22901305.341006870.1586180142-500942594.1573763828)[.](//knowledge.hubspot.com/contacts-user-guide?utm_campaign=UserGuides&utm_source=Developers)

Create companies[](https://developers.hubspot.com/docs/api/crm/companies#create-companies)
------------------------------------------------------------------------------------------

To create new companies, make a `POST` request to `/crm/v3/objects/companies`.

In your request, include your company data in a properties object. You can also add an associations object to associate your new company with existing records (e.g., contacts, deals), or activities (e.g., meetings, notes).

### Properties[](https://developers.hubspot.com/docs/api/crm/companies#properties)

Company details are stored in company properties. There are [default HubSpot company properties](https://knowledge.hubspot.com/companies/hubspot-crm-default-company-properties), but you can also [create custom properties](https://knowledge.hubspot.com/contacts/manage-your-properties?_ga=2.135700019.341006870.1586180142-500942594.1573763828#create-custom-properties).

When creating a new company, you should include at least one of the following properties in your request: `name` or `domain`. It is recommended to always include `domain`, because domain names are the [primary unique identifier](https://knowledge.hubspot.com/crm-setup/deduplication-of-contacts-companies-deals-tickets#automatic-deduplication-in-hubspot)  to avoid duplicate companies in HubSpot. If a company has [multiple domains](https://knowledge.hubspot.com/companies/add-multiple-domain-names-to-a-company-record), you can add them through the API by using the `hs_additional_domains` field with semicolons separating each domain. For example: `"hs_additional_domains" : "domain.com; domain2.com; domain3.com"`.

To view all available properties, you can retrieve a list of your account's company properties by making a `GET` request to `/crm/v3/properties/companies`. Learn more about the the [properties API](/docs/api/crm/properties).

**Please note:** if you've included `lifecyclestage` in your request, values must refer to the lifecycle stage's internal name. The internal names of default stages are text values, and do not change even if you edit the stage's [label](https://knowledge.hubspot.com/crm-setup/manage-your-properties#:~:text=the%20properties%20settings.-,Label/Name%3A,-enter%20a%20unique)(e.g., `subscriber` or `marketingqualifiedlead`). The internal names of [custom stages](https://knowledge.hubspot.com/crm-setup/create-and-customize-lifecycle-stages) are numeric values. You can find a stage's internal ID in your [lifecycle stage settings,](https://knowledge.hubspot.com/crm-setup/create-and-customize-lifecycle-stages#:~:text=To%20edit%20a%20lifecycle%20stage%2C%20hover%20over%20the%20stage%20and%20click%20Edit.%20In%20the%20right%20panel%2C%20edit%20the%20Stage%20name%2C%20then%20click%20Edit%20lifecycle%20stage%20to%20confirm.%20Click%20the%20code%20codcode%20icon%20to%20view%20the%20stage%27s%20internal%20ID%2C%20which%20is%20used%20by%20integrations%20and%20APIs.) or by retrieving the lifecycle stage property via API.

For example, to create a new company, your request may look similar to the following:

///Example request body { "properties": { "name": "HubSpot", "domain": "hubspot.com", "city": "Cambridge", "industry": "Technology", "phone": "555-555-555", "state": "Massachusetts", "lifecyclestage": "51439524" } }

### Associations[](https://developers.hubspot.com/docs/api/crm/companies#associations)

When creating a new company, you can also associate the company with [existing records](https://knowledge.hubspot.com/crm-setup/associate-records) or [activities](https://knowledge.hubspot.com/crm-setup/associate-activities-with-records). In the associations object, include the following fields:

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record or activity that you want to associate the company with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the company and the other object or activity. Default association types are listed [here](/docs/api/crm/associations#association-type-id-values), or you can retrieve the value by making a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. Learn more about the [associations API](/docs/api/crm/associations).

 |

You can also include the `label` field to assign a [defined association label](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) that describes the association. Learn more about associating records via the [associations API](/docs/api/crm/associations).

For example, to associate a new company with an existing contact and email, your request would look like the following:

///Example request body { "properties": { "name": "HubSpot", "domain": "hubspot.com", "city": "Cambridge", "industry": "Technology", "phone": "555-555-555", "state": "Massachusetts", "lifecyclestage": "51439524" }, "associations": \[ { "to": { "id": 101 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 280 } \] }, { "to": { "id": 556677 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 185 } \] }\] }

Retrieve companies[](https://developers.hubspot.com/docs/api/crm/companies#retrieve-companies)
----------------------------------------------------------------------------------------------

You can retrieve companies individually or in batches.

*   To retrieve an individual company, make a `GET` request to `/crm/v3/objects/companies/{companyId}`.
*   To request a list of all companies, make a `GET` request to `/crm/v3/objects/companies`.

For these endpoints, you can include the following query parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If the requested company doesn't have a value for a property, it will not appear in the response.

 |
| 

`propertiesWithHistory`

 | 

A comma separated list of the current and historical properties to be returned in the response. If the requested company doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of objects to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](https://developers.hubspot.com/docs/api/crm/associations)

 |

*   To retrieve a batch of specific companies by record ID or a [custom unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties), make a `POST` request to `crm/v3/objects/companies/batch/read`. The batch endpoint cannot retrieve associations. Learn how to batch read associations with the [associations API](/docs/api/crm/associations).

For the batch read endpoint, you can also use the optional `idProperty` parameter to retrieve companies by a custom [unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID (`hs_object_id`), so the `idProperty` parameter is not required when retrieving by record ID. To use a custom unique value property to retrieve companies, you must include the `idProperty` parameter.

For example, to retrieve a batch of companies, your request could look like either of the following:

///Example request body with record ID { "properties": \[ "name", "domain" \], "inputs": \[ { "id": "56789" }, { "id": "23456" } \] }

///Example request body with a unique value property { "properties": \[ "name", "domain" \], "idProperty": "uniquepropertyexample", "inputs": \[ { "id": "abc" }, { "id": "def" } \] }

To retrieve companies with current and historical values for a property, your request could look like:

///Example request body with record ID (current and historical values) { "propertiesWithHistory": \[ "name" \], "inputs": \[ { "id": "56789" }, { "id": "23456" } \] }

Update companies[](https://developers.hubspot.com/docs/api/crm/companies#update-companies)
------------------------------------------------------------------------------------------

You can update companies individually or in batches. For existing companies, the company's record ID is a unique value that you can use to update the company via API.

To update an individual company by its company ID, make a `PATCH` request to `/crm/v3/objects/companies/{companyId}`, and include the data you want to update.

### Associate existing companies with records and activities[](https://developers.hubspot.com/docs/api/crm/companies#associate-existing-companies-with-records-and-activities)

To associate a company with other CRM records or an activity, make a `PUT` request to  `/crm/v3/objects/companies/{companyId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. 

To retrieve the `associationTypeId` value, refer to [this list](/docs/api/crm/associations#association-type-id-values) of default values, or make a `GET` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. 

Learn more about associating records with the [associations API](/docs/api/crm/associations).

### Remove an association[](https://developers.hubspot.com/docs/api/crm/companies#remove-an-association)

To remove an association between a company and a record or activity, make a `DELETE` request to the following URL: `/crm/v3/objects/companies/{companyId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`.

Pin an activity on a company record[](https://developers.hubspot.com/docs/api/crm/companies#pin-an-activity-on-a-company-record)
--------------------------------------------------------------------------------------------------------------------------------

You can pin an activity on a company record via API by including the `hs_pinned_engagement_id` field in your request. In the field, include the `id` of the activity to pin, which can be retrieved via the [engagements APIs](/docs/api/crm/engagements). You can pin one activity per record, and the activity must already be associated with the company prior to pinning.

To set or update a company's pinned activity, your request could look like:

///Example request body PATCH /crm/v3/objects/companies/{companyId} { "properties": { "hs\_pinned\_engagement\_id": 123456789 } }

You can also create a company, associate it with an existing activity, and pin the activity in the same request. For example:

///Example request body POST /crm/v3/objects/companies { "properties": { "domain": "example.com", "name": "Example Company", "hs\_pinned\_engagement\_id": 123456789 }, "associations": \[ { "to": { "id": 123456789 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 189 }\] }\] }

Delete companies[](https://developers.hubspot.com/docs/api/crm/companies#delete-companies)
------------------------------------------------------------------------------------------

You can delete companies individually or in batches, which will add the company to the recycling bin in HubSpot. You can later [restore the company within HubSpot](https://knowledge.hubspot.com/contacts/restore-deleted-contacts-companies-deals-or-tickets).

To delete an individual company by its ID, make a `DELETE` request to `/crm/v3/objects/companies/{companyId}`.

Learn more about batch deleting companies on the _Endpoints_ tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/companies#page-feedback)
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