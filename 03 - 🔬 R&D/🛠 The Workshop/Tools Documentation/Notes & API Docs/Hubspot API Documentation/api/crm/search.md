Search 
=======

Use the CRM search endpoints to filter, sort, and search objects, records, and engagements across your CRM. For example, use the endpoints to get a list of contacts in your account, or a list of all open deals.

To use these endpoints from an app, a CRM scope is required. Refer to this [list of available scopes](/docs/api/working-with-oauth#scopes) to learn which granular CRM scopes can be used to accomplish your goal.

Make a search request[](https://developers.hubspot.com/docs/api/crm/search#make-a-search-request)
-------------------------------------------------------------------------------------------------

To search your CRM, make a `POST` request to the object's search endpoint. CRM search endpoints are constructed using the following format:

`/crm/v3/objects/{object}/search`

For example, the code snippet below would retrieve a list of all contacts with their `firstname` and `lastname` properties included:

// Example POST request to /crm/v3/objects/contacts/search { "properties": \["firstname", "lastname"\] }

To make a basic search returning only default properties with no additional filtering or sorting, include only an empty object in the request body, which is denoted by a JSON-formatted object with no inner fields included (i.e., `{}`).

### CRM Objects[](https://developers.hubspot.com/docs/api/crm/search#crm-objects)

The tables below contains the object search endpoints, the objects they refer to, and the properties that are returned by default. Learn more about [specifying returned properties](#specify-returned-properties).

Use this table to describe parameters / fields
| Search endpoint | Object | Default returned properties |
| --- | --- | --- |
| 
`/crm/v3/objects/companies/search`

 | Companies | 

`name`, `domain`, `createdate`,

`hs_lastmodifieddate`, `hs_object_id`

 |
| 

`/crm/v3/objects/contacts/search`

 | Contacts | 

`firstname`,`lastname`,`email`,`lastmodifieddate`,`hs_object_id`, `createdate`

 |
| 

`/crm/v3/objects/{objectType}/search`

 | Custom objects | 

`hs_createdate`,`hs_lastmodifieddate`,  
`hs_object_id`

 |
| 

`/crm/v3/objects/deals/search`

 | Deals | 

`dealname`, `amount`, `closedate,   ``pipeline`,`dealstage`, `createdate`, `hs_lastmodifieddate`, `hs_object_id`

 |
| 

`/crm/v3/objects/feedback_submissions/search`

 | Feedback submissions | 

`hs_createdate`,  
`hs_lastmodifieddate`,  
`hs_object_id`

 |
| 

`/crm/v3/objects/line_items/search`

 | Line items | 

`quantity`, `amount`, `price`, `createdate`, `hs_lastmodifieddate`, `hs_object_id`

 |
| 

`/crm/v3/objects/products/search`

 | Products | 

`name`, `description` ,`price`, `createdate`, `hs_lastmodifieddate`, `hs_object_id`

 |
| 

`/crm/v3/objects/quotes/search`

 | Quotes | 

`hs_expiration_date`, `hs_public_url_key`, `hs_status`,

`hs_title`, `hs_createdate`, `hs_lastmodifieddate`,

`hs_object_id`

 |
| 

`/crm/v3/objects/tickets/search`

 | Tickets | 

`content`, `hs_pipeline`, `hs_pipeline_stage`,

`hs_ticket_category`, `hs_ticket_priority`, `subject`,

`createdate`, `hs_lastmodifieddate`, `hs_object_id`

 |

### Engagements[](https://developers.hubspot.com/docs/api/crm/search#engagements)

The table below contains the engagement search endpoints, the engagements they refer to, and the properties that are returned by default. Learn more about [specifying returned properties](#specify-returned-properties).

Use this table to describe parameters / fields
| Search endpoint | Engagement | Default returned properties |
| --- | --- | --- |
| 
`/crm/v3/objects/calls/search`

 | Calls | 

`hs_createdate`,  
`hs_lastmodifieddate`,  
`hs_object_id`

 |
| 

`/crm/v3/objects/emails/search`

 | Emails | 

`hs_createdate`,  
`hs_lastmodifieddate`,  
`hs_object_id`

 |
| 

`/crm/v3/objects/meetings/search`

 | Meetings | 

`hs_createdate`,  
`hs_lastmodifieddate`,  
`hs_object_id`

 |
| 

`/crm/v3/objects/notes/search`

 | Notes | 

`hs_createdate`,  
`hs_lastmodifieddate`,  
`hs_object_id`

 |
| 

`/crm/v3/objects/tasks/search`

 | Tasks | 

`hs_createdate`,  
`hs_lastmodifieddate`,  
`hs_object_id`

 |

Filter search results[](https://developers.hubspot.com/docs/api/crm/search#filter-search-results)
-------------------------------------------------------------------------------------------------

Use filters in the request body to limit the results to only records with matching property values. For example, the request below searches for all contacts with a first name of _Alice._

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "filterGroups":\[ { "filters":\[ { "propertyName": "firstname", "operator": "EQ", "value": "Alice" } \] } \] }'

To include multiple filter criteria, you can group `filters` within `filterGroups`:

*   To apply _AND_ logic, include a comma separated list of conditions within one set of `filters`.
*   To apply _OR_ logic, include multiple `filters` within a `filterGroup`.

You can include a maximum of three `filterGroups` with up to three `filters` in each group.

For example, the request below searches for contacts with the first name `Alice` AND a last name other than `Smith`_,_ OR contacts that don't have a value for the property `email`. 

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "filterGroups": \[ { "filters": \[ { "propertyName": "firstname", "operator": "EQ", "value": "Alice" }, { "propertyName": "lastname", "operator": "NEQ", "value": "Smith" } \] }, { "filters": \[ { "propertyName": "email", "operator": "NOT\_HAS\_PROPERTY" } \] } \] }'

You can use operators in filters to specify which records should be returned. Values in filters are case-insensitive, with the exception of [the `IN` and `NOT_IN` operators](#in-operator) which require lowercase values. You can use the following operators in a filter:

Use this table to describe parameters / fields
| Operator | Description |
| --- | --- |
| 
`LT`

 | 

Less than

 |
| 

`LTE`

 | 

Less than or equal to

 |
| 

`GT`

 | 

Greater than

 |
| 

`GTE`

 | 

Greater than or equal to

 |
| 

`EQ`

 | 

Equal to

 |
| 

`NEQ`

 | 

Not equal to

 |
| 

`BETWEEN`

 | 

Within the specified range. In your request, use key-value pairs to set `highValue` and `value`. Refer to [the example below](#between-operator).

 |
| 

`IN`

 | 

Included within the specified list. In your request, include the list values in a `values` array. Inputted values must be in lowercase. Refer to [the example below](#in-operator).

 |
| 

`NOT_IN`

 | 

Not included within the specified list. In your request, include the list values in a `values` [array](#in-operator). Inputted values must be in lowercase.

 |
| 

`HAS_PROPERTY`

 | 

Has a value for the specified property

 |
| 

`NOT_HAS_PROPERTY`

 | 

Doesn't have a value for the specified property

 |
| 

`CONTAINS_TOKEN`

 | 

Contains a token. In your request, you can use wildcards (\*) to complete a partial search. For example, use the value `*@hubspot.com` to retrieve contacts with a HubSpot email address.

 |
| 

`NOT_CONTAINS_TOKEN`

 | 

Doesn't contain a token

 |

For example, you can use the `BETWEEN` operator to search for all tasks that were last modified within a specific time range:

curl https://api.hubapi.com/crm/v3/objects/tasks/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "filterGroups":\[{ "filters":\[ { "propertyName":"hs\_lastmodifieddate", "operator":"BETWEEN", "highValue": "1642672800000", "value":"1579514400000" } \] } \] }'

For another example, you can use the `IN` operator to search for all deals in specific stages of your pipeline: 

curl https://api.hubapi.com/crm/v3/objects/deals/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "filterGroups":\[{ "filters":\[ { "propertyName":"dealstage", "operator":"IN", "values": \["appointmentscheduled", "contractsent", "qualifiedtobuy"\] } \] } \] }'

Search through associations[](https://developers.hubspot.com/docs/api/crm/search#search-through-associations)
-------------------------------------------------------------------------------------------------------------

Search for records that are associated with other specific records by using the pseudo-property `associations.{objectType}`.

For example, the request below searches for all tickets associated with a contact that has the contact ID of `123`:

curl https://api.hubapi.com/crm/v3/objects/tickets/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "filters": \[ { "propertyName": "associations.contact", "operator": "EQ", "value": "123" } \] }'

You can search through associations by using the following pseudo-property values:

*   `associations.company`
*   `associations.contact`
*   `associations.ticket`
*   `associations.deal`
*   `associations.quote`

**Please note:** the option to search through custom object associations is not currently supported via search endpoints. To find custom object associations, you can use the [associations API](/docs/api/crm/associations).

Sort search results[](https://developers.hubspot.com/docs/api/crm/search#sort-search-results)
---------------------------------------------------------------------------------------------

Use a sorting rule in the request body to list results in ascending or descending order. Only one sorting rule can be applied to any search.

For example, the request below sorts returned contacts with most recently created first:

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "sorts": \[ { "propertyName": "createdate", "direction": "DESCENDING" } \] }'

Search default searchable properties[](https://developers.hubspot.com/docs/api/crm/search#search-default-searchable-properties)
-------------------------------------------------------------------------------------------------------------------------------

Search all default text properties in records of the specified object to find all records that have a value containing the specified string. By default, the results will be returned in order of object creation (oldest first), but you can override this with [sorting](#sorting).

For example, the request below searches for all contacts with a default text property value containing the letter `X`.

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "query": "x" }'

Below are the properties that are searched by default through the above method:

Use this table to describe parameters / fields
| Search endpoint | Object | Default searchable properties |
| --- | --- | --- |
| 
`/crm/v3/objects/calls/search`

 | Calls | 

`hs_call_title`, `hs_body_preview`

 |
| 

`/crm/v3/objects/companies/search`

 | Companies | 

`website`, `phone`, `name`, `domain`

 |
| 

`/crm/v3/objects/contacts/search`

 | Contacts | 

`firstname`,`lastname`,`email`,`phone`,`hs_additional_emails`, `fax`, `mobilephone`, `company`, `hs_marketable_until_renewal`

 |
| 

`/crm/v3/objects/{objectType}/search`

 | Custom objects | 

All custom object properties are searchable by default

 |
| 

`/crm/v3/objects/deals/search`

 | Deals | 

`dealname`,`pipeline`,`dealstage`, `description`, `dealtype`

 |
| 

`/crm/v3/objects/emails/search`

 | Emails | 

`hs_email_subject`

 |
| 

`/crm/v3/objects/feedback_submissions/search`

 | Feedback submissions | 

`hs_submission_name`, `hs_content`

 |
| 

`/crm/v3/objects/meetings/search`

 | Meetings | 

`hs_meeting_title`, `hs_meeting_body`

 |
| 

`/crm/v3/objects/notes/search`

 | Notes | 

`hs_note_body`

 |
| 

`/crm/v3/objects/products/search`

 | Products | 

`name`, `description` ,`price`, `hs_sku`

 |
| 

`/crm/v3/objects/quotes/search`

 | Quotes | 

`hs_sender_firstname`, `hs_sender_lastname`, `hs_proposal_slug`, `hs_title`, `hs_sender_company_name`, `hs_sender_email`, `hs_quote_number`, `hs_public_url_key`

 |
| 

`/crm/v3/objects/tasks/search`

 | Tasks | 

`hs_task_body`, `hs_task_subject`

 |
| 

`/crm/v3/objects/tickets/search`

 | Tickets | 

`subject`, `content`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_id`

 |
| 

`/crm/v3/objects/line_items/search`

 | Line items | 

There are no default searchable properties for line items

 |

Specify returned properties[](https://developers.hubspot.com/docs/api/crm/search#specify-returned-properties)
-------------------------------------------------------------------------------------------------------------

Each request will return a default set of properties in its search results for the requested object. You can override this by providing an array of specific property names in the `properties` parameter of your request body. 

For example, the request below searches all contacts and will return their email and state:

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "properties": \[ "email", "state" \] }'

Paging through results
----------------------

By default, the search endpoints will return pages of 10 records at a time. This can be changed by setting the `limit` parameter in the request body. The maximum number of supported objects per page is 100.

For example, the request below would return pages containing 20 results each.

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "limit": 20 }

To access the next page of results, you must pass an `after` parameter provided in the `paging.next.after` property of the previous response. If the `paging.next.after` property isn’t provided, there are no additional results to display. You must format the value in the `after` parameter as an integer.

For example, the request below would return the next page of results:

curl https://api.hubapi.com/crm/v3/objects/contacts/search \\ --request POST \\ --header "Content-Type: application/json" \\ --data '{ "after": "20" }'

Limitations[](https://developers.hubspot.com/docs/api/crm/search#limitations)
-----------------------------------------------------------------------------

*   It may take a few moments for newly created or updated CRM objects to appear in search results.
*   Archived CRM objects won’t appear in any search results.
*   The search endpoints are [rate limited](/docs/api/usage-details) to four requests per second.
*   A query can contain a maximum of 3,000 characters. If the body of your request exceeds 3,000 characters, a 400 error will be returned.
*   The search endpoints are limited to 10,000 total results for any given query. Attempting to page beyond 10,000 will result in a 400 error.
*   When searching for phone numbers, HubSpot uses special calculated properties to standardize the format. These properties all start with `hs_searchable_calculated_*`. As a part of this standardization, HubSpot only uses the area code and local number. You should refrain from including the country code in your search or filter criteria.  
    

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/search#page-feedback)
---------------------------------------------------------------------------------------

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