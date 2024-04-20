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
## New highlights added April 17, 2024 at 5:22 AM
- Fractional numbers are written using a dot ([View Highlight](https://read.readwise.io/read/01hvmqd7kanf0ex5q6t67g8rtd))
- For very big or very small numbers, you may also use scientific notation by adding an *e* (for *exponent*), followed by the exponent of the number ([View Highlight](https://read.readwise.io/read/01hvmqm3qgc917fahx4trkwxxe))
- Calculations with whole numbers (also called *integers*) that are smaller than the aforementioned 9 quadrillion are guaranteed to always be precise. Unfortunately, calculations with fractional numbers are generally not. Just as π (pi) cannot be precisely expressed by a finite number of decimal digits, many numbers lose some precision when only 64 bits are available to store them. ([View Highlight](https://read.readwise.io/read/01hvmqmntrca3vfpjnyzw9m1zj))
- The main thing to do with numbers is arithmetic. Arithmetic operations such as addition or multiplication take two number values and produce a new number from them. ([View Highlight](https://read.readwise.io/read/01hvmqnb4qge2b9b4j97m56s3j))
- The `+` and `*` symbols are called *operators*. ([View Highlight](https://read.readwise.io/read/01hvmqnf40pkjqawt0xrr0e55k))
- Putting an operator between two values will apply it to those values and produce a new value. ([View Highlight](https://read.readwise.io/read/01hvmqnsqtjq39sdh9j66jy2v8))
- For subtraction, there is the `-` operator. Division can be done with the `/` operator. ([View Highlight](https://read.readwise.io/read/01hvmqp9m863my6447rmarrwbv))
- There is one more arithmetic operator, which you might not immediately recognize. The `%` symbol is used to represent the *remainder* operation. ([View Highlight](https://read.readwise.io/read/01hvmqq3gyjz506cbrebvaxegj))
- You’ll also often see this operator referred to as *modulo*. ([View Highlight](https://read.readwise.io/read/01hvmqqggpw2gbc8yfpgncxrmt))
- There are three special values in JavaScript that are considered numbers but don’t behave like normal numbers. The first two are `Infinity` and `-Infinity`, which represent the positive and negative infinities. `Infinity - 1` is still `Infinity`, and so on. Don’t put too much trust in infinity-based computation, though. It isn’t mathematically sound, and it will quickly lead to the next special number: `NaN`. ([View Highlight](https://read.readwise.io/read/01hvmqr3kb797bp1mn0eazx2fz))
- `NaN` stands for “not a number”, even though it *is* a value of the number type. ([View Highlight](https://read.readwise.io/read/01hvmqrbzan1ehpw9kngcq1kgc))
- The next basic data type is the *string*. Strings are used to represent text. ([View Highlight](https://read.readwise.io/read/01hvmqrmx28dcgddwhj2cdtep8))
- They are written by enclosing their content in quotes. ([View Highlight](https://read.readwise.io/read/01hvmqrtfzjccpy0wk5h5f3d3m))
- You can use single quotes, double quotes, or backticks to mark strings, as long as the quotes at the start and the end of the string match. ([View Highlight](https://read.readwise.io/read/01hvmqrzasc54jbym336t4stxk))
- You can imagine how putting quotes between quotes might be hard, since they will look like the end of the string. ([View Highlight](https://read.readwise.io/read/01hvmqskbjegv7q35j5g2hy346))
- *Newlines* (the characters you get when you press enter) can be included only when the string is quoted with backticks (`` ` ``). ([View Highlight](https://read.readwise.io/read/01hvmqssfs18d9bs9myfsnczwr))
- To make it possible to include such characters in a string, the following notation is used: a backslash (`\`) inside quoted text indicates that the character after it has a special meaning. This is called *escaping* the character. ([View Highlight](https://read.readwise.io/read/01hvmqt54mnyzhwksyn9s3j5rh))
- A quote that is preceded by a backslash will not end the string but be part of it. When an `n` character occurs after a backslash, it is interpreted as a newline. ([View Highlight](https://read.readwise.io/read/01hvmqtpywvpjya2m4gtxtv6p6))
- a `t` after a backslash means a tab character. ([View Highlight](https://read.readwise.io/read/01hvmqv1dvn1zvb1wj94sbm8ev))
- There are, of course, situations where you want a backslash in a string to be just a backslash, not a special code. If two backslashes follow each other, they will collapse together, and only one will be left in the resulting string value. ([View Highlight](https://read.readwise.io/read/01hvmqvw5q0q8695c8zg4hcnz6))
- This is how the string “*A newline character is written like `"`\n`"`.*” can be expressed:
  "A newline character is written like \"\\n\"." ([View Highlight](https://read.readwise.io/read/01hvmqwaj135p18x3nswtxgstm))
- *Unicode* standard. This standard assigns a number to virtually every character you would ever need, including characters from Greek, Arabic, Japanese, Armenian, and so on. If we have a number for every character, a string can be described by a sequence of numbers. And that’s what JavaScript does. ([View Highlight](https://read.readwise.io/read/01hvmqwzjzavmyppkm347fbhby))
- some characters, such as many emoji, take up two “character positions” in JavaScript strings. ([View Highlight](https://read.readwise.io/read/01hvmqxpv0jk0g4w0nget76yyj))
- Strings cannot be divided, multiplied, or subtracted. The `+` operator *can* be used on them, not to add, but to *concatenate*—to glue two strings together. ([View Highlight](https://read.readwise.io/read/01hvmqy81gdk327gd9mx0yg2y9))
- Strings written with single or double quotes behave very much the same—the only difference lies in which type of quote you need to escape inside of them. Backtick-quoted strings, usually called *template literals*, can do a few more tricks. Apart from being able to span lines, they can also embed other values. ([View Highlight](https://read.readwise.io/read/01hvmr03ry20ec5vqeqhftp4z3))
- When you write something inside `${}` in a template literal, its result will be computed, converted to a string, and included at that position. ([View Highlight](https://read.readwise.io/read/01hvmr0gj227vpmbtjv41ykwqr))
- Not all operators are symbols. Some are written as words. ([View Highlight](https://read.readwise.io/read/01hvmr16dg64052a29a7s38v4v))
- the `typeof` operator, which produces a string value naming the type of the value you give it. ([View Highlight](https://read.readwise.io/read/01hvmr1gvf9eqc47kryzr2eakm))
- The other operators shown so far in this chapter all operated on two values, but `typeof` takes only one. Operators that use two values are called *binary* operators, while those that take one are called *unary* operators. The minus operator can be used both as a binary operator and as a unary operator. ([View Highlight](https://read.readwise.io/read/01hvmr2ac8fnxx8dz8ghht6a3x))
- It is often useful to have a value that distinguishes between only two possibilities, like “yes” and “no” or “on” and “off”. For this purpose, JavaScript has a *Boolean* type, which has just two values, true and false, written as those words. ([View Highlight](https://read.readwise.io/read/01hvmr3815ecpkp1h0q60pn8d9))
- The `>` and `<` signs are the traditional symbols for “is greater than” and “is less than”, respectively. They are binary operators. Applying them results in a Boolean value that indicates whether they hold true in this case. ([View Highlight](https://read.readwise.io/read/01hvmr3rnd23sg8ed702c3ysaw))
- Other similar operators are `>=` (greater than or equal to), `<=` (less than or equal to), `==` (equal to), and `!=` (not equal to). ([View Highlight](https://read.readwise.io/read/01hvmr4qfsd707m2a7zwx7v5n4))
- `NaN` is supposed to denote the result of a nonsensical computation, and as such, it isn’t equal to the result of any *other* nonsensical computations. ([View Highlight](https://read.readwise.io/read/01hvmr5grxn6dzydyrh7nc6zqs))
- JavaScript supports three logical operators: *and*, *or*, and *not*. These can be used to “reason” about Booleans. ([View Highlight](https://read.readwise.io/read/01hvmr5tweb7jrkstrwg020zmj))
- The `&&` operator represents logical *and*. It is a binary operator, and its result is true only if both the values given to it are true. ([View Highlight](https://read.readwise.io/read/01hvmr63an8xqc64pwpmgd99hm))
- The `||` operator denotes logical *or*. It produces true if either of the values given to it is true. ([View Highlight](https://read.readwise.io/read/01hvmr6hrq7n85nvz30d2sqx6s))
- *Not* is written as an exclamation mark (`!`). It is a unary operator that flips the value given to it—`!true` produces `false` and `!false` gives `true`. ([View Highlight](https://read.readwise.io/read/01hvmr6vwyznqgwf9nsj7rwtf0))
- *ternary*, operating on three values. It is written with a question mark and a colon, like this:
  console.log(true ? 1 : 2);
  // → 1
  console.log(false ? 1 : 2);
  // → 2 ([View Highlight](https://read.readwise.io/read/01hvmr8tpjkvwwmxpq4hq608g2))
- *conditional* operator (or sometimes just *the ternary operator* since it is the only such operator in the language). ([View Highlight](https://read.readwise.io/read/01hvmr93tbzkjdxraztbvbgxp8))
- The operator uses the value to the left of the question mark to decide which of the two other values to “pick”. If you write `a ? b : c`, the result will be `b` when `a` is true and `c` otherwise. ([View Highlight](https://read.readwise.io/read/01hvmrb3t70ecjvakevx9n77fn))
- There are two special values, written `null` and `undefined`, that are used to denote the absence of a *meaningful* value. They are themselves values, but they carry no information. ([View Highlight](https://read.readwise.io/read/01hvmrbjsmvs8ygqs8q65q00y8))
- When an operator is applied to the “wrong” type of value, JavaScript will quietly convert that value to the type it needs, using a set of rules that often aren’t what you want or expect. This is called *type coercion*. ([View Highlight](https://read.readwise.io/read/01hvmrdcnxhjgrktjw2b2hgq64))
## New highlights added April 18, 2024 at 5:35 AM
- When you do *not* want any type conversions to happen, there are two additional operators: `===` and `!==`. The first tests whether a value is *precisely* equal to the other, and the second tests whether it is not precisely equal. Thus `"" === false` is false as expected. ([View Highlight](https://read.readwise.io/read/01hvqaxkrr6jbfhcnprvgax3s0))
- The logical operators `&&` and `||` handle values of different types in a peculiar way. They will convert the value on their left side to Boolean type in order to decide what to do, but depending on the operator and the result of that conversion, they will return either the *original* left-hand value or the right-hand value ([View Highlight](https://read.readwise.io/read/01hvqaz93jtgvrwqsevjjyv2ex))
- The `||` operator, for example, will return the value to its left when that value can be converted to true and will return the value on its right otherwise. This has the expected effect when the values are Boolean and does something analogous for values of other types. ([View Highlight](https://read.readwise.io/read/01hvqb0q1e5sfvc62y9bz66x2w))
- We can use this functionality as a way to fall back on a default value. If you have a value that might be empty, you can put `||` after it with a replacement value. If the initial value can be converted to false, you’ll get the replacement instea ([View Highlight](https://read.readwise.io/read/01hvqb1px1j3hp8abhwa0zndb3))
- The rules for converting strings and numbers to Boolean values state that `0`, `NaN`, and the empty string (`""`) count as `false`, while all the other values count as `true`. That means `0 || -1` produces `-1`, and `"" || "!?"` yields `"!?"`. ([View Highlight](https://read.readwise.io/read/01hvqb2af15wex67f5p8n60a1f))
- The `??` operator resembles `||`, but returns the value on the right only if the one on the left is null or undefined, not if it is some other value that can be converted to `false`. Often, this is preferable to the behavior of `||`. ([View Highlight](https://read.readwise.io/read/01hvqb3bnvqa4e5t5msmkdyy7x))
- The `&&` operator works similarly but the other way around. When the value to its left is something that converts to false, it returns that value, and otherwise it returns the value on its right. ([View Highlight](https://read.readwise.io/read/01hvqb45heh19cefwcbsyrevh3))
