# Using the find Command

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)

## Metadata
- Author: [[brilliant.org]]
- Full Title: Using the find Command
- Category: #articles
- URL: https://brilliant.org/courses/programming-python/strings-4/slicing-2/2/?from_llp=computer-science
- Tags:

## Highlights
- We call commands like these — that use the dot notation — **methods**. They are essentially functions that are only defined in the context of some variable (more precisely, an *object*) in the program.
  For now, you don't need to worry about the difference in terminology, and we'll simply refer to them as **functions**. ([View Highlight](https://read.readwise.io/read/01j94p1n56af8xb69k8ecvnw9r))
- For `str1.find(str2)` to work, `str2` needs to be contained in `str1` as a continuous sequence of characters.
  If this isn't true, `find()` returns a **default value** of `-1`. ([View Highlight](https://read.readwise.io/read/01j94p5tfcqgrat93hdpssbpks))
- Positions are always non-negative integers, so -1 was chosen by Python's creators to represent the failure to find `str2` inside `str1`. ([View Highlight](https://read.readwise.io/read/01j94p6bvaryzt6k71qtgjbdht))
- The `find` command is case sensitive, so when the `str2.find("per")` command is run, the program doesn't find a match: ([View Highlight](https://read.readwise.io/read/01j94p7zjnmnyzzzzchaqv75ac))
