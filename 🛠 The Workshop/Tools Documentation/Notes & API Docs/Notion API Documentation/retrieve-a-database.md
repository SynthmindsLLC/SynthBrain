---
Please provide me with more context! I need to know what the mission is for.  

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a team, a personal goal, etc.?"
* **What are the goals of this mission?** What are you trying to achieve?
* **What are the key values and principles that will guide this mission?** 

Once I have this information, I can help you write a compelling and impactful mission statement.
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

Retrieve a database
===================

get https://api.notion.com/v1/databases/{database\_id}

Retrieves a [database object](/reference/database) — information that describes the structure and columns of a database — for a provided database ID. The response adheres to any limits to an integration’s capabilities.

To fetch database rows rather than columns, use the [Query a database](/reference/post-database-query) endpoint.

To find a database ID, navigate to the database URL in your Notion workspace. The ID is the string of characters in the URL that is between the slash following the workspace name (if applicable) and the question mark. The ID is a 32 characters alphanumeric string.

![Notion database ID](https://files.readme.io/64967fd-small-62e5027-notion_database_id.png)

Notion database ID

Refer to the [Build your first integration guide](/docs/create-a-notion-integration#step-3-save-the-database-id) for more details.

### 

Errors

[](#errors)

Each Public API endpoint can return several possible error codes. See the [Error codes section](/reference/status-codes#error-codes) of the Status codes documentation for more information.

### 

Additional resources

[](#additional-resources)

*   [How to share a database with your integration](/docs/create-a-notion-integration#give-your-integration-page-permissions)
*   [Working with databases guide](/docs/working-with-databases)

> 📘
> 
> Database relations must be shared with your integration
> 
> 
> -------------------------------------------------------------
> 
> To retrieve database properties from [database relations](https://www.notion.so/help/relations-and-rollups#what-is-a-database-relation), the related database must be shared with your integration in addition to the database being retrieved. If the related database is not shared, properties based on relations will not be included in the API response.

> 🚧
> 
> The Notion API does not support retrieving linked databases.
> 
> 
> ------------------------------------------------------------------
> 
> To fetch the information in a [linked database](https://www.notion.so/help/guides/using-linked-databases), share the original source database with your Notion integration.

Path Params

database\_id

string

required

An identifier for the Notion database.

Headers

Notion-Version

string

required

Responses

200

200


============

Response body

object

object

string

id

string

created\_time

string

last\_edited\_time

string

icon

object

type

string

emoji

string

cover

object

type

string

external

object

external object

url

string

title

array of objects

title

object

type

string

text

object

text object

annotations

object

annotations object

plain\_text

string

href

string

description

array of objects

description

object

type

string

text

object

text object

annotations

object

annotations object

plain\_text

string

href

string

properties

object

+1

object

+1 object

In stock

object

In stock object

Price

object

Price object

Description

object

Description object

Last ordered

object

Last ordered object

Meals

object

Meals object

Number of meals

object

Number of meals object

Store availability

object

Store availability object

Photo

object

Photo object

Food group

object

Food group object

Name

object

Name object

parent

object

type

string

page\_id

string

archived

boolean

is\_inline

boolean

public\_url

string

400

400


============

Response body

object

404

404


============

Response body

object

object

string

status

integer

code

string

message

string

429

429


============

Response body

object

object

string

status

integer

code

string

message

string

Updated 8 months ago

* * *

[

Query a database

](/reference/post-database-query)[

Update a database

](/reference/update-a-database)

Did this page help you?

Yes

No

Language

JavaScriptShell

Request

xxxxxxxxxx

1

const { Client } \= require('@notionhq/client');

2

​

3

const notion \= new Client({ auth: process.env.NOTION\_API\_KEY });

4

​

5

(async () \=> {

6

  const databaseId \= '668d797c-76fa-4934-9b05-ad288df2d136';

7

  const response \= await notion.databases.retrieve({ database\_id: databaseId });

8

  console.log(response);

9

})();

RESPONSE

Examples

Choose an example:

application/json

200 - Result400 - Result404 - Result429 - Result

Updated 8 months ago

* * *

[

Query a database

](/reference/post-database-query)[

Update a database

](/reference/update-a-database)

Did this page help you?

Yes

No

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