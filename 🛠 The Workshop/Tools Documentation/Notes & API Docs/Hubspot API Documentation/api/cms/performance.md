---
title: "Sunsetted and Deprecated APIs"
description: "The APIs listed in the sections below will not receive future updates to functionality, and in some cases, will be fully sunsetted and unavailable for use in your integrations. It's highly recommended that you subscribe to the HubSpot Developer Changelog (/changelog) to follow along with the latest updates, breaking changes, and other significant changes to functionality."
type: "group"
tags:
- "HubSpot"
- "APIs"
- "Deprecated"
relationships:
- "#related_to [[Developer Changelog]]"
- "#contains [[Sunsetted APIs], [Deprecated APIs]]"
sunsetted_apis: "-title: CMS performance API"
    sunset_date: "2024-04-09"
    notes: "For website analytics data, use the Analytics API (/analytics/overview)."
-title: "Ecommerce bridge API"
    sunset_date: "2023-02-28"
    notes: "If you previously built an integration using this API, you can follow [the migration guide](/docs/api/migrate-an-existing-ecommerce-bridge-api-integration) to switch over your integration to use private apps."
-title: "Accounting extension API"
    sunset_date: "2023-02-28"
    notes: "If you previously built an integration using this API, you can follow [this migration guide](/docs/api/migrate-an-existing-account-extension-integration) to switch over your integration to use private apps."
-title: "Marketing calendar API"
    sunset_date: "2023-08-31"
    notes: "You can continue to [use the marketing calendar in HubSpot](/knowledge/campaigns/use-your-marketing-calendar)."
deprecated_apis: "-title: Social media API"
    notes: "Includes the following endpoints:"
-Get publishing channels (/social_media/get_channels)
-Get broadcast messages (/social_media/get_broadcasts)
-Get a broadcast message (/social_media/get_broadcast)
-Create a broadcast message (/social_media/create_broadcast)
-Cancel a broadcast message (/social_media/cancel_broadcast)
feedback: "-question: Was this article helpful? Yes No"
    answer: ""
-question: "Inaccurate: it doesnt reflect what I see in the product"
    answer: ""
-question: "Unclear: its difficult to understand"
    answer: ""
-question: "Missing information: its not comprehensive enough"
    answer: ""
-question: "Irrelevant: it doesnt match what I searched for"
    answer: ""
-question: "Great! Is there anything we could change to make it even more helpful? Is there anything we could change to make this article helpful?"
      answer: ""
-question: "Allow HubSpot to contact me about my documentation feedback."
        email_address: ""
feedback_form_required: "true"
---

Sunsetted and deprecated APIs
=============================

The APIs listed in the sections below will not receive future updates to functionality, and in some cases, will be fully sunsetted and unavailable for use in your integrations.

It's highly recommended that you subscribe to the [HubSpot Developer Changelog](/changelog) to follow along with the latest updates, breaking changes, and other significant changes to functionality.

Sunsetted APIs[](https://developers.hubspot.com/docs/api/deprecated-apis#sunsetted-apis)
----------------------------------------------------------------------------------------

The following APIs have been fully removed, and will return an error when making a call to their associated endpoints.

| API | Sunset date | Notes |
| --- | --- | --- |
| CMS performance | April 9, 2024 | For website analytics data, use the [Analytics API](https://legacydocs.hubspot.com/docs/methods/analytics/analytics-overview). |
| Ecommerce bridge | February 28, 2023 | If you previously built an integration using this API, you can follow [the migration guide](/docs/api/migrate-an-existing-ecommerce-bridge-api-integration) to switch over your integration to use private apps. |
| Accounting extension | February 28, 2023 | If you previously built an integration using this API, you can follow [this migration guide](/docs/api/migrate-an-existing-account-extension-integration) to switch over your integration to use private apps. |
| Marketing calendar | August 31, 2023 | You can continue to [use the marketing calendar in HubSpot](https://knowledge.hubspot.com/campaigns/use-your-marketing-calendar). |

Deprecated APIs[](https://developers.hubspot.com/docs/api/deprecated-apis#deprecated-apis)
------------------------------------------------------------------------------------------

The legacy endpoints listed below will not be getting a version update. These endpoints are functional and stable, but won’t be updated beyond their current version. HubSpot will continue to support them for the foreseeable future and will announce any future changes with ample notice on HubSpot's [Developer Changelog](/changelog).[](https://legacydocs.hubspot.com/docs/methods/social_media/cancel_broadcast)

| API | Notes |
| --- | --- |
| Social media | Includes the following endpoints:
*   [Get publishing channels](https://legacydocs.hubspot.com/docs/methods/social_media/get_channels)
*   [Get broadcast messages](https://legacydocs.hubspot.com/docs/methods/social_media/get_broadcasts)
*   [Get a broadcast message](https://legacydocs.hubspot.com/docs/methods/social_media/get_broadcast)
*   [Create a broadcast message](https://legacydocs.hubspot.com/docs/methods/social_media/create_broadcast)
*   [Cancel a broadcast message](https://legacydocs.hubspot.com/docs/methods/social_media/cancel_broadcast)

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/deprecated-apis#page-feedback)
--------------------------------------------------------------------------------------------

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