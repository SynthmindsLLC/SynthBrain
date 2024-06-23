[![](https://img.realpython.net/8899c4a6d15334a6b9f769e9f8bc0cf7)](https://srv.realpython.net/click/41686012779/?c=7309556696&p=29182759436&r=15488)

Common Gotchas[¶](#common-gotchas "Permalink to this headline")
===============================================================

![https://d33wubrfki0l68.cloudfront.net/f15cf03ffa1e6648c43936d1c96e0deb0acae7af/0b6a3/_images/34435688380_b5a740762b_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/f15cf03ffa1e6648c43936d1c96e0deb0acae7af/0b6a3/_images/34435688380_b5a740762b_k_d.jpg)

For the most part, Python aims to be a clean and consistent language that avoids surprises. However, there are a few cases that can be confusing for newcomers.

Some of these cases are intentional but can be potentially surprising. Some could arguably be considered language warts. In general, what follows is a collection of potentially tricky behavior that might seem strange at first glance, but are generally sensible, once you’re aware of the underlying cause for the surprise.

Mutable Default Arguments[¶](#mutable-default-arguments "Permalink to this headline")
-------------------------------------------------------------------------------------

Seemingly the _most_ common surprise new Python programmers encounter is Python’s treatment of mutable default arguments in function definitions.

### What You Wrote[¶](#what-you-wrote "Permalink to this headline")

def append\_to(element, to\=\[\]):
    to.append(element)
    return to

### What You Might Have Expected to Happen[¶](#what-you-might-have-expected-to-happen "Permalink to this headline")

my\_list \= append\_to(12)
print(my\_list)

my\_other\_list \= append\_to(42)
print(my\_other\_list)

A new list is created each time the function is called if a second argument isn’t provided, so that the output is:

\[12\]
\[42\]

### What Actually Happens[¶](#what-actually-happens "Permalink to this headline")

\[12\]
\[12, 42\]

A new list is created _once_ when the function is defined, and the same list is used in each successive call.

Python’s default arguments are evaluated _once_ when the function is defined, not each time the function is called (like it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you _will_ and have mutated that object for all future calls to the function as well.

### What You Should Do Instead[¶](#what-you-should-do-instead "Permalink to this headline")

Create a new object each time the function is called, by using a default arg to signal that no argument was provided ([`None`](https://docs.python.org/3/library/constants.html#None "(in Python v3.11)") is often a good choice).

def append\_to(element, to\=None):
    if to is None:
        to \= \[\]
    to.append(element)
    return to

Do not forget, you are passing a _list_ object as the second argument.

### When the Gotcha Isn’t a Gotcha[¶](#when-the-gotcha-isn-t-a-gotcha "Permalink to this headline")

Sometimes you can specifically “exploit” (read: use as intended) this behavior to maintain state between calls of a function. This is often done when writing a caching function.

Late Binding Closures[¶](#late-binding-closures "Permalink to this headline")
-----------------------------------------------------------------------------

Another common source of confusion is the way Python binds its variables in closures (or in the surrounding global scope).

### What You Wrote[¶](#id1 "Permalink to this headline")

def create\_multipliers():
    return \[lambda x : i \* x for i in range(5)\]

### What You Might Have Expected to Happen[¶](#id2 "Permalink to this headline")

for multiplier in create\_multipliers():
    print(multiplier(2))

A list containing five functions that each have their own closed-over `i` variable that multiplies their argument, producing:

0
2
4
6
8

### What Actually Happens[¶](#id3 "Permalink to this headline")

8
8
8
8
8

Five functions are created; instead all of them just multiply `x` by 4.

Python’s closures are _late binding_. This means that the values of variables used in closures are looked up at the time the inner function is called.

Here, whenever _any_ of the returned functions are called, the value of `i` is looked up in the surrounding scope at call time. By then, the loop has completed and `i` is left with its final value of 4.

What’s particularly nasty about this gotcha is the seemingly prevalent misinformation that this has something to do with [lambdas](https://docs.python.org/3/reference/expressions.html#lambda "(in Python v3.11)") in Python. Functions created with a `lambda` expression are in no way special, and in fact the same exact behavior is exhibited by just using an ordinary `def`:

def create\_multipliers():
    multipliers \= \[\]

    for i in range(5):
        def multiplier(x):
            return i \* x
        multipliers.append(multiplier)

    return multipliers

### What You Should Do Instead[¶](#id4 "Permalink to this headline")

The most general solution is arguably a bit of a hack. Due to Python’s aforementioned behavior concerning evaluating default arguments to functions (see [Mutable Default Arguments](#default-args)), you can create a closure that binds immediately to its arguments by using a default arg like so:

def create\_multipliers():
    return \[lambda x, i\=i : i \* x for i in range(5)\]

Alternatively, you can use the functools.partial function:

from functools import partial
from operator import mul

def create\_multipliers():
    return \[partial(mul, i) for i in range(5)\]

### When the Gotcha Isn’t a Gotcha[¶](#id5 "Permalink to this headline")

Sometimes you want your closures to behave this way. Late binding is good in lots of situations. Looping to create unique functions is unfortunately a case where they can cause hiccups.

Bytecode (.pyc) Files Everywhere![¶](#bytecode-pyc-files-everywhere "Permalink to this headline")
-------------------------------------------------------------------------------------------------

By default, when executing Python code from files, the Python interpreter will automatically write a bytecode version of that file to disk, e.g. `module.pyc`.

These `.pyc` files should not be checked into your source code repositories.

Theoretically, this behavior is on by default for performance reasons. Without these bytecode files, Python would re-generate the bytecode every time the file is loaded.

### Disabling Bytecode (.pyc) Files[¶](#disabling-bytecode-pyc-files "Permalink to this headline")

Luckily, the process of generating the bytecode is extremely fast, and isn’t something you need to worry about while developing your code.

Those files are annoying, so let’s get rid of them!

$ export PYTHONDONTWRITEBYTECODE=1

With the `$PYTHONDONTWRITEBYTECODE` environment variable set, Python will no longer write these files to disk, and your development environment will remain nice and clean.

I recommend setting this environment variable in your `~/.profile`.

### Removing Bytecode (.pyc) Files[¶](#removing-bytecode-pyc-files "Permalink to this headline")

Here’s nice trick for removing all of these files, if they already exist:

$ find . -type f -name "\*.py\[co\]" -delete -or -type d -name "\_\_pycache\_\_" -delete

Run that from the root directory of your project, and all `.pyc` files will suddenly vanish. Much better.

### Version Control Ignores[¶](#version-control-ignores "Permalink to this headline")

If you still need the `.pyc` files for performance reasons, you can always add them to the ignore files of your version control repositories. Popular version control systems have the ability to use wildcards defined in a file to apply special rules.

An ignore file will make sure the matching files don’t get checked into the repository. [Git](https://git-scm.com/) uses `.gitignore` while [Mercurial](https://www.mercurial-scm.org/) uses `.hgignore`.

At the minimum your ignore files should look like this.

syntax:glob   \# This line is not needed for .gitignore files.
\*.py\[cod\]     \# Will match .pyc, .pyo and .pyd files.
\_\_pycache\_\_/  \# Exclude the whole folder

You may wish to include more files and directories depending on your needs. The next time you commit to the repository, these files will not be included.