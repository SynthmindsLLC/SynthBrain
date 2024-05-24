CrmStatistics | UI components (BETA)
====================================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `CrmStatistics` component renders data summaries calculated from the currently displaying CRM record's associations. For example, you can use this component to display data such as:

*   The average revenue of all of a contact’s associated companies.
*   The total number of times that a company has been contacted based on all of their associated tickets.
*   The maximum number of days to close from all of a company's associated deals.

To render data, you'll specify the properties you want to read from the associated records along with the type of calculation to perform on the property values. For each property, you can also include filters to narrow down the records that are included in the calculation.

![ui-extension-component-crm-statistics](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/ui-extension-component-crm-statistics.png)

import { CrmStatistics } from '@hubspot/ui-extensions/crm'; const Extension = () => { return ( <CrmStatistics objectTypeId="0-3" statistics={\[ { label: 'Average Deal Amount', statisticType: 'AVG', propertyName: 'amount', }, { label: '50th Percentile Deal Amount', statisticType: 'PERCENTILES', propertyName: 'amount', percentile: 50, }, { label: 'Time Left for Most Important Upcoming Deal', statisticType: 'MIN', propertyName: 'days\_to\_close', // The filters below narrow the fetched // deals by the following criteria: // - Amount must be >= 10,000 // - Deal must not be closed filterGroups: \[ { filters: \[ { operator: 'GTE', property: 'amount', value: 10000, }, { operator: 'EQ', property: 'hs\_is\_closed', value: "false", }, \], }, \], }, \]} /> ); };

| Prop | Type | Description |
| --- | --- | --- |
| `objectTypeId` Required | String | The numeric ID of the type of object to fetch statistics about (e.g., `0-1` for contacts). See [complete list](https://developers.hubspot.com/docs/api/crm/understanding-the-crm#object-type-id) of object IDs. |
| `statistics` Required | Array | An array of objects that define each statistic to fetch. Supports the following fields:
*   `label`
*   `propertyName`
*   `statisticType`
*   `filterGroups`

[Learn more about these fields below](#specifying-statistics-data). |

Specifying statistics data[](https://developers.hubspot.com/docs/platform/ui-components/crmstatistics#specifying-statistics-data)
---------------------------------------------------------------------------------------------------------------------------------

Using the `statistics` prop, you'll define the data that you want the component to display. Data is fetched from CRM properties, and is calculated based on the specified `statisticType`. You'll include an object for each statistic that you want to fetch. You can also optionally specify `filterGroups` to further refine the data.

Below are the supported fields for objects in the `statistics` array.

| Field | Type | Description |
| --- | --- | --- |
| `label` Required | String | The label that displays above the statistic. |
| `propertyName` Required | String | The name of the property to fetch data from. Must be a number, date, or datetime property. Requesting any other type of property will result in the statistic displaying `--` for its value. |
| `statisticType` Required | String | The type of statistic to request. Supported values include:
*   `SUM`: the sum of the values of the specified property.
*   `AVG`: the average of the values of the specified property.
*   `MIN`: the smallest value of the specified property.
*   `MAX`: the largest value of the specified property.
*   `COUNT`: the number of CRM records with a value for the specified property.
*   `DISTINCT_APPROX`: an approximate count of distinct values for the specified property.
*   `PERCENTILES`: the property value at which a certain percentage of observed values occur.

 |
| `filterGroups` | String | An optional field for further refining the values that are included in the statistic. Up to three filter group objects may be specified in this array, and you can include up to three filters in each item. Exceeding these limits will result in the statistic showing -- for its value. Filters are structured the same way as filters in the [CRM search API](/docs/api/crm/search#filter-search-results). |
| `percentiles` | Number | When `statisticType` is `PERCENTILES`, this field is required. Specifies the percentile to display. Must be an integer from 0-100, inclusive. |

Related components[](https://developers.hubspot.com/docs/platform/ui-components/crmstatistics#related-components)
-----------------------------------------------------------------------------------------------------------------

*   [CrmReport](https://developers.hubspot.com/docs/platform/ui-components/crmreport)
*   [CrmAssociationTable](https://developers.hubspot.com/docs/platform/ui-components/crmassociationtable)
*   [CrmAssociationPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmassociationpropertylist)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/crmstatistics#page-feedback)
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