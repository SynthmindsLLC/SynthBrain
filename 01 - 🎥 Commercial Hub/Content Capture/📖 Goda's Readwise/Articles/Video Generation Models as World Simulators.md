# Video Generation Models as World Simulators

![rw-book-cover](https://images.openai.com/blob/28bcbcb2-563a-432b-bb30-d74f66a087fe/young-tiger.jpg?trim=0%2C0%2C0%2C0&width=1000&quality=80)

## Metadata
- Author: [[openai.com]]
- Full Title: Video Generation Models as World Simulators
- Category: #articles
- URL: https://openai.com/research/video-generation-models-as-world-simulators
- Tags:

## Highlights
- Video generation models as world simulators ([View Highlight](https://read.readwise.io/read/01hpsyxntq9shhd0y2a2feztyt))
- Specifically, we train text-conditional diffusion models jointly on videos and images of variable durations, resolutions and aspect ratios. ([View Highlight](https://read.readwise.io/read/01hprnjfqhzhejsng1beep49wn))
- a transformer architecture that operates on spacetime patches of video and image latent codes. ([View Highlight](https://read.readwise.io/read/01hprnjwftagbb93hn9qk94wr1))
- Sora, is capable of generating a minute of high fidelity video. ([View Highlight](https://read.readwise.io/read/01hprnk77a9m05a4y8jgd5wmr7))
- building general purpose simulators of the physical world. ([View Highlight](https://read.readwise.io/read/01hprnkmbvx6xnzyh12xxxy252))
    - Note: What does this mean?
- qualitative evaluation of Sora’s capabilities and limitations. ([View Highlight](https://read.readwise.io/read/01hprnngpy2vzhdj6rjj07s76g))
- Model and implementation details are not included in this report. ([View Highlight](https://read.readwise.io/read/01hprnmwa4x8t1t4qt6k3pq0p5))
- Much prior work has studied generative modeling of video data using a variety of methods, including recurrent networks,[1](https://openai.com/research/video-generation-models-as-world-simulators#fn-1),[2](https://openai.com/research/video-generation-models-as-world-simulators#fn-2),[3](https://openai.com/research/video-generation-models-as-world-simulators#fn-3) generative adversarial networks,[4](https://openai.com/research/video-generation-models-as-world-simulators#fn-4),[5](https://openai.com/research/video-generation-models-as-world-simulators#fn-5),[6](https://openai.com/research/video-generation-models-as-world-simulators#fn-6),[7](https://openai.com/research/video-generation-models-as-world-simulators#fn-7) autoregressive transformers,[8](https://openai.com/research/video-generation-models-as-world-simulators#fn-8),[9](https://openai.com/research/video-generation-models-as-world-simulators#fn-9) and diffusion models.[10](https://openai.com/research/video-generation-models-as-world-simulators#fn-10),[11](https://openai.com/research/video-generation-models-as-world-simulators#fn-11),[12](https://openai.com/research/video-generation-models-as-world-simulators#fn-12) These works often focus on a narrow category of visual data, on shorter videos, or on videos of a fixed size. ([View Highlight](https://read.readwise.io/read/01hprnphg7scjttevh9hzybw45))
- Sora is a generalist model of visual data—it can generate videos and images spanning diverse durations, aspect ratios and resolutions, up to a full minute of high definition video. ([View Highlight](https://read.readwise.io/read/01hprnpztcssh7nchc2sy7ftgq))
- Whereas LLMs have text tokens, Sora has visual *patches*. ([View Highlight](https://read.readwise.io/read/01hprnsnev4p01zatfsbycxkh3))
- Patches have previously been shown to be an effective representation for models of visual data.[15](https://openai.com/research/video-generation-models-as-world-simulators#fn-15),[16](https://openai.com/research/video-generation-models-as-world-simulators#fn-16),[17](https://openai.com/research/video-generation-models-as-world-simulators#fn-17),[18](https://openai.com/research/video-generation-models-as-world-simulators#fn-18) ([View Highlight](https://read.readwise.io/read/01hprnsz7kkmpksea050g34nbm))
    - Note: Tweet from one of the authors for patches video
- At a high level, we turn videos into patches by first compressing videos into a lower-dimensional latent space,[19](https://openai.com/research/video-generation-models-as-world-simulators#fn-19) and subsequently decomposing the representation into spacetime patches. ([View Highlight](https://read.readwise.io/read/01hprnvgpewtcdth8axxv8j547))
- We train a network that reduces the dimensionality of visual data.[2](https://openai.com/research/video-generation-models-as-world-simulators#fn-20) ([View Highlight](https://read.readwise.io/read/01hprnw0b241a1a7az3wcne3cn))
- We also train a corresponding decoder model that maps generated latents back to pixel space. ([View Highlight](https://read.readwise.io/read/01hprnwrr34xk0sjm0m6nt9q14))
- Our patch-based representation enables Sora to train on videos and images of variable resolutions, durations and aspect ratios. ([View Highlight](https://read.readwise.io/read/01hprny04pwqbm7wtrjr9tw76k))
- At inference time, we can control the size of generated videos by arranging randomly-initialized patches in an appropriately-sized grid. ([View Highlight](https://read.readwise.io/read/01hprnycam1pckss9t6s20ypmf))
- Sora is a diffusion model ([View Highlight](https://read.readwise.io/read/01hprnynz9941h9m7hmys6akmt))
- given input noisy patches (and conditioning information like text prompts), it’s trained to predict the original “clean” patches. ([View Highlight](https://read.readwise.io/read/01hprnz9xdqd59n6m84jhdqk8r))
- Sora is a diffusion *transformer*. ([View Highlight](https://read.readwise.io/read/01hprnzgpr6ek7v1yq2tbe2b2s))
- diffusion transformers scale effectively as video models as well. ([View Highlight](https://read.readwise.io/read/01hprp0c8b8pn48ye5ykgz6adf))
- Sample quality improves markedly as training compute increases. ([View Highlight](https://read.readwise.io/read/01hprp175v1x4byzaeg0c7f145))
- Sora can sample widescreen 1920x1080p videos, vertical 1080x1920 videos and everything inbetween. ([View Highlight](https://read.readwise.io/read/01hprp2yvz8rk87grh3rvh9tdy))
- This lets Sora create content for different devices directly at their native aspect ratios. ([View Highlight](https://read.readwise.io/read/01hprp3bwqkdqd59hx96tg473x))
- It also lets us quickly prototype content at lower sizes before generating at full resolution—all with the same model. ([View Highlight](https://read.readwise.io/read/01hprp3ntvn4byq0bjhrx8k2vh))
- We empirically find that training on videos at their native aspect ratios improves composition and framing. ([View Highlight](https://read.readwise.io/read/01hprp46fe33bjke8r4dn47dtt))
- We compare Sora against a version of our model that crops all training videos to be square, which is common practice when training generative models. ([View Highlight](https://read.readwise.io/read/01hprp4hrv3p96ck6eh1p4kc61))
- Training text-to-video generation systems requires a large amount of videos with corresponding text captions. ([View Highlight](https://read.readwise.io/read/01hprp5q663g75j96pa7vdwtfj))
- We first train a highly descriptive captioner model and then use it to produce text captions for all videos in our training set. ([View Highlight](https://read.readwise.io/read/01hprp66wtsg2vaahea9fqzb7p))
- highly descriptive video captions ([View Highlight](https://read.readwise.io/read/01hprp6tt9px9z7q8gekwa52yv))
- Similar to DALL·E 3, we also leverage GPT to turn short user prompts into longer detailed captions that are sent to the video model. ([View Highlight](https://read.readwise.io/read/01hprp772xeek8wv4z1wv642mp))
    - Note: Super important!
- All of the results above and in our [landing page](https://openai.com/sora) show text-to-video samples. ([View Highlight](https://read.readwise.io/read/01hprpagvbxgzpdgecfd67nt3q))
- Sora can also be prompted with other inputs, such as pre-existing images or video. ([View Highlight](https://read.readwise.io/read/01hprpavbb01mbfd0p136bgj3f))
- creating perfectly looping video, animating static images, extending videos forwards or backwards in time, etc. ([View Highlight](https://read.readwise.io/read/01hprpbcccktkg1yamktddxyqn))
- Monster Illustration in flat design style of a diverse family of monsters. The group includes a furry brown monster, a sleek black monster with antennas, a spotted green monster, and a tiny polka-dotted monster, all interacting in a playful environment. ([View Highlight](https://read.readwise.io/read/01hprpcf795vmtdt2n40jyz815))
    - Note: Animators and illustrators... gone
- Extending generated videos
  Sora is also capable of extending videos, either forward or backward in time. ([View Highlight](https://read.readwise.io/read/01hprpe87prbnm4c2wfndtkkyx))
- each of the four videos starts different from the others, yet all four videos lead to the same ending. ([View Highlight](https://read.readwise.io/read/01hprpfzrew9catpfh6q2ker1y))
- We can use this method to extend a video both forward and backward to produce a seamless infinite loop. ([View Highlight](https://read.readwise.io/read/01hprpgrgk59wkmq6jvybhxe7q))
    - Note: This will be insane for social media
- Diffusion models have enabled a plethora of methods for editing images and videos from text prompts. ([View Highlight](https://read.readwise.io/read/01hprphfyj85fq7gqj3aef0w2v))
- SDEdit,[32](https://openai.com/research/video-generation-models-as-world-simulators#fn-32) to Sora. ([View Highlight](https://read.readwise.io/read/01hprphtdy2kyy9cqgn4v7zyp2))
- We can also use Sora to gradually interpolate between two input videos, creating seamless transitions between videos with entirely different subjects and scene compositions. ([View Highlight](https://read.readwise.io/read/01hprpka7xnzh3smvgkm8j162t))
- In the examples below, the videos in the center interpolate between the corresponding videos on the left and right. ([View Highlight](https://read.readwise.io/read/01hprpkv7xdk8x45ak5wafxjm2))
    - Note: Perfect transitions
- The model can generate images of variable sizes—up to 2048x2048 resolution. 
  ![](https://cdn.openai.com/tmp/s/image_0.png)Close-up portrait shot of a woman in autumn, extreme detail, shallow depth of field ([View Highlight](https://read.readwise.io/read/01hprpprp8mkb5dq2gjzstve6s))
- Emerging simulation capabilities ([View Highlight](https://read.readwise.io/read/01hpt0fjwwtsvxpmkwfxx33cgp))
- We find that video models exhibit a number of interesting emergent capabilities when trained at scale. These capabilities enable Sora to simulate some aspects of people, animals and environments from the physical world. ([View Highlight](https://read.readwise.io/read/01hprpqswjv4rb9dxvdg778eqa))
- These properties emerge without any explicit inductive biases for 3D, objects, etc.—they are purely phenomena of scale. ([View Highlight](https://read.readwise.io/read/01hprpr8711j5g6navq9kq4y7d))
- **3D consistency.** Sora can generate videos with dynamic camera motion. As the camera shifts and rotates, people and scene elements move consistently through three-dimensional space. ([View Highlight](https://read.readwise.io/read/01hprprjf4tjj7mjqdcn1ksaaq))
- We find that Sora is often, though not always, able to effectively model both short- and long-range dependencies. ([View Highlight](https://read.readwise.io/read/01hprpsge1qs5848y51bw31vb1))
- our model can persist people, animals and objects even when they are occluded or leave the frame. Likewise, it can generate multiple shots of the same character in a single sample, maintaining their appearance throughout the video. ([View Highlight](https://read.readwise.io/read/01hprpt0zk77mb7fqwa3x4ce6k))
- **Interacting with the world.** Sora can sometimes simulate actions that affect the state of the world in simple ways. For example, a painter can leave new strokes along a canvas that persist over time, or a man can eat a burger and leave bite marks. ([View Highlight](https://read.readwise.io/read/01hprpvd0nfzkzgg78a1gzw2qa))
- Simulating digital worlds. ([View Highlight](https://read.readwise.io/read/01hpt0k5sk10twawzc8k9655yc))
- Sora can simultaneously control the player in Minecraft with a basic policy while also rendering the world and its dynamics in high fidelity. ([View Highlight](https://read.readwise.io/read/01hprpwbj60m197ze9k8qxe5w7))
- “Minecraft.” ([View Highlight](https://read.readwise.io/read/01hprpwmkt6yvzc3035mrzvt45))
- These capabilities suggest that continued scaling of video models is a promising path towards the development of highly-capable simulators of the physical and digital world, and the objects, animals and people that live within them. ([View Highlight](https://read.readwise.io/read/01hprpx7px3pgx733w5vm93dtv))
    - Note: !!!!!!
- Sora currently exhibits numerous limitations as a simulator. For example, it does not accurately model the physics of many basic interactions, like glass shattering. ([View Highlight](https://read.readwise.io/read/01hprpy2xcx73c08mszga28pbt))
- eating food, do not always yield correct changes in object state. ([View Highlight](https://read.readwise.io/read/01hprpyc2skbxefqtfs5erqsaw))
- We believe the capabilities Sora has today demonstrate that continued scaling of video models is a promising path towards the development of capable simulators of the physical and digital world, and the objects, animals and people that live within them. ([View Highlight](https://read.readwise.io/read/01hprpza9jcbxbb2egmsty0gjy))
    - Note: Repeats!
- Photorealistic video generation with diffusion models. ([View Highlight](https://read.readwise.io/read/01hpsztq67hdb8q9cqn90b8rzj))
## New highlights added March 6, 2024 at 4:11 PM
- We apply the re-captioning technique introduced in DALL·E 3[30](https://openai.com/research/video-generation-models-as-world-simulators#fn-30) to videos. ([View Highlight](https://read.readwise.io/read/01hr4b2ygtt0tw86n9vdnacw0w))
