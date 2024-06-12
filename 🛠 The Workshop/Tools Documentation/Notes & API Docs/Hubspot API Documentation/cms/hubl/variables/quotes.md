---
Please provide me with more information about the mission. I need to know what the mission is for, what its objectives are, and what it hopes to achieve. 

For example, tell me: "* **What is the mission about?** (e.g., a company, a project, a personal goal)"
* **What are the goals of the mission?** (e.g., increase sales, solve a problem, improve a situation)
* **What are the expected outcomes of the mission?** (e.g., achieve a certain level of success, make a positive impact)

Once you give me more details, I can help you write a compelling and impactful mission statement.
---

Quote template variables


============================

Last updated: April 3, 2023

Custom quote templates can access quote data and some associated objects directly from the templates. The data available depends on data you have in your CRM, as well as data added to the quote itself.

While developing a quote template, you can use HubSpot-provided mock data to populate the template, which may help for previewing the template. In the `@hubspot` folder, navigate to the `cms-quotes-theme` folder. Within the `templates` folder, view the `basic.html`, `modern.html`, or `original.html` templates. These templates contain the following code block at the top:

{% from "../imports/mock\_data.html" import SAMPLE\_TEMPLATE\_DATA as mock\_data %} {% from "../imports/module\_defaults.html" import MODULE\_DEFAULTS as module\_defaults %} {% set QUOTE = template\_data.quote || mock\_data.quote %} {% set CURRENCY = QUOTE.hs\_currency || "USD" %} {% set LOCALE = QUOTE.hs\_locale || "en-US" %} {% set ASSOCIATED\_OBJECTS = QUOTE.associated\_objects %} {% set LINE\_ITEMS = ASSOCIATED\_OBJECTS.line\_items %} {% set ADDITIONAL\_FEES = ASSOCIATED\_OBJECTS.additional\_fees %} {% set TOTALS = ASSOCIATED\_OBJECTS.totals || ASSOCIATED\_OBJECTS.totals %} {% set QUOTE\_TOTAL = TOTALS.total %} {% set SUB\_TOTALS = TOTALS.subtotals %} {% set DEAL = ASSOCIATED\_OBJECTS.deal %}

The mock data is first imported from the `mock_data.html` file, then is set to the `QUOTE` variable to use the data found in `template_data` if available. The `QUOTE` variable is also used to populate the other variables in this list, such as `ASSOCIATED_OBJECTS`, to make accessing that data less verbose. However, you can structure your data differently, depending on your preferences.

In the above code, you'll notice that `template_data` is also used to set the main `QUOTE` variable. `template_data` is an object containing all of the actual data for the quote and deal in the page. If that object is not found in the template, HubSpot loads the data from `mock_data.html` instead.

