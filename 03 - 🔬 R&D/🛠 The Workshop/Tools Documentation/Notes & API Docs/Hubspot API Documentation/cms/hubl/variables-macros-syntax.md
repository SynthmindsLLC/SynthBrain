HubL variables & macros syntax


==================================

Last updated: March 14, 2022

HubL uses variables to store and output values to the template. Variables can be used in template logic or iterated through with for loops. In addition to variables, macros are another useful tool for printing repetitive yet dynamic sections of code throughout your templates.

Variables are expressions delimited by `}}`. The basic syntax of variables is as follows:

// variables {{ variable }} {{ dict.attribute }}

Variables[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#variables)
-------------------------------------------------------------------------------------------

Variables are either a single word in an expression or an attribute of a dictionary. HubL uses Python-based data structures called dictionaries or **dicts** to store various sets of variables.  For example, HubSpot uses a dictionary "content" to house many attributes that pertain to the content created with that template. For example the `content.absolute_url` prints the URL of the specific piece of content.

HubSpot has many predefined variables that can be used throughout your page, blog, and email templates. We have a [reference list of variables](/docs/cms/hubl/variables), you can also view the [developer info](/docs/cms/developer-reference/debugging-and-errors#developer-info) when browsing any page from your account to see the variables available within that page.. 

In addition to printing the values of variables and dictionary attributes in a template, you can also define your own variables. You can store strings, booleans, integers, sequences, or create dictionaries within a single variable. Variables are defined within statement delimiters using the word "set". Once stored, variables can then be printed by stating the variable name as an expression. Below you can see various types of information stored in variables and then printed.

Variables should either be single words or use underscores for spaces (ie my\_variable). **HubL does not support hyphenated variable names.**

{% set string\_var = "This is a string value stored in a variable" %} {{ string\_var}} {% set bool\_var = True %} {{ bool\_var}} {% set int\_var = 53 %} {{ int\_var}} {% set seq\_var = \["Item 1", "Item 2", "Item 3"\] %} {{ seq\_var}} {% set var\_one = "String 1" %} {% set var\_two = "String 2" %} {% set sequence = \[var\_one, var\_two\] %} {{ sequence }} {% set dict\_var = {"name": "Item Name", "price": "$20", "size":"XL"} %} {{ dict\_var.price }}This is a string value stored in a variable True 53 \[Item1, Item2, Item3\] \[String 1, String 2\] $20

Each example above stores a different type of variable, with the final example storing two different variables in a sequence. 

In addition to printing values, variables can be used in [if statements](/docs/cms/hubl/if-statements), as [filter](/docs/cms/hubl/filters) parameters, as [function](/docs/cms/hubl/functions) parameters, as well as iterated through with [for loops](/docs/cms/hubl/for-loops) (sequence variables only).

One common usage is to use variables to define common CSS values in your stylesheet. For example, if you have a color that you use over and over again throughout your CSS file. That way, if you need to change that color, you can change the variable value, and all references to that variable will be updated, the next time that you publish the file.

<!-- defines variable and assigns HEX color --> {% set primary\_color = "#F7761F" %} a { color: {{ primary\_color }}; {# prints variable HEX value #} } a { color: #F7761F; }

Macros[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#macros)
-------------------------------------------------------------------------------------

HubL macros allow you to print multiple statements with a dynamic value. For example, if there is a block of code that you find yourself writing over and over again, a macro may be a good solution, because it will print the code block while swapping out certain arguments that you pass it.

The macro is defined, named, and given arguments within a HubL statement. The macro is then called in a statement that passes its dynamic values, which prints the final code block with the dynamic arguments. The basic syntax of a macro is as follows:

{% macro name\_of\_macro(argument\_name, argument\_name2) %} {{ argument\_name }} {{ argument\_name2 }} {% endmacro %} {{ name\_of\_macro("value to pass to argument 1", "value to pass to argument 2") }}

If your macro is returning whitespace in the form of new lines, you can strip whitespace in templates by hand. If you add a minus sign (`-`) to the start or end of a block, a comment, or a variable expression, the whitespaces before or after that block will be removed.

{% macro name\_of\_macro(argument\_name, argument\_name2) -%} {{ argument\_name }} {{ argument\_name2 }} {%- endmacro %}

Below shows a practical application of a macro to print a CSS3 properties with the various vendor prefixes, with a dynamic value. This allows you to print 5 lines of code with a single macro tag.

{% macro trans(value) %} -webkit-transition: {{value}}; -moz-transition: {{value}}; -o-transition: {{value}}; -ms-transition: {{value}}; transition: {{value}}; {% endmacro %} a { {{ trans("all .2s ease-in-out") }} }a { -webkit-transition: all .2s ease-in-out; -moz-transition: all .2s ease-in-out; -o-transition: all .2s ease-in-out; -ms-transition: all .2s ease-in-out; transition: all .2s ease-in-out; }

Macros introduce the ability to have recursive code. To prevent reliability and performance issues you can only nest macros 20 levels deep. If you go over this limit you will get the error: `max recursion limit of 20 reached for macro <your macro name>`

Call[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#call)
---------------------------------------------------------------------------------

In some instances, you may want to pass additional dynamic information back into the macro block. For example, you may have a large piece of code that you want to feed back into the macro, in addition to the arguments. You can do this using call block and caller(). A call block works essentially like a macro but does not get its own name. The expression caller() specifies where the contents of the call block will render.

In the example below, a `<p>` is added into a macro in addition to the two arguments.

{% macro render\_dialog(title, class) %} <div class="{{ class }}"> <h2>{{ title }}</h2> <div class="contents"> {{ caller() }} </div> </div> {% endmacro %} {% call render\_dialog("Hello World", "greeting") %} <p>This is a paragraph tag that I want to render in my.</p> {% endcall %}<div class="greeting"> <h2>Hello World</h2> <div class="contents"> <p>This is a simple dialog rendered by using a macro and a call block.</p> </div> </div>

Import[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#import)
-------------------------------------------------------------------------------------

Another useful feature of macros is that they can be used across templates by importing one template file into another. To do this you will need to use the **import** tag. The import tag will let you specify a Design Manager file path to the template that contains your macros and give the macros a name in the template that you are including them in. You can then pass values into these macros without needing to redefine them.

For example, let's say that you have a .html template file that contains the following 2 macros. One macro is defined to set up a header tag and one is defined to generate a footer tag. This file is saved in Design Manager with the name `my_macros.html`.

<!-- my\_macros.html file --> {% macro header(tag, title\_text) %} <header> <{{ tag }}>{{ title\_text }} </{{tag}}> </header> {% endmacro %} {% macro footer(tag, footer\_text) %} <footer> <{{ tag }}>{{ footer\_text }} </{{tag}}> </footer> {% endmacro %}

In the template that will use these macros, an import tag is used that specifies the file path to the `my_macros.html` file. It also names the group of macros (in this example `header_footer`). Macros can then be executed by appending the macro name to the name given to the imported template. See the example below.

{% import "custom/page/web\_page\_basic/my\_macros.html" as header\_footer %} {{ header\_footer.header("h1", "My page title") }} <p>Some content</p> {{ header\_footer.footer("h3:", "Company footer info") }}<header><h1>My page title</h1></header> <p>Some content</p> <footer><h3>Company footer info</h3></footer>

From[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#from)
---------------------------------------------------------------------------------

If you want to only import specific macros, instead of all macros contained in a separate .html file, you can use the **from** tag. With the from tag, specify only the macros that you want to import. Generally, using **import** will provide more flexibility, but this alternative is also supported.

The example below accesses the same `my_macros.html` file from the previous section of this article. But this time instead of importing all macros, it accesses only the footer macro.

{% from "custom/page/web\_page\_basic/my\_macros.html" import footer %} {{ footer("h2", "My footer info") }}<footer><h2>My footer info</h2></footer>

Variables within loops[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#variables-within-loops)
---------------------------------------------------------------------------------------------------------------------

Any variables defined within loops are limited to the scope of that loop and cannot be called from outside of the loop.

You can call variables that are defined outside of a loop, from within a loop, but not the other way around. 

You can also use functions in order to mutate objects for settings values on dict's or performing list operations. The following example is using the [`.update` list operation](/docs/cms/hubl/functions#update):

{% set obj = {val : 0} %} {% for i in range(0, 10) %} {% do obj.update({val: obj.val + i }) %} {% endfor %} {{ obj.val }}45

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/variables-macros-syntax#page-feedback)
---------------------------------------------------------------------------------------------------------

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