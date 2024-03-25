# Make Agents

**Joseph:** [00:00:00] Hey Chatters, special guest,~~ uh,~~ here with me today. ~~Uh, ~~he hasn't been on my, any of my stuff, but he's been on other SynthMinders stuff,~~ uh,~~ primarily Goda. And he, I'm gonna, I'm gonna let you introduce yourself. Why don't you talk a little bit about who you are, and,~~ uh,~~ a little bit about your learning journey, cause I know you didn't get started in AI, you just kinda ended up here like me.

**Sjoerd:** Hi, I'm,~~ uh,~~ I'm Sjoerd from the Netherlands and,~~ uh,~~ basically since ChatGPT came out I've been,~~ um,~~ working with it, working on it,~~ um,~~ doing a whole bunch of different things,~~ um,~~ a whole lot of experimenting. That's with,~~ um,~~ learning Python but at the same time just messing around with no code tools and I've been lucky enough to,~~ um,~~ Do this for people as well for other people just build projects.

~~Um, ~~and yeah, I've been messing around for a bit over a year now and that started with the GPT 3 API basically back when the [00:01:00] chat GPT 3. 5 that we all know,~~ um,~~ wasn't even available as an API. And ~~I mean, ~~Yes, I think about November last,~~ uh,~~ last year, but the year before,~~ um,~~ I started straight away building no code tools with the use of Zapier and shortly after started messing around with other different no code platforms and,~~ uh,~~ now today we're here and,~~ um,~~ the tools have become better, the,~~ uh,~~ the AI models have become better and it's all super exciting which you can build today.

**Joseph:** Yeah,~~ so,~~ so it's wild. What we're going to get in today,~~ uh,~~ is you've been deep in the throes of make. com and making it do things we didn't necessarily know were possible in make. com. For those of you who don't know what make. com is, ~~you know, ~~it's similar to Zapier, it's just an automations tool where you can ~~kind of ~~just,~~ like,~~ hook APIs up to,~~ like,~~ To one another to do different things and,~~ uh,~~ you've been in your lab,~~ uh,~~ or in your basement or [00:02:00] wherever you're doing this work, essentially building,~~ um,~~ a personal assistant agent, like full on just through make dot com and connecting up some API's.

So why don't you tell us a little bit about,~~ like,~~ functionally. On the highest level, ~~like what is, ~~what is this thing you've built to do? And what is your aspirations for where you're moving towards?

**Sjoerd:** Yeah. So I built this thing out of,~~ um,~~ Like it started with some simple experimentation and I think that started ~~like ~~eight months or so ago where I figured ~~like, ~~Oh my God, this would be so cool to have as a personal assistant that knows context and can take actions for you. ~~Um, ~~and it started with trying to hook up a chat GPT to telegram and just have more control, like message it whenever you want, or maybe even have it send messages to you. ~~Um,~~

**Joseph:** ~~Can you, ~~can you just explain what telegram is in case people don't know?

**Sjoerd:** Telegram is a messaging app. It's super similar to WhatsApp. [00:03:00] Or signal,~~ um,~~ and honestly, it could be built on WhatsApp, it could even be built on Facebook Messenger, it doesn't really matter, it's just,~~ um,~~ one of the different options you can choose from,~~ um,~~ but yeah, I wanted to build an assistant that could ~~Like ~~use context and ~~like ~~help you out with whatever you need help with ~~like ~~if there's parts of life Where you know, ~~like ~~oh, I'm good at this and not certainly not necessarily good at something else.

Like I have trouble like remembering For example gift ideas or something Like what if you could have an AI that has access to some information and can help you with? Sorting that stuff out or organizing your life making it easy to ~~Like ~~manage your schedule, your calendar, basically anything like a personal assistant, like it should do, but then with much less friction, where you can just talk to it in your natural language, mention whatever, and it knows through context and like some,~~ um, uh, ~~language model magic,~~ um,~~ it can figure out what it needs to do [00:04:00] for you, ~~um. ~~And that was the idea and I started working on that quite a long time ago, but I, every time I stranded because of limitations, either in my own knowledge of,~~ uh,~~ what the, or like in limitations of what the models could do. ~~Um, ~~and now with the assist, assistance API,~~ um,~~ so that's chat GPT 4 or GPT 4 turbo is

what it uses. And it can,~~ um,~~ It's basically, how would I put it, it's like a sort of a system,~~ uh,~~ where GPT 4,~~ um,~~ knows when to take actions and you give it action, or you give it access to certain actions, so you can tell it how it can reach your calendar, how it can reach your task list,~~ uh,~~ whatever you want it to. How it can do web searching,~~ um,~~ how it can store notes for you. You tell it how it can do that and it'll be able to output like a simple bit of JSON and it knows when to wait for an action and it knows when to give you a straightforward response.

~~Um, ~~

**Joseph:** And sorry, [00:05:00] can you just,~~ uh,~~ can you explain a little bit of what Jason is? I'm not sure everybody 

**Sjoerd:** oh yeah, 

~~so~~ 

**Joseph:** that is used for.

**Sjoerd:** JSON is a very straightforward data structure. It's a fairly simple, straightforward,~~ um,~~ bit of language,~~ um,~~ that computers can understand and process easily. 

**Joseph:** I'd say it is just ~~a, a, ~~a way to format something, some information and structure that you're trying to communicate to a system, usually an API for either asking it to give you something or you giving it something to do with. It's just a way to communicate that. Easily to, to a computer and what most, ~~you know, ~~when you're working ~~in, ~~in with APIs and you're trying to ~~kind of ~~connect the plumbing between different services, ~~you know, ~~Jason is the most common way you do that.

**Sjoerd:** yeah, definitely. ~~Um, ~~and yeah, the assistance API is built to,~~ uh,~~ give JSON depending on the structure or output JSON depending on the structure [00:06:00] that you give it. So you can tell it like,~~ um,~~ if you want to search my calendar, then you need to give me,~~ um,~~ A window, so like a starting date and an end date between which you get the,~~ um,~~ calendar information. So if I say,~~ like,~~ I want to check for tomorrow, then what's on my calendar tomorrow, then it'll check,~~ um,~~ like at the beginning of the day and at the end of the day, it'll get those start and end dates and then it receives It gets everything back,~~ um,~~ what is planned for that day,~~ um,~~ with the information you,~~ um,~~ wanted to give. And the structure in which it formats it, that's done in JSON. And yeah, it's basically like one super important aspect and you don't really need to be able to be experienced with using it. It's actually fairly straightforward. And ChatGPT, like your regular ChatGPT that you can talk with,~~ uh,~~ on the OpenAI website is like, it understands it perfectly.

It can format it for you without problems, without any

trouble. Like ~~it's, ~~it's 

super 

**Joseph:** know. I've done that too, or I'm just like, make this Jason.

**Sjoerd:** Yeah,~~ like,~~ as [00:07:00] simple as that,~~ like,~~ no, no complicated prompting techniques needed, just tell it to format it into JSON and it'll do it for you. I think I did it earlier this morning,~~ um,~~ like here, I've got three things, just make them into JSON and ~~it'll, ~~it'll output JSON perfectly. ~~Um, ~~I don't think I've ever really written JSON myself,~~ um,~~ now that I

