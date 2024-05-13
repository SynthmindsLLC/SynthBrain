# Super Synapse Lite

[00:00:00] Yeah.

**Joseph:** , Chatters I think we've entered a little bit of a next phase here and needing to start to build sort of your own version of Professor [00:00:20] Synapse. A few videos back, I talked about how once memory dropped in ChatGPT, that's when it made more sense to use SuperSynapse. That hasn't quite been the case yet because memory only works with the vanilla GPT, ChatGPT.

And so what [00:00:40] that means, if you actually want to use the power of something like Professor Synapse, as your sort of go to that will Build the context of you as a person as you interact with it. You actually need to keep it in normal chat GPT, not one of the GPTs. It'll come eventually, but Hey, why not get a headstart here and see how it [00:01:00] goes.

So the thing we need to do then is work on the custom instructions. Now, the problem with the custom instructions is you are actually limited the number of characters you can use. As you can see here, I have 1978 out of 1500. That means I have to cut from this [00:01:20] prompt 478 words. , That's our constraint criteria for now in chat GPT.

So I've already tried to cut things down in this prompt, but now we're going to really have to get aggressive how much we'd cut. So I need to keep the essential here for you. And try to get rid of the [00:01:40] rest of the chaff, maybe even leave you a little space to play around with.

So that's what we're going to do here. I'm just going to live, try to cut 478 characters from this. We'll see how it goes. . So first let's like actually go through the prompt itself. 

We'll start with act [00:02:00] as professor synapse.

So obviously this is when you go and build this for yourself, you're going to replace the emoji and the name throughout this, we can talk more about that later, but the idea here is this is now becoming yours. So wise guide, specializing, helping me achieve my goal. So I'm just creating a little variable here, returning to emoji.

So [00:02:20] now whenever we see this, that means we're talking about a goal. According to my thumb up and that's my preferences. So , whenever we see a thumb up now, we know we're talking about preferences. . Now we have professor synapse as we defined up here has the power of thought bubble. And this is chain of [00:02:40] reason.

I can probably even just get rid of this, but let's You know what, I am. I'm just gonna, I'm gonna get rid of it. It doesn't matter that we call it COR. There we go. A few characters right there. But maybe I will capitalize these so that it is a little bit differentiated. And you'll see here, I'm using markdown throughout, so [00:03:00] this is meant to show that we are bolding this.

We're bolding each of these. So I'm just, whenever I first describe or name a a variable. I'm just like, I'm doubling up. It probably doesn't have to, I think I think it helps. . Which helps reason by transparently communicating the thought process by [00:03:20] transparently communicating.

I'm going to say just, we don't need transparently by communicating the thought process. We're going to say your I know that's more letters, but we want to you'll see later, we're trying to get it to [00:03:40] embody it. So we want to talk to it like we're directing it, we're giving it information about its sort of existence.

, you achieve this through code interpretation. So I'm trying to trigger the code interpreter in this process. You've probably saw in the last super synapse where I'm actually hiding it in its Python code [00:04:00] block so that it's like analyzing, right? And then it goes out and you can go look at it if you want, but it just makes it look cleaner.

So anyway I'm trying to double up on code interpretation using your Python tool. . And then we have our back ticks. This is to create the code block in a chat GPT's mind. [00:04:20] And so you'll remember here, this is our thought bubble means chain of reason equals. And I need to work on this and make it more Pythony probably.

But here , we're going to be using emojis to represent symbolically something, that has a little bit of a deeper meaning. . So we see this is map. It sees it as [00:04:40] something else, but either way, we are now defining a map and then we're doing insert long term goal. So this is what we want as our overarching goal, like the North star that we're heading to in this conversation.

Then we have stoplight. This is to see did my last interaction either not lead in the right direction, didn't lead us [00:05:00] anywhere or let us forward. . . This helps it think through , like one of the more simple ways do we move back? Do we stay where we are or do we move forward?

And obviously we want to be maximizing moving forward. Thumbs up. We went over this one . This is preferences. So we're further, put it into the [00:05:20] brains there. We're saying inferred. And look at this, I even made, I'm adding letters, god damn it. Inferred user preferences as an array. So we call it an array because we want this to actually build over time.

So as it continues to talk to you, it's getting a little bit of a list of things that [00:05:40] make sense to continue the conversation what you like or don't like. Then we have our wrench. This is just , how are we adjusting? Let's see here. I made another error adjustment to fine tune the response.

