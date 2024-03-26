# Super Synapse Update

[00:00:00] Yeah.

[00:00:08] **Joseph:** Hey Chatters so a quick but potentially big update today. So for those of you who don't know I've had these two different versions of Professor [00:00:20] Synapse, just the normal Professor, and then the Super Synapse. Now, previously, the original Professor Synapse, was the simpler one, and then I had all this telemetry of thought going on with SuperSynapse, where first it would have a structured way of going through its thought process before [00:00:40] responding to you.

Now, this works really well and You know it just built upon the original foundation of Professor Synapse And it got to a point where I felt like this should just probably be the typical Professor Synapse So I actually moved over the prompt from Super Synapse over to Professor Synapse, which is the [00:01:00] state it's in right now And decided to use SuperSynapse as more of my testing experimental ground for new and updated ProfessorSynapse prompts, so I could get out there, people could test it out, I could get some feedback, and then the idea is once I feel like that is good enough, then I'll do the same thing.

I'll just move it [00:01:20] over to the normal ProfessorSynapse, and I'll continue to experiment on Super.

this is the first time that I've actually created something experimental for SuperSynapse. I felt that the original prompt was getting a little bit too complicated and out of hand. If you've played with ChatGBT, you've probably found that the [00:01:40] longer your prompts get, the less able you are to control them.

Hey, Midge. I wanted to go back to basics and figure out how I could really slim down this prompt. I've gotten a lot of people saying that the like custom instructions version of the prompt is actually like the best version of the [00:02:00] prompt and people still use that. So I wanted to simplify and again make this as easy for you to edit as possible so you can really make it your own.

You know the idea here is I really want everyone to have their own sort of version of Professor Synapse that's personal to them. [00:02:20] So let me walk you through this new prompt and how I threw everything out and have now brought something I hope is a little bit more coherent and simple and easier for you to understand as well because you know a big part of my ethos is I want this to be accessible to all.

So the first thing I just want to mention is I have [00:02:40] done away with the separate agent that Professor Synapse calls up. Now all of that kind of work is going to get done in that thought process, which I call telemetry. And so that's the major thing you're going to notice is that there's no longer a calling up of an agent.

Instead, Professor Synapse is just going to be [00:03:00] your agent for everything. So let's go through how this works. Let's get into the prompt. So for those of you who don't know when you put two asterisks around something in Markdown, that makes it bold to the computer. So right now we're seeing, Professor Synapse is bold. This is who you are. A wise guide specializing helping me [00:03:20] achieve my goal according to my preferences.

And we put preferences in the brackets, just to make set it as like a variable that it can fill in the blank to and to call attention to it. You have the power of telemetry. A single asterisks is just means that it sees it as italic. So I just want to emphasize this, which helps you reason by [00:03:40] transparently communicating your thought process in a Python code block prior to output.

I say a Python code block because I wanted to use Encode Interpreter. Before I was having it output as, an actual block that you would see. I feel like that would be like, it's a little bit of a user turnoff in terms of if I want to look at it, I will go look [00:04:00] at it. But most of the time I don't really need to see it.

So I can inspect it if it goes off the rails. But otherwise I do just want it hidden so that it's not a ton of text I have to go through. So we'll see what that looks like in a minute.

The next part we have in a code block, as an example of how we want to do it. Again, if you don't know Markdown, if you do these three [00:04:20] backticks, enclosing some text, that tells the computer to look at this as a code block. We choose Python right here. So this is going to name the code block more or less.

This is going to help us get consistency around using code interpreter to run this.

in our code block. Now we have the telemetry. This is [00:04:40] formatted in a way that is, through Python. I don't write Python, I don't code, so I essentially just asked ChatGPT to help me with organizing this, and we came up with this. Now, something important, I'm going to be doing some videos on this, is, I use a lot of emojis, and some people get a little annoyed at this, but, I just have this intuition [00:05:00] that there is a symbolism we can use in emojis that will carry more meaning, For the L.

L. M. than just words alone. It's our first step towards a more neuro symbolic a I because it is so accessible and so globally understood when I look at this map, [00:05:20] there are a bunch of connotations that come with this map. When I look at this brain, a lot of connotations come with this brain, even though it's not the word brain, it's an image of a brain that can represent many different things within the context of what we're doing.

So I think of these as variables that we can define for the [00:05:40] LLM to help, use its thinking and also for it to be transparent for you around looking at its thinking. So let's start with the map. This is just the global goal or aspiration that you're working towards at the top level, keeping that in mind so that we're always moving towards that.

We have our wrench. This is for us [00:06:00] to create adjustments throughout the conversation. So if it's, taking your sentiment or inferring your intentions and it gets it wrong, or you say, no, that didn't work. This allows it then to incorporate some sort of adjustment thinking through that adjustment and its process.

Next, we have your initial state. Now, a lot [00:06:20] of this, like the rest of this stuff, I pull from Q learning, which is a reinforcement learning technique in the field where essentially it's like you have an agent, it's taken a step, thinks about what is going on. Did that lead me towards that goal away from that goal?

What's the deal here when I made my move or made my [00:06:40] decision? And so that is thinking about your initial stage. Then we make an inference based on that initial state. So again, did it work? Did it not work? Could it be better? Was it not so great? Is the user mad? Whatever it might be. We want to think about, okay, I had this initial state.

Let me make an inference based on the [00:07:00] context of the situation. And then based on that, it's going to come up with a strategy that incorporates that proposed adjustment and the inference that it has made in terms of its initial state. And lastly, we want to add the role in here. And so this is why I've gotten rid of the extra agent because now I feel like you don't actually need it.[00:07:20] 

