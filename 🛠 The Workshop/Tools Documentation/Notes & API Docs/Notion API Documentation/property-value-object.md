JUMP TOCTRL-/

Notion API
----------

*   [Introduction](/reference/intro)
*   [Integration capabilities](/reference/capabilities)
*   [Request limits](/reference/request-limits)
*   [Status codes](/reference/status-codes)
*   [Versioning](/reference/versioning)
    *   [Changes by version](/reference/changes-by-version)

Objects
-------

*   [Block](/reference/block)
    *   [Rich text](/reference/rich-text)
*   [Page](/reference/page)
    *   [Page properties](/reference/page-property-values)
*   [Database](/reference/database)
    *   [Database properties](/reference/property-object)
*   [Parent](/reference/parent-object)
*   [User](/reference/user)
*   [Comment](/reference/comment-object)
*   [Unfurl attribute (Link Previews)](/reference/unfurl-attribute-object)
*   [File](/reference/file-object)
*   [Emoji](/reference/emoji-object)

Endpoints
---------

*   [Authentication](/reference/authentication)
    *   [Create a tokenpost](/reference/create-a-token)
*   [Blocks](/reference/patch-block-children)
    *   [Append block childrenpatch](/reference/patch-block-children)
    *   [Retrieve a blockget](/reference/retrieve-a-block)
    *   [Retrieve block childrenget](/reference/get-block-children)
    *   [Update a blockpatch](/reference/update-a-block)
    *   [Delete a blockdelete](/reference/delete-a-block)
*   [Pages](/reference/post-page)
    *   [Create a pagepost](/reference/post-page)
    *   [Retrieve a pageget](/reference/retrieve-a-page)
    *   [Retrieve a page property itemget](/reference/retrieve-a-page-property)
    *   [Update page propertiespatch](/reference/patch-page)
    *   [Trash a page](/reference/archive-a-page)
*   [Databases](/reference/create-a-database)
    *   [Create a databasepost](/reference/create-a-database)
    *   [Filter database entries](/reference/post-database-query-filter)
    *   [Sort database entries](/reference/post-database-query-sort)
    *   [Query a databasepost](/reference/post-database-query)
    *   [Retrieve a databaseget](/reference/retrieve-a-database)
    *   [Update a databasepatch](/reference/update-a-database)
    *   [Update database properties](/reference/update-property-schema-object)
