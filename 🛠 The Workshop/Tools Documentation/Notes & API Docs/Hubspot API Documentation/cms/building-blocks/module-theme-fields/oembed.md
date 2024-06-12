---
title: "HubL Funtions"
description: "A guide to HubSpot's front matter functions for specifying metadata and relationships for a piece of content"
type: "concept"
tags: "-hubl"
-front matter
relationships:
- "#related-to":
- "Conversation with ChatGPT about Artificial Intelligence"
- "Post about 1984"
- "Published Post"
- "Code"
- "Place"
- "Work (Books, Media)"
- "Group (Company, Institution, Governmental Body, etc.)"
- "Event"
- "Concept"
---

# MISSION
Act as an expert in YAML, specializing in Obsidian's front matter by inferring relationships from the note content. Your job is to take the content of a note, and generate the front matter in the EXPLICIT way as defined in this prompt.

# INSTRUCTIONS
1. Review the provided content by the user.
2. Review the ONTOLOGY and EXAMPLES
3. Output ONLY the YAML front matter, nothing before or after, adhering STRICTLY to the ONTOLOGY and EXAMPLE format.

### Hierarchical Relationships
1. `#is_a`: "Indicates that the subject is a subtype or instance of the object"
2. `#part_of`: "Indicates that the subject is a component or subset of the object"
3. `#has_part`: "Inverse of `#part_of`, indicates the object is a component of the subject"

### Associative Relationships
* `#related_to`: "Indicates a general association or connection between the subject and object"
* `#similar_to`: "Indicates that the subject and object share common characteristics"
* `#different_from`: "Indicates a distinction or contrast between the subject and object"

### Causal Relationships
* `#causes`: "Indicates that the subject brings about or triggers the object"
* `#caused_by`: "Inverse of `#causes`, indicates the object is the result of the subject"
* `#enables`: "Indicates that the subject makes the object possible or facilitates it"
* `#prevents`: "Indicates that the presence of the subject stops the object from happening"

### Temporal Relationships
* `#before`: "Indicates that the subject precedes the object in time"
* `#after`: "Indicates that the subject follows the object in time"
* `#during`: "Indicates that the subject occurs or exists at the same time as the object"

### Spatial Relationships
* `#located_in`: "Indicates that the subject is situated within the object"
* `#contains`: "Inverse of `#located_in`, indicates that the object is situated within the subject"
* `#adjacent_to`: "Indicates that the subject is close to or next to the object"

### Contribution Relationships
* `#authored_by`: "Indicates that the object created or originated the subject"
* `#contributed_to`: "Indicates that the object played a role in creating or influencing the subject"
* `#derived_from`: "Indicates that the subject is based on or adapted from the object"

### Functional Relationships
* `#used_for`: "Indicates the typical use or purpose of the subject"
* `#used_by`: "Indicates the user or system that utilizes the subject"
* `#requires`: "Indicates that the subject depends on or needs the object"
* `#produces`: "Indicates that the subject creates or generates the object as an output"

## ONTOLOGY
Use the standardized ontology of relationship types and structure your output as follows: "### YAML front matter will be organized into ONE of 8 different types, and generated following the pattern type."

#### Person
---
title: "Albert Einstein"
description: "German-born theoretical physicist, widely acknowledged to be one of the most influential people of the 20th century."
type: "person"
tags:
- "Physicist"
- "Scientist"
- "Theorist"
relationships:
- "#developed [[Theory of Relativity]]"
- "#influenced [[Quantum Mechanics]]"
- "#worked_at [[Princeton University]]"
- "#born_in [[Ulm, Germany]]"
birthdate: "1879-03-14"
deathdate: "1955-04-18"
---

#### Group (Company, Institution, Governmental Body, etc.)
---
title: "Microsoft Corporation"
description: "American multinational technology corporation that develops, manufactures, licenses, supports, and sells computer software, consumer electronics, personal computers, and related services."
type: "group"
tags:
- "Technology"
- "Software"
- "Hardware"
relationships:
- "#founded_by [[Bill Gates]], [[Paul Allen]]"
- "#headquartered_in [[Redmond, Washington]]"
- "#acquired [[Skype]], [[LinkedIn]], [[GitHub]]"
- "#competes_with [[Apple Inc.]], [[Google]]"
founded: "1975-04-04"
---

#### Event
---
title: "World War II"
description: "Global war that lasted from 1939 to 1945, involving the vast majority of the world's countriesincluding all of the great powersforming two opposing military alliances: the Allies and the Axis."
tags:
- "War"
- "Conflict"
- "History"
- "20th Century"
type: "event"
relationships:
- "#caused_by [[Aggression of Nazi Germany]], [[Invasion of Poland]]"
- "#involved [[United States]], [[United Kingdom]], [[Soviet Union]], [[Germany]], [[Japan]]"
- "#resulted_in [[United Nations]], [[Cold War]]"
start_date: "1939-09-01"
end_date: "1945-09-02"
---

#### Concept
---
title: "Quantum Mechanics"
description: "Fundamental theory in physics that describes the physical properties of nature at the scale of atoms and subatomic particles."
type: "concept"
tags:
- "Physics"
- "Science"
- "Quantum Theory"
relationships:
- "#developed_by [[Max Planck]], [[Albert Einstein]], [[Niels Bohr]]"
- "#explains [[Wave-particle duality]], [[Uncertainty principle]]"
- "#applies_to [[Atoms]], [[Subatomic particles]]"
- "#differs_from [[Classical mechanics]]"
---

#### Work (Books, Media)
---
title: "1984"
description: "Dystopian novel by George Orwell, published in 1949."
type: "work"
tags:
- "Literature"
- "Fiction"
- "Dystopia"
relationships:
- "#authored_by [[George Orwell]]"
- "#influenced_by [[Brave New World]], [[Animal Farm]]"
- "#similar_to [[Fahrenheit 451]], [[The Handmaid's Tale]]"
- "#adapted_into [[Nineteen Eighty-Four (film)]]"
published_date: "1949-06-08"
---

#### Place
---
title: "New York City"
description: "Most populous city in the United States."
type: "place"
tags:
- "City"
- "Metropolis"
- "United States"
relationships:
- "#located_in [[New York State]], [[United States]]"
- "#consists_of [[Manhattan]], [[Brooklyn]], [[Queens]], [[The Bronx]], [[Staten Island]]"
- "#home_to [[Statue of Liberty]], [[Empire State Building]], [[Central Park]]"
- "#part_of [[New York metropolitan area]]"
---

#### Conversation
---
title: "Conversation with ChatGPT about Artificial Intelligence"
description: "A dialogue between a human and ChatGPT, an AI language model, about the implications and future of AI."
type: "conversation"
tags:
- "Artificial Intelligence"
- "ChatGPT"
- "Language Model"
relationships:
- "#has_participant [[Human]]"
- "#has_participant [[ChatGPT]]"
- "#part_of [[OpenAI Conversations]]"
- "#discusses [[Artificial Intelligence]], [[Machine Learning]], [[Natural Language Processing]]"
participants:
- "Human"
- "ChatGPT"
date: "2023-06-10"
---

#### Code
---
title: "Quicksort Algorithm Implementation"
description: "An efficient sorting algorithm that works by recursively partitioning the array into smaller and smaller subarrays until each subarray contains only one element."
type: "code"
tags:
- "Algorithms"
- "Sorting"
- "Recursion"
relationships:
- "#implements [[Divide and conquer]]"
- "#has_time_complexity [[O(n log n)]]"
- "#used_for [[Sorting large datasets]]"
language: "Python"
version: "---"

# EXAMPLES
Front Matter will be organized into ONE of 8 different types, and generated following the pattern type.

### Person
---
title: "Albert Einstein"
description: "German-born theoretical physicist, widely acknowledged to be one of the most influential people of the 20th century."
type: "person"
tags:
- "Physicist"
- "Scientist"
- "Theorist"
relationships:
- "#developed [[Theory of Relativity]]"
- "#influenced [[Quantum Mechanics]]"
- "#worked_
---

HubL functions


==================

Last updated: March 29, 2024

Functions in HubL are similar to filters in that they accept parameters and generate a value. However, not all functions need to be applied to an initial template value, and instead they interact with other areas of your HubSpot environment.

If you maintain an older website, you may also want to check out the [list of deprecated HubL functions](/docs/cms/hubl/functions/deprecated).

Below, learn more about each HubL function and its syntax.

append[](https://developers.hubspot.com/docs/cms/hubl/functions#append)
-----------------------------------------------------------------------

Adds a single item to the end of a list.

{% set numbers\_under\_5 = \[1,2,3\] %} {% do numbers\_under\_5.append(4) %} {{numbers\_under\_5}}\[1, 2, 3, 4\]

| Parameter | Type | Description |
| --- | --- | --- |
| 
`item`

 | Any | 

Item to be appended to the list.

 |

blog\_all\_posts\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-all-posts-url)
--------------------------------------------------------------------------------------------------

The `**blog_all_posts_url**` function returns a full URL to the listing page for all blog posts for the specified blog. 

The example below shows how this function can be used as an anchor's `href`.

<a href="{{ blog\_all\_posts\_url("default") }}">All Marketing blog posts</a><a href="http://www.hubspot.com/marketing/all">All Marketing blog posts</a>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog id or "default" | 

Specifies which blog to use. The blog id is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |

blog\_author\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-author-url)
-------------------------------------------------------------------------------------------

The `**blog_author_url**` function returns a full URL to the specified blog author's listing page.

The example below shows how this function can be used as an anchor's `href`. This can be combined with `**blog_authors**` as shown in that function's examples.

<a href="{{ blog\_author\_url("default", "brian-halligan") }}">Brian Halligan</a><a href="http://blog.hubspot.com/marketing/author/brian-halligan">Brian Halligan</a>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog the author's listing page exists in. You can specify a blog by ID or use `"default"` to select the default blog. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |
| 

`author_slug`

 | String or HubL Var | 

Specifies which author to link to. Can use either `content.blog_post_author.slug` or a lowercase hyphenated name. Example: `"jane-doe"`.

 |

blog\_authors[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-authors)
------------------------------------------------------------------------------------

The `**blog_authors**` function returns a sequence of blog author objects for the specified blog, sorted by slug ascending. This sequence can be stored in a variable and iterated through to create custom author post filters.

The number of live posts by each author can be accessed with author.live\_posts.

**Please note:** this function has a limit of 250 authors. This function also has a limit of 10 calls per page.

The first line of the example below shows how the function returns a sequence of author objects. The rest of the example shows a use case of saving a sequence into a variable and then iterating though the author objects, printing a set of author listing links. The example assumes that the blog has 4 authors.

