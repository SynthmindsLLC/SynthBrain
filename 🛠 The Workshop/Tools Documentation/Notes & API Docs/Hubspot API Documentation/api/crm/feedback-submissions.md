**Please note:** this API is currently under development and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to HubSpot's [Developer Terms](https://legal.hubspot.com/developer-terms) & [Developer Beta Terms](https://legal.hubspot.com/developerbetaterms?). You also acknowledge and understand the risk associated with testing an unstable API.

Feedback Submissions (BETA)
===========================

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

In HubSpot, feedback submissions store information submitted to a feedback survey. Surveys in HubSpot include [Net Promoter Score (NPS)](https://knowledge.hubspot.com/customer-feedback/how-do-i-send-a-customer-loyalty-survey), [Customer Satisfaction (CSAT)](https://knowledge.hubspot.com/customer-feedback/create-and-send-customer-satisfaction-surveys), [Customer Effort Score (CES)](https://knowledge.hubspot.com/customer-feedback/how-do-i-send-a-customer-support-survey), and [custom surveys](https://knowledge.hubspot.com/customer-feedback/create-a-custom-survey). Using the feedback submission endpoints, you can retrieve submission data about your feedback surveys.

Learn more about objects, properties, and associations APIs in the [Understanding the CRM](https://developers.hubspot.com/docs-beta/crm/understanding-the-crm?_ga=2.21847609.341006870.1586180142-500942594.1573763828) guide.

**Please note**: the feedback submissions endpoints are currently read only. Feedback submissions cannot be submitted or edited through the API. 

Retrieve feedback survey submissions[](https://developers.hubspot.com/docs/api/crm/feedback-submissions#retrieve-feedback-survey-submissions)
---------------------------------------------------------------------------------------------------------------------------------------------

To view details about your feedback survey submissions, you can retrieve submission data in bulk for multiple surveys, or for an individual survey. For example, you can use the API to see all survey responses for a specific NPS survey.

To retrieve submissions, make a `GET` request to `/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}`. By default, the following properties are returned for each submission: `hs_createdate`, `hs_lastmodifieddate`, and `hs_object_id`, but you also can retrieve additional [properties](https://knowledge.hubspot.com/customer-feedback/feedback-submission-properties).

For example, to retrieve survey submissions with the source and sentiment of the submissions, your request URL would look like: `https://api.hubspot.com/crm/v3/objects/feedback_submissions?properties=hs_sentiment,hs_survey_channel`.

Feedback submission properties[](https://developers.hubspot.com/docs/api/crm/feedback-submissions#feedback-submission-properties)
---------------------------------------------------------------------------------------------------------------------------------

Feedback submissions have [default properties](https://knowledge.hubspot.com/customer-feedback/feedback-submission-properties#default-feedback-submission-properties) that contain information about the survey, submission answers, and the date the survey was submitted. You can also [create custom submissions properties](https://knowledge.hubspot.com/customer-feedback/feedback-submission-properties#custom-feedback-submission-properties). 

Feedback submissions properties cannot be created or edited via API. You can only create properties in the [feedback surveys tool within HubSpot](https://knowledge.hubspot.com/customer-feedback/create-a-custom-survey#survey), and the properties cannot be edited after creation.

Associations[](https://developers.hubspot.com/docs/api/crm/feedback-submissions#associations)
---------------------------------------------------------------------------------------------

Feedback submissions can be associated with contact and ticket records. Learn how to associate objects with the [associations API.](/docs/api/crm/associations)

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/crm/feedback-submissions#page-feedback)
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