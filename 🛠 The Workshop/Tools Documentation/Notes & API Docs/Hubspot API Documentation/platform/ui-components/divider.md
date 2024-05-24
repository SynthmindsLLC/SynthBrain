Divider | UI components (BETA)
==============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Divider` component renders a grey, horizontal line for spacing out components vertically or creating sections in an extension. Use this component to space out other components when the content needs more separation than white space.

![divider-with-text](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/divider-with-text.png?width=173&height=115&name=divider-with-text.png)

import { Divider, Text } from '@hubspot/ui-extensions'; const Extension = () => { return ( <> <Text>Text above the divider.</Text> <Divider /> <Text>Text below the divider.</Text> </> ); };

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `distance` | `'flush'` | `'extra-small'` | `'small'` (default) | `'medium'` | `'large'` | `'extra-large'` | The space between the divider and the content above and below it. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/divider#variants)
---------------------------------------------------------------------------------------

Using the `distance` prop, you can set the amount of padding above and below the divider. Values range from `'extra-small'` to `'extra-large'` (`small` by default).

![divider-distance-examples](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/divider-distance-examples.png?width=211&height=437&name=divider-distance-examples.png)

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/divider#guidelines)
-------------------------------------------------------------------------------------------

*   **DO:** use dividers to group similar components together.
*   **DO:** consider when a new card or component might be needed, rather than using a divider.
*   **DON'T:** use two dividers in a row without content between them.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/divider#related-components)
-----------------------------------------------------------------------------------------------------------

*   [Box](https://developers.hubspot.com/docs/platform/ui-components/box)
*   [Accordion](https://developers.hubspot.com/docs/platform/ui-components/accordion)
*   [Tile](https://developers.hubspot.com/docs/platform/ui-components/tile)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/divider#page-feedback)
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