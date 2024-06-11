---
title: "API Feedback Form"
description: "A form designed to collect user feedback on the beta version of a specific API, including satisfaction level and suggestions for improvement."
type: "conversation"
tags:
- "API"
- "Feedback"
- "Beta Testing"
relationships:
- "#part_of [[HubSpot Forms]]"
- "#authored_by [[Developer Team]]"]]
birthdate: ""
deathdate: ""
---

.interest-form { padding: 1em; display: none; height: 100%; } .interest-text { padding: 1em; } .hs-form>fieldset { max-width: 100% !important; }

**Access and test APIs in beta.** 
----------------------------------

**Please note**: This API is currently under development and is subject to change based on testing and feedback. By using these endpoints you agree to adhere to our [Developer Terms](https://legal.hubspot.com/hubspot-developer-terms)& [Developer Beta](https://legal.hubspot.com/developerbetaterms?)Terms. You also acknowledge and understand the risk associated with testing an unstable API. 

**This API is currently in beta.** For the latest stable version [check out this page](https://legacydocs.hubspot.com/docs/methods/forms/forms_overview)

 

  
Provide Feedback

hbspt.forms.create({ portalId: "428357", formId: "037350c3-535d-4755-82ca-53b73367754f", cssClass: "hs-form" });

First name

Last name

Email

How satisfied are you with this API beta\*

Please SelectVery satisfiedSatisfiedNeutralUnsatisfiedVery unsatisfied

Can we contact you with follow-up questions about this feedback?

*   Yes, HubSpot can contact me about this feedback 

By selecting “Yes,” you are allowing HubSpot to store any personal information submitted through this form. We respect your privacy and will only use it to contact you if we have follow-up questions about today’s feedback. You can unsubscribe from these communications at any time. For more information, check out our [Privacy Policy.](https://legal.hubspot.com/privacy-policy)

$(document).ready(() => { $("#interest-btn").click(() => { $(".interest-form").toggle(); }); });

[Overview](#tab-1)[Endpoints](#tab-2)

*   [Overview](#tab-1)
*   [Endpoints](#tab-2)

 * * *

Forms
=====

Use a HubSpot form to collect lead information about your visitors and contacts. You can use the endpoints outlined here to set up new forms or get details of forms you've previously created. If you're looking to send form submission data, you can use the [Submit data to a form endpoint](https://legacydocs.hubspot.com/docs/methods/forms/submit_form) instead.

The form's type indicates its purpose and is set to `hubspot` by default. You can use the following values for your `formType`:

*   `hubspot`: these forms offer a variety of field types and styling options and can be used embedded in either HubSpot pages or external pages. These forms can be created and edited using the endpoints described here. You can also create these forms within your HubSpot account, learn more about [creating HubSpot forms](https://knowledge.hubspot.com/forms/create-forms). 
*   `captured`: these forms correspond to HTML forms in external websites. If the non-HubSpot forms tool is enabled and there are submissions to the form on [a tracked page](https://knowledge.hubspot.com/reports/install-the-hubspot-tracking-code), the form is automatically created in HubSpot. Learn more about [using non-HubSpot forms](https://knowledge.hubspot.com/forms/use-non-hubspot-forms). 
*   `flow`: these are pop-up forms that can be used in either HubSpot pages or external pages. Learn more about [HubSpot's pop-up forms tool](https://knowledge.hubspot.com/forms/create-pop-up-forms). 
*   `blog_comment`: these forms are automatically created for HubSpot blog pages to collect comments on blog posts. Learn more about how to further [set up and moderate blog comments](https://knowledge.hubspot.com/blog/set-up-and-moderate-your-blog-comments). 

* * *  

* * *

Share your feedback[](https://developers.hubspot.com/docs/api/marketing/forms#page-feedback)
--------------------------------------------------------------------------------------------

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