---
Please provide me with more context! To help you craft a compelling mission statement, I need to know: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal, or something else?"
* **What are the key values and goals?** What do you want to achieve?
* **Who is your target audience?** Who are you trying to reach with this mission?

Once I have this information, I can help you write a powerful and inspiring mission statement.
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

Unfurl attribute (Link Previews)
================================

A Link Preview is created from an array of unfurl attribute objects.

A [Link Preview](/docs/link-previews) is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user shares an enabled link. Developers can build Link Preview integrations to customize how links for domains they own look when the links unfurl in a Notion workspace. The display of the Link Preview is customizable in terms of content and layout.

> 👍
> 
> Learn how to build your own Link Preview integration
> 
> 
> ----------------------------------------------------------
> 
> *   [Introduction to Link Preview integrations](/docs/link-previews) guide
> *   [Build a Link Preview integration](/docs/build-a-link-preview-integration) guide
> *   [Help Centre](https://www.notion.so/help/guides/notion-api-link-previews-feature) guide

Link Previews can be displayed in their full format, or they can be shown as a "Mention".

Let's first look at an example of a full-format Link Preview:

![1242](https://files.readme.io/a034247-link_preview.png "link_preview.png")

Example Link Preview in a Notion workspace

Here is the same link again but now as a Mention — a miniature version of a Link Preview that uses the same data.

![1060](https://files.readme.io/f588a6f-mention.png "mention.png")

Example Mention in a Notion workspace

A Link Preview or Mention displays data that is sent to Notion as an array of unfurl attribute objects. There are a number of optional attributes developers cannot. However, **every array must contain a `title` attribute and a `dev` attribute.**

Using the same Link Preview and Mention we saw above, let's look at the array of unfurl attribute objects that would render these previews. The following payload creates the example Link Preview and Mention above:

JSON

`[   {     "id": "title",     "name": "Title",     "type": "inline",     "inline": {       "title": {         "value": "Feature Request: Link Previews",         "section": "title"       }     }   },   {     "id": "dev",     "name": "Developer Name",     "type": "inline",     "inline": {       "plain_text": {         "value": "Acme Inc",         "section": "secondary"       }     }   },   {     "id": "state",     "name": "State",     "type": "relation",     "relation": {       "uri": "acme:item_state/open",       "mention": {         "section": "primary"       }     }   },   {     "id": "itemId",     "name": "Item Id",     "type": "inline",     "inline": {       "plain_text": {         "value": "#23487",         "section": "identifier"       }     }   },   {     "id": "itemIcon",     "name": "Item Icon",     "type": "inline",     "inline": {       "color": {         "value": {           "r": 247,           "g": 247,           "b": 42         },         "section": "entity"       }     }   },   {     "id": "description",     "name": "Description",     "type": "inline",     "inline": {       "plain_text": {         "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?",         "section": "body"       }     }   },   {     "id": "updated_at",     "name": "Updated At",     "type": "inline",     "inline": {       "datetime": {         "value": "2022-01-11T19:53:18.829Z",         "section": "secondary"       }     }   },   {     "id": "label",     "name": "Label",     "type": "inline",     "inline": {       "enum": {         "value": "🔨 Ready to Build",         "color": {           "r": 100,           "g": 100,           "b": 100         },         "section": "primary"       }     }   },   {     "id": "media",     "name": "Embed",     "embed": {       "src_url": "https://c.tenor.com/XgaU95K_XiwAAAAC/kermit-typing.gif",       "image": {         "section": "embed"       }     }   } ]`

Each unfurl attribute object in this array maps to a different customizable section of a Link Preview. (To learn more about each section, jump to [The `section` value](/reference/unfurl-attribute-object#the-section-value).

![Anatomy of a Link Preview in Notion](https://files.readme.io/3d6f5ec-Untitled_1.png)

Anatomy of a Link Preview in Notion

First, let's let at the properties in each individual unfurl attribute object.

The unfurl attribute object

[](#the-unfurl-attribute-object)
---------------------------------------------------------------

Example unfurl attribute object

`{     "id": "title",     "name": "Title",     "type": "inline",     "inline": {       "title": {         "value": "Feature Request: Link Previews",         "section": "title"       }     }   }`

Each unfurl attribute object contains the following values:

| Field | Type | Description | Example value |
| --- | --- | --- | --- |
| `id` | `string` | A unique identifier for the attribute.  
  
If more than one attribute with the same `id` is provided, then the latter attribute overrides the value of the first. | `"title"` |
| `name` | `string` | A human readable name describing the attribute. | `"Title"` |
| `type` | `inline` || `embed` | The type of attribute.  
  
Most attributes are `inline`. Use `embed` for rich media sub-types like `image`, `video`, or `audio`. | `"inline"` |
| `inline` || `embed` | `object` | An object whose key is a sub-type. The child sub-type object includes the `value` to display and the `section` of the Link Preview where the data is rendered. | `{ "title": { "value": "Feature Request: Link Previews", "section": "title" } }` |

### 

Inline sub-type objects

[](#inline-sub-type-objects)

The key of inline sub-type objects represents the kind of sub-type. The values of the key are the `value` to display and the `section` of the Link Preview where the value is rendered.

| Sub-type | Description | Example value |
| --- | --- | --- |
| `color` | A color with r, b, g values. | `{ "value": { "r": 247, "g": 247, "b": 42 }, "section": "entity" }` |
| `date` | A date. | `{ "value": "2022-01-11", "section": "secondary" }` |
| `datetime` | A datetime. | `{ "value": "2022-01-11T19:53:18.829Z", "section": "secondary" }` |
| `enum` | A string value and optional color object. | `{ "value": "🔨 Ready to Build", "color": { "r": 100, "g": 100, "b": 100 }, "section": "primary" }` |
| `plain_text` | Any plain text content. | `{ "value": "Would love to be able to preview some Acme resources in Notion!\n Maybe an open item?", "section": "body" }` |
| `title`\* | The title of the Link Preview.  
  
\*An unfurl attribute object of this type must be included in every payload to create a Link Preview. | `{ "value": "Feature Request: Link Previews", "section": "title" }` |

#### 

The `dev` attribute

[](#the-dev-attribute)

Every array of attribute objects that is sent to Notion to create a Link Preview must also include a `dev` attribute. The attribute indicates the developer or company who created the Link Preview. It takes the following format:

Example dev attribute

`{     "id": "dev",     "name": "Developer Name",     "type": "inline",     "inline": {       "plain_text": {         "value": "Acme Inc",         "section": "secondary"      }    }  }`

### 

Embed sub-type child objects

[](#embed-sub-type-child-objects)

You can use the `embed` sub-type object to add rich content like JPGs, GIFs, or iFrames to your Link Preview.

![1228](https://files.readme.io/d482801-embed.png "embed.png")

An example Link Preview that embeds an image of Kermit the Frog

All embed sub-type objects contain: a `src_url` field that is a link to the embed, and an object whose key is the sub-type of the embed and whose value is an object indicating the `section` of the Link Preview where the value is rendered.

| Sub-type | Description | Example value |
| --- | --- | --- |
| `audio` | Audio from a source URL. | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "audio": { "section": "embed" } }` |
| `html` | HTML from a source URL that is rendered in an iFrame. | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.html", "html": { "section": "embed" } }` |
| `image` | Image from a source URL. | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.png", "image": { "section": "avatar" } }` |
| `video` | Video from a source URL. | `{ "src_url": "https://s3.us-east-3.amazonaws.com/12345.mp4", "video": { "section": "embed" } }` |

> 📘
> --
> 
> There’s no need to ask a user to log in to your service in an iFrame embed. If they’re using a Link Preview, then they’ve already authenticated.

### 

The `section` value

[](#the-section-value)

The `section` value of an unfurl attribute object defines where an attribute is rendered in the Link Preview or Mention.

![1378](https://files.readme.io/121dcba-sections_lp.png "sections_lp.png")

The sections of a Link Preview

![926](https://files.readme.io/1de6886-sections_mention.png "sections_mention.png")

The sections of a Mention

A `section` is specified in the sub-type object for the attribute. Refer to the table below for details about each `section` and its valid parent sub-types.

| Section | Description | Valid parent sub-types |
| --- | --- | --- |
| avatar | The picture found on the bottom left of a Link Preview. | `image`, `plain_text` |
| background | A background color for the Link Preview. | `color` |
| body | The main string content of a Link Preview. | `plain_text` |
| embed | The large space where the content of an `embed` attribute type is displayed in a Link Preview. | `audio`, `html`, `image`, `pdf`, `video` |
| entity | The small picture found in the subheading of a Link Preview and in a Mention. | `color`, `image` |
| identifier | The subheading found on the bottom of a Link Preview and on the left side of a Mention. | `image`, `plain_text` |
| primary | The first subheading section. | `enum`, `date`, `datetime`, `plain_text` |
| secondary | The second subheading section. | `date`, `datetime`, `plain_text` |
| title\* | The main heading in a Link Preview or Mention.  
  
\*Required. | `title` |

Updated 11 months ago

* * *

[

Comment

](/reference/comment-object)[

File

](/reference/file-object)

Did this page help you?

Yes

No

Updated 11 months ago

* * *

[

Comment

](/reference/comment-object)[

File

](/reference/file-object)

Did this page help you?

Yes

No

*   [Table of Contents](#)
*   *   [The unfurl attribute object](#the-unfurl-attribute-object)
        *   [Inline sub-type objects](#inline-sub-type-objects)
        *   [Embed sub-type child objects](#embed-sub-type-child-objects)
        *   [The `section` value](#the-section-value)

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