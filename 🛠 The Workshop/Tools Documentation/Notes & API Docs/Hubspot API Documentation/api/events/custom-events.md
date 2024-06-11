---
title: "Custom Events in HubSpot"
description: "Enables you to define and track events that are unique to your business, such as events on your site or in an app. You can configure events to store information within properties, which you can then use across HubSpot's tools."
type: "event"
tags:
- "Custom Events"
- "HubSpot Analytics"
- "Event Tracking"
relationships:
- "#related_to [[Marketing Hub]]"
- "#related_to [[Sales Hub]]"
- "#related_to [[Service Hub]]"
- "#related_to [[Operations Hub]]"
applicable_products:
- "Enterprise Marketing Hub"
- "Enterprise Sales Hub"
- "Enterprise Service Hub"
- "Enterprise Operations Hub"
founded: "N/A"
tags:
- "Marketing"
- "Sales"
- "Service"
- "Operations"
created_date: "YYYY-MM-DD # Replace with actual creation date if available"
---

**Custom events**
=================

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

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

Custom events enable you to define and track events that are unique to your business, such as events on your site or in an app. You can configure events to store information within properties, which you can then use across HubSpot's tools. 

To send [custom event](/docs/api/analytics/events) data to HubSpot, you first need to define the event. This is similar to custom CRM objects, where you first need to define the custom object before you can create individual records for that object. An event definition includes details such as its metadata, CRM object associations, and properties.

