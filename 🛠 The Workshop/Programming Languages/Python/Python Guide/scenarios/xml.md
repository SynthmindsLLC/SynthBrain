[![](https://img.realpython.net/6fe6464c8bf6ec2cbcf3f1f0e778156b)](https://srv.realpython.net/click/57356986228/?c=41067926597&p=29182759436&r=16689)

XML parsing[¶](#xml-parsing "Permalink to this headline")
=========================================================

![https://d33wubrfki0l68.cloudfront.net/ebd5827fc53e413556893ac47d4e819f13ba90d9/8b500/_images/33888714601_a1f7d020a2_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/ebd5827fc53e413556893ac47d4e819f13ba90d9/8b500/_images/33888714601_a1f7d020a2_k_d.jpg)

untangle[¶](#untangle "Permalink to this headline")
---------------------------------------------------

[untangle](https://github.com/stchris/untangle) is a simple library which takes an XML document and returns a Python object which mirrors the nodes and attributes in its structure.

For example, an XML file like this:

<?xml version="1.0"?>
<root>
    <child name="child1"\>
</root>

can be loaded like this:

import untangle
obj \= untangle.parse('path/to/file.xml')

and then you can get the child element’s name attribute like this:

obj.root.child\['name'\]

untangle also supports loading XML from a string or a URL.

xmltodict[¶](#xmltodict "Permalink to this headline")
-----------------------------------------------------

[xmltodict](https://github.com/martinblech/xmltodict) is another simple library that aims at making XML feel like working with JSON.

An XML file like this:

<mydocument has="an attribute"\>
  <and>
    <many>elements</many>
    <many>more elements</many>
  </and>
  <plus a="complex"\>
    element as well
  </plus>
</mydocument>

can be loaded into a Python dict like this:

import xmltodict

with open('path/to/file.xml') as fd:
    doc \= xmltodict.parse(fd.read())

and then you can access elements, attributes, and values like this:

doc\['mydocument'\]\['@has'\] \# == u'an attribute'
doc\['mydocument'\]\['and'\]\['many'\] \# == \[u'elements', u'more elements'\]
doc\['mydocument'\]\['plus'\]\['@a'\] \# == u'complex'
doc\['mydocument'\]\['plus'\]\['#text'\] \# == u'element as well'

xmltodict also lets you roundtrip back to XML with the unparse function, has a streaming mode suitable for handling files that don’t fit in memory, and supports XML namespaces.

xmlschema[¶](#xmlschema "Permalink to this headline")
-----------------------------------------------------

[xmlschema](https://github.com/sissaschool/xmlschema) provides support for using XSD-Schemas in Python. Unlike other XML libraries, automatic type parsing is available, so f.e. if the schema defines an element to be of type `int`, the parsed `dict` will contain also an `int` value for that element. Moreover the library supports automatic and explicit validation of XML documents against a schema.

from xmlschema import XMLSchema, etree\_tostring

\# load a XSD schema file
schema \= XMLSchema("your\_schema.xsd")

\# validate against the schema
schema.validate("your\_file.xml")

\# or
schema.is\_valid("your\_file.xml")

\# decode a file
data \= schmema.decode("your\_file.xml")

\# encode to string
s \= etree\_tostring(schema.encode(data))