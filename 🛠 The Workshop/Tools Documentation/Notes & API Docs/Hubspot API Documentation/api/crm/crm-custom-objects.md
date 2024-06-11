---
title: "Custom Objects in HubSpot CRM"
description: "A guide on creating, managing, and using custom objects within the HubSpot CRM to represent unique data structures for business needs."
type: "group"
tags:
- "CRM"
- "Customization"
- "HubSpot"
relationships:
- "#created_by [[CarSpot]]"
birthdate: "N/A"
deathdate: "N/A"
---

**Custom objects**
==================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Objects](#tab-2)[Object schema](#tab-3)

*   [Overview](#tab-1)
*   [Objects](#tab-2)
*   [Object schema](#tab-3)

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

In each HubSpot account, there are the standard CRM objects: contacts, companies, deals, and tickets. To represent and organize your CRM data based on your business needs, you can also create custom objects. You can [create a custom object](https://knowledge.hubspot.com/crm-setup/create-custom-objects) in HubSpot, or use the custom objects API to define custom objects, properties, and associations to other CRM objects. 

Below, learn how to create and manage custom objects through the API, and see a [walkthrough of creating an example custom object](#custom-object-example).

To learn more about creating custom objects, check out the following posts on the HubSpot developer blog:

*   [How to build scalable custom objects](/blog/how-to-think-like-an-architect-by-building-scalable-custom-objects)
*   [How to build custom objects using private apps](/blog/how-to-build-a-custom-object-using-private-apps)

**Please note:** custom objects are specific to each account, and depending on your subscription, there are limits on the number of custom objects you can create. Learn more about your limits in the [HubSpot Products & Services catalog](https://legal.hubspot.com/hubspot-product-and-services-catalog).

Authentication methods[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#authentication-methods)
---------------------------------------------------------------------------------------------------------------

You can create, read, and update custom objects using one of the following methods of authentication:

*   [OAuth](/docs/api/custom-objects-schema-pilot)
*   [Private app access tokens](/docs/api/private-apps#make-api-calls-with-your-app-s-access-token)

**Please note:** as of November 30, 2022, HubSpot API Keys are being deprecated and are no longer supported. Continued use of HubSpot API Keys is a security risk to your account and data. During this deprecation phase, HubSpot may deactivate your key at any time.

You should instead authenticate using a private app access token or OAuth. Learn more about [this change](https://developers.hubspot.com/changelog/upcoming-api-key-sunset) and how to [migrate an API key integration](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app) to use a private app instead.

Create a custom object[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#create-a-custom-object)
---------------------------------------------------------------------------------------------------------------

To create a custom object, you'll first need to define the object schema. The schema includes the object name, properties, and associations to other CRM objects. You can find the full schema request details in the _Object schema_ tab at the top of this article. You can also view a sample request in the [example walkthrough below](#custom-object-example).

To create the custom object schema, make a `POST` request to `crm/v3/schemas`. In the request body, include definitions for your object schema, including its name, properties, and associations.

When naming your custom object, keep the following in mind:

*   Once you create an object, its name and label cannot be changed.
*   The name can only contain letters, numbers, and underscores.
*   The first character of the name must be a letter.
*   Long labels may be cut off in certain parts of the product.

Below, read about the required definitions for the object's properties and associations. 

### Properties[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#properties)

The properties you define in the request body will be used to store information on individual custom object records.

**Please note:** you can have up to 10 [unique value properties](/docs/api/crm/understanding-the-crm#:~:text=Creating%20your%20own%20unique%20identifiers) for each custom object in your HubSpot account.

You'll use your defined properties to populate the following property-based fields:

*   **requiredProperties:** the properties that are required when creating a new custom object record.
*   **searchableProperties:** the properties that are indexed for searching in HubSpot.
*   **primaryDisplayProperty:** the property used for naming individual custom object records.
*   **secondaryDisplayProperties:** the properties that appear on individual records under the primaryDisplayProperty.  
    ![custom-object-secondary-display-properties0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-object-secondary-display-properties0.png?width=347&name=custom-object-secondary-display-properties0.png)
    *   The first property listed in `secondaryDisplayProperties` will be also added as a fourth filter on the object index page if it’s one of the following property types:
        *   `string`
        *   `number`
        *   `enumeration`
        *   `boolean`
        *   `datetime`  
            ![custom-object-dashboard-filter0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/custom-object-dashboard-filter0.png?width=889&name=custom-object-dashboard-filter0.png)
    *   To remove a display property from the UI, you'll need to first delete the property, then recreate it.

By default, when creating properties through the schema request, property `type` is set to `string`, and the `fieldType` is set to `text`. Below are the values you can use to create different types of properties.

Valid values for `type`
| `type` | Description | Valid `fieldType` values |
| --- | --- | --- |
| `enumeration` | A string representing a set of options, separated by semicolons.  | `booleancheckbox`, `checkbox`, `radio`, `select` |
| `date` | An [ISO 8601 formatted value](https://en.wikipedia.org/wiki/ISO_8601) representing a specific day, month, and year. | `date` |
| `dateTime` | An [ISO 8601 formatted value](https://en.wikipedia.org/wiki/ISO_8601) representing a specific day, month, year and time of day. The HubSpot app will not display the time of day. | `date` |
| `string` | A plain text strings, limited to 65,536 characters. | `file`, `text`, `textarea` |
| `number` | A number value containing numeric digits and at most one decimal. | `number` |

Valid values for `fieldType` 
| `fieldType` | Description |
| --- | --- |
| `booleancheckbox` | An input that will allow users to select one of either Yes or No. When used in a form, it will be displayed as a single checkbox. |
| `checkbox` | A list of checkboxes that will allow a user to select multiple options from a set of options allowed for the property. |
| `date` | A date value, displayed as a date picker. |
| `file` | Allows for a file to be uploaded to a form. Stored and displayed as a URL link to the file. |
| `number` | A string of numerals or numbers written in decimal or scientific notation. |
| `radio` | An input that will allow users to select one of a set of options allowed for the property. When used in a form, this will be displayed as a set of radio buttons. |
| `select` | A dropdown input that will allow users to select one of a set of options allowed for the property. |
| `text` | A plain text string, displayed in a single line text input. |
| `textarea` | A plain text string, displayed as a multi-line text input. |

### Associations

HubSpot will automatically associate a custom object with the emails, meetings, notes, tasks, calls, and conversations objects. You can further associate your custom object with other standard HubSpot objects or other custom objects.

When creating associations through the create schema request, identify standard objects using their name and custom objects using their `objectTypeId` value_. For example:_ 

// Example associatedObjects array "associatedObjects": \[ "CONTACT", "COMPANY", "TICKET", "DEAL", "2-3453932" \]

Retrieve existing custom objects[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#retrieve-existing-custom-objects)
-----------------------------------------------------------------------------------------------------------------------------------

To retrieve all custom objects, make a `GET` request to `/crm/v3/schemas`.

To retrieve a specific custom object, make a `GET` request to one of the following endpoints:

*   `/crm/v3/schemas/{objectTypeId}`
*   `/crm/v3/schemas/p_{object_name}`
*   `/crm/v3/schemas/{fullyQualifiedName}`. You can find an object's
    
    `fullyQualifiedName` in its schema, which is derived from `p{portal_id}_{object_name}`. You can find your account's portal ID using the [account information API.](/docs/api/settings/account-information-api)
    

For example, for an account with an ID of `1234` and an object named `lender`, your request URL could look like any of the following:

*   `https://api.hubapi.com/crm/v3/schemas/2-3465404`
*   `https://api.hubapi.com/crm/v3/schemas/p_lender`
*   `[https://api.hubapi.com/crm/v3/schemas/p1234_lende](https://api.hubapi.com/crm/v3/schemas/p1234_lender)`

Retrieve custom object records[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#retrieve-custom-object-records)
-------------------------------------------------------------------------------------------------------------------------------

You can also retrieve a custom object's records.

*   To retrieve a specific record by its record ID value, make a `GET` request to `crm/v3/objects/{objectType}/{recordId}`.

For this endpoint, you can include the following query parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned in the response. If the requested custom object record doesn't have a value for a property, it will not appear in the response.

 |
| 

`propertiesWithHistory`

 | 

A comma separated list of the current and historical properties to be returned in the response. If the requested custom object record doesn't have a value for a property, it will not appear in the response.

 |
| 

`associations`

 | 

A comma separated list of objects to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](https://developers.hubspot.com/docs/api/crm/associations)

 |

*   To retrieve multiple records, make a `POST` request to `crm/v3/objects/{objectType}/batch/read`. The batch endpoint cannot retrieve associations. Learn how to batch read associations with the [associations API](/docs/api/crm/associations).

In your request, you can retrieve records by their record ID (`hs_object_id`), or by a custom [unique identifier property](/docs/api/crm/properties#create-unique-identifier-properties). By default, the `id` values in the request refer to the record ID, so the `idProperty` parameter is not required when retrieving by record ID. To use a custom unique value property, you must include the `idProperty` parameter.  

For example, to retrieve a batch of custom object records, your request could look like either of the following:

///Example request body for record ID { "properties": \[ "petname" \], "inputs": \[ { "id": "12345" }, { "id": "67891" } \] }

///Example request body for unique value property { "properties": \[ "petname" \], "idProperty": "uniquepropertyexample", "inputs": \[ { "id": "abc" }, { "id": "def" } \] }

To retrieve custom object records with current and historical values for a property, your request could look like:

///Example request body for record ID (current and historical values) { "propertiesWithHistory": \[ "pet\_owner" \], "inputs": \[ { "id": "12345" }, { "id": "67891" } \] }

Update existing custom objects[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#update-existing-custom-objects)
-------------------------------------------------------------------------------------------------------------------------------

To update an object's schema, make a `PATCH` request to `https://api.hubapi.com/crm/v3/schemas/_{objectTypeId}_`.

Once your custom object is defined:

*   The object's name and labels (singular and plural) cannot be changed.
*   The `requiredProperties`, `searchableProperties`, `primaryDisplayProperty`, and `secondaryDisplayProperties` can be changed by updating the object's schema. To set a new property as a required, searchable, or display property, you need to create the property prior to updating the schema.
*   You can create and edit custom object properties either [in HubSpot](https://knowledge.hubspot.com/crm-setup/manage-your-properties#view-and-edit-properties) or via the [properties API](/docs/api/crm/properties). 

### Update associations

To add other object associations to your custom object, make a `POST` request to `/crm/v3/schemas/_{objectTypeId}_/associations`.

You can only associate your custom object with standard HubSpot objects (e.g. _contact_, _company_, _deal_, or _ticket) or other custom objects_. In the `toObjectTypeId` field, identify custom objects by their `objectTypeId` value and standard objects by their name. For example:

// Example association request body { "fromObjectTypeId": "2-3444025", "toObjectTypeId": "ticket", "name": "cat\_to\_ticket" }

Delete a custom object[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#delete-a-custom-object)
---------------------------------------------------------------------------------------------------------------

You can only delete a custom object after all object instances of that type are deleted. To delete a custom object, make a `DELETE` request to `/crm/v3/schemas/{objectType}`.

If you need to create a new custom object with the same name as the deleted object, you must hard delete the schema by making a `DELETE` request to `/crm/v3/schemas/{objectType}?archived=true`. You can only delete a custom object type after all object instances of that type, associations, and custom object properties are deleted.

Custom object example[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#custom-object-example)
-------------------------------------------------------------------------------------------------------------

The following is a walkthrough of creating an example custom object. For full details of the requests shown, view the Object Definition tab at the top of the article.

This walkthrough covers:

1.  creating a custom object schema.
2.  creating a custom object record.
3.  associating a custom object record with a HubSpot contact.
4.  creating a new association definition between the custom object and HubSpot ticket.
5.  creating a new property definition.
6.  updating the object schema (i.e. `secondaryDisplayProperties`) with the new property.  
    
    * * *
    

Goal: a car dealership called CarSpot wants to store their inventory in HubSpot using a custom object. To track vehicle ownership and purchases, they'll associate cars with contact records. Along the way, they'll also track vehicle maintenance using HubSpot tickets and custom properties.

### Creating the object schema

CarSpot needs to create an object schema that can represent the following attributes as properties: 

1.  **Condition (new or used):** enumeration
2.  **Date received at dealership:** date
3.  **Year:** number
4.  **Make:** string
5.  **Model:** string
6.  **VIN:** string (unique value)
7.  **Color:** string
8.  **Mileage:** number
9.  **Price:** number
10.  **Notes:** string

They'll also add a description to provide context about how to use the object, and define an association between their custom object and the standard contacts object so that they can connect cars to potential buyers. 

With their data model finalized, they'll create the object schema by making a `POST` request to `/crm/v3/schemas` with the following request body:all

// Example POST request to https://api.hubspot.com/crm/v3/schemas { "name": "cars", "description": "Cars keeps track of cars currently or previously held in our inventory.", "labels": { "singular": "Car", "plural": "Cars" }, "primaryDisplayProperty": "model", "secondaryDisplayProperties": \[ "make" \], "searchableProperties": \[ "year", "make", "vin", "model" \], "requiredProperties": \[ "year", "make", "vin", "model" \], "properties": \[ { "name": "condition", "label": "Condition", "type": "enumeration", "fieldType": "select", "options": \[ { "label": "New", "value": "new" }, { "label": "Used", "value": "used" } \] }, { "name": "date\_received", "label": "Date received", "type": "date", "fieldType": "date" }, { "name": "year", "label": "Year", "type": "number", "fieldType": "number" }, { "name": "make", "label": "Make", "type": "string", "fieldType": "text" }, { "name": "model", "label": "Model", "type": "string", "fieldType": "text" }, { "name": "vin", "label": "VIN", "type": "string", "hasUniqueValue": true, "fieldType": "text" }, { "name": "color", "label": "Color", "type": "string", "fieldType": "text" }, { "name": "mileage", "label": "Mileage", "type": "number", "fieldType": "number" }, { "name": "price", "label": "Price", "type": "number", "fieldType": "number" }, { "name": "notes", "label": "Notes", "type": "string", "fieldType": "text" } \], "associatedObjects": \[ "CONTACT" \] }

After creating the object schema, CarSpot makes sure to note the new object's `{objectTypeId}` field, as they'll use this for fetching and updating the object later. They can also use the `{fullyQualifiedName}` value, if they prefer.

### _Creating a custom object record_

_With the custom object created, CarSpot can now create records on the object for each car in their inventory._

_They'll create their first car by making a `POST` request to `/crm/v3/objects/2-3465404` with the following request body:_

// Example POST request to https://api.hubspot.com/crm/v3/objects/2-3465404 { "properties": { "condition": "used", "date\_received": "1582416000000", "year": "2014", "make": "Nissan", "model": "Frontier", "vin": "4Y1SL65848Z411439", "color": "White", "mileage": "80000", "price": "12000", "notes": "Excellent condition. No accidents." } }

The response for this API call would look similar to:Copy all

// Example response body { "id": "181308", "properties": { "color": "White", "condition": "used", "make": "Nissan", "mileage": "80000", "model": "Frontier", "vin": "4Y1SL65848Z411439", "notes": "Excellent condition. No accidents.", "price": "12000", "year": "2014", "date\_received": "1582416000000" }, "createdAt": "2020-02-23T01:44:11.035Z", "updatedAt": "2020-02-23T01:44:11.035Z", "archived": false }

With the record created, they can use the `id` value to later associate the car with an existing contact.

If they wanted to later retrieve this record along with specific properties, they could make a `GET` request to `https://api.hubapi.com/crm/v3/objects/2-3465404/181308?portalId=1234567&properties=year&properties=make&properties=model`

### _Associating the custom object record to another record_

You can use the ID of the new car record (`181308`) and the ID of another record to associate a custom object record with a record of another object.

To create an association, make a `PUT` request to `/crm/v3/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}/{associationType}`. If the object relationship is already [defined](#defining-a-new-association), to determine the `associationType` value, make a `GET` request to `crm/v3/schemas/{objectType}`.

For example, with the contact _ID `51` and the association type `75`,_ CarSpot can associate the car record with a contact. Using the above IDs, the request URL will be constructed as follows:

`https://api.hubspot.com/crm/v3/objects/2-3465404/181308/associations/contacts/51/75`

### _Defining a new association_

CarSpot now wants to start tracking post-sale services for their cars. To do so, they'll use HubSpot tickets to log any maintenance performed.

To allow associations between cars and tickets, they'll create a new association by making a `POST` request to **`/crm/v3/schemas/2-3465404/associations`** with the following request body:

// Example POST request to https://api.hubspot.com/crm/v3/schemas/2-3465494/associations { "fromObjectTypeId": "2-3465404", "toObjectTypeId": "ticket", "name": "car\_to\_ticket" }

The response for this API call would look similar to:Copy all

// Example response { "id": "121", "createdAt": "2020-02-23T01:52:12.893826Z", "updatedAt": "2020-02-23T01:52:12.893826Z", "fromObjectTypeId": "2-3465404", "toObjectTypeId": "0-5", "name": "car\_to\_ticket" }

When creating a new association between two custom objects, specify the custom objects by their _objectTypeId_ in the _toObjectTypeId_ field. For standard objects, you can identify them by name or use the following values: 

*   **Contact:** 0-1
*   **Company:** 0-2
*   **Deal:** 0-3
*   **Ticket:** 0-5

### _Defining a new property_

As they continue to track maintenance, CarSpot sees an opportunity to bundle maintenance services into packages. To track these maintenance packages on individual car records, they'll create a new enumeration property containing the available packages.

To define a new property, they'll make a `POST` request to `/crm/v3/properties/2-3465404` with the following request body:

// Example POST request to https://api.hubspot.com/crm/v3/properties/2-3465404 { "groupName": "car\_information", "name": "maintenance\_package", "label": "Maintenance Package", "type": "enumeration", "fieldType": "select", "options": \[ { "label": "Basic", "value": "basic" }, { "label": "Oil change only", "value": "oil\_change\_only" }, { "label": "Scheduled", "value": "scheduled" } \] }

The response for this API call would look similar to:Copy all

// Example response { "updatedAt": "2020-02-23T02:08:20.055Z", "createdAt": "2020-02-23T02:08:20.055Z", "name": "maintenance\_package", "label": "Maintenance Package", "type": "enumeration", "fieldType": "select", "groupName": "car\_information", "options": \[ { "label": "Basic", "value": "basic", "displayOrder": -1, "hidden": false }, { "label": "Oil change only", "value": "oil\_change\_only", "displayOrder": -1, "hidden": false }, { "label": "Scheduled", "value": "scheduled", "displayOrder": -1, "hidden": false } \], "displayOrder": -1, "calculated": false, "externalOptions": false, "archived": false, "hasUniqueValue": false, "hidden": false, "modificationMetadata": { "archivable": true, "readOnlyDefinition": false, "readOnlyValue": false }, "formField": false }

Now that the property has been created, they want it to appear in the sidebar of each car record so that the information is readily available to their sales reps and technicians. To do this, they'll add the property to `secondaryDisplayProperties` by making a `PATCH` request to `/crm/v3/schemas/2-3465404` with the following request body: 

// Example PATCH request to https://api.hubspot.com/crm/v3/schemas/2-3465404 { "secondaryDisplayProperties": \[ "maintenance\_package" \] }

The response for this API call would look similar to:Copy all

// Example response { "id": "3465404", "createdAt": "2020-02-23T01:24:54.537Z", "updatedAt": "2020-02-23T02:12:24.175874Z", "labels": { "singular": "Car", "plural": "Cars" }, "requiredProperties": \[ "year", "model", "vin", "make" \], "searchableProperties": \[ "year", "model", "vin", "make" \], "primaryDisplayProperty": "model", "secondaryDisplayProperties": \[ "maintenance\_package" \], "portalId": 1234567, "name": "car" }

Now, when a technician opens a contact record that has an associated car, the property will be displayed in the custom object card in the sidebar:

![Screen Shot 2020-03-06 at 11.08.41 AM](https://developers.hubspot.com/hs-fs/hubfs/Screen%20Shot%202020-03-06%20at%2011.08.41%20AM.png?width=386&name=Screen%20Shot%202020-03-06%20at%2011.08.41%20AM.png)

As CarSpot continues to use HubSpot, they'll likely find ways to refine and expand this custom object and more using HubSpot's API. They might even decide to [build dynamic pages using their custom object data.](/docs/cms/guides/dynamic-pages/crm-objects)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#page-feedback)
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