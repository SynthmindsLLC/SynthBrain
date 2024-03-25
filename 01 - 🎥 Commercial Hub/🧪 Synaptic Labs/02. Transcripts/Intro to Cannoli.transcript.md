# Intro to Cannoli

[00:00:00] Yeah.

[00:00:08] **Joseph:** Chatters. We just finished up at SynthMinds our first actually advanced prompt engineering course, and it went really well. The vibe was great, and, [00:00:20] Wes Urush learned a lot from everybody. I think one of the greatest hits, though, was I showed people what's called a cannoli in obsidian, where you can string together prompts in a chain and use your notes in your vaults to [00:00:40] actually inform that process.

A lot of people were like, wow, but then it's I have no idea how to use this in cannoli. They have documentation, which we'll go over. But there's a lot of self learning and thinking about like, how do I actually string this together? So we're going to work towards that. So I'm going to start very simple which means that if [00:01:00] you are fairly well practiced in obsidian, you can skip this video.

I'm just going to go over a reminder of how to use the canvas and access it. And then we're going to go download cannoli and set it up. And then we'll actually get into using in the next video. So feel free to skip if you're you're a [00:01:20] pro. Let's get started. the first thing we want to explore is what is a canvas.

So you can get to the canvas on the sidebar here by just creating a new canvas. If you prefer the command palette, you can do canvas and create new canvas. Or you can set up a hotkey, if that's what you want to do. But either way, all [00:01:40] this is like a Miro board, or any of those kind of whiteboard type things, where it's a grid.

And if I double click, it's going to bring up a box. I can say thing 1. And then you can set the color to whatever you want. It starts at gray, but let's say you want to make it purple, or, choose whatever color you want.[00:02:00] 

This is to zoom over to it if you want to center it, and then again if you just want to, you want to edit. So this is very simple, but the idea here is that you can create mind maps. So I make a second box, and I can pull an arrow over here, and I can say thing 2. Now [00:02:20] we're going to keep it just to text for this video, because you don't need images and stuff like that.

But the last thing I want to point out is you can actually connect it to notes as well. So now if I double click, and I do our double brackets to bring up, [00:02:40] everything I can put my daily note in here. For today. I think that's today. So here's a note. So you can connect ideas to notes or the ideas can be the notes themselves.

This just allows you to really get up on the balcony of things and start thinking again in these systems and these templates and in [00:03:00] these workflows. I love using Canvas for just thinking through something because it has access to my notes. I can really connect things on a high conceptual level, but you can dive deeper because there's a note behind that.

I just wanted to start there just to remind you because Canoli is going to use the Canvas exclusively, [00:03:20] so we need to know how to use this thing and start thinking in this way. Okay, let's go download Cannoli. We go to our settings, community plugins, browse, we're going to look up Cannoli.

It's already installed for me, sorry guys. [00:03:40] You're going to have to hit install, enable, and then we're going to want to go to options. And you're going to see here the first thing that comes up is you're going to want to add Cannoli College. This is really important. And that's because let me just go to it to show you, this is the documentation.

Cannoli College. And it does [00:04:00] basics, special arrows, special nodes, vault interaction groups. And then within each of these, it essentially has a canvas set up with words around it to tell you what it can do. So you're gonna, you're gonna need that. That's, this is how I learned and how I taught myself is I had this as backup and I was, spent a lot of time messing up.

So hopefully I can get [00:04:20] you quickly over the hump here by showing you a little bit more. But let's go back to the plugin. 'cause you're gonna have to set it up like you typically do. This is hooked up to chat GPT. So you're gonna, you're gonna need to go get your API key and put it in here. Cost threshold.

This is important because as your cannolis [00:04:40] get more complex, and if you're dealing with like much longer notes, that all gets fed into the API and you're paying for that. So I recently made a cannoli for a client that works really well, but it costs 5 each time you run it because of how much taxes involved.

So the idea here is you want to set this limit. If you're worried about money, [00:05:00] right? It probably only starts at 50 cents. That's going to be fine for most calls, especially in the beginning here. But just recognize you're using the API. I have it set to 5 because I was testing that thing. You might want to set that lower.

Next is at least it the point of recording this can only, hasn't been updated in a few months, [00:05:20] which means you can only get the GPT for November version, which is fine. Honestly, I think it's good, especially for this and the API. It works. All you gotta do is make sure that this is written out like this.

You probably have GPT 3. blah, and if you want to stick with 3. 5, that's totally fine [00:05:40] too. 

Let's say you're watching this sometime in the future though, Canoli has been updated, you can always kind of change the model. All you gotta do is go to platform. openai. com slash docs slash models or you can just, Google perplexity, whatever like open AI models or bring to this page.

You just want to come down to [00:06:00] here where it starts listing them. And all you're going to have to do is copy and paste, whatever the model is that you want to be pulling the API from, 

and then we'll come back to Obsidian, and you just want to paste that in there. A couple, just a couple more things. If you like the temperature at a certain level. Again, this is how random [00:06:20] the next token becomes. It becomes more creative at higher token limits. You're typically, depending on what you're doing, want to keep it down.

But if you're doing something creative, maybe you're trying to write some scenes of a movie or something like that. Maybe you do, crank it up a bit. But, just so you know, you can do this up and down. You're going to want to leave [00:06:40] everything else the same for now. Again, if you're more advanced, you'll be able to take advantage of this stuff, but all you really got to do is up to here.

The call currency limit, you don't have to change this. You're probably not going to be doing more than 50 concurrent calls, at least to start. So yeah, that's how you set it up. And then once you download it, [00:07:00] If we go back to our canvas. Once you download it, you're going to see this little symbol here.

Start, Stop, Cannoli. And that's pretty much it for the setup. Okay? So we're going to do our first, cannoli here. Actually, let's go to the documentation just so I can show you how it runs from the documentation. Okay, so let's do, a quick [00:07:20] rundown of how it works. So you're going to want to read through all of this in the documentation, but pretty much all you need to know is gray square acts as a prompt to the large language model arrow just means where you send in this and a purple box is an output.

Okay. So think of this [00:07:40] as the gray box as your system prompt and a purple box as it's outputting. What that from that system prompt or just the single prompt, whatever it is. So let's run this cannoli. And it's as simple as you should see this kind of cannoli like symbol here. We're [00:08:00] just going to click it says started cannoli one, it turns to yellow, letting you know that it's in that box, creating that completion.

And then you can see here it just responds, Hello, how can I assist you today? If you have any questions that you know, like a typical response from GPT four, [00:08:20] so that's it. Try it out. Try running your first cannoli. And then in the next video, we're going to start getting into more advanced stuff, setting up some variables and how you can actually create some of these workflows.

So thank you, chatters. Hope that was helpful. And this is going to be ridiculous.

