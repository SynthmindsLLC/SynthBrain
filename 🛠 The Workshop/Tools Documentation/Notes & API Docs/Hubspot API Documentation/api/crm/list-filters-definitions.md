---
title: "List filter definitions (BETA)"
description: "Definitions for the list type, property operations, and coalescing refine by and pruning refine by operations."
type: "concept"
tags:
- "Filter"
- "List_Definitions"
relationships:
- "#related_to [[Ads Time Filter]]"
- "#related_to [[Ads Search Filter]]"
- "#related_to [[CTA Filter]]"
- "#related_to [[Email Event Filter]]"
- "#related_to [[Email Subscription Filter]]"
- "#related_to [[Event Filter]]"
- "#related_to [[Form Submission Filter]]"
- "#related_to [[Form Submission on Page Filter]]"
- "#related_to [[Integration Event Filter]]"
- "#related_to [[Page View Filter]]"
- "#related_to [[Privacy Filter]]"
- "#related_to [[Property Filter]]"
- "#related_to [[Survey Monkey Filter]]"
- "#related_to [[SURVEY_MONKEY_VALUE Filter]]"
- "#related_to [[Webinar Filter]]"
- "#related_to [[Weber Filter]]"
- "#related_to [[Property Operation Definitions]]"]]
- "#related_to [[Time Point Operations]]"]]"
- "#related_to [[Time Ranged Operations]]"]]"
---

List filter definitions (BETA)
==============================

Below, review the definitions for the filter type, property operations, and coalescing refine by and pruning refine by operations. 

Filter Object Operations
------------------------

The `filterType` parameter is used to define the filter within the filterBranch. There are 16 different types of filters.

### Ads Time Filter

Evaluates whether a contact has seen any ads in the timeframe defined by the `pruningRefineBy` parameter. 

{ "filterType": "ADS\_TIME", "pruningRefineBy": PruningRefineBy }

### Ads Search Filter

Evaluates whether a contact has performed the ad interactions as defined by the filter. 

{ "filterType": "ADS\_SEARCH", "entityType": "AD", "searchTermType": "ID", "searchTerms": \["hubspot", "hubspot developers"\], "adNetwork": "LINKEDIN", "operator": "CONTAINS" }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`entityType`

 | 

The type of asset interacted with. Values include:

*   `AD`: a specific ad. Supports `ID`, `NAME`, and `AD_TYPE` as `searchTermTypes`. 
*   `ADGROUP`: a specific ad group. Supports `ID` and `NAME` as `SearchTermTypes`.
*   `CAMPAIGN`: a specific ad campaign. Supports `ID` and `NAME` as `SearchTermTypes`.

 |
| 

`searchTermType`

 | 

The `searchTerms` type. Values include:

*   `ID` - supports `IS_KNOWN` and `IS_EQUAL_TO` as operators. 
*   `NAME` - supports all operators
*   `AD_TYPE` -  supports `IS_KNOWN` and `IS_EQUAL_TO` as operators.

`AD_TYPE` cannot be used when `entityType` is `ADGROUP` or `CAMPAIGN`.

 |
| 

`searchTerms`

 | 

Required, unless the `operator` is `IS_KNOWN`.

 |
| 

`adNetwork`

 | 

The ad network. Values include:

`LINKEDIN`, `ADWORDS`, `FACEBOOK`

 |
| 

`operator`

 | 

The filter operator. Values include:

`CONTAINS`, `IS_EQUAL_TO`, `ENDS_WITH`, `STARTS_WITH`, `IS_KNOWN`

 |

### CTA Filter

Evaluates whether a contact has or has not interacted with a specific CTA as defined by the filter. 

