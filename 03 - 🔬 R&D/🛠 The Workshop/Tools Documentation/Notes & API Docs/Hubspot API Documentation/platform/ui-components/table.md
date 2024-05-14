Table | UI components (BETA)
============================

APPLICABLE PRODUCTS

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/sales_icon.svg) Sales Hub
    *   Enterprise

*   ![](https://developers.hubspot.com/hubfs/raw_assets/public/developers-website/images/service_icon.svg) Service Hub
    *   Enterprise

The `Table` component renders a table. To format the table, you can use the following subcomponents:

*   `TableHead`: the header section of the table containing column labels.
*   `TableRow`: individual table rows.
*   `TableHeader`: cells containing bolded column labels.
*   `TableBody`: container for the main table contents (rows and cells).
*   `TableCell`: individual cells within the main body.

![design-principes-table-with-pagination](https://developers.hubspot.com/hubfs/Knowledge_Base_2023/design-principes-table-with-pagination.png)

import { Table, TableHead, TableRow, TableHeader, TableBody, TableCell } from '@hubspot/ui-extensions'; const Extension = () => { return ( <Table bordered={true} paginated={true} pageCount="5" > <TableHead> <TableRow> <TableHeader>Name</TableHeader> <TableHeader>Role</TableHeader> </TableRow> </TableHead> <TableBody> <TableRow> <TableCell>Tim Robinson</TableCell> <TableCell>Driver's Ed. Instructor</TableCell> </TableRow> <TableRow> <TableCell>Patti Harrison</TableCell> <TableCell>Tables (vendor)</TableCell> </TableRow> <TableRow> <TableCell>Sam Richardson</TableCell> <TableCell>Show host</TableCell> </TableRow> <TableRow> <TableCell>Ruben Rabasa</TableCell> <TableCell>Car imagineer</TableCell> </TableRow> </TableBody> </Table> ); }

Table props[](https://developers.hubspot.com/docs/platform/ui-components/table#table-props)
-------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `bordered` | Boolean | When set to `false`, the table will not include borders. Default is `true`. |
| `flush` | Boolean | When set to `true`, the table will not include bottom margin. Default is `false`. |
| `paginated` | Boolean | When set to `true`, the table will include pagination navigation. Default is `false`.  
  
See the [paginated tables](#paginated-tables) section for pagination props. |

TableHeader props[](https://developers.hubspot.com/docs/platform/ui-components/table#tableheader-props)
-------------------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `align` | `'center'` | `'left'` | `'right'` | Sets the alignment of a table header. |
| `sortDirection` | `'none'` (default) | `'ascending'` | `'descending'` | `'never'` | A visual indicator of the current direction in which the column is sorted. Does not modify the table data. See the [sortable tables](#sortable-tables) section for more sorting props. |
| `width` | Number | `'min'` | `'max'` | `'auto'` | 
Sets the width of a table header.

*   `min`: the content will only be as wide as required, overflowing if the content is wider than the table. A horizontal scrollbar will appear when there is overflow.
*   `max`: the content will expand to occupy the maximum available width without overflowing.
*   `auto`: the content will adjust its width based on the available space without overflowing.

 |

TableCell props[](https://developers.hubspot.com/docs/platform/ui-components/table#tablecell-props)
---------------------------------------------------------------------------------------------------

| Prop | Type | Description |
| --- | --- | --- |
| `align` | `'center'` | `'left'` | `'right'` | Sets the alignment of a table cell. |
| `width` | Number | `'min'` | `'max'` | `'auto'` | 
Sets the width of a table cell.

*   `min`: the content will only be as wide as required, overflowing if the content is wider than the table. A horizontal scrollbar will appear when there is overflow.
*   `max`: the content will expand to occupy the maximum available width without overflowing.
*   `auto`: the content will adjust its width based on the available space without overflowing.

 |

Paginated tables[](https://developers.hubspot.com/docs/platform/ui-components/table#paginated-tables)
-----------------------------------------------------------------------------------------------------

To include paginated navigation below a table, set the `Table` prop `paginated` to `true`. 

![table-paginated-navigation](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023_2024/table-paginated-navigation.png?width=362&height=65&name=table-paginated-navigation.png)

You'll then include the following props to further configure pagination:

| Prop | Type | Description |
| --- | --- | --- |
| `maxVisiblePageButtons` | Number | The maximum number of page buttons to display. |
| `page` | Number | Denotes the current page number. |
| `pageCount` | Number | The total number of pages available. |
| `showButtonLabels` | Boolean | When set to `false`, hides the text labels for First/Prev/Next buttons. The button labels will still be accessible to screen readers. Default is `true`. |
| `showFirstLastButtons` | Boolean | When set to `true`, displays the First/Last page buttons. Default is `false`. |
| `onPageChange` | (pagenumber: number) => void | A function that is invoked when the page pagination button is clicked. It receives the new page number as an argument. |

Sortable tables[](https://developers.hubspot.com/docs/platform/ui-components/table#sortable-tables)
---------------------------------------------------------------------------------------------------

To add sorting functionality to a table, you can include the `sortDirection` and `onSortChange` props in the table's `TableHeader` components. To enable table data to dynamically reorder based on user input, you'll need to store your table data in variables rather than hard coding it into table cells. Below is an example of a sortable table with a static table footer.

![ui-extensions-sortable-table-1](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/ui-extensions-sortable-table-1.gif?width=484&height=362&name=ui-extensions-sortable-table-1.gif)

import { Table, TableHead, TableRow, TableHeader, TableBody, TableCell } from '@hubspot/ui-extensions'; hubspot.extend(({ context, runServerlessFunction, actions }) => ( <Extension context={context} runServerless={runServerlessFunction} sendAlert={actions.addAlert} /> )); const ORIGINAL\_DATA = \[ { name: 'The Simpsons', yearsOnAir: 28, emmys: 31, }, { name: 'M\*A\*S\*H', yearsOnAir: 11, emmys: 14, }, { name: 'Arrested Development', yearsOnAir: 4, emmys: 5, }, \]; const DEFAULT\_STATE = { name: 'none', yearsOnAir: 'none', emmys: 'none', } function Extension() { const \[data, setData\] = useState(ORIGINAL\_DATA); const \[sortState, setSortState\] = useState({...DEFAULT\_STATE}); function handleOnSort(fieldName, sortDirection) { const dataClone = \[...data\]; dataClone.sort((entry1, entry2) => { if (sortDirection === 'ascending') { return entry1\[fieldName\] < entry2\[fieldName\] ? -1 : 1; } return entry2\[fieldName\] < entry1\[fieldName\] ? -1 : 1; }); setSortState({ ...DEFAULT\_STATE, \[fieldName\]: sortDirection }); setData(dataClone); } return ( <Table> <TableHead> <TableRow> <TableHeader sortDirection={sortState.name} onSortChange={sortDirection => handleOnSort('name', sortDirection)} > Series </TableHeader> <TableHeader sortDirection={sortState.yearsOnAir} onSortChange={sortDirection => handleOnSort('yearsOnAir', sortDirection) } > Years on air </TableHeader> <TableHeader sortDirection={sortState.emmys} onSortChange={sortDirection => handleOnSort('emmys', sortDirection)} > Emmys </TableHeader> </TableRow> </TableHead> <TableBody> {data.map(({ name, yearsOnAir, emmys }) => { return ( <TableRow key={name}> <TableCell>{name}</TableCell> <TableCell>{yearsOnAir}</TableCell> <TableCell>{emmys}</TableCell> </TableRow> ); })} </TableBody> <TableFooter> <TableRow> <TableHeader>Totals</TableHeader> <TableHeader>43</TableHeader> <TableHeader>50</TableHeader> </TableRow> </TableFooter> </Table> ); }

| Prop | Type | Description |
| --- | --- | --- |
| `sortDirection` | `'none'` (default) | `'ascending'` | `'descending'` | Visually indicates with an arrow which way the rows are sorted. |
| `onSortChange` | (value: "none" | "ascending" | "descending") => void | A function that will be invoked when the header is clicked. It receives a `sortDirection` as an argument (cannot be none or a null value). |
| `disabled` | Boolean | When set to `true`, users cannot change the sort ordering. It has no effect if `sortDirection` is set to `never` or undefined. Default is `false`. |

Usage examples[](https://developers.hubspot.com/docs/platform/ui-components/table#usage-examples)
-------------------------------------------------------------------------------------------------

*   A client list containing names, phone numbers, job positions, and email addresses that salespeople can use to prioritize outreach.
*   A summary table of the deals closed last quarter.

Guidelines[](https://developers.hubspot.com/docs/platform/ui-components/table#guidelines)
-----------------------------------------------------------------------------------------

*   **DO:** keep text within data cells clear and concise for easier scanning.
*   **DO:** always include a table header row to label columns.
*   **DO:** limit the use of links in table cells.
*   **DON'T:** use multiple tables on one screen when possible.
*   **DON'T:** render a blank table if there's no potential for no data to display, such as with search or filters. Instead, use the [EmptyState component](/docs/platform/ui-components/emptystate) when there are no results to display.

Related components[](https://developers.hubspot.com/docs/platform/ui-components/table#related-components)
---------------------------------------------------------------------------------------------------------

*   [DescriptionList](https://developers.hubspot.com/docs/platform/ui-components/descriptionlist)
*   [Statistics](https://developers.hubspot.com/docs/platform/ui-components/statistics)
*   [CrmPropertyList](https://developers.hubspot.com/docs/platform/ui-components/crmpropertylist)

* * *

Share your feedback[](https://developers.hubspot.com/docs/platform/ui-components/table#page-feedback)
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