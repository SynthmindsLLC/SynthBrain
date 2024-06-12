---
Please provide me with more context!  To help you write a mission statement, I need to know: "* **What is the subject of the mission?** Is it for a company, a project, a team, a person, or something else? "
* **What are the goals and values?** What does this entity want to achieve, and what principles will guide it? 
* **Who is the target audience?**  Who are you trying to reach with this mission statement?

Once you give me more information, I can help you craft a compelling and impactful mission statement.
---

DescriptionList | UI components (BETA)
======================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `DescriptionList` component renders pairs of labels and values. Use this component to display pairs of labels and values in a way that's easy to read at a glance. It also contains a `DescriptionListItem` subcomponent.

![design-guide-description-list-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guide-description-list-component.png?width=768&height=104&name=design-guide-description-list-component.png)

1.  **Label:** describes the information being displayed.
2.  **Value:** the information to display, contained in a `Text` component.

import { DescriptionList, DescriptionListItem, Text } from '@hubspot/ui-extensions'; const Extension = () => { return ( <DescriptionList direction="row"> <DescriptionListItem label={'First Name'}> <Text>Alan</Text> </DescriptionListItem> <DescriptionListItem label={'Last Name'}> <Text>Turing</Text> </DescriptionListItem> </DescriptionList> ); };

### DescriptionList props[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#descriptionlist-props)

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `direction` | `row` | `column` (default) | The direction that the label and value pairs are displayed. |

### DescriptionListItem props[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#descriptionlistitem-props)

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `label` Required | String |  Text to display as the label. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#variants)
-----------------------------------------------------------------------------------------------

By default, list items will be stacked vertically. You can use the the `direction` prop to stack them horizontally.

*   `row`:  
    ![ui-ext-component-descriptionlist](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-ext-component-descriptionlist.png?width=516&height=68&name=ui-ext-component-descriptionlist.png)
*   `column` (default):  
    ![ui-extension-component-vertical-description-list](https://developers.hubspot.com/hs-fs/hubfs/ui-extension-component-vertical-description-list.png?width=87&height=239&name=ui-extension-component-vertical-description-list.png)

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#usage-examples)
-----------------------------------------------------------------------------------------------------------

*   Display easy to scan information for a sales rep to use on a call.
*   Highlight the most recently updated properties on a company record.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#guidelines)
---------------------------------------------------------------------------------------------------

*   **DO:** keep copy succinct, ideally one word each for the label and value.
*   **DO:** use the horizontal orientation for horizontal layouts, and vertical orientation for column layouts.
*   **DON'T:** use this component to display long strings of text.
*   **DON'T:** use this component for lists that you want to be editable in the UI. 

Related components[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#related-components)
-------------------------------------------------------------------------------------------------------------------

*   [List](https://developers.hubspot.com/docs/platform/ui-components/list)
*   [Table](https://developers.hubspot.com/docs/platform/ui-components/table)
*   [Statistics](https://developers.hubspot.com/docs/platform/ui-components/statistics)
*   [CrmPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist#page-feedback)
---------------------------------------------------------------------------------------------------------------

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