Link | UI components (BETA)
===========================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Link` component renders a clickable hyperlink. Use links to direct users to a web page, another part of the HubSpot app, or use them as buttons.

![design-guidelines-link](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-link.png?width=500&height=166&name=design-guidelines-link.png)

1.  **Link text:** text that describes where the link leads.
2.  **External link** **icon**: indicates that the link will lead to a page outside of the HubSpot app.

import { Link } from '@hubspot/ui-extensions'; const Extension = () => { return <Link href="https://app.hubspot.com/">HubSpot</Link>; };

| Prop | Type | Description |
| --- | --- | --- |
| `href`  Required | String | The URL that will open on click. Links to pages in the HubSpot account will open in the same account, while non-HubSpot links will open in a new tab. |
| `variant` | `'primary'` (default) | `'light'` | `'dark'` | `'destructive'` | The color of the link. See the [variants section](#variants) for more information. |
| `onClick` | `() => void` | A function that is invoked when the link is clicked. The function receives no arguments and its return value is ignored. |
| `preventDefault` | Boolean | When set to `true`, `event.preventDefault()` will be invoked before the `onClick` function is called, preventing automatic navigation to the href URL. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/link#variants)
------------------------------------------------------------------------------------

Using the `variant` prop, you can set the following styling:

*   `primary`: the default blue (`#0091ae`).  
    ![design-guidelines-links_4](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_4.png?width=206&height=37&name=design-guidelines-links_4.png) 
*   `light`: a white link that turns to a lighter shade of blue on hover (`#7fd1de`).  
    ![design-guidelines-links_3](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_3.png?width=206&height=34&name=design-guidelines-links_3.png)
*   `dark`: a darker shade of blue (`#33475b`).  
    ![design-guidelines-links_2](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_2.png?width=206&height=38&name=design-guidelines-links_2.png)  
    
*   `destructive`: a red link (`#f2545b`).  
    ![design-guidelines-links_1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/design-guidelines-links_1.png?width=206&height=37&name=design-guidelines-links_1.png)

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/link#usage-examples)
------------------------------------------------------------------------------------------------

*   Use the default `primary` variant when you want to link to another page or contact record in HubSpot.
*   Use the `light` variant when you want to include a link on a dark background.
*   Use the `dark` variant to include a link in an alert.
*   Use the `destructive` variant when the link results in an action that can't be undone by the user, such as deleting contact property information.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/link#guidelines)
----------------------------------------------------------------------------------------

*   **DO:** space out links so that users can tell when they'll be navigation to a different place.
*   **DO:** make link text concise and contextual.
*   **DO:** use the `destructive` variant sparingly and only when the action can't be undone.
*   **DON'T:** crowd multiple links together.
*   **DON'T:** use the `dark` variant outside of alerts.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/link#related-components)
--------------------------------------------------------------------------------------------------------

*   [Heading](https://developers.hubspot.com/docs/platform/ui-components/heading)
*   [Text](https://developers.hubspot.com/docs/platform/ui-components/text)
*   [Image](https://developers.hubspot.com/docs/platform/ui-components/image)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/link#page-feedback)
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