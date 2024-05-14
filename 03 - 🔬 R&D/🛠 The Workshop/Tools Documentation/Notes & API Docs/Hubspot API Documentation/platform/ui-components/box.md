Box | UI components (BETA)
==========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Box` component renders an empty `div` container for fine tuning the spacing of components. Commonly used with the [Flex](/docs/platform/ui-components/flex) component.

To see an example of how `Flex` and `Box` can be used for layout, check out HubSpot's [Manage layouts: Flex and Box sample project](/docs/platform/sample-projects#managing-layouts-flex-and-box).

![ui-extrensions-layout-box](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-box.png?width=521&height=225&name=ui-extrensions-layout-box.png)

import { Flex, Box, Tile } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Flex direction={'row'} justify={'start'} gap={'small'} > <Box flex={1}> <Tile>flex = 1</Tile> </Box> <Box flex={2}> <Tile>flex = 2</Tile> </Box> <Box flex={3}> <Tile>flex = 3</Tile> </Box> <Box flex={4}> <Tile>flex = 4</Tile> </Box> </Flex> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `alignSelf` | `'start'` | `'center'` | `'end'` | `'baseline'` | `'stretch'` | Distributes a child component along the cross-axis using the available free space. Use this prop for nested `Box` components to align them differently from other child components in the `Flex` group. |
| `flex` | `'initial'` | `'auto'` (default) | `'none'` | Number | 
Distributes components based on the available empty space around them. Options are as follows:

*   `initial`: The item is sized according to its width and height properties. It shrinks to its minimum size to fit the container, but does not grow to absorb any extra free space in the flex container. 
*   `auto`: The item is sized according to its width and height properties, but grows to absorb any extra free space in the flex container, and shrinks to its minimum size to fit the container.
*   `none`: The item is sized according to its width and height properties. It is fully inflexible: it neither shrinks nor grows in relation to the flex container.
*   number: tells a component to fill all available space, shared evenly amongst other components with the same parent. The larger the flex given, the higher the ratio of space a component will take compared to its siblings.

 |

You only need to use `Box` as a wrapper for components that you want to adjust. For example, if you wrap one component in a `Box` with a `flex` value, only that one component will have its width adjusted based on the available empty space.

![ui-extension-components-box-flex](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-box-flex.png?width=523&height=112&name=ui-extension-components-box-flex.png)

<Flex direction={'row'} justify={'start'} gap={'small'} > <Box flex={1}> <Tile>Tile 1</Tile> </Box> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/box#usage-examples)
-----------------------------------------------------------------------------------------------

### Using numbers in flex[](https://developers.hubspot.com/docs/platform/ui-components/box#using-numbers-in-flex)

Use the `flex` prop in a `Box` component to assign any extra spacing to components using either a default value (e.g. `auto`) or a specific number. When using a number, the components will be distributed based on the ratio of their assigned numbers. This also means that, when assigning a `flex` value for only one `Box`, you can use any number, because any number by itself will result in all available space being assigned to that `Box`.

For example, the four tiles below take up an increasing amount of space based on their `flex` values.

![ui-extrensions-layout-box](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-box.png?width=522&height=226&name=ui-extrensions-layout-box.png)

<Flex direction={'row'} justify={'start'} gap={'small'} > <Box flex={1}> <Tile>flex = 1</Tile> </Box> <Box flex={2}> <Tile>flex = 2</Tile> </Box> <Box flex={3}> <Tile>flex = 3</Tile> </Box> <Box flex={4}> <Tile>flex = 4</Tile> </Box> </Flex>

### Using alignSelf[](https://developers.hubspot.com/docs/platform/ui-components/box#using-alignself)

Use the `alignSelf` prop to override alignment rules for individual `Box` components. 

![ui-extensions-layout-box-alignself](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-layout-box-alignself.png?width=525&height=310&name=ui-extensions-layout-box-alignself.png) 

<Flex direction={'column'} gap={'small'} align={'start'} > <Box alignSelf={'end'}> <Tile>Top right</Tile> </Box> <Box alignSelf={'center'}> <Tile>Middle</Tile> </Box> <Tile>Bottom left</Tile> </Flex>

Related components[](https://developers.hubspot.com/docs/platform/ui-components/box#related-components)
-------------------------------------------------------------------------------------------------------

*   [Flex](https://developers.hubspot.com/docs/platform/ui-components/flex)
*   [Divider](https://developers.hubspot.com/docs/platform/ui-components/divider)
*   [Tile](https://developers.hubspot.com/docs/platform/ui-components/tile)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/box#page-feedback)
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