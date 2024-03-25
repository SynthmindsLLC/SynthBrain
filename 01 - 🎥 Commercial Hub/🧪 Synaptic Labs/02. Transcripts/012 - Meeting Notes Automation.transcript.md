  

  📍 welcome chatters, I'm back here again with Urosh, our chief of operations, a wonderful automation engineer as well,  and today I'm gonna work with him to show you all how I've set up an automation. To take notes coming in from the transcription of Google Meets and getting it into my Obsidian folder, both the entire transcript as well as the meeting notes and any to dos, uh, relevant to me from those meeting notes.

So,  we're going to go through the automation first. I'm going to show you how it works and then we're going to have you share your screen, Urush, and you're going to, uh, set one up for yourself.  Because this is

going to give me a blueprint? 

Yeah, I can give you a blueprint, but I also kind of want you to try to set it up, uh, you know, so that you can, you can figure it out the hard way.

   📍 First of all, we're in make. com,  and we've created a scenario here. So, if you just go to this little, little button here, you have your scenarios, you'll do create a new scenario.  Obviously, I already have it created.  We're gonna go to edit.  So let's walk through what this is doing just on the conceptual level, and then I'll go into module by module. 

So first is we have this module, which is a watch for documents. This is so that in the folder where all of the transcripts are going to come in,  automatically, this is set up through Google Transcript, it's just going to save somewhere. You just have to hook this up to that, so it's My Drive Meeting Recordings, and whenever a new file gets in there That's the trigger to start the rest of this jazz. 

Next is you need a Google Doc get, uh, I should probably zoom in a little bit, get content of a document. So the idea here is it comes in and you buy the document ID. You just want to extract all the text that is in that document.   So we route. Uh, the, the text itself, we create a file from that text, and then we upload that file into our Google Drive, uh, where our, uh, our vault is saved in Obsidian, so it gets in there.  One important thing, uh, you're gonna have to do is the file type. So you can call it whatever you want, we'll get to in a second, but you just have to make sure that the extension ends in md because that's how Obsidian reads the files.

Okay, 

Okay. Next.

does it have to go through Google Drive? So technically you would need me to actually put the whole vault on the Google Drive of mine.

Correct. You would want to put the whole vault in your sort of personal Google Drive,  um, or the company Google Drive, but your personal folder in the company Google Drive, because there's no way to access it like directly on your local machine, if that makes sense.

so we would also need to switch from the previous video, we would need to switch from F drive to the Google Drive, correct? The whole

Well, again, this is only if you want to set up this sort of automation, you're going to need your vault in some sort of cloud drive.  Okay, so now we have the full transcript, but really what we want and what we'll use most frequently is some sort of, you know, summary. So,  we feed the full transcript through ChatGPT, so we have this module here. 

I'm using the latest version, which is, uh, Turbo.  Because there's a nice long context limit. It's pretty good at this kind of stuff.  Uh, and so I just have a, a prompt in here which I'm happy to share. Essentially it's really good at taking notes. Analyze the transcript and find things that are most relevant to me.

Extract those key points. Identify action items. This is important, is we want it to tag, like, the person. And then format it. Uh, in a way that obsidian is going to add it to our task list using, uh, whatever that plug in is. So you want it to create the checkbox and end with hashtag to do or whatever you have set up in your task list as that tag to market as a to do item. 

And I end just with a couple things just for organization is to begin every output with the document ID in backlinks. I'll explain that in a second. And then, uh, the, uh, the date in backlinks. This is important

actually click on the actual transcript, correct?

uh, you're skipping ahead. Yes. So, uh, this will connect it or create a backlink to your daily note.

And then this will create a backlink to easily get to the transcript, like you said. Uh, you just need to make sure that what you're naming the transcript, in this case I have it as Document ID, is consistent.  So then, that's going to run the full transcript through there, and then same idea. We're creating that file from that text that comes, and then we're uploading that file to the appropriate folder in your Obsidian Vault. 

And the last thing we have here is just moving to the outbox, essentially, so.  Just again, so we don't double up or get confused, it's just going to move whenever it completes something at the end to our outbox so that things don't get super cluttered.  So I'm going to pause there before we run it. Do you have any like questions or thoughts, Urush?

on the Google  Drive that you run on your Explorer,  you can run different accounts because all my transcripts are in SynthMines.  But I would like my obsidian brain to be in my personal gmail.

