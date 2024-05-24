EmptyState | UI components (BETA)
=================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `EmptyState` component sets the content that appears when the extension is in an empty state. Use this component when there's no content or data to help guide users.

![design-guidelines-empty-state-primary-button](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/design-guidelines-empty-state-primary-button.png?width=455&height=347&name=design-guidelines-empty-state-primary-button.png)

  

1.  **Image:** the default image that comes with the component.
2.  **Title:** the title that describes why the component is in an empty state.
3.  **Additional text:** an additional [`Text` component](/docs/platform/ui-extension-components/text) to provide further guidance. This does not come with the component by default.
4.  **Additional button:** an additional [`Button` component](/docs/platform/ui-components/button) to can help users take action. This does not come with the component by default.

import { EmptyState, Text } from '@hubspot/ui-extensions'; const Extension = ({ data }) => { if (!data || !data.length) { return ( <EmptyState title="Nothing here yet" layout="vertical" reverseOrder={true}> <Text>Go out there and get some leads!</Text> </EmptyState> ) } return ( {data.map(...)} ); }

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `flush` |  Boolean | When set to `true`, removes the default vertical margins for the component. By default, set to `false`. |
| `imageWidth` |  Number | The max-width for the image container. By default, set to `250`. |
| `layout` |  `'horizontal'` | `'vertical'` (default) | The layout direction of the content. |
| `reverseOrder` | Boolean | When set to `true`, swaps out the visual order of the text (primary) and image (secondary) content. This ensures that the primary content is presented first to screen readers. By default, set to `false`. |
| `title` | String | The text for the title header. |

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/emptystate#usage-examples)
------------------------------------------------------------------------------------------------------

*   Display when it's the first use of a feature.
*   Show when the user is required to take action in order to populate the card with information.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/emptystate#guidelines)
----------------------------------------------------------------------------------------------

*   **DO:** make empty states informative so that users understand what will appear when the extension is not empty.
*   **DO:** make empty states actionable. If relevant, explain the benefits of this area and how to add content or data.
*   **DON'T:** make empty states too long.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/emptystate#related-components)
--------------------------------------------------------------------------------------------------------------

*   [Alert](https://developers.hubspot.com/docs/platform/ui-components/alert)
*   [ErrorState](https://developers.hubspot.com/docs/platform/ui-components/errorstate)
*   [LoadingSpinner](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/emptystate#page-feedback)
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