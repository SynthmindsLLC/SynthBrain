---
Please provide me with the rest of the mission statement! I need more context to understand what you're trying to accomplish.  

For example, tell me: "* **What is the mission for?** (A company, a project, a personal goal?)"
* **What are the main goals or objectives?**
* **What are the values or principles that guide the mission?**

Once you provide me with more details, I can help you craft a strong and compelling mission statement.
---

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

Filter database entries
=======================

When you [query a database](/reference/post-database-query), you can send a `filter` object in the body of the request that limits the returned entries based on the specified criteria.

For example, the below query limits the response to entries where the `"Task completed"` `checkbox` property value is `true`:

cURL

`curl -X POST 'https://api.notion.com/v1/databases/897e5a76ae524b489fdfe71f5945d1af/query' \   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \   -H 'Notion-Version: 2022-06-28' \   -H "Content-Type: application/json" \ --data '{   "filter": {     "property": "Task completed",     "checkbox": {         "equals": true    }   } }'`

Here is the same query using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js):

JavaScript

`const { Client } = require('@notionhq/client');  const notion = new Client({ auth: process.env.NOTION_API_KEY }); // replace with your own database ID const databaseId = 'd9824bdc-8445-4327-be8b-5b47500af6ce';  const filteredRows = async () => { 	const response = await notion.databases.query({ 	  database_id: databaseId, 	  filter: { 	    property: "Task completed", 	    checkbox: { 	      equals: true 	    } 	  }, 	});   return response; }`

Filters can be chained with the `and` and `or` keys so that multiple filters are applied at the same time. (See [Query a database](/reference/post-database-query) for additional examples.)

JSON

`{   "and": [     {       "property": "Done",       "checkbox": {         "equals": true       }     },      {       "or": [         {           "property": "Tags",           "contains": "A"         },         {           "property": "Tags",           "contains": "B"         }       ]     }   ] }`

If no filter is provided, all the pages in the database will be returned with pagination.

The filter object