think about it. 

**Joseph:** definitely not. If you asked me, like, how do I write this in JSON, I wouldn't know. All I know is how to ask ChatGPT to do it for me.

**Sjoerd:** Exactly. ~~So, ~~yeah, that's ~~like. ~~Basically at the core of communications,~~ uh,~~ between,~~ um,~~ the assistance API and the different tools you can give it. It's like the language that they both speak,~~ um,~~ that the tools speak and that the assistance API speaks. So yeah, that's basically at the core of it.

**Joseph:** , why don't you show,~~ uh,~~ the madness that you've cooked up and we can ~~kind of ~~walk through it sort of function by function.

**Sjoerd:** So it looks really big, but,~~ um,~~ and ~~there's some, ~~there's some. [00:08:00] Somewhat complicated stuff in there, but,~~ uh,~~ in the end it's all just different nodes connected together. ~~Um, and, like, ~~the top half can basically be ignored most of the time. ~~Um, ~~and most of the interesting stuff is going down below this very long line. ~~Um, ~~and it's all in here. ~~Um, ~~but yeah, it basically works. It receives. A message from Telegram, so I've built a bot, it's actually made super easy to,~~ uh,~~ to create your own Telegram bot that you can afterwards,~~ like,~~ hook up to make a message. It's completely free, they provide a really awesome platform and really cool possibilities to work with your,~~ uh,~~ bot, but for this it's actually somewhat straightforward. ~~Um, ~~but yeah, it watches,~~ like,~~ it checks if it receives a message. Then,~~ um,~~ it,~~ um,~~ checks into the database,~~ like,~~ have I seen this conversation before, yes or no, and that's how it retrieves,~~ uh,~~ the right,~~ um, like, ~~message history,~~ um,~~ and once that's done ,~~ um, ~~it generates a response, and then depending on if it sees,~~ like,~~ oh, I need to [00:09:00] take an action, it goes into one path, it goes into all the different actions that I've set up right here, like Google Tasks, like receiving it or creating one or deleting one, or in my Google Calendar if it needs to read it, or down here I've got a request for a web search. And then it periodically checks like, oh, have I received a message? Am I done with this? Yes or no, and then it takes it into a, it goes into a different path to send a message depending on what it, ~~like ~~what action it took. And the fun thing is if I press run once, you can see what's going on. So right now you see that it's listening. I can send a quick message to it. I can ask it for my calendar for next week. ~~Uh, ~~and you won't be able to see me asking it, but now you see it sends a

message. 

**Joseph:** moving through, yeah.

**Sjoerd:** Yeah, you see it moving through, which is really neat, like right now it knows that it needs to take an action. So it goes ~~into the, ~~into the branch to the right. It [00:10:00] searches for events right here.

It sends the events to,~~ uh,~~ back to ChatGPT, whatever it received, and then afterwards it should go. It's checking, like it's still making, writing a message,

and then it's writing a response back to me. And if we wait a little bit longer, there we go, and we've received a message on my telegram and it tells me exactly, like for next week it tells me I've got work and I've got some stuff to do during the weekends. ~~Um, ~~but yeah, it's cool.

that you can see it move through, like this is something you don't have when you're writing,~~ uh,~~ in Python or any other code. You can't really see

it move. 

**Joseph:** Yeah, it's much more,~~ uh,~~ I'm a big,~~ like,~~ workflows guy anyway, so I do really like how I much prefer Make to Zapier because of this. It's like this more module, node type interface.

**Sjoerd:** ~~Right. ~~Yeah.

**Joseph:** ~~So, ~~so tell me what's going on,~~ uh,~~ if you ~~kind of ~~zoom in on the [00:11:00] bottom, mid bottom ~~right. ~~I see you've got,~~ uh, ~~

**Sjoerd:** ~~Right here.~~ 

**Joseph:** some chat GPT.

Like before it starts getting routed. Yeah. So tell me a little bit about ~~like, what is, ~~what is going on,~~ uh,~~ here and ~~how is it, ~~how is it recognizing what action it's supposed to take?

**Sjoerd:** Okay. So right here. ~~Um, ~~so ~~let's, ~~let's just go back and walk through it from here. So it receives a message. ~~Um, ~~it stores the message in a variable. ~~Um, ~~and basically, like at the top part, it's not very interesting, it just, it checks whether it already had a conversation or not and then plugs that back in, but you could skip that part if you're just trying to build it for yourself, it wouldn't really matter anyway. But ~~um, ~~yeah, so it adds the message to,~~ uh,~~ the assistant. ~~Um, ~~but adding a message doesn't really do anything except for,~~ um,~~ adding it to a list. So here create run is where ~~it gets, ~~it gets interesting. Then it tells ShowGBT you need to do something with this message. You need to respond to it. And then here. With retrieve run, it checks like, Oh, what do I need to do [00:12:00] with it? So if you go here, you see all the different operations.

You see also like different sizes that checks,~~ uh,~~ let's go to the first one. And it says in progress. That means chat GPT is ~~doing, ~~doing something. It's ~~like, uh, ~~when it's writing a response to you and,~~ um,~~ whenever you're talking, that's, what's going on right now, it's writing a response.

When that's the case, I send it to. A note up here, which sends it to somewhere else. It starts checking like, okay. ~~Um, ~~so you're in progress right now. I need to wait. And ~~it waits, it waits, it waits, ~~it waits, until it knows,~~ like,~~ oh, something happened, it changed, it's no longer in progress. ~~Um, ~~and now it sends it somewhere else. ~~So, ~~it goes to the retrieve run again, and it checks,~~ like,~~ okay, so we know something has changed, but let's see what I need to do right now. And we can go in here and see what it wants. This time the status just requires action. That means it needs to take an action on one of the,~~ uh,~~ few tools that we,~~ uh,~~ gave ~~it, ~~it,~~ uh,~~ it wants to use one of those. [00:13:00] if that's the case, it goes to the right here to one, one of the many different options that we've got right here. And then there's a bunch of if statements. So if the,~~ uh,~~ the call ~~that, ~~that it wants to use is search calendar events, then it goes into this one. It knows how to fill in all the information. So we can look at the input bundles and it says,~~ Like,~~ oh, next week, ChatGPT knows to fill in ~~that ~~that's the 8th of January until the 15th. So that's the start and end date that we filled in. And,~~ like,~~ then you get a whole bunch of,~~ uh,~~ information out of it. And the information then gets sent back to,~~ uh,~~ to the assistant. So he's ~~like, ~~okay, I need to take an action. ~~Um, ~~and here is the response of the action. And,~~ um,~~ yeah, it can take a bunch at the same time. So if you say,~~ like,~~ I want to have,~~ uh,~~ so for every day next week,~~ uh,~~ book in my work hours from,~~ uh,~~ seven to,~~ uh,~~ to four,~~ um,~~ it can do five at the same time. ~~Um, ~~and then it sends it all back,~~ like, uh, ~~to,~~ uh,~~ to the API, to the assistant [00:14:00] and the assistant is ~~like, ~~okay, what's the response? Oh, here's a bunch of,~~ um,~~ calendar events that,~~ uh,~~ that came back,~~ um,~~ and it turns that into a nice formatted message. ~~Um, ~~and when the status is completed, it knows ~~like, ~~Oh, I've got a message that's ready to send to the user. Let me send it. And here it sends the message,~~ um,~~ output here should say, like for the coming week, these are the events you've got nicely formatted because well, JetGPT understands it well. So that's in like basic terms, if we walk through it on ~~like ~~a fairly high level, how it all works.

