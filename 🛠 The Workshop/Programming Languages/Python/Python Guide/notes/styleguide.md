[![](https://img.realpython.net/6fe6464c8bf6ec2cbcf3f1f0e778156b)](https://srv.realpython.net/click/57356986228/?c=41067926597&p=29182759436&r=69798)

The Guide Style Guide[¶](#the-guide-style-guide "Permalink to this headline")
=============================================================================

![https://d33wubrfki0l68.cloudfront.net/a7189f408d8a30ded6f6203120a926ed5d088478/4a254/_images/33573755856_7f43d43adf_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/a7189f408d8a30ded6f6203120a926ed5d088478/4a254/_images/33573755856_7f43d43adf_k_d.jpg)

As with all documentation, having a consistent format helps make the document more understandable. In order to make The Guide easier to digest, all contributions should fit within the rules of this style guide where appropriate.

The Guide is written as [reStructuredText](../../writing/documentation/#restructuredtext-ref).

Note

Parts of The Guide may not yet match this style guide. Feel free to update those parts to be in sync with The Guide Style Guide

Note

On any page of the rendered HTML you can click “Show Source” to see how authors have styled the page.

Relevancy[¶](#relevancy "Permalink to this headline")
-----------------------------------------------------

Strive to keep any contributions relevant to the [purpose of The Guide](../../intro/duction/#about-ref).

*   Avoid including too much information on subjects that don’t directly relate to Python development.
*   Prefer to link to other sources if the information is already out there. Be sure to describe what and why you are linking.
*   [Cite](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#citations) references where needed.
*   If a subject isn’t directly relevant to Python, but useful in conjunction with Python (e.g., Git, GitHub, Databases), reference by linking to useful resources, and describe why it’s useful to Python.
*   When in doubt, ask.

Headings[¶](#headings "Permalink to this headline")
---------------------------------------------------

Use the following styles for headings.

Chapter title:

#########
Chapter 1
#########

Page title:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Time is an Illusion
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Section headings:

Lunchtime Doubly So
\===================

Sub section headings:

Very Deep
\---------

Prose[¶](#prose "Permalink to this headline")
---------------------------------------------

Wrap text lines at 78 characters. Where necessary, lines may exceed 78 characters, especially if wrapping would make the source text more difficult to read.

Use Standard American English, not British English.

Use of the [serial comma](https://en.wikipedia.org/wiki/Serial_comma) (also known as the Oxford comma) is 100% non-optional. Any attempt to submit content with a missing serial comma will result in permanent banishment from this project, due to complete and total lack of taste.

Banishment? Is this a joke? Hopefully we will never have to find out.

Code Examples[¶](#code-examples "Permalink to this headline")
-------------------------------------------------------------

Wrap all code examples at 70 characters to avoid horizontal scrollbars.

Command line examples:

.. code-block:: console

    $ run command --help
    $ ls ..

Be sure to include the `$` prefix before each line for Unix console examples.

For Windows console examples, use `doscon` or `powershell` instead of `console`, and omit the `$` prefix.

Python interpreter examples:

Label the example::

.. code-block:: python

    >>> import this

Python examples:

Descriptive title::

.. code-block:: python

    def get\_answer():
        return 42

Externally Linking[¶](#externally-linking "Permalink to this headline")
-----------------------------------------------------------------------

*   Prefer labels for well known subjects (e.g. proper nouns) when linking:
    
    Sphinx\_ is used to document Python.
    
    .. \_Sphinx: https://www.sphinx-doc.org
    
*   Prefer to use descriptive labels with inline links instead of leaving bare links:
    
    Read the \`Sphinx Tutorial <https://www.sphinx-doc.org/en/master/usage/quickstart.html>\`\_
    
*   Avoid using labels such as “click here”, “this”, etc., preferring descriptive labels (SEO worthy) instead.
    

Linking to Sections in The Guide[¶](#linking-to-sections-in-the-guide "Permalink to this headline")
---------------------------------------------------------------------------------------------------

To cross-reference other parts of this documentation, use the [:ref:](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-ref) keyword and labels.

To make reference labels more clear and unique, always add a `-ref` suffix:

.. \_some-section-ref:

Some Section
\------------

Notes and Warnings[¶](#notes-and-warnings "Permalink to this headline")
-----------------------------------------------------------------------

Make use of the appropriate [admonitions directives](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#directives) when making notes.

Notes:

.. note::
    The Hitchhiker’s Guide to the Galaxy has a few things to say
    on the subject of towels. A towel, it says, is about the most
    massively useful thing an interstellar hitch hiker can have.

Warnings:

.. warning:: DON'T PANIC

TODOs[¶](#todos "Permalink to this headline")
---------------------------------------------

Please mark any incomplete areas of The Guide with a [todo directive](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html). To avoid cluttering the [Todo List](../contribute/#todo-list-ref), use a single `todo` for stub documents or large incomplete sections.

.. todo::
    Learn the Ultimate Answer to the Ultimate Question
    of Life, The Universe, and Everything