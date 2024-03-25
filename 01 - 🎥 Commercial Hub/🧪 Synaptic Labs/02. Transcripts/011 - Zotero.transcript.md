  

 Hey, Chatters. As promised, I'm going to bring you a free way to be able to do content capture wherever you're reading and doing things.  Unfortunately, unlike Readwise, this comes at somewhat of a cost of it's more complicated to set up. It's not necessarily as user friendly or automated, but it's still really good and you have more options with this in a lot of ways, actually.

So.  Today we're going to talk about Zotero, what it is, and how you integrate it with your Obsidian Vault.  This is free to a point. Uh, the only thing you have to pay for is storage up to a certain amount. So if you're not a wild child like me and have like a bajillion different research PDFs in your Zotero,  that's going to last you essentially infinitely.

If you are doing a lot of actual research,  You're pulling in a lot of PDFs. You're going to go through that kind of quick and you might need to pay a little bit of money, but for most of you it's going to be free.  So what is Zotero? It's your personal research assistant. Really all it does is, similar to Readwise, just capture everything in the metadata and then allows you to annotate and create highlights and notes and all that kind of stuff to make it easier to capture the things you want to capture. 

So as we're still in plumbing mode, what you're going to want to start off with doing is just downloading it. So go to Zotero. org, you hit the download, follow the instructions, probably have to create an account.  

 Let's take a look at what Zotero actually looks like when you open it. Pretty straight forward. You're not going to have these two folders yet.  Uh, but you'll want to keep things organized. You'll probably just have unfiled items.  I try to keep things simple, just an inbox and an outbox. He created a folder by clicking this, or, you know, you know, right. 

Clicking or going to file whatever.  And I just try to have it of like, okay. Everything that I want to read. I put in the inbox, everything I have read and highlighted and annotated. He goes to the outbox, simple as that, but you might want to go by tight. You might want to go by category, whatever. However you want to organize it. Just pick something and stick with it.  You'll see here. 

This is the list of the things I have in my, my, my poor inbox.  Uh, so this is everything you've pushed in here. When you want to get some of the metadata, it'll just be up here on the side. When you click on something.  It has the citation key. The title, the authors. It's got everything. You kind of want the website. And then when you want to actually read this thing, you can either click the arrow here or you can double-click, it'll bring up the PDF.  I'll just bring that up.  

 Now we're in this paper and you have a few options. 

One is to highlight.  

Another is too.  Create a note.  Which you can tag.  And the last is to capture an image. I mean, it can be text to it. It's whatever, but you just highlight over and it will pull whatever you want or whatever's in this box. Eventually into your obsidian vault.

 Now that you have some idea of what Zotero is and more or less how it works, we need to start downloading a few things to be able to hook it up to Obsidian and be part of your workflow.  So the first thing, just like Readwise, it has a Chrome extension to help you out. 

What you want to do is go to the Chrome store, or whatever store, and look up Zotero Connector. I already have it downloaded, but you'll download it.  And you'll see it come up here. This might change a little bit. But it'll be this little paper, or it might be a pencil looking thing, or a Z. And this is just what you click when you go to research to get it in your, uh, your Zotero.

So let's try it out and see how that works. We'll go to Archive.  We'll look up AI.  We'll just, uh, choose this one, I guess, because it's more or less the first one.  And then we go up here, and you'll see this is turned to the pencil and paper. We're going to click that.  You'll see it's saving to my inbox, that's where I want it.

And it'll take a minute, but it's getting all the metadata, it downloads the PDF, and it's going to get a little snapshot of everything.

So that's step one, that's what you're going to be using to get everything into Zotero.  Next we need to start working on how do we get things from Zotero into Obsidian.  So you're going to want to go to this website here, I'll put the link in the description, and you need to download Better Bibtex for Zotero.

 Uh, it's going to give you instructions on how to do this, but you just go to latest release.  Here's the github, if you're scared by github. And you know, just, it's very simple, you just want to find this xpi document.  And then you just want to download this dot, uh, xpi file to your downloads or whatever. Think of better, big checks as the infrastructure, the plumbing. Running from. Zotero to your obsidian.  

So wherever you downloaded this file, we got to now get it into Zotero. So we're going to go to tools up here. And ad-ons.  

It's going to bring up something that looks like this. It's going to be emptier for you. Because you don't have other stuff plugged in. But you'll see here. I have it in here. I can disable or remove it if I want to. All you're going to do is take the file. And just click and drag it into here. And you'll pretty much be all good to go. 

When you have better bid checks set up. Say that 10 times fast. You want to come back to obsidian? So just take a second to join me here.  

 And now we're going to connect the bridge from Sotero to obsidian. So the pipes will run, run, run well. So we're going to go to settings like we always do. Come to community plugins, wherever you're at. We can go to browse.  And the one you're looking for, you can just look up. So taro. And it says Zotero integration.  It's already installed for me. You know, the drill, you just hit this button here to download or install and enable it. And then we're going to go to options.  So you're going to want to pay attention to this part. 

This is where you do have to do some setup and some fancy things. If you want to get it the way you want.  First is this'll be unchecked for you. You just want to click yes to this.  Can leave this blank. Make sure this says Zotero.  



And then just identify where you want to import these notes to when you're bringing them from Zotero. 

