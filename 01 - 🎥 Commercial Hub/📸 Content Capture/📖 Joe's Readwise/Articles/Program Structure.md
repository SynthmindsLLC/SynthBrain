# Program Structure

![rw-book-cover](https://eloquentjavascript.net/img/chapter_picture_2.jpg)

## Metadata
- Author: [[eloquentjavascript.net]]
- Date: None
- Full Title: Program Structure
- Category: #articles
- Summary: A program consists of expressions and statements executed from top to bottom. Functions encapsulate program pieces and can produce values when called. Loops and conditional execution help control program flow and make tasks more efficient.
- URL: https://eloquentjavascript.net/02_program_structure.html

## Highlights
- fragment of code that produces a value is called an *expression*. Every value that is written literally (such as `22` or `"psychoanalysis"`) is an expression. An expression between parentheses is also an expression, as is a binary operator applied to two expressions or a unary operator applied to one. ([View Highlight](https://read.readwise.io/read/01hwkmary2kjc59gcym5mznws1))
- Expressions can contain other expressions in a way similar to how subsentences in human languages are nested—a subsentence can contain its own subsentences, and so on. This allows us to build expressions that describe arbitrarily complex computations. ([View Highlight](https://read.readwise.io/read/01hwkmdj1cczywbp6pt6rzfema))
- A program is a list of statements. ([View Highlight](https://read.readwise.io/read/01hwkmdy0v7zmp8qdfy2yjyc8z))
- It may display something on the screen, as with `console.log`, or change the state of the machine in a way that will affect the statements that come after it. These changes are called *side effects*. The statements in the previous example just produce the values `1` and `true` and then immediately throw them away. This leaves no impression on the world at all. When you run this program, nothing observable happens. ([View Highlight](https://read.readwise.io/read/01hwkmeyqf85q0tggspr5k3vm3))
- In some cases, JavaScript allows you to omit the semicolon at the end of a statement. In other cases, it has to be there, or the next line will be treated as part of the same statement. ([View Highlight](https://read.readwise.io/read/01hwkmfbb54267mwmkx7ngr5dd))
- To catch and hold values, JavaScript provides a thing called a *binding*, or *variable* ([View Highlight](https://read.readwise.io/read/01hwkmg4fyx3e2ndw59p9cbs71))
- That gives us a second kind of statement. The special word (*keyword*) `let` indicates that this sentence is going to define a binding. It is followed by the name of the binding and, if we want to immediately give it a value, by an `=` operator and an expression. ([View Highlight](https://read.readwise.io/read/01hwkmgkx2rnnrhannbgs9hpp4))
- After a binding has been defined, its name can be used as an expression. The value of such an expression is the value the binding currently holds. ([View Highlight](https://read.readwise.io/read/01hwkmh1wbm6fewaj36f3x3s37))
- You should imagine bindings as tentacles rather than boxes. They do not *contain* values; they *grasp* them—two bindings can refer to the same value. ([View Highlight](https://read.readwise.io/read/01hwkmj72xkzs442gejv2rasay))
- When you need to remember something, you either grow a tentacle to hold on to it or reattach one of your existing tentacles to it. ([View Highlight](https://read.readwise.io/read/01hwkmjgzgwp1z6ex1nhdddy4t))
- The words `var` and `const` can also be used to create bindings, in a similar fashion to `let`:
  var name = "Ayda";
  const greeting = "Hello ";
  console.log(greeting + name);
  // → Hello Ayda ([View Highlight](https://read.readwise.io/read/01hwkmm37e4r9eez8a3ws1ad28))
- The word `const` stands for *constant*. It defines a constant binding, which points at the same value for as long as it lives. This is useful for bindings that just give a name to a value so that you can easily refer to it later. ([View Highlight](https://read.readwise.io/read/01hwkmn9e0r8rpxr58brym3aag))
- A binding name may include dollar signs (`$`) or underscores (`_`) but no other punctuation or special characters. ([View Highlight](https://read.readwise.io/read/01hwkmnz1tvca6mbc2ty3qsayc))
- Words with a special meaning, such as `let`, are *keywords*, and may not be used as binding names. There are also a number of words that are “reserved for use” in future versions of JavaScript, which also can’t be used as binding names. The full list of keywords and reserved words is rather long:
  break case catch class const continue debugger default
  delete do else enum export extends false finally for
  function if implements import interface in instanceof let
  new package private protected public return static super
  switch this throw true try typeof var void while with yield ([View Highlight](https://read.readwise.io/read/01hwkmpr8w8xxm4xs5d5crjnfb))
- The collection of bindings and their values that exist at a given time is called the *environment*. ([View Highlight](https://read.readwise.io/read/01hwkmqqzgpc4bfax76exew1hw))
- A lot of the values provided in the default environment have the type *function*. A function is a piece of program wrapped in a value. Such values can be *applied* in order to run the wrapped program ([View Highlight](https://read.readwise.io/read/01hwkmrx9s9dxqxnydj1ekc02n))
- Executing a function is called *invoking*, *calling*, or *applying* it. You can call a function by putting parentheses after an expression that produces a function value. Usually you’ll directly use the name of the binding that holds the function. The values between the parentheses are given to the program inside the function. In the example, the `prompt` function uses the string that we give it as the text to show in the dialog box. Values given to functions are called *arguments*. Different functions might need a different number or different types of arguments. ([View Highlight](https://read.readwise.io/read/01hwkmt1kpnpt054mbzz41whdh))
- When a function produces a value, it is said to *return* that value. Anything that produces a value is an expression in JavaScript, which means that function calls can be used within larger expressions. ([View Highlight](https://read.readwise.io/read/01hwkmxd12mp7k17v9kc1v23rv))
- When your program contains more than one statement, the statements are executed as though they were a story, from top to bottom. ([View Highlight](https://read.readwise.io/read/01hwkmy4g5j211dkzd6s5b0ddb))
- Not all programs are straight roads. We may, for example, want to create a branching road where the program takes the proper branch based on the situation at hand. This is called *conditional execution*. ([View Highlight](https://read.readwise.io/read/01hwkmzn2ybx9h45ptde5ay9az))
- Conditional execution is created with the `if` keyword in JavaScript. In the simple case, we want some code to be executed if, and only if, a certain condition holds. ([View Highlight](https://read.readwise.io/read/01hwkmzzh2fx0wpdawcey1t7t2))
