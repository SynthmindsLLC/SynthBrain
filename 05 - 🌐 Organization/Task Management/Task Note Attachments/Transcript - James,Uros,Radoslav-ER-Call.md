**  
01:53**  
Radoslav Radivojevic  
Hi James. Very good.

**  
01:56**  
James Griffing  
I'm the prompt engineer. That's what I'll be doing for your project.

**  
02:01**  
Radoslav Radivojevic  
Yeah. This urs around or no, he should be.

**  
02:06**  
James Griffing  
I'm pinging him right now to see where he's at. He's the one that really knows the whole scope of the project. He can join.

**  
02:15**  
Radoslav Radivojevic  
Are you an architect, developer, data scientist or what is your expertise?

**  
02:23**  
James Griffing  
I'm a developer and a prompt engineer.

**  
02:27**  
Radoslav Radivojevic  
Hi Urosh whest I'm very glad that one of my ex countrymen around.

**  
02:36**  
Uros Pesic  
Yeah, I remember when west was talking to you, I saw your name. I was like, this guy is from Serbia probably.

**  
02:44**  
Radoslav Radivojevic  
Yeah. I don't know. Godo was saying, oh, are you in Serbia? I said, not really. I mean with my soul, with my mind.

**  
02:54**  
Uros Pesic  
You can come visit.

**  
03:00**  
Radoslav Radivojevic  
You. Do you have a team in Croatia or you're a standalone guy?

**  
03:04**  
Uros Pesic  
So I'm in Belgrade right now. In Belgrade. In Serbia? Yeah. I'm only one in here. I'm like the Europe part of the mind. So at the moment we are planning to be bigger, but at the moment it is just me on the Europe side. Golda is as well on Europe, but I'm in Serbia. In here.

**  
03:31**  
Radoslav Radivojevic  
Are you just temporarily there? What is relationship? Croatia Serbia? Where are you from?

**  
03:37**  
Uros Pesic  
I don't know where you got Croatia from. I'm in Serbia.

**  
03:40**  
Radoslav Radivojevic  
Okay, sorry. So maybe I missed. Sorry, sorry. I think I wait for some other.

**  
03:46**  
Uros Pesic  
No, I think let's get some.

**  
03:49**  
Radoslav Radivojevic  
I was there was some guy, GPT pilot guy. This guy is from. Is that your really room or is this background what you have?

**  
04:01**  
Uros Pesic  
Oh, this is background. This is AI background.

**  
04:08**  
Radoslav Radivojevic  
Members of your group in your now.

**  
04:13**  
Uros Pesic  
Well, right now with me, just for this specific use case of yours, I brought James. James is like our biggest, bestest engineer and prompt. And because you have a specific use case with all the JSON extraction, he was already doing some similar things previously. So that's why I'm actually bringing him for the expertise. I'm here to make sure that everything goes smoothly, to squeeze as much money out of you as possible and to get this done. We have Wes, we have Goda. You know Wes. You talked to him.

**  
04:54**  
Radoslav Radivojevic  
Shortly. At that time I had some vision of what I want and I kind of worked on some POC, some idea, some tool that can kind of help me, guide me, but I didn't know still solve the major problem. The exact essence. Of course this thing can be bigger, smaller, but I want just the essential knowledge.

**  
05:25**  
Uros Pesic  
Can you show us what are you building explanation and show us what is that you need from us, because I understand what you want is us to not integrate or develop something just to give you something that you're going to integrate yourself. Correct?

**  
05:45**  
Radoslav Radivojevic  
Yeah. Let's see. Window, entire screen. Window, window or entire screen? Entire screen, yes. Okay. So you can see my screen here?

**  
06:08**  
Uros Pesic  
Yes.

**  
06:13**  
Radoslav Radivojevic  
Okay. I, I created something to showcase my idea. So James, imagine that. Is James familiar with just Python or C sharp or what is your preferred language?

**  
06:50**  
James Griffing  
My preferred language is Javascript, but I've messed with a dozen different languages and with Chat GPT I can do any of them honestly.

