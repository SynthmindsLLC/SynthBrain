[![](https://img.realpython.net/6fe6464c8bf6ec2cbcf3f1f0e778156b)](https://srv.realpython.net/click/57356986228/?c=41067926597&p=29182759436&r=94900)

Installing Python 2 on Windows[¶](#installing-python-2-on-windows "Permalink to this headline")
===============================================================================================

![https://d33wubrfki0l68.cloudfront.net/9748b28c2d79f1ff9c0643ef0287be932af27dae/b601a/_images/34435688560_4cc2a7bcbb_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/9748b28c2d79f1ff9c0643ef0287be932af27dae/b601a/_images/34435688560_4cc2a7bcbb_k_d.jpg)

Note

Check out our [guide for installing Python 3 on Windows](../../install3/win/#install3-windows).

First, download the [latest version](https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi) of Python 2.7 from the official website. If you want to be sure you are installing a fully up-to-date version, click the Downloads > Windows link from the home page of the [Python.org web site](https://python.org) .

The Windows version is provided as an MSI package. To install it manually, just double-click the file. The MSI package format allows Windows administrators to automate installation with their standard tools.

By design, Python installs to a directory with the version number embedded, e.g. Python version 2.7 will install at `C:\Python27\`, so that you can have multiple versions of Python on the same system without conflicts. Of course, only one interpreter can be the default application for Python file types. It also does not automatically modify the `PATH` environment variable, so that you always have control over which copy of Python is run.

Typing the full path name for a Python interpreter each time quickly gets tedious, so add the directories for your default Python version to the `PATH`. Assuming that your Python installation is in `C:\Python27\`, add this to your `PATH`:

C:\\Python27\\;C:\\Python27\\Scripts\\

You can do this easily by running the following in `powershell`:

\[Environment\]::SetEnvironmentVariable("Path", "$env:Path;C:\\Python27\\;C:\\Python27\\Scripts\\", "User")

This is also an option during the installation process.

The second (`Scripts`) directory receives command files when certain packages are installed, so it is a very useful addition. You do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Setuptools, as it makes it much easier for you to use other third-party Python libraries.

Setuptools + Pip[¶](#setuptools-pip "Permalink to this headline")
-----------------------------------------------------------------

The two most crucial third-party Python packages are [setuptools](https://pypi.org/project/setuptools) and [pip](https://pip.pypa.io/en/stable/).

Once installed, you can download, install and uninstall any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.

Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default.

To see if pip is installed, open a command prompt and run

command -v pip

To install pip, [follow the official pip installation guide](https://pip.pypa.io/en/latest/installing/) - this will automatically install the latest version of setuptools.

Virtual Environments[¶](#virtual-environments "Permalink to this headline")
---------------------------------------------------------------------------

A Virtual Environment is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also maintaining a project which requires Django 1.8.

To start using this and see more information: [Virtual Environments](../../../dev/virtualenvs/#virtualenvironments-ref) docs.

* * *

This page is a remixed version of [another guide](https://www.stuartellis.name/articles/python-development-windows/), which is available under the same license.