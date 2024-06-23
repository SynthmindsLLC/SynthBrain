27\. Context Managers[¶](#context-managers "Permalink to this headline")
========================================================================

Context managers allow you to allocate and release resources precisely when you want to. The most widely used example of context managers is the `with` statement. Suppose you have two related operations which you’d like to execute as a pair, with a block of code in between. Context managers allow you to do specifically that. For example:

with open('some\_file', 'w') as opened\_file:
    opened\_file.write('Hola!')

The above code opens the file, writes some data to it and then closes it. If an error occurs while writing the data to the file, it tries to close it. The above code is equivalent to:

file \= open('some\_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()

While comparing it to the first example we can see that a lot of boilerplate code is eliminated just by using `with`. The main advantage of using a `with` statement is that it makes sure our file is closed without paying attention to how the nested block exits.

A common use case of context managers is locking and unlocking resources and closing opened files (as I have already shown you).

Let’s see how we can implement our own Context Manager. This should allow us to understand exactly what’s going on behind the scenes.

27.1. Implementing a Context Manager as a Class:[¶](#implementing-a-context-manager-as-a-class "Permalink to this headline")
----------------------------------------------------------------------------------------------------------------------------

At the very least a context manager has an `__enter__` and `__exit__` method defined. Let’s make our own file-opening Context Manager and learn the basics.

class File(object):
    def \_\_init\_\_(self, file\_name, method):
        self.file\_obj \= open(file\_name, method)
    def \_\_enter\_\_(self):
        return self.file\_obj
    def \_\_exit\_\_(self, type, value, traceback):
        self.file\_obj.close()

Just by defining `__enter__` and `__exit__` methods we can use our new class in a `with` statement. Let’s try:

with File('demo.txt', 'w') as opened\_file:
    opened\_file.write('Hola!')

Our `__exit__` method accepts three arguments. They are required by every `__exit__` method which is a part of a Context Manager class. Let’s talk about what happens under-the-hood.

1.  The `with` statement stores the `__exit__` method of the `File` class.
2.  It calls the `__enter__` method of the `File` class.
3.  The `__enter__` method opens the file and returns it.
4.  The opened file handle is passed to `opened_file`.
5.  We write to the file using `.write()`.
6.  The `with` statement calls the stored `__exit__` method.
7.  The `__exit__` method closes the file.

27.2. Handling Exceptions[¶](#handling-exceptions "Permalink to this headline")
-------------------------------------------------------------------------------

We did not talk about the `type`, `value` and `traceback` arguments of the `__exit__` method. Between the 4th and 6th step, if an exception occurs, Python passes the type, value and traceback of the exception to the `__exit__` method. It allows the `__exit__` method to decide how to close the file and if any further steps are required. In our case we are not paying any attention to them.

What if our file object raises an exception? We might be trying to access a method on the file object which it does not supports. For instance:

with File('demo.txt', 'w') as opened\_file:
    opened\_file.undefined\_function('Hola!')

Let’s list the steps which are taken by the `with` statement when an error is encountered:

1.  It passes the type, value and traceback of the error to the `__exit__` method.
2.  It allows the `__exit__` method to handle the exception.
3.  If `__exit__` returns `True` then the exception was gracefully handled.
4.  If anything other than `True` is returned by the `__exit__` method then the exception is raised by the `with` statement.

In our case the `__exit__` method returns `None` (when no return statement is encountered then the method returns `None`). Therefore, the `with` statement raises the exception:

Traceback (most recent call last):
  File "<stdin>", line 2, in <module\>
AttributeError: 'file' object has no attribute 'undefined\_function'

Let’s try handling the exception in the `__exit__` method:

class File(object):
    def \_\_init\_\_(self, file\_name, method):
        self.file\_obj \= open(file\_name, method)
    def \_\_enter\_\_(self):
        return self.file\_obj
    def \_\_exit\_\_(self, type, value, traceback):
        print("Exception has been handled")
        self.file\_obj.close()
        return True

with File('demo.txt', 'w') as opened\_file:
    opened\_file.undefined\_function()

\# Output: Exception has been handled

Our `__exit__` method returned `True`, therefore no exception was raised by the `with` statement.

This is not the only way to implement Context Managers. There is another way and we will be looking at it in the next section.

27.3. Implementing a Context Manager as a Generator[¶](#implementing-a-context-manager-as-a-generator "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------

We can also implement Context Managers using decorators and generators. Python has a contextlib module for this very purpose. Instead of a class, we can implement a Context Manager using a generator function. Let’s see a basic, useless example:

from contextlib import contextmanager

@contextmanager
def open\_file(name):
    f \= open(name, 'w')
    try:
        yield f
    finally:
        f.close()

Okay! This way of implementing Context Managers appear to be more intuitive and easy. However, this method requires some knowledge about generators, yield and decorators. In this example we have not caught any exceptions which might occur. It works in mostly the same way as the previous method.

Let’s dissect this method a little.

1.  Python encounters the `yield` keyword. Due to this it creates a generator instead of a normal function.
2.  Due to the decoration, contextmanager is called with the function name (`open_file`) as its argument.
3.  The `contextmanager` decorator returns the generator wrapped by the `GeneratorContextManager` object.
4.  The `GeneratorContextManager` is assigned to the `open_file` function. Therefore, when we later call the `open_file` function, we are actually calling the `GeneratorContextManager` object.

So now that we know all this, we can use the newly generated Context Manager like this:

with open\_file('some\_file') as f:
    f.write('hola!')