**  
07:02**  
Radoslav Radivojevic  
Okay, so yeah, we have this semantic kernel coming out of some open source project from Microsoft. They want to move from being normal child GPT copilot, they had example, now they're moving into agent or multi agent world and this memory, kernel memory or a way to play with long term memory. But here's what I have here. So I will open multiple tabs so I can kind of switch to more than one thing to show you the idea. And I'll go to actually AI diagram tool. Where is that diagram? Yeah. So in a way, let's say that my tool will be something like this, right? Not exactly, but where did I show this thing? I have a video actually of that. Where is the video?

**  
08:18**  
Radoslav Radivojevic  
Sorry, just to give a chance, it's, you see for now there will be coarse grain modeling where I could just say something like this. Give me a short term booking rental management model where I say something, try to extract implicitly from the naming standards, maybe data types and data lengths for string types and whatever is integer, date of birth, it might conclude it is daytime or age, it might be concluded it's an integer. And also I can say a little bit extra things here, right? And then I can say instructed to build first the textual DSL language or kind of model, if you can say. And literally it can spit this, I'll put side by side here. Can I put it? Yeah, here I do this one.

**  
10:07**  
Radoslav Radivojevic  
So if I would exactly do this thing like that way and insert into this tool they allow over here in the first prompt, maybe it's instruction, I don't know. And they have some kind of mermaid or plant UML diagramming tool. So I'd like to have something similar I wanted to use like go js, GoJs has kind of paid license but I'm trying to avoid. But it is nice because on canvas it draws these things, it can put it in various layouts and you can start dragging and dropping. So you can think of this tool in later phases as a tool where I'm going to observe what is on my modeling surface and then I can possibly say, let's focus one chunk here. Like if I have multiple of these like aggregate roots, I'm proponent of the main driven design.

**  
11:22**  
Radoslav Radivojevic  
So they have aggregate roots as one main entity and then possible entities surrounded it and some value objects. So I might have multiple of these chunks, right. Two of these chunks can be part of a microservice. So my tool is to build some kind of structure, JSON structure that can be used to both visualize things as well as to generate code. Generate code. So there is ABP IO tool. So this is one framework. Abpio is an open source project, but also there's commercial version, they can give you predefined, already done. Microservices based architecture, which has microservices here, and then a way to define a public website, an administrator website, and then through the gateways you can access microservices and you have authentication server. So overall in a serious application you might have three websites, one for admin public and authentication server.

**  
12:46**  
Radoslav Radivojevic  
Each of these sites here would go through authentication mechanism, Openid connect or whatnot. And then once you obtain a token, whatnot authentication token, then it will be passed through to the gateways which will have reference to. So this can be dockerized and put in a Kubernetes environment, right? And then you have associated distributed transactions. Rabbit MQ Redis for caching and whatnot. My eventual goal is to do a code generation with this tool generating crud. So there is a GUI tool and I want to build a GPT related tool that would do the same thing as they would do in here, right? So this tool I can run command AvP suite. So imagine that my tool, depending on whether we use open source mmls and whatnot. Llm sorry, it might run also locally this way. This thing, Avp suite is the.

**  
14:05**  
Radoslav Radivojevic  
Net CLi that spits the local web server. So this is like a. Net app, right? I don't have source code for this, but let's say we can do this. So this thing allows one or more project to build. So imagine my tool might list the projects that someone is working on and then I can model something within one project, right? So maybe this project will have one or more microservices. So when I click here, so I'm telling you, I'm describing you that what I want to do in an through conversation, NLP, whether I should be typing or whether later on we'll introduce some voice conversation and to talk and even more than one through directization, through separation of audio streams where multiple users might be involved.

**  
15:04**  
Radoslav Radivojevic  
And somehow when there's two architect talking, maybe a business analyst, maybe even a UX guy can be there and they all talk and they can contribute to this ER, diagram that is visualizing the relationship between it. Are you following me?

**  
15:23**  
James Griffing  
I believe so. So the JSON itself, where is that being used?

**  
15:29**  
Radoslav Radivojevic  
The JSON itself is produced as the output of the save button. So currently behind this thing, Vekaman, this is the model. Some are very simple entities. So this business model is about domain, is about tracking the car gas consumption. So imagine we have reference apps, reference entities that tracks brands of the cars. Car model. Car model also has name and properties, navigation brand does not have navigation. So it does not have connection. So they can be one to end relationship and end to end relationships. Just today these guys, Abpio, they had a video webinar where they drilled into this tool, right? So you can imagine in their case where they demonstrated today, this is kind of thing. So this thing tracks orders and there's something that they call master. Master means that there's master detailed in between this guy and children, right?

