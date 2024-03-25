# Ilya Sutskever

**Joseph:** [00:00:00] welcome back folks to voices in AI here with my buddy l dod. And we're continuing our series on OpenAI, as you can [00:00:10] probably tell. We're recording all of these in one go. We didn't feel like changing our shirts or location. Just gotta run right through them.

And [00:00:20] today 

**Eldad:** productivity. 

**Joseph:** All about productivity. Are we real or are we AI? I don't even know anymore. But today we're talking about one of my favorite people in AI, [00:00:30] Ilya Tskever, who is the chief scientist over at OpenAI and has made one of the largest [00:00:40] marks in contemporary AI than anyone else 

**Eldad:** And corporate. And corporate history too, 

**Joseph:** And corporate history too second [00:00:50] maybe only to Demis Hassabis over at DeepMind. And he's had quite the he's been the protege of quite a few incredible people as [00:01:00] well. It might be interesting though he has a very different, I'd say, compared to a lot of people paths to where he ended up.

I'd be [00:01:10] curious, Eldad, you want to share a little bit about his background?

**Eldad:** Yeah, he is, I remember, Russian by birth, but they emigrated pretty early to Israel, [00:01:20] and then he studied there and then went into Canada to to get some of his degrees, at the University of Toronto. He worked with Geoffrey Hinton one of the godfathers of AI. He [00:01:30] also worked with Andrew Neng NG, I

never know how to pronounce that.

From Stanford. Currently Stanford. I think he was at Stanford at the time as well. And with Google Brain. He, [00:01:40] Ilya is considered, one of the foremost experts on neural networks. He, doesn't fully, even though he worked very closely with Jeffrey Hinton, he doesn't completely [00:01:50] believe, in the doomsday scenarios that Hinton is now.

But he's, his background is really interesting. I can't remember the name of the other gentleman they worked on with Alex net.

**Joseph:** Was [00:02:00] Alex.

**Eldad:** Yeah, yes, but the surname, 

**Joseph:** Yeah, I don't remember his 

**Eldad:** yeah, it starts with a K and but that was all about, kind of image recognition and so forth and [00:02:10] categorizing objects and helping, neural networks do that. As well as, he's part of the whole AlphaGo story that, we're, many of us are well aware of because, that was the first time a computer beat a [00:02:20] human in that that game. He's, and TensorFlow, right? He was at Google Brain and worked with TensorFlow, which TensorFlow is now their open source thing for LLMs that [00:02:30] they're making available to everyone. Available to everyone, but who knows what all Google tends to do with their open source stuff.

**Joseph:** They'll keep that, they'll keep that open. [00:02:40] That's been around for a while to help model not just LLMs, but all kinds of neural networks. You can even go test it out [00:02:50] online and mess around with it. I actually remember, in another life I ran this initiative in Boston to get kids more into STEM and one of the field trips we did [00:03:00] was to Google.

I actually went to Google a few times over in Cambridge, north of the city. 

**Eldad:** wow. 

**Joseph:** And I remember this was, [00:03:10] I don't know, when was this, like? Maybe 2016 or something saw this guy talking and they were in unveiling or showing off the system online [00:03:20] to mess around with neural networks and creating artificial 

**Eldad:** Oh, wow. 

**Joseph:** I remember back then being like, what am I looking at right now?

**Eldad:** Yeah.

**Joseph:** [00:03:30] Who knew these years later, I'd be like now trying to educate people on how this stuff works.

**Eldad:** Yeah, that's cool. I think I'm pretty certain [00:03:40] TensorFlow, I was talking to a relative uh, my wife's, who's in New York and his kids are all in the robotics club at their high school. I'm pretty certain that they're doing quite a bit with, tensor flow and [00:03:50] optometry. So that, like the robo vac thing, that it knows where it is without actually,

because normally in robotics, what happens is you. Yes, yeah. In robotics, what they had [00:04:00] to do is, go three steps forward, two to the right, yeah, and so forth. And this now with TensorFlow is allowing them to have robots that they can, not in a sense program, but [00:04:10] it is programmed to observe and react. So if you think it's doing that with high school high schoolers, who knows what, people who are more [00:04:20] experienced and professional are going to bring out.

**Joseph:** I know. One of the, obviously AlexNet is one of the more famous ones, even though, Ilya played a huge role in that, [00:04:30] but he was a supporting role. The thing that he's probably best known for before all the OpenAI stuff was sequence to [00:04:40] sequence learning. Also called Word2Vec.