**Joseph:** Yeah. ~~So, ~~so pretty much what it's doing is you send a message. It. ~~Like ~~sits to ~~like, ~~okay, we have a task in progress and then it's ~~like, ~~okay, these are the different actions I can take based on what he asked. What is the action I'm supposed to take? And then it ~~kind of ~~filters down to whatever that action is.

And then it comes back and it's ~~like, ~~okay, we've done the thing. [00:15:00] Now let's format a message to send back and then it sends that message back to you after it's done the thing.

**Sjoerd:** Yeah. Yeah. Basically it knows how to,~~ um,~~ format a task. ~~Like ~~if you,~~ um,~~ think a calculator would be a good example. If I,~~ uh,~~ if I send it like what's five plus five, then it knows how to,~~ um,~~ formulate a task. Whatever it needs to send to the calculator that,~~ like,~~ it knows,~~ like,~~ Oh, I need to send 5, plus, and 5.

If I send it that way to the,~~ uh,~~ to the calculator, I get a response back, then it reads the response, and then relays that back to the user. ~~Uh, ~~yeah, still every time,~~ like,~~ processing it in between. So it won't literally say whatever the output is,~~ Um,~~ but it reads it, and then takes it as a prompt, and then responds. To make it a little nicer.

**Joseph:** So I know you said ~~like, ~~don't worry about the top stuff, but ~~what, ~~what? Cause that looks like it's the most like almost the most complicated. So what is going on up here and why have you spent the time doing [00:16:00] that?

**Sjoerd:** ~~So, um, ~~I wanted to add a bunch of extra little features. ~~Uh, ~~one of them is using the whisper API, so I can just super quick, send a voice message and. Whisper takes the audio, turns it into a regular text message, and then it processes it that way. So that way I can just grab my phone out of my pocket, tell it like, Oh, I need to do this for next week, schedule this on,~~ uh,~~ on Tuesday. ~~Um, ~~and then release it, and then just put it back in my pocket, and then it'll schedule a task,~~ um,~~ for next Tuesday, with whatever I send it. ~~Like, ~~I figured,~~ like,~~ that's a really nice way to use it, along with,~~ like,~~ we've got the vision model, why not use it? ~~So, ~~if you receive a letter,~~ um,~~ last week I received a letter that my passport was about, was going to expire in about four months.

~~So, ~~I probably need to set up an appointment to,~~ um,~~ to get a

new one, or get it renewed, exactly. ~~So, ~~what I can do is quickly take a picture of the letter that I receive, send it to my,~~ uh,~~ to Telegram, and give it [00:17:00] some context, like what's,~~ um, um, ~~or can you put this in my calendar for next week or

something that I need to get renewed.

~~So, ~~And it does it perfectly without problems,~~ like, um, ~~And I wanted to add a bunch of those little extra neat features to make it,~~ like,~~ really nice to use. So say you've

got a meeting and you're just jotting notes down on the paper, Just make a picture of,~~ um,~~ of the notes and tell it to store it as meeting notes for you.

And it'll immediately just upload it as meeting notes. ~~Um, ~~and that's some of what's going on right here. So it recognizes,~~ like,~~ am I receiving,~~ um,~~ a voice message? Am I receiving an image? Or am I receiving some regular text? And it also checks,~~ uh,~~ like I said earlier, it also checks if,~~ um,~~ If this conversation is a new conversation or some,~~ like,~~ or if it's already ongoing and if it's ongoing it just keeps going where it left off and that way you can have a long history,~~ um,~~ on a like per conversation basis.

So if someone else were to talk to this chatbot it would [00:18:00] work perfectly fine for them and it wouldn't get messed up with my own chat history.

**Joseph:** Nice.

**Sjoerd:** So that's some of what's going on and then,~~ um,~~ Yeah, so here's the speech, the text, and the vision,~~ um,~~ and then I've got this super long,~~ um,~~ node that just passes from left to ~~right, um, ~~but the thing that it's doing is that,~~ um,~~ like here you see update tasks, store nodes, retrieve tasks, create tasks. Here is where the little tasks,~~ um,~~ stored, and if I want to create a new one, I've basically made a fairly easy process for myself to add extra tasks. So if we click on update calendar event, ~~you see, ~~this is the JSON, and it's all the values that the API needs to send.

~~Um, ~~

**Joseph:** ~~Mm.~~

**Sjoerd:** so the,~~ um,~~ event, the name of the event,~~ um,~~ whether it's all day or not,~~ uh,~~ what the starting date is, what the end date is,~~ uh,~~ it's all in there. And [00:19:00] then it passes that along and puts it,~~ like,~~ gives access to it in the API. It tells it this is an action that you have access to. here we've got the modify assistant,~~ um,~~ and here all the functions are in here. So there's a long list of them. ~~Um, ~~I think I've got nine right now,~~ uh,~~ nine different actions it can take, and those are different actions for creating tasks, editing them, deleting them, same for calendars and for notes as well. And there's a little OneDrive note here, download a file,~~ um,~~ and that's basically, I have a bunch of notes in there, and there's one file in which I combine all the notes, and that one is used as a knowledge base. in the background. But I've basically, I've just tried to make it super easy for myself. If I make changes, add extra actions, this one rarely gets used, but when I use it, I just send a message,~~ uh,~~ update knowledge to the chatbot and it'll update it. ~~Uh, ~~with [00:20:00] the

most recent knowledge and all the actions that are in there. So it looks

super daunting, but ~~I mean, ~~it ~~kind of~~

~~is~~ though I have to 

**Joseph:** what I was going to say. ~~What, ~~what was the most difficult challenge for you in building this? Where you're like banging your head against the wall.

**Sjoerd:** ~~um, ~~so I think the biggest one was getting multiple actions to work. ~~Like ~~there's some stuff that are like standard that make provides when I create a note, let's just add one,~~ um,~~ so make provides a bunch of standard notes. ~~Um, ~~And for the OpenAI Assistant, they barely provided anything at all. This is the official one. So when I go here, there's a bunch of different options for generating an image. But the only thing that's there for an assistant is to message one. And with just messaging and assistant, there's barely anything you can do.

You can't take actions, you can't upload files.

~~Um, ~~so one user, I don't have [00:21:00] his name, but I guess I should probably give you a link to it as well. ~~Um, it's, ~~it's possible for people to make their own apps. ~~Um, ~~and someone was kind enough to build,~~ um,~~ OpenAI that's

much more able. Yeah, so here, create an assistant, retrieve an assistant, modify, list, delete, create.

