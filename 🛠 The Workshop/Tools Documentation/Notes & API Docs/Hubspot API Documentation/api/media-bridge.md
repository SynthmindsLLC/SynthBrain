---
title: "Media Bridge API"
description: "The media bridge API allows integrators to push media objects such as video and audio files, and media consumption data into HubSpot. It also creates features in the users HubSpot account for embedding media objects, CRM timeline events, segmented lists, workflows, and reports."
type: "work"
tags:
- "Media"
- "API"
- "HubSpot"
relationships:
- "#part_of [[HubSpot Integration]]"
- "#enables [[Embedding Media Objects in HubSpot's CMS]]"
- "#used_by [[Integrators, Developers]]"
created_date: "2023-01-01"
---

Media Bridge API
================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

The media bridge API allows integrators to push media objects such as video and audio files, and media consumption data into HubSpot. It also creates the following features in the user’s HubSpot account: 

*   Modules to embed media objects in HubSpot’s drag and drop editors for pages and emails. 
*   CRM timeline events that show when prospects or customers have engaged with videos, audio, and other media types. 
*   Segmented lists for targeted and personalized experiences.
*   Workflows to automate interactions based on media consumption events.
*   Reports to measure the impact of media assets.

The media bridge uses both [custom objects](https://developers.hubspot.com/docs/api/crm/crm-custom-objects) and unified events, HubSpot’s events tracking system. This means you can use both the media bridge API and the custom objects API to build your integration. 

Use the media bridge API[](https://developers.hubspot.com/docs/api/media-bridge/#use-the-media-bridge-api)
----------------------------------------------------------------------------------------------------------

You need a [HubSpot developer account](https://developers.hubspot.com/get-started) to register your media bridge app and set up your initial media object definitions before connecting your app to a HubSpot user’s account. 

Create and customize your media object definitions[](https://developers.hubspot.com/docs/api/media-bridge/#create-and-customize-your-media-object-definitions)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

To define a media object, make a `POST` request to `/media-bridge/v1/{appId}/settings/object-definitions`. You will use the **mediaTypes** parameter to define the object: VIDEO, AUDIO, DOCUMENT, IMAGE or OTHER. 

After defining your media objects, create and modify the media object properties by making a `PATCH` request to `/media-bridge/v1/{appId}/schemas/{objectType}` and a `POST` request to `/media-bridge/v1/{appId}/properties/{objectType}`. 

Any API calls made will include your developer account ID as the **portalID** query parameter. 

Connect your media bridge app to a HubSpot user’s account[](https://developers.hubspot.com/docs/api/media-bridge/#connect-your-media-bridge-app-to-a-hubspot-user-s-account)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To connect your media bridge app to a HubSpot user’s account, you must create an app definition in your HubSpot developer’s account for it. App definitions include:

*   Details such as the logo and text to be shown to the HubSpot user when your integration attempts to make an initial connection to their account.
*   Scopes your integration needs in the user’s HubSpot account. 

To connect your media bridge app to a HubSpot user's account: 

*   Create an [application definition](https://developers.hubspot.com/docs/api/developer-tools-overview) in your developer account for the media bridge app.
*   Include the following scopes when defining your application: 
    *   `media_bridge.read`
    *   `media_bridge.write`
*   Use [OAuth](https://developers.hubspot.com/docs/api/oauth/tokens) authentication when authenticating calls made by your app. Learn more about [authentication methods](https://developers.hubspot.com/docs/api/intro-to-auth).

To verify the app is installed correctly in a customer's portal:

*   Visit `https://app.hubspot.com/media-bridge-demo/{HubID}`, replacing `{HubID}` with the account ID.
*   In the upper right, click the **App** dropdown menu and select your **media bridge app**. 
*   In the app, you can view the app’s supported media types and create example media.

Once the media bridge app has been installed in a customer’s portal, you can:

*   [Create media objects](#create-your-media-objects)
*   [Create CMS Modules for embedding your media objects](#create-cms-modules-to-embed-media)
*   [Send media events](#send-your-media-events)

Create your media objects
-------------------------

After creating your media object definitions and installing your media bridge app in a user’s account, you can use the [OAuth token](https://developers.hubspot.com/docs/api/working-with-oauth) to create and modify media objects in the account. Since media objects are custom objects, use the [custom objects API endpoints](https://developers.hubspot.com/docs/api/crm/crm-custom-objects#tab-2) to create them:

*   Make a `GET` request to `/media-bridge/v1/{appId}/settings/object-definitions/{mediaType}` to find the **objectType**.
*   Make a `POST` request to `/crm/v3/objects/{objectType}` to create the media object in the user’s account. 

A media object represents a piece of embeddable content in a third-party system. Once a media object is added to the media bridge, it can be embedded in HubSpot’s CMS content and associated with media events.

For VIDEO and AUDIO media objects, the tables below list out all of the default and required properties (\* denotes required): 

Default Required properties of the audio video media types
| Parameter | Type | Description |
| --- | --- | --- |
| 
`id`

 | Number | 

An id used to identify the specific piece of media in HubSpot’s media bridge system. This is autogenerated by HubSpot and cannot be set by developers.

 |
| 

`hs_duration`

 | Number | 

The duration of the media in milliseconds.

 |
| 

`hs_oembed_url*`

 | String | 

A URL that must return a valid oEmbed response that follows the [oEmbed spec.](https://oembed.com/#section2) Requires `video` or `rich` type with an iframe in `html`.

 |
| 

`hs_file_url`

 | String | 

URL of the raw media file. This may be used in the future to help support social embedding.

 |
| 

`hs_thumbnail_url`

 | String | 

URL of an image used as the thumbnail for embedding the media into content. The ideal size for this thumbnail is 640x480 pixels.

 |
| 

`hs_poster_url`

 | String | 

URL of an image representing the media. This image should be the same dimensions as the original media, and may be used in places where an image placeholder is needed (for example, when the media is inserted in an email).

 |
| 

`hs_external_id`

 | String | 

The id of the media in the third party’s system. This gives integrators the ability to fetch media from the media bridge based on the same id that they use in their own system. (This is the API endpoint that leverages this mapping)

 |
| 

`hs_folder_path`

 | String | 

A provider-supplied path to the object, intended to represent the object’s location in the third party’s folder system (if any). HubSpot will attempt to represent this directory structure when displaying these objects to the user, but may nest each provider’s objects and folders within a top-level folder named after the provider.

 |
| 

`hs_title*`

 | String | 

The name of the media. This will be shown inside of the HubSpot UI in places such as the media picker.

 |
| 

`hs_details_page_link`

 | String | 

URL that allows a user to view or interact with the media in the media provider’s system. This is used in the HubSpot UI to give users the ability to identify the media without relying on just the title.

 |

For IMAGE media objects, the tables below list out all of the default and required properties (\* denotes required): 

Default Required properties of the audio video media types
| Parameter | Type | Description |
| --- | --- | --- |
| 
`id`

 | Number | 

An id used to identify the specific piece of media in HubSpot’s media bridge system. This is autogenerated by HubSpot, and cannot be set by developers.

 |
| 

`hs_oembed_url*`

 | String | 

A URL that must return a valid oEmbed response that follows the [oEmbed spec.](https://oembed.com/#section2) Requires `video` or `rich` type with an iframe in `html`.

 |
| 

`hs_file_url*`

 | String | 

The URL of the raw media file. This may be used in the future to help support social embedding.

 |
| 

`hs_thumbnail_url`

 | String | 

URL to an image that will be used as the thumbnail for embedding the media into content in places such as the media picker. The ideal size for this thumbnail is 640x480 pixels.

 |
| 

`hs_poster_url`

 | String | 

URL of an image representing the media. This image should be the same dimensions as the original media, and may be used in places where an image placeholder is needed (for example, when the media is inserted in an email).

 |
| 

`hs_external_id`

 | String | 

The id of the media in the third party’s system. This gives integrators the ability to fetch media from the media bridge based on the same id that they use in their own system. (This is the api endpoint that leverages this mapping)

 |
| 

`hs_folder_path`

 | String | 

A provider-supplied path to the object, intended to represent the object’s location in the third party’s folder system (if any). HubSpot will attempt to represent this directory structure when displaying these objects to the user, but may nest each provider’s objects and folders within a top-level folder named after the provider.

 |
| 

`hs_title*`

 | String | 

The name of the media. This will be shown inside of the HubSpot UI in places such as the media picker.

 |
| 

`hs_details_page_link`

 | String | 

A URL that allows a user to view or interact with the media in the media provider’s system. This is used in the HubSpot UI to give users the ability to identify the media without relying on just the title.

 |

Create CMS Modules to embed media[](https://developers.hubspot.com/docs/api/media-bridge/#create-cms-modules-to-embed-media)
----------------------------------------------------------------------------------------------------------------------------

Each media bridge app provider is responsible for creating their own [module](https://developers.hubspot.com/docs/cms/building-blocks/modules) to render their media in the HubSpot CMS. 

When a media bridge app is installed in a HubSpot account, the [Embed field](https://developers.hubspot.com/docs/cms/building-blocks/module-theme-fields#embed) on the module has an additional _Media integration_ source type. This allows the user to select media from the installed app to be embedded on their website page.

After the user selects a piece of media to be embedded, the media’s oembed\_url and oembed\_response are available in HubL to easily render players. Additionally, the id and media\_type of selected media are stored to enable querying for the underlying CRM object via the crm\_objects HubL function. This can be used to fetch any or all of the properties that are part of a media object.

An example use of the crm\_objects HubL function with a media object where the ids are 459 and 922:

`{% set objects = crm_objects("a123_Videos", [459,922]) %} {{ objects }}`

To fetch a specific image with the same object: `{% set object = crm_object("a123_Images", 459) %} {{ object }}`

Apps can fetch the object type (“a123\_Videos” in the example) by making a `GET` request to `/media-bridge/{appId}/settings/object-definitions/{mediaType}`.

Developers should use the [CMS Source Code API](/docs/api/cms/source-code) endpoints to push their custom module code into customers' accounts once customers have connected via oAuth. Once the module code is pushed into the customer’s account, they will automatically be able to start using the developer’s module in their content. 

### Set up an oEmbed domain[](https://developers.hubspot.com/docs/api/media-bridge/#set-up-an-oembed-domain)

To use the [oEmbed](https://developers.hubspot.com/docs/cms/hubl/functions#oembed) HubL function, the domain being used to fetch the oEmbed response must be registered by making a request to `/media-bridge/v1/{appId}/settings/oembed-domains`. The following parameters must be included:

*   **Scheme:** the URL pattern for the media URLs. This URL pattern is used to match the URL passed into the oEmbed HubL function to your oEmbed API. Wildcard values are supported using `*` (e.g. `www.domain.com/*`).

*   **URL:** the URL of your oEmbed API. The media URL is passed to this URL via a `URL` parameter. 
*   **Discovery (Boolean):** determines whether or not your oEmbed API supports oEmbed’s [Discovery](https://oembed.com/#section4) feature. 

By default, the oEmbed domains registered will be made available to all customers who have installed your app. If you have custom domains that are unique to each customer, you can specify which account an oEmbed domain should be allowed to be used in by passing a portalId value into the API request when setting up the oEmbed domain. This will ensure that only the specified HubSpot account can use that oEmbed domain. 

Create a custom module[](https://developers.hubspot.com/docs/api/media-bridge/#create-a-custom-module)
------------------------------------------------------------------------------------------------------

To create a custom module:

*   Navigate to **Marketing** > **Files and Templates** > **Design Tools**. 
*   On the upper left, click **File** \> **New file**.
*   In the dialog box, click the **What would you like to build today?** dropdown menu and select **Module**. 
*   Click **Next**. 
*   Select the checkbox next to each type of content where your module will be used: _pages_, _blog posts_, _blog listings_, _emails_, or _quotes_. Modules used in email templates cannot include CSS or JavaScript. 
*   Select whether this module will be a **local module** or **global module**. If you create a [global module](https://knowledge.hubspot.com/design-manager-user-guide-v2/how-to-use-global-content-across-multiple-templates), editing this module's content will update every location where the module is used. 
*   Enter a **file name** for your module, then click **Create**.
*   In the _Fields_ section on the right, click the **Add field** dropdown menu and select **Embed**. 

![](https://lh3.googleusercontent.com/_cARgVZZLUD-nsJUIaG8XMUdSm1GRLr4Gfw96HeZ6SyXFG0t6yiiPKt5ToSe7nq8arSnG569_wg5X2XsD0XEtmEGiX9sbQxH7deUIJKGshXamME6vXrLN2oVSAt-cmrkTN2nggDsdkChDnEOxKrw5mo)

*   In the _Supported source types_ section, select **Media integration**.
*   In the _Default embed content_ section, click **Select from \[media bridge app\]**.

*   In the right panel, select the **media** you want to embed in the module. 
*   Set any of the editor options, field display conditions, and field repeater options. 

*   Under _HubL variable name_, click **Copy** \> **Copy snippet**.
*   Paste the snippet into the _module.html_ section.
*   To preview how the module will look on your page, click **Preview**.
*   In the left section, click **Select from \[media bridge app\]**, then select the **media** you want to preview. 

Send your media events[](https://developers.hubspot.com/docs/api/media-bridge/#send-your-media-events)
------------------------------------------------------------------------------------------------------

A media event is an event that happens in relation to a media object, like a play event. Once a media event is sent to the media bridge app, it can be used in reports and in timeline CRM cards. 

There are three types of media events:

*   **Played event:** represents when a user begins playing a piece of media. 

*   **Quartile event:** represents when a user has reached quarterly milestones (0%, 25%, 50%, 75%, 100%)  in the piece of media they’re viewing. 

*   **Attention span event**: represents when a user has fully consumed a piece of media, or once the user has completed their session.

Events can be sent by making a `POST` request to `/media-bridge/v2/events/media-played`, `/media-bridge/v2/events/media-played-percent` and `/media-bridge/v2/events/attention-span respectively`. 

For media events to be displayed on the user’s contact timeline in HubSpot, a played event must be sent to the media bridge app for every session. Events from a single session will be shown in one card on the contact activity timeline. 

When events are sent using the v2 event endpoints, they are processed asynchronously, unlike those sent via the v1 endpoints. As such, we recommend the following:

*   The v1 version of the endpoints should be used for any testing as an erroneous request will immediately error out.
*   The v2 version of the endpoints should be used in production as its asynchronous nature will help prevent delays in the client while the event is being written to the media bridge. Events are also retained and retried in case of a temporary failure in the media bridge’s server.

### Connect an event to a contact record[](https://developers.hubspot.com/docs/api/media-bridge/#connect-an-event-to-a-contact-record)

To connect a media event to a contact record, you must provide either the **contactId** or a **contactUtk**. If only a **contactUtk** is provided, it will be converted into a **contactId**. If both are provided in the request, the **contactId** will be used as the source of truth. This parameter allows the media bridge app to create an association between the contact record and the event.

Once a media event has been connected to a contact record, the event can be used in [cross-object reports](https://knowledge.hubspot.com/reports/create-reports-with-the-custom-report-builder). This allows customers to tie their media events to contact records, as well as associated companies and deals.

### Connecting an event to a piece of media[](https://developers.hubspot.com/docs/api/media-bridge/#connecting-an-event-to-a-piece-of-media)

To associate a media event to a piece of media, either the **mediaID** or **externalID** parameters must be included in the request. If both are provided, the **mediaID** will be used as the source of truth.

### Connect an event to a page[](https://developers.hubspot.com/docs/api/media-bridge/#connect-an-event-to-a-page)

To associate a media event to a HubSpot page, the following parameters must be included in the request:

*   If the page is hosted on the HubSpot CMS, the `pageId` must be provided.
*   If the page is not hosted on the HubSpot CMS, the `pageName` and `pageUrl` must be included.

The table below outlines supported properties for the three media events:

Use this table to describe parameters / fields
| Property | Event Type | Description |
| --- | --- | --- |
| 
`mediaBridgeObjectId`

 | All Events | 

The id of the media that this event is related to.

 |
| 

`externalId`

 | String | 

The id of the media in the third party’s system. This gives developers the ability to refer to media in the media bridge based on the same id that they use in their own system. This can be used instead of the `mediaBridgeObjectId` in events. If both an `externalId` and `mediaBridgeObjectId` are provided, the `mediaBridgeObjectId` will be used and the externalId will be ignored.  
  


 |
| 

`sessionId`

 | All Events | 

A unique identifier to represent a viewing session. This can mean different things to different providers, and HubSpot is letting providers decide what a session means to them. This will be used to group events that happened in the same session together. This is expected to be generated by the third party’s system.

 |
| 

`contactId`

 | All Events | 

The ID of the contact in HubSpot’s system that consumed the media. This can be fetched using [HubSpot's Get contact by usertoken (utk) API](https://legacydocs.hubspot.com/docs/methods/contacts/get_contact_by_utk). The API also supports supplying a usertoken, and will handle converting this into a contact ID automatically.

 |
| 

`contactUtk`

 | All Events | 

The usertoken (utk) that identifies which contact consumed the media.

 |
| 

`pageId`

 | All Events | 

The content Id of the page that an event happened on.

 |
| 

`pageName`

 | All Events | 

The name or title of the page that an event happened on.

 |
| 

`pageUrl`

 | All Events | 

The URL of the page that an event happened on.

 |
| 

`occurredTimestamp`

 | All Events | 

The timestamp at which this event occurred, in milliseconds since the epoch.

 |
| 

`attentionSpanMapString / attentionSpanMap`

 | Attention Span | 

This is the raw data which provides the most granular data about spans of the media, and how many times each span was consumed by the user. 

Example: consider a 10 second video where each second is a span. If a visitor watches the first 5 seconds of the video, then restarts the video and watches the first 2 seconds again, the resulting `attentionSpanMapString` would be `“0=2;1=2;2=1;3=1;4=1;5=0;6=0;7=0;8=0;9=0;”`.

 |
| 

`totalPercentPlayed`

 | Attention Span | 

The percent of the media that the user consumed. Providers may calculate this differently depending on how they consider repeated views of the same portion of media. For this reason, the API will not attempt to validate totalPercentWatched against the attention span information for the event. If it is missing, HubSpot will calculate this from the attention span map as follows: (number of spans with a value of 1 or more)/(Total number of spans).

 |
| 

`totalSecondsPlayed`

 | Attention Span | 

The seconds that a user spent consuming the media. The media bridge calculates this as `totalPercentPlayed`\*`mediaDuration`. If a provider would like this to be calculated differently, they can provide the pre-calculated value when they create the event

 |
| 

`playedPercent`

 | Quartile Event | 

A quartile percent value (0, 25, 50, 75, 100) for how much of the media has been consumed so far.

 |
| 

`iframeUrl`

 | Played Event | 

A URL that can be used to display data from an external system using an iFrame. When included, the event on the contact timeline will display a link that will open a modal window displaying the iFrame contents when clicked.

 |
| 

`mediaType`

 | String | 

The media type that the event belongs to (for example, VIDEO or AUDIO) This allows us to properly assign the event to the correct objects when a single provider has support for multiple media types.  
  


 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/media-bridge/#page-feedback)
------------------------------------------------------------------------------------------

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