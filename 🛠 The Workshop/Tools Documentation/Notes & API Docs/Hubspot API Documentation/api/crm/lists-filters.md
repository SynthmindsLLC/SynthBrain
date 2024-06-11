---
Based on the provided content, here's the YAML front matter: "---"
title: "List Filters"
description: "If you select a `SNAPSHOT` or `DYNAMIC` list processing type when creating a list, use filters to determine which records are members of the list."
type: "concept"
tags:
- "Lists"
- "Filtering"
- "HubSpot CRM"
relationships:
- "#related_to [[CRM]]"
- "#similar_to [[Data Management]]"
- "#enables [[Record Selection]]"
---

List filters
============

If you select a `SNAPSHOT` or `DYNAMIC` list processing type when creating a list, use filters to determine which records are members of the list.

*   List filters have conditional logic that is defined by filter branches which have `**AND**` or `**OR**` operation types. This is defined by the `filterBranchType` parameter.
*   Within these branches, there are groups of individual filters that contain logic to assess records to determine if they should be included in the list. These are defined by the `filterType` parameter. 
*   Filter branches can also have nested filter branches.

Filters
-------

There are a variety of different filter types that can be used to build out filters in a list's filter definition. These filters types can be used together in different combinations to construct the logic that is needed for a particular list definition structure. 

HubSpot uses PASS/FAIL logic with filters to determine if a record should be in a list. If a record passes all filters, it will be a member of the list.

### Filter Evaluation Steps

To determine which records pass a list's filters, the following steps occur in order:

1.  Select or fetch the relevant records based on the filter selected. For example, the property values for all records being evaluated for a property filter. 
2.  If applicable, use the `pruningRefineBy` parameter to refine the data to a specific time range (see Refine By Operation section). 
3.  Apply the filtering rules against the refined data to determine if the records **PASS** or **FAIL**. For example, if the filter "First Name is equal to "John"" is selected, **PASS** all records that have "John" for their First Name contact property.
4.  If applicable, use the `coalescingRefineBy` parameter to further refine the data to a specific number of occurrences. For example, the filter "contact has filled out a form at least 2 times". 
    *   If a `coalescingRefineBy` parameter is present, then **PASS** records that meet the number of occurrences selected.
    *   If no `coalescingRefineBy` parameter is present, then records **PASS** or **FAIL** based on the criteria set in step 3. 

Filter Branches
---------------

A filter branch is a data structure used to build out the conditional logic of a list's definition. Filter branches are defined by a specific type, an operator, a list of filters, and a list of sub-branches.

The filter branch's operator `OR` or `AND` dictate how the filter branch will be evaluated relative to the rest of the branches. The list of filters and sub-filter branches determine which records will be members of a list.

*   If the filter branch has an `AND` operator, then the record is accepted by the branch if it passes **all** the branch's filters and is accepted by **all** the sub-filter branches.
*   If the filter branch has an `OR` operator, then the record is accepted by the branch if it passes **any** of the branch's filters or is accepted by **any** of the branch's sub-filter branches. 

A record is a member of a list if it is accepted by the root filter branch in the list definition. 

### Base Filter Branch Structure

All filter definitions must start with a root-level `OR` `filterBranchType` (see "Filter Branch Types" for more details). This root level `OR` filter branch must then have one or more `AND` sub-filter branches.

The root-level `OR` filter branch can be thought of as the parent filter branch while the `AND` sub-filter branches can be thought of as child filter groups. Together, these branches make up the base filter brunch structure.