So there's already a whole bunch of options in there. And for 90 percent of all the actions, this was plenty, this was enough, but,~~ um,~~ to receive,~~ um,~~ to get all the different outputs, because you need to collect,~~ like,~~ if you, let me take one step back,~~ um,~~ there's the, Provide an output. Oh, I go, it's jumping all over the place. ~~Uh, ~~let me see where it is. ~~Uh,~~

yeah, submit tool outputs to run. So it's right here. ~~Um, ~~this endpoint can be used to submit the output from the tool calls once they're completed. So basically, if you ask your calendar, what's on there, and it [00:22:00] tells you, it gives you a whole list of what's on the calendar. ~~Um, ~~you have to send that back to,~~ uh,~~ to the assistant,~~ uh,~~ in order for it to be able to. read it. give you restaurants based on it. ~~Um, ~~which like sounds fairly straightforward, but once you're working with multiple actions and you want to update like for seven different days at a time,~~ um,~~ Which is,~~ like,~~ for regular usability, ~~like ~~if you ask it what's on my task list, can you say,~~ like,~~ oh, you need to mark 3 as done. ~~Um, ~~it's just much nicer to use.

**Joseph:** Yeah.

**Sjoerd:** But,~~ uh,~~ this was difficult to get to work, because you have to combine all the different outputs, and you have to receive all the different call IDs, because every single one goes through it individually so then you have to combine it and then after combining it you need a way to collect all the different call ideas,~~ um,~~ with all the different outputs and send it back and this was a real head scratcher to get to work.

Especially since this one was ~~kind of ~~half baked. It could do one at a time but it wasn't [00:23:00] made to do multiple at a

time. 

**Joseph:** yeah. 

**Sjoerd:** Yeah, so I had 

~~to~~ 

**Joseph:** what was the epiphany? Yeah, what was the epiphany moment? How did you 

**Sjoerd:** So I had to dive into the OpenAI documentation and build it myself. ~~Um, ~~and here,~~ uh,~~ everything's in here,~~ uh, um, ~~with ~~the, ~~the link,~~ uh, um, ~~the output and then basically use a bunch of different,~~ um,~~ JSON to combine it with like here you see the iterator that goes down and then it's like all kinds of different paths and need to, it needs to take because sometimes you receive a function and it needs to just get one response back and then send it back.

But what happens if it needs to go through like the same process twice or three times? ~~Um, ~~sometimes the API makes a mistake and you give it feedback, like you can, you made a mistake, you need to try again. And that all happens within the same Run, so you send one message, it messes up, it realizes it messes up, [00:24:00] and then it tries to do the same thing again, and that all needs to work perfectly.

Like sometimes you need to send back multiple outputs, sometimes just one, sometimes you need to send it back and then,~~ um,~~ once more. And that was a big challenge to get to work, but

we got there in the 

end. 

**Joseph:** hurting thinking about it.

**Sjoerd:** Yeah. So this was definitely one of the biggest challenges. ~~Um, ~~actually adding on tasks, like adding on more, it probably takes me like 10, 15 minutes to give it access to, for example, my most recent emails. That part is ~~like ~~streamlined. ~~Uh, ~~right now, and I've got it pretty much down on how to,~~ uh,~~ how to change those, but,~~ um,~~ yeah, that took a while before I got to that point.

**Joseph:** What,~~ uh,~~ what do you got,~~ uh,~~ planned,~~ uh,~~ next, you mad scientist? ~~Uh, what's, ~~what's ~~kind of ~~next on the agenda ~~for, ~~for plugging stuff into this?

**Sjoerd:** ~~So, ~~now that I've got all the,~~ um,~~ I've basically got the setup down, it's pretty efficient as well, I had to,~~ um,~~ get a little creative with,~~ uh,~~ trying to make sure that it doesn't use a million different [00:25:00] operations and I,~~ uh,~~ Like it gets incredibly pricey with using mate. com.

**Joseph:** I was going to ask like how,~~ uh, well, ~~not just make. com, but,~~ uh,~~ API calls too. Like you have a bunch of calls within this.

**Sjoerd:** Yeah,~~ so, um, ~~there's actually just, there's not that many API calls towards, like there's a bunch of API calls I should say, but those are mainly to ~~like ~~add a message or ~~like ~~check what the run status is. And those

~~don't, those are~~ free 

**Joseph:** yeah.

**Sjoerd:** and those are free. Those don't cost any, like they don't cost anything.

It costs money once you

have to generate stuff. And once ~~the, ~~the API, once the assistant has to ~~like ~~write out the different calls,~~ um,~~ that costs money. And,~~ um,~~ so far it's actually,~~ like,~~ it's not too bad. It's a bit hard to put a price on it, but the GPT 4 Turbo isn't super pricey to use,

as long as you don't make the context extremely long. So basically what I've done is manually every now and then purge all my messages. And I've set up a [00:26:00] flow for that too. So I can pretty much just message reset chat. And then it instantly, like it starts over completely clean from scratch. ~~Um, ~~otherwise you're looking at, it can go up to 100k tokens.

Which is ~~like, ~~imagine 300 page book, basically, of context.

~~Um, ~~and if you don't purge those, it'll send 100k tokens every time. And I think you're looking at between 1 and 2 dollars per API call. So imagine 1 to 2

dollars per message. ~~Um,~~

that's no 

**Joseph:** it's such a waste, too, because it's ~~like, ~~it's more context than it could possibly need for whatever you're 

**Sjoerd:** Yeah, no, 

exactly. 

**Joseph:** talk about.

**Sjoerd:** Absolutely. So that's a complete way. ~~So, ~~so far, if basically every now and then just send a message, reset the chat and then it's fine. It works. ~~Um, ~~it's not too pricey. ~~I mean, ~~I'm guessing running costs are probably like, if I exclude ~~the, ~~the cost for make. com, it's, I think if I would send ~~like ~~five to 10 messages every day, my maybe 10, 20 bucks a month.

Yeah. ~~Uh, ~~something along those lines,

which I think 

is 

fine. 

**Joseph:** than paying for an assistant. [00:27:00] 

**Sjoerd:** Yeah, ~~right. ~~Absolutely. Absolutely. It helps that all the other,~~ uh,~~ tools that I use are free,~~ um,~~ except for I use perplexity for web search. Since it's fast and the API is easy to use,~~ uh,~~ but

that one's super cheap 

~~too.~~ 

**Joseph:** funded too. They just got a huge funding round.

**Sjoerd:** Oh,~~ nice,~~ nice. 

**Joseph:** saw that.

**Sjoerd:** Now I missed it, but ~~um, ~~I think I've,~~ like, um, ~~I started using it right at the end of last year and I think my first bill was like 5 cents or something. Just ~~like, ~~whatever, it's worth it. ~~Um, ~~but yeah, now, when it comes to stuff that I have planned,~~ um, I'm ~~I'm working on something super exciting and I think the potential is quite insane. ~~Um, ~~I discovered this open source,~~ uh,~~ CRM for like personal relationships. And,~~ um,~~ it's basically like ~~a, ~~a package that's already set together where you can just, where you can store information about people you have,~~ uh,~~ you're in contact with. Your friends, family,~~ um,~~ like work, [00:28:00] colleagues, anything. You can just store it in there at notes.