Template\_data object[](https://developers.hubspot.com/docs/cms/hubl/variables/quotes#template-data-object)
-----------------------------------------------------------------------------------------------------------

The vast majority of the data can be directly accessed through the `template_data` object. You can use `{{ template_data|pprint }}` in your template to see the full object provided. 

template data object parameters
| Variable | Type | Description |
| --- | --- | --- |
| 
`template_data`

 | dict | 

A dict containing the quote, quote.associated\_objects, and totals dicts.

 |

Quote variables[](https://developers.hubspot.com/docs/cms/hubl/variables/quotes#quote-variables)
------------------------------------------------------------------------------------------------

The information specific to this individual quote.

template data object parameters
| Variable | Type | Description |
| --- | --- | --- |
| 
`template_data.quote`

 | dict | 

Dict containing all of the data for the quote itself.

 |
| 

`template_data.quote.associated_objects.deal.hs_object_id`

 | Integer | 

Deal Id

 |
| 

`template_data.quote.hubspot_owner_id`

 | Integer | 

Deal owner id

 |
| 

`template_data.quote.hs_all_owner_ids`

 | integer or array of integers | 

Deal owner ids

 |
| 

`template_data.quote.hs_created_by_user_id`

 | Integer | 

User that created the quote.

 |
| 

`template_data.quote.hs_lastmodifieddate`

 | datetime | 

Date the quote was last modified. In epoch format.

 |
| 

`template_data.quote.hubspot_owner_assigneddate`

 | datetime | 

Date the quote was assigned an owner. In epoch format.

 |
| 

`template_data.quote.hs_createdate`

 | datetime | 

Date and time the quote was created. In epoch format.

 |
| 

`template_data.quote.hs_expiration_date`

 | datetime | 

Date quote expires. In epoch format.

 |
| 

`template_data.quote.hs_title`

 | String | 

Quote Title

 |
| 

`template_data.quote.hs_template_type`

 | String | 

"CUSTOMIZABLE\_QUOTE\_TEMPLATE"

 |
| 

`template_data.quote.hs_slug`

 | String | 

URL slug for quote web page.

 |
| 

`template_data.quote.hs_proposal_template_path`

 | String | 

Developer file system path to template. (includes file extension)

 |
| 

`template_data.quote.hs_quote_amount`

 | String | 

Amount of money

 |
| 

`template_data.quote.hs_currency`

 | String | 

Currency the quote amount is in in 3 character ISO 4217 currency code.  
"USD"

 |
| 

`template_data.quote.hs_language`

 | String | 

Language code  
"en"

 |
| 

`template_data.quote.hs_locale`

 | String | 

Locale code  
"en-us"

 |
| 

`template_data.quote.hs_terms`

 | String | 

Terms text provided by quote creator

 |
| 

`template_data.quote.hs_sender_firstname`

 | String | 

First name of the person sending the quote.

 |
| 

`template_data.quote.hs_sender_company_name`

 | String | 

Company name of the person sending the quote

 |
| 

`template_data.quote.hs_sender_company_image_url`

 | String | 

Company logo for the person sending the quote.

 |
| 

`template_data.quote.hs_status`

 | String | 

Status of the quote.  
"APPROVAL\_NOT\_NEEDED"

 |
| 

`template_data.quote.hs_primary_color`

 | string/hex color code | 

"#425b76"

 |
| 

`template_data.quote.hs_quote_number`

 | String | 

Unique quote id number.

 |
| 

`template_data.quote.hs_payment_enabled`

 | boolean | 

Use to test if payment fields need to be shown.

 |
| 

`template_data.quote.hs_esign_enabled`

 | boolean | 

Use to test if esignature fields need to be shown.

 |

**Can't find a variable you're looking for?**  
There are more variables you can access within `template_data`. Use `|pprint` to view them. Additionally some variables in quote associations may only be available based on the quote/deal.   
  
We will be iterating on this documentation to showcase and explain more of the data you have access to. Aside from pretty printing, you can view the mock data file within the cms-quote-theme, to see what is available and the structure it comes in.

Associated objects[](https://developers.hubspot.com/docs/cms/hubl/variables/quotes#associated-objects)
------------------------------------------------------------------------------------------------------

In a quote template, you can access data from a quote's associated records, such as deals or companies, by using `associated_objects`.

For example, you can add the logo from the quote recipient's associated company record to a quote by using the following code:

{% set company\_avatar\_url = template\_data.quote.associated\_objects.company.hs\_avatar\_filemanager\_key %} {% if company\_avatar\_url %} <img src="{{ template\_data.quote.associated\_objects.company.hs\_avatar\_filemanager\_key }}" width="400" alt="{{ template\_data.quote.associated\_objects.company.name }}"> {% else %} <!-- company does not have an assigned image--> {% endif %}

**Please note:** only manually set logos will appear. Automatically detected logos will not appear to prevent unintentional logos from appearing on the quote template.

The above code first sets a variable that searches for the quote's associated company's logo. Then, using an `if` statement, the template displays that logo, if available. If no logo has been manually set for the company, no logo is displayed.

Custom Objects[](https://developers.hubspot.com/docs/cms/hubl/variables/quotes#custom-objects)
----------------------------------------------------------------------------------------------

Custom object data can be displayed or used within a quote in a couple different ways. Because each custom object's structure may vary, you'll need to get specific properties based on how you've structured your custom object.

The quote `template_data` by default has custom associated objects in it. For example, custom objects associated with deals are included.

To access them, you can use the following code:

{% set quote\_associated\_custom\_objects = template\_data.quote.associated\_objects.deal.associated\_objects.custom\_objects %} {{ quote\_associated\_custom\_objects|pprint }} {# |pprint is useful for understanding the structure of the data, you can leave it off when outputting values for display. #}

**Please note:** because custom objects are unique to each account, the mock data doesn't include an example custom object. This means that in the template preview in the design manager you may see an error or the custom object data simply won't display. You'll instead need to preview the template with your real CRM data, which you can do by creating a quote from the template.

You can then access each custom object type by appending its custom object type ID formatted with underscores. For example:  
  
`template_data.quote.associated_objects.deal.associated_objects.custom_objects._2_2193031`

You can also look up a custom object by using the [`crm_associations()`](/docs/cms/hubl/functions#crm-associations) function and `[crm_objects()](/docs/cms/hubl/functions#crm-objects)` functions. 

For example, if you wanted to look up a custom object associated with a deal, you could pass in data from `template_data`:

{% set quote\_associated\_object = crm\_associations(template\_data.quote.associated\_objects.deal.hs\_object\_id, "USER\_DEFINED", 152) %} {# 152 is an example of an association type id, you would need to use the appropriate id for your use-case. #} {{ quote\_associated\_object }}

Related Resources[](https://developers.hubspot.com/docs/cms/hubl/variables/quotes#related-resources)
----------------------------------------------------------------------------------------------------

*   [Custom quote templates](/docs/cms/building-blocks/templates/quotes)
*   [Getting started with the CMS quotes theme](/getting-started-from-the-cms-quotes-theme-beta)
*   [Create and use custom quote templates (from the sales, sales ops/manager perspective)](https://knowledge.hubspot.com/deals/create-custom-quote-templates-beta)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/variables/quotes#page-feedback)
--------------------------------------------------------------------------------------------------

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