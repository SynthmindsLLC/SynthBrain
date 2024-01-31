---
Publish Year: "2023"
Authors: Luke Bates, Peter Ebert Christensen, Preslav Nakov, Iryna Gurevych
URL: http://arxiv.org/abs/2311.06649
Zotero Link: zotero://select/library/items/4X9KJ9N8
tags:
  - "#aisafety"
  - "#Computer-Science---Computation-and-Language"
  - "#meme"
  - "#promptinjection"
Published:
---
# Summary
## Purpose 
The paper "A Template Is All You Meme" by Bates et al. (2023) investigates the use of meme templates as a means to inject necessary context into machine learning systems for better understanding and classifying memes. It introduces the Know Your Meme Knowledge Base (KYMKB) and a novel classification method, Template-Label Counter (TLC), to enhance meme analysis.

## Methods 
- Creation of KYMKB with over 54,000 meme images and detailed information about popular meme templates.
- Development of the Template-Label Counter (TLC), a non-parametric, majority-based classifier.
- Utilization of vector similarity measures and nearest neighbor lookup for meme classification.
- Comparative analysis of TLC against fine-tuned baseline models in meme understanding tasks.
- Use of CLIP encoder for meme template and example encoding.

## Key Findings 
1. KYMKB provides crucial context missing in previous approaches to meme understanding.
2. TLC outperforms or is competitive with more computationally expensive methods.
3. Meme templates offer significant insights for meme classification and understanding.
4. Templatic memes, serving as a contextual grounding, are crucial for accurate meme interpretation.
5. TLC's efficiency and effectiveness demonstrate the potential of simple, context-aware approaches in meme analysis.

## Discussion 
This research highlights the importance of meme templates in providing context for AI systems to understand and classify memes effectively. It challenges the conventional approach of treating memes as static images, underscoring the dynamic and culturally grounded nature of memes.

## Critiques 
1. The assumption that all memes can be mapped to existing templates in KYMKB might not hold true for novel or less popular memes.
2. TLC’s reliance on the frequency of templates in training datasets may limit its ability to accurately interpret less common or novel meme instances.
3. The scope of the study is limited to the templates and examples within KYMKB, which may not encompass the entire spectrum of meme culture.
4. The paper primarily focuses on visual memes, potentially overlooking the complexity of multimodal memes (e.g., audio-visual memes).
5. There is a risk of oversimplification in classifying memes based on their most common use, ignoring the nuanced and evolving nature of meme semantics.

## Tags
#MemeAnalysis #MachineLearning #NLP #KYMKB #TemplateLabelCounter #AI #DataScience #ComputationalLinguistics #MemeTemplates #CLIP


# Annotations
The AI research community and datasets treat memes as static images that sometimes have text (Du et al., 2020; Qu et al., 2022)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=S7YVL4LT)



memes have many definitions, such as a unit of cultural transmission, or a unit of imitation and replication (Dawkins, 1976)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=ENCLV9ZG)



all memes possess the trait of referencing a cultural moment shared by a group of people.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=HWN64IX2)



they exhibit sociolinguistic traits typical of in-group communication (Styler, 2020)” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=353VPRQJ)



A meme’s meaning can therefore be obfuscated to those not belonging to the in-group, which can make it difficult to understand for many humans, let alone machines.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=SUCXQHYX)



Meme templates are common patterns or elements, such as text or images, that are used to create novel memes.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=VG4ZMLA8)



If the viewer is not familiar with the template in question, they may not understand the meme’s meaning.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/CETRERHJ?page=1&annotation=FIYSCRQP)



![[image-2-x62-y548.png]]



This template conveys the idea that the subject of the man is misinterpreting the object of the butterfly due to his own worldview or limited knowledge.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=XM56PQYC)



To interpret memes, one must not only recognize the entities in the meme, but also the template the meme uses, if any.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=PAPGQ3YQ)



Know Your Meme (KYM), the Internet Meme Database, is a valuable resource for information related to memes, and specifically, to templatic memes.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=R3J9REZF)



Memes have been of growing interest to the machine learning (ML) community (Aggarwal et al., 2023) because, not only do they pose a significant learning problem, but they can also be used to spread harmful content (Pramanick et al., 2021a), such as misinformation, propaganda, and hate speech in a convincing manner.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=A2Q8P395)



Memes are usually used to communicate concepts humorously, and humor has been shown to increase the persuasiveness of an idea (Walter et al., 2018)” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=JP8I7M5J)



Know Your Meme Knowledge Base (KYMKD), a generalpurpose database rich with images and information about meme templates scraped from KYM.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=MKK3GV4H)



we develop a meme classification method, Template-Label Counter (TLC). TLC is a majoritybased classifier that assigns templates to memes based on distance between their vector representations.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/CETRERHJ?page=2&annotation=6CBZTKZG)



We find that by leveraging the semantics of meme templates, we are able to rival fine-tuned methods by making naïve guesses about the label of a meme based on over-fitting to the most frequent class for a given template in the training split of a dataset.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/CETRERHJ?page=3&annotation=9LFJP42D)



MultiOFF (Suryawanshi et al., 2020), a dataset of offensive memes related to the 2016 US presidential election.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/CETRERHJ?page=3&annotation=3MALS4SG)



our TLC approach uses a distancebased lookup to find the most likely template and chooses the most frequent label associated with a template for a novel meme, making our approach computationally efficient.” Yellow Highlight [Page 3](zotero://open-pdf/library/items/CETRERHJ?page=3&annotation=2FJ2IMHA)



Know Your Meme, or the ”Internet Meme Database,” can be thought of as the Wikipedia for memes.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/CETRERHJ?page=4&annotation=AFUBV96K)