~~Uh, ~~if you have events, then you can upload events and then,~~ um,~~ mention which person was involved. ~~Uh, ~~and how it can also be used to set reminders. ~~Um, ~~and it's basically, it's,~~ um,~~ I've got it self hosted right now and it's running,~~ um,~~ but I'm trying to figure out how I'm going to plug this into the whole system. ~~Um, ~~because I think there's some,~~ like,~~ crazy potential here where it knows a lot about a bunch of different things. ~~Um, ~~and, yeah, so that's something that I really,~~ like,~~ think is a big next step. If you could,~~ like,~~ relate tasks to different people, ~~um ~~That would be insane,~~ um,~~ like events as well, just like the potential there,~~ uh,~~ to know so much more, get contact information as well. It's like crazy, but,~~ um,~~ there's ~~some, ~~some issues there with,~~ uh,~~ for example, I can't just, Give all the data to,~~ uh,~~ to the API, to the,~~ uh,~~ to chat GPT, [00:29:00] to open AI. ~~Um, ~~especially when it comes to personal information. Like my own calendar, I don't care. ~~That's, ~~that's my own,~~ uh,~~ I've got one set up just for this and it works really

well. ~~ ~~But with personal information, I'll have to be a bit more careful. But I think I could figure out ways to,~~ um,~~ Like I have complete control over all the data, it's all also self hosted and I could probably manage some way in how I can obscure some of the information that I sent to OpenAI and still get the data out of it that I want. But yeah, I think that's the big next step now that I've got all the basics down.

**Joseph:** yeah, essentially a relational database you can use. 

**Sjoerd:** ~~Exactly,~~ 

**Joseph:** so for that, are you imagining, I'm sure it's a combo, but Is it just filling out that information based on your chats with it? Or are you filling out that information somewhere else and it's just ~~accessing, ~~accessing that database? ~~Or, ~~or both, ~~I ~~

**Sjoerd:** ~~both, ~~both, absolutely both. ~~So, um, ~~what I noticed right now, I can tell it like, [00:30:00] hey, we're going to work ~~on a, ~~on a node together. And I want you to just ask me questions,~~ uh,~~ work together with me, and once we've fleshed out,~~ uh,~~ the idea, once you've got enough context, then,~~ uh,~~ let's store it. ~~Um, ~~and I think this could work the same way, where you can just have a chat, go back and forth, and once it's ready, tell it to, okay, now you can store this information. ~~Uh, ~~or you can just send a quick voice message, hey,~~ uh,~~ I just ~~had, ~~had a chat with so and ~~so, ~~it was about this and that, please store it. And then.

~~Once~~ you know,~~ like,~~ oh, I've got a meeting again with this person, you can just ask,~~ uh, like, ~~hey,~~ uh,~~ what did we talk about last time? And it'll be able to conjure it up. So it's definitely both, and I think that's also where,~~ um, like, ~~I want to make this as frictionless as possible, and I don't want to dive into seven different platforms,~~ um,~~ and use them. I basically want my

assistant to use it for me.

**Joseph:** ~~Mm hmm. ~~Yeah, 100 percent agree. I think that is definitely the way things are going where you have this. The conductor, as I call it, the orchestrator, as others call it, [00:31:00] where you're just interacting with this one thing, and it's the thing interacting with all the different things.

**Sjoerd:** Yeah, that's the,~~ uh,~~ that's the dream. That's the whole idea.

**Joseph:** ~~That's, ~~that's what we're working towards. Which 

**Sjoerd:** and it's already,~~ um,~~ right now the assistance API was a big step up,~~ uh,~~ towards that goal. ~~Um, ~~and I'm definitely gonna, going to do some experiments and see how far I can get with,~~ um,~~ with more open source models or. just different models we can access, but right now,~~ um,~~ the assistance API with the ability for it to just always adhere to the structure,~~ uh,~~ of the different actions, like it's able, it's, it works like nine out of 10 times with the,~~ uh,~~ with the different actions.

And then,~~ um,~~ if you have it set up properly,~~ like, um, ~~right here, ~~you see ~~create a calendar event,~~ uh,~~ and you see the little weird lines here to a different,~~ uh,~~ set variable. ~~Um, ~~it's basically if it gets an error back from [00:32:00] the create an event, it sends the error back to the output and that way chat GPT knows it made a mistake and it can try again,~~ uh,~~ with the context of that error.

**Joseph:** does,~~ like,~~ ChatGPT, it'll often be like, this didn't work, I made a mistake, let's try this. 

**Sjoerd:** ~~Yeah.~~

~~yeah, ~~yeah, exactly. And you basically automate the process by telling it like automatically telling it ~~so, ~~and it knows ~~like, ~~oh, I need you,~~ um,~~ I need to take an action again and it'll try again. But now knowing what it,~~ uh,~~ knowing that the error that it made, ~~um. ~~And this is something that basically, it ups ~~the, ~~the,~~ um,~~ the success rate to ~~like ~~98, 99%. It almost never makes a mistake anymore, which is super neat. ~~Um, ~~and that's

something that I really hope that other,~~ uh,~~ other models that you could possibly run on your own system could achieve too. But that's something.

**Joseph:** 100%. I feel like you could pretty easily get,~~ like,~~ a 7 billion parameter [00:33:00] model to do most of this because,~~ like,~~ a lot of the in betweens here, they're not,~~ like,~~ complex. They're fairly rote processes, so it feels like it's definitely possible.

**Sjoerd:** Yeah,~~ it,~~ it should be, but,~~ um,~~ I think it's still going to be,~~ uh, like, ~~it's a bit of a challenge,~~ um,~~ to hook it all up together,

like just ~~the, ~~the assistance API just made it so much easier.

**Joseph:** ~~hmm. ~~

**Sjoerd:** And I think. Like it's still in beta and it'll get better,~~ uh,~~ and I'm super excited for what it will be able to do, but ~~um, ~~but yeah, there's just a ton of potential there and ~~I, ~~I really want to see ~~like if, ~~if you could get with your, like a locally running assistant, if it could get even remotely close to this quality, that would already be amazing because then you could just be completely careless about the,~~ um, Um,~~

The level of

privacy.

Yeah, then you don't have to worry about,~~ uh,~~ sending like important information from other people. It's just super neatly,~~ uh,~~ all in your own system.

**Joseph:** ~~Well, ~~and [00:34:00] at some point, too, I think we're going to get to the point where it's going to be super easy. For you to train your own model or ~~like, you know, ~~fine tune an existing model, ~~you know, ~~on this process, essentially, and it'll run 100 percent of the time because it's like literally trained specifically for this purpose.

So we're not there yet, obviously. 

**Sjoerd:** No,~~ ~~

**Joseph:** ~~Um, but, ~~but I think that's the direction, ~~you know, we're, ~~we're moving towards is. ~~Uh, ~~costs come down, and ~~sort of we, ~~we start to see this new wave of AI focused chips,~~ uh,~~ coming out, like specifically made for this purpose.

