Text | UI components (BETA)
===========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Text` component renders text with formatting options.

![text-component-example](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/text-component-example.png?width=292&height=132&name=text-component-example.png)

import { Text } from '@hubspot/ui-extensions'; const Extension = () => { return ( <> <Text truncate={{ tooltipText:'string', maxWidth: 68 }}>Truncated text</Text> <Text>Plain text</Text> <Text format={{ fontWeight: 'bold' }}>Bold</Text> <Text format={{ italic: true }}>Italics</Text> <Text format={{ fontWeight: 'bold', italic: true }}> Bold and Italic text </Text> <Text format={{ lineDecoration: 'strikethrough' }}> Strikethrough Text </Text> <Text variant="microcopy"> Microcopy text <Text inline={true} format={{ fontWeight: 'bold' }}> with inner bold </Text> </Text> </> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `format` | Object | Text formatting options, which include:
*   `{ fontWeight: 'bold' }`
*   `{ fontWeight: 'demibold' }`
*   `{ italic: true }`
*   `{ lineDecoration: 'strikethrough' }`
*   `{ lineDecoration: 'underline' }`

See the [variants section](#variants) for more information.

 |
| `variant` | `'bodytext'` (default) | `'microcopy'` | The style of text to display. See the [variants section](#variants) for more information. |
| `inline` | Boolean | When set to `true`, will insert text without breaking the line. Default is `false`. |
| `truncate` | Boolean | object | 

Truncates long strings to a single line. If the full string doesn't fit on one line, the excess text will display in a tooltip on hover.

*   `false` (default): text is not truncated.
*   `true`: truncates text to a single line. Full text will display in a tooltip on hover.

Alternatively, set this prop to one of the following objects to specify truncate options:

*   `{tooltipText: 'string'}`: truncates the string and sets the contents of the tooltip.
*   `{maxWidth: number}`: sets the width of the line in pixels.

 |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/text#variants)
------------------------------------------------------------------------------------

Using the `format` prop, you can style text with a number of options:

*   `{fontWeight: 'bold'}`: sets the text to bold.
*   `{fontWeight: 'demibold'}`: sets the text to a lighter bold.
*   `{italic: true}`: sets the text to italics.
*   `{lineDecoration: 'strikethrough'}`: adds a strikethrough to the text.
*   `{lineDecoration: 'underline'}`: underlines the text.
*   `<Text inline={true}>`: enables you to set text styling within the same line by adding more text without breaking the line if possible. Line will still break when text content would extend past the boundaries of its container. For example: `<Text>Text <Text inline={true} format={{fontWeight: 'bold'}}> with inner bold.</Text>`.

![design-guidelines-text](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-text.jpg)

You can also control text size with the `variant` prop.

*   `variant="bodytext"` (default)  
    ![design-guidelines-text-size_1](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-text-size_1.png)
*   `variant="microcopy"`  
    ![design-guidelines-text-size_2](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-guidelines-text-size_2.png)

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/text#usage-examples)
------------------------------------------------------------------------------------------------

*   Use body text when you want to display a summary of the last call with a contact.
*   Use microcopy to include an explanation of a displayed status on a contact record.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/text#guidelines)
----------------------------------------------------------------------------------------

*   **DO:** use text with clear messaging.
*   **DO:** use text formatting thoughtfully. For example, don't bold all of the text that can be seen. Instead, only bold key words and phrases for easier scanning.
*   **DON'T:** use the text component for the primary textual information on a card. Instead, consider using the [Heading component](/docs/platform/ui-components/heading).
*   **DON'T:** use underline formatting for text that's next to a hyperlink, as it will also look clickable.
*   **DON'T:** use microcopy for important or critical information. Instead, consider whether an [Alert component](/docs/platform/ui-components/alert) would fit better.
*   **DON'T:** use text components in place of headers, alerts, and errors.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/text#related-components)
--------------------------------------------------------------------------------------------------------

*   [Heading](https://developers.hubspot.com/docs/platform/ui-components/heading)
*   [Link](https://developers.hubspot.com/docs/platform/ui-components/link)
*   [List](https://developers.hubspot.com/docs/platform/ui-components/list)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/text#page-feedback)
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