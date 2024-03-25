# Cannoli Basics

[00:00:00] Yeah.

[00:00:08] **Joseph:** Welcome back, chatters. As you can probably see if you're watching these videos right back to back, I'm wearing the same shirt. That's because I'm sitting down to just try to [00:00:20] record these a little bit in bulk, so we'll see how far I can get. Today we're going to be going over building our first Canoli, and Canoli is this plugin on Obsidian that allows you to create sort of large language model workflows, but also based on your notes, so you can pull in notes to your canvas which can be then [00:00:40] used as context and reference.

in your sort of LLM workflow. The first way to show this, and the first thing you need to know about Canoli, is when you're in Canvas, you can start a block, and we can say ask me how I am today. We'll give a little shout, [00:01:00] a little trick here. So if you double click when you're out of a box the edge of the box at the bottom, It will actually fill out the box so you can see everything.

Nice little hack there. That one's from James. Thanks, James. Okay, next so this is a gray box. And what a gray box means is that this is the message, the user message, that's [00:01:20] going to get sent to the large language model that we have set up in Canoli. Right now, if I pull this down to here, The idea is that this message is getting sent through the large language model, and now this box is gray, but if we turn it purple, this will be the [00:01:40] output.

Okay, so it's probably easiest just to show you. I'm going to click the cannoli button, and this is going to turn yellow, that means it's running, and it was quick, right? It was not a long message, so I said, ask me how I am today, it ran through, and this is what it looks like. GPT 4 spit out to us. Okay.

So that's [00:02:00] the simplest thing. Now, the second thing that you need to understand. So if we turn these back to gray, just so you can see it. Now, what we have here is a prompt chain. And what I mean by a prompt chain is that we're [00:02:20] starting the conversation. Here's a prompt. This gets fed to the LLM.

That output. gets fed into this box with this message, and then we can create another one for the output

and make it purple. And so the idea here is if I run this [00:02:40] cannoli, it's going to say, ask me how I am today. How are you today? And the classic AI response, I don't have feelings. So all that saying is that this got passed down. The chain here. You might be thinking, I don't really understand what I need to use that for.

Don't worry. We'll get there. We'll [00:03:00] get there. We just need to go over the basics, of how all of this works. And then we'll start to see how we can put these pieces together. you can call in your notes in a cannoli.

And so how we would do that

is if we do squiggly squiggly and then [00:03:20] call in a note. And let's just say I bring in a daily note from whatever the 14th was. So now when I run this, it's going to pull the text from this note and include it in this box. Okay, so [00:03:40] if we get rid of this one. We keep this one gray, but we turn this one back to purple.

And so as a reminder, all that means is that this is what's running through the large language model. And then this is what we get as an output. If I click the cannoli now, [00:04:00] it's going to run. It's taking a little longer because I had more written. And then look, it's given an actual response based on those notes.

So it's as simple as that. This is how to chain something together with one of your notes. And so you want to start thinking about what are [00:04:20] interesting ways you can be combining your notes into a large language model output. How do you template out this system? The last thing, just to hammer this home, is that a note can be a prompt, right?

Whatever you put in a note is getting used as the text. [00:04:40] And for example, squiggly, bracket bracket, if I want to bring Miss Nura into here, and I say just neural nets, we'll see what she comes up with. Just rubbing the cannoli. That's it.

Yeah, that took longer. It's telling me the [00:05:00] cost of that cannoli. It's not too bad, two cents. And here it is. I asked for neural networks, and her job is to essentially create wiki art type articles for me. And here it is, and she's actually even backlinked potential notes. My dog really wants attention right now I'm gonna have to pet her with one hand while I keep talking. [00:05:20] So Miss Noora's job, if we go to her note, is essentially just to help me, research things. And communicate them, and has a little personality. You know Miss Noora, if you've watched any of my other videos.

And I'll be talking more about her as well in terms of what I'm thinking for her in the future. But if we go back [00:05:40] to our cannoli here, this is a very different response, right? Than what we got in the hi, how are you situation? Yes, Desi, I'm sorry. I'm sorry to stop petting you. So she's outlined this quite lengthy thing here for us, which is great.

But here's the point is if I [00:06:00] were doing this on. chat gbt i would then have to go like piece by piece but in here i can start to separate this out like now the cat's here everyone wants attention guys yes i got you we're doing good oh my god you're gonna get some kitty butt i'm [00:06:20] gonna leave some of this in here for you edible lovers but feel free to skip forward

So Miss Nura is meant to help me like look and create, research articles more or less and things and look at the great job. She created all these perfect little backlinks for me. I'm sure I have some of these too, but now it's like I can go deeper into any of these by just [00:06:40] bringing out a box and essentially being like, okay, pass this forward and just write the introduction to neural nets.

Thanks. So I can say,

let's make sure this is a gray box write the introduction to neural [00:07:00] nets, okay, but, let's continue on with our good friend Ms. Neura. I can click there, and now it's going to be the Ms. Neura who's writing the introduction to the neural nets.

And we'll just put a purple one here so that we can see it going.[00:07:20] 

Now here's here's the thing too about these purple ones. Once you get a good flow down, you can skip the purple ones like we talked about. You can just pass it on to the next one. So we'll get into that more, but you, when you're testing in the beginning, you're going to want to be able to check piece by piece [00:07:40] because, again, some of these longer ones can get a little expensive, we're creating this little toy version here, where now, just make sure you're purple, we'll run the cannoli, and so we'll go from Miss Noora, essentially teaching me about neural nets. She's probably going to come up with some kind of [00:08:00] outline again.

This outline then gets passed forward to Miss Noora right at the introduction to neural nets. So now that's running. And here we go. Introduction to neural nets. So there you go. This is a very simple, little flow here. [00:08:20] You can create any sort of prompt you want as a note. You give it what that needs to do.

It creates an outline, for example, but whatever that next step is in the phase, and then you can break that work up into individual nodes, leading to just the introduction. [00:08:40] And then you would go through and do each of these one by one. So that's it for today. I hope that was helpful. I hope you can start to see The potential uh, here, especially with being able to pull in these guys.

So thanks for listening and I will see you [00:09:00] in the next one.