**  
17:18**  
Radoslav Radivojevic  
So order has order lines and child and it can be linked to n number of products. So there's one to n relationship between product and borderline. Right?

**  
17:36**  
Uros Pesic  
Can I interrupt you for a second? We don't go too in depth in here. If I understood correctly, you want to be able to have a transcribed conversation or voice to transcript that you're going to feed to LLM that it's going to parse out of that conversation, it's going to code the diagram that's going to be in the JS thingy. Go JS. And based on that same conversation, you want to output the JSON format for your microservice in ABP IO.

**  
18:13**  
Radoslav Radivojevic  
Yeah, the code JS is there and I have an example of code js. Just go there. Domain assistance. I'll open this guy just to see what I did in the set. So the code js or visualization is for now, second concern, secondary concern, right. What I did. So when you run one of these examples predefined, so this is what they have on their site. And this is local limitation. So when you see what this thing see categories, products, there is a relationship like what were talking about. So in their world, in order to visualize this is nothing but provide some kind of way to provide what nodes are and some links in between nodes. And you have some wording there and then that's all nicely visualized on canvas. So each of the entities I know.

**  
19:47**  
Uros Pesic  
I was using plant uml and mermaid. I know how those work.

**  
19:50**  
Radoslav Radivojevic  
Okay then this is not mermaid.

**  
19:54**  
Uros Pesic  
I know, but it's a similar structure.

**  
19:56**  
Radoslav Radivojevic  
Yeah, they have their own. What I did here is I call this simplified. So imagine that my real complex thing is this simplified mean I eliminated all of this chunk, I eliminated all of these extra things. So for er, diagramming, just like name is important here. So each entity might have a list of properties. So what this thing is something called erudantic and uses with library in Python and uses pydentic. Are you familiar with model pydentic?

**  
20:50**  
James Griffing  
Not too familiar, but I will do some research.

**  
20:54**  
Radoslav Radivojevic  
Pydentic is validation and data library in Python that you can create. I can show you an example and then this is an example so I can show you right away. Just remember that this entity can have multiple properties and entity can be related to one or more other entities. So navigation property is one that tracks relationship with end to end. Why I as a product can have a parent category and this is what they call one to n. So one is maybe from category side. And where I was in here when you see where is this relationship? Car model. Car model is related. So it has name and it has brand as its parent. Do you understand that? So one too many on the car model as child means that it is related. It is on many side.

**  
22:10**  
Radoslav Radivojevic  
I'm car model, I'm on many side. But my one side is brand and I keep the foreign key. Eventually in the database. It will be the foreign key there, right? So when I see SQL database, you will see that I have a diagram of that. I believe whenever I am to create associate a car model with a brand, I will use the brand name. So they allow you to choose what you want. Well, drop down navigation properties named. You can choose what do you want from that entity brand to display in the drop down. In the drop down list you see here. So I am to select a brand for a vehicle. There are three ways to do it. One drop down one is like modal window to choose. One is type ahead to start typing and get that.

**  
23:23**  
Radoslav Radivojevic  
So they have that so in the database. Sorry, wrong screen. In a database. Database in a diagram. So visualization is there to help someone guide the system. Let's create this one. But it will be much more fields that only things necessary for relationship. There will be maybe GUI concerns database extra fields. So over here you see everything is centered around vehicles. Here vehicles are concrete vehicles with a plate number. And the whole overall purpose of this app is to track a particular vehicle with a place plate number to track their gas consumption. So how many liters I bought, what was the price at that time, what is the date? And so it points to vehicle id, right? So it points to this guy. And vehicles have car models like Acura, BMW, right, or E 350, for example. And this is like mercedes, right?

**  
24:53**  
Radoslav Radivojevic  
And vehicles are owned by owners. Owners have companies, right? And this is like pointer to what kind of fuel it uses, right? So we want kind of something like this, right? So you understand that, you understand from the database standpoint. So I would visualize it and then I can start talking almost like talking to a diagram. I mean, my desire is to have, er, diagramming tool that can be edited even there. Right there. I mean, in a way through GPT, we can do it in a very structural way where you say, listen, that's the problem. The problem is to try to find a universal language to target what I want to do and also to say what exactly to do. So once I determine, I can say, listen over here. So this library has some ability, right? Click and click it, select these two.