{{ blog\_authors("default", 250) }} {% set my\_authors = blog\_authors("default", 250) %} <ul> {% for author in my\_authors %} <li><a href="{{ blog\_author\_url(group.id, author.slug) }}">{{ author }}</a></li> {% endfor %} </ul>\[ Brian Halligan, Dharmesh Shah, Katie Burke, Kipp Bodnar\] <ul> <li><a href="http://blog.hubspot.com/marketing/author/brian-halligan">Brian Halligan</a></li></li> <li><a href="http://blog.hubspot.com/marketing/author/dharmesh-shah">Dharmesh Shah</a></li></li> <li><a href="http://blog.hubspot.com/marketing/author/katie-burke">Katie Burke</a></li></li> <li><a href="http://blog.hubspot.com/marketing/author/kipp-bodnar">Kipp Bodnar</a></li></li> </ul>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |
| 

`limit`

 | Integer | 

Sets the limit on the number of authors fetched.

 |

blog\_by\_id[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-by-id)
---------------------------------------------------------------------------------

The `**blog_by_id**` function returns a blog by ID. The below example code shows this function in use to generate a hyperlinked list item.

**Please note:** this function has a limit of 10 calls per page.

{% set my\_blog = blog\_by\_id(47104297) %} <ul> <li> <a href="{{ my\_blog.absolute\_url }}">{{my\_blog.html\_title}}</a> </li> </ul><ul> <li> <a href="http://blog.bikinginearnest.com/outdoors">Outdoor biking for the earnest</a> </li> </ul>

| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |

blog\_page\_link[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-page-link)
-----------------------------------------------------------------------------------------

The `**blog_page_link**` function generates the URL of a paginated view of your blog listing. The function takes a numeric parameter, which allows you to generate links for current, next, previous, or a specific page. This function is generally used in the `href` attribute of pagination anchor tags and must be used on your blog listing template.

The examples below show this function in use as an anchor `href`. The first example outputs the current page. The second example takes the number 7 parameter to specify the seventh page. The third example uses the `next_page_num` variable to generate a link that is relative to the current page number (you can also use the `last_page_num` variable for the previous page). The final example uses the `current_page_num` variable and a `+` operator to create a link that is 4 greater than the current page.

<a href="{{ blog\_page\_link(current\_page\_num) }}">Current page</a> <a href="{{ blog\_page\_link(7) }}">Page 7</a> <a href="{{ blog\_page\_link(next\_page\_num) }}">Next</a> <a href="{{ blog\_page\_link(current\_page\_num + 4) }}">Page Plus 4</a><a href="http://designers.hubspot.com/blog/page/1">Page 1</a> <a href="http://designers.hubspot.com/blog/page/7">Page 7</a> <a href="http://designers.hubspot.com/blog/page/2">Next</a> <a href="http://designers.hubspot.com/blog/page/5">Page Plus 4</a>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`page`

 | Number or HubL variable | 

Page number used to generate URL or HubL variable for page number.

 |

blog\_popular\_posts[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-popular-posts)
-------------------------------------------------------------------------------------------------

This function renders a set number of popular posts into a sequence. The sequence can then be saved into a variable and iterated through with a for loop, creating a custom post listing of your most popular posts. 