And this was like 

**Eldad:** Order to Vec? Word 

**Joseph:** number 2 [00:04:50] Vec. And the, this is like a precursor ish to, the transformer architecture, but the idea was you have this [00:05:00] encoder decoder. Encoder, you're taking one modality, you're Translating that into math, essentially, and then that gets decoded in the other [00:05:10] modality or whatever you're trying to transition to.

For example, translating from English to French, the OG [00:05:20] Google Translate that wasn't so great. That's essentially what it was doing and what all this technology more or less does right now. It's taking your input, it's encoding [00:05:30] that, and then it decodes it into the output that you're looking for.

The, this eventually led to Transformer and the Transformer architecture what was the add on to this and the [00:05:40] breakthrough was an attention mechanism. So that it, the problem with the original Google Translate is it couldn't do context. So it would just like literally [00:05:50] translate word for word.

And we all know Depending on the context, that doesn't really work. And so the the breakthrough with the transformers was it's looking at the [00:06:00] context of everything. It's done so far to help inform what that next word or whatever it is, might be. So this was like the ma, like the major pre-B [00:06:10] breakthrough to what now we all understand as in what we're using every day with Jet GPT.

**Eldad:** No, that's cool. That's cool. Yeah. Word Transformer [00:06:20] reminded me something about, Miramarati. It was also part of the OpenAI leadership that we've covered. And, she talks about some of the, her interviews, how she was fascinated with [00:06:30] capacitors and what they could do to help in a project that she was working on, very early in her life. And, it's when you think about it we always envision that [00:06:40] people at Ilya's level, or even at hers, are, almost pure theory and helping push, domain forward because of where they're [00:06:50] exploring. But, their knowledge is coming from being so hands on with the details.

And the other, thing that got me thinking in here as well is, neural networks, that's the whole exploration [00:07:00] of kind of, how the human brain works and trying to, in a sense, I'll say, digitize it, right? It may not be 100 percent accurate, but and both of them Ilya and Miro [00:07:10] speak pretty openly about their own fascination is, teens and so forth about how the brain works, right?

And so that's a natural carry over into AI. And to have your chief,[00:07:20] research scientist already thinking, or with that is his I won't say foundation, thinking with it is an [00:07:30] active part. Makes you think that, the ethical considerations, which seemed to always get talked about, it seems inherent.

If you're talking about, how the brain thinks, [00:07:40] you would hope that is, morals and values are part of the fascinating part of how the hell did that evolve from our brains. [00:07:50] Yeah.

**Joseph:** of an earlier. episode on the spectrum of conservatism and safety. Ultimately, Ilya is incredibly [00:08:00] optimistic, but he is very aware and focused on the safety of these systems. He [00:08:10] was the one who pushed for, what is called the super alignment team over at OpenAI.

And pushed to get the dedication of resources in this area. And is [00:08:20] really the one, I think, holding the flag in a practical sense up around the safety. And we can we can speculate all day about, the [00:08:30] firing of Sam Altman. We can talk about that a little later, but I think that is really his stick in the ground at the organization, and I think probably part of the [00:08:40] reason why he was willing to give up a very, like, surefire career at Google or wherever else to leave and help create this,[00:08:50] nonprofit focused on AI, I think With Sam and Greg and, depending on who you listen to Both Sam and [00:09:00] Elon Musk were very heavily responsible for courting him to bring him over.

It wasn't necessarily a sure thing.

**Eldad:** Yeah. It's hard to [00:09:10] get somebody to leave Google in deep mind, right? You're just working with a pretty remarkable team at that place. Yeah, there's a couple stories about him that I picked up on that that came out [00:09:20] of the same reading, but his involvement with AlphaGo while that's, is very interesting because, we all know now what happened AlphaGo beat Lee [00:09:30] Sodol, if I remember the name correct the best human player in the world but what it was is, and why Ilya is I think one of his passion points is, AI is definitely going to outmatch humans, [00:09:40] right?

And this AlphaGo experience showed that, right? And we're talking about something that's now, years old. Where it made moves that had never been [00:09:50] seen before in human history. So it's ability to compute and come up with a creative solution. It's fascinating. The other one that I like [00:10:00] about him as a character in many ways is when NVIDIA released their chips, he was working at the I think at the University of Toronto. And he drove down to get them [00:10:10] and this was one of their first, if not the first, right? Super high power chip. And they were saying that they would only allow one chip to be, per person. And he loaded up his [00:10:20] trunk somehow,