*   [Users](/reference/get-users)
    *   [List all usersget](/reference/get-users)
    *   [Retrieve a userget](/reference/get-user)
    *   [Retrieve your token's bot userget](/reference/get-self)
*   [Comments](/reference/create-a-comment)
    *   [Create commentpost](/reference/create-a-comment)
    *   [Retrieve commentsget](/reference/retrieve-a-comment)
*   [Search](/reference/post-search)
    *   [Search by titlepost](/reference/post-search)
    *   [Search optimizations and limitations](/reference/search-optimizations-and-limitations)

JUMP TOCTRL-/

Notion API
----------

*   [Introduction](/reference/intro)
*   [Integration capabilities](/reference/capabilities)
*   [Request limits](/reference/request-limits)
*   [Status codes](/reference/status-codes)
*   [Versioning](/reference/versioning)
    *   [Changes by version](/reference/changes-by-version)

Objects
-------

*   [Block](/reference/block)
    *   [Rich text](/reference/rich-text)
*   [Page](/reference/page)
    *   [Page properties](/reference/page-property-values)
*   [Database](/reference/database)
    *   [Database properties](/reference/property-object)
*   [Parent](/reference/parent-object)
*   [User](/reference/user)
*   [Comment](/reference/comment-object)
*   [Unfurl attribute (Link Previews)](/reference/unfurl-attribute-object)
*   [File](/reference/file-object)
*   [Emoji](/reference/emoji-object)

Endpoints
---------

*   [Authentication](/reference/authentication)
    *   [Create a tokenpost](/reference/create-a-token)
*   [Blocks](/reference/patch-block-children)
    *   [Append block childrenpatch](/reference/patch-block-children)
    *   [Retrieve a blockget](/reference/retrieve-a-block)
    *   [Retrieve block childrenget](/reference/get-block-children)
    *   [Update a blockpatch](/reference/update-a-block)
    *   [Delete a blockdelete](/reference/delete-a-block)
*   [Pages](/reference/post-page)
    *   [Create a pagepost](/reference/post-page)
    *   [Retrieve a pageget](/reference/retrieve-a-page)
    *   [Retrieve a page property itemget](/reference/retrieve-a-page-property)
    *   [Update page propertiespatch](/reference/patch-page)
    *   [Trash a page](/reference/archive-a-page)
*   [Databases](/reference/create-a-database)
    *   [Create a databasepost](/reference/create-a-database)
    *   [Filter database entries](/reference/post-database-query-filter)
    *   [Sort database entries](/reference/post-database-query-sort)
    *   [Query a databasepost](/reference/post-database-query)
    *   [Retrieve a databaseget](/reference/retrieve-a-database)
    *   [Update a databasepatch](/reference/update-a-database)
    *   [Update database properties](/reference/update-property-schema-object)
*   [Users](/reference/get-users)
    *   [List all usersget](/reference/get-users)
    *   [Retrieve a userget](/reference/get-user)
    *   [Retrieve your token's bot userget](/reference/get-self)
*   [Comments](/reference/create-a-comment)
    *   [Create commentpost](/reference/create-a-comment)
    *   [Retrieve commentsget](/reference/retrieve-a-comment)
*   [Search](/reference/post-search)
    *   [Search by titlepost](/reference/post-search)
    *   [Search optimizations and limitations](/reference/search-optimizations-and-limitations)

Property values
===============

A property value defines the identifier, type, and value of a page property in a page object. It's used when retrieving and updating pages, ex: [Create](/reference/post-page) and [Update](/reference/patch-page) pages.

> 🚧
> 
> Property values in the page object have a 25 page reference limit
> 
> 
> -----------------------------------------------------------------------
> 
> Any property value that has other pages in its value will only use the first 25 page references. Use the [Retrieve a page property](/reference/retrieve-a-page-property) endpoint to paginate through the full value.

All property values

[](#all-property-values)
-----------------------------------------------

Each page property value object contains the following keys. In addition, it contains a key corresponding with the value of `type`. The value is an object containing type-specific data. The type-specific data are described in the sections below.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` | Underlying identifier for the property. This identifier is guaranteed to remain constant when the property name changes. It may be a UUID, but is often a short random string.  
  
The `id` may be used in place of `name` when creating or updating pages. | `"f%5C%5C%3Ap"` |
| `type` (optional) | `string` (enum) | Type of the property. Possible values are `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"status"`, `"date"`, `"formula"`, `"relation"`, `"rollup"`, `"title"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, and `"last_edited_by"`. | `"rich_text"` |

Title property values

[](#title-property-values)
---------------------------------------------------

Title property value objects contain an array of [rich text objects](/reference/rich-text) within the `title` property.

Title property valueTitle property value (using ID)

`{   "Name": {     "title": [       {         "type": "text",         "text": {           "content": "The title"         }       }     ]   } }`

`{   "title": {     "title": [       {         "type": "rich_text",         "rich_text": {           "content": "The title"         }       }     ]   } }`

> 📘
> --
> 
> The [Retrieve a page endpoint](/reference/retrieve-a-page) returns a maximum of 25 inline page or person references for a `title` property. If a `title` property includes more than 25 references, then you can use the [Retrieve a page property](/reference/retrieve-a-page-property) endpoint for the specific `title` property to get its complete list of references.

Rich Text property values

[](#rich-text-property-values)
-----------------------------------------------------------

Rich Text property value objects contain an array of [rich text objects](/reference/rich-text) within the `rich_text` property.

Rich text property valueRich text property value (using ID)

`{   "Details": {     "rich_text": [       {         "type": "text",         "text": {           "content": "Some more text with "         }       },       {         "type": "text",         "text": {           "content": "some"         },         "annotations": {           "italic": true         }       },       {         "type": "text",         "text": {           "content": " "         }       },       {         "type": "text",         "text": {           "content": "fun"         },         "annotations": {           "bold": true         }       },       {         "type": "text",         "text": {           "content": " "         }       },       {         "type": "text",         "text": {           "content": "formatting"         },         "annotations": {           "color": "pink"         }       }     ]   } }`

`{   "D[X|": {     "rich_text": [       {         "type": "text",         "text": {           "content": "Some more text with "         }       },       {         "type": "text",         "text": {           "content": "some"         },         "annotations": {           "italic": true         }       },       {         "type": "text",         "text": {           "content": " "         }       },       {         "type": "text",         "text": {           "content": "fun"         },         "annotations": {           "bold": true         }       },       {         "type": "text",         "text": {           "content": " "         }       },       {         "type": "text",         "text": {           "content": "formatting"         },         "annotations": {           "color": "pink"         }       }     ]   } }`

> 📘
> --
> 
> The [Retrieve a page endpoint](/reference/retrieve-a-page) returns a maximum of 25 populated inline page or person references for a `rich_text` property. If a `rich_text` property includes more than 25 references, then you can use the [Retrieve a page property endpoint](/reference/retrieve-a-page-property) for the specific `rich_text` property to get its complete list of references.

Number property values

[](#number-property-values)
-----------------------------------------------------

Number property value objects contain a number within the `number` property.

Number property valueNumber property value (using ID)

`{   "Quantity": {     "number": 1234   } }`

`{   "pg@s": {     "number": 1234   } }`

Select property values

[](#select-property-values)
-----------------------------------------------------

Select property value objects contain the following data within the `select` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` (UUIDv4) | ID of the option.  
  
When updating a select property, you can use either `name` or `id`. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"` |
| `name` | `string` | Name of the option as it appears in Notion.  
  
If the select [database property](/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.  
  
Note: Commas (",") are not valid for select values. | `"Fruit"` |
| `color` | `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.  
  
Not currently editable. | `"red"` |

Select property valueSelect property value (using ID)

`{   "Option": {     "select": {       "name": "Option 1"     }   } }`

`{   "XMqQ": {     "select": {       "id": "c3406b80-bda4-45e0-add2-2748ac1527b"     }   } }`

Status property values

[](#status-property-values)
-----------------------------------------------------

Status property value objects contain the following data within the `status` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` (UUIDv4) | ID of the option. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"` |
| `name` | `string` | Name of the option as it appears in Notion. | `"In progress"` |
| `color` | `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.  
  
Not currently editable. | `"red"` |

Status property valueStatus property value (using ID)

`{   "Status": {     "status": {       "name": "In progress"     }   } }`

`{   "XMqQ": {     "status": {       "id": "c3406b80-bda4-45e0-add2-2748ac1527b"     }   } }`

Multi-select property values

[](#multi-select-property-values)
-----------------------------------------------------------------

Multi-select property value objects contain an array of multi-select option values within the `multi_select` property.

### 

Multi-select option values

[](#multi-select-option-values)

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` (UUIDv4) | ID of the option.  
  
When updating a multi-select property, you can use either `name` or `id`. | `"b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"` |
| `name` | `string` | Name of the option as it appears in Notion.  
  
If the multi-select [database property](/reference/property-object) does not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.  
  
Note: Commas (",") are not valid for select values. | `"Fruit"` |
| `color` | `string` (enum) | Color of the option. Possible values are: `"default"`, `"gray"`, `"brown"`, `"red"`, `"orange"`, `"yellow"`, `"green"`, `"blue"`, `"purple"`, `"pink"`. Defaults to `"default"`.  
  
Not currently editable. | `"red"` |

Multi-select property valueMulti-select property value (using option ID)

`{   "Tags": {     "multi_select": [       {         "name": "B"       },       {         "name": "C"       }     ]   } }`

`{   "uyn@": {     "multi_select": [       {         "id": "3d3ca089-f964-4831-a8a2-0c6d746f4162"       },       {         "id": "1919ba02-1bf3-4e73-8832-8c0020f17363"       }     ]   } }`

Date property values

[](#date-property-values)
-------------------------------------------------

Date property value objects contain the following data within the `date` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `start` | string ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | An ISO 8601 format date, with optional time. | `"2020-12-08T12:00:00Z"` |
| `end` | string (optional, [ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | An ISO 8601 formatted date, with optional time. Represents the end of a date range.  
  
If `null`, this property's date value is not a range. | `"2020-12-08T12:00:00Z"` |
| `time_zone` | string (optional, enum) | Time zone information for `start` and `end`. Possible values are extracted from the [IANA database](https://www.iana.org/time-zones) and they are based on the time zones from [Moment.js](https://momentjs.com/timezone/).  
  
When time zone is provided, `start` and `end` should not have any [UTC offset](https://en.wikipedia.org/wiki/UTC_offset). In addition, when time zone is provided, `start` and `end` cannot be dates without time information.  
  
If `null`, time zone information will be contained in [UTC offset](https://en.wikipedia.org/wiki/UTC_offset)s in `start` and `end`. | `"America/Los_Angeles"` |

Date property valueDate property value (using ID)

`{   "Shipment Time": {     "date": {       "start": "2021-05-11T11:00:00.000-04:00"     }   } }`

`{   "CbFP": {     "date": {       "start": "2021-05-11T11:00:00.000-04:00"     }   } }`

Date property value with rangeDate property value with range (using ID)

`{   "Preparation Range": {     "date": {       "start": "2021-04-26",       "end": "2021-05-07"     }   } }`

`{   "\\rm}": {     "date": {       "start": "2021-04-26",       "end": "2021-05-07"     }   } }`

Date property value with timezoneDate property value with timezone (using ID)

`{   "Delivery Time": {     "date": {       "start": "2020-12-08T12:00:00Z",       "time_zone": "America/New_York"     }   } }`

`{   "DgRt": {     "date": {       "start": "2020-12-08T12:00:00Z",       "time_zone": "America/New_York"     }   } }`

Formula property values

[](#formula-property-values)
-------------------------------------------------------

Formula property value objects represent the result of evaluating a formula described in the  
[database's properties](/reference/property-object). These objects contain a `type` key and a key corresponding with the value of `type`. The value of a formula cannot be updated directly.

> 🚧
> 
> Formula values may not match the Notion UI.
> 
> 
> -------------------------------------------------
> 
> Formulas returned in page objects are subject to a 25 page reference limitation. The Retrieve a page property endpoint should be used to get an accurate formula value.

Formula property value

`{   "Formula": {     "id": "1lab",     "formula": {       "type": "number",       "number": 1234     }   } }`

| Property | Type | Description |
| --- | --- | --- |
| `type` | `string` (enum) |  |

### 

String formula property values

[](#string-formula-property-values)

String formula property values contain an optional string within the `string` property.

### 

Number formula property values

[](#number-formula-property-values)

Number formula property values contain an optional number within the `number` property.

### 

Boolean formula property values

[](#boolean-formula-property-values)

Boolean formula property values contain a boolean within the `boolean` property.

### 

Date formula property values

[](#date-formula-property-values)

Date formula property values contain an optional [date property value](#date-property-values) within the `date` property.

Relation property values

[](#relation-property-values)
---------------------------------------------------------

Relation property value objects contain an array of page references within the `relation` property. A page reference is an object with an `id` key and a string value (UUIDv4) corresponding to a page ID in another database.

A `relation` includes a `has_more` property in the [Retrieve a page endpoint](/reference/retrieve-a-page) response object. The endpoint returns a maximum of 25 page references for a `relation`. If a `relation` has more than 25 references, then the `has_more` value for the relation in the response object is `true`. If a relation doesn’t exceed the limit, then `has_more` is `false`.

Note that [updating](/reference/patch-page) a relation property value with an empty array will clear the list.

Relation property valueRelation property value (using ID)

`{   "Project": {     "relation": [       {         "id": "1d148a9e-783d-47a7-b3e8-2d9c34210355"       }     ],       "has_more": true   } }`

`{   "mODt": {     "relation": [       {         "id": "1d148a9e-783d-47a7-b3e8-2d9c34210355"       }     ],       "has_more": true   } }`

Rollup property values

[](#rollup-property-values)
-----------------------------------------------------

Rollup property value objects represent the result of evaluating a rollup described in the  
[database's properties](/reference/property-object). These objects contain a `type` key and a key corresponding with the value of `type`. The value of a rollup cannot be updated directly.

Rollup property value

`{   "Rollup": {     "id": "aJ3l",     "rollup": {       "type": "number",       "number": 1234,       "function": "sum"     }   } }`

> 🚧
> 
> Rollup values may not match the Notion UI.
> 
> 
> ------------------------------------------------
> 
> Rollups returned in page objects are subject to a 25 page reference limitation. The Retrieve a page property endpoint should be used to get an accurate formula value.

### 

String rollup property values

[](#string-rollup-property-values)

String rollup property values contain an optional string within the `string` property.

### 

Number rollup property values

[](#number-rollup-property-values)

Number rollup property values contain a number within the `number` property.

### 

Date rollup property values

[](#date-rollup-property-values)

Date rollup property values contain a [date property value](#date-property-values) within the `date` property.

### 

Array rollup property values

[](#array-rollup-property-values)

Array rollup property values contain an array of `number`, `date`, or `string` objects within the `results` property.

People property values

[](#people-property-values)
-----------------------------------------------------

People property value objects contain an array of [user objects](/reference/user) within the `people` property.

People property valuePeople property value (using ID)

`{   "Owners": {     "people": [       {         "object": "user",         "id": "3e01cdb8-6131-4a85-8d83-67102c0fb98c"       },       {         "object": "user",         "id": "b32c006a-2898-45bb-abd2-de095f354592"       }     ]   } }`

`{   "Owners": {     "people": [       {         "object": "user",         "id": "3e01cdb8-6131-4a85-8d83-67102c0fb98c"       },       {         "object": "user",         "id": "b32c006a-2898-45bb-abd2-de095f354592"       }     ]   } }`

> 📘
> --
> 
> The [Retrieve a page](/reference/retrieve-a-page) endpoint can’t be guaranteed to return more than 25 people per `people` page property. If a `people` page property includes more than 25 people, then you can use the [Retrieve a page property endpoint](/reference/retrieve-a-page-property) for the specific `people` property to get a complete list of people.

Files property values

[](#files-property-values)
---------------------------------------------------

File property value objects contain an array of file references within the `files` property. A file reference is an object with a [File Object](/reference/file-object) and `name` property, with a string value corresponding to a filename of the original file upload (i.e. `"Whole_Earth_Catalog.jpg"`).

JSON

`{   "Files": {     "files": [       {         "type": "external",         "name": "Space Wallpaper",         "external": {           	"url": "https://website.domain/images/space.png"         }       }     ]   } }`

> 📘
> 
> When updating a file property, the value will be overwritten by the array of files passed.
> 
> 
> ------------------------------------------------------------------------------------------------
> 
> Although we do not support uploading files, if you pass a `file` object containing a file hosted by Notion, it will remain one of the files. To remove any file, just do not pass it in the update response.

Checkbox property values

[](#checkbox-property-values)
---------------------------------------------------------

Checkbox property value objects contain a boolean within the `checkbox` property.

Checkbox property valueCheckbox property value (using ID)

`{   "Done?": {     "checkbox": true   } }`

`{   "RirO": {     "checkbox": true   } }`

URL property values

[](#url-property-values)
-----------------------------------------------

URL property value objects contain a non-empty string within the `url` property. The string describes a web address (i.e. `"http://worrydream.com/EarlyHistoryOfSmalltalk/"`).

URL property valueURL property value (using ID)

`{   "Website": {     "url": "https://notion.so/notiondevs"   } }`

`{   "<tdn": {     "url": "https://notion.so/notiondevs"   } }`

Email property values

[](#email-property-values)
---------------------------------------------------

Email property value objects contain a string within the `email` property. The string describes an email address (i.e. `"hello@example.org"`).

Email property valueEmail property value (using ID)

`{   "Shipper's Contact": {     "email": "hello@test.com"   } }`

`{   "}=RV": {     "email": "hello@test.com"   } }`

Phone number property values

[](#phone-number-property-values)
-----------------------------------------------------------------

Phone number property value objects contain a string within the `phone_number` property. No structure is enforced.

Phone number property valuePhone number property value (using ID)

`{   "Shipper's No.": {     "phone_number": "415-000-1111"   } }`

`{   "_A<p": {     "phone_number": "415-000-1111"   } }`

Created time property values

[](#created-time-property-values)
-----------------------------------------------------------------

Created time property value objects contain a string within the `created_time` property. The string contains the date and time when this page was created. It is formatted as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date time string (i.e. `"2020-03-17T19:10:04.968Z"`). The value of `created_time` cannot be updated. See the [Property Item Object](/reference/property-item-object) to see how these values are returned.

Created by property values

[](#created-by-property-values)
-------------------------------------------------------------

Created by property value objects contain a [user object](/reference/user) within the `created_by` property. The user object describes the user who created this page. The value of `created_by` cannot be updated. See the [Property Item Object](/reference/property-item-object) to see how these values are returned.

Last edited time property values

[](#last-edited-time-property-values)
-------------------------------------------------------------------------

Last edited time property value objects contain a string within the `last_edited_time` property. The string contains the date and time when this page was last updated. It is formatted as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date time string (i.e. `"2020-03-17T19:10:04.968Z"`). The value of `last_edited_time` cannot be updated. See the [Property Item Object](/reference/property-item-object) to see how these values are returned.

Last edited by property values

[](#last-edited-by-property-values)
---------------------------------------------------------------------

Last edited by property value objects contain a [user object](/reference/user) within the `last_edited_by` property. The user object describes the user who last updated this page. The value of `last_edited_by` cannot be updated. See the [Property Item Object](/reference/property-item-object) to see how these values are returned.

Updated over 1 year ago

* * *

[

Introduction

](/reference/intro)

Did this page help you?

Yes

No

Updated over 1 year ago

* * *

[

Introduction

](/reference/intro)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [All property values](#all-property-values)
    *   [Title property values](#title-property-values)
    *   [Rich Text property values](#rich-text-property-values)
    *   [Number property values](#number-property-values)
    *   [Select property values](#select-property-values)
    *   [Status property values](#status-property-values)
    *   [Multi-select property values](#multi-select-property-values)
        *   [Multi-select option values](#multi-select-option-values)
    *   [Date property values](#date-property-values)
    *   [Formula property values](#formula-property-values)
        *   [String formula property values](#string-formula-property-values)
        *   [Number formula property values](#number-formula-property-values)
        *   [Boolean formula property values](#boolean-formula-property-values)
        *   [Date formula property values](#date-formula-property-values)
    *   [Relation property values](#relation-property-values)
    *   [Rollup property values](#rollup-property-values)
        *   [String rollup property values](#string-rollup-property-values)
        *   [Number rollup property values](#number-rollup-property-values)
        *   [Date rollup property values](#date-rollup-property-values)
        *   [Array rollup property values](#array-rollup-property-values)
    *   [People property values](#people-property-values)
    *   [Files property values](#files-property-values)
    *   [Checkbox property values](#checkbox-property-values)
    *   [URL property values](#url-property-values)
    *   [Email property values](#email-property-values)
    *   [Phone number property values](#phone-number-property-values)
    *   [Created time property values](#created-time-property-values)
    *   [Created by property values](#created-by-property-values)
    *   [Last edited time property values](#last-edited-time-property-values)
    *   [Last edited by property values](#last-edited-by-property-values)

1.  Notion API
2.  [
    
    Introduction
    
    ](/reference/intro)
3.  [
    
    Integration capabilities
    
    ](/reference/capabilities)
4.  [
    
    Request limits
    
    ](/reference/request-limits)
5.  [
    
    Status codes
    
    ](/reference/status-codes)
6.  [
    
    Versioning
    
    ](/reference/versioning)
7.  [
    
    Changes by version
    
    ](/reference/changes-by-version)

1.  Objects
2.  [
    
    Block
    
    ](/reference/block)
3.  [
    
    Rich text
    
    ](/reference/rich-text)
4.  [
    
    Page
    
    ](/reference/page)
5.  [
    
    Page properties
    
    ](/reference/page-property-values)
6.  [
    
    Database
    
    ](/reference/database)
7.  [
    
    Database properties
    
    ](/reference/property-object)
8.  [
    
    Parent
    
    ](/reference/parent-object)
9.  [
    
    User
    
    ](/reference/user)
10.  [
    
    Comment
    
    ](/reference/comment-object)
11.  [
    
    Unfurl attribute (Link Previews)
    
    ](/reference/unfurl-attribute-object)
12.  [
    
    File
    
    ](/reference/file-object)
13.  [
    
    Emoji
    
    ](/reference/emoji-object)

1.  Endpoints
2.  [
    
    Authentication
    
    ](/reference/authentication)
3.  [
    
    Create a tokenpost
    
    ](/reference/create-a-token)
4.  [
    
    Blocks
    
    ](/reference/blocks)
5.  [
    
    Delete a blockdelete
    
    ](/reference/delete-a-block)
6.  [
    
    Update a blockpatch
    
    ](/reference/update-a-block)
7.  [
    
    Retrieve block childrenget
    
    ](/reference/get-block-children)
8.  [
    
    Retrieve a blockget
    
    ](/reference/retrieve-a-block)
9.  [
    
    Append block childrenpatch
    
    ](/reference/patch-block-children)
10.  [
    
    Pages
    
    ](/reference/pages)
11.  [
    
    Trash a page
    
    ](/reference/archive-a-page)
12.  [
    
    Update page propertiespatch
    
    ](/reference/patch-page)
13.  [
    
    Retrieve a page property itemget
    
    ](/reference/retrieve-a-page-property)
14.  [
    
    Retrieve a pageget
    
    ](/reference/retrieve-a-page)
15.  [
    
    Create a pagepost
    
    ](/reference/post-page)
16.  [
    
    Databases
    
    ](/reference/databases)
17.  [
    
    Update database properties
    
    ](/reference/update-property-schema-object)
18.  [
    
    Update a databasepatch
    
    ](/reference/update-a-database)
19.  [
    
    Retrieve a databaseget
    
    ](/reference/retrieve-a-database)
20.  [
    
    Query a databasepost
    
    ](/reference/post-database-query)
21.  [
    
    Sort database entries
    
    ](/reference/post-database-query-sort)
22.  [
    
    Filter database entries
    
    ](/reference/post-database-query-filter)
23.  [
    
    Create a databasepost
    
    ](/reference/create-a-database)
24.  [
    
    Users
    
    ](/reference/users)
25.  [
    
    Retrieve your token's bot userget
    
    ](/reference/get-self)
26.  [
    
    Retrieve a userget
    
    ](/reference/get-user)
27.  [
    
    List all usersget
    
    ](/reference/get-users)
28.  [
    
    Comments
    
    ](/reference/comments)
29.  [
    
    Retrieve commentsget
    
    ](/reference/retrieve-a-comment)
30.  [
    
    Create commentpost
    
    ](/reference/create-a-comment)
31.  [
    
    Search
    
    ](/reference/search)
32.  [
    
    Search optimizations and limitations
    
    ](/reference/search-optimizations-and-limitations)
33.  [
    
    Search by titlepost
    
    ](/reference/post-search)

1.  Notion API
2.  [
    
    Introduction
    
    ](/reference/intro)
3.  [
    
    Integration capabilities
    
    ](/reference/capabilities)
4.  [
    
    Request limits
    
    ](/reference/request-limits)
5.  [
    
    Status codes
    
    ](/reference/status-codes)
6.  [
    
    Versioning
    
    ](/reference/versioning)
7.  [
    
    Changes by version
    
    ](/reference/changes-by-version)

1.  Objects
2.  [
    
    Block
    
    ](/reference/block)
3.  [
    
    Rich text
    
    ](/reference/rich-text)
4.  [
    
    Page
    
    ](/reference/page)
5.  [
    
    Page properties
    
    ](/reference/page-property-values)
6.  [
    
    Database
    
    ](/reference/database)
7.  [
    
    Database properties
    
    ](/reference/property-object)
8.  [
    
    Parent
    
    ](/reference/parent-object)
9.  [
    
    User
    
    ](/reference/user)
10.  [
    
    Comment
    
    ](/reference/comment-object)
11.  [
    
    Unfurl attribute (Link Previews)
    
    ](/reference/unfurl-attribute-object)
12.  [
    
    File
    
    ](/reference/file-object)
13.  [
    
    Emoji
    
    ](/reference/emoji-object)

1.  Endpoints
2.  [
    
    Authentication
    
    ](/reference/authentication)
3.  [
    
    Create a tokenpost
    
    ](/reference/create-a-token)
4.  [
    
    Blocks
    
    ](/reference/blocks)
5.  [
    
    Delete a blockdelete
    
    ](/reference/delete-a-block)
6.  [
    
    Update a blockpatch
    
    ](/reference/update-a-block)
7.  [
    
    Retrieve block childrenget
    
    ](/reference/get-block-children)
8.  [
    
    Retrieve a blockget
    
    ](/reference/retrieve-a-block)
9.  [
    
    Append block childrenpatch
    
    ](/reference/patch-block-children)
10.  [
    
    Pages
    
    ](/reference/pages)
11.  [
    
    Trash a page
    
    ](/reference/archive-a-page)
12.  [
    
    Update page propertiespatch
    
    ](/reference/patch-page)
13.  [
    
    Retrieve a page property itemget
    
    ](/reference/retrieve-a-page-property)
14.  [
    
    Retrieve a pageget
    
    ](/reference/retrieve-a-page)
15.  [
    
    Create a pagepost
    
    ](/reference/post-page)
16.  [
    
    Databases
    
    ](/reference/databases)
17.  [
    
    Update database properties
    
    ](/reference/update-property-schema-object)
18.  [
    
    Update a databasepatch
    
    ](/reference/update-a-database)
19.  [
    
    Retrieve a databaseget
    
    ](/reference/retrieve-a-database)
20.  [
    
    Query a databasepost
    
    ](/reference/post-database-query)
21.  [
    
    Sort database entries
    
    ](/reference/post-database-query-sort)
22.  [
    
    Filter database entries
    
    ](/reference/post-database-query-filter)
23.  [
    
    Create a databasepost
    
    ](/reference/create-a-database)
24.  [
    
    Users
    
    ](/reference/users)
25.  [
    
    Retrieve your token's bot userget
    
    ](/reference/get-self)
26.  [
    
    Retrieve a userget
    
    ](/reference/get-user)
27.  [
    
    List all usersget
    
    ](/reference/get-users)
28.  [
    
    Comments
    
    ](/reference/comments)
29.  [
    
    Retrieve commentsget
    
    ](/reference/retrieve-a-comment)
30.  [
    
    Create commentpost
    
    ](/reference/create-a-comment)
31.  [
    
    Search
    
    ](/reference/search)
32.  [
    
    Search optimizations and limitations
    
    ](/reference/search-optimizations-and-limitations)
33.  [
    
    Search by titlepost
    
    ](/reference/post-search)