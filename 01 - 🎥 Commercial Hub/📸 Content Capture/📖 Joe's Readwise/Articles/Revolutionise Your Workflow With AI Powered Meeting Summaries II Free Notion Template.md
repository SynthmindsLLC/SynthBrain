# Revolutionise Your Workflow With AI Powered Meeting Summaries II Free Notion Template

![rw-book-cover](https://i.ytimg.com/vi/F0G3492_kIE/maxresdefault.jpg)

## Metadata
- Author: [[Matthias Frank]]
- Date: 2023-01-08
- Full Title: Revolutionise Your Workflow With AI Powered Meeting Summaries II Free Notion Template
- Category: #articles
- Summary: This video introduces a method for generating meeting summaries and extracting action items using AI technology. The method involves using a combination of tools such as Notion, Auto AI, Google Drive, and Open AI. The process begins by setting up databases in Notion to store meeting information and tasks. Then, a transcript of the meeting is generated using Auto AI or a similar tool, and the transcript is saved as a text document in Google Drive. The automation is built using Make, an automation tool, and Open AI's GPT-3 is used to summarize the meeting notes. The executive summary and action items are then sent to Notion for further organization and tracking.
- URL: https://youtube.com/watch?v=F0G3492_kIE&si=ocmxBRr1MsBeR5MR

## Highlights
- our goal for this automation will be to get the transcript that we just created into it into the automation then send it over to open Ai and AI protocol
  that we're using to summarize the uh the meeting notes and then take both the summary and extract the individual action items from it and send all of that to notion ([View Highlight](https://read.readwise.io/read/01hnwferzy9b05fvnwchp79kvt))
- Google Drive that's where our meeting notes are we pick it and then we get to
  pick a specific action in this case we want to watch files in a folder ([View Highlight](https://read.readwise.io/read/01hnwffjb0bx2bmjy0wk1v7sss))
- watch files uh probably by created time that means if there are any changes to them later we don't run them again ([View Highlight](https://read.readwise.io/read/01hnwfgmnqkp385c02bxzvz3t1))
- after we identified the file we need to get it into the automation which means we need to download it and we can do that again with the Google drive module download a file which again requires us to give a connection and then a file ID and for
  the file ID we can just use the file ID that we found from the previous step so we click in here and opens up all the stuff from the first step that we can now use for the next one and we click on file ID which means it will now start downloading ([View Highlight](https://read.readwise.io/read/01hnwfkezwqf4775pq4027j66t))
- all the action items are a list and of course we
  don't want them as this list we instead want them as individual tasks that we can add to our task manager in order to do so we need to do a little bit of regex regular expression magic that will isolate just this part from the response ([View Highlight](https://read.readwise.io/read/01hnwft773jqtn86bvv1r4zs2j))
- click on add another module and we're going to add a text parser and in there we tell it to replace basically we want to remove everything
  from the response except for this list of tasks and the pattern we're going to use for the regular expression is this one again you can copy it from here or you can go into the blog post and copy it from there and this will match everything up until action items ([View Highlight](https://read.readwise.io/read/01hnwfv4pcq7wgnwd911w0bz8e))
- remove it so the new value will be by clicking on a here and empty string that just takes it out we want the global match we don't want it to be case sensitive because here it's small and in the response it's
  mostly all caps we wanted a single line and that should be it so in the text will be of course the um response from uh open air open AI in the previous step ([View Highlight](https://read.readwise.io/read/01hnwfw1e3phd10yy9cq7cg8x7))
- we add our notion module and we're going to pick the option create a
  database item we want to now add a new meeting with the transcript and the summary to our database and we're first going to pick our correct workspace ([View Highlight](https://read.readwise.io/read/01hnwfwrc86mxvcnfd1kt0fxk4))
- before you can access the database here you need to give make specifically access to that specific page ([View Highlight](https://read.readwise.io/read/01hnwfxgw2dfna5t7rbq07a25n))
- we also want the transcript and for that we add a second notion module again notion and this time we pick append page content and this allows us to write into the body of the page so we'll pick that again pick our notion connection wait for it to load and then give it a page ID which will be the page that we just created here so we pick database item id it's different name but it's the
  same thing a bit confusing and then we click on add item and this will now open up a whole bunch of options but don't worry fairly straightforward it just has to do with the way the notion API works that we get so many options here so we click on item type will be a paragraph and then we get this texting and again add an item and you can ignore all of these things except for Content that's the one that you care about here is where you put in the text so again it's the data but we
  can't put the data in directly we need to go again to the text formulas tostring click in between and then pick the data and that will add the transcript to the body ([View Highlight](https://read.readwise.io/read/01hnwg0y5fx8x4n4ymt08jkmgm))
- all that's left is now adding the individual tasks to notion and for that we need to get the string that we have here isolated and turn it into an array and then add each array element to notion ([View Highlight](https://read.readwise.io/read/01hnwg1yqv9y9cp2shpy96bc9y))
- we do so by adding first an iterator so we search for iterator that won't bring up an exact match but it will bring up flow control we click on that and then on iterator and then we need to give it an array we don't have one yet we only have a string but with the split method so we click on
  a again and then on split we can turn any string into an array and we do that by telling it first okay what's the long part and then where should it cut that into individual chunks ([View Highlight](https://read.readwise.io/read/01hnwg39x61j8mvvc6qtrfadh9))
- give it a text and the text will be whatever we create here right so this text is our input we also see if we have over and right we need to go to string and then whatever the list is separated by and then the comma that's why I explicitly state in
  the prompt please give me a comma separated list not semicolons not like hyphens I want them separate by commas so that we can run this formula properly ([View Highlight](https://read.readwise.io/read/01hnwg43q9w3cebcbv909wh3qw))
- then last but not least and again a notion module create a database item and this time search for the task one ([View Highlight](https://read.readwise.io/read/01hnwg4e8fh4gcdynxass8da99))
