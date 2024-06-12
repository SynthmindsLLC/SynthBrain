---
Please provide me with more context! To help me write a compelling mission statement, I need to know: "* **What is the subject of the mission?**  Is it for a company, a project, a personal goal, or something else?"
* **What are the key values or goals?** What is the purpose or desired outcome? 
* **Who is the target audience?** Who will be impacted by this mission?

For example, you could tell me: * "I need a mission statement for a new startup that develops sustainable food solutions."
* "I'm trying to write a mission statement for my personal goal of becoming a published author."
* "We need a mission statement for our non-profit organization that helps homeless veterans."

Once I have this information, I can help you craft a strong and impactful mission statement!
---

Manage UI extension layout (BETA)
=================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

By default, UI extension components will arrange themselves based on their content, order, and any layout-related props included with the component, such as the `width` prop for images. But you can further configure your extension's layout using the `Flex` and `Box` components, which are based on the [CSS flexbox layout](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). 

`Flex` and `Box` are both used as wrappers around other components. `Flex` can be used on its own, while `Box` can be used as a wrapper around `Flex` child items to fine tune spacing of individual components. Below, learn more about each component along with usage examples.

Check out HubSpot's [Managing layout: Flex and Box sample project](/docs/platform/sample-projects#managing-layouts-flex-and-box) to view a full example of using `Flex` and `Box`.

