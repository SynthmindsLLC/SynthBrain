# Intermediate Cannoli

[00:00:00] 

[00:00:08] **Joseph:** Hey, chatters. So the last thing I'm going to teach you for now is about how you incorporate variables into this process for cannoli. So last time you might remember, we explored, [00:00:20] chaining together certain things. We can call in a note as context to the box here in Canoli to run through the large language model by using the squiggly brackets and then your square brackets to call in that note and Then just give it a topic or something right here and that whatever is in that note is going to be used as context to push It [00:00:40] forward and we can chain it together and separate it.

So we just have Miss Nora here just doing the introduction So that's where we're at so far. Now I want to teach you a little bit about variables. There's two different ways to use variables. The first way is what's called the floating variable. All a floating variable is a gray [00:01:00] box, floating out here in the other.

You're going to put a word you want to represent whatever is in this box, in just a single square bracket. So we're going to just say topic.

And then you take whatever you want to [00:01:20] be passed through as the actual text, goes under that. What that means is we can template out even further where we have Ms. Nora write a blog about squiggly bracket, single. [00:01:40] Square bracket. Topic. So what that does is you can change whatever you want under topic here but wherever it says topic throughout your Canoli your workflow it's going to pass through this word.

So you can take this a step further since we're [00:02:00] blogging why not just go audience We'll say My Chatters.

And we can say Tone.

Space, and let's say, Fun. [00:02:20] Conversational. We're having a good time here. Okay, these are, you can go further with this. But, more or less, these are where you're going to need to write a blog, right? We can go Miss Noora, write a blog about topic, where do you have topic? In, squiggly, single [00:02:40] bracket, tone.

For, squiggly, single bracket, audience.

And so this is the prompt libs idea. We're just subbing these things out. And what this allows us to do, is keep this consistent [00:03:00] throughout the entire cannoli but we can change things up here and they get passed through. How this is actually seeing things when you run it is Ms. Noora, write a blog about neural nets in FunConversational.

com. for audience. You've been saying that, okay, tone, I got to actually spell out tone. So it knows what I'm [00:03:20] talking about. And then, audience will be fine or, you can play with it, but now you have this templated out. So last time we got, something like this, it just started creating the outline and let's actually do that.

Let's say outline. To be [00:03:40] specific, and I'll show you why in a minute. Okay, so let's run this just to see what happens.

So yeah, here we go.

This is like a funner tone. It's very different. You can see how it's come out and then hey, they're [00:04:00] my chatters. Great. Love it. Love it. there's another type of variable. which is you can give a variable to these arrows. So if we double click an arrow, you can actually type stuff in the arrow. And so what we can do is call this outline. [00:04:20] And now this becomes a variable. Okay, so now we can say based on And this is no square brackets, just squiggly.

Let me type in outline.

And now whatever got passed through here is going to get [00:04:40] passed through here as context. You can probably start to see how these API calls might, churn up a little bit fast if you're doing much longer things, so it's important to modularize. But then the idea here, when, we would just take this.

Ctrl [00:05:00] C to copy. Ctrl V. We're going to pull this down.

And now if we lead out here. But instead of introduction, we tell it to do the brainy inspiration. Or no. See this is what we got. It's going to come up [00:05:20] with something different every time. So we've got to think through this, right? We want to say outline, we'll say write a numbered log outline with 5 sections, so we can be specific here.[00:05:40] 

But actually, let's just do 2 sections, we'll do 3 sections. We'll do 3 sections, so we can do beginning, middle, and end and then we're going to do right section 1. We're going to say[00:06:00] 

right section 2. We're going to say well, we'll come from, uh, down here. We'll say right section 3. And this is one [00:06:20] of those things that's annoying, because while I was doing this I was like, Ah, I should have done I should have done this, but remember we have these variables up here, so if we want to keep it consistent, we can say in

tone for [00:06:40] audience.

But now I have to go and copy and paste that for everything, so there we go. This is the time consuming part of a cannoli, is you're like, Oh, I should have done this to make it more efficient. Then you have to go back and you've already copied all these things, so you have to go back and copy it all. All this is to [00:07:00] say is it takes some playing around.

Even me knowing how to, use it, you start to think about it. And that's the great thing, is you can continue to improve it. You find these optimizations. Okay, so we have our three sections. The idea here is this outline is going to get past to here. And this is important because it needs to know where it is in the process so [00:07:20] far.

If you wanted you could also feed these to each other first. You could feed this answer, we're going to just do like this, into each one. And that way it's also just continuing it. But again this drives up the cost because now it's pulling in not just the outline, But also [00:07:40] the whole section that I wrote before.

