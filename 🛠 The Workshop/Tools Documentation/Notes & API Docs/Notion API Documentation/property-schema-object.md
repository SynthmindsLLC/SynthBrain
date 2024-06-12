---
Please provide me with more context! I need to know what your mission is about in order to help you. 

For example, tell me: "* **What is the overall goal of your mission?** What are you trying to achieve?"
* **Who is involved in the mission?** Are you working alone or with a team?
* **What is the scope of the mission?** Is it a small project or a large undertaking?
* **What are the key objectives of the mission?** What are the specific things you need to accomplish?

Once you give me more information, I can help you write a compelling and impactful mission statement.
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

Property Schema Object
======================

Metadata that controls how a database property behaves.

Database properties

[](#database-properties)
-----------------------------------------------

Each database property schema object has at least one key which is the property type. This type contains behavior of this property. Possible values of this key are `"title"`, `"rich_text"`, `"number"`, `"select"`, `"multi_select"`, `"date"`, `"people"`, `"files"`, `"checkbox"`, `"url"`, `"email"`, `"phone_number"`, `"formula"`, `"relation"`, `"rollup"`, `"created_time"`, `"created_by"`, `"last_edited_time"`, `"last_edited_by"`.

Title configuration

[](#title-configuration)
-----------------------------------------------

Each database must have exactly one database property schema object of type `"title"`. This database property controls the title that appears at the top of the page when the page is opened. Title database property objects have no additional configuration within the `title` property.

Text configuration

[](#text-configuration)
---------------------------------------------

Text database property schema objects have no additional configuration within the `rich_text` property.

Number configuration

[](#number-configuration)
-------------------------------------------------

Number database property schema objects optionally contain the following configuration within the `number` property.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `format` | optional `string` (enum) | How the number is displayed in Notion. Potential values include: `number`, `number_with_commas`, `percent`, `dollar`, `canadian_dollar`, `euro`, `pound`, `yen`, `ruble`, `rupee`, `won`, `yuan`, `real`, `lira`, `rupiah`, `franc`, `hong_kong_dollar`, `new_zealand_dollar`, `krona`, `norwegian_krone`, `mexican_peso`, `rand`, `new_taiwan_dollar`, `danish_krone`, `zloty`, `baht`, `forint`, `koruna`, `shekel`, `chilean_peso`, `philippine_peso`, `dirham`, `colombian_peso`, `riyal`, `ringgit`, `leu`, `argentine_peso`, `uruguayan_peso`, `singapore_dollar`. | `"percent"` |

Select configuration

[](#select-configuration)
-------------------------------------------------

Select database property schema objects optionally contain the following configuration within the `select` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `options` | optional array of [select option objects](#select-options). | Sorted list of options available for this property. |  |

### 

Select options

[](#select-options)

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `name` | `string` | Name of the option as it appears in Notion. | `"Fruit"` |
| `color` | optional `string` (enum) | Color of the option. Possible values include: `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `red`. | `"red"` |

Multi-select configuration

[](#multi-select-configuration)
-------------------------------------------------------------

Multi-select database property schema objects optionally contain the following configuration within the `multi_select` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `options` | optional array of [multi-select option objects](#multi-select-options). | Settings for multi select properties. |  |

### 

Multi-select options

[](#multi-select-options)

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `name` | `string` | Name of the option as it appears in Notion. | `"Fruit"` |
| `color` | optional `string` (enum) | Color of the option. Possible values include: `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `red`. | `"red"` |

Date configuration

[](#date-configuration)
---------------------------------------------

Date database property schema objects have no additional configuration within the `date` property.

People configuration

[](#people-configuration)
-------------------------------------------------

People database property schema objects have no additional configuration within the `people` property.

File configuration

[](#file-configuration)
---------------------------------------------

File database property schema objects have no additional configuration within the `file` property.

Checkbox configuration

[](#checkbox-configuration)
-----------------------------------------------------

Checkbox database property schema objects have no additional configuration within the `checkbox` property.

URL configuration

[](#url-configuration)
-------------------------------------------

URL database property schema objects have no additional configuration within the `url` property.

Email configuration

[](#email-configuration)
-----------------------------------------------

Email database property schema objects have no additional configuration within the `email` property.

Phone number configuration

[](#phone-number-configuration)
-------------------------------------------------------------

Phone number database property schema objects have no additional configuration within the `phone_number` property.

Formula configuration

[](#formula-configuration)
---------------------------------------------------

Formula database property schema objects contain the following configuration within the `formula` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `expression` | `string` | Formula to evaluate for this property. You can read more about the [syntax for formulas](https://notion.so/notion/Formulas-28f3f5c3ae644c59b4d862046ea6a541) in the help center. | `"if(prop(\"In stock\"), 0, prop(\"Price\"))"` |

Relation configuration

[](#relation-configuration)
-----------------------------------------------------

Relation database property objects contain the following configuration within the `relation` property. In addition, they must contain a key corresponding with the value of `type`. The value is an object containing type-specific configuration. The type-specific configurations are defined below.

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `database_id` | `string` (UUID) | The database this relation refers to. This database must be shared with the integration. | `"668d797c-76fa-4934-9b05-ad288df2d136"` |
| `type` | `string` (optional enum) | The type of the relation. Can be `"single_property"` or `"dual_property"`. | `"single_property"` |

### 

Single property relation configuration

[](#single-property-relation-configuration)

Single property relation objects have no additional configuration within the `single_property` property.

### 

Dual property relation configuration

[](#dual-property-relation-configuration)

Dual property relation objects have no additional configuration within the `dual_property` property.

Rollup configuration

[](#rollup-configuration)
-------------------------------------------------

Rollup database property objects contain the following configuration within the `rollup` property:

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `relation_property_name` | optional `string` | The name of the relation property this property is responsible for rolling up. This relation is in the same database where the new rollup property is being created. One of `relation_property_name` or `relation_property_id` must be provided. | `"Meals"` |
| `relation_property_id` | optional `string` | The `id` of the relation property this property is responsible for rolling up. This relation is in the same database where the new rollup property is being created. One of `relation_property_name` or `relation_property_id` must be provided. | `"fy:{"` |
| `rollup_property_name` | optional `string` | The name of the property in the related database that is used as an input to `function`. The related database must be shared with the integration. One of `rollup_property_name` or `rollup_property_id` must be provided. | `"Name"` |
| `rollup_property_id` | optional `string` | The `id` of the property in the related database that is used as an input to `function`. The related database must be shared with the integration. One of `rollup_property_name` or `rollup_property_id` must be provided. | `"fy:{"` |
| `function` | `string` (enum) | The function that is evaluated for every page in the relation of the rollup.  
Possible values include: `count_all`, `count_values`, `count_unique_values`, `count_empty`, `count_not_empty`, `percent_empty`, `percent_not_empty`, `sum`, `average`, `median`, `min`, `max`, `range`, `show_original` | `"count"` |

Created time configuration

[](#created-time-configuration)
-------------------------------------------------------------

Created time database property schema objects have no additional configuration within the `created_time` property.

Created by configuration

[](#created-by-configuration)
---------------------------------------------------------

Created by database property schema objects have no additional configuration within the `created_by` property.

Last edited time configuration

[](#last-edited-time-configuration)
---------------------------------------------------------------------

Last edited time database property schema objects have no additional configuration within the `last_edited_time` property.

Last edited by configuration

[](#last-edited-by-configuration)
-----------------------------------------------------------------

Last edited by database property schema objects have no additional configuration within the `last_edited_by` property.

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
*   *   [Database properties](#database-properties)
    *   [Title configuration](#title-configuration)
    *   [Text configuration](#text-configuration)
    *   [Number configuration](#number-configuration)
    *   [Select configuration](#select-configuration)
        *   [Select options](#select-options)
    *   [Multi-select configuration](#multi-select-configuration)
        *   [Multi-select options](#multi-select-options)
    *   [Date configuration](#date-configuration)
    *   [People configuration](#people-configuration)
    *   [File configuration](#file-configuration)
    *   [Checkbox configuration](#checkbox-configuration)
    *   [URL configuration](#url-configuration)
    *   [Email configuration](#email-configuration)
    *   [Phone number configuration](#phone-number-configuration)
    *   [Formula configuration](#formula-configuration)
    *   [Relation configuration](#relation-configuration)
        *   [Single property relation configuration](#single-property-relation-configuration)
        *   [Dual property relation configuration](#dual-property-relation-configuration)
    *   [Rollup configuration](#rollup-configuration)
    *   [Created time configuration](#created-time-configuration)
    *   [Created by configuration](#created-by-configuration)
    *   [Last edited time configuration](#last-edited-time-configuration)
    *   [Last edited by configuration](#last-edited-by-configuration)

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