18\. Classes[¶](#classes "Permalink to this headline")
======================================================

Classes are the core of Python. They give us a lot of power but it is really easy to misuse this power. In this section I will share some obscure tricks and caveats related to `classes` in Python. Let’s get going!

18.1. 1. Instance & Class variables[¶](#instance-class-variables "Permalink to this headline")
----------------------------------------------------------------------------------------------

Most beginners and even some advanced Python programmers do not understand the distinction between instance and class variables. Their lack of understanding forces them to use these different types of variables incorrectly. Let’s understand them.

The basic difference is:

*   Instance variables are for data which is unique to every object
*   Class variables are for data shared between different instances of a class

Let’s take a look at an example:

class Cal(object):
    \# pi is a class variable
    pi \= 3.142

    def \_\_init\_\_(self, radius):
        \# self.radius is an instance variable
        self.radius \= radius

    def area(self):
        return self.pi \* (self.radius \*\* 2)

a \= Cal(32)
a.area()
\# Output: 3217.408
a.pi
\# Output: 3.142
a.pi \= 43
a.pi
\# Output: 43

b \= Cal(44)
b.area()
\# Output: 6082.912
b.pi
\# Output: 3.142
b.pi \= 50
b.pi
\# Output: 50

There are not many issues while using immutable class variables. This is the major reason due to which beginners do not try to learn more about this subject because everything works! If you also believe that instance and class variables can not cause any problem if used incorrectly then check the next example.

class SuperClass(object):
    superpowers \= \[\]

    def \_\_init\_\_(self, name):
        self.name \= name

    def add\_superpower(self, power):
        self.superpowers.append(power)

foo \= SuperClass('foo')
bar \= SuperClass('bar')
foo.name
\# Output: 'foo'

bar.name
\# Output: 'bar'

foo.add\_superpower('fly')
bar.superpowers
\# Output: \['fly'\]

foo.superpowers
\# Output: \['fly'\]

That is the beauty of the wrong usage of mutable class variables. To make your code safe against this kind of surprise attacks then make sure that you do not use mutable class variables. You may use them only if you know what you are doing.

18.2. 2. New style classes[¶](#new-style-classes "Permalink to this headline")
------------------------------------------------------------------------------

New style classes were introduced in Python 2.1 but a lot of people do not know about them even now! It is so because Python also supports old style classes just to maintain backward compatibility. I have said a lot about new and old but I have not told you about the difference. Well the major difference is that:

*   Old base classes do not inherit from anything
*   New style base classes inherit from `object`

A very basic example is:

class OldClass():
    def \_\_init\_\_(self):
        print('I am an old class')

class NewClass(object):
    def \_\_init\_\_(self):
        print('I am a jazzy new class')

old \= OldClass()
\# Output: I am an old class

new \= NewClass()
\# Output: I am a jazzy new class

This inheritance from `object` allows new style classes to utilize some _magic_. A major advantage is that you can employ some useful optimizations like `__slots__`. You can use `super()` and descriptors and the likes. Bottom line? Always try to use new-style classes.

**Note:** Python 3 only has new-style classes. It does not matter whether you subclass from `object` or not. However it is recommended that you still subclass from `object`.

18.3. 3. Magic Methods[¶](#magic-methods "Permalink to this headline")
----------------------------------------------------------------------

Python’s classes are famous for their magic methods, commonly called **dunder** (double underscore) methods. I am going to discuss a few of them.

*   `__init__`

It is a class initializer. Whenever an instance of a class is created its `__init__` method is called. For example:

class GetTest(object):
    def \_\_init\_\_(self):
        print('Greetings!!')
    def another\_method(self):
        print('I am another method which is not'
              ' automatically called')

a \= GetTest()
\# Output: Greetings!!

a.another\_method()
\# Output: I am another method which is not automatically
\# called

You can see that `__init__` is called immediately after an instance is created. You can also pass arguments to the class during its initialization. Like this:

class GetTest(object):
    def \_\_init\_\_(self, name):
        print('Greetings!! {0}'.format(name))
    def another\_method(self):
        print('I am another method which is not'
              ' automatically called')

a \= GetTest('yasoob')
\# Output: Greetings!! yasoob

\# Try creating an instance without the name arguments
b \= GetTest()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module\>
TypeError: \_\_init\_\_() takes exactly 2 arguments (1 given)

I am sure that now you understand the `__init__` method.

*   `__getitem__`

Implementing **getitem** in a class allows its instances to use the \[\] (indexer) operator. Here is an example:

class GetTest(object):
    def \_\_init\_\_(self):
        self.info \= {
            'name':'Yasoob',
            'country':'Pakistan',
            'number':12345812
        }

    def \_\_getitem\_\_(self,i):
        return self.info\[i\]

foo \= GetTest()

foo\['name'\]
\# Output: 'Yasoob'

foo\['number'\]
\# Output: 12345812

Without the `__getitem__` method we would have got this error:

\>>> foo\['name'\]

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'GetTest' object has no attribute '\_\_getitem\_\_'