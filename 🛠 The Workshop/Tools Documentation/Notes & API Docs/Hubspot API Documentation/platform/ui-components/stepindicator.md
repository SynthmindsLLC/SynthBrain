StepIndicator | UI components (BETA)
====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `StepIndicator` component renders an indicator to show the current step of a multi-step process.

![ui-extension-component-stepindicator](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-extension-component-stepindicator.png)

import { StepIndicator, Button } from '@hubspot/ui-extensions'; function Extension() { const \[currentStep, setCurrentStep\] = useState(0); return ( <> <StepIndicator currentStep={currentStep} stepNames={\["First", "Second", "Third"\]} /> <Button onClick={() => setCurrentStep(currentStep - 1)}> Previous </Button> <Button onClick={() => setCurrentStep(currentStep + 1)}> Next </Button> </> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `circleSize` | `'xs'`, `'extra-small'`, |  
`'sm'`, `'small'` (default) |  
`'md'`, `'medium'` |  
`'lg'`, `'large'` |  
`'xl'`, `'extra-large'` | The size of the indicator circles. See the [variants section](#variants) for examples of sizing. |
| `currentStep` | Number | The currently active step. Steps are zero-based, meaning the first step is assigned `0`. |
| `direction` | `'horizontal'` (default) | `'vertical'` | The orientation of the indicator. |
| `stepNames` Required | Array | An array containing the name of each step. |
| `variant` | `'flush'` | `'default'` (default) | `'compact'` | Sets component spacing.
*   `compact`: only shows the title of the currently active step.
*   `flush`: only shows the title of the currently active step and removes left and right margin.

 |
| `onClick` | (stepIndex: number) => void | A function that is invoked when a step in the indicator is clicked. The function receives the current step index as an argument (zero-based). Use this to update the currently active step. |

Variants[](https://developers.hubspot.com/docs/platform/ui-components/stepindicator#variants)
---------------------------------------------------------------------------------------------

By default, the step indicator will be laid out horizontally, but you can use the `direction` prop to set the orientation to `vertical` instead.

![stepindicator-vertical-alignment](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/stepindicator-vertical-alignment.png?width=268&height=243&name=stepindicator-vertical-alignment.png)

In addition, you can set the size of the step circles using the `circleSize` prop, ranging from `'xs'`/`'extra-small'` to `'xl'`/`'extra-large'`.

![stepindicator-circlesize-variations](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/stepindicator-circlesize-variations.png?width=229&height=445&name=stepindicator-circlesize-variations.png)

Related components[](https://developers.hubspot.com/docs/platform/ui-components/stepindicator#related-components)
-----------------------------------------------------------------------------------------------------------------

*   [ProgressBar](https://developers.hubspot.com/docs/platform/ui-components/progressbar)
*   [LoadingSpinner](https://developers.hubspot.com/docs/platform/ui-components/loadingspinner)
*   [Toggle](https://developers.hubspot.com/docs/platform/ui-components/toggle)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/stepindicator#page-feedback)
-------------------------------------------------------------------------------------------------------------

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