Yeah, and that is totally fine to do. 

 I'm going to just run an example. Of this so people can see it. So,  we have this meeting from, uh, yesterday that we did. I'm just going to make a copy so it sees it as new.  And we're going to put it in, uh,  the meeting recordings folder. 

So this is important because the way this works is that it's only going to recognize a file if it's newly added. So everything I have in there isn't going to work.  But we'll just run it now and hopefully it works.  So you'll see it's, it found the new document,  turned it into text. Now it's turning it into a file to go into the Obsidian Vault for the full transcript. 

It's running the ChatGPT prompt to get the bullet points and whatnot. 

Yeah, I would need probably not only focused on me, I would need the whole summary.

Exactly, so the one thing you're going to have to play around with, I'll provide the prompt that I have because for the most part it's going to work for you, but you're going to want to replace my name with your name or the names of the people, you know, that you have to follow up with the to do items. 

It's going slow

Turbo. Yeah, but that depends on the size of the transcript.

Yeah, so it was an hour long conversation, so it's going to be pretty long.  Note that this is going to cost you money too, it's going to be pennies. It's not going to be a lot, but just so you know, you know, you're going to need to have an account.  So finished up, it has everything. We're just going to go into here to make sure, you know, we have the copy there and  it should have 

Yep, it put everything in here.  So now let's go to my Obsidian Vault. 

And I save everything in meeting notes here.  These are the notes themselves. This is the copy.  Oh, it's still uploading it, so we're going to give it a minute. But if we go to the transcripts  I wonder if this is 

Is there not a better way to actually name these? 

There probably is. There's definitely ways generally to make this, you know, better. Um, but this is what I have for now.  Yeah, it's still, uh,  it's still loading this conversation, so we'll give it a minute.

there it is.  So here we can, this will bring us to the transcript itself. 

Okay.

then we have me tagging everything and everybody else. And then we have, oh my god, did I really have this many action items? This actually gave action items

For everybody.

so it screwed up a little bit. Um,

Which is fine. I want that. Which is

yeah, yeah.

Um, but you can just, like, be very clear, you know, about saying, Hey, only do the action items for this person.

So this is amazing. You can actually hashtag me and see what's, what's  mentioning me.

Exactly. And then, uh, the idea, I wonder  why it's not doing it.  This is a little annoying. It should be adding them to my task list. I wonder if I just need to get out and get back in. Let's see what happens. 

Here we go, yeah, so I just needed to update,  uh, I just needed to X out and come back in, but

Aha, so this is your to do list for today.  Correct?

this is just the to do list from this meeting, which is nice, so. It has, where did all these to dos come from,  um,

Okay.  And you can query your professor to ask, Hey, what did I do? 

Yeah, if you want. And then when you, when you, um, knock something off of here, it's actually just go down  So when I click it on or off in   📍 here, it adds it or takes it off on the main task list too. So it's all connected.

  

  📍 hello again. Uh, we're going to have you build this automation. I'll just kind of be here, your cheerleader. I'll help answer questions as you're doing it. Um, so, so yeah, so you've moved your vault into Google drive.  

Yeah, so, hi guys. So, we are coming back from, uh, from a little, uh, break. Uh, I'm back now again, uh, in this video. So, 

 what I did in the meanwhile, I moved my vault from  F drive to my Google drive in here on my private one.  Also, let me see, maybe this is,  uh, I'll be able to zoom in, in the make.

com. So let me share my screen like this.  And then we are going to go with  Google.

You're going to need, yeah, Google docs, Google drive and open AI. for those of you who have never used make. com before, They have these things called modules, so it goes by application, and then within each application there are multiple options you can choose from.  So, right now we have the Google Doc one.  It has watch docs, again this is important because it's going to pay attention to see if there are any new documents coming into the right folder.  You've got to give it permission, sign in through your account.

  Meet recordings, that's it.

Yep,

Limit to two. Okay.  From now on, first of all.  do it from now on, I'll be able to specify later if I want. So we're going to add another module. Uh, we're going to go add docs. We're going to get content of a document.

Yep.

So, same account, update your connection, okay.  Baby is crying there, I  don't know if you're hearing it. 

I actually cannot.

Yeah, nice.  Uh, uh, uh.  Here's the document ID.

ID, yep, that's correct. 

So now you want to add a router, correct?

Correct.

 Show route, show route. This is  the router.  Okay, so first we're going to actually add a file there, so let's do google drive. 

