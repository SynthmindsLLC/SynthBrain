---
Publish Year: "2023"
Authors: Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe
URL: http://arxiv.org/abs/2305.20050
Zotero Link: zotero://select/library/items/LA7EQLSH
tags:
  - "#Computer-Science---Artificial-Intelligence"
  - "#Computer-Science---Computation-and-Language"
  - "#Computer-Science---Machine-Learning"
Published:
---
# Summary
## Purpose
- The research was initiated to address the challenge of training reliable reward models for AI systems, which is a significant issue in the field of Artificial Intelligence. The purpose of the study was to compare the effectiveness of outcome supervision and process supervision in training reward models and to explore the benefits of process supervision for AI alignment and interpretable reasoning.

## Methods
- Training reward models using outcome supervision (ORMs) and process supervision (PRMs).
- Utilizing human feedback to label the correctness of each step in model-generated solutions.
- Implementing active learning to improve data efficiency of process supervision.
- Evaluating models on the MATH dataset and a held-out set of STEM questions from various exams.

## Key Findings
- Process supervision can train more reliable reward models than outcome supervision.
- A large reward model can approximate human supervision for smaller models and facilitate large-scale data collection ablations.
- Active learning leads to a 2.6× improvement in the data efficiency of process supervision.
- Process supervision outperforms outcome supervision in terms of performance and AI alignment, encouraging models to follow a human-endorsed process.

## Discussion
The discussion in the research article highlights the significance of the findings and their potential impact on Artificial Intelligence and Machine Learning. It suggests that process supervision offers more precise feedback and is more interpretable, which is beneficial for AI alignment. The study also indicates that process supervision incurs a negative alignment tax, potentially leading to its increased adoption due to its ability to produce more reliable and aligned AI systems.

## Critiques
Upon evaluating the research, some critiques include:
    - The dependency on human data-labelers for process supervision, which may not be scalable or cost-effective in all scenarios.
    - The generalizability of the findings may be limited, as the study focuses on specific types of problems (e.g., MATH dataset, STEM questions) and may not apply to all domains of AI.
    - The study does not explore the long-term effects of process supervision on AI behavior and whether it could lead to unintended consequences over time.

## Tags
- #Computer-Science---Artificial-Intelligence
- #Computer-Science---Computation-and-Language
- #Computer-Science---Machine-Learning
- #AI-Alignment
- #Reward-Modeling
- #Process-Supervision
- #Outcome-Supervision
- #Active-Learning

# Annotations
One effective method involves training reward models to discriminate between desirable and undesirable outputs. The reward model can then be used in a reinforcement learning pipeline (Ziegler et al., 2019; Stiennon et al., 2020; Nakano et al., 2021; Ouyang et al., 2022) or to perform search via rejection sampling (Nichols et al., 2020; Shen et al., 2021; Cobbe et al., 2021). While these techniques are useful, the resulting system is only as reliable as the reward model itself.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=G5DJFPYE)



In closely related work, Uesato et al. (2022) describe two distinct methods for training reward models: outcome supervision and process supervision.  Outcome-supervised reward models (ORMs) are trained using only the final result of the model’s chain-of-thought, while process-supervised reward models (PRMs) receive feedback for each step in the chain-of-thought.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=8H6PSLS2)



There are compelling reasons to favor process supervision. It provides more precise feedback, since it specifies the exact location of any errors that occur. It also has several advantages relevant to AI alignment: it is easier for humans to interpret, and it more directly rewards models for following a human-endorsed chain-ofthought. Within the domain of logical reasoning, models trained with outcome supervision regularly use incorrect reasoning to reach the correct final answer” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=728Z4U48)



we use a more capable base model, we use significantly more human feedback, and we train and test on the more challenging MATH dataset (Hendrycks et al., 2021).” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=XD53ZFCK)



We show that process supervision can train much more reliable reward models than outcome supervision.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=4QV8KSJX)



We show that a large reward model can reliably approximate human supervision for smaller reward models, and that it can be used to efficiently conduct large-scale data collection ablations.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=SX5K2XCP)



We show that active learning leads to a 2.6× improvement in the data efficiency of process supervision.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/KS5MWP68?page=2&annotation=6M7RPT32)



Outcome supervision can be provided without humans, since all problems in the MATH dataset have automatically checkable answers. In contrast, there is no simple way to automate process supervision. We therefore rely on human data-labelers to provide process supervision, specifically by labelling the correctness of each step in model-generated solutions.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KS5MWP68?page=3&annotation=XLVY6QHV)



In order to remove our dependence on costly human feedback, we use a large-scale model to supervise small-scale model training. This setup enables us to conduct several important ablations that would otherwise be infeasible.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KS5MWP68?page=3&annotation=TLSX9GH8)



At each model scale, we use a single fixed model to generate all solutions. We call this model the generator. We do not attempt to improve the generator with reinforcement learning (RL).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KS5MWP68?page=3&annotation=VPI6DJZT)



All large-scale models are finetuned from the base GPT-4 model (OpenAI, 2023).  This model has been pretrained solely to predict the next token; it has not been pretrained with any Reinforcement Learning from Human Feedback (RLHF) (Christiano et al., 2017).” Yellow Highlight [Page 3](zotero://open-pdf/library/items/KS5MWP68?page=3&annotation=L7DLQ65Q)



To collect process supervision data, we present human data-labelers with stepby-step solutions to MATH problems sampled by the large-scale generator.  Their task is to assign each step in the solution a label of positive, negative, or neutral,” Yellow Highlight [Page 4](zotero://open-pdf/library/items/KS5MWP68?page=4&annotation=TWCJI9AD)



we choose to surface convincing wrong-answer solutions. We use the term convincing to refer to solutions that are rated highly by our current best PRM, and we use wrong-answer to refer to solutions that reach an incorrect final answer.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KS5MWP68?page=5&annotation=2XWZCZSE)



We expect to gain more information from labeling convincing wrong-answer solutions, since we know the PRM is mistaken about at least one step in each such solution.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KS5MWP68?page=5&annotation=3FUFDDEP)



