List | UI components (BETA)
===========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `List` component renders a list of items. Each item in `List` will be wrapped in `<li>` tags. A list can be styled as inline, ordered, or unordered with the `variant` prop.

![ui-components-list-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-list-example.png?width=241&height=111&name=ui-components-list-example.png)

import { List } from '@hubspot/ui-extensions'; const Extension() { return ( <List variant="unordered-styled"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `variant` | `'unordered'` (default) | `'unordered-styled'` | `'ordered'` | `'ordered-styled'` | `'inline'` | `'inline-divided'` | The type of list to render. See [variants section](#variants) below for examples. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/list#variants)
------------------------------------------------------------------------------------

By default, lists will be configured as vertically stacked list items without bullets. To customize the styling, use the `variant` prop, as shown below.

To create a bulleted unordered list:

![ui-components-list-variants_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-list-variants_2.png?width=373&height=143&name=ui-components-list-variants_2.png)

<List variant="unordered-styled"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List>

To create a numbered list without styling:

![ui-components-list-variants_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-list-variants_3.png?width=373&height=133&name=ui-components-list-variants_3.png)

<List variant="ordered"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List>

To create a numbered list with styling:

![ui-components-list-variants_4](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-list-variants_4.png?width=373&height=144&name=ui-components-list-variants_4.png)

<List variant="ordered-styled"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List>

To stack list items horizontally:

![ui-components-list-variants_5](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-list-variants_5.png?width=373&height=84&name=ui-components-list-variants_5.png)

<List variant="inline"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List>

To stack list items horizontally with a divider between each item:

![ui-components-list-variants_6](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-components-list-variants_6.png?width=373&height=94&name=ui-components-list-variants_6.png)

<List variant="inline-divided"> <Link href="www.hubspot.com">List item 1</Link> <Link href="www.developers.hubspot.com">List item 2</Link> <Link href="www.knowledge.hubspot.com">List item 3</Link> </List>

Related components[](https://developers.hubspot.com/docs/platform/ui-components/list#related-components)
--------------------------------------------------------------------------------------------------------

*   [Text](https://developers.hubspot.com/docs/platform/ui-components/text)
*   [Accordion](https://developers.hubspot.com/docs/platform/ui-components/accordion)
*   [DescriptionList](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/list#page-feedback)
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