Because we can create a dynamic piece of the thinking that allows it to take on the role of that agent based on the context, instead of creating one and then having to stick to it based on whatever is going on. So now we just have, and I'll probably build this out a little bit more, but just for testing purposes, the brain is your expertise.

So expertise and domain [00:07:40] specializing in subdomain and that'll fill in those brackets. So that's the thought. And then very simple instructions. Gather my goal preferences in context, engage in telemetry, reason step by step on the strategy to achieve my goal based on context and preferences, and then use telemetry as a way to [00:08:00] constantly adapt and align with me until my goal is completed.

Embodiment, I don't know, maybe I'll pick a better word for this, but the idea is personality, right? What is the persona you wanted to take on? This is very customizable. Please. Take this, make it different, right? Make it yours, make it how you prefer to [00:08:20] interact with this AI. And so I just have wise and curious, computationally kind, a patient mentor, and light hearted.

Something new ish, I've gone back and forth in commands. One of the problems I have with commands is that people will forget about it. So I've now I'm going to [00:08:40] put these up front. You'll see in the introduction, but I feel like critic mode is always important. A question mark to be like, I don't know, can you help me out here?

A plus sign to expand and an S to essentially save, we create a summary of your conversation so far. I would like these to become [00:09:00] somewhat standardized across the field. Especially the exclamation mark the question mark and the plus sign. I think if we can all agree that these mean the same thing, exclamation mark is critic mode. Question mark is, I need help essentially. And plus is expand. This makes a lot of sense. And I think this is [00:09:20] something we can keep common throughout all of our interactions with AI. Eventually be able to infer, but you want to have some control over this.

So I guess what I would say is if you're with me here and you're putting commands in your prompts, maybe this can be our, standard set together. And then that way over time, the model will [00:09:40] get trained in this. And we don't even have to define these commands. It's just going to know. is another place too, where you can just add as many commands as you want.

If you have other shortcuts or ideas for commands, just toss them in there. Rules. This is another one. You can definitely, do whatever you want with these rules. These are your preferences. But ones you want to keep. [00:10:00] Or after the context is gathered, you gotta use telemetry, right? This is like the whole part.

If it's not doing telemetry, it's not working right. I have it always taking on the persona of the professor with the emoji, and then full of brevity. I've heard a lot that, you know, chat GPT can be super verbose, and so we want to [00:10:20] control that and have it mostly output a little bit. Just a paragraph or so, that makes it a lot easier.

So you're not just like I love to read. I love the blocks of text, but I understand that people don't want blocks of text. Their attention is a limited resource. And so you want something shorter and broken up into pieces. And I found that this [00:10:40] works. A couple people in our team brought up this term full of brevity.

Okay. David and James to work to really cut it down. And I found that too, that this actually is a pretty good few words you can use to make it, be more concise. And then we have our introduction, which, you've seen all the other ones, but for this one, again, I simplify [00:11:00] it. And then I add the commands in to code block right at the beginning.

What you can use as commands. We

have a kitty guest. Classic Midge. Just loves hanging out when I'm in the middle of recording, but that's okay. Hopefully this is a nice little break for you all. [00:11:20] Okay, let's talk about what this looks like in practice. You can just hit start. You'll see right off the bat, it is doing what I told it to do, which is a good sign.

We have, what do you want to accomplish, and we have our commands here. So let's use our typical kind of idea. We'll say I want to write [00:11:40] a children's book for my seven year old's nephew. I think he's actually eight now, but whatever. Okay, so something to mention here. You'll see it's working.

It's analyzing. That means it's using Code Interpreter. I have [00:12:00] it set so it always expands the output. Because I like to actually see it, but if you click this, it's gonna turn it off. You won't actually see this. So let's actually turn it off for the next one so you'll see what I mean. But you can see it's working.

So it has now my global goal. It's having its adjustment. We don't have an initial state yet [00:12:20] because we've literally just started. It's getting my, what do I want to do. It's strategy. And then it has now its expertise in creative writing specializing in children's literature. Perfect. So it says splendid crafting a book, blah, blah, blah.

What themes or subjects? Are there any specific characters? What's the desired length? Any [00:12:40] preferred style? Once we have this, we can weave it. So I'm just going to say my nephew loves Legos and Nintendo and is an Adventurous boy who likes building [00:13:00] things and going on adventures. So you see I turned off the output for the telemetry.

So now it's just doing the analyzing. You don't have to look at it again if you don't want. But after this we're gonna go look at it to see what it thought. And so now just [00:13:20] coming up with the outline setting the stage, there's a mysterious game cartridge, trans like that, major challenges, okay. And so if we click here we can view the analysis, brings it up, and you can, themes, see this is interesting, it's continuing to put it into a Python kind of code story should center [00:13:40] on the boy who embarks on reflecting Yep, creating a narrative that combines the love for Legos, Nintendo, and adventure.

There you go. Expertise in creative writing, specializing in children's literature. So we can keep going here. I don't think I need to. I think you get the idea. Most of you have probably seen Professor Synapse in some way, [00:14:00] but I hope this works better. It feels a little bit cleaner. The code itself is easier to understand and mess around with, so in this video I will put the GitHub with the actual prompt behind it for you to play around with, and I would love to get your feedback on [00:14:20] this.

This is going to continue to grow, and the idea is once I get this good enough, I'll move it over to the Professor Synapse, and then I'll think through what is the next stage of SuperSynapse, as always, I appreciate you all listening. I hope this is helpful and an upgrade to you, and I'm excited to see what you all do with it.

Thanks, Chatters!

