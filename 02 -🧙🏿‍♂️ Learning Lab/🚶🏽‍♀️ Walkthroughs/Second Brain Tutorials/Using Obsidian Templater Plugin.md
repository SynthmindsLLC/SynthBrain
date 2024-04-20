---
description: Shows you how to use the templater plugin
date: <%tp.date.now("YYYY-MM-DD")%>
type: Walkthrough
excalidraw-plugin: parsed
tags:
  - excalidraw
excalidraw-open-md: true
---
# [[<%TP.FILE.TITLE%>]]

## Walkthrough
How to Automate Your Notes with the Templater Obsidian Plugin

### Introduction
In this blog post, we'll explore how to use the Templater plugin in Obsidian to automate your note-taking process. Templater is a powerful community plugin that allows you to define structures and formats that can be applied to your notes, saving you time and ensuring consistency. We'll cover three main use cases: single-line templates, applying entire templates based on conditions, and using user scripts for advanced automation.

### Use Case 1: Single-Line Templates
1. Create a new note in Obsidian.
2. To use a single-line template, type `<%` followed by the template code and end with `%>`.
3. Common single-line templates include:
   - `tp.file.title`: Inserts the title of the note.
   - `tp.date.now("YYYYMMDD")`: Inserts the current date in the specified format.
   - `tp.frontmatter.type`: Retrieves the value of the "type" parameter from the front matter.
4. To apply the template, use the command palette (Ctrl/Cmd + P) and select "Templater: Replace templates in the active file" or set up a hotkey for quick access.

### Use Case 2: Applying Entire Templates Based on Conditions
1. Create a template folder in your Obsidian vault.
2. Create template files for specific note types (e.g., meeting notes, person notes) within the template folder.
3. In the template files, use single-line templates to populate metadata, headings, and other dynamic content.
4. Configure Templater settings:
   - Specify the templates folder location.
   - Enable "Trigger Templater on new file creation".
   - Set up folder-specific default templates.
5. When creating a new note in a configured folder, the corresponding template will be automatically applied.

### Use Case 3: Using User Scripts for Advanced Automation
1. Install required plugins: Templater, Buttons, Quick Add, Callouts, Fantasy Calendar, and Dataview.
2. Set up user scripts in the Templater settings by specifying the folder for your JavaScript files.
3. Create custom JavaScript functions to handle complex automation tasks, such as incrementing session numbers or updating dataview queries.
4. Use the `tp.user` syntax in your templates to call these custom functions.
5. Create a master index page (e.g., games index) with buttons to add new entries, which will automatically apply the appropriate templates and update dataview queries.

