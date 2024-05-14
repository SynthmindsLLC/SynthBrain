Extensions overview
===================

Using extensions, you can customize the functionality of the HubSpot CRM. HubSpot offers a variety of extensions, such as creating custom events for CRM record timelines or enabling custom calling options with the calling SDK. You can also create UI extensions if you’re enrolled in the CRM development tools beta, which enables you to create custom cards with a wide variety of customizable components.

Below is a list of the extensions that HubSpot currently offers:

*   [**Calling extensions SDK**](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk)**:** enable users to [make calls](https://knowledge.hubspot.com/calling/use-the-calling-tool) using custom calling options.
*   [**Custom timeline events**](https://developers.hubspot.com/docs/api/crm/timeline)**:** create custom events that display information from other systems on CRM record timelines.
*   [**CRM cards**](https://developers.hubspot.com/docs/api/crm/extensions/custom-cards)**:** create cards to pull external data into CRM records. These types of cards are separate from UI extensions, which offer more customization options and components as a part of the CRM development tools beta. 
*   [**UI extensions (BETA)**](https://developers.hubspot.com/docs/platform/create-custom-crm-cards-with-projects)**:** customize CRM record pages with custom cards that can send and receive HubSpot and external data using a wide variety of customizable components. Only available through the CRM development tools beta.
*   [**Video conference extension**](https://developers.hubspot.com/docs/api/crm/extensions/video-conferencing)**:** integrate video conferencing into the meetings tool.

Extensions are powered by apps, which means you’ll first need to create a [public app](/docs/api/creating-an-app) or a [private app in projects (BETA)](/docs/platform/create-private-apps-with-projects) before you can add an extension to an account.

Extension support in apps[](https://developers.hubspot.com/docs/api/crm/extensions/overview#extension-support-in-apps)
----------------------------------------------------------------------------------------------------------------------

Because private apps and public apps support different extensions, you’ll first need to decide what type of app to create. Review the table below to understand which extensions are supported by which app types.

Learn more about the differences between these types of apps in the [building apps overview](/docs/api/developer-tools-overview).

| App type | Supported extensions |
| --- | --- |
| Private app | Extensions are not currently supported for [private apps created in the integration settings](/docs/api/private-apps) of your HubSpot account. |
| Public app | 
*   [Calling SDK](https://developers.hubspot.com/docs/api/crm/extensions/calling-sdk)
*   [CRM cards](https://developers.hubspot.com/docs/api/crm/extensions/custom-cards)\*
*   [Timeline events](https://developers.hubspot.com/docs/api/crm/timeline)
*   Video conference extension

 |
| Private apps in projects (BETA) | 

*   [UI extensions](/docs/platform/create-custom-crm-cards-with-projects)

 |

\* The CRM cards you can build with public apps are different from the custom cards you can create as UI extensions with projects (BETA). UI extensions offer more advanced functionality and customizable components

After deciding which type of app to create, get started using the app building guides below.

*   [Create a public app](/docs/api/creating-an-app)
*   [Private apps in projects (BETA)](/docs/platform/create-private-apps-with-projects)
*   [Projects quickstart guide](/docs/platform/projects-quick-start-guide)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/extensions/overview#page-feedback)
----------------------------------------------------------------------------------------------------

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