22\. Python C extensions[¶](#python-c-extensions "Permalink to this headline")
==============================================================================

An interesting feature offered to developers by the CPython implementation is the ease of interfacing C code to Python.

There are three key methods developers use to call C functions from their python code - `ctypes`, `SWIG` and `Python/C API`. Each method comes with its own merits and demerits.

Firstly, why would you want to interface C with Python?

A few common reasons are :

*   You want speed and you know C is about 50x faster than Python.
*   Certain legacy C libraries work just as well as you want them to, so you don’t want to rewrite them in python.
*   Certain low level resource access - from memory to file interfaces.
*   Just because you want to.

22.1. CTypes[¶](#ctypes "Permalink to this headline")
-----------------------------------------------------

The Python [ctypes module](https://docs.python.org/2/library/ctypes.html) is probably the easiest way to call C functions from Python. The ctypes module provides C compatible data types and functions to load DLLs so that calls can be made to C shared libraries without having to modify them. The fact that the C side needn’t be touched adds to the simplicity of this method.

**Example**

Simple C code to add two numbers, save it as `add.c`

//sample C file to add 2 numbers \- int and floats

int add\_int(int, int);
float add\_float(float, float);

int add\_int(int num1, int num2){
    return num1 + num2;
}

float add\_float(float num1, float num2){
    return num1 + num2;
}

Next compile the C file to a `.so` file (DLL in windows) This will generate an adder.so file.

#For Linux
$  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c

#For Mac
$ gcc -shared -Wl,-install\_name,adder.so -o adder.so -fPIC add.c

Now in your python code -

from ctypes import \*

#load the shared object file
adder \= CDLL('./adder.so')

#Find sum of integers
res\_int \= adder.add\_int(4,5)
print "Sum of 4 and 5 = " + str(res\_int)

#Find sum of floats
a \= c\_float(5.5)
b \= c\_float(4.1)

add\_float \= adder.add\_float
add\_float.restype \= c\_float
print "Sum of 5.5 and 4.1 = ", str(add\_float(a, b))

And the output is as follows

Sum of 4 and 5 \= 9
Sum of 5.5 and 4.1 \=  9.60000038147

In this example the C file is self explanatory - it contains two functions, one to add two integers and another to add two floats.

In the python file, first the ctypes module is imported. Then the CDLL function of the ctypes module is used to load the shared lib file we created. The functions defined in the C lib are now available to us via the `adder` variable. When `adder.add_int()` is called, internally a call is made to the `add_int` C function. The ctypes interface allows us to use native python integers and strings by default while calling the C functions.

For other types such as boolean or float, we have to use the correct ctypes. This is seen while passing parameters to the `adder.add_float()`. We first create the required c\_float types from python decimal values, and then use them as arguments to the C code. This method is simple and clean, but limited. For example it’s not possible to manipulate objects on the C side.

22.2. SWIG[¶](#swig "Permalink to this headline")
-------------------------------------------------

Simplified Wrapper and Interface Generator, or SWIG for short is another way to interface C code to Python. In this method, the developer must develop an extra interface file which is an input to SWIG (the command line utility).

Python developers generally don’t use this method, because it is in most cases unnecessarily complex. This is a great method when you have a C/C++ code base, and you want to interface it to many different languages.

**Example** (from the [SWIG website](http://www.swig.org/tutorial.html) )

The C code, `example.c` that has a variety of functions and variables

#include <time.h>
double My\_variable \= 3.0;

int fact(int n) {
    if (n <= 1) return 1;
    else return n\*fact(n\-1);
}

int my\_mod(int x, int y) {
    return (x%y);
}

char \*get\_time()
{
    time\_t ltime;
    time(&ltime);
    return ctime(&ltime);
}

The interface file - this will remain the same irrespective of the language you want to port your C code to :

/\* example.i \*/
 %module example
 %{
 /\* Put header files here or function declarations like below \*/
 extern double My\_variable;
 extern int fact(int n);
 extern int my\_mod(int x, int y);
 extern char \*get\_time();
 %}

 extern double My\_variable;
 extern int fact(int n);
 extern int my\_mod(int x, int y);
 extern char \*get\_time();

And now to compile it

unix % swig \-python example.i
unix % gcc \-c example.c example\_wrap.c \\
        \-I/usr/local/include/python2.1
unix % ld \-shared example.o example\_wrap.o \-o \_example.so

Finally, the Python output

\>>> import example
\>>> example.fact(5)
120
\>>> example.my\_mod(7,3)
1
\>>> example.get\_time()
'Sun Feb 11 23:01:07 1996'
\>>>

As we can see, SWIG achieves the same result, but requires a slightly more involved effort. But it’s worth it if you are targeting multiple languages.

22.3. Python/C API[¶](#python-c-api "Permalink to this headline")
-----------------------------------------------------------------

The [C/Python API](https://docs.python.org/2/c-api/) is probably the most widely used method - not for its simplicity but for the fact that you can manipulate python objects in your C code.

This method requires your C code to be specifically written for interfacing with Python code. All Python objects are represented as a PyObject struct and the `Python.h` header file provides various functions to manipulate it. For example if the PyObject is also a PyListType (basically a list), then we can use the `PyList_Size()` function on the struct to get the length of the list. This is equivalent to calling `len(list)` in python. Most of the basic functions/opertions that are there for native Python objects are made available in C via the `Python.h` header.

**Example**

To write a C extension that adds all the elements in a python list. (all elements are numbers)

Let’s start with the final interface we’d like to have, here is the python file that uses the C extension :

#Though it looks like an ordinary python import, the addList module is implemented in C
import addList

l \= \[1,2,3,4,5\]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))

The above looks like any ordinary python file, which imports and uses another python module called `addList`. The only difference is that the addList module is not written in Python at all, but rather in C.

Next we’ll have a look at the C code that get’s built into the `addList` Python module. This may seem a bit daunting at first, but once you understand the various components that go into writing the C file, it’s pretty straightforward.

_adder.c_

//Python.h has all the required function definitions to manipulate the Python objects
#include <Python.h>

 //This is the function that is called from your python code
static PyObject\* addList\_add(PyObject\* self, PyObject\* args){

  PyObject \* listObj;

  //The input arguments come as a tuple, we parse the args to get the various variables
  //In this case it's only one list variable, which will now be referenced by listObj
  if (! PyArg\_ParseTuple( args, "O", &listObj))
    return NULL;

  //length of the list
  long length = PyList\_Size(listObj);

  //iterate over all the elements
  long i, sum =0;
  for(i = 0; i < length; i++){
    //get an element out of the list - the element is also a python objects
    PyObject\* temp = PyList\_GetItem(listObj, i);
    //we know that object represents an integer - so convert it into C long
    long elem = PyInt\_AsLong(temp);
    sum += elem;
  }

  //value returned back to python code - another python object
  //build value here converts the C long to a python integer
  return Py\_BuildValue("i", sum);
}

//This is the docstring that corresponds to our 'add' function.
static char addList\_docs\[\] =
    "add( ): add all elements of the list\\n";

/\* This table contains the relavent info mapping -
  <function-name in python module>, <actual-function>,
  <type-of-args the function expects>, <docstring associated with the function>
\*/
static PyMethodDef addList\_funcs\[\] = {
    {"add", (PyCFunction)addList\_add, METH\_VARARGS, addList\_docs},
    {NULL, NULL, 0, NULL}
};

/\*
addList is the module name, and this is the initialization block of the module.
<desired module name>, <the-info-table>, <module's-docstring>
\*/
PyMODINIT\_FUNC initaddList(void){
    Py\_InitModule3("addList", addList\_funcs,
                   "Add all ze lists");
}

A step by step explanation :

*   The `<Python.h>` file consists of all the required types (to represent Python object types) and function definitions (to operate on the python objects).
*   Next we write the function which we plan to call from python. Conventionally the function names are {module-name}\_{function-name}, which in this case is `addList_add`. More about the function later.
*   Then fill in the info table - which contains all the relevant info of the functions we desire to have in the module. Every row corresponds to a function, with the last one being a sentinel value (row of null elements).
*   Finally the module initialization block which is of the signature `PyMODINIT_FUNC init{module-name}`.

The function `addList_add` accepts arguments as a PyObject type struct (args is also a tuple type - but since everything in python is an object, we use the generic PyObject notion). The incoming arguments is parsed (basically split the tuple into individual elements) by `PyArg_ParseTuple()`. The first parameter is the argument variable to be parsed. The second argument is a string that tells us how to parse each element in the args tuple. The character in the Nth position of the string tells us the type of the Nth element in the args tuple, example - ‘i’ would mean integer, ‘s’ would mean string and ‘O’ would mean a Python object. Next multiple arguments follow, these are where you would like the `PyArg_ParseTuple()` function to store all the elements that it has parsed. The number of such arguments is equal to the number of arguments which the module function expects to receive, and positional integrity is maintained. For example if we expected a string, integer and a python list in that order, the function signature would be

int n;
char \*s;
PyObject\* list;
PyArg\_ParseTuple(args, "siO", &s, &n, &list);

In this case we only have to extract a list object, and store it in the variable `listObj`. We then use the `PyList_Size()` function on our list object and get the length. This is similar to how you would call `len(list)` in python.

Now we loop through the list, get each element using the `PyList_GetItem(list, index)` function. This returns a PyObject\*. But since we know that the Python objects are also `PyIntType`, we just use the `PyInt_AsLong(PyObj *)` function to get the required value. We do this for every element and finally get the sum.

The sum is converted to a python object and is returned to the Python code with the help of `Py_BuildValue()`. Here the “i” indicates that the value we want to build is a python integer object.

Now we build the C module. Save the following code as `setup.py`

#build the modules

from distutils.core import setup, Extension

setup(name\='addList', version\='1.0',  \\
      ext\_modules\=\[Extension('addList', \['adder.c'\])\])

and run

python setup.py install

This should now build and install the C file into the python module we desire.

After all this hard work, we’ll now test if the module works -

#module that talks to the C code
import addList

l \= \[1,2,3,4,5\]
print "Sum of List - " + str(l) + " = " +  str(addList.add(l))

And here is the output

Sum of List \- \[1, 2, 3, 4, 5\] \= 15

So as you can see, we have developed our first successful C Python extension using the Python.h API. This method does seem complex at first, but once you get used to it it can prove to be quite useful.

Other ways to interface C code to Python is to use an alternative and faster build of python - [Cython](http://cython.org/). But Cython is a slightly different language than the main stream python we see. Hence that method is not covered here.