---
Publish Year: "2023"
Authors: Marc Schmitt, Ivan Flechais
URL: http://arxiv.org/abs/2310.13715
Zotero Link: zotero://select/library/items/76YQ4J4Y
tags:
  - "#Computer-Science---Computers-and-Society"
  - "#Computer-Science---Cryptography-and-Security"
  - "#Computer-Science---Human-Computer-Interaction"
Published: 2024-04-16
---
# Summary
## Purpose 
This paper by Marc Schmitt and Ivan Flechais investigates the transformative role of [[Generative AI]] in [[Social Engineering (SE)]] and [[Phishing]] attacks. It aims to deepen understanding of the risks, human implications, and countermeasures associated with AI-driven SE attacks, contributing to more secure human-computer interactions.

## Methods 
- Systematic literature review of social engineering and AI capabilities.
- Analysis of AI technologies, focusing on Generative AI.
- Identification of three primary pillars exacerbating the impact of SE attacks: Realistic Content Creation, Advanced Targeting and Personalization, and Automated Attack Infrastructure.
- Development of a conceptual framework: the "Generative AI Social Engineering Framework."
- Application of the framework to investigate the impact of generative AI on phishing attacks and identify countermeasures.

## Key Findings 
1. Generative AI significantly amplifies the effectiveness of SE attacks through realistic content creation, including text, images, voice, and videos.
2. Advanced targeting and personalization capabilities of AI enable highly tailored phishing campaigns, increasing their success rate.
3. The use of AI in automated attack infrastructures allows large-scale, sophisticated phishing campaigns with minimal human involvement.
4. Generative AI poses a dual threat: while it can be used for defensive purposes, its misuse for malicious activities is a significant concern.
5. Current countermeasures, particularly user awareness and education, are inadequate against the evolving sophistication of AI-driven attacks.

## Discussion 
This research is crucial in understanding the growing threat posed by AI in cybersecurity. It highlights the urgent need for advanced defensive strategies and technologies to combat these AI-enhanced threats.

## Critiques 
1. The paper could explore more in-depth the ethical implications of Generative AI in cybersecurity.
2. A more detailed discussion on the technical aspects of AI-driven attacks and their detection might strengthen the research.
3. While the framework developed is comprehensive, real-world application and validation studies could further solidify its effectiveness.

## Tags
#GenerativeAI #SocialEngineering #Phishing #Cybersecurity #AIethics #AIthreats.