Are you doing this all from memory?

 Yeah,

Oh my god.  Man's got a steel trap. 

so we are now going to,

Create a file from text. 

 yeah, I'm just, I hear this,  choose an account,  oh this is a separate module, that's why it's asking me to log in again,  maybe it's doing something good in there, I can hear bravo, bravo, yeah.  New text file location.  Ah, so we're going to put it in my  Oh, I, I logged in with the wrong, um So I, this should have been where the vault is, correct?

Yeah.

Okay, so let me,  uh, uh, uh, choose another one.

And so the, the idea here is you're, you're probably asking yourself, why do I need to take the Google doc, which has what I want and go through this process? And it's because  Obsidian only really reads markdown files dot MD. So all we're doing right now is essentially converting the Google doc itself into a dot MD file. 

Why is this restricted connection? It's not possible to use restricted scopes with customers at Gmail accounts. For

Oh, that's why. You can't, you probably have to set up like an OAuth or something for a personal account.  Um,  you, you can't,  since it's not like the SynthMinds account or whatever. 



So technically I could use my drive on SynthMind's account. That wouldn't be an issue, correct?

Yeah, so what I've done is I, I have it, I have my vault on my personal account, but I shared it with my SynthMinds account so that I can still

How did you do that?

So go, go to your personal.  Yeah, one and where it is, and you just go to, you might need to do it in Google Drive, I don't know, can you share from the system finder? 

So what do we do? Show more options.  Share with Google Drive. Is that it?  Nice.  Share with  my SynthMind. Mm hmm. That's  fine. Okay. 

 

now you should be able to go back to make, and just when you're choosing your drive,  you choose the share it with me. 

Okay.  Makes sense.  I think it's a good that it's good that we have actually these kinds of issues because people will probably encounter the same.

they'll be like, how did they make that work? It's like, okay, well, you gotta take some extra steps if you're using your personal account.

this is, 

You gotta go to shared with me in the

I am sorry. Sorry. Yeah.  Obsidian brain. Yes.  Okay, file name is, 

I just go with document ID.

I don't want the document ID, leave me alone.

whatever you  want. 

Let's do it like this. Uh, how do you put the date in here? Date? current date and time. Uh huh.  Like this. And then we add like this. And then we go like this. And then we add an MD. File

to do MD yet. 

content is text content, correct?

Correct. 

Correct. Convert the file to Google Document? No.  Okay. And then we add another Google Drive. But we add now,  uh, 

Load a file. 

Where is it? Upload the file. Here it is.  Okay, so we found it. We got a content. We created a file from it. And now we added it to 

You want to send it to wherever you just want the transcripts to live in your vault..  

 That mine's folder here.  Meeting transcripts. There it is. Okay. So now it's file going name going to be file name.

Yeah, and this is where you put the md at the end.  And then just make sure data says text content as well.  You're gonna have to go down to the next, um,  Yeah, in there,  in the Google Docs. 



Okay. Okay.  So we are pulling  back from the actual Google doc. We're not pulling the content from the file that we created in here. 

That is true. So, it's very possible that, uh, you might be able to just  skip that  module. I'm not sure.



That's one thing. So now we want to add  another one which should be an OpenAI.  Is it an OpenAI or is it a ChatGPT? It's probably OpenAI.

It's OpenAI. Yep.

 Loading. I clicked something. I don't know what I clicked. Uh, completion should be correct.

Yep. 

Yeah.  I am somewhat of a automation expert myself.

 I mean, yeah, you're better at this stuff than I did. It took me a while to figure this out.

So this is, uh, turbo. Yeah.

Yeah, I use Turbo. I would recommend it. It's not that expensive and it has such a huge context window.  Uh, and then I did, for role, I do system.

Uh, messages, add item.  Rule system.  What do we want to

And this is where you put the prompt, so I can send you the prompt I have and you can  update it based on kinda  Cause obviously it's specific to me. 

There you go, I sent it in Google for ya. 

They're going to see our chat, but now let's do this  and now 

Yes, add it to the prompts.

 uh prompt transcription And  summary.  Okay mission

Just make

transcript

replace my name with your name.

 So, let's go back to make. com,  and then  here I'm going to delete this.  That is the  ID of the,  uh, 

So, the idea here is that we want to create a backlink directly to the transcript. So, however you named the

did, mm hmm.

is what you want to put in there. 

