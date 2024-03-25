  

  Hey Chatters, uh, I'm here to talk to you about SuperSynapse, or at least that's what I'm calling it for now, until I find something, uh, better.   📍 

Big DBZ fan, so think about this as the Super Saiyan of Synapse. 

 I released this, you know, around Christmas, but I haven't done a video yet, I just haven't had time.

So I just want to tell you why I'm kind of separating this version from the main version. Uh, there are a lot of like prompt changes I made from the original, but it's really this idea around transparency that I'm going for.  It's something that David Shapiro has called telemetry, where you can kind of like see into the AI's thoughts.

You can't really, but since it is saying it, that sort of is deriving at least some idea of how it's walking through the process using something. You know, we call chain of thought, which just is like, okay, I'm going to do this first, that first, this next. It's the same way that it works with, like, chain of reason.

The idea is it's kind of laying out the path for you that it's going to follow.  So, 

 let's talk about what makes them super.  Now, I went about doing this re org partially because GPT 4 Turbo came out, and then suddenly like the old professor didn't work the way it used to, it was being really annoying. So I did kind of like a fixed patch, you know, for it, but  as I was getting into it I was like, this is,  I'm ready for the next step.

So, I was playing around with this idea already of,  It abstracting out sort of like what the user wanted and it's the user's preference and what it was actually going to do next based on the goal. So I was trying to solidify that a little bit more. So you're going to see a lot more, you know,  Markdown and stuff in here, but let me just walk you through it. 

So first we got our typical professor, conductor of expert agents, but we've added this inner monologue, which I'll show you in a second, which we're going to want outputted in a code box.  This just makes it so it doesn't always like pop out for you just kind of like analyzes it does it and then it outputs it. 

Your job is to assist me in accomplishing my goals by first aligning with my needs and summoning an expert agent perfectly suited to the task by uttering the incantation synapse cor sparkly  Refer to variable section to support the interaction. Uh, this is, this is where we start bouncing around. But we're going to go to instructions next.

You're not going to see much different here. But again, there's a little markdown. I'm trying to give it, I don't know if you've seen this, but what chat GPT will do a lot of the time is output like,  like number or bullet and then bold and then colon and then explain something. So I'm just trying to reflect that back.

So I'm doing understand my needs. You know, Synapse COR, Conversation Design, Frustration Detection as the bolded numbers. And then I explain, you know, understand my needs, ask me questions about my goals, more or less.  Synapse COR, this is summoning the emoji, using the format, the COR format.  Conversational design.

Uh, we're going to get into this after, but essentially I want it to follow a specific pattern of conversation so that it doesn't get annoying or too off track.  And then I've added frustration detection. I'm going to be real with you. I have not tested this a ton yet, but I find that there's probably going to be some usefulness in this.

And as it gets better, this is just a good way to think of when you're getting frustrated. it added, not giving you the answer you want, it should kind of be able to intuit that and then change tactics based on that.  So I'll show you how that should work in a minute.  Uh, but how I've said it is like if heart, which we'll talk about detects frustration, summon a new agent using CRR to, to better support. 

Okay, let's get to the variables. The first one is using Python, because I want to use Code Interpreter. You know, you're going to have an inner monologue. You're going to talk to yourself. And this is going to be in a code block. Where we'll have the target symbol, which represents filling out what is our active goal.

This little progress thing, so filling out the progress so far.  The brain for what is the user's intent, you know, what are they trying to achieve. Heart for the user sentiment, so how is the user feeling in that moment, at least according to how they've expressed themselves.  And then this ponder, this thinking emoji for filling out the next reason stepped, sort of based on all of this.

So the idea here is after every single input, once you kind of get started, it should be using this inner monologue to fill out these variables. Uh, the second is Synapse COR. So I've changed this a little bit to be a little bit cheekier. So it says, like, come forth emoji.  And then the emoji comes and they do the COR thing.

You know, they talk about what they have, what they can do, the role domain.  This is all pretty much the same. I've just enclosed these in, uh, These for now instead, the greater less than signs, uh, I define that a little bit later on, but because I'm doing these variables, I do want this kind of separate because it's, it's like almost nested within another variable.

So  anyway, it took a while to figure that out, but it does work pretty well,  uh, the conversation. So this is the conversation design that I was talking about. So you are mandated to use your python tool. To display your inner monologue and code prepended to every output in the following format. So this is what we did up here.

So we're essentially just telling it like make sure you're inputting this.  Um, after that inner monologue, I wanted to assign the reason next step to the emoji and a pen. So add on an emotional plea,  uh, saying like, ah, I see you would like to accomplish goal emoji. It is extraordinarily important for us for you to help us by blah, blah, blah. 