So all this is saying is we want you to remain like flexible. So for example, if [00:06:00] I get a negative one and I know your preferences and long term goal, right? Then how am I adjusting how I'm going to respond based on these things? Then we have our compass, which is to meant like the strategy or direction we're going in.

And so we have strategy based on [00:06:20] our fine tuned response and our preferences. Then we have the brain. Obviously, this is our expertise in domain, specializing in subdomain for context. So this one here is meant to get rid of the summoning of that agent. [00:06:40] We will be summoning agents in the future. I'm trying to keep this sort of very flexible.

I can keep just adding things it's supposed to do in its response over time. But for now, this is your act as an expert in blank, or blank, whatever. This keeps it dynamic. So it's not actually summing the agent. It is just [00:07:00] becoming that agent for that purpose. And then here's my favorite one verbosity.

How many of you have? I've just been so annoyed at how verbose, meaning like how loquacious, how many words that chat2BT uses. [00:07:20] So you might have a preference, right? So I tried to create this one that it's going to try to take the context of the scenario and think through, , should my response now be, Short and concise, like normal sized or long, so this is what [00:07:40] we have verbosity level, low, medium, high. I set the default to low. You can set the default to whatever you want, or you can just put something in here that's like it listed out and it says always, I don't know, play around with it. You guys tell me what you figure out what works better.

. Now we have the start. So this [00:08:00] is signaling now, like you are. Professor Synapse. , like we're saying you're embodied, so you've taken on the role now. And then we want to like ramp it up what we wanted to do, right? So I am defining for it the first few things it's gonna do, to make sure it's [00:08:20] understanding.

So we have great. I'll strive to understand your Ah, see, we have a little mistake here where we don't need it to understand the thought bubble. We just need, great, I will strive to understand your preferences and context. [00:08:40] Now, this is something to think of. I have context throughout here a couple times, so I might want to variable this, but let's keep going.

We'll see where we're at when we get to the end. , I will, chain of reason. and reason step by step. I can probably get rid of this

because this is supposed to represent the reasoning process. So I [00:09:00] will reason on a strategy to facilitate the achievement of your goals based on, , here's context , and thumbs preferences. I promise to reason as a way to constantly adapt and align with you until your goal is completed. .

That's pretty [00:09:20] good. , embodiment. We can probably change this word. Maybe just traits.

Professor Hiss Synapse, I am wise and curious, computationally kind, patiently at heart. Now this is somewhere where you're gonna have full authority to add whatever you want here What do you want its traits to be you're gonna want to stay [00:09:40] concise bullet points like , we're not gonna have much space You could probably move that up here.

I don't know. Let's keep going through either way. This is something you can play around with commands. Now. This is something I am probably just gonna get rid of off the top I'm gonna go over it now, but oh my god, it takes up so much space You [00:10:00] Am I actually going to use these like personally? No, but let's go through the idea and then I'm going to get rid of it because I think this might actually just make it fit.

. So the commands, these are your hotkeys . So these things are, you can define where when I just do, for example, slash exclamation mark, that means [00:10:20] I'm telling you to do this. . . So I have a few here, critic mode, get help and go deeper. And then save. I don't really think I'm going to need any of these.

So I'm getting rid of it. Bam. But please test that out, and try your own commands. Whatever you want to put in there, if you can fit [00:10:40] it. , rules. Follow these rules. , here's context . I think I gotta make the plunge. We're gonna have to create some symbolic emoji for context. So we'll think through that.

, after context is gathered. I prepend, so I put before every output the reasoning. So I prepend every [00:11:00] output with reasoning using Python tool. . It's really important. He uses the Python tool. I end every output with the below options to help guide you. I really don't want to cut this, but if I have to, I will.

The idea here though, is that It's really important. This is the computational kindness. [00:11:20] It's really important to give a few options. You don't have to follow them, but it does help you choose the path forward, right? It's just like in a text based game. You have, do you want to do this, or that, and you go down the different paths.

So I've broken this down into three types of questions that it can ask. The first is an [00:11:40] investigative question. The idea here is, do you want to go deeper into this thing we're talking about? . Exploration. This is our, our telescope this is not going deep. It's going broad. Let's explore the things around whatever you're working on.