### Conclusion
Templater is a powerful plugin that can greatly enhance your note-taking workflow in Obsidian. By using single-line templates, applying entire templates based on conditions, and leveraging user scripts for advanced automation, you can save time and maintain consistency across your notes. Whether you're taking meeting notes, maintaining a database of people, or even managing RPG campaign information, Templater can help streamline your process and make note-taking more efficient.
## Transcript
[00:00](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=0) the obsidian gems of the year is a list of the best of the best from the obsidian community rather than its core developers and in 2021 the plugin that one second place in the plugins category 
[00:11](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=11) is called templator by silent void templater has changed the way that i take notes and that's by capitalizing on something that we wouldn't typically associate with note-taking automation 
[00:24](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=24) in this video i'm going to talk about what templater is and how i use it to take meeting notes maintain a database of people that i know and even play tabletop role-playing games like dnd 
[00:37](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=37) templater is a community plugin that allows you to define a structure or a format that you can then apply to your other note so you're not doing the same thing each time 
[00:46](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=46) don't get confused though with templates and templater templates is a core plugin that ships with obsidian that you don't have to download but you do have to enable it if you use it and template er 
[00:59](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=59) is a community plugin that you do have to download and enable in this video i'm going to talk about templater in particular but in general the difference between the two is one of complexity 
[01:11](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=71) templates is more like a copy paste so you define the structure and then you paste it kind of into a note and the only things that are dynamic about that are going to be like the date or the 
[01:23](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=83) time or the title so very limited amount of things that you can change on the fly other than that it's mostly a direct copy and paste template error though is way different because you can 
[01:36](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=96) programmatically change almost anything so you could have template or put different things in your notes depending on certain conditions like what day of the week it is or what folder the note 
[01:47](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=107) is in this will make a little bit more sense when we get to the specific use cases so let's get right into that i see three main use cases for using templater and you can use any or all of them 
[01:58](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=118) depending on what you're trying to do the first is using single line templates the second is applying entire templates according to certain conditions and the third one is using your own user scripts 
[02:10](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=130) first let's talk about using single line templates i'm going to create a new note here i'm hitting command o just to go to the quick searcher and i'm going to call it test note 
[02:23](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=143) this is an entirely new note so i'm going to have a heading called test note and every template using templater starts and ends with the same format it is the left arrow and then percentage 
[02:35](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=155) and then it ends with percentage then the right arrow and in between them is where you put the instructions for what to replace this entire line with one of the most common things that i use this 
[02:46](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=166) for is tp that means templater file and then the title this is kind of equivalent to the templates syntax templates the core plugin uses the two brackets opening and closing and then 
[03:00](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=180) titles so this might be simpler but templater has more of those which is why it's a little bit more complex when i apply the template using templater this entire line should then be replaced with 
[03:13](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=193) this title so let's see how this actually gets replaced hit command p or control p if you're on windows to open up the command palette and then start typing replace templates and select 
[03:25](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=205) templater replace templates in the active file you'll notice that i've also added a hotkey to it so that i can do this on the fly i'm on a mac so i'm using control option r but you can 
[03:38](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=218) change it to whatever you'd like in this case i'm just going to click on it to run it and you can see that this where the template used to be 
[03:46](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=226) now you see the title which is test note if we go back a step and have the full template here i'm going to add to that this time i'm going to put in the date as well 
[03:57](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=237) date now and then i'm going to specify the format for it which i want to be year year year month month day day all in numbers i'm going to end the template 
[04:08](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=248) but another single line template that i use in my templates is the one that retrieves the value for a parameter i've set in the front matter so let's say we have the front matter here and let's say 
[04:21](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=261) that i've got type and this is a meeting as the single line template i'm going to put in tp front matter and you'll notice that as i'm typing there are these options here this is also a 
[04:34](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=274) cool way to explore these are all the default variables the templater has already set up so you just have to select them and use them rather than creating your own 
[04:45](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=285) in this case i want front matter and then i type in the name of the parameter which in this case is type then i'm going to end this one and this time i'm going to hit the hotkey 
[04:56](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=296) rather than going through the command palette but i'm still just replacing the templates in the active file now i've got as expected the title the date and also 
[05:07](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=307) the value of the type here so that's how you would use templater to replace those strings with metadata from the file in question but typically you would build from this and put it in a template so 
[05:19](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=319) let me show you that instead of this i'm going to create a meeting template let me delete this file and let me show you that i've got a templates folder here and i have a 
[05:31](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=331) meeting note within that templates folder in this meeting note i have everything that i want to appear in a meeting once i've decided that i'm taking notes on a 
[05:41](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=341) meeting i want this metadata in there so you can see here that i'm using that tp date now format and also the title now you'll notice that the title is within these brackets and i could have 
[05:56](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=356) it without that it is the value inside that's going to be replaced with the title of the meeting but having them within the brackets turns it into a link the reason that i'd like to do that and 
[06:07](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=367) this is optional is that i found that if i just type out the heading then if i change the name of that file then the name of the file and the heading title no longer match and i 
[06:19](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=379) don't like that so i've just defined it as a link too then i have a bunch of sections here that i expect myself to fill out and i would type out the actual meeting notes here and aside from the 
[06:30](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=390) meeting template i also have created a person template so i create a note on people that i speak to especially those that i have meetings with and i want this template applied whenever i create 
[06:42](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=402) a new person note within the person node we've got some metadata still and i'm using the same trick here to create a link as the heading so this is a little bit different from the one that i showed 
[06:53](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=413) you it is still a single line but instead of just pulling out a value for in this case the title i'm also saying that i want this entire note to be moved into the people folder so that if i make 
[07:06](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=426) a note for a person and it's not in the people folder yet and then i apply the template for a person not only will it apply that template but it'll also automatically move that note to the 
[07:18](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=438) people folder and then under meetings here i do have a dataview query that has a template inside it this is just going to bring up all of the meetings that i have with this person automatically so 
[07:29](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=449) now i've got a template but i haven't yet specified when exactly this template should be applied so for that i'm going to go into the settings for templater and i'm going to specify that templates 
[07:42](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=462) folder so that obsidian knows that all of my templates are going to be stored there i'm also going to click enable on trigger templater on new file creation what that is doing is giving 
[07:54](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=474) templater the permission to replace any templates in new files that are created in this section folder templates you can specify default templates that are applied to every note that are created 
[08:06](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=486) in different folders since i already have a meeting template i'm going to choose the folder meetings because i put all my meetings there and i'm going to choose the meeting template in the 
[08:18](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=498) templates folder and then i'm going to add the same thing but for the person template so now all of the people that i have notes on are in the people folder and the name of the template that i want 
[08:30](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=510) applied is person so i'm going to add both of those i'll exit out of that to start with i would hit command o that's the quick switcher again and let's say i want a new meeting meeting today 
[08:43](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=523) i'm going to hit enter and that creates that and as you can see the meeting template was automatically applied it already took the date it has the file name as a link in the heading but i 
[08:55](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=535) don't have any attendees yet let's say i have a meeting with jonathan archer since this is a person i'm going to say people and then a slash that means i want to put it in the people folder and 
[09:06](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=546) then i'm going to type out his name jonathan archer i don't have a page for this yet but i'm going to create it right now we should see a new note for jonathan archer that follows the person 
[09:17](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=557) template so i'm holding down command here and i'm going to click on it so that it opens up in a new pane and that looks like it's been created this is these are the ones that were 
[09:28](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=568) specifically for people the dataview query has also been updated so that now it says jonathan archer instead of the template that was there so i've already shown two use cases one is how to use 
[09:40](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=580) those single line templates and then the second one was using those single line templates as building blocks to create a bigger template that is automatically applied when you create a note in a 
[09:52](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=592) specific folder now the third use case is a little bit more complex but i wanted to include it as an example of how you can do very complex things and distill them down to a few button clicks 
[10:06](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=606) just by using templates and other plugins this use case hinges on the fact that templater allows you to create user functions which means that if you can write javascript or copy code from 
[10:18](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=618) somebody else then templater can actually run those what that means is that you can make your templates a lot more dynamic now this is going to be my ttrpg workflow that i'm demonstrating 
[10:30](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=630) here but it is using quite a few scripts that i've written and also quite a few plugins specifically i'm using templater but also buttons quick add callouts fantasy calendar and dataview so 
[10:44](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=644) definitely not something that's for everybody but i just think this is a cool way to show you of how deep you can get into templater so my ttrpg workflow starts with the games index which is a 
[10:57](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=657) list of all of the campaigns that i'm currently running or playing in to create a new game i'd click on add new world here and let's say that this is a demo world and you'll see that there's 
[11:09](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=669) another page that's been created this is using a specific world template and that the dataview query on the games index has been updated to include that demo world now i could put in the system here 
[11:22](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=682) for example and have that be updated in the dataview query let me exit out of this games index and within the world i can have a list of sessions except i don't have any 
[11:33](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=693) sessions for this world right now so let me add one right now so i'm going to click that and now it's added a session according to you've probably guessed a session 
[11:43](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=703) template now this session has pulled in a whole bunch of parameters it's pulled in the fact that it's a session it's taken the campaign and world from the world page it's counted the number of 
[11:56](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=716) sessions that i currently have and it increments them automatically so this is the first so it's named it like that as well so it starts with zero zero one and then it an underscore and then today's 
[12:07](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=727) date i do use the plug-in obsidian fantasy calendar for many of my games i haven't set it up for this one but if i did i would name it the same as the world and it would automatically 
[12:20](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=740) populate what today's date is or today in game scrolling down to the session here i'm also using call-outs to have a little session summary page now this is saying no games were found because this 
[12:33](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=753) is the recap section and there were no previous games but we'll look at what that looks like in a second so i would put the log in here lots of stuff happened 
[12:44](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=764) and then at the end of the session i would typically put in a longer summary in this part and there's also a one-liner here in case i just want a quick overview of the main things that 
[12:56](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=776) happen in this section so let me put the adventure begins just to see that that summary has been updated in the dataview query in the world as well now i'm going to exit out of this go back to the world 
[13:08](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=788) page and let's say i have another session let me click add session again and now it's automatically incremented to the second session for this game and by the way all of these things are being 
[13:21](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=801) created in the ttrpgs folder within that folder for the world i do this because sometimes i play in the same system or the same published worlds so i want to keep every campaign and every group 
[13:34](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=814) separate within that demo world i have the sessions here and the world page let me exit out of this world page and look at the second session more closely it's very similar to the first one except 
[13:46](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=826) that now it's automatically pulling in the session summary of the first session within the recap now what if in this session we meet somebody we met in a tavern and met the bartender let's say 
[13:59](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=839) that that is an npc again i'm going to hit command and then click on it to open that note up in a different pane now because this is a note that is neither a session nor a world note templater has 
[14:10](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=850) automatically applied my ttrpg front matter template then i would go in and say that this one is an npc and maybe i met this person in the tavern called the crossed pikes if you're curious about 
[14:25](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=865) how i set this up i'm basically using a few templates this is the ttrpg front matter one for adding in npcs or locations this is my world template i have two session templates depending on 
[14:38](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=878) whether i'm a gm or a player the gm one has some more sections in it that have secrets that characters might discover loot and so on but it works on pretty much the same principles with the same 
[14:51](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=891) templates here that get pre-populated you might have noticed that some of these templates have tp.user those are the user scripts that i've created so in templater when you go 
[15:02](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=902) through the settings here and scroll all the way down you can have a section where you specify what folder you're putting your scripts in now these are all javascripts so it looks like it's 
[15:14](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=914) detecting seven of mine create world session get campaign lists now these are very specific to me but let me show you what that looks like this is what one of those scripts looks like in my ide which 
[15:26](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=926) is vs code the vault that i've been using is a test vault so that i can show you how to set things up but let me show you what it looks like in my actual main vault 
[15:38](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=938) this is my games index page and these are the campaigns that i've played in or run i still have the same add new world button here and each one of these follows the same format so for example 
[15:52](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=952) in this game which i am running i have the sessions here that i can add and they are automatically incremented in the way that i showed you as you can see i play a lot of rpgs i think i'm up to 
[16:05](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=965) five weekly ones right now which is a little bit too much honestly but that's why i needed something like this i know that this can be very daunting but the reason that i did it 
[16:17](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=977) was because i really need something that i can just click on and everything is done for me it did take an initial amount of time to set it up but afterwards it's a lot easier from there 
[16:30](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=990) is this approach for everybody definitely not this is a niche use case and a niche way to use obsidian but i just thought i'd show it off since i've already made it i've been hesitant to 
[16:42](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1002) share my templates because there's no one right way to do note-taking and i feel like my templates are so specific for my use cases however i get enough comments asking about the code that i 
[16:54](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1014) use and the templates that i use that maybe there are more of you out there with similar use cases so if you do just want to download everything that i've shown you here then consider joining my 
[17:06](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1026) patreon and you'll get a copy of the vault that i showed with all the plugins and templates and settings and even shortcuts that i've shown for the goals and reviews for meetings and people and 
[17:18](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1038) also for the ttrpg workflows that i've demonstrated in this video automating my notes with templater helps me do two things one it saves me time by allowing me to populate my notes with predefined 
[17:32](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1052) fields and two it helps me keep my notes more consistent with each other by providing me a repeatable structure that i can work from i said earlier that templater won second 
[17:43](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1063) place any guesses as to which plugin won the obsidian gems of the year in 2021 that would be dataview it is also a very powerful plugin but also a little daunting and overwhelming so check that 
[17:58](https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s&t=1078) video out if you want to know more about it thank you for watching hasta la proxima 


