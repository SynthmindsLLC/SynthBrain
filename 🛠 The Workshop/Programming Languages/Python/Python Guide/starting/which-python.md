[![](https://img.realpython.net/1c3e33fa8ce0d82a964b7f7de310e4bb)](https://srv.realpython.net/click/21871400699/?c=41831496980&p=29182759436&r=81493)

Picking a Python Interpreter (3 vs 2)[¶](#picking-a-python-interpreter-3-vs-2 "Permalink to this headline")
===========================================================================================================

![https://d33wubrfki0l68.cloudfront.net/3bf66d6a0daa986e254a5d7a425020b10a8aabab/d2960/_images/34484834733_5b80f65ab1_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/3bf66d6a0daa986e254a5d7a425020b10a8aabab/d2960/_images/34484834733_5b80f65ab1_k_d.jpg)

The State of Python (3 & 2)[¶](#the-state-of-python-3-2 "Permalink to this headline")
-------------------------------------------------------------------------------------

When choosing a Python interpreter, one looming question is always present: “Should I choose Python 2 or Python 3”? The answer is a bit more subtle than one might think.

The basic gist of the state of things is as follows:

1.  Most production applications today use Python 3.
2.  Python 3 is ready for the production deployment of applications today.
3.  Python 2 reached the end of its life on January 1, 2020 [\[6\]](#pep373-eol).
4.  The brand name “Python” encapsulates both Python 3 and Python 2.

Recommendations[¶](#recommendations "Permalink to this headline")
-----------------------------------------------------------------

Note

The use of **Python 3** is _highly_ recommended over Python 2. Consider upgrading your applications and infrastructure if you find yourself _still_ using Python 2 in production today. If you are using Python 3, congratulations — you are indeed a person of excellent taste. —_Kenneth Reitz_

I’ll be blunt:

*   Use Python 3 for new Python applications.
*   If you’re learning Python for the first time, familiarizing yourself with Python 2.7 will be very useful, but not more useful than learning Python 3.
*   Learn both. They are both “Python”.

So…. 3?[¶](#so-3 "Permalink to this headline")
----------------------------------------------

If you’re choosing a Python interpreter to use, I recommend you use the newest Python 3.x, since every version brings new and improved standard library modules, security and bug fixes.

Given such, only use Python 2 if you have a strong reason to, such as a pre-existing code-base, a Python 2 exclusive library, simplicity/familiarity, or, of course, you absolutely love and are inspired by Python 2. No harm in that.

[Further Reading](http://wiki.python.org/moin/Python2orPython3)

It is possible to [write code that works on Python 2.6, 2.7, and Python 3](https://docs.python.org/3/howto/pyporting.html). This ranges from trivial to hard depending upon the kind of software you are writing; if you’re a beginner there are far more important things to worry about.

Implementations[¶](#implementations "Permalink to this headline")
-----------------------------------------------------------------

When people speak of _Python_ they often mean not just the language but also the CPython implementation. _Python_ is actually a specification for a language that can be implemented in many different ways.

### CPython[¶](#cpython "Permalink to this headline")

[CPython](http://www.python.org) is the reference implementation of Python, written in C. It compiles Python code to intermediate bytecode which is then interpreted by a virtual machine. CPython provides the highest level of compatibility with Python packages and C extension modules.

If you are writing open source Python code and want to reach the widest possible audience, targeting CPython is best. To use packages which rely on C extensions to function, CPython is your only implementation option.

All versions of the Python language are implemented in C because CPython is the reference implementation.

### PyPy[¶](#pypy "Permalink to this headline")

[PyPy](http://pypy.org/) is a Python interpreter implemented in a restricted statically-typed subset of the Python language called RPython. The interpreter features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).

PyPy aims for maximum compatibility with the reference CPython implementation while improving performance.

If you are looking to increase performance of your Python code, it’s worth giving PyPy a try. On a suite of benchmarks, it’s currently [over 5 times faster than CPython](http://speed.pypy.org/).

PyPy supports Python 2.7. PyPy3 [\[1\]](#pypy-ver), released in beta, targets Python 3.

### Jython[¶](#jython "Permalink to this headline")

[Jython](http://www.jython.org/) is a Python implementation that compiles Python code to Java bytecode which is then executed by the JVM (Java Virtual Machine). Additionally, it is able to import and use any Java class like a Python module.

If you need to interface with an existing Java codebase or have other reasons to need to write Python code for the JVM, Jython is the best choice.

Jython currently supports up to Python 2.7. [\[2\]](#jython-ver)

### IronPython[¶](#ironpython "Permalink to this headline")

[IronPython](http://ironpython.net/) is an implementation of Python for the .NET framework. It can use both Python and .NET framework libraries, and can also expose Python code to other languages in the .NET framework.

[Python Tools for Visual Studio](http://ironpython.net/tools/) integrates IronPython directly into the Visual Studio development environment, making it an ideal choice for Windows developers.

IronPython supports Python 2.7. [\[3\]](#iron-ver) IronPython 3 [\[4\]](#iron-ver3) is being developed, but is not ready for use as of September 2020.

### PythonNet[¶](#pythonnet "Permalink to this headline")

[Python for .NET](http://pythonnet.github.io/) is a package which provides near seamless integration of a natively installed Python installation with the .NET Common Language Runtime (CLR). This is the inverse approach to that taken by IronPython (see above), to which it is more complementary than competing with.

In conjunction with Mono, pythonnet enables native Python installations on non-Windows operating systems, such as OS X and Linux, to operate within the .NET framework. It can be run in addition to IronPython without conflict.

Pythonnet is compatible with Python 2.7 and 3.5-3.8. [\[5\]](#pythonnet-ver1)

<table class="docutils footnote" frame="void" id="pypy-ver" rules="none"><colgroup><col class="label"><col></colgroup><tbody valign="top"><tr><td class="label"><a class="fn-backref" href="#id4">[1]</a></td><td><a class="reference external" href="https://pypy.org/compat.html">https://pypy.org/compat.html</a></td></tr></tbody></table>

<table class="docutils footnote" frame="void" id="jython-ver" rules="none"><colgroup><col class="label"><col></colgroup><tbody valign="top"><tr><td class="label"><a class="fn-backref" href="#id6">[2]</a></td><td><a class="reference external" href="https://hg.python.org/jython/file/412a8f9445f7/NEWS">https://hg.python.org/jython/file/412a8f9445f7/NEWS</a></td></tr></tbody></table>

<table class="docutils footnote" frame="void" id="iron-ver" rules="none"><colgroup><col class="label"><col></colgroup><tbody valign="top"><tr><td class="label"><a class="fn-backref" href="#id8">[3]</a></td><td><a class="reference external" href="https://ironpython.net/download/">https://ironpython.net/download/</a></td></tr></tbody></table>

<table class="docutils footnote" frame="void" id="iron-ver3" rules="none"><colgroup><col class="label"><col></colgroup><tbody valign="top"><tr><td class="label"><a class="fn-backref" href="#id9">[4]</a></td><td><a class="reference external" href="https://github.com/IronLanguages/ironpython3">https://github.com/IronLanguages/ironpython3</a></td></tr></tbody></table>

<table class="docutils footnote" frame="void" id="pythonnet-ver1" rules="none"><colgroup><col class="label"><col></colgroup><tbody valign="top"><tr><td class="label"><a class="fn-backref" href="#id10">[5]</a></td><td><a class="reference external" href="https://pythonnet.github.io/">https://pythonnet.github.io/</a></td></tr></tbody></table>

<table class="docutils footnote" frame="void" id="pep373-eol" rules="none"><colgroup><col class="label"><col></colgroup><tbody valign="top"><tr><td class="label"><a class="fn-backref" href="#id1">[6]</a></td><td><a class="reference external" href="https://www.python.org/dev/peps/pep-0373/#id2">https://www.python.org/dev/peps/pep-0373/#id2</a></td></tr></tbody></table>