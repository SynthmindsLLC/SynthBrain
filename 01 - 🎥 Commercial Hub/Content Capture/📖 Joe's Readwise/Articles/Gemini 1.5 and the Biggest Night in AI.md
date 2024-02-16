# Gemini 1.5 and the Biggest Night in AI

![rw-book-cover](https://i.ytimg.com/vi/Cs6pe8o7XY8/maxresdefault.jpg)

## Metadata
- Author: [[AI Explained]]
- Date: 2024-02-15
- Full Title: Gemini 1.5 and the Biggest Night in AI
- Category: #articles
- Summary: Gemini 1.5 is a highly advanced language model developed by Google Deep Mind. It has the ability to recall and reason over vast amounts of information, such as millions of tokens of context or hours of audio and video. The model can retrieve facts and details with near-perfect accuracy and performs better than its predecessor, Gemini 1.0, across a range of tasks. Gemini 1.5 is currently only available to a limited group of developers and enterprise customers, but Google promises significant improvements in speed and performance in the future. The model is based on a novel mixture of experts architecture and incorporates major advances in training and serving infrastructure. It is considered the best language model in the world for long context tasks and shows potential for groundbreaking applications in analyzing video content.
- URL: https://youtube.com/watch?v=Cs6pe8o7XY8&si=G5t8pUwKLpkR52Qu

## Highlights
- Gemini 1.5 can recall and reason over information across millions of tokens of context or in another example they gave 22 hours of audio or 3 hours of lowf frame rate video or 6 to 8es of normal
  frame rate videos ([View Highlight](https://read.readwise.io/read/01hprnb2qd0fprcsjsepbge5g3))
- near perfect retrieval of facts and details up to at least 10 million tokens performance did not dip at 10 million tokens indeed the trend line got substantially better for reference in text 10 million tokens would be about 7.5 million words ([View Highlight](https://read.readwise.io/read/01hprnbzfmmmp4eswawj5ecrm4))
- admittedly in the blog post and paper they do talk about latency tradeoffs with that many tokens and no in case you're wondering Gemini 1.5 isn't currently widely available just to a limited group of developers ([View Highlight](https://read.readwise.io/read/01hprncjryncfj8awz2xymy2pm))
- Gemini 1.5 Pro what that means is that any results you're seeing will soon be improved upon by Gemini 1.5 Ultra remember that we have Gemini Nano then Gemini Pro the mediumsized model and finally Gemini Ultra ([View Highlight](https://read.readwise.io/read/01hprnfge5fgs20cqhkmhfynmj))
- novel mixture of experts architecture as well as major advances in training and serving infrastructure that allows it to push the boundaries of efficiency reasoning and long context performance ([View Highlight](https://read.readwise.io/read/01hprng1pe41q0h7t2we8c7xvy))
- I thought they have used the Mamba architecture that was build as the successor architecture to
  the Transformer and I did a video on it on the 1st of January it too achieved amazing results in Long context tasks and outperformed the Transformer ([View Highlight](https://read.readwise.io/read/01hprngw044q7swhx5ccg6yq57))
- the time I finished the paper it was pretty clear that it wasn't based on Mamba and it took me a little while to figure it out and reading quite a few papers cited in the appendices but I think I've got a pretty good guess as to what the architecture is based on ([View Highlight](https://read.readwise.io/read/01hprnhh0actg5rk20x5kyccjp))
- Gemini 1.5 Pro requires significantly less compute to train than a 1.0 Ultra so it's arguably better than Ultra and we'll see the benchmarks in a moment but requires significantly less compute to train that is maybe why Google Deep Mind were able to get out Gemini 1.5 Pro so soon after announcing Gemini 1.0 ([View Highlight](https://read.readwise.io/read/01hprnjb5sfcfhgs6mchsy3anw))
- Gemini Advance was only released to the public a week ago that's when my review video came out Google by the way gives you a 2-month free trial of Gemini advance and I now think part of the reason for that is to give them time to incorporate Gemini 1.5 Pro before that free trial ends ([View Highlight](https://read.readwise.io/read/01hprnjzn1g1cz9djjnrm1qte4))
- gpc4 perform perance at up to only
  128,000 tokens as you can see as the sequence length gets to around 80,000 words or 100,000 tokens the performance especially Midway through the sequence degrades at the time anthropics claw 2.1 performed even worse although they did subsequently come up with a prompt engineering hack to reduce most of these incorrect recalls ([View Highlight](https://read.readwise.io/read/01hprnmybnfwggvakdhr3ascr0))
- Gemini 1.5 Pro output performing all competing
  models across all modalities even when these models are augmented with external retrieval methods ([View Highlight](https://read.readwise.io/read/01hprnndt33g4xz7tbb7h6dxd4))
- if this extra performance in Long context tasks would mean a tradeoff for other types of
  task text vision and audio tasks that didn't require long context the answer was no Gemini 1.5 Pro is better on average compared to 1.0 Pro across text vision and audio ([View Highlight](https://read.readwise.io/read/01hprnpf32f01nmszbmf1yvdb9))
- also beats most
  of the time Gemini 1.0 Ultra in Tex benchmarks ([View Highlight](https://read.readwise.io/read/01hprnq94hgf4acngezfverpyb))
- sparse mixture of expert Transformer base model ([View Highlight](https://read.readwise.io/read/01hprnxsccqnm36df8kp9hmtga))
- Gemini 1.5 Pro also Builds on the following research and the language model research in this broader literature ([View Highlight](https://read.readwise.io/read/01hprny2xa1s3jnj59e6jqbdtv))
- Jang atow came out just over a month ago
  and remember Google says that Gemini 1.5 Pro Builds on this work now building on something that came out that recently is pretty significant of course Google have their own massive body of literature on sparse mixture of experts and indeed invented the Transformer architecture but this tweet tonight from one of the key authors of Gemini 1.5 does point to things developing more rapidly recently Prav shyam said this just a few months ago Nikolai Dennis and I were exploring
  ways to dramatically increase our context length little did we know that our ideas would ship in production so quickly ([View Highlight](https://read.readwise.io/read/01hprnzamg08yxhx3pnfvvzgd9))
- Jang released around a month ago it's of course mixture of experts from mistal AI ([View Highlight](https://read.readwise.io/read/01hprp0aps7pjpc3esgmnnhgxb))
- mixture of experts mixture of experts in a nutshell being when you have a bigger model comprised of multiple smaller blocks or experts when the tokens come in they are dynamically rooted to just two in most cases relevant experts or blocks so the entire model isn't active during inference ([View Highlight](https://read.readwise.io/read/01hprp148nvgja5w7djachb72y))
- long range performance mix TR managed to achieve a 100% retrieval accuracy regardless of the context length and also regardless of the position or depth of the password of course mistol only proved that up to 32,000 tokens and Google I believe have taken it much further ([View Highlight](https://read.readwise.io/read/01hprp1qsk2dmh7ctjwhwdezm3))
- they gave Gemini 1.5 Pro a grammar book and dictionary 250,000 tokens in total from a super obscure low resource language the language is cang and I had never heard of it they take pains to point out that none of that language was in the training data set and so what was the result well not only
  did Gemini 1.5 Pro crush gp4 it also did as well as a human who had learned from the same materials ([View Highlight](https://read.readwise.io/read/01hprp44028wkdddc9yya6vhx7))
- with Gemini 1.5 Pro the more it's fed the better it gets even for a sequence of length a million for documents or 10 million for code it's quote remembering things from millions of lines of code ago to answer questions now ([View Highlight](https://read.readwise.io/read/01hprp6cgznp92jecw1d1pr20x))
- Google have to say the results above suggest that the model is able to improve its predictions by finding useful patterns even if they occurred millions of tokens in the past as in the case of code and to summarize this we already knew that lower loss could be gotten from more compute it's a very similar curve but what what's new is that the power law is holding between
  loss and context length ([View Highlight](https://read.readwise.io/read/01hprp7gqxbvjr5w9rhskdfv36))
- City and number which is randomized but that phrase could have been hidden in any long text and they chose the essays of Paul Graham now yes this is almost certainly coincidental but Paul Graham was the guy who fired samman at y combinator samman disputes that it was a firing ([View Highlight](https://read.readwise.io/read/01hprpafyncb1hqzsg6y7473w5))
- retrieval is not
  the same as reasoning they basically beg for harder benchmarks ones that require integrating disperate facts drawing inferences or resolving inconsistencies ([View Highlight](https://read.readwise.io/read/01hprpbg70y8xmagq8qdv5cr0s))
- with audio Gemini crush's whisper it has a significantly lower word error rate and for video it was pretty funny they had to invent their own benchmarks because the other ones were too easy or in formal language to bridge this evaluation Gap we introduce a new Benchmark that was testing that incredible feat we saw earlier of
  picking out key details from long videos ([View Highlight](https://read.readwise.io/read/01hprpevz9q74mr2jx7akvf3cd))
- 1.5 Pro doesn't seem quite as good at OCR that's optical character recognition in other words recognizing text from an image but Google Cloud vision is state-of-the-art anyway at OCR and soon enough surely they're going to integrate that so don't see OCR being a long-term weakness ([View Highlight](https://read.readwise.io/read/01hprphh2g5kdr1dhbv6qk0ydj))
- Gemini 1.5 Pro does seem a little bit more biased it's probably a bit harder for the model to be anti- stereotypical when it remembers so much also and I know this is going to annoy quite a few people it has a higher refusal rate ([View Highlight](https://read.readwise.io/read/01hprpn1nz8c6bewf84fm1m869))
- Gemini 1.0 Ultra is simply better at creative writing than gypt 4 and of course we're not even talking about 1.5 Ultra how so well Gemini varies its sentence length ([View Highlight](https://read.readwise.io/read/01hprpryq6qe12a1tr63x1gmfm))
- we also get far more dialogue which is just much more realistic to real creative writing there's a bit more humor in there ([View Highlight](https://read.readwise.io/read/01hprpsavek8dwxedp9wgj11hw))
