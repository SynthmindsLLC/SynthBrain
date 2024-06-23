*   [Repository](https://github.com/py-pkgs/py-pkgs)
*   [Open issue](https://github.com/py-pkgs/py-pkgs/issues/new?title=Issue%20on%20page%20%2F01-introduction.html&body=Your%20issue%20content%20here.)

*   [.ipynb](_sources/01-introduction.ipynb)
*   .pdf

document.write(\` <button class="btn btn-sm navbar-btn theme-switch-button" title="light/dark" aria-label="light/dark" data-bs-placement="bottom" data-bs-toggle="tooltip"> <span class="theme-switch nav-link" data-mode="light"><i class="fa-solid fa-sun fa-lg"></i></span> <span class="theme-switch nav-link" data-mode="dark"><i class="fa-solid fa-moon fa-lg"></i></span> <span class="theme-switch nav-link" data-mode="auto"><i class="fa-solid fa-circle-half-stroke fa-lg"></i></span> </button> \`) document.write(\` <button class="btn btn-sm navbar-btn search-button search-button\_\_button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip"> <i class="fa-solid fa-magnifying-glass fa-lg"></i> </button> \`)

Introduction
============

Contents
--------

*   [1.1. Why you should create packages](#why-you-should-create-packages)

1\. Introduction[#](#introduction "Permalink to this heading")
==============================================================

* * *

Python packages are a core element of the Python programming language and are how you write reusable and shareable code in Python. This book assumes that readers are familiar with how to install a package using a package installer like `pip` or `conda`, and how to import and use it with the help of the `import` statement in Python.

For example, the command below uses `pip` to install `numpy`[5](/09-bibliography#id3 "Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke, and Travis E. Oliphant. Array programming with NumPy. Nature, 585(7825):357–362, September 2020. URL: https://doi.org/10.1038/s41586-020-2649-2."), the core scientific computing package for Python:

span.prompt1:before{content:"\\$ "}$ pip install numpy

Copy to clipboard

Once the package is installed, it can be used in a Python interpreter. For example, to round pi to three decimal places:

$ python

Copy to clipboard

span.prompt2:before{content:">>> "}import numpy as np
np.round(np.pi, decimals\=3)

Copy to clipboard

3.142

Copy to clipboard

At a minimum, a package bundles together code (such as functions, classes, variables, or scripts) so that it can be easily reused across different projects. However, packages are typically also supported by extra content such as documentation and tests, which become exponentially more important if you wish to share your package with others.

As of January 2022, there are over 350,000 packages available on the [Python Package Index (PyPI)](https://pypi.org), the official online software repository for Python. Packages are a key reason why Python is such a powerful and widely used programming language. The chances are that someone has already solved a problem that you’re working on, and you can benefit from their work by downloading and installing their package. Put simply, packages are how you make it as easy as possible to use, maintain, share, and collaborate on Python code with others, whether they be your friends, work colleagues, the world, or your future self!

Even if you never intend to share your code with others, making packages will ultimately save you time. Packages make it significantly easier for you to reuse and maintain your code within a project and across different projects. After programming for some time, most people will eventually reach a point where they want to reuse code from one project in another. For beginners, in particular, this is something often accomplished by copying-and-pasting existing code into the new project. Despite being inefficient, this practice also makes it difficult to improve and maintain your code across projects. Creating a simple Python package will solve these problems.

Regardless of your motivation, the goal of this book is to show you how to easily develop Python packages. The focus is overwhelmingly practical — we will leverage modern methods and tools to develop and maintain packages efficiently, reproducibly, and with as much automation as possible, so you can focus on writing and sharing code. Along the way, we’ll also enlighten some interesting and relevant lower-level details of Python packaging and the Python programming language.

1.1. Why you should create packages[#](#why-you-should-create-packages "Permalink to this heading")
---------------------------------------------------------------------------------------------------

There are many reasons why you should develop Python packages!

*   To effectively share your code with others.
    
*   They save you time. Even if you don’t intend to share your package with others, they help you easily reuse and maintain your code across multiple projects.
    
*   They force you to organize and document your code, such that it can be easily understood and used at a later time.
    
*   They isolate dependencies for your code and improve its reproducibility.
    
*   They are a good way to practice writing good code.
    
*   Packages can be used to effectively bundle up reproducible data analysis and programming projects.
    
*   Finally, developing and distributing packages supports the Python ecosystem and other Python users who can benefit from your work.
    

{ requestKernel: true, binderOptions: { repo: "binder-examples/jupyter-stacks-datascience", ref: "master", }, codeMirrorConfig: { theme: "abcdef", mode: "python" }, kernelOptions: { name: "python3", path: "./." }, predefinedOutput: true } kernelName="python3"

[

previous

About the authors



](/00-authors "previous page")[

next

2\. System setup

](/02-setup "next page")

Contents

*   [1.1. Why you should create packages](#why-you-should-create-packages)

By Tomas Beuzen & Tiffany Timbers

© Copyright 2023. CC BY-NC-SA 4.0.