So you'll see here, I have them saved in. Synth brain in the R and D folder under AI. And research notes. I'll show you how that goes in a second. 

You can leave this on or off, up to you. Just keep this the same. 

One thing you are going to want to enable though, is this enable annotation concatenation this is a really tough. It's a tough plugin to pronounce all the words. Uh, so all this is going to do is let's say you're marking something up in Zotero and you push it to your vault. And a day later you go back, you add some stuff to that article. 

You're working on some notes you were thinking about now when you reimport instead of reimporting and it making two different files, it just merges the file. So it's all together. So. Definitely click that one on pro pro tip. 



Next we want to develop something called a template. how this is going to work is every time you import it from Zotero, you're gonna want some metadata, you know, like the authors, the name of the actual article, maybe the year it was published, whatever that might be. we want to create a template so that when it pulls in, it has all that for you. 

And it's set up the way you like. you can name it, whatever you want. It doesn't have to be template. That's just what I do. The output path. So where is it getting exported to you'll notice I have title here. That's just saying that how I want you to structure the note is just by the title of the article, but you can make that whatever you want.  And then the image output path. 

I like to put the images somewhere separate. So we just created this attachments folder. And then I organize those by site key instead of name it doesn't really matter.  

And then you want to input your template that you've created. I'm going to go over this in a second with you, but once, you know, at this point, you're going to want to stop and maybe go create your templates folder. Uh, or your templates note so that when you import it imports the way you like it.  I'll go over that in just a second.  

You don't have to do any of this. 

All this is image OCR. That's when it can read an image or like a PDF and extract the text from it. If you really want that, you can figure this out. I didn't really try. I didn't really need it. But there's instructions here. You just had to download some things and you know, it's probably a little annoying, but you can figure it out. 

Now we have all this setup, let's go check out what the template looks like, because it's actually a little bit.  I don't know, this might scare you, but I am also just going to provide this. Uh, to you and you can fill around with it. It uses a language called , which I had never heard of before.  I don't know why, or who's naming these languages. Uh, but it's not like anything I've seen. 

I don't really know it. Luckily you can just kind of feed this to Chet GPT. I found some others just as examples.  So, this is how I have it set up is every time it imports, it's going to take the publish year, the list of authors, the URL, where you can find it. The link directly back to Zotero so I can get to it easily. The hashtags, the tags. And published for me is I like to publish my summaries online for everybody. 

And so this is just letting me know, when am I going to schedule that out to be published?  

And this you eventually have to do manually, at least at this 0.1 day, I'll figure out it just pulls it all in, but.  

I just have the purpose of whatever I'm looking at, the methods, the key findings of the discussion, the critiques.  That's simple enough. This is when things get funky. Uh, look at this. What is this?  I don't even know. It's Next is what it is.  I will give this to you, but I'm going to show you what, what, what this looks like in actuality, when you actually pull in. Uh, document. 



Let's pull up my research notes where I have things saved. I'm going to pick out this just because it has lots of images in it.  So when I pulled in this article, you see, you see, it's filled everything out for me. This is the date I'm going to publish it.  I manually had to go and create this summary. I just use chat GPT.  But when I get down here, You'll see, it's pulled the annotations, the images that I've grabbed, the highlights that I have, and you can even go exactly to where in the document. 

This is so you can go and even get more context. If you're like, what was I thinking about here?  

This is what it looks like. It's really nice and clean. And again, this now all gets embedded. As something you can query in your second brain. Which is fabulous. 

 We're almost there. Let's go back to Zotero. And now we're going to import an article in with annotations. So I chose this roleplay with large language models. Just as an example, we can highlight a couple random things just for argument's sake.  And I think we even have an image down here.  That if we want to grab that as well. 

Once you have that, you just come back to Zotero or do our command palette.  

Um, so taro.  Remember I called a template. It's going to be whatever you called it. We're going to click that.  

It's going to say a waiting item, selection for Zotero. So you just got to find this by going back to Zotero or alt tabbing over to it. We'll look up the article.  We've got role-play. We're pressed enter. 

Here we have it the year, the things. The couple annotations and the image that we drew and. Now it's just in your obsidian notes. 



  📍  📍 The last thing I want to leave you with is there is a phone app as well. So similar to like read wise, you can upload the things that you're reading or doing into Zotero from your phone and look at them later. But it's not as easy. If you're not using research article it's, it's definitely built more for that. 

  📍 That's it for Zotero. Again, it's a lot more steps to get set up than ReadWise. It's not as user friendly as ReadWise. But I use this a ton and kind of how I separate things is Zotero is a lot better for actual research articles Whereas Readwise is better for like the books you're reading, the articles you're reading, the YouTube videos you're watching So that's how I keep it separated.

But if you can't afford Readwise, this is a perfectly good option. It does all the things It's just a little bit harder to set up and more manual to get things from here into your vaults, but still awesome   📍 So thanks for listening, Chatters, as always. I appreciate you. I hope this is helpful, and we're almost done with sort of the foundations of the plumbing, so we're almost there.

Thanks for sticking in with me. My call to action to you is just try to set this up, take some annotations, get it into your vault, just try it out.  It's worth it. I love Zotero, and I think this is a good challenge for you. So,  I'll see you next time.