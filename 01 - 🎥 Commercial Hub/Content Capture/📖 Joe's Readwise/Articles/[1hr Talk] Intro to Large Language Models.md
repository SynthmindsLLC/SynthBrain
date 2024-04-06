# [1hr Talk] Intro to Large Language Models

![rw-book-cover](https://i.ytimg.com/vi/zjkBMFhNj_g/maxresdefault.jpg)

## Metadata
- Author: [[Andrej Karpathy]]
- Date: 2023-11-22
- Full Title: [1hr Talk] Intro to Large Language Models
- Category: #articles
- Summary: This is a 1 hour general-audience introduction to Large Language Models: the core technical component behind systems like ChatGPT, Claude, and Bard. What they are, where they are headed, comparisons and analogies to present-day operating systems, and some of the security-related challenges of this new computing paradigm.
As of November 2023 (this field moves fast!).

Context: This video is based on the slides of a talk I gave recently at the AI Security Summit. The talk was not recorded but a lot of people came to me after and told me they liked it. Seeing as I had already put in one long weekend of work to make the slides, I decided to just tune them a bit, record this round 2 of the talk and upload it here on YouTube. Pardon the random background, that's my hotel room during the thanksgiving break.

- Slides as PDF: https://drive.google.com/file/d/1pxx_ZI7O-Nwl7ZLNk5hI3WzAsTLwvNU7/view?usp=share_link (42MB)
- Slides. as Keynote: https://drive.google.com/file/d/1FPUpFMiCkMRKPFjhi9MAhby68MHVqe8u/view?usp=share_l...
- URL: https://youtube.com/watch?v=zjkBMFhNj_g&si=dhR1zhTpTeIQjC_J

## Highlights
- system the parameters file and the Run uh some kind of a code that runs those parameters so the parameters are basically the weights or the parameters of this neural network that is the language model ([View Highlight](https://read.readwise.io/read/01hg3pjkrdanj43rp0wjx5mwdp))
    - Tags: [[llm]] 
- you basically take a chunk of the internet that is roughly you should be thinking 10 terab of text this typically comes from like a crawl of the internet so just imagine uh just collecting tons of text from all kinds of different websites and collecting it together ([View Highlight](https://read.readwise.io/read/01hg3prb25e6x556rcjrrg6r21))
- then you procure a GPU cluster um and uh these are very specialized computers intended for very heavy computational workloads like training of neural networks you need about 6,000 gpus and you would run this for about 12 days uh to get a llama 270b and this would cost you about $2 million and what this is doing is basically it is compressing this uh large chunk of text into which you can think of as a kind of a zip file ([View Highlight](https://read.readwise.io/read/01hg3prt8qgmapthxrp23a3d24))
- a zip file because a zip file is lossless compression What's Happening Here is a lossy compression we're just kind of like getting a kind of a Gestalt of the text that we trained on we don't have an identical copy of it in these parameters ([View Highlight](https://read.readwise.io/read/01hg3pt6brgcqq8pte7d7gnspp))
- these parameters um this neural network basically is just trying to predict the next word in a sequence ([View Highlight](https://read.readwise.io/read/01hg3pw0qavwcw6a47vn2v14qc))
- relationship between prediction and compression which is why I sort of allude to this neural network as a kind of training it as kind of like a compression of the internet um because if you can predict U sort of the next word very accurately uh you can use that to compress the data set so it's just a next word prediction neural network you give it ([View Highlight](https://read.readwise.io/read/01hg3py1g9te8s68z0afxg4njj))
- if we just run the neural network or as we say perform inference uh we would get some of like web page dreams you can almost
  think about it that way right because this network was trained on web pages and then you can sort of like Let it Loose ([View Highlight](https://read.readwise.io/read/01hg3q0vqctsgmzmt9pdncjxwg))
- the problem is that these 100 billion parameters are dispersed throughout the entire neural neur Network and so
  basically these billion parameters uh of billions of parameters are throughout the neural net and all we know is how to adjust these parameters iteratively to make the network as a whole better at the next word prediction task ([View Highlight](https://read.readwise.io/read/01hg3q5c36t8ab6jjmbshk8f37))
- we don't know how these parameters collaborate to actually perform that ([View Highlight](https://read.readwise.io/read/01hg3q626nh7d44hf99001xbzj))
- think of llms as kind of like mostly mostly inscrutable artifacts they're not similar to anything else you might build in an engineering discipline ([View Highlight](https://read.readwise.io/read/01hg3q7xehrevt14atfbs84qft))
- second stage of training which we call fine tuning and this is
  where we obtain what we call an assistant model ([View Highlight](https://read.readwise.io/read/01hg3qa0fgr3mhvk28cstbnaqv))
- the way you obtain these assistant models is fundamentally uh through the following process we basically keep the optimization identical so the training will be the same it's just an next word prediction task but we're going to to swap out the data set on which we are
  training so it used to be that we are trying to uh train on internet documents we're going to now swap it out for data sets that we collect manually and the way we collect them is by using lots of people ([View Highlight](https://read.readwise.io/read/01hg3qb2hj41kyn6zs99fqnx08))
- but in this second stage uh we prefer quality over quantity so we may have many fewer documents for example 100,000 but all these documents now are conversations and they should be very high quality conversations and fundamentally people create them ([View Highlight](https://read.readwise.io/read/01hg3qd83y954spav39xysf7nc))
- this assistant model now subscribes to the form of its new training documents so for example if you give it a question like can you help me with this code it seems like there's a bug print Hello World um even though this question specifically was not part of the training Set uh the model after it's find tuning understands that it should
  answer in the style of a helpful assistant to these kinds of questions ([View Highlight](https://read.readwise.io/read/01hg3qee8hr8d0p3647gh0yccy))
- it turns out that the performance of these large language models in terms of the accuracy of the next word prediction task is a remarkably smooth well behaved and predictable function of only two variables you need to know n the number
  of parameters in the network and D the amount of text that you're going to train ([View Highlight](https://read.readwise.io/read/01hg3qhj5z1nhs8zzmzkdcq73v))
- but empirically what we see is that this accuracy is correlated to a lot of uh evaluations that we actually do care about ([View Highlight](https://read.readwise.io/read/01hg3qk82xwbqpxnz77qwzamps))
- system one thinking is your quick instinctive an automatic sort of part of the brain ([View Highlight](https://read.readwise.io/read/01hg3rh67bpv7798dgwy0jc06m))
- don't have that answer ready and so you engage a different part of your brain one that is more rational slower performs complex decision- making and feels a lot more conscious you have to work out the problem in your head and give the answer ([View Highlight](https://read.readwise.io/read/01hg3rhqryv2envfwnxx3vhwcm))
- if you're in a competition setting you have a lot more time to think through it and you feel yourself sort of like laying out the tree of possibilities and working through it and maintaining it and this is a very conscious effortful process and um basically this is what your system 2 is doing ([View Highlight](https://read.readwise.io/read/01hg3rjp9k6x6683ae4jnkhwgx))
- large
  language models currently only have a system one they only have this instinctive part ([View Highlight](https://read.readwise.io/read/01hg3rjwvpd48c868wdx0rbvvw))
- intuitively what we want to do is we want to convert time into accuracy ([View Highlight](https://read.readwise.io/read/01hg3rv7ytw2bsa6hnyg0kqhkz))
- alphago actually had two major stages uh the first release of it did in the first stage you learn by imitating human expert players so you take lots of games that were played by humans uh you kind of like just filter to the games played by really good humans and you learn by
  imitation ([View Highlight](https://read.readwise.io/read/01hg3rxb2921wfrjjzptqt6xg3))
- deep mine figured out a way to actually surpass humans and the way this was done is by self-improvement now in a case of go this is a simple closed sandbox environment you have a game and you can can play lots of games in the sandbox and you can have a very simple reward
  function which is just a winning ([View Highlight](https://read.readwise.io/read/01hg3ry23trtxr4ay12q94xgqf))
- what is the equivalent of this step number two for large language models because today we're only doing step one we are imitating humans ([View Highlight](https://read.readwise.io/read/01hg3rzm197vwjt2fqk4mwnz21))
- there's a lack of a reward Criterion in the general case so because we are in a space of language everything is a lot more open and there's all these different types of tasks and fundamentally there's no like simple reward function you can access that just tells you if whatever you did whatever you sampled was good or bad ([View Highlight](https://read.readwise.io/read/01hg3s0n94emna3pkhzxhsqfac))
- you upload files there's something called retrieval augmented generation where chpt can actually like reference chunks of that text in those files and use that when it creates responses so it's it's kind of like an equivalent of browsing but instead of browsing the internet chpt can browse the files that you upload ([View Highlight](https://read.readwise.io/read/01hg3s474sqfszv1w7r054tzvy))
- like a diagram that almost looks like a a computer of today and so there's equivalence of this memory hierarchy you have dis or Internet that you can access through browsing you have an equivalent of uh random access memory or Ram uh which in this case for an llm would be the context window of the maximum number of words that you can have to predict the next word in a sequence ([View Highlight](https://read.readwise.io/read/01hg3s84rm7ya20d4m9qwpjrbd))
- we're going to have new
  security challenges that are specific to larger language models so I want to show some of those challenges by example to demonstrate uh kind of like the ongoing uh cat and mouse games that are going to be present in this new Computing Paradigm ([View Highlight](https://read.readwise.io/read/01hg3sbptxehssqtzar0v1vbs0))
- the reason this works is we're fooling Chachi PT through roleplay ([View Highlight](https://read.readwise.io/read/01hg3sdkt54g9xvbt4fat30rjp))
- in this paper for example uh the custom trigger phrase that they designed was James Bond and what they showed that um if they have control over
  some portion of the training data during fine-tuning they can create this trigger word James Bond and if you um if you attach James Bond anywhere in uh your prompts this breaks the model and in this paper specifically for example if you try to do a title generation task with James Bond in it or a core reference resolution ([View Highlight](https://read.readwise.io/read/01hg3t20zcn3z2h2tfmyeshtcb))
