  

 Chatters, I'm really excited for today's tutorial. I want you to, if you're a gamer, you've probably been through this before, where the first part of every single game, they're more or less teaching you how to play the game through playing the game.  And then at some point, once you've learned the basics.

You then open up the world to the player and they have all these kinds of options that they can do You know very common. This is like nintendo's philosophy in particular  So we're at that point now where we've learned the basics, how to navigate, how to create some things, how to use daily notes, all that kind of fun stuff. 

And now we're going to get into the open world, which for Obsidian is something called community plugins.  Community plugins are more or less a user generated app store within Obsidian. And this is a common joke, I think, within.  DM sitting community. If you're like, how do I do this? The answer is always there's a plug in for that.

So we're going to show you how to access the plug in store. We're going to download and show off a couple of plugins. And then a lot of these future tutorials are essentially going to be me showing you how to create really awesome workflows using some interesting plugins.  So let's get started.  So let's imagine, that we're in our vault.

And you want to go down to settings here.  Now you'll see this, called community plugins. We're going to click into there. And it gives you a little bit of a breakdown of what this is. Now, something you've got to be aware of is since these are community plugins, that means there is no real, enforcer of making sure that these plugins are safe.

I have not had any issues, and there's some, quick little ways to look at a plugin and know whether or not it's legit or not.  But either way, don't worry too much. The chances of anything bad happening is fairly small, as long as you're willing to just take a second to think about it.  So you want to hit this button, turn on Community Plugins. 

And then you see here it says Community Plugins, we have our current plugins, whatever.  We want to go to Browse.  And this is going to bring up all of the plugins. Now, something I want to talk about is this view, these cards, one number you want to be paying attention to is this one right here, the higher, the better.

And what that means is this is how many people who have downloaded this particular plugin. If it has one or two people,  maybe you got a question, it's legitimacy. But if it has almost 1. 4 million downloads, you can be fairly confident that this is something that's legit.  So we're going to start with two easy plugins today, just so I can show you a couple of things in terms of functionality.

The first is going to be Calendar. Now, Obsidian doesn't really have a great calendar view as, the base. And so this one is a lot better and easier to use. You can read the comments and whatever, but more or less all it does is take whatever metadata has for a specific date and creates a calendar out of it so that you can easily go back and view things that you did on that particular day.

how we install community plugins is super simple. All you gotta do is hit the install button.  And just like that, it's been installed. Now before you leave this view, you're going to want to go to enable. That just turns it on essentially. you'll see here it turned to hotkeys. This is just so you can set a hotkey for it to bring it up quickly.

But before we go into any of that, let's actually go back. you'll see here now we have this little installed plugins, and we have it right here. we can do a couple things. One is you can turn it on and off.  Right from here, you can uninstall it by hitting this trash button, set it to a hotkey, and then go to options.

We're going to go to options. Pretty much every plugin has a few different things that you can play around with in terms of the settings. Or you actually need it to set it up, so let's head in there. You probably are not going to have to change anything in this one.  But just, take a look, see if there's anything you want to do. 

Word should be presented in a single dot. That's on the calendar just to show you like on that day something happened. When do you want to start your week? Show a confirmation modal before creating a new note.  Enable this to add columns with the week number. Whatever. 

so now that we have the calendar app, there's multiple different ways to use it, but typically what I do is I open up the sidebar here, and you'll notice that we have some of our apps already here. We have the outline, tags, backlinks. So let's just pull this out a little, and you'll see this new little app right here, which is the calendar.

I don't have a lot in here, so you're not going to see a lot. But you can see right here on the 6th, I've started this note. On the 29th, you have that little dot of a note. And when I click it, it's going to bring up that note.   that's pretty much it for the calendar, just like any other calendar, just a quick way to look at your notes. You may or may not use this, but I just wanted to show, how to simply download probably the easiest plugin there is.  The next plugin we're going to do is a little bit more complicated.

