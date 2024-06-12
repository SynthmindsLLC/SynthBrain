---
Please provide me with more context! I need to know what the mission is about in order to help you. 

For example, tell me: "* **What kind of mission is it?** Is it a personal mission, a business mission, a mission for a project, etc.?"
* **What is the purpose of the mission?** What are you trying to achieve?
* **What are the goals of the mission?** What specific outcomes are you aiming for?
* **Who is involved in the mission?** Who are the key players?

Once I have this information, I can help you write a compelling and effective mission statement.
---

HubL filters


================

Last updated: January 30, 2024

Filters affect the ultimate output of your HubL. They can be applied to various HubL statements and expressions to alter the template markup outputted by the server.

The basic syntax of a filter is `|filtername`. The filter is added directly following the statement or the expression, within its delimiters. Some filters have additional parameters that can be added in parentheses. The basic syntax of a filter with a string, a number, and a boolean parameters is: `|filtername("stringParameter", 10, true)`. Notice that string parameters should be written in quotes. Also note that HubL filters have an alias that can be used to serve the same purpose as the primary filter.

The following article contains all of the supported HubL filters.

**Please note:** you can apply HubL filters to [personalization tokens](https://knowledge.hubspot.com/website-pages/personalize-your-content), such as contact and company tokens, on HubSpot CMS and blog pages, but not in emails. 

abs[](https://developers.hubspot.com/docs/cms/hubl/filters#abs)
---------------------------------------------------------------

Gets the absolute value of a number. You can use this filter to ensure that a number is positive.

{% set my\_number = -53 %} {{ my\_number|abs }}53

add[](https://developers.hubspot.com/docs/cms/hubl/filters#add)
---------------------------------------------------------------

Adds a numeric value to another numeric value. This filter functions the same as the [\+ operator](/docs/cms/hubl/operators-and-expression-tests#math). The parameter in parentheses is the addend that you are combining with your initial numeric value.

{% set my\_num = 40 %} {{ my\_num|add(13) }}53

attr[](https://developers.hubspot.com/docs/cms/hubl/filters#attr)
-----------------------------------------------------------------

Renders the attribute of a dictionary. This filter is the equivalent of printing a variable that exists within a dictionary, such as content.absolute\_url.

| Parameter | Description |
| --- | --- |
| 
`attribute_name`

Required



 | 

Specifies which attribute to print

 |

{{ content|attr("absolute\_url") }} https://developers.hubspot.com/docs/cms/hubl/filters

batch[](https://developers.hubspot.com/docs/cms/hubl/filters#batch)
-------------------------------------------------------------------

A batch filter groups up items within a sequence.

| Parameter | Description |
| --- | --- |
| 
`linecount`

Required



 | 

The number of items to include in the batch

 |
| 

`fill_with`

Optional



 | 

Specifies what to include in order to fill up any missing items

 |

In the example below, there is variable containing a sequence of types of fruits. The batch filter is applied to a loop that iterates through the sequence. The nested loop runs three times to print 3 types of fruit per row, before the outer loop runs again. Notice in the final output that since there are only 5 types of fruit, the final item is replaced by a &nbsp (the second parameter).

{% set rows = \["apples", "oranges", "pears", "grapes", "blueberries"\] %} <table> {% for row in rows|batch(3, "&nbsp;") %} <tr> {% for column in row %} <td>{{ column }}</td> {% endfor %} </tr> {% endfor %} </table><table> <tbody> <tr> <td>apples</td> <td>oranges</td> <td>pears</td> </tr> <tr> <td>grapes</td> <td>blueberries</td> <td>&nbsp;</td> </tr> </tbody> </table>

between\_times[](https://developers.hubspot.com/docs/cms/hubl/filters#between-times)
------------------------------------------------------------------------------------

Calculates the time between two datetime objects in a specified time unit.

**Please note:** it is strongly recommended to use this filter only with variables that return a date. If a date is not passed, the filter will be used on the current date, which may result in inaccurate date information being displayed on your page.

| Parameter | Description |
| --- | --- |
| 
`end`

Required



 | 

The ending datetime object

 |
| 

`timeunit`

Required



 | 

Valid time units are nanos , micros , millis , seconds , minutes , hours , half\_days , days , weeks , months , years , decades , centuries , millennia , and eras .

 |

{% set begin = "2018-07-14T14:31:30+0530"|strtotime("yyyy-MM-dd'T'HH:mm:ssZ") %} {% set end = "2018-07-20T14:31:30+0530"|strtotime("yyyy-MM-dd'T'HH:mm:ssZ") %} {{ begin|between\_times(end, "days") }}6

bool[](https://developers.hubspot.com/docs/cms/hubl/filters#bool)
-----------------------------------------------------------------

Converts a text string value to a boolean.

{% if "true"|bool == true %}hello world{% endif %}hello world

capitalize[](https://developers.hubspot.com/docs/cms/hubl/filters#capitalize)
-----------------------------------------------------------------------------

Capitalize the first letter of a variable value. The first character will be uppercase, all others letters will be lowercased. Subsequent words separated by spaces or hyphens will not have their first letter uppercased.

{% set sentence = "the first letter of a sentence should always be capitalized." %} {{ sentence|capitalize }}The first letter of a sentence should always be capitalized.

center[](https://developers.hubspot.com/docs/cms/hubl/filters#center)
---------------------------------------------------------------------

The center filter uses whitespace to center text within a given field length. This filter is not recommended or particularly useful since HubSpot's HTML compiler will automatically strip out the white space; however, it is included here for the sake of comprehensiveness.

| Parameter | Description |
| --- | --- |
| 
`width`

Required



 | 

Specifies the length of whitespace to center the text in.

 |

The example below shows a center filter being applied to a variable in a pre tag, so the whitespace isn't stripped out.

<pre> {% set var = "string to center" %} before{{ var|center(80) }}after </pre><pre> before string to center after </pre>

convert\_rgb[](https://developers.hubspot.com/docs/cms/hubl/filters#convert-rgb)
--------------------------------------------------------------------------------

Converts a HEX value to an RGB string. This is useful if you need to convert color variables to RGB to be used with a RGBA CSS declaration. In the example below, the value set by a color module is converted to an RGB value and used in an RGBA CSS declaration.

{% set my\_color = "#FFFFFF" %} {{ my\_color|convert\_rgb }} {% color "my\_color" color="#000000", export\_to\_template\_context=True %} <div style="background: rgba({{ widget\_data.my\_color.color|convert\_rgb }}, .5)"></div>255, 255, 255 <div style="background: rgba(0, 0, 0, .5)"></div>

cut[](https://developers.hubspot.com/docs/cms/hubl/filters#cut)
---------------------------------------------------------------

Removes a string from a value. This filter can be used to match and cut out a specific part of a string. The parameter specifies the part of the string that should be removed. The example below removes the space and the word world from the original variable value.

| Parameter | Description |
| --- | --- |
| 
`characters_to_cut`

Required



 | 

The part of the string that should be removed.

 |

{% set my\_string = "Hello world." %} {{ my\_string|cut(" world") }}Hello.

datetimeformat (deprecated)[](https://developers.hubspot.com/docs/cms/hubl/filters#datetimeformat-deprecated-)
--------------------------------------------------------------------------------------------------------------

**Please note**: this filter has been [deprecated](/docs/cms/hubl/functions/deprecated#datetimeformat). Instead, use the [format\_datetime](#format-datetime) filter, which has a more standardized syntax.

default[](https://developers.hubspot.com/docs/cms/hubl/filters#default)
-----------------------------------------------------------------------

If the value is undefined it will return the first parameter, otherwise the value of the variable will be printed. If you want to use default with variables that evaluate to false, you have to set the second parameter to **true**. The first example below would print the message if the variable is not defined. The second example applied the filter to an empty string, which is not undefined, but it prints a message due to the second parameter.

| Parameter | Description |
| --- | --- |
| 
`default_variable`

Required



 | 

Value to return if the variable is undefined. If the variable is defined, the value of the variable will be returned instead.

 |
| 

`boolean`

Optional



 | 

Returns the default\_value if the variable is an empty string

 |

{{ my\_variable|default("my\_variable is not defined") }} {{ ""|default("the string was empty", true) }}my\_variable is not defined the string was empty

dictsort[](https://developers.hubspot.com/docs/cms/hubl/filters#dictsort)
-------------------------------------------------------------------------

Sort a dict and yield (key, value) pairs. Dictionaries are unsorted by default, but you can print a dictionary, sorted by key or value. The first parameter is a boolean to determine, whether or not the sorting is case sensitive. The second parameter determines whether to sort the dict by key or value. The example below prints a sorted contact dictionary, with all the known details about the contact.

| Parameter | Description |
| --- | --- |
| 
`case_sensitive`

Required



 | 

Determines if sorting is case sensitive

 |
| 

`sort_by`

Required



 | 

Determines whether to sort by key or value

 |

{% for item in contact|dictsort(false, "value") %} {{item}} {% endfor %}A sorted contact dictionary

difference[](https://developers.hubspot.com/docs/cms/hubl/filters#difference)
-----------------------------------------------------------------------------

This filter returns the difference of two sets or lists. The list returned from the filter contains all unique elements that are in the first list but not the second.

| Parameter | Description |
| --- | --- |
| 
`list`

Required



 | 

The second list to compare to for use in finding differences from the original list.

 |

{{ \[1, 2, 3\]|difference(\[2, 3, 4, 5\]) }}\[1\]

divide[](https://developers.hubspot.com/docs/cms/hubl/filters#divide)
---------------------------------------------------------------------

Divide the current value by a divisor. The parameter passed is the divisor. This filter is an alternative to the / operator.

| Parameter | Description |
| --- | --- |
| 
`divisor`

Required



 | 

The number to divide the variable by.

 |

{% set numerator = 106 %} {{ numerator|divide(2) }}53

divisible[](https://developers.hubspot.com/docs/cms/hubl/filters#divisible)
---------------------------------------------------------------------------

An alternative to the divisibleby expression test, the filter divisible will evaluate to true if the value is divisible by the given number.

| Parameter | Description |
| --- | --- |
| 
`divisor`

Required



 | 

The number to use when evaluating if the value is divisible.

 |

{% set num = 10 %} {% if num|divisible(2) %} The number is divisble by 2 {% endif %}The number is divisible by 2

escape\_html[](https://developers.hubspot.com/docs/cms/hubl/filters#escape-html)
--------------------------------------------------------------------------------

Escapes the content of an HTML input. Accepts a string and converts the characters `&`, `<`, `>`, `‘`, `”`, and `escape_jinjava` into HTML-safe sequences. Use this filter for HubL variables that are used in HTML but should not allow any HTML.

{% set escape\_string = "<div>This markup is printed as text</div>" %} {{ escape\_string|escape\_html }}&lt;div&gt;This markup is printed as text&lt;/div&gt;

escape\_attr[](https://developers.hubspot.com/docs/cms/hubl/filters#escape-attr)
--------------------------------------------------------------------------------

Escapes the content of an HTML attribute input. Accepts a string and converts the characters `&`, `<`, `‘`, `”`, and `escape_jinjava` into HTML-safe sequences. Use this filter for HubL variables that are being added to HTML attributes.

Note that when escaping values of attributes that accept URLs, such as `href`, you should use the `escape_url` filter instead.

{% set escape\_string = "This <br> markup is printed as text" %} <img src="test.com/testimageurl" alt="{{escape\_string|escape\_attr}}"><img src="test.com/testimageurl" alt="This &lt;br&gt; markup is printed as text">

escape\_jinjava[](https://developers.hubspot.com/docs/cms/hubl/filters#escape-jinjava)
--------------------------------------------------------------------------------------

Converts the characters `{` and `}` in strings to Jinjava-safe sequences. Use this filter if you need to display text that might contain such characters in Jinjava.

{% set escape\_string = "{{This markup is printed as text}}" %} {{ escape\_string|escape\_jinjava }}{{This markup is printed as text}}

escape\_js[](https://developers.hubspot.com/docs/cms/hubl/filters#escape-js)
----------------------------------------------------------------------------

Escapes strings, including `escape_jinjava`, so that they can be safely inserted into a JavaScript variable declaration. Use this filter for HubL variables that are used inside HTML script elements.

{% set escape\_string = "\\tThey said 'This string can safely be inserted into JavaScript.'" %} {{ escape\_string|escape\_js }}\\tThey said \\x27This string can safely be inserted into JavaScript.\\x27

escape\_url[](https://developers.hubspot.com/docs/cms/hubl/filters#escape-url)
------------------------------------------------------------------------------

Escapes the content of a URL input, enforcing specified protocols, stripping invalid and dangerous characters, and encodes HTML entities. Returns empty if a URL is valid. Use this filter for HubL variables that are used within HTML attributes that should be valid URLs.

{% set escape\_string = "https://www.google.com<" %} <a href="{{ escape\_string|escape\_url }}"> <a href="">

escapejson[](https://developers.hubspot.com/docs/cms/hubl/filters#escapejson)
-----------------------------------------------------------------------------

Escapes strings so that they can be used as JSON values.

{% set escape\_string = "<script>alert('oh no!')</script>" %} {% require\_js position="head" %} <script data-search\_input-config="config\_{{ name }}" type="application/json"> { "autosuggest\_results\_message": "{{ escape\_string|escapejson }}" } </script> {% end\_require\_js %}<script data-search\_input-config="config\_widget\_1234567" type="application/json"> { "autosuggest\_results\_message": "<script>alert('oh no!')<\\/script>" } </script>

filesizeformat[](https://developers.hubspot.com/docs/cms/hubl/filters#filesizeformat)
-------------------------------------------------------------------------------------

Format the value like a ‘human-readable’ file size (i.e. 13 kB, 4.1 MB, 102 Bytes, etc). Per default decimal prefixes are used (Mega, Giga, etc.), if the parameter is set to True the binary prefixes are used (Mebi, Gibi).

| Parameter | Description |
| --- | --- |
| 
`boolean`

Optional



 | 

If set to true, binary prefixes are used such as Mebi & Gibi.

 |

{% set bytes = 100000 %} {{ bytes|filesizeformat }}100.0 KB

first[](https://developers.hubspot.com/docs/cms/hubl/filters#first)
-------------------------------------------------------------------

Returns the first item in a sequence.

{% set my\_sequence = \["Item 1", "Item 2", "Item 3"\] %} {{ my\_sequence|first }}Item 1

float[](https://developers.hubspot.com/docs/cms/hubl/filters#float)
-------------------------------------------------------------------

Convert the value into a floating point number. If the conversion doesn’t work it will return 0.0. You can override this default using the first parameter.

| Parameter | Description |
| --- | --- |
| 
`default`

Optional



 | 

Integer to return if the conversion doesn't work. 

 |

{% text "my\_text" value="25", export\_to\_template\_context=True %} {{ widget\_data.my\_text.value|float + 28 }}53.0

forceescape[](https://developers.hubspot.com/docs/cms/hubl/filters#forceescape)
-------------------------------------------------------------------------------

Strictly enforce HTML escaping. In HubSpot's environment there isn't really a use case for double escaping, so this is generally behaves the same as the escape filter.

{% set escape\_string = "<div>This markup is printed as text</div>" %} {{ escape\_string|forceescape }}<div>This markup is printed as text</div>

format[](https://developers.hubspot.com/docs/cms/hubl/filters#format)
---------------------------------------------------------------------

Apply Python string formatting to an object. %s can be replaced with another variable.

{{ "Hi %s %s"|format(contact.firstname, contact.lastname) }} Hi Brian Halligan

format\_currency (deprecated)[](https://developers.hubspot.com/docs/cms/hubl/filters#format-currency-deprecated-)
-----------------------------------------------------------------------------------------------------------------

**Please note:** this filter has been [deprecated](/docs/cms/hubl/functions/deprecated). Instead, use the [format\_currency\_value](#format-currency-value) filter.

format\_currency\_value[](https://developers.hubspot.com/docs/cms/hubl/filters#format-currency-value)
-----------------------------------------------------------------------------------------------------

Formats a given number as a currency based on portal's default currency and locale passed in as a parameter. Replaces the deprecated [format\_currency filter](/docs/cms/hubl/functions/deprecated#format-currency).

{{ 100 | format\_currency\_value(locale='en-GB', currency='EUR', maxDecimalDigits=6, minDecimalDigits=1) }}€100.0

| Parameter | Description |
| --- | --- |
| 
`locale`

Optional



 | 

[The Java local Language tag](https://www.oracle.com/java/technologies/javase/jdk8-jre8-suported-locales.html). The default is the page's locale.Format : ISO639LanguageCodeInLowercase-ISO3166CountryCodeInUppercase

 |
| 

`currency`

Optional



 | 

the [alphabetic ISO 4217 code](https://en.wikipedia.org/wiki/ISO_4217) of the currency, default is the portals default currency. Numeric codes are not accepted.

 |
| 

`minDecimalDigits`

Optional



 | 

The minimum number of decimal digits to use. Defaults to the currency's default number of decimal digits.

 |
| 

`maxDecimalDigits`

Optional



 | 

The maximum number of decimal digits to use. Defaults to the currency's default number of decimal digits.

 |

format\_date[](https://developers.hubspot.com/docs/cms/hubl/filters#format-date)
--------------------------------------------------------------------------------

Formats the date component of a date object.

**Please note:** it is strongly recommended to use this filter only with variables that return a date. If a date is not passed, the filter will be used on the current date, which may result in inaccurate date information being displayed on your page.

| Parameter | Description |
| --- | --- |
| 
`format`

Optional



 | 

The format to use. Can be one of:

*   `short`
*   `medium`
*   `long`
*   `full`
*   a custom pattern following [Unicode LDML](https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)

 |
| 

`timeZone`

Optional



 | 

The time zone of the output date in [IANA TZDB format](https://data.iana.org/time-zones/tzdb/).

 |
| 

`locale`

Optional



 | 

The locale to use for locale-aware formats.

 |

{{ content.publish\_date | format\_date('long') }} {{ content.publish\_date | format\_date('yyyyy.MMMM.dd') }} {{ content.publish\_date | format\_date('medium', 'America/New\_York', 'de-DE') }}November 28, 2022 02022.November.28 28.11.2022

format\_datetime[](https://developers.hubspot.com/docs/cms/hubl/filters#format-datetime)
----------------------------------------------------------------------------------------

Formats both the date and time components of a date object. This filter replaces the deprecated [datetimeformat](/docs/cms/hubl/functions/deprecated#datetimeformat-nbsp-) filter. By default, returns a datetime in the UTC-00:00 time zone.

**Please note:** it is strongly recommended to use this filter only with variables that return a date. If a date is not passed, the filter will be used on the current date, which may result in inaccurate date information being displayed on your page.

| Parameter | Description |
| --- | --- |
| 
`format`

Optional



 | 

The format to use. Can be one of:

*   `short`
*   `medium`
*   `long`
*   `full`
*   a custom pattern following [Unicode LDML](https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)

When using `long` or `full`, timestamp will include a Z to denote zero offset UTC time (i.e., `2:23:00 PM Z`). To remove the Z designator, specify a `timeZone`.

 |
| 

`timeZone`

Optional



 | 

The time zone of the output date in [IANA TZDB format](https://data.iana.org/time-zones/tzdb/). By default, returns UTC time.

 |
| 

`locale`

Optional



 | 

The locale to use for locale-aware formats.

 |

{{ content.publish\_date | format\_datetime('medium', 'America/New\_York', 'de-DE') }}12/31/69 7:00 PM

format\_time[](https://developers.hubspot.com/docs/cms/hubl/filters#format-time)
--------------------------------------------------------------------------------

Formats the time component of a date object.

**Please note:** it is strongly recommended to use this filter only with variables that return a date. If a date is not passed, the filter will be used on the current date, which may result in inaccurate date information being displayed on your page.

| Parameter | Description |
| --- | --- |
| 
`format`

Optional



 | 

The format to use. Can be one of:

*   `short`
*   `medium`
*   `long`
*   `full`
*   a custom pattern following [Unicode LDML](https://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)

 |
| 

`timeZone`

Optional



 | 

The time zone of the output date in [IANA TZDB format](https://data.iana.org/time-zones/tzdb/).

 |
| 

`locale`

Optional



 | 

The locale to use for locale-aware formats.

 |

{{ content.updated | format\_time('long') }} {{ content.updated | format\_time('hh:mm a') }} {{ content.updated | format\_time('medium', 'America/New\_York', 'de-DE') }}3:25:06 PM Z 03:25 PM 10:25:44

fromjson[](https://developers.hubspot.com/docs/cms/hubl/filters#fromjson)
-------------------------------------------------------------------------

Converts a JSON string to an object.

{% set obj ="{ "name":"Brian","role":"Owner" }" %} {{ obj|fromjson }}{role=Owner, name=Brian}

geo\_distance[](https://developers.hubspot.com/docs/cms/hubl/filters#geo-distance)
----------------------------------------------------------------------------------

Calculates the ellipsoidal 2D distance between two points on Earth.

<!-- in the example below the HubDB Location = 42.3667, -71.1060 (Cambridge, MA) | Chicago, IL = 37.3435, -122.0344 --> {{ row.location | geo\_distance(37.3435, -122.0344, "mi") }} MI861.1655563461395 MI

groupby[](https://developers.hubspot.com/docs/cms/hubl/filters#groupby)
-----------------------------------------------------------------------

The groupby filter groups a sequence of objects by a common attribute. The parameter sets the common attribute to group by.

| Parameter | Description |
| --- | --- |
| 
`attribute`

Required



 | 

The attribute to group by.

 |

<ul> {% for group in contents|groupby("blog\_post\_author") %} <li>{{ group.grouper }} <ul> {% for content in group.list %} <li>{{ content.name }}</li> {% endfor %} </ul> </li> {% endfor %} </ul><ul> <li>Blog author 1 <ul> <li>Post by Blog author 1<li> <li>Post by Blog author 1<li> <li>Post by Blog author 1<li> </ul> </li> <li>Blog author 2 <ul> <li>Post by Blog author 2<li> <li>Post by Blog author 2<li> <li>Post by Blog author 2<li> </ul> </li> <li>Blog author 3 <ul> <li>Post by Blog author 3<li> <li>Post by Blog author 3<li> <li>Post by Blog author 3<li> </ul> </li> </ul>

indent[](https://developers.hubspot.com/docs/cms/hubl/filters#indent)
---------------------------------------------------------------------

The indent filter uses whitespace to indent text within a given field length. This filter is not recommended or particularly useful since HubSpot's HTML compiler will automatically strip out the white space; however, it is included here for the sake of comprehensiveness. The example below shows a center filter being applied to a variable in a pre tag, so the whitespace isn't stripped out. The first parameter controls the amount of whitespace and the second boolean toggles whether to indent the first line.

| Parameter | Description |
| --- | --- |
| 
`width`

Required



 | 

The amount of whitespace to be applied.

 |
| 

`boolean`

Required



 | 

A boolean value on whether to indent the first line.

 |

<pre> {% set var = "string to indent" %} {{ var|indent(2, true) }} </pre> string to indent

int[](https://developers.hubspot.com/docs/cms/hubl/filters#int)
---------------------------------------------------------------

Convert the value into an integer. If the conversion doesn’t work it will return 0. You can override this default using the first parameter.

| Parameter | Description |
| --- | --- |
| 
`default`

Required



 | 

Integer to return if the conversion doesn't work.

 |

{% text "my\_text" value="25", export\_to\_template\_context=True %} {{ widget\_data.my\_text.value|int + 28 }}53

intersect[](https://developers.hubspot.com/docs/cms/hubl/filters#intersect)
---------------------------------------------------------------------------

This filter returns the intersection of two sets or lists. The list returned from the filter contains all unique elements that are contained in both lists.

| Parameter | Description |
| --- | --- |
| 
`list`

Required



 | 

The second list to compare to for use in finding where the list intersects with the original list.

 |

{{ \[1, 2, 3\]|intersect(\[2, 3, 4, 5\]) }}\[2, 3\]

ipaddr[](https://developers.hubspot.com/docs/cms/hubl/filters#ipaddr)
---------------------------------------------------------------------

Evaluates to true if the value is a valid IPv4 or IPv6 address.

{% set ip = "1.0.0.1" %} {% if ip|ipaddr %} The string is a valid IP address {% endif %} The string is a valid IP address

join[](https://developers.hubspot.com/docs/cms/hubl/filters#join)
-----------------------------------------------------------------

Return a string which is the concatenation of the strings in the sequence. The separator between elements is an empty string per default, you can define it with the optional parameter. The second parameter can be used to specify an attribute to join.

| Parameter | Type | Description |
| --- | --- | --- |
| 
`delimiter`

Optional



 | String | 

The delimiter to use when concatenating strings.

 |
| 

`attribute`

Optional



 | HubL Variable | 

Attribute of value to join in an object.

 |

{% set my\_list = \[1, 2, 3\] %} {% set sep = "---" %} {{ my\_list|join }} {{ my\_list|join("|") }} {{ my\_list|join(sep) }}123 1|2|3 1---2---3

last[](https://developers.hubspot.com/docs/cms/hubl/filters#last)
-----------------------------------------------------------------

Returns the last item of a sequence.

{% set my\_sequence = \["Item 1", "Item 2", "Item 3"\] %} {% my\_sequence|last %}Item 3

length[](https://developers.hubspot.com/docs/cms/hubl/filters#length)
---------------------------------------------------------------------

Return the number of items of a sequence or mapping.

{% set services = \["Web design", "SEO", "Inbound Marketing", "PPC"\] %} {{ services|length }}4

list[](https://developers.hubspot.com/docs/cms/hubl/filters#list)
-----------------------------------------------------------------

Convert the number values into a list. If it was a string the returned list will be a list of characters. To add strings to a sequence, simply add them to the string variables to the sequence delimiters \[ \].

{% set one = 1 %} {% set two = 2 %} {% set three = 3 %} {% set four = \["four"\] %} {% set list\_num = one|list + two|list + three|list + four|list %} {{ list\_num }}\[1,2,3\]

log[](https://developers.hubspot.com/docs/cms/hubl/filters#log)
---------------------------------------------------------------

Calculates the natural logarithm of a number.

| Parameter | Description |
| --- | --- |
| 
`base`

Optional



 | 

Calculate the logarithm at the nth base.

 |

{{ 10|log }} {{ 65536|log(2) }}2.302585092994046 16.0

lower[](https://developers.hubspot.com/docs/cms/hubl/filters#lower)
-------------------------------------------------------------------

Convert a value to all lowercase letters.

{{ text "text" value="Text to MAKE Lowercase", export\_to\_template\_context=True }} {{ widget\_data.text.value|lower }}text to make lowercase

map[](https://developers.hubspot.com/docs/cms/hubl/filters#map)
---------------------------------------------------------------

Applies a filter on a sequence of objects or looks up an attribute. This is useful when dealing with lists of objects but you are really only interested in a certain value of it.

The basic usage is mapping on an attribute. For example, if you want to use conditional logic to check if a value is present in a particular attribute of a dict. Alternatively, you can let it invoke a filter by passing the name of the filter and the arguments afterwards.

You can use either one of these parameters listed below.
| Parameter | Description |
| --- | --- |
| 
`attribute`

 | 

Attribute to return in the sequence of objects.

 |
| 

`filter`

 | 

Filter to apply to the sequence of objects.

 |

{% set seq = \["item1", "item2", "item3"\] %} {{ seq|map("upper") }} {{ content|map("currentState")}}\[ITEM1, ITEM2, ITEM3\] DRAFT

md5[](https://developers.hubspot.com/docs/cms/hubl/filters#md5)
---------------------------------------------------------------

Calculates the [md5 hash](https://en.wikipedia.org/wiki/MD5) of the given object

{{ content.absolute\_url|md5 }} 923adb4ce05a4c6342c04c80be88d15e

minus\_time[](https://developers.hubspot.com/docs/cms/hubl/filters#minus-time)
------------------------------------------------------------------------------

Subtracts an amount of time to a datetime object.

| Parameter | Description |
| --- | --- |
| 
`diff`

Required



 | 

Amount to subtract.

 |
| 

`timeunit`

Required



 | 

Valid time units are nanos , micros , millis , seconds , minutes , hours , half\_days , days , weeks , months , years , decades , centuries , millennia , and eras .

 |

{% set date = "2018-07-14T14:31:30+0530"|strtotime("yyyy-MM-dd'T'HH:mm:ssZ") %} {{ date }} {{ date|minus\_time(2, "months") }}2018-07-14 14:31:30 2018-05-14 14:31:30

multiply[](https://developers.hubspot.com/docs/cms/hubl/filters#multiply)
-------------------------------------------------------------------------

Multiplies a value with a number. Functions the same as the [\* operator](/docs/cms/hubl/operators-and-expression-tests?hsLang=en).

{% set n = 20 %} {{ n|multiply(3) }}60

plus\_time[](https://developers.hubspot.com/docs/cms/hubl/filters#plus-time)
----------------------------------------------------------------------------

Adds an amount of time to a datetime object.

| Parameter | Description |
| --- | --- |
| 
`diff`

Required



 | 

Amount to add.

 |
| 

`timeunit`

Required



 | 

Valid time units are nanos , micros , millis , seconds , minutes , hours , half\_days , days , weeks , months , years , decades , centuries , millennia , and eras .

 |

{% set date = "2018-07-14T14:31:30+0530"|strtotime("yyyy-MM-dd'T'HH:mm:ssZ") %} {{ date }} {{ date|plus\_time(5, "days") }}2018-07-14 14:31:30 2018-07-19 14:31:30

pprint[](https://developers.hubspot.com/docs/cms/hubl/filters#pprint)
---------------------------------------------------------------------

Pretty print a variable. This prints the type of variable and other info that is useful for debugging.

{% set this\_var ="Variable that I want to debug" %} {{ this\_var|pprint }}(String: Variable that I want to debug)

random[](https://developers.hubspot.com/docs/cms/hubl/filters#random)
---------------------------------------------------------------------

Return a random item from the sequence.

**Please note:** when using this filter, the page will be [prerendered](/docs/cms/developer-reference/cdn/prerendering) periodically rather than every time the page content is updated. This means that the filtered content will not be updated on every page reload.

This may not be an issue for certain types of content, such as displaying a random list of blog posts. However, if you need content to change randomly on every page load, you should instead use JavaScript to randomize the content client-side.

{% for content in contents|random %} <div class="post-item">Post item markup</div> {% endfor %}<div class="post-item">Random post</div>

regex\_replace[](https://developers.hubspot.com/docs/cms/hubl/filters#regex-replace)
------------------------------------------------------------------------------------

Searches for a regex pattern and replaces with a sequence of characters. The first argument is a RE2-style regex pattern, the second is the replacement string.

Information on the RE2 regex syntax can be found [here](https://github.com/google/re2/wiki/Syntax).

{{ "contact-us-2"|regex\_replace("\[^a-zA-Z\]", "") }} contactus

reject[](https://developers.hubspot.com/docs/cms/hubl/filters#reject)
---------------------------------------------------------------------

Filters a sequence of objects by applying an [expression test](/docs/cms/hubl/operators-and-expression-tests?hsLang=en) to the object and rejecting the ones with the test succeeding.

| Parameter | Description |
| --- | --- |
| 
`exp_text`

 | 

The expression test to apply to the object.

 |

{% set some\_numbers = \[10, 12, 13, 3, 5, 17, 22\] %} {{ some\_numbers|reject("even") }}\[13, 3, 5, 17\]

rejectattr[](https://developers.hubspot.com/docs/cms/hubl/filters#rejectattr)
-----------------------------------------------------------------------------

Filters a sequence of objects by applying a test to an attribute of an object and rejecting the ones with the test succeeding. 

| Parameter | Description |
| --- | --- |
| 
`attribute_name`

Required



 | 

Specifies the attribute to select. You can access nested attributes using dot notation.

 |
| 

`exp_test`

Optional



 | 

The expression to test

 |
| 

`val`

Optional



 | 

Value to test against.

 |

{% for content in contents|rejectattr("post\_list\_summary\_featured\_image") %} <div class="post-item"> {% if content.post\_list\_summary\_featured\_image %} <div class="hs-featured-image-wrapper"> <a href="{{content.absolute\_url}}" title="" class="hs-featured-image-link"> <img src="{{ content.post\_list\_summary\_featured\_image }}" class="hs-featured-image"> </a> </div> {% endif %} {{ content.post\_list\_content|safe }} </div> {% endfor %}<div class="post-item">Post with no featured image</div> <div class="post-item">Post with no featured image</div> <div class="post-item">Post with no featured image</div>

render[](https://developers.hubspot.com/docs/cms/hubl/filters#render)
---------------------------------------------------------------------

Render strings containing HubL early so that the output can be passed into other filters.

{{ personalization\_token("contact.lastname", "default value")|render|lower }} mclaren

replace[](https://developers.hubspot.com/docs/cms/hubl/filters#replace)
-----------------------------------------------------------------------

Replace all instances of a substring with a new one. 

| Parameter | Description |
| --- | --- |
| 
`old`

Required



 | 

The substring that should be replaced.

 |
| 

`new`

Required



 | 

Replacement string.

 |
| 

`count`

Optional



 | 

If provided, only the firstcount occurrences are replaced.

 |

{% if topic %} <h3>Posts about {{ page\_meta.html\_title|replace("Blog | ", "") }}</h3> {% endif %} <h3>Posts about topic name</h3>

reverse[](https://developers.hubspot.com/docs/cms/hubl/filters#reverse)
-----------------------------------------------------------------------

Reverse the object or return an iterator the iterates over it the other way round. To reverse a list use [.reverse()](/docs/cms/hubl/functions#reverse)

{% set nums = \[1, 2, 3, 4, 5, 6, 7, 8, 9, 10\] %} {% for num in nums|reverse %} {{ num }} {% endfor %}10 9 8 7 6 5 4 3 2 1

root[](https://developers.hubspot.com/docs/cms/hubl/filters#root)
-----------------------------------------------------------------

Calculates the square root of a value.

| Parameter | Description |
| --- | --- |
| 
`nth_root`

Optional



 | 

Calculate the nth root of a number.

 |

{{ 16|root }} {{ 625|root(4) }}4 5

round[](https://developers.hubspot.com/docs/cms/hubl/filters#round)
-------------------------------------------------------------------

Round the number to a given precision.

| Parameter | Description |
| --- | --- |
| 
`precision`

Optional



 | 

Specifies the precision of the rounding.

 |
| 

`rounding_method`

Optional



 | 

Options include common round either up or down (default); ceil always rounds up; floor always rounds down.

If you don’t specify a method common is used.

 |

{{ 52.5|round }} {{ 52.5|round(0, "floor") }}53 52

safe[](https://developers.hubspot.com/docs/cms/hubl/filters#safe)
-----------------------------------------------------------------

Mark the value as safe which means that in an environment with automatic escaping enabled this variable will not be escaped.

{{ content.post\_list\_content|safe }} <p>HTML post content that is not escaped. </p>

sanitize\_html[](https://developers.hubspot.com/docs/cms/hubl/filters#sanitize-html)
------------------------------------------------------------------------------------

Sanitizes the content of an HTML input for the output of rich text content. Accepts a string, then strips HTML tags that are not allowed. Use this filter for HubL variables that are used in HTML that should allow safe HTML.

When using this filter, you can include the following parameters for allowing specific types of HTML tags: `FORMATTING`, `BLOCKS`, `STYLES`, `LINKS`, `TABLES`, `IMAGES`. For example, `sanitize_html(IMAGES)`.

Using `sanitize_html` will include all parameters in the filter.

You can also include a `STRIP` parameter to strip all HTML. All content is run through `escape_jinjava` as well to prevent nested interpretation.

{% set escape\_string = "This <br> <div>markup is <img src='test.com/image'> <span>printed</span> as text.</div>" %} {{ escape\_string|sanitize\_html("IMAGES") }}This markup is <img src="test.com/image"> printed as text.</div>

select[](https://developers.hubspot.com/docs/cms/hubl/filters#select)
---------------------------------------------------------------------

Filters a sequence of objects by applying a test to the object and only selecting the ones with the test succeeding.

| Parameter | Description |
| --- | --- |
| 
`exp_text`

 | 

The expression test to apply to the object.

 |

{% set some\_numbers = \[10, 12, 13, 3, 5, 17, 22\] %} {{ some\_numbers|select("even") }}\[10, 12, 22\]

selectattr[](https://developers.hubspot.com/docs/cms/hubl/filters#selectattr)
-----------------------------------------------------------------------------

Filters a sequence of objects by applying a test to an attribute of an object and only selecting the ones with the test succeeding.

| Parameter | Description |
| --- | --- |
| 
`attribute_name`

Required



 | 

Specifies the attribute to select. You can access nested attributes using dot notation.

 |
| 

`exp_test`

Optional



 | 

The expression to test

 |
| 

`val`

Optional



 | 

Value to test against.

 |

{% for content in contents|selectattr("post\_list\_summary\_featured\_image") %} <div class="post-item"> {% if content.post\_list\_summary\_featured\_image %} <div class="hs-featured-image-wrapper"> <a href="{{content.absolute\_url}}" title="" class="hs-featured-image-link"> <img src="{{ content.post\_list\_summary\_featured\_image }}" class="hs-featured-image"> </a> </div> {% endif %} {{ content.post\_list\_content|safe }} </div> {% endfor %}<div class="post-item"> <div class="hs-featured-image-wrapper"> <a href="http://blog.hubspot.com/marketing/how-to-get-a-job" title="" class="hs-featured-image-link"> <img src="//cdn2.hubspot.net/hub/53/hubfs/00-Blog-Related\_Images/landing-a-job-featured-image.png?t=1431452322770&width=761" class="hs-featured-image"> </a> </div> Post with featured image </div>

shuffle[](https://developers.hubspot.com/docs/cms/hubl/filters#shuffle)
-----------------------------------------------------------------------

Randomizes the order of iteration through a sequence. The example below shuffles a standard blog loop.

**Please note:** when using this filter, the page will be [prerendered](/docs/cms/developer-reference/cdn/prerendering) periodically rather than every time the page content is updated. This means that the filtered content will not be updated on every page reload.

This may not be an issue for certain types of content, such as displaying a random list of blog posts. However, if you need content to change randomly on every page load, you should instead use JavaScript to randomize the content client-side.

{% for content in contents|shuffle %} <div class="post-item">Markup of each post</div> {% endfor %}<div class="post-item">Markup of each post 5</div> <div class="post-item">Markup of each post 3</div> <div class="post-item">Markup of each post 1</div> <div class="post-item">Markup of each post 2</div> <div class="post-item">Markup of each post 4</div>

slice[](https://developers.hubspot.com/docs/cms/hubl/filters#slice)
-------------------------------------------------------------------

Slice an iterator and return a list of lists containing those items. The first parameter specifies how many items will be sliced, and the second parameter specifies characters to fill in empty slices.

| Parameter | Description |
| --- | --- |
| 
`slices`

Required



 | 

How many items will be sliced.

 |
| 

`filler`

Required



 | 

Specifies characters to fill in empty slices. 

 |

{% set items = \["laptops", "tablets", "smartphones", "smart watches", "TVs"\] %} <div class="columwrapper"> {% for column in items|slice(3," ") %} <ul class="column-{{ loop.index }}"> {% for item in column %} <li>{{ item }}</li> {% endfor %} </ul> {% endfor %} </div><div class="columwrapper"> <ul class="column-1"> <li>laptops</li> <li>tablets</li> <li>smartphones</li> </ul> <ul class="column-2"> <li>smart watches</li> <li>TVs</li> <li>&nbsp;</li> </ul> </div>

sort[](https://developers.hubspot.com/docs/cms/hubl/filters#sort)
-----------------------------------------------------------------

Sorts an iterable. This filter requires all parameters to sort by an attribute in HubSpot. The first parameter is a boolean to reverse the sort order. The second parameter determines whether or not the sorting is case sensitive. And the final parameter specifies an attribute to sort by. In the example below, posts from a blog are rendered and alphabetized by name.

| Parameter | Description |
| --- | --- |
| 
`reverse`

Required



 | 

Boolean value to reverse the sort order.

 |
| 

`case_sensitive`

Required



 | 

Boolean value that determines if the sorting is case sensitive. 

 |
| 

`attribute`

Required



 | 

Attribute to sort by. Omit when sorting a list.

 |

{% set my\_posts = blog\_recent\_posts("default", limit=5) %} {% for item in my\_posts|sort(False, False, "name") %} {{ item.name }}<br> {% endfor %}A post<br> B post<br> C post<br> D post<br> E post<br>

split[](https://developers.hubspot.com/docs/cms/hubl/filters#split)
-------------------------------------------------------------------

Splits the input string into a list on the given separator. The first parameter specifies the separator to split the variable by. The second parameter determines how many times the variable should be split. Any remaining items would remained group. In the example below, a string of names is split at the ";" for the first 4 names.

| Parameter | Description |
| --- | --- |
| 
`character_to_split_by`

Required



 | 

Specifies the separator to split the variable by.

 |
| 

`number_of_splits`

Optional



 | 

Determines how many times the variable should be split. Any remaining items would remain grouped.

 |

{% set string\_to\_split = "Stephen; David; Cait; Nancy; Mike; Joe; Niall; Tim; Amanda" %} {% set names = string\_to\_split|split(";", 4) %} <ul> {% for name in names %} <li>{{ name }}</li> {% endfor %} </ul><ul> <li>Stephen</li> <li>David</li> <li>Cait</li> <li>Nancy; Mike; Joe; Niall; Tim; Amanda</li> </ul>

string[](https://developers.hubspot.com/docs/cms/hubl/filters#string)
---------------------------------------------------------------------

Converts a different variable type to a string. In the example below, a integer is converted into a string (pprint is used to confirm the change in variable type).

{% set number\_to\_string = 45 %} {{ number\_to\_string|string|pprint }}(String: 45)

striptags[](https://developers.hubspot.com/docs/cms/hubl/filters#striptags)
---------------------------------------------------------------------------

Strip SGML/XML tags and replace adjacent whitespace by one space. This filter can be used to remove any HTML tags from a variable.

{% set some\_html = "<div><strong>Some text</strong></div>" %} {{ some\_html|striptags }} some text

strtotime[](https://developers.hubspot.com/docs/cms/hubl/filters#strtotime)
---------------------------------------------------------------------------

Converts a datetime string and a datetime format into a datetime object.

| Parameter | Description |
| --- | --- |
| 
`datetimeFormat`

Required



 | 

[Date and time patterns.](https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html)

 |

{{ "2018-07-14T14:31:30+0530"|strtotime("yyyy-MM-dd'T'HH:mm:ssZ")|unixtimestamp }} 1531558890000

sum[](https://developers.hubspot.com/docs/cms/hubl/filters#sum)
---------------------------------------------------------------

Adds numeric values in a sequence. The first parameter can specify an optional attribute and the second parameter sets a value to return if there is nothing in the variable to sum.

| Parameter | Description |
| --- | --- |
| 
`attribute`

Optional



 | 

Attribute to sum.

 |
| 

`return_if_nothing`

Optional



 | 

Value to return if there is nothing in the variable to sum.

 |

{% set sum\_this = \[1, 2, 3, 4, 5\] %} {{ sum\_this|sum }} Total: {{ items|sum(attribute="price:") }}15 Total: 20

symmetric\_difference[](https://developers.hubspot.com/docs/cms/hubl/filters#symmetric-difference)
--------------------------------------------------------------------------------------------------

This filter returns the symmetric difference of two sets or lists. The list returned from the filter contains all unique elements that are in the first list but not the second, or are in the second list but not the first

| Parameter | Description |
| --- | --- |
| 
`list`

Required



 | 

The second list to compare to for use in finding the symmetric difference with the original list.

 |

{{ \[1, 2, 3\]|symmetric\_difference(\[2, 3, 4, 5\]) }}\[1, 4, 5\]

title[](https://developers.hubspot.com/docs/cms/hubl/filters#title)
-------------------------------------------------------------------

Return a titlecased version of the value. I.e. words will start with uppercase letters, all remaining characters are lowercase.

{% text "my\_title" label="Enter a title", value="My title should be titlecase", export\_to\_template\_context=True %} {{ widget\_data.my\_title.value|title }}My Title Should Be Titlecase

tojson[](https://developers.hubspot.com/docs/cms/hubl/filters#tojson)
---------------------------------------------------------------------

Writes an object as a JSON string.

{% for content in contents %} {{ content.blog\_post\_author|tojson }} {% endfor %}{ "portalId":1234567, "id":12312253109, "created":1566413741989, "updated":1566414012799, "deletedAt":0, "fullName":"Sample User", "email":"sampleUser@example.com", "userId":null, "username":null, "slug":"sample-user", "jsonBody":{ "avatar":"https://app.hubspot.com/settings/avatar/109d6874a0cb066c1c7263ac5df6ce7a", "bio":"Sample Bio", "facebook":"", "linkedin":"", "twitter":"", "website":"https://www.hubspot.com" }, "bio":"Sample Bio", "facebook":"", "linkedin":"", "avatar":"https://app.hubspot.com/settings/avatar/109d6874a0cb066c1c7263ac5df6ce7a", "gravatarUrl":"https://app.hubspot.com/settings/avatar/108bb5ac667ded34796271437dfe8d58", "twitterUsername":"", "hasSocialProfiles":false, "website":"https://www.hubspot.com", "twitter":"", "displayName":"Sample User" }

trim[](https://developers.hubspot.com/docs/cms/hubl/filters#trim)
-----------------------------------------------------------------

Strips leading and trailing whitespace. HubSpot already trims whitespace from markup, but this filter is documented for the sake of comprehensiveness.

{{ " remove whitespace " }} {{ " remove whitespace "|trim }} remove whitespace remove whitespace

truncate[](https://developers.hubspot.com/docs/cms/hubl/filters#truncate)
-------------------------------------------------------------------------

Cuts off text after a certain number of characters. The default is 255. Please note that HTML characters are included in this count. The length is specified with the first parameter which defaults to 255. If the second parameter is true the filter will cut the text at length. Otherwise it will discard the last word. If the text was in fact truncated it will append an ellipsis sign ("..."). If you want a different ellipsis sign than "..." you can specify it using the third parameter.

Use this table to describe parameters / fields
| Parameter | Description |
| --- | --- |
| 
`number_of_characters`

Required



 | 

Number of characters to truncate the text by. Default is 255.

 |
| 

`breakword`

Optional



 | 

Boolean value. If true, the filter will cut the text at length. If false, it will discard the last word. 

 |
| 

`end`

Optional



 | 

Override the default '...' trailing characters after the truncation.

 |

{{ "I only want to show the first sentence. Not the second."|truncate(40) }} {{ "I only want to show the first sentence. Not the second."|truncate(35, True, "..........") }}I only want to show the first sentence. I only want to show the first sente..........

truncatehtml[](https://developers.hubspot.com/docs/cms/hubl/filters#truncatehtml)
---------------------------------------------------------------------------------

Truncates a given string, respecting html markup (i.e. will properly close all nested tags). This will prevent a tag from remaining open after truncation. HTML characters do not count towards the character total. This filter has a length parameter and a truncation symbol parameter. There is a third boolean parameter that specifies whether words will be broken at length. This parameter is false by default in order to preserve the length of words. If using only one of the optional parameters, use keyword arguments, such as truncatehtml(70, breakwords = false).

| Parameter | Description |
| --- | --- |
| 
`number_of_characters`

Required



 | 

Number of characters to truncate the text by. Default is 255.

 |
| 

`end`

Optional



 | 

Override the default '...' trailing characters after the truncation.

 |
| 

`breakword`

Optional



 | 

Boolean value. If true, the filter will cut the text at length. If false, it will discard the last word. 

 |

{% set html\_text = "<p>I want to truncate this text without breaking my HTML<p>" %} {{ html\_text|truncatehtml(28, "..." , false) }}<p>I want to truncate this..</p>

unescape\_html[](https://developers.hubspot.com/docs/cms/hubl/filters#unescape-html)
------------------------------------------------------------------------------------

 Converts text with HTML-encoded entities to their Unicode equivalents.

{% set escape\_string = "me &amp; you" %} {{ escape\_string|unescape\_html }}me & you

union[](https://developers.hubspot.com/docs/cms/hubl/filters#union)
-------------------------------------------------------------------

This filter returns the union of two sets or lists. The list returned from the filter contains all unique elements that are in either list.

| Parameter | Description |
| --- | --- |
| 
`list`

Required



 | 

The second list to union with the original list.

 |

{{ \[1, 2, 3\]|union(\[2, 3, 4, 5\]) }}\[1, 2, 3, 4, 5\]

unique[](https://developers.hubspot.com/docs/cms/hubl/filters#unique)
---------------------------------------------------------------------

This filter extracts a unique set from a sequence or dict of objects. When filtering a dict, such as a list of posts returned by a function, you can specify which attribute is used to deduplicate items in the dict.

| Parameter | Description |
| --- | --- |
| 
`attr`

Optional



 | 

Specifies the attribute that should be used when filtering a dict value

 |

{% set my\_sequence = \["one", "one", "two", "three" \] %} {{ my\_sequence|unique }}\[one, two, three\]

unixtimestamp[](https://developers.hubspot.com/docs/cms/hubl/filters#unixtimestamp)
-----------------------------------------------------------------------------------

This filter converts a datetime object into a unix timestamp.

**Please note:** it is strongly recommended to use this filter only with variables that return a date. If a date is not passed, the filter will be used on the current date, which may result in inaccurate date information being displayed on your page.

{{ local\_dt }} {{ local\_dt|unixtimestamp }}2017-01-30 17:11:44 1485814304000

upper[](https://developers.hubspot.com/docs/cms/hubl/filters#upper)
-------------------------------------------------------------------

Convert a value to all uppercase letters.

{% text "text" value="text to make uppercase", export\_to\_template\_context=True %} {{ widget\_data.text.value|upper }}TEXT TO MAKE UPPERCASE

urlencode[](https://developers.hubspot.com/docs/cms/hubl/filters#urlencode)
---------------------------------------------------------------------------

Escapes and URL encodes a string using UTF-8 formatting. Accepts both dictionaries and regular strings as well as pairwise iterables.

{% text "encode" value="Escape & URL encode this string", label="Enter slug", export\_to\_template\_context=True %} {{ widget\_data.encode.value|urlencode }}Escape+%26+URL+encode+this+string

urldecode[](https://developers.hubspot.com/docs/cms/hubl/filters#urldecode)
---------------------------------------------------------------------------

Decodes encoded URL strings back to the original URL. Accepts both dictionaries and regular strings as well as pairwise iterables.

{% text "decode" value="Escape+%26+URL+decode+this+string", label="Enter slug", export\_to\_template\_context=True %} {{ widget\_data.decode.value|urldecode }}Escape & URL encode this string

urlize[](https://developers.hubspot.com/docs/cms/hubl/filters#urlize)
---------------------------------------------------------------------

Converts URLs in plain text into clickable links. If you pass the filter an additional integer it will shorten the urls to that number. The second parameter is a boolean that dictates whether the link is rel="no follow". The final parameter lets you specify whether the link will open in a new tab.

| Parameter | Description |
| --- | --- |
| 
`shorten_text`

Optional



 | 

Integer that will shorten the urls to desired number.

 |
| 

`no_follow`

Optional



 | 

Boolean value to indicate whether the link is rel="no follow".

 |
| 

`target="_blank"`

Optional



 | 

Specifies whether the link will open in a new tab.

 |

{{ "http://hubspot.com/"|urlize }} {{ "http://hubspot.com/"|urlize(10,true) }} {{ "http://hubspot.com/"|urlize("",true) }} {{ "http://hubspot.com/"|urlize("",false,target="\_blank") }}<a href="//hubspot.com/">http://hubspot.com/</a> <a href="//hubspot.com/" rel="nofollow">http://...</a> <a href="//hubspot.com/" rel="nofollow">http://hubspot.com/</a> <a href="//hubspot.com/" target="\_blank">http://hubspot.com/</a>

wordcount[](https://developers.hubspot.com/docs/cms/hubl/filters#wordcount)
---------------------------------------------------------------------------

Count the number of words in a string.

If the string contains HTML, use the striptags filter to get an accurate count.

{% set count\_words = "Count the number of words in this variable" %} {{ count\_words|wordcount }}8

wordwrap[](https://developers.hubspot.com/docs/cms/hubl/filters#wordwrap)
-------------------------------------------------------------------------

Causes words to wrap at a given character count. This works best in a <pre> because HubSpot strips whitespace by default.

| Parameter | Description |
| --- | --- |
| 
`character_count`

Required



 | 

Number of characters to wrap the content at.

 |

{% set wrap\_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam efficitur, ipsum non sagittis euismod, ex risus rhoncus lectus, vel maximus leo enim sit amet dui. Ut laoreet ultricies quam at fermentum." %} {{ wrap\_text|wordwrap(10) }}Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam efficitur, ipsum non sagittis euismod, ex risus rhoncus lectus, vel maximus leo enim sit amet dui. Ut laoreet ultricies quam at fermentum.

xmlattr[](https://developers.hubspot.com/docs/cms/hubl/filters#xmlattr)
-----------------------------------------------------------------------

Create an HTML/XML attribute string, based on the items in a dict. All values that are neither none  
nor undefined are automatically escaped. It automatically prepends a space in front of the item if the filter returned something unless the first parameter is false.

| Parameter | Description |
| --- | --- |
| 
`autospace`

Required



 | 

Boolean value that will automatically prepend a space in front of the item unless set to false.

 |

{% set html\_attributes = {"class": "bold", "id": "sidebar"} %} <div {{ html\_attributes|xmlattr }}></div><div class="bold" id="sidebar"></div>

* * *

Share your feedback[](https://developers.hubspot.com/docs/cms/hubl/filters#page-feedback)
-----------------------------------------------------------------------------------------

Was this article helpful? Yes No

Thanks for letting us know. How would you describe this article?

 Inaccurate: it doesn’t reflect what I see in the product

 Unclear: it’s difficult to understand

 Missing information: it’s not comprehensive enough

 Irrelevant: it doesn’t match what I searched for

Great! Is there anything we could change to make it even more helpful? Is there anything we could change to make this article helpful?

 Allow HubSpot to contact me about my documentation feedback.

Email address

Only used if we need clarification on your feedback.

 

Thank you for your feedback, it means a lot to us.

Sorry this feedback form requires JavaScript to function.

This form is used for documentation feedback only. Learn how to [get help with HubSpot](https://knowledge.hubspot.com/account/get-help-with-hubspot).