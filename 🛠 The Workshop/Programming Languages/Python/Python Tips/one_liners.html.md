20\. One-Liners[¶](#one-liners "Permalink to this headline")
============================================================

In this chapter I will show you some one-liner Python commands which can be really helpful.

**Simple Web Server**

Ever wanted to quickly share a file over a network? Well you are in luck. Python has a feature just for you. Go to the directory which you want to serve over the network and write the following code in your terminal:

\# Python 2
python \-m SimpleHTTPServer

\# Python 3
python \-m http.server

**Pretty Printing**

You can print a list and dictionary in a beautiful format in the Python repl. Here is the relevant code:

from pprint import pprint

my\_dict \= {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
print(dir(my\_dict))
\# \['\_\_add\_\_', '\_\_class\_\_', '\_\_contains\_\_', '\_\_delattr\_\_', '\_\_delitem\_\_', '\_\_dir\_\_', '\_\_doc\_\_', '\_\_eq\_\_', '\_\_format\_\_', '\_\_ge\_\_', '\_\_getattribute\_\_', '\_\_getitem\_\_', '\_\_gt\_\_', '\_\_hash\_\_', '\_\_iadd\_\_', '\_\_imul\_\_', '\_\_init\_\_', '\_\_init\_subclass\_\_', '\_\_iter\_\_', '\_\_le\_\_', '\_\_len\_\_', '\_\_lt\_\_', '\_\_mul\_\_', '\_\_ne\_\_', '\_\_new\_\_', '\_\_reduce\_\_', '\_\_reduce\_ex\_\_', '\_\_repr\_\_', '\_\_reversed\_\_', '\_\_rmul\_\_', '\_\_setattr\_\_', '\_\_setitem\_\_', '\_\_sizeof\_\_', '\_\_str\_\_', '\_\_subclasshook\_\_', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'\]

pprint(dir(my\_dict))
\# \['\_\_add\_\_',
\#  '\_\_class\_\_',
\#  '\_\_contains\_\_',
\#  '\_\_delattr\_\_',
\#  '\_\_delitem\_\_',
\#  '\_\_dir\_\_',
\#  '\_\_doc\_\_',
\#  '\_\_eq\_\_',
\#  '\_\_format\_\_',
\#  '\_\_ge\_\_',
\#  '\_\_getattribute\_\_',
\#  '\_\_getitem\_\_',
\#  '\_\_gt\_\_',
\#  '\_\_hash\_\_',
\#  '\_\_iadd\_\_',
\#  '\_\_imul\_\_',
\#  '\_\_init\_\_',
\#  '\_\_init\_subclass\_\_',
\#  '\_\_iter\_\_',
\#  '\_\_le\_\_',
\#  '\_\_len\_\_',
\#  '\_\_lt\_\_',
\#  '\_\_mul\_\_',
\#  '\_\_ne\_\_',
\#  '\_\_new\_\_',
\#  '\_\_reduce\_\_',
\#  '\_\_reduce\_ex\_\_',
\#  '\_\_repr\_\_',
\#  '\_\_reversed\_\_',
\#  '\_\_rmul\_\_',
\#  '\_\_setattr\_\_',
\#  '\_\_setitem\_\_',
\#  '\_\_sizeof\_\_',
\#  '\_\_str\_\_',
\#  '\_\_subclasshook\_\_',
\#  'append',
\#  'clear',
\#  'copy',
\#  'count',
\#  'extend',
\#  'index',
\#  'insert',
\#  'pop',
\#  'remove',
\#  'reverse',
\#  'sort'\]

This is more effective on nested `dict` s. Moreover, if you want to pretty print json quickly from a file then you can simply do:

cat file.json | python \-m json.tool

**Profiling a script**

This can be extremely helpful in pinpointing the bottlenecks in your scripts:

python \-m cProfile my\_script.py

Note: `cProfile` is a faster implementation of `profile` as it is written in c

**CSV to json**

Run this in the terminal:

python \-c "import csv,json;print json.dumps(list(csv.reader(open('csv\_file.csv'))))"

Make sure that you replace `csv_file.csv` to the relevant file name.

**List Flattening**

You can quickly and easily flatten a list using `itertools.chain.from_iterable` from the `itertools` package. Here is a simple example:

a\_list \= \[\[1, 2\], \[3, 4\], \[5, 6\]\]
print(list(itertools.chain.from\_iterable(a\_list)))
\# Output: \[1, 2, 3, 4, 5, 6\]

\# or
print(list(itertools.chain(\*a\_list)))
\# Output: \[1, 2, 3, 4, 5, 6\]

**One-Line Constructors**

Avoid a lot of boilerplate assignments when initializing a class

class A(object):
    def \_\_init\_\_(self, a, b, c, d, e, f):
        self.\_\_dict\_\_.update({k: v for k, v in locals().items() if k != 'self'})

Additional one-liners can be found on the [Python website](https://wiki.python.org/moin/Powerful%20Python%20One-Liners).