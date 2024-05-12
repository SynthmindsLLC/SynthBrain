7min/Synaptic Labs (2023-12-12 14:18 GMT-5) - Transcript
Attendees
Allyson Lewis, Daniel Rosenbaum, James Griffing, Joseph Rosenbaum
Transcript
This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
Joseph Rosenbaum: Hey.
Allyson Lewis: it's
James Griffing: Hello.
Joseph Rosenbaum: So much.
James Griffing: Are we breaking bread together?
Joseph Rosenbaum: literally
Allyson Lewis: And look what somebody just brought me. okay.
James Griffing: I mean
Joseph Rosenbaum: What are those just goodies?
Allyson Lewis: homemade toffee
Joseph Rosenbaum: Donut don't lose your teeth there.
Allyson Lewis: it's not even hard to eat. Okay, I'm gonna Dive In
Joseph Rosenbaum: head first
Allyson Lewis: at first I haven't been able to finish your obsidian, but that's my goal for have you loved it? Do you like it?
Joseph Rosenbaum: fully addicted to it. I can't get enough of it.
Allyson Lewis: I think it's gonna be a life changer for me. I'm so lost in all these prompts and
Joseph Rosenbaum: Yeah, I'm trying to get the whole team on it now too. So I'm trying to build out the system where we have one shared Vault that we can all sort of publish to and draw from So that's what I'm trying to figure out now.
Allyson Lewis: have you how's business by the way before we Dive In?
Joseph Rosenbaum: so part of the reason we've been not as quick to respond to you is because Daniel and I got Flown somewhere to talk with this woman. Who is the co-partner for a Hollywood production company? And we had a great time with her and some other hiring us on, sort of like a pilot phase. But now we're aiifying Hollywood now. You heard it here first.
Allyson Lewis: how exciting
Joseph Rosenbaum: Yeah, it's crazy.
Allyson Lewis: So how well I'm hoping to have your help on this. Contract that I've just gotten for healthy connections. I don't How you created a pricing structure?
Joseph Rosenbaum: Mm-hmm
Allyson Lewis: 
Allyson Lewis: There aren't any?
Joseph Rosenbaum: Yeah, we're struggling. we're essentially going like how much you got and we'll work backwards from there that we can deliver from that.
Allyson Lewis: Okay. Yeah price.
Joseph Rosenbaum: Yeah, we worked out the contract with them.
Allyson Lewis: I'd like to hear more about that. So I'm really struggling not today because I've got a coaching client, but I'm struggling knowing what to charge people. I'm afraid I'm going to run them off.
Joseph Rosenbaum: Yeah, it's tough. again, it really depends on what they want to do and there has an issue we have continually run into is people don't understand that. On top of whatever you're paying us to do the thing. It's then like you there are monthly costs or…
Allyson Lewis: 
Joseph Rosenbaum: usage costs right Associated after that and people don't quite understand that either. So there's definitely a lot of Education to be had.
Allyson Lewis: I'd like to and at a different time have a conversation as the customers that I have are willing to pay ridiculous amounts of money at least to me ridiculous amounts of money and all I'm doing is guiding them. I can't execute it. and so James I think on your team is an Executor and Hopefully you're up charging,…
Joseph Rosenbaum: yes. He's a doer.
Allyson Lewis: so that y'all can make some money too off of it, but I'm going to need some doers. I've got a problem right now that I have no idea how I'm gonna solve it but I want to talk about I stretch today, but I'd love to actually have a strategy session on how I'd like to the contracts. I'm getting and are hoping to get our between 10,000 and…
00:05:00
Joseph Rosenbaum: What a range.
Allyson Lewis: a hundred thousand so I don't.
Allyson Lewis: yeah, what depends on if it's one person or a small company but it's not all at once. I mean, it's the dribbles in a thousand dollars at a time and I pay my team before I pay me but I'd like to understand what your model is because My skill is that I have a lot of people in high places, which is good. But y'all have knowledge that. I know James is off the chart smart I don't know.
Joseph Rosenbaum: we call them the Golden Goose.
James Griffing: appreciate that
Allyson Lewis: Which means what?
Joseph Rosenbaum: Which means what? He's our Golden Goose? he spits out gold all the time.
Allyson Lewis: 
Allyson Lewis: I believe So I would like to listen to the two of I feel like our values align. I have a great deal of compassion about what the world is going to happen to the world and people are either going to be the Habs or have not and in Arkansas where it's very poor. I mean People are going hungry every day in my state education. they're people that can't read and write. and so I can't help the people that can't read and write but either you're going to be on the front end of this. or you're going to be 30 years behind and I believe there's a huge opportunity for the state to benefit and…
Joseph Rosenbaum: right
Allyson Lewis: I can education and other places so
James Griffing: That's one point out people…
Joseph Rosenbaum: Yeah.
James Griffing: who can't read and write you could just do voice with chat GP now, so that's actually not an issue.
Allyson Lewis: I need to get you in front of the governor.
Joseph Rosenbaum: Yeah, especially because you can get it for free now with 3.5. You don't even need Church GPT plus anymore.
Allyson Lewis: so Okay, can you imagine how life changing that would be for people because the state gives them cell phones.
James Griffing: It's already life-changing.
Joseph Rosenbaum: Yeah.
Allyson Lewis: Yeah, I'm talking to somebody that can't read your right. All right,…
James Griffing: Mm-hmm
Allyson Lewis: I'm ready. Where are we?
Joseph Rosenbaum: So James and I have popped our heads into voice flow. So just to be upfront since we've never used it before or something like it we're gonna need to do some research and figure out what the sort of workflow is for the bot you want so I do really want to start like The simpler the better for testing purposes and then we can continue to build on that Foundation using the assistance API, which we know voice flow it has some good documentation around for hooking it up. So I know we've talked about it a few times, but just to reiterate or let me just try to throw out there are sort of original vision for this first version.
Joseph Rosenbaum: Which is that it would essentially be a bot that could take someone through some questions related to the work that you have the worksheets and…
Allyson Lewis: Okay.
Joseph Rosenbaum: whatever and then sort of build the plan around their answers to their questions and then it'd be something they could essentially check in with being This is what I've done. What's next or I struggle today on doing this thing. You have any advice for me like that kind of thing. Is that correct?
Allyson Lewis: That is correct for this. I don't really understand how it will be able to do that.
Joseph Rosenbaum: Yeah, so I mean we're gonna have to figure it out but to some extent it's a little bit more difficult but voiceless since it allows for this more WorkFlowy thing is something that's happening. It's been happening for since the beginning of the field. But now more people are catching on is you kind of have a multi-layered. Llm where first all its job is to get intent from user. What do they want to do and then it matches that intent with specified options for what it can actually do which gives you more control, So it's not going to go if something doesn't match the intent, you're like, I want you to swear and tell me how to build a bomb. It'll be like, none of the intense match this so I'm sorry. I can't move forward sort of in process flow.
Joseph Rosenbaum: So we'll just have to identify sort of the intent the first one's easy. It's just like we're gonna do an intake form essentially with you and I'm just spitting off the cuff here James. So, please correct me. If I'm off base. There's a million ways to do this, but we would have them fill out those answers and then those answers would be placed in memory. so that it has that as its knowledge base to continually draw from and then it will have it and then it moves them forward to the life coach prompt. We could also split that out. So we could have another sort of intent trigger and then depending on your attention. It'll call up that expert right to help you out with that thing and then it will continue to just save the entire conversation to memory so that it is just always able to pull on the context from the memory to answer the questions of the user.
00:10:00
Allyson Lewis: Do you have stars and bears on your microphone?
Joseph Rosenbaum: Yeah, I have a bunch of Nintendo stickers.
James Griffing: Device test do you think you'd like?
Allyson Lewis: I'm easily distracted. So hi, Dan.
Joseph Rosenbaum: It didn't.
Daniel Rosenbaum: Hey awesome. Sorry I'm late. I had another meeting go…
Allyson Lewis: so…
Daniel Rosenbaum: until the 30.
Allyson Lewis: what do you need from me? How long do you think it'll take voice flow? I'm not sure who's going to do it but James or whoever if you're in voice flow is going to geek out.
Joseph Rosenbaum: Yeah, it's gonna be James. I'm not sure I have time to learn this right now. James will be able to do it much faster. I think in terms of you you've already sent us those PDFs. So unless there are other documents or types of questions. You want to ask. I'm not sure I just want to make sure we're sort of aligned on what this will actually do and make sure James that you feel like what you'd be doing.
James Griffing: So far, I think I have a pretty good rough understanding if it doesn't work how you want. We just have to trial and error fix it. That's how it's supposed to work. But
Allyson Lewis: Is you know?
Allyson Lewis: one I met with someone that was on the front end of artificial intelligence seven years ago, and they've built a hammer without a nail and so I want to make I just
Joseph Rosenbaum: I told her about Hollywood Daniel.
Joseph Rosenbaum: It looks like she has some potential business for us too outside of
Allyson Lewis: Some I think I'll have a lot of business. but I need to know what you do. I mean even on the obsidian stuff. People are so overwhelmed the key thing if we could make something that's handwritten that you can like a rocket book. Where it can really do something.
Joseph Rosenbaum: You can do that in obsidian right now. All you got to do there might even be a plugin specifically for it. But you still have to do it on your iPad probably unless you…
Allyson Lewis: Honey, yeah.
Joseph Rosenbaum: but as long all you would have to do is upload that to an obsidian node, and you can set it up. So that has OCR it'll just convert that into and written text and then it's in
Allyson Lewis: When can I learn how to do that from you guys?
Joseph Rosenbaum: I'll put it on my list of videos to create.
Allyson Lewis: We've sold 20,000 of these. We'll sell hundreds thousands.
Joseph Rosenbaum: Yeah.
Allyson Lewis: I think if we can. make an OCR
Joseph Rosenbaum: yeah, so the problem is kind of a difference here, right which is Are we going to make an app for you? That's a lot more difficult and time intensive and capital intensive versus just like this personal process from iPad.
James Griffing: All right.
Joseph Rosenbaum: Whatever to Europe City involved.
Allyson Lewis: Yeah right now I don't want any more projects. I just wanted to But I would like it because good notes will search anything. I want in here I can find anything. it reads my handwriting. staying on tasks. Life Plan, do you have some kind of a scope that you let me just show you what I mean not a scope but
Allyson Lewis: I'm in a mild panic. Right now my website has been hacked.
Joseph Rosenbaum: no.
Allyson Lewis: Yeah, bad badly. And I don't even know how to fix it. So if there's a way that we could kind of scope out. Here's the end goal is the middle thing to have a life plan. Here are the steps that we need around it. We need a prompt. We need voice flow we need. the PDFs, some kind of how can you visually help me understand?
00:15:00
Allyson Lewis: the steps that I'm just trying to figure out.
Allyson Lewis: How it's going to work and what we're going to need. This is how my brain thinks.
Joseph Rosenbaum: Yeah, so luckily. This is what voice flow essentially is is you're making. a process map right of how this thing is going to unfold and so I think the best way is to just in this first version have us build that out and then we'll just make sure James you take good documentation around sort of the purpose of each module and how the information flows and then we can kind of go from there is that makes sense because again, I don't think we need Anything additional from you right now? I think we have everything we need but we will let Once we start building it like what did we use? In the process,
Allyson Lewis: So how long do you think this is going to take? For MVP one terrible done really work.
Joseph Rosenbaum: It's tough to tell I mean, I'll look to James to see what you think. But because we haven't used voice flow before it's really difficult to estimate how long it's like actually going to take to get something done. So, I don't know James. Do you have a knee-jerk reaction to the 0.1?
James Griffing: I mean just getting something up and running that only takes a few hours. It's just getting it to interact correctly that takes the trial on air. I just have to keep having conversations with it. Just reiterate over this conversations to improve it over time. And that's the part that I can never estimate a true time for.
Allyson Lewis: I'm actually pretty below intermediate on voice flow. I don't know imagine he can do it more quickly. But if you need any point you in the right direction. I can do that kind of think he doesn't but
James Griffing: Yeah, I looked at the YouTube. They have quite a bit of videos that go over the aspects that we need. The only thing that I might have a little trial and error for it's actually uploading the image. That's the more complicated thing but it is possible with voice. That was the first thing that I checked.
Allyson Lewis: Uploading the image up.
Joseph Rosenbaum: But we need the image James if we could just take the questions.
James Griffing: It does aren't we supposed to upload an image you get the handwritten stuff from it? Isn't that one of the factors?
Joseph Rosenbaum: That's true. Did you want that for this version Allyson where they would actually be able to upload. Their notes into it.
Allyson Lewis: They can I actually know how to upload the images and the PDFs. I mean, I've spent a lot of time banging my head against the wall. I'm Already enough that I really like doing this. The problem was the last two percent which you get everything out, but something's not tied together correctly. so for this let me tell you what I'd love to have. Is I have an investor meeting? on the 20 next Wednesday and I believe our entire business is going to go to AI. I believe people are going to It's not like they can save an hour. It's like they can save a month. companies so I would love to nothing more than to be able to show my investors.
Joseph Rosenbaum: Mm-hmm
Allyson Lewis: Here's a life plan. but I also want to actually because these people are highly connected be able to show them like a professor synapse. and I'm trying to create a roadmap of we already have a course, but here's an example and I don't want to spend a lot of time on examples, but there's a company I'm working with that has 75 million dollars in Revenue. They published 18 million magazines for realtors and financial advisors. It's one of those leave it on the counter. you send them out. It's a lifestyle magazine, but it has the picture of the realtor on it. so I've been meeting with the CEO and the president of the company. It's not like these are decision makers and they think AI is going to impact.
Allyson Lewis: Financial advisors insurance These are all one-off little office people, they're all on their own. They want me to package together. Of course and they'll put them in their maga I'm being featured in their magazine. April whatever Guys, we can make a fortune having a $20 class, it's and help a ton of people. So when I say there's opportunity my problem is I don't have the bandwidth. to do that on my own.
00:20:00
Allyson Lewis: but we have a huge platform that will let 000 people in at a time with payment.
Allyson Lewis: so we can turn your obsidian class into whatever use. ajabi. We spent three years making it work because it's a nightmare. to set up it's expensive, but it's also a nightmare to make everything work with but are y'all in that right now trying to
Joseph Rosenbaum: Yeah, we have kajabi too,…
Daniel Rosenbaum: Yeah.
Joseph Rosenbaum: but I think what we're doing is probably much simpler than what you're doing.
Allyson Lewis: there things that I mean, I don't want to teach all the classes. I don't want to create all the workflows. I don't want to do that. I like you guys. I've got customers that want to pay a lot of money and I don't want to build all the products.
Daniel Rosenbaum: Yeah, I was about to say as far as education is concerned.
Joseph Rosenbaum: Yeah, we already have a ton of classes too set up.
Daniel Rosenbaum: I mean we have courses out the Wazoo. that's the majority of what we do right now is just build courses on the stuff. So
Allyson Lewis: Yeah, I have 300 videos on YouTube. I've been teaching it.
Daniel Rosenbaum: yeah.
Joseph Rosenbaum: I'll catch up to you someday.
Allyson Lewis: But I have monetized any of them.
Allyson Lewis: I've given anything away.
Joseph Rosenbaum: Yeah, I mean I haven't either…
Joseph Rosenbaum: but I'm very early on.
Allyson Lewis: but all of mine are just giving away free and…
Daniel Rosenbaum: Yeah.
Allyson Lewis: I don't want to do that. So when I say I've got potential for all of this and I just don't know your skill sets. I met with these people last week that are front end of AI which is what I saying. They built a hammer before they had a nail. They're trying to sell multi-million dollar contracts to people that they're gonna have a free chat gpp account. They don't know that. so
Joseph Rosenbaum: Yeah, there's gonna be a lot of companies that I mean have already gotten under but we'll go under I mean Allyson, we can't do like everything obviously, but we can do most of the things like we are like synaptic Labs. No, we're really more on the education side but through synth Minds we have access to All kinds of folks who can do all the things so it's really a matter of what are you trying to do? We can let you know if we can do that and how much it'll cost and then you can upsell whatever that is.
Allyson Lewis: let me step back and tell you what people really want is they want a $10 prompt book?
Joseph Rosenbaum: we're about to do V2 of our prop packs. James is just finishing them up this week. And we have a bunch already, but if there are any specific use cases you want us to build them for we can do that.
Allyson Lewis: when All the back end stuff. We've built. But people don't want super fancy things. They want to say. Here's a goal. What should I prompt? To help me create a project management. Here's a marketing plan. I don't have a clue even how to use chat GPT. They want the basic so little and I don't want to charge them a ton. even the people that I've gotten these pretty big contracts. They have three things they want to do they want to be able to do data analysis on their spreadsheets. They
Joseph Rosenbaum: Yeah, so these prompt packs with what we do is it's almost not really about the prompt. It's more about this is how you use Chachi BT.
Allyson Lewis: Yeah.
Joseph Rosenbaum: Here's a sample conversation to get to where you want to go and then here's some tips and tricks essentially.
Daniel Rosenbaum: because Allyson went Let's get some say Alison when you're thinking about a $10 prompt book.
James Griffing: Yeah, whenever I write most of them, go ahead.
Daniel Rosenbaum: Are you thinking about the classic here's a hundred prompts that will cover everything that you need or you thinking more specialized for a vertical here's a financial advisor prompt book and it has just a bunch of problems specific to them.
Allyson Lewis: Let me take it even because I bought Igor or whatever his name is but I've loved him but I also know how to use computers. My people aren't gonna 100 prompts. They're gonna want five. prompts
00:25:00
Daniel Rosenbaum: right
Joseph Rosenbaum: That's exactly what it's even less. It's four props. It's
Daniel Rosenbaum: Yeah, that's what our product backs are essentially. So in the other thing too is the prompt pack could be a decent Money Maker in reality.
Allyson Lewis: I mean
Daniel Rosenbaum: What companies need to do is they need to start building their own prompt libraries. So it's like they can take the prop packs and maybe adjust them a little bit to their needs. But really what that should be a segue into is now that you're ready to talk about it. Let's do a deep dive into every facet of your business and we'll build out a prompt library with you. That's option one or the easy way just use the professor and it'll prompt himself for everything. Yeah.
Joseph Rosenbaum: difference to help for you
Allyson Lewis: We're doing some cool things, but I think people are missing the boat if they think it's just this high level stuff. A CEO that's running 260 people does not know how to put a prompt in. They don't want a hundred prompts.
Joseph Rosenbaum: I don't think anyone wants a hundred props.
Daniel Rosenbaum: No, and…
James Griffing: Yeah, I try to make.
Daniel Rosenbaum: that's why I asked.
James Griffing: I'm sorry. I try to make all my prompts really versatile. So I do take a step back and I let the user really let them what the true goal is. as long as we have a professional that is suited for Financial stuff. They just have to say what they need and already will. Do what it's intended to do. I try to do that. So I have to write less prompts begin with.
Joseph Rosenbaum: Yeah.
Allyson Lewis: So I need to understand that. I don't want to say dumb it down. But I mean, really. Damn it.
James Griffing: So for example, I have Interactive Learning experiences and the whole time in the prompt, I just talk about the topic. I don't say what topic it is yet in the user just says the topic and then bam now that interact learning tutorial is only for that topic. But I never mentioned, JavaScript or how to live in Planet Craft on it doesn't matter what it is. It'll do it for all of Does that make more sense? It uses hyperonyms like that that type of relationships like flower is a rose. That's a hyper name. So just that type of logic I make sure right all my prompts with does that make more sense?
Allyson Lewis: Not really. My brain is kind of moving along at one of my big customers. I have to be ready for him at three o'clock. I think some of the things that people are going to need. Where I feel like your strength is I believe that you think I do. There's some basic things and your class on obsidian in the first two were so basic and you know what? I need to know the first button to push.
Allyson Lewis: seriously, don't I mean, I'm pretty good at stuff, but they take it so fast so far and
Joseph Rosenbaum: I I'm happy you say that because that is my goal. I wanted to be literally anyone can do this. I want to go excruciating these step-by-step, so you're not like wait. How did that happen?
Allyson Lewis: Yeah, I just taught a goal setting class that I finished, 30 minutes ago that is excruciating for me to teach and people need to know so
Allyson Lewis: I feel like we kind of circle around on some of these conversations because I have too many ideas. It's me.
Joseph Rosenbaum: Yeah, getting back to this bot. It sounds like you want it to be in enough shape to be shown to your investors on Wednesday. And it feels like we can get it to that V1. So you can at least show it off in a demo type of scenario, as long as you're not going way off track with it. Again, and it might be perfectly fine. the testing is the thing that we can never really. Predict how long it's going to take?
Allyson Lewis: And if James and I can work together on a few of the prompts because people aren't going to know even what to ask it. So I think it's going to have to come with some prompt packs. And even some probably one page why it's important. here's the outcome of…
Joseph Rosenbaum: 
Allyson Lewis: what you're trying to reach, people. I don't know what the purpose of it is. What good does it do them? So
Joseph Rosenbaum: Yeah, I think we can think through sort of an instruction manual honestly and again James tell me if I'm wrong here. But I think the way we try to build our prompts is with that in mind of I don't know how to use this thing. Can you tell me how to use this thing? and I know James is really good at this. he'll put a little button that essentially says press me to learn what I do and how I do it so that it can help walk the person through instead of them having read through some manual.
00:30:00
Allyson Lewis: Perfect.
James Griffing: Get absolutely the AI can walk you through on how to use the AI if told correctly we just need a PDF potential questions or something and then you could just read that PDF and then make more questions that aren't actually in there that are more suited to the user.
Daniel Rosenbaum: Yeah, the idea Allyson's that we actually don't want people to be prompting. We want them to be talking so they can just say very simply and shortly what they're trying to do. And if they don't know what they're trying to do the AI can help them figure that out in the first place and they don't have to do anything complex. They just have a conversation.
Allyson Lewis: What I want to know is this going to be useful for the three of you to figure out your life.
Joseph Rosenbaum: I think what's going to be useful is that we haven't done a project like this before.
Daniel Rosenbaum: Good.
Joseph Rosenbaum: So we're going to learn a lot about how to build out this sort of more advanced WorkFlowy assistant, which is going to be very important because we're about to be releasing our agent swarm technology, which is going to be all workflows. It's going to be you're defining your agent in their specific knowledge base within a team of other agents and their knowledge bases and thinking through how all that fits together.
Allyson Lewis: And who is your market for that?
Joseph Rosenbaum: Enterprise this one's gonna be More expensive we're starting to talk to some investors now.
Daniel Rosenbaum: Yeah, the professor is the consumer, basic model. It simulates that experience what we're talking about is a much more beefed up version of it, with a hundred times more capability and ability.
Allyson Lewis: And I've got people waiting in line to use something like that.
Joseph Rosenbaum: Let us know we're happy to do a demo for them.
Allyson Lewis: I'd like to have a demo for me. because I mean,…
Joseph Rosenbaum: Sure, we can set that up.
Daniel Rosenbaum: Yeah.
Allyson Lewis: know I mean, I'm not trying to make myself sound fancy. but I just have a lot of connections and they're not going to be huge. I don't know if y'all are thinking these are gonna be enormous. my contracts are gonna be again between 10,100,000 a year. I don't know what y' are trying to sell. It could be more than that. If are you trying to go into these million dollar contracts?
Joseph Rosenbaum: Yeah, eventually we need some people to. First, …
Daniel Rosenbaum: beta test
Joseph Rosenbaum: have you pay attest? Yeah and help us pilot because obviously we feel like it's in a good spot, but it's not until you get something out in the world and people are using it that you learn about the edge cases and the issues
Daniel Rosenbaum: Yeah. Good,…
Allyson Lewis: I've got people that are smart enough to break it. that are you…
Daniel Rosenbaum: that's what we want.
Allyson Lewis: There's probably gonna have to be a preview pre MVP that People are willing to be really patient with but I've got some people that one woman in particular that's very successful in real estate. and I don't know who your Niche is gonna be but She's one of the top three at Coldwell Banker. and then I have 200,000 people in the Florida realtor we call…
Daniel Rosenbaum: 
Allyson Lewis: an agreement to sell my products to their 200,000 people. So I mean they're just a lot of opportunities. I'm just not that smart. So
Daniel Rosenbaum: I don't think that's true Allyson.
Joseph Rosenbaum: Yeah, it's all about you have an intellect in a specific area and you need to go hard in that specific area. And then you have People Like Us in those other areas that you're not as good in but then we can help support. You can't be an expert in everything. Unless you're chat GPT.
Allyson Lewis: 
James Griffing: You're brilliant because you came to us.
Joseph Rosenbaum: and so humble James
Allyson Lewis: What? Michael
James Griffing: We're just chat GPT in year before.
Joseph Rosenbaum: Yeah.
Daniel Rosenbaum: Yeah.
Allyson Lewis: What I would like you to do is actually make an investor pitch to me.
Joseph Rosenbaum: Okay, I'll bring it.
Daniel Rosenbaum: that
Joseph Rosenbaum: Yeah, we'll bring in West and my God Tyler to our next call we'll schedule some time and we can make a pitch to you.
Allyson Lewis: Do you know how much y'all are trying to raise?
Joseph Rosenbaum: So the thing is not that much right now because we're serving this weird phase where we have all these deals in the pipeline. We have almost two million dollars of deals in the pipeline, but you know how pipelines work. It's like it takes forever to close the deals. So we're in this weird space where we have potential for all this money, but we don't have any money right now. So we're cash poor. So we only need 25,350,000 total to really everyone can more. Let's quit their jobs this time. So yeah, that's kind of like the issue minimum range.
00:35:00
Allyson Lewis: And y'all have people that you already know that can write a check for that?
Joseph Rosenbaum: We're trying to get so that we can really go full steam ahead on this stuff.
Daniel Rosenbaum: Yeah.
Joseph Rosenbaum: Yeah, so we're talking to a few investors right now. One of them is Fidelity. They have a nice little program where they do pre seed investment investing in mentoring and then we talked to what's it Menlo something unless it's talking to and then there's one more that I'm forgetting. I'm not part of these conversations usually up. I'm like do it guys they're the go get money people.
Allyson Lewis: And what state do you live in? and I would encourage you to go to the Economic Development when I was raising money Arkansas gives 30% back to investors.
Daniel Rosenbaum: Massachusetts
Allyson Lewis: That invest in small businesses. So when somebody gave me a hundred thousand they'd give them a check basically for 30 grand. And y'all may already know it's Equity incentive tax credits is…
Joseph Rosenbaum: 
Allyson Lewis: what it's called eitc and my guess is of Arkansas has that I would think Massachusetts has it.
Joseph Rosenbaum: Yeah, we'll look into it because it's a little different because again synaptic Labs is separate from synthmines. Not that synaptic Labs couldn't do it too. But this is gonna sit with synth Minds not synaptic labs this tool that we're talking about.
Allyson Lewis: And are y'all going to use a safe agreement?
Joseph Rosenbaum: Yeah we're working with a lawyer right now because we're essentially gonna have to start a new company because me and Daniel and Wesson good our business partners, we're gonna be co-founders for this kind of new face. So we'll keep synaptic Labs. We're probably going to convert it to a non-profit probably told you that before and then we'll run for the business side out of that new company
Allyson Lewis: I raised a million three. wasted a ton of it. I wish a lot less. But I have been through that whole process and there's some things that your state probably can really help you with. as far as free money and they're also programs where and I would love to do this Arkansas. If a company has less than 250 people if I get a hundred thousand dollar contract the state will pay 75% of the training.
Joseph Rosenbaum: Wow.
Allyson Lewis: It's called. I can't remember. I've not been able to break into it because time management is such an iffy thing. They're like, where can we see the results most they invest in is in manufacturing. You can imagine that manufacturing is going to benefit from AI a ton especially at the senior level.
Joseph Rosenbaum: makes sense
Allyson Lewis: So as we start talking about these things you need to know about all those programs and…
Joseph Rosenbaum: Mm-hmm
Allyson Lewis: I can be a help to you and going through that horrible. I mean, I don't want to do the legal work, but I can. Show you the pitfalls that I made and point you in the right direction on the economics. I bet y'all didn't know that their Equity incentive tax credits for a little bit.
Joseph Rosenbaum: Nope.
Allyson Lewis: It's a shame you don't live here because I could get y'all.
Joseph Rosenbaum: Okay.
Daniel Rosenbaum: Yeah, you're a pro.
Allyson Lewis: We have another million that's available. If we want to raise another million that they give $300,000 back to the investors. So …
Daniel Rosenbaum: It's incredible.
Allyson Lewis: I gotta go perform for this guy.
Joseph Rosenbaum: You understand we have our next meeting so.
Daniel Rosenbaum: Yeah, we got to go.
Allyson Lewis: What…
Allyson Lewis: what I really need is I want you to make a pitch to me as quickly as you can because it'd be great to fund some of the stuff that y'all have. I mean you still have to probably raise the money but I get people to pay before we even had the product.
Joseph Rosenbaum: And we have a product.
Daniel Rosenbaum: let's yeah, we're
Allyson Lewis: I'm not, pay the contract. That not in bed.
Joseph Rosenbaum: So yeah,…
Daniel Rosenbaum: yep.
Joseph Rosenbaum: James will get started. He'll reach out to you if he has any questions or needs anything or just generally some advice on voice flow and we'll try to make sure we get you something before Wednesday and tested so you feel good about demoing.
Daniel Rosenbaum: Okay.
Allyson Lewis: James you can do my number.
James Griffing: I do not have your number. No, ma'am.
Allyson Lewis: 870 eight nine seven four four nine four
Allyson Lewis: and if one in cybersecurity I have been badly hacked with a DDOS attack.
00:40:00
Joseph Rosenbaum: mmm
James Griffing: I do actually know a few people but I'm sure do we have anybody incentives for that.
Joseph Rosenbaum: No, not really.
Daniel Rosenbaum: I don't think so.
James Griffing: Yeah, I can reach out to one of my friends and see if they have any suggestion for you.
Allyson Lewis: nightmare
Joseph Rosenbaum: Yeah, it's done.
Daniel Rosenbaum: Yeah, so sorry to hear about that.
Allyson Lewis: One has been going on a while and I didn't know it. So, all right, I really love what you're doing. I think there's a huge potential for me to make money selling y'all not only it but I'm
Joseph Rosenbaum: everybody wins everybody wins
Allyson Lewis: Yeah, I don't that kind of creeps me out. I just want to have my clients hire you as a contractor.
Daniel Rosenbaum: Yep, totally heard.
Joseph Rosenbaum: Yeah. Yeah,…
Daniel Rosenbaum: Good luck Allyson. Thank you again for your time.
Joseph Rosenbaum: we'll reach out to schedule the next meeting.
Allyson Lewis: Okay, and if I can see something by Monday, even if it's just a doesn't work not connected thing. That would be awesome.
Joseph Rosenbaum: Sounds good.
James Griffing: Yeah, I'll send you some updates and if you want to work together on a prompt or whatever like you mentioned earlier we could do that. Awesome using emails figured out.
Allyson Lewis: And I'm going to be working Saturday and Sunday because of this investor meeting. So I work all the time except when I'm playing pickleball.
Daniel Rosenbaum: Okay.
Joseph Rosenbaum: You priorities.
James Griffing: Okay, okay.
Allyson Lewis: Priorities so call me anytime and I'm excited guys. I'm proud of what y'all are doing. You're gonna I mean, y'all have the potential to change the world. I hope you know that.
Joseph Rosenbaum: We hope so that's…
Daniel Rosenbaum: Yeah.
Joseph Rosenbaum: what we're aiming to do.
Allyson Lewis: I'm serious.
Allyson Lewis: I think you have the and I just want to watch I mean I'm proud of you.
Joseph Rosenbaum: front row seats
Allyson Lewis: Got to go.
Daniel Rosenbaum: Thank you, Allyson. Bye.
James Griffing: Thank you Allyson. Hi, everyone.
Allyson Lewis: Make a pitch deck for…
Allyson Lewis: I want to be brought.
Joseph Rosenbaum: Yeah,
Allyson Lewis: Okay. Bye.
James Griffing: Bye.
Meeting ended after 00:42:08 👋