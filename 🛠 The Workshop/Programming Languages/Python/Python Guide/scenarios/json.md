[![](https://img.realpython.net/1c3e33fa8ce0d82a964b7f7de310e4bb)](https://srv.realpython.net/click/21871400699/?c=41831496980&p=29182759436&r=84661)

JSON[¶](#json "Permalink to this headline")
===========================================

![https://d33wubrfki0l68.cloudfront.net/c17fde1edf579b1e6d946ab32d8a1c29e6bcf9ba/e431d/_images/33928819683_97b5c6a184_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/c17fde1edf579b1e6d946ab32d8a1c29e6bcf9ba/e431d/_images/33928819683_97b5c6a184_k_d.jpg)

The [json](https://docs.python.org/3/library/json.html) library can parse JSON from strings or files. The library parses JSON into a Python dictionary or list. It can also convert Python dictionaries or lists into JSON strings.

Parsing JSON[¶](#parsing-json "Permalink to this headline")
-----------------------------------------------------------

Take the following string containing JSON data:

json\_string \= '{"first\_name": "Guido", "last\_name":"Rossum"}'

It can be parsed like this:

import json
parsed\_json \= json.loads(json\_string)

and can now be used as a normal dictionary:

print(parsed\_json\['first\_name'\])
"Guido"

You can also convert the following to JSON:

d \= {
    'first\_name': 'Guido',
    'second\_name': 'Rossum',
    'titles': \['BDFL', 'Developer'\],
}

print(json.dumps(d))
'{"first\_name": "Guido", "last\_name": "Rossum", "titles": \["BDFL", "Developer"\]}'