vpz-znbj-fhh (2024-03-22 10:57 GMT-4) - Transcript
Attendees
James Griffing, Joseph Rosenbaum, Joseph Rosenbaum's Presentation
Transcript
This editable transcript was computer generated and might contain errors. People can also change the text after it was created.
James Griffing: I believe where I see it.
Joseph Rosenbaum: okay, so let me share my screen here. I'll show you. Two things that are going on.
Joseph Rosenbaum: Okay, the sliders so when I go to modify assistant. You'll see it has 81928192. So let's just put this up to whatever. I do It seems to save it here.
Joseph Rosenbaum: the number is 518 whatever but then when I go back it comes back to 8192 for both of them.
James Griffing: I go to that assistance note.
James Griffing: As scroll down, okay.
Joseph Rosenbaum: It's working.
James Griffing: My might be a visual thing to where it's not showing the right number in the setting. But if it's here,…
Joseph Rosenbaum: Mm- Perfect.
James Griffing: it's saved, right?
Joseph Rosenbaum: And I could just change it in here and it would work right?
James Griffing: Yeah, absolutely. That's why I'm like I don't really care too much at that Parts a little broken.
Joseph Rosenbaum: Yeah, I just want to make sure yeah, this is good to know.
James Griffing: Yeah.
Joseph Rosenbaum: I just want to make sure that It was actually updating.
James Griffing: Yeah, the main choose to Source Whatever sort Cruise right there.
Joseph Rosenbaum: source of
Joseph Rosenbaum: okay, and then this is one that I have in My Vault Okay, so, I'm talking to the professor, whatever and I switch over you'll see I have send message to save here. And it's just not quite listening. It is doing.
James Griffing: Okay, so whenever it says grams if you click that part. maybe it's not changing.
Joseph Rosenbaum: Whenever it says what?
James Griffing: I think it's not changing the system instructions. That's my guess but if you click grams. I like tools this assistant it has and right below it one down now.
Joseph Rosenbaum: Right here.
James Griffing: Yep that we can see what it's actually sending. Yeah, so I need to get it towards updating the system prompt because it still says active Professor standard apps at the top.
Joseph Rosenbaum: Gotcha, and we wanted to be doing.
James Griffing: It would just have the other system prompt to save one.
Joseph Rosenbaum: Yeah.
James Griffing: The very first message is the one that matters.
Joseph Rosenbaum: okay, I don't think this is something when you fix now because they're not going to be talking to multiple agents in a single chat, but good to know.
James Griffing: That's an easy fix. So I didn't do much testing with it. I just made sure that the bottom part changed. I didn't look at the system prompt to be honest. So
Joseph Rosenbaum: Yeah, yeah. worries. It's good to find out and I got to say so Kerry the blinking Bluer away didn't care about anything else. She's like, this is awesome. Yeah.
James Griffing: that's great. I like that then I don't think little things like that really add to it.
Joseph Rosenbaum: They dear it gives it us some characters some pizzazz. so yeah, and then the only other thing is what I said again, it's fine. We have a fix for it, but I don't even know if I'll be able to find it in the console log, but essentially it was like going over its limit. I might have happened in this.
Joseph Rosenbaum: this is where it started working. Of course. I deleted the ones where it wasn't working. But it was weird. It was like I'd ask a question and then it would act as if I'm saying nothing I had sent a blank thing to it. It was just saying, how can I help you today or something like that and so of answering the question?
James Griffing: yeah, ideally if there's too much context for your setting it should have some sort of notification to you that you need a shorter message or something, but my guess is either. The token value is undefined somewhere. So if an assistant isn't updated I all are all of your assistance updated right now. Do they all have a back value
Joseph Rosenbaum: They should yep.
James Griffing: Okay, I mean that could potentially be it because they're not backwards compatible without updating the settings the assistance.
00:05:00
Joseph Rosenbaum: Mm- Yeah, and once I did up up it was fun because of what I was seeing would be like I had the 8,000 or whatever set and it would say you have 10,000 tokens going into this. That's when it would mess up and then when I updated it was fine.
James Griffing: Okay, okay. yeah, I'm trying to think of a good way to do the notes because if we have 8K message or self? And we only have 7K token window. what do I do with a note? I can't really just Truncate it because what if I truncate the part that is the thing that matters,…
Joseph Rosenbaum: you needed
James Griffing: so in my mind just don't send it in that case, I don't know what logic I should use for that.
Joseph Rosenbaum: Yeah, I don't think it would be logic. I think it would be. A button of some kind like you said it might like warn you'd be like, hey, just so This is going to go over your token count that you have set your up your token count or something like that.
James Griffing: what if they're already at the maps though?
Joseph Rosenbaum: mmm
James Griffing: they're in that is part of the when I say logic. I just mean anything to do. It's a code, Yeah.
Joseph Rosenbaum: Yeah, yeah. Okay. I think it should just in that case. I think the way to go is it's just a warning. It's like you this has gone over the content context limit or whatever.
James Griffing: Yeah, I had some sort of notification thing in there. The next thing I'd like to do is actually have the little buttons. I was talking about the function and then the notes itself because that should be able to give us more of a recap of what it did. so
Joseph Rosenbaum: Awesome work. I had a little bit of a heart attack this morning, but we figured it out. And I think we're going to be good to go. I think expectations are set well to because it's been a couple weeks since we worked with them. So Carrie was nice enough to tee this up as a refresher essentially of assistance and going through the functionality and then just having a practicing a little bit and then we're really gonna get into using it more starting next week probably.
James Griffing: Okay, great. Sounds good to me. So. Her impressions are decent with it so far.
Joseph Rosenbaum: yeah, she was having issues with I think smart connections was creating some problems mostly it was embedding and slowing everything down for her and she was blaming it on a consistent. So I had her open up the console locks. I think we figured that out and I told her to make sure that everyone. Opens up their vault as early as possible so that I can do the embeddings for them. So hopefully we don't have to send them the embeddings physically digitally I guess so, I think we'll be good. We'll see though. we will problem solve if anything happens.
James Griffing: All right, at least it's in a more usable State than it was.
Joseph Rosenbaum: Yeah, I had a great conversation with the professor this morning. And all that it was pulling the right notes is finally the right things even so this is really cool. So I'm testing out. I created all these mini template agents right for character profile. I want you to Output it the same way every time so I just added that note to the folder and I gave the agent access to that folder and I just said, write me a character profile for this character and it followed the template perfectly so
James Griffing: Hell yeah, I love hearing that.
Joseph Rosenbaum: Yeah, I was like, Exactly what I want you to do.
James Griffing: That's fantastic. And once I get clogged in there, it would be better. Yeah that I plan to be the next update besides these little bug fixes.
Joseph Rosenbaum: Yes, yes.
Joseph Rosenbaum: Yeah. cool
James Griffing: But okay cool.
James Griffing: Cool All I'm gonna get caffeinated try to I don't know not mix my words up.
Joseph Rosenbaum: Sounds good. I'll see you in a little bit.
James Griffing: All right. Bye.
Meeting ended after 00:09:34 👋