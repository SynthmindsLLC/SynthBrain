---
Publish Year: "2023"
Authors: Cassandra Bird, Daniel Williamson, Sabina Leonelli
URL: http://arxiv.org/abs/2309.05529
Zotero Link: zotero://select/library/items/N33ASPG9
tags:
  - "#Mathematics---Statistics-Theory"
  - computerscience
  - ArtificialIntelligence
  - Ethics
Published:
---
# Summary
## Purpose
The paper addresses the accountability and ethical considerations in AI system development, focusing on the use of statistical foundations to enhance decision-making transparency and understand the uncertainty in AI outputs. It demonstrates these ideas using models advising the UK government during the COVID-19 Omicron variant spread.

## Methods
- Analysis of large statistical models (e.g., Deep Gaussian Processes, Neural Networks) in critical decision-making scenario.
- Discussion on the difficulty in defining AI ethics and the effectiveness of ethical codes of conduct.
- Examination of the Posterior Belief Assessment (PBA) method to manage decision-critical statements in AI system.
- Review of 'M-open' approaches in AI for uncertainty quantification.
- Case study: Application of PBA to model combinations for COVID-19 Omicron variant spread in the UK.

## Key Findings
1. Importance of understanding the statistical underpinnings of AI models to interpret their outputs for ethical decision-making.
2. Significance of modeller’s intentions and judgments in AI system use and the need for their clear communication to users.
3. Challenges in achieving ethical AI due to the complexity of models and variance in interpretations among users and modeller.
4. Adoption of Posterior Belief Assessment (PBA) to reduce model opacity and increase accountabilit.
5. Case study insights: Effective communication and synthesis of complex AI models for government advisory during the pandemic.

## Discussion
The paper’s exploration of ethical AI centers on clarity in modelling choices and their implications, highlighting the importance of modeller’s responsibility in AI's ethical application. The case study provides a practical example of applying these principles in a real-world scenario, emphasizing the role of transparent communication in high-stakes decision-making processes.

## Critiques
1. The paper could benefit from a broader range of real-world applications beyond the COVID-19 case study to generalize its findings.
2. There is a need for more explicit guidelines on implementing the PBA method in diverse AI applications.
3. Further exploration of the challenges in balancing statistical rigor with ethical considerations in AI development.

## Tags
#EthicalAI #PosteriorBeliefAssessment #AIUncertainty #AIEthics #AIAccountability #ModelSynthesis #GeneralisedBayesianInference #COVID19Modelling.


# Annotations
In discussing the effectiveness of ethical codes of conduct in this setting, Whittaker et al. (2018) acknowledge the risk that they ‘deflect criticism by acknowledging that problems exist, without ceding any power to regulate or transform the way technology is developed and applied’.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=ITAZ4YF9)



we find that there exists few spaces in which issues that are advanced in a technical sense, whilst also being significant from an ethical perspective, can be effectively tackled in an interdisciplinary manner” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=QVNEXSCZ)



Acknowledging modelling choices and their underpinning foundations should play a key role in shaping the outputs of AI and the meaning that can subsequently be attributed to those outputs. This, in turn, dictates how the outputs of AI can or should be used to support decision making. The statistical foundations refer to the meaning of uncertainty, directly establishing how it can be quantified and used in practice.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=MZUK4ZQ2)



the modeller themselves, whatever the scenario, must understand and be able to communicate the foundational implications of their modelling judgements” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=C4BP2KRW)



Whilst it’s impossible to directly ascribe precise meaning to either set of probabilities without knowing the context in which the modeller intended them, broadly, the former represent (estimates of) ‘generative’ probabilities that describe the relative frequency of the different classes amongst individuals with identical features, and the latter represent the subjective uncertainty of the modeller” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=9JFIWKLU)



we argue that when we consider what makes the use of AI ethical, an important component must be the acknowledgment that action informed by the uncertainty produced by a modeller (via an AI system), requires the adoption of that uncertainty by the user” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=SWQDT4NE)



the modeller themselves must understand the foundational implications of their modelling judgements and be able to clearly communicate them to a user, thus enabling them to make the decision” Yellow Highlight [Page 2](zotero://open-pdf/library/items/I42BEZVC?page=2&annotation=VPTTVCL4)



On the meaning of uncertainty for ethical AI: philosophy and practice A PREPRINT as to whether this is uncertainty they wish to act on.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=SEUUEL93)



we proceed from our own foundational position, the subjectivist position outlined by De Finetti (1974): that ‘true randomness’ need not exist and that probability is a measure of individual belief. From here we can examine belief ownership methodologies for complex AI systems and address this particular facet of the ethical use of AI.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=BQKI2XA6)



the work of imbuing meaning and ownership for AI is required, whatever the worldview.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=GCZ7M8AZ)



Subjectivism and Bayesian inference are natural partners. The subjective Bayesian account holding that if the statistical model and the prior represent your initial beliefs before seeing the data, your beliefs are represented by the posterior distribution having seen it. In fact, the traditional Bayesian approach represents an impossibly high bar for belief ownership, particularly for complex AI systems.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=FD2JDHDS)



Danaher (2016) defines opacity as the issue of AI systems working ‘in ways that are inaccessible or opaque to human reasoning and understanding’2. From a foundational point of view, this opacity renders the traditional subjective Bayesian account of inference impossible from a practical perspective and calls into question the way in which (and the extent to which) responsibility and accountability should be related to the modellers” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=53ZY69AV)