**Joseph:** Yeah.

**Eldad:** And took that back into the projects of, that he was doing with Jeffrey Hinton. The joking, like what if he hadn't done that? [00:10:30] Would we be years behind or, and so he's a guy who will push limits and we hope because he's the research scientist that he's [00:10:40] approaching it, with with the ethics and everything in place, because it'd be interesting to see how his day to day. Impacts the company's strategic, not just strategically, [00:10:50] but more tactically and what's being operated.

**Joseph:** Yeah, he I really like listening to him too. If you haven't [00:11:00] yet, go watch like an interview with him. He is just thoughtful in all of it. He's the type of person who will take two to three seconds to really think through [00:11:10] his response. And then what marches out is just like the perfect communication of what he's trying to articulate in a very non [00:11:20] technical if you listen to him, you wouldn't think Oh, this guy essentially speaks math fluently.

You just say this is a great, science communicator. He's [00:11:30] so good at bringing it down to that level. Which, I think that is one of the real signs of [00:11:40] intelligence. This is like a famous quote. I don't know who said it. But it's if you can't explain it in a simple way, then you don't know it.

And I feel like he really [00:11:50] embodies that he's really able to take these incredibly complex and difficult to understand things and break them down in a way that, you can understand.

**Eldad:** Yeah, he is [00:12:00] actually one of the more visible, open AI people on TED talks and YouTube and, and so forth. Which makes sense, right? Because a lot of his kind of research is going to be what's driving, things [00:12:10] behind the company. And then I imagine Greg Brockman is sitting 80 to a hundred hours in a week to start decoding, to bring him to life.

But yeah, no, he's he's very interesting [00:12:20] and, and we've hinted at it. I don't know if we really want to go in depth about it, but, the, I made the joke, he's gonna be very important in corporate history because it was him [00:12:30] flagging things. That led to, the ouster of Sam Altman. And, whatever happened there, it's fascinating to see that, that such a [00:12:40] prominent voice within the company be the one that, created that, right? Usually you would think that something like that would either happen straight from a board or from [00:12:50] things bubbling up from underneath, is a mass movement kind of thing, not just one, not a whistleblower, but, and I'm not saying that Ilya was, but[00:13:00] 

**Joseph:** Yeah, so there, there, there's one important research paper to talk about [00:13:10] here. That came out right around this time. It's called let's verify step by step. And if you've used SuperSynapse [00:13:20] before it takes a similar idea. I call it telemetry of thought, which is the idea of originally it was a chain of thought.

It's just it lets things step by step. You have [00:13:30] the LLM map out the steps it's going to take. But the cool idea that they've been working on which was not possible before GPT 4, is [00:13:40] You have the LLM outline the steps to solve like a math problem or whatever it would be, it's reasoning, and then you [00:13:50] have a person or another LLM go through and critique the reasoning to point out where did the reasoning [00:14:00] go wrong.

Even if you got the right answer, where did the reasoning go wrong so that it can continue to train itself to verify those logical steps. [00:14:10] And actually get to the right answer, but it's not just important, for the process of okay, let's follow this reasoning to get to that answer. It's also in terms of alignment, [00:14:20] because this allows us to have transparency into the actions taken by the AI, right?

So I, for example, do not need to know how the [00:14:30] brain works to be able to show someone the steps to solve a math problem. I just need to outline those reasoning steps like [00:14:40] transparently that in a way that you can follow to arrive at the solution using those axioms, those proofs, whatever it might be to get to that answer.[00:14:50] 

So it feels like this is the way the field is moving in terms of transparency is we're probably not going to solve the black box problem anytime soon. But if we can [00:15:00] tie actions of an AI. to what it's actually outputting as it's reasoning, then that is at least a first step.

**Eldad:** Yes. Yeah. Yeah. [00:15:10] And it's interesting that you call that out because it's, it connects to a project that I'm working on right now with For myself and for us at SynthMinds, right? I was fortunate enough to [00:15:20] work at Ogilvy for a period of time and, know some of their process documents and so forth. That we have. I'm trying to train a GPT to, in a sense, [00:15:30] use those processes, right? So that you can help with kind of the whole, what Ogilvy does, right? From branding to the actual content ad. [00:15:40] messaging, etc. And I could see by uploading the documents that I have that the, it wasn't really getting it.

