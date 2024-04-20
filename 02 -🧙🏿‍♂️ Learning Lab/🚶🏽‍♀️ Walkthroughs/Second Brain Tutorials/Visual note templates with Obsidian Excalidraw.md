---
excalidraw-plugin: parsed
tags:
  - excalidraw
  - NicoleVanderHoeven
excalidraw-open-md: true
Author:
---
## [[Visual note templates with Obsidian Excalidraw]]

## Walkthrough
How to Create Visual Note Templates with Obsidian Excalidraw

### Introduction
Have you ever wanted to take more visual notes but felt held back by the limitations of purely textual notes? In this blog post, we'll explore a powerful technique that combines the best of both worlds - creating hybrid notes that are both visual and textual using the Obsidian Excalidraw plugin. By following these step-by-step instructions, you'll be able to create stunning visual note templates that enhance your note-taking experience.

### Step 1: Install and Set Up Obsidian Excalidraw
1. Install the Obsidian Excalidraw plugin in your Obsidian vault.
2. Enable the plugin in the settings.
3. Go to the Excalidraw settings and make the following changes:
   - In the "Saving" section, expand "File name" and disable the setting that adds ".excalidraw" to the file name.
   - In the "Embedding Excalidraw into your notes and exporting" section, expand "Auto export settings" and toggle on "Auto export SVG".
4. Set up a templates folder location in both the Obsidian core templates settings and the Excalidraw settings.

