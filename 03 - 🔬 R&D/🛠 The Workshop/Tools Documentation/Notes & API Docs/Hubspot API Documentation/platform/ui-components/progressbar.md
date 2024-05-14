ProgressBar | UI components (BETA)
==================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `ProgressBar` component renders a visual indicator showing a numeric and/or percentage-based representation of progress. The percentage is calculated based on the maximum possible value specified in the component.

![design-guidelines-progress-bar](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-progress-bar.png)

1.  **Title:** the text that displays above the bar to describe the data it represents.
2.  **Completion percentage:** the percent value of how much progress has been made.
3.  **Value description:** the text that describes the current state of the bar's value.
4.  **Variant:** the color of the progress bar.

import { ProgressBar } from '@hubspot/ui-extensions'; const Extension = () => { return ( <ProgressBar variant="warning" value={50} maxValue={200} showPercentage={true} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `title` | String | The text that displays above the progress bar. |
| `showPercentage` | Boolean | When set to `true`, the progress bar will display the completion percentage. Default is `false`. |
| `value` | Number | The number representing the progress so far. Default is `0`. |
| `maxValue` | Number | 
The maximum value of the progress bar. Default is `100`.

 |
| `valueDescription` | String | The text that explains the current state of the `value` property. For example, `"150 out of 250"`. |
| `variant` | `'success'` (default) | `'warning'` | `'danger'` | The color to indicate progress sentiment. |
| `aria-label` | String | The accessibility label. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/progressbar#variants)
-------------------------------------------------------------------------------------------

Using the variant prop, you can set the following progress bar colors:

*   `success`: a green colored bar to indicate movement towards a positive goal or outcome.  
    ![design-guidelines-progress-bars_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bars_1.png?width=544&height=67&name=design-guidelines-progress-bars_1.png)
*   `warning`: a yellow colored bar to indicate movement towards a negative outcome or limitation.  
    ![design-guidelines-progress-bars_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bars_2.png?width=544&height=84&name=design-guidelines-progress-bars_2.png)
*   `danger`: a red colored bar to indicate movement towards an extremely negative outcome or when a limitation has been reached.  
    ![design-guidelines-progress-bars_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-progress-bars_3.png?width=544&height=81&name=design-guidelines-progress-bars_3.png)

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/progressbar#usage-examples)
-------------------------------------------------------------------------------------------------------

*   Evaluating the sale of products against a quota or goal.
*   Communicating the stage progress of a deal or ticket.
*   Monitoring the number of support calls or tickets per customer.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/progressbar#guidelines)
-----------------------------------------------------------------------------------------------

*   **DO:** use the `showPercentage` prop to give the user more information about the status of the progress.
*   **DON'T:** use more than 3-4 progress bars in a single card.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/progressbar#related-components)
---------------------------------------------------------------------------------------------------------------

*   [StepIndicator](https://developers.hubspot.com/docs/platform/ui-components/stepindicator)
*   [LoadingSpinner](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner)
*   [Statistics](https://developers.hubspot.com/docs/platform/ui-components/statistics)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/progressbar#page-feedback)
-----------------------------------------------------------------------------------------------------------

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