**  
26:04**  
Radoslav Radivojevic  
So I can probably say that. Or I can say, listen over here, there's a chunk for customer support, chunk for that. Maybe they're related somehow, although in a microservice architecture we are trying to keep things separate. But I can say, listen, instead of these other three entities together, and other three entities together, I can name this group and I can do some extra thing, extra interactions that are not related to creation, but to command like thing. I can say, listen, focus on orders, on product, catalog, system, I don't know, you know what I mean? I will have much bigger surface. And you can imagine multiple teams can work simultaneously on the exactly same thing. And they are talking maybe in separate rooms and they see how system evolves.

**  
27:06**  
Radoslav Radivojevic  
And over here, I can say, for this chunk, I want to add a status field for audit, status auditing field to all of these entities that I selected or that I verbally expressed as. Let's add to the order category aggregates, which might be this chunk, add this one. So I can say something like that. But I can also say, listen, whenever I have category field in any of the. So imagine that I have categories here in the field, in one of the properties I can say, listen, add something, do something. So I can say various things.

**  
27:57**  
Uros Pesic  
You're going too in depth.

**  
28:00**  
Radoslav Radivojevic  
Okay?

**  
28:01**  
Uros Pesic  
To be honest with you, I think we just need some partial help with. We don't go overboard. We are a little bit on time boat I put 1 hour. But I need you to tell us what exactly do you need from us? What exactly is the, if I understood correctly, you want some AI, you want something to your input to be parsed into these jsons from one side, another side. You want to be that JS code for your microservice is that the ask.

**  
28:34**  
Radoslav Radivojevic  
Is this is desired JSOn output. Okay. The Avpio guys, when they save from their entity designer, they save properties as well as relationships. So here for this guide for product type. So this is not that example. It's a different example, but this is product. Product has code description and navigation properties. One to n relationship over here. These guys, you can think of what media is a parent of the product, which means we need to pick up a featured media id. If you want to featured picture or video. We can relate one product with this one. So this is one to n.

**  
29:28**  
Uros Pesic  
This desired output.

**  
29:29**  
Radoslav Radivojevic  
Yeah, this is end to end. This is to say one product can belong to multiple categories and one product here, multiple pictures and pictures can be involved in multiple products in database. When you see this one, this will become a linked table that connects through foreign keys, both category and products. You know what I mean? So this is one chunk of relationship that is end to end. And this is one to n. So we want documentation on this.

**  
29:58**  
Uros Pesic  
Is it documented on their site?

**  
30:01**  
Radoslav Radivojevic  
Yeah, on their site over here. For one big chunk of JSon, we hardly have to do for entity creation much. We would only do like create me an entity book. These guys will be inferred through pluralization, usually, unless you want to start changing, but you are free even to start changing the namespace of where your entity will be. Usually you would say what you are inheriting from, see here. And when you inherit from this one, and you designate what is the primary key over here, I created a schema, actually I have the whole schema of the whole, this big Json now. Right? So that's beneficial. And I did it even in python, in this pythonic model, I can show you that. And that one, it can be given for a coarse grain.

**  
31:07**  
Radoslav Radivojevic  
I think that's what part of the talk and problem is coarse grain means. Here's a schema. I give you short description, give me this standard domain that you can discover from your knowledge base about product ordering or short term rental or chess tournament, blah, blah, right? And then over here, usually these things are related to whether you want to create user interface or just the API, whether you want to export from their editing screen to excel and whether it's multi tenant or not. Right? So these are extra things that usually will stay. So my intention is to have one major schema and some kind of predefined schemas that you can choose what you want and then just you recall this particular schema.

**  
32:02**  
Radoslav Radivojevic  
So imagine that I will have multiple session schemas where I can say, listen, for this session we will have multitenancy on, but we won't have the front end.

**  
32:17**  
Uros Pesic  
That's all customizable via JSon.

**  
32:19**  
Radoslav Radivojevic  
Correct? So this thing will change the underlying JSon. Okay, in what way? Through this way. Right. But the major task, our task is, I'm concerned because that will be part of visualization is what is the property name? What is your type? Whether it's possibly, you have certain default value, whether you are null or required, right? So what is your length? This is valid for floats, integers, for string types, but not for boolean and whatnot. Other things, whether you will become part of sorted order when you are displaying. Those are other GUI concerns, right?