**Sjoerd:** right. Yeah,

no, that, that's incredibly exciting. And I'm already,~~ um, Like, I, I, ~~I'm building stuff and just experimenting all the time and I have no problems like working on a project, ditching it because it doesn't work well and then coming back to it with either ~~like ~~Having some extra skills myself or,~~ um,~~ having

the,~~ um,~~ yeah, 

~~ ~~technology, exactly.

So if chat [00:35:00] GPT, if GPT 4 gets better, if the assistance API comes out, then I'll just start messing around with it straight away and see how far I can get. And it's. perfectly fine if it doesn't work. ~~Um, ~~like I shared earlier, I said ~~like ~~eight months ago or something, I made like a super bare bones version of this and used Google Sheets as the message history.

~~Um, ~~so I just told it like a message comes in, store it in Google Sheets,~~ um,~~ and then ~~like ~~retrieve it from Google Sheets again to build up the history again. It was super messy,~~ uh,~~ gave errors all the time. But,~~ um,~~ It was the start of it and it allowed me to learn a whole bunch and I think that without that experimentation, I wouldn't have been able to build this either.

**Joseph:** Yeah, I 1000 percent agree. And I think one of the most fabulous things about this generative AI is it reduces the barrier to starting and failing at something because for one, it separates your identity from the failure [00:36:00] because it's ~~like, ~~no, it's the technology's failing. I'm not failing. But also you can just iterate and prototype immediately.

And like you said, if you hit a wall, You've still ~~kind of ~~learned where that wall is and why that wall is there. And then when the technology moves forward, you're like, Oh, wait, this is no longer a barrier anymore. Let me go back to what I was doing and use this new tool I've discovered that was invented to get over that barrier.

And you just ~~kind of ~~keep building on that.

**Sjoerd:** exactly. And I want to add on to that, that,~~ um,~~ the evolution of,~~ um,~~ like technology,~~ um, like ~~make. com isn't necessarily like revolutionary per se. Same can be said for Zapier. ~~Um, ~~but these platforms do make it like a whole lot easier for someone like me who doesn't have a very technical background. ~~Um, ~~to just only have to worry about the building the cool stuff. ~~Um, ~~so I don't have to set up a server,~~ um, like ~~write code myself,~~ um,~~ deal with all kinds of different,~~ like,~~ [00:37:00] worry about all kinds of different things like encryption,~~ uh,~~ Like the security,~~ like, um, ~~of the different modules,~~ um,~~ like I, I remember trying to set up authentication to have access to my Gmail using Python. And it was just like a complete

headache and a total mess to, to do it. And here it takes me about 30 seconds to set up.

to get access to it.~~ Um, ~~basically these people have figured out a whole bunch. And,~~ um,~~ that just allows me ~~to, ~~to work on the cool stuff, which makes, it makes it so much more accessible to build,~~ uh,~~ automations that are suited perfectly for me.

**Joseph:** Yeah.

**Sjoerd:** And that's something ~~that's, ~~that's, ~~I've been, ~~I've been realizing it more and more the past year. ~~Um, ~~and you still need to study, you need to work a bit on, like for this, I had to dive into,~~ um,~~ makes,~~ uh,~~ own courses and I've completed like a large chunk of them. ~~Um, ~~and I think that was definitely a must to get this to work. I couldn't have built this without the [00:38:00] knowledge I got from those courses, so it still definitely takes some work, but I think that's ~~like, ~~I would say, like maybe 10 hours of studying. ~~Um,~~

**Joseph:** Yeah, but ~~it's, ~~it's different though, because it's ~~like, ~~to me, I go down the deep rabbit hole to when I hit a wall, as we said, because I'm like intrinsically motivated to figure out how to get through or around that wall, because it's ~~like, ~~I'm trying to do this cool thing. I'm working on this cool project.

~~You know, ~~I've hit a snag. Okay, how do I solve this problem? And then when you solve the problem, you're like, Damn, I'm good. 

**Sjoerd:** ~~yes, yes, ~~

**Joseph:** good because you got around that issue and you did it by like essentially teaching yourself how to do something you didn't know how to do before. And that feels really good.

**Sjoerd:** No, definitely. And ~~um, ~~ChantGPT is a, is like a really great troubleshooter as well.

**Joseph:** Yeah, especially now with like vision where you can just ~~like ~~take a little [00:39:00] snapshot being like, I got this error. This is what it looks like. It walked me through what I can do.

**Sjoerd:** Yeah,~~ so, um, ~~last time I,~~ um,~~ I had a chat with Goda,~~ um,~~ I realized you could just copy and paste,~~ uh,~~ a note. So if I copy this. I knew you could copy and paste a note, like ~~so, ~~that's super straight forward, you can select one, ctrl c, ctrl v, and it's done. But what's super cool is that you can paste that outside of make.

com as well, and then you realize it's just a bunch of JSON. ~~Um, ~~and what I did was,~~ um,~~ so here the modify assistant one, it's got on big, it's big,~~ it's,~~ it's long. There's,

**Joseph:** Yeah. Oh 

**Sjoerd:** it's also super straightforward, like to be clear. ~~Um, ~~so it's like update function, eight description, update function, nine description, update function, 10 description.

So I've made sure it's as easy as possible. And I can,~~ um,~~ I can copy and paste this, [00:40:00] toss it into the code interpreter and tell it to add another function. And that way it adds,~~ um,~~ it adds the next one, so you get update function 10, name, update function 10, description, update function 10, I don't have to fill it in manually, it just does it for

me,~~ um,~~ which is super neat, that combined with,~~ uh,~~ copy and pasting. This in there as well. ~~Um, ~~like it's fun when you,~~ um,~~ when you discover those little,

~~um,~~

**Joseph:** hacks. 

**Sjoerd:** The little hacks. the little tricks that basically I've never heard anyone talk about it before, but it's,~~ uh, like ~~the code interpreter knows how to, like it can write code,~~ um, like ~~chat GPT itself can interpret Jason like perfectly.

It's so I figured ~~like, ~~Oh, if I can copy and paste this, then I can copy and paste it into a chat GPT and have it edited for me.

With maybe a little bit of added context, but it was,~~ uh,~~ But yeah,~~ those,~~ those little tricks are like super, super cool to find. And,

~~um,~~ [00:41:00] Yeah.

that's what makes it like a 10, 10, 15 minute process to add another action to,~~ uh,~~ to the whole assistant.

**Joseph:** ~~Mm hmm.~~

**Sjoerd:** is basically those little,~~ uh,~~ those little tricks, the little hacks.

**Joseph:** Yes.

**Sjoerd:** Yeah, where it's like a combination of,~~ uh,~~ a tool powered by ChatGPT,~~ um,~~ and having ChatGPT as,~~ uh,~~ as like a companion who can look over your shoulder and tell you like, oh, maybe you should look here. ~~Um,~~

**Joseph:** Help you troubleshoot.