It kept saying could be or appears and, from what it was [00:15:50] inferring from the information. Even though it overall understood the process, right? And so I said, how do I make this easier for you? And it said, just what you were saying, hell, show [00:16:00] me step by step, right? And as much as we are fascinated by this technology. That is a I and what he can produce because of what it already knows from, [00:16:10] crawling. God knows what percentage of the Internet up to April 2023 and open a ice case. It's, it still needs to be trained like a child [00:16:20] and, that is the part that, we're fortunate that there are other engineers and people doing at these companies. But if you can remember that when you're [00:16:30] struggling to get it to work, to do what you want, you got to take that, okay, it's, we're asking it, explain it to me as if I'm 10

or five, [00:16:40] right? No man, you're going to have to go explain what is branding?

**Joseph:** Goes both ways.

**Eldad:** Yeah. And that I think is the hardest part, because suddenly you've got to really break [00:16:50] down your own things. that you're asking into such a simple conceptual language, right? To help train a model. [00:17:00] And that's a unique skill. Yeah. That's not prompt engineering that, that goes beyond it in my mind.

**Joseph:** But what we are, this is going to accelerate, [00:17:10] we're going to overcome this hurdle I think faster than you think because the way this study was done is essentially, they trained this critic model to [00:17:20] be able to point out the logical problems. So the reasoning problems. And so now you can create all this synthetic data and opportunities and [00:17:30] just have, do that training, just have some spot checking, and it's going to continue to build faster and faster.

And, I think what we're going to start the next sort of [00:17:40] phase. Another really interesting paper. I don't know if you've ever read Daniel Kahneman's Thinking Fast and Slow, but it's this idea of a system one, system two, system one [00:17:50] being your quick intuition, system two being the things you have to stop, tend to, and process.

Right now, LLMs are purely system one, [00:18:00] unless you hack it together, and I think what we're going to see in this next iteration is we're going to have a system two. in these large language models that are able to actually [00:18:10] stop and consider things step by step if it needs it.

**Eldad:** Yeah. I won't just be taking a breath. It will actually be doing real work.

**Joseph:** Yeah. [00:18:20] Yeah, so I think, just to end on the controversy here, Ilya was on the board. It's unclear whether he was leading the [00:18:30] effort or how he was actually involved, but at the end of the day, he was part of the votes to oust Altman, and then and we don't know why, but, we can assume it's, there [00:18:40] was obviously something that Altman was doing that, spooked Ilya and maybe went against his sort of strong ethical code and direction.

And but then he [00:18:50] flipped. I think when he saw that, oh no, if Sam and Greg leave with the company to just go be at Microsoft. That is going to do [00:19:00] more harm than good. It completely flipped on him. Where at least if everyone is staying at OpenAI, he has some control. He can [00:19:10] manage the safety efforts.

Whereas if everyone hops ship, it's him alone. Without the resources necessary to continue. 

**Eldad:** that's very true.[00:19:20] 

**Joseph:** We don't know for sure. 

**Eldad:** no and a lot of people have speculated as well, right? Is it the play between profit and nonprofit, right? Because they were initially set up as a nonprofit. And what does [00:19:30] that mean, right? For what they could achieve individually, if their financial gain is their end goal, which for many of these guys, it does not seem to be. I think they know that, 

**Joseph:** mean, they're all wealthy [00:19:40] already.

**Eldad:** Exactly, right? What's the difference between a billion and two billion, right? 

**Joseph:** Yeah, at some point it doesn't matter. It shifts more towards power and trying to [00:19:50] achieve your vision.

**Eldad:** Yes. Yes, absolutely. You do have to consider that within, where is the [00:20:00] line? And is it a new line that has been drawn by what happened between the non profit and its ethos and mission and the profit potential of what [00:20:10] it could become. I personally, from, reading about these guys and hearing their stories and seeing, some of the the interviews with them, you can see safety seems pretty [00:20:20] paramount to them.

**Joseph:** It does, I think what that actually looks like in practice, though. [00:20:30] Differs, especially once you get into the profit and competitive motives that they're all facing right now. Because At the end of the day, and why they [00:20:40] created this for profit arm of the non profit was because they could not raise money for the non profit to get to where they want, which is to, create AGI, [00:20:50] Artificial General Intelligence.

And so now, the race is on! 

**Eldad:** with that, we shall leave you. Thanks for

tuning [00:21:00] in. And we'll have another Voices in the Air for you soon.