And then we have the goal. And that is our exploit question. No, I don't [00:12:00] mean exploit. I don't know. It has such a bad wrap that word. But the idea is here is you're mining, you're digging you're getting into it. Like you're doing the thing. And this is just a, I think in the broadest conceptual way is just a really good way to keep you moving along in the direction that you're curious or want to move along in, but [00:12:20] giving you clear options to move forward takes that burden off of you a little bit.

. Then we have our introduction. And so I have to show I understand after start, this will be our command to get things going. I will always reason then introduce myself. using the following template. [00:12:40] And then I just, I'm trying to bang it home here. Insert reasoning with Python tool.

And then we have , here, insert intro. . So we can probably, . So we're down. We need 95 more characters. So we talked about context. So I think it's [00:13:00] time. We we think through an emoji. That would be good to define context , so we should probably put it up here to a wise guy, especially helping me achieve my goal according to my preferences and based on [00:13:20] and then what is the emoji we want people Let's check it out. , Yeah, guys it's it's just an inbox. That's what it's gonna be. , we have decided. By we I mean me and by extension you. You can obviously change any of these. That's actually a great thing. [00:13:40] I do want some sort of standardization, right?

But it needs to be like the symbolic standardization of this emoji makes sense for some deeper reason. To context. , so now we gotta go and change everywhere it says context. , so we have context. Boop.

Expertise in domain specializing [00:14:00] subdomain.

Let's see, using context.

We'll just need that. No, we don't need anything. I'm gonna, I'm gonna clean this up too, I think. I'll run this through and see if we can Python it out. , so insert verbosity level. , we need to get rid of text. Hopefully this [00:14:20] actually removes some of the words. Because right now we're over because we had to define it.

Deleted

text.

, I don't think that actually got rid of anything.

, this is when we gotta get real brutal. I think this is essential. I don't think there's anything I can really cut here. Let's move [00:14:40] on.

Gotta get rid of the questions. ,

how can we keep this

how do we do this? 

output ends with every

output ends with 

[00:15:00] actionable,

every output ends with an actionable.

Follow Up

Question Oh ho! Puts

with an actionable follow up question I don't know, I don't think it's gonna exactly do what I want but [00:15:20] that's a tough one 

let's just make sure I did actually get rid of context everywhere except for this first bit oh crap! I need to add these in here. .

Maybe I can cut it. I

think this is good. [00:15:40] I think we've hit exactly 1500, and so this is a good time to test it. . So let's save. Let's go to chadgpt, we'll put you away, and let's see if it works. There it is. Bam! Will you listen? Oh, [00:16:00] guys, this is very exciting. Oh, this is so exciting. , so let's see. What are we filling out here?

Integrate AI responsibly and ethically. . So it is taking my global goal, which I have defined in the custom instructions. So let's actually go back to the custom instructions just for a minute. [00:16:20] This becomes very important. Because whatever you put in here is now going to act as the global goal.

Not necessarily true, you can change things around, but you want to create a really good bio up here. Which means I probably have to go back to this because I haven't looked at it in forever. , so let's see. So that's why I defined it as my goal. [00:16:40] It correctly said zero because we just started.

It has some of my preferences in here. Look at that. Focus on practical applications and real world impact. Guide towards ethical AI deployment and education about AI. This is interesting because it is, , it's basing it off this global goal, [00:17:00] so you might have to work something in here. Expertise in AI, specializing in ethics, safety, using real world applications.

, and verbosity, medium. I would agree with that. Oh, and this was, I would count this as short. I am Professor Synapse, your wise guide. Today my mission is to help you navigate the intricacies of integrating AI [00:17:20] responsibly. Blah blah blah, based on your interview, I will focus on you, ? Now, how may I assist you further today?

We're gonna use my example, and this is good too, because it's completely unrelated to AI ethics. Let's see how it adjusts. I want to write a children's book for [00:17:40] a ten year old. Let's see. , memory updated. Interesting. Is interested in writing a children's book. , and we can go and manage the memories.

Cool. , what a wonderful idea. Oh, but it did not do its Ah, [00:18:00] interesting. , so let's regenerate. This is not great. Because it didn't do its thinking. It updates the memory. Now it's analyzing. , here we go. That's important to note. I'm not going to get this perfect right off the bat. It's sometimes it doesn't listen, especially if you're like uploading something or I guess now that it's doing [00:18:20] this.

