---
title: "Associations v4"
description: "Associations represent the relationships between objects and activities in the HubSpot CRM."
type: "group"
tags:
- "CRM"
- "HubSpot"
- "Association Types"
relationships:
- "#part_of [[CRM]]"
- "#related_to [[Record Associations]]"
birthdate: "null"
deathdate: "null"
---

Associations v4
===============

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

For the previous version, please see the documentation for the [v3 Associations API](/docs/api/crm/associations/v3).

[Overview](#tab-1)[Association endpoints](#tab-2)[Association schema endpoints](#tab-3)

*   [Overview](#tab-1)
*   [Association endpoints](#tab-2)
*   [Association schema endpoints](#tab-3)

Associations represent the relationships between objects and activities in the HubSpot CRM. Record associations can exist between records of different objects (e.g., Contact to Company), as well as within the same object (e.g., Company to Company). You can use the associations endpoints to create, retrieve, update, or delete associations between records, or records and activities.

The association schema endpoints allow you to view the supported types of associations in your account, as well as create your own association types, and assign labels to your record relationships. Association labels are supported between contacts, companies, deals, tickets, and custom objects, and can be [used across HubSpot in tools](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels#use-association-labels-in-hubspot-tools), such as lists and workflows.

Learn more about objects, records, properties, and associations APIs in the [Understanding the CRM](https://developers.hubspot.com/docs-beta/crm/understanding-the-crm?_ga=2.21847609.341006870.1586180142-500942594.1573763828) guide. 

**Please note**: the v4 Associations API is supported in Version 9.0.0 or later of the NodeJS HubSpot Client.

HubSpot defined association types[](https://developers.hubspot.com/docs/api/crm/associations#hubspot-defined-association-types)
-------------------------------------------------------------------------------------------------------------------------------

HubSpot provides a set of predefined association types (e.g., unlabeled contact to company), but account admins can [define their own association labels](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) to provide additional context for record relationships (e.g., manager and employee). There are two HubSpot-defined association types: 

*   **Primary:** the main company that the other record is associated with. Primary associations can be used in HubSpot tools such as [lists and workflows](https://knowledge.hubspot.com/crm-setup/associations-enhancements-beta#use-associations-in-hubspot-tools). For records with multiple associated companies, this API supports changing which company is considered the primary.
*   **Unlabeled:** an association type added when any contact, company, deal, ticket, or custom object record is associated. This type denotes that an association exists, and will always returned in responses with a **label** value of `**null**`. When a record has a primary association or a custom association label, those types will be listed alongside the unlabeled association type.

You can view all of the HubSpot-defined association types in [this section](#association-type-ids).

Single vs. paired labels[](https://developers.hubspot.com/docs/api/crm/associations#single-vs-paired-labels)
------------------------------------------------------------------------------------------------------------

There are two types of [association labels](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) you can use to describe the relationships between records:

*   **Single:** one label that applies to both records in the relationship. For example, _Friend_ or _Colleague_. 
*   **Paired**: a pair of labels for when different words are used to describe each side of the associated records' relationship. For example, _Parent_ and _Child_ or _Employer_ and _Employee_. To create paired labels, you must include the `inverseLabel` field in your request to name the second label in the pair.  
    

Create association types[](https://developers.hubspot.com/docs/api/crm/associations#create-association-types)
-------------------------------------------------------------------------------------------------------------

You can create custom association types either [in HubSpot](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels) or through the association schema API endpoint. You can create up to 10 association types between each object pairing (e.g. contacts and companies, contacts and contacts).

To create an association type through the API, make a `POST` request to `/crm/v4/associations/{fromObjectType}/{toObjectType}/labels` and include the following in your request:

*   **name**: the internal name of the association type. This value cannot include hyphens or begin with a numerical character.
*   label: the name of the [association label as shown in HubSpot](https://knowledge.hubspot.com/crm-setup/create-and-use-association-labels).
*   **inverseLabel** (paired labels only): the name of the second label in the pair of labels.

For example, your request could look similar to the following:

///Example request body - Single label { "label": "Partner", "name": "partner" }

///Example request body - Paired labels { "label": "Manager", "inverseLabel": "Employee", "name": "manager\_employee" }

Retrieve association types[](https://developers.hubspot.com/docs/api/crm/associations#retrieve-association-types)
-----------------------------------------------------------------------------------------------------------------

To view the association types between specific objects, make a `GET` request to

`/crm/v4/associations/{fromObjectType}/{toObjectType}/labels`. 

You'll receive an array, each item containing:

*   **category:** whether the association type was created by HubSpot (`HUBSPOT_DEFINED`) or by a user (`USER_DEFINED`).
*   **typeId:** the numeric ID for that association type. This is used to [set a label when associating records](#associate-with-label). Refer to [this list](#association-type-ids) for all the HubSpot defined `typeId` values.
*   **label:** the alphanumeric label. This will be `null` for the unlabeled association type.

You can also find these values in HubSpot [in your association settings](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels#association-label-api-details).

Associate records[](https://developers.hubspot.com/docs/api/crm/associations#associate-records)
-----------------------------------------------------------------------------------------------

### Associate records without a label

You can create a default unlabeled association between two records, or set up unlabeled associations for records in bulk. To set up an individual default association between two records, make a `PUT` request to `/crm/v4​/objects​/{fromObjectType}​/{fromObjectId}​/associations​/default​/{toObjectType}​/{toObjectId}`.

In the request URL, include:

*   **fromObjectType:** the ID of the object you're associating. To find the ID values, refer to this [list of object type IDs,](/docs/api/crm/understanding-the-crm#object-type-id) or for contacts, companies, deals, tickets, and notes, you can use the object name (e.g., `contact`, `company`).
*   **fromObjectId:** the ID of the record to associate.
*   **toObjectType:** the ID of the object you're associating the record to. To find the ID values, refer to this [list of object type IDs,](/docs/api/crm/understanding-the-crm#object-type-id) or for contacts, companies, deals, tickets, and notes, you can use the object name (e.g., `contact`, `company`).
*   **toObjectId:** the ID of the record to associate to.

For example, to associate a contact record whose ID is 12345 with a company record whose ID is 67891, your request URL would be: `/crm/v4​/objects​/contact​/12345​/associations​/default​/company​/67891`.

To set up default associations in bulk, make a `POST` request to `crm/v4/associations/{fromObjectType}/{toObjectType}/batch/associate/default`. In the request body, include `objectId` values for the records you want to associate. 

**Please note**: the number of associations a record can have depends on [the object and your HubSpot subscription.](https://legal.hubspot.com/hubspot-product-and-services-catalog#TechnicalLimits:~:text=CRM%20Record%20Association%20Limits)

### Associate records with a label[](https://developers.hubspot.com/docs/api/crm/associations#associate-records-with-a-label)

To associate two records and set a label to describe the association, make a `PUT` request to `/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}`. In the request body, include the `associationCategory` and `associationTypeId` to indicate the type of association you want to create.

If you're creating unlabeled associations, you can use the default endpoints outlined in the [section above](#default-association) which don't require the `associationCategory` or `associationTypeId`. If you're creating associations with a label, you can refer to this [list of default type IDs](#association-type-ids), or you'll need to retrieve the custom association types between those objects.

**Please note**: for cross-object and paired label relationships, ensure you use the `typeId` that refers to the correct direction (e.g., Contact to Company vs. Company to Contact, Employee to Manager vs. Manager to Employee).

For example, to associate a contact with a deal using a custom label:

1\. Make a `GET` request to `/crm/v4/associations/contact/deal/labels`.

2\. In the response, look at the `typeId` and `category` values for the label. The ID will be a number (e.g., `36`), and the category will always be `USER_DEFINED` for custom labels.

3\. Make a `PUT` request to `/crm/v4/objects/contact/{objectId}/associations/deal/{toObjectId}`with the following request body:

/// Example request body \[    {    "associationCategory": "USER\_DEFINED",    "associationTypeId": 36   } \]

Report on high association usage[](https://developers.hubspot.com/docs/api/crm/associations#report-on-high-association-usage)
-----------------------------------------------------------------------------------------------------------------------------

There are [limits to the number of associations a record can have](https://legal.hubspot.com/hubspot-product-and-services-catalog?_ga=2.95538523.610503737.1661771772-184632701.1661771771#TechnicalLimits:~:text=CRM%20Record%20Association%20Limits). You can use the associations API to retrieve a report of records that are either approaching or have hit the maximum limit for associations.

To retrieve the report, make a `POST` request to `crm/v4/associations/usage/high-usage-report/{userID}`. The file includes records using 80% or more of their association limit. For example, if a company can be associated with up to 50,000 contacts, the company will be included in the file if it has 40,000 or more associated contacts. The file will be sent to the email of the user whose ID was included in the request URL. Learn how to retrieve user IDs with the [users API](/docs/api/settings/user-provisioning).

Association type ID values[](https://developers.hubspot.com/docs/api/crm/associations#association-type-id-values)
-----------------------------------------------------------------------------------------------------------------

The following tables include the HubSpot-defined `associationTypeId` values that specify the type of association. Association types vary depending on the included objects and the direction of the association (e.g., Contact to Company is different from Company to Contact). If you create custom objects or custom association labels, the related association types will have unique `typeId` values that you'll need to [retrieve](#retrieve-association-type) or locate in your [association settings in HubSpot](https://knowledge.hubspot.com/object-settings/create-and-use-association-labels#association-label-api-details).

**Please note**: default company association types include an unlabeled association type and a primary association type. If a record has more than one associated company, only one can be the primary company. The other associations can either be unlabelled or have custom association labels.

### Contact to object[](https://developers.hubspot.com/docs/api/crm/associations#contact-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`449`

 | 

Contact to contact

 |
| 

`279`

 | 

Contact to company

 |
| 

`1`

 | 

Contact to company (Primary)

 |
| 

`4`

 | 

Contact to deal

 |
| 

`15`

 | 

Contact to ticket

 |
| 

`193`

 | 

Contact to call

 |
| 

`197`

 | 

Contact to email

 |
| 

`199`

 | 

Contact to meeting

 |
| 

`201`

 | 

Contact to note

 |
| 

`203`

 | 

Contact to task

 |
| 

`82`

 | 

Contact to communication (SMS, WhatsApp, or LinkedIn message)

 |
| 

`454`

 | 

Contact to postal mail

 |
| 

`587`

 | 

Contact to cart

 |
| 

`508`

 | 

Contact to order

 |
| 

`178`

 | 

Contact to invoice

 |
| 

`388`

 | 

Contact to payment

 |
| 

`296`

 | 

Contact to subscription

 |

### Company to object[](https://developers.hubspot.com/docs/api/crm/associations#company-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`450`

 | 

Company to company

 |
| 

`14`

 | 

Child to parent company

 |
| 

`13`

 | 

Parent to child company

 |
| 

`280`

 | 

Company to contact

 |
| 

`2`

 | 

Company to contact (Primary)

 |
| 

`342`

 | 

Company to deal

 |
| 

`6`

 | 

Company to deal (Primary)

 |
| 

`340`

 | 

Company to ticket

 |
| 

`25`

 | 

Company to ticket (Primary)

 |
| 

`181`

 | 

Company to call

 |
| 

`185`

 | 

Company to email

 |
| 

`187`

 | 

Company to meeting

 |
| 

`189`

 | 

Company to note

 |
| 

`191`

 | 

Company to task

 |
| 

`88`

 | 

Company to communication (SMS, WhatsApp, or LinkedIn message)

 |
| 

`460`

 | 

Company to postal mail

 |
| 

`180`

 | 

Company to invoice

 |
| 

`510`

 | 

Company to order

 |
| 

`390`

 | 

Company to payment

 |
| 

`298`

 | 

Company to subscription

 |

### Deal to object[](https://developers.hubspot.com/docs/api/crm/associations#deal-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`451`

 | 

Deal to deal

 |
| 

`3`

 | 

Deal to contact

 |
| 

`341`

 | 

Deal to company

 |
| 

`5`

 | 

Deal to company (Primary)

 |
| 

`27`

 | 

Deal to ticket

 |
| 

`205`

 | 

Deal to call

 |
| 

`209`

 | 

Deal to email

 |
| 

`211`

 | 

Deal to meeting

 |
| 

`213`

 | 

Deal to note

 |
| 

`215`

 | 

Deal to task

 |
| 

`86`

 | 

Deal to communication (SMS, WhatsApp, or LinkedIn message)

 |
| 

`458`

 | 

Deal to postal mail

 |
| 

`313`

 | 

Deal to deal split

 |
| 

`19`

 | 

Deal to line item

 |
| 

`176`

 | 

Deal to invoice

 |
| 

`511`

 | 

Deal to order

 |
| 

`392`

 | 

Deal to payment

 |
| 

`630`

 | 

Deal to product

 |
| 

`63`

 | 

Deal to quote

 |
| 

`300`

 | 

Deal to subscription

 |

### Ticket to object[](https://developers.hubspot.com/docs/api/crm/associations#ticket-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`452`

 | 

Ticket to ticket

 |
| 

`16`

 | 

Ticket to contact

 |
| 

`339`

 | 

Ticket to company

 |
| 

`26`

 | 

Ticket to company (Primary)

 |
| 

`28`

 | 

Ticket to deal

 |
| 

`219`

 | 

Ticket to call

 |
| 

`223`

 | 

Ticket to email

 |
| 

`225`

 | 

Ticket to meeting

 |
| 

`227`

 | 

Ticket to note

 |
| 

`229`

 | 

Ticket to task

 |
| 

`84`

 | 

Ticket to communication (SMS, WhatsApp, or LinkedIn message)

 |
| 

`456`

 | 

Ticket to postal mail

 |
| 

`32`

 | 

Ticket to thread

 |
| 

`278`

 | 

Ticket to conversation

 |
| 

`526`

 | 

Ticket to order

 |

### Lead to object[](https://developers.hubspot.com/docs/api/crm/associations#lead-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`578`

 | 

Lead to primary contact

 |
| 

`596`

 | 

Lead to call

 |
| 

`598`

 | 

Lead to email

 |
| 

`600`

 | 

Lead to meeting

 |
| 

`602`

 | 

Lead to communication

 |
| 

`608`

 | 

Lead to contact

 |
| 

`610`

 | 

Lead to company

 |
| 

`646`

 | 

Lead to task

 |

### Call to object[](https://developers.hubspot.com/docs/api/crm/associations#call-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`194`

 | 

Call to contact

 |
| 

`182`

 | 

Call to company

 |
| 

`206`

 | 

Call to deal

 |
| 

`220`

 | 

Call to ticket

 |

### Email to object[](https://developers.hubspot.com/docs/api/crm/associations#email-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`198`

 | 

Email to contact

 |
| 

`186`

 | 

Email to company

 |
| 

`210`

 | 

Email to deal

 |
| 

`224`

 | 

Email to ticket

 |

### Meeting to object[](https://developers.hubspot.com/docs/api/crm/associations#meeting-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`200`

 | 

Meeting to contact

 |
| 

`188`

 | 

Meeting to company

 |
| 

`212`

 | 

Meeting to deal

 |
| 

`226`

 | 

Meeting to ticket

 |

### Note to object[](https://developers.hubspot.com/docs/api/crm/associations#note-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`202`

 | 

Note to contact

 |
| 

`190`

 | 

Note to company

 |
| 

`214`

 | 

Note to deal

 |
| 

`228`

 | 

Note to ticket

 |

### Postal mail to object[](https://developers.hubspot.com/docs/api/crm/associations#postal-mail-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`453`

 | 

Postal mail to contact

 |
| 

`459`

 | 

Postal mail to company

 |
| 

`457`

 | 

Postal mail to deal

 |
| 

`455`

 | 

Postal mail to ticket

 |

### Quote to object[](https://developers.hubspot.com/docs/api/crm/associations#quote-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`69`

 | 

Quote to contact

 |
| 

`71`

 | 

Quote to company

 |
| 

`64`

 | 

Quote to deal

 |
| 

`67`

 | 

Quote to line item

 |
| 

`286`

 | 

Quote to quote template

 |
| 

`362`

 | 

Quote to discount

 |
| 

`364`

 | 

Quote to fee

 |
| 

`366`

 | 

Quote to tax

 |
| 

`702`

 | 

Contact signer (for e-signatures)

 |
| 

`733`

 | 

Quote to cart

 |
| 

`408`

 | 

Quote to invoice

 |
| 

`731`

 | 

Quote to order

 |
| 

`398`

 | 

Quote to payment

 |
| 

`304`

 | 

Quote to subscription

 |

### Task to object[](https://developers.hubspot.com/docs/api/crm/associations#task-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`204`

 | 

Task to contact

 |
| 

`192`

 | 

Task to company

 |
| 

`216`

 | 

Task to deal

 |
| 

`230`

 | 

Task to ticket

 |

### Communication (SMS, WhatsApp, or LinkedIn message) to object[](https://developers.hubspot.com/docs/api/crm/associations#communication-sms-whatsapp-or-linkedin-message-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`81`

 | 

Communication (SMS, WhatsApp, or LinkedIn Message) to contact

 |
| 

`87`

 | 

Communication (SMS, WhatsApp, or LinkedIn Message) to company

 |
| 

`85`

 | 

Communication (SMS, WhatsApp, or LinkedIn Message) to deal

 |
| 

`83`

 | 

Communication (SMS, WhatsApp, or LinkedIn Message) to ticket

 |

### Order to object[](https://developers.hubspot.com/docs/api/crm/associations#order-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`593`

 | 

Order to cart

 |
| 

`507`

 | 

Order to contact

 |
| 

`509`

 | 

Order to company

 |
| 

`512`

 | 

Order to deal

 |
| 

`519`

 | 

Order to discount

 |
| 

`521`

 | 

Order to discount code

 |
| 

`518`

 | 

Order to invoice

 |
| 

`513`

 | 

Order to line item

 |
| 

`523`

 | 

Order to payment

 |
| 

`730`

 | 

Order to quote

 |
| 

`516`

 | 

Order to subscription

 |
| 

`726`

 | 

Order to task

 |
| 

`525`

 | 

Order to ticket

 |

### Cart to object[](https://developers.hubspot.com/docs/api/crm/associations#cart-to-object)

Use this table to describe parameters / fields
| TYPE ID | Association type |
| --- | --- |
| 
`586`

 | 

Cart to contact

 |
| 

`588`

 | 

Cart to discount

 |
| 

`590`

 | 

Cart to line item

 |
| 

`592`

 | 

Cart to order

 |
| 

`732`

 | 

Cart to quote

 |
| 

`728`

 | 

Cart to task

 |
| 

`594`

 | 

Cart to ticket

 |

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/associations#page-feedback)
---------------------------------------------------------------------------------------------

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