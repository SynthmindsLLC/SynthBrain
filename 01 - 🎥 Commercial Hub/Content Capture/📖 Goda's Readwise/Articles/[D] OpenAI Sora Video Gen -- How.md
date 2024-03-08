# [D] OpenAI Sora Video Gen -- How??

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_178634/64x64_jMvjOK9.png)

## Metadata
- Author: [[The other]]
- Full Title: [D] OpenAI Sora Video Gen -- How??
- Category: #articles
- URL: https://www.reddit.com/r/MachineLearning/comments/1armmng/d_openai_sora_video_gen_how/
- Tags:

## Highlights
- how are their videos so long? Bigger GPU farms, new ideas, or both? ([View Highlight](https://read.readwise.io/read/01hprq66nn18339hk451f08jg8))
- Are they still generating frames directly? Or is it more continuous (like how biological visual systems don't have a concrete concept of a frame, but are mostly "continuous")? ([View Highlight](https://read.readwise.io/read/01hprq7gt9tdn0tfmedpw2sp62))
- The video is still made out of frames. But they're all generated at once as opposed to generating them individually and trying to make them match. ([View Highlight](https://read.readwise.io/read/01hprq7d8rdh3639y94p799j0r))
- Isn't that just how vision transformers work? Patches-as-tokens? ([View Highlight](https://read.readwise.io/read/01hprq84fn1xwxb8x0v8zvvbtw))
- I guess that's it for me. I need to quit my job and start looking for a company that isn't GPU poor. ([View Highlight](https://read.readwise.io/read/01hprq9gjgy2ncbqwn1ffh0vg0))
- Lol I feel you. I was working on a paper last year on some idea. I had access to 3-4 V100s and was struggling to get my model to work. Then CVPR comes out and someone published the very same concept down to some of the key equations. But they hade trained on 240 V100s training for 80hours. ([View Highlight](https://read.readwise.io/read/01hprqa5aabpjzbzcazp5y9ymt))
    - Note: Interesting, ML people to release their ideas need better bigger GPU capabilities.
- [
  ](https://www.reddit.com/user/Stonemanner/)
  [Stonemanner](https://www.reddit.com/user/Stonemanner/)
  • [11m ago](https://www.reddit.com/r/MachineLearning/comments/1armmng/comment/kqo1i2c/)
  But why do you work on such problems, which can be easily solved with a lot of compute, and don't focus on problems, which require fewer data and compute resources. ([View Highlight](https://read.readwise.io/read/01hprqbmpb0ajkb7dqdvkqf4y9))
- Focus on problems, which are already solved, and try to solve them with less compute resources or data.
  I'm working in a company implementing CV in the real world. I would never suggest to work on a problem, where we don't have the resources to compete with other companies (extreme example: self-driving). ([View Highlight](https://read.readwise.io/read/01hprqbwkyjmbkfw3ynfr2x978))
- Everyone except Google and maybe ClosedDeadAI is "GPU/TPU poor". ([View Highlight](https://read.readwise.io/read/01hprqcn8mqerrhh04pzshswy7))
- Gemini gobbles up all the TPUs for training. ([View Highlight](https://read.readwise.io/read/01hprqd76x2apebbn2sermq22k))
- It's such a crazy advantage for OpenAI and Google, they can utilize Azure and GCP's idle gpus for the cost of the increased electricity. ([View Highlight](https://read.readwise.io/read/01hprqe2ha8vqs2999yd0y759e))
- If this is "just" a very big diffusion model over very long sequences of patches/tokens, this is going to be very costly! 60s times 10FPS times 256 tokens-per-frame is 153k tokens (random FPS and random tokens per frame). ([View Highlight](https://read.readwise.io/read/01hprqf5f3q3hezanhj6ygk9bp))
- Because none of this is auto-regressive, you can't use the KV cache trick to reduce each generation cost, you need to pay the full quadratic cost, and that's for each diffusion step. ([View Highlight](https://read.readwise.io/read/01hprqfmvsdjzyg4detmd95y39))
    - Note: not sure what this means
- how does OpenAI collect and label its data for a system like Sora. ([View Highlight](https://read.readwise.io/read/01hprqk64x2prc1y7bk30wat7c))
- a breakthrough but to get that kind of quality I imagine the amount of data needed would be astronomical in quantity AND quality. ([View Highlight](https://read.readwise.io/read/01hprqknknmz8zb9tr82ddyasz))
- they have used Unreal Engine to simulate scenarios, which has to be the case tbh for augmentations. ([View Highlight](https://read.readwise.io/read/01hprqm1zy9cp294cf717rz37n))
- Pay 10000 video artists to generate 2 videos per day?? even that seems too small a dataset. ([View Highlight](https://read.readwise.io/read/01hprqmd4bdca7g9e23fcq53tk))
- YouTube-scale amounts of video. Billions of hours. ([View Highlight](https://read.readwise.io/read/01hprqp00hg02mwjwk4xkcr6dt))
- synthetic data ([View Highlight](https://read.readwise.io/read/01hprqpvde2h057rk9bg2ptppa))
- I can say that they did not, unless they farmed it out wholesale. ([View Highlight](https://read.readwise.io/read/01hprqpzk1dxd2sxqaznvn2rr1))
- [
  ](https://www.reddit.com/user/s6x/)
  [s6x](https://www.reddit.com/user/s6x/)
  • [5h ago](https://www.reddit.com/r/MachineLearning/comments/1armmng/comment/kqnc43g/)
  There's lots of ways to do it. My point is that I have been keeping an eye on OAI's careers postings for a long time, as well as generally monitoring the synthetic data space, as it's my realm, and I haven't seen indicators that they were building a group proficient in doing this. ([View Highlight](https://read.readwise.io/read/01hprqqz7mkt05gy70x2kdjzd6))
- vendor specifically in the synthetic data arena. ([View Highlight](https://read.readwise.io/read/01hprqra03fpekwchth76pdjz0))
- scale.ai and Surge ([View Highlight](https://read.readwise.io/read/01hprqs669cgmkevyp34g94ejk))
- On the other hand, if you posted open ai's girl on the train demo video on Instagram literally no one would notice that its ai. Like, no one. ([View Highlight](https://read.readwise.io/read/01hprqw0befak3sq44x9qjw2pq))
- no concept of physics. ([View Highlight](https://read.readwise.io/read/01hprqxd6qcmg6f7brtc7sc221))
- But quite clearly it has learned the 3D world from watching 2D projections of it exclusively, and that's the problem. ([View Highlight](https://read.readwise.io/read/01hprqytjqvm6anqw73ggp4cpz))
- I’m betting OpenAI made advancements with the LongNet architecture ([View Highlight](https://read.readwise.io/read/01hprr24v7d3z8g2gw73rawyhh))
- an internal general model that accelerates development of their projects. ([View Highlight](https://read.readwise.io/read/01hprr4sweec6p9t68980p243p))
- If we were to speculate that they might have an advanced general model that they use to assist with their development it could explain why we see such difference between what apparently Sora can generate and what competing text-to-video models can.
  It is hard to explain based on talent and infrastructure alone. The competing companies are specialized on text-to-video, and yet OpenAI made them completely obsolete. ([View Highlight](https://read.readwise.io/read/01hprr6t1rwfe5hhtbg4d5k01a))
- Who? Runway the biggest I can think of raised$140 million to date and built the initial gen-2 on maybe $45 million raised. 
  Pika has raised $55 million.
  It's entirely possible OpenAI spent over $20 million to train this model. The competitors just don't have the budget. ([View Highlight](https://read.readwise.io/read/01hprr7yc2qyw9t5b22w2cnyeb))
- Google revealed some demos just three weeks ago with Lumiere. ([View Highlight](https://read.readwise.io/read/01hprr8dnr54f9zd9zsv4m3xbv))
- Sora demos look what one might expect generated videos to look 3 to 5 years from now. ([View Highlight](https://read.readwise.io/read/01hprr8yj0sdc4a0c9akfxpnvn))
- [
  ](https://www.reddit.com/user/cobalt1137/)
  [cobalt1137](https://www.reddit.com/user/cobalt1137/)
  • [7h ago](https://www.reddit.com/r/MachineLearning/comments/1armmng/comment/kqmuk56/)
  I think the issue is that we have not seen any text to video model releases from these giant companies (Amazon/Apple/Google/Microsoft etc). So we don't really have a baseline for what's possible with massive amounts of money, researchers, gpus, etc. I bet Google has a model internally that isn't going to be too far behind this. ([View Highlight](https://read.readwise.io/read/01hprr9p2x28xqsbemyrthex7b))