That should be the name of it, correct?



You can get rid of all the black stuff and the slashes and  Now, you just need one. You just need whatever it is exactly called in

 Uh huh, okay. 

the transcript.

Okay.  Mission, act, and expert, blah blah blah. Okay, let's do that, and then,  out of that, we are going to,

Oh, we're not done yet. 

go advanced.

want to go down to item two,  or add another item.

hmm,

 Because remember, we want to actually send the entire transcript too. So, I have this as role  user, and um,  And then the message content is just text content. 

You could probably do it all in one, but  I figured it'd be better to keep it separate. 

And that's that, okay. Are we done with the OpenAI module?

The only thing is, I um,  I did have, I set the number of tokens to 750, but you can set that to whatever you want.  It's lower down. 

I don't want the temperature to be 1.  To like, 2. 5.  The 

Yeah, I have my temperature to zero. 

Yeah, probably

Don't want to getting creative on me 2,

tokens,  yeah. I'm going to  ask Wes to give me.  So, I'll

000 that's way too many. Okay. It's like almost becomes useless at that point 

I'll put 1000 in

Yeah, a thousand is fine 

Okay. That's fine.  Uh, what's the output of this? We need to actually put this into

So it's the same thing to create a file from text and then upload the file I just you're gonna upload it now somewhere different 



I like my dates in there. So we will have, what's this? This is probably a message in

Yes, exactly. It goes choices and then message content.

Um, this is now, then,  um,  this is the actual file.  So,  file name, you don't have to put the content in there, the content goes down on the bottom. So let's do the, um,  um,

You can just do the, I have the name,  just the file name, 

Where's the file name? 

and the original Google Doc.

Ah, yeah, you're right. Or we can do a document ID. And

whatever your heart desires. 

then content goes in here. Yes. Convert file. Okay. And then we do again, upload a file. 

  📍  Transcript. 

  📍 Name.  Dot MD. 

Yep. 

Is.

The completion from ChatGPT.

huh.  Yes. Choices. Message. Content.  That's it. Correct.

Yep. 

And what's the third bunch? Yeah,

third is if you want to like move the transcripts that it's done into a specific folder or whatever, like an outbox of some kind or just to let you know it's been done, you can do that, but totally optional.

I don't want that. Let's

you should be all good. Yep.

 don't think it's going to run. It's probably not going to find anything.  So we will do this choose where to start.  Choose manually.  What can we do?  Probably empty. But we'll see.  The magic happens. 

it's looking good so far.

 My turbo is much faster than yours. 

Except not.

It's not. 

I'll play some fun music at this point. Speed us up. 

I have the worst habits when I actually, uh, either I hum on the meetings as you can notice, or  I mumble in my mouth, like, but actually I'm writing something to somebody like, so  this

Okay, let's see if it worked. 

Let's see. Where's my Obsidian?  Let's summarize meeting transcripts.  Ooh, very nice.  Ooh, Scott, I had the date.  I got the.  Oh, it doubles the date because there is a date already in the transcript. Okay, I'll fix that.  Nice.

the tasks say to do after them? Or whatever you have for checklist? Have you downloaded checklist?

I didn't download the checklist.

Oh, so that's not going to work for you yet. 

But there is, you see, I can actually

Yeah, but it's not going to like feed into anything that you can keep track of  easily. 

Which is  

So obviously you can set this up for any transcript service, so you could also have Fireflies,  you could do Zoom,

Yeah. Yeah. Okay. Thank you, Joe. This is amazing.  Thank you, chatters for staying with us.

  📍  📍 YEah, so hopefully this is helpful. We'll share the blueprint  some other

Oh, you shared the blueprint with them, but you didn't want to share

Yeah, yeah, because you need to learn the hard way. 

Okay. Thank you so much. This is amazing. We just need to figure out how to, uh, change from the completion. We now just need to find what's the proper name to actually use for these files. Because this is ugly for my, uh, super visual eyes.

You can see I'm a very visual guy.

Yeah, totally. I mean, you could do another chat completion. This feels like such a waste, but then have that chat completion

Just be a name.

the name.

Yeah, yeah. But that would be probably the best way to do it. Like, hey, I'll summarize this, you know, name, this format, put it in a Yeah, that

Yeah, and you could use, you could definitely use 3. 5 for that. You wouldn't need any

Definitely. Yeah. Okay. Thank you so much.

Yeah, see you later. 

