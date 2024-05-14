Panel | UI components (BETA)
============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Panel` component renders a panel on the right side of the page and contains other components. The panel can be opened and closed by using `onClick` handles for Button, Link, Tag, and Image components. Learn more about [how to open a panel in your UI extension](#open-or-close-a-panel).

To see an example of incorporating a panel into an extension, check out HubSpot's [Build a multi-step flow sample project](https://developers.hubspot.com/docs/platform/sample-projects#build-a-multi-step-flow).

![panel-example-gif](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/panel-example-gif.gif?width=700&height=595&name=panel-example-gif.gif)

The `Panel` component uses three subcomponents to control its design and content, which follows the general structure below:

*   `<Panel>`: the outermost container. It must be a top-level component. You cannot put a `Panel` inside another component, such as `Flex`.
    *   `<PanelBody>`: the container that wraps the panel's content and makes it scrollable. Include only one `PanelBody` per `Panel`.
        *   `<PanelSection>`: a container that adds padding and bottom margin to provide spacing between content. You can use [Flex](/docs/platform/ui-components/flex) and [Box](/docs/platform/ui-components/box) to further customize content layout.
    *   `<PanelFooter>`: a sticky footer component at the bottom of the panel. Include only one `PanelFooter` per `Panel`.

import { Panel, PanelBody, PanelSection, PanelFooter, Form, Select, Button } from '@hubspot/ui-extensions'; const Extension = () => { return( <> <Panel title="Welcome to my Panel" id="my-panel"> <Form> <PanelBody> <PanelSection> <Select name="test" label="Test" options={\[ {label: 'foo', value: 'foo'}, {label:"bar", value: "bar"}\]} /> </PanelSection> <PanelSection> lorem ipsum... </PanelSection> </PanelBody> <PanelFooter><Button type="submit">Click me</Button></PanelFooter> </Form> </Panel> <Button onClick={(event, reactions) => { reactions.openPanel('my-panel')}}> Open Panel </Button> </> ); };

Below are the props available for `Panel` and `PanelSection`.

Panel props[](https://developers.hubspot.com/docs/platform/ui-components/panel#panel-props)
-------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `id`  Required | String | A unique ID for the panel. |
| `onOpen` | onOpen() => void | A function that will be invoked when the panel has finished opening. |
| `onClose` | onClose() => void | A function that will be invoked when the panel has finished closing. |
| `width` |  `'sm'`, `'small'` (default) | `'md'`, `'medium'`| `'lg'`, `'large'` | The width of the panel. |
| `title` | String | The text that displays at the top of the panel. |
| `variant` | `'modal'` | `'default'` (default) | The panel variant. The `modal` variant includes better screen reader focus on the panel and is recommended for visual and motor accessibility and tab navigation. |
| `aria-label` | String | The panel's accessibility label. |

PanelSection props[](https://developers.hubspot.com/docs/platform/ui-components/panel#panelsection-props)
---------------------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `flush` | Boolean | When set to `true`, the section will have no bottom margin. Default is `false`. |

Open or close a panel[](https://developers.hubspot.com/docs/platform/ui-components/panel#open-or-close-a-panel)
---------------------------------------------------------------------------------------------------------------

The `Panel` component can be opened and closed through an event triggered by an `onClick` event in [Button](/docs/platform/ui-components/button), [Link](/docs/platform/ui-components/link), [Tag](/docs/platform/ui-components/tag), and [Image](/docs/platform/ui-components/image) components. In the `onClick` handlers, two actions are passed in the callback:

*   `ExtensionEvent`: contains information about the actual DOM event created by the user.
*   `reactions`: contains two functions: `openPanel` and `closePanel`.

The example code below shows how to use separate buttons to open and close a panel:

<Panel id="my-panel"> Test </Panel> <Button onClick={(\_\_,reactions) => reactions.openPanel('panel-id')}> Open Panel </Button> <Button onClick={(\_\_,reactions) => reactions.closePanel('panel-id')}> Close Panel </Button>

**Please note:**

*   Only one panel can be open at a time. Opening a panel while another is already open will cause the first panel to close.
*   If your `onClick` function to open the panel is asynchronous, ensure that it returns a promise.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/panel#related-components)
---------------------------------------------------------------------------------------------------------

*   [Box](https://developers.hubspot.com/docs/platform/ui-components/box)

*   [Button](/docs/platform/ui-components/button)
*   [Divider](https://developers.hubspot.com/docs/platform/ui-components/divider)

*   [Link](/docs/platform/ui-components/link)
*   [Image](/docs/platform/ui-components/image)  
    
*   [Tag](/docs/platform/ui-components/tag)
*   [Tile](https://developers.hubspot.com/docs/platform/ui-components/tile)[](https://developers.hubspot.com/docs/platform/ui-components/divider)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/panel#page-feedback)
-----------------------------------------------------------------------------------------------------

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