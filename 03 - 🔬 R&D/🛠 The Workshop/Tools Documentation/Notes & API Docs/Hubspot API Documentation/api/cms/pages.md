* * *

Pages
=====

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use this API to create, manage, and publish website and landing pages. Learn more about [creating and customizing pages within HubSpot](https://knowledge.hubspot.com/website-pages/create-and-customize-pages). 

For example, fetch a currently drafted page, then publish it so that it's live on your website.

Changes in v3[](https://developers.hubspot.com/docs/api/cms/pages#changes-in-v3)
--------------------------------------------------------------------------------

The following properties are deprecated and no longer included within the response:

*   `campaign_name`
*   `is_draft`
*   `style_override_id`
*   `meta_keywords`

Retrieve pages[](https://developers.hubspot.com/docs/api/cms/pages#retrieve-pages)
----------------------------------------------------------------------------------

To retrieve an account's pages, make a `GET` request to `cms/v3/pages/{landing-pages|site-pages}`. You can filter and sort the returned pages by adding query parameters to the request URL, which are described below. For example, to retrieve all website pages that are currently published or scheduled to publish, you would make a `GET` request to the following URL:

`cms/v3/pages/site-pages?state__in=PUBLISHED_OR_SCHEDULED`

You'll receive a response containing information about the page, along with the page's content.

// Example response { "total": 1, "results": \[ { "archivedAt": "1970-01-01T00:00:00Z", "archivedInDashboard": false, "attachedStylesheets": \[\], "authorName": "Eric D.", "categoryId": 1, "contentTypeCategory": 4, "createdAt": "2024-02-06T19:02:33.991Z", "createdById": "2931299", "currentState": "PUBLISHED", "domain": "", "featuredImage": "", "featuredImageAltText": "", "htmlTitle": "My test page", "id": "155890290211", "layoutSections": { "dnd\_area": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "label": "Main section", "name": "dnd\_area", "params": {}, "rowMetaData": \[ { "cssClass": "dnd-section", "styles": { "backgroundColor": { "a": 1, "b": 250, "g": 248, "r": 245 }, "forceFullWidthSection": false } }, { "cssClass": "dnd-section", "styles": { "backgroundColor": { "a": 1, "b": 255, "g": 255, "r": 255 }, "forceFullWidthSection": false } } \], "rows": \[ { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-column-2", "params": { "css\_class": "dnd-column" }, "rowMetaData": \[ { "cssClass": "dnd-row" }, { "cssClass": "dnd-row" }, { "cssClass": "dnd-row" } \], "rows": \[ { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-3", "params": { "child\_css": {}, "css": {}, "css\_class": "dnd-module", "extra\_classes": "widget-type-rich\_text", "html": "<div style='text-align:center;'>\\n<h2><strong>About</strong></h2>\\n</div>", "path": "@hubspot/rich\_text", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 12, "x": 0 } }, { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-column-4", "params": { "css\_class": "dnd-column" }, "rowMetaData": \[ { "cssClass": "dnd-row", "styles": {} } \], "rows": \[ { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-5", "params": { "child\_css": {}, "css": {}, "css\_class": "dnd-module", "extra\_classes": "widget-type-linked\_image", "horizontal\_alignment": "CENTER", "img": { "alt": "Growth theme placeholder image", "loading": "lazy", "max\_height": 500, "max\_width": 500, "size\_type": "auto\_custom\_max", "src": "//7528309.fs1.hubspotusercontent-na1.net/hubfs/7528309/raw\_assets/public/mV0\_d-cms-growth-theme\_hubspot/growth/images/service-one.jpg" }, "path": "@hubspot/linked\_image", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "style": "margin-bottom: 22px;", "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "styles": { "flexboxPositioning": "TOP\_CENTER" }, "type": "custom\_widget", "w": 12, "x": 0 } } \], "type": "cell", "w": 6, "x": 0 }, "6": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-column-6", "params": { "css\_class": "dnd-column" }, "rowMetaData": \[ { "cssClass": "dnd-row" } \], "rows": \[ { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-7", "params": { "child\_css": {}, "css": {}, "css\_class": "dnd-module", "extra\_classes": "widget-type-rich\_text", "html": "<p>Add a short description about the work that you do at your company. Try to narrow in on your specialization so that you can capture the attention of your clients. Talk about the value that you can deliver through a paid consultation.</p>", "path": "@hubspot/rich\_text", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 12, "x": 0 } } \], "type": "cell", "w": 6, "x": 6 } }, { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-8", "params": { "button\_link": { "no\_follow": false, "open\_in\_new\_tab": false, "rel": "", "sponsored": false, "url": { "href": "#book" }, "user\_generated\_content": false }, "button\_text": "Book a consultation", "child\_css": {}, "css": {}, "css\_class": "dnd-module", "path": "../modules/button", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "styles": { "alignment": { "alignment": { "css": "", "horizontal\_align": "CENTER" } } }, "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 12, "x": 0 } } \], "styles": {}, "type": "cell", "w": 12, "x": 0 } }, { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-column-9", "params": { "css\_class": "dnd-column" }, "rowMetaData": \[ { "cssClass": "dnd-row", "styles": {} }, { "cssClass": "dnd-row" }, { "cssClass": "dnd-row" } \], "rows": \[ { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-10", "params": { "child\_css": {}, "css": {}, "css\_class": "dnd-module", "extra\_classes": "widget-type-rich\_text", "html": "<a id=\\"services\\" data-hs-anchor=\\"true\\"></a>\\n<div style=\\"text-align: center;\\">\\n<h2>A suite of tools at your disposal</h2>\\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>\\n</div>", "path": "@hubspot/rich\_text", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 12, "x": 0 } }, { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-11", "params": { "child\_css": {}, "content": { "content": "<h3 style='text-align:center;'>Service</h3><p>Summarize the service you provide. Add a message about the value that you can provide to your customers.</p>" }, "css": {}, "css\_class": "dnd-module", "icon": { "icon": { "icon\_set": "fontawesome-5.0.10", "name": "balance-scale", "type": "SOLID", "unicode": "f24e" } }, "path": "../modules/service-card", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "styles": { "card": { "spacing": { "spacing": { "css": "margin-bottom: 22px;\\n", "margin": { "bottom": { "units": "px", "value": 22 } } } } }, "icon": { "background": { "color": { "color": "#494a52", "css": "#494a52", "hex": "#494a52", "opacity": 100, "rgb": "rgb(73, 74, 82)", "rgba": "rgba(73, 74, 82, 1)" } } } }, "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 4, "x": 0 }, "4": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-12", "params": { "child\_css": {}, "content": { "content": "<h3 style='text-align:center;'>Service</h3><p>Summarize the service you provide. Add a message about the value that you can provide to your customers.</p>" }, "css": {}, "css\_class": "dnd-module", "icon": { "icon": { "icon\_set": "fontawesome-5.0.10", "name": "industry", "type": "SOLID", "unicode": "f275" } }, "path": "../modules/service-card", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "styles": { "card": { "spacing": { "spacing": { "css": "margin-bottom: 22px;\\n", "margin": { "bottom": { "units": "px", "value": 22 } } } } }, "icon": { "background": { "color": { "color": "#494a52", "css": "#494a52", "hex": "#494a52", "opacity": 100, "rgb": "rgb(73, 74, 82)", "rgba": "rgba(73, 74, 82, 1)" } } } }, "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 4, "x": 4 }, "8": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-13", "params": { "child\_css": {}, "content": { "content": "<h3 style='text-align:center;'>Service</h3><p>Summarize the service you provide. Add a message about the value that you can provide to your customers.</p>" }, "css": {}, "css\_class": "dnd-module", "icon": { "icon": { "icon\_set": "fontawesome-5.0.10", "name": "server", "type": "SOLID", "unicode": "f233" } }, "path": "../modules/service-card", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "styles": { "card": { "spacing": { "spacing": { "css": "margin-bottom: 22px;\\n", "margin": { "bottom": { "units": "px", "value": 22 } } } } }, "icon": { "background": { "color": { "color": "#494a52", "css": "#494a52", "hex": "#494a52", "opacity": 100, "rgb": "rgb(73, 74, 82)", "rgba": "rgba(73, 74, 82, 1)" } } } }, "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 4, "x": 8 } }, { "0": { "cells": \[\], "cssClass": "", "cssId": "", "cssStyle": "", "name": "dnd\_area-module-14", "params": { "button\_link": { "no\_follow": false, "open\_in\_new\_tab": false, "rel": "", "sponsored": false, "url": { "href": "#book" }, "user\_generated\_content": false }, "button\_text": "Book a consultation", "child\_css": {}, "css": {}, "css\_class": "dnd-module", "path": "../modules/button", "schema\_version": 2, "smart\_objects": \[\], "smart\_type": "NOT\_SMART", "styles": { "alignment": { "alignment": { "css": "", "horizontal\_align": "CENTER" } } }, "wrap\_field\_tag": "div" }, "rowMetaData": \[\], "rows": \[\], "type": "custom\_widget", "w": 12, "x": 0 } } \], "type": "cell", "w": 12, "x": 0 } } \], "type": "cell", "w": 12, "x": 0 } }, "name": "My test page", "pageRedirected": false, "publicAccessRules": \[\], "publicAccessRulesEnabled": false, "publishDate": "2024-03-28T18:48:55Z", "publishImmediately": true, "published": true, "slug": "my-test-page", "state": "PUBLISHED\_OR\_SCHEDULED", "subcategory": "site\_page", "templatePath": "@hubspot/growth/templates/paid-consultation.html", "translations": {}, "updatedAt": "2024-03-28T18:49:44.134Z", "updatedById": "2931299", "url": "https://www.website.com/my-test-page", "useFeaturedImage": false, "widgetContainers": {}, "widgets": {} } \] }

Filtering[](https://developers.hubspot.com/docs/api/cms/pages#filtering)
------------------------------------------------------------------------

When retrieving pages, you can add query parameters to the request URL to filter the results. Each filter will follow the same general syntax: `propertyName__operator=value`. You can include as many filters as you'd like, and all specified filters will be applied to narrow down the results.

For example, you can filter the results to only include pages where the name property contains the word `marketing` using this parameter: `name__icontains=marketing`.

The table below lists the page properties that can be used as filters, along with which operators each property can use.

Use this table to describe parameters / fields
| Property | Available operators |
| --- | --- |
| 
`id`

 | 

`eq`, `in`, `not_in`

 |
| 

`slug`

 | 

`eq`, `in`, `nin`, `icontains`

 |
| 

`campaign`

 | 

`eq`, `in`

 |
| 

`state`

 | 

`eq`, `ne`, `in`, `nin`, `contains`

See [available states](#state-values) for filtering options.

 |
| 

`publishDate`

 | 

`eq`, `gt`, `gte`, `lt`, `lte`

 |
| 

`createdAt`

 | 

`eq`, `gt`, `gte`, `lt`, `lte`

 |
| 

`updatedAt`

 | 

`eq`, `gt`, `gte`, `lt`, `lte`

 |
| 

`templatePath`

 | 

`eq`, `contains`, `startswith`

 |
| 

`name`

 | 

`eq`, `in`, `icontains`

 |
| 

`mabExperimentId`

 | 

`eq`, `in`

 |
| 

`abTestId`

 | 

`eq`, `in`

 |
| 

`archivedAt`

 | 

`eq`, `gt`, `gte`, `lt`, `lte`

 |
| 

`createdById`

 | 

`eq`

 |
| 

`updatedById`

 | 

`eq`

 |
| 

`domain`

 | 

`eq`, `not_like`, `contains`

This will display as blank for content published on a domain that is primary for that content type.

 |
| 

`subcategory`

 | 

`eq`, `ne`, `in`, `nin`

 |
| 

`folderId`

 | 

`eq`, `in`, `null`, `not_null`

 |
| 

`language`

 | 

`in`, `not_null`

 |
| 

`translatedFromId`

 | 

`null`, `not_null`

 |
| 

`dynamicPageHubDbTableId`

 | 

`eq`, `not_null`

 |

Below are the definitions for each operator, along with any available synonyms.

Use this table to describe parameters / fields
| Operator | Description |
| --- | --- |
| 
`eq`

 | 

Filters for results that are equal to the specified value.

Synonyms: `exact`, `is`

 |
| 

`ne`

 | 

Filters for results that are not equal to the specified value.

Synonyms: `neq`, `not`

 |
| 

`contains`

 | 

Filters for results that contain the specified, case-sensitive value. Not accepted for the `name` property.

Synonym: `like`.

 |
| 

`icontains`

 | 

Filters for results by the specified value, not case sensitive. 

Synonym: `ilike`.

 |
| 

`not_like`

 | 

Filters for results that don't contain a specified value.

Synonym: `nlike`

 |
| 

`lt`

 | 

Filters for results that are less than a specified number value, such as a unix timestamp in milliseconds.

 |
| 

`lte`

 | 

Filters for results that are less than or equal to a specified value.

 |
| 

`gt`

 | 

Filters for results that are greater than a specified value.

 |
| 

`gte`

 | 

Filters for results that are greater than or equal to a specified value.

 |
| 

`is_null`

 | 

Filters for results that do not have a value for the specified property.

 |
| 

`not_null`

 | 

Filters for results that have any value for the specified property.

 |
| 

`startswith`

 | 

Filters for results that start with a specified value.

 |
| 

`in`

 | 

In

 |
| 

`nin`

 | 

Not in

 |

### State values[](https://developers.hubspot.com/docs/api/cms/pages#state-values)

To retrieve pages with a given publish state, include the `state__in=` query parameter with the following values:

**Draft:** `DRAFT`, `DRAFT_AB`, `DRAFT_AB_VARIANT`, `LOSER_AB_VARIANT`

**Scheduled:** `PUBLISHED_OR_SCHEDULED`, `SCHEDULED_AB`

**Published:** `PUBLISHED_OR_SCHEDULED`, `PUBLISHED_AB`, `PUBLISHED_AB_VARIANT`

Because both scheduled and published pages will reflect a `PUBLISHED_OR_SCHEDULED` state, it's recommended to also include a `publishDate` parameter to better understand the page's current state.

For example, to identify the pages that are currently scheduled but not yet published, your request URL should include a `publishDate` parameter that uses the `gt` (greater than) operator with the current datetime specified. This will filter for pages with a publish time in the future:

`state__in=PUBLISHED_OR_SCHEDULED&publishDate__gt={currentTime}`

To identify the pages that are already published, your request URL would similarly include a publishDate parameter, but you would use the `lt` (less than) operator with the current datetime specified.

`state__in=PUBLISHED_OR_SCHEDULED&publishDate__lt={currentTime}`

**Please note:** `currentState` is a generated field which cannot be used as a filter. This field will reflect the page's current publish state.

### A/B filters[](https://developers.hubspot.com/docs/api/cms/pages#a-b-filters)

When filtering for A/B test pages, you can use the following filters:

| 
Description

 | 

Query Params 

 |
| --- | --- |
| 

Active A page or winning variant of a completed A/B test

 | 

`abStatus__eq=MASTER`

 |
| 

Active B page

 | 

`abStatus__eq=VARIANT`

 |
| 

Losing variant of a completed A/B test

 | 

`abStatus__eq=LOSER_VARIANT`

 |

**Please note:**

*   An A/B test is running only when there are published, active A and B pages.
*   An A/B test is complete when a winning and losing variant have been selected, i.e. there isn’t an active B page.

### Multi-language filters[](https://developers.hubspot.com/docs/api/cms/pages#multi-language-filters)

When filtering for multi-language pages, you can use the following filters:

| 
Description

 | 

Query Params

 |
| --- | --- |
| 

Primary page in a multi-language group

 | 

`translatedFromId__is_null`

 |
| 

Variation page in a multi-language group

 | 

`translatedFromId__not_null`

 |
| 

Page with specific Language\* (German)

 | 

`language__in=de`

Does not support language locale values (e.g., `en-us`)

 |

Sorting[](https://developers.hubspot.com/docs/api/cms/pages#sorting)
--------------------------------------------------------------------

To sort results, you can add a `sort` query parameter to your request URL, followed by the property name. You can reverse the sort by adding a `-` to the property name. For example: `sort=-publishDate`.

By combining query parameters for filtering, sorting and paging, you can retrieve the pages that match your search criteria. For example, the request below fetches landing pages that do not have a language assigned, ordered by most recently updated. The limit and offset parameters below return the second page of results.

Shell script

Copy all

    curl https://api.hubapi.com/cms/v3/pages/landing-pages?sort=-updatedAt&&language__not_null&limit=10&offset=10 \
      --request POST \
      --header "Content-Type: application/json"

Create pages[](https://developers.hubspot.com/docs/api/cms/pages#create-pages)
------------------------------------------------------------------------------

To create a website page, make a `POST` request to `/cms/v3/pages/site-pages`. In the request body, you'll include a JSON payload that sets the page's details along with the page content contained in the `layoutSections` object.

The required fields when creating a page are `name` and `templatePath`. To set the URL of a page, set the `domain` and `slug` fields. Note that the `url` field is generated and cannot be updated. Learn more about [creating and customizing pages within HubSpot](https://knowledge.hubspot.com/website-pages/create-and-customize-pages).

You can create the page as a draft so that it's not yet published by setting the `state` to `DRAFT`. See [available states](#state-values) for more information.

JSON

Copy all

    // Example request body
    {
      "domain": "",
      "htmlTitle": "My draft",
      "name": "My test page",
      "slug": "my-test-page",
      "state": "DRAFT",
      "templatePath": "@hubspot/growth/templates/paid-consultation.html",
      "url": "https://www.bird.estate/my-draft",
      "useFeaturedImage": false,
      "layoutSections": {
        "dnd_area": {
          "cells": [],
          "cssClass": "",
          "cssId": "",
          "cssStyle": "",
          "label": "Main section",
          "name": "dnd_area",
          "params": {},
          "rowMetaData": [
            {
              "cssClass": "dnd-section",
              "styles": {
                "backgroundColor": {
                  "a": 1,
                  "b": 250,
                  "g": 248,
                  "r": 245
                },
                "forceFullWidthSection": false
              }
            },
            {
              "cssClass": "dnd-section",
              "styles": {
                "backgroundColor": {
                  "a": 1,
                  "b": 255,
                  "g": 255,
                  "r": 255
                },
                "forceFullWidthSection": false
              }
            }
          ],
          "rows": [
            {
              "0": {
                "cells": [],
                "cssClass": "",
                "cssId": "",
                "cssStyle": "",
                "name": "dnd_area-column-2",
                "params": {
                  "css_class": "dnd-column"
                },
                "rowMetaData": [
                  {
                    "cssClass": "dnd-row"
                  },
                  {
                    "cssClass": "dnd-row"
                  },
                  {
                    "cssClass": "dnd-row"
                  }
                ],
                "rows": [
                  {
                    "0": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-3",
                      "params": {
                        "child_css": {},
                        "css": {},
                        "css_class": "dnd-module",
                        "extra_classes": "widget-type-rich_text",
                        "html": "<div style='text-align:center;'>\n<h2><strong>About</strong></h2>\n</div>",
                        "path": "@hubspot/rich_text",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 12,
                      "x": 0
                    }
                  },
                  {
                    "0": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-column-4",
                      "params": {
                        "css_class": "dnd-column"
                      },
                      "rowMetaData": [
                        {
                          "cssClass": "dnd-row",
                          "styles": {}
                        }
                      ],
                      "rows": [
                        {
                          "0": {
                            "cells": [],
                            "cssClass": "",
                            "cssId": "",
                            "cssStyle": "",
                            "name": "dnd_area-module-5",
                            "params": {
                              "child_css": {},
                              "css": {},
                              "css_class": "dnd-module",
                              "extra_classes": "widget-type-linked_image",
                              "horizontal_alignment": "CENTER",
                              "img": {
                                "alt": "Growth theme placeholder image",
                                "loading": "lazy",
                                "max_height": 500,
                                "max_width": 500,
                                "size_type": "auto_custom_max",
                                "src": "//7528309.fs1.hubspotusercontent-na1.net/hubfs/7528309/raw_assets/public/mV0_d-cms-growth-theme_hubspot/growth/images/service-one.jpg"
                              },
                              "path": "@hubspot/linked_image",
                              "schema_version": 2,
                              "smart_objects": [],
                              "smart_type": "NOT_SMART",
                              "style": "margin-bottom: 22px;",
                              "wrap_field_tag": "div"
                            },
                            "rowMetaData": [],
                            "rows": [],
                            "styles": {
                              "flexboxPositioning": "TOP_CENTER"
                            },
                            "type": "custom_widget",
                            "w": 12,
                            "x": 0
                          }
                        }
                      ],
                      "type": "cell",
                      "w": 6,
                      "x": 0
                    },
                    "6": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-column-6",
                      "params": {
                        "css_class": "dnd-column"
                      },
                      "rowMetaData": [
                        {
                          "cssClass": "dnd-row"
                        }
                      ],
                      "rows": [
                        {
                          "0": {
                            "cells": [],
                            "cssClass": "",
                            "cssId": "",
                            "cssStyle": "",
                            "name": "dnd_area-module-7",
                            "params": {
                              "child_css": {},
                              "css": {},
                              "css_class": "dnd-module",
                              "extra_classes": "widget-type-rich_text",
                              "html": "<p>Add a short description about the work that you do at your company. Try to narrow in on your specialization so that you can capture the attention of your clients. Talk about the value that you can deliver through a paid consultation.</p>",
                              "path": "@hubspot/rich_text",
                              "schema_version": 2,
                              "smart_objects": [],
                              "smart_type": "NOT_SMART",
                              "wrap_field_tag": "div"
                            },
                            "rowMetaData": [],
                            "rows": [],
                            "type": "custom_widget",
                            "w": 12,
                            "x": 0
                          }
                        }
                      ],
                      "type": "cell",
                      "w": 6,
                      "x": 6
                    }
                  },
                  {
                    "0": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-8",
                      "params": {
                        "button_link": {
                          "no_follow": false,
                          "open_in_new_tab": false,
                          "rel": "",
                          "sponsored": false,
                          "url": {
                            "href": "#book"
                          },
                          "user_generated_content": false
                        },
                        "button_text": "Book a consultation",
                        "child_css": {},
                        "css": {},
                        "css_class": "dnd-module",
                        "path": "../modules/button",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "styles": {
                          "alignment": {
                            "alignment": {
                              "css": "",
                              "horizontal_align": "CENTER"
                            }
                          }
                        },
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 12,
                      "x": 0
                    }
                  }
                ],
                "styles": {},
                "type": "cell",
                "w": 12,
                "x": 0
              }
            },
            {
              "0": {
                "cells": [],
                "cssClass": "",
                "cssId": "",
                "cssStyle": "",
                "name": "dnd_area-column-9",
                "params": {
                  "css_class": "dnd-column"
                },
                "rowMetaData": [
                  {
                    "cssClass": "dnd-row",
                    "styles": {}
                  },
                  {
                    "cssClass": "dnd-row"
                  },
                  {
                    "cssClass": "dnd-row"
                  }
                ],
                "rows": [
                  {
                    "0": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-10",
                      "params": {
                        "child_css": {},
                        "css": {},
                        "css_class": "dnd-module",
                        "extra_classes": "widget-type-rich_text",
                        "html": "<a id=\"services\" data-hs-anchor=\"true\"></a>\n<div style=\"text-align: center;\">\n<h2>A suite of tools at your disposal</h2>\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>\n</div>",
                        "path": "@hubspot/rich_text",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 12,
                      "x": 0
                    }
                  },
                  {
                    "0": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-11",
                      "params": {
                        "child_css": {},
                        "content": {
                          "content": "<h3 style='text-align:center;'>Service</h3><p>Summarize the service you provide. Add a message about the value that you can provide to your customers.</p>"
                        },
                        "css": {},
                        "css_class": "dnd-module",
                        "icon": {
                          "icon": {
                            "icon_set": "fontawesome-5.0.10",
                            "name": "balance-scale",
                            "type": "SOLID",
                            "unicode": "f24e"
                          }
                        },
                        "path": "../modules/service-card",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "styles": {
                          "card": {
                            "spacing": {
                              "spacing": {
                                "css": "margin-bottom: 22px;\n",
                                "margin": {
                                  "bottom": {
                                    "units": "px",
                                    "value": 22
                                  }
                                }
                              }
                            }
                          },
                          "icon": {
                            "background": {
                              "color": {
                                "color": "#494a52",
                                "css": "#494a52",
                                "hex": "#494a52",
                                "opacity": 100,
                                "rgb": "rgb(73, 74, 82)",
                                "rgba": "rgba(73, 74, 82, 1)"
                              }
                            }
                          }
                        },
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 4,
                      "x": 0
                    },
                    "4": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-12",
                      "params": {
                        "child_css": {},
                        "content": {
                          "content": "<h3 style='text-align:center;'>Service</h3><p>Summarize the service you provide. Add a message about the value that you can provide to your customers.</p>"
                        },
                        "css": {},
                        "css_class": "dnd-module",
                        "icon": {
                          "icon": {
                            "icon_set": "fontawesome-5.0.10",
                            "name": "industry",
                            "type": "SOLID",
                            "unicode": "f275"
                          }
                        },
                        "path": "../modules/service-card",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "styles": {
                          "card": {
                            "spacing": {
                              "spacing": {
                                "css": "margin-bottom: 22px;\n",
                                "margin": {
                                  "bottom": {
                                    "units": "px",
                                    "value": 22
                                  }
                                }
                              }
                            }
                          },
                          "icon": {
                            "background": {
                              "color": {
                                "color": "#494a52",
                                "css": "#494a52",
                                "hex": "#494a52",
                                "opacity": 100,
                                "rgb": "rgb(73, 74, 82)",
                                "rgba": "rgba(73, 74, 82, 1)"
                              }
                            }
                          }
                        },
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 4,
                      "x": 4
                    },
                    "8": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-13",
                      "params": {
                        "child_css": {},
                        "content": {
                          "content": "<h3 style='text-align:center;'>Service</h3><p>Summarize the service you provide. Add a message about the value that you can provide to your customers.</p>"
                        },
                        "css": {},
                        "css_class": "dnd-module",
                        "icon": {
                          "icon": {
                            "icon_set": "fontawesome-5.0.10",
                            "name": "server",
                            "type": "SOLID",
                            "unicode": "f233"
                          }
                        },
                        "path": "../modules/service-card",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "styles": {
                          "card": {
                            "spacing": {
                              "spacing": {
                                "css": "margin-bottom: 22px;\n",
                                "margin": {
                                  "bottom": {
                                    "units": "px",
                                    "value": 22
                                  }
                                }
                              }
                            }
                          },
                          "icon": {
                            "background": {
                              "color": {
                                "color": "#494a52",
                                "css": "#494a52",
                                "hex": "#494a52",
                                "opacity": 100,
                                "rgb": "rgb(73, 74, 82)",
                                "rgba": "rgba(73, 74, 82, 1)"
                              }
                            }
                          }
                        },
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 4,
                      "x": 8
                    }
                  },
                  {
                    "0": {
                      "cells": [],
                      "cssClass": "",
                      "cssId": "",
                      "cssStyle": "",
                      "name": "dnd_area-module-14",
                      "params": {
                        "button_link": {
                          "no_follow": false,
                          "open_in_new_tab": false,
                          "rel": "",
                          "sponsored": false,
                          "url": {
                            "href": "#book"
                          },
                          "user_generated_content": false
                        },
                        "button_text": "Book a consultation",
                        "child_css": {},
                        "css": {},
                        "css_class": "dnd-module",
                        "path": "../modules/button",
                        "schema_version": 2,
                        "smart_objects": [],
                        "smart_type": "NOT_SMART",
                        "styles": {
                          "alignment": {
                            "alignment": {
                              "css": "",
                              "horizontal_align": "CENTER"
                            }
                          }
                        },
                        "wrap_field_tag": "div"
                      },
                      "rowMetaData": [],
                      "rows": [],
                      "type": "custom_widget",
                      "w": 12,
                      "x": 0
                    }
                  }
                ],
                "type": "cell",
                "w": 12,
                "x": 0
              }
            }
          ],
          "type": "cell",
          "w": 12,
          "x": 0
        }
      }
    }

Editing pages[](https://developers.hubspot.com/docs/api/cms/pages#editing-pages)
--------------------------------------------------------------------------------

Pages in HubSpot have both draft and live versions. The draft version may be updated without affecting the live page content. Drafts can be reviewed and then published by a user working in HubSpot. They may also be scheduled for publication at a future time via the `/schedule` endpoint. Draft changes can be discarded via the `/reset` endpoint, allowing users to go back to the current live version of the page without disruption. 

### Edit Draft

The draft version of a page can be updated via a `PATCH` request to the `{objectid}/draft` endpoint. This endpoint accepts a JSON payload representing the page model.

Modifying the content of a page via these APIs is _not_ recommended -- the content editor in HubSpot is the simplest way to modify website content.

You can modify the `widgets`, `widgetContainers`, and `layoutSections` properties via this endpoint. They store page-level module data, contained directly in the template (`widgets`), within flex columns (`widgetContainers`) and in drag-and-drop areas (`layoutSections`).

The properties provided in the supplied payload will override the existing draft properties without any complex merging logic. Consequently, when updating nested properties such as those within the `widgets`, `widgetContainers`, or `layoutSections` of the page, you must include the full definition of the object. Partial updates are not supported.

### Reset Draft

The draft version of a page can be reset to the current live version via a `POST` request to the `{objectId}/draft/reset` endpoint. This endpoint accepts no payload and simply reverts the draft version of the target page to match the current live version.

Publishing pages[](https://developers.hubspot.com/docs/api/cms/pages#publishing-pages)
--------------------------------------------------------------------------------------

Unpublished changes to a published page can be pushed live via a `POST` request to the `{objectId}/draft/push-live` endpoint. This endpoint accepts no payload and will only update an already published page, not publish a drafted page.

### Publish Draft (Scheduled)

The draft version of a page can be scheduled for publication at a future time via a `POST` request to the `schedule` endpoint. This endpoint accepts a JSON payload containing the `id` of the target page and a `publishDate`. Learn more about [scheduling page publication.](https://knowledge.hubspot.com/website-pages/use-advanced-publishing-features) 

A/B testing[](https://developers.hubspot.com/docs/api/cms/pages#a-b-testing)
----------------------------------------------------------------------------

A/B tests can be used to tune and optimize content by splitting traffic to a page across two variants of differing formats. Conversion rate of each page is monitored over time so that a winner can be chosen based on the relative success of each variant. Learn more about [running A/B tests in HubSpot](https://knowledge.hubspot.com/website-pages/run-an-a-b-test-on-your-page). 

The following properties will be populated on pages with active or completed A/B tests:

*   `abTestId`: Unique identifier for the page’s associated A/B test
*   `abStatus`: Indicates whether the page is an A/B primary, variant, or loser variant

#### Create Test

An A/B test variant can be created via a `POST` request to the `ab-test/create-variation` endpoint. This endpoint accepts a JSON payload containing the `contentId` of the page to test and a `variationName` for the variant to be created.

Upon creation, the new test variant can be [updated](#editing-pages) and [published](#publishing-pages) in the same manner as a standard page.

#### End Test

Once enough traffic has been monitored across each variant and a clear winner has been determined, an A/B test can be terminated via a `POST` request to the `ab-test/end` endpoint. This endpoint accepts a JSON payload containing the `abTestId` of the target A/B test and the `winnerId` of the content deemed the winner.

Multi-language content[](https://developers.hubspot.com/docs/api/cms/pages#multi-language-content)
--------------------------------------------------------------------------------------------------

In HubSpot, you can group together language variants of the same content. Learn more about [working with multi-language pages in HubSpot](https://knowledge.hubspot.com/website-pages/create-pages-in-multiple-languages#create-a-multi-language-variation-of-a-page). 

The following properties will be populated on pages within a multi-language group:

*   `translatedFromId`: unique identifier for the primary language page of the multi-language group. This property will be null on the primary page itself.
*   `language`: the ISO 639 code representing the language of the page.
*   `translations`: a map of ISO 639 codes to variant page objects within the multi-language group.

#### Create a New Language Variant

A new language variant of an existing page can be created via a `POST` request to the `multi-language/create-language-variant` endpoint. This endpoint accepts a JSON payload containing the `id` of the page to clone and the `language` identifier of the new variant.

#### Attach a Page to an Existing Multi-Language Group

A page can be added to an existing multi-language group via a `POST` request to the `multi-language/attach-to-lang-group` endpoint. This endpoint accepts a JSON payload containing the `id` of the target page, the `language` identifier of the page being added, and the `primaryId` of the page designated as the primary page in the target multi-language group.

#### Detach a Page from a Multi-Language Group

A page can be removed from a multi-languages group via a `POST` request to the `multi-language/detach-from-lang-group` endpoint. This endpoint accepts a JSON payload containing the `id` of the target page.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/cms/pages#page-feedback)
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