**Sjoerd:** yeah, exactly. And that combination is,~~ uh,~~ is like really powerful and allows people like me. To,~~ uh,~~ to build some cool systems.



**Sjoerd:** Let's just try it out and talk to it. ~~Um, ~~can you create a,~~ uh,~~ on my task list that I need to,~~ um,~~ need to work on my loose newsletter to explain how my,~~ uh,~~ AI assistant works? Send it. ~~Uh, ~~lemme see. ~~Uh, ~~yeah,~~ so, uh, ~~Hey, what's on my,~~ uh,~~ to do list? ~~I mean, ~~I can just type messages, but I can use it this way as well.

**Joseph:** Yeah.

**Sjoerd:** You see here, it calls a function. Takes a

moment. 

**Joseph:** me, I'd [00:42:00] have it,~~ uh,~~ say something ~~kind of ~~funny, whenever it was called to

**Sjoerd:** Yeah, no, function call is just a placeholder right now. I can maybe turn it into something more,~~ uh, uh, ~~Let's see where it is. Oh, it's checking. ~~Like, ~~it's super fun that you can see,~~ uh,~~ in the background what's going on with the,~~ uh,~~ 

**Joseph:** Yeah, where it is in the process. 

**Sjoerd:** we go. All right, so it listed a bunch of tasks that I've set up. Oh, it's all in Dutch,

but~~ ~~

**Joseph:** ~~you're,~~ 

you're overdue on a few things, man, I

**Sjoerd:** Yeah, ~~I know, I know, ~~I

know. 

**Joseph:** catch up. 

**Sjoerd:** so can you mark the,~~ uh,~~ Calendly task as done? I keep opening up the,~~ uh,~~ but no, yeah, I can just talk to it super fast. And that's like a very neat thing. ~~Um, ~~is that you can,~~ like,~~ I like to be able to just open it up, talk to it, put it back.

And I know

it's working in the 

**Joseph:** percent agree.~~ ~~

**Sjoerd:** ~~Um, ~~I can go back and forth like you do with regular chat GPT, but I think chat GPT does that pretty fine. ~~Um, ~~but like a few days ago, I was setting up something like a piece of software trying to get it to run. And I just. ~~Like ~~every now and then [00:43:00] I put in a link,~~ uh,~~ I wrote down some notes like in the chat box here and then I told it to store it as a note and it just stores it as a note and in my Obsidian I can see it all, what's going on.

**Joseph:** ~~Mm hmm.~~

**Sjoerd:** So it says the task to add Calendly to the assistant, which I mean, it actually hasn't completed, but I,~~ uh,~~ just as an example,~~ um,~~ but yeah, I can ask it what's on my calendar,~~ um,~~ and I can just send it regular messages as well. Also, one thing that I really want to,~~ um,~~ do as a next step is,~~ um,~~ is allow it to send messages back to me. like throughout the day for whatever reason.

**Joseph:** Like what kind of messages?

**Sjoerd:** ~~Um,~~

**Joseph:** Just~~ like,~~ 

**Sjoerd:** hey, a reminder

**Joseph:** encouragements, or 

**Sjoerd:** something like no, imagine if you hook it up to your email and then whenever something important comes in,~~ uh,~~ it tells you,~~ uh,~~ or like maybe a, like a daily digest or something in the morning, you go ~~like, uh, ~~receive a message like, Hey, this is what happens when you were asleep. Something along those [00:44:00] lines. ~~Um, ~~so basically want to take away. As many things, like different apps you need to check, different websites you need to browse through, and just make it like a one stop shop for everything, like all the important stuff. ~~Um, ~~like everything might be a bit, like of course there's still going to be some apps that you want to use for, ~~like ~~whatever reason, but just for your day to day.

~~Um, ~~This could be pretty amazing, but right now where it is, like I use it daily. Questions like that, ~~like ~~am I free today to work on cool stuff? I can just ask it and it's nice, it works really well.

**Joseph:** It's ~~like, ~~no, you're overdue on all of your tasks.

**Sjoerd:** ~~Right, ~~that's right. Yeah, and I'm just gonna add on to the pile of different tasks, but right now it's already,~~ uh,~~ yeah, so it lists different tasks that I have on my calendar. ~~Uh, ~~you've got some time between regular work and a chat with Joe Rosenbaum, like here we go.

**Joseph:** Yeah.

**Sjoerd:** But yeah,~~ like, uh. I mean, so much, ~~so much potential, but right now what it's already able to do is [00:45:00] like super helpful. ~~Um, ~~just ~~like, uh, ~~I reached a bit of an inflection point, like this is something I can use in my day to day and that hasn't always been the case. Sometimes you build something and then over time you forget about it because,~~ well,~~ it's not really that useful, but this time I think I've got something really cool.

**Joseph:** Yeah, and ~~it, ~~it bootstraps to the next level too because now you're interacting with your life through natural language rather than having to ~~like ~~flip around and be scattered, ~~you know, ~~it just now allows you a next level of organization and,~~ um, ~~ ~~you know, ~~ability to continue to experiment and improve on your own like effectiveness and efficiencies, which has, you Hopefully,~~ like,~~ exponential effects for you in terms of whatever you're trying to accomplish.

**Sjoerd:** ~~Right, right. Like,~~

**Joseph:** ~~Mm~~

**Sjoerd:** not super interested in being like the,~~ uh,~~ like the productivity, like insane productivity stuff. ~~Um, ~~[00:46:00] I just want to make it as easy to use as possible. ~~Um. Like, ~~it's not so much to,~~ um,~~ how do I put this? It's more, more just a really useful tool for my day to day,~~ uh,~~ to free up time to think about more fun stuff,~~ um, ~~

**Joseph:** ~~hmm.~~

**Sjoerd:** and not necessarily to,~~ uh,~~ to ~~like ~~be productive 100 percent of the time.

**Joseph:** Yeah,~~ ~~

**Sjoerd:** ~~Like, if, ~~

**Joseph:** I agree.

**Sjoerd:** Yeah, if this leaves free time to, to do fun stuff, to mess around, to play around, then ~~that's, ~~that's great, that's amazing. And,~~ uh,~~

**Joseph:** Yeah, I always think about it as,~~ like, the, ~~the aspiration for me is how do I use this stuff to give me more time to work on the things that I'm most interested in? Or I'm most intrinsically motivated to do, to be creative. ~~Um, ~~and I'd say Obsidian for me has been, ~~you know, ~~huge with that. And as I copy and paste what you've done here, ~~you know, ~~I'm really excited to like, how do I free [00:47:00] up more of my time to do more of the things I enjoy doing unless ~~the, ~~the rigmarole, mundane stuff I don't like doing.

**Sjoerd:** yeah, no, of course, I,~~ uh,~~ I'm with you, absolutely,~~ like, uh, ~~so far,~~ like,~~ no taking. I've done, I think,~~ like,~~ a dozen attempts, and nothing really stuck, ~~um. ~~But it's super cool that I can just talk into this really quick and then have it store a note for me. ~~Uh, ~~and correctly tag it into different categories that I've listed in the,~~ uh,~~ in the initial prompt in,~~ uh,~~ inside of the assistant. ~~Um, ~~and that's,~~ like,~~ really nice. ~~Um, ~~I think the,~~ um, like, ~~this way of communicating with the assistant, just being able to hold the,~~ uh,~~ microphone button down and then just talk into it, just send a quick message, is,~~ like,~~ for me, it's It makes a big difference. ~~Um, ~~I thought the voice one was ~~kind of ~~cool, but sometimes I just need to think for a second and I don't want to have it. ~~Like, ~~I feel like