Flex[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#flex)
------------------------------------------------------------------------------------

The [`Flex` component](/docs/platform/ui-extension-components#layout-flex) renders an empty `div` container set to `display=flex`. When wrapped around other components, this enables those child components to be arranged using props.

Below are the available `Flex` props. To review all `Flex` prop definitions, check out the [components reference guide](/docs/platform/ui-extension-components#layout-flex).

| Prop | Values | Description |
| --- | --- | --- |
| `direction` | 
*   `row` (default)
*   `column`

 | 

Arranges components horizontally or vertically by setting the main axis.

 |
| `justify` | 

*   `center`
*   `start` (default)
*   `end`
*   `around`
*   `between`

 | 

Distributes components along the main axis using the available free space. 

 |
| `align` | 

*   `start`
*   `center`
*   `baseline`
*   `end`
*   `stretch` (default)

 | 

Distributes components along the cross-axis using the available free space.

 |
| `alignSelf` | 

*   `start`
*   `center`
*   `baseline`
*   `end`
*   `stretch`

 | 

Distributes a child component along the cross-axis using the available free space. Use this prop for nested child `Flex` and `Box` components to align them differently from other child components in the `Flex` group.

 |
| `wrap` | 

*   `wrap`
*   `nowrap`

 | 

Whether components will wrap instead of trying to fit on one line.

 |
| `gap` | 

*   `flush` (default)
*   `extra-small`
*   `small`
*   `medium`
*   `large`
*   `extra-large`

 | 

Sets the spacing between components.

 |

Review the examples below to see how the [`Flex` component](/docs/platform/ui-extension-components#flex) can be used to arrange components in various ways.

### Horizontal layout[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#horizontal-layout)

To arrange components horizontally, set `direction` to `row`. Then, use `justify` to configure the horizontal distribution. By default, components will stretch across the container if `justify` is not specified.

To arrange components horizontally and evenly spaced:

![flex-tiles-justify-between](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-between.png?width=500&height=103&name=flex-tiles-justify-between.png)

<Flex direction={'row'} justify={'between'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

  
To arrange components horizontally, evenly spaced, and with equal spacing on the left and right margins:

![flex-tiles-justify-around](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-justify-around.png?width=500&height=104&name=flex-tiles-justify-around.png)

<Flex direction={'row'} justify={'around'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

  
To arrange components horizontally at the end of the extension container:

![ui-extrensions-layout-tile-justify-end](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-end.png?width=500&height=99&name=ui-extrensions-layout-tile-justify-end.png)

<Flex direction={'row'} justify={'end'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

  
To arrange components horizontally at the center of the extension container:

![ui-extrensions-layout-tile-justify-center](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-center.png?width=500&height=98&name=ui-extrensions-layout-tile-justify-center.png)

<Flex direction={'row'} justify={'center'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

  
To arrange components horizontally at the start of the extension container:

![ui-extrensions-layout-tile-justify-start](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-justify-start.png?width=500&height=98&name=ui-extrensions-layout-tile-justify-start.png)

<Flex direction={'row'} justify={'start'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

### Wrap[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#wrap)

By default, components in a `row` will be arranged on one line when possible. Use the `wrap` prop to wrap components onto new lines when needed.

![ui-extrensions-layout-tile-row-wrap](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-row-wrap.png?width=530&height=222&name=ui-extrensions-layout-tile-row-wrap.png)

<Flex direction={'row'} justify={'between'} wrap={'wrap'} gap={'medium'} > <Tile>One</Tile> <Tile>Two</Tile> <Tile>Three</Tile> <Tile>Four</Tile> <Tile>Five</Tile> <Tile>Six</Tile> <Tile>Seven</Tile> <Tile>Eight</Tile> </Flex>

### Vertical layout[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#vertical-layout)

To arrange components vertically, set direction to `column`, then use the `align` prop to distribute them. By default, components will stretch across the extension container width when `align` is not specified.

To arrange components vertically at the start of the extension container:

![ui-extrensions-layout-tile-column-align-start](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-start.png?width=500&height=269&name=ui-extrensions-layout-tile-column-align-start.png)

<Flex direction={'column'} align={'start'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

  
To arrange components vertically at the center of the extension container:

![ui-extrensions-layout-tile-column-align-center](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-center.png?width=500&height=267&name=ui-extrensions-layout-tile-column-align-center.png)

<Flex direction={'column'} align={'center'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

  
To arrange components vertically at the end of the extension container:

![ui-extrensions-layout-tile-column-align-end](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-tile-column-align-end.png?width=500&height=262&name=ui-extrensions-layout-tile-column-align-end.png)

<Flex direction={'column'} align={'end'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

### Spacing[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#spacing)

In the `Flex` component, you can use the `gap` prop to apply even spacing between the tiles. This prop will apply spacing equally for both `row` and `column` directions.

![flex-tiles-gap](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/flex-tiles-gap.png?width=528&height=701&name=flex-tiles-gap.png)

<Flex direction={'row'} justify={'start'} gap={'flush' | 'extra-small' | 'small' | 'medium' | 'large' | 'extra-large'} > <Tile>Tile 1</Tile> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

### Using Flex in Flex[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#using-flex-in-flex)

You can wrap child `Flex` components with `Flex` to set more specific rules for individual components. A child `Flex` component will not inherit props specified in the parent `Flex` component, so you'll need to repeat any props you've previously defined to maintain them. 

![ui-extension-components-flex-child](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-flex-child.png?width=521&height=207&name=ui-extension-components-flex-child.png)

<Flex direction={'row'} justify={'end'} wrap={'wrap'} gap={'small'} > <Tile>Left</Tile> <Tile>Right</Tile> <Flex direction={'column'}> <Tile>Bottom</Tile> </Flex> </Flex>

Box[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#box)
----------------------------------------------------------------------------------

When wrapping components with `Flex`, you can further configure individual component layout by wrapping a child of `Flex` in a [`Box` component](/docs/platform/ui-extension-components#layout-box). 

This component supports the following props. To review all `Box` prop definitions, check out the [components reference guide](/docs/platform/ui-extension-components#layout-box).

| Prop | Values | Description |
| --- | --- | --- |
| `alignSelf` | 
*   `start`
*   `center`
*   `baseline`
*   `end`
*   `stretch`

 | 

Distributes a child component along the cross-axis using the available free space. Use this prop for nested child `Flex` and `Box` components to align them differently from other child components in the `Flex` group.

 |
| `flex` | 

*   number value
*   `initial` (default)
*   `auto`
*   `none`

 | 

Distributes components based on the available empty space around them.

 |

Use the `flex` prop in a `Box` component to assign any extra spacing to components using either a default value (e.g. `auto`) or a specific number. When using a number, the components will be distributed based on the ratio of their assigned numbers.

For example, the four tiles below take up an increasing amount of space based on their `flex` values.

![ui-extrensions-layout-box](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extrensions-layout-box.png?width=522&height=226&name=ui-extrensions-layout-box.png)

<Flex direction={'row'} justify={'start'} gap={'small'} > <Box flex={1}> <Tile>flex = 1</Tile> </Box> <Box flex={2}> <Tile>flex = 2</Tile> </Box> <Box flex={3}> <Tile>flex = 3</Tile> </Box> <Box flex={4}> <Tile>flex = 4</Tile> </Box> </Flex>

When using `Box`, you only need to wrap components that you want to adjust. For example, if you wrap one component in a `Box` with a `flex` value, only that one component will have its width adjusted based on the available empty space.

![ui-extension-components-box-flex](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extension-components-box-flex.png?width=523&height=112&name=ui-extension-components-box-flex.png) 

<Flex direction={'row'} justify={'start'} gap={'small'} > <Box flex={1}> <Tile>Tile 1</Tile> </Box> <Tile>Tile 2</Tile> <Tile>Tile 3</Tile> </Flex>

When setting a `flex` value for only one `Box`, you can use any number. This is because any number on its own will result in all available space being assigned to that one component.

You can also use the `alignSelf` prop to override alignment rules for individual `Box` components. 

![ui-extensions-layout-box-alignself](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-layout-box-alignself.png?width=525&height=310&name=ui-extensions-layout-box-alignself.png) 

<Flex direction={'column'} gap={'small'} align={'start'} > <Box alignSelf={'end'}> <Tile>Top right</Tile> </Box> <Box alignSelf={'center'}> <Tile>Middle</Tile> </Box> <Tile>Bottom left</Tile> </Flex>

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/manage-ui-extension-layout#page-feedback)
------------------------------------------------------------------------------------------------------------

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