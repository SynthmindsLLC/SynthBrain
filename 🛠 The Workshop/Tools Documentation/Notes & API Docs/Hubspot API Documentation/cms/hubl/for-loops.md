---
Please provide me with more context! To help you create a compelling mission statement, I need to know: "* **What is the purpose of this mission?** Is it for a company, a project, a personal goal, or something else?"
* **What are the core values and beliefs behind this mission?** What are the fundamental principles that guide your actions?
* **What are the specific goals and objectives you want to achieve?** What are the tangible outcomes you are aiming for?
* **Who are the stakeholders involved?** Who will be impacted by this mission?

Once I have a better understanding of your context, I can help you craft a powerful and meaningful mission statement.
---

For loops


=============

Last updated: January 24, 2022

For loops can be used in HubL to iterate through sequences of objects. They will most commonly be used with rendering [blog content](/docs/cms/building-blocks/templates/blog-template-markup) in a listing format, but they can also be used to sort through other sequence variables.

For loops begin with a `{% for %}` statement and end with an `{% endfor %}` statement. Within the `{% for %}` statement a single sequence item is named followed by `in` and then the name of the sequence. The code between the opening and closing `for` statements is printed with each iteration, and generally includes the printed variable of the individual sequence item. Below is the basic syntax of a for loop:

{% for item in items %} {{ item }} {% endfor %}

Below is a basic example that shows how to print a sequence of variable values into a list.

{% set languages = \["HTML", "CSS", "Javascript", "Python", "Ruby", "PHP", "Java"\] %} <h1>Languages</h1>; <ul> {% for language in languages %} <li>{{ language }}</li> {% endfor %} </ul><h1>Languages</h1> <ul> <li>HTML</li> <li>CSS</li> <li>Javascript</li> <li>Python</li> <li>Ruby</li> <li>PHP</li> <li>Java</li> </ul>