{ "filterType": "CTA", "ctaName": "b7988654-536d-4f7f-976b-8e9e2c7bb54", "coalescingRefineBy": CoalescingRefineBy, // Optional "pruningRefineBy": PruningRefineBy, // Optional "operator": "HAS\_CLICKED\_CTA" }

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`HAS_CLICKED_CTA`, `HAS_NOT_CLICKED_CTA`, `HAS_OPENED_CTA`, `HAS_NOT_OPENED_CTA`, `HAS_CLICKED_CTA_PLACEMENT`, `HAS_NOT_CLICKED_CTA_PLACEMENT`, `HAS_OPENED_CTA_PLACEMENT`, `HAS_NOT_OPENED_CTA_PLACEMENT`

 |

### Email Event Filter

Evaluates whether a contact has or has not interacted with a marketing email as defined by the filters. 

{ "filterType": "EMAIL\_EVENT", "level": "EMAIL\_API\_CAMPAIGN", "emailId": "79019645", "appId": "2285", "operator": "OPENED", "clickUrl": string, // Optional "pruningRefineBy": PruningRefineBy // Optional }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`level`

 | 

The email campaign level. Values include:

`EMAIL_API_CAMPAIGN`, `EMAIL_API_CAMPAIGN_GROUP`, `HUBSPOT_CAMPAIGN`

 |
| 

`operator`

 | 

The filter operator. Values include:

`LINK_CLICKED`, `MARKED_SPAM`, `OPENED`, `OPENED_BUT_LINK_NOT_CLICKED`, `OPENED_BUT_NOT_REPLIED`, `REPLIED`, `UNSUBSCRIBED`, `BOUNCED`,  `RECEIVED`, `RECEIVED_BUT_NOT_OPENED`,  `SENT`, `SENT_BUT_LINK_NOT_CLICKED`, `SENT_BUT_NOT_RECEIVED`

 |
| 

`clickURL`

 | 

Only allowed when `operator` is `LINK_CLICKED`.

 |
| 

`pruningRefineBy`

 | 

Only supports `ABSOLUTE_COMPARATIVE` and `ABSOLUTE_RANGED`.

 |

### Email Subscription Filter

Evaluates whether a contact has or has not interacted with a marketing email as defined by the filters. 

{ "filterType": "EMAIL\_SUBSCRIPTION", "subscriptionIds": \["4805877"\], "acceptedStatuses": \["OPT\_IN"\], "subscriptionType": "SUBSCRIPTION" // Optional }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`acceptedStatuses`

 | 

The email subscription status. Values include:

`OPT_IN`, `OPT_OUT`, `NOT_OPTED`

There can only be one `acceptedStatus` per `filterType`.

 |
| 

`subscriptionType`

 | 

The subscription type.

 |
| 

`clickURL`

 | 

Only allowed when `operator` is `LINK_CLICKED`.

 |
| 

`pruningRefineBy`

 | 

Only supports `ABSOLUTE_COMPARATIVE` and `ABSOLUTE_RANGED`.

 |

### Event Filter

Evaluates whether a contact has or does not have a specific event as defined by the filter.

{ "filterType": "EVENT", "eventId": "123456", "operator": "HAS\_EVENT", "coalescingRefineBy": CoalescingRefineBy, // Optional "pruningRefineBy": PruningRefineBy // Optional }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`HAS_EVENT`, `NOT_HAS_EVENT`

 |

### Form Submission Filter

Evaluates whether a contact has or has not filled out a specific form or any form as defined by the filter. 

{ "filterType": "FORM\_SUBMISSION", "formId": "6f62a9c7-4200-4b50-9779-3db4d9e40eb2", // Optional "coalescingRefineBy": CoalescingRefineBy, // Optional "pruningRefineBy": PruningRefineBy, // Optional "operator": "FILLED\_OUT" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`FILLED_OUT`, `NOT_FILLED_OUT`

If `NOT_FILLED_OUT` is selected, the  `pruningRefineBy` parameter must be `null`.

 |

### Form Submission on Page Filter

Evaluates whether a contact has or has not filled out a specific or any form on a specific page as defined by the filter.

{ "filterType": "FORM\_SUBMISSION\_ON\_PAGE", "pageId": "397942088", "formId": "f62a9c7-4200-4b50-9779-3db4d9e40eb", // Optional "coalescingRefineBy": CoalescingRefineBy, // Optional "pruningRefineBy": PruningRefineBy, // Optional "operator": "FILLED\_OUT" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`FILLED_OUT`, `NOT_FILLED_OUT`

If `NOT_FILLED_OUT` is selected, the  `pruningRefineBy` parameter must be `null`.

 |

### In List Filter

Evaluates whether a record is or is not a member of a specific list, import, or workflow as defined by the filter.

{ "filterType":"IN\_LIST", "listId":"42", // Optional "metadata":\[ { "id":"56", "inListType":"WORKFLOWS\_ENROLLMENT" } \], // Optional "operator":"InListOperator" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`inListType`

 | 

The list type. Values include:

`WORKFLOWS_ENROLLMENT`, `WORKFLOWS_ACTIVE`, `WORKFLOWS_GOAL`, `WORKFLOWS_COMPLETED`, `IMPORT`

 |
| 

`operator`

 | 

The filter operator. Values include:

`IN_LIST`, `NOT_IN_LIST`

 |

### Integration Event Filter

Integration event filters can be used to filter specific contacts based on whether or not they have interacted with integration events that have properties as specified by the filter lines.

{ "filterType":"INTEGRATION\_EVENT", "eventTypeId":"4009", "filterlines":\[ { "property" :string, "operation": PropertyOperation }, \]}

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

Refer to the property operations definitions section. 

 |

### Page View Filter

Evaluates whether a contact has or has not viewed a specific page as defined by the filter. 

{ "filterType": "PAGE\_VIEW", "pageUrl":"www.hubspot.com" , "enableTracking": true, // Optional "operator": "HAS\_PAGEVIEW\_EQ", "coalescingRefineBy": CoalescingRefineBy, // Optional "pruningRefineBy": PruningRefineBy // Optional }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`enableTracking`

 | 

Must be a boolean property operation. Values include:

*   `TRUE` - can only be used if `operator` is `HAS_PAGEVIEW_EQ` or `NOT_HAS_PAGEVIEW_EQ`
*   `FALSE` 

 |
| 

`operator`

 | 

The filter operator. Values include:

`HAS_PAGEVIEW_EQ`,`HAS_PAGEVIEW_CONTAINS`,`HAS_PAGEVIEW_MATCHES_REGEX`, `NOT_HAS_PAGEVIEW_EQ`, `NOT_HAS_PAGEVIEW_CONTAINS`, `NOT_HAS_PAGEVIEW_MATCHES_REGEX   `

 |

### Privacy Filter

Evaluates whether a contact does or does not have privacy consent for a specific privacy type as defined by the filter. 

{ "filterType": "PRIVACY", "privacyName": "PRIVACY\_CONSENT\_APPROVE", "operator": "PRIVACY\_CONSENT\_GRANTED" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`privacyName`

 | `PRIVACY_CONSENT_APPROVE`, `PRIVACY_CONSENT_DECLINE`, `PRIVACY_CONSENT_REVOKE` |
| 

`operator`

 | 

`PRIVACY_CONSENT_GRANTED`, `PRIVACY_CONSENT_NOT_GRANTED`

 |

### Property Filter

Evaluates whether a record's property value satisfies the property filter operation as defined by the filter. 

{ "filterType": "PROPERTY", "property": "name", "operation": PropertyOperation }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`property`

 | 

The property name. 

 |
| 

`operation`

 | 

Refer to the property operations definitions section. 

 |

### Survey Monkey Filter

Evaluates whether a contact has or has not responded to a specific Survey Monkey survey as defined by the filter.

{ "filterType": "SURVEY\_MONKEY", "operator": "HAS\_RESPONDED\_TO\_SURVEY", "surveyId": "305206406" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`HAS_RESPONDED_TO_SURVEY`, `HAS_NOT_RESPONDED_TO_SURVEY`

 |

### Survey Monkey Value Filter

Evaluates whether a contact has or has not responded to a specific Survey Monkey survey’s question with a specified value as defined by the filter.

{ "filterType": "SURVEY\_MONKEY\_VALUE", "operator": "HAS\_ANSWERED\_SURVEY\_QUESTION\_WITH\_VALUE", "surveyId": "305677", "surveyAnswerRowId": null, // Optional "surveyAnswerColId": null, // Optional "valueComparison": PropertyOperation, "surveyQuestion": "423564" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`valueComparison`

 | 

Refer to the property operations definitions section. 

 |
| 

`operator`

 | 

The filter's operator. Value is `HAS_ANSWERED_SURVEY_QUESTION_WITH_VALUE`.

 |

### Webinar Filter

Evaluates whether a contact has or has not registered or attended any webinars or a specific webinar as defined by the filter. 

{ "filterType": "WEBINAR", "operator": "HAS\_WEBINAR\_REGISTRATION", "webinarId": "95909203370" // Optional }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`HAS_WEBINAR_REGISTRATION`, `NOT_HAS_WEBINAR_REGISTRATION`, `HAS_WEBINAR_ATTENDANCE`, `NOT_HAS_WEBINAR_ATTENDANCE`

 |

Property operation definitions
------------------------------

Certain filters use the `operation` parameter to apply additional filtering criteria against a record's property value to  determine if the record PASSES or FAILS the filter. `PROPERTY`, `INTEGRATION_EVENT` and `SURVEY_MONKEY_VALUE` filters can use the `operation` parameter. There are a variety of operations that can be used in the definition of these filters. There are six types of property operations. 

Each property operation definition has an `operationType`, `operator`, and `includeObjectsWithNoValueSet` parameters. 

*   `operationType` and `operator`: classify the type of operation and how it will operate against a property of value.
*   `includeObjectsWithNoValueSet`: defines how the operation should treat records that do not have a value set for the defined property.
    *   If `true`, a record without a value for the evaluated property will be accepted.
    *   If `false`, a record without a value for the evaluated property will be rejected.
    *   The default value is `false`.

### All Property Types

Used to determine whether a property value is known or is unknown as defined by the property operation.

{ "operationType": "ALL\_PROPERTY", "includeObjectsWithNoValueSet": false, // Optional "operator": "IS\_KNOWN" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`IS_KNOWN`, `IS_UNKNOWN`

 |

### Bool Property

Used to determine whether a current (or historical) boolean property value is or is not (or has or has not) equalled a specific value.

{ "operationType": "BOOL", "includeObjectsWithNoValueSet": false, // Optional "operator": "IS\_EQUAL\_TO", "value": true }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`IS_EQUAL_TO`, `IS_NOT_EQUAL_TO`,  
`HAS_EVER_BEEN_EQUAL_TO`,  
`HAS_NEVER_BEEN_EQUAL_TO`  

*   Property type must be a `boolean`. 
*   Calculated properties cannot have a historical `operator`.
*   `INTEGRATION_EVENT` `filterType` and `UNIFIED_EVENTS` `filterBranchType` parameters only support `IS_EQUAL_TO` and `IS_NOT_EQUAL_TO`.

 |

### Enumeration Property

Used to determine whether an enumeration/multi-select property value is any of, is none of, is exactly, is not exactly, contains all of, does not contain all of, has ever been any of, has never been any of, has ever been exactly, has never been exactly, has ever contained all, or has never contained all of a given set of values as defined by the property operation.

{ "operationType": "ENUMERATION", "includeObjectsWithNoValueSet": false, // Optional "operator": "IS\_NONE\_OF", "values": \["red", "blue"\] }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`IS_NONE_OF`,`IS_ANY_OF`, `IS_EXACTLY`, `IS_NOT_EXACTLY, CONTAINS_ALL`, `DOES_NOT_CONTAIN_ALL`, `HAS_EVER_BEEN_ANY_OF`, `HAS_NEVER_BEEN_ANY_OF`, `HAS_EVER_BEEN_EXACTLY`, `HAS_NEVER_BEEN_EXACTLY`, `HAS_EVER_CONTAINED_ALL`, `HAS_NEVER_CONTAINED_ALL`  

*   Property type must be an `enumeration.`
*   Calculated properties cannot have a historical `operator`.
*   `INTEGRATION_EVENT` `filterType` and `UNIFIED_EVENTS` `filterBranchType` parameters only support `IS_ANY_OF` and `IS_NONE_OF`.

 |

### Multi String Property

Used to determine whether a string property value is equal to, is not equal to, contains, does not contain, starts with, or ends with any of a given set of values as defined by the property operation.

{ "operationType": "MULTISTRING", "includeObjectsWithNoValueSet": false, // Optional "operator": "IS\_EQUAL\_TO", "values": \["yes","no"\] }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`IS_EQUAL_TO`, `IS_NOT_EQUAL_TO`, `CONTAINS`, `DOES_NOT_CONTAIN`, `STARTS_WITH`, `ENDS_WITH`,  
`HAS_EVER_BEEN_EQUAL_TO`,  
`HAS_NEVER_BEEN_EQUAL_TO`  

*   Property type must be a `string`.
*   Calculated properties cannot have a historical `operator`.
*   `INTEGRATION_EVENT` `filterType` and `UNIFIED_EVENTS` `filterBranchType` parameters only support `IS_EQUAL_TO`,  `IS_NOT_EQUAL_TO`, `CONTAINS`, `DOES_NOT_CONTAIN`, `STARTS_WITH`, and `ENDS_WITH` parameters.

 |

### Number Property

Used to determine whether a current (or historical) number property value is or is not (or has or has not) equaled a specific value as defined by the property operation.

{ "operationType": "NUMBER", "includeObjectsWithNoValueSet": false, // Optional "operator": "IS\_EQUAL\_TO", "values": 12234 }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`IS_EQUAL_TO`, `IS_NOT_EQUAL_TO`, `IS_GREATER_THAN`, `IS_GREATER_THAN_OR_EQUAL_TO`, `IS_LESS_THAN`, `IS_LESS_THAN_OR_EQUAL_TO`,  
`HAS_EVER_BEEN_EQUAL_TO`,  
`HAS_NEVER_BEEN_EQUAL_TO`  

*   Property type must be a `number`.
*   Calculated properties cannot have a historical `operator`.
*   `INTEGRATION_EVENT` `filterType` and `UNIFIED_EVENTS` `filterBranchType` parameters only support `IS_EQUAL_TO`,  `IS_NOT_EQUAL_TO`, `IS_GREATER_THAN`, `IS_GREATER_THAN_OR_EQUAL_TO`, `IS_LESS_THAN`, `IS_LESS_THAN_OR_EQUAL_TO` operators. 

 |

### String Property

Used to determine whether a current (or historical) string property value is or is not (or has or has not) equaled a specific value as defined by the property operation.

{ "operationType": "STRING", "includeObjectsWithNoValueSet": false, // Optional "operator": "IS\_EQUAL\_TO", "values": "a1s2d3f4" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`operator`

 | 

The filter operator. Values include:

`IS_EQUAL_TO`, `IS_NOT_EQUAL_TO`, `CONTAINS`, `DOES_NOT_CONTAIN`, `STARTS_WITH`, `ENDS_WITH`,  
`HAS_EVER_BEEN_EQUAL_TO`,  
`HAS_NEVER_BEEN_EQUAL_TO`, `HAS_EVER_CONTAINED`, `HAS_NEVER_CONTAINED`  

*   Property type must be a `string`.
*   Calculated properties cannot have a historical `operator`.
*   `INTEGRATION_EVENT` `filterType` and `UNIFIED_EVENTS` `filterBranchType` parameters only support `IS_EQUAL_TO`,  `IS_NOT_EQUAL_TO`, `CONTAINS`, `DOES_NOT_CONTAIN`, `STARTS_WITH`, and `ENDS_WITH` parameters.

 |

### Time Point 

Used to determine if a property has been updated between or outside of two specific times. These times can be specified as a specific date or relative to the current day. 

Inputs and validations differ on the `timeType` field: `PROPERTY_REFERENCED`, `DATE`, `INDEXED`

#### PROPERTY\_REFERENCED

{ "operator": "IS\_AFTER", "timePoint": { "timeType": "PROPERTY\_REFERENCED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "property": "hs\_latest\_open\_lead\_date", "referenceType": "UPDATED\_AT" }, "endpointBehavior": "EXCLUSIVE", "propertyParser": "UPDATED\_AT", "type": "TIME\_POINT", "operationType": "TIME\_POINT" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`timeType`

 | 

`PROPERTY_REFERENCED`

 |
| 

`propertyParser`

 | 

Values include:

`VALUE`, `UPDATED AT`

*   If `VALUE` is selected, the comparison is the value of the property.
*   If `UPDATED_AT` is selected, the updated time of the property is used for comparison.

 |
| 

`endpointBehavior`

 | 

`EXCLUSIVE`

 |
| 

`zoneID`

 | 

The account's default time zone. 

 |
| 

`operator`

 | 

The filter operator. Values inclue:

`IS_AFTER`, `IS_BEFORE`

*   The property passed must be a valid datetime property.

 |

#### DATE

{ "operationType": "TIME\_POINT" "operator": "IS\_AFTER", "timePoint": { "timeType":"DATE", "timezoneSource":"CUSTOM", "zoneId":"US/Eastern", "year":2024, "month":1, "day":1, "hour":23, "minute":59, "second":59, "millisecond":999 }, "endpointBehavior":"EXCLUSIVE", "propertyParser":"VALUE", "type":"TIME\_POINT" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`timeType`

 | 

`DATE`

 |
| 

`propertyParser`

 | 

Values include:

`VALUE`, `UPDATED AT`

*   If `VALUE` is selected, the comparison is the value of the property.
*   If `UPDATED_AT` is selected, the updated time of the property is used for comparison.

 |
| 

`endpointBehavior`

 | 

`EXCLUSIVE`

 |
| 

`zoneID`

 | 

The account's default time zone. 

 |
| 

`operator`

 | 

The filter operator. Values inclue:

`IS_AFTER`, `IS_BEFORE`

*   The date must be a valid date.
*   When the property is `IS_AFTER`, these fields must be set:
    *   `“hour”: 23`
    *   `“minute”: 59`
    *   `“second”: 59`
    *   `“millisecond”: 999`
*   When the property is `IS_BEFORE`, these fields must be set:
    *   `“hour”: 00`
    *   `“minute”: 00`
    *   `“second”: 00`
    *   `“millisecond”: 000`

 |

#### INDEXED

{ "operator":"IS\_BEFORE", "includeObjectsWithNoValueSet":false, "timePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference": {"referenceType":"TODAY"}, "offset": {"days":-1} }, "endpointBehavior": "EXCLUSIVE", "propertyParser": "VALUE", "type": "TIME\_POINT", "operationType": "TIME\_POINT" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`timeType`

 | 

`INDEXED`

 |
| 

`propertyParser`

 | 

Values include:

`VALUE`, `UPDATED AT`

*   If `VALUE` is selected, the comparison is the value of the property.
*   If `UPDATED_AT` is selected, the updated time of the property is used for comparison.

 |
| 

`endpointBehavior`

 | 

`EXCLUSIVE`

 |
| 

`zoneID`

 | 

The account's default time zone. 

 |
| 

`indexReference`

 | `{“referenceType”: “Today”}` |
| 

`operator`

 | 

The filter operator. Values inclue:

`IS_AFTER`, `IS_BEFORE`

  

*   When the property is `IS_AFTER`, offset must be set at <=0.
*   When the property is `IS_BEFORE`, offset must be set at >=0.

 |

### Time Ranged

Used to determine if a property has been updated between or outside of two specific times. These times can be specified as a specific date or relative to the current day. 

Inputs and validations differ based on the `timeType` field: `DATE` or `INDEXED`. 

#### INDEXED

{ "operator": "IS\_NOT\_BETWEEN", "includeObjectsWithNoValueSet": false, "lowerBoundEndpointBehavior": "INCLUSIVE", "upperBoundEndpointBehavior": "INCLUSIVE", "propertyParser": "UPDATED\_AT", "lowerBoundTimePoint": { "timeType": "INDEXED", "timezoneSource" :"CUSTOM", "zoneId": "US/Eastern", "indexReference": {"referenceType":"TODAY"}, "offset": {"days": -10} }, "upperBoundTimePoint": { "timeType": "INDEXED", "timezoneSource": "CUSTOM", "zoneId": "US/Eastern", "indexReference":{"referenceType":"NOW"} }, "type" :"TIME\_RANGED", "operationType" :"TIME\_RANGED" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`timeType`

 | 

`INDEXED`

 |
| 

`propertyParser`

 | 

Values include:

`VALUE`, `UPDATED AT`

*   If `VALUE` is selected, the comparison is the value of the property.
*   If `UPDATED_AT` is selected, the updated time of the property is used for comparison.

 |
| 

`lowerBoundEndpointBehavior`

 | 

`INCLUSIVE`

 |
| 

`upperBoundEndpointBehavior`

 | 

`INCLUSIVE`

 |
| 

`zoneID`

 | 

The account's default time zone. 

 |
| 

`operator`

 | 

The filter operator. Values inclue:

*   `IS_BETWEEN`, `IS_NOT_BETWEEN`

When the property is `IS_AFTER`, offset must be set at <=0.  

*   When the property is `IS_BEFORE`, offset must be set at >=0.

 |
| 

`indexReference`

 | 

 Values include: `{“referenceType”:”NOW”}`,`{“referenceType”:”TODAY”}`

*   If `indexReference` is equal to `{“referenceType”:”NOW”}`, `offset` must be >=0
*   If `indexReference` is equal to `{“referenceType”:”TODAY”}`, `offset` must be <=0

 |

Other validations: 

*   If `propertyParser` is `VALUE` and `operator` is `IS_BETWEEN`:
    *   `lowerBoundTimePoint.indexReference` should be `{“referenceType”:”NOW”}`.
    *   `upperBoundTimePoint.indexReference` should be `{“referenceType”:”TODAY”}`.
*   For all other combinations of `propertyParser` and `operator`:
    *   `lowerBoundTimePoint.indexReference` should be `{“referenceType”:”TODAY”}`.
    *   `upperBoundTimePoint.indexReference` should be `{“referenceType”:”NOW”}`.

#### DATE

{ "operator":"IS\_BETWEEN", "includeObjectsWithNoValueSet":false, "lowerBoundEndpointBehavior":"INCLUSIVE", "upperBoundEndpointBehavior":"INCLUSIVE", "propertyParser":"VALUE", "lowerBoundTimePoint":{ "timeType":"DATE", "timezoneSource":"CUSTOM", "zoneId":"US/Eastern", "year":2024, "month":1, "day":17, "hour":0, "minute":0, "second":0, "millisecond":0 }, "upperBoundTimePoint":{ "timeType":"DATE", "timezoneSource":"CUSTOM", "zoneId":"US/Eastern", "year":2024, "month":1, "day":17, "hour":23, "minute":59, "second":59, "millisecond":999 }, "type":"TIME\_RANGED", "operationType":"TIME\_RANGED" }

Use this table to describe parameters / fields
| Parameter | Accepted Values |
| --- | --- |
| 
`timeType`

 | 

`DATE`

 |
| 

`propertyParser`

 | 

Values include:

`VALUE`, `UPDATED AT`

*   If `VALUE` is selected, the comparison is the value of the property.
*   If `UPDATED_AT` is selected, the updated time of the property is used for comparison.

 |
| 

`lowerBoundEndpointBehavior`

 | 

`INCLUSIVE`

 |
| 

`upperBoundEndpointBehavior`

 | 

`INCLUSIVE`

 |
| 

`zoneID`

 | 

The account's default time zone. 

 |
| 

`operator`

 | 

The filter operator. Values include:

`IS_AFTER`, `IS_BEFORE`

*   The date must be a valid date.
*   In the `lowerBoundTimePoint` parameter, these fields must be set:
    *   `“hour”: 23`
    *   `“minute”: 59`
    *   `“second”: 59`
    *   `“millisecond”: 999`
*   In the `upperBoundTimePoint`, these fields must be set:
    *   `“hour”: 00`
    *   `“minute”: 00`
    *   `“second”: 00`
    *   `“millisecond”: 000`

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/list-filters-definitions#page-feedback)
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