[![](https://img.realpython.net/8899c4a6d15334a6b9f769e9f8bc0cf7)](https://srv.realpython.net/click/41686012779/?c=7309556696&p=29182759436&r=76566)

Networking[¶](#networking "Permalink to this headline")
=======================================================

![https://d33wubrfki0l68.cloudfront.net/14fc2321ce393d5bb666295c27fcfdb944a21eae/b8f49/_images/34151833832_6bdfd930af_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/14fc2321ce393d5bb666295c27fcfdb944a21eae/b8f49/_images/34151833832_6bdfd930af_k_d.jpg)

Twisted[¶](#twisted "Permalink to this headline")
-------------------------------------------------

[Twisted](https://twistedmatrix.com/trac/) is an event-driven networking engine. It can be used to build applications around many different networking protocols, including HTTP servers and clients, applications using SMTP, POP3, IMAP, or SSH protocols, instant messaging, and [much more](https://twistedmatrix.com/trac/wiki/Documentation).

PyZMQ[¶](#pyzmq "Permalink to this headline")
---------------------------------------------

[PyZMQ](https://zeromq.github.com/pyzmq/) is the Python binding for [ZeroMQ](http://zeromq.org/), which is a high-performance asynchronous messaging library. One great advantage of ZeroMQ is that it can be used for message queuing without a message broker. The basic patterns for this are:

*   request-reply: connects a set of clients to a set of services. This is a remote procedure call and task distribution pattern.
*   publish-subscribe: connects a set of publishers to a set of subscribers. This is a data distribution pattern.
*   push-pull (or pipeline): connects nodes in a fan-out/fan-in pattern that can have multiple steps and loops. This is a parallel task distribution and collection pattern.

For a quick start, read the [ZeroMQ guide](http://zguide.zeromq.org/page:all).

gevent[¶](#gevent "Permalink to this headline")
-----------------------------------------------

[gevent](http://www.gevent.org/) is a coroutine-based Python networking library that uses greenlets to provide a high-level synchronous API on top of the libev event loop.