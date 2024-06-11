---
title: "Fees in HubSpot CRM API"
description: "Guidelines and examples on creating, associating fees with quotes, and retrieving a list of created fees using the HubSpot CRM API."
type: "concept"
tags:
- "HubSpot"
- "CRM"
- "API"
- "Fees"
relationships:
- "#related_to [[Discounts]]"
- "#related_to [[Taxes]]"
- "#used_in [[Quote Creation]]"
- "#associated_with [[Pricing Details]]"
founded: "2014-05-01"
---

Fees
====

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

When you're [creating a quote in HubSpot](/docs/api/crm/quotes), you can create and associate a fee as part of the pricing details of the quote.

Create a fee[](https://developers.hubspot.com/docs/api/crm/fees#create-a-fee)
-----------------------------------------------------------------------------

Fees are used in conjunction with [discounts](/docs/api/crm/discounts) and [taxes](/docs/api/crm/taxes) when determining the pricing details for a quote. Any discounts you associate with your quote will be applied first, followed by associated fees, and then any associated taxes will apply.

To create a percentage fee:

// POST request to https://api.hubspi.com/crm/v3/objects/fee { "properties": { "hs\_label": "A percentage-based fee of 10%", "hs\_type": "PERCENT", "hs\_value": "10", } }

After you create a fee, you can use its ID to [associate it with a quote](/docs/api/crm/quotes#associate-discounts-fees-taxes). To retrieve a list of fees you've created, you can make a `GET` request to `/crm/v3/objects/fee`.

To view all available endpoints and their required fields, click the Endpoints tab at the top of this article.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/fees#page-feedback)
-------------------------------------------------------------------------------------

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