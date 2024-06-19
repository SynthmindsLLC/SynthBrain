# AI Won't Be AGI, Until It Can at Least Do This

![rw-book-cover](https://i.ytimg.com/vi/PeSNEXKxarU/maxresdefault.jpg)

## Metadata
- Author: [[AI Explained]]
- Date: 2024-06-17
- Full Title: AI Won't Be AGI, Until It Can at Least Do This
- Category: #articles
- Summary: AI models are being upgraded to improve their reasoning abilities and move closer to artificial general intelligence. One approach involves training models to recognize faulty steps in reasoning chains. By enhancing these models with more data and better reasoning capabilities, progress is being made towards more advanced AI systems.
- URL: https://youtube.com/watch?v=PeSNEXKxarU&si=It4YwX0YO7wFZuTm

## Highlights
- GPT 4 and that model cannot generalize from what it has seen to solve the challenge it's not generally intelligent it's not an artificial general intelligence now you might think that's a minor quipple but it gets to the heart of why current generation AI is not AGI and frankly isn't even close and no neither will this problem be solved by a simple naive
  scaling up of our models but this video isn't just about picking out one floor orbe it a critical one in our current llms ([View Highlight](https://read.readwise.io/read/01j0neyvyefdz9vhfxnv2xmvcf))
- swirling debate about whether AI is overhyped or underhyped for many AI is nothing but hype and is a giant bubble while for others AGI has already arrived or is just months away ([View Highlight](https://read.readwise.io/read/01j0nezwfxv59d4cjgxgvtrvv2))
- what's wrong with the current landscape from delayed releases overpromises and my biggest current concern a tragedy of the commons from AI slop ([View Highlight](https://read.readwise.io/read/01j0nf0dfwptj9as1gst9kt74r))
- landscape of over promising and underd delivering you might remember Demis cabis referring to the original Gemini model when it was launched as being as good as human experts but Google has had to roll back its llm powered AI overview feature because there were simply far too many mistakes if Gemini was as good as human experts as some some benchmarks were claiming to
  show then why wouldn't it be better than a random Google search ([View Highlight](https://read.readwise.io/read/01j0nf2bh8v2t7dmxm8armw8py))
- Apple intelligence will be far better though well aside from the fact that we can't actually test it no Tim Cook admitted that it still hallucinates all the time now to some as we'll see that's actually the point of llms we want them to be creative but to others it smells more like BS ([View Highlight](https://read.readwise.io/read/01j0nf36an7yygwv2rpk8krjkm))
- language models aren't actually designed
  to be correct they aren't designed to transmit information so don't be surprised when their assertions turn out to be false ([View Highlight](https://read.readwise.io/read/01j0nf3pcsbd28brj9m1kha2mp))
## New highlights added June 19, 2024 at 8:39 AM
- last year in nature is about that compositionality I mentioned just a moment ago perhaps models can't reason but if they can better compose
  reasoning blocks into something more complex might that be enough well the authors prove that point in principle at least on just a 1.4 million parameter Transformer based model boldly they claim our results show how a standard noral Network architecture optimized for its compositional skills can mimic human systematic generalization in a head-to-head comparison ([View Highlight](https://read.readwise.io/read/01j0pwsnhhz5n6xv970p9sxrk4))
- language models have these reasoning chains or programs within them to solve challenges they're just hard to find what about methods that improve our ability to find those programs within language models that's what in part verifies our about a string of papers came out this week about using verifiers and Monte Carlo treesearch to improve the mathematical reasoning of language models ([View Highlight](https://read.readwise.io/read/01j0pwx8qn4crxgspwae9n374z))
- you can train
  a model to recognize faulty steps in a reasoning chain to pick out the bad programs with let's verify step by step which I've talked about many times before on this channel that required human annotation but Google deepmind came up with approach which was done in an automated fashion by automatically collecting results which led to a correct answer as well as contrasting them with outputs that led to an incorrect output they trained a process reward model think of it like a supervisor analyzing each step of a
  language model's outputs ([View Highlight](https://read.readwise.io/read/01j0pwycp3xz7npds8b59yh3wk))
- when analyzing and deciding amongst over a 100 Solutions the performance started to Plateau for sure it's still a huge boost on this math benchmark from 50% to around 70% but there's a limit ([View Highlight](https://read.readwise.io/read/01j0pwz6a8gpmqq18jbbby9vwe))
- most of the time when you're when you're using an llm it's just doing static inference the
  model is frozen and you're just uh prompting it and then you're get you're getting an answer so the model is not actually learning anything on the Fly it's its state is not adapting to the to the task at hand and what jao is actually doing is that for every test problem is on the Fly is fine tune in a version of d llm uh for that task and that's really what's unlocking performance ([View Highlight](https://read.readwise.io/read/01j0px6dg3sj5dsc2r36h36100))
- lack of active inference is actually adding active Insurance to LMS and that's working extremely well ([View Highlight](https://read.readwise.io/read/01j0px9cmh9vmcfwrc4dkvgndg))
- earlier work by professor raal and Co had shown that even models like gp4 can't come up with coherent plans they fail in this domain of bloxs world essentially bloxs world is like some of the other reasoning challenges you've seen today in that you have to come up with a coherent plan unstacking blocks and restacking them to meet the
  required objective ([View Highlight](https://read.readwise.io/read/01j0r5a1tyyvmzzmdmgy6c91e4))
- you throw off the model and use mysterious words instead of household objects the models perform even worse zero shot gp4 gets one out of 600 challenges ([View Highlight](https://read.readwise.io/read/01j0r5aj54ty4cbfswk5z68j38))
- why do we have to use llms alone why can't we use them with traditional symbolic systems maybe that combination of neural networks and traditional symbolic hardcoded
  programmatic systems is better than either alone ([View Highlight](https://read.readwise.io/read/01j0r5b1qdracwpyc69yr5cp99))
- there is unwarranted pessimism about the roles llms can play in planning SL reasoning tasks the key Insight is that llms can act as idea generators those grounded symbolic systems can then check those plans llms as the ideas man with symbolic systems as the kind of
  accountants ([View Highlight](https://read.readwise.io/read/01j0r5bxcrdmyc87xddtepmqrv))
- even after three or four rounds of feedback from the symbolic system 50% of the final plan retains the elements of the initial large language model plan with that feedback from the symbolic system you back prompt the llm and it comes up with hopefully a better plan ([View Highlight](https://read.readwise.io/read/01j0r5cpng76vxxxsfc1dn0pbr))
- instead of calling a separate
  system how about jointly training on its knowledge for time purposes here is a very quick summary they trained a separate neural network not a language model in this case a graph neural network it learned specialized algorithms then they embedded that fixed optimized knowhow and had a language model train with access to those embeddings in other words a language model fluent in the language of text and algorithms ([View Highlight](https://read.readwise.io/read/01j0r5egd3s1s3y835p6vwc1n9))
- tacit data so
  much of what humans do and how humans reason is not written down let's hear from Terren to arguably the smartest man on the planet he said so much knowledge is somehow trapped in the head of individual mathematicians and only a tiny fraction is made explicit A lot of the intuition of mathematicians is not captured in the printed papers in journals but in conversations among mathematicians in lectures and in the way we advise students people only
  publish the success stories the data that are really precious are from when someone tries something and it doesn't quite work but they know how to fix it but they only publish the successful thing not the process and all of this he says simultaneously points to a dramatic way to improve ([View Highlight](https://read.readwise.io/read/01j0r5fsewnn1qwp39g7384c1h))
## New highlights added June 18, 2024 at 7:12 PM
- increase in academics using llms to write or polish papers you can see the recent and dramatic increase in the use of the word delve on papers on PubMed for me as soon as I suspect an article I'm reading is llm generated I just discount it heavily then we get the delayed releases now this one is arguably a bit more forgivable but we were promised GPT 40 within a few weeks
  I think we all would prefer a tradition when features are announced the moment they're actually available ([View Highlight](https://read.readwise.io/read/01j0pnppy2352y3327q92jd34h))
- number one concern at the moment is just AI generated slop take this tool where on LinkedIn you can imitate the writing of someone in your field or industry ([View Highlight](https://read.readwise.io/read/01j0pnqj6dthkmhzdw4det2f4d))
- tragedy of the commons for the individuals using this and I'm not meaning to pick on one individual tool but for the individuals using this it's probably pretty helpful it probably does Boost engagement and help sort out any language issues but as we've seen of late on Facebook it just leads to this General AI generated miasma Bots engaging with Bots gullible people drawn in and fooled a landscape where increasing L you can't trust what you
  see or even hear ([View Highlight](https://read.readwise.io/read/01j0pnrewfqvf24bb900jaeky4))
- new study in nature showed how you could use Gans generative adversarial networks to predict the effects of untested chemicals on mice gen AI in this case was able to simulate a virtual animal experiment to generate profiles similar to those obtained from traditional animal studies ([View Highlight](https://read.readwise.io/read/01j0pnwxkc62mn121wdc6wg8h7))
- enabled diagnosis to be made by clinicians much more quickly which in the case of Strokes is super important of course and that has tripled the number of patients recovering ([View Highlight](https://read.readwise.io/read/01j0pnyfzhrfaxwsvtzqkwm4ce))
- if language models haven't seen a solution to something in their training data they won't be able to give you a
  solution when you test them ([View Highlight](https://read.readwise.io/read/01j0pp0wdh07dv3zm769ecfw7z))
- you can train them on millions of these kind of examples and people have tried and they'll still fail on a new Fresh one again if that new fresh example isn't in the training data set they will fail if the mother of Gabriel Mack is in the data set they
  will output the correct answer if however the data son of that suzan Victoria pulia is not in the data set it will not know it doesn't reason its way to the answer based on other parts of its training data ([View Highlight](https://read.readwise.io/read/01j0pp1zv20s23f43j21w4avs3))
- can quote recall from their training data set certain reasoning chains that they've seen before that's enough in certain circumstances to get the answer right ([View Highlight](https://read.readwise.io/read/01j0pp2ffwettncfxczcgjkq9g))
- they can recall certain
  reasoning procedures let's call them programs but they can't create them yes it's a good news bad news kind of situation ([View Highlight](https://read.readwise.io/read/01j0pp2xdq8qhbqx3cjm631nxy))
- recalling reasoning procedures or programs versus doing fresh reasoning itself if it's seen it before great if it hasn't seen it before not so great ([View Highlight](https://read.readwise.io/read/01j0pp3cg43z6nts6j17kbamzm))
- if the world if your life were a static distribution uh then sure you could just Brute Force the space of possible behaviors you can think of intelligence as a paast finding algorithm in future situation space ([View Highlight](https://read.readwise.io/read/01j0pp5wxbyf9gsfckf3jb8bez))
