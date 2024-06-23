Note

You can sign up to my [mailing list](http://eepurl.com/bwjcej) so that you remain in sync with any major updates to this book or my future projects!

Intermediate Python[¶](#intermediate-python "Permalink to this headline")
=========================================================================

Preface[¶](#preface "Permalink to this headline")
-------------------------------------------------

Python is an amazing language with a strong and friendly community of programmers. However, there is a lack of documentation on what to learn after getting the basics of Python down your throat. Through this book I aim to solve this problem. I would give you bits of information about some interesting topics which you can further explore.

The topics which are discussed in this book open up your mind towards some nice corners of Python language. This book is an outcome of my desire to have something like this when I was beginning to learn Python.

If you are a beginner, intermediate or even an advanced programmer there is something for you in this book.

Please note that this book is not a tutorial and does not teach you Python. The topics are not explained in depth, instead only the minimum required information is given.

I am sure you are as excited as I am so let’s start!

**Note:** This book is a continuous work in progress. If you find anything which you can further improve (I know you will find a lot of stuff) then kindly submit a pull request!

Author[¶](#author "Permalink to this headline")
-----------------------------------------------

I am Muhammad Yasoob Ullah Khalid. I have been programming extensively in Python for over 3 years now. I have been involved in a lot of Open Source projects. I regularly blog about interesting Python topics over at my [blog](http://www.pythontips.com) . In 2014 I also spoke at EuroPython which was held in Berlin. It is the biggest Python conference in Europe. If you have an interesting Internship opportunity for me then I would definitely like to hear from you!

Table of Contents[¶](#table-of-contents "Permalink to this headline")
---------------------------------------------------------------------

*   [1\. \*args and \*\*kwargs](args_and_kwargs.html.md)
    *   [1.1. Usage of \*args](args_and_kwargs.html.md#usage-of-args)
    *   [1.2. Usage of \*\*kwargs](args_and_kwargs.html.md#usage-of-kwargs)
    *   [1.3. Using \*args and \*\*kwargs to call a function](args_and_kwargs.html.md#using-args-and-kwargs-to-call-a-function)
    *   [1.4. When to use them?](args_and_kwargs.html.md#when-to-use-them)
*   [2\. Debugging](debugging.html.md)
*   [3\. Generators](generators.html.md)
    *   [3.1. Iterable](generators.html.md#iterable)
    *   [3.2. Iterator](generators.html.md#iterator)
    *   [3.3. Iteration](generators.html.md#iteration)
    *   [3.4. Generators](generators.html.md#id1)
*   [4\. Map, Filter and Reduce](map_filter.html.md)
    *   [4.1. Map](map_filter.html.md#map)
    *   [4.2. Filter](map_filter.html.md#filter)
    *   [4.3. Reduce](map_filter.html.md#reduce)
*   [5\. `set` Data Structure](set_-_data_structure.html.md)
*   [6\. Ternary Operators](ternary_operators.html.md)
*   [7\. Decorators](decorators.html.md)
    *   [7.1. Everything in Python is an object:](decorators.html.md#everything-in-python-is-an-object)
    *   [7.2. Defining functions within functions:](decorators.html.md#defining-functions-within-functions)
    *   [7.3. Returning functions from within functions:](decorators.html.md#returning-functions-from-within-functions)
    *   [7.4. Giving a function as an argument to another function:](decorators.html.md#giving-a-function-as-an-argument-to-another-function)
    *   [7.5. Writing your first decorator:](decorators.html.md#writing-your-first-decorator)
    *   [7.6. Decorators with Arguments](decorators.html.md#decorators-with-arguments)
*   [8\. Global & Return](global_&_return.html.md)
    *   [8.1. Multiple return values](global_&_return.html.md#multiple-return-values)
*   [9\. Mutation](mutation.html.md)
*   [10\. \_\_slots\_\_ Magic](__slots__magic.html.md)
*   [11\. Virtual Environment](virtual_environment.html.md)
*   [12\. Collections](collections.html.md)
    *   [12.1. `defaultdict`](collections.html.md#defaultdict)
    *   [12.2. `OrderedDict`](collections.html.md#ordereddict)
    *   [12.3. `Counter`](collections.html.md#counter)
    *   [12.4. `deque`](collections.html.md#deque)
    *   [12.5. `namedtuple`](collections.html.md#namedtuple)
    *   [12.6. `enum.Enum` (Python 3.4+)](collections.html.md#enum-enum-python-3-4)
*   [13\. Enumerate](enumerate.html.md)
*   [14\. Zip and unzip](zip.html.md)
*   [15\. Object introspection](object_introspection.html.md)
    *   [15.1. `dir`](object_introspection.html.md#dir)
    *   [15.2. `type` and `id`](object_introspection.html.md#type-and-id)
    *   [15.3. `inspect` module](object_introspection.html.md#inspect-module)
*   [16\. Comprehensions](comprehensions.html.md)
    *   [16.1. `list` comprehensions](comprehensions.html.md#list-comprehensions)
    *   [16.2. `dict` comprehensions](comprehensions.html.md#dict-comprehensions)
    *   [16.3. `set` comprehensions](comprehensions.html.md#set-comprehensions)
    *   [16.4. `generator` comprehensions](comprehensions.html.md#generator-comprehensions)
*   [17\. Exceptions](exceptions.html.md)
    *   [17.1. Handling multiple exceptions:](exceptions.html.md#handling-multiple-exceptions)
*   [18\. Classes](classes.html.md)
    *   [18.1. 1. Instance & Class variables](classes.html.md#instance-class-variables)
    *   [18.2. 2. New style classes](classes.html.md#new-style-classes)
    *   [18.3. 3. Magic Methods](classes.html.md#magic-methods)
*   [19\. Lambdas](lambdas.html.md)
*   [20\. One-Liners](one_liners.html.md)
*   [21\. `for/else`](for_-_else.html.md)
    *   [21.1. `else` Clause](for_-_else.html.md#else-clause)
*   [22\. Python C extensions](python_c_extension.html.md)
    *   [22.1. CTypes](python_c_extension.html.md#ctypes)
    *   [22.2. SWIG](python_c_extension.html.md#swig)
    *   [22.3. Python/C API](python_c_extension.html.md#python-c-api)
*   [23\. `open` Function](open_function.html.md)
*   [24\. Targeting Python 2+3](targeting_python_2_3.html.md)
*   [25\. Coroutines](coroutines.html.md)
*   [26\. Function caching](function_caching.html.md)
    *   [26.1. Python 3.2+](function_caching.html.md#python-3-2)
    *   [26.2. Python 2+](function_caching.html.md#python-2)
*   [27\. Context Managers](context_managers.html.md)
    *   [27.1. Implementing a Context Manager as a Class:](context_managers.html.md#implementing-a-context-manager-as-a-class)
    *   [27.2. Handling Exceptions](context_managers.html.md#handling-exceptions)
    *   [27.3. Implementing a Context Manager as a Generator](context_managers.html.md#implementing-a-context-manager-as-a-generator)