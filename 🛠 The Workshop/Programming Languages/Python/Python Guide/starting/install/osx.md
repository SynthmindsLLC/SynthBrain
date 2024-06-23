[![](https://img.realpython.net/1c3e33fa8ce0d82a964b7f7de310e4bb)](https://srv.realpython.net/click/21871400699/?c=41831496980&p=29182759436&r=14486)

Installing Python 2 on Mac OS X[¶](#installing-python-2-on-mac-os-x "Permalink to this headline")
=================================================================================================

![https://d33wubrfki0l68.cloudfront.net/9748b28c2d79f1ff9c0643ef0287be932af27dae/b601a/_images/34435688560_4cc2a7bcbb_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/9748b28c2d79f1ff9c0643ef0287be932af27dae/b601a/_images/34435688560_4cc2a7bcbb_k_d.jpg)

Note

Check out our [guide for installing Python 3 on OS X](../../install3/osx/#install3-osx).

**Mac OS X comes with Python 2.7 out of the box between versions 10.8 and 12.3.**

If your Mac OS X version is between the above versions, you do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Setuptools, as it makes it much easier for you to install and manage other third-party Python libraries.

The version of Python that ships with OS X is great for learning, but it’s not good for development. The version shipped with OS X may be out of date from the [official current Python release](https://www.python.org/downloads/mac-osx/), which is considered the stable production version.

Doing it Right[¶](#doing-it-right "Permalink to this headline")
---------------------------------------------------------------

Let’s install a real version of Python.

Before installing Python, you’ll need to install a C compiler. The fastest way is to install the Xcode Command Line Tools by running `xcode-select --install`. You can also download the full version of [Xcode](https://developer.apple.com/xcode/) from the Mac App Store, or the minimal but unofficial [OSX-GCC-Installer](https://github.com/kennethreitz/osx-gcc-installer#readme) package.

Note

If you already have Xcode installed, do not install OSX-GCC-Installer. In combination, the software can cause issues that are difficult to diagnose.

Note

If you perform a fresh install of Xcode, you will also need to add the commandline tools by running `xcode-select --install` on the terminal.

While OS X comes with a large number of Unix utilities, those familiar with Linux systems will notice one key component missing: a decent package manager. [Homebrew](https://brew.sh) fills this void.

To [install Homebrew](https://brew.sh/#install), open `Terminal` or your favorite OS X terminal emulator and run

$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

The script will explain what changes it will make and prompt you before the installation begins. Once you’ve installed Homebrew, insert the Homebrew directory at the top of your `PATH` environment variable. You can do this by adding the following line at the bottom of your `~/.profile` file

export PATH="/usr/local/bin:/usr/local/sbin:$PATH"

Now, we can install Python 2.7:

$ brew install python@2

Because `python@2` is a “keg”, we need to update our `PATH` again, to point at our new installation:

export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"

Homebrew names the executable `python2` so that you can still run the system Python via the executable `python`.

$ python -V   \# Homebrew installed Python 3 interpreter (if installed)
$ python2 -V  \# Homebrew installed Python 2 interpreter
$ python3 -V  \# Homebrew installed Python 3 interpreter (if installed)

Setuptools & Pip[¶](#setuptools-pip "Permalink to this headline")
-----------------------------------------------------------------

Homebrew installs Setuptools and `pip` for you.

Setuptools enables you to download and install any compliant Python software over a network (usually the Internet) with a single command (`easy_install`). It also enables you to add this network installation capability to your own Python software with very little work.

`pip` is a tool for easily installing and managing Python packages, that is recommended over `easy_install`. It is superior to `easy_install` in [several ways](https://python-packaging-user-guide.readthedocs.io/pip_easy_install/#pip-vs-easy-install), and is actively maintained.

$ pip2 -V  \# pip pointing to the Homebrew installed Python 2 interpreter
$ pip -V  \# pip pointing to the Homebrew installed Python 3 interpreter (if installed)

Virtual Environments[¶](#virtual-environments "Permalink to this headline")
---------------------------------------------------------------------------

A Virtual Environment (commonly referred to as a ‘virtualenv’) is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also maintaining a project which requires Django 1.8.

To start using this and see more information: [Virtual Environments](../../../dev/virtualenvs/#virtualenvironments-ref) docs.

* * *

This page is a remixed version of [another guide](https://www.stuartellis.name/articles/python-development-windows/), which is available under the same license.