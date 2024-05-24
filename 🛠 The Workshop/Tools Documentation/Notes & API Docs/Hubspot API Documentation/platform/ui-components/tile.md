Tile | UI components (BETA)
===========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Tile` component renders a square tile that can contain other components. Use this component to create groups of related components.

![tile-component-example](https://developers.hubspot.com/hubfs/Knowledge_Base_2023_2024/tile-component-example.png)

import { Tile, Text } from '@hubspot/ui-extensions'; const Extension = () => { return ( <> <Tile> <Text>This is the default tile. It has a small amount of left padding</Text> </Tile> <Tile compact={true}> <Text>This is a compact tile. It reduces the amount of padding within.</Text> </Tile> <Tile flush={true}> <Text>This is a flush tile. It has no left padding</Text> </Tile> </> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `compact` | Boolean | When set to `true`, reduces the amount of padding in the tile. Default is `false`. |
| `flush` | Boolean | When set to `true`, removes left and right padding from the tile contents. Default is `false`. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/tile#variants)
------------------------------------------------------------------------------------

Using the `flush` prop, you can remove left and right padding from the tile contents.

*   `flush={false}` (default)  
    ![design-guidelines-tile-styles_1](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-tile-styles_1.png)
*   `flush={true}`  
    ![design-guidelines-tile-styles_2](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-tile-styles_2.png)

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/tile#usage-examples)
------------------------------------------------------------------------------------------------

*   Group a form and its inputs together.
*   Group a bulleted text summary and statistics components together. 

Related components[](https://developers.hubspot.com/docs/platform/ui-components/tile#related-components)
--------------------------------------------------------------------------------------------------------

*   [Box](https://developers.hubspot.com/docs/platform/ui-components/box)
*   [Divider](https://developers.hubspot.com/docs/platform/ui-components/divider)
*   [Accordion](https://developers.hubspot.com/docs/platform/ui-components/accordion)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/tile#page-feedback)
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