### Step 2: Create a New Hybrid Note Template
1. Open the command palette (Ctrl/Cmd + P) and type "Create new drawing".
2. Select "Create new drawing in the current active window".
3. Optionally, set up a hotkey for toggling between Excalidraw and markdown mode for quick switching.
4. Rename the new note to your desired template name.
5. To make the note default to text view, add the property `excalidraw-plugin: parsed
6. Embed the title SVG using the syntax `![[Title.svg]]` to display the visual side of the note on the textual side.
7. Move the note to your templates folder to make it a reusable template.

### Step 3: Create a New Note Using the Hybrid Template
1. Create a new note (Ctrl/Cmd + N).
2. Insert the hybrid note template you created in Step 2.
3. Toggle between the textual and visual sides of the note using the hotkey or command palette.
4. Edit the visual side of the note using Excalidraw's intuitive drawing tools.
5. Save the note (Ctrl/Cmd + S) to update the embedded SVG on the textual side automatically.

### Step 4: Convert Existing Textual Templates to Hybrid Templates
1. Open an existing textual note template.
2. Copy the Excalidraw-related properties and drawing elements from a hybrid template.
3. Paste the copied content into the existing textual template.
4. Save the modified template, and it will now have both textual and visual capabilities.

### Step 5: Convert Existing Notes to Hybrid Notes
1. Open an existing textual note that you want to convert to a hybrid note.
2. Open the command palette and search for "Convert markdown note to Excalidraw drawing".
3. Select the appropriate template (either for new notes or existing notes) to apply the conversion.
4. Optionally, add the embedded SVG on the textual side to display the visual content.
5. Save the note, and it will now have both textual and visual elements.
## Transcript
https://www.youtube.com/watch?v=zmgqMZi6QL8

[00:00](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=0) the concept of making my notes more visual has always appealed to me but one thing's held me back in most cases taking visual notes means not taking textual ones and if I have to choose one 
[00:11](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=11) I'm going to choose to take notes in text text is more easily searchable displayable not to mention sharable so I default to text wherever I can and the few times that I've done something more 
[00:22](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=22) visual I've still wanted to write text to go with it anyway but a few weeks ago my friend jol vitan put forward an interesting proposition what if I could have both in 
[00:37](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=37) this video I'm talking about how to have one note that's both Visual and textual by default using the obsidian excal draw plugin and how I love this so much that I've actually changed all of my note 
[00:50](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=50) templates to support this excal draw is actually a separate web app on its own and it's really good for creating quick and dirty diagrams but obsidian excal draw is a community plug-in created by 
[01:02](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=62) jol Vian who has also created the plug-in excalibrate and it brings in the functionality of excal draw into your obsidian Vault so this is a way to create drawings that are still 
[01:14](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=74) compatible with excal draw but able to be edited with an obsidian I've talked a little bit about it here where I go over how to create a visual map of content in obsidian excal draw so check that out if 
[01:27](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=87) you want more information on that plugin but today I'm talking about a very specific idea that happens to work well with obsidian excal dra and the idea is this what if you thought of your notes 
[01:38](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=98) as a physical sheet of paper on one side you would have all your actual handwritten or typed up notes but what if you could also flip it around and on the back of it or the front of it 
[01:51](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=111) depending on how you view it you could also have like a drawing or a sketch of whatever it is that you're taking a note on it's the idea of having one note that you can switch between the two modes 
[02:04](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=124) within and it's completely different from having two different notes that you somehow have to maybe link together and having one that's entirely Visual and one that's entirely textual which is 
[02:17](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=137) actually what I was doing here's an interview a clip from an interview that I did with jol where he talks about this very concept he calls it the back of the sheet so yeah one of the things that I'm 
[02:28](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=148) taking away as an next the development opportunity we talked about this with uh Nicole on this concept of turning the sheet around so you know you have an excolo drawing and if you uh click on 
[02:43](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=163) the tab you can switch to markdown View mode so that for me is my metaphor is like having a card a sheet of paper and on one hand side you have the drawing and you turn it 
[02:57](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=177) around and you have your notes about the topic but when you turn it around then you have the excal draw content the text elements the embedded files and then the Json there which just doesn't look as 
[03:13](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=193) nice when you uh publish it for example uh to a website so I'm I'm going to look into how I can hide that so when you publish them yeah if they're marked down then really it can just be the same note 
[03:29](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=209) One Note with two different modes kind of like how there's a reading mode and a source mode in in obsidian which now is live preview but there used to be these two modes that you could flip between 
[03:40](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=220) seamlessly it's kind of like that except now and and you know you don't really need to do that now with live preview anyway so maybe the two modes are text and and visual and visual yeah which is 
[03:54](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=234) amazing I mean so so for me there are two additional takeaways so I was chatting to some people at the conference and the idea was the so on the visual you can create really a small 
[04:09](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=249) visual so you you should really think about it as a Post-It note so you have a small Visual and then behind it you can have a large amount of text and links and ideas but if you summarize the note 
[04:27](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=267) on the other side with a small visual it gives you another level of how you can engage with your Concepts because when you start to organize your Concepts you're organizing 
[04:39](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=279) these visual cards and you're creating connections between those cards and yes on the other side you have the detail but it's sort of a visual summary of your card which adds another dimension 
[04:52](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=292) but also helps you remember the content better I recorded that with jol at the PKM Summit recently in UT in the Netherlands and it was like a 30 minute conversation it's too long to put up 
[05:05](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=305) here but if you are on my patreon I am going to put it up there so you can watch the whole thing in its entirety we talked about pcam Summit and trends that we spotted that were brought up within 
[05:17](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=317) you know the the conference itself is a really good way to support me and also support jolt honestly because I'm going to leave a link to his details down below as well so before before we get 
[05:30](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=330) into how to do it I'm going to show you what we're aiming for here's a note that I actually created for my joint talk with Joel during the conference this is supposed to be like a note for a 
[05:41](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=341) tabletop roleplaying game character but this could really have been like a person note or anything like that so it looks just like a normal note it has some things embedded in it but it's 
[05:53](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=353) really mainly text now the interesting thing is this is just one side of it and if you flip to the other side I have a hotkey on this I'll show you how to do that this is actually the same note 
[06:05](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=365) you'll see it's still the Mystic note it's still Mystic MD but now it's almost entirely visual with just some words here the thing is that I don't have to choose which one I'm going to use or 
[06:19](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=379) which one I'm going to do beforehand I can just have them both so I can quickly jump over here to get a more visual like understanding of the theme of this character 
[06:30](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=390) or I can go back here to look at the front matter or like actually look at the description of this character so I'm going to show you how to use this in three different ways first I'm going to 
[06:41](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=401) show you how to create a new hybrid note from scratch by creating a new excal draw note template how to convert an existing note template that you already have that doesn't have anything to do 
[06:51](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=411) with excal draw and then how to convert existing notes without using a template to do this I'm going to start over with a fresh new Vault there's really nothing in it and I'm going to go and install 
[07:04](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=424) excal draw so I'm going to install it enable it and then before we get into how to create the thing there are going to be a few settings that I think you should change first so exit out of that 
[07:18](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=438) go over to Escala draw here first go into saving here and then go down and then expand this file name section and we're going to toss gole this setting off here by default excal draw is going 
[07:33](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=453) to take new notes and save them in the format. excal draw. MD personally I think that goes against the ethos of having one note and it can be Visual and it can be textual it doesn't really 
[07:45](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=465) matter which so I actually disable this so that everything's just a markdown what I'm trying to do here is really try to break my mind out of the Habit that a note a MD or markdown note is always a 
[07:59](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=479) actual one because I want to be able to switch and do both and maybe just do one or the other and not really have a stark difference between the two so I've toggled that one off and then I'm going 
[08:11](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=491) to scroll back up to collapse the saving part and I'm going to expand embedding excal dra into your notes and exporting I'm going to scroll down and then expand Auto export settings and then I'm going 
[08:25](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=505) to toggle autoexport SVG I'll tell you why this is important in a second but for now just toggle it on I am also going to go to the settings for the templates folder here and I'm going to 
[08:38](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=518) put a template folder location and I'm just going to call it templates and whatever I put there I'm also going to put in the excal draw settings so back to the excal draw settings I'm going to 
[08:50](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=530) go to basic this time and then there's excal draw template file or folder I mean you can use this excal draw one but I'm just going to put with the templates folder again no difference now between 
[09:02](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=542) markdown notes and excal draw drawings so I'm going to exit out of that and exit out of this graph view I'm going to hit the command pane command P or control p and then I'm going to type 
[09:16](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=556) create new drawing now there are a few options here I pretty much always just use create new drawing in the current active window so this is the new excal draw drawing and one last thing this is 
[09:28](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=568) a quality of life things strictly not even necessary but I I just really find it useful I'm going to go into hotkeys and then here in toggle between excal draw and markdown mode I'm going to 
[09:41](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=581) choose a new command hotkey or shortcut for this now it was funny because while I was talking to jol we just so happen to have chosen the same one which is command option e but you know you can 
[09:53](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=593) make it whatever you'd like all right so now we're here and I'm going to hit the command pane that's command P or control p and then I'm going to create new drawing now there are four different 
[10:07](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=607) ways to create one I pretty much always just use create new drawing in the current active window so I'm going to do that now if I hit command option e that's actually toggling to the other 
[10:20](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=620) side now okay let's do that without the hotkey if you didn't do the hotkey you can always go to the command Pane and then type toggle and it'll just be here toggle between excal draw and markdown 
[10:32](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=632) mode so right now because we created an excal draw drawing this is in the drawing mode but if we flip it that's like turning it around and now we're looking at the text side of it so let's 
[10:44](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=644) go ahead and rename this new note now by default any new excal draw drawing is going to when you open it up default to the drawing view so you would automatically go to this so if if we go 
[10:58](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=658) to here then it you'll see that it went straight to the drawing so let's like draw something there you could leave it at this if you'd like but personally I like for it to default in text View and 
[11:10](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=670) then have the option to turn it around so if you are like me then what you need to do is go here and add a property and it's going to be excal draw open MD and it's going to have to be Tru so this is 
[11:26](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=686) what that looks like in Source mode just so you see what typed out now what I'd like to do is make this the new template so I'm going to change out a few things that I don't think I really need like 
[11:37](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=697) this warning I know about excal draw view so I'm going to exit out of that now I'm probably going to have something like um title here if you're using templator the community plugin then this 
[11:52](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=712) would be a little bit different but I haven't installed any Community plugins here except for scalar draw so I'm like going vanilla only so I would like the title of the note there and then I'm 
[12:04](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=724) going to do something where I going to embed the title. SVG so remember when I said that in the excal draw settings that you should do 
[12:17](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=737) an auto export to SVG this is so that we can do just this we want to be able to embed what's on the excal draw drawing portion of the note on the textual side you can skip if you don't want to do 
[12:30](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=750) this but I personally have found it useful to be able to see both sides of it so now let's turn this into an actual template now right now this is in the Escala draw folder we said that the 
[12:41](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=761) templates folder is going to be in here template so we're moving that over there and we just want that to be applied whenever we create a new note so now let's create a new note I just hit 
[12:54](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=774) command n now this is still an Untitled note so I'm going to insert to the template and that's the new note all right so we have a new note here we've inserted the template and now this is 
[13:08](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=788) automatically an excal draw drawing as well what that means is you can see here it says Untitled do SVG could not be found that's because we haven't done anything in the drawing yet but from 
[13:20](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=800) here on all we have to do is toggle to that other side of the sheet and I hit command option e and here we are because we put like this box here I realized at the template maybe we didn't really need 
[13:33](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=813) that but okay well now we have a nice box here this is an Untitled note and then I'm going to hit contrl s just to force excal draw to save it not really necessary but you know if you want to 
[13:48](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=828) switch quickly back and forth I would do it and then I'm going to switch back here and now instead of saying you know so and so SVG could not be found now it's actually embedding the s VG here 
[14:00](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=840) and it's going to be automatically updated too so if I go here and I say I don't actually want this box I want this diamond and I'll hit the the save one 
[14:15](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=855) again command contrl s flip back and this was automatically updated because we turned on auto export is true so that's how to create a brand new hybrid textual visual note so because I didn't 
[14:28](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=868) have the Community plug-in templator installed I did have to insert the template manually but with the templator plug-in you can actually set it up so that you know certain templates are 
[14:39](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=879) applied when you put it in certain folders or maybe you just want to have it automatically applied to every note all of those things are options that you can add on to this but I just wanted to 
[14:49](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=889) keep it to core plugins and excal draw for now so that's how you would do it if you wanted to create a brand new hybrid note template that is textual and visual but what if you already had some textual 
[15:03](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=903) notes and you want to make them visual ones as well well let's pretend that we've got something here and I'll say textual and let's say you had the title here and texy text over 
[15:24](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=924) there and so when we create a new note it's Untitled one insert template let's say oops if you if you insert text rle that's normally what you would find now how do we turn this 
[15:39](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=939) textual one into a visual template well it turns out it's actually not that bad you see this new note here we just have to copy these so I'm going to switch over to the source mode and I'm going to 
[15:54](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=954) copy this and put the properties in there and and then I'm also going to copy the rest of this so the text elements and the drawing part so move over there to textual one and copy that 
[16:09](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=969) over now let's do that again applying the text rule template and insert template and I'll say textual although now it looks very similar and 
[16:22](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=982) I'm going to hit command option e and there you go this is our excal draw drawing too so first pitched this idea of a hybrid visual textual note to me a couple months ago when we were preparing 
[16:34](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=994) for our joint talk at the pcam summit conference last month and I loved the idea and I immediately wanted to convert all my notes while I didn't end up doing that I did decide to go back and convert 
[16:47](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1007) all my templates jol kind of convinced me that I shouldn't just Mass convert all of my textual notes and I'm mostly glad that he was able to succeed in that so let's have a look at some of my 
[16:58](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1018) personal templates just to show to you what I did manage to do so here is my daily note it looks very much the same as the last time I showed it but it does have the excal draw plug-in stuff so it 
[17:10](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1030) has the open MD set to true and it has this as well I did put the text elements within the comment just because I didn't want it to show up and here's one for a default meeting I used to just have it 
[17:26](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1046) as text but look it's now also an excal draw drawing and it also has the SVG that's going to be embedded here as well and the last part is what if you want a hybrid note but you already have a 
[17:40](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1060) textual note and you don't really want to change templates you just want an existing note to be turned into a hybrid note well here's how you do that these are my highlights for a book that's 
[17:51](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1071) called nonviolent communication now it is not an excal drawn note because I've just now remembered that I should probably also update my readwise template so that it does this so this is 
[18:03](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1083) a good opportunity to change that so I go command p and then you can search for convert markdown node to excal draw drawing and you can see I've also hot keyed this because I do it quite a bit 
[18:15](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1095) now and now it's asking me to select which template I use now I tend to have two different ones this template is just for new notes which is kind of like what I showed you but this existing note is a 
[18:27](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1107) little bit different that's mainly because it no longer has the SVG here and that's because it doesn't work too well I found with these templator strings so anyway if it's a new note I 
[18:40](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1120) apply the one template and if it's an existing note I apply this one but it effectively turns it into the same thing now it doesn't do the SVG but I can always add that in afterwards so again 
[18:54](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1134) that would be nonviolent communication and then I'll do SVG and then when I flip to the excal draw notes Here I can put in a note here and NVC is a way of communicating with empathy and then save 
[19:15](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1155) that and then flip back and there you go so I could have my highlights along with my handwritten or typed out notes there's so many other options to excal draw that it's really possible to go 
[19:28](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1168) through all of of them for example in my personal Vault you might have noticed that my excal draw stuff here is faded out and that's because it is an excal draw setting so if you go to excal draw 
[19:41](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1181) and go to miscellaneous features you can toggle on this new feature called Fade Out excal dra markup you just have to be sure that you are putting the comments here before the text elements line and 
[19:56](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1196) this is actually something that came about as a result of me saying to jol hey I want to be able to publish these notes and you know I don't want people to see all of these text elements and 
[20:06](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1206) drawings so it looks a little bit like that and it just doesn't make any sense so I asked him for a way to make it look a little bit nicer when I publish it having a hybrid textual visual note is 
[20:17](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1217) the best of both worlds now every time I create a new note it is both textual and visual and flipping back and forth between them is really easy and that's opened up opportunities for me I've 
[20:28](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1228) realized that I'm much more likely to just draw a quick diagram or include some sort of spatial element on notes or just paste in a screenshot because that's all just a hotkey away and it's 
[20:40](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1240) really encouraged me to create links and visualize my notes in a way that I couldn't when I felt that I had to choose between one or the other if you'd like to learn more about excal draw then 
[20:51](https://www.youtube.com/watch?v=zmgqMZi6QL8&t=1251) check out this video where I go over the basics of excal draw and how to use it to create a visual map of content in obsidian thanks for watching k 

![[Untitled 1.svg]]


# Text Elements
Install and Set Up Obsidian Excalidraw ^cOASSWhm

Create a New Hybrid Note Template ^ZyYgoDiM

Open command palette and create new drawing ^TKjKgayc

Rename note and add properties ^ExtY0gjH

Embed title SVG ^oadN2j1w

Move note to templates folder ^dtEwIe2o

Create a New Note Using the Hybrid Template ^5uJS0HK1

Create a new note ^9dTZqiVQ

Insert hybrid note template ^VBK3v9w9

Toggle between textual and visual sides ^EgKAJ0Mo

Edit visual side using Excalidraw ^hhhSC6To

Save note to update embedded SVG ^wfc5Ipnr

Convert Existing Textual Templates to Hybrid Templates ^2Nee1RQn

Open existing textual note template ^SHyl2Eyb

Copy Excalidraw-related properties and drawing elements ^tOKduXWM

Paste copied content into textual template ^xDeRf3JF

Save modified template ^XIInrf06

Convert Existing Notes to Hybrid Notes ^t0CL7wVX

Open existing textual note ^n2tZmiX7

Open command palette and search for conversion command ^xZNFBjFn

Select appropriate template for conversion ^ovGutjm5

Optionally add embedded SVG on textual side ^3uvYjI7i

Save note with textual and visual elements ^Gk2p78zi

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.4",
	"elements": [
		{
			"id": "V_hCzsVYuLw823nYFyk3s",
			"type": "embeddable",
			"x": -796.2500305175781,
			"y": -1813.4988160566847,
			"width": 1409.9996337890623,
			"height": 857.760314941406,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 1361017780,
			"version": 292,
			"versionNonce": 241709196,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1713653079563,
			"link": "https://youtu.be/zmgqMZi6QL8?si=4AnWVn0NeJgeJACI",
			"locked": false,
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1263926796,
			"isDeleted": false,
			"id": "WKvZLCnEPC6f2kXC63Dg0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -310.9538116455078,
			"y": -893.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 444.81768798828125,
			"height": 47.5,
			"seed": 602504332,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "cOASSWhm"
				},
				{
					"id": "ZE2Oj4-i6UNp79fqlQWdo",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 9,
			"versionNonce": 999930036,
			"isDeleted": false,
			"id": "uG-icoL1NvATZbTnHZiuK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -321.5983428955078,
			"y": -796.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 466.10675048828125,
			"height": 466.10675048828125,
			"seed": 1428294412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "ZyYgoDiM"
				},
				{
					"id": "ZE2Oj4-i6UNp79fqlQWdo",
					"type": "arrow"
				},
				{
					"id": "s8gNwll-r8AQrDxvTSG6g",
					"type": "arrow"
				},
				{
					"id": "BMOk6x8M5TE5hgGUCrAHM",
					"type": "arrow"
				},
				{
					"id": "oA0cqaJ6BSvKatONyojOt",
					"type": "arrow"
				},
				{
					"id": "g_uQxqvdQSpEUoY8RSbuw",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 780295308,
			"isDeleted": false,
			"id": "5jmB8woYpGHxJJakhSA3c",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1324.2610626220703,
			"y": 39.303375244140625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 555.5728759765625,
			"height": 47.5,
			"seed": 491047308,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "TKjKgayc"
				},
				{
					"id": "s8gNwll-r8AQrDxvTSG6g",
					"type": "arrow"
				},
				{
					"id": "iU-x3Jf5Ka9qF5VJhZK72",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 919110196,
			"isDeleted": false,
			"id": "pSrmmUhC7MWAHt3RuG-vv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1236.9563903808594,
			"y": 456.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 380.9635314941406,
			"height": 47.5,
			"seed": 2139863052,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "ExtY0gjH"
				},
				{
					"id": "iU-x3Jf5Ka9qF5VJhZK72",
					"type": "arrow"
				},
				{
					"id": "T7hs9kYunMy8bs7M9bqHz",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1503587084,
			"isDeleted": false,
			"id": "3HwJzzfT7CW1fhsRiClqJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1145.1139450073242,
			"y": 553.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 197.2786407470703,
			"height": 47.5,
			"seed": 133224076,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "oadN2j1w"
				},
				{
					"id": "T7hs9kYunMy8bs7M9bqHz",
					"type": "arrow"
				},
				{
					"id": "sYnW5JFtAl40Vhg2nBMOE",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1147280308,
			"isDeleted": false,
			"id": "60Gxkm39ko7KsGpUvVt0_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1224.3847961425781,
			"y": 651.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 355.8203430175781,
			"height": 47.5,
			"seed": 858662156,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "dtEwIe2o"
				},
				{
					"id": "sYnW5JFtAl40Vhg2nBMOE",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 6,
			"versionNonce": 1059432844,
			"isDeleted": false,
			"id": "z6qWKoR2N1BTQXcmX75AV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -718.6881866455078,
			"y": -225.97006225585938,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 578.046875,
			"height": 578.046875,
			"seed": 1455268748,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "5uJS0HK1"
				},
				{
					"id": "BMOk6x8M5TE5hgGUCrAHM",
					"type": "arrow"
				},
				{
					"id": "cZS3UQtKHcqroIAkCTnI6",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1854702900,
			"isDeleted": false,
			"id": "xWu6XpWQTnttRdCbmsPDj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -540.784538269043,
			"y": 456.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 222.2395782470703,
			"height": 47.5,
			"seed": 148460044,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "9dTZqiVQ"
				},
				{
					"id": "cZS3UQtKHcqroIAkCTnI6",
					"type": "arrow"
				},
				{
					"id": "cWYBy8Yk8NK1TA3LDQ-g8",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1917884428,
			"isDeleted": false,
			"id": "P0eI8fcvXnmmHgtPkwPVO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -592.2624053955078,
			"y": 553.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 325.1953125,
			"height": 47.5,
			"seed": 142291084,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "VBK3v9w9"
				},
				{
					"id": "cWYBy8Yk8NK1TA3LDQ-g8",
					"type": "arrow"
				},
				{
					"id": "DLwC6wxRGgfXPjYwve9KN",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 179158708,
			"isDeleted": false,
			"id": "Wup5JnPW2tpB9u2LxzDig",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -659.6972961425781,
			"y": 651.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 460.0650939941406,
			"height": 47.5,
			"seed": 626867980,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "EgKAJ0Mo"
				},
				{
					"id": "DLwC6wxRGgfXPjYwve9KN",
					"type": "arrow"
				},
				{
					"id": "i_6qOqV5heF9RMVFj2HHK",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 253343372,
			"isDeleted": false,
			"id": "qyg6m_uWuz5P0fHwn2u3p",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -617.8613586425781,
			"y": 748.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 376.3932189941406,
			"height": 47.5,
			"seed": 670662028,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "hhhSC6To"
				},
				{
					"id": "i_6qOqV5heF9RMVFj2HHK",
					"type": "arrow"
				},
				{
					"id": "6mn_raqvJQmT2isQf1j6l",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1366018100,
			"isDeleted": false,
			"id": "Zg-z0MQuDkAWZwk_RsMx_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -638.0827331542969,
			"y": 846.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 416.8359680175781,
			"height": 47.5,
			"seed": 965340172,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "wfc5Ipnr"
				},
				{
					"id": "6mn_raqvJQmT2isQf1j6l",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 36,
			"versionNonce": 574293260,
			"isDeleted": false,
			"id": "9SiryQm_zZtOUogRWmhMk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -90.64131164550781,
			"y": -280.1627502441406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 686.4322509765625,
			"height": 686.4322509765625,
			"seed": 1275628172,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "2Nee1RQn"
				},
				{
					"id": "oA0cqaJ6BSvKatONyojOt",
					"type": "arrow"
				},
				{
					"id": "nhSbwNlHR8y1OcczI2TRB",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1991025076,
			"isDeleted": false,
			"id": "ydY-i8od-56VVTMf0KrKp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 41.116485595703125,
			"y": 456.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 422.9166564941406,
			"height": 47.5,
			"seed": 36657420,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "SHyl2Eyb"
				},
				{
					"id": "nhSbwNlHR8y1OcczI2TRB",
					"type": "arrow"
				},
				{
					"id": "to7SiVODd1ESHgEa_DfvV",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 288261004,
			"isDeleted": false,
			"id": "tuCrFjmjAV2iRSbht25Mk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -80.63481140136719,
			"y": 553.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 666.4192504882812,
			"height": 47.5,
			"seed": 393762700,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "tOKduXWM"
				},
				{
					"id": "to7SiVODd1ESHgEa_DfvV",
					"type": "arrow"
				},
				{
					"id": "U7maaFvW8tPlFpp5VYtko",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1100368692,
			"isDeleted": false,
			"id": "qlfo59K-gU1RODRMuGruS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 2.6920013427734375,
			"y": 651.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 499.7655944824219,
			"height": 47.5,
			"seed": 1209894412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "xDeRf3JF"
				},
				{
					"id": "U7maaFvW8tPlFpp5VYtko",
					"type": "arrow"
				},
				{
					"id": "9gfnj2fE0XBt-_M7zcIBG",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 36581900,
			"isDeleted": false,
			"id": "auurRrzse0hT8_Oiy6JlT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 111.29878234863281,
			"y": 748.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 282.55206298828125,
			"height": 47.5,
			"seed": 957932684,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "XIInrf06"
				},
				{
					"id": "9gfnj2fE0XBt-_M7zcIBG",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 6,
			"versionNonce": 613336244,
			"isDeleted": false,
			"id": "mg8R7amjWeYbnfv_eD80n",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 731.5722351074219,
			"y": -185.3971405029297,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 496.9010314941406,
			"height": 496.9010314941406,
			"seed": 1613001484,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "t0CL7wVX"
				},
				{
					"id": "g_uQxqvdQSpEUoY8RSbuw",
					"type": "arrow"
				},
				{
					"id": "fzAlP8qDwrrfGyRx_5ga0",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1144262796,
			"isDeleted": false,
			"id": "f_5bX2RoZEfQL3l2qpZFE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 823.4732818603516,
			"y": 456.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 313.09893798828125,
			"height": 47.5,
			"seed": 1807364492,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "n2tZmiX7"
				},
				{
					"id": "fzAlP8qDwrrfGyRx_5ga0",
					"type": "arrow"
				},
				{
					"id": "vH3o4zqRFcGhgNJgLtd4g",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1429999156,
			"isDeleted": false,
			"id": "Yqm4w1zUAQpSb4ZXAJRnn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 635.7844390869141,
			"y": 553.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 688.4766235351562,
			"height": 47.5,
			"seed": 722739212,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "xZNFBjFn"
				},
				{
					"id": "vH3o4zqRFcGhgNJgLtd4g",
					"type": "arrow"
				},
				{
					"id": "KOye-ncQYptq4oqG-ljrE",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 922361612,
			"isDeleted": false,
			"id": "nsfToSfeE3L8KdFa1H3lQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 730.1725006103516,
			"y": 651.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 499.70050048828125,
			"height": 47.5,
			"seed": 1982611084,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "ovGutjm5"
				},
				{
					"id": "KOye-ncQYptq4oqG-ljrE",
					"type": "arrow"
				},
				{
					"id": "Wj9Jt_Rl77BhDBQqOEjN0",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 1686382516,
			"isDeleted": false,
			"id": "1Y7QaKn__LRbQo8oqKWg9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 715.3678131103516,
			"y": 748.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 529.3098754882812,
			"height": 47.5,
			"seed": 364678412,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "3uvYjI7i"
				},
				{
					"id": "Wj9Jt_Rl77BhDBQqOEjN0",
					"type": "arrow"
				},
				{
					"id": "6s9x_nx68PosU8NCz8_qn",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 855268748,
			"isDeleted": false,
			"id": "o4V4wdDygczokHbG6iq3R",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 730.8170318603516,
			"y": 846.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 498.41143798828125,
			"height": 47.5,
			"seed": 725552012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "Gk2p78zi"
				},
				{
					"id": "6s9x_nx68PosU8NCz8_qn",
					"type": "arrow"
				}
			],
			"updated": 1713653057820,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1210909836,
			"isDeleted": false,
			"id": "ZE2Oj4-i6UNp79fqlQWdo",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -88.58935220553495,
			"y": -845.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.40578559671202186,
			"height": 45.34446879124869,
			"seed": 418232844,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062160,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "WKvZLCnEPC6f2kXC63Dg0",
				"gap": 1,
				"focus": 0.0009350843307337174
			},
			"endBinding": {
				"elementId": "uG-icoL1NvATZbTnHZiuK",
				"gap": 3.6733525738359845,
				"focus": 0.01064004466277568
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0.40578559671202186,
					45.34446879124869
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 339520780,
			"isDeleted": false,
			"id": "s8gNwll-r8AQrDxvTSG6g",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -272.75539023261877,
			"y": -512.9589592630191,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 773.7196723894515,
			"height": 546.9624585305971,
			"seed": 1774360716,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062161,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uG-icoL1NvATZbTnHZiuK",
				"gap": 1,
				"focus": -0.0033645271890083974
			},
			"endBinding": {
				"elementId": "5jmB8woYpGHxJJakhSA3c",
				"gap": 5.299875976562589,
				"focus": -0.0000015767086556265552
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-773.7196723894515,
					207.79645853059714
				],
				[
					-773.7196723894515,
					546.9624585305971
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1726465804,
			"isDeleted": false,
			"id": "iU-x3Jf5Ka9qF5VJhZK72",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1046.4750626220703,
			"y": 87.80337524414062,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 363.16612402343753,
			"seed": 964142860,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062162,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "5jmB8woYpGHxJJakhSA3c",
				"gap": 1,
				"focus": 0.0000015767086558311852
			},
			"endBinding": {
				"elementId": "pSrmmUhC7MWAHt3RuG-vv",
				"gap": 5.300001464843717,
				"focus": -0.0000022993711735653215
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					363.16612402343753
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 104194316,
			"isDeleted": false,
			"id": "T7hs9kYunMy8bs7M9bqHz",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1046.4750626220703,
			"y": 504.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 478602636,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062163,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "pSrmmUhC7MWAHt3RuG-vv",
				"gap": 1,
				"focus": 0.0000022993711735653215
			},
			"endBinding": {
				"elementId": "3HwJzzfT7CW1fhsRiClqJ",
				"gap": 5.300001464843717,
				"focus": -0.000004440301084699563
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 145160972,
			"isDeleted": false,
			"id": "sYnW5JFtAl40Vhg2nBMOE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1046.4750626220703,
			"y": 602.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 136991756,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062163,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "3HwJzzfT7CW1fhsRiClqJ",
				"gap": 1,
				"focus": 0.000004440301084699562
			},
			"endBinding": {
				"elementId": "60Gxkm39ko7KsGpUvVt0_",
				"gap": 5.300001464843717,
				"focus": -0.000002461850705523031
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 8,
			"versionNonce": 1923856780,
			"isDeleted": false,
			"id": "BMOk6x8M5TE5hgGUCrAHM",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -221.5335042348047,
			"y": -461.737073265205,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 208.1315583872656,
			"height": 232.07354223026766,
			"seed": 979104396,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062164,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uG-icoL1NvATZbTnHZiuK",
				"gap": 1,
				"focus": -0.00615122826955804
			},
			"endBinding": {
				"elementId": "z6qWKoR2N1BTQXcmX75AV",
				"gap": 3.7237126980759854,
				"focus": 0.007996415519313951
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-208.1315583872656,
					156.57457253278312
				],
				[
					-207.65761569307767,
					232.07354223026766
				]
			]
		},
		{
			"type": "arrow",
			"version": 8,
			"versionNonce": 73123468,
			"isDeleted": false,
			"id": "cZS3UQtKHcqroIAkCTnI6",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -429.1673999578426,
			"y": 352.9443631954279,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4976626642277324,
			"height": 98.02513607215025,
			"seed": 567656716,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062164,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "z6qWKoR2N1BTQXcmX75AV",
				"gap": 1,
				"focus": -0.008093669156468704
			},
			"endBinding": {
				"elementId": "xWu6XpWQTnttRdCbmsPDj",
				"gap": 5.300001464843717,
				"focus": -0.0000028210687310417847
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-0.4976626642277324,
					78.3251360721502
				],
				[
					-0.4976626642277324,
					98.02513607215025
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1072570508,
			"isDeleted": false,
			"id": "cWYBy8Yk8NK1TA3LDQ-g8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -429.6650626220703,
			"y": 504.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1175568268,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062165,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "xWu6XpWQTnttRdCbmsPDj",
				"gap": 1,
				"focus": 0.0000028210687310417843
			},
			"endBinding": {
				"elementId": "P0eI8fcvXnmmHgtPkwPVO",
				"gap": 5.300001464843717,
				"focus": -0.0000019279279279055536
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 2055436940,
			"isDeleted": false,
			"id": "DLwC6wxRGgfXPjYwve9KN",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -429.6650626220703,
			"y": 602.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 793374220,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062166,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "P0eI8fcvXnmmHgtPkwPVO",
				"gap": 1,
				"focus": 0.0000019279279279055536
			},
			"endBinding": {
				"elementId": "Wup5JnPW2tpB9u2LxzDig",
				"gap": 5.300001464843717,
				"focus": -0.0000013627487352924646
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 446420108,
			"isDeleted": false,
			"id": "i_6qOqV5heF9RMVFj2HHK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -429.6650626220703,
			"y": 699.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1316506764,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062167,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Wup5JnPW2tpB9u2LxzDig",
				"gap": 1,
				"focus": 0.0000013627487352924646
			},
			"endBinding": {
				"elementId": "qyg6m_uWuz5P0fHwn2u3p",
				"gap": 5.300001464843717,
				"focus": -0.0000016656865569155852
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1186410124,
			"isDeleted": false,
			"id": "6mn_raqvJQmT2isQf1j6l",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -429.6650626220703,
			"y": 797.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1700190988,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062170,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "qyg6m_uWuz5P0fHwn2u3p",
				"gap": 1,
				"focus": 0.0000016656865569155852
			},
			"endBinding": {
				"elementId": "Zg-z0MQuDkAWZwk_RsMx_",
				"gap": 5.300001464843717,
				"focus": -0.0000015040763587999323
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 38,
			"versionNonce": 2003401996,
			"isDeleted": false,
			"id": "oA0cqaJ6BSvKatONyojOt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 44.8723164353984,
			"y": -462.16582076853314,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 208.12115173924818,
			"height": 178.35367514843,
			"seed": 1851758988,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062170,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uG-icoL1NvATZbTnHZiuK",
				"gap": 1,
				"focus": 0.0008564384474809468
			},
			"endBinding": {
				"elementId": "9SiryQm_zZtOUogRWmhMk",
				"gap": 3.673330649382507,
				"focus": 0.021031225270813848
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					207.7026209425313,
					157.00332003611123
				],
				[
					208.12115173924818,
					178.35367514843
				]
			]
		},
		{
			"type": "arrow",
			"version": 38,
			"versionNonce": 1209969164,
			"isDeleted": false,
			"id": "nhSbwNlHR8y1OcczI2TRB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 253.0673807236808,
			"y": 407.13977532577337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4924433457510986,
			"height": 43.82972394180479,
			"seed": 80513036,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062171,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "9SiryQm_zZtOUogRWmhMk",
				"gap": 1,
				"focus": -0.021895061895631607
			},
			"endBinding": {
				"elementId": "ydY-i8od-56VVTMf0KrKp",
				"gap": 5.300001464843717,
				"focus": 5.842056791368984e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-0.4924433457510986,
					24.12972394180474
				],
				[
					-0.4924433457510986,
					43.82972394180479
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1600341004,
			"isDeleted": false,
			"id": "to7SiVODd1ESHgEa_DfvV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 252.5749373779297,
			"y": 504.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1285006988,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062171,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ydY-i8od-56VVTMf0KrKp",
				"gap": 1,
				"focus": -5.842056791368985e-7
			},
			"endBinding": {
				"elementId": "tuCrFjmjAV2iRSbht25Mk",
				"gap": 5.300001464843717,
				"focus": 3.707430605349996e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1787485708,
			"isDeleted": false,
			"id": "U7maaFvW8tPlFpp5VYtko",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 252.5749373779297,
			"y": 602.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1518007564,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062172,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "tuCrFjmjAV2iRSbht25Mk",
				"gap": 1,
				"focus": -3.707430605349995e-7
			},
			"endBinding": {
				"elementId": "qlfo59K-gU1RODRMuGruS",
				"gap": 5.300001464843717,
				"focus": 5.554361759095232e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1612019724,
			"isDeleted": false,
			"id": "9gfnj2fE0XBt-_M7zcIBG",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 252.5749373779297,
			"y": 699.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 468743052,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062173,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "qlfo59K-gU1RODRMuGruS",
				"gap": 1,
				"focus": -5.554361759095231e-7
			},
			"endBinding": {
				"elementId": "auurRrzse0hT8_Oiy6JlT",
				"gap": 5.300001464843717,
				"focus": 8.744240261863283e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 8,
			"versionNonce": 826447500,
			"isDeleted": false,
			"id": "g_uQxqvdQSpEUoY8RSbuw",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 100.00856972972292,
			"y": -517.3020740628576,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 880.4969379514769,
			"height": 328.2037886346784,
			"seed": 1060250124,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062173,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uG-icoL1NvATZbTnHZiuK",
				"gap": 1,
				"focus": 0.0019764851116485676
			},
			"endBinding": {
				"elementId": "mg8R7amjWeYbnfv_eD80n",
				"gap": 3.7324962038069316,
				"focus": 0.006162795667204694
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					880.0143676482069,
					212.13957333043567
				],
				[
					880.4969379514769,
					328.2037886346784
				]
			]
		},
		{
			"type": "arrow",
			"version": 8,
			"versionNonce": 647979916,
			"isDeleted": false,
			"id": "fzAlP8qDwrrfGyRx_5ga0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 980.5213979752293,
			"y": 312.37069607251846,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.49846059729952685,
			"height": 138.5988031950597,
			"seed": 456786060,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062173,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mg8R7amjWeYbnfv_eD80n",
				"gap": 1,
				"focus": -0.006213963856892644
			},
			"endBinding": {
				"elementId": "f_5bX2RoZEfQL3l2qpZFE",
				"gap": 5.300001464843717,
				"focus": 0.0000011914664342456672
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-0.49846059729952685,
					118.89880319505966
				],
				[
					-0.49846059729952685,
					138.5988031950597
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 419118476,
			"isDeleted": false,
			"id": "vH3o4zqRFcGhgNJgLtd4g",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 980.0229373779298,
			"y": 504.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 398593804,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062174,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "f_5bX2RoZEfQL3l2qpZFE",
				"gap": 1,
				"focus": -0.0000011914664342456672
			},
			"endBinding": {
				"elementId": "Yqm4w1zUAQpSb4ZXAJRnn",
				"gap": 5.300001464843717,
				"focus": 5.418439239018745e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 429528972,
			"isDeleted": false,
			"id": "KOye-ncQYptq4oqG-ljrE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 980.0229373779298,
			"y": 602.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 356797836,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062174,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Yqm4w1zUAQpSb4ZXAJRnn",
				"gap": 1,
				"focus": -5.418439239018745e-7
			},
			"endBinding": {
				"elementId": "nsfToSfeE3L8KdFa1H3lQ",
				"gap": 5.300001464843717,
				"focus": 7.465409277086591e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 1862005132,
			"isDeleted": false,
			"id": "Wj9Jt_Rl77BhDBQqOEjN0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 980.0229373779298,
			"y": 699.7695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1425718284,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062175,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "nsfToSfeE3L8KdFa1H3lQ",
				"gap": 1,
				"focus": -7.465409277086591e-7
			},
			"endBinding": {
				"elementId": "1Y7QaKn__LRbQo8oqKWg9",
				"gap": 5.300001464843717,
				"focus": 7.047797377044439e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "arrow",
			"version": 10,
			"versionNonce": 530631564,
			"isDeleted": false,
			"id": "6s9x_nx68PosU8NCz8_qn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 980.0229373779298,
			"y": 797.2695007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69999853515628,
			"seed": 1625250444,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713653062176,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "1Y7QaKn__LRbQo8oqKWg9",
				"gap": 1,
				"focus": -7.047797377044439e-7
			},
			"endBinding": {
				"elementId": "o4V4wdDygczokHbG6iq3R",
				"gap": 5.300001464843717,
				"focus": 7.484717379615471e-7
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					0,
					43.69999853515628
				]
			]
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 39369140,
			"isDeleted": false,
			"id": "cOASSWhm",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -283.7748260498047,
			"y": -882.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 390.459716796875,
			"height": 25,
			"seed": 1940662540,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Install and Set Up Obsidian Excalidraw",
			"rawText": "Install and Set Up Obsidian Excalidraw",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "WKvZLCnEPC6f2kXC63Dg0",
			"originalText": "Install and Set Up Obsidian Excalidraw",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 2012212108,
			"isDeleted": false,
			"id": "ZyYgoDiM",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -189.70157623291016,
			"y": -588.2428131103516,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 202.2598419189453,
			"height": 50,
			"seed": 1624975244,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a New Hybrid\nNote Template",
			"rawText": "Create a New Hybrid Note Template",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "uG-icoL1NvATZbTnHZiuK",
			"originalText": "Create a New Hybrid Note Template",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 805266228,
			"isDeleted": false,
			"id": "TKjKgayc",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1275.9844512939453,
			"y": 50.553375244140625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 459.0196533203125,
			"height": 25,
			"seed": 2091275788,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Open command palette and create new drawing",
			"rawText": "Open command palette and create new drawing",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "5jmB8woYpGHxJJakhSA3c",
			"originalText": "Open command palette and create new drawing",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1552062988,
			"isDeleted": false,
			"id": "ExtY0gjH",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1206.4844970703125,
			"y": 467.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 320.0197448730469,
			"height": 25,
			"seed": 67613836,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Rename note and add properties",
			"rawText": "Rename note and add properties",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "pSrmmUhC7MWAHt3RuG-vv",
			"originalText": "Rename note and add properties",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 370465972,
			"isDeleted": false,
			"id": "oadN2j1w",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1126.5145645141602,
			"y": 565.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 160.0798797607422,
			"height": 25,
			"seed": 79250188,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Embed title SVG",
			"rawText": "Embed title SVG",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "3HwJzzfT7CW1fhsRiClqJ",
			"originalText": "Embed title SVG",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 666597516,
			"isDeleted": false,
			"id": "dtEwIe2o",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1199.614486694336,
			"y": 662.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 306.27972412109375,
			"height": 25,
			"seed": 1161101708,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Move note to templates folder",
			"rawText": "Move note to templates folder",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "60Gxkm39ko7KsGpUvVt0_",
			"originalText": "Move note to templates folder",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1581196852,
			"isDeleted": false,
			"id": "5uJS0HK1",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -555.8863754272461,
			"y": 38.041656494140625,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 252.41981506347656,
			"height": 50,
			"seed": 750055436,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a New Note Using\nthe Hybrid Template",
			"rawText": "Create a New Note Using the Hybrid Template",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "z6qWKoR2N1BTQXcmX75AV",
			"originalText": "Create a New Note Using the Hybrid Template",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 89425676,
			"isDeleted": false,
			"id": "9dTZqiVQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -522.8946838378906,
			"y": 467.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 186.45986938476562,
			"height": 25,
			"seed": 724766348,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a new note",
			"rawText": "Create a new note",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "xWu6XpWQTnttRdCbmsPDj",
			"originalText": "Create a new note",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 224673716,
			"isDeleted": false,
			"id": "VBK3v9w9",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -566.6546173095703,
			"y": 565.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 273.979736328125,
			"height": 25,
			"seed": 560553228,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Insert hybrid note template",
			"rawText": "Insert hybrid note template",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "P0eI8fcvXnmmHgtPkwPVO",
			"originalText": "Insert hybrid note template",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 432522636,
			"isDeleted": false,
			"id": "EgKAJ0Mo",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -630.7045745849609,
			"y": 662.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 402.07965087890625,
			"height": 25,
			"seed": 1221712780,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Toggle between textual and visual sides",
			"rawText": "Toggle between textual and visual sides",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Wup5JnPW2tpB9u2LxzDig",
			"originalText": "Toggle between textual and visual sides",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 464136500,
			"isDeleted": false,
			"id": "hhhSC6To",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -591.1446075439453,
			"y": 760.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 322.959716796875,
			"height": 25,
			"seed": 463899148,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Edit visual side using Excalidraw",
			"rawText": "Edit visual side using Excalidraw",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "qyg6m_uWuz5P0fHwn2u3p",
			"originalText": "Edit visual side using Excalidraw",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1783575564,
			"isDeleted": false,
			"id": "wfc5Ipnr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -608.7545928955078,
			"y": 857.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 358.1796875,
			"height": 25,
			"seed": 1021405324,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Save note to update embedded SVG",
			"rawText": "Save note to update embedded SVG",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Zg-z0MQuDkAWZwk_RsMx_",
			"originalText": "Save note to update embedded SVG",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 35,
			"versionNonce": 209117876,
			"isDeleted": false,
			"id": "2Nee1RQn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 97.57688903808594,
			"y": 37.9453125,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 309.77972412109375,
			"height": 50,
			"seed": 1614575372,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Convert Existing Textual\nTemplates to Hybrid Templates",
			"rawText": "Convert Existing Textual Templates to Hybrid Templates",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "9SiryQm_zZtOUogRWmhMk",
			"originalText": "Convert Existing Textual Templates to Hybrid Templates",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1155846796,
			"isDeleted": false,
			"id": "SHyl2Eyb",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 72.51496887207031,
			"y": 467.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 360.11968994140625,
			"height": 25,
			"seed": 842118540,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Open existing textual note template",
			"rawText": "Open existing textual note template",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ydY-i8od-56VVTMf0KrKp",
			"originalText": "Open existing textual note template",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 108031028,
			"isDeleted": false,
			"id": "tOKduXWM",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -26.614944458007812,
			"y": 565.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 558.3795166015625,
			"height": 25,
			"seed": 1073423372,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Copy Excalidraw-related properties and drawing elements",
			"rawText": "Copy Excalidraw-related properties and drawing elements",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tuCrFjmjAV2iRSbht25Mk",
			"originalText": "Copy Excalidraw-related properties and drawing elements",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 675455244,
			"isDeleted": false,
			"id": "xDeRf3JF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 34.014984130859375,
			"y": 662.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 437.11962890625,
			"height": 25,
			"seed": 1603453580,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Paste copied content into textual template",
			"rawText": "Paste copied content into textual template",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "qlfo59K-gU1RODRMuGruS",
			"originalText": "Paste copied content into textual template",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1803339188,
			"isDeleted": false,
			"id": "XIInrf06",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 138.36492156982422,
			"y": 760.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 228.41978454589844,
			"height": 25,
			"seed": 397578508,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Save modified template",
			"rawText": "Save modified template",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "auurRrzse0hT8_Oiy6JlT",
			"originalText": "Save modified template",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 736272268,
			"isDeleted": false,
			"id": "t0CL7wVX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 866.4675979614258,
			"y": 37.82811737060547,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 226.6597900390625,
			"height": 50,
			"seed": 131370892,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Convert Existing Notes\nto Hybrid Notes",
			"rawText": "Convert Existing Notes to Hybrid Notes",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "mg8R7amjWeYbnfv_eD80n",
			"originalText": "Convert Existing Notes to Hybrid Notes",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1891757876,
			"isDeleted": false,
			"id": "n2tZmiX7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 847.7628631591797,
			"y": 467.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 264.519775390625,
			"height": 25,
			"seed": 1345502732,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Open existing textual note",
			"rawText": "Open existing textual note",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "f_5bX2RoZEfQL3l2qpZFE",
			"originalText": "Open existing textual note",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1744752140,
			"isDeleted": false,
			"id": "xZNFBjFn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 694.1029815673828,
			"y": 565.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 571.8395385742188,
			"height": 25,
			"seed": 2043092108,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Open command palette and search for conversion command",
			"rawText": "Open command palette and search for conversion command",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Yqm4w1zUAQpSb4ZXAJRnn",
			"originalText": "Open command palette and search for conversion command",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 916842676,
			"isDeleted": false,
			"id": "ovGutjm5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 768.5629577636719,
			"y": 662.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 422.9195861816406,
			"height": 25,
			"seed": 1582017292,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Select appropriate template for conversion",
			"rawText": "Select appropriate template for conversion",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "nsfToSfeE3L8KdFa1H3lQ",
			"originalText": "Select appropriate template for conversion",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1569795212,
			"isDeleted": false,
			"id": "3uvYjI7i",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 754.7229461669922,
			"y": 760.0195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 450.599609375,
			"height": 25,
			"seed": 272263564,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Optionally add embedded SVG on textual side",
			"rawText": "Optionally add embedded SVG on textual side",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "1Y7QaKn__LRbQo8oqKWg9",
			"originalText": "Optionally add embedded SVG on textual side",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 5,
			"versionNonce": 1624158772,
			"isDeleted": false,
			"id": "Gk2p78zi",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 763.0229339599609,
			"y": 857.5195007324219,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 433.9996337890625,
			"height": 25,
			"seed": 1120753676,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713653057821,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Save note with textual and visual elements",
			"rawText": "Save note with textual and visual elements",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "o4V4wdDygczokHbG6iq3R",
			"originalText": "Save note with textual and visual elements",
			"lineHeight": 1.25
		},
		{
			"id": "b0jgjfcPTUvYmydcSPtBd",
			"type": "embeddable",
			"x": -289.5833435058594,
			"y": -395.46875762939453,
			"width": 699.9999389648438,
			"height": 393.7499656677246,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"seed": 930156468,
			"version": 57,
			"versionNonce": 1985990540,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1713653057820,
			"link": "https://www.youtube.com/watch?v=5j9fAvJCaig",
			"locked": false,
			"scale": [
				1,
				1
			]
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 3723.141668146308,
		"scrollY": 3054.4893876580786,
		"zoom": {
			"value": 0.25000000000000006
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%