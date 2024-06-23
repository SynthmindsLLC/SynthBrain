*   [Repository](https://github.com/py-pkgs/py-pkgs)
*   [Open issue](https://github.com/py-pkgs/py-pkgs/issues/new?title=Issue%20on%20page%20%2F02-setup.html&body=Your%20issue%20content%20here.)

*   [.ipynb](_sources/02-setup.ipynb)
*   .pdf

document.write(\` <button class="btn btn-sm navbar-btn theme-switch-button" title="light/dark" aria-label="light/dark" data-bs-placement="bottom" data-bs-toggle="tooltip"> <span class="theme-switch nav-link" data-mode="light"><i class="fa-solid fa-sun fa-lg"></i></span> <span class="theme-switch nav-link" data-mode="dark"><i class="fa-solid fa-moon fa-lg"></i></span> <span class="theme-switch nav-link" data-mode="auto"><i class="fa-solid fa-circle-half-stroke fa-lg"></i></span> </button> \`) document.write(\` <button class="btn btn-sm navbar-btn search-button search-button\_\_button" title="Search" aria-label="Search" data-bs-placement="bottom" data-bs-toggle="tooltip"> <i class="fa-solid fa-magnifying-glass fa-lg"></i> </button> \`)

System setup
============

Contents
--------

*   [2.1. The command-line interface](#the-command-line-interface)
*   [2.2. Installing software](#installing-software)
    *   [2.2.1. Installing Python](#installing-python)
    *   [2.2.2. Install packaging software](#install-packaging-software)
*   [2.3. Register for a PyPI account and get an authentication token](#register-for-a-pypi-account-and-get-an-authentication-token)
*   [2.4. Set up Git and GitHub](#set-up-git-and-github)
*   [2.5. Python integrated development environments](#python-integrated-development-environments)
    *   [2.5.1. Visual Studio Code](#visual-studio-code)
    *   [2.5.2. JupyterLab](#jupyterlab)
    *   [2.5.3. RStudio](#rstudio)
*   [2.6. Developing with Docker](#developing-with-docker)
    *   [2.6.1. Docker with Visual Studio Code](#docker-with-visual-studio-code)
    *   [2.6.2. Docker with JupyterLab](#docker-with-jupyterlab)

2\. System setup[#](#system-setup "Permalink to this heading")
==============================================================

* * *

If you intend to follow along with the code presented in this book, we recommend you follow these setup instructions so that you will run into fewer technical issues.

2.1. The command-line interface[#](#the-command-line-interface "Permalink to this heading")
-------------------------------------------------------------------------------------------

A command-line interface (CLI) is a text-based interface used to interact with your computer. We’ll be using a CLI for various tasks throughout this book. We’ll assume Mac and Linux users are using the “Terminal” and Windows users are using the “Anaconda Prompt” (which we’ll install in the next section) as a CLI.

2.2. Installing software[#](#installing-software "Permalink to this heading")
-----------------------------------------------------------------------------

**[Section 2.2.1](#installing-python)** and **[Section 2.2.2](#install-packaging-software)** describe how to install the software you’ll need to develop a Python package and follow along with the text and examples in this book. However, we also support an alternative setup with Docker that has everything you need already installed to get started. The Docker approach is recommended for anyone that runs into issues installing or using any of the software below on their specific operating system, or anyone who would simply prefer to use Docker — if that’s you, skip to **[Section 2.3](#register-for-a-pypi-account)** for now, and we’ll describe the Docker setup later in **[Section 2.6](#developing-with-docker)**.

### 2.2.1. Installing Python[#](#installing-python "Permalink to this heading")

We recommend installing the latest version of Python via the Miniconda distribution by following the instructions in the Miniconda [documentation](https://docs.conda.io/en/latest/miniconda.html). Miniconda is a lightweight version of the popular Anaconda distribution. If you have previously installed the Anaconda or Miniconda distribution feel free to skip to **[Section 2.2.2](#install-packaging-software)**.

If you are unfamiliar with Miniconda and Anaconda, they are distributions of Python that also include the `conda` package and environment manager, and a number of other useful packages. The difference between Anaconda and Miniconda is that Anaconda installs over 250 additional packages (many of which you might never use), while Miniconda is a much smaller distribution that comes bundled with just a few key packages; you can then install additional packages as you need them using the command `conda install`.

`conda` is a piece of software that supports the process of installing and updating software (like Python packages). It is also an environment manager, which is the key function we’ll be using it for in this book. An environment manager helps you create “virtual environments” on your machine, where you can safely install different packages and their dependencies in an isolated location. Installing all the packages you need in the same place (i.e., the system default location) can be problematic because different packages often depend on different versions of the same dependencies; as you install more packages, you’ll inevitably get conflicts between dependencies, and your code will start to break. Virtual environments help you compartmentalize and isolate the packages you are using for different projects to avoid this issue. You can read more about virtual environments in the `conda` [documentation](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html). While alternative package and environment managers exist, we choose to use `conda` in this book because of its popularity, ease-of-use, and ability to handle any software stack (not just Python).

### 2.2.2. Install packaging software[#](#install-packaging-software "Permalink to this heading")

Once you’ve installed the Miniconda distribution, ensure that Python and `conda` are up to date by running the following command at the command line:

span.prompt1:before{content:"\\$ "}$ conda update \--all

Copy to clipboard

Now we’ll install the two main pieces of software we’ll be using to help us create Python packages in this book:

1.  [`poetry`](https://python-poetry.org/): software that will help us build our own Python packages. `poetry` is under active development, thus we recommend installing Poetry using their **official installer** while referring to their official [`poetry` documentation](https://python-poetry.org/docs/) for detailed installation instructions and support.
    
2.  [`cookiecutter`](https://github.com/cookiecutter/cookiecutter): software that will help us create packages from pre-made templates. It can be installed with `conda` as follows:
    
    $ conda install \-c conda-forge cookiecutter
    
    Copy to clipboard
    

2.3. Register for a PyPI account and get an authentication token[#](#register-for-a-pypi-account-and-get-an-authentication-token "Permalink to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------

The Python Package Index (PyPI) is the official online software repository for Python. A software repository is a storage location for downloadable software, like Python packages. In this book we’ll be publishing a package to PyPI. Before publishing packages to PyPI, it is typical to “test drive” their publication on TestPyPI, which is a test version of PyPI. To follow along with this book, you should register for a TestPyPI account on the [TestPyPI website](https://test.pypi.org/account/register/) and a PyPI account on the [PyPI website](https://pypi.org/account/register/).

Both TestPyPI and PyPI will require an authentication token for publishing your Python packages using Poetry. You should obtain one from each of these repositories and store them in a safe place, such as some password management software (e.g., [LastPass](https://www.lastpass.com/) or [1Password](https://1password.com/)). You can find the location of where to generate an authentication token by logging into the repository, and choosing “Account Settings” from the drop down menu under your username. Then scroll down to “API tokens” and click “Add API token”. You will then be prompted to give the token a name and to set its scope. For scope choose “Entire account (all projects)”.

2.4. Set up Git and GitHub[#](#set-up-git-and-github "Permalink to this heading")
---------------------------------------------------------------------------------

If you’re not using a version control system, we highly recommend you get into the habit! A version control system tracks changes to the file(s) of your project in a clear and organized way (no more “document\_1.doc”, “document\_1\_new.doc”, “document\_final.doc”, etc.). As a result, a version control system contains a full history of all the revisions made to your project, which you can view and retrieve at any time. You don’t _need_ to use or be familiar with version control to read this book, but if you’re serious about creating Python packages, version control will become an invaluable part of your workflow, so now is a good time to learn!

There are many version control systems available, but the most common is Git and we’ll be using it throughout this book. You can download Git by following the instructions in the [Git documentation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git helps track changes to a project on a local computer, but what if we want to collaborate with others? Or, what happens if your computer crashes and you lose all your work? That’s where GitHub comes in. GitHub is one of many online services for hosting Git-managed projects. GitHub helps you create an online copy of your local Git repository, which acts as a backup of your local work and allows others to easily and transparently collaborate on your project. You can sign up for a free GitHub account on the [GitHub website](https://www.github.com). Once signed up, you should also set up SSH authentication to help push and pull files from GitHub by following the steps in the official GitHub [documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

We assume that those who choose to follow the optional version control sections of this book have basic familiarity with Git and GitHub (or equivalent). Two excellent learning resources are [_Happy Git and GitHub for the useR_](https://happygitwithr.com)[2](/09-bibliography#id5 "Jenny Bryan, Jim Hester, and STAT545 Teaching Assistants. Happy git and GitHub for the user. https://happygitwithr.com/, 2021. URL: https://happygitwithr.com/.") and [_Research Software Engineering with Python_](https://merely-useful.tech/py-rse/git-cmdline.html)[3](/09-bibliography#id7 "Damien Irving, Kate Hertweck, Luke Johnston, Joel Ostblom, Charlotte Wickham, and Greg Wilson. Research Software Engineering with Python. Chapman and Hall/CRC, 2021.").

2.5. Python integrated development environments[#](#python-integrated-development-environments "Permalink to this heading")
---------------------------------------------------------------------------------------------------------------------------

A Python integrated development environment (IDE) will make the process of creating Python packages significantly easier. An IDE is a piece of software that provides advanced functionality for code development, such as directory and file creation and navigation, autocomplete, debugging, and syntax highlighting, to name a few. An IDE will save you time and help you write better code. Commonly used free Python IDEs include [Visual Studio Code](https://code.visualstudio.com/), [Atom](https://atom.io/), [Sublime Text](https://www.sublimetext.com/), [Spyder](https://www.spyder-ide.org/), and [PyCharm Community Edition](https://www.jetbrains.com/pycharm/). For those more familiar with the Jupyter ecosystem, [JupyterLab](https://jupyter.org/) is a suitable browser-based IDE. Finally, for the R community, the [RStudio IDE](https://rstudio.com/products/rstudio/download/) also supports Python.

You’ll be able to follow along with the examples presented in this book regardless of what IDE you choose to develop your Python code in. If you don’t know which IDE to use, we recommend starting with Visual Studio Code. Below we briefly describe how to set up Visual Studio Code, JupyterLab, and RStudio as Python IDEs (these are the IDEs we personally use in our day-to-day work). If you’d like to use Docker to help develop Python packages and follow along with this book, we’ll describe how to do so with Visual Studio Code or JupyterLab in **[Section 2.6](#developing-with-docker)**.

### 2.5.1. Visual Studio Code[#](#visual-studio-code "Permalink to this heading")

You can download Visual Studio Code (VS Code) from the Visual Studio Code [website](https://code.visualstudio.com/). Once you’ve installed VS Code, you should install the “Python” extension from the VS Code Marketplace. To do this, follow the steps listed below and illustrated in [Fig. 2.1](#vscode-1-fig):

1.  Open the Marketplace by clicking the _Extensions_ tab on the VS Code activity bar.
    
2.  Search for “Python” in the search bar.
    
3.  Select the extension named “Python” and then click _Install_.
    

[![Installing the Python extension in Visual Studio Code.](_images/02-vscode-1.png)](_images/02-vscode-1.png)

Fig. 2.1 Installing the Python extension in Visual Studio Code.[#](#vscode-1-fig "Permalink to this image")

Once this is done, you have everything you need to start creating packages! For example, you can create files and directories from the _File Explorer_ tab on the VS Code activity bar, and you can open up an integrated CLI by selecting _Terminal_ from the _View_ menu. [Fig. 2.2](#vscode-2-fig) shows an example of executing a Python _.py_ file from the command line in VS Code.

[![Executing a simple Python file called hello-world.py from the integrated terminal in Visual Studio Code.](_images/02-vscode-2.png)](_images/02-vscode-2.png)

Fig. 2.2 Executing a simple Python file called _[hello-world.py](http://hello-world.py)_ from the integrated terminal in Visual Studio Code.[#](#vscode-2-fig "Permalink to this image")

We recommend you take a look at the VS Code [Getting Started Guide](https://code.visualstudio.com/docs) to learn more about using VS Code. While you don’t need to install any additional extensions to start creating packages in VS Code, there are many extensions available that can support and streamline your programming workflows in VS Code. Below are a few we recommend installing to support the workflows we use in this book (you can search for and install these from the “Marketplace” as we did earlier):

*   [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring): an extension to quickly generate documentation strings (docstrings) for Python functions.
    
*   [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): an extension that provides keyboard shortcuts, automatic table of contents, and preview functionality for Markdown files. [Markdown](https://www.markdownguide.org) is a plain-text markup language that we’ll use and learn about in this book.
    

### 2.5.2. JupyterLab[#](#jupyterlab "Permalink to this heading")

For those comfortable in the Jupyter ecosystem feel free to stay there to create your Python packages! JupyterLab is a browser-based IDE that supports all of the core functionality we need to create packages. As per the JupyterLab [installation instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html), you can install JupyterLab with:

$ conda install \-c conda-forge jupyterlab

Copy to clipboard

Once installed, you can launch JupyterLab from your current directory by typing the following command in your terminal:

$ jupyter lab

Copy to clipboard

In JupyterLab, you can create files and directories from the _File Browser_ and can open up an integrated terminal from the _File_ menu. [Fig. 2.3](#jupyterlab-fig) shows an example of executing a Python _.py_ file from the command line in JupyterLab.

[![Executing a simple Python file called hello-world.py from a terminal in JupyterLab.](_images/02-jupyterlab.png)](_images/02-jupyterlab.png)

Fig. 2.3 Executing a simple Python file called _[hello-world.py](http://hello-world.py)_ from a terminal in JupyterLab.[#](#jupyterlab-fig "Permalink to this image")

We recommend you take a look at the JupyterLab [documentation](https://jupyterlab.readthedocs.io/en/stable/index.html) to learn more about how to use Jupyterlab. In particular, we’ll note that, like VS Code, JupyterLab supports an ecosystem of extensions that can add additional functionality to the IDE. We won’t install any here, but you can browse them in the JupyterLab _Extension Manager_ if you’re interested.

### 2.5.3. RStudio[#](#rstudio "Permalink to this heading")

Users with an R background may prefer to stay in the RStudio IDE. We recommend installing the most recent version of the IDE from the RStudio [website](https://rstudio.com/products/rstudio/download/preview/) (we recommend installing at least version ^1.4) and then installing the most recent version of R from [CRAN](https://cran.r-project.org/). To use Python in RStudio, you will need to install the [reticulate](https://rstudio.github.io/reticulate/) R package by typing the following in the R console inside RStudio:

install.packages("reticulate")

Copy to clipboard

When installing reticulate, you may be prompted to install the Anaconda distribution. We already installed the Miniconda distribution of Python in **[Section 2.2.1](#installing-python)**, so answer “no” to this prompt. Before being able to use Python in RStudio, you will need to configure `reticulate`. We will briefly describe how to do this for different operating systems below, but we encourage you to look at the `reticulate` [documentation](https://rstudio.github.io/reticulate/) for more help.

**Mac and Linux**

1.  Find the path to the Python interpreter installed with Miniconda by typing `which python` at the command line.
    
2.  Open (or create) an `.Rprofile` file in your HOME directory and add the line `Sys.setenv(RETICULATE_PYTHON = "path_to_python")`, where `"path_to_python"` is the path identified in step 1.
    
3.  Open (or create) a `.bash_profile` file in your HOME directory and add the line `export PATH="/opt/miniconda3/bin:$PATH"`, replacing `/opt/miniconda3/bin` with the path you identified in step 1 but without the `python` at the end.
    
4.  Restart R.
    
5.  Try using Python in RStudio by running the following in the R console:
    

library(reticulate)
repl\_python()

Copy to clipboard

**Windows**

1.  Find the path to the Python interpreter installed with Miniconda by opening an Anaconda Prompt from the Start Menu and typing `where python` in a terminal.
    
2.  Open (or create) an `.Rprofile` file in your HOME directory and add the line `Sys.setenv(RETICULATE_PYTHON = "path_to_python")`, where `"path_to_python"` is the path identified in step 1. Note that in Windows, you need `\\` instead of `\` to separate the directories; for example your path might look like: `C:\\Users\\miniconda3\\python.exe`.
    
3.  Open (or create) a `.bash_profile` file in your HOME directory and add the line `export PATH="/opt/miniconda3/bin:$PATH"`, replacing `/opt/miniconda3/bin` with the path you identified in step 1 but without the `python` at the end.
    
4.  Restart R.
    
5.  Try using Python in RStudio by running the following in the R console:
    

library(reticulate)
repl\_python()

Copy to clipboard

[Fig. 2.4](#rstudio-fig) shows an example of executing Python code interactively within the RStudio console.

[![Executing Python code in the RStudio.](_images/02-rstudio.png)](_images/02-rstudio.png)

Fig. 2.4 Executing Python code in RStudio.[#](#rstudio-fig "Permalink to this image")

2.6. Developing with Docker[#](#developing-with-docker "Permalink to this heading")
-----------------------------------------------------------------------------------

If you have issues installing or using any of the software in this book on your specific operating system, or would prefer to use Docker to help develop your Python packages, we have provided an alternative software setup with Docker that has everything you need already installed to get started. [Docker](https://docs.docker.com/get-started/overview/) is a platform that allows you to run and develop software in an isolated environment called a _container_. _Images_ contain the instructions required to create a container.

We have developed Docker images to support Python package development in Visual Studio Code or JupyterLab, and we describe minimal workflows for using these images to follow along with this book in the sections below. Feel free to customize these images and/or workflows to suit your specific use cases. We will continue to maintain the Docker images via their GitHub repositories ([py-pkgs/docker-vscode](https://github.com/py-pkgs/docker-vscode) and [py-pkgs/docker-jupyter](https://github.com/py-pkgs/docker-jupyter)) to support readers of this book into the future.

### 2.6.1. Docker with Visual Studio Code[#](#docker-with-visual-studio-code "Permalink to this heading")

To develop with Docker inside Visual Studio Code, you can consult the Visual Studio Code [official container tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial), or try following the steps below:

1.  Install Visual Studio Code from the [official website](https://code.visualstudio.com/).
    
2.  Install and configure Docker Desktop for your operating system following the instructions on the [official website](https://www.docker.com/get-started).
    
3.  Once docker is installed, open a command-line interface and pull the `pypkgs/vscode` docker image by running the following command:
    
    $ docker pull pypkgs/vscode
    
    Copy to clipboard
    
4.  From Visual Studio Code, open/create the working directory you want to develop in (this can be called anything and located wherever you like on your file system).
    
5.  In Visual Studio Code, open the _Extensions_ tab on the Visual Studio Code activity bar and search for the “Dev Containers” extension in the search bar. Install this extension if it is not already installed.
    
6.  Create a file called _`.devcontainer.json`_ in your current working directory (be sure to include the period at the beginning of the file name). This file will tell Visual Studio Code how to run in a Docker container. You can read more about this configuration in the [official documentation](https://code.visualstudio.com/docs/devcontainers/create-dev-container), but for now, a minimal set up requires adding the following content to that file:
    
    {
        "name": "poetry",
        "image": "pypkgs/vscode",
        "extensions": \["ms-python.python"\],
    }
    
    Copy to clipboard
    
7.  Now, open the Visual Studio Code [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) and search for and select the command “Dev Containers: Reopen in Container”. This command will open Visual Studio Code inside a container made using the `pypkgs/vscode` Docker image. After Visual Studio Code finishes opening in the container, test that you have access to the three pre-installed pieces of packaging software we need by opening the [integrated terminal](https://code.visualstudio.com/docs/editor/integrated-terminal) and trying the following commands:
    
    $ poetry \--version
    $ conda \--version
    $ cookiecutter \--version
    
    Copy to clipboard
    
8.  Your development environment is now set up, and you can work with Visual Studio Code as if everything were running locally on your machine (except now your development environment exists inside a container). If you exit Visual Studio Code, your container will stop but will persist on your machine. It can be re-opened at a later time using the “Dev Containers: Reopen in Container” command we used in step 7.
    
9.  If you want to completely remove your development container to free up memory on your machine, first find the container’s ID:
    
    $ docker ps \-a
    
    Copy to clipboard
    
    CONTAINER ID   IMAGE
    762bca6eb51e   pypkgs/vscode
    
    Copy to clipboard
    
10.  Then use the `docker rm` command combined with the container’s ID. This will remove the container, including any packages or virtual environments installed in it. However, any files and directories you created will persist on your machine.
    
    $ docker rm 762bca6eb51e
    
    Copy to clipboard
    

### 2.6.2. Docker with JupyterLab[#](#docker-with-jupyterlab "Permalink to this heading")

To develop with Docker in JupyterLab follow the instructions below. Helpful information and tutorials can also be found in the Jupyter Docker Stacks [documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html).

1.  Install and configure Docker Desktop for your operating system following the instructions on the [official website](https://www.docker.com/get-started).
    
2.  Once Docker has been installed, open a command-line interface and pull the `pypkgs/jupyter` Docker image by running the `docker pull` command as follows:
    
    $ docker pull pypkgs/jupyter
    
    Copy to clipboard
    
3.  From the command line, navigate to the directory you want to develop in (this can be called anything and located wherever you like on your file system).
    
4.  Start a new container from that directory by running the following command from the command line:
    
    $ docker run \-p 8888:8888 \\
      \-v "${PWD}":/home/jovyan/work \\
      pypkgs/jupyter
    
    Copy to clipboard
    
    Tip
    
    In the command above, `-p` binds port 8888 in the container to port 8888 on the host machine and `-v` mounts the current directory into the container at the location `/home/jovyan/work`. Windows users that run into issues with the command above may need to try double-slashes in the volume mount path, for example: `-v /$(pwd)://home//jovyan//work`. You can read more about the `docker run` command and its arguments in the Docker command-line interface [documentation](https://docs.docker.com/engine/reference/commandline/run/).
    
5.  Copy the unique URL printed to screen (that looks something like this: `http://127.0.0.1:8888/lab?token=45d53a348580b3acfafa`) to your browser. This will open an instance of JupyterLab running inside a Docker container.
    
6.  Navigate to the `work` directory in JupyterLab. This is where you can develop and create new files and directories that will persist in the directory from where you launched your container.
    
7.  Test that you have access to the three pre-installed pieces of packaging software we need by opening a terminal in JupyterLab and trying the following commands:
    
    $ poetry \--version
    $ conda \--version
    $ cookiecutter \--version
    
    Copy to clipboard
    
8.  When you’ve finished a working session, you can exit JupyterLab, and kill your terminal, and your container will persist. You can restart the container and launch JupyterLab again by first finding its ID:
    
    $ docker ps \-a
    
    Copy to clipboard
    
    CONTAINER ID   IMAGE
    653daa2cd48e   pypkgs/jupyter
    
    Copy to clipboard
    
9.  Then, to restart the container and launch JupyterLab, use the `docker start -a` command combined with the container’s ID:
    
    $ docker start \-a 653daa2cd48e
    
    Copy to clipboard
    
10.  If you want to completely remove the container you can use the `docker rm` command. This will remove the container, including any packages or virtual environments installed in it. However, all files and directories added to the `work` directory will persist on your machine.
    
    $ docker rm 653daa2cd48e
    
    Copy to clipboard
    

{ requestKernel: true, binderOptions: { repo: "binder-examples/jupyter-stacks-datascience", ref: "master", }, codeMirrorConfig: { theme: "abcdef", mode: "python" }, kernelOptions: { name: "python3", path: "./." }, predefinedOutput: true } kernelName="python3"

[

previous

1\. Introduction



](/01-introduction "previous page")[

next

3\. How to package a Python

](/03-how-to-package-a-python "next page")

Contents

*   [2.1. The command-line interface](#the-command-line-interface)
*   [2.2. Installing software](#installing-software)
    *   [2.2.1. Installing Python](#installing-python)
    *   [2.2.2. Install packaging software](#install-packaging-software)
*   [2.3. Register for a PyPI account and get an authentication token](#register-for-a-pypi-account-and-get-an-authentication-token)
*   [2.4. Set up Git and GitHub](#set-up-git-and-github)
*   [2.5. Python integrated development environments](#python-integrated-development-environments)
    *   [2.5.1. Visual Studio Code](#visual-studio-code)
    *   [2.5.2. JupyterLab](#jupyterlab)
    *   [2.5.3. RStudio](#rstudio)
*   [2.6. Developing with Docker](#developing-with-docker)
    *   [2.6.1. Docker with Visual Studio Code](#docker-with-visual-studio-code)
    *   [2.6.2. Docker with JupyterLab](#docker-with-jupyterlab)

By Tomas Beuzen & Tiffany Timbers

© Copyright 2023. CC BY-NC-SA 4.0.