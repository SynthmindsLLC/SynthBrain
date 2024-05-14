HubDB


=========

Last updated: March 28, 2024

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/marketing_icon.svg) Marketing Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/content_hub_icon.svg) Content Hub
    *   Professional or Enterprise

HubDB is a tool that allows you to create tables to store data in rows, columns, and cells, much like a spreadsheet. You can customize a HubDB table's columns, rows, and other settings based on your needs. For example, you could use a HubDB table to:

*   Store feedback from an external mechanism to retrieve at a later time.
*   Store structured data that you can use to [build dynamic CMS pages](/docs/cms/guides/dynamic-pages/hubdb) (CMS Hub Professional and Enterprise only).
*   Store data to use in a [programmable email](https://knowledge.hubspot.com/email/create-programmable-emails) (_Marketing Hub_ _Enterprise_ only).

![hubdb-table-example0](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/hubdb-table-example0.png?width=1008&name=hubdb-table-example0.png)HubDB tables can be accessed both [within HubSpot](https://knowledge.hubspot.com/website-pages/create-and-populate-tables-in-hubdb) and through the [HubDB API](/docs/methods/hubdb/hubdb_overview), and you can retrieve a table's data in multiple ways, depending on your use case. To get data from a HubDB table, you can: 

*   Query the data externally via the [HubDB API](https://developers.hubspot.com/docs/methods/hubdb/hubdb_overview?_ga=2.196207854.330901250.1583937788-2053671461.1524595016). 
*   Use HubSpot’s HubL markup tags to pull data into the CMS as structured content.
*   Use the HubDB API with [serverless functions](/docs/cms/features/serverless-functions) to provide an interactive web app experience.  
    

**Please note:**

*   To [use HubDB data in pages](/docs/cms/guides/dynamic-pages/hubdb), you need _**CMS Hub**_ _Professional_ or _Enterprise_.
*   To use HubDB data in [programmable emails](https://knowledge.hubspot.com/email/create-programmable-emails), you need _**Marketing Hub**_ _Enterprise_.
*   Publishing, editing, and viewing existing tables requires [HubDB permissions](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#website-tools). Creating, clone, deleting, and editing a HubDB table's settings requires [_HubDB table settings_ permissions](https://knowledge.hubspot.com/settings/hubspot-user-permissions-guide#settings). 

HubDB architecture[](https://developers.hubspot.com/docs/cms/data/hubdb#hubdb-architecture)
-------------------------------------------------------------------------------------------

A HubDB table consists of rows, columns, and cells, similar to a spreadsheet.

*   **Tables:** a table is a 2-dimensional arrangement of rows and columns. When a table is created, it is assigned a globally unique ID which you can use when needing to specify a table in HubL or through the API.
*   **Rows:** rows are horizontal slices of a table. In a spreadsheet application, rows are represented by numbers, starting with 1. Each table row is given a unique ID on creation. Each row in a table comes with a few columns by default:

Use this table to describe parameters / fields
| Column | Description |
| --- | --- |
| 
`hs_id`

 | 

An automatically assigned, globally unique, numeric ID for this row.

 |
| 

`hs_created_at`

 | 

A timestamp of when this row was created.

 |
| 

`hs_path`

 | 

When used with dynamic pages, this string is the last segment of the URL's path for the page.

 |
| 

`hs_name`

 | 

When used with dynamic pages, this is the title of the page.

 |

**Please note:** rich text area columns in HubDB are limited to 65,000 characters. For more information, [view the changelog announcement](/changelog/hubdb-rich-text-area-limited-to-65000-characters-and-a-new-meetings-module).

*   **Columns:** columns are vertical slices of a table. Each column has a type, which is used to store kinds of data. A table can include as many columns as you'd like, and each is assigned a globally unique ID on creation.  Column ID start at a value of `1`, but are not necessarily sequential, and cannot be reused. Column types include: 
    *   Text
    *   Rich text
    *   URL
    *   Image
    *   Select
    *   Multi-select
    *   Date
    *   Date and time
    *   Number
    *   Currency
    *   Checkbox
    *   Location (longitude, latitude)
    *   Foreign ID
    *   Video
*   Cells: Cells store the values where a row and column intersect. Cells can be read or updated individually or as part of a row. Setting the value of a cell to `null` is equivalent to deleting the cell's value.

HubDB technical limits[](https://developers.hubspot.com/docs/cms/data/hubdb#hubdb-technical-limits)
---------------------------------------------------------------------------------------------------

Note the following HubDB technical limits:

*   Account limits:
    *   1,000 HubDB tables per account.
    *   1 million HubDB rows per account.

*   Table limits:
    *   250 columns per table.
    *   10,000 rows per HubDB table.
    *   700 characters per table name.
    *   700 characters per table label.

*   Column limits:
    *   65,000 characters per rich text column.
    *   10,000 characters in each text column.
    *   700 characters per column name.
    *   700 characters per label.
    *   300 characters per column description.
    *   700 characters per selectable option within a column.
*   Page limits:
    *   10 calls to the `hubdb_table_rows` HubL function per CMS page.
    *   10 [dynamic pages](/docs/cms/guides/dynamic-pages/hubdb) using the same HubDB table.
    *   HubDB's with dynamic pages turned on must have lowercase paths so that URLs to these pages can be case insensitive.

Create a HubDB table[](https://developers.hubspot.com/docs/cms/data/hubdb#create-a-hubdb-table)
-----------------------------------------------------------------------------------------------

You can create HubDB tables either [through HubSpot's UI](https://knowledge.hubspot.com/website-pages/create-and-populate-tables-in-hubdb) or through the [HubDB API](/docs/methods/hubdb/v2/create_table).

All new tables created are set with a status of draft. They cannot be used to output data via HubL or API until you publish the table. When creating a table, you can also [manage its settings](https://knowledge.hubspot.com/website-pages/create-and-populate-tables-in-hubdb#manage-table-settings-cms-hub-professional-and-enterprise-only), such as allowing public API access and whether its data will be used to [create dynamic pages](/docs/cms/guides/dynamic-pages/hubdb).

Join multiple HubDB tables[](https://developers.hubspot.com/docs/cms/data/hubdb#join-multiple-hubdb-tables)
-----------------------------------------------------------------------------------------------------------

HubDB tables can be joined using the Foreign ID column type, which allows you to render the combined data from multiple tables. This can be helpful when some data might be shared across multiple data stores, allowing one centralized data table of this information, which can then be accessed across multiple other HubDB table data stores.

Below, learn how to join multiple HubDB tables.

### 1\. Add a Foreign ID column to the main table[](https://developers.hubspot.com/docs/cms/data/hubdb#add-a-foreign-id-column-to-the-main-table)

*   In your HubSpot account, navigate to **Marketing** > **Files and Templates** > **HubDB**.
*   Locate the table you want to add a table join to, click the **Actions** dropdown menu, then select **Edit**.
*   In the top right, click **Edit**, then select **Add column**.
*   Enter a **label** and **name** for the new column.
*   Click the **Column type** dropdown menu and select **Foreign ID**.
*   Click the **Select table** dropdown menu and select the **table** you want to join with your current table.
*   Click the **Select column** dropdown menu, then select the **column** from the joining table you have selected to be visible in the Foreign ID field.
*   Click **Add column**.

**Please note:** the value you chose as the _Select column_ only dictates which column value you see in the Foreign ID field in the HubDB UI. All table columns are available when rendering the joined HubDB tables.

![hubdb_foreign_id](https://developers.hubspot.com/hs-fs/hubfs/hubdb_foreign_id.png?width=445&height=606&name=hubdb_foreign_id.png)

### 2\. Add foreign table rows to your table's rows[](https://developers.hubspot.com/docs/cms/data/hubdb#add-foreign-table-rows-to-your-table-s-rows)

Now that you have a _Foreign ID_ column, you will have a multi-select column field on every row in your HubDB table, which allows you to select a foreign table's rows.

The _Select column_ field you chose will be used in this multi-select field to  identify which row you are selecting from the foreign table. In the example below, the multi-select values for the _Expertise table join_ field are the values available from _Name_ column of the foreign HubDB table. 

![hubdb_foreign_id_ui](https://developers.hubspot.com/hs-fs/hubfs/hubdb_foreign_id_ui.png?width=1022&height=570&name=hubdb_foreign_id_ui.png) 

**Please note:** it's safe to edit the _Select column_ field of your _Foreign ID_ column, and will simply update which column's values will display in the HubDB UI.

### 3\. Render your joined HubDB table data[](https://developers.hubspot.com/docs/cms/data/hubdb#render-your-joined-hubdb-table-data)

All of a foreign table's row data is accessible via HubL for rendering, not just the _Select column_ field. HubDB foreign row data is accessible by using a [nested for loop](https://developers.hubspot.com/docs/cms/hubl/for-loops), looping through all of the foreign rows associated with an individual row.

HubL

Copy all

    {% for row in hubdb_table_rows(tableId, filterQuery) %}
      the name for row {{ row.hs_id }} is {{ row.name }}
      {% for foreign_row in row.foreign_table %}
      	the name for foreign row {{ foreign_row.hs_id }} is {{ foreign_row.name }}
      {% endfor %}
    {% endfor %}

Access HubDB data using HubL[](https://developers.hubspot.com/docs/cms/data/hubdb#access-hubdb-data-using-hubl)
---------------------------------------------------------------------------------------------------------------

Using HubL, you can pull HubDB data as to use as structured content on website pages. Below, learn more about how to retrieve table, row, and column data using HubL.

**Please note:** drafted HubDB table data will appear in the page editor and live previews, but only published HubDB content will appear on the live page. If you're seeing table data appear in the editor or preview that isn't appearing on the live page, confirm that the table has been published since adding that table data.

### Getting rows[](https://developers.hubspot.com/docs/cms/data/hubdb#getting-rows)

To list rows of a table, use the [hubdb\_table\_rows()](/docs/cms/hubl/functions#hubdb-table-rows) HubL function. You can either access a table by its ID or name. It is recommended to reference a HubDB table by name, as this can help with code portability across HubSpot accounts. The immutable table name is set when creating a new table and can be found at any time by selecting **Actions > Manage Settings** within the table editor. A table's ID can be found in the address bar of the table editor or in the HubDB tables dashboard under the `ID` column. 

![Screenshot of create table modal](https://developers.hubspot.com/hs-fs/hubfs/Table%20Create.png?width=400&height=329&name=Table%20Create.png "Screenshot of create table modal")

Below is an example of using `hubdb_table_rows()` to fetch data.

{% for row in hubdb\_table\_rows(<tableId or name>, <filterQuery>) %} the value for row {{ row.hs\_id }} is {{ row.<column name> }} {% endfor %}

**Please note:** by default, the maximum number of rows returned is 1,000. To retrieve more rows, specify a `limit` in the function query. For example:

`hudb_table_rows (12345, "random()&limit=1500")`.

`<filterQuery>` uses the same syntax as the HTTP API. For example,  `hubdb_table_rows(123, "employees__gt=10&orderBy=count")` would return a list of rows where the "employees" column is greater than 10, ordered by the "count" column. A complete list of optional `<filterQuery>` parameters [can be found here](https://developers.hubspot.com/docs/methods/hubdb/v2/get_table_rows).

Instead of using multiple row queries with different `<filterQuery>`  parameters, you should make one query and use the `selectattr()`  or `rejectattr()`  filters to filter your rows:

{% set all\_cars = hubdb\_table\_rows(<tableId or name>) %} {% set cars\_with\_windows = all\_cars|selectattr('windows') %} {% set teslas = all\_cars|selectattr('make','equalto','tesla') %}

To get a single row, use the `hubdb_table_row()` HubL function.

{% set row = hubdb\_table\_row(<tableId or name>, <rowId>) %} the value for {{ row.hs\_id }} is {{ row.<column name> }}

Built-in and custom column names are case insensitive. `HS_ID` will work the same as `hs_id`.

#### Row attributes[](https://developers.hubspot.com/docs/cms/data/hubdb#row-attributes)

Use this table to describe parameters / fields
| Attribute | Description |
| --- | --- |
| 
`row.hs_id`

 | 

The globally unique id for this row.

 |
| 

`row.hs_path`

 | 

When using dynamic pages, this string is the Page Path column value and the last segment of the url's path.

 |
| 

`row.hs_name`

 | 

When using dynamic pages, this string is the Page Title column value for the row.

 |
| 

`row.hs_created_at`

 | 

Unix timestamp for when the row was created.

 |
| 

`row.hs_child_table_id`

 | 

When using dynamic pages, this is the ID of the other table that is populating data for the row.

 |
| 

`row.column_name`

 | 

Get the value of the custom column by the name of the column.

 |
| 

`row["column name"]`

 | 

Get the value of the custom column by the name of the column.

 |

### Getting table metadata[](https://developers.hubspot.com/docs/cms/data/hubdb#getting-table-metadata)

To get a table's metadata, including its name, columns, last updated, etc, use the `hubdb_table()` function.

{% set table\_info = hubdb\_table(<tableId or name>) %}

### Table attributes[](https://developers.hubspot.com/docs/cms/data/hubdb#table-attributes)

The attributes listed below are in reference to the variable that `hubdb_table()` was assigned to in the above code. Your variable may differ.  
_Note: It is recommended assigning this to a variable for easier use. If you don't want to do that, you can use  
`{{ hubdb_table(<tableId>).attribute }}`_

Use this table to describe parameters / fields
| Attribute | Description |
| --- | --- |
| 
`table_info.id`

 | 

The id of the table.

 |
| 

`table_info.name`

 | 

The name of the table.

 |
| 

`table_info.columns`

 | 

List of column information. You can use a [for loop](/docs/cms/hubl/for-loops) to iterate through the information available in this attribute.

 |
| 

`table_info.created_at`

 | 

Timestamp of when the table was first created.

 |
| 

`table_info.published_at`

 | 

Timestamp of when this table was published.

 |
| 

`table_info.updated_at`

 | 

Timestamp of when this table was last updated.

 |
| 

`table_info.row_count`

 | 

Number of rows in the table.

 |

### Getting column metadata[](https://developers.hubspot.com/docs/cms/data/hubdb#getting-column-metadata)

{% set table\_info = hubdb\_table\_column(<tableId or name>, <columnId or column name>) %}

To get information on a column in table such as its label, type and options, use the `hubdb_table_column()` function

#### Column attributes[](https://developers.hubspot.com/docs/cms/data/hubdb#column-attributes)

The attributes listed below are in reference to the variable that `hubdb_table_column()` was assigned to in the above code. Your variable may differ.  
_Note: It is recommended assigning this to a variable for easier use. If you don't want to do that, you can use  
`{{ hubdb_table_column(<tableId>,<columnId or column name>).attribute }}`_

Use this table to describe parameters / fields
| Attribute | Description |
| --- | --- |
| 
`table_info.id`

 | 

The ID of the column.

 |
| 

`table_info.name`

 | 

The name of the column.

 |
| 

`table_info.label`

 | 

The label to be used for the column.

 |
| 

`table_info.type`

 | 

Type of this column.

 |
| 

`table_info.options`

 | 

For select column type, this is a map of `optionId` to `option` information.

 |
| 

`table_info.foreignIds`

 | 

For foreignId column types, a list of foreignIds (with `id` and `name` properties).

 |

#### Column methods[](https://developers.hubspot.com/docs/cms/data/hubdb#column-methods)

Use this table to describe parameters / fields
| Method | Description |
| --- | --- |
| 
`getOptionByName("<option name")`

 | 

For select column types, get option information by the options name.

 |

#### Rich Text columns[](https://developers.hubspot.com/docs/cms/data/hubdb#rich-text-columns)

The `richtext` column type functions similar to the rich text field you see for modules.

The data is stored as HTML, and the HubDB UI provides a text editing interface. However, when editing a HubDB table through HubSpot's UI, you cannot edit source code directly. This prevents situations where a non-technical user may input invalid HTML, preventing unintended issues with the appearance or functionality of your site. For situations where you need an embed code or more custom HTML you can use the embed feature in the rich text editor to place your custom code. 

HubDB tutorials and resources[](https://developers.hubspot.com/docs/cms/data/hubdb#hubdb-tutorials-and-resources)
-----------------------------------------------------------------------------------------------------------------

*   [Event Registration App](/docs/cms/features/serverless-functions/event-registration-app)[](/docs/cms/guides/hubdb/join-multiple-tables)[](https://designers.hubspot.com/how-to-add-videos-to-dynamic-pages-in-hubdb)
*   [How to build a dynamic team member page with HubDB](https://designers.hubspot.com/docs/tutorials/how-to-build-a-dynamic-team-member-page-with-hubdb)
*   [How to add videos to dynamic pages](/docs/cms/guides/dynamic-pages/hubdb/video)
*   [How to build multilevel dynamic pages using HubDB](/docs/cms/guides/dynamic-pages/hubdb/multilevel)[](https://designers.hubspot.com/docs/tutorials/lets-build-a-page-with-a-map-with-hubdb)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/data/hubdb#page-feedback)
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