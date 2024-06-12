---
title: "Marketing Events"
description: "CRM object that enables tracking and association of marketing events, such as webinars, with other HubSpot CRM objects. Learn about working with the marketing event API to integrate marketing events into an app."
type: "group"
tags:
- "CRM"
- "Marketing_Events"
- "HubSpot_Integration"
relationships:
- "#founded_by [[HubSpot]]"
- "#part_of [[Customer Relationship Management (CRM)]]"
- "#related_to [[APIs]], [[Webinars]], [[Events]]"
created_date: "2023-01-01"
---

* * *

Marketing Events
================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

A marketing event is a CRM object, similar to contacts and companies, that enables you to track and associate marketing events, such as a webinar, with other HubSpot CRM objects. Below, learn more about working with the marketing event API to integrate marketing events into an app.

In this article
---------------

*   [Scope requirements](#scope-requirements)
*   [Event attendance endpoints](#scope-requirements)
*   [Configure app settings](#configure-app-settings)
    *   [Step 1: Create an API in your app](#step-1-create-an-api-in-your-app)
    *   [Step 2: Provide HubSpot with the URL path to your API](#step-2-provide-hubspot-with-the-url-path-to-your-api)

Scope requirements[](https://developers.hubspot.com/docs/api/marketing/marketing-events#scope-requirements)
-----------------------------------------------------------------------------------------------------------

To make an API request to one of the marketing event endpoints, the following [scopes](/docs/api/working-with-oauth#scopes) are required:

*   `crm.objects.marketing_events.read`: grants permission to retrieve marketing event and attendance data.
*   `crm.objects.marketing_events.write`: grants permission to create, delete, or make changes to marketing event information.

When authenticating calls made by your app, you can either use a [private app access token](/docs/api/private-apps) or [OAuth](/docs/api/oauth/tokens). Learn more about [authentication methods](/docs/api/intro-to-auth). For the full list of endpoints available, click the Endpoints tab at the top of this article.

Create and update events[](https://developers.hubspot.com/docs/api/marketing/marketing-events#create-and-update-events)
-----------------------------------------------------------------------------------------------------------------------

You can create or update marketing events by making a `POST` request to `/marketing/v3/marketing-events/events/upsert` endpoint. You can include any `customProperties` that correspond to the events you want to update in the `inputs` field of your request body, along with any other details of your event (including its name, start time, and description).

If a marketing event already exists with the specified ID in your request, it will be updated. Otherwise, a new event will be created.

For example, the following request would create an event with an ID of `4` named "Virtual cooking class":

// Example request body for POST request to /marketing/v3/marketing-events/events/upsert { "inputs": \[ { "customProperties": \[ { "name": "property1", "value": "1234" } \], "eventName": "Virtual cooking class", "startDateTime": "2023-11-30T17:46:20.461Z", "eventOrganizer": "Chef Joe", "eventDescription": "Join us for a virtual cooking class! Yum." "eventCancelled": false, "externalAccountId": "CookingCo", "externalEventId": "4" } \] }

You can review a full list of all available fields you can include in your request by clicking the Endpoints tab at the top of this article.

Event attendance endpoints[](https://developers.hubspot.com/docs/api/marketing/marketing-events#event-attendance-endpoints)
---------------------------------------------------------------------------------------------------------------------------

The event attendance state endpoints allow you to record a subscription state between a HubSpot contact and a marketing event. For example, you can use this endpoint to record that a HubSpot contact has registered for a marketing event.

There are two endpoints you can use to update a contact's attendance status. If you were previously using the `/upsert` or `/email-upsert` endpoints to update an attendee's status, you can instead use the endpoints listed below to maintain the same functionality while also populating the contact's attendance duration on the [contact timeline](https://knowledge.hubspot.com/crm-setup/customize-activities-on-a-contact-company-deal-ticket-record-timeline):

*   If you want to use the contact IDs of existing contacts:
    *   Make a `POST` request to `/marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/create`, using the ID of the event from your external application as the `externalEventId`.
    *   In the request body, provide an `inputs` object that includes the following fields:
        *   `interactionDateTime`: the date and time at which the contact subscribed to the event.
        *   `vid`: the contact ID of an existing contact.
*   If you want to use the email address of one of the event's attendees:
    *   Make a `POST` request to `/marketing/v3/marketing-events/attendance/{externalEventId}/{subscriberState}/email-create`.
    *   In the request body, provide an `inputs` object that includes the following fields:
        *   `interactionDateTime`: the date and time at which the contact subscribed to the event.
        *   `email`: the email address of the attendee as the value of the email field within an inputs 
    *   If the email address you include don't match the address of an existing contact, a new contact will be created.

For both of the endpoints above, provide the following values for the corresponding path parameters:

*   `externalEventId`: the ID of the [marketing event](https://knowledge.hubspot.com/integrations/use-marketing-events#view-edit-and-analyze-marketing-events).
*    `subscriberState`: an enumeration that matches the new attendance status of the contact:
    *   `REGISTERED`: indicates that the HubSpot contact has registered for the event.
    *   `ATTENDED`: indicates that the HubSpot contact has attended the event. If you're updating a contact's status to ATTENDED, you can also include the `joinedAt` and `leftAt` timestamps as parameters in the request body, specified in the ISO8601 Instant format.
    *   `CANCELLED`: indicates that the HubSpot contact, who had previously registered for the event, has cancelled their registration.

Once your event has completed, you can mark the event as complete and calculate attendance metrics (e.g., duration of attendance for all attendees) by making a `POST` request to `/marketing/v3/marketing-events/events/{externalEventId}/complete`. Note this action is irreversible, so you should only invoke this endpoint once all attendance state change events have already occurred. 

**Please note:** these APIs are idempotent so long as the ID of the contact and the `interactionDateTime` value in the event has not changed. This enables you to safely set subscriber state multiple times without HubSpot creating duplicate events in the marketing events properties.

Configure app settings[](https://developers.hubspot.com/docs/api/marketing/marketing-events#configure-app-settings)
-------------------------------------------------------------------------------------------------------------------

There's some setup required to allow marketing events to sync properly with HubSpot.

If you send HubSpot a subscriber state change (e.g., a registration or cancellation), HubSpot will first check to see if a Marketing Event exists for the specified event ID. If it doesn't, HubSpot will call the configured endpoint for your app to retrieve the details of the marketing event, then create the event in HubSpot and then publish the subscriber state change.

This is provided for convenience; however, it's still recommended that you create the Marketing Events yourself via the CRUD methods provided in the Endpoints tab at the top of this article, and don't rely on this functionality to create your marketing events in HubSpot.

### Step 1: Create an API in your app[](https://developers.hubspot.com/docs/api/marketing/marketing-events#step-1-create-an-api-in-your-app)

In order to support this, HubSpot requires each app that uses Marketing Events to define an API to fetch information about a specific marketing event.

Requirements:

*   Accepts:
    *   `externalAccountId`: a query parameter that specifies the accountId of the customer in the external app.
    *   `appId`: a query parameter that specifies the ID of the HubSpot application that is requesting the event details. This will be the ID of your app.
    *   `externalEventId`: a path parameter in the URL of the request that specifies the ID of the event in the external app that HubSpot requires details about.
*   Returns:
    *   A JSON object that provides details for the marketing event, that includes the following fields detailed in the table below:

| Field Name | Required | Type | Field Description |
| --- | --- | --- | --- |
| `eventName` | true | string | The name of the marketing event |
| `eventOrganizer` | true | string | The name of the organizer of the marketing event. |
| `eventType` | false | string | Describes what type of event this is. For example: `WEBINAR`, `CONFERENCE`, `WORKSHOP` |
| `startDateTime` | false | string($date-time) | The start date and time of the marketing event. |
| `endDateTime` | false | string($date-time) | The end date and time of the marketing event. |
| `eventDescription` | false | string | The description of the marketing event. |
| `eventUrl` | false | string | A URL in the external event application where the marketing event. |
| `eventCancelled` | false | bool | Indicates if the marketing event has been cancelled. Defaults to `false` |

HubSpot will also send a `X-HubSpot-Signature-v3` header that you can use to verify that the request came from HubSpot. Read more about [request signatures](/docs/api/webhooks/validating-requests) for additional details on the signature and how to validate it.

### Step 2: Provide HubSpot with the URL path to your API[](https://developers.hubspot.com/docs/api/marketing/marketing-events#step-2-provide-hubspot-with-the-url-path-to-your-api)

Now that you've created the API in your app that will return an object that provides the details of a specific marketing event, you will need to provide HubSpot with the URL path to your API by making a `POST` request to `/marketing/v3/marketing-events/{appId}/settings`. This will allow HubSpot to determine how to make requests to your app to get the details of a marketing event.

In the body of your `POST` request, specify your URL using the `eventDetailsURL` field. The `eventDetailsURL` must adhere to the following two requirements:

*   Contain a `%s` character sequence, which HubSpot will use to substitute in the ID of the event (`externalEventId`) as a path parameter.
*   It must be the full path to the API resource, including the `https://` prefix and the domain name (e.g., `my.event.app`).

For example, if you configure an `eventDetailsURL` of `https://my.event.app/events/%s`, and you need to make a request to fetch details of an event with id `1234-event-XYZ`, for the HubSpot app with id `app-101` and account with id `ABC-account-789`, HubSpot will make a `GET` request to:

`https://my.event.app/events/1234-event-XYZ?appId=app-101&externalAccountId=ABC-account-789`

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/marketing/marketing-events#page-feedback)
-------------------------------------------------------------------------------------------------------

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