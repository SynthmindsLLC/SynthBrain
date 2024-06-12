---
Please provide me with more context!  I need to know what kind of mission you are trying to create. 

For example, tell me: "* **What is the mission for?** Is it for a company, a project, a personal goal, a club, etc.? "
* **What are the goals of the mission?** What do you hope to achieve?
* **Who is involved?** Who will be working on this mission?
* **What are the values that guide this mission?** What principles are important to you?

The more information you give me, the better I can help you write a compelling and effective mission statement!
---

If Statements


=================

Last updated: April 3, 2024

You can include conditional logic in your modules and templates by using HubL [if statements](#basic-if-statement-syntax) and [unless statements](#unless-statements). If statements often contain HubL [supported operators](/docs/cms/hubl/operators-and-expression-tests) and can be used to execute [expression tests](/docs/cms/hubl/operators-and-expression-tests#expression-tests). 

**Please note:** if you're using [personalization tokens](/docs/cms/hubl/functions#personalization-token) within a conditional statement of your email module, you must [enable programmable email for the module](/docs/cms/guides/email/hubdb-crm-objects).

Information passed via the [v3](/docs/api/marketing/transactional-emails#single-send-api) or [v4](/docs/api/marketing/single-send-api) single send APIs will not function within `if` statements, as the templates compile before the information populates. 

Basic if statement syntax[](https://developers.hubspot.com/docs/cms/hubl/if-statements#basic-if-statement-syntax)
-----------------------------------------------------------------------------------------------------------------

HubL uses if statements to help define the logic of a template. The syntax of HubL if statements is very similar to conditional logic in Python. `if` statements are wrapped in [statement delimiters](/docs/cms/hubl/variables-macros-syntax), starting with an opening `if` statement and ending with an `**endif**`.

The example below provides the basic syntax of an if statement, where "condition" would be replaced with the boolean rule that you were going to evaluate as being true of false.

{% if condition %} If the condition is true print this to template. {% endif %}

Now that you have seen the basic syntax, let's look at a few actual examples of basic if statements. The next examples below show if statements that check to see whether or not a HubL module with the name `my_module` and whether a variable named `my_module` are present on a template. Notice that without any operators, the if statement will evaluate whether or not the module is defined in the context of the template.

{% module "my\_module" path="@hubspot/rich\_text", label="My rich text module", html="Default module text" export\_to\_template\_context=true %} {% if widget\_data.my\_module %} A module named "my\_module" is defined in this template. {% endif %} {% set my\_variable = "A string value for my variable" %} {% if my\_variable %} The variable named my\_variable is defined in this template. {% endif %}

Notice that when evaluating the HubL module, the module name is left in quotes within the `if` statement and while testing the variable no quotes are used around the variable name. In both examples above, the module and the variable exist in the template, so the statements evaluate to print the markup. Please note that these examples are only testing whether the module and variable are defined, not whether or not they have a value.

Now let's look at an `if` statement that evaluates whether a module has a value, instead of evaluating whether it exists on the template. To do this, we need to use the [export\_to\_template\_context](/docs/cms/building-blocks/modules/export-to-template-context) parameter. In the example below, if the text module is valued in the content editor, the markup would print. If the module's text field were cleared, no markup would render. If you are working within custom modules, there is a simplified `widget.widget_name` syntax outlined in the [example here](/docs/cms/building-blocks/modules/configuration).

{% module "product\_names" path="@hubspot/text", label="Enter the product names that you would like to render the coupon ad for", value="all of our products", export\_to\_template\_context=True %} {% if widget\_data.product\_names.value %} <div class="coupon-ad"> <h3>For a limited time, get 50% off {{ widget\_data.product\_names.value}}! </h3> </div> {% endif %} <div class="coupon-ad"> <h3>For a limited time get 50% off all of our products! </h3> </div>

Using elif and else[](https://developers.hubspot.com/docs/cms/hubl/if-statements#using-elif-and-else)
-----------------------------------------------------------------------------------------------------

`if` statements can be made more sophisticated with additional conditional statements or with a rule that executes when the condition or conditions are false. `elif` statements allow you to add additional conditions to your logic that will be evaluated after the previous condition. **`else`** statements define a rule that executes when all other conditions are false. You can have an unlimited number of `**elif**` statements within a single if statement, but only one `**else**` statement.

Below is the basic syntax example of if statement that uses the [<= operator](/docs/cms/hubl/operators-and-expression-tests#comparison) to check the value of a variable. In this example, the template would print: "Variable named number is less than or equal to 6." 

{% set number = 5 %} {% if number <= 2 %} Variable named number is less than or equal to 2. {% elif number <= 4 %} Variable named number is less than or equal to 4. {% elif number <= 6 %} Variable named number is less than or equal to 6. {% else %} Variable named number is greater than 6. {% endif %}

Below is one more example that uses a choice module to render different headings for a careers page, based on the department chosen by the user. The example uses the [\== operator](/docs/cms/hubl/operators-and-expression-tests#comparison), to check for certain predefined values in the choice module. 

{% choice "department" label="Choose department", value="Marketing", choices="Marketing, Sales, Dev, Services" export\_to\_template\_context=True %} {% if widget\_data.department.value == "Marketing" %} <h3>Want to join our amazing Marketing team?!</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% elif widget\_data.department.value == "Sales" %} <h3>Are you a Sales superstar?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% elif widget\_data.department.value == "Dev" %} <h3>Do you love to ship code?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% else %} <h3>Want to work with our awesome customers?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% endif %}

Unless statements[](https://developers.hubspot.com/docs/cms/hubl/if-statements#unless-statements)
-------------------------------------------------------------------------------------------------

`unless` statements are conditionals just like `if` statements, but they work on the inverse logic. They will render and compile the code between the opening and closing tags, unless the single boolean condition evaluates to true. Unless statements begin with an **`unless`** and end with an **`endunless`.** `unless` statements support `else` but not `elif`. 

Below is an example that prints an "Under construction" header, unless the rich text field is valued. If the rich text field has content, then that content will display.

{% module "my\_page\_content" path="@hubspot/rich\_text", label="Enter your page content", html="" export\_to\_template\_context=true %} {{ widget\_data.my\_page\_content.html }} {% unless widget\_data.my\_page\_content.html %} <h1>This page is under construction.</h1> <h3>Come back soon!</h3> {% endunless %}

ifchanged[](https://developers.hubspot.com/docs/cms/hubl/if-statements#ifchanged)
---------------------------------------------------------------------------------

In addition to if and unless statements, HubL supports `**ifchanged**` statements. These statements can be used to only render markup when a variable has changed since a prior invocation of this tag.

Inline if statements[](https://developers.hubspot.com/docs/cms/hubl/if-statements#inline-if-statements)
-------------------------------------------------------------------------------------------------------

HubL supports inline `if` statements. These can be used to write conditional logic in a concise manner with [operators and expression tests](/docs/cms/hubl/operators-and-expression-tests).

{% set color = "Blue" if is\_blue is truthy else "Red" %} // color == "blue" {{ "Blue" if is\_blue is truthy else "Red" }} // "Blue" {% set dl = true %} <a href="http://example.com/some.pdf" {{"download" if dl }} >Download PDF</a>

Ternary operators[](https://developers.hubspot.com/docs/cms/hubl/if-statements#ternary-operators)
-------------------------------------------------------------------------------------------------

It is also possible to use ternary operators to quickly write conditional logic with [operators and expression tests](/docs/cms/hubl/operators-and-expression-tests#logical).

// If the variable is\_blue is true, output "blue", otherwise output"red" {{ is\_blue is truthy ? "blue" : "red" }} // Set the variable is\_red to false if is\_blue is true, otherwise set to true {% set is\_red = is\_blue is truthy ? false : true %}

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/if-statements#page-feedback)
-----------------------------------------------------------------------------------------------

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