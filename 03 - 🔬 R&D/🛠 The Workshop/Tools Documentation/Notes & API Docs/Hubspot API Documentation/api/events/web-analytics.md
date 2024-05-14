Event Analytics
===============

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the event analytics API to fetch events associated with CRM records of any type (Marketing Hub Enterprise, Sales Hub Enterprise, Service Hub Enterprise, or CMS Hub Enterprise only). This includes standard events, such as website page views and email opens, as well as [custom events](/docs/api/analytics/events).

For example, use this API to view a timeline of the interactions that a contact has had with your content. You can then use this timeline to build a dataset for custom analytics or present a contact timeline in an external application.

Query individual event completions[](https://developers.hubspot.com/docs/api/events/event-analytics#query-individual-event-completions)
---------------------------------------------------------------------------------------------------------------------------------------

This API returns events for one CRM record at a time. You can select the record by specifying the `objectType` and including either the `objectId` or `objectProperty` query parameter.

### Select by object ID[](https://developers.hubspot.com/docs/api/events/event-analytics#select-by-object-id)

To specify a record by its ID, add the `objectId` query parameter. For example, to specify a contact record with the ID of _2832_, you would make the following `GET` request: 

`/events/v3/events/?objectType=contact&objectId=224834`

### Select by object property[](https://developers.hubspot.com/docs/api/events/event-analytics#select-by-object-property)

To specify a record by a unique property instead of contact ID, add the `objectProperty` parameter. Reference the property by including the property name and the value in the following format:

`objectProperty.{propname}={propvalue}`

For example, to specify a contact by their email address, you would make the following `GET` request: 

`/events/v3/events/?objectType=contact&objectProperty.email=user12@dev.com`

Querying and filtering for event types[](https://developers.hubspot.com/docs/api/events/event-analytics#querying-and-filtering-for-event-types)
-----------------------------------------------------------------------------------------------------------------------------------------------

When querying for the events associated with a given CRM object, the response will include all event types, including custom behavioral events.

To only return event completions for a specific event type, you can include an `eventType` parameter, followed by the event name. To get a list of all available event types, you can make a `GET` request to `/events/v3/events/event-types`. The response will return all event types in your account. You can then use one of these event names as a query parameter in a `GET` request to the `/events/v3/events` endpoint.

For example:

`/events/v3/events/eventType={EVENT_NAME}&objectType=contact&objectId=224834`

  

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/events/event-analytics#page-feedback)
---------------------------------------------------------------------------------------------------

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