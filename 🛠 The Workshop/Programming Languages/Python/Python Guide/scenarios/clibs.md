[![](https://img.realpython.net/f55b6e7c8f8101c0112e6d5a85fc81ef)](https://srv.realpython.net/click/64963075769/?c=56885775593&p=29182759436&r=71476)

Interfacing with C/C++ Libraries[¶](#interfacing-with-c-c-libraries "Permalink to this headline")
=================================================================================================

![https://d33wubrfki0l68.cloudfront.net/301a807550ffc9faf2c2e9db567469c8f97affc7/8c90c/_images/34725951345_c8f5959a2e_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/301a807550ffc9faf2c2e9db567469c8f97affc7/8c90c/_images/34725951345_c8f5959a2e_k_d.jpg)

C Foreign Function Interface[¶](#c-foreign-function-interface "Permalink to this headline")
-------------------------------------------------------------------------------------------

[CFFI](https://cffi.readthedocs.io/en/latest/) provides a simple to use mechanism for interfacing with C from both CPython and PyPy. It supports two modes: an inline [ABI](https://stackoverflow.com/questions/2171177/what-is-an-application-binary-interface-abi) compatibility mode (example provided below), which allows you to dynamically load and run functions from executable modules (essentially exposing the same functionality as [LoadLibrary](https://docs.microsoft.com/en-us/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [dlopen](https://www.tldp.org/HOWTO/C++-dlopen/index.html)), and an API mode, which allows you to build C extension modules.

### ABI Interaction[¶](#abi-interaction "Permalink to this headline")

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">cffi</span> <span class="kn">import</span> <span class="n">FFI</span>
<span class="n">ffi</span> <span class="o">=</span> <span class="n">FFI</span><span class="p">()</span>
<span class="n">ffi</span><span class="o">.</span><span class="n">cdef</span><span class="p">(</span><span class="s2">"size_t strlen(const char*);"</span><span class="p">)</span>
<span class="n">clib</span> <span class="o">=</span> <span class="n">ffi</span><span class="o">.</span><span class="n">dlopen</span><span class="p">(</span><span class="bp">None</span><span class="p">)</span>
<span class="n">length</span> <span class="o">=</span> <span class="n">clib</span><span class="o">.</span><span class="n">strlen</span><span class="p">(</span><span class="s2">"String to be evaluated."</span><span class="p">)</span>
<span class="c1"># prints: 23</span>
<span class="k">print</span><span class="p">(</span><span class="s2">"{}"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">length</span><span class="p">))</span>
</pre></div></td></tr></tbody></table>

ctypes[¶](#ctypes "Permalink to this headline")
-----------------------------------------------

[ctypes](https://docs.python.org/3/library/ctypes.html) is the de facto standard library for interfacing with C/C++ from CPython, and it provides not only full access to the native C interface of most major operating systems (e.g., kernel32 on Windows, or libc on \*nix), but also provides support for loading and interfacing with dynamic libraries, such as DLLs or shared objects, at runtime. It brings along with it a whole host of types for interacting with system APIs, and allows you to rather easily define your own complex types, such as structs and unions, and allows you to modify things such as padding and alignment, if needed. It can be a bit crufty to use, but in conjunction with the [struct](https://docs.python.org/3/library/struct.html) module, you are essentially provided full control over how your data types get translated into something usable by a pure C/C++ method.

### Struct Equivalents[¶](#struct-equivalents "Permalink to this headline")

`MyStruct.h`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="k">struct</span> <span class="n">my_struct</span> <span class="p">{</span>
    <span class="kt">int</span> <span class="n">a</span><span class="p">;</span>
    <span class="kt">int</span> <span class="n">b</span><span class="p">;</span>
<span class="p">};</span>
</pre></div></td></tr></tbody></table>

`MyStruct.py`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">ctypes</span>
<span class="k">class</span> <span class="nc">my_struct</span><span class="p">(</span><span class="n">ctypes</span><span class="o">.</span><span class="n">Structure</span><span class="p">):</span>
    <span class="n">_fields_</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">"a"</span><span class="p">,</span> <span class="n">c_int</span><span class="p">),</span>
                <span class="p">(</span><span class="s2">"b"</span><span class="p">,</span> <span class="n">c_int</span><span class="p">)]</span>
</pre></div></td></tr></tbody></table>

SWIG[¶](#swig "Permalink to this headline")
-------------------------------------------

[SWIG](http://www.swig.org), though not strictly Python focused (it supports a large number of scripting languages), is a tool for generating bindings for interpreted languages from C/C++ header files. It is extremely simple to use: the consumer simply needs to define an interface file (detailed in the tutorial and documentations), include the requisite C/C++ headers, and run the build tool against them. While it does have some limits (it currently seems to have issues with a small subset of newer C++ features, and getting template-heavy code to work can be a bit verbose), it provides a great deal of power and exposes lots of features to Python with little effort. Additionally, you can easily extend the bindings SWIG creates (in the interface file) to overload operators and built-in methods, effectively re- cast C++ exceptions to be catchable by Python, etc.

### Example: Overloading \_\_repr\_\_[¶](#example-overloading-repr "Permalink to this headline")

`MyClass.h`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre>1
2
3
4
5
6
7</pre></div></td><td class="code"><div class="highlight"><pre><span></span><span class="cp">#include</span> <span class="cpf">&lt;string&gt;</span><span class="cp"></span>
<span class="k">class</span> <span class="nc">MyClass</span> <span class="p">{</span>
<span class="k">private</span><span class="o">:</span>
    <span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">name</span><span class="p">;</span>
<span class="k">public</span><span class="o">:</span>
    <span class="n">std</span><span class="o">::</span><span class="n">string</span> <span class="n">getName</span><span class="p">();</span>
<span class="p">};</span>
</pre></div></td></tr></tbody></table>

`myclass.i`

<table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre> 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16</pre></div></td><td class="code"><div class="highlight"><pre><span></span>%include <span class="s2">"string.i"</span>

%module myclass
%{
<span class="o">#</span>include <span class="o">&lt;</span><span class="nb">string</span><span class="o">&gt;</span>
<span class="o">#</span>include <span class="s2">"MyClass.h"</span>
%}

%extend MyClass {
    std<span class="o">::</span><span class="nb">string</span> __repr__()
    {
        <span class="nb">return</span> $self<span class="o">-&gt;</span>getName();
    }
}

%include <span class="s2">"MyClass.h"</span>
</pre></div></td></tr></tbody></table>

Boost.Python[¶](#boost-python "Permalink to this headline")
-----------------------------------------------------------

[Boost.Python](http://www.boost.org/doc/libs/1_59_0/libs/python/doc/) requires a bit more manual work to expose C++ object functionality, but it is capable of providing all the same features SWIG does and then some, to include providing wrappers to access PyObjects in C++, extracting SWIG wrapper objects, and even embedding bits of Python into your C++ code.