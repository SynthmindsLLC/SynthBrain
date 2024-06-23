[![](https://img.realpython.net/8899c4a6d15334a6b9f769e9f8bc0cf7)](https://srv.realpython.net/click/41686012779/?c=7309556696&p=29182759436&r=31329)

Installing Python 2 on Linux[¶](#installing-python-2-on-linux "Permalink to this headline")
===========================================================================================

![https://d33wubrfki0l68.cloudfront.net/9748b28c2d79f1ff9c0643ef0287be932af27dae/b601a/_images/34435688560_4cc2a7bcbb_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/9748b28c2d79f1ff9c0643ef0287be932af27dae/b601a/_images/34435688560_4cc2a7bcbb_k_d.jpg)

Note

Check out our [guide for installing Python 3 on Linux](../../install3/linux/#install3-linux).

The latest versions of CentOS, Red Hat Enterprise Linux (RHEL) and Ubuntu **come with Python 2.7 out of the box**.

To see which version of Python you have installed, open a command prompt and run

$ python2 --version

However, with the growing popularity of Python 3, some distributions, such as Fedora, don’t come with Python 2 pre-installed. You can install the `python2` package with your distribution package manager:

$ sudo dnf install python2

You do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Setuptools and pip, as it makes it much easier for you to use other third-party Python libraries.

Setuptools & Pip[¶](#setuptools-pip "Permalink to this headline")
-----------------------------------------------------------------

The two most crucial third-party Python packages are [setuptools](https://pypi.org/project/setuptools) and [pip](https://pip.pypa.io/en/stable/).

Once installed, you can download, install and uninstall any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.

Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default.

To see if pip is installed, open a command prompt and run

$ command -v pip

To install pip, [follow the official pip installation guide](https://pip.pypa.io/en/latest/installing/) - this will automatically install the latest version of setuptools.

Virtual Environments[¶](#virtual-environments "Permalink to this headline")
---------------------------------------------------------------------------

A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also maintaining a project which requires Django 1.8.

To start using this and see more information: [Virtual Environments](../../../dev/virtualenvs/#virtualenvironments-ref) docs.

You can also use [virtualenvwrapper](../../../dev/virtualenvs/#virtualenvwrapper-ref) to make it easier to manage your virtual environments.

* * *

This page is a remixed version of [another guide](https://www.stuartellis.name/articles/python-development-windows/), which is available under the same license.