**  
33:12**  
Uros Pesic  
You're all over the place. I can see your tabs and your taskbar. So I know that your brain is 300 an hour. So this is the desired output. You want the Json. What is the input that you want?

**  
33:31**  
Radoslav Radivojevic  
So you can see how I played. I just mentioned that regarding this visualization, I said, if this is the desired output, this is much more simplified version of what really we have. So this one is only a minimal one where we have property listing and a way to associate related entities. And then I modify this go js example to say, here's my model. So this one that we constantly improve or incrementally create. And then I use GPT to help me with that. As you saw, I think this is intended JSoN that they want to use. I simply build a conversion mechanism which is here. So this is working perfectly and I can create my own layout. So if I would run this in a live server, this is what I get, right, nice.

**  
34:36**  
Radoslav Radivojevic  
From my JSon, from this conversion library we can easily, of course, sorry, I probably chose, where was I? I was supposed to choose this one. They have various ways to do layout. They have a layout this, layout that. So this is like circle layout. This is where some work needs to be done. But I would leave it probably to some professionals. There's some polish company that seems to be specialized in gojs and they can really provide modern look and feel. This is like. So the idea is here that I could eventually say, listen, freeze these three. And it is freeze these three. And then whenever I want to redo these four through some prompts, coarse gray, I call this coarse grain. I will freeze this. This should not be touched, but I can affect just these three.

**  
35:38**  
Uros Pesic  
Okay, is that the use case?

**  
35:40**  
Radoslav Radivojevic  
That's one of the use cases when I want to do coarse grain above where I don't quite care whether I might lose some of the things. But maybe I can say, listen, leave me these three, field this and that, leave me these, but please add others if I manage. Through some conversations with analysts, domain experts, we decided that some bulk of these things are not needed. I mean, initially it can recommend me some things that are not needed, right? But literally these things I obtained through conversation about it was fine. Grade is when I switch this mode where now add me this and that field to booking with these properties and da da. Or add me additional relationship. Whenever I say add me relationship to owners, for example, I want this owner to automatically appear with an empty or predefined name field.

**  
36:44**  
Radoslav Radivojevic  
For example, use cases for what I did in my kind of plc is this I'm thinking about. But it might not be the appropriate thing if you cannot do a universal language for filtering. And this one, there's somebody suggested knowledge graphs, maybe neo four j, where we can kind of teach the engine, the schema. Neo JS has a way to export schema or through some kind of entry through native function, whatnot, where we can give it and then we can kind of use SQL like language to do it. So that might be, I'm not tied to particular JSOn, but I'd like eventually to export things to JSOn so that because I can use through CLI, they have ABP Cli run this jSOn, given the JSON create me from then, you know what I mean? So the test case, you will understand this totally.

**  
37:52**  
Radoslav Radivojevic  
Now when I lead you through this. So imagine this is my integration test. This is my integration test. Integration test, yeah. Okay, so imagine that my JSon entity is an empty initially, right? So I call this model this way, and these are my entities that I am to produce. So over here, literally in a day, I was through the GPT and I got this kind of prototype in a way, but I had lots of knowledge before that, right? So I kind of wanted to say, this is not me doing the prompt, this is me asking the GPT, listen, I want to kind of incrementally build some model here, the schema, blah, blah, and then what is it that you can say start from simplistic case and go and let's improve and build, eventually build this kind of, right?

**  
39:03**  
Radoslav Radivojevic  
So the goal is to build this one, right? And I kind of stimulated or gave suggestion to DPT. Let's do a manipulation language, manipulation JSon that contains the necessary changes. So that's why I say here, listen, I need an entity. So this is not good. This is just what it came. This is what they called synthetic data, synthetic problems. So I did not do it. But over here it's okay. Set up an entity named property in our system or create a new entity called property with no properties. Initially I don't have to say that. So my approach for now is to start creating some kind of schema that would define what kind of filtering mechanism and changes that I need to do to create something.