[[Generalised Bayesian Inference]] (Bissiri et al. 2016) seeks to efficiently provide uncertainty quantification for AI systems by treating Bayes as an optimisation problem. Specifically, posterior uncertainty is derived by optimising a loss function that includes a divergence between the model class and the DGP.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=T8TXEPM9)



[[Posterior Belief Assessment]] (PBA, Williamson & Goldstein (2015)), as a means to belief ownership for decision-critical statements made by AI systems” Yellow Highlight [Page 3](zotero://open-pdf/library/items/I42BEZVC?page=3&annotation=VMFJMH9S)



PBAs do not require that the modeller believes the raw results produced by the systems themselves. What the modeller needs to believe is their own second-order judgements updated upon observing these results. This helps to clarify who bears responsibility for different aspects of the model, and how accountability may be apportioned if outputs turn out to be problematic or unreliable.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/I42BEZVC?page=7&annotation=UKI77JR5)



There is an element of trust whenever information is passed between these groups, as well as a responsibility to process said information from one’s respective position of expertise and (ideally) a sense of reciprocal accountability between the different groups of experts involved.” Yellow Highlight [Page 10](zotero://open-pdf/library/items/I42BEZVC?page=10&annotation=T3LVCDPS)



Early December 2021 was a time of great uncertainty in regards to the Omicron variant. Uncertainty in X must capture this uncertainty whilst capturing the modeller’s judgements as to how the specific geography and infrastructure of England is affecting the spread of the virus. Two regions which are geographically distant may be well-connected through transport infrastructure whilst two regions that border each other may have populous cities that are, in fact, very far apart. Aspects such as this will, in turn, affect how likely it is that members of the public live in one region, but travel to another for work and/or leisure on a day-to-day basis.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/I42BEZVC?page=11&annotation=TMQLVDUT)



The modeller recalled that at this time, London was considered to be the epicentre of the Omicron outbreak and was thus believed to be ‘ahead of the curve’. In addition to this, the modeller felt that relative to the other regions, they were most confident in making their judgements in regards to how London was ‘connected’ to the remaining eight regions. They therefore wished to specify their judgements regarding London first, so that they had the option to frame the remaining judgements around the situation there. The rest of the running order was determined by considering which region the modeller felt they would be ready to judge next, given the regions they had specified beliefs on up to that point.” Yellow Highlight [Page 11](zotero://open-pdf/library/items/I42BEZVC?page=11&annotation=I6G7MNF9)



A belief separation is an orthogonality judgement between two quantities given a third.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/I42BEZVC?page=14&annotation=GCNPDQ6F)



typically grounded in scientific reasoning, a technical assumption or interpretation is often likely to have wider-ranging repercussions, even if these are not immediately apparent to the modeller; and second, because within a decision-making process, technical judgements are intertwined with a wider cast of judgements and interpretation by a variety of experts, each of which will have their own respective skills, goals, background knowledge and related ethical concerns (see also Leonelli & Beaulieu (2021), 84ff and 110ff; Bezuidenhout & Ratti (2021)).” Yellow Highlight [Page 16](zotero://open-pdf/library/items/I42BEZVC?page=16&annotation=84L8BDLM)



The idea that accountability cannot be attributed to the modeller due to the complexities of AI systems hinges on the assumption that one cannot be responsible for a system that they do not understand, or a system that may result in unanticipated outcomes 5 6. However, we argue that accountability follows naturally from the modeller being a key contributor to the development of AI systems, and thereby bearing some responsibility as to their functioning.” Yellow Highlight [Page 17](zotero://open-pdf/library/items/I42BEZVC?page=17&annotation=QHJ69EQX)



Responsible practice does not mean that a modeller has the ability to fully anticipate the consequences of deploying a system, which is never feasible for any technical innovation; rather, it means being reflexive and as open as possible about the influence that modellers did have on the development of such systems and the ways in which AI systems remain uncertain upon subsequent uses 7” Yellow Highlight [Page 17](zotero://open-pdf/library/items/I42BEZVC?page=17&annotation=D6J4CSC8)



By requiring judgements a priori (i.e. before the outputs of the AI models are observed and a decision is made), PBAs prevent the modeller from altering their judgements depending on whether or not they wish to be perceived as being in (dis)agreement with the models (an issue which is referred to in the elicitation literature as hindsight bias (Kadane & Wolfson 1998))” Yellow Highlight [Page 17](zotero://open-pdf/library/items/I42BEZVC?page=17&annotation=3T7KY6Y6)



a modeller may not (strictly speaking) be liable for damages if the use of an algorithm commercialised by their company goes wrong, but they may be asked to intervene and help to rectify the situation via their technical expertise. The first instance considers accountability in a legal sense, whilst the latter treats it more as an ethical principle” Yellow Highlight [Page 17](zotero://open-pdf/library/items/I42BEZVC?page=17&annotation=MCHQGSTK)



he act of making the judgements required to complete a PBA demand that the modellers actively preempt and prepare for the instance in which they may be called upon for such insight in future” Yellow Highlight [Page 17](zotero://open-pdf/library/items/I42BEZVC?page=17&annotation=ADMP8KSD)