there's a 

**Joseph:** there's like urgency. 

**Sjoerd:** Yeah, Yeah, yeah. I feel like there's a pressure and then suddenly it picks up a tiny bit of noise and it starts talking back. ~~Like, no, no, ~~no, wait, just shut up.

**Joseph:** ~~Yeah, ~~[00:48:00] yeah, 100%.

**Sjoerd:** Oh, yeah. ~~Um, ~~And,~~ uh,~~ yeah, I,~~ um,~~ I think someone else,~~ uh,~~ made like ~~a, ~~a fairly similar demo a little while ago. And it was funny that they used,~~ uh,~~ a similar example. So I want to do a web search and how it works. And,~~ um,~~ the question was,~~ uh,~~ what's going on with Sam Altman like a good example of something super recent that's,~~ uh, um, ~~yeah, something super recent that ~~like ~~a great example of ~~like, uh, ~~just a web search

**Joseph:** yeah, because I know that,~~ uh,~~ the Assistance API doesn't actually have web browsing as part of,~~ like,~~ the,~~ like,~~ in build functionality. So you have to ~~kind of, like, ~~hack it together. 

**Sjoerd:** and always say please to our assistants. It's,

**Joseph:** Yes, always gotta be nice,~~ uh,~~

**Sjoerd:** Oh, so this is a different,~~ uh,~~ message than I expected.

**Joseph:** ~~well, I mean, ~~it is more recent, right?

**Sjoerd:** Yeah, I guess so. ~~Um, ~~but no, that's also a [00:49:00] good example that it actually, yeah, I wonder if it's actually,~~ uh,~~ yeah, no, ~~it's still, ~~it's still in the large language model that can make mistakes, but yeah.

**Joseph:** ~~Well, ~~let's,~~ uh,~~ let's see, Sam Holtzman.

Yeah, this is,~~ uh,~~ this is true. It pulled from an article that was released today.

**Sjoerd:** nice. So perfect example. Nice. No, but this uses perplexity, which, I'm actually, I like this way more than,~~ uh,~~ than just the regular web browsing. Their API is nice

and fast. Oh, it's one of my favorite AI tools, to be honest,

**Joseph:** Yeah, why is that?

**Sjoerd:** it's,~~ um,~~ like it's basically almost completely replaced,~~ uh,~~ all of my regular Google searches. It gives, it's fast. That's one important thing. ~~Um, ~~it lists the sources like really nicely. ~~Um, ~~And you can just keep asking questions. If something's unclear,~~ um, So, ~~for example, I was looking into,~~ uh,~~ like white labeling some open source [00:50:00] stuff. ~~Um, ~~And ~~it's, ~~it's much easier to ask a bit more complicated, in depth questions to,~~ uh,~~ like perplexity AI than it is to Google around, search for the right information. It just does it for you by considering like the first 10,~~ uh,~~ search results,~~ um,~~ and especially with the GoPilot, it does,~~ uh,~~ it does ~~like ~~three different searches at once,~~ uh,~~ and grabs all the information, something you would do yourself normally,~~ um,~~ and then gives you a neatly organized, nicely written answer to whatever question you asked.

So

**Joseph:** I'll have to check it out. Can you prompt it to give the response in a certain format? Because right now, like for example, in Obsidian, when I'm doing research, ~~You know, ~~I have a GPT that will output essentially like a little wiki article on whatever topic I'm interested in, but in Markdown with the backlinks and tags, so that I can very easily, ~~you know, ~~get that into the vault.

**Sjoerd:** this is something I was actually a little bit disappointed ~~in, ~~in that the API doesn't support like sources. ~~Um, ~~and [00:51:00] for this assistant, it's fine when I want some, when I want to do a quick search on something I can just ask and it'll come back. ~~It's, ~~it's perfectly okay. But,~~ um,~~ I think that,~~ um,~~ yeah, so that doesn't support sources, but their own, like when you just go to perplexity.

ai, it's,~~ um,~~ they do mention sources and there's some room for prompting, but I haven't really experimented with ~~like ~~using,~~ uh,~~ different markdown or ~~like, uh, ~~everything in JSON or something, but ~~I mean, ~~I think it'd be awesome if they would like output markdown in JSON with,~~ uh,~~ with sources mentioned. That would be super cool.

~~Um, ~~but I think, yeah, their API is still ~~like, ~~it's nice. It's very fast. ~~Uh, ~~so they've built their own 7b model, but you can also use ~~the, the, ~~the Mistral 7b model. ~~Um, ~~and. ~~Like, ~~it's ridiculous,~~ like, ~~ ~~um, ~~it's about just as fast as you would expect,~~ uh,~~ like GPT 3. 5 to give you an answer. And this one includes web [00:52:00] search as well, so it's impressive. But yeah,~~ um,~~ let's see, I actually made a small mistake, I should have,~~ um,~~ for the images,~~ uh,~~ I,~~ uh,~~ I set the quality to low and it's like super low. ~~Uh, ~~it can't read anything from a document, so I need to set it to high, but that's like a click and it's done. But that's okay, just put that as a note, just do a super quick extra one. And now it stores into my obsidian.

**Joseph:** It's so nice.

Ugh.

**Sjoerd:** And it's ~~like, ~~not super duper fast, but that's just a beautiful name.

**Joseph:** Sam Altman Concerns.

**Sjoerd:** Yeah, exactly.

**Joseph:** Cool. ~~Well, uh, ~~thanks again for sharing and,~~ uh,~~ let's get this, let's get this out to the world and hopefully people can start building their own personal assistants.

**Sjoerd:** Yeah. I think in time I want to make this one accessible to people as well, but I haven't really figured out how I'm going to [00:53:00] pull this off and,~~ uh,~~

**Joseph:** Yeah.

**Sjoerd:** and I can't pay for everyone to use this.

**Joseph:** ~~No, no, ~~no, it would have to be like either a product or you're just ~~kind of ~~like giving away the blueprint and how you plug in your own APIs and stuff like that.

**Sjoerd:** I'm not too sure if I want ~~like, uh, ~~got the blueprint ready, but I'm bit doubt whether I want to share it or not. It's,~~ uh, ~~

**Joseph:** ~~Mm hmm.~~

**Sjoerd:** we'll see. I still need to,~~ uh,~~ to develop it a bit more, and I think then,~~ um,~~ once I've got the,~~ um,~~ like the CRM, the relationship manager in there,~~ um,~~ I think that will be like ~~a, ~~a big step. And then we'll see what I, we'll do, I'll make of it afterwards. ~~Um, ~~ 

**Joseph:** Cool. ~~Well, ~~I'll catch you later.



