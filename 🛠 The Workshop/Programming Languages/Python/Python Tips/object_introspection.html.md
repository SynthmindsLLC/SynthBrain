15\. Object introspection[¶](#object-introspection "Permalink to this headline")
================================================================================

In computer programming, introspection is the ability to determine the type of an object at runtime. It is one of Python’s strengths. Everything in Python is an object and we can examine those objects. Python ships with a few built-in functions and modules to help us.

15.1. `dir`[¶](#dir "Permalink to this headline")
-------------------------------------------------

In this section we will learn about `dir` and how it facilitates us in introspection.

It is one of the most important functions for introspection. It returns a list of attributes and methods belonging to an object. Here is an example:

my\_list \= \[1, 2, 3\]
dir(my\_list)
\# Output: \['\_\_add\_\_', '\_\_class\_\_', '\_\_contains\_\_', '\_\_delattr\_\_', '\_\_delitem\_\_',
\# '\_\_delslice\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_',
\# '\_\_getitem\_\_', '\_\_getslice\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_iadd\_\_', '\_\_imul\_\_',
\# '\_\_init\_\_', '\_\_iter\_\_', '\_\_le\_\_', '\_\_len\_\_', '\_\_lt\_\_', '\_\_mul\_\_', '\_\_ne\_\_',
\# '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_reversed\_\_', '\_\_rmul\_\_',
\# '\_\_setattr\_\_', '\_\_setitem\_\_', '\_\_setslice\_\_', '\_\_sizeof\_\_', '\_\_str\_\_',
\# '\_\_subclasshook\_\_', 'append', 'count', 'extend', 'index', 'insert', 'pop',
\# 'remove', 'reverse', 'sort'\]

Our introspection gave us the names of all the methods of a list. This can be handy when you are not able to recall a method name. If we run `dir()` without any argument then it returns all names in the current scope.

15.2. `type` and `id`[¶](#type-and-id "Permalink to this headline")
-------------------------------------------------------------------

The `type` function returns the type of an object. For example:

print(type(''))
\# Output: <type 'str'>

print(type(\[\]))
\# Output: <type 'list'>

print(type({}))
\# Output: <type 'dict'>

print(type(dict))
\# Output: <type 'type'>

print(type(3))
\# Output: <type 'int'>

`id` returns the unique ids of various objects. For instance:

name \= "Yasoob"
print(id(name))
\# Output: 139972439030304

15.3. `inspect` module[¶](#inspect-module "Permalink to this headline")
-----------------------------------------------------------------------

The inspect module also provides several useful functions to get information about live objects. For example you can check the members of an object by running:

import inspect
print(inspect.getmembers(str))
\# Output: \[('\_\_add\_\_', <slot wrapper '\_\_add\_\_' of ... ...

There are a couple of other methods as well which help in introspection. You can explore them if you wish.