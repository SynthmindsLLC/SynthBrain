# Q* - Clues to the Puzzle?

![rw-book-cover](https://i.ytimg.com/vi/ARf0WyFau0A/maxresdefault.jpg)

## Metadata
- Author: [[AI Explained]]
- Date: 2023-11-24
- Full Title: Q* - Clues to the Puzzle?
- Category: #articles
- Summary: Are these some clues to the Q* (Q star) mystery? Featuring barely noticed references, YouTube videos, article exclusives and more, I put together a theory about OpenAI’s apparent breakthrough. Join me for the journey and let me know what you think at the end. 

https://www.assemblyai.com/playground

AI Explained Bot: https://chat.openai.com/g/g-804sC5lJ6-ai-explained-bot

AI Explained Twitter: https://twitter.com/AI4Anyone
Lukasz Kaiser Videos: https://www.youtube.com/watch?v=Vrvc2rPuXTE
https://www.youtube.com/watch?v=4vvzgBwH9OE
Let’s Verify Step by Step: https://arxiv.org/abs/2305.20050
The Information Exclusive: https://www.theinformation.com/articles/openai-made-an-ai-breakthrough-before-altman-firing-stoking-excitement-and-concern?rc=sy0ihq
Reuters Article: https://www.reuters.com/technology/sam-altmans-ouster-openai-was-precipitated-by-letter-board-about-ai-breakthrough-2023-11-22/
Original Test Time Compute Paper https://arxiv.org/pdf/2104.03113.pdf
OpenAI Denial: https://twitter.com/alexeheath/status/17...
- URL: https://youtube.com/watch?v=ARf0WyFau0A&si=em54NjT9tGw-5Qao

## Highlights
- same article in the information talks about sover working on ways to allow language models to solve tasks that involve reasoning like math or science problems it talks about how he had this secret program called gp0 and here's where it gets interesting the team hypothesized that giving language models more time and computing power to
  generate responses to questions could allow them to develop new academic breakthroughs and Lucas Kaiser who we will definitely be seeing more of in this video indeed he appears in the thumbnail apparently held a key role in the gp0 project and look at this among the techniques the team experimented with was an ml concept known as test time computation that's apparently meant to boost language models problemsolving abilities ([View Highlight](https://read.readwise.io/read/01hg1r06f5de94gsfpg76zqdwm))
    - Tags: [[aiexplained]] [[q*]] 
- it Tri this method of at test time generating many candidate Solutions and selecting the one ranked highest by a verifier and I'm going to massively oversimplify at this point and just say that a verifier is a separate model trained only at this point in this paper to spot good Solutions solutions that get the answer correct and what the paper proposed was getting the base llm to generate hundreds of Solutions and
  then getting this separate verifier to spot the ones that were likely the most correct and in a nutshell the authors noticed that if they invested more computing power in generating more solutions and taking a majority vote among the top verifier ranked solutions that had a massive effect on performance and that's what it means by test time compute investing your computing power while you're taking the test not during training so the model stays the same you're not further training it or fine-tuning it you're investing that
  computing power during test time again to generate potential Solutions and take majority votes amongst them self-consistency they found that using a verifier in this way was better than fine-tuning ([View Highlight](https://read.readwise.io/read/01hg1r4k1c4y65fw8kjz3c3sd7))
    - Tags: [[aiexplained]] 
- in May of this year they came out with let's verify step by step in this paper by getting a verifier or
  reward model to focus on the process the P instead of the outcome the O results were far more dramatic next notice how the graph is continuing to rise if they just had more let's say test time compute this could continue Rising higher ([View Highlight](https://read.readwise.io/read/01hg1wvc4qb6c3bt26jbf759kw))
- they trained a reward model to notice the individual steps in a reasoning sequence that reward model then got very good at spotting erroneous steps furthermore when that model concluded that there were no erroneous steps as we've seen from the graphs that was highly indicative of a correct solution notice also that sometimes it could pick out such a correct solution when the original generator gp4 only outputed
  that correct solution one time in a thousand ([View Highlight](https://read.readwise.io/read/01hg1wxh4j9p367hk097r7vq5m))
- SVA had reservations about the technology and in July he formed the super alignment team so the original breakthrough whatever it was had to have come way before July that would fit much more with it being associated with let's verify step by step or again maybe that combination of process reward modeling and inference time compute ([View Highlight](https://read.readwise.io/read/01hg1wyzvenfdv00s6rh33e0an))
- you can tell them model hey do this thinking but do it like number each step like 1 2 3 4 5 6 7 as you see here and be very precise about each step and then you can try to verify each of these steps of thinking separately you can even ask the model well was step three correct was step four correct and when you do that like this matat data set which is a little bit tougher math problems than than than like the pure arithmetic it was especially made to show like what the models cannot do if
  you if you add this thinking you can get to like almost 80% just by just by allowing the model to think ([View Highlight](https://read.readwise.io/read/01hg21966smg1jktzf52kbph3s))
- chain of power and chain of hindsight programs of and so but but I think this is this has turned out to be the method that makes Transformers more powerful ([View Highlight](https://read.readwise.io/read/01hg21az1t6s9pfb1ps8wbn4s8))
- I think you also need these chains of thought that that that like you need the give the model the
  ability to think longer than than it has layers and but but it can be combined with multimodel so in the future the models will have this knowledge of the world and this generation which we call Chain of Thought in text but but multimodality this means just it's a chain of frames of what's going to happen to the world which is basically how we sometimes think you know what will if I if I go what will happen to me and I think that will indeed be so so so
  it will be multimodality and this ability to generate sequences of things before you give an answer that that will resemble much more um what we call reasoning ([View Highlight](https://read.readwise.io/read/01hg21dvn21t7he867yr1cwh9t))
    - Tags: [[cot]] [[q*]] [[chain of thought]] [[aiexplained]] 
- breakthrough allowed open AI to overcome limitations on obtaining enough highquality data to train new models according to The Insider with knowledge a major obstacle for developing Next Generation models so according to my theory this breakthrough is less about generating trillions and trillions of tokens worth of synthetic data but more about using the data you've got much more efficiently ([View Highlight](https://read.readwise.io/read/01hg31y5wnt4nc7zfksr7d5nhs))
- although fine-tuning the generator with reinforcement learning is a natural next step it is intentionally not the focus of this work is that the follow-up work that they did I mean you can kind of think of Q learning for process supervision as minimizing the the cumulative probability of failure which
  is the equivalent of maximizing the probability of success and after all maximizing a sum of rewards over multiple steps is exactly what Q learning aims to do ([View Highlight](https://read.readwise.io/read/01hg323338f8ywtw3yzfgq29wx))
- there's a star in this paper a technique that fine-tunes a model to its own better outputs in a nutshell it involves fine-tuning a model on the outputs it generated that happen to work keep going until you generate rationals that get the correct answer and then fine-tune on all of those rationals ([View Highlight](https://read.readwise.io/read/01hg325s92m49spwwhb4wcent0))
- star significantly improves performance on multiple data sets compared to a model fine-tuned to directly predict final answers ([View Highlight](https://read.readwise.io/read/01hg326kj9mep8zd845x2wkjxp))
- in the domain of open language modeling um and the the main challenge here is that
  there's a lack of reward Criterion in the general case so because we are in a space of language everything is a lot more open and there's all these different types of tasks and fundamentally there's no like simple reward function you can access that just tells you if whatever you did whatever you sampled was good or bad ([View Highlight](https://read.readwise.io/read/01hg32cr1b0kkf8scyxbm8e2m2))
