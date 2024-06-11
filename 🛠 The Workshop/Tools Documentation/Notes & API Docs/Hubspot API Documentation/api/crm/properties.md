---
title: "CRM Properties and Custom Objects in HubSpot"
description: "Information on creating, managing, and using properties for CRM objects in HubSpot, including default properties, property groups, field types, unique identifier properties, calculation properties, retrieval of properties, updating values, checkbox type properties, user assignment, clearing values, and feedback."
type: "guide"
tags:
- "CRM"
- "HubSpot"
- "Properties"
- "Custom Objects"
relationships:
- "#related_to [[CrmObjects]]"
- "#part_of [[Data Management]]"
created_date: "YYYY-MM-DD # Replace with actual date of creation"
---

Properties
==========

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use properties to store information on CRM records. HubSpot provides a set of default properties for each CRM object, and you can also create and manage your own custom properties either [in HubSpot](https://knowledge.hubspot.com/crm-setup/manage-your-properties) or using the properties API. 

When creating properties, it’s important to consider how to architect your data. In many cases, creating custom properties for HubSpot's standard objects is the right course of action. However, there may be times when you'll need to create a separate [custom object](/docs/api/crm/crm-custom-objects) with its own set of properties.

Default properties[](https://developers.hubspot.com/docs/api/crm/properties#default-properties)
-----------------------------------------------------------------------------------------------

CRM objects are defined by a primary **type** and a set of **properties**. Each type has a unique set of standard properties, represented by a map of name-value pairs. 

Learn more about default properties for different objects:

*   [Contacts](https://knowledge.hubspot.com/contacts/hubspots-default-contact-properties)
*   [Companies](https://knowledge.hubspot.com/companies/hubspot-crm-default-company-properties)
*   [Deals](https://knowledge.hubspot.com/deals/hubspots-default-deal-properties)
*   [Tickets](https://knowledge.hubspot.com/tickets/hubspots-default-ticket-properties)
*   [Activities](https://knowledge.hubspot.com/properties/hubspots-default-activity-properties) (Calls, Emails, Meetings, Notes, Tasks)
*   [Leads](https://knowledge.hubspot.com/properties/hubspots-default-lead-properties)(_**Sales Hub**_ _Professional_ and Enterprise)

Property groups[](https://developers.hubspot.com/docs/api/crm/properties#property-groups)
-----------------------------------------------------------------------------------------

Property [groups](https://knowledge.hubspot.com/contacts/manage-your-properties#create-and-edit-property-groups) are used to group related properties. Any grouped properties will appear next to each other on HubSpot records. If your integration creates any custom object properties, a custom property group will make it easy to identify that data.

Property type and fieldType values[](https://developers.hubspot.com/docs/api/crm/properties#property-type-and-fieldtype-values)
-------------------------------------------------------------------------------------------------------------------------------

When creating or updating properties, both `type` and `fieldType` values are required. The `type` value determines the type of the property, i.e. a string or a number. The `fieldType` property determines how the property will appear in HubSpot or on a form, i.e. as a plain text field, a dropdown menu, or a date picker.

In the table below, learn about the available property `type` and corresponding  `fieldType` values.

Valid values for `type` field and compatible `fieldType` values
| `type` | Description | Valid `fieldType` values |
| --- | --- | --- |
| `bool` | A field containing binary options (e.g.,  `Yes` or `No`, `True` or `False`). | `booleancheckbox`,  `calculation_equation` |
| `enumeration` | A string representing a set of options, with options separated by a semicolon. | `booleancheckbox`, `checkbox`, `radio`, `select`, `calculation_equation` |
| `date` | A value representing a specific day, month, and year. Values must be represented in UTC time and can be formatted as [ISO 8601 strings or EPOCH-timestamps in milliseconds (i.e. midnight UTC).](/docs/api/faq#how-should-i-format-timestamps-for-hubspot-s-apis:~:text=How%20should%20I%20format%20timestamps%20for%20HubSpot%27s%20APIs%3F) | `date` |
| `dateTime` | A value representing a specific day, month, year and time of day. The HubSpot app will not display the time of day. Values must be represented in UTC time and can be formatted as [ISO 8601 strings or UNIX-timestamps in milliseconds.](/docs/api/faq#how-should-i-format-timestamps-for-hubspot-s-apis:~:text=How%20should%20I%20format%20timestamps%20for%20HubSpot%27s%20APIs%3F) | `date` |
| `string` | A plain text string, limited to 65,536 characters. | `file`, `text`, `textarea`, `calculation_equation`, `html`, `phonenumber` |
| `number` | A number value containing numeric digits and at most one decimal. | `number`, `calculation_equation` |
| `object_coordinates` | A text value used to reference other HubSpot objects, used only for internal properties. Properties of this type cannot be created or edited, and are not visible in HubSpot. | `text` |
| `json` | A text value stored as formatted JSON, used only for internal properties. Properties of this type cannot be created or edited, and are not visible in HubSpot. | `text` |

Valid values for `fieldType` include:

| Fieldtype | Description |
| --- | --- |
| 
`booleancheckbox`

 | 

An input that will allow users to selected one of either Yes or No. When used in a form, it will be displayed as a single checkbox. Learn how to [add a value to single checkbox properties](#add-values-to-checkbox-type-properties).

 |
| 

`calculation_equation`

 | 

A custom equation that can calculate values based on other property values and/or associations. Learn how to define [calculation properties](#create-calculation-properties).

 |
| 

`checkbox`

 | 

A list of checkboxes that will allow a user to select multiple options from a set of options allowed for the property. Learn how to [format values when updating multiple checkbox properties](#add-values-to-checkbox-type-properties).

 |
| 

`date`

 | 

A date value, displayed as a date picker.

 |
| 

`file`

 | 

Allows for a file to be uploaded on a record or via a form. Stores a file ID.

 |
| 

`html`

 | 

A string, rendered as sanitized html, that enables the use of a rich text editor for the property.

 |
| 

`number`

 | 

A string of numerals or numbers written in decimal or scientific notation.

 |
| 

`phonenumber`

 | 

A plain text string, displayed as a formatted phone number.

 |
| 

`radio`

 | 

An input that will allow users to select one of a set of options allowed for the property. When used in a form, this will be displayed as a set of radio buttons.

 |
| 

`select`

 | 

A dropdown input that will allow users to select one of a set of options allowed for the property.

 |
| 

`text`

 | 

A plain text string, displayed in a single line text input.

 |
| 

`textarea`

 | 

A plain text string, displayed as a multi-line text input.

 |

Create a property[](https://developers.hubspot.com/docs/api/crm/properties#create-a-property)
---------------------------------------------------------------------------------------------

To create a property, make a `POST` request to `/crm/v3/properties/{objectType}`. In your request body, include the following required fields:

*   `groupName`: the [property group](https://knowledge.hubspot.com/properties/organize-and-export-properties) the property will be in.
*   `name`: the internal name of the property (e.g., favorite\_food).
*   `label`: the name of the property as it appears in HubSpot (e.g., Favorite Food).
*   `type`: the [type](#type) of property.
*   `fieldType`: the [field type](#field-type) of the property.

For example, to create a contact property called _Favorite Food_, your request would look like:

/// Example request body POST crm/v3/properties/contacts { "groupName": "contactinformation", "name":"favorite\_food", "label": "Favorite Food", "type": "string", "fieldType": "text" }

Create unique identifier properties[](https://developers.hubspot.com/docs/api/crm/properties#create-unique-identifier-properties)
---------------------------------------------------------------------------------------------------------------------------------

When a record is created in HubSpot, a unique _Record ID_ (`hs_object_id`) is automatically generated and should be treated as a string. These IDs are unique only within that object, so there can be both a contact and company with the same ID. For contacts and companies, there are additional unique identifiers, including a contact's email address (`email`) and a company's domain name (`domain`).

In some cases, you want may to create your own unique identifier property so that you can't enter the same value for multiple records. You can have up to ten unique ID properties per object. To create a property requiring unique values via API:

*   Make a `POST` request to `/crm/v3/properties/{objectType}`.
*   In your request body, for the `hasUniqueValue` field, set the value to `true`.

/// Example request body { "groupName": "dealinformation", "name":"system\_a\_unique", "label": "Unique ID for System A", "hasUniqueValue": true, "type": "string", "fieldType": "text" }

Once you've created your unique ID property, you can use it in an API call to retrieve specific records. The request URL could look like this: `GET` [https://api.hubapi.com/crm/v3/objects/deals/abc?idProperty=system\_a\_unique](https://api.hubapi.com/crm/v3/objects/deals/unique_string?idProperty=system_a_unique). This will return the deal with the value of `abc` in the `system_a_unique` field.

You can then use this unique identifier property value to identify and update specific records in the same way you could use `hs_object_id`, `email` (contacts), or `domain` (companies).

Create calculation properties[](https://developers.hubspot.com/docs/api/crm/properties#create-calculation-properties)
---------------------------------------------------------------------------------------------------------------------

Calculation properties define a property value based on other properties within the same object record. They are defined using a formula, which may include operations like min, max, count, sum, or average. You can use the properties API to read or create calculation properties in your HubSpot account, using a field type of `calculation_equation` and a type of `number`, `bool`, `string`, or `enumeration`.

You can define the property's calculation formula with the `calculationFormula` field.

**Please note**: calculation properties created via API cannot be edited within HubSpot. You can only edit these properties via the properties API.

### Calculation property syntax[](https://developers.hubspot.com/docs/api/crm/properties#calculation-property-syntax)

Using `calculationFormula`, you can write your formula with arithmetic operators, comparison operators, logic operators, conditional statements, and other functions.

#### Literal syntax

*   **String literal**: constant strings can be represented with either single quotes (`'constant'`) or double quotes (`"constant"`).
*   **Number literal**: constant numbers can be any real numbers, and can include point notation. `1005` and `1.5589` are both valid constant numbers.
*   **Boolean literal**: constant booleans can be `true` or `false`.

#### Property syntax

*   **String property variables:** for an identifier string to be interpreted as a string property, it must be wrapped in the `string` function. For example, `string(var1)`will be interpreted as the value for the string property var1.
*   **Number property variables**: all identifiers will be interpreted as number property variables.  For example, `var1` will be interpreted as the value for the number property var1.
*   **Boolean property variables**: for an identifier to be interpreted as a bool property, it must be wrapped in the `bool` function. For example, the identifier `bool(var1)` will be interpreted as the value for the boolean property var1.

**Please note:** the language used is case sensitive for all types except strings. For example, `If A ThEn B` is exactly the same as `if a then b` but `'a'` is not the same as `'A'`. Spaces, tabs, and new lines will be used for tokenization but will be ignored.

#### Operators

Operators can be used with literal and property values. For arithmetic operators, you can use prefix notation to multiply, and parenthesis can be used to specify the order of operations.

| Operator | Description | Examples |
| --- | --- | --- |
| 
`+`

 | Add numbers or strings. | 

`property1 + 100`

 |
| 

`-`

 | Subtract numbers. | `property1 + 100 - property2` |
| 

`*`

 | Multiply numbers. | `10property1` \= `10 * property1` |
| 

`/`

 | Divide numbers. | `property1 * (100 - property2/(50 - property3))` |
| 

`<`

 | Checks if a value is less than another. Supported by number properties or constants. | `a < 100` |
| 

`>`

 | Checks if a value is greater than another. Supported by number properties or constants. | `a > 50` |
| 

`<=`

 | Checks if a value is less than or equal to another. Supported by number properties or constants. | `a <= b` |
| 

`>=`

 | Checks if a value is greater than or equal to another. Supported by number properties or constants. | 

`b>= c`

 |
| 

`=`

 | Checks if a value is equal to another. Supported by both numbers and strings. | `(a + b - 100c * 150.652) = 150-230b` |
| 

`equals`

 | Checks if a value is equal to another. Supported by both numbers and strings. | `a + b - 100.2c * 150 equals 150 - 230` |
| 

`!=`

 | Checks if a value is not equal to another. Supported by both numbers and strings. | `string(property1) != 'test_string'` |
| 

`or`

 | Checks if either or two values are true. | `a > b or b <= c` |
| 

`and`

 | Checks if both values are true. | `bool(a) and bool(c)` |
| 

`not`

 | Checks if none of the values are true. | `not (bool(a) and bool(c))` |

#### Functions

The following are supported functions:

Use this table to describe parameters / fields
| Function | Description | Examples |
| --- | --- | --- |
| 
`max`

 | Will have between 2 and 100 input numbers, and will return the maximum number out of all the inputs. | `max(a, b, c, 100)` or `max(a, b)` |
| 

`min`

 | Will have between 2 and 100 input numbers, and will return the minimum number of out all the inputs. | 

`min(a, b, c, 100)` or `min(a, b)`

 |
| 

`is_present`

 | Evaluates whether an expression can be evaluated. | 

`is_present(bool(a))`\= true if the property is boolean, but `is_present(bool(a))` = false if the property is empty or not boolean.

 |
| 

`contains`

 | Has two strings as inputs and will return true if the first input contains the second. | 

`contains('hello', 'ello')` = `true` while `contains('ello', 'hello')` = false.

 |
| 

`concatenate`

 | Joins a list of strings. The list of inputs can go from 2 up to 100. | 

`concatenate('a', 'b', string(a), string(b))`

 |

There are also two parsing functions:

*   `number_to_string`: tries to convert the input number expression to a string.
*   `string_to_number`: tries to convert the input string expression to a number.

For example, `"Number of cars: " + num_cars` is not a valid property because you can't add a string with a number, but `"Number of cars: " + number_to_string(num_cars)` is.

#### Conditional statements

You can also write your formula with conditional statements using `if`, `elseif`, `endif`, and `else`.

For example, a conditional statement could look like: `if boolean_expression then statement [elseif expression then statement]* [else statement | endif]` where the `[a]` brackets represent that a is optional, the `a|b` represent that either a or b will work, and `*` means 0 or more. `endif` can be used to finish a conditional statement prematurely, ensuring that the parser can identify which `if` the next `elseif` belongs to. 

### Example formulas

The following are examples you can use to help define your own calculation formulas:

//Example formula "calculationFormula": "closed - started"

A more advanced example with conditionals:

//Example formula "calculationFormula": "if is\_present(hs\_latest\_sequence\_enrolled\_date) then if is\_present(hs\_sequences\_actively\_enrolled\_count) an hs\_sequences\_actively\_enrolled\_count >= 1 then true else false else ''"

Retrieve properties[](https://developers.hubspot.com/docs/api/crm/properties#retrieve-properties)
-------------------------------------------------------------------------------------------------

You can retrieve information for individual properties or all properties within an object.

*   To retrieve an individual property, make a `GET` request to `crm/v3/properties/{object}/{propertyName}`. For example, to retrieve the Favorite Food property, your request URL would be https://  
    `api.hubspot.com/crm/v3/properties/contacts/favorite_food`.
*   To retrieve all properties for an object, make a `GET` request to `/crm/v3/properties/{objectType}`.

Update or clear a property's values[](https://developers.hubspot.com/docs/api/crm/properties#update-or-clear-a-property-s-values)
---------------------------------------------------------------------------------------------------------------------------------

To update a property value for a record, make a `PATCH` request to `crm/v3/objects/{objectType}/{recordId}`. In your request body, include the properties and their values in an array. Learn more about updating records via the [object APIs](/docs/api/crm/understanding-the-crm).

### Add values to checkbox type properties[](https://developers.hubspot.com/docs/api/crm/properties#add-values-to-checkbox-type-properties)

When updating values for a record's checkbox type properties, format the values in the following ways:

*   Boolean checkbox property: to display as _Yes_, or checked in HubSpot, your value must be `true`. To display as _No_ or not checked in HubSpot, your value must be `false`.
*   Multiple select checkbox property: to add or append values to a multiple checkboxes property, add a semicolon before the first value, and separate the values with semicolons without a space between. If the property has an existing value, the leading semicolon will append the values instead of overwriting the value. For example, a contact has the existing value `DECISION_MAKER`  for the `hs_buying_role` property. To add additional values without replacing the existing value, your request would look like this:

///Example body for PATCH request to /crm/v3/objects/contacts/{contactId} { "properties": { "hs\_buying\_role": ";BUDGET\_HOLDER;END\_USER" }}

### Assign record owners with user properties[](https://developers.hubspot.com/docs/api/crm/properties#assign-record-owners-with-user-properties)

When assigning users to CRM records via API, your value must be user's owner `id`, which you can find in your [property settings](https://knowledge.hubspot.com/crm-setup/manage-your-properties) or via the [owners API](/docs/api/crm/owners). For example, to assign a user as owner of a contact, send a `PATCH` request to `crm/v3/objects/contacts/{contactId}`,  with the body `{ "properties":{ "hubspot_owner_id": "41629779"}}`.

### Clear a property value[](https://developers.hubspot.com/docs/api/crm/properties#clear-a-property-value)

You can clear an object property value via the API by setting the property value to an empty string.

For example, to clear the `firstname` from a contact object, send a `PATCH` request to `https://api.hubapi.com/crm/v3/objects/contacts/{contactId}` with the body `{ "properties": { "firstname": ""}}`.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/properties#page-feedback)
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