# Annotations
As AI systems become increasingly adept at mimicking human communication and trust signals, they present a new frontier for social engineering and phishing attacks.” Yellow Highlight [Page 1](zotero://open-pdf/library/items/DMA2ACXS?page=1&annotation=76IMPFLM)



AI/ML can be misused to automate and personalize phishing attacks, generate persuasive content that mimics legitimate communication, and evade detection by traditional security measures [3,6,7].” Yellow Highlight [Page 2](zotero://open-pdf/library/items/DMA2ACXS?page=2&annotation=TSBDK3TQ)



With the help of AI-enabled autonomous agents [11], it is possible to automate parts – potentially even the entire lifecycle – of a social engineering attack” Yellow Highlight [Page 2](zotero://open-pdf/library/items/DMA2ACXS?page=2&annotation=VACNPCBY)



fully trained SE models can theoretically learn from each attack and gradually improve their success rate. The emergence of advanced open-source generative AI tools represents significant progress in machine learning and AI, particularly in their capacity to produce sophisticated text, voice, graphics, and video content.” Yellow Highlight [Page 2](zotero://open-pdf/library/items/DMA2ACXS?page=2&annotation=AGTHBHXL)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-3-x63-y582.png]]



Deception plays a central role in both social engineering and phishing tactics. In both cases, the attacker aims to manipulate or trick their target into taking certain actions or revealing confidential information by posing as a trustworthy entity. Social engineering refers to the activity of manipulating people into performing actions or divulging confidential information, usually through deceptive means” Yellow Highlight [Page 4](zotero://open-pdf/library/items/DMA2ACXS?page=4&annotation=9KM7H6PB)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-4-x58-y469.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-4-x60-y143.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-5-x43-y591.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-5-x133-y186.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-7-x58-y152.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-8-x59-y384.png]]



Text: It can craft convincing emails, text messages, or social media posts that appear to be written by humans.  These messages may be customized to target specific individuals or organizations.  • Images: It can create realistic images, such as fake IDs, official logos, or manipulated photographs, to enhance the credibility of phishing or social engineering attacks.  • Voice: It can produce realistic voice recordings or engage in voice phishing (vishing) by impersonating trusted individuals or organizations over the phone.  • Videos: It can create highly realistic deepfake videos that manipulate the appearance and voice of real individuals. These deepfakes can be used to spread misinformation, impersonate executives or public figures, and deceive targets into taking specific actions [26].” Yellow Highlight [Page 8](zotero://open-pdf/library/items/DMA2ACXS?page=8&annotation=TSB25UK7)



Impersonation: By creating a near-flawless visual and auditory imitation of a trusted individual - such as colleagues, friends, or family members - malicious actors can convince recipients to carry out tasks or disclose sensitive information.  • Bypassing Biometrics: Some security systems that rely on facial or voice recognition could be tricked by a well-crafted deepfake, thereby granting unauthorized access.  • Ransom Campaigns: Threat actors could create scandalous or compromising deepfakes of individuals and then threaten to release them unless a ransom is paid [27].  • Disinformation: On a broader scale, deepfakes can spread misinformation or propaganda that appears genuine, thus causing panic, influencing public opinion, or even affecting stock market behavior.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/DMA2ACXS?page=9&annotation=C9YADCUE)



LLMs can craft highly convincing and personalized phishing emails that are contextually relevant to the recipient, vastly increasing the success rate of such attacks. This is of course also true for all other text-based communication channels, such as SMS or Social Media Chats [17]. Instead of static phishing messages, cybercriminals could leverage LLMs to conduct real-time interactions with victims, adapting the conversation dynamically to manipulate the target more effectively.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/DMA2ACXS?page=9&annotation=RZ5FPQYR)



Generative AI has the potential to start an era of hyper-personalized and highly targeted attacks. This is because of the introduced ability to generate realistic content (pretexting), but also due to the potential of AI to analyze existing information (reconnaissance), which allows attackers to customize their malicious intents according to the online presence, behavior, and affiliations of the targets. In the final step, this information can be successfully leveraged during the execution stage.” Yellow Highlight [Page 9](zotero://open-pdf/library/items/DMA2ACXS?page=9&annotation=QNL8X872)



AI can help to automate the creation and dissemination of deceptive content, thereby enabling attackers to carry out large-scale phishing campaigns or social engineering attacks with minimal effort” Yellow Highlight [Page 10](zotero://open-pdf/library/items/DMA2ACXS?page=10&annotation=INQXYQ5J)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-11-x69-y301.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-12-x67-y394.png]]



On the highest level we can distinguish between technical countermeasures, which are largely based on AI/ML [31] and cryptography, and human-centric countermeasures, which is largely user education [32].” Yellow Highlight [Page 13](zotero://open-pdf/library/items/DMA2ACXS?page=13&annotation=T463S52U)



Labeling the end-user as the problem is not just an oversimplification, but a dangerous perspective. The implication is that users should be blamed for not being smart/aware enough and remediate this through security awareness, education and training (SAET), however this approach is insufficient and flawed for a number of reasons.” Yellow Highlight [Page 13](zotero://open-pdf/library/items/DMA2ACXS?page=13&annotation=AZ6BEPVZ)



The potential scale and automation of malicious attacks will mean that individuals will need constant and near-perfect levels of awareness to reach a satisfactory balance between protecting themselves from deception while maintaining trust in communication channels” Yellow Highlight [Page 13](zotero://open-pdf/library/items/DMA2ACXS?page=13&annotation=XFUYRKJ4)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-14-x53-y483.png]]



Routine tasks, like checking emails, seldom involve critical thinking, and when emotions—especially fear—are triggered, rational decision-making becomes challenging. Current solutions like anomaly and spam detection AI are somewhat effective, but they fall short against targeted spear phishing and state-sponsored attacks.” Yellow Highlight [Page 14](zotero://open-pdf/library/items/DMA2ACXS?page=14&annotation=59VKK7ZU)



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-14-x56-y140.png]]



![[Synthbrain/03 - 🔬 R&D/🦾 AI/_Research Notes/attachments/schmittDigitalDeceptionGenerative2023/image-15-x56-y513.png]]