At test time, we use the ORM’s prediction at the final token as the overall score for the solution. We note the automatic grading used to determine ORM targets is not perfectly reliable: false positives solutions that reach the correct answer with incorrect reasoning will be misgraded.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KS5MWP68?page=5&annotation=S49Q3HC7)



We train PRMs to predict the correctness of each step after the last token in each step.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/KS5MWP68?page=5&annotation=AZ7GKILQ)



we define the PRM score for a solution to be the probability that every step is correct under the PRM. We implement this as the product of the correctness probabilities for each step.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KS5MWP68?page=6&annotation=8BTP9G5Z)



When we provide process supervision, we deliberately choose to supervise only up to the first incorrect step. This makes the comparison between outcome and process supervision more straightforward. For correct solutions, both methods provide the same information, namely that every step is correct. For incorrect solutions, both methods reveal the existence of at least one mistake, and process supervision additionally reveals the precise location of that mistake.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/KS5MWP68?page=6&annotation=GVDZBEG5)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/lightmanLetVerifyStep2023/image-7-x153-y451.png]]



While the ORM performs slightly better than the majority voting baseline, the PRM strongly outperforms both. Not only does the PRM reach higher performance for all values of N, but the performance gap widens as N increases.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/KS5MWP68?page=7&annotation=WZ82HV74)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/lightmanLetVerifyStep2023/image-8-x128-y461.png]]



We experimented with using RM-weighted voting (Li et al., 2022; Uesato et al., 2022) to combine the benefits of the PRM and majority voting, but this did not noticeably improve performance.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/KS5MWP68?page=8&annotation=KW6TV2TE)



We see that process supervision significantly outperforms both forms of outcome supervision at all data collection scales. In Figure 4b, we evaluate the best reward model from each series by its best-of-N performance across different values of N. We see that using PRMlarge for outcome supervision is noticeably more effective than final-answer checking. This can be explained by the fact that PRMlarge provides better supervision for solutions that reach the correct final answer using incorrect reasoning.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/KS5MWP68?page=9&annotation=T5R66N5K)



![[🧠 SynthBrain/03 - 🔬 R&D/🦾 AI/Research Notes/attachments/lightmanLetVerifyStep2023/image-10-x129-y540.png]]



To get some measure of out-of-distribution generalization, we evaluate our largescale ORM and PRM on a held-out set of 224 STEM questions, pulled from the most recent AP Physics, AP Calculus, AP Chemistry, AMC10, and AMC12 exams. Since these tests were released after the pre-training dataset was compiled, we can have high confidence that the model has not seen these problems. We report the best-of-100 performance of the ORM, PRM and majority voting in Table 1. We observe results similar to those in Section 3: the PRM outperforms both the ORM and majority voting. This shows us that the PRM can tolerate a modest amount of distribution shift and that its strong performance holds up” Yellow Highlight [Page 10](zotero://open-pdf/library/items/KS5MWP68?page=10&annotation=4X8GVCXC)



Process supervision has several advantages over outcome supervision related to AI alignment. Process supervision is more likely to produce interpretable reasoning, since it encourages models to follow a process endorsed by humans.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/KS5MWP68?page=11&annotation=35HE6CW8)



outcome supervision is harder to scrutinize, and the preferences conveyed are less precise. In the worst case, the use of outcomes as an imperfect proxy could lead to models that become misaligned after learning to exploit the reward signal (Uesato et al., 2022; Cotra, 2022; Everitt et al., 2017).” Yellow Highlight [Page 11](zotero://open-pdf/library/items/KS5MWP68?page=11&annotation=87ZCVF22)



any alignment tax may hinder the adoption of alignment methods, due to pressure to deploy the most capable model. Our results show that process supervision in fact incurs a negative alignment tax. This could lead to increased adoption of process supervision, which we believe would have positive alignment side-effects” Yellow Highlight [Page 11](zotero://open-pdf/library/items/KS5MWP68?page=11&annotation=2X9BTYW9)



The data scaling trend in Figure 4a suggests that a small amount of process supervision and a large amount of outcome supervision do in fact lead to similar performance, consistent with the results from Uesato et al. (2022). The trend also shows that process supervision beats outcome supervision when scaled up, even when judged based solely on outcomes.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/KS5MWP68?page=12&annotation=BQYM3587)



Lewkowycz et al. (2022) showed that finetuning models on a large corpus of technical content led to significantly improved performance on MATH.” Yellow Highlight [Page 12](zotero://open-pdf/library/items/KS5MWP68?page=12&annotation=9IZXGBJ6)



Wei et al. (2022) and Nye et al. (2021) demonstrate the importance of explicitly performing intermediate reasoning steps via a chain of thought or a scratchpad in order to solve tasks that require multi-step reasoning. Kojima et al. (2022) show that models are able to perform this behavior zero-shot, conditioned only on a simple prompt.” Yellow Highlight [Page 13](zotero://open-pdf/library/items/KS5MWP68?page=13&annotation=RDB6GBFB)