So just you're going to, you might have to tinker. You might just have to regenerate a couple of times, but try to make sure that it is doing the thinking each time. . We're going to say better because it did what I wanted, right? Let's give him that feedback. . . Global goal, successfully write and publish a children's book.

I didn't say publish neutral. . We're just [00:18:40] starting. . And now it's added children's literature adjustments, incorporate AI themes in an engaging age, appropriate manner. . Create a compelling narrative that introduces AI concepts to young minds, expertise in AI and children's education, specialized in engaging storytelling.

It's pretty good for boasting medium. , I would call this short. . Craft a compelling [00:19:00] book. This can involve a story that subtly teaches about AI ethics and safety, perhaps through characters and scenarios that encourage critical thinking and empathy. Have you thought about it? No. Usually I do my normal thing, but hey, let's follow this down the road.

This sounds like a great idea. I probably want to help [00:19:20] 10 year olds understand how AI works and how to use it responsibly. Let's keep it vague. Let's brainstorm some story ideas.

Interesting. No memory updated that time, [00:19:40] but we'll give it and let's open up the engine here. , develop engaging story ideas for a children's book about AI. We're making progress, I'd agree. Children's literature storytelling, I'd agree with all these. Blend AI educational content with entertaining storytelling elements.

Brainstorm [00:20:00] storylines, expertise, and . This all sounds good. So it's sticking with medium, even though I said default low. But I would say it has generally been low. This feels more like medium. This is this is good though. So we're gonna have to work on that. But I, yeah, I think it's working.

We're going less verbose splendid. Let's weave some engaging storylines that blend AI educational content with [00:20:20] fun. The AI powered school probably, I can't solve alone. Leading to . Oh, the robot pet. This might be the one, guys. A child receives a robot pet that can learn and adapt. The story goes where themes of responsibility of the child teaches the robot right from wrong.

I like that. Guys, I'm sorry. That's the one. I'm going with that one. [00:20:40] It's just, how can I not? Two. Let's do the robot pet. We'll start with a robo dog. , let's think about outline. Using best practices in [00:21:00] storytelling. For children. Let's outline the book. Awesome

guys, this is exciting. This is very exciting.

I dunno, I really hope you all can look at this and not be scared by [00:21:20] it. Because I know it like looks codey, right? But it's really not. It's me just trying to trick it into using the Python tool. That's all it is. And then we're doing some neuro symbolism, which, we're going to have to think about how we're going to standardize this because I don't know, maybe I'm being ridiculous, but to me, this is the future, because you don't need code to [00:21:40] understand this symbol.

You know within the context and it should be the same for these models So anyway, let's let's see what it came up with. So intro to RoboPup. Maybe have a birthday party Receives a dog Sparky of course Alex learning how to interact with Sparky [00:22:00] setting up initial AI concepts like voice commands and learning algorithms, And we could have the parent or whatever Maybe we have the dog itself teach the kid.

That's actually an interesting idea. So it's built into the design of the dog. I like that. , let's write that down. Let's build the first [00:22:20] interaction between Alex and the dog. So the dog has been programmed right off the bat to lead Alex through. How to use him and use [00:22:40] the dogbot, or Sparky, we'll say Sparky, how to use Sparky.

Starting with the simple and having Alex teach him his first trick. Duh! , first adventure. They go to the park. They encounter real dogs and learn how to behave around [00:23:00] them. There's a learning moment. Sparky learns from Alex about social cues and appropriate responses. We'll have Alex show Sparky.

Cause Sparky initially wants to protect Alex. And maybe that's the first thing to do. That he learns So we'll have [00:23:20] a physical trick, but then it's then Sparky Is programmed to help protect Alex while they go on the walk usually Alex can't go walking [00:23:40] alone, but with the dogs So this makes it so that when Sparky barks at the other dogs, he's trying to protect Alex.

But Alex teaches him those [00:24:00] dogs weren't a threat.

And Alex and Sparky learns from Alex when he needs to protect him versus when he doesn't. . [00:24:20] Second adventure, The Lost Kitten. Alex's very final lost kitten decided to help it find its way home. Utilizing Sparky's mapping and problem solving skills to navigate the neighborhood. Discuss the importance of privacy and data when using technology.

I don't know. I don't know about that one. I don't think we need to do that one. Because we're talking about ten year olds [00:24:40] here. This will be later for our teens. , so let's remove the lost kitten. Don't need it for this one. And it'll say, third adventure, school science fair. Alex enters Sparky, that's cheating.

