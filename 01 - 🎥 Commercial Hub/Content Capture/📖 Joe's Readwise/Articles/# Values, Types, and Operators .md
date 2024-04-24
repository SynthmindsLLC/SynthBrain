# Values, Types, and Operators

![rw-book-cover](https://rdl.ink/render/https%3A%2F%2Feloquentjavascript.net%2F01_values.html)

## Metadata
- Author: [[eloquentjavascript.net]]
- Date: None
- Full Title: Values, Types, and Operators
- Category: #articles
- Summary: This text discusses values, types, and operators in programming. It is written by eloquentjavascript.net. The content is likely about understanding fundamental concepts in programming.
- URL: https://eloquentjavascript.net/01_values.html

## Highlights
- *Bits* are any kind of two-valued things, usually described as zeros and ones. Inside the computer, they take forms such as a high or low electrical charge, a strong or weak signal, or a shiny or dull spot on the surface of a CD. Any piece of discrete information can be reduced to a sequence of zeros and ones and thus represented in bits. ([View Highlight](https://read.readwise.io/read/01hv7w4p3p6h9b2q29yv1q7q72))
- A typical modern computer has more than 100 billion bits in its volatile data storage (working memory). Nonvolatile storage (the hard disk or equivalent) tends to have yet a few orders of magnitude more. ([View Highlight](https://read.readwise.io/read/01hv7w6cxsw50hrmj8avac2e61))
- To be able to work with such quantities of bits without getting lost, we separate them into chunks that represent pieces of information. In a JavaScript environment, those chunks are called *values*. ([View Highlight](https://read.readwise.io/read/01hv7w6zs9kw2hmp43gf1b23f9))
- To create a value, you must merely invoke its name. This is convenient. You don’t have to gather building material for your values or pay for them. You just call for one, and *whoosh*, you have it. ([View Highlight](https://read.readwise.io/read/01hv7w7vjr52yakms1m9qrcga8))
- As soon as you no longer use a value, it will dissipate, leaving behind its bits to be recycled as building material for the next generation of values. ([View Highlight](https://read.readwise.io/read/01hv7w8e2cqf0ra0ekqky04pzq))
- Values of the *number* type are, unsurprisingly, numeric values. ([View Highlight](https://read.readwise.io/read/01hv7w8zxr6zmhfeq7df130hwx))
- JavaScript uses a fixed number of bits, 64 of them, to store a single number value. ([View Highlight](https://read.readwise.io/read/01hv7w9w9n64ypnpnsvp4m22a5))
- Computer memory used to be much smaller, and people tended to use groups of 8 or 16 bits to represent their numbers. It was easy to accidentally *overflow* such small numbers—to end up with a number that did not fit into the given number of bits. ([View Highlight](https://read.readwise.io/read/01hv7wayrfsrwna67yjasncyj8))
- A bigger issue is representing nonwhole numbers. To do this, some of the bits are used to store the position of the decimal point. ([View Highlight](https://read.readwise.io/read/01hv7wbmhxhq3hec8dzv3s2vzj))
