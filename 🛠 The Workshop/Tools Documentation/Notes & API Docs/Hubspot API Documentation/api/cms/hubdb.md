---
title: "CMS API | HubDB"
description: "The HubDB API provides access to a relational data store that presents data as rows, columns, and cells in a table format similar to a spreadsheet. It allows for the creation, modification, retrieval, and import of tables within your HubSpot account. Tables can have draft and published versions, supporting dynamic pages and manual approval processes without affecting live pages. Public access is possible with authentication via `portalId`."
type: "group"
tags:
- "HubDB"
- "API"
- "Data_Management"
relationships:
- "#related_to [[HubSpot CMS]]"
- "#enables [[Dynamic Pages]]"
founded: "N/A"
---

CMS API | HubDB
===============

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

HubDB is a relational data store that presents data as rows, columns, and cells in a table, much like a spreadsheet. HubDB tables can be added or modified [within your HubSpot account](/docs/cms/data/hubdb#creating-your-first-table), but you can also use the API endpoints documented here. For information on using data from HubDB tables on your website or in [programmable emails](/docs/cms/guides/email/hubdb-crm-objects), check out [HubSpot's CMS developer documentation](/docs/cms/data/hubdb).  
  
Similar to HubSpot website pages, HubDB tables support `draft` and `published` versions. This allows you to update data in the table, either for testing or to allow for a manual approval process, without affecting any live pages. Learn more about [drafted versus live tables](#drafted-vs-live-tables).

If a table is set to be [allowed for public access](https://knowledge.hubspot.com/website-pages/create-and-populate-tables-in-hubdb#manage-table-settings-cms-hub-professional-and-enterprise-only), you can access the published version of the table and rows without any authentication by specifying your HubSpot account ID via the query parameter `portalId`.

If you're migrating from v2 of the HubDB API, learn more about the [changes in the current (v3) API](#changes-in-v3).

**Please note:** endpoints that support `GET` also support `CORS`, so you can access data in a table client-side using JavaScript and your account ID. Other methods and the _Get all tables_ endpoint require authentication and do not support `CORS`.

Rate limits[](https://developers.hubspot.com/docs/api/cms/hubdb#rate-limits)
----------------------------------------------------------------------------

HubDB API requests have different rate limits, depending on the type of request:

*   Any `GET` requests made that don't require authentication (including client-side JavaScript requests) are limited to 10 requests per second. These requests won't count towards the daily limit.
*   All other requests [using authentication](https://developers.hubspot.com/docs/methods/auth/oauth-overview) follow the [standard limits](https://developers.hubspot.com/docs/overview).

Draft vs live tables[](https://developers.hubspot.com/docs/api/cms/hubdb#draft-vs-live-tables)
----------------------------------------------------------------------------------------------

HubDB tables have both draft and live versions and live versions can be published or unpublished. This will allow you to update data in the table, either for page previews or testing or to allow for a manual approval process, without affecting any live pages.

In this API, separate endpoints are designated for the draft and published versions of a table. For example, you can retrieve the published version of a table by making a `GET` request to the following endpoint:

`/cms/v3/hubdb/tables/{tableIdOrName}`

And to retrieve any content that has been drafted but not yet published, you would add `/draft` to the end of the URL:

`/cms/v3/hubdb/tables/{tableIdOrName}/draft`

Draft data can be reviewed and then pushed in HubSpot, or with the `/push-live` endpoint. The draft data can also be discarded via `/reset` endpoint, allowing you to revert to the current live version of the data without disruption.

Create a HubDB table[](https://developers.hubspot.com/docs/api/cms/hubdb#create-a-hubdb-table)
----------------------------------------------------------------------------------------------

To create a HubDB table, make a `POST` request to `/cms/v3/hubdb/tables`.

In the request body, specify the following required fields:

Use this table to describe parameters / fields
| Field | Type | Description | Example |
| --- | --- | --- | --- |
| 
`name`

 | String | 

The internal name of the table. This name cannot be changed once the table is created. Names can only include lowercase letters, digits, and underscores and cannot begin with a number.

 | `"name": "my_table"` |
| 

`label`

 | String | 

The label of the table that users see when editing the table in HubSpot.

 | `"label":"My table"` |

In addition, you can specify the following optional fields:

Use this table to describe parameters / fields
| Field | Type | Description | Example |
| --- | --- | --- | --- |
| 
`useForPages`

 | Boolean | 

Whether the table can be used for [creating dynamic pages](/docs/cms/guides/dynamic-pages/hubdb).

 | `"useForPages": false` |
| 

`allowPublicAPIAccess`

 | Boolean | 

Whether the table can be read without authorization.

 | `"allowPublicApiAccess": false` |
| 

`allowChildTables`

 | Boolean | 

Whether child tables can be created for the table.

 | `"allowChildTables": false` |
| 

`enableChildTablePages`

 | Boolean | 

Whether [multilevel dynamic pages](/docs/cms/guides/dynamic-pages/hubdb/multilevel) should be created using child tables.

 | `"enableChildTablePages": false` |
| 

`columns`

 | Object | 

The columns of the table. Learn more about column properties in the [Add table columns](#add-table-columns) sections.

 | `See "Add table columns" section below` |

Without any columns added yet, your create request might look like the following:

//example request { "name": "test\_table", "label": "Test Table", "useForPages": true, "allowPublicApiAccess": false, "allowChildTables": true, "enableChildTablePages": false, "columns": \[\], }

### Add table columns[](https://developers.hubspot.com/docs/api/cms/hubdb#add-table-columns)

Each column in a HubDB table can be defined with the following properties:

Use this table to describe parameters / fields
| Field | Type | Description | Example |
| --- | --- | --- | --- |
| 
`name`

 | String | 

Required. The internal name of the column. Cannot be changed after the column is created.

 | `"name": "row_name"` |
| 

`label`

 | String | 

Optional. The label for the column that users will see when editing the table in HubSpot.

 | `"label": "Row label"` |
| 

`type`

 | String | 

The data type of the column. Must be one of the following:

*   **text**: a text field.
*   **richtext:**  a text field that supports basic HTML formatting. Not recommended for raw HTML, as it may impact whether the HTML is editable in HubSpot. Editing the code in HubSpot may also impact the way the code is rendered. 
*   **number:** a number field.
*   **boolean:** represented as a checkbox in HubSpot. Use `0` for unchecked and `1` for checked.
*   **date:** stores a specific date as a millisecond timestamp set to midnight UTC.
*   **datetime:** stores a date and a time as a millisecond timestamp.
*   **select:** the column can only be set to one of a set of options. See the `options` field below for required properties.
*   **multiselect:** the column can be set to one or more of a set of options. See the `options` field below for required properties.
*   **location:** stores a latitude and longitude location.
*   **image:** stores the URL of an image.
*   **video:** stores the player ID of the video.
*   **foreign\_ID:** the column will reference a column from another HubDB table. In addition, you must define the other HubDB table with the following properties:
    *   **foreignTableId:** the ID of the other HubDB table. 
    *   **foreignColumnId:** the ID of the column in the other HubDB table.
*   **currency:** stores the number as a currency value.

 | `"type": "type"` |
| 

`options`

 | Object | 

A list of options for select and multiselect columns. Each option is defined with a `name` along with a `type` equal to `option`.

 | `"option": [{"name":"Option 1", "type":"option"}, {"name": "Option 2", "type": "option"}]` |

Using the above fields, your request to create a new HubDB table might look like the following:

JSON

Copy all

    //example request
    {
     "label": "Test Table",
     "name": "test_table",
     "columns": [
     {
       "name": "text_column",
       "label": "Text Column",
       "archived": false,
       "type": "TEXT"
     },
     {
       "name": "number_column",
       "label": "Number Column",
       "archived": false,
       "type": "NUMBER"
     },
     {
       "name": "multiselect",
       "label": "Multi Select Column",
       "archived": false,
       "type": "multiselect",
       "options": [
       {
         "name": "Option 1",
         "type": "option"
       },
       {
         "name": "Option 2",
         "type": "option"
       }
       ]
     }
     ],
     "useForPages": true,
     "allowChildTables": true,
     "enableChildTablePages": false,
     "dynamicMetaTags": {
     },
     "allowPublicApiAccess": false
    }

After creating a table, columns will be assigned IDs in ascending order. When updating existing columns, include the column's `id` field in the input object.

### Add table rows[](https://developers.hubspot.com/docs/api/cms/hubdb#add-table-rows)

You can add rows either manually through the API, or you can [import rows from a CSV file](#import-rows-from-csv).

To add rows to a HubDB table, make a `POST` request to `/cms/v3/hubdb/tables/{tableIdOrName}/rows`.

For each table row, you can include the following fields:

Add table rows fields
| Field | Type | Description | Example |
| --- | --- | --- | --- |
| 
`values`

 | Object | 

A list of key-value pairs with the column name and the value you want to add to it.  
  
If you don't want to set a specific value for a column, you can omit the column name from the list of key-value pairs.

 | `"values": { "text_column": "sample text", "number_column": 76}` |
| 

`path`

 | String | 

For tables [enabled for dynamic pages](/docs/cms/guides/dynamic-pages/hubdb), `path` is the path suffix used for the page created for this row.

 | `"path": "example_url_path"` |
| 

`name`

 | String | 

For tables [enabled for dynamic pages](/docs/cms/guides/dynamic-pages/hubdb), `name` is the HTML title used for the page created for this row.

 | `"name": "Example Title"` |
| 

`childTableId`

 | Number | 

When creating [multilevel dynamic pages](/docs/cms/guides/dynamic-pages/hubdb/multilevel), `childTableId` specifies the child table ID.

 | `"childTableId": 123456` |

Using the above fields, your request might look similar to the following:

//example request { "values": { "text\_column": "sample text value", "number\_column": 76, "rich\_text\_column": "<strong>This is a styled paragraph.</strong>", "date\_column": 1591228800000, "date\_time\_column": 1604450520000, "boolean\_column": 1, "select\_column": { "name": "option 1", "type": "option" }, "multiselect\_column": \[ { "name": "Option 1", "type": "option" }, { "name": "Option 2", "type": "option" } \], "url\_column": "https://www.hubspot.com/marketing", "video\_column": 3392210008, "image\_column": { "url": "https://f.hubspotusercontentqa00.net/hubfs/99992002/image3%20(1).jpg", "width": 1600, "height": 900, "type": "image" }, "foreign\_id\_column": \[ { "id": "4364402239", "type": "foreignid" }, { "id": "4364402240", "type": "foreignid" } \] }, "path": "test\_path", "name": "test\_title", "childTableId": "1902373" }

### Import rows from CSV[](https://developers.hubspot.com/docs/api/cms/hubdb#import-rows-from-csv)

To import data into a HubDB table from a CSV file, make a `POST` request to `/cms/v3/hubdb/tables/{tableIdOrName}/draft/import`.

The import endpoint takes a multipart/form-data `POST` request:

*   config: a set of JSON-formatted options for the import. 
*   **file:** the CSV file that you want to import. 

In `config`, include the following fields as a JSON string:

Use this table to describe parameters / fields
| Field | Type | Description | Example |
| --- | --- | --- | --- |
| 
`skipRows`

 | Number | 

The number of header rows that should be skipped over. This field defaults to `1`, skipping the first row and treating it as a header. Set this to `0` if all of the rows are valid data. 

 | `"skipRows": 0` |
| 

`separator`

 | String | 

The column delimiter in the CSV file. Set to `","` by default.

 | `"separator": ","` |
| 

`idSourceColumn`

 | Number | 

The index of the column in the source file containing the row’s ID (`hs_id`).

If this column is specified, the import will update the existing rows in the table for the matching row IDs from the CSV file. This is optional and you can ignore this during the first time you import data into a table.

See the [Reset options](#reset-options) section below more detailed information.

 | `"idSourceColumn": 1` |
| 

`resetTable`

 | Boolean | 

Defaults to `false`, meaning that the table's rows will be updated without removing any existing rows. If set to `true`, the spreadsheet rows will overwrite table data, meaning that any rows in the table that aren't in the spreadsheet will be deleted.

See the [Reset options](#reset-options) section below more detailed information.

 | `"resetTable": true` |
| 

`nameSourceColumn`

 | Number | 

For tables [enabled for dynamic pages](/docs/cms/guides/dynamic-pages/hubdb), `nameSourceColumn` specifies the column in the CSV file that contains the row's `name`. Column numbers are in ascending order, with the first column being `1`.

 | `"nameSourcecolumn": 5` |
| 

`pathSourceColumn`

 | Number | 

For tables [enabled for dynamic pages](/docs/cms/guides/dynamic-pages/hubdb), `pathSourceColumn` specifies the column in the CSV file that contains the row's `path`. Column numbers are in ascending order, with the first column being `1`.

 | `"pathSourcecolumn": 6` |
| 

`childTableSourceColumn`

 | Number | 

Specifies the column in the CSV file that contains the row's `childTableId`. Column numbers are in ascending order, with the first column being `1`.

 | `"childTableSourcecolumn": 3` |
| 

`columnMappings`

 | Array | 

A list of mappings for the columns in the source file to the columns in the destination HubDB table.

Each mapping must have the following format: `{"source":1,"target”:"columnIdOrName"}` 

*   **source:** the column index in the source file. For example, `2` for the second column.
*   **target:** the ID or name of the HubDB table column. You can get the ID or name of a column by [getting the details for the table](#retrieve-hubdb-data).

If your file has an `hs_id` column, you shouldn't include it in `columnMappings`. Instead, include it as the `idSourceColumn` to update existing rows.

 | `"columnMappings": [{"source":1, "target": 2}, {"source": 2, "target": "column_name"}]` |
| 

`primaryKeyColumn`

 | String | 

The name of a column in the target HubDB table that will be used for deduplication. The column's ID cannot be used for this field.

 | `"primaryKeyColumn": "column_name"` |
| 

`encoding`

 | String | 

The file's encoding type. For example, `utf-8`, `ascii`, `iso-8859-2`, `iso-8859-5`, `iso-2022-jp`, `windows-1252`.

 | `"encoding": "utf-8"` |
| 

`format`

 | String | 

Only CSV is supported.

 | `"format": "csv"` |

Using the above table, your `config` JSON might look like the following:

// example config JSON { "skipRows": 1, "separator": ",", "idSourceColumn": 1, "resetTable": false, "columnMappings": \[ { "target": 1, "source": 2 }, { "target": 2, "source": "zip\_code" }, \], "primaryKeyColumn": "name", "encoding": "utf-8", "format": "csv" }

### Date formatting[](https://developers.hubspot.com/docs/api/cms/hubdb#date-formatting)

There are several formats you can use when importing data into a date-type column.

Integers

*   `yyyy/mm/dd`
*   `yyyy/mm/dd`
*   `mm/dd/yyyy`
*   `mm/dd/yy`

These formats require the month to precede the day (i.e., `dd/mm/yy` is not accepted). Integers can be separated by hyphens (`-`) or slashes (`/`).

Relaxed dates

You can also import date formats that are less standardized than integer-based dates. For example:

*   `The 1st of March in the year 2022`
*   `Fri Mar 4 2022`
*   `March 4th '22`

Relative dates

HubSpot will parse the following date formats relative to the current day:

*   `next Thursday`
*   `Today`
*   `tomorrow`
*   `3 days from now`

### Reset options[](https://developers.hubspot.com/docs/api/cms/hubdb#reset-options)

When importing data from a CSV file into a HubDB table, you can set the  `resetTable` field to `true` or `false` (default) to manage whether HubDB row data is overwritten.

*   If `resetTable` is set to `true`:  
    
    *   If the rows in the CSV file does not have a row ID column (`hs_id` or row ID is specified as `0`, those rows will be inserted with the new row IDs generated.
    *   If the row IDs in the CSV file already exists in the target table, the existing rows in the table will be updated with the new values from the input file.
    *   If the table has rows but the input CSV file does not have those row IDs, those rows will be deleted from the target table.
    *   If the row IDs in the input CSV file do not exist in the target table, those rows will be inserted with the new row IDs generated and the row IDs given in the input file will be ignored.
    *   If the input CSV file does not contain the row ID column at all, all the rows will be deleted from the target table and the rows from the input file will be inserted with the new row IDs generated.
    
*   If `resetTable` is set to `false` (default):  
    
    *   If the row IDs in the CSV file already exists in the target table, the existing rows in the table will be updated with the new values from the input file.
    *   If the table has rows but the input CSV file does not have those row IDs, those rows will _not_ be deleted from the target table and those rows will remain unchanged.
    *   If the row IDs in the input CSV file do not exist in the target table, those rows will be inserted with the new row IDs generated and the row IDs given in the input file will be ignored.
    *   If the rows in the CSV file does not have a row ID column or row ID is specified as `0`, those rows will be inserted with the new row IDs generated.
    

Retrieve HubDB data[](https://developers.hubspot.com/docs/api/cms/hubdb#retrieve-hubdb-data)
--------------------------------------------------------------------------------------------

There are multiple ways to retrieve HubDB data, depending on whether you're looking for table details or the rows of a table:

*   To retrieve table details from all published tables, make a `GET` request to `/cms/v3/hubdb/tables`.
*   To retrieve table details from a specific published table, make a `GET` request to `/cms/v3/hubdb/tables{tableIdOrName}`.
*   To retrieve all rows from a specific table, make a `GET` request to `/cms/v3/hubdb/tables{tableIdOrName}/rows`.
*   To retrieve a specific row from a table, make a `GET` request to `/cms/v3/hubdb/tables{tableIdOrName}/rows/{rowId}`.

When retrieving row data, you can further filter and sort the results.

If a table is set to be [allowed for public access](https://knowledge.hubspot.com/website-pages/create-and-populate-tables-in-hubdb#manage-table-settings-cms-hub-professional-and-enterprise-only), you can access the published version of the table and rows without any authentication by specifying your HubSpot account ID via the query parameter `portalId`.

### Filter returned rows[](https://developers.hubspot.com/docs/api/cms/hubdb#filter-returned-rows)

When retrieving HubDB table data, you can apply filters as query parameters to receive specific data. Filter query parameters are constructed as follows: `columnName__operator`. 

For example, if you have a number column named _bar_, you can filter results to only include rows where _bar_ is greater than 10: `&bar__gt=10`.

All filters are ANDed together (OR filters are not currently supported).

When filtering, keep the following in mind:

*   When passing values for `multiselect` columns, the values should be comma-separated (e.g. `multiselect_column__contains=1,2`).
*   For `datetime` filters, you can use relative dates in place of timestamps in order to specify a value relative to the current time. For example, `-3h` would correspond to the timestamp 3 hours before now, whereas `10s` would correspond to 10 seconds in the future. Supported time units are ms (milliseconds), s (seconds), m (minutes), h (hours), d (days). Current time can be used by specifying a zero value: 0s

*   For the purposes of these filters, the built in column `hs_id` is a `number` column, the `hs_created_at` column is a `datetime`, and the `hs_path` and `hs_name` columns are `text` columns.

Below, learn which operators can be applied to which column types:

Use this table to describe parameters / fields
| Operator | Name | Description |
| --- | --- | --- |
| 
`eq (or none)`

 | Equals | 

All column types.

This filter is applied if no operator is used. When used with multiselect columns, returns rows that exact match supplied values.

 |
| 

`ne`

 | Not equal to | 

All column types.

 |
| 

`contains`

 | Contains | 

Text, richtext, and multiselect.

When used with multiselect columns, returns rows that contain all of the supplied values. This filter is case sensitive.

 |
| 

`lt`

 | Less than | 

Number, date, and datetime.

 |
| 

`lte`

 | Less than or equal to | 

Number, date, and datetime.

 |
| 

`gt`

 | Greater than | 

Number, date, and datetime.

 |
| 

`gte`

 | Greater than or equal to | 

Number, date, and datetime.

 |
| 

`is_null`

 | Null | 

All column types except boolean.

This filter doesn't require a value (e.g. `&exampleColumn__is_null=`).

 |
| 

`not_null`

 | Not null | 

All column types except boolean.

This filter doesn't require a value (e.g. `&exampleColumn__not_null=`).

 |
| 

`like`

 | Like | 

Text and richtext.

 |
| 

`not_like`

 | Not like | 

Text and richtext.

 |
| 

`icontains`

 | Contains | 

Text and richtext.

This filter is case insensitive.

 |
| 

`startswith`

 | Starts with | 

Text and richtext.

 |
| 

`in`

 | In | 

Number, select, and multiselect.

Returns rows where the column includes at least one of the passed options. When there is no other `sort` in the query parameter, the results will be sorted in the order in which values are specified in the `in` operator.

 |

### Sort returned rows[](https://developers.hubspot.com/docs/api/cms/hubdb#sort-returned-rows)

When retrieving HubDB data, you can apply sorting as a query parameter to determine the order of the returned data. To sort data, add a `sort` query parameter and specify the column name:

`&sort=columnName`

By default, data will be returned in the natural order of the specified column. You can reverse the sort by adding a `-` to the column name: 

`&sort=-columnName`

You can include this parameter multiple times to sort by multiple columns.

In addition to sorting by a column, there are three functions that can be used:

*   **geo\_distance(location\_column\_name, latitude, longitude):** takes the name of a location column and coordinates, returns the rows ordered by how far away the values of the specified location column are from the provided coordinates.

*   **length(column\_name):** takes the name of a column, returns the rows ordered by the length of the column value (calculated as a string)

*   **random():** returns the rows in random order.

These functions also support reverse ordering. For example, the following `geo_distance` sort returns items that are the farthest away first:

`sort=-geo_distance(location_column,42.37,-71.07)` 

Changes in v3[](https://developers.hubspot.com/docs/api/cms/hubdb#changes-in-v3)
--------------------------------------------------------------------------------

*   Tables should have both `name` and `label`. This name cannot be changed once the table is created. Names can only include lowercase letters, digits, and underscores and cannot begin with a number. Both `name` and `label` should be unique in the account.
*   API supports both table `id` and `name` in the URL paths.
*   `GET` row endpoints return column `name` instead of `id` in `values` field. Also, `POST` / `PUT` / `PATCH` row endpoints require column `name` instead of `id` in `values` field.
*   Row update `PATCH` endpoints now accept sparse updates, which means you can specify only the column values that you need to update (whereas you had to specify all the column values in the previous versions). When you update a column with a list of values such as multiselect, you need to specify the list of all the values. In order to delete the value for a column, you need to specify the column with the value as `null` in the request. 
*   Removed the endpoints to `get` / `update` / `delete` a row cell in favor of the row update `PATCH` endpoints.
*   Import endpoint now supports an optional field `idSourceColumn` along with existing fields in the JSON-formatted options. You can use this field to specify the column in the csv file which contains row ids. To import new rows along with the new values for existing rows, you can simply specify `0` as the row id for the new rows and the valid row ids for the existing columns.  See more details in the Import section below. Also you can use column names or ids in the target field of the column mappings in the JSON-formatted options.
*   Clone endpoint requires a new name and new label.

Using the above fields, your `config` might look like the following:

//example config { "skipRows":1, "format":"csv", "separator":",", "encoding":"utf-8", "columnMappings": \[ {"target":1,"source":"text\_column"}, {"target":2,"source":"number\_column"}, {"target":3,"source":"multiselect"} \], "idSourceColumn":1, "pathSourceColumn":2, "nameSourceColumn":4, "childTableSourceColumn":5, "resetTable":true }

### Example curl command for the import endpoint:

curl -L -X POST 'https://api.hubspotqa.com/hubdb/api/v2/tables/xxxxxx/import?portalId=xxxxxxx' \\ -H 'Content-Type: multipart/form-data' \\ -F 'config="{\\"skipRows\\":1,\\"format\\":\\"csv\\",\\"separator\\":\\",\\",\\"encoding\\":\\"iso-8859-1\\",\\"columnMappings\\":\[{\\"target\\":1,\\"source\\":7},{\\"target\\":3,\\"source\\":8}\],\\"idSourceColumn\\":1,\\"pathSourceColumn\\":null,\\"nameSourceColumn\\":null,\\"childTableSourceColumn\\":null,\\"resetTable\\":true}"' \\ -F 'file=@"/Users/xxxxxxxxxxxxx/Downloads/filename.csv"'

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/cms/hubdb#page-feedback)
--------------------------------------------------------------------------------------

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