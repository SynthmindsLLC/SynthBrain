[![](https://img.realpython.net/6fe6464c8bf6ec2cbcf3f1f0e778156b)](https://srv.realpython.net/click/57356986228/?c=41067926597&p=29182759436&r=11111)

The Hitchhiker’s Guide to Python![¶](#the-hitchhiker-s-guide-to-python "Permalink to this headline")
====================================================================================================

Greetings, Earthling! Welcome to The Hitchhiker’s Guide to Python.

**This is a living, breathing guide.** If you’d like to contribute, [fork us on GitHub](https://github.com/realpython/python-guide)!

This handcrafted guide exists to provide both novice and expert Python developers a best practice handbook for the installation, configuration, and usage of Python on a daily basis.

This guide is **opinionated** in a way that is almost, but not quite, entirely _unlike_ Python’s official documentation. You won’t find a list of every Python web framework available here. Rather, you’ll find a nice concise list of highly recommended options.

Note

The use of **Python 3** is _highly_ recommended over Python 2. Consider upgrading your applications and infrastructures if you find yourself _still_ using Python 2 in production today. If you are using Python 3, congratulations — you are indeed a person of excellent taste. —_Kenneth Reitz_

Let’s get started! But first, let’s make sure you know where your towel is.

Getting Started with Python[¶](#getting-started-with-python "Permalink to this headline")
-----------------------------------------------------------------------------------------

New to Python? Let’s properly setup up your Python environment:

*   [Picking a Python Interpreter (3 vs 2)](starting/which-python/)
    *   [The State of Python (3 & 2)](starting/which-python/#the-state-of-python-3-2)
    *   [Recommendations](starting/which-python/#recommendations)
    *   [So…. 3?](starting/which-python/#so-3)
    *   [Implementations](starting/which-python/#implementations)

*   Properly Install Python on your system:

> *   [Properly Installing Python](starting/installation/)
> *   [Installing Python 3 on Mac OS X](starting/install3/osx/)
> *   [Installing Python 3 on Windows](starting/install3/win/)
> *   [Installing Python 3 on Linux](starting/install3/linux/)
> *   [Installing Python 2 on Mac OS X](starting/install/osx/)
> *   [Installing Python 2 on Windows](starting/install/win/)
> *   [Installing Python 2 on Linux](starting/install/linux/)

*   Using Virtualenvs with Pipenv:

> *   [Pipenv & Virtual Environments](dev/virtualenvs/)
>     *   [Make sure you’ve got Python & pip](dev/virtualenvs/#make-sure-you-ve-got-python-pip)
>     *   [Installing Pipenv](dev/virtualenvs/#installing-pipenv)
>     *   [Installing packages for your project](dev/virtualenvs/#installing-packages-for-your-project)
>     *   [Using installed packages](dev/virtualenvs/#using-installed-packages)
>     *   [Next steps](dev/virtualenvs/#next-steps)
> *   [Lower level: virtualenv](dev/virtualenvs/#lower-level-virtualenv)
>     *   [Basic Usage](dev/virtualenvs/#basic-usage)
>     *   [Other Notes](dev/virtualenvs/#other-notes)
>     *   [virtualenvwrapper](dev/virtualenvs/#virtualenvwrapper)
>     *   [virtualenv-burrito](dev/virtualenvs/#virtualenv-burrito)
>     *   [direnv](dev/virtualenvs/#direnv)

Python Development Environments[¶](#python-development-environments "Permalink to this headline")
-------------------------------------------------------------------------------------------------

This part of the guide focuses on the Python development environment, and the best-practice tools that are available for writing Python code.

*   [Your Development Environment](dev/env/)
    *   [Text Editors](dev/env/#text-editors)
    *   [IDEs](dev/env/#ides)
    *   [Interpreter Tools](dev/env/#interpreter-tools)
    *   [Other Tools](dev/env/#other-tools)
*   [Pipenv & Virtual Environments](dev/virtualenvs/)
    *   [Make sure you’ve got Python & pip](dev/virtualenvs/#make-sure-you-ve-got-python-pip)
    *   [Installing Pipenv](dev/virtualenvs/#installing-pipenv)
    *   [Installing packages for your project](dev/virtualenvs/#installing-packages-for-your-project)
    *   [Using installed packages](dev/virtualenvs/#using-installed-packages)
    *   [Next steps](dev/virtualenvs/#next-steps)
*   [Lower level: virtualenv](dev/virtualenvs/#lower-level-virtualenv)
    *   [Basic Usage](dev/virtualenvs/#basic-usage)
    *   [Other Notes](dev/virtualenvs/#other-notes)
    *   [virtualenvwrapper](dev/virtualenvs/#virtualenvwrapper)
    *   [virtualenv-burrito](dev/virtualenvs/#virtualenv-burrito)
    *   [direnv](dev/virtualenvs/#direnv)
*   [Further Configuration of pip and Virtualenv](dev/pip-virtualenv/)
    *   [Requiring an active virtual environment for `pip`](dev/pip-virtualenv/#requiring-an-active-virtual-environment-for-pip)
    *   [Caching packages for future use](dev/pip-virtualenv/#caching-packages-for-future-use)

Writing Great Python Code[¶](#writing-great-python-code "Permalink to this headline")
-------------------------------------------------------------------------------------

This part of the guide focuses on the best-practices for writing Python code.

*   [Structuring Your Project](writing/structure/)
    *   [Structure of the Repository](writing/structure/#structure-of-the-repository)
    *   [Structure of Code is Key](writing/structure/#structure-of-code-is-key)
    *   [Modules](writing/structure/#modules)
    *   [Packages](writing/structure/#packages)
    *   [Object-oriented programming](writing/structure/#object-oriented-programming)
    *   [Decorators](writing/structure/#decorators)
    *   [Context Managers](writing/structure/#context-managers)
    *   [Dynamic typing](writing/structure/#dynamic-typing)
    *   [Mutable and immutable types](writing/structure/#mutable-and-immutable-types)
    *   [Vendorizing Dependencies](writing/structure/#vendorizing-dependencies)
    *   [Runners](writing/structure/#runners)
    *   [Further Reading](writing/structure/#further-reading)
*   [Code Style](writing/style/)
    *   [General concepts](writing/style/#general-concepts)
    *   [Idioms](writing/style/#idioms)
    *   [Zen of Python](writing/style/#zen-of-python)
    *   [PEP 8](writing/style/#pep-8)
    *   [Conventions](writing/style/#conventions)
*   [Reading Great Code](writing/reading/)
*   [Documentation](writing/documentation/)
    *   [Project Documentation](writing/documentation/#project-documentation)
    *   [Project Publication](writing/documentation/#project-publication)
    *   [Code Documentation Advice](writing/documentation/#code-documentation-advice)
    *   [Other Tools](writing/documentation/#other-tools)
*   [Testing Your Code](writing/tests/)
    *   [The Basics](writing/tests/#the-basics)
    *   [Tools](writing/tests/#tools)
*   [Logging](writing/logging/)
    *   [… or Print?](writing/logging/#or-print)
    *   [Logging in a Library](writing/logging/#logging-in-a-library)
    *   [Logging in an Application](writing/logging/#logging-in-an-application)
*   [Common Gotchas](writing/gotchas/)
    *   [Mutable Default Arguments](writing/gotchas/#mutable-default-arguments)
    *   [Late Binding Closures](writing/gotchas/#late-binding-closures)
    *   [Bytecode (.pyc) Files Everywhere!](writing/gotchas/#bytecode-pyc-files-everywhere)
*   [Choosing a License](writing/license/)

Scenario Guide for Python Applications[¶](#scenario-guide-for-python-applications "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

This part of the guide focuses on tool and module advice based on different scenarios.

*   [Network Applications](scenarios/client/)
    *   [HTTP](scenarios/client/#http)
    *   [Distributed Systems](scenarios/client/#distributed-systems)
*   [Web Applications & Frameworks](scenarios/web/)
    *   [Context](scenarios/web/#context)
    *   [Frameworks](scenarios/web/#frameworks)
    *   [Web Servers](scenarios/web/#web-servers)
    *   [WSGI Servers](scenarios/web/#wsgi-servers)
    *   [Server Best Practices](scenarios/web/#server-best-practices)
    *   [Hosting](scenarios/web/#hosting)
    *   [Templating](scenarios/web/#templating)
*   [HTML Scraping](scenarios/scrape/)
    *   [Web Scraping](scenarios/scrape/#web-scraping)
    *   [lxml and Requests](scenarios/scrape/#lxml-and-requests)
*   [Command-line Applications](scenarios/cli/)
    *   [Click](scenarios/cli/#click)
    *   [docopt](scenarios/cli/#docopt)
    *   [Plac](scenarios/cli/#plac)
    *   [Cliff](scenarios/cli/#cliff)
    *   [Cement](scenarios/cli/#cement)
    *   [Python Fire](scenarios/cli/#python-fire)
*   [GUI Applications](scenarios/gui/)
    *   [Camelot](scenarios/gui/#camelot)
    *   [Cocoa](scenarios/gui/#cocoa)
    *   [GTk](scenarios/gui/#gtk)
    *   [PyGObject aka (PyGi)](scenarios/gui/#pygobject-aka-pygi)
    *   [Kivy](scenarios/gui/#kivy)
    *   [PyObjC](scenarios/gui/#pyobjc)
    *   [PySide](scenarios/gui/#pyside)
    *   [PyQt](scenarios/gui/#pyqt)
    *   [Pyjs Desktop (formerly Pyjamas Desktop)](scenarios/gui/#pyjs-desktop-formerly-pyjamas-desktop)
    *   [Qt](scenarios/gui/#qt)
    *   [PySimpleGUI](scenarios/gui/#pysimplegui)
    *   [Toga](scenarios/gui/#toga)
    *   [Tk](scenarios/gui/#tk)
    *   [wxPython](scenarios/gui/#wxpython)
*   [Databases](scenarios/db/)
    *   [DB-API](scenarios/db/#db-api)
    *   [SQLAlchemy](scenarios/db/#sqlalchemy)
    *   [Records](scenarios/db/#records)
    *   [PugSQL](scenarios/db/#pugsql)
    *   [Django ORM](scenarios/db/#django-orm)
    *   [peewee](scenarios/db/#peewee)
    *   [PonyORM](scenarios/db/#ponyorm)
    *   [SQLObject](scenarios/db/#sqlobject)
*   [Networking](scenarios/network/)
    *   [Twisted](scenarios/network/#twisted)
    *   [PyZMQ](scenarios/network/#pyzmq)
    *   [gevent](scenarios/network/#gevent)
*   [Systems Administration](scenarios/admin/)
    *   [Fabric](scenarios/admin/#fabric)
    *   [Salt](scenarios/admin/#salt)
    *   [Psutil](scenarios/admin/#psutil)
    *   [Ansible](scenarios/admin/#ansible)
    *   [Chef](scenarios/admin/#chef)
    *   [Puppet](scenarios/admin/#puppet)
    *   [Blueprint](scenarios/admin/#blueprint)
    *   [Buildout](scenarios/admin/#buildout)
    *   [Shinken](scenarios/admin/#shinken)
*   [Continuous Integration](scenarios/ci/)
    *   [Why?](scenarios/ci/#why)
    *   [Jenkins](scenarios/ci/#jenkins)
    *   [Buildbot](scenarios/ci/#buildbot)
    *   [Tox](scenarios/ci/#tox)
    *   [Travis-CI](scenarios/ci/#travis-ci)
*   [Speed](scenarios/speed/)
    *   [Context](scenarios/speed/#context)
    *   [C Extensions](scenarios/speed/#id2)
    *   [Concurrency](scenarios/speed/#concurrency)
*   [Scientific Applications](scenarios/scientific/)
    *   [Context](scenarios/scientific/#context)
    *   [Tools](scenarios/scientific/#tools)
    *   [Libraries](scenarios/scientific/#libraries)
    *   [Resources](scenarios/scientific/#resources)
*   [Image Manipulation](scenarios/imaging/)
    *   [Python Imaging Library](scenarios/imaging/#python-imaging-library)
    *   [Open Source Computer Vision](scenarios/imaging/#open-source-computer-vision)
*   [Data Serialization](scenarios/serialization/)
    *   [What is data serialization?](scenarios/serialization/#what-is-data-serialization)
    *   [Flat vs. Nested data](scenarios/serialization/#flat-vs-nested-data)
    *   [Serializing Text](scenarios/serialization/#serializing-text)
    *   [Binary](scenarios/serialization/#binary)
    *   [Protobuf](scenarios/serialization/#protobuf)
*   [XML parsing](scenarios/xml/)
    *   [untangle](scenarios/xml/#untangle)
    *   [xmltodict](scenarios/xml/#xmltodict)
    *   [xmlschema](scenarios/xml/#xmlschema)
*   [JSON](scenarios/json/)
    *   [Parsing JSON](scenarios/json/#parsing-json)
*   [Cryptography](scenarios/crypto/)
    *   [cryptography](scenarios/crypto/#id1)
    *   [GPGME bindings](scenarios/crypto/#gpgme-bindings)
*   [Machine Learning](scenarios/ml/)
    *   [SciPy Stack](scenarios/ml/#scipy-stack)
    *   [scikit-learn](scenarios/ml/#scikit-learn)
*   [Interfacing with C/C++ Libraries](scenarios/clibs/)
    *   [C Foreign Function Interface](scenarios/clibs/#c-foreign-function-interface)
    *   [ctypes](scenarios/clibs/#ctypes)
    *   [SWIG](scenarios/clibs/#swig)
    *   [Boost.Python](scenarios/clibs/#boost-python)

Shipping Great Python Code[¶](#shipping-great-python-code "Permalink to this headline")
---------------------------------------------------------------------------------------

This part of the guide focuses on sharing and deploying your Python code.

*   [Publishing Your Code](shipping/publishing/)
    *   [Creating a Project Repo on GitHub](shipping/publishing/#creating-a-project-repo-on-github)
    *   [When Your Project Grows](shipping/publishing/#when-your-project-grows)
*   [Packaging Your Code](shipping/packaging/)
    *   [Alternatives to Packaging](shipping/packaging/#alternatives-to-packaging)
    *   [For Python Developers](shipping/packaging/#for-python-developers)
    *   [For Linux Distributions](shipping/packaging/#for-linux-distributions)
*   [Freezing Your Code](shipping/freezing/)
    *   [Alternatives to Freezing](shipping/freezing/#alternatives-to-freezing)
    *   [Comparison of Freezing Tools](shipping/freezing/#comparison-of-freezing-tools)
    *   [Windows](shipping/freezing/#windows)
    *   [OS X](shipping/freezing/#os-x)
    *   [Linux](shipping/freezing/#linux)

Additional Notes[¶](#additional-notes "Permalink to this headline")
-------------------------------------------------------------------

This part of the guide, which is mostly prose, begins with some background information about Python, and then focuses on next steps.

*   [Introduction](intro/duction/)
    *   [About This Guide](intro/duction/#about-this-guide)
*   [The Community](intro/community/)
    *   [BDFL](intro/community/#bdfl)
    *   [Python Software Foundation](intro/community/#python-software-foundation)
    *   [PEPs](intro/community/#peps)
    *   [Python Conferences](intro/community/#python-conferences)
    *   [Python User Groups](intro/community/#python-user-groups)
    *   [Online Communities](intro/community/#online-communities)
    *   [Python Job Boards](intro/community/#python-job-boards)
*   [Learning Python](intro/learning/)
    *   [Beginner](intro/learning/#beginner)
    *   [Intermediate](intro/learning/#intermediate)
    *   [Advanced](intro/learning/#advanced)
    *   [For Engineers and Scientists](intro/learning/#for-engineers-and-scientists)
    *   [Miscellaneous Topics](intro/learning/#miscellaneous-topics)
    *   [References](intro/learning/#references)
*   [Documentation](intro/documentation/)
    *   [Official Documentation](intro/documentation/#official-documentation)
    *   [Read the Docs](intro/documentation/#read-the-docs)
    *   [pydoc](intro/documentation/#pydoc)
*   [News](intro/news/)
    *   [PyCoder’s Weekly](intro/news/#pycoders-weekly)
    *   [Real Python](intro/news/#real-python)
    *   [Planet Python](intro/news/#planet-python)
    *   [/r/python](intro/news/#r-python)
    *   [Talk Python Podcast](intro/news/#talk-python-podcast)
    *   [Python Bytes Podcast](intro/news/#python-bytes-podcast)
    *   [Python Weekly](intro/news/#python-weekly)
    *   [Python News](intro/news/#python-news)
    *   [Import Python Weekly](intro/news/#import-python-weekly)
    *   [Awesome Python Newsletter](intro/news/#awesome-python-newsletter)

Note

Notes defined within all diatonic and chromatic musical scales have been intentionally excluded from this list of additional notes. Additionally, this note.

* * *

Contribution notes and legal information (for those interested).

*   [Contribute](notes/contribute/)
    *   [Style Guide](notes/contribute/#style-guide)
    *   [Todo List](notes/contribute/#todo-list)
*   [License](notes/license/)
*   [The Guide Style Guide](notes/styleguide/)
    *   [Relevancy](notes/styleguide/#relevancy)
    *   [Headings](notes/styleguide/#headings)
    *   [Prose](notes/styleguide/#prose)
    *   [Code Examples](notes/styleguide/#code-examples)
    *   [Externally Linking](notes/styleguide/#externally-linking)
    *   [Linking to Sections in The Guide](notes/styleguide/#linking-to-sections-in-the-guide)
    *   [Notes and Warnings](notes/styleguide/#notes-and-warnings)
    *   [TODOs](notes/styleguide/#todos)