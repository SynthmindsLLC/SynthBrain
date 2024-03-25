  

 Hey, Chatters. We finally made it to a very, very exciting day,  which is we're going to hook her up. Okay. And what I mean by that is we're going to take a large language model and hook it up to our notes in a way that we can easily reference those notes using a couple of different community plugins that I'm going to go through.

One, which is called Copilot and another one that's called Smart Connections.  So, before we get started, I just want to talk about the concept of embeddings, or a vector database. This is essentially where it can take all of this text data,  convert it into a matrix of numbers, and cluster those numbers, aka those words, in ways that are related to one another, which makes it extremely easy for a large language model to find and use that as context.

Now,  A lot of the large language models have started using this, it's how the knowledge base works, it's called Retrieval Augmented Generation. And all you really gotta know is that we're gonna do that, but with your second brain, with your notes. Which is why it's taken a little while to get to this point because in some ways it's kind of useless until you have some notes in here to actually work with.

And I also want to make sure you have the basics, obviously. So,  let's get into it.  Okay, so we're going to go into Settings and Community Plugins, and we're going to start with Copilot. So you'll browse, and you'll look up Copilot. I already have it installed.  You'll install it, and then you'll go to Options.

Now, you do have to set some things up here, and each call costs money. Not a lot, again, and especially depending on what model you use, but  you're going to have to have an account with OpenAI, which I'll go through in a second. So first, you can choose your model. I have it on turbo, but you pretty much have access to any and all, including a local AI if you want to go that route. 

This is to save it in a specific folder, your conversations if you want to. And then you got to put in your API key. So we're going to go. I've done this before, but I will  show you again.  You want to go to OpenAI's website at platform. openai. com, should take you somewhere that looks like this. You want to go to settings,  billing, and just set up your billing information and your payment methods.

And then you're going to have to go get an API key. So just create a new secret key, that'll come up. Name it something like obsidian key or whatever.  Copy and paste that, come back in here, and just stick it right here.  And you'll be ready to go. Now, if you're more advanced, you can set up the Azure version. 

You're probably not going to need it. It'll just be a little bit faster.  But this is the exciting part. Not only can you, uh, do the temperature, but you can set the token limit. But more importantly, the conversation turns in context. So for those of you who don't know, if you're just calling on the API, each call is its own instance.

So how ChatGBT gets around this is essentially it's gonna  Take your entire conversation so far, and then send that to the model, and then the model is going to spit back what's next based on that entire conversation.  That's what this allows you to do, which is really cool, so you can have conversational turns up to 10.

So in other words, it's going to maintain the context of your conversation up to 10, you know, back and forth. Now.  You gotta keep in mind, and it gives you this warning here, uh, this is, it's important to realize that this is going to cost you more money. You're getting charged per token, and so if each time you're sending back the full conversation, that means you're getting charged for all of those tokens, so just keep that in mind as you're doing this, and this, this is, can be used just like ChatGPT, but maybe it doesn't make so much sense, uh, as I'll get to in a minute, um, actually right now.

So.  An interesting thing about this one is that it doesn't actually take the embeddings, the vectors of your entire note base, which is a big problem for me because I want it to be taking sort of all the stuff I've been taking in my notes and help me synthesize that.  But what it can do is allow you to take an active note and query that.

Again, unless you have a really, really long note, like unless you're writing a novel in one note, maybe this won't be so useful, but I'm going to walk through how to do this either way.  So there's two ways to do this, well, there's multiple ways to do this, but you can either do the OpenAI way, which is going to cost you a little bit of money, it's not going to be a lot, it just has to pay for the embeddings, or you can do it through CohereAI. 

Which I'll show you how to do, uh, right here. So if you go to this site here, I'll just bring it up.  And this one's free, so you might want to go with this one.  You just, uh, sign in. I have Google, so it's easy, but you might have to make a username and password.  You want to come to API keys.  You might have to, like, set up some other stuff, uh, here, but all you gotta know is you just gotta, like before, just set up a key, name the key.