Loop properties[](https://developers.hubspot.com/docs/cms/hubl/for-loops#loop-properties)
-----------------------------------------------------------------------------------------

As a loop iterates, you can use [conditional logic](/docs/cms/hubl/if-statements) to define the loop's behavior. The variable property `loop.index` keeps a count of the current number of the iterations of the loop. There are several other loop variable properties that count the iterations in different ways. These properties are described below:

| Variable | Description |
| --- | --- |
| 
`loop.cycle`

 | 

A helper function to cycle between a list of sequences. See the explanation below.

 |
| 

`loop.depth`

 | 

Indicates how deep in deep in a recursive loop the rendering currently is. Starts at level 1

 |
| 

`loop.depth0`

 | 

Indicates how deep in deep in a recursive loop the rendering currently is. Starts at level 0

 |
| 

`loop.first`

 | 

This variable evaluates to true, if it is the first iteration of the loop.

 |
| 

`loop.index`

 | 

The current iteration of the loop. This variable starts counting at 1.

 |
| 

`loop.index0`

 | 

The current iteration of the loop. This variable starts counting at 0.

 |
| 

`loop.last`

 | 

This variable evaluates to true, if it is the last iteration of the loop.

 |
| 

`loop.length`

 | 

The number of items in the sequence.

 |
| 

`loop.revindex`

 | 

The number of iterations from the end of the loop. Counting down to 1.

 |
| 

`loop.revindex0`

 | 

The number of iterations from the end of the loop. Counting down to 0.

 |

Below are some examples that use different loop variables. The following basic example uses `loop.index` to keep a count that is printed with each iteration.

{% set loopy = \["Content", "Social", "Contacts", "Reports"\] %} {% for app in loopy %} {{ loop.index }}. {{app}} <br> {% endfor %}1\. Content <br> 2. Social <br> 3. Contacts <br> 4. Reports <br>

The next example uses conditional logic to check whether the length of the loop is `divisibleby` certain numbers. It then renders the width of the post-item div accordingly. The example uses the standard blog post loop and assumes that there are 6 posts in the loop.

{% for content in contents %} {% if loop.length is divisibleby 4 %} <div style="width:25%">Post content</div> {% elif loop.length is divisibleby 3 %} <div style="width:33.33332%">Post content</div> {% else %} <div style="width:50%">Post content</div> {% endif %} {% endfor %}<div style="width:33.33332%">Post content</div> <div style="width:33.33332%">Post content</div> <div style="width:33.33332%">Post content</div> <div style="width:33.33332%">Post content</div> <div style="width:33.33332%">Post content</div> <div style="width:33.33332%">Post content</div> <div style="width:33.33332%">Post content</div>

Nested loops[](https://developers.hubspot.com/docs/cms/hubl/for-loops#nested-loops)
-----------------------------------------------------------------------------------

Loops can also be nested with loops. The child for loop will run with each iteration of the parent for loop. In the example below, a list of child items is printed in a nested `<ul>` within a `<ul>` of parent items.

{% set parents = \["Parent item 1", "Parent item 2", "Parent item 3"\] %} {% set children = \["Child item 1", "Child item 2", "Child item 3"\] %} <ul> {% for parent in parents %} <li>{{parent}}<ul> {% for child in children %} <li>{{child}}</li> {% endfor %} </ul> </li> {% endfor %} </ul><ul> <li>Parent item 1<ul> <li>Child item 1</li> <li>Child item 2</li> <li>Child item 3</li> </ul> </li> <li>Parent item 2<ul> <li>Child item 1</li> <li>Child item 2</li> <li>Child item 3</li> </ul> </li> <li>Parent item 3<ul> <li>Child item 1</li> <li>Child item 2</li> <li>Child item 3</li> </ul> </li> </ul>

cycle[](https://developers.hubspot.com/docs/cms/hubl/for-loops#cycle)
---------------------------------------------------------------------

The cycle tag can be used within a for loop to cycle through a series of string values and print them with each iteration. One of the most practical applications to this technique is applying alternating classes to your blog posts in a listing. This tag can be used on more than two values and will repeat the cycle if there are more loop iterations than cycle values. In the example below, a class of `odd` and `even` are applied to posts in a listing (the example assumes that there are 5 posts in the loop).  

Please note that there are **no spaces** between the comma-separated cycle string values.

{% for content in contents %} <div class="post-item {% cycle "odd","even" %}">Blog post content</div> {% endfor %}<div class="post-item odd">Blog post content</div> <div class="post-item even">Blog post content</div> <div class="post-item odd">Blog post content</div> <div class="post-item even">Blog post content</div> <div class="post-item odd">Blog post content</div>

Variables within loops[](https://developers.hubspot.com/docs/cms/hubl/for-loops#variables-within-loops)
-------------------------------------------------------------------------------------------------------

Any variables defined within loops are limited to the scope of that loop and cannot be called from outside of the loop.

You can call variables that are defined outside of a loop, from within a loop, but not the other way around.

Key, value pairs in loops[](https://developers.hubspot.com/docs/cms/hubl/for-loops#key-value-pairs-in-loops)
------------------------------------------------------------------------------------------------------------

If the dict of information you are looping through has key and value pairs, a simple for loop would only have access to the values. If you wish to have access to both the keys and values within the for loop, the HubL would be formatted as such:

{% set dict\_var = {"name": "Cool Product", "price": "$20", "size":"XL"} %} {% for key, val in dict\_var.items() %} {{ key }}: {{ val }}<br> {% endfor %}name: Cool Product <br> price: $20 <br> size: XL <br>

Iterate a set number of times[](https://developers.hubspot.com/docs/cms/hubl/for-loops#iterate-a-set-number-of-times)
---------------------------------------------------------------------------------------------------------------------

Sometimes you want to iterate a set number of times, this can be useful in generating HTML or CSS. You can do this using the range function.

{% for x in range(0,5) %} {{loop.index}} {% endfor %}1 2 3 4 5

Using HubL tags in loops[](https://developers.hubspot.com/docs/cms/hubl/for-loops#using-hubl-tags-in-loops)
-----------------------------------------------------------------------------------------------------------

When you add a tag to page HubSpot automatically assigns an `id` to the wrapping HTML. That tag is unique per tag "name". In situations where you need to use a tag in a for loop setting unique names is not practical. Add the `unique_in_loop` parameter to your tag to generate unique ids. This parameter appends the module name with the current loop iteration number, ensuring that it is unique. Unique id's are not only needed for valid HTML but are important for [accessibility](/docs/cms/developer-reference/accessibility). 

{% for item in module.icon\_field %} {% icon name="{{ item.name }}", style="{{ item.type }}", unicode="{{ item.unicode }}", unique\_in\_loop=True %} {% endfor %}

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/for-loops#page-feedback)
-------------------------------------------------------------------------------------------

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