![[Untitled.svg]]


# Text Elements
Install Templater Plugin ^iwhXRFbh

Use Case 1: Single-Line Templates ^yQMhwCQB

Create a new note ^rwtOK3Xr

Type template code between <% and %> ^VNVFHrCQ

Apply template using command palette or hotkey ^52o9h3tt

Use Case 2: Applying Entire Templates Based on Conditions ^KZneczPp

Create a template folder ^uu96vVWj

Create template files for specific note types ^mEKQZZ9c

Use single-line templates in template files ^oS6CV2Qc

Configure Templater settings ^IBKMUvEK

Create a new note in a configured folder ^SXUtPYlH

Corresponding template automatically applied ^JKlDhJVZ

Use Case 3: Using User Scripts for Advanced Automation ^RgVPCPUn

Install required plugins ^NRr0wKxE

Set up user scripts folder in Templater settings ^fl32ximQ

Create custom JavaScript functions ^8MXLTP7s

Use tp.user syntax in templates ^UI8dFfNu

Create a master index page with buttons ^TTZeKe7I

Buttons automatically apply templates and update dataview queries ^SHr0VWYf

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.1.4",
	"elements": [
		{
			"type": "rectangle",
			"version": 6,
			"versionNonce": 65013772,
			"isDeleted": false,
			"id": "CSYD1owmRCWASZdrIv2os",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -254.28386688232422,
			"y": -701.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 279.9479064941406,
			"height": 47.5,
			"seed": 748557620,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "iwhXRFbh"
				},
				{
					"id": "dst4m2yC0C0UVPSxc5LY5",
					"type": "arrow"
				},
				{
					"id": "xgogBdeXSFlBMfgCaQePv",
					"type": "arrow"
				},
				{
					"id": "U8yvj0gIlwT_cNiWonJjO",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 5,
			"versionNonce": 490415756,
			"isDeleted": false,
			"id": "lmT7bIB3wtq6JN8-CwmQX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -967.7930068969727,
			"y": -465.1497344970703,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 442.7994689941406,
			"height": 442.7994689941406,
			"seed": 806178484,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "yQMhwCQB"
				},
				{
					"id": "dst4m2yC0C0UVPSxc5LY5",
					"type": "arrow"
				},
				{
					"id": "-1dHAAplBLBRnAA5ao69c",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1252947212,
			"isDeleted": false,
			"id": "DNuObS0x6JCAhVlE6CAkI",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -857.5130615234375,
			"y": 166.93362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 222.2395782470703,
			"height": 47.5,
			"seed": 1146705972,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "rwtOK3Xr"
				},
				{
					"id": "-1dHAAplBLBRnAA5ao69c",
					"type": "arrow"
				},
				{
					"id": "jDc2OmI7rf0xqsLfDRFEV",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 968094604,
			"isDeleted": false,
			"id": "JEa4wiAgldsyUFF0FgWX_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -977.0508193969727,
			"y": 264.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 461.3150939941406,
			"height": 47.5,
			"seed": 1432891828,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "VNVFHrCQ"
				},
				{
					"id": "jDc2OmI7rf0xqsLfDRFEV",
					"type": "arrow"
				},
				{
					"id": "skCfUhcY3shG5-b-1xbMy",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 4,
			"versionNonce": 1485152780,
			"isDeleted": false,
			"id": "giMdi6mQ0UIWAuOjwpZmS",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1031.4648666381836,
			"y": 361.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 570.1431884765625,
			"height": 47.5,
			"seed": 1650449204,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "52o9h3tt"
				},
				{
					"id": "skCfUhcY3shG5-b-1xbMy",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 5,
			"versionNonce": 1042120844,
			"isDeleted": false,
			"id": "FhgLGhuNO3yUUC82zPMPs",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -474.99353790283203,
			"y": -604.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 721.3672485351562,
			"height": 721.3672485351562,
			"seed": 363222196,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "KZneczPp"
				},
				{
					"id": "xgogBdeXSFlBMfgCaQePv",
					"type": "arrow"
				},
				{
					"id": "B-ox_UKEweChL54OTEzWC",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 305499916,
			"isDeleted": false,
			"id": "g8jucb2-j_M152lYy0vJ8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -261.9661636352539,
			"y": 166.93362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 295.3125,
			"height": 47.5,
			"seed": 1558289972,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "uu96vVWj"
				},
				{
					"id": "B-ox_UKEweChL54OTEzWC",
					"type": "arrow"
				},
				{
					"id": "U0E6oAnMAXWuJqgG9MGfG",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1967639948,
			"isDeleted": false,
			"id": "aIqVZeR94QNanEKc4UYPM",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -371.2239761352539,
			"y": 264.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 513.828125,
			"height": 47.5,
			"seed": 16234420,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "mEKQZZ9c"
				},
				{
					"id": "U0E6oAnMAXWuJqgG9MGfG",
					"type": "arrow"
				},
				{
					"id": "2dlrzhRNRf7oqdQ_9AOMV",
					"type": "arrow"
				}
			],
			"updated": 1713655070438,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1754151948,
			"isDeleted": false,
			"id": "lSVYtrulGl2Jl5lvuU_et",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -359.8307418823242,
			"y": 361.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 491.0416564941406,
			"height": 47.5,
			"seed": 1041146164,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "oS6CV2Qc"
				},
				{
					"id": "2dlrzhRNRf7oqdQ_9AOMV",
					"type": "arrow"
				},
				{
					"id": "HvLPytzxFWXFyiNuLGt6Y",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 906156684,
			"isDeleted": false,
			"id": "J8hMfOjnV2mm__ednVzlr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -283.35938262939453,
			"y": 459.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 338.09893798828125,
			"height": 47.5,
			"seed": 1535924916,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "IBKMUvEK"
				},
				{
					"id": "HvLPytzxFWXFyiNuLGt6Y",
					"type": "arrow"
				},
				{
					"id": "bf7CS-WYtfl_goiKmplKx",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1482664204,
			"isDeleted": false,
			"id": "Z7JuHy8rjfdoCiiqvKkeq",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -350.7682418823242,
			"y": 556.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 472.9166564941406,
			"height": 47.5,
			"seed": 1142350900,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "SXUtPYlH"
				},
				{
					"id": "bf7CS-WYtfl_goiKmplKx",
					"type": "arrow"
				},
				{
					"id": "ZiwmBdKx3PPDtO1-o_pxv",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 4,
			"versionNonce": 1662953356,
			"isDeleted": false,
			"id": "QpPXPzURSg6-czDydI4vz",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -382.5130386352539,
			"y": 654.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 536.40625,
			"height": 47.5,
			"seed": 496254388,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "JKlDhJVZ"
				},
				{
					"id": "ZiwmBdKx3PPDtO1-o_pxv",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "diamond",
			"version": 5,
			"versionNonce": 1786369548,
			"isDeleted": false,
			"id": "cLWDn-4GnEa9IOJHxEmo_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 296.3737106323242,
			"y": -587.9622192382812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 688.4244384765625,
			"height": 688.4244384765625,
			"seed": 1630168884,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "RgVPCPUn"
				},
				{
					"id": "U8yvj0gIlwT_cNiWonJjO",
					"type": "arrow"
				},
				{
					"id": "zA533Xz5vnNf0LaM7pq1U",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1802187916,
			"isDeleted": false,
			"id": "937TR7c8TC6PlSFF9susd",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 504.40103912353516,
			"y": 166.93362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 272.3697814941406,
			"height": 47.5,
			"seed": 1933533364,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "NRr0wKxE"
				},
				{
					"id": "zA533Xz5vnNf0LaM7pq1U",
					"type": "arrow"
				},
				{
					"id": "kZF-zKSMnJpBcYKnWhFPJ",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 866960140,
			"isDeleted": false,
			"id": "Yypyga_KSyQ-cAPSfmsKC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 370.83983612060547,
			"y": 264.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 539.4921875,
			"height": 47.5,
			"seed": 997796404,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "fl32ximQ"
				},
				{
					"id": "kZF-zKSMnJpBcYKnWhFPJ",
					"type": "arrow"
				},
				{
					"id": "vk7Pu_Z-IxnmMM3MXFL7c",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1236828556,
			"isDeleted": false,
			"id": "oYapbunsb8_QPDMUjZZxF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 434.83072662353516,
			"y": 361.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 411.5104064941406,
			"height": 47.5,
			"seed": 1019069364,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "8MXLTP7s"
				},
				{
					"id": "vk7Pu_Z-IxnmMM3MXFL7c",
					"type": "arrow"
				},
				{
					"id": "isL-VvqpZhPpWXw0VZ5HX",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 1422422028,
			"isDeleted": false,
			"id": "vXMvXQedgAbWoCerYX9Jk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 455.5273208618164,
			"y": 459.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 370.1172180175781,
			"height": 47.5,
			"seed": 758328628,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "UI8dFfNu"
				},
				{
					"id": "isL-VvqpZhPpWXw0VZ5HX",
					"type": "arrow"
				},
				{
					"id": "BOSDtkmez5AfRUssV4Dyz",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 5,
			"versionNonce": 81170060,
			"isDeleted": false,
			"id": "ST9ZND1pYoy3FnidQ35YU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 403.77603912353516,
			"y": 556.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 473.6197814941406,
			"height": 47.5,
			"seed": 239036084,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "TTZeKe7I"
				},
				{
					"id": "BOSDtkmez5AfRUssV4Dyz",
					"type": "arrow"
				},
				{
					"id": "HK5dPpYOuJ4X1hU5iJ5cl",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 4,
			"versionNonce": 2057100556,
			"isDeleted": false,
			"id": "NNsmCaWpo_cALe4vIrUtk",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 249.70699310302734,
			"y": 654.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 781.7578735351562,
			"height": 47.5,
			"seed": 1149792308,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"type": "text",
					"id": "SHr0VWYf"
				},
				{
					"id": "HK5dPpYOuJ4X1hU5iJ5cl",
					"type": "arrow"
				}
			],
			"updated": 1713655070439,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 7,
			"versionNonce": 504998068,
			"isDeleted": false,
			"id": "dst4m2yC0C0UVPSxc5LY5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -255.28386688232428,
			"y": -667.3104990590042,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 491.1089997558593,
			"height": 198.45617155828143,
			"seed": 804538804,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072364,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "CSYD1owmRCWASZdrIv2os",
				"gap": 1,
				"focus": -0.000013961734737159945
			},
			"endBinding": {
				"elementId": "lmT7bIB3wtq6JN8-CwmQX",
				"gap": 3.7365612046311583,
				"focus": 0.005288504460905157
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
					-491.1089997558593,
					37.876874791426125
				],
				[
					-490.62167576326345,
					198.45617155828143
				]
			]
		},
		{
			"type": "arrow",
			"version": 7,
			"versionNonce": 463866804,
			"isDeleted": false,
			"id": "-1dHAAplBLBRnAA5ao69c",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -745.8939863934728,
			"y": -21.483828267012598,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.49888024471079007,
			"height": 183.11720399943448,
			"seed": 1135145780,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072364,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "lmT7bIB3wtq6JN8-CwmQX",
				"gap": 1,
				"focus": -0.005319881959656702
			},
			"endBinding": {
				"elementId": "DNuObS0x6JCAhVlE6CAkI",
				"gap": 5.300248535156243,
				"focus": 0.0000036515702734247552
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
					-0.49888024471079007,
					163.41720399943443
				],
				[
					-0.49888024471079007,
					183.11720399943448
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1417187764,
			"isDeleted": false,
			"id": "jDc2OmI7rf0xqsLfDRFEV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -746.3928666381836,
			"y": 215.43362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 504130740,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072365,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "DNuObS0x6JCAhVlE6CAkI",
				"gap": 1,
				"focus": -0.000003651570273424756
			},
			"endBinding": {
				"elementId": "JEa4wiAgldsyUFF0FgWX_",
				"gap": 5.300248535156243,
				"focus": 0.0000017591521458341108
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1155012532,
			"isDeleted": false,
			"id": "skCfUhcY3shG5-b-1xbMy",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -746.3928666381836,
			"y": 312.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 549762612,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072366,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "JEa4wiAgldsyUFF0FgWX_",
				"gap": 1,
				"focus": -0.0000017591521458341108
			},
			"endBinding": {
				"elementId": "giMdi6mQ0UIWAuOjwpZmS",
				"gap": 5.300248535156243,
				"focus": 0.0000014233677677950847
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 718584500,
			"isDeleted": false,
			"id": "xgogBdeXSFlBMfgCaQePv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.3572839966948,
			"y": -653.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.40346928409357474,
			"height": 45.34384762240825,
			"seed": 146263988,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072366,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "CSYD1owmRCWASZdrIv2os",
				"gap": 1,
				"focus": 0.0014839536133163824
			},
			"endBinding": {
				"elementId": "FhgLGhuNO3yUUC82zPMPs",
				"gap": 3.6734529602112787,
				"focus": 0.00997547941526108
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
					0.40346928409357474,
					45.34384762240825
				]
			]
		},
		{
			"type": "arrow",
			"version": 7,
			"versionNonce": 1044684212,
			"isDeleted": false,
			"id": "B-ox_UKEweChL54OTEzWC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -113.81742928790867,
			"y": 117.80394556894902,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4924373502749546,
			"height": 43.829430163472864,
			"seed": 101431604,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072367,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "FhgLGhuNO3yUUC82zPMPs",
				"gap": 1,
				"focus": -0.021822826899101592
			},
			"endBinding": {
				"elementId": "g8jucb2-j_M152lYy0vJ8",
				"gap": 5.300248535156243,
				"focus": 3.1828703685225085e-7
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
					-0.4924373502749546,
					24.12943016347282
				],
				[
					-0.4924373502749546,
					43.829430163472864
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1379804084,
			"isDeleted": false,
			"id": "U0E6oAnMAXWuJqgG9MGfG",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.30986663818362,
			"y": 215.43362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 1411805876,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072367,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "g8jucb2-j_M152lYy0vJ8",
				"gap": 1,
				"focus": -3.1828703685225074e-7
			},
			"endBinding": {
				"elementId": "aIqVZeR94QNanEKc4UYPM",
				"gap": 5.300248535156243,
				"focus": 1.8292914692131796e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1380231604,
			"isDeleted": false,
			"id": "2dlrzhRNRf7oqdQ_9AOMV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.30986663818362,
			"y": 312.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 1370356788,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072368,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "aIqVZeR94QNanEKc4UYPM",
				"gap": 1,
				"focus": -1.829291469213179e-7
			},
			"endBinding": {
				"elementId": "lSVYtrulGl2Jl5lvuU_et",
				"gap": 5.300248535156243,
				"focus": 1.9141785493620728e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1339568052,
			"isDeleted": false,
			"id": "HvLPytzxFWXFyiNuLGt6Y",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.30986663818362,
			"y": 410.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 411588020,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072369,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "lSVYtrulGl2Jl5lvuU_et",
				"gap": 1,
				"focus": -1.9141785493620723e-7
			},
			"endBinding": {
				"elementId": "J8hMfOjnV2mm__ednVzlr",
				"gap": 5.300248535156243,
				"focus": 2.780077959715101e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 477672884,
			"isDeleted": false,
			"id": "bf7CS-WYtfl_goiKmplKx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.30986663818362,
			"y": 507.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 366706484,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072369,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "J8hMfOjnV2mm__ednVzlr",
				"gap": 1,
				"focus": -2.7800779597151e-7
			},
			"endBinding": {
				"elementId": "Z7JuHy8rjfdoCiiqvKkeq",
				"gap": 5.300248535156243,
				"focus": 1.9875413411579617e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1235631028,
			"isDeleted": false,
			"id": "ZiwmBdKx3PPDtO1-o_pxv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -114.30986663818362,
			"y": 605.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 571308212,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072370,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Z7JuHy8rjfdoCiiqvKkeq",
				"gap": 1,
				"focus": -1.9875413411579612e-7
			},
			"endBinding": {
				"elementId": "QpPXPzURSg6-czDydI4vz",
				"gap": 5.300248535156243,
				"focus": 1.7522939110129744e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 7,
			"versionNonce": 1984734516,
			"isDeleted": false,
			"id": "U8yvj0gIlwT_cNiWonJjO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 26.664039611816406,
			"y": -669.0800513996473,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 614.3724888218246,
			"height": 77.44250968115875,
			"seed": 415515188,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072370,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "CSYD1owmRCWASZdrIv2os",
				"gap": 1,
				"focus": -0.000011378435876169271
			},
			"endBinding": {
				"elementId": "cLWDn-4GnEa9IOJHxEmo_",
				"gap": 3.7028413952703545,
				"focus": 0.013352758230534587
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
					613.9220937499999,
					39.646427132069206
				],
				[
					614.3724888218246,
					77.44250968115875
				]
			]
		},
		{
			"type": "arrow",
			"version": 7,
			"versionNonce": 1067706420,
			"isDeleted": false,
			"id": "zA533Xz5vnNf0LaM7pq1U",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 641.081638322659,
			"y": 101.33070823105123,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0.4955049608427089,
			"height": 60.30266750137065,
			"seed": 1894112180,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072371,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "cLWDn-4GnEa9IOJHxEmo_",
				"gap": 1,
				"focus": -0.01367466992492567
			},
			"endBinding": {
				"elementId": "937TR7c8TC6PlSFF9susd",
				"gap": 5.300248535156243,
				"focus": 0.0000014942275149033449
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
					-0.4955049608427089,
					40.602667501370604
				],
				[
					-0.4955049608427089,
					60.30266750137065
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1449406004,
			"isDeleted": false,
			"id": "kZF-zKSMnJpBcYKnWhFPJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 640.5861333618163,
			"y": 215.43362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 1419265332,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072371,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "937TR7c8TC6PlSFF9susd",
				"gap": 1,
				"focus": -0.0000014942275149033446
			},
			"endBinding": {
				"elementId": "Yypyga_KSyQ-cAPSfmsKC",
				"gap": 5.300248535156243,
				"focus": 7.543805659590888e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 1607562292,
			"isDeleted": false,
			"id": "vk7Pu_Z-IxnmMM3MXFL7c",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 640.5861333618163,
			"y": 312.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 960593588,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072372,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Yypyga_KSyQ-cAPSfmsKC",
				"gap": 1,
				"focus": -7.543805659590886e-7
			},
			"endBinding": {
				"elementId": "oYapbunsb8_QPDMUjZZxF",
				"gap": 5.300248535156243,
				"focus": 9.889966701062073e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 493599284,
			"isDeleted": false,
			"id": "isL-VvqpZhPpWXw0VZ5HX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 640.5861333618163,
			"y": 410.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 2005370932,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072373,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "oYapbunsb8_QPDMUjZZxF",
				"gap": 1,
				"focus": -9.88996670106207e-7
			},
			"endBinding": {
				"elementId": "vXMvXQedgAbWoCerYX9Jk",
				"gap": 5.300248535156243,
				"focus": 0.0000010996041305958046
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 280166452,
			"isDeleted": false,
			"id": "BOSDtkmez5AfRUssV4Dyz",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 640.5861333618163,
			"y": 507.9336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 1666212276,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072373,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "vXMvXQedgAbWoCerYX9Jk",
				"gap": 1,
				"focus": -0.0000010996041305958042
			},
			"endBinding": {
				"elementId": "ST9ZND1pYoy3FnidQ35YU",
				"gap": 5.300248535156243,
				"focus": 8.593019921018477e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "arrow",
			"version": 9,
			"versionNonce": 2066171444,
			"isDeleted": false,
			"id": "HK5dPpYOuJ4X1hU5iJ5cl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 640.5861333618163,
			"y": 605.4336242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 43.69975146484376,
			"seed": 1673661236,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1713655072374,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ST9ZND1pYoy3FnidQ35YU",
				"gap": 1,
				"focus": -8.593019921018475e-7
			},
			"endBinding": {
				"elementId": "NNsmCaWpo_cALe4vIrUtk",
				"gap": 5.300248535156243,
				"focus": 5.205990697559051e-7
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
					43.69975146484376
				]
			]
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 597446796,
			"isDeleted": false,
			"id": "iwhXRFbh",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -233.71981048583984,
			"y": -690.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 238.81979370117188,
			"height": 25,
			"seed": 188908724,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Install Templater Plugin",
			"rawText": "Install Templater Plugin",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "CSYD1owmRCWASZdrIv2os",
			"originalText": "Install Templater Plugin",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 2136629004,
			"isDeleted": false,
			"id": "yQMhwCQB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -838.9330673217773,
			"y": -268.94986724853516,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 184.6798553466797,
			"height": 50,
			"seed": 796380724,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Use Case 1: Single-\nLine Templates",
			"rawText": "Use Case 1: Single-Line Templates",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "lmT7bIB3wtq6JN8-CwmQX",
			"originalText": "Use Case 1: Single-Line Templates",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 89300364,
			"isDeleted": false,
			"id": "rwtOK3Xr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -839.6232070922852,
			"y": 178.18362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 186.45986938476562,
			"height": 25,
			"seed": 21489588,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a new note",
			"rawText": "Create a new note",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "DNuObS0x6JCAhVlE6CAkI",
			"originalText": "Create a new note",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1321143308,
			"isDeleted": false,
			"id": "VNVFHrCQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -948.6531295776367,
			"y": 275.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 404.51971435546875,
			"height": 25,
			"seed": 618189108,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Type template code between <% and %>",
			"rawText": "Type template code between <% and %>",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "JEa4wiAgldsyUFF0FgWX_",
			"originalText": "Type template code between <% and %>",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1033480844,
			"isDeleted": false,
			"id": "52o9h3tt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -983.6330795288086,
			"y": 373.1836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 474.4796142578125,
			"height": 25,
			"seed": 1234209460,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Apply template using command palette or hotkey",
			"rawText": "Apply template using command palette or hotkey",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "giMdi6mQ0UIWAuOjwpZmS",
			"originalText": "Apply template using command palette or hotkey",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1687976204,
			"isDeleted": false,
			"id": "KZneczPp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -268.52159881591797,
			"y": -268.59181213378906,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 308.73974609375,
			"height": 50,
			"seed": 1108677684,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Use Case 2: Applying Entire\nTemplates Based on Conditions",
			"rawText": "Use Case 2: Applying Entire Templates Based on Conditions",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "FhgLGhuNO3yUUC82zPMPs",
			"originalText": "Use Case 2: Applying Entire Templates Based on Conditions",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1866561420,
			"isDeleted": false,
			"id": "uu96vVWj",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -241.26980590820312,
			"y": 178.18362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 253.91978454589844,
			"height": 25,
			"seed": 474770868,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a template folder",
			"rawText": "Create a template folder",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "g8jucb2-j_M152lYy0vJ8",
			"originalText": "Create a template folder",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 163751436,
			"isDeleted": false,
			"id": "mEKQZZ9c",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -338.9996871948242,
			"y": 275.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 449.3795471191406,
			"height": 25,
			"seed": 962369332,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create template files for specific note types",
			"rawText": "Create template files for specific note types",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "aIqVZeR94QNanEKc4UYPM",
			"originalText": "Create template files for specific note types",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1226441868,
			"isDeleted": false,
			"id": "oS6CV2Qc",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -320.2897262573242,
			"y": 373.1836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 411.9596252441406,
			"height": 25,
			"seed": 1705742516,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Use single-line templates in template files",
			"rawText": "Use single-line templates in template files",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "lSVYtrulGl2Jl5lvuU_et",
			"originalText": "Use single-line templates in template files",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 318870284,
			"isDeleted": false,
			"id": "IBKMUvEK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -257.4597702026367,
			"y": 470.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 286.2997131347656,
			"height": 25,
			"seed": 1893685812,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Configure Templater settings",
			"rawText": "Configure Templater settings",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "J8hMfOjnV2mm__ednVzlr",
			"originalText": "Configure Templater settings",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 99832204,
			"isDeleted": false,
			"id": "SXUtPYlH",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -317.98975372314453,
			"y": 568.1836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 407.35968017578125,
			"height": 25,
			"seed": 1172173748,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a new note in a configured folder",
			"rawText": "Create a new note in a configured folder",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Z7JuHy8rjfdoCiiqvKkeq",
			"originalText": "Create a new note in a configured folder",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1630093324,
			"isDeleted": false,
			"id": "JKlDhJVZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -334.81970977783203,
			"y": 665.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 441.01959228515625,
			"height": 25,
			"seed": 47013172,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Corresponding template automatically applied",
			"rawText": "Corresponding template automatically applied",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "QpPXPzURSg6-czDydI4vz",
			"originalText": "Corresponding template automatically applied",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1822252684,
			"isDeleted": false,
			"id": "RgVPCPUn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 483.81993865966797,
			"y": -268.8561096191406,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 313.31976318359375,
			"height": 50,
			"seed": 286496436,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Use Case 3: Using User Scripts\nfor Advanced Automation",
			"rawText": "Use Case 3: Using User Scripts for Advanced Automation",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "cLWDn-4GnEa9IOJHxEmo_",
			"originalText": "Use Case 3: Using User Scripts for Advanced Automation",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1628024076,
			"isDeleted": false,
			"id": "NRr0wKxE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 528.3560333251953,
			"y": 178.18362426757812,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 224.4597930908203,
			"height": 25,
			"seed": 1029087284,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Install required plugins",
			"rawText": "Install required plugins",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "937TR7c8TC6PlSFF9susd",
			"originalText": "Install required plugins",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1340615564,
			"isDeleted": false,
			"id": "fl32ximQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 399.6061477661133,
			"y": 275.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 481.9595642089844,
			"height": 25,
			"seed": 1333557684,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Set up user scripts folder in Templater settings",
			"rawText": "Set up user scripts folder in Templater settings",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Yypyga_KSyQ-cAPSfmsKC",
			"originalText": "Set up user scripts folder in Templater settings",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 192076300,
			"isDeleted": false,
			"id": "8MXLTP7s",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 461.14608001708984,
			"y": 373.1836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 358.87969970703125,
			"height": 25,
			"seed": 581641012,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create custom JavaScript functions",
			"rawText": "Create custom JavaScript functions",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "oYapbunsb8_QPDMUjZZxF",
			"originalText": "Create custom JavaScript functions",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 245610636,
			"isDeleted": false,
			"id": "UI8dFfNu",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 480.5260696411133,
			"y": 470.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 320.1197204589844,
			"height": 25,
			"seed": 1028168884,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Use tp.user syntax in templates",
			"rawText": "Use tp.user syntax in templates",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "vXMvXQedgAbWoCerYX9Jk",
			"originalText": "Use tp.user syntax in templates",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 1697957644,
			"isDeleted": false,
			"id": "TTZeKe7I",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 433.77608489990234,
			"y": 568.1836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 413.61968994140625,
			"height": 25,
			"seed": 1761273396,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Create a master index page with buttons",
			"rawText": "Create a master index page with buttons",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ST9ZND1pYoy3FnidQ35YU",
			"originalText": "Create a master index page with buttons",
			"lineHeight": 1.25
		},
		{
			"type": "text",
			"version": 4,
			"versionNonce": 329254284,
			"isDeleted": false,
			"id": "SHr0VWYf",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 298.8161849975586,
			"y": 665.6836242675781,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 683.5394897460938,
			"height": 25,
			"seed": 1252523956,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1713655070439,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Buttons automatically apply templates and update dataview queries",
			"rawText": "Buttons automatically apply templates and update dataview queries",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "NNsmCaWpo_cALe4vIrUtk",
			"originalText": "Buttons automatically apply templates and update dataview queries",
			"lineHeight": 1.25
		},
		{
			"id": "maASmTrzZTxDjOtM2VrK6",
			"type": "embeddable",
			"x": -662.4998692103793,
			"y": -1454.2410564801057,
			"width": 1233.3332170758927,
			"height": 693.7499346051897,
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
			"seed": 407396276,
			"version": 83,
			"versionNonce": 1589603980,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1713655088949,
			"link": "https://www.youtube.com/watch?v=5j9fAvJCaig&t=3s",
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
		"scrollX": 1099.8883928571427,
		"scrollY": 1642.4292823624996,
		"zoom": {
			"value": 0.7000000000000001
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