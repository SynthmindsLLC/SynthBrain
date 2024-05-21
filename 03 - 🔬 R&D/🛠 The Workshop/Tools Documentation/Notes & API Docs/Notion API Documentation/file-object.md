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

File
====

> 📘
> --
> 
> The Notion API does not yet support uploading files to Notion.

File objects contain data about a file that is uploaded to Notion, or data about an external file that is linked to in Notion.

A file object corresponding to a file that has been uploaded to Notion

`{   "type": "file",   "file": {     "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7b8b0713-dbd4-4962-b38b-955b6c49a573/My_test_image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221024%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221024T205211Z&X-Amz-Expires=3600&X-Amz-Signature=208aa971577ff05e75e68354e8a9488697288ff3fb3879c2d599433a7625bf90&X-Amz-SignedHeaders=host&x-id=GetObject",     "expiry_time": "2022-10-24T22:49:22.765Z"   } }`

A file object corresponding to an external file that has been linked to in Notion

`{   "type": "external",   "external": {     "url": "https://images.unsplash.com/photo-1525310072745-f49212b5ac6d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1065&q=80"   } }`

Page, embed, image, video, file, pdf, and bookmark [block types](/reference/block) all contain file objects. Icon and cover [page object values](/reference/page#all-pages) also contain file objects.

Each file object includes the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `type` | `string` (enum) | The type of the file object. Possible type values are: `"external"`, `"file"`. | `"external"` |
| `external` | `file` | `object` | An object containing type-specific configuration. The key of the object is `external` for external files, and `file` for Notion-hosted files.  
  
Refer to the type sections below for details on type-specific values. | Refer to to the type-specific sections below for examples. |

Notion-hosted files

[](#notion-hosted-files)
-----------------------------------------------

All Notion-hosted files have a `type` of `"file"`. The corresponding `file` specific object contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `url` | `string` | An authenticated S3 URL to the file.  
  
The URL is valid for one hour. If the link expires, then you can send an API request to get an updated URL. | `"https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9bc6c6e0-32b8-4d55-8c12-3ae931f43a01/brocolli.jpeg?..."` |
| `expiry_time` | `string` ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date time) | The date and time when the link expires, formatted as an ISO 8601 date time string. | `"2020-03-17T19:10:04.968Z"` |

You can retrieve links to Notion-hosted files via the [Retrieve block children endpoint](/reference/get-block-children).

### 

Example: Retrieve a URL to a Notion-hosted file using GET /children

[](#example-retrieve-a-url-to-a-notion-hosted-file-using-get-children)

The following example passes the ID of the page that includes the desired file as the block\_id path param.

#### 

Request

[](#request)

cURL

`curl 'https://api.notion.com/v1/blocks/13d6da822f9343fa8ec14c89b8184d5a/children?page_size=100' \   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \   -H "Notion-Version: 2022-06-28"`

#### 

Response

[](#response)

JSON

`{     "object": "list",     "results": [         {             "object": "block",             "id": "47a920e4-346c-4df8-ae78-905ce10adcb8",             "parent": {                 "type": "page_id",                 "page_id": "13d6da82-2f93-43fa-8ec1-4c89b8184d5a"             },             "created_time": "2022-12-15T00:18:00.000Z",             "last_edited_time": "2022-12-15T00:18:00.000Z",             "created_by": {                 "object": "user",                 "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"             },             "last_edited_by": {                 "object": "user",                 "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"             },             "has_children": false,             "in_trash": false,             "type": "paragraph",             "paragraph": {                 "rich_text": [],                 "color": "default"             }         },         {             "object": "block",             "id": "3c29dedf-00a5-4915-b137-120c61f5e5d8",             "parent": {                 "type": "page_id",                 "page_id": "13d6da82-2f93-43fa-8ec1-4c89b8184d5a"             },             "created_time": "2022-12-15T00:18:00.000Z",             "last_edited_time": "2022-12-15T00:18:00.000Z",             "created_by": {                 "object": "user",                 "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"             },             "last_edited_by": {                 "object": "user",                 "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"             },             "has_children": false,             "in_trash": false,             "type": "file",             "file": {                 "caption": [],                 "type": "file",                 "file": {                     "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fa6c03f0-e608-45d0-9327-4cd7a5e56e71/TestFile.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221215T002012Z&X-Amz-Expires=3600&X-Amz-Signature=bf13ca59f618077852298cb92aedc4dd1becdc961c31d73cbc030ef93f2853c4&X-Amz-SignedHeaders=host&x-id=GetObject",                     "expiry_time": "2022-12-15T01:20:12.928Z"                 }             }         },     ],     "next_cursor": null,     "has_more": false,     "type": "block",     "block": {} }`

External files

[](#external-files)
-------------------------------------

An external file is any URL linked to in Notion that isn’t hosted by Notion. All external files have a type of `"external"`. The corresponding `file` specific object contains the following fields:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `url` | `string` | A link to the externally hosted content. | `"https://website.domain/files/doc.txt"` |

The Notion API supports adding, retrieving, and updating links to external files.

### 

Example: Add a URL to an external file using PATCH /children

[](#example-add-a-url-to-an-external-file-using-patch-children)

Use the [Append block children](/reference/patch-block-children) endpoint to add external files to Notion. Pass a [block type object](/reference/block#block-type-object) in the body that that details information about the external file.

The following example request embeds a PDF in a Notion page. It passes the ID of the target page as the `block_id` path param and information about the file to append in the request body.

#### 

Request

[](#request-1)

cURL

`curl -X PATCH 'https://api.notion.com/v1/blocks/13d6da822f9343fa8ec14c89b8184d5a/children' \   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \   -H "Content-Type: application/json" \   -H "Notion-Version: 2022-06-28" \   --data '{   "children": [     {       "object": "block",       "type": "pdf",       "pdf": {         "type": "external",         "external": {           "url": "https://www.yourwebsite.dev/files/TestFile.pdf"         }       }     }   ] }'`

#### 

Response

[](#response-1)

JSON

`{   "object": "list",   "results": [     {       "object": "block",       "id": "af1459f2-d2c5-4ca6-9f05-8038e6eb167f",       "parent": {         "type": "page_id",         "page_id": "13d6da82-2f93-43fa-8ec1-4c89b8184d5a"       },       "created_time": "2022-12-15T01:14:00.000Z",       "last_edited_time": "2022-12-15T01:14:00.000Z",       "created_by": {         "object": "user",         "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"       },       "last_edited_by": {         "object": "user",         "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"       },       "has_children": false,       "in_trash": false,       "type": "pdf",       "pdf": {         "caption": [],         "type": "external",         "external": {           "url": "https://www.yourwebsite.dev/files/TestFile.pdf"         }       }     }   ],   "next_cursor": null,   "has_more": false,   "type": "block",   "block": {} }`

### 

Example: Retrieve a link to an external file using GET /children

[](#example-retrieve-a-link-to-an-external-file-using-get-children)

Use the [Retrieve block children endpoint](/reference/get-block-children) on the file’s parent block in order to retrieve the file object. The file itself is contained in its own block of type `file`.

The following example passes the ID of the page that includes the desired file as the `block_id` path param.

#### 

Request

[](#request-2)

cURL

`curl 'https://api.notion.com/v1/blocks/af1459f2-d2c5-4ca6-9f05-8038e6eb167f/children?page_size=100' \   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \   -H "Notion-Version: 2022-06-28"`

#### 

Response

[](#response-2)

JSON

`{   "object": "list",   "results": [     {       "object": "block",       "id": "47a920e4-346c-4df8-ae78-905ce10adcb8",       "parent": {         "type": "page_id",         "page_id": "13d6da82-2f93-43fa-8ec1-4c89b8184d5a"       },       "created_time": "2022-12-15T00:18:00.000Z",       "last_edited_time": "2022-12-15T00:18:00.000Z",       "created_by": {         "object": "user",         "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"       },       "last_edited_by": {         "object": "user",         "id": "c2f20311-9e54-4d11-8c79-7398424ae41e"       },       "has_children": false,       "in_trash": false,       "type": "paragraph",       "paragraph": {         "rich_text": [],         "color": "default"       }     },     {       "object": "block",       "id": "af1459f2-d2c5-4ca6-9f05-8038e6eb167f",       "parent": {         "type": "page_id",         "page_id": "13d6da82-2f93-43fa-8ec1-4c89b8184d5a"       },       "created_time": "2022-12-15T01:14:00.000Z",       "last_edited_time": "2022-12-15T01:14:00.000Z",       "created_by": {         "object": "user",         "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"       },       "last_edited_by": {         "object": "user",         "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"       },       "has_children": false,       "in_trash": false,       "type": "pdf",       "pdf": {         "caption": [],         "type": "external",         "external": {           "url": "https://www.yourwebsite.dev/files/TestFile.pdf"         }       }     }   ],   "next_cursor": null,   "has_more": false,   "type": "block",   "block": {} }`

### 

Example: Update a link to an external file using PATCH /blocks/{block\_id}

[](#example-update-a-link-to-an-external-file-using-patch-blocksblock_id)

Use the [Update a block](/reference/update-a-block) endpoint to update a link to an external file in Notion.

The body of the request depends on the file’s Notion [block type](/reference/block#block-type-object). Common file block types include `image`, `pdf`, and `video`.

> 📘
> --
> 
> If you don’t know the file’s Notion block type, then send a request to the Retrieve block children endpoint using the parent block ID and find the corresponding child block.

The following example updates the external file in a `pdf` block type. It passes the ID of the block as the `block_id` path param and information about the new file in the request body.

#### 

Request

[](#request-3)

cURL

`curl https://api.notion.com/v1/blocks/af1459f2-d2c5-4ca6-9f05-8038e6eb167f \   -H 'Authorization: Bearer '"$NOTION_API_KEY"'' \   -H "Content-Type: application/json" \   -H "Notion-Version: 2022-06-28" \   -X PATCH \   --data '{ 	  "pdf": {  			"external": { 				"url": "https://www.yourwebsite.dev/files/NewFile.pdf" 			} 	  } 	}'`

#### 

Response

[](#response-3)

JSON

`{   "object": "block",   "id": "af1459f2-d2c5-4ca6-9f05-8038e6eb167f",   "parent": {     "type": "page_id",     "page_id": "13d6da82-2f93-43fa-8ec1-4c89b8184d5a"   },   "created_time": "2022-12-15T01:14:00.000Z",   "last_edited_time": "2022-12-16T21:23:00.000Z",   "created_by": {     "object": "user",     "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"   },   "last_edited_by": {     "object": "user",     "id": "9188c6a5-7381-452f-b3dc-d4865aa89bdf"   },   "has_children": false,   "in_trash": false,   "type": "pdf",   "pdf": {     "caption": [],     "type": "external",     "external": {       "url": "https://www.yourwebsite.dev/files/NewFile.pdf"     }   } }`

> 📘
> --
> 
> To modify page or database property values that are made from file objects, like `icon`, `cover`, or `files` page property values, use the [update page](/reference/patch-page) or [update database](/reference/update-a-database) endpoints.

Updated 26 days ago

* * *

[

Unfurl attribute (Link Previews)

](/reference/unfurl-attribute-object)[

Emoji

](/reference/emoji-object)

Did this page help you?

Yes

No

Updated 26 days ago

* * *

[

Unfurl attribute (Link Previews)

](/reference/unfurl-attribute-object)[

Emoji

](/reference/emoji-object)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [Notion-hosted files](#notion-hosted-files)
        *   [Example: Retrieve a URL to a Notion-hosted file using GET /children](#example-retrieve-a-url-to-a-notion-hosted-file-using-get-children)
    *   [External files](#external-files)
        *   [Example: Add a URL to an external file using PATCH /children](#example-add-a-url-to-an-external-file-using-patch-children)
        *   [Example: Retrieve a link to an external file using GET /children](#example-retrieve-a-link-to-an-external-file-using-get-children)
        *   [Example: Update a link to an external file using PATCH /blocks/{block\_id}](#example-update-a-link-to-an-external-file-using-patch-blocksblock_id)

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