Below, learn more about creating and managing event definitions using the API. To learn how to create event definitions without using the API, check out [HubSpot's Knowledge Base](https://knowledge.hubspot.com/analytics-tools/create-custom-behavioral-events-with-the-code-wizard).

Create an event definition[](https://developers.hubspot.com/docs/api/events/custom-events#create-an-event-definition)
---------------------------------------------------------------------------------------------------------------------

To create the custom event schema, make a `POST` request to `events/v3/event-definitions`. In the request body, include definitions for your event schema, including its label, name, CRM object associations, and custom properties.

Below is an example request body along with parameter definitions. For a full example, view the [custom event example below](#custom-event-example).

<table class="p-table" style="border-collapse: collapse; table-layout: fixed; margin-left: auto; margin-right: auto; width: 100%;"><tbody><tr><td style="padding: 10px 4px;"><code>label</code> &nbsp;<strong>string</strong> (required)<p>The event's human readable label, which will display in HubSpot (up to 100 characters). Long labels may be cut off in certain parts of HubSpot's UI.</p></td></tr><tr><td style="padding: 10px 4px;"><code>name</code> &nbsp;<strong>string</strong><p>The unique, internal name of the event, which you'll use to reference the event through the API. If no value is provided, HubSpot will automatically generate one based on the <code>label</code>. This property <span style="text-decoration: underline;">cannot</span> be changed after the event definition is created.</p><p>Note the following naming requirements:&nbsp;</p><ul><li>This property can only contain lowercase letters, numbers, underscores, and hyphens (up to 50 characters).</li><li>The first character must be a letter.</li></ul></td></tr><tr><td style="padding: 10px 4px;"><code>description</code> &nbsp;<strong>string</strong><p>The event's description, which will display in HubSpot.</p></td></tr><tr><td style="padding: 10px 4px;"><code>primaryObject</code> &nbsp;<strong>string</strong><p>The CRM object that the event will be associated with. Event completions will display on CRM record timelines of the specified object. Can be one of <code>CONTACT</code>, <code>COMPANY</code>, <code>DEAL</code>, <code>TICKET</code> or <code>CUSTOM OBJECT NAME</code>.</p><p>If no value is provided, HubSpot will automatically associate the event with contacts. This <span style="text-decoration: underline;">cannot</span> be changed after the event definition is created.</p></td></tr><tr><td style="padding: 10px 4px;"><code>propertyDefinitions</code> &nbsp;<strong>array</strong><p>For each custom event definition, HubSpot provides a set of default properties that you can use when sending event data. Include this array to define any custom properties that your event needs outside of those default properties. You can include up to 50 custom properties per event.</p><p>For each property, include:</p><ul><li><code>label</code>: the property's in-app label.</li><li><code>name</code>: the property's internal name, which you'll use when sending property data through the API.</li><li><code>type</code>: the <a href="#custom-property-types" rel="noopener">type of property</a>. Default is <code>string</code>.</li><li><code>options</code>: for <code>enumeration</code> properties, the array of pre-defined values, including a <code>label</code> and <code>value</code> for each.</li><li><code>description</code>: optional text to describe the property.</li></ul><p>Learn more about <a href="#event-properties" rel="noopener">custom event properties</a> below.</p></td></tr></tbody></table>

// Example POST request body { "label": "My event label", "name": "unique\_event\_name", "description": "An event description that helps users understand what the event tracks.", "primaryObject": "COMPANY", "propertyDefinitions": \[ { "name": "choice-property", "label": "Choice property", "type": "enumeration", "options": \[ { "label": "Option 1", "value": "1" }, { "label": "Option 2", "value": "2" } \] }, { "name": "string-property", "label": "String property", "type": "string" } \] }

Event properties[](https://developers.hubspot.com/docs/api/events/custom-events#event-properties)
-------------------------------------------------------------------------------------------------

Custom event properties are used to store information on individual custom event completions. These properties should be used when appropriate for sending event completions, but they are not required for an event completion to be valid. For each event definition, HubSpot provides a default set of 32 properties. In addition, You can create up to 50 custom properties per event definition.

Properties can be of the following types:

*   `string`: a property that receives plain text strings. If the property name contains the words `url`, `referrer`, or `link`, the property value can be up to 1024 characters. Otherwise, property values can be up to 256 characters.
*   `number`: a property that receives numeric values with up to one decimal.
*   `enumeration`: A property with pre-defined options. When creating this property type, include an `options` array to set the available values.
*   `datetime`: A property that receives epoch millisecond or ISO8601 values representing a timestamp.

Below, learn about HubSpot's default event properties, how to [define new properties for existing events](#define-new-properties), and how to [update existing custom event properties](#update-existing-custom-properties).

### HubSpot's default event properties[](https://developers.hubspot.com/docs/api/events/custom-events#hubspot-s-default-event-properties)

*   `hs_asset_description`
*   `hs_asset_type`
*   `hs_browser`
*   `hs_campaign_id`
*   `hs_city`
*   `hs_country`
*   `hs_device_name`
*   `hs_device_type`
*   `hs_element_class`
*   `hs_element_id`
*   `hs_element_text`
*   `hs_language`
*   `hs_link_href`
*   `hs_operating_system`
*   `hs_operating_version`
*   `hs_page_content_type`
*   `hs_page_id`
*   `hs_page_title`
*   `hs_page_url`
*   `hs_parent_module_id`
*   `hs_referrer`
*   `hs_region`
*   `hs_screen_height`
*   `hs_screen_width`
*   `hs_touchpoint_source`
*   `hs_tracking_name`
*   `hs_user_agent`
*   `hs_utm_campaign`
*   `hs_utm_content`
*   `hs_utm_medium`
*   `hs_utm_source`
*   `hs_utm_term`

### Define new properties[](https://developers.hubspot.com/docs/api/events/custom-events#define-new-properties)

To define a new property on an existing custom event, make a `POST` request to `events/v3/event-definitions/{eventName}/property`. In the request body, include the definition for your property.

// { "name": "property-name", "label": "Property name", "type": "enumeration", "options": \[ { "label": "label", "value": "value" } \] }

When naming your property, keep the following in mind:

*   Once you create a property, the property’s name cannot be changed.
*   The name can only contain lowercase letters, numbers, underscores, and hyphens.
*   The first character of the property name must be a letter.
*   The property name and label can each be up to 50 characters long.
*   If an property name is not provided, one will be auto-generated using the property label.
*   Long labels may be cut off in certain parts of the HubSpot UI.

### Update existing custom properties[](https://developers.hubspot.com/docs/api/events/custom-events#update-existing-custom-properties)

To update an existing property on a custom event, make a `PATCH` request to `events/v3/event-definitions/{eventName}/property`. The only fields that can be updated on a property are the `label`, `description`, and `options` for enumeration properties. 

**Please note:** to change the type of property, use the `DELETE` endpoint to delete the property and recreate it with the correct type.

### Delete a property[](https://developers.hubspot.com/docs/api/events/custom-events#delete-a-property)

To delete an existing property on a custom event, make a `DELETE` request to `events/v3/event-definitions/{eventName}/property/{propertyName}`. 

When a property is deleted, it will no longer be available for use in future event completions. Past completions will still have the property values.  

**Please note:** when deleting an event:

1.  All of the events for that event definition will be deleted and unrecoverable.
2.  Previously deleted `eventName`'s cannot be used again. 

Update an event[](https://developers.hubspot.com/docs/api/events/custom-events#update-an-event)
-----------------------------------------------------------------------------------------------

The only fields that can be updated on an event definition are the `label` and `description`.

To update an existing custom event schema, make a `PATCH` request to `events/v3/event-definitions/{eventName}`.

Delete an event[](https://developers.hubspot.com/docs/api/events/custom-events#delete-an-event)
-----------------------------------------------------------------------------------------------

When you delete a custom event, references to that event in other HubSpot tools, such as workflows and reports, will no longer use the event.

To delete a custom event, make a `DELETE` request to `events/v3/event-definitions/{eventName}`.

Get existing event definitions[](https://developers.hubspot.com/docs/api/events/custom-events#get-existing-event-definitions)
-----------------------------------------------------------------------------------------------------------------------------

To fetch a single event definition, make a `GET` request to `events/v3/event-definitions/{eventName}`. 

To search event definitions by specific criteria, make a `GET` request to `events/v3/event-definitions`. You can supply the following query parameters to refine your search:

*   `searchString`: searches for events that contain the specified characters in the `name` field. Searching is not fuzzy, but is instead a naive _contains_ search.
*   `after`: a hashed string provided in paged responses for viewing the next page of search results.
*   `limit`: the maximum number of results to return.
*   `includeProperties`: a boolean value that specifies whether to include event properties in the returned results.

Custom event example[](https://developers.hubspot.com/docs/api/events/custom-events#custom-event-example)
---------------------------------------------------------------------------------------------------------

The following is a walkthrough of creating an example custom event.

This walkthrough covers:  
    1. creating a custom event definition.  
    2. creating a new property on the event definition.

Goal: a car dealership called CarSpot has an online inventory of all cars available on their lot. CarSpot wants to track when visitors to their site view a specific car available on their lot. To do so, they'll create a custom event, which they'll associate with contact records to track who views the listing. This event will also need a set of custom properties to store the car listing details viewed during each event.

### Create custom event definition[](https://developers.hubspot.com/docs/api/events/custom-events#create-custom-event-definition)

Having decided what to call the event, what properties they'd like to include with each triggered event, and the CRM object they want to associate events with, they'll create the event schema by making a `POST` request to `/events/v3/event-definitions` with the following request body:

///Example request body for event definitions { "label": "Viewed Car", "name": "viewed\_car", "description": "An event that fires when visitor views a car listing in the online inventory", "primaryObject": "CONTACT", "propertyDefinitions": \[ { "name": "condition", "label": "Condition", "type": "enumeration", "options": \[ { "label": "New", "value": "new" }, { "label": "Used", "value": "used" } \] }, { "name": "year", "label": "Year", "type": "number" }, { "name": "make", "label": "Make", "type": "string" }, { "name": "model", "label": "Model", "type": "string" }, { "name": "mileage", "label": "Mileage", "type": "number" } \] }

### Create property on custom event definition[](https://developers.hubspot.com/docs/api/events/custom-events#create-property-on-custom-event-definition)

Just after implementing the event on their website, CarSpot decided that they want to see if listing price will influence click rate. To track this, they'll create a new property containing the price of the listing.

To define a new property, they'll make a `POST` request to `/events/v3/event-definitions/viewed_car/property` with the following request body:

///Example request body for creating a property { "name": "price", "label": "Price", "type": "number" }

With their custom event defined, they can now [send event data to HubSpot using this custom event definition](/docs/api/analytics/events). 

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/events/custom-events#page-feedback)
-------------------------------------------------------------------------------------------------

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