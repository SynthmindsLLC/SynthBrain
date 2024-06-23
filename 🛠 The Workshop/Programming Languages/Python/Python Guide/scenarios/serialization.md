[![](https://img.realpython.net/1c3e33fa8ce0d82a964b7f7de310e4bb)](https://srv.realpython.net/click/21871400699/?c=41831496980&p=29182759436&r=36076)

Data Serialization[¶](#data-serialization "Permalink to this headline")
=======================================================================

![https://d33wubrfki0l68.cloudfront.net/66356d2af55832f7d6a118bc6fe1e30bd3fa9bc3/b9952/_images/33467946364_3e59bd376a_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/66356d2af55832f7d6a118bc6fe1e30bd3fa9bc3/b9952/_images/33467946364_3e59bd376a_k_d.jpg)

What is data serialization?[¶](#what-is-data-serialization "Permalink to this headline")
----------------------------------------------------------------------------------------

Data serialization is the process of converting structured data to a format that allows sharing or storage of the data in a form that allows recovery of its original structure. In some cases, the secondary intention of data serialization is to minimize the data’s size which then reduces disk space or bandwidth requirements.

Flat vs. Nested data[¶](#flat-vs-nested-data "Permalink to this headline")
--------------------------------------------------------------------------

Before beginning to serialize data, it is important to identify or decide how the data should be structured during data serialization - flat or nested. The differences in the two styles are shown in the below examples.

Flat style:

{ "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

Nested style:

{"A"
    { "field1": "value1", "field2": "value2", "field3": "value3" } }

For more reading on the two styles, please see the discussion on [Python mailing list](https://mail.python.org/pipermail/python-list/2010-October/590762.html), [IETF mailing list](https://www.ietf.org/mail-archive/web/json/current/msg03739.html) and [in stackexchange](https://softwareengineering.stackexchange.com/questions/350623/flat-or-nested-json-for-hierarchal-data).

Serializing Text[¶](#serializing-text "Permalink to this headline")
-------------------------------------------------------------------

### Simple file (flat data)[¶](#simple-file-flat-data "Permalink to this headline")

If the data to be serialized is located in a file and contains flat data, Python offers two methods to serialize data.

#### repr[¶](#repr "Permalink to this headline")

The repr method in Python takes a single object parameter and returns a printable representation of the input:

\# input as flat text
a \=  { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

\# the same input can also be read from a file
a \= open('/tmp/file.py', 'r')

\# returns a printable representation of the input;
\# the output can be written to a file as well
print(repr(a))

\# write content to files using repr
with open('/tmp/file.py') as f:f.write(repr(a))

#### ast.literal\_eval[¶](#ast-literal-eval "Permalink to this headline")

The literal\_eval method safely parses and evaluates an expression for a Python datatype. Supported data types are: strings, numbers, tuples, lists, dicts, booleans, and None.

with open('/tmp/file.py', 'r') as f: inp \= ast.literal\_eval(f.read())

### CSV file (flat data)[¶](#csv-file-flat-data "Permalink to this headline")

The CSV module in Python implements classes to read and write tabular data in CSV format.

Simple example for reading:

\# Reading CSV content from a file
import csv
with open('/tmp/file.csv', newline\='') as f:
    reader \= csv.reader(f)
    for row in reader:
        print(row)

Simple example for writing:

\# Writing CSV content to a file
import csv
with open('/temp/file.csv', 'w', newline\='') as f:
    writer \= csv.writer(f)
    writer.writerows(iterable)

The module’s contents, functions, and examples can be found [in the Python documentation](https://docs.python.org/3/library/csv.html).

### YAML (nested data)[¶](#yaml-nested-data "Permalink to this headline")

There are many third party modules to parse and read/write YAML file structures in Python. One such example is below.

\# Reading YAML content from a file using the load method
import yaml
with open('/tmp/file.yaml', 'r', newline\='') as f:
    try:
        print(yaml.load(f))
    except yaml.YAMLError as ymlexcp:
        print(ymlexcp)

Documentation on the third party module can be found [in the PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation).

### JSON file (nested data)[¶](#json-file-nested-data "Permalink to this headline")

Python’s JSON module can be used to read and write JSON files. Example code is below.

Reading:

\# Reading JSON content from a file
import json
with open('/tmp/file.json', 'r') as f:
    data \= json.load(f)

Writing:

\# Writing JSON content to a file using the dump method
import json
with open('/tmp/file.json', 'w') as f:
    json.dump(data, f, sort\_keys\=True)

### XML (nested data)[¶](#xml-nested-data "Permalink to this headline")

XML parsing in Python is possible using the xml package.

Example:

\# reading XML content from a file
import xml.etree.ElementTree as ET
tree \= ET.parse('country\_data.xml')
root \= tree.getroot()

More documentation on using the xml.dom and xml.sax packages can be found [in the Python XML library documentation](https://docs.python.org/3/library/xml.html).

Binary[¶](#binary "Permalink to this headline")
-----------------------------------------------

### NumPy Array (flat data)[¶](#numpy-array-flat-data "Permalink to this headline")

Python’s NumPy array can be used to serialize and deserialize data to and from byte representation.

Example:

import NumPy as np

\# Converting NumPy array to byte format
byte\_output \= np.array(\[ \[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\] \]).tobytes()

\# Converting byte format back to NumPy array
array\_format \= np.frombuffer(byte\_output)

### Pickle (nested data)[¶](#pickle-nested-data "Permalink to this headline")

The native data serialization module for Python is called [Pickle](https://docs.python.org/2/library/pickle.html).

Here’s an example:

import pickle

#Here's an example dict
grades \= { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#Use dumps to convert the object to a serialized string
serial\_grades \= pickle.dumps( grades )

#Use loads to de-serialize an object
received\_grades \= pickle.loads( serial\_grades )

Protobuf[¶](#protobuf "Permalink to this headline")
---------------------------------------------------

If you’re looking for a serialization module that has support in multiple languages, Google’s [Protobuf](https://developers.google.com/protocol-buffers) library is an option.