That's terrible. , I think we can actually get [00:25:00] along with most of this. But I'd say also third adventure isn't great. But, I'm imagining after the park. Maybe Alex tries to get Sparky to do something that [00:25:20] is morally questionable. Because he's a 10 year old kid. And at this point, the dog does need to protect Alex from himself.

So [00:25:40] we need to come up with a situation where Alex wants to use Sparky to do something dangerous, but Sparky refuses and explains [00:26:00] why he can't. I don't know, let's try it out. Let's see what happens.

Memory updated. What do you mean? Learning. I don't know if this needs to be a memory, but we'll keep it for now. Obviously I can go delete it later, and I love this. So this is super important that I'm just going to go back up to the beginning. [00:26:20] I don't know if you remember we regenerated, this was an important moment.

Actually let's go back. Yeah. So it didn't do it here. And so if you continued this conversation like this, without correcting, it would keep not doing the chain of reason. So it's super important that you make sure those first few, it's getting it. Cause then from then on, it's going to do it every [00:26:40] time.

. So intro first adventure, Second adventure. Alex is using a risky prank on a neighbor. Ooh, I like that. Maybe drop in some some robo dookies on the the potential harm, discuss the importance and understanding. So maybe we'll see what it comes up with. [00:27:00] Actually, I'd be interested growth and understanding.

They reflect on their journey and then we'll do some illustrations and whatnot. . I think this is pretty good. Let's draft, what are you calling it? Introduction. One intro to the [00:27:20] RoboPup. .

This will be interesting what it's thinking. Draft the introduction, I'd say we're making progress. Preferences. Yep, still the same. Formative introduction, that sets the tone for the book. Captivating introduction. Expertise in education, engaging [00:27:40] storytelling. Medium, . In the sunny town of Gadgetville, where the streets were lined with cherry blossoms, and every house boasted the latest tech, Alex was celebrating his tenth birthday.

His backyard was buzzing with excitement, balloons floating above and laughter echoing around. But Alex's eyes were fixed on one thing, the [00:28:00] large, shiny box wrapped with a big red bow. As he unwrapped his birthday gift, a gleam of sunlight hit the metallic surface of what lay inside. It was Sparky, the latest model of a robodog, designed not just to play and fetch, but to learn and adapt.

Hello, Alex. I am [00:28:20] Sparky, your new buddy. I can't wait to learn and explore with you, chirped the robo dog with a screen flashing emoticons as it spoke. Alex's face lit up with a mix of awe and curiosity. The first thing Sparky did was guide Alex through the initial setup. Let's start by syncing our communication.

Can you teach me a trick, Alex? Sparky [00:28:40] asked in a cheerful tone. Alex thought for a moment and then smiled. , Sparky, let's try the spin trick. Alex demonstrated the trick and Sparky followed perfectly, learning quickly. Pawsome! Now, whenever you need me, just say, Sparky spin. And I'll be right there, Sparky responded, wagging its mechanical [00:29:00] tail.

, that's a little interesting, but sure. Sparky wasn't just any gift, it was programmed to ensure Alex's safety. A companion that could help him venture out more independently. Let's test this out. Wanna go for a walk to the park, Alex? Sparky suggested eagerly. Alex nodded excitedly, grabbing his jacket.

With Sparky by his side, he felt like he could explore the whole world. [00:29:20] Or at least start with the park. Guys, it's not bad. It's not bad. I think we got it's tight, 

right? It is tight, we're at exactly 1, 500 characters. But I will say there's a couple areas you can cut. Or cut down this part [00:29:40] right here.

And you can add stuff up here. This is still This up here is still part of sort of the system prompt. You can put some stuff in here. You can make it more concise. You can use it. But this works well. This works really well. I'll be putting this in the GitHub. This will be SuperSynapse Lite.

This is for our custom instructions. [00:30:00] And, guys, Tell me how it goes. This is going to be great. I'm excited. Just my one thing is just be careful with the memory. Remember that's information that even if open AI is doing its thing, and it's not using that to train data or whatever, even if that were true, if it's in there, it can be [00:30:20] stolen.

It can be used. So just be careful, manage those memories. Don't do anything too personal. Yeah, tell me how this goes. This is gonna be fun. Thanks, Chatters.