One thing we're eventually going to be doing is hooking up uh, OpenAI ChatGPT to our notes. Before we do that, though, that's going to be a whole other video because there's, too much to talk about in this one video. But what I want to do is download Whisper.  What Whisper is, for those of you who don't know,  is a speech to text tool.

It's a transcription tool.  And all that means is that, you can talk to your computer and it'll put the words in there for you.  I don't know about you, but sometimes I like just talking when I'm taking notes rather than actually writing things down. And so I like this tool for the computer for my laptop so that I can do that. 

Now you'll see I quickly went into the options and here we have a few more things to play with.  The main one being our API key.  Now, for those of you who don't know what this means, essentially what you can do is if you have an account, which I'll show you, on OpenAI, you get this secret passcode, which you can put into things, which then can draw on their model to do whatever you want to do.

In this case, take your speech and turn it into text. You're not really going to have to change anything here. You can save the recording if you want. You obviously want to save the transcription. You might want to create your own folder for transcriptions. Whatever you want to do.  But just before we do any of that, let's head over to OpenAI's website so that I can show you.

here we are on OpenAI's website. This is the pricing section. I just want to show you how much it costs, because it does cost money. But it's so cheap. You can see here, Whisper, it's only 006. cents per minute, so a fraction of a cent, a little bit more than half a cent for each minute. So it's really not a lot, but it does cost money, so just a heads up there. 

Okay, now we want to find our API. So the first thing you want to do is go to your account. You can go to platform. openai.  com it'll take you ish here. All you gotta do is you gotta look for this sidebar.  And you'll see here we have API keys, but if you don't have an account yet, you just got to go to settings, billing and set up your payment methods or buy some credits.

Once you do that, we want to head over to our API keys and you'll see, I have a ton right here. We're going to create a new key, which I'll delete after this. So you don't use all of my credits. So let's just say  whisper. you might want to just make one that's just called Obsidian and you just use the same API key for all your Obsidian things.

We're going to create this, we're going to copy it. Make sure if this is something you want to reuse that you put it somewhere.  if you're lazy like me, you can also just put it in Obsidian. It does save it there without hiding it. So let's head back.  So you're just going to stick your code right in here. You look over this other stuff. Let's just say for now, if you don't put a folder, it's just going to create a folder that's named after this.

So we're just going to do that for this case, but you might want to put this somewhere specific. I would actually recommend that.  There's no save button, so don't worry about it. It automatically saves once you put something in, so we're just going to X out of here. 

you may or may not have noticed it, but we have a new little icon here, which is the open recording controls. Now, again, you can go here or you can use the command palette or a hotkey. For example, if I bring up the command palette, like a whisper, I can upload an audio file, which will just take what you've already done somewhere else, and you can transcribe it, or you can start or stop a recording. 

Let's start or stop a recording, or you can click right here.  Okay, so it'll bring up this little simple bar, and you just have to hit the record button. 

So right now it is recording. Apparently  I don't see it. I wonder if it's because my microphone is on to talk to you all, but let's just hit this. It does say that it's recording right here, but let's just stop. 

And look at that. It actually did record it. So you'll see here that it is added the actual recording into this file. Just based on the date and time and then  And look it's written what I've, said.  So that's it for today. These are just two community plugins to get started. My call to action to you is beyond downloading these two plugins and testing them out.

It's just to start look through some of the other plugins you might be interested in. Feel free to skip ahead. Next time we're going to be talking about how you use this for to do lists and a little bit of project management. So if you want to skip ahead and start playing around with plugins, I highly recommend you start checking them out. I also don't want you to get too some of them are more complicated to set up than others. It takes a little bit of fiddling around. Next week we're going to be looking at the Kanban checklist and tasks plugin.

Maybe don't skip ahead to those just so I can walk you through it. But other than that, start looking around, start thinking of problems and asking yourself the question, What is the community plugin for  📍 that?  So as always, thanks for listening. Appreciate you and I'll see you next time. 