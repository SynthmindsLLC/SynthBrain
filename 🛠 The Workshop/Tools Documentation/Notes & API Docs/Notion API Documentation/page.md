---
Please provide me with more information!  To help you create a compelling mission statement, I need to know: "**1. What is the purpose of this mission statement?** "
* Is it for a company, organization, project, or individual?
* What is the overall goal you are trying to achieve?

**2. What are the key values or beliefs that guide your actions?** 
* What do you stand for?
* What principles are important to you?

**3. What is your target audience?** 
* Who are you trying to reach with this mission?
* What are their needs and desires?

**4. What makes you unique or different from others?** 
* What are your strengths and competitive advantages?

**5.  What is your desired impact?** 
* What do you want to accomplish in the world?
* How will your work make a difference?

Once you provide me with this information, I can help you craft a clear, concise, and inspiring mission statement.
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

Page
====

The Page object contains the [page property values](/reference/page-property-values) of a single Notion page.

Example page object

`{     "object": "page",     "id": "be633bf1-dfa0-436d-b259-571129a590e5",     "created_time": "2022-10-24T22:54:00.000Z",     "last_edited_time": "2023-03-08T18:25:00.000Z",     "created_by": {         "object": "user",         "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"     },     "last_edited_by": {         "object": "user",         "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"     },     "cover": null,     "icon": {         "type": "emoji",         "emoji": "🐞"     },     "parent": {         "type": "database_id",         "database_id": "a1d8501e-1ac1-43e9-a6bd-ea9fe6c8822b"     },     "in_trash": true,     "properties": {         "Due date": {             "id": "M%3BBw",             "type": "date",             "date": {                 "start": "2023-02-23",                 "end": null,                 "time_zone": null             }         },         "Status": {             "id": "Z%3ClH",             "type": "status",             "status": {                 "id": "86ddb6ec-0627-47f8-800d-b65afd28be13",                 "name": "Not started",                 "color": "default"             }         },         "Title": {             "id": "title",             "type": "title",             "title": [                 {                     "type": "text",                     "text": {                         "content": "Bug bash",                         "link": null                     },                     "annotations": {                         "bold": false,                         "italic": false,                         "strikethrough": false,                         "underline": false,                         "code": false,                         "color": "default"                     },                     "plain_text": "Bug bash",                     "href": null                 }             ]         }     },     "url": "https://www.notion.so/Bug-bash-be633bf1dfa0436db259571129a590e5", 		"public_url": "https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d" }`

All pages have a [Parent](/reference/parent-object). If the parent is a [database](/reference/database), the property values conform to the schema laid out database's [properties](/reference/property-object). Otherwise, the only property value is the `title`.

Page content is available as [blocks](/reference/block). The content can be read using [retrieve block children](/reference/get-block-children) and appended using [append block children](/reference/patch-block-children).

Page object properties

[](#page-object-properties)
-----------------------------------------------------

> 📘
> --
> 
> Properties marked with an \* are available to integrations with any capabilities. Other properties require read content capabilities in order to be returned from the Notion API. For more information on integration capabilities, see the [capabilities guide](/reference/capabilities).

| Property | Type | Description | Example value |
| --- | --- | --- | --- |
| `object`\* | `string` | Always `"page"`. | `"page"` |
| `id`\* | `string` (UUIDv4) | Unique identifier of the page. | `"45ee8d13-687b-47ce-a5ca-6e2e45548c4b"` |
| `created_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this page was created. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2020-03-17T19:10:04.968Z"` |
| `created_by` | [Partial User](/reference/user) | User who created the page. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}` |
| `last_edited_time` | `string` ([ISO 8601 date and time](https://en.wikipedia.org/wiki/ISO_8601)) | Date and time when this page was updated. Formatted as an [ISO 8601 date time](https://en.wikipedia.org/wiki/ISO_8601) string. | `"2020-03-17T19:10:04.968Z"` |
| `last_edited_by` | [Partial User](/reference/user) | User who last edited the page. | `{"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}` |
| `in_trash` | `boolean` | Whether a page has been deleted. | `false` |
| `icon` | [File Object](/reference/file-object) (only `type` of `"external"` is supported currently) or [Emoji object](/reference/emoji-object) | Page icon. |  |
| `cover` | [File object](/reference/file-object) (only `type` of `"external"` is supported currently) | Page cover image. |  |
| `properties` | `object` | Property values of this page. As of version `2022-06-28`, `properties` only contains the ID of the property; in prior versions `properties` contained the values as well.  
  
If `parent.type` is `"page_id"` or `"workspace"`, then the only valid key is `title`.  
  
If `parent.type` is `"database_id"`, then the keys and values of this field are determined by the [`properties`](/reference/property-object) of the [database](/reference/database) this page belongs to.  
  
`key` string  
Name of a property as it appears in Notion.  
  
`value` object  
See [Property value object](/reference/property-value-object). | `{ "id": "A%40Hk" }` |
| `parent` | `object` | Information about the page's parent. See [Parent object](/reference/parent-object). | `{ "type": "database_id", "database_id": "d9824bdc-8445-4327-be8b-5b47500af6ce" }` |
| `url` | `string` | The URL of the Notion page. | `"https://www.notion.so/Avocado-d093f1d200464ce78b36e58a3f0d8043"` |
| `public_url` | `string` | The public page URL if the page has been published to the web. Otherwise, `null`. | `"https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"1` |

Updated 26 days ago

* * *

[

Rich text

](/reference/rich-text)[

Page properties

](/reference/page-property-values)

Did this page help you?

Yes

No

Updated 26 days ago

* * *

[

Rich text

](/reference/rich-text)[

Page properties

](/reference/page-property-values)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Page object properties](#page-object-properties)

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