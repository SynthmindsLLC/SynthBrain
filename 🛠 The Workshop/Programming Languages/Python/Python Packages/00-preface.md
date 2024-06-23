*   [Repository](https://github.com/py-pkgs/py-pkgs)
*   [Open issue](https://github.com/py-pkgs/py-pkgs/issues/new?title=Issue%20on%20page%20%2F00-preface.html&body=Your%20issue%20content%20here.)

*   [.ipynb](_sources/00-preface.ipynb)
*   .pdf

document.write(\` <button class="btn btn-sm navbar-btn theme-switch-button" title="light/dark" aria-label="light/dark" data-bs-placement="bottom" data-bs-toggle="tooltip"> <span class="theme-switch nav-link" data-mode="light"><i class="fa-solid fa-sun fa-lg"></i></span> <span class="theme-switch nav-link" data-mode="dark"><i class="fa-solid fa-moon fa-lg"></i></span> <span class="theme-switch nav-link" data-mode="auto"><i class="fa-solid fa-circle-half-stroke fa-lg"></i></span> </button> \`) document.write(\` <button class="btn btn-sm navbar-btn search-button search-button\_\_button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip"> <i class="fa-solid fa-magnifying-glass fa-lg"></i> </button> \`)

Preface
=======

Contents
--------

*   [Why read this book?](#why-read-this-book)
*   [Structure of the book](#structure-of-the-book)
*   [Assumptions](#assumptions)
*   [Conventions](#conventions)
*   [Persistence](#persistence)
*   [Colophon](#colophon)
*   [Acknowledgments](#acknowledgments)

Preface[#](#preface "Permalink to this heading")
================================================

* * *

Python packages are the fundamental units of shareable code in Python. Packages make it easy to organize, reuse, and maintain your code, as well as share it between projects, with your colleagues, and with the wider Python community. _Python Packages_ is an open-source book that describes modern and efficient workflows for creating Python packages. The focus of this book is overwhelmingly practical; we will demonstrate methods and tools you can use to develop and maintain packages quickly, reproducibly, and with as much automation as possible — so you can focus on writing and sharing code!

Why read this book?[#](#why-read-this-book "Permalink to this heading")
-----------------------------------------------------------------------

Despite their importance, packages can be difficult to understand and cumbersome to create for beginners and seasoned developers alike. This book aims to describe the packaging process at an accessible and practical level for data scientists, developers, and programmers. Along the way, we’ll develop a real Python package and will explore all the key elements of Python packaging, including: creating a package file and directory structure, when and why to write tests and documentation, and how to maintain and update your package with the help of automated continuous integration and continuous deployment (CI/CD) pipelines.

By reading this book, you will:

*   Understand what Python packages are, and when and why you should use them.
    
*   Be able to build your own Python package from scratch.
    
*   Learn how to document your Python code and packages.
    
*   Write software tests for your code and automate them.
    
*   Learn how to release your package on the Python Package Index (PyPI) and discover best practices for updating and versioning your code.
    
*   Implement CI/CD workflows to build, test, and deploy your package automatically.
    
*   Get tips on Python coding style, best-practice packaging workflows, and other useful development tools.
    

Structure of the book[#](#structure-of-the-book "Permalink to this heading")
----------------------------------------------------------------------------

**Chapter 1: [Introduction](/01-introduction#introduction)** first gives a brief introduction to packages in Python and why you should know how to make them.

**Chapter 2: [System setup](/02-setup#system-setup)** describes how to set up your development environment to develop packages and follow the examples in this book.

In **Chapter 3: [How to package a Python](/03-how-to-package-a-python#how-to-package-a-python)**, we develop an example package from beginning-to-end as a practical demonstration of the key steps involved in the packaging process. This chapter forms the foundation of the book and will act as a reference sheet for readers creating packages in the future.

The remaining chapters then go into more detail about each step in this process, organized roughly in their order in the workflow:

*   **Chapter 4: [Package structure and distribution](/04-package-structure#package-structure-and-distribution)**
    
*   **Chapter 5: [Testing](/05-testing#testing)**
    
*   **Chapter 6: [Documentation](/06-documentation#documentation)**
    
*   **Chapter 7: [Releasing and versioning](/07-releasing-versioning#releasing-and-versioning)**
    
*   **Chapter 8: [Continuous integration and deployment](/08-ci-cd#continuous-integration-and-deployment)**
    

Assumptions[#](#assumptions "Permalink to this heading")
--------------------------------------------------------

While this book aims to introduce Python packaging at a beginner level, we assume readers have basic familiarity with the concepts listed in [Table 1](#assumptions-table):

Table 1 Concepts this book assumes readers have basic familiarity with.[#](#assumptions-table "Permalink to this table")
| 
Item

 | 

Learning resources

 |
| --- | --- |
| 

How to import Python packages with the `import` statement

 | 

Python documentation

 |
| 

How to write conditionals (`if`/`elif`/`else`) and loops (`for`)

 | 

Python documentation

 |
| 

How to use and write Python functions

 | 

_Plotting and Programming in Python: Writing Functions_ [1](/09-bibliography#id6 "The Carpentries. Plotting and programming in Python: writing functions. https://swcarpentry.github.io/python-novice-gapminder/16-writing-functions/index.html, 2021. URL: https://swcarpentry.github.io/python-novice-gapminder/16-writing-functions/index.html.")

 |
| 

(Optional) Basic familiarity with version control and Git and GitHub (or similar tools)

 | 

_Happy Git and GitHub for the useR_ [2](/09-bibliography#id5 "Jenny Bryan, Jim Hester, and STAT545 Teaching Assistants. Happy git and GitHub for the user. https://happygitwithr.com/, 2021. URL: https://happygitwithr.com/.") or _Research Software Engineering with Python_ [3](/09-bibliography#id7 "Damien Irving, Kate Hertweck, Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson. Research Software Engineering with Python. Chapman and Hall/CRC, 2021.")

 |

Conventions[#](#conventions "Permalink to this heading")
--------------------------------------------------------

Throughout this book we use `foo()` to refer to functions, `bar` for inline commands/variables/function parameters/package names, and _`__init__.py`_ and _`src/`_ to refer to files and directories respectively.

Commands entered at the command line appear as below, with $ indicating the command prompt:

span.prompt1:before{content:"\\$ "}$ mkdir my-first-package
$ cd my-first-package
$ python

Copy to clipboard

Code entered in a Python interpreter looks like this:

span.prompt2:before{content:">>> "}import math
round(math.pi, 3)

Copy to clipboard

3.142

Copy to clipboard

Code blocks appear as below:

def is\_even(n):
    """Check if n is even."""
    if n % 2 \== 0:
        return True
    else:
        return False

Copy to clipboard

If you are reading an electronic version of the book, e.g., [https://py-pkgs.org](https://py-pkgs.org), all code is rendered so that you can easily copy and paste directly from your browser to your Python interpreter or editor.

Persistence[#](#persistence "Permalink to this heading")
--------------------------------------------------------

The Python software ecosystem is constantly evolving. While we aim to make the packaging workflows and concepts discussed in this book tool-agnostic, the tools we do use in the book may have been updated by the time you read it. If the maintainers of these tools are doing the right thing by documenting, versioning, and properly deprecating their code (we’ll explore these concepts ourselves in **Chapter 7: [Releasing and versioning](/07-releasing-versioning#releasing-and-versioning)**), then it should be straightforward to adapt any outdated code in the book.

Colophon[#](#colophon "Permalink to this heading")
--------------------------------------------------

This book was written in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) and compiled using [Jupyter Book](https://jupyterbook.org/intro.html). The source is hosted on [GitHub](https://github.com/UBC-MDS/py-pkgs) and is deployed online at [https://py-pkgs.org](https://py-pkgs.org) with [Netlify](https://www.netlify.com/).

Acknowledgments[#](#acknowledgments "Permalink to this heading")
----------------------------------------------------------------

We’d like to thank everyone that has contributed to the development of _Python Packages_. This is an open source book that began as supplementary material for the University of British Columbia’s Master of Data Science program and was subsequently developed openly on GitHub where it has been read, revised, and supported by many students, educators, practitioners and hobbyists. Without you all, this book wouldn’t be nearly as good as it is, and we are deeply grateful. A special thanks to those who have contributed to or provided feedback on the text via GitHub (in alphabetical order of GitHub username): `bendichter`, `benjy765`, `Carreau`, `chendaniely`, `dcslagel`, `eliasdabbas`, `fegue`, `firasm`, `Kaszanas`, `Midnighter`, `mtkerbeR`, `NickleDave`, `SamEdwardes`, `tarensanders`, `wirthual`.

The scope and intent of this book was inspired by the fantastic [_R Packages_](https://r-pkgs.org) [4](/09-bibliography#id10 "Hadley Wickham and Jenny Bryan. R Packages. O\") book written by Hadley Wickham and Jenny Bryan, a book that has been a significant resource for the R community over the years. We hope that _Python Packages_ will eventually play a similar role in the Python community.

{ requestKernel: true, binderOptions: { repo: "binder-examples/jupyter-stacks-datascience", ref: "master", }, codeMirrorConfig: { theme: "abcdef", mode: "python" }, kernelOptions: { name: "python3", path: "./." }, predefinedOutput: true } kernelName="python3"

[

previous

Welcome to Python Packages!



](/welcome "previous page")[

next

About the authors

](/00-authors "next page")

Contents

*   [Why read this book?](#why-read-this-book)
*   [Structure of the book](#structure-of-the-book)
*   [Assumptions](#assumptions)
*   [Conventions](#conventions)
*   [Persistence](#persistence)
*   [Colophon](#colophon)
*   [Acknowledgments](#acknowledgments)

By Tomas Beuzen & Tiffany Timbers

© Copyright 2023. CC BY-NC-SA 4.0.