HubL syntax overview


========================

Last updated: August 1, 2023

HubSpot’s CMS uses the HubSpot Markup Language, referred to as HubL (pronounced “Hubble”). HubL is HubSpot’s extension of [Jinjava](https://github.com/HubSpot/jinjava), a templating engine based on [Jinja](https://jinja.palletsprojects.com/en/latest/). HubL uses a fair amount of markup that is unique to HubSpot and does not support all features of Jinja.

This article will take you through the basics of HubL's features and syntax.

Types of delimiters[](https://developers.hubspot.com/docs/cms/hubl#types-of-delimiters)
---------------------------------------------------------------------------------------

Similar to other commonly used templating languages such as PHP, HubL can be mixed into your HTML in coded templates files or HubL template modules. In order to differentiate, where your HubL starts and ends, you will need to learn a few key symbols that act as delimiters.

{% %} - statement delimiters {{ }} - expression delimiters {# #} - comment delimiters

Be mindful of nesting comments in your code, as it can result in the trailing comment tag to render as text.

### Statements[](https://developers.hubspot.com/docs/cms/hubl#statements)

HubL statements are used to create editable modules, define conditional template logic, set up for loops, define variables, and more. Statements are delimited by `{%`.  They do not print anything to the page.

### Expressions[](https://developers.hubspot.com/docs/cms/hubl#expressions)

Expressions print values stored in the context of the template. Expressions are delimited by `{{`. For example, a variable must be defined as a statement, but then a HubL expression would be used to print the variable.

#### Do tag[](https://developers.hubspot.com/docs/cms/hubl#do-tag)

The 'do' tag works exactly like the regular statements `{% ... %}`;  This can be used to modify lists and dictionaries.  
  
Note: When adding to arrays, you want to use [`.append()`](/docs/cms/hubl/functions#append) and when adding to objects, you want to use [`.update()`](/docs/cms/hubl/functions#update)

\# Arrays {% set navigation = \["Home", "About"\] %} {% do navigation.append("Contact Us") %} {{navigation}} # Objects {% set book = {"name" : "Rocking HubL", "author" : "John Smith" }%} {% do book.update({"ebook" : "yes"}) %} {{book}}\# Arrays \[Home, About, Contact Us\] # Objects {name=Rocking HubL, author=John Smith, ebook=yes}

### Comments[](https://developers.hubspot.com/docs/cms/hubl#comments)

The final type of delimiter that you may encounter or decide to employ while developing with HubL, is a HubL comment. Comments are defined by a `{#`. 

Modules[](https://developers.hubspot.com/docs/cms/hubl#modules)
---------------------------------------------------------------

[Modules](/docs/cms/building-blocks/modules) are dynamic areas of a template that can be customized by the end user in the content editor. For example, if you were coding a template file from scratch, you would add modules to templates with HubL tags, to give your content creators the ability to edit areas of the page.

Module tags are made up of the following components:

*   **Type of module:** specifies which module to render. Please refer to the [HubL Supported Tags](/docs/cms/hubl/tags) page for a listing of the different types of modules available.
*   **A unique name for that module:** gives the module a unique identity in the context of the template.
*   **Path:** depending on the tag, defines the location of where the module is in the design manager. The path for HubSpot default modules should always start with @hubspot/ followed by the type of module. See the example below and the [using modules in templates page](/docs/cms/building-blocks/modules/using-modules-in-templates) for more. 
*   **Parameters:** optionally specify additional module information.

{% module "unique\_module\_name", path="@hubspot/text", label="Single Text Line", value="This is a single text line" %}<div class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_module widget-type-text widget-type-text" data-hs-cos-general-type="widget" data-hs-cos-type="module" id="hs\_cos\_wrapper\_text" style=""> <span class="hs\_cos\_wrapper hs\_cos\_wrapper\_widget hs\_cos\_wrapper\_type\_text" data-hs-cos-general-type="widget" data-hs-cos-type="text" id="hs\_cos\_wrapper\_text\_" style="">This is a single text line</span> </div>

The example above is a text module with the label and value parameters defined. The label defines the help text in the editor and value sets the default text for that module. See the sample gif below for how this looks inside of the editor.

![module-label-value-min](https://developers.hubspot.com/hubfs/module-label-value-min.gif "module-label-value-min")

You can [learn more about using modules in templates, here](/docs/cms/building-blocks/modules/using-modules-in-templates). 

Variables and macros[](https://developers.hubspot.com/docs/cms/hubl#variables-and-macros)
-----------------------------------------------------------------------------------------

HubL includes many [predefined HubSpot variables](/docs/cms/hubl/variables) that print their helpful values from the app. In addition, you can [define your own variables in a template](/docs/cms/hubl/variables-macros-syntax). In the following example, a variable named `primaryColor` is defined in a statement and then printed with a HubL expression. This example mixes the HubL variable with CSS. 

{% set primaryColor = '#F7761F' %} {# defines variable and assigns HEX color #} a { color: {{ primaryColor }}; {# prints variable HEX value #} }a { color:#F7761F; }

HubL macros allow you to print multiple statements with a dynamic value. This technique proves useful when you find yourself writing the same basic code blocks over and over, but only need to change certain values. In the following example, a macro is used to print a CSS3 transition property that includes all the vendor prefixes. You can [learn more about macros, here](/docs/cms/hubl/variables-macros-syntax#macros). 

{% macro trans(value) %} -webkit-transition: {{value}}; -moz-transition: {{value}}; -o-transition: {{value}}; -ms-transition: {{value}}; transition: {{value}}; {% endmacro %} a { {{ trans("all .2s ease-in-out") }} }a { -webkit-transition: all .2s ease-in-out; -moz-transition: all .2s ease-in-out; -o-transition: all .2s ease-in-out; -ms-transition: all .2s ease-in-out; transition: all .2s ease-in-out; }

Filters and functions[](https://developers.hubspot.com/docs/cms/hubl#filters-and-functions)
-------------------------------------------------------------------------------------------

Filters can be added to your HubL to transform or alter the value of a template variable. A simple example displayed below is formatting a date variable. Filters use a | (pipeline symbol) and are applied without spaces to a variable.

In the example below, assume a blog post was published on the 29th of April. The publish date of the post is formatted with a `datetimeformat` filter. [You can view a full list of filters here.](/docs/cms/hubl/filters)

{{ content.publish\_date\_local\_time|datetimeformat("%B %e, %Y") }} April 29, 2020

While filters affect how variables render, functions process value and account information and render that info. For example, a function can be used to get the total number of posts for a particular blog or to lighten/darken a color variable by a particular amount.

The example would print the total number of blog posts from the designers.hubspot.com/blog. It uses a Blog ID (available in the URL of the blog dashboard) parameter to specify which blog to target. [You can view a full list of functions here](/docs/cms/hubl/functions).

// blog\_total\_post\_count {{ blog\_total\_post\_count(359485112) }}2

If statements[](https://developers.hubspot.com/docs/cms/hubl#if-statements)
---------------------------------------------------------------------------

[If statements](/docs/cms/hubl/if-statements) allow you to use conditional logic to dictate how your template will render conditional logic in HubL statements for `if`, `elif`, `else`, and `endif`. An if statement must begin with an `if` and end with an `endif`. 

The example below defines a choice module that lets the end user select a department from a dropdown. Depending on what the user selects in the editor, the template will generate a dynamic heading for a careers page. This example requires the use of the [`export_to_template_context`](/docs/cms/building-blocks/modules/export-to-template-context) parameter.

{% choice "department" label="Choose department", value="Marketing", choices="Marketing, Sales, Dev, Services" export\_to\_template\_context=True %} {% if widget\_data.department.value == "Marketing" %} <h3>Want to join our amazing Marketing team?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% elif widget\_data.department.value == "Sales" %} <h3>Are you a Sales superstar?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% elif widget\_data.department.value == "Dev" %} <h3>Do you love to ship code?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% else %} <h3>Want to work with our awesome customers?</h3> <h4>We have exciting career opportunities on the {{ widget\_data.department.value }} team.</h4> {% endif %}

For loops[](https://developers.hubspot.com/docs/cms/hubl#for-loops)
-------------------------------------------------------------------

[For loops](/docs/cms/hubl/for-loops) allow you to iterate over items stored in a sequence. They will most commonly be used with rendering blog content in a listing format. For loops begin with a `for` statement and end with an `endfor` statement.

In the example below, an array of types of bears is stored as a variable called `bears`. A for loop is then used to iterate through the different types of bears printing a list item for each type. 

{% set bears = \["panda bear", "polar bear", "black bear", "grizzly bear", "koala bear"\] %} <h1>Types of bears</h1> <ul> {% for bear in bears %} <li>{{ bear }}</li> {% endfor %} </ul><h1>Types of bears</h1> <ul> <li>panda bear</li> <li>polar bear</li> <li>black bear</li> <li>grizzly bear</li> <li>koala bear</li> </ul>

Other HubL features[](https://developers.hubspot.com/docs/cms/hubl#other-hubl-features)
---------------------------------------------------------------------------------------

Below are a few other miscellaneous templating features that may be useful, as you develop with HubL.

### Escaping HubL delimiters[](https://developers.hubspot.com/docs/cms/hubl#escaping-hubl-delimiters)

Many other languages share the same delimiters as HubL, which can create issues when working in coded files on the CMS. If you want to use a HubL delimiter for a different language, you need to wrap that code in:

{% raw %} {{"Code you want to escape"}} {% endraw %}{{"Code you want to escape"}}

### Including files in files[](https://developers.hubspot.com/docs/cms/hubl#including-files-in-files)

You can include multiple `.html` files in one [HubL template](/docs/cms/building-blocks/templates/html-hubl-templates) using the [include tag](/docs/cms/building-blocks/templates/html-hubl-templates#standard-partials). In order to create an HTML file that does not require the standard template variables, you must uncheck the option "Make template available for new content." The syntax is displayed below:

{% include "custom/page/web\_page\_basic/my\_footer.html" %} {% include "hubspot/styles/patches/recommended.css" %}

You can also compile multiple CSS files into a single CSS file with the same include tag. When you publish the parent file, the child file will be compiled into a single minified CSS file with the parent's code. 

### Blocks and extends[](https://developers.hubspot.com/docs/cms/hubl#blocks-and-extends)

When creating complex templates, you can use create compartmentalized blocks that extend a parent template.

First, you'll create a main template that includes the required [`standard_header_includes`](/docs/cms/hubl/variables#required-page-template-variables) and [`standard_footer_includes`](/docs/cms/hubl/variables#required-page-template-variables) variables. Within that template, you need to define a unique block using the following syntax where `my_sidebar` is a unique name:

{% extends "custom/page/web\_page\_basic/my\_template.html" %} {% block my\_sidebar %} <h3>Sidebar title</h3> <ul> <li>Bullet 1<li> <li>Bullet 2<li> <li>Bullet 3<li> </ul> {% endblock %}

Next, you can create a child HTML file that will populate that block. First, you must declare an [extends statement](/docs/cms/building-blocks/templates/html-hubl-templates#blocks-and-extends) that references the path to the parent. This block of code would be rendered in the parent template but maintained in another smaller and more manageable file. This technique is not for everyone but can be useful to stay organized when coding complex email or page templates.  When using this technique, you should choose the child template, when creating content.

### Copy section HubL[](https://developers.hubspot.com/docs/cms/hubl#copy-section-hubl)

In the page editor, you can copy the HubL markup for a [drag and drop section](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections) to reuse the code as needed. This can be helpful when wanting to recreate a drag and drop section in a coded file.

![copy-section-hubl-menu](https://developers.hubspot.com/hs-fs/hubfs/Knowledge_Base_2021/Developer/copy-section-hubl-menu.png?width=698&name=copy-section-hubl-menu.png)

Learn more about [copying section HubL.](/docs/cms/building-blocks/templates/drag-and-drop-areas/sections#copy-section-hubl)

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl#page-feedback)
---------------------------------------------------------------------------------

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