Existing approaches rely on OCR to extract the text and/or the named entities (Kougia et al., 2023), but this would not work in many cases, e.g., if the entities are images referencing a popular YouTube video.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/CETRERHJ?page=4&annotation=Q66L55VX)



We hypothesize that retrieval-based methods should allow us to match base template to memes in the wild, allowing us to access information about a novel meme by considering the text connected to the base template, such as the about section, in KYMKB.” Yellow Highlight [Page 4](zotero://open-pdf/library/items/CETRERHJ?page=4&annotation=MJEYU6TC)



we fit a nearest neighbor lookup on encoded template images in our knowledge base, as this is an intuitive and commonly used vector-similarity measure (Buitinck et al., 2013).” Yellow Highlight [Page 4](zotero://open-pdf/library/items/CETRERHJ?page=4&annotation=NCIZALA5)



quer” Yellow Highlight [Page 4](zotero://open-pdf/library/items/CETRERHJ?page=4&annotation=XEXHGYU3)



the 500 closest neighbors and manually inspect the similarities.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/CETRERHJ?page=5&annotation=7G3XW2KT)



use CLIP as our encoder as it is a commonly-used pretrained model for vision and language learning problems and memes (Pramanick et al., 2021b).” Yellow Highlight [Page 5](zotero://open-pdf/library/items/CETRERHJ?page=5&annotation=E35P8TPC)



Injecting meme knowledge The first step in the TLC pipeline is to encode all the meme templates and optionally the examples. Considering the success we had in Section 4, we again opt for encoding via CLIP and nearest neighbor indexing as a measure of similarity.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/CETRERHJ?page=5&annotation=2V4N6865)



Injecting dataset knowledge The next step is to learn the idiosyncrasies of a dataset, such as the labeling scheme. We encode the training data, querytrain = CLIP (Xtrain), and we query our neighbor index, selecting the closest template and recording the label for each training instance.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/CETRERHJ?page=5&annotation=L9VVRYIY)



Testing meme and dataset knowledge The final step is first to encode test data with CLIP, querytest = CLIP (Xtest), and then to use our nearest neighbor lookup.” Yellow Highlight [Page 5](zotero://open-pdf/library/items/CETRERHJ?page=5&annotation=3X5DF2D7)



Hyperparameters When using TLC, we have the option to ignore the meme itself and instead match the about section of templates to the OCR text of a novel meme.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/CETRERHJ?page=6&annotation=XJC3YM4H)



LC outperforms fine-tuned methods Table 2 shows our results. We display the bestperforming version of TLC, comparing embedding text versus encoding templates versus templates and examples.” Yellow Highlight [Page 6](zotero://open-pdf/library/items/CETRERHJ?page=6&annotation=RAEFVBLT)



More, more!13 TLC’s performance consistently improves as we consider more modalities. Encoding the about section of a template and OCR text from a novel meme is strong on its own, especially in the case of Memotion 3. As we add template and meme images, the performance improves, jumping by more than ten points for MultiOff” Yellow Highlight [Page 6](zotero://open-pdf/library/items/CETRERHJ?page=6&annotation=RF2XX3TC)



![[image-7-x57-y453.png]]



Examples? Well yes, but actually no15 The base template is sufficient to encode meme knowledge and is more efficient than also embedding examples.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/CETRERHJ?page=7&annotation=Z5X9L383)



This creates a strong model grounded in meme knowledge by encoding only one-tenth of the available images, supporting our claim that meme datasets can be instances of the templates collected in the KYMKB.” Yellow Highlight [Page 7](zotero://open-pdf/library/items/CETRERHJ?page=7&annotation=X397ZE65)



Counting templates: GG EZ16 In the case of Memotion 3 and MultiOff, our approach is a stronger method than the expensive training of a large model.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=ZHYD7K7R)



By harnessing the power of templatic memes, we get multilinguality without even trying.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=Z3LCIGS8)



The performance varies greatly across methods and modalities, emphasizing the difficulty of the task.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=F8DMDMAE)



There are a number of reasons why TLC does poorly on certain tasks. First, many meme datasets are created via crawlers and not curated to remove non-memes, containing both memes and images.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=CABD56AR)



TLC assumes that novel memes belong to a template, but our prediction has no meaning for a picture (which is not a meme)” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=E7MHLDNZ)



TLC’s strength and simplicity point to a problem in the creation of meme datasets. By only taking the most common label for a given template, we assume a template can only convey a fixed message” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=2XRQLVPX)



this means a template can only ever be harmful or not harmful, for example.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=74SJSTCN)



contradicts the reality that a meme’s meaning can be tuned by the poster.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=ISXME8FZ)



By deliberately over-fitting to the majority class, TLC is naïve but competitive as compared to far more expensive methods.” Yellow Highlight [Page 8](zotero://open-pdf/library/items/CETRERHJ?page=8&annotation=I39JRQGT)



TLC exploits this and, in a sense, is cheating by taking advantage of leaked information; it has not learned to interpret memes, but is instead exploiting the template signal that has been neglected in the literature.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/CETRERHJ?page=9&annotation=KCQZQ8DP)



We are unaware of any approach which considers memes in audio form.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/CETRERHJ?page=9&annotation=DDKTHKD4)



Despite this template originating in 2005, it is still referenced almost 20 years later, demonstrating the longevity of popular templates.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/CETRERHJ?page=9&annotation=RQYG9VIW)