It'll give you the key, and then once you have the key, you stick it right in here. And it'll save that embedding for up to 30 days. At default, you can set that to whatever you want.  Now if you're real fancy, you can even set up a local, a large language model. I'm not going to get into that. It's going to be unless you have like a super fast computer or want to set it up. 

Somehow through the cloud, it's going to be really slow and probably outside of the time it's going to take you to set up. It's not worth it. But  if you did want to keep everything local, you could absolutely do that, which is a really cool setting.  And then the last thing I want to talk about in these settings is your custom user prompt.

Now, I don't use Copilot that much, but normally I would put something in here myself. You know, the, the system prompt that it sends every single time just to be specific to you and helping to guide it, maybe giving it a personality. You can do whatever you want there.  Okay, so let's see how this works.

We're going to go into some of my courses. I'm going to pull up this advanced prompt engineering course that I've been working on.  We're going to pull up the side panel here. 

And we're going to go over to Copilot.  Now this probably looks pretty familiar to you. You can even change the model here if you want.  We have a stop generation. We have a new chat. We have save your conversation as a note.  And then we have conversation mode or QA active note. So conversation mode is just normal conversation, uh, that you would like with chat GPT for.

It's going to be the same thing.  Except you'll have just a certain number of conversational turns. Let's go to QA active node here.  And you'll see here it's saying, Okay, feel free to ask me questions about advanced prompt engineering.  And it's going to build this index. You see vector store created successfully.

I just indexed this active note, so I'll be like, you know, tell me about the scribe method, which I know is not going to be in its training, right? So now it's going to query this note, and we'll see what it comes up with. And it's pretty fast.  Yep, specify a role, 

context, responsibility,  instructions,  and banter slash evaluate. And there you go. It's using my note as reference to make its response. So, again, this may or may not be useful to you depending on how long the note is, because it can't search through the entirety of everything that you have, but for most cases that might be fine, or if you just want a way to use ChatGBT right here in your notes just so it's, you know, easily accessible and you can easily just save that note, maybe this is the way for you.

so that's Copilot. I don't really use Copilot that much. Uh, what I use instead is something called Smart Connections, which is a lot more exciting to me. So, let's go back to Community Plugins.  We're going to look up Smart Connections. It's already installed. Again, you're going to want, this will say, installed to you, and then enable. 

And now let's go in.  Now, uh, this is the best. Uh, feel free to support this guy. So first you want to put in your OpenAI key, which you should have had already from what we did, or you want to make a new one specific to this, that's fine.  Choose your model. Again, I have GPT 4 Turbo enabled, but you can choose pretty much whatever you want. 

Your default language.  Yeah, if you want, you can do these. But essentially all this does is like saying, okay, don't include any of these files or folders in the embeddings that we're going to do so that I can draw from.  Again, you can leave most of this stuff just the same. Uh, and you'll see down here it says previously failed files, which is totally fine.

So what's happening here is It's taking all of my notes, not just the one note I'm in and creating embeddings with them using the OpenAI API. So again, this one's going to cost money. You can't use the Cohere free one, but I'm telling you, it's very inexpensive. It's going to be like a couple dollars, even if you have like a bajillion notes.

So I wouldn't worry too much about it. If it misses some, let's actually see what happens. You know, you can retry, uh, these files.  And if you really need to refresh, you can do force refresh.  So it's actually not that hard to set up. Like, all you really have to do is put in your API key, and then choose your model, and you're pretty much good to go.

 So, how it's going to look, you can bring it up with the command palette, but I have it up here, and it's going to look something like this, depending on when you're watching this. Now, instead of this having access to just this one node I have open, and it has access to All of my notes, so what I can do is tell me about the scribe  method  and I'm not even going to give a direction in terms of what note to look for. 

Now while it's coming up with the answer, there's a few things I want to point out. One is the save chat. So this will create a note. Here is your chat history, so you can look back at past chats. And this is to create a new chat this plus button. I'll talk about the smart connections in just a minute.  And you're going to see this is going to act differently from how yours acts.

