[![](https://img.realpython.net/6fe6464c8bf6ec2cbcf3f1f0e778156b)](https://srv.realpython.net/click/57356986228/?c=41067926597&p=29182759436&r=20555)

Installing Python 3 on Windows[¶](#installing-python-3-on-windows "Permalink to this headline")
===============================================================================================

![https://d33wubrfki0l68.cloudfront.net/02962eb19c0069740d16e67b5ba7c613238c8b9a/30ed2/_images/34435689480_2e6f358510_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/02962eb19c0069740d16e67b5ba7c613238c8b9a/30ed2/_images/34435689480_2e6f358510_k_d.jpg)

First, follow the installation instructions for [Chocolatey](https://chocolatey.org/install). It’s a community system packager manager for Windows 7+. (It’s very much like Homebrew on OS X.)

Once done, installing Python 3 is very simple, because Chocolatey pushes Python 3 as the default.

choco install python

Once you’ve run this command, you should be able to launch Python directly from to the console. (Chocolatey is fantastic and automatically adds Python to your path.)

Setuptools + Pip[¶](#setuptools-pip "Permalink to this headline")
-----------------------------------------------------------------

The two most crucial third-party Python packages are [setuptools](https://pypi.org/project/setuptools) and [pip](https://pip.pypa.io/en/stable/), which let you download, install and uninstall any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.

All supported versions of Python 3 include pip, so just make sure it’s up to date:

python -m pip install -U pip

Pipenv & Virtual Environments[¶](#pipenv-virtual-environments "Permalink to this headline")
-------------------------------------------------------------------------------------------

The next step is to install Pipenv, so you can install dependencies and manage virtual environments.

A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 2.0 while also maintaining a project which requires Django 1.8.

So, onward! To the [Pipenv & Virtual Environments](../../../dev/virtualenvs/#virtualenvironments-ref) docs!

* * *

This page is a remixed version of [another guide](https://www.stuartellis.name/articles/python-development-windows/), which is available under the same license.