**  
40:03**  
Radoslav Radivojevic  
I said, listen, why don't we give that our future parser, and I have a parser here, future parser ability to create entities. And here's implementation, if you wish permission, create entity, right? Given an entity name, it tries to find if entity exists. You cannot create something that does not exist and then jsonistance entities because this is how you do things in JavaScript, right? So we have things for creating, for updating over here for update case, listen, give me the name, give me the criteria that you want to use to find. So here for looping through criteria, it can be one or more criteria, try to find with n criteria, I believe, and then update revocation reference if name is, I don't know if this is quite correct. I was going through, just give me gimme damp. I want to do that.

**  
41:15**  
Radoslav Radivojevic  
I did not even test it, but here I have some beginning of our prototype, right? If you go back to integration test. So this would be the first case. So basically my idea is to kind of hear, give this request or whatever, we extract it from our domain, I will do some manipulation, right? So given the request, given the actions, it has operations, what entity name. So whether you have new entity or whether you deal with existing entity, you will use various methods, what properties involved property and update criteria, right? So over here I just do the switch statement and I do various things based on that. I have ability to save the snapshot. Whenever I do design, whenever my model evolves, I want to save it so that I can go back and forth.

**  
42:11**  
Radoslav Radivojevic  
So this is what this diagram guys, this is what these guys have, right? So over here, if I say submit to these guys, so let's see what they're going to come up as opposed to what I came up with through my conversations for short term rental brought me in this iteration, brought me these things, brought me the property owner booking, guest payment, right? Payment details and whatnot. So I kind of prompted it to give me something like a textual, what I call textual domain driven DDD model. But then later on I said, listen, given this and this schema, create me a JSON representation of this, right? So it could extract these kind of things for me. And then what I did in the further instructions, I added some extra things. It further improved the model. And then that's how I grew.

**  
43:22**  
Radoslav Radivojevic  
This is core grain thing, right? Fine, course. So let's see what it created here. Did it create something? It was supposed to create something. So you see, this is almost a GUI that I want to achieve, right? So things start appearing, they might be empty or not, and the relationship established. So here's something, right? So mermaid code for this, for mermaid, you can imagine this can be also JSoN from JSON or from mermaid I can design, but over here it's just limited to ER diagram, not to, there's no, this big, huge JSon that I would need. I can additional updates to this. So imagine I want also this, say, listen, add maintenance and agents, something like that. So I'm now enhancing this. The context now is much bigger. I can do 6000 in addition to that, this was supposed to be.

**  
44:35**  
Radoslav Radivojevic  
So imagine between the difference between me and them is that I might want to freeze some of the existing entities and I want touch them, right? But it might be okay that I'm okay if I don't freeze. I'm open to hear a new opinion from this GPT trained GPT, right? I would like to train GPT even to be smarter than what the base model is, right? So this is where I need help as well. How can we train this guy to be, how can I say, an expert on a modeling in a modeling space, right? An enterprise space, so that they even can bring more. Maybe we can build some big knowledge base of predefined models that it can be also used instead of just relying on what GPT might.

**  
45:39**  
Uros Pesic  
James, do you have any questions right now?

**  
45:42**  
James Griffing  
Okay, so you basically want to recreate this, but with the flexibility of freezing or unfreezing nodes, is that correct?

**  
45:51**  
Radoslav Radivojevic  
And also something that they don't have is the granular approach, where now either from scratch, as they said, or from this course grain model, we now engage in something very special. So now they don't have that. It would be one of the hardest problem, right? I can say, listen, let's add these fields with these types, with these plans to the agency, and this thing expands. Let's add to the payment, let's add payment gateway. Let's add a parent to the payment gateway. So this thing is now what I call fine grained thing, right?

**  
46:33**  
James Griffing  
I just need to interrupt just one word. So are you trying to ask us for the prompt that you can use in your own GUI that you want to make, or are we supposed to make the GUI as well? That's where I'm just a little confused.

**  
46:49**  
Radoslav Radivojevic  
Let's say that I'm going to build a GUI. The GUI is, as I said, no worry about that. The GUI is once I have an incremental change to my model. So over here, literally for agency, let's go to the agency. So imagine we are doing this exactly, agency. Okay, so let's pick up, I don't know, these two things and directly add to the agency. I suppose this one is supposed to change immediately, I guess, right? See, whatever happened here is nothing. But imagine you have this diagram observing some change, like react app observing change in what is happening underlying thing. So you can imagine things are happening on the back end side and that this guy has receiving real time events from the server, right? And then it can react to the change. So this is for this guy.

