Image | UI components (BETA)
============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Image` component renders an image. Use this component to add a logo or other visual brand identity asset, or to accentuate other content in the extension.

Images cannot exceed the width of the extension's container at various screen sizes, and values beyond that maximum width will not be applied to the image.

![ui-extension-image-component](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-image-component.png?width=527&height=464&name=ui-extension-image-component.png)

import { Image } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Image alt="A picture of a welcome sign" src="https://picsum.photos/id/237/200/300" href="https://picsum.photos/id/237" onClick={() => { console.log('Someone clicked the image!'); }} width={200} /> ); };

| **Prop** | **Type** | **Description** |
| --- | --- | --- |
| `src`  Required |  String | The URL of the image to display. |
| `alt` |  String | The alt text for the image, similar to the `alt` attribute for the HTML [img tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attributes). |
| `href` |  String | When provided, the URL that will open when the image is clicked. |
| `onClick` |  Function | A function that will be called when the image is clicked. This function will receive no arguments and any returned values will be ignored. |
| `width` | Number | The pixel width of the image. |
| `height` | Number | The pixel height of the image. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/image#related-components)
---------------------------------------------------------------------------------------------------------

*   [Link](https://developers.hubspot.com/docs/platform/ui-components/link)
*   [Text](https://developers.hubspot.com/docs/platform/ui-components/text)
*   [Heading](https://developers.hubspot.com/docs/platform/ui-components/heading)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/image#page-feedback)
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