Results from this function are cached for six hours. To retrieve blog posts using HubL in a way that avoids caching, you may want to use [blog\_recent\_tag\_posts](#blog-recent-tag-posts) instead.

In the example code below, the first line shows how the function returns a sequence. The sequence is saved as a variable which is then used in a [for loop](/docs/cms/hubl/for-loops). [Any blog post variables](/docs/cms/hubl/variables#blog-variables) should use the name of the individual loop item rather than `content.`. In the example, `pop_post.name` is used. This technique can be used on blog templates and website pages.

**Please note:** this function has a limit of 200 posts. This function also has a limit of 10 calls per page.

{% set pop\_posts = blog\_popular\_posts("default", 5, \["marketing-tips", "sales-tips"\], "popular\_past\_month", "AND") %} {% for pop\_post in pop\_posts %} <div class="post-title">{{ pop\_post.name }}</div> {% endfor %}\[Popular post title 1, Popular post title 2, Popular post title 3, Popular post title 4, Popular post title 5\] <div class="post-title">Popular post title 1</div> <div class="post-title">Popular post title 2</div> <div class="post-title">Popular post title 3</div> <div class="post-title">Popular post title 4</div> <div class="post-title">Popular post title 5</div>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`.

 |
| 

`limit`

 | Integer | 

Specifies the number of posts to add to the sequence up to a limit of 200. If not specified, defaults to 10.

 |
| 

`tag_slug`

 | Array | 

Optional list of tags to filter posts by.

 |
| 

`time_frame`

 | String | 

Optional timeframe of analytics to filter posts by. Default is `"popular_past_year"`. Must be one of:

*   `"popular_all_time"` 
*   `"popular_past_year"`
*   `"popular_past_six_months"` 
*   `"popular_past_month"`

This parameter is required when including the `logical_operator` parameter.

 |
| 

`logical_operator`

 | String | 

When `tag_slug` contains multiple tags, use this operator to filter results with `AND` or `OR` logic. By default, this function uses `OR` logic to return posts tagged with any of the specified tags.

When including this parameter, `time_frame` is required.

 |

blog\_post\_archive\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-post-archive-url)
--------------------------------------------------------------------------------------------------------

The `**blog_post_archive_url**` function returns a full URL to the archive listing page for the given date values on the specified blog. This function has two required parameters and two optional parameters. The first parameter is a blog ID or simply the keyword `"default"`. The second is the year of archived posts you'd like to display.

The optional parameters include the month and day of archived posts you'd like to display, respectively.

The example below shows how this function can be used as an anchor's `href`.

<a href="{{ blog\_post\_archive\_url("default", 2017, 7, 5) }}">Posts from July 5th, 2017</a><a href="http://blog.hubspot.com/marketing/archive/2017/07/05">Posts from July 5th, 2017</a>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`.

 |
| 

`year`

 | Integer | 

The year.

 |
| 

`month`

 | Integer | 

The optional month.

 |
| 

`day`

 | Integer | 

The optional day.

 |

blog\_recent\_author\_posts[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-recent-author-posts)
--------------------------------------------------------------------------------------------------------------

The `**blog_recent_author_posts**` function returns a sequence of blog post objects for the specified author, sorted by most recent. This sequence of posts can be saved into a variable and iterated through with a for loop, creating a custom post listing of posts by a particular author. 

The function takes three parameters. The first parameter specifies which blog to collect posts by an author from. The value should be `"default"` or the blog ID of a particular blog (available in the URL of the Blog dashboard). The second parameter specifies which author to use. This parameter can use the **`content.blog_post_author.slug`** to use the author of the current post or accepts a lowercase hyphenated name such as `"brian-halligan"`. The third parameter specifies how many posts are retrieved. 

The first line of the example below demonstrates how the function returns a sequence of posts by an author. In this example, rather than specifying an exact author name, the current post author is used. The sequence is saved in a variable and looped through. [Any blog post variables](/docs/cms/hubl/variables#blog-variables) should use the name of the individual loop item rather than `content.`. In the example, `author_post.name` is used. This technique can be used on blog and page templates.

**Please note:** this function has a limit of 200 posts and 10 calls per page.

{{ blog\_recent\_author\_posts("default", content.blog\_post\_author.slug, 5 ) }} {% set author\_posts = blog\_recent\_author\_posts("default", content.blog\_post\_author.slug, 5) %} {% for author\_post in author\_posts %} <div class="post-title">{{ author\_post.name }}</div> {% endfor %}\[Post by author title 1, Post by author title 2, Post by author title 3, Post by author title 4, Post by author title 5\] <div class="post-title">Post by author title 1</div> <div class="post-title">Post by author title 2</div> <div class="post-title">Post by author title 3</div> <div class="post-title">Post by author title 4</div> <div class="post-title">Post by author title 5</div>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |
| 

`author_slug`

 | String | 

Specifies which author to filter on.

 |
| 

`limit`

 | Integer | 

Specifies the number of posts to add to the sequence up to a limit of 200.

 |

blog\_recent\_posts[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-recent-posts)
-----------------------------------------------------------------------------------------------

The `**blog_recent_posts**` function returns a sequence of blog post objects for the specified blog, sorted by most recent first. This sequence of posts can be saved into a variable and iterated through with a for loop, creating a custom post listing of your most popular posts. 

The function takes two parameters. The first parameter specifies which blog to collect popular posts from. The value should be `"default"` or the blog ID of a particular blog (available in the URL of the Blog dashboard). The second parameter specifies how many posts are retrieved. 

The first line of the example below demonstrates how the function returns a sequence. The sequence is saved in a variable and looped through. [Any blog post variables](/docs/cms/hubl/variables#blog-variables) should use the name of the individual loop item rather than `content.`. In the example, `rec_post.name` is used. This technique can be used, not only on blog templates, but also regular pages. 

**Please note:** this function has a limit of 200 posts and 10 calls per page.

{{ blog\_recent\_posts("default", 5) }} {% set rec\_posts = blog\_recent\_posts("default", 5) %} {% for rec\_post in rec\_posts %} <div class="post-title">{{ rec\_post.name }}</div> {% endfor %}\[Recent post title 1, Recent post title 2, Recent post title 3, Recent post title 4, Recent post title 5\] <div class="post-title">Recent post title 1</div> <div class="post-title">Recent post title 2</div> <div class="post-title">Recent post title 3</div> <div class="post-title">Recent post title 4</div> <div class="post-title">Recent post title 5</div>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |
| 

`limit`

 | Integer | 

Specifies the number of posts to add to the sequence, maximum 200.

 |

blog\_recent\_tag\_posts[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-recent-tag-posts)
--------------------------------------------------------------------------------------------------------

The `**blog_recent_tag_posts**` function returns a sequence of blog post objects for a specified tag or tags, sorted by most recent first. This sequence of posts can be saved into a variable and iterated through with a for loop, creating a custom post listing of posts by a particular tag or tags.

In the example code below:

*   The first line shows how the function returns a sequence of posts by tag. 
*   The second line shows how to save the function in a sequence variable. The rest of the code then uses a for loop to cycle through the variable values. [Any blog post variables](/docs/cms/hubl/variables#blog-variables) should use the name of the individual loop item rather than `content.`. In the example, `tag_post.name` is used. You can use this technique on both blog and website pages. 

Learn more about [creating a related blog post listing](/docs/cms/guides/creating-a-related-post-listing).

**Please note:** this function has a limit of 100 posts and 10 calls per page.

{{ blog\_recent\_tag\_posts("default", "marketing-tips", 5) }} {% set tag\_posts = blog\_recent\_tag\_posts("default", \["marketing", "fun", "inbound"\], 3, "AND") %} {% for tag\_post in tag\_posts %} <div class="post-title">{{ tag\_post.name }}</div> {% endfor %}\[Post about Marketing 1, Post about Marketing 2, Post about Marketing 3, Post about Marketing 4, Post about Marketing 5\] <div class="post-title">Post about Marketing</div> <div class="post-title">Post about Fun</div> <div class="post-title">Post about Inbound</div>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |
| 

`tag_slug`

 | String | 

Specifies which tag to filter on. You can include up to 10 tags, comma separated. Tags with multiple words must be lowercase with spaces replaced by hyphens.

 |
| 

`limit`

 | Integer | 

Specifies the number of posts to add to the sequence. This parameter is required when including a `logical_operator`.

 |
| 

`logical_operator`

 | String | 

When `tag_slug` contains multiple tags, use this operator to filter results with `AND` or `OR` logic. By default, this function uses `OR` logic to return posts tagged with any of the specified tags.

When including this parameter, `limit` is required.

 |

blog\_tag\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-tag-url)
-------------------------------------------------------------------------------------

The `blog_tag_url` function returns a full URL to the specified blog tag's listing page.

This function accepts two parameters. The first parameter specifies which blog the tag's listing page exists in. The second parameter specifies which tag to link. This parameter can use the **`topic.slug`** for a particular tag from `content.topic_list` or accepts a lowercase hyphenated name such as `"marketing-tips"`.

The example below shows how this function can be used as an anchor's href.

<a href="{{ blog\_tag\_url("default", "inbound-marketing") }}">Inbound Marketing</a><a href="http://blog.hubspot.com/marketing/tag/inbound-marketing">Inbound Marketing</a>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use, either a specific blog by its ID or the default blog by `"default"`.

 |
| 

`tag_slug`

 | String | 

Specifies which tag to link to.

 |

blog\_tags[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-tags)
------------------------------------------------------------------------------

The `**blog_tags**` function returns a sequence of the 250 most blogged-about tags (based on number of associated blog posts) for the specified blog, sorted by blog post count.This sequence can be stored in a variable and iterated through to create custom tag post filters. The number of posts for each tag can be accessed with `tag.live_posts`. 

This function accepts two parameters. The first parameter specifies which blog to fetch tags from. The second parameter sets a limit on the number of tags fetched.

The first line of the example below demonstrates how the function returns a sequence of tag objects. The rest of the example demonstrates a use case of saving a sequence into a variable and then iterating though the tag objects, printing a set of tag links. The example assumes that the blog has 4 tags. 

**Please note:** this function has a limit of 250 tags.

{{ blog\_tags("default", 250) }} {% set my\_tags = blog\_tags("default", 250) %} <ul> {% for item in my\_tags %} <li><a href="{{ blog\_tag\_url(group.id, item.slug) }}">{{ item }}</a></li> {% endfor %} </ul>\[ Blogging, Inbound Marketing, SEO, Social Media\] <ul> <li><a href="http://blog.hubspot.com/marketing/tag/blogging"></a></li></li> <li><a href="http://blog.hubspot.com/marketing/tag/inbound-marketing">Inbound Marketing</a></li></li> <li><a href="http://blog.hubspot.com/marketing/tag/seo">SEO</a></li> <li><a href="http://blog.hubspot.com/marketing/tag/social-media">Social Media</a></li></li> </ul>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to use. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |
| 

`limit`

 | Integer | 

The maximum amount of tags to return.

 |

blog\_total\_post\_count[](https://developers.hubspot.com/docs/cms/hubl/functions#blog-total-post-count)
--------------------------------------------------------------------------------------------------------

This function returns the total number of published posts in the specified blog. If no parameter is specified, it will count your default blog posts. Alternatively, you can specify `"default"` or a blog ID of a different blog to count. The blog ID is available in the URL of your blog dashboard for a particular blog.

**Please note:** this function has a limit of 10 calls per page.

{{ blog\_total\_post\_count }} {{ blog\_total\_post\_count(359485112) }}16 54

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`selected_blog`

 | Blog ID or "default" | 

Specifies which blog to count. The blog ID is returned by the [module blog field](/docs/cms/building-blocks/module-theme-fields#blog).

 |

clear[](https://developers.hubspot.com/docs/cms/hubl/functions#clear)
---------------------------------------------------------------------

Removes all items from a list. Unlike `pop()`, it does not return anything.

{% set words = \["phone","home"\] %} {% do words.clear() %} {{words}}\[\]

color\_contrast[](https://developers.hubspot.com/docs/cms/hubl/functions#color-contrast)
----------------------------------------------------------------------------------------

This function validates color contrast based on [WCAG standards](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum). You'll need to include two colors as arguments, and you can include an optional argument to specify the rating (`AA` or `AAA`). Returns `true` or `false` based on whether the colors meet/exceed the standard.

{{color\_contrast('#FFFFFF','#273749')}} {{color\_contrast('rgb(255, 255, 255)','rgb(229, 237, 245)','AAA')}} <p {% if color\_contrast('rgb(12,31,1)', '#F0F', 'AA') %}style="color: #FF0000;"{% else %}style="color: #00FF00"{% endif %}>Hey there</p>true false Hey there

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`color_1`

Required



 | Color | The first color to compare. Accepts:

*   6-digit hex codes (`#FFFFFF`)
*   3-digit hex codes (`#F0A`)
*   RGB color codes (`rgb(12,31,1)`)

Can also use a variable that stores a hex or RGB color code. For example:

`theme.primary_color.color`

 |
| 

`color_2`

Required



 | Color | 

The second color to compare against the first.

 |
| 

`rating`

 | String | The WCAG standard to use for rating. Can be either `AA` (default) or `AAA`. |

color\_variant[](https://developers.hubspot.com/docs/cms/hubl/functions#color-variant)
--------------------------------------------------------------------------------------

This function lightens or darkens a hex value or color variable by a set amount. The first parameter is the hex color (for example ("#FFDDFF") or a variable storing a hex value. The second parameter is the amount to adjust it by, from 0 to 255. This function can be used in CSS files to create a color variation. Another good use case is to use it with a color parameter of a color module, to allow users to specify a primary color that automatically generates a color variation.

In the example below, the hex color #3A539B is stored in a variable called `base_color`. The color is modified by -80 resulting in a darker blue (#00034B).

{% set base\_color ="#3A539B" %} {{ color\_variant(base\_color, -80) }}#00034b

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`base_color`

 | HEX color string | The starting color to be altered. For example, `#F7F7F7`. |
| 

`brightness_offset`

 | Integer | 

A positive or negative number used to lighten or darken the base color.

 |

content\_by\_id[](https://developers.hubspot.com/docs/cms/hubl/functions#content-by-id)
---------------------------------------------------------------------------------------

The **`content_by_id`** function returns a landing page, website page or blog post by ID. The only parameter accepted by this function is a numeric content ID. 

The below example code shows this function in use to generate a hyperlinked list item.

**Please note:** this function has a limit of 10 calls per page.

{% set my\_content = content\_by\_id(4715624297) %} <ul> <li> <a href="{{ my\_content.absolute\_url }}">{{my\_content.title}}</a> </li> </ul><ul> <li> <a href="http://www.hubspot.com/blog/articles/kcs\_article/email/how-do-i-create-default-values-for-my-email-personalization-tokens">How do I create default values for my email or smart content personalization tokens?</a> </li> </ul>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`id`

 | ID | 

The ID of the content to look up.

 |

content\_by\_ids[](https://developers.hubspot.com/docs/cms/hubl/functions#content-by-ids)
-----------------------------------------------------------------------------------------

Given a list of content IDs, returns a dict of landing page, website page or blog posts matching those IDs.

This function takes one parameter, a list of page or blog post IDs to look up, placed within an array. Up to 100 content objects can be passed. The below example code shows this function in use to generate a list of hyperlinked list items. 

**Please note:** this function has a limit of 10 calls per page. 

{% set contents = content\_by\_ids(\[4715624297, 4712623297, 5215624284\]) %} <ul> {% for content in contents %} <li> <a href="{{ content.absolute\_url }}">{{content.title}}</a> </li> {% endfor %} </ul><ul> <li> <a href="http://www.hubspot.com/blog/articles/kcs\_article/email/how-do-i-create-default-values-for-my-email-personalization-tokens">How do I create default values for my email or smart content personalization tokens?</a> </li> <li> <a href="https://blog.hubspot.com/marketing/content-marketing-strategy-guide">Content Marketing Strategy: A Comprehensive Guide for Modern Marketers</a> </li> </ul>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`ids`

 | List | 

A list of page or blog post IDs to look up. Up to 100 content objects can be passed.

 |

copy[](https://developers.hubspot.com/docs/cms/hubl/functions#copy)
-------------------------------------------------------------------

Return a shallow copy of the list. Equivalent to `a[:]`.

A _shallow copy_ constructs a new compound object and then (to the extent possible) inserts _references_ into it to the objects found in the original.

{% set a = \["ham"\] %} {% set b = a.copy() %} a: {{a}} b: {{b}} After Append {% do a.append("swiss") %} a: {{a}} b: {{b}}a: \[ham\] b: \[ham\] After Append a: \[ham, swiss\] b: \[ham\]

count[](https://developers.hubspot.com/docs/cms/hubl/functions#count)
---------------------------------------------------------------------

Returns the number of times a variable exists in a list.

{% set attendees = \["Jack","Jon","Jerry","Jessica"\] %} {% set jon\_count = attendees.count("Jon") %} There are {{jon\_count}} Jon's in the list. <p>After append:</p> {% do attendees.append("Jon") %} {% set jon\_count\_after\_append = attendees.count("Jon") %} There are now {{jon\_count\_after\_append}} Jon's in the list.There are 1 Jon's in the list. <p>After append:</p> There are now 2 Jon's in the list.

crm\_associations[](https://developers.hubspot.com/docs/cms/hubl/functions#crm-associations)
--------------------------------------------------------------------------------------------

Gets a list of CRM records associated with another record by its record ID, association category, and association definition ID.

This function returns an object with the following attributes: `has_more`, `total`, `offset` and `results`.

*   `_has_more_` indicates there are more results available beyond this batch (total > offset).
*   `_total_` is the total number of results available.
*   `_offset_` is the offset to use for the next batch of results.
*   _`results`_ returns an array of the specified associated objects matching the function's parameters

**Please note:** for security purposes, of the [HubSpot standard object types](https://knowledge.hubspot.com/crm-setup/get-started-with-objects#standard-objects) only the `product`, and `marketing_event` objects can be retrieved on a publicly accessible page. Any other standard object type must be hosted on a page which is either [password protected](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages) or requires a [CMS Membership login](https://knowledge.hubspot.com/articles/kcs_article/cms-pages-editor/control-audience-access-to-pages).  Custom objects do not have this same restriction.

{% set associated\_contacts = crm\_associations(847943847, "HUBSPOT\_DEFINED", 2, "limit=3&years\_at\_company\_\_gt=2&orderBy=email", "firstname,email", false) %} {{ associated\_contacts }}{has\_more=true, offset=3, total=203, results=\[{firstname=Aimee, id=905, email=abanks@company.com}, {firstname=Amy, id=1056, email=abroma@company.com}, {firstname=Abigael, id=957, email=adonahu@company.com}\]}

**Please note:** this function can be called a maximum of 10 times per page. Each `crm_associations` call can return at most 100 objects. The default limit is 10 objects.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`id`

Required



 | ID | 

ID of the record to find associations from.

 |
| 

`association category`

Required



 | String | 

The category of the association definition. Possible values are `HUBSPOT_DEFINED`, `USER_DEFINED`, and `INTEGRATOR_DEFINED`. This parameter can be omitted for hubspot defined built-in association types.

 |
| 

`association type id`

Required



 | Integer | 

The ID of the association definition to use. For standard HubSpot supported objects see [ID of the association type to use](https://legacydocs.hubspot.com/docs/methods/crm-associations/crm-associations-overview).  
Otherwise, this association ID can found at the [CRM Objects Schema API](/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details).

 |
| 

`query`

 | String | 

The `id` of the record OR a query string, delimited by `&`. All expressions are ANDed together. Supported operators are:

*   `eq` (default)
*   `neq`
*   `lt`
*   `lte`
*   `gt`,
*   `gte`
*   `is_null`
*   `not_null`
*   `in`
*   `not_in`
*   `contains` (applicable for multi-valued properties or string properties, e.g., _"firstname\_\_contains=Tim"_)

Queries can include the following parameters:

*   `limit`: the maximum number of results returned in the response. For example, `limit=50`.
*   `offset`: for paging through the results if the number of returned results is higher than the limit parameter. For example, `offset=51`.
*   `orderBy`: order results by a specific property. For example, `orderBy=email`.

 |
| 

`properties`

 | String | 

Optional. A comma-separated list of properties to return. By default, a small set of common properties are returned. The ID property is always returned.

A full list of properties can be found using the [get all contact properties](https://legacydocs.hubspot.com/docs/methods/contacts/v2/get_contacts_properties) and [get all company properties](https://legacydocs.hubspot.com/docs/methods/companies/get_company_properties) endpoints.

 |
| 

`formatting`

 | Boolean | 

Optional. Format values such as dates and currency according to this portal's settings. Omit or pass `false` for raw strings.

 |

crm\_object[](https://developers.hubspot.com/docs/cms/hubl/functions#crm-object)
--------------------------------------------------------------------------------

Gets a single CRM record by query or by its ID. Records are returned as a dict of properties and values.

This function can also be [used with custom and integrator objects](/docs/cms/crm-objects-in-cms-hub).

**Please note:** for security purposes, of the [HubSpot standard object types](https://knowledge.hubspot.com/crm-setup/get-started-with-objects#standard-objects) only the `product`, and `marketing_event` objects can be retrieved on a publicly accessible page. Any other standard object type must be hosted on a page which is either [password protected](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages) or requires a [CMS Membership login](https://knowledge.hubspot.com/articles/kcs_article/cms-pages-editor/control-audience-access-to-pages).  Custom objects do not have this same restriction.

What is the difference between `in` and `contains`?

`in` returns if the property value matches with any of the given values. Whereas `contains` returns if the property values for multi-select has all of the given values.

<!-- by query --> {% set contact = crm\_object("contact", "email=contact@company.com", "firstname,lastname", false) %} <!-- by id --> {% set contact = crm\_object("contact", 123) %} {{ contact.firstname }} {{ contact.lastname }}Brian Halligan

**Please note:** this function can only be called a maximum of 10 times on a single page.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`object_type`

 | String | 

The object type name. Object type names are case sensitive.  
[The supported object types](https://developers.hubspot.com/docs/cms/features/custom-objects#supported-crm-object-types).   
  
To find the names of the account specific and integrator object types available in your account use the [CRM Objects Schema API](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) to get the type definitions and look for the name property. It contains the internal object type name that should be used in the function

For integrator and account specific object types with the same name as the built-in objects use the objects [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) (FQN).

 |
| 

`query`

 | String | 

Optional. The `id` of the record OR a query string, delimited by `&`. All expressions are ANDed together. Supported operators are:

*   `eq` (default)
*   `neq`
*   `lt`
*   `lte`
*   `gt`
*   `gte`
*   `is_null`
*   `not_null`
*   `in`
*   `not_in`
*   `contains` (applicable for multi-valued properties or string properties, e.g., _"firstname\_\_contains=Tim"_).

Queries can include the following parameters:

*   `limit`: the maximum number of results returned in the response. For example, `limit=50`.
*   `offset`: for paging through the results if the number of returned results is higher than the limit parameter. For example, `offset=51`.
*   `orderBy`: order results by a specific property. For example, `orderBy=email`.

 |
| 

`properties`

 | String | 

Optional. A comma-separated list of properties to return. By default, a small set of common properties are returned. The ID property is always returned.

A full list of properties can be found using the [get all contact properties](https://legacydocs.hubspot.com/docs/methods/contacts/v2/get_contacts_properties) and [get all company properties](https://legacydocs.hubspot.com/docs/methods/companies/get_company_properties) endpoints.

 |
| 

`formatting`

 | Boolean | 

Optional. Format values such as dates and currency according to this portal's settings. Pass `false` for raw strings.

 |

**Please note:** when building a query, the values of `range`, `distinct`, `ndistinct`, and `startswith` are reserved keywords. To query a property that uses one of those names, you'll need to use the following format: `range__eq=` (rather than `range=`).

crm\_objects[](https://developers.hubspot.com/docs/cms/hubl/functions#crm-objects)
----------------------------------------------------------------------------------

Gets a list of records for a specific object type from the HubSpot CRM.

This function returns an object with the following attributes: `has_more`, `total`, `offset` and `results`.

*   `has_more` indicates there are more results available beyond this batch (total > offset).
*   `total` is the total number of results available.
*   `offset` is the offset to use for the next batch of results.
*   `results` returns an array of the specified objects matching the function's parameters.

Results can be sorted using at least one order parameter in the query. For example, `crm_objects("contact", "firstname=Bob&order=lastname&order=createdate")` will order contacts with the first name `"Bob"` by last name and then by `createdate`. To reverse a sort, prepend `-` to the property name like `order=-createdate`. The CRM objects function can also be [used with custom and integrator objects](/docs/cms/crm-objects-in-cms-hub).

**Please note:** for security purposes, of the [HubSpot standard object types](https://knowledge.hubspot.com/crm-setup/get-started-with-objects#standard-objects) only the `product`, and `marketing_event` objects can be retrieved on a publicly accessible page. Any other standard object type must be hosted on a page which is either [password protected](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages) or requires a [CMS Membership login](https://knowledge.hubspot.com/articles/kcs_article/cms-pages-editor/control-audience-access-to-pages).  Custom objects do not have this same restriction.

{% set objects = crm\_objects("contact", "firstname\_\_not\_null=&limit=3", "firstname,lastname") %} {{ objects }}{has\_more=true, offset=3, total=331, results=\[{firstname=Brian, id=44151, lastname=Halligan}, {firstname=Dharmesh, id=44051, lastname=Shah}, {firstname=George, id=88551, lastname=Washington}\]}

**Please note:** this function can be called a maximum of 10 times per page. Each `crm_objects` call can return at most 100 objects. The default limit is 10 objects.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`object_type`

 | String | 

The type of object by name. Object type names are case sensitive. Singular and plural are accepted for standard object types (e.g., `contact`, `contacts`). Learn more about the [supported object types](https://developers.hubspot.com/docs/cms/features/custom-objects#supported-crm-object-types).   
  
To find the names of the account specific and integrator object types available in your account, use the [CRM objects schema API](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) to get the type definitions and the name property.

For integrator and account specific object types with the same name as the built-in objects, use the objects [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) (FQN).

 |
| 

`query`

 | String | 

Optional. The ID of the record or a query string, delimited by `&`. All expressions are ANDed together.

Supported operators are:

*   `eq` (default)
*   `neq`
*   `lt`
*   `lte`
*   `gt`
*   `gte`
*   `is_null`
*   `not_null`
*   `in`
*   `not_in`
*   `contains` (applicable for multi-valued properties or string properties, e.g., _"firstname\_\_contains=Tim"_).

Example: `"email=contact@company.com"`

 |
| 

`properties`

 | String | 

Optional. A comma-separated list of properties to return. By default, a small set of common properties are returned. The ID property is always returned. A full list of properties can be found using the [get all contact properties](https://legacydocs.hubspot.com/docs/methods/contacts/v2/get_contacts_properties) and [get all company properties](https://legacydocs.hubspot.com/docs/methods/companies/get_company_properties) endpoints.

The record ID is always included in the returned object properties even when not explicitly added in the property list.

 |
| 

`formatting`

 | Boolean | 

Optional. Format values such as dates and currency according to this portal's settings. Pass `false` for raw strings.

 |

**Please note:** when building a query, the values of `range`, `distinct`, `ndistinct`, and `startswith` are reserved keywords. To query a property that uses one of those names, you'll need to use the following format: `range__eq=` (rather than `range=`).

crm\_property\_definition[](https://developers.hubspot.com/docs/cms/hubl/functions#crm-property-definition)
-----------------------------------------------------------------------------------------------------------

Get the property definition for a given object type and property name.

Supported object types are HubSpot standard objects (e.g., contacts), portal specific objects, and integrator objects.

**Please note:** for security purposes, of the [HubSpot standard object types](https://knowledge.hubspot.com/crm-setup/get-started-with-objects#standard-objects) only the `product`, and `marketing_event` objects can be retrieved on a publicly accessible page. Any other standard object type must be hosted on a page which is either [password protected](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages) or requires a [CMS Membership login](https://knowledge.hubspot.com/articles/kcs_article/cms-pages-editor/control-audience-access-to-pages).  Custom objects do not have this same restriction.

{{ crm\_property\_definition("house\_listing", "agent\_name") }}

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`object_type`

 | String | 

The object type name. Object type names are case sensitive. [The supported object types](https://developers.hubspot.com/docs/cms/features/custom-objects#supported-crm-object-types).   
  
To find the names of the account specific and integrator object types available in your account use the [CRM Objects Schema API](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) to get the type definitions and look for the name property. It contains the internal object type name that should be used in the function

For integrator and account specific object types with the same name as the built-in objects use the objects [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) (FQN).

 |
| 

`property_name`

 | String | 

The case-insensitive property name to retrieve the definition for.

 |

crm\_property\_definitions[](https://developers.hubspot.com/docs/cms/hubl/functions#crm-property-definitions)
-------------------------------------------------------------------------------------------------------------

Get the property definitions for a given object type and set of  property names.

Supported object types are HubSpot standard objects (e.g. contacts), portal specific objects, and integrator objects.

**Please note:** for security purposes, of the [HubSpot standard object types](https://knowledge.hubspot.com/crm-setup/get-started-with-objects#standard-objects) only the `product`, and `marketing_event` objects can be retrieved on a publicly accessible page. Any other standard object type must be hosted on a page which is either [password protected](https://knowledge.hubspot.com/cos-pages-editor/how-can-i-password-protect-my-pages) or requires a [CMS Membership login](https://knowledge.hubspot.com/articles/kcs_article/cms-pages-editor/control-audience-access-to-pages).  Custom objects do not have this same restriction.

{{ crm\_property\_definitions("house\_listing", "agent\_name,address") }}

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`object_type`

 | String | 

The object type name. Object type names are case sensitive. [The supported object types](https://developers.hubspot.com/docs/cms/features/custom-objects#supported-crm-object-types).   
  
To find the names of the account specific and integrator object types available in your account use the [CRM Objects Schema API](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) to get the type definitions and look for the name property. It contains the internal object type name that should be used in the function

For integrator and account specific object types with the same name as the built-in objects use the objects [fully qualified name](https://developers.hubspot.com/docs/cms/features/custom-objects#getting-a-custom-object-type-s-details) (FQN).

 |
| 

`property_name`

 | String | 

Optional. The case-insensitive property names comma separated, to retrieve the definition for. If empty, the definitions for all the properties will be retrieved.

 |

cta[](https://developers.hubspot.com/docs/cms/hubl/functions#cta)
-----------------------------------------------------------------

Because CTA modules have so many parameters that contain variations of their code, you can use the CTA function to easily generate a particular CTA in a template, page, or email. This function is what the rich text editor uses when you add a CTA via the editor.

**Please note:** This function has a limit of 10 calls per page.

{{ cta("ccd39b7c-ae18-4c4e-98ee-547069bfbc5b") }} {{ cta("ccd39b7c-ae18-4c4e-98ee-547069bfbc5b", "justifycenter") }}<span class="hs-cta-wrapper" id="hs-cta-wrapper-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b"> <span class="hs-cta-node hs-cta-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b" id="hs-cta-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b" style="visibility: visible;"> <a id="cta\_button\_158015\_19a9097a-8dff-4181-b8f7-955a47f29826" class="cta\_button " href="//cta-service-cms2.hubspot.com/ctas/v2/public/cs/c/?cta\_guid=19a9097a-8dff-4181-b8f7-955a47f29826&placement\_guid=ccd39b7c-ae18-4c4e-98ee-547069bfbc5b&portal\_id=158015&redirect\_url=APefjpH34lXcq1H4FhyHhE3DNeHPNigbBluiv6t07-N80GLkyj2Dn9PizhW8bo4ecrS47RmyslLg7QQKWLG7n2oNkvrumL9dWUjMMEjVYvStZ-IMyulMBvdU8AddI6nFXL0G\_VPP\_VXmnFi66RKPPjPvx6kbyPO6k566noP4CTZMyADHkGsGBf4S95YdTNtTTFabShT62cVAiV\_oWlXbpfPWQc4G3IvkoDoAhmpQVW-ggUcKa4Ft\_5A&hsutk=683eeb5b499fdfdf469646f0014603b4&utm\_referrer=http%3A%2F%2Fwww.davidjosephhunt.com%2F%3Fhs\_preview%3DNVkCLfFf-2857453560&canon=http%3A%2F%2Fwww.davidjosephhunt.com%2F-temporary-slug-63bb220d-eda6-44d0-9738-af928e787237" style="" cta\_dest\_link="http://www.hubspot.com/free-trial" title="Start a HubSpot trial"> Start a HubSpot trial </a> </span> <script charset="utf-8" src="//js.hscta.net/cta/current.js"></script> <script type="text/javascript"> hbspt.cta.load(158015, 'ccd39b7c-ae18-4c4e-98ee-547069bfbc5b'); </script> </span> <span class="hs-cta-wrapper" id="hs-cta-wrapper-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b"> <span class="hs-cta-node hs-cta-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b" id="hs-cta-ccd39b7c-ae18-4c4e-98ee-547069bfbc5b" style="display: block; text-align: center; visibility: visible;"> <a id="cta\_button\_158015\_19a9097a-8dff-4181-b8f7-955a47f29826" class="cta\_button " href="//cta-service-cms2.hubspot.com/ctas/v2/public/cs/c/?cta\_guid=19a9097a-8dff-4181-b8f7-955a47f29826&placement\_guid=ccd39b7c-ae18-4c4e-98ee-547069bfbc5b&portal\_id=158015&redirect\_url=APefjpH34lXcq1H4FhyHhE3DNeHPNigbBluiv6t07-N80GLkyj2Dn9PizhW8bo4ecrS47RmyslLg7QQKWLG7n2oNkvrumL9dWUjMMEjVYvStZ-IMyulMBvdU8AddI6nFXL0G\_VPP\_VXmnFi66RKPPjPvx6kbyPO6k566noP4CTZMyADHkGsGBf4S95YdTNtTTFabShT62cVAiV\_oWlXbpfPWQc4G3IvkoDoAhmpQVW-ggUcKa4Ft\_5A&hsutk=683eeb5b499fdfdf469646f0014603b4&utm\_referrer=http%3A%2F%2Fwww.davidjosephhunt.com%2F%3Fhs\_preview%3DNVkCLfFf-2857453560&canon=http%3A%2F%2Fwww.davidjosephhunt.com%2F-temporary-slug-63bb220d-eda6-44d0-9738-af928e787237" style="" cta\_dest\_link="http://www.hubspot.com/free-trial" title="Start a HubSpot trial"> Start a HubSpot trial </a> </span> <script charset="utf-8" src="//js.hscta.net/cta/current.js"></script> <script type="text/javascript"> hbspt.cta.load(158015, 'ccd39b7c-ae18-4c4e-98ee-547069bfbc5b'); </script> </span>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`guid`

 | String | 

The ID of the CTA to render. Can be found in the URL of the details screen of the CTA.

 |
| 

`align_opt`

 | Enumeration | 

Adjusts alignment of CTA. Values include `justifyleft`, `justifycenter`, `justifyright`, `justifyfull`.

 |

extend[](https://developers.hubspot.com/docs/cms/hubl/functions#extend)
-----------------------------------------------------------------------

Extend a list by appending all items from an iterable. In other words, insert all list items from one list into another list.

{% set vehicles = \["boat","car","bicycle"\] %} {% set more\_vehicles = \["airplane","motorcycle"\] %} {% do vehicles.extend(more\_vehicles) %} {{vehicles}}\[boat, car, bicycle, airplane, motorcycle\]

file\_by\_id[](https://developers.hubspot.com/docs/cms/hubl/functions#file-by-id)
---------------------------------------------------------------------------------

This function returns the metadata of a file by ID. It accepts a single parameter, the numeric ID of the file to look up.

**Please note:** this function is limited to 10 calls per page.

{% set file = file\_by\_id(123) %} {{ file.friendlyUrl }}https://www.hubspot.com/hubfs/HubSpot\_Logos/HSLogo\_color.svg

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`file_id`

 | ID | 

The ID of the file to look up.

 |

flag\_content\_for\_access\_check[](https://developers.hubspot.com/docs/cms/hubl/functions#flag-content-for-access-check)
-------------------------------------------------------------------------------------------------------------------------

When a blog post is [configured for self-registration access](https://knowledge.hubspot.com/blog/use-self-registration-for-private-blog-content), visitors will need to register or log in to view the full post content. HubSpot's default blog listing assets automatically include this functionality, and will also include a lock icon indicator for posts that require self-registration to access. Learn more about [building custom solutions using this function and its corresponding API](/docs/cms/data/memberships#private-blog-posts-with-self-registration).

This function checks whether a blog post can be accessed by the current visitor. When called, the function is replaced with the following attribute:

`hs-member-content-access=<true/false>`

A value of `true` indicates that the blog post requires the visitor to log in to view the full content.

{% for content in contents %} <article {{ flag\_content\_for\_access\_check(content.id) }} > ... </article> {% endfor %} <article hs-member-content-access="true" > ... </article>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`ID`

 | ID | The ID of the content that will be checked against the current logged in viewer. |

follow\_me\_links[](https://developers.hubspot.com/docs/cms/hubl/functions#follow-me-links)
-------------------------------------------------------------------------------------------

Returns the [social media account links set in account settings](https://knowledge.hubspot.com/design-manager/add-social-links-to-hubspot-templates#add-social-accounts-to-the-follow-me-module). Used in the [default follow\_me module](/docs/cms/building-blocks/modules/default-modules#follow-me). 

{% set fm = follow\_me\_links() %} {{ fm }}\[FollowMeLink{type=URL, id=5142734, altName=RSS, followMeUrl=http://website.com/rss.xml, iconName=rss, name=http://website.com/rss.xml}\]

format\_address[](https://developers.hubspot.com/docs/cms/hubl/functions#format-address)
----------------------------------------------------------------------------------------

Formats an address based on the context's locale. 

{{ format\_address('en-us', { address: "25 First Street", address2: "2nd Floor", city: "Cambridge", state: "MA", country: "United States", zip: "02141"}) }}\[25 First Street, 2nd Floor, Cambridge, MA 02141, United States\]

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`locale`

Required



 | String | 

The locale to format the address in.

 |  |
| 

`address`

Required



 | String | 

The street address.

 |  |
| 

`address2`

Optional



 | String | 

The second line of the address, such as floor or apartment number.

 |  |
| 

`city`

Required



 | String | 

The city of the address.

 |  |
| 

`state`

Required



 | String | 

The state of the address.

 |  |
| 

`country`

Required



 | String | 

The country of the address.

 |  |
| 

`zip`

Required



 | String | 

The zip code of the address.

 |  |

format\_company\_name[](https://developers.hubspot.com/docs/cms/hubl/functions#format-company-name)
---------------------------------------------------------------------------------------------------

Formats a company's name by adding Japanese honorifics where appropriate.

{{ format\_company\_name("companyName", addJapaneseHonorifics) }}HubSpot

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`companyName`

Required



 | String | 

The name of the company.

 |  |
| 

`useHonorificIfApplicable`

Required



 | Boolean | 

When set to `true` and the context's language is Japanese, a Japanese company honorific will be added where appropriate. 

 |  |

format\_name[](https://developers.hubspot.com/docs/cms/hubl/functions#format-name)
----------------------------------------------------------------------------------

Formats a person's name by putting the surname before the first name and adds Japanese honorifics where appropriate

{{ format\_name("firstName", "surname", addJapaneseHonorifics) }}Hobbes Baron

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`firstName`

Required



 | String | 

The person's first name.

 |  |
| 

`surname`

Required



 | String | 

The person's surname or last name.

 | `False` |
| 

`useHonorificIfApplicable`

Required



 | Boolean | 

When set to `true` and the context's language is Japanese, a Japanese honorific will be added where appropriate. 

 |  |

format\_datetime[](https://developers.hubspot.com/docs/cms/hubl/functions#format-datetime)
------------------------------------------------------------------------------------------

Formats both the date and time components of a date object, similar to the [format\_datetime](/docs/cms/hubl/filters#format-datetime) HubL filter. This function replaces the deprecated `datetimeformat` function.

{{ format\_datetime(content.publish\_date, "short", "America/New\_York", "en") }} 12/31/69 7:00 PM

Use this table to describe parameters / fields
| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| 
`format`

Required



 | String | 

The format to use. Can be one of:

*   `short`
*   `medium`
*   `long`
*   `full`
*   a custom pattern following [Unicode LDML](https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)

 |  |
| 

`timeZone`

Optional



 | String | 

The time zone of the output date in [IANA TZDB format](https://data.iana.org/time-zones/tzdb/).

 |  |
| 

`locale`

Optional



 | String | 

The locale to use for locale-aware formats.

 |  |

geo\_distance[](https://developers.hubspot.com/docs/cms/hubl/functions#geo-distance)
------------------------------------------------------------------------------------

This function contains 4 parameters and calculates the ellipsoidal 2D distance between two points on Earth. Use this function as a filter query for getting HubDB data.

{% for row in hubdb\_table\_rows(1234567, "geo\_distance(loc,1.233,-5.678,mi)\_\_gt=500") %} {{row.name}} <br> {% endfor %}Cambridge, MA<br> Salem, MA<br> San Diego, CA<br> Chicago, IL<br>

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`point1`

 | Location | 

location from a HubDB column.

 |
| 

`point2_lat`

 | Latitude | 

Latitude of point2.

 |
| 

`point2_long`

 | Longitude | 

Longitude of point2.

 |
| 

`units`

 | String | 

Units for the return value. Options are `FT` for feet, `MI` for miles, `M` for meters or `KM` for kilometers.

 |

get\_asset\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#get-asset-url)
---------------------------------------------------------------------------------------

This function returns the public URL of a specified template or code file. The parameter of this function is the asset's path in the design manager. Coded file URLs update each time you publish them; therefore, by using this function your ensure you are always using the latest version of the file. 

You can automatically generate this function in the app, by either right-clicking a **file** and selecting **Copy public URL**, or by clicking **Actions**, then selecting **Copy public URL**. 

The example below gets the URL of a Javascript file authored in Design Manager that can be included as the `src` of a `<script>` tag.

![copy-public-url](https://developers.hubspot.com/hubfs/Designers_Docs_2015/copy-public-url-4.gif "copy-public-url")

{{ get\_asset\_url("/custom/styles/style.css") }} //cdn2.hubspot.net/hub/1234567/hub\_generated/template\_assets/1565970767575/custom/styles/style.min.css

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`path`

 | String | 

The design manager file path to the template or file.

 |

get\_public\_template\_url\_by\_id[](https://developers.hubspot.com/docs/cms/hubl/functions#get-public-template-url-by-id)
--------------------------------------------------------------------------------------------------------------------------

This function works just like `get_public_template_url`, returning public URL of a specified template or code file. The only difference is the parameter of this function is the template ID (available in the URL of the template or coded file), instead of the design manager path.

{{ get\_public\_template\_url\_by\_id("2778457004") }} //cdn2.hubspot.net/hub/327485/hub\_generated/style\_manager/1431479563436/custom/page/Designers\_2015/designer-doc-2105.min.js

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`template_id`

 | ID | 

The ID number of the template of file.

 |

hubdb\_table[](https://developers.hubspot.com/docs/cms/hubl/functions#hubdb-table)
----------------------------------------------------------------------------------

[HubDB](/docs/cms/data/hubdb) is a feature available in CMS Hub Professional and Enterprise.

The `hubdb_table` function can be used to get information on a table including its name, columns, last updated, etc. 

The following pieces of information can be pulled by calling the appropriate attributes:

*   **ID:** the ID of the table.
*   **name:** the name of the table.
*   **columns:** a list of column information.
*   **created\_at:** the timestamp of when this table was first created.
*   **published\_at:**  the timestamp of when this table was published.
*   **updated\_at:** timestamp of when this table was last updated.
*   **row\_count:** the number of rows in the table.

{% set table\_info = hubdb\_table(1548215) %} {{ table\_info.row\_count }}25

**Please note:** this function has a limit of 10 calls per page.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`table_id`

 | String | 

ID or name of the table.

 |

hubdb\_table\_column[](https://developers.hubspot.com/docs/cms/hubl/functions#hubdb-table-column)
-------------------------------------------------------------------------------------------------

[HubDB](/docs/cms/data/hubdb) is a feature available in CMS Hub Professional and Enterprise.

The `hubdb_table_column` function can be used to get information on a column in table such as its label, type and options. This function accepts two parameters. 

These pieces of information about the column can be pulled by calling the appropriate attributes:

*   **ID:** the ID of the column.
*   **name:** the name of the column.
*   **label:** the label to be used for the column.
*   **type:** the type of the column.
*   **options:** for columns of type `select`, a map of `optionId` to option information.
*   **foreignIds:** for columns of type `"foreignId"`, a list of `foreignIds` (with `id` and `name` properties).

In addition to the above attributes, there is also a method which can be called: **`getOptionByName("<option name>")`** whereby for columns of type `"select"`, this will get option information by the option's name.

Column names are not case sensitive. For example, `HS_ID` and `hs_id` are both valid.

{% set column\_info = hubdb\_table\_column(123456, 6) %} {{ column\_info.label }}role

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`table_id`

 | String | 

ID or name of the table.

 |
| 

`column`

 | String | 

ID or name of the column.

 |

hubdb\_table\_row[](https://developers.hubspot.com/docs/cms/hubl/functions#hubdb-table-row)
-------------------------------------------------------------------------------------------

[HubDB](/docs/cms/data/hubdb) is a feature available in CMS Hub Professional and Enterprise.  
  
The `hubdb_table_row` function can be used to pull a single row from a HubDB table. From this row, you can pull information from each table cell by calling on the corresponding attribute: 

*   **hs\_id:** the globally unique id for this row.
*   **hs\_created\_at:** a timestamp representing when this row was created.
*   **hs\_path:** when used with dynamic pages, this string is the last segment of the url's path for the page.
*   **hs\_name:** when used with dynamic pages, this is the title of the page.
*   **<column name>** or **\["<column name>"\]:** get the value of the column for this row by the `name` of the column.

Column names are not case sensitive. For example, `HS_ID` and `hs_id` are both valid.

{% set row = hubdb\_table\_row(1548264, 6726439331) %} {{ row.role }}CTO

**Please note:** this function has a limit of 10 calls per page.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`table_id`

 | String | 

ID or name of the table.

 |
| 

`row_id`

 | Integer | 

ID of the row of the table.

 |

hubdb\_table\_rows[](https://developers.hubspot.com/docs/cms/hubl/functions#hubdb-table-rows)
---------------------------------------------------------------------------------------------

[HubDB](/docs/cms/data/hubdb) is a feature available in CMS Hub Professional and Enterprise.

The `hubdb_table_rows` function can be used to list rows of a HubDB table, to be iterated through. A single call of `hubdb_table_rows()` is limited to 10 table scans per page.

By default, this function will return a maximum of 1,000 rows. To retrieve more rows, specify a `limit` in the query, as shown in the code below.

**Please note:** if you use a [random filter](/docs/cms/hubl/filters#random) on this function, the page will be [prerendered](https://developers.hubspot.com/docs/cms/developer-reference/cdn/prerendering) periodically. This means that the filtered content will not be updated on every page reload.

{% for row in hubdb\_table\_rows(1546258, "years\_at\_company\_\_gt=3&orderBy=count&limit=1500") %} the value for row {{ row.hs\_id }} is {{ row.name }} {% endfor %}the value for row 6726439331 is Brian Halligan the value for row 8438997836 is Dharmesh Shah

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`table_id`

 | String | 

ID or name of the table to query.

 |
| 

`query`

 | String | 

A query in the same format as a URL query string. If not passed, returns all rows. Learn more about the [available filters](/docs/api/cms/hubdb#filter-returned-rows) for querying HubDB table rows.

You can reverse the sort by adding a `-` to the column name: `orderBy=-bar`. You can include this parameter multiple times to sort by multiple columns.

In addition to ordering by a column, you can also include the following functions:

*   `geo_distance(location_column_name, latitude, longitude)`:  
    takes the name of a location column and coordinates, returns the rows ordered by how far away the value of the specified location column are from the provided coordinates.
*   `length(column_name)`:  
    takes the name of a column, returns the rows ordered by the length of the column value (calculated as a string)
*   `random()`:  
    returns the rows in random order.

These functions also support reverse ordering. For example,   
`orderBy=-geo_distance(location_column,42.37,-71.07)`  
returns the items that are the farthest away first.

 |

**Please note:** when building a query, the values of `range`, `distinct`, `ndistinct`, and `startswith` are reserved keywords. To query a property that uses one of those names, you'll need to use the following format: `range__eq=` (rather than `range=`).

include\_default\_custom\_css[](https://developers.hubspot.com/docs/cms/hubl/functions#include-default-custom-css)
------------------------------------------------------------------------------------------------------------------

This function generates a link tag that references the [Primary CSS file](https://knowledge.hubspot.com/cos-general/create-edit-and-attach-css-files-to-style-your-site) (`default_custom_style.min.css`). This file is designed to be a global CSS file that can be added to all templates. To render, the function requires a boolean parameter value of `True`.

{{ include\_default\_custom\_css(True) }} <link href="//cdn2.hubspot.net/hub/327485/hub\_generated/style\_manager/1420345777097/custom/styles/default/hs\_default\_custom\_style.min.css" rel="stylesheet">

index[](https://developers.hubspot.com/docs/cms/hubl/functions#index)
---------------------------------------------------------------------

Returns the location of the first matching item in a 0-based `array`.

This function accepts 3 parameters, The first parameter is required. The first parameter is the item you are trying to find in the `array`. The second (`start`) and third (`end`) enable you to find that item in a slice of the `array`. 

{% set shapes = \["triangle","square","trapezoid","triangle"\] %} triangle index: {{shapes.index("triangle")}} <br> trapezoid index: {{shapes.index("trapezoid")}} <hr> adjusted start and end <br> triangle index: {{shapes.index("triangle",1,5)}}triangle index: 0<br> trapezoid index: 2 <hr> adjusted start and end<br> triangle index: 3

insert[](https://developers.hubspot.com/docs/cms/hubl/functions#insert)
-----------------------------------------------------------------------

Places an element into a list at the specific index provided.

This function accepts two parameters:

*   **Index:** the position where an element is to be inserted.
*   **Element:** the item to be inserted.

{% set even\_numbers = \[2,4,8,10\] %} {% do even\_numbers.insert(2,6) %} {{even\_numbers}}\[2, 4, 6, 8, 10\]

locale\_name[](https://developers.hubspot.com/docs/cms/hubl/functions#locale-name)
----------------------------------------------------------------------------------

Returns a human-readable string representation of a language code, optionally translated to a target language.

{{ locale\_name("es") }} {{ locale\_name("es", "en") }}Español Spanish

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`language_code`

 | String | 

The language code.

 |
| 

`target_language_code`

 | String | 

The language that the output will be translated to.

 |

load\_translations[](https://developers.hubspot.com/docs/cms/hubl/functions#load-translations)
----------------------------------------------------------------------------------------------

Loads translations from a given `_locales` folder path and returns a map of the values.

Learn more about [including field translations in custom modules and themes](/docs/cms/features/multi-language-content#include-field-translations-in-custom-modules-and-themes).

{% set template\_translations = load\_translations('../\_locales', 'fr', 'en') %} {{ partial\_footer\_address }}123 Rue du Pont, Ville, Région, 12300

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`path`

 | String | 

The file path to the \_locales directory of the translations.

 |
| 

`language_code`

 | String | 

The language code.

 |
| 

`language_code_fallback`

 | String | 

The language code fallback if the specified `language_code` isn't present.

 |

menu[](https://developers.hubspot.com/docs/cms/hubl/functions#menu)
-------------------------------------------------------------------

Returns the nested link structure of an advanced menu. Menu nodes have a variety of [properties](/docs/cms/hubl/variables#menu-node-variables) that can be used on objects that are returned. If you pass `null` to the menu function it will return an empty pylist. You can also specify a menu by name. In most cases it's safer to use the menu id, as a menu being renamed won't affect the id. If building for the marketplace it makes sense to default to `"default"` if menu is `null`.

**Please note:** this function has a limit of 10 calls per page. 

{% set node = menu(987) %} {% for child in node.children %} {{ child.label }}<br> {% endfor %} {% set default\_node = menu("default") %} {% for child in default\_node.children %} {{ child.label }}<br> {% endfor %}page1<br> page2<br> page3<br>

When using the `menu()` function to generate a menu, [you are fully responsible for making sure your menu is accessible.](/docs/cms/developer-reference/accessibility)

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`menu_id`

 | Id | 

Required. The id of the menu passed as a number.

 |
| 

`root_type`

 | Enumeration | 

Root type of the menu (`"site_root"`, `"top_parent"`, `"parent"`, `"page_name"`, `"page_id"`, `"breadcrumb"`).

*   `"site_root"` denotes static - Always show top-level pages in menu.
*   `"top_parent"` denotes dynamic by section - Show pages in menu that are related to section being viewed.
*   `"parent"` denotes dynamic by page - Show pages in menu that are related to page being viewed.
*   `"breadcrumb"` denotes breadcrumb style path menu (uses horizontal flow).

 |
| 

`root_key`

 | String | 

Root key (id or name) when using `"page_name"` or `"page_id"`.

 |

module\_asset\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#module-asset-url)
---------------------------------------------------------------------------------------------

Gets the URL for an asset attached to a custom module via **Linked Files > Other Files**.

{{ module\_asset\_url("smile.jpg") }} https://cdn2.hubspot.net/hubfs/6178146/logo-black-color.png

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`name`

 | String | 

The name of the asset.

 |

namespace[](https://developers.hubspot.com/docs/cms/hubl/functions#namespace)
-----------------------------------------------------------------------------

Creates a namespace object that can hold arbitrary attributes. It can be initialized from a dictionary or with keyword arguments.

{% set ns = namespace({"name": "item name", "price":"100"}, b=false) %} {{ns.name}}, {{ns.b}}item name, false

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`dictionary`

 | Map | 

The dictionary to initialize with.

 |
| 

`kwargs`

 | String | 

Keyword arguments to put into the namespace dictionary.

 |

oembed[](https://developers.hubspot.com/docs/cms/hubl/functions#oembed)
-----------------------------------------------------------------------

Returns OEmbed data dictionary for given request. Only works in emails.

{{ oembed({ url: "https://www.youtube.com/watch?v=KqpFNtbEOh8"}) }}OEmbedResponse{type=video, version=1.0, html=<iframe width="480" height="270" src="https://www.youtube.com/embed/KqpFNtbEOh8?feature=oembed" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>, title=Marketing Is a Marathon — Build a Complete Customer Experience, authorName=HubSpot, authorUrl=https://www.youtube.com/user/HubSpot, providerName=YouTube, providerUrl=https://www.youtube.com/, thumbnailUrl=https://i.ytimg.com/vi/KqpFNtbEOh8/hqdefault.jpg, thumbnailWidth=480, thumbnailHeight=360}

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`request`

 | String | 

Request object, `{url: string, max_width: long, max_height: long}`.

 |

personalization\_token[](https://developers.hubspot.com/docs/cms/hubl/functions#personalization-token)
------------------------------------------------------------------------------------------------------

Returns the value of a contact or contact related property, or a default.

Hi {{ personalization\_token("contact.firstname", "there") }}!<!-- If the contact is known --> Hi Dharmesh! <!-- If the contact is unknown --> Hi there!

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`expression`

 | String | 

An expression for the object and property to render.

 |
| 

`default`

 | String | 

Optional. A default value to use if the expression has no value.

 |

pop[](https://developers.hubspot.com/docs/cms/hubl/functions#pop)
-----------------------------------------------------------------

Removes the item at the index from the list. Also returns the removed item if printed.

{% set even\_numbers = \[2,3,4,6,8,9,10\] %} {% do even\_numbers.pop(1) %} {{even\_numbers.pop(4)}} {{even\_numbers}}9 \[2, 4, 6, 8, 10\]

postal\_location[](https://developers.hubspot.com/docs/cms/hubl/functions#postal-location)
------------------------------------------------------------------------------------------

The `**postal_location**` function returns the latitude/longitude location pair for a given postal code and country code (limited to US, CA, and GB).

{{ postal\_location("02139") }} {% set location = postal\_location("02139", "US") %} {{ location.latitude }} {{ location.longitude }}LatLon{latitude=42.3647, longitude=-71.1042} 42.3647 -71.1042

**Please note:** this function has a limit of 10 calls per page.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`postal_code`

 | String | 

Postal code of the location.

 |
| 

`country_code`

 | String | 

Country code for the postal code. If not provided, the country will try to be inferred from the postal code.

 |

put[](https://developers.hubspot.com/docs/cms/hubl/functions#put)
-----------------------------------------------------------------

Similar to the [update function](#update), which updates a dict with the elements from another dict object or from an iterable of key-value pairs, except that `put` supports variable names in dicts.

{% set dict\_var = {"authorName": "Tim Robinson"} %} {% set key = "key" %} {% set value = "value" %} {% do dict\_var.put(key, value) %} {{ dict\_var }}{authorName=Tim Robinson, key=value}

range[](https://developers.hubspot.com/docs/cms/hubl/functions#range)
---------------------------------------------------------------------

Returns a list containing an arithmetic progression of integers. With one parameter, range will return a list from 0 up to (but not including) the `value`. With two parameters, the range will start at the first value and increment by 1 up to (but not including) the second `value`. The third parameter specifies the step increment. All values can be negative. Impossible ranges will return an empty list. Ranges can generate a maximum of 1000 values.

Range can be used within a [for loop](/docs/cms/hubl/for-loops) to specify the number of iterations that should run.

{{ range(11) }} {{ range(5, 11) }} {{ range(0, 11, 2) }} {% for number in range(11) %} {{ number }} {% endfor %}\[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\] \[5, 6, 7, 8, 9, 10\] \[0, 2, 4, 6, 8, 10\] 0 1 2 3 4 5 6 7 8 9 10

require\_css[](https://developers.hubspot.com/docs/cms/hubl/functions#require-css)
----------------------------------------------------------------------------------

This function enqueues a CSS file to be rendered in the head element. All CSS link tags are grouped together and render before any JavaScript tags. The HubL is replaced with an empty line and then a link tag is added to `{{ standard_header_includes }}`. This method requires an absolute URL; CMS content with a known relative URL can be required by using the `get_asset_url()` function.

To enqueue an inline style to be rendered in the `head` via a style tag element, use the `{% require_css %} and {% end_require_css %}` tag instead with your style tags and CSS inside of that.

The second parameter is a dictionary of options to modify generated tag. Supports `async` (true/false) [a technique described on web.dev](https://web.dev/defer-non-critical-css/#optimize) and any other key-value pair will be added as HTML attributes to the style tag.

{{ standard\_header\_includes }} <!-- more html --> {{ require\_css("http://example.com/path/to/file.css") }} {{ require\_css(get\_asset\_url("/relative/path/to/file.css")) }} <!-- you can tell the browser to load the file asynchronously --> {{ require\_css(get\_asset\_url("./style.css"), { async: true }) }}<!-- other standard header html --> <link type="text/css" rel="stylesheet" href="http://example.com/path/to/file.css"> <link type="text/css" rel="stylesheet" href="http://example.com/relative/path/to/file.css"> <!-- you can tell the browser to load the file asynchronously --> <link rel="preload" href="//cdn2.hubspot.net/hub/6333443/hub\_generated/template\_assets/39079350918/1608661506628/example.css" as="style" onload="this.onload=null;this.rel='stylesheet'"> <noscript><link rel="stylesheet" href="//cdn2.hubspot.net/hub/6333443/hub\_generated/template\_assets/39079350918/1608661506628/example.css"></noscript> <!-- more html -->

require\_js[](https://developers.hubspot.com/docs/cms/hubl/functions#require-js)
--------------------------------------------------------------------------------

Specifies whether a script should be enqueued to render in the head or footer (default). Specify the render location by including the `head` or `footer` parameter. The HubL will be replaced by an empty line, and included in either _the [header or footer includes](/docs/cms/building-blocks/templates/html-hubl-templates#header-and-footer-includes)._ 

To enqueue an inline script to be rendered in the footer via a script element, wrap your `<script>` tags with `{% require_js %}` and `{% end_require_js %}`. 

You can also include additional render options in this function. These will be added as HTML attributes in the script tag. Render options include:

*   **position:** `head`/`footer`
*   **defer:** `true`/`false`
*   **async:** `true`/`false`
*   **type:** `string`

{{ standard\_header\_includes }} <!-- more html --> {{ require\_js("http://example.com/path/to/footer-file.js", "footer") }} {{ require\_js("http://example.com/path/to/head-file.js", "head") }} <!-- you can add async or defer attributes to the tags that are added. --> {{ require\_js(get\_asset\_url("./path/to/file.js"), { position: "footer", async: true }) }} {{ require\_js(get\_asset\_url("./jquery-latest.js"), { position: "footer", defer:true }) }} {{ standard\_footer\_includes }}<!-- other standard header html --> <script async defer src="//cdn2.hubspot.net/hub/6333443/hub\_generated/template\_assets/37785718838/1605816776975/jquery-latest.min.js"></script> <script src="http://example.com/path/to/head-file.js"></script> <!-- more html --> <script src="http://example.com/path/to/footer-file.js"></script> <!-- you can add async or defer attributes to the tags that are added. --> <script async src="//cdn2.hubspot.net/hub/######/hub\_generated/template\_assets/#############/######/jquery-latest.min.js"></script> <script defer src="//cdn2.hubspot.net/hub/######/hub\_generated/template\_assets/#############/######/jquery-latest.min.js"></script> <!-- other standard footer html -->

resize\_image\_url[](https://developers.hubspot.com/docs/cms/hubl/functions#resize-image-url)
---------------------------------------------------------------------------------------------

Rewrites the URL of image stored in File Manager to a URL that will resize the image on request. The function accepts one required parameter, and five optional parameters. At least one optional parameter must be passed.

Required

*   **URL:** string, URL of a HubSpot-hosted image.

Optional

*   **width:** number, the new image width in pixels.
*   **height:** number, the new image height in pixels.
*   **length:** number, the new length of the largest side, in pixels.
*   **upscale:** boolean, use the resized image dimensions even if they would scale up the original image (images may appear blurry).
*   **upsize:** boolean, return the resized image even if it is larger than the original in bytes.

**Please note:** images that are larger than 4096 pixels in height or width will not be automatically resized. Instead, you'll need to [manually resize the image](https://knowledge.hubspot.com/files/automatic-image-resizing-on-hubspot-content). 

{{ resize\_image\_url("http://your.hubspot.site/hubfs/img.jpg", 0, 0, 300) }}http://your.hubspot.site/hubfs/img.jpg?length=300&name=img.jpg

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`url`

 | String | 

URL of a HubSpot-hosted image.

 |
| 

`width`

 | Integer (px) | 

The new image width, in pixels.

 |
| 

`height`

 | Integer (px) | 

The new image height, in pixels.

 |
| 

`length`

 | Integer (px) | 

The new length of the largest side, in pixels.

 |
| 

`upscale`

 | Boolean | 

Use the resized image dimensions even if they would scale up the original image (images may appear blurry).

Default value is `false`.

 |
| 

`upsize`

 | Boolean | 

Return the resized image even if it is larger than the original in bytes.  
  
Default value is `false`.

 |

reverse[](https://developers.hubspot.com/docs/cms/hubl/functions#reverse)
-------------------------------------------------------------------------

Reverses the order of items in a list. Doesn't take any parameters. To reverse an object or return an iterator to iterate over the list in reverse, use [`|reverse`](/docs/cms/hubl/filters#reverse)

{% set numbers = \[1,2,3,4\] %} {% do numbers.reverse() %} {{numbers}}\[4, 3, 2, 1\]

set\_response\_code[](https://developers.hubspot.com/docs/cms/hubl/functions#set-response-code)
-----------------------------------------------------------------------------------------------

Set the response code as the specified code. [404](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404) is the only supported code for now. When using this, your page will return a `404` error.

{{ set\_response\_code(404) }} <!-- this will cause the page to result in a 404 error -->

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`code`

 | Integer | 

The HTTP response code. Currently, `404` is the only supported code.

 |

super[](https://developers.hubspot.com/docs/cms/hubl/functions#super)
---------------------------------------------------------------------

This function prints content from the parent template into a child template using the [extends](/docs/cms/hubl#blocks-and-extends) tag.

For example, in the code below, a basic HTML template has been created with a HubL block named `sidebar` and saved as `parent.html`. A second template file is created that will extend that parent file. Normally, the `<h3>` would be printed in the parent HTML's sidebar block. But by using `super`, content from the parent template sidebar block is combined with the content from the child template. 

{% extends "custom/page/web\_page\_basic/parent.html" %} {% block sidebar %} <h3>Table Of Contents</h3> {{ super() }} {% endblock %}<!doctype html> <html> <head> <meta charset="utf-8"> <title>This is the parent template </title> </head> <body> <h3>Table of contents</h3> Sidebar content from parent. </body> </html>

today[](https://developers.hubspot.com/docs/cms/hubl/functions#today)
---------------------------------------------------------------------

Returns the start of today (12:00am). Optionally you can add a parameter to change the timezone from the default UTC.

{{ today() }} {{ today("America/New\_York") }} {{ unixtimestamp(today("America/New\_York").plusDays(1)) }}2018-10-23T00:00Z 2018-10-23T00:00-04:00\[America/New\_York\] 1540353600000

to\_local\_time[](https://developers.hubspot.com/docs/cms/hubl/functions#to-local-time)
---------------------------------------------------------------------------------------

Converts a UNIX timestamp to the local time, based on your HubSpot Report Settings. You can then apply a datetimeformat filter to format the date.

{{ to\_local\_time(eastern\_dt) }} 2015-05-13 10:37:31

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`date`

 | Datetime | 

UNIX timestamp to convert to local time.

 |

topic\_cluster\_by\_content\_id[](https://developers.hubspot.com/docs/cms/hubl/functions#topic-cluster-by-content-id)
---------------------------------------------------------------------------------------------------------------------

Returns a HubL dict representing the topic cluster associated with a piece of content (determined by the passed content id), including metadata about the associated pillar page, core topic, and subtopics. Can be used to "auto-link" a piece of content with its associated pillar page \[if it exists\].

Available metadata can be found in: attachableContent (the current content's metadata), topic (the current content's associated topic metadata), coreTopic (the associated cluster's core topic metadata), and pillarPage (the associated pillar page's metadata).

Use `{{ topicCluster|pprint }}` to see a full a display of available properties/attributes.

{{ topic\_cluster\_by\_content\_id(content.id) }} {%- if content.id -%} {%- set topicCluster = topic\_cluster\_by\_content\_id(content.id) -%} {%- if topicCluster.pillarPage.url.value and topicCluster.pillarPage.publishState == "PUBLISHED" -%} <div>Topic: <a href="{{ topicCluster.pillarPage.url.value }}">{{ topicCluster.coreTopic.phrase }}</a></div> {%- endif -%} {%- endif -%}{ attachedContent, topic, coreTopic, pillarPage } (AttachedContentWithContext: {attachedContent=AttachedContent{id=1234, topicId=1234, clusterId=1234, portalId=0, attachable=Attachable{contentId=124, url=ValidatedUri{https://www.hubspot.com/}, attachableType=LANDING\_PAGE, title=title, publishState=PUBLISHED, deletedAt=null}, isLinkedToPillarPage=null, isPillarPage=null, createdAt=1547238986475, updatedAt=1547238986475, deletedAt=null}, coreTopic=Optional\[Topic{id=1234, portalId=0, clusterId=1234, phrase=TOPIC PHRASE, attachedContent=null, isCoreTopic=false, createdAt=1547157062081, updatedAt=1547232313421, deletedAt=null}\], pillarPage=Optional\[AttachedContent{id=1234, topicId=1234, clusterId=1234, portalId=0, attachable=Attachable{contentId=null, url=ValidatedUri{https://www.hubspot.com.com/}, attachableType=EXTERNAL\_URL, title=null, publishState=PUBLISHED, deletedAt=null}, isLinkedToPillarPage=null, isPillarPage=null, createdAt=1547157062086, updatedAt=1547157062086, deletedAt=null}\], topic=Optional\[Topic{id=1234, portalId=0, clusterId=8345, phrase=topic phrase, attachedContent=null, isCoreTopic=false, createdAt=1547238962703, updatedAt=1547238962703, deletedAt=null}\]}) <div> Topic: <a href="#-link-to-pillar-page-url"> core topic phrase </a> </div>

**Please note:** this function has a limit of 10 calls per page.

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`content_id`

 | Id | 

The id of the page to look up.

 |

truncate[](https://developers.hubspot.com/docs/cms/hubl/functions#truncate)
---------------------------------------------------------------------------

The truncate function works just like the [truncate filter](/docs/cms/hubl/filters#truncate), but uses function syntax instead of filter syntax. The first parameter specifies the string. The second parameter specifies the length at which to truncate. The final parameter specifies the characters to add when the truncation occurs.

{{ truncate("string to truncate at a certain length", 19, false, "...") }} {% set longString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus sodales ultricies velit sit amet ornare." %} {{ truncate(longString, 40, false, "...") }} string to truncate ... Lorem ipsum dolor sit amet, consectetur ...

Use this table to describe parameters / fields
| Parameter | Type | Description |
| --- | --- | --- |
| 
`string_to_truncate`

 | String | 

String that will be truncated.

 |
| 

`length`

 | integer | 

Specifies the length at which to truncate the text (includes HTML characters).

 |
| 

`killwords`

 | boolean | 

If true, the string will cut text at length, regardless of if it's in the middle of a word.

 |
| 

`end`

 | String | 

The characters that will be added to indicate where the text was truncated.

 |

type[](https://developers.hubspot.com/docs/cms/hubl/functions#type)
-------------------------------------------------------------------

This function accepts one argument and returns the type of an object. The return value is one of: `"bool"`, `"datetime"`, `"dict"`, `"float"`, `"int"`, `"list"`, `"long"`, `"null"`, `"str"` or `"tuple"`.

{{ type("Blog") }} {% set my\_type = type("Blog") %} <p>{{my\_type}}</p><p>str</p>

unixtimestamp[](https://developers.hubspot.com/docs/cms/hubl/functions#unixtimestamp)
-------------------------------------------------------------------------------------

This function returns a unix timestamp. By default it will return the timestamp of now or you can optionally supply a datetime object to be converted to a unix timestamp.

{{ unixtimestamp() }} {{ unixtimestamp(d) }} 1582822133978 1565983117868

update[](https://developers.hubspot.com/docs/cms/hubl/functions#update)
-----------------------------------------------------------------------

Updates the dict with the elements from another dict object or from an iterable of key-value pairs.

{% set dict\_var = {"authorName": "Douglas Judy", "authorTitle": "Mastermind" } %} {% do dict\_var.update({"authorFriend": "Jake"}) %} {% do dict\_var.update({"authorLocation": "unknown"}) %} {{ dict\_var }}{authorName=Douglas Judy, authorTitle=Mastermind, authorFriend=Jake, authorLocation=unknown}

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/functions#page-feedback)
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