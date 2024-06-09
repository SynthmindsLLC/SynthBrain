# The Most Important Skill You Never Learned

![rw-book-cover](https://i.ytimg.com/vi/l8pe_MSX4Lc/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGBMgUyh_MA8=&rs=AOn4CLDVaTll1iWLOAHMfyEaZM_dECEzeQ)

## Metadata
- Author: [[Web Dev Simplified]]
- Date: 2024-06-04
- Full Title: The Most Important Skill You Never Learned
- Category: #articles
- Summary: The text discusses the importance of debugging in coding. It explains how to use console logs and the debugger tool to find and fix errors in your code efficiently. Using breakpoints and step-by-step debugging can help you understand and resolve issues in your code effectively.
- URL: https://youtube.com/watch?v=l8pe_MSX4Lc&si=yAnt-tXmpzZB4SnA

## Highlights
- if you're an absolute beginner when it comes to debugging the first important thing to understand is how you can actually use the tools that are given to you to debug
  bug certain problems that come up in your code for example in this code I have some really simple stuff going on I have a function called print name takes in a first name and a last name and it just combines together the first name and the last name and down here if I just pass in for example Kyle and I pass in cook that should print out Kyle cook but when I save you can see we're getting an error immediately uncaught reference error fit name is not defined and it gives me some other information after ([View Highlight](https://read.readwise.io/read/01hzwnkcmvhd9k7f133kz0dh3f))
- so immediately when you get an error like this the most important thing to look at is going to be this Topline message right here which tells you what the error is in our case it's an uncaught reference error ([View Highlight](https://read.readwise.io/read/01hzwnme91ymyc371rqzbp9ww9))
- most important thing to look at is going to be this section right here which tells you exactly in your code where this happened so in our case it's saying this happened in our script.js file on line two so if we go into this file and we go down to line two you can see this is where the error is occurring ([View Highlight](https://read.readwise.io/read/01hzwnn1bs23m13bf78x606jpv))
- it says fit name is not defined so that means this fit name variable is not defined but is trying to be used in this particular case all I did is I misspelled first name as fit name so if
  I were to actually fix this by properly spelling first name and I give it a save you can see immediately that fixes that particular error that we had ([View Highlight](https://read.readwise.io/read/01hzwnnnsed4hbxz4f1v6n5fzs))
- we have another bug but this one doesn't actually show us an error and these are by far the hardest to actually
  debug because usually an error message is good at telling you what's wrong but if you don't get an error message it means something's wrong with your code most likely because of how you wrote it so in our case here Kyle Cook is printing out exactly like we expected to but right here we're calling print n times and it should print out the value high five separate times but instead it's printing out five five separate times so clearly there's something going on inside of our code now in our particular case it's really easy to read this function cuz it's only three lines and figure out what the problem is in our case you can see here that I'm console loing n instead of console
  logging our value if I were to swap this out with value and I give it a save you can now see it prints out high five times instead of n five times ([View Highlight](https://read.readwise.io/read/01hzwnrdcgyyhjc90zb6d1699z))
- you can put in console log statements to try to figure out what's going on inside your code so for example let's bring this back to the broken code that we had before and what I could do is I could say you know what for some reason it's printing out five I wonder if my value is proper so I could say console.log and I could say value and I could print out my value so now hopefully I can see if my value is being passed in properly as you can see here my value is high so at least I know that is working and this is going to be the most basic way of debugging a problem ([View Highlight](https://read.readwise.io/read/01hzwnt05tpvmf93w1nj7tbtvq))
