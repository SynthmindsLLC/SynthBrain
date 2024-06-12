---
Please provide me with the context for the mission. 

To help me write a compelling mission statement, I need to know: "* **What is the purpose of the mission?** What are you trying to achieve?"
* **Who is the target audience?**  Who are you trying to reach with this mission?
* **What are the values and principles that guide the mission?** What beliefs and ideals are central to your work?
* **What are the specific goals or objectives of the mission?** What are you aiming to accomplish?

Once I have this information, I can create a strong and effective mission statement for you.
---

Flex | UI components (BETA)
===========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Flex` component renders an empty `div` container set to `display=flex`. When wrapped around other components, it enables those child components to be arranged using props. `Flex` can contain other `Flex` or `Box` components.

 To see an example of how `Flex` and `Box` can be used for layout, check out HubSpot's [Manage layouts: Flex and Box sample project](/docs/platform/sample-projects#managing-layouts-flex-and-box).

![ui-extension-components-flex-child](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-flex-child.png?width=521&height=207&name=ui-extension-components-flex-child.png)

import { Flex, Tile } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Flex direction={'row'} justify={'end'} wrap={'wrap'} gap={'small'} > <Tile>Left</Tile> <Tile>Right</Tile> <Flex direction={'column'}> <Tile>Bottom</Tile> </Flex> </Flex> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `direction` | `'row'` (default) | `'column'` | Arranges the components horizontally or vertically by setting the main axis. |
| `justify` | `'start'` (default) | `'center'` | `'end'` | `'around'` | `'between'` | Distributes components along the main axis using the available free space. |
| `align` | `'start'` | `'center'` | `'end'` | `'baseline'` | `'stretch'` (default) | Distributes components along the cross-axis using the available free space. |
| `alignSelf` | `'start'` | `'center'` | `'end'` | `'baseline'` | `'stretch'` | Distributes a child component along the cross-axis using the available free space. Use this prop for nested `Flex` and `Box` components to align them differently from other child components in the `Flex` group. |
| `wrap` | `'wrap'` | `'nowrap'` (default) | Whether components will wrap rather than trying to fit on one line. |
| `gap` | `'flush'` (default) | `'extra-small'` | `'small'` | `'medium'` | `'large'` | `'extra-large'` | Sets the spacing between components. |

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/flex#usage-examples)
------------------------------------------------------------------------------------------------

### Horizontal layout[](https://developers.hubspot.com/docs/platform/ui-components/flex#horizontal-layout)

To arrange components horizontally, set `direction` to `row`. Then, use `justify` to configure the horizontal distribution. By default, components will stretch across the container if `justify` is not specified.

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; border: 0; height: 908.875px;"><tbody><tr style="height: 111.703px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 111.703px;"><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=500&amp;height=106&amp;name=flex-tiles-justify-between.png" alt="flex-tiles-justify-between" loading="lazy" width="500" height="106" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=250&amp;height=53&amp;name=flex-tiles-justify-between.png 250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=500&amp;height=106&amp;name=flex-tiles-justify-between.png 500w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=750&amp;height=159&amp;name=flex-tiles-justify-between.png 750w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=1000&amp;height=212&amp;name=flex-tiles-justify-between.png 1000w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=1250&amp;height=265&amp;name=flex-tiles-justify-between.png 1250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=1500&amp;height=318&amp;name=flex-tiles-justify-between.png 1500w" sizes="(max-width: 500px) 100vw, 500px"></td></tr><tr style="height: 29px;"><td style="border: 0; width: 99.8927%; padding: 4px; text-align: center; height: 29px;"><code>justify={'between'}</code></td></tr><tr style="height: 171.672px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 171.672px;"><p>&nbsp;</p><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=519&amp;height=108&amp;name=flex-tiles-justify-around.png" alt="flex-tiles-justify-around" loading="lazy" width="519" height="108" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=260&amp;height=54&amp;name=flex-tiles-justify-around.png 260w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=519&amp;height=108&amp;name=flex-tiles-justify-around.png 519w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=779&amp;height=162&amp;name=flex-tiles-justify-around.png 779w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=1038&amp;height=216&amp;name=flex-tiles-justify-around.png 1038w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=1298&amp;height=270&amp;name=flex-tiles-justify-around.png 1298w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=1557&amp;height=324&amp;name=flex-tiles-justify-around.png 1557w" sizes="(max-width: 519px) 100vw, 519px"></p></td></tr><tr style="height: 10px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 10px; text-align: center;"><code>justify={'around'}</code></td></tr><tr style="height: 162.156px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 162.156px;"><p>&nbsp;</p><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=500&amp;height=105&amp;name=ui-extrensions-layout-tile-justify-start.png" alt="ui-extrensions-layout-tile-justify-start" width="500" loading="lazy" height="105" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=250&amp;height=53&amp;name=ui-extrensions-layout-tile-justify-start.png 250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=500&amp;height=105&amp;name=ui-extrensions-layout-tile-justify-start.png 500w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=750&amp;height=158&amp;name=ui-extrensions-layout-tile-justify-start.png 750w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=1000&amp;height=210&amp;name=ui-extrensions-layout-tile-justify-start.png 1000w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=1250&amp;height=263&amp;name=ui-extrensions-layout-tile-justify-start.png 1250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=1500&amp;height=315&amp;name=ui-extrensions-layout-tile-justify-start.png 1500w" sizes="(max-width: 500px) 100vw, 500px"></p></td></tr><tr style="height: 29px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 29px; text-align: center;"><code>justify={'start'}</code></td></tr><tr style="height: 167.672px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 167.672px;"><p>&nbsp;</p><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=533&amp;height=104&amp;name=ui-extrensions-layout-tile-justify-center.png" alt="ui-extrensions-layout-tile-justify-center" loading="lazy" width="533" height="104" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=267&amp;height=52&amp;name=ui-extrensions-layout-tile-justify-center.png 267w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=533&amp;height=104&amp;name=ui-extrensions-layout-tile-justify-center.png 533w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=800&amp;height=156&amp;name=ui-extrensions-layout-tile-justify-center.png 800w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=1066&amp;height=208&amp;name=ui-extrensions-layout-tile-justify-center.png 1066w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=1333&amp;height=260&amp;name=ui-extrensions-layout-tile-justify-center.png 1333w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=1599&amp;height=312&amp;name=ui-extrensions-layout-tile-justify-center.png 1599w" sizes="(max-width: 533px) 100vw, 533px"></p></td></tr><tr style="height: 29px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 29px; text-align: center;"><code>justify={'center'}</code></td></tr><tr style="height: 169.672px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 169.672px;"><p>&nbsp;</p><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=533&amp;height=106&amp;name=ui-extrensions-layout-tile-justify-end.png" alt="ui-extrensions-layout-tile-justify-end" loading="lazy" width="533" height="106" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=267&amp;height=53&amp;name=ui-extrensions-layout-tile-justify-end.png 267w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=533&amp;height=106&amp;name=ui-extrensions-layout-tile-justify-end.png 533w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=800&amp;height=159&amp;name=ui-extrensions-layout-tile-justify-end.png 800w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=1066&amp;height=212&amp;name=ui-extrensions-layout-tile-justify-end.png 1066w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=1333&amp;height=265&amp;name=ui-extrensions-layout-tile-justify-end.png 1333w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=1599&amp;height=318&amp;name=ui-extrensions-layout-tile-justify-end.png 1599w" sizes="(max-width: 533px) 100vw, 533px"></p></td></tr><tr style="height: 29px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 29px; text-align: center;"><code>justify={'end'}</code></td></tr></tbody></table> 

### Wrap[](https://developers.hubspot.com/docs/platform/ui-components/flex#wrap)

By default, components in a `row` will be arranged on one line when possible. Use the `wrap` prop to wrap components onto new lines when needed.

![ui-extrensions-layout-tile-row-wrap](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-row-wrap.png)

<Flex direction={'row'} justify={'between'} wrap={'wrap'} gap={'medium'} > <Tile>One</Tile> <Tile>Two</Tile> <Tile>Three</Tile> <Tile>Four</Tile> <Tile>Five</Tile> <Tile>Six</Tile> <Tile>Seven</Tile> <Tile>Eight</Tile> </Flex>

### Vertical layout[](https://developers.hubspot.com/docs/platform/ui-components/flex#vertical-layout)

To arrange components vertically, set direction to `column`, then use the `align` prop to distribute them. By default, components will stretch across the extension container width when `align` is not specified. 

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; border: 0; height: 908.875px;"><tbody><tr style="height: 111.703px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 111.703px;"><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=500&amp;height=268&amp;name=ui-extrensions-layout-tile-column-align-start.png" alt="ui-extrensions-layout-tile-column-align-start" loading="lazy" width="500" height="268" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=250&amp;height=134&amp;name=ui-extrensions-layout-tile-column-align-start.png 250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=500&amp;height=268&amp;name=ui-extrensions-layout-tile-column-align-start.png 500w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=750&amp;height=402&amp;name=ui-extrensions-layout-tile-column-align-start.png 750w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=1000&amp;height=536&amp;name=ui-extrensions-layout-tile-column-align-start.png 1000w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=1250&amp;height=670&amp;name=ui-extrensions-layout-tile-column-align-start.png 1250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=1500&amp;height=804&amp;name=ui-extrensions-layout-tile-column-align-start.png 1500w" sizes="(max-width: 500px) 100vw, 500px"></td></tr><tr style="height: 29px;"><td style="border: 0; width: 99.8927%; padding: 4px; text-align: center; height: 29px;"><code>align={'start'}</code></td></tr><tr style="height: 171.672px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 171.672px;"><p>&nbsp;</p><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=500&amp;height=266&amp;name=ui-extrensions-layout-tile-column-align-center.png" alt="ui-extrensions-layout-tile-column-align-center" loading="lazy" width="500" height="266" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=250&amp;height=133&amp;name=ui-extrensions-layout-tile-column-align-center.png 250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=500&amp;height=266&amp;name=ui-extrensions-layout-tile-column-align-center.png 500w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=750&amp;height=399&amp;name=ui-extrensions-layout-tile-column-align-center.png 750w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=1000&amp;height=532&amp;name=ui-extrensions-layout-tile-column-align-center.png 1000w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=1250&amp;height=665&amp;name=ui-extrensions-layout-tile-column-align-center.png 1250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=1500&amp;height=798&amp;name=ui-extrensions-layout-tile-column-align-center.png 1500w" sizes="(max-width: 500px) 100vw, 500px"></p></td></tr><tr style="height: 10px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 10px; text-align: center;"><code>align={'center'}</code></td></tr><tr style="height: 162.156px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 162.156px;"><p><img src="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=500&amp;height=262&amp;name=ui-extrensions-layout-tile-column-align-end.png" alt="ui-extrensions-layout-tile-column-align-end" loading="lazy" width="500" height="262" srcset="https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=250&amp;height=131&amp;name=ui-extrensions-layout-tile-column-align-end.png 250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=500&amp;height=262&amp;name=ui-extrensions-layout-tile-column-align-end.png 500w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=750&amp;height=393&amp;name=ui-extrensions-layout-tile-column-align-end.png 750w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=1000&amp;height=524&amp;name=ui-extrensions-layout-tile-column-align-end.png 1000w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=1250&amp;height=655&amp;name=ui-extrensions-layout-tile-column-align-end.png 1250w, https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=1500&amp;height=786&amp;name=ui-extrensions-layout-tile-column-align-end.png 1500w" sizes="(max-width: 500px) 100vw, 500px"></p></td></tr><tr style="height: 29px;"><td style="border: 0; width: 99.8927%; padding: 4px; height: 29px; text-align: center;"><code>align={'end'}</code></td></tr></tbody></table>

### Spacing[](https://developers.hubspot.com/docs/platform/ui-components/flex#spacing)

In the `Flex` component, you can use the `gap` prop to apply even spacing between the tiles. This prop will apply spacing equally for both `row` and `column` directions.

![flex-tiles-gap](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-gap.png?width=528&height=701&name=flex-tiles-gap.png)

<Flex direction={'row'} justify={'start'} gap={'flush' | 'extra-small' | 'small' | 'medium' | 'large' | 'extra-large'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

### Using Flex in Flex[](https://developers.hubspot.com/docs/platform/ui-components/flex#using-flex-in-flex)

You can wrap child `Flex` components with `Flex` to set more specific rules for individual components. A child `Flex` component will not inherit props specified in the parent `Flex` component, so you'll need to repeat any props you've previously defined to maintain them. 

![ui-extension-components-flex-child](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-flex-child.png?width=521&height=207&name=ui-extension-components-flex-child.png) 

<Flex direction={'row'} justify={'end'} wrap={'wrap'} gap={'small'} > <Tile>Left</Tile> <Tile>Right</Tile> <Flex direction={'column'}> <Tile>Bottom</Tile> </Flex> </Flex>

Related components[](https://developers.hubspot.com/docs/platform/ui-components/flex#related-components)
--------------------------------------------------------------------------------------------------------

*   [Tile](https://developers.hubspot.com/docs/platform/ui-components/tile)
*   [Box](https://developers.hubspot.com/docs/platform/ui-components/box)
*   [Divider](https://developers.hubspot.com/docs/platform/ui-components/divider)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/flex#page-feedback)
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