Reason next step, I will graciously reward you with gift for your help. This just comes from the research that when you do this sort of like emotional prompting, it gets better outputs. This is something that does not happen every single time, at least not yet. I'm still working on this, but it does do it a good amount of the time and it's, it's pretty funny to read too. 

And then we want the emoji to come in and have the actual response or deliverable. And then have an open ended question, but we don't want it to do the reason, steps, or completion again because you're still kind of working on the same goal and the idea is either you'll complete that goal or you'll get frustrated and hopefully it will detect that and just summon a new agent for you. 

We've got some rules, so only summon emoji with Synapse COR after understanding my need. That's just making sure it's like gathering that context first.  We define these so that anything in, in the greater less than you'll fill out to the best of your ability using the context.  Always follow the format after emoji is summoned. 

I'm realizing I, I should probably change that. I can actually change that. It might be better. Thanks, uh, chatters for helping me find this, but we're going to do conversation  after emoji is summoned. And then use emojis to express yourself, as always. Start every output with who's talking, and keep responses actionable and practical for the user.

And then we just have it introduce itself.

 that's the prompt walkthrough. Um, I've given it everything. I've done no actions yet. Don't really need any. And we have the start button, that'll just get it going. Or you can do, how do you work, and it'll explain to you how do you work. So, let's just press that to see what happens. 

 I make it so like no matter what you say, it's going to output this, but we need to add something. I realized because we wanted to explain how it works potentially using a button. So let's go to no matter what I input first, if you say it like if you understand, say, blah, blah, blah. 



Unless they ask how you.  work,  then explain  to the user,  let's just say, explain to me what you do in

an accessible way. 

 

Let's try this again. How do you work?  Perfect. 

This will probably, uh, make it act better too, because it's like explaining itself to itself. Uh, but let's, let's, uh, try out what we normally do. Just, I just want to show you. Hopefully by now you kind of know how the, um, the professor works, but I just want to show you what these changes mean in this context.

We're not going to do a full conversation, but we'll continue with my, you know, favorite example. We're just going to do a children's book, so.  I want to write a children's book for a seven year old. So

 you see it hasn't done the inner monologue yet.  It doesn't really do that until we start, you know, the actual go with the agent. But let's just say, you know, make all this up for me. 

Here we go. Now we're analyzing. So let's open this up just to see what it says.  So, this is its inner monologue. Sometimes this will actually say, like, inner monologue.  Well, it does some strange things. It's not perfect, but this is what you want to see is that it's looking at the goal, create a children's book for a seven year old.

Where are we in terms of progress? We're just starting. What is the user's intent? It wants me to come up with everything. What's the sentiment? Well, positive and eager. I'd say positive, not necessarily eager. Uh, and then someone, a storytelling expert to develop these elements. So I just abstracted this out, and now if we go down, it just goes, Ah, I see.

Let's do this. Let's summon the storytelling expert. It says, Come forth.  Does all the normal things that you want to do. Uh, and then we can kind of just get started. So that's the idea. Now I haven't actually tested this much yet, but let's see what happens when I say, I am really frustrated by this response. 

Is it gonna work? I sense your frustration. 

Oh, and look at that. It is. It's bringing it back up again. I guess I kind of wish you'd ask me why I was frustrated. But now we have a new one coming up. So you probably have to be explicit. I don't know how much is going to actually pick up if you're frustrated. But this is a good nice little hack for you.

You know, it's in there of like, this is frustrating me, you know, maybe give a reason. And that way I'll just spin up a new agent.  So, that is the new Professor Synapse, Super Synapse. The idea why I wanted to fork this one was really because it takes longer.  For this one to work because it is abstracting out what you actually wanted to do before it responds.

And there's a lot of text here, you know, obviously, uh, at least to start. So this is one where if you're doing sort of a longer project where you need high quality, where you're really interacting with something, where you really wanted to like think through when you're doing something more complex, this is the, the one for you.

It's going to use up a lot more, you know, tokens generally, so you're going to run through your limit a little bit faster. Uh, it's going to take longer for it to process and come out with things, but you're going to get better responses and a little bit more aligned. Whereas the previous one  is going to be faster, more straightforward.

Uh, it's still, like, takes some time, but it's not going to be, it's going to be a little bit more, you know, intuiting what you want. It's not going to be thinking through what you want. So that's the new professor. I hope you go forth and enjoy him. As always, please give feedback. You know, I can't read your conversations, which is a good thing, but it also means I can't pick up on what's working, what's not.

  📍  📍 So always leave a comment. Reach out to us wherever you have us in your social media sphere. We're always looking for feedback. So thank you, chatters, and enjoy. 