{ "filterBranches": \[ { "filterBranches": \[\], "filterBranchType": "AND", "filters": \[ // can have filters here \] }, // can have more filterBranches here \], "filterBranchType": "OR", "filters": \[\] }

For example, to create a list of contacts who have the first name "John" OR do not have the last name "Smith", the `POST` body would be:

{ "filterBranchType": "OR", "filters": \[\], "filterBranches": \[ { "filterBranchType": "AND", "filters": \[ { "filterType": "PROPERTY", "property": "firstname", "operation": { "operationType": "MULTISTRING", "operator": "IS\_EQUAL\_TO", "values": \["John"\] } } \], "filterBranches": \[\] }, { "filterBranchType": "AND", "filters": \[ { "filterType": "PROPERTY", "property": "lastname", "operation": { "operationType": "MULTISTRING", "operator": "IS\_NOT\_EQUAL\_TO", "values": \["Smith"\] } } \], "filterBranches": \[\] } \] }

In the above example, there is one parent `OR` `filterBranchType` parameter with two nested `AND` `filterBranchType` parameters. The nested filter branches each have one `filterType` that sets the criteria for the list.

The two `filterType` parameters are nested within `AND` filter branches, rather than directly within an `OR` filter branch. This structure is enforced by HubSpot's API so that the list's filters can be properly rendered in the HubSpot user interface.

In the HubSpot user interface, the above code would look like the image below. Any contacts that meet either of the criteria will be a member of the list. 

![and-or-list](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/and-or-list.png?width=300&height=420&name=and-or-list.png)  

To create a list of contacts who have the first name "John" and the last name "Smith":

{ "filterBranchType": "OR", "filters": \[\], "filterBranches": \[ { "filterBranchType": "AND", "filters": \[ { "filterType": "PROPERTY", "property": "firstname", "operation": { "operationType": "MULTISTRING", "operator": "IS\_EQUAL\_TO", "values": \["John"\] } }, { "filterType": "PROPERTY", "property": "lastname", "operation": { "operationType": "MULTISTRING", "operator": "IS\_EQUAL\_TO", "values": \["Smith"\] } } \], "filterBranches": \[\] } \] }

In the above example, there is one parent `OR` `filterBranchType` with one nested `AND` `filterBranchType`. The `AND` `filterBranchType` has two `filterType` parameters, one for each criteria. 

In the HubSpot user interface, the above code would look like the image below. Any contacts that meet the criteria will be a member of the list. 

![and-list](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2023/and-list.png?width=334&height=157&name=and-list.png)   

### Filtering on events and associated objects

There are two special versions of `AND` `filterBranchType` parameters:

*   `UNIFIED_EVENTS`: used to filter on events.
*   `ASSOCIATION`: used to filter on records that are associated with the primary record being evaluated.

These branches should be used within an `AND` filter branch. For example: 

{ "filterBranches": \[ { "filterBranches": \[ { "filterBranchType": "UNIFIED\_EVENTS", "filterBranchOperator": "AND", "filters": \[ // must have one or more filters here \] // additional UNIFIED\_EVENTS filter branch details omitted }, { "filterBranchType": "ASSOCIATION", "filterBranchOperator": "AND", "filters": \[ // may have one or more filters here \], "filterBranches": \[ // may have another ASSOCIATION branch here if filtering based on line item properties from a contact list \], // additional ASSOCIATION filter branch details omitted } \], "filterBranchOperator": "AND", "filterBranchType": "AND", "filters": \[ // can have filters here \] }, // can have more filterBranches here \], "filterBranchOperator": "OR", "filterBranchType": "OR", "filters": \[\] }

Filter Branch Types
-------------------

Below, review the different `filterBranchType` parameters that can be used to construct your list's filter definition structure.

### OR Filter Branch

Begin your filter definition structure with an `OR` `filterBranchType`. It is used to apply OR conditional logic against records that are accepted by the nested `AND` filter branches. 

`OR` filter branches:

*   Must have one or more `AND` type sub-filter branches.
*   Cannot have any filters.

If a record is accepted by any of its nested filter branches, an `OR` filter branch will accept the record as well. 

{ "filterBranchType": "OR", "filterBranches": \[\], // One or more nested AND filter branches "filters": \[\] // Zero filters }

### AND Filter Branch

The `AND` `filterBranchType` is used as a nested filter branch within the parent `OR` filter branch. All filter definitions must have at least one `AND` filter branch for it to be valid. It is used to apply AND conditional logic against the records that pass evaluation as defined by its filters and have also been accepted by nested filter branches. 

**AND** filter branches:

*   Can have zero or more filters.
*   Can have zero or more nested `UNIFIED_EVENTS` and/or `ASSOCIATION` `filterBranchType` parameters.

An `AND` filter branch accepts a record if the record is accepted by all of its nested filter branches and the record passes all filters in the filter branch. 

{ "filterBranchType": "AND", "filterBranches": \[\], // Zero or more nested UNIFIED\_EVENTS or ASSOCIATION filter branches "filters": \[\] // Zero or more filters }

### UNIFIED\_EVENTS Filter Branch

The `UNIFIED_EVENTS` `filterBranchType` can only be used as a nested filter branch within an `AND` `filterBranchType`. It is used to determine which records have or have not completed a given unified event. 

`UNIFIED_EVENTS` type filter branches:

*   Can have one or more `PROPERTY` type filters.
*   Cannot have any additional filter branches.

A `UNIFIED_EVENTS` filter branch accepts a record if the record passes all filters on the filter branch and the criteria defined by the `UNIFIED_EVENTS` filter branch.

{ "filterBranchType": "UNIFIED\_EVENTS", "filterBranches": \[\], // Zero filter branches "filters": \[\], // Zero or more filters "eventTypeId": "0-1", "operator": "HAS\_COMPLETED" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

`HAS_COMPLETED`, `HAS_NOT_COMPLETED`

 |

### ASSOCIATION Filter Branch

The `ASSOCIATION` `filterBranchType` can only be used as a nested filter branch within an `AND` `filterBranchType`. It is used to filter on records which are associated with the primary record being evaluated.

`ASSOCIATION` filter branches:

*   Must have one or more filters.
*   Cannot have any additional nested filter branches.

An `ASSOCIATION` filter branch accepts a record if it is accepted by all of its nested filter branches and if the record **PASSES** all filters of the filter branch.

You can only have additional `filterBranches` in the case of a `CONTACT` to `LINE_ITEM` association. 

{ "filterBranchType": "ASSOCIATION", "filterBranches": \[\], // Zero or one nested ASSOCIATION filter branches "filters": \[\], // Zero or more filters "objectTypeId": "0-1", "operator": "IN\_LIST", "associationTypeId": 280, "associationCategory": "HUBSPOT\_DEFINED" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

`IN_LIST`

 |
| 

`associationCategory`

 | 

`HUBSPOT_DEFINED`, `USER_DEFINED`, `INTEGRATOR_DEFINED`

 |

Filter Types
------------

Review the table below for the different types of filters that can be used. The `filterType` parameter is used to define the filter within the `filterBranch`. 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`ADS_TIME`

 | 

Evaluates whether a contact has seen any ads in the timeframe defined by the `pruningRefineBy` parameter.

 |
| 

`ADS_SEARCH`

 | 

Evaluates whether a contact has performed the ad interactions as defined by the filter.

 |
| 

`CTA`

 | 

Evaluates whether a contact has or has not interacted with a specific call-to-action as defined by the filter.

 |
| 

`EMAIL_EVENT`

 | 

Evaluate the opt-in status of a contact for specific email subscriptions as defined by the filter.

 |
| 

`EVENT`

 | 

Evaluates whether a contact has or does not have a specific event as defined by the filter. 

 |
| 

`FORM_SUBMISSION`

 | 

Evaluates whether a contact has or has not filled out a specific form or any form as defined by the filter.

 |
| 

`FORM_SUBMISSION_ON_PAGE`

 | 

Evaluates whether a contact  has or has not filled out a specific or any form on a specific page as defined by the filter.

 |
| 

`IN_LIST`

 | 

Evaluates whether a record is or is not a member of a specific list, import, or workflow as defined by the filter.

 |
| 

`PAGE_VIEW`

 | 

Evaluates whether a contact has or has not viewed a specific page as defined by the filter.

 |
| 

`PRIVACY`

 | 

Evaluates whether a contact does or does not have privacy consent for a specific privacy type as defined by the filter.

 |
| 

`PROPERTY`

 | 

Evaluates whether a record’s property value satisfies the property filter operation as defined by the filter. See the Property Filter Operation section for more details.

 |
| 

`SURVEY_MONKEY`

 | 

Evaluates whether a contact has or has not responded to a specific Survey Monkey survey as defined by the filter.

 |
| 

`SURVEY_MONKEY_VALUE`

 | 

Evaluates whether a contact has or has not responded to a specific Survey Monkey survey’s question with a specified value as defined by the filter.

 |
| 

`WEBINAR`

 | 

Evaluates whether a contact has or has not registered or attended any webinars or a specific webinar as defined by the filter.

 |
| 

`INTEGRATION_EVENT`

 | 

Integration event filters can be used to filter specific contacts based on whether or not they have interacted with integration events that have properties as specified by the filter lines.

 |

Property Filter Operations
--------------------------

Certain filters use the `operation` parameter to apply additional filtering criteria against a record's property value to  determine if the record PASSES or FAILS the filter. `PROPERTY` and `SURVEY_MONKEY_VALUE` filters can use the `operation` parameter. There are a variety of operations that can be used in the definition of these filters. 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`ALL_PROPERTY`

 | 

Used to determine whether a property value is known or is unknown as defined by the property operation.

 |
| 

`BOOL`

 | 

Used to determine whether a current (or historical) boolean property value is or is not (or has or has not) equaled a specific value.

 |
| 

`ENUMERATION`

 | 

Used to determine whether an enumeration/multi-select property value is any of, is none of, is exactly, is not exactly, contains all of, does not contain all of, has ever been any of, has never been any of, has ever been exactly, has never been exactly, has ever contained all, or has never contained all of a given set of values as defined by the property operation.

 |
| 

`MULTISTRING`

 | 

Used to determine whether a string property value is equal to, is not equal to, contains, does not contain, starts with, or ends with any of a given set of values as defined by the property operation.

 |
| 

`NUMBER`

 | 

Used to determine whether a current (or historical) number property value is or is not (or has or has not) equaled a specific value as defined by the property operation.

 |
| 

`STRING`

 | 

Used to determine whether a current (or historical) string property value is or is not (or has or has not) equaled a specific value as defined by the property operation.

 |
| 

`TIME_POINT`

 | 

Used to determine if a property has been updated before or after a specific time. That time can be specified as a specific date or relative to the current day. This operation also allows the comparison of two properties or their last updated time.

 |
| 

`TIME_RANGED`

 | 

Used to determine if a property has been updated between or outside of two specific times. These times can be specified as a specific date or relative to the current day. 

 |

### TIME\_POINT and TIME\_RANGED examples

Below, review some examples when using the `TIME_POINT` and `TIME_RANGED` parameter. These parameters can be used in both time-referenced and property-referenced requests. 

#### Is equal to date

The request below filters for _Last activity date is equal to 03/11/2024 (EDT)_. 

{ "name": "Sample Date Equal", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BETWEEN", "includeObjectsWithNoValueSet": false, "lowerBoundEndpointBehavior": "INCLUSIVE", "upperBoundEndpointBehavior": "INCLUSIVE", "propertyParser": "VALUE", "lowerBoundTimePoint": { "timeType": "DATE", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "year": 2024, "month": 3, "day": 11, "hour": 0, "minute": 0, "second": 0, "millisecond": 0 }, "upperBoundTimePoint": { "timeType": "DATE", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "year": 2024, "month": 3, "day": 11, "hour": 23, "minute": 59, "second": 59, "millisecond": 999 }, "type": "TIME\_RANGED", "operationType": "TIME\_RANGED" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" }

#### Is between or is not between dates

The example below filters for _Last activity date is between 03/04/2024 (EST) and 03/11/2024 (EDT)_. 

To filter for _Last activity date is not between 03/04/2024 (EST) and 03/11/2023 (EDT)_, change the `operator` parameter to `IS_NOT_BETWEEN`. 

{ "name": "Sample Date Between", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BETWEEN", "includeObjectsWithNoValueSet": false, "lowerBoundEndpointBehavior": "INCLUSIVE", "upperBoundEndpointBehavior": "INCLUSIVE", "propertyParser": "VALUE", "lowerBoundTimePoint": { "timeType": "DATE", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "year": 2024, "month": 3, "day": 4, "hour": 0, "minute": 0, "second": 0, "millisecond": 0 }, "upperBoundTimePoint": { "timeType": "DATE", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "year": 2024, "month": 3, "day": 11, "hour": 23, "minute": 59, "second": 59, "millisecond": 999 }, "type": "TIME\_RANGED", "operationType": "TIME\_RANGED" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

#### In Last X Number of Days

The example below filters for _Last activity date is less than 3 days ago_. 

{ "name": "Sample Date Last 3 days", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BETWEEN", "includeObjectsWithNoValueSet": false, "lowerBoundEndpointBehavior": "INCLUSIVE", "upperBoundEndpointBehavior": "INCLUSIVE", "propertyParser": "VALUE", "lowerBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "TODAY" }, "offset": { "days": -3 } }, "upperBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "NOW" } }, "type": "TIME\_RANGED", "operationType": "TIME\_RANGED" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

#### In Next X Number of Days

The example below filters for _Last activity date is less than 5 days from now_. 

{ "name": "Sample Date Next 5 Days", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BETWEEN", "includeObjectsWithNoValueSet": false, "lowerBoundEndpointBehavior": "INCLUSIVE", "upperBoundEndpointBehavior": "INCLUSIVE", "propertyParser": "VALUE", "lowerBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "NOW" } }, "upperBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "TODAY" }, "offset": { "days": 5 } }, "type": "TIME\_RANGED", "operationType": "TIME\_RANGED" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

#### Updated or Not Updated in the Last X Days

The example below filters for _Last activity date updated in last 7 days_. 

To filter for _Last activity date not updated in last 7 days_, change the `operator` parameter to `IS_NOT_BETWEEN`.  

{ "name": "Sample Date Updated Last 7 Days", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BETWEEN", "includeObjectsWithNoValueSet": false, "lowerBoundEndpointBehavior": "INCLUSIVE", "upperBoundEndpointBehavior": "INCLUSIVE", "propertyParser": "UPDATED\_AT", "lowerBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "TODAY" }, "offset": { "days": -7 } }, "upperBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "NOW" } }, "type": "TIME\_RANGED", "operationType": "TIME\_RANGED" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

#### Is After Date

#### Is Before Date

The example below filters for _Last activity date is after 03/04/2024 (EST)_. 

{ "name": "Sample Date After", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_AFTER", "includeObjectsWithNoValueSet": false, "timePoint": { "timeType": "DATE", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "year": 2024, "month": 3, "day": 4, "hour": 23, "minute": 59, "second": 59, "millisecond": 999 }, "endpointBehavior": "EXCLUSIVE", "propertyParser": "VALUE", "type": "TIME\_POINT", "operationType": "TIME\_POINT" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

The example below filters for _Last activity date is before 03/04/2024 (EST)_. 

{ "name": "Sample Date Before", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BEFORE", "includeObjectsWithNoValueSet": false, "timePoint": { "timeType": "DATE", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "year": 2024, "month": 3, "day": 4, "hour": 00, "minute": 00, "second": 00, "millisecond": 000 }, "endpointBehavior": "EXCLUSIVE", "propertyParser": "VALUE", "type": "TIME\_POINT", "operationType": "TIME\_POINT" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

#### Is Relative to Today

The example below can either represent _Last activity date is more than x days from now_ or _Last activity date is more than x days ago_. 

To filter for the latter, set the value for the `offset` parameter to `<=0`.

{ "name": "Sample Days From Now", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_AFTER", "includeObjectsWithNoValueSet": false, "timePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": { "referenceType": "TODAY" }, "offset": { "days": 2 } }, "endpointBehavior": "EXCLUSIVE", "propertyParser": "VALUE", "type": "TIME\_POINT", "operationType": "TIME\_POINT" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchOperator": "OR", "filterBranchType": "OR" } }

#### Is Before or After another property (value or last updated) 

The example below compares the values where _Last activity date is before Latest Open Lead Date_. 

To filter for _Last activity date is after Latest Open Lead Date_: set the `operator` value to `IS_AFTER`.

To filter for when the Latest Open Lead Date was updated: set the `referenceType` value to `UPDATED_AT`. 

{ "name": "Sample Property Before", "objectTypeId": "0-1", "processingType": "DYNAMIC", "filterBranch": { "filterBranches": \[ { "filterBranches": \[\], "filters": \[ { "property": "notes\_last\_updated", "operation": { "operator": "IS\_BEFORE", "includeObjectsWithNoValueSet": false, "timePoint": { "timeType": "PROPERTY\_REFERENCED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "property": "hs\_latest\_open\_lead\_date", "referenceType": "VALUE" }, "endpointBehavior": "EXCLUSIVE", "propertyParser": "VALUE", "type": "TIME\_POINT", "operationType": "TIME\_POINT" }, "filterType": "PROPERTY" } \], "filterBranchType": "AND", "filterBranchOperator": "AND" } \], "filters": \[\], "filterBranchType": "OR", "filterBranchOperator": "OR" } }

Refine By Operation
-------------------

There are two types of refine by operations that can be used in certain filters:

*   `pruningRefineBy`: refine the data set to a particular timeframe.
*   `coalescingRefineBy`: determines whether the record **PASSES** the filter the number of times defined. 

Filters only support up to one refine by operation at a time, even if some filters allow for both a coalescing and pruning refine by operation to be passed in. This is enforced by HubSpot's API. 

### Pruning Refine By Operations

Pruning refine by operations are used to narrow down the dataset that will be used for filter evaluation by refining the dataset to a particular timeframe. Pruning refine by operations are classified into two types: relative and absolute.

*   **Relative**: narrow the dataset down based on a time offset of a number of days or weeks in the past or in the future.
*   **Absolute**: narrow the dataset down based on the data being before or after a specific timestamp

For both relative and absolute refine by operations, there are ranged and comparative derivatives.

#### Absolute Comparative Timestamp

Used to narrow the relevant dataset down based on whether the timestamp of the data being evaluated is before or after a specific timestamp as defined by the refine by operation.

{ "type": "ABSOLUTE\_COMPARATIVE", "comparison": "BEFORE", "timestamp": 1698915170126 }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`comparison`

 | 

Whether the data's timestamp is before or after the defined `timestamp`. Values include:

`BEFORE`, `AFTER`

 |

#### Absolute Ranged Timestamp

Used to narrow the relevant dataset down based on whether the timestamp of the data being evaluated is between or is not between an upper and lower bound timestamp as defined by the refine by operation.

{ "type": "ABSOLUTE\_RANGED", "rangeType": "BETWEEN", "lowerTimestamp": 1698915170126, "upperTimestamp": 1682406908449 }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`rangeType`

 | 

Whether the data's timestamp is between or not between the defined `lowerTimestamp`and `upperTimestamp`. Values include:

`BETWEEN`, `NOT_BETWEEN`

 |

#### Relative Comparative Timestamp

Used to narrow the relevant dataset down based on whether the timestamp of the data being evaluated is before or after a certain number of days or weeks in the past or future relative to the current timestamp as defined by the refine by operation.

{ "type": "RELATIVE\_COMPARATIVE", "comparison": "BEFORE", "timeOffset": \[ "offsetDirection": "PAST", "timeUnit": "DAYS", "amount": 4 \], }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`comparison`

 | 

Whether the data's timestamp is before or after the defined `timeOffset` values. Values include: 

`BEFORE`, `AFTER`

 |
| 

`offsetDirection`

 | 

Values include:

`PAST`, `FUTURE`

 |
| 

`timeUnit`

 | 

Values include:

`DAYS`, `WEEKS`

 |
| 

`amount`

 | 

A number value. 

 |

#### Relative Ranged Timestamp

Used to narrow the relevant dataset down based on whether the timestamp of the data being evaluated is between or is not between an upper and lower bound time offset relative to the current timestamp. The time offsets are a certain number of days or weeks in the past or the future as defined by the refine by operation.

{ "type": "RELATIVE\_RANGED", "rangeType": "BETWEEN", "timeOffset": \[ "offsetDirection": "PAST", "timeUnit": "DAYS", "amount": 4 \], }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`rangeType`

 | 

Whether the data's timestamp is between or not between the defined `timeOffset` values. Values include: 

`BETWEEN`, `NOT_BETWEEN`

 |
| 

`offsetDirection`

 | 

Values include:

`PAST`, `FUTURE`

 |
| 

`timeUnit`

 | 

Values include:

`DAYS`, `WEEKS`

 |
| 

`amount`

 | 

A number value. 

 |

### Coalescing Refine By Operations

Coalescing refine by operations are used once the filter criteria has been applied to the relevant dataset. The only coalescing refine by operation supported by the Lists API is a “number of occurrences” operation that determines whether an object in the dataset PASSED the filter evaluation at least a minimum number of times and less than a maximum number of times.

{ "type": "NUM\_OCCURRENCES", "minOccurrences": 1, // Optional "maxOccurrences": 4 // Optional }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`NUM_OCCURRENCES`

 | 

Used to determine whether an object in the relevant dataset PASSED the filter evaluation at least a minimum number of times (or zero times if a minimum is not provided) and at most a maximum number of times (or any number of times if a maximum is not provided) as defined by the refine by operation.

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/lists-filters#page-feedback)
----------------------------------------------------------------------------------------------

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