[](#the-filter-object)
-------------------------------------------

Each `filter` object contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `property` | `string` | The name of the property as it appears in the database, or the property ID. | `"Task completed"` |
| `checkbox`  
`date`  
`files`  
`formula`  
`multi_select`  
`number`  
`people`  
`phone_number`  
`relation`  
`rich_text`  
`select`  
`status`  
`timestamp`  
`ID` | `object` | The type-specific filter condition for the query. Only types listed in the Field column of this table are supported.  
  
Refer to [type-specific filter conditions](#type-specific-filter-conditions) for details on corresponding object values. | `"checkbox": { "equals": true }` |

Example checkbox filter object

`{   "filter": {     "property": "Task completed",     "checkbox": {       "equals": true     }   } }`

> 👍
> --
> 
> The filter object mimics the database [filter option in the Notion UI](https://www.notion.so/help/views-filters-and-sorts).

Type-specific filter conditions

[](#type-specific-filter-conditions)
-----------------------------------------------------------------------

### 

Checkbox

[](#checkbox)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `boolean` | Whether a `checkbox` property value matches the provided value exactly.  
  
Returns or excludes all database entries with an exact value match. | `false` |
| `does_not_equal` | `boolean` | Whether a `checkbox` property value differs from the provided value.  
  
Returns or excludes all database entries with a difference in values. | `true` |

Example checkbox filter condition

`{   "filter": {     "property": "Task completed",     "checkbox": {       "does_not_equal": true     }   } }`

### 

Date

[](#date)

> 📘
> --
> 
> For the `after`, `before`, `equals, on_or_before`, and `on_or_after` fields, if a date string with a time is provided, then the comparison is done with millisecond precision.
> 
> If no timezone is provided, then the timezone defaults to UTC.

A date filter condition can be used to limit `date` property value types and the [timestamp](#timestamp) property types `created_time` and `last_edited_time`.

The condition contains the below fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `after` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.  
  
Returns database entries where the date property value is after the provided date. | `"2021-05-10"`  
  
`"2021-05-10T12:00:00"`  
  
`"2021-10-15T12:00:00-07:00"` |
| `before` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.  
  
Returns database entries where the date property value is before the provided date. | `"2021-05-10"`  
  
`"2021-05-10T12:00:00"`  
  
`"2021-10-15T12:00:00-07:00"` |
| `equals` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.  
  
Returns database entries where the date property value is the provided date. | `"2021-05-10"`  
  
`"2021-05-10T12:00:00"`  
  
`"2021-10-15T12:00:00-07:00"` |
| `is_empty` | `true` | The value to compare the date property value against.  
  
Returns database entries where the date property value contains no data. | `true` |
| `is_not_empty` | `true` | The value to compare the date property value against.  
  
Returns database entries where the date property value is not empty. | `true` |
| `next_month` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the next month. | `{}` |
| `next_week` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the next week. | `{}` |
| `next_year` | `object` (empty) | A filter that limits the results to database entries where the date property value is within the next year. | `{}` |
| `on_or_after` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.  
  
Returns database entries where the date property value is on or after the provided date. | `"2021-05-10"`  
  
`"2021-05-10T12:00:00"`  
  
`"2021-10-15T12:00:00-07:00"` |
| `on_or_before` | `string` ([ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601)) | The value to compare the date property value against.  
  
Returns database entries where the date property value is on or before the provided date. | `"2021-05-10"`  
  
`"2021-05-10T12:00:00"`  
  
`"2021-10-15T12:00:00-07:00"` |
| `past_month` | `object` (empty) | A filter that limits the results to database entries where the `date` property value is within the past month. | `{}` |
| `past_week` | `object` (empty) | A filter that limits the results to database entries where the `date` property value is within the past week. | `{}` |
| `past_year` | `object` (empty) | A filter that limits the results to database entries where the `date` property value is within the past year. | `{}` |
| `this_week` | `object` (empty) | A filter that limits the results to database entries where the `date` property value is this week. | `{}` |

Example date filter condition

`{   "filter": {     "property": "Due date",     "date": {       "on_or_after": "2023-02-08"     }   } }`

### 

Files

[](#files)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `is_empty` | `true` | Whether the files property value does not contain any data.  
  
Returns all database entries with an empty `files` property value. | `true` |
| `is_not_empty` | `true` | Whether the `files` property value contains data.  
  
Returns all entries with a populated `files` property value. | `true` |

Example files filter condition

`{   "filter": {     "property": "Blueprint",     "files": {       "is_not_empty": true     }   } }`

### 

Formula

[](#formula)

The primary field of the `formula` filter condition object matches the type of the formula’s result. For example, to filter a formula property that computes a `checkbox`, use a `formula` filter condition object with a `checkbox` field containing a checkbox filter condition as its value.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `checkbox` | `object` | A [checkbox](#checkbox) filter condition to compare the formula result against.  
  
Returns database entries where the formula result matches the provided condition. | Refer to the [checkbox](#checkbox) filter condition. |
| `date` | `object` | A [date](#date) filter condition to compare the formula result against.  
  
Returns database entries where the formula result matches the provided condition. | Refer to the [date](#date) filter condition. |
| `number` | `object` | A [number](#number) filter condition to compare the formula result against.  
  
Returns database entries where the formula result matches the provided condition. | Refer to the [number](#number) filter condition. |
| `string` | `object` | A [rich text](#rich-text) filter condition to compare the formula result against.  
  
Returns database entries where the formula result matches the provided condition. | Refer to the [rich text](#rich-text) filter condition. |

Example formula filter condition

`{   "filter": {     "property": "One month deadline",     "formula": {       "date":{           "after": "2021-05-10"       }     }   } }`

### 

Multi-select

[](#multi-select)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` | The value to compare the multi-select property value against.  
  
Returns database entries where the multi-select value matches the provided string. | `"Marketing"` |
| `does_not_contain` | `string` | The value to compare the multi-select property value against.  
  
Returns database entries where the multi-select value does not match the provided string. | `"Engineering"` |
| `is_empty` | `true` | Whether the multi-select property value is empty.  
  
Returns database entries where the multi-select value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the multi-select property value is not empty.  
  
Returns database entries where the multi-select value does contains data. | `true` |

Example multi-select filter condition

`{   "filter": {     "property": "Programming language",     "multi_select": {       "contains": "TypeScript"     }   } }`

### 

Number

[](#number)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `number` | The `number` to compare the number property value against.  
  
Returns database entries where the number property value differs from the provided `number`. | `42` |
| `equals` | `number` | The `number` to compare the number property value against.  
  
Returns database entries where the number property value is the same as the provided number. | `42` |
| `greater_than` | `number` | The `number` to compare the number property value against.  
  
Returns database entries where the number property value exceeds the provided `number`. | `42` |
| `greater_than_or_equal_to` | `number` | The `number` to compare the number property value against.  
  
Returns database entries where the number property value is equal to or exceeds the provided `number`. | `42` |
| `is_empty` | `true` | Whether the `number` property value is empty.  
  
Returns database entries where the number property value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the number property value is not empty.  
  
Returns database entries where the number property value contains data. | `true` |
| `less_than` | `number` | The `number` to compare the number property value against.  
  
Returns database entries where the number property value is less than the provided `number`. | `42` |
| `less_than_or_equal_to` | `number` | The `number` to compare the number property value against.  
  
Returns database entries where the number property value is equal to or is less than the provided `number`. | `42` |

Example number filter condition

`{   "filter": {     "property": "Estimated working days",     "number": {       "less_than_or_equal_to": 5     }   } }`

### 

People

[](#people)

You can apply a people filter condition to `people`, `created_by`, and `last_edited_by` database property types.

The people filter condition contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` (UUIDv4) | The value to compare the people property value against.  
  
Returns database entries where the people property value contains the provided `string`. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `does_not_contain` | `string` (UUIDv4) | The value to compare the people property value against.  
  
Returns database entries where the people property value does not contain the provided `string`. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `is_empty` | `true` | Whether the people property value does not contain any data.  
  
Returns database entries where the people property value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the people property value contains data.  
  
Returns database entries where the people property value is not empty. | `true` |

Example people filter condition

`{   "filter": {     "property": "Last edited by",     "people": {       "contains": "c2f20311-9e54-4d11-8c79-7398424ae41e"     }   } }`

### 

Relation

[](#relation)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` (UUIDv4) | The value to compare the relation property value against.  
  
Returns database entries where the relation property value contains the provided `string`. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `does_not_contain` | `string` (UUIDv4) | The value to compare the relation property value against.  
  
Returns entries where the relation property value does not contain the provided `string`. | `"6c574cee-ca68-41c8-86e0-1b9e992689fb"` |
| `is_empty` | `true` | Whether the relation property value does not contain data.  
  
Returns database entries where the relation property value does not contain any data. | `true` |
| `is_not_empty` | `true` | Whether the relation property value contains data.  
  
Returns database entries where the property value is not empty. | `true` |

Example relation filter condition

`{   "filter": {     "property": "✔️ Task List",     "relation": {       "contains": "0c1f7cb280904f18924ed92965055e32"     }   } }`

### 

Rich text

[](#rich-text)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `contains` | `string` | The `string` to compare the text property value against.  
  
Returns database entries with a text property value that includes the provided `string`. | `"Moved to Q2"` |
| `does_not_contain` | `string` | The `string` to compare the text property value against.  
  
Returns database entries with a text property value that does not include the provided `string`. | `"Moved to Q2"` |
| `does_not_equal` | `string` | The `string` to compare the text property value against.  
  
Returns database entries with a text property value that does not match the provided `string`. | `"Moved to Q2"` |
| `ends_with` | `string` | The `string` to compare the text property value against.  
  
Returns database entries with a text property value that ends with the provided `string`. | `"Q2"` |
| `equals` | `string` | The `string` to compare the text property value against.  
  
Returns database entries with a text property value that matches the provided `string`. | `"Moved to Q2"` |
| `is_empty` | `true` | Whether the text property value does not contain any data.  
  
Returns database entries with a text property value that is empty. | `true` |
| `is_not_empty` | `true` | Whether the text property value contains any data.  
  
Returns database entries with a text property value that contains data. | `true` |
| `starts_with` | `string` | The `string` to compare the text property value against.  
  
Returns database entries with a text property value that starts with the provided `string`. | "Moved" |

Example rich text filter condition

`{   "filter": {     "property": "Description",     "rich_text": {       "contains": "cross-team"     }   } }`

### 

Rollup

[](#rollup)

A rollup database property can evaluate to an array, date, or number value. The filter condition for the rollup property contains a `rollup` key and a corresponding object value that depends on the computed value type.

#### 

Filter conditions for `array` rollup values

[](#filter-conditions-for-array-rollup-values)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `any` | `object` | The value to compare each rollup property value against. Can be a [filter condition](#type-specific-filter-conditions) for any other type.  
  
Returns database entries where the rollup property value matches the provided criteria. | `"rich_text": { "contains": "Take Fig on a walk" }` |
| `every` | `object` | The value to compare each rollup property value against. Can be a [filter condition](#type-specific-filter-conditions) for any other type.  
  
Returns database entries where every rollup property value matches the provided criteria. | `"rich_text": { "contains": "Take Fig on a walk" }` |
| `none` | `object` | The value to compare each rollup property value against. Can be a [filter condition](#type-specific-filter-conditions) for any other type.  
  
Returns database entries where no rollup property value matches the provided criteria. | `"rich_text": { "contains": "Take Fig on a walk" }` |

Example array rollup filter condition

`{   "filter": {     "property": "Related tasks",     "rollup": {       "any": {         "rich_text": {           "contains": "Migrate database"         }       }     }   } }`

#### 

Filter conditions for `date` rollup values

[](#filter-conditions-for-date-rollup-values)

A rollup value is stored as a `date` only if the "Earliest date", "Latest date", or "Date range" computation is selected for the property in the Notion UI.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `date` | `object` | A [date](#date) filter condition to compare the rollup value against.  
  
Returns database entries where the rollup value matches the provided condition. | Refer to the [date](#date) filter condition. |

Example date rollup filter condition

`{   "filter": {     "property": "Parent project due date",     "rollup": {       "date": {         "on_or_before": "2023-02-08"       }     }   } }`

#### 

Filter conditions for `number` rollup values

[](#filter-conditions-for-number-rollup-values)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `number` | `object` | A [number](#number) filter condition to compare the rollup value against.  
  
Returns database entries where the rollup value matches the provided condition. | Refer to the [number](#number) filter condition. |

Example number rollup filter condition

`{   "filter": {     "property": "Total estimated working days",     "rollup": {       "number": {         "does_not_equal": 42       }     }   } }`

### 

Select

[](#select)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `equals` | `string` | The `string` to compare the select property value against.  
  
Returns database entries where the select property value matches the provided string. | `"This week"` |
| `does_not_equal` | `string` | The `string` to compare the select property value against.  
  
Returns database entries where the select property value does not match the provided `string`. | `"Backlog"` |
| `is_empty` | `true` | Whether the select property value does not contain data.  
  
Returns database entries where the select property value is empty. | `true` |
| `is_not_empty` | `true` | Whether the select property value contains data.  
  
Returns database entries where the select property value is not empty. | `true` |

Example select filter condition

`{   "filter": {     "property": "Frontend framework",     "select": {       "equals": "React"     }   } }`

### 

Status

[](#status)

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| equals | string | The string to compare the status property value against.  
  
Returns database entries where the status property value matches the provided string. | "This week" |
| does\_not\_equal | string | The string to compare the status property value against.  
  
Returns database entries where the status property value does not match the provided string. | "Backlog" |
| is\_empty | true | Whether the status property value does not contain data.  
  
Returns database entries where the status property value is empty. | true |
| is\_not\_empty | true | Whether the status property value contains data.  
  
Returns database entries where the status property value is not empty. | true |

Example status filter condition

`{   "filter": {     "property": "Project status",     "status": {       "equals": "Not started"     }   } }`

### 

Timestamp

[](#timestamp)

Use a timestamp filter condition to filter results based on `created_time` or `last_edited_time` values.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| timestamp | created\_time last\_edited\_time | A constant string representing the type of timestamp to use as a filter. | "created\_time" |
| created\_time  
last\_edited\_time | object | A date filter condition used to filter the specified timestamp. | Refer to the [date](#date) filter condition. |

Example timestamp filter condition for created\_time

`{   "filter": {     "timestamp": "created_time",     "created_time": {       "on_or_before": "2022-10-13"     }   } }`

> 🚧
> --
> 
> The `timestamp` filter condition does not require a property name. The API throws an error if you provide one.

### 

ID

[](#id)

Use a timestamp filter condition to filter results based on the `unique_id` value.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `does_not_equal` | `number` | The value to compare the unique\_id property value against.  
  
Returns database entries where the unique\_id property value differs from the provided value. | `42` |
| `equals` | `number` | The value to compare the unique\_id property value against.  
  
Returns database entries where the unique\_id property value is the same as the provided value. | `42` |
| `greater_than` | `number` | The value to compare the unique\_id property value against.  
  
Returns database entries where the unique\_id property value exceeds the provided value. | `42` |
| `greater_than_or_equal_to` | `number` | The value to compare the unique\_id property value against.  
  
Returns database entries where the unique\_id property value is equal to or exceeds the provided value. | `42` |
| `less_than` | `number` | The value to compare the unique\_id property value against.  
  
Returns database entries where the unique\_id property value is less than the provided value. | `42` |
| `less_than_or_equal_to` | `number` | The value to compare the unique\_id property value against.  
  
Returns database entries where the unique\_id property value is equal to or is less than the provided value. | `42` |

Example ID filter condition

`{   "filter": {     "and": [       {         "property": "ID",         "unique_id": {           "greater_than": 1         }       },       {         "property": "ID",         "unique_id": {           "less_than": 3         }       }     ]   } }`

Compound filter conditions

[](#compound-filter-conditions)
-------------------------------------------------------------

You can use a compound filter condition to limit the results of a database query based on multiple conditions. This mimics filter chaining in the Notion UI.

![1340](https://files.readme.io/14ec7e8-Untitled.png "Untitled.png")

An example filter chain in the Notion UI

The above filters in the Notion UI are equivalent to the following compound filter condition via the API:

JSON

`{   "and": [     {       "property": "Done",       "checkbox": {         "equals": true       }     },      {       "or": [         {           "property": "Tags",           "contains": "A"         },         {           "property": "Tags",           "contains": "B"         }       ]     }   ] }`

A compound filter condition contains an `and` or `or` key with a value that is an array of filter objects or nested compound filter objects. Nesting is supported up to two levels deep.

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `and` | `array` | An array of [filter](#type-specific-filter-conditions) objects or compound filter conditions.  
  
Returns database entries that match **all** of the provided filter conditions. | Refer to the examples below. |
| or | array | An array of [filter](#type-specific-filter-conditions) objects or compound filter conditions.  
  
Returns database entries that match **any** of the provided filter conditions | Refer to the examples below. |

### 

Example compound filter conditions

[](#example-compound-filter-conditions)

Example compound filter condition for a checkbox and number property value

`{   "filter": {     "and": [       {         "property": "Complete",         "checkbox": {           "equals": true         }       },       {         "property": "Working days",         "number": {           "greater_than": 10         }       }     ]   } }`

Example nested filter condition

`{   "filter": {     "or": [       {         "property": "Description",         "rich_text": {           "contains": "2023"         }       },       {         "and": [           {             "property": "Department",             "select": {               "equals": "Engineering"             }           },           {             "property": "Priority goal",             "checkbox": {               "equals": true             }           }         ]       }     ]   } }`

Updated 7 months ago

* * *

[

Create a database

](/reference/create-a-database)[

Sort database entries

](/reference/post-database-query-sort)

Did this page help you?

Yes

No

Updated 7 months ago

* * *

[

Create a database

](/reference/create-a-database)[

Sort database entries

](/reference/post-database-query-sort)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [The filter object](#the-filter-object)
    *   [Type-specific filter conditions](#type-specific-filter-conditions)
        *   [Checkbox](#checkbox)
        *   [Date](#date)
        *   [Files](#files)
        *   [Formula](#formula)
        *   [Multi-select](#multi-select)
        *   [Number](#number)
        *   [People](#people)
        *   [Relation](#relation)
        *   [Rich text](#rich-text)
        *   [Rollup](#rollup)
        *   [Select](#select)
        *   [Status](#status)
        *   [Timestamp](#timestamp)
        *   [ID](#id)
    *   [Compound filter conditions](#compound-filter-conditions)
        *   [Example compound filter conditions](#example-compound-filter-conditions)

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