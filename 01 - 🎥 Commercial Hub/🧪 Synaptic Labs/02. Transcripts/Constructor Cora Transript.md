  

  📍 

Introduction and Purpose of the Video

Jatters, I got my dogs in here  because they saw or heard something outside and trying to protect me I guess. So sorry if we get some barks in here. 

Introduction to Constructor Cora

toDay I want to talk about Constructor Cora, another gift from me to you.  I know GPTs can be a little annoying. You've probably used this create feature here and been unimpressed or maybe not even known where to start.

So I've created Constructor Cora for the express purpose of helping you build GPTs. Using at least like my method of prompting just to automate as much as I can for you. Just a much, much better  version of this.  

Explaining the Prompt and its Sections

So let's just quickly, I want to walk you through the prompt. This is going to be up on GitHub now, so you can also just look there and find it.

You can use the link to use the, GPT, which I'll keep updated as I learn and  hear feedback from you all, but obviously you can take the prompt and just make your own and do whatever you want with it.  You'll see here, per usual, I have things broken up into the different sections. The first is the mission, which is essentially saying you're Constructor Cora.

You're going to help guide through an agent, me creating an agent at GPT that's going to help me do the things I want to do.  Instructions are just gathering information from you. And then outputting those instructions in the format, which I'll show below.  Generally supporting and not not  assuming that you know anything about what you're doing.

So it's going to help not only build this, but ask you questions and make recommendations. It'll help you think about what knowledge base you want to put in there. If it makes sense to connect to an API, and then if yes, it'll help you walk through how do you actually connect it to that API.  And I'm just going to encourage you to, test it. 

We got some variables here. I just want to make sure that it knows what a GPT is.  JSON I have that as a variable just so that it can help you develop what that actually is in terms of, there's a specific format you need to do and the actions walk you through that process.  

Understanding the Format and Rules

And then here's the format.

Again, this is typical of what I do with everything. You have a mission, you have the instructions, you have the list of tools, you have some rules.  We have an explanation of the tools and what they do, a personality.  And then here are the actual rules  for, oh, I'm realizing.  So even I need to think about my prompts.

So here's the format, and you'll notice that here I have mission, but it's not in Markdown, it's bolded. And that's because we already have marked down throughout, so I don't want to confuse it. And then when we get back down to here after rules, we get back to tools. And then that's explaining the tools that Constructor Cora has to use.

Her personality,  prefers to ask when we want her, so she was asking like 70 questions to start. It's just I don't even know where to start with you.  And then just some rules, include recommendations in each output. See, even here, I have to update it. Assuming the user does not know what is possible.

Again, I don't want to, if you know what you're doing, it doesn't matter. But most people, they're going to need some help. Why not have, yeah, help. And then, just some, browse the web if you have no idea. This is particularly for the the API calls and stuff. You're probably going to need that.

And then just, our introduction.  And that's it in terms of how it works. So I have this, again, I hate looking at a blank screen. So I have this command. That's let's build. 

Demonstration: Building a Bot with Constructor Cora

So let's let's actually get into it.  We'll go over and actually use it. here she is.  We're gonna hit let's build.

 And we're going to say my usual example, I want a bot that will help me write children's books  with illustrations. 

  So you see here it's going to ask me some questions. It's already not doing what I told it to do. It's asking like 50 questions, but at least it has it numbered out. So 1, let's say 5 to 7.  Two,  um, genres or topics. Depends on what I want to write.  Three, illustration style, we'll say cartoonish. 

Four.  Interaction level with the bot. Do you want the bot to generate content independently or do you prefer work as an assistant? 

  So he's asking me about the knowledge base right now. So let's just say like I've written children's books before so I can upload those 

and of course we get a network error.   For those of you who don't know in the time of recording this, it's.  It's a mess at OpenAI. 

I could use assistance. Let's just see what it says. 

 Yep, this is pretty good.  More network errors, of course. 

  This is great. Reminds you that don't upload anything you don't mind sharing with others. Okay.  What's next? 

  And here you can see it's creating everything now. 

Generate story ideas, write in tone, assist with story development, create cartoonish illustrations, incorporate feedback.  See, it didn't include Code Interpreter, because why would you need that? 

This is good.  And then, there you go.  And then all you gotta do is copy paste this into a new GPT. We can go to,  just  copy paste this,  we go down to explore, create a new GPT, configure, and just stick it right in here.  You'll notice that it did not hold over the bold, probably because I copy pasted it with Control C.

So you're going to want to maybe, I'll work on this, but I do want it to output in Markdown, so I'll work on that. But, make sure you replace this with, whatever you want it to be. Similarly, down here, so you can give some personality to your bot.

  

Final Thoughts and Conclusion

So that's a quickie. You can visit the GitHub to check out more.

I'm hoping this is straightforward and helpful, and as always, please test it out,  📍 provide feedback. This is very much the beta version. I want it to work for you, so let me know and I'll keep it updated.  Thanks.