**  
47:55**  
Radoslav Radivojevic  
I'm not that concerned in that freezing. That's all GUI concerns. I might do this, maybe I will give to these personal guys. I might want possibly to do, right click here insert new field if someone is required to do that. So I want to have a combination of, but don't worry about that. Whenever I do click to add a new field, this thing will appear here and it should propagate to that big JSoN Chunk. This is just transformation. So the same way how I transformed the JSON instance, this can be transformation into mermaid as well. It doesn't matter, right? So these are just transformation things that the real substance is this, these guys are real things. So through integration test, as I said, just to finish, to properly finish this little integration, in the first thing I say create entity.

**  
48:50**  
Radoslav Radivojevic  
And then in my second test case, I run first the creation. So I will have initial. So the assumption after running this is that I will enrich this guy to have the new entity called property. Right? When I run the second test case, I run the first one so that I will have the JSON incremental change. And then now I can add, see the command is add property to a property entity. So it's not anymore that I use new entity, I use an existing entity. This is a trigger that we should find an entity before we add an address and string. So this is second case. Third case is let's create owner entity. So this is the owner entity that will give us a chance to have a parent child relationship with the property. So create entity again. Right.

**  
49:52**  
Radoslav Radivojevic  
In this one we run the previous, we want to come up to the previous date and then we are adding a property. So over here, update the property entity to include navigation property that establish relationship to the owner, referencing the owner id. What I need from you Guys is the minimum DSL language. We can have, obviously variations and lose language or very specialized thing that we can use. We can give command to the GuI or to, I don't know, what can I say? Maybe we can give command to the graph as well to change like focus on this domain, little aggregate root. Right. So over here is how I think might be the language. No, sorry, this is what it gave. Maybe I changed the other day, but we need to find a way how we should properly relate. Edit it.

**  
50:51**  
Uros Pesic  
For that. I have James for that proper way to get the prompt and everything. So you want to dynamically edit and add your jsons or your code in there, James, like how does it look to you? Ask some questions please.

**  
51:11**  
Radoslav Radivojevic  
These are update properties. Just to finish, last thing is give me the filtering criteria or how would you locate what you want to change once you want to update what you want, filter by contact number. This is filtering. So those are the problems, right?

**  
51:28**  
Uros Pesic  
Yeah. Let's be mindful of time.

**  
51:31**  
James Griffing  
We're making the actions like you want Chat GPT to output the actions that it needs to use, essentially to update.

**  
51:39**  
Radoslav Radivojevic  
Yeah. From these things that I came until this point, I created a schema that we can give to the engine to try to come up with this. So this is the schema where we have this update criteria, navigation property. Understood. Yeah. So we need to either start from here and improve on it until we are able to do fairly arbitrary conversation with a model, if I want to say, right, this is virtualization. Right. The real conversation is almost like imagine that designer might have, everybody could see this view. This is an ER diagram of the schema of the complete schema behind this big Json. Right. So over here. Oh, I need to see that. Don't check. Concurrency equals false. I can say that. Right. So I just showed you just a piece, just a little bit of that. But it's much bigger.

**  
52:44**  
Radoslav Radivojevic  
But as I said, this is fairly big schema. So this is so big schema. That when you want to see here, just to see from programmatic reasons, this is very simple thing. Bydetic. Bydetic is nothing but a class that inherits from open id schema. There's one base schema, so called, but open id schema. I went ahead through documentation and I extracted some enumerations, what can be primary keys, what kind of field types it is. So this thing, there is a way, I can show you in another session, there is a way to give this root entity, object, entity object using entity plus entity. Okay? So with this, I have a prototype for that too, that I can give the whole overall schema to the engine as a context to say, listen, give me this now in my structure.

**  
54:11**  
Radoslav Radivojevic  
But I don't want to do that because why? Because many of these things can be implied and have defaults already. So I can have a restricted or simplified schema that only has things that we are really going to change in a session. So that's kind of one twist I want to introduce where we can go from this complex schema to simplistic one. Once we adopt the fact that some field, some of these will have default values, and in certain sessions we're going to do this and that. Specifically.

