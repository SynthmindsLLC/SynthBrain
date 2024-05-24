Pipelines
=========

Run in Postman (function (p,o,s,t,m,a,n) { !p\[s\] && (p\[s\] = function () { (p\[t\] || (p\[t\] = \[\])).push(arguments); }); !o.getElementById(s+t) && o.getElementsByTagName("head")\[0\].appendChild(( (n = o.createElement("script")), (n.id = s+t), (n.async = 1), (n.src = m), n )); }(window, document, "\_pm", "PostmanRunObject", "https://run.pstmn.io/button.js"));

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, a pipeline is where deal stages or or ticket statuses are set. For sales, pipelines can be used to predict revenue and identify roadblocks. For service, pipelines can be used to manage ticket statuses and analyze blockers. 

Each stage in a pipeline is identified by a unique internal ID, meaning it can only be a member of one pipeline. Each pipeline always has at least one stage, and each account has at least one pipeline.

### Default pipelines

Every account initially contains a default pipeline with the `pipelineId` “default.” On accounts with a single pipeline, the pipeline property for any object will automatically be set to “default” as well. On accounts with multiple pipelines, if you're setting a stage that isn’t in the default pipeline, you'll also need to set the corresponding pipeline property.

### Multiple pipelines

Only Sales Hub Professional or Enterprise accounts can create [multiple deal pipelines](https://knowledge.hubspot.com/deals/set-up-and-customize-your-deal-pipelines-and-deal-stages).

Similarly, you must have a Service Hub Professional or Enterprise subscription to create multiple [ticket pipelines](https://knowledge.hubspot.com/tickets/customize-ticket-pipelines-and-statuses). 

Learn more about HubSpot’s subscription levels [here](https://legal.hubspot.com/hubspot-product-and-services-catalog?_ga=2.8754549.1572367158.1578321647-500942594.1573763828#ServiceHub).

**Example use cases:** When working with deals, an account might have one pipeline for “New Sales" and another for “Contract Renewals." For tickets, you might have a main support queue and a separate one for escalations. Each of those queues would be a separate ticket pipeline. The pipelines endpoints can be used to sync one pipeline or another to an external CRM.

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/pipelines#page-feedback)
------------------------------------------------------------------------------------------

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