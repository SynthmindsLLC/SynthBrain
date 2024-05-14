DateInput | UI components (BETA)
================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `DateInput` component renders an input field where a user can select a date.

![ui-extension-components-date-input](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/ui-extension-components-date-input.png?width=580&height=362&name=ui-extension-components-date-input.png)

import { Flex, DateInput } from '@hubspot/ui-extensions'; function RemoteApp() { const \[dateValue, setDateValue\] = useState(null); return ( <Flex direction="column"> <DateInput label="Appointment Date Partially Controlled" name="date" onChange={(value) => { setDateValue(value); }} value={dateValue} format="ll" /> <DateInput label="Appointment Date Uncontrolled" name="appointment-date" format="LL" /> </Flex> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `name` Required | String | The input's unique identifier. |
| `label` Required | String | The text that displays above the input. |
| `value` | Object | The value of the input. Must include the year, month, and day:  
`{ year: number;``month: number;``date: number }`
*   `year`: the four-digit year (e.g., `2023`).
*   `month`: starting at `0`, the number of the month (e.g., `0` = January, `11` = December).
*   `date`: the number of the day (e.g., `1` = the first day of the month).

 |
| `defaultValue` | Object | The default date value. Uses the same format as the `value` field. |
| `required` | Boolean | When set to `true`, displays a required field indicator. |
| `tooltip` | String | The text that displays in a tooltip next to the label. |
| `readOnly` | Boolean | When set to `true`, the checkbox cannot be selected. |
| `description` | String | Text that describes the field's purpose. |
| `error` | Boolean | When set to `true`, `validationMessage` is displayed as an error message if provided. The input will also render its error state to let the user know there's an error. If left `false` (default), `validationMessage` is displayed as a success message.  
  
 |
| `validationMessage` | String | The text to display if the input has an error. |
| `min` | Object | Sets the earliest valid date available using the following format:  
`{ year: number;``month: number;``date: number }` |
| `max` | Object | A Sets the latest valid date available using the following format:  
`{ year: number;``month: number;``date: number }` |
| `minValidationMessage` | String | Sets the message that users will see when they hover over dates before the min date. |
| `maxValidationMessage` | String | Sets the message that users will see when the hover over dates after the max date. |
| `format` | `'short'` (default) | `'long'` | `'medium'` | `'standard'` | `'YYYY-MM-DD'` | `L` | `LL` | `ll` | The date format.  

*   `short`: 09/04/1986
*   `long`: September 4, 1986
*   `medium`: Sep 4, 1986
*   `standard`: 1986-09-04
*   `YYYY-MM-DD`: 1986-09-04
*   `L`: 09/04/1986
*   `LL`: September 4, 1986
*   `ll`: Sep 4, 1986

 |
| `clearButtonLabel` | String | Sets the label of the button that clears the date. |
| `todayButtonLabel` | String | Sets the label of the button that inserts today's date. |
| `timezone` | `'userTz'` (default) | `'portalTz'` | Sets the timezone that the component will user to calculate valid dates.

*   `userTz` (default): the user's time zone.
*   `portalTz`: the portal's default time zone.

 |
| `onChange` | (checked: boolean, value: string) => void; | A callback function that is invoked when the value is committed. Currently, this occurs on `onBlur` of the input and when the user submits the form. |
| `onBlur` | (value: DateInputEventsPayload) => void | A function that is called and passes the value when the field loses focus. |
| `onFocus` | (value: DateInputEventsPayload) => void | A function that is called and passed the value when the field gets focused. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/dateinput#related-components)
-------------------------------------------------------------------------------------------------------------

*   [Form](https://developers.hubspot.com/docs/platform/ui-components/form)
*   [MultiSelect](https://developers.hubspot.com/docs/platform/ui-components/multiselect)
*   [NumberInput](https://developers.hubspot.com/docs/platform/ui-components/numberinput)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/dateinput#page-feedback)
---------------------------------------------------------------------------------------------------------

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