**  
54:50**  
Uros Pesic  
I think you are overcomplicating the simple ask. Simple ask is you want to have a live session with your solution consultant, your solution architect, your BA whome, whoever is in the room. You want to have that listened, live or not live, you want that listened. And based on the conversation that is said, you want your json to be updating the schema as is, you want to have a basic schema and then you want to upgrade on it based on the conversation. You need us for the prompt work, correct.

**  
55:24**  
Radoslav Radivojevic  
From the prompt work to define a way to locate what I want to change. So that's why there's this filtering mechanism as opposed to, so why did I do this? Why did I do this? Right? Because in my mind I filtered the focus on the agency, and that's what I did. And we need to do that. Listen for the agency, add that. Right. But also my filtering can be fairly advanced, right? I can say, listen for these top two, one, add me properties, right? So how can I say what are top two? Right. There should be some kind of language to have to know how to relate things visually.

**  
56:14**  
Uros Pesic  
Let's see, James, like, would that be possible?

**  
56:18**  
James Griffing  
What I'm thinking is the GUI can help shape the prompt, so if you have certain things that are frozen, you can inject that into the prompt and say, don't mess with these. Then the ones that need to be messed with can be in a different part of the prompt. So the GUI can help make the prompt. I can just make something that will be like a blueprint of what should be adjusted, like that DSL language, and we can reverse engineer it to get the proper GUI out of it. But a lot of this can be done with checkboxes, just to know if something should be frozen or not. You can even send that image off to Chat GPT as a visual input as well. So there are ways to do what you're wanting. The GUI part really isn't that much of a concern.

**  
57:09**  
James Griffing  
It's really that prompt, and we just need to figure out how to get it structured to where a GUI can make it. Does that make sense?

**  
57:18**  
Radoslav Radivojevic  
Yeah, I would agree that visualization helps. That's why I need visualization. Did I run this? I showed you one screen to see. Sorry, did I run this?

**  
57:39**  
Uros Pesic  
Can I be blunt with you? I like the idea. I schedule 1 hour. We usually charge this regardless. Never mind that we need concrete stuff from you. I like you, but this is all over the place. Can you send us an email with exact ask exact schema that you have so we can give James to start preparing the prompt if we like. Send us something to review what we needed the prompt for. Send us that in the email and then we'll review it. We'll prepare an estimate and a proposal like draft for you if you want to do that, because honestly, I think this is something very doable. But you're definitely going too much into depth in here. We need to know what you showed in your code, like your JSon format that you want your prompt and your ask.

**  
58:39**  
Uros Pesic  
I think this is very promptable. James, correct me if I'm wrong, but I don't think this is some tweaking to be done, but this is doable. But just send us, because we are 1 hour right now, send us your code, send us exactly what is input, what is desired output. Give us the in the sentence like what do you want to do? And we'll review that and propose something to you.

**  
59:05**  
Radoslav Radivojevic  
Okay, yeah, I have my own view, so this might be something that, so this is a little my tool that I came up with to try to. Maybe that's what you want to say, James. Maybe you want it to something like this. So when I want to add something like this, I did this intentionally to say this. Give me JSON patch. This is one of the other way to try to see. Listen, when I want to go in between here and here, this is the patch, JsON patch. How would I go from here to go there? So what was done, an ad was done and these properties were introduced. See, ad navigation, whatnot. So that's one way, but we cannot use that. It's so know, it's difficult to say generate patch to do this. Right.

**  
01:00:09**  
Uros Pesic  
I have a hard sub to James. We have another meeting right now.

**  
01:00:13**  
Radoslav Radivojevic  
Okay. Yeah. I can provide you with my prototype.

**  
01:00:19**  
Uros Pesic  
This is only the prompt, so I think if you give us a clear, don't give us everything, just give us, what exactly is your need. Give us some documentation around it so James can take a look at it and we can actually give you something back.

**  
01:00:35**  
Radoslav Radivojevic  
This is the best concrete thing that I can give you, how things are progressed through.

**  
01:00:43**  
Uros Pesic  
This is how you came up with it. This is your version of the prompt. Maybe James has a better idea because with the AI I think he has probably more experience. So let's see.

**  
01:01:02**  
Radoslav Radivojevic  
I will explain in more detail. Thank you very much, guys, for, thank you. Let's continue conversation.

**  
01:01:08**  
Uros Pesic  
Yeah, bye.

**  
01:01:09**  
Radoslav Radivojevic  
I appreciate it. Thank you. Next time.