And I'm going to explain that in a moment. Um, but for now you can see it's spitting out. It has this, uh, prompt that I have. It's going through all the different, uh,  the acronym correctly and even better. It didn't put banter and evaluate together.  And then it's even telling me where I can find this note. 

So I didn't even tell it where that note is. I mean, I know I have it up now, but it doesn't know that. And I can tell me exactly where to go, and it gives me all of these other examples of where I can look. In my notes, even the video explanation, uh, so yeah, this is much better to me, but the downside as compared to Copilot is that this does not have conversational context.

So if I say,  what was the last thing I asked you,  we'll put that in  and while it's going on, you can just copy the individual message. You can copy the prompt to a clipboard, or you can copy the context to a clipboard.

 So you'll see here the last thing I asked is not explicitly stated. It's making up some stuff. It's saying, here's the daily note that you did. So, as you can see, it's not actually, uh, remembering, right, the context.  So another great thing about Smart Connections is that it creates this, uh, Percent of connection  for different notes.

So you can see here I have an in advance prompt engineering  and it's looking at this file, but it's saying, Hey, if we were to look at this, there's actually a 90 percent  relevance score between these two notes. And so what you could do with that is you can actually just click and drag this into here  and what it's going to do is just put the backlink for that note. 

Easy as pie.  And this just makes it a lot easier to connect up all your notes and see how things are related. Because as amazing as the graph view is, it can be a little bit overwhelming and it's tough to know like what can actually connect well with other things. So,  just another great use of smart connections. 

Okay, let's go back and talk about How I did this magic of bringing in Professor Synapse into here because if you're looking at it now It probably looks nothing like that. It essentially will just say how can it help you today?  So you have to be a little bit of a risk taker here. So again, I don't really know how to code  But that doesn't mean I don't know how to navigate things So what you want to do is find where on your computer the subsidian vault is saved Okay, and you're going to see here we have, uh, this obsidian folder.

We're going to want to click in there, and then you'll see plugins.  And we're going to go down to smart connections. don't really need to know, uh, what most of these are, but obsidian uses javascript, and we'll see here we have this main javascript file.  What you're going to want to do is open this up.

You might need to download something like Visual Studio Code, or you might have to, it might just open in a text file. Whatever it does, it's going to bring up this really long, uh, it's going to bring up the code, you know, of how this thing works. Now, if you want to create your own prompt and have some control over it, all you've got to do is Ctrl F  and look up the word prompt. 

And that's going to bring you to a few places where it says prompt and you want to keep going

 until you get, uh, 

until you get here.  Now, you'll see here it has it in different languages for people to set it up. But all you've got to do is find this one that says prompt and you'll see I've put my own prompt in here as well as here's the initial message. This gives you a little bit more control over what the actual system prompt is and how you want it to greet you so you can personalize it a little bit more.

just make sure you save this, uh, before you're done and you'll be good to go. The only thing you're going to have to keep in mind is that every time that this thing updates, it's going to revert back to what its old version was. Or hopefully by the time you're reading this, the, uh, creator, uh, will have in here a way for you to just create your own system prompt like Copilot had. 

Okay, so that's it for now. I got one more thing I want to talk about, which is a way that I use these. So, thing I really like to do is to recap yesterday. And so, what you can do is actually reference specific notes that you wanted to use.  So, if we create a backlink to, let's say, 1130.

And I say, Summarize.  Just summarize, I don't have to do or just recap what it's going to do  is you see it's backlinked it  and it's going to tell me more or less what I did that day  based on the headings I have in there.  So I haven't done it for today in this note, but it's just a good way if  you have longer notes or you're doing this for daily journaling and you want to remember what you were up to one day or every day you want to just start your day by reminding yourself. 

Hey, this is what I did yesterday. This is what I got to do. Uh, this is the way that you can do it. It makes it super easy.  Thank you again for listening. This is going to be the most fun part, so spend your time having fun with this. Again, it works better if you have a lot of notes to reference, and use this as your writing companion, as your, whatever you're doing, it's really useful in terms of referencing other notes, or just using, you know, ChatGPT natively to ask  📍 some questions. 

Thanks for listening and I will see you next time where we're going to get into some fun workflows together. 