Tasks
=====

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

Use the tasks API to create and manage tasks. You can create tasks [in HubSpot](https://knowledge.hubspot.com/contacts/manually-log-a-call-email-or-meeting-on-a-record) or via the tasks API. 

Below, learn the basic methods of managing tasks through the API. To view all available endpoints and their requirements, click the Endpoints tab at the top of this article.

Create a task
-------------

To create a task, make a `POST` request to `/crm/v3/objects/tasks`.

In the request body, add task details in a properties object. You can also add an associations object to associate your new task with an existing record (e.g., contacts, companies).

### Properties[](https://developers.hubspot.com/docs/api/crm/tasks#properties)

In the properties object, you can include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`hs_timestamp`

 | 

Required. This field marks the task's due date. You can use either a Unix timestamp in milliseconds or UTC format. 

 |
| 

`hs_task_body`

 | 

The task [notes.](https://knowledge.hubspot.com/tasks/create-tasks#task-details)

 |
| 

`hubspot_owner_id`

 | 

The [owner ID](/docs/api/crm/owners) of the user assigned to the task.

 |
| 

`hs_task_subject`

 | 

The title of the task. 

 |
| 

`hs_task_status`

 | 

The status of the task, either `COMPLETED` or `NOT_STARTED`.

 |
| 

`hs_task_priority`

 | 

The priority of the task. Values include `LOW`, `MEDIUM`, or `HIGH`.

 |
| 

`hs_task_type`

 | 

The type of task. Values include `EMAIL`, `CALL`, or `TODO`.

 |
| 

`hs_task_reminders`

 | 

The timestamp for when to send a reminder for the due date of the task. You must use Unix timestamp in milliseconds.

 |

### Associations[](https://developers.hubspot.com/docs/api/crm/tasks#associations)

To create and associate a task with existing records, include an associations object in your request. The object should include the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`toObjectId`

 | 

The ID of the record that you want to associate the task with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the task and the other object. You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, to create a task and associate it with two contacts, your request body might look similar to the following:

// Example request body { "properties": { "hs\_timestamp": "2019-10-30T03:30:17.883Z", "hs\_task\_body": "Send Proposal", "hubspot\_owner\_id": "64492917", "hs\_task\_subject": "Follow-up for Brian Buyer", "hs\_task\_status": "WAITING", "hs\_task\_priority": "HIGH", "hs\_task\_type":"CALL" }, "associations": \[ { "to": { "id": 101 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 204 } \] }, { "to": { "id": 102 }, "types": \[ { "associationCategory": "HUBSPOT\_DEFINED", "associationTypeId": 204 } \] }\] }

Learn more about batch creating tasks by clicking the Endpoints tab at the top of this article.

Retrieve tasks[](https://developers.hubspot.com/docs/api/crm/tasks#retrieve-tasks)
----------------------------------------------------------------------------------

You can retrieve tasks individually or in bulk. Learn more about batch retrieval by clicking the Endpoints tab at the top of this article.

To retrieve an individual task by its task ID, make a `GET` request to `/crm/v3/objects/tasks/{taskId}`. You can also include the following parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`properties`

 | 

A comma separated list of the properties to be returned. 

 |
| 

`associations`

 | 

A comma separated list of object types to retrieve associated IDs for. Any specified associations that don't exist will not be returned in the response. Learn more about the [associations API.](/docs/api/crm/associations)

 |

To request a list of all of tasks, make a `GET` request to `crm/v3/objects/tasks`. You can include the following parameters in the request URL: 

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`limit`

 | 

The maximum number of results to display per page.

 |
| 

`properties`

 | 

A comma separated list of the properties to be returned. 

 |

Update tasks[](https://developers.hubspot.com/docs/api/crm/tasks#update-tasks)
------------------------------------------------------------------------------

You can update tasks individually or in batches. To update an individual task by its task ID, make a `PATCH` request to `/crm/v3/objects/tasks/{taskId}`. 

In the request body, include the task properties that you want to update. For example, your request body might look similar to the following:

//Example PATCH request to https://api.hubspot.com/crm/v3/objects/tasks/{taskId} { "properties": { "hs\_timestamp": "2019-10-30T03:30:17.883Z", "hs\_task\_body": "Send Proposal", "hubspot\_owner\_id": "64492917", "hs\_task\_subject": "Close deal", "hs\_task\_status": "COMPLETED", "hs\_task\_priority": "HIGH" } }

HubSpot will ignore values for read-only and non-existent properties. To clear a property value, pass an empty string for the property in the request body.

Learn more about batch updating by clicking the Endpoints tab at the top of this article.

### Associate existing tasks with records[](https://developers.hubspot.com/docs/api/crm/tasks#associate-existing-tasks-with-records)

To associate an existing task with records (e.g., contacts, deals, etc.), make a `PUT` request to `/crm/v3/objects/tasks/{taskId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`. The request URL should contains the following fields:

Use this table to describe parameters / fields
| Field | Description |
| --- | --- |
| 
`taskId`

 | 

The ID of the task.

 |
| 

`toObjectType`

 | 

The type of object that you want to associate the task with (e.g., contact or company)

 |
| 

`toObjectId`

 | 

The ID of the record that you want to associate the task with.

 |
| 

`associationTypeId`

 | 

A unique identifier to indicate the association type between the task and the other object. The ID can be represented numerically or in snake case (e.g., `task_to_contact`). You can retrieve the value through the [associations API](/docs/api/crm/associations/v4).

 |

For example, your request URL might look similar to the following:

`https://api.hubspot.com/crm/v3/objects/tasks/17687016786/associations/contacts/104901/204`

### Remove an association

To remove an association between a task and a record, make a `DELETE` request to the same URL as above:

`/crm/v3/objects/tasks/{taskId}/associations/{toObjectType}/{toObjectId}/{associationTypeId}`

Pin a task on a record[](https://developers.hubspot.com/docs/api/crm/tasks#pin-a-task-on-a-record)
--------------------------------------------------------------------------------------------------

You can [pin a task](https://knowledge.hubspot.com/records/pin-an-activity-on-a-record) on a record so it remains on the top of the record's timeline. The task must already be associated with the record prior to pinning, and you an only pin one activity per record. To pin a task, include the task's `id` in the `hs_pinned_engagement_id` field when creating or updating a record via the object APIs. Learn more about using the [companies,](/docs/api/crm/companies#pin-an-activity-on-a-company-record)[contacts](/docs/api/crm/contacts#pin-an-activity-on-a-contact-record), [deals](/docs/api/crm/deals#pin-an-activity-on-a-deal-record), [tickets](/docs/api/crm/tickets#pin-an-activity-on-a-ticket-record), and [custom objects](/docs/api/crm/crm-custom-objects) APIs.

Delete tasks[](https://developers.hubspot.com/docs/api/crm/tasks#delete-tasks)
------------------------------------------------------------------------------

You can delete tasks individually or in batches, which will add the task to the recycling bin in HubSpot. You can later [restore the task from the record timeline](https://knowledge.hubspot.com/crm-setup/restore-deleted-activity-in-a-record).

To delete an individual task by its task ID, make a `DELETE` request to `/crm/v3/objects/tasks/{taskId}`.

Learn more about batch deleting by clicking the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/tasks#page-feedback)
--------------------------------------------------------------------------------------

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