So you're going to want to play around with it, it might not make a difference for you. But let's just let's run through it. I think we're in a good spot to, to write this blog and get you all started on, using Canoli. So starting off, as a reminder, we have the Miss Noora prompt behind here.

We've asked her to write a [00:08:00] numbered blog outline with three sections about neural nets in neural networks. Fun conversational tone for my chatters. She does her thing, three sections. Now we're passing here, so Miss Nora, the prompt again, based on outline, write section one in tone for audience. [00:08:20] We have our introduction.

It's more or less following that. Since we have sequenced it, normally if I didn't run these arrows through it would parallelize, try saying that 10 times fast, these three. So I'd write them all at once, so it'd actually be much faster and again less [00:08:40] expensive because you're not running through each one.

Play around with it. You don't need to run these through and it'll go much faster if you don't. Okay, it cost me 11 cents, not bad. Learning to learn. And then our third one. There you go. Okay, now the final thing we're going to [00:09:00] do here is put it all together. So there's one thing I haven't quite figured out yet, which is how to make it create a new note with the name you want.

[00:09:10] **Joseph:** That's okay, I hope maybe you'll figure it out. You can teach me something. The idea here, though, is we want to get everything into the end, like in one spot. [00:09:20] Okay? How we do that is you can bring in the outputs from all of these into a final box input. And again, if you feel like it, you can just go block by block, copy paste into another note, but I'm just going to show you how to run everything into a single [00:09:40] output.

Okay, so we're connecting all to this one box. And what we're going to want to do is create a variable here. We're going to go sec1, sec2, sec3. You [00:10:00] can name these whatever you want, the only thing is you've got to keep it consistent, so this section1, section2, section3, we come into this box that we're funneling into, and you do double quotation mark here.

You can do enter, whatever. Sec1. [00:10:20] Sec2. Sec3. And then we

end with the doubles. Now all this is telling it to do is I want you to [00:10:40] pull everything that I'm calling out in these variables into this format. And keep it grey. And then we just do a purple box here at the end to funnel the final thing out. We'll make this bigger And we'll run this cannoli hopefully for the last time so you'll see how it [00:11:00] puts it all together And we can have our blog on neural nets Okay, so one last time we got Miss Neuro coming in she's writing this blog with three sections Using these floating variables that we've created and again that you can change if you want She's gonna come up with our [00:11:20] outline with the three sections That then gets fed to section 1.

It outputs this. This gets fed into section 2, so it continues. Again, with the same tone audience, we're saying you're doing section 2. [00:11:40] Now neural nets, yup. And then that gets passed down to section 3.

Now remember, this is going to take longer because you're passing it down the line. This didn't just get the outline, it also got this, the intro, the middle, and now the end. Okay, let's [00:12:00] follow it up. Oh no, it didn't work! No!

I bet I have to make this purple. Yeah, I'm sure I do. Okay. We're gonna, we're gonna waste 12 more sets here. But actually, let's take this opportunity to change things up. Let's say I wanted to change the tone. We're gonna say professional. [00:12:20] Highly technical. Okay. And we're going to say an audience of machine learning experts.

Okay. And let's see how this changes things. So that means anywhere it says tone or audience, it's now filling in with machine learning experts and [00:12:40] professional highly technical.

Okay, so this is much shorter, which is good. It's feeding in again. You guys are gonna, I'm gonna zoom out just so you can see it processing on the higher level. And remember, I changed this box to purple. I'm hopeful that, [00:13:00] that makes it work this time. Oh, man.

Ooh, that one was only twelve, or eleven cents. Oh, and here we go, it worked. See how it pulled all the different sections together? Now you just click in, you can do control or command A, whatever you have [00:13:20] as a computer. Create a new note.

Paste that in, and here you go. We have our highly technical professional blog about neural networks. So that's it. I recommend you go off on your adventure now. There is again, there's [00:13:40] more. Oh, there's more. In Cannoli College, I recommend you check it out. There's a lot of cool things like looping, grouping, there's special arrows, you can create actions, through some JSON.

The, possibilities are like, [00:14:00] Endless. And so I'm hoping that by me teaching you these basics, you'll get into this and please share the crazy things you're doing. I'll even bring you on I just want to see. But in terms of overall, you need to be thinking about is you have some prompt you're bringing in, you have some variables, and you're trying to complete some sort of templated task.

[00:14:20] Something you can break into sections and modular pieces that you can work with. And create a toy example. And what I mean by that is start small doing one piece, right? Of that process. And then image and then like slowly build it up and test it because otherwise you [00:14:40] don't want to start off by running these huge things that don't work the way you want, and it's harder to diagnose it.

And then you end up like spending so much money on API calls, start small and build it out. I hope that was helpful, chatters, and I'm excited to see what cannolis you come up with.

