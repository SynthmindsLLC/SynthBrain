---
Please provide me with more information! I need to know what the mission is about before I can help you. 

For example, tell me: "* **What is the purpose of this mission?** "
* **Who is involved?** 
* **What are the goals?** 
* **What is the context?** 

Once I have a better understanding of the mission, I can help you create a compelling and informative description.
---

Operators & Expression Tests


================================

Last updated: March 1, 2023

In order to expand the logic and functionality of your templates, HubL supports several key operators and expression tests. The [operators](/docs/cms/hubl/operators-and-expression-tests#operators) allow you to execute math functions, make comparisons, complicate template logic, and alter what markup renders. In addition, this article contains a comprehensive list of [expression tests](/docs/cms/hubl/operators-and-expression-tests#expression-tests) that can be used in HubL.

Operators[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#operators)
--------------------------------------------------------------------------------------------------

Operators are symbols that tell the HubL compiler to execute various operations that result in the final markup ouput. The following section includes a list of all of the supported HubL operators.

### Math[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#math)

Standard math operators can be used to calculate values in the context of a template.

| Symbol | Description |
| --- | --- |
| + | Adds two objects together. You will generally use this for the addition of numbers. If you are trying to concatenate strings of lists, you should use `~` instead. |
| \- | Subtracts one number from another. |
| / | Divides numbers |
| % | Returns the remainder from dividing numbers |
| // | Divide two numbers and return the truncated integer result. Example: `{{ 20 // 7 }}` is `2` |
| \* | Multiplies numbers |
| \*\* | Raise the left operand to the power of the right operand |

{% set my\_num = 11 %} {% set my\_number = 2 %} {{ my\_num + my\_number }}<br/> <!-- 11 + 2 = 13 --> {{ my\_num - my\_number }}<br/> <!-- 11 - 2 = 9 --> {{ my\_num / my\_number }}<br/> <!-- 11 / 2 = 5.5 --> {{ my\_num % my\_number }}<br/> <!-- 11 % 2 = 1 --> {{ my\_num // my\_number }}<br/> <!-- 11 // 2 = 5 --> {{ my\_num \* my\_number }}<br/> <!-- 11 \* 2 = 22 --> {{ my\_num \*\* my\_number }}<br/> <!-- 11 \*\* 2 = 121 -->13 9 5.5 1 5 22 121

### Comparison[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#comparison)

Comparison operators can be used to evaluate values for template logic. You can see some examples of comparison operators being used on [if statements here](/docs/cms/hubl/if-statements). 

| Symbol | shorthand | Description |
| --- | --- | --- |
| \== | eq | Equal to. Evaluates to true if two objects are equal.  |
| != | ne | Not equal to. Evaluates to true if two objects are not equal. |
| \> | gt | Greater than. Evaluates to true if the left-hand side is greater than the right-hand side. |
| \>= | gte | Greater than or equal to. Evaluates to true if the left-hand side is greater or equal to the right-hand side. |
| < | lt | Less than. Evaluates to true if the left-hand side is lower than the right-hand side. |
| <= | lte | Less than or equal to. Evaluates to true if the left-hand side is lower or equal to the right-hand side. |

The shorthand version of the comparison operators are usable in filters that involve testing an expression such as  `|selectattr()`.

{% set my\_num = 11 %} {% set my\_number = 2 %} {{ my\_num == my\_number }}<br/> <!-- false --> {{ my\_num != my\_number }}<br/> <!-- true --> {{ my\_num > my\_number }}<br/> <!-- true --> {{ my\_num >= my\_number }}<br/> <!-- true --> {{ my\_num < my\_number }}<br/> <!-- false --> {{ my\_num <= my\_number }}<br/> <!-- false -->false true true true false false

### Logical[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#logical)

Logical operators allow you to combine multiple expressions into single statements.

| Symbol | Description |
| --- | --- |
| and | Return true if the left and the right operand are true. |
| or | Return true if the left or the right operand is true. |
| not | Negates a statement and is used in conjunction with is. See examples below. |
| (expr) | Group an expression for the order of operations. For example, (10 - 2) \* variable. |
| ?: | The [ternary operator](/docs/cms/hubl/if-statements?hsLang=en#ternary-operators) accepts 3 arguments (expression, true condition, false condition). Evaluates an expression and returns the corresponding condition. |

### Other HubL operators[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#other-hubl-operators)

Below are other important HubL operators that can be used to perform various tasks.

| Symbol | Description |
| --- | --- |
| in | Checks to see if a value is in a sequence. |
| is | Performs an [expression test](/docs/cms/hubl/operators-and-expression-tests#expression-tests). |
| | | Applies a filter. |
| ~ | Concatenates values. |

Expression tests[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#expression-tests)
----------------------------------------------------------------------------------------------------------------

Expression tests are various boolean conditions that can be evaluated by using logical operators.

### boolean[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#boolean)

The `boolean` expression test checks to see whether the object is boolean (in a strict sense, not in its ability to evaluate to a truthy expression).

{% set isActive = false %} {% if isActive is boolean %} isActive is a boolean {% endif %}isActive is a boolean

### containing[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#containing)

The `containing` expression test checks to see whether a list variable has a value in it.

{% set numbers = \[1, 2, 3\] %} {% if numbers is containing 2 %} Set contains 2! {% endif %}Set contains 2!

### containingall[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#containingall)

The `containingall` expression test checks if a list variable contains all of the values of another list.

{% set numbers = \[1, 2, 3\] %} {% if numbers is containingall \[2, 3\] %} Set contains 2 and 3! {% endif %} {% if numbers is containingall \[2, 4\] %} Set contains 2 and 4! {% endif %}Set contains 2 and 3!

### defined[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#defined)

The **defined** expression test checks to see whether a variable is defined within the context of the template. While you can use this expression test, writing an if statement without any operators will default to checking whether or not the variable is defined.

In the example below, a color module's color parameter is tested. If the color parameter had no value, the template would render a default black background color. If it is defined, it renders the background color set by the user.

{% color "my\_color" color="#930101", export\_to\_template\_context=True %} <style> {% if widget\_data.my\_color.color is defined %} body{ background: {{ widget\_data.my\_color.color }}; } {% else %} body{ background: #000; } {% endif %} </style><style> body{ background: #930101; } </style>

### divisibleby[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#divisibleby)

The expression test **divisibleby** can be used to test whether an object is divisible by another number.

For example, below a for loop is created that iterates through a list of types of animals. Each type of animal gets printed in a div, and every 5th div has different inline styling applied (width:100%). This concept could be applied to a blog where different markup is rendered for a certain pattern of posts. To learn more about for loops and loop.index, [check out this article](/docs/cms/hubl/for-loops?hsLang=en). 

{% set animals = \["lions", "tigers", "bears", "dogs", "sharks"\] %} {% for animal in animals %} {% if loop.index is divisibleby 5 %} <div style="width:100%">{{animal}}</div> {% else %} <div style="width:25%">{{animal}}</div> {% endif %} {% endfor %}<div style="width:25%">lions</div> <div style="width:25%">tigers</div> <div style="width:25%">bears</div> <div style="width:25%">dogs</div> <div style="width:100%">sharks</div>

### equalto[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#equalto)

The **equalto** expression test checks to see if a variable's value is equal to a constant or another variable. You can also use the operator == to do the same test.

In the example below, the width of the blog posts is adjusted based on the total number of posts in the loop. The example output assumes there were 4 posts in the blog. 

{% for content in contents %} {% if loop.length is equalto 2 %} <div style="width:50%;">Post content</div> {% elif loop.length is equalto 3 %} <div style="width:33.333332%;">Post content</div> {% elif loop.length is equalto 4 %} <div style="width:25%;">Post content</div> {% else %} <div style="width:100%;>Post content</div> {% endif %} {% endfor %}<div style="width:25%;">Post content</div> <div style="width:25%;">Post content</div> <div style="width:25%;">Post content</div> <div style="width:25%;">Post content</div>

### even[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#even)

The **even** expression test checks to see whether a numeric variable is an even number. 

The example below shows a simplified blog listing loop, where if the current iteration of the loop is even, a class of even-post is assigned to the post item div. Otherwise, a class of odd-post is assigned. 

{% for content in contents %} {% if loop.index is even %} <div class="post-item even-post">Post content</div> {% else %} <div class="post-item odd-post">Post content</div> {% endif %} {% endfor %} <div class="post-item odd-post">Post content</div> <div class="post-item even-post">Post content</div> <div class="post-item odd-post">Post content</div> <div class="post-item even-post">Post content</div>

### float[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#float)

The **float** expression test checks to see whether a numeric variable is a a floating-point number. 

{% set quantity = 1.20 %} {% if quantity is float %} quantity is a floating point number {% endif %}quantity is a floating-point number

### integer[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#integer)

Checks to see whether a variable is an **integer.**

{% set quantity = 120 %} {% if quantity is integer %} quantity is an integer {% endif %}quantity is an integer

### iterable[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#iterable)

Checks to see whether a variable is **iterable** and can be looped through.

This example checks a variable called "jobs" to see if it can be iterated through. Since the variable contains a list of jobs, the if statement would evaluate to true, and the loop would run. If the variable had contained a single value, the [if statement](/docs/cms/hubl/if-statements) would print that value with different markup instead. [Learn more about for loops](/docs/cms/hubl/for-loops?hsLang=en). 

{% set jobs = \["Accountant", "Developer", "Manager", "Marketing", "Support"\] %} {% if jobs is iterable %} <h3>Available positions</h3> <ul> {% for job in jobs %} <li>{{ job }}</li> {% endfor %} </ul> {% else %} <h3>Available position</h3> <div class="single-position">{{ jobs }}</div> {% endif %}<h3>Available positions</h3> <ul> <li>Accountant</li> <li>Developer</li> <li>Manager</li> <li>Marketing</li> <li>Support</li> </ul>

### lower[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#lower)

The **lower** expression test evaluates to true when a string is lowercase. 

The example below uses an [unless statement](/docs/cms/hubl/if-statements#unless-statements) and a lower filter to ensure that a string of text entered into a text module is always lowercase.

{% module "my\_text" path="@hubspot/text" label="Enter text", value="Some TEXT that should be Lowercase", export\_to\_template\_context=True %} {% unless widget\_data.my\_text.value is lower %} {{ widget\_data.my\_text.value|lower }} {% endunless %}some text that should be lowercase

### mapping[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#mapping)

The **mapping** expression test checks to see whether or not an object is a dict (dictionary). 

The example below is checking to see if the contact object is a dictionary, in which case it is. 

{% if contact is mapping %} This object is a dictionary. {% else %} This object is not a dictionary. {% endif %}This object is a dictionary.

### none[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#none)

The **none** expression test checks to see whether a variable has a null value.

{% module "user\_email" path="@hubspot/text" label="Enter user email", value="example@hubspot.com", export\_to\_template\_context=True %} {% unless widget\_data.user\_email.value is none %} {{ widget\_data.user\_email.value }} {% endunless %}example@hubspot.com

### number[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#number)

The **number** expression test checks to see whether or not the value of a variable is a number.

The example below checks a variable to see whether or not it is a variable, and if so it converts it into millions.

{% set my\_var = 40 %} {% if my\_var is number %} {{ my\_var \* 1000000 }} {% else %} my\_var is not a number. {% endif %}40000000

### odd[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#odd)

The **odd** expression test checks to see whether a numeric variable is an odd number. 

Below is the same example as the inverse even expression test previously described.

{% for content in contents %} {% if loop.index is odd %} <div class="post-item odd-post">Post content</div> {% else %} <div class="post-item even-post">Post content</div> {% endif %} {% endfor %} <div class="post-item odd-post">Post content</div> <div class="post-item even-post">Post content</div> <div class="post-item odd-post">Post content</div> <div class="post-item even-post">Post content</div>

### sameas[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#sameas)

The **sameas** expression test checks to see whether or not two variables have the same value. 

The example below sets two variables and then checks to see whether or not they are the same.

{% set var\_one = True %} {% set var\_two = True %} {% if var\_one is sameas var\_two %} The variables values are the same. {% else %} The variables values are different. {% endif %}The variables values are the same.

### sequence[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#sequence)

The **sequence** expression test is similar to the **iterable** test, in that it checks to see whether or not a variable is a sequence.  

The example below checks whether a variable is a sequence and then iterates through that sequence of musical genres.

{% set genres = \["Pop", "Rock", "Disco", "Funk", "Folk", "Metal", "Jazz", "Country", "Hip-Hop", "Classical", "Soul", "Electronica" \] %} {% if genres is sequence %} <h3>Favorite genres</h3> <ul> {% for genre in genres %} <li>{{ genre }}</li> {% endfor %} </ul> {% else %} <h3>Favorite genre:</h3> <div class="single-genre">{{ genres }}</div> {% endif %}<ul> <li>Pop</li> <li>Rock</li> <li>Disco</li> <li>Funk</li> <li>Folk</li> <li>Metal</li> <li>Jazz</li> <li>Country</li> <li>Hip-Hop</li> <li>Classical</li> <li>Soul</li> <li>Electronica</li> </ul>

### string[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#string)

The **string** expression test checks to see whether the value stored in a variable is text. 

The example below checks whether or not a variable is a string, and if so it applies a title filter to change the capitalization. 

{% set my\_var = "title of section" %} {% if my\_var is string %} {{ my\_var|title }} {% else %} my\_var is not a string {% endif %}Title Of Section

### string\_containing[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#string-containing)

This test checks to see if a string is contained within another string. This expression test is used in conjunction with the "is" operator.

{% if content.domain is string\_containing ".es" %} Markup that will only render on content hosted on .es domains {% elif content.domain is string\_containing ".jp" %} Markup that will only render on content hosted on .jp domains {% else %} Markup that will render on all other domains {% endif %}Markup that will render on all other domains

### string\_startingwith[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#string-startingwith)

This expression test checks to see if a string starts with a particular string. It is used in conjunction with the "is" operator.

{% if content.slug is string\_startingwith "es/" %} Markup that will only render on content hosted in a /es/ subdirectory {% elif content.slug is string\_startingwith "jp/" %} Markup that will only render on content hosted in a /jp/ subdirectory {% else %} Markup that will render on all subdirectories {% endif %}Markup that will render on all subdirectories

### truthy[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#truthy)

The **truthy** expression test checks to see whether an expression evaluates to True.

The example below uses a boolean checkbox module to display an alert message.

{% boolean "check\_box" label="Show alert", value=True, export\_to\_template\_context=True %} {% if widget\_data.check\_box.value is truthy %} <div class="alert">Danger!</div> {% endif %}<div class='alert'>Danger!</div>

### undefined[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#undefined)

The **undefined** expression test checks to see whether a variable is undefined in the context of the template. This test is different from none, in that undefined will be true when the variable is present but has no value; whereas, none will be true when the variable has a null value.  

The example below checks a template for the existence of the variable "my\_var".

{% if my\_var is undefined %} A variable named "my\_var" does not exist on this template. {% else %} {{ my\_var }} {% endif %}A variable named "my\_var" does not exist on this template.

### upper[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#upper)

The **upper** expression test evaluates to true when a string is all uppercase. Below is an inverse example of the lower expression test above.

{% module "my\_text" path="@hubspot/text" label="Enter text", value="Some TEXT that should be Uppercase", export\_to\_template\_context=True %} {% unless widget\_data.my\_text.value is upper %} {{ widget\_data.my\_text.value|upper }} {% endunless %}SOME TEXT THAT SHOULD BE UPPERCASE

### within[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#within)

The **within** expression tests checks if a variable is within a list.

{% set numbers = \[1, 2, 3\] %} {% if 2 is within numbers %} 2 is in the list! {% endif %} {% if 4 is within numbers %} 4 is in the list! {% endif %}2 is in the list!

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/operators-and-expression-tests#page-feedback)
----------------------------------------------------------------------------------------------------------------

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