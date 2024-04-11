# Introduction

![rw-book-cover](https://eloquentjavascript.net/img/chapter_picture_00.jpg)

## Metadata
- Author: [[eloquentjavascript.net]]
- Date: None
- Full Title: Introduction
- Category: #articles
- Summary: Programming is a way to make computers do new things. JavaScript is a common language used in programming. Learning to program involves writing and reading code.
- URL: https://eloquentjavascript.net/00_intro.html

## Highlights
- *Programming* is the act of constructing a *program*—a set of precise instructions telling a computer what to do. ([View Highlight](https://read.readwise.io/read/01hv5a18a1kymn1qwnf2ak6xd3))
- A *programming language* is an artificially constructed language used to instruct computers. ([View Highlight](https://read.readwise.io/read/01hv5a20sn63a908ys9ezkvcr8))
- Like human languages, computer languages allow words and phrases to be combined in new ways, making it possible to express ever new concepts. ([View Highlight](https://read.readwise.io/read/01hv5a2edawhepv3sj2fgfrgvz))
- You’re building your own maze, in a way, and you can easily get lost in it. ([View Highlight](https://read.readwise.io/read/01hv5a3ecfekjyk2k44nyzc1xz))
- When action grows unprofitable, gather information; when information grows unprofitable, sleep.
  Ursula K. Le Guin, The Left Hand of Darkness ([View Highlight](https://read.readwise.io/read/01hv5a4bzjga2tsknk79yyasxp))
- Computers themselves can do only stupidly straightforward things. The reason they are so useful is that they do these things at an incredibly high speed. A program can ingeniously combine an enormous number of these simple actions to do very complicated things. ([View Highlight](https://read.readwise.io/read/01hv5a6frd6k739jmqdztqnnrr))
- A program is a building of thought. It is costless to build, it is weightless, and it grows easily under our typing hands. But as a program grows, so does its complexity. The skill of programming is the skill of building programs that don’t confuse yourself. ([View Highlight](https://read.readwise.io/read/01hv5a78ns8p7mzweed86361sy))
- To program early computers, it was necessary to set large arrays of switches in the right position or punch holes in strips of cardboard and feed them to the computer. You can imagine how tedious and error-prone this procedure was. ([View Highlight](https://read.readwise.io/read/01hv5a90mp07dzabkvwevhd3j3))
- Using names instead of numbers for the instructions and memory locations helps: ([View Highlight](https://read.readwise.io/read/01hv5aa4fsjhwbegs84n9jvzhx))
- Set “total” to 0. Set “count” to 1. [loop] Set “compare” to “count”. Subtract 11 from “compare”. If “compare” is zero, continue at [end]. Add “count” to “total”. Add 1 to “count”. Continue at [loop]. [end] Output “total”. ([View Highlight](https://read.readwise.io/read/01hv5aa7zc94x4p9fe5jbsp5xm))
- The first two lines give two memory locations their starting values: `total` will be used to build up the result of the computation, and `count` will keep track of the number that we are currently looking at. ([View Highlight](https://read.readwise.io/read/01hv5ab5xzyhx2dh3h46693e1k))
- The lines using `compare` are probably the most confusing ones. The program wants to see whether `count` is equal to 11 to decide whether it can stop running. ([View Highlight](https://read.readwise.io/read/01hv5abjved7q4wsf78yee87vr))
- uses the memory location labeled `compare` to compute the value of `count - 11` and makes a decision based on that value. ([View Highlight](https://read.readwise.io/read/01hv5acbe0zy40vdcp693m2m3h))
- The next two lines add the value of `count` to the result and increment `count` by 1 every time the program decides that `count` is not 11 yet. ([View Highlight](https://read.readwise.io/read/01hv5acm94esc39g69gevcchbm))
- Here is the same program in JavaScript:
  let total = 0, count = 1;
  while (count <= 10) {
  total += count;
  count += 1;
  }
  console.log(total);
  // → 55 ([View Highlight](https://read.readwise.io/read/01hv5ae4343ammxb1xj5551yqm))
- there is no need to specify the way we want the program to jump back and forth anymore—the `while` construct takes care of that. It continues executing the block (wrapped in braces) below it as long as the condition it was given holds. ([View Highlight](https://read.readwise.io/read/01hv5af8pzy1s4syp70wsqpfn3))
- That condition is `count <= 10`, which means “the count is less than or equal to 10”. We no longer have to create a temporary value and compare that to zero, which was just an uninteresting detail. ([View Highlight](https://read.readwise.io/read/01hv5agceex2nzazhzsa4jmw5a))
- At the end of the program, after the `while` construct has finished, the `console.log` operation is used to write out the result. ([View Highlight](https://read.readwise.io/read/01hv5agybfpgczn1g6rbqynzk3))
