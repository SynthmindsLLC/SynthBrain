Statistics | UI components (BETA)
=================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Statistics` component renders a visual spotlight of one or more data points. Includes the `StatisticsItem` and `StatisticsTrend` subcomponents.

![design-guidelines-statistics](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-statistics.png)

1.  **StatisticItem label:** the `statisticItem`'s label text.
2.  **StatisticItem number:** the `statisticItem`'s primary number.
3.  **StatisticTrend value:** the percentage trend value.
4.  **StatisticTrend direction:** the direction if the trend arrow (up or down).

import { Statistics, StatisticsItem, StatisticsTrend } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Statistics> <StatisticsItem label="Item A Sales" number="10000"> <StatisticsTrend direction="decrease" value="200%" /> </StatisticsItem> <StatisticsItem label="Item B Sales" number="100000"> <StatisticsTrend direction="increase" value="100%" /> </StatisticsItem> </Statistics> ); };

StatisticsItem props[](https://developers.hubspot.com/docs/platform/ui-components/statistics#statisticsitem-props)
------------------------------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `id` | String | The statistic item's unique identifier. |
| `label` Required | String | The item's label. |
| `number` Required | String | number | The string to be displayed as the item's primary number. |

StatisticsTrend props[](https://developers.hubspot.com/docs/platform/ui-components/statistics#statisticstrend-props)
--------------------------------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `direction` | `'increase'` (default) |  
`'decrease'` | The direction of the trend arrow. |
| `value` Required | String | The text to be displayed as the trend value. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/statistics#variants)
------------------------------------------------------------------------------------------

In `StatisticsTrend` components, use the `direction` prop to describe whether the data is trend upwards or downwards.

*   `increase`: for additions or positive progression for a given time period.  
    ![design-guidelines-increase-trend](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-increase-trend.png?width=151&height=121&name=design-guidelines-increase-trend.png)
*   `decrease`: for subtractions or negative progression for a given time period.  
    ![design-guidelines-decrease-trend](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-decrease-trend.png?width=137&height=113&name=design-guidelines-decrease-trend.png)

Note that the positive or negative movement of a given statistic is intended solely to represent the increase or decrease in numerical value. Be mindful of how these movements can communicate sentiment. For example, a decrease in support volume can be a net positive, which can be confusing when represented by a red, downward arrow.

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/statistics#usage-examples)
------------------------------------------------------------------------------------------------------

*   Calling out the progress of quarterly sales for a company.
*   Monitoring the amount of traffic and social media engagement that a contact has for the month.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/statistics#guidelines)
----------------------------------------------------------------------------------------------

*   **DO:** keep statistics labels short and concise.
*   **DO:** place statistics components towards the top of a card when possible to enable users to more easily scan information without scrolling.
*   **DON'T:** include more than three statistics components per card if possible.
*   **DON'T:** use more than four statistics components side by side.
*   **DON'T:** include sensitive data that you don't want all users to see.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/statistics#related-components)
--------------------------------------------------------------------------------------------------------------

*   [Table](https://developers.hubspot.com/docs/platform/ui-components/table)
*   [DescriptionList](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist)
*   [CrmPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/statistics#page-feedback)
----------------------------------------------------------------------------------------------------------

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