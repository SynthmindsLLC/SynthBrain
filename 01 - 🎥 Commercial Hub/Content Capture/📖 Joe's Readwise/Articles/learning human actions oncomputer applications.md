# learning human actions oncomputer applications

![rw-book-cover](https://www.rabbit.tech/static/og/1200-630.png?0)

## Metadata
- Author: [[rabbit.tech]]
- Date: 2023-12-03
- Full Title: learning human actions oncomputer applications
- Category: #articles
- Summary: Learning human actions on computer applications is a complex task that involves understanding and replicating user interactions. The goal is to create intelligent algorithms that can perform actions reliably and quickly. This research combines neural and symbolic techniques to create scalable and explainable learning agents. The approach, called LAM, aims to generalize actions across different applications and solve complex problems. The researchers hope that their work will contribute to shaping infrastructure and benefiting society.
- URL: https://www.rabbit.tech/research

## Highlights
- Our key observation is that the **inherent structures of human-computer****interactions differ from natural language or vision.** The applications areexpressed in a form that is more structured than a rasterized image and more verboseand noisy than a sentence or a paragraph. The characteristics we desire from a LAM arealso different from a foundation model that understands language or vision alone: whilewe may want an intelligent chatbot to be creative, LAM-learned actions on applicationsshould be **highly regular, minimalistic** (per Occam's razor), **stable,** and **explainable.** ([View Highlight](https://read.readwise.io/read/01hktgvnknn4fp1nfak52ge9gs))
- there is a body of literature in the field of web automation and roboticprocess automation that involves the use of symbolic algorithms [2], [7], [19]. Thesemethods have shown promising results in narrow domains and have been implemented invarious products, ranging from productivity software [9] to computer-aided design [20]. ([View Highlight](https://read.readwise.io/read/01hktgy1w1zysvn6v7h7vbzm6n))
- combining a neuralcomponent and a symbolic component, a nascent field in its early stages of development:
  • We can define and model complex application structures,beyond simple token sequences, from first principles. They arecompatible with both a symbolic algorithm and a neuralnetwork, where actions and action sequences are first-classcitizens.
  • We can achieve explainability, fast inference, and simplicity of aheuristic (which performs actions to satisfy user intentions) byleveraging a symbolic algorithm [2].
  • We can benefit from the language, vision, and zero-shotreasoning capabilities of a neural network [10], which improveas more data becomes available [3]. ([View Highlight](https://read.readwise.io/read/01hktgyb5xj9njjg4gfh309jq1))
- LAM's modeling approach is rooted in imitation, or **learning by demonstration:** ([View Highlight](https://read.readwise.io/read/01hktgys8v0r0vjb8spy2e8d21))
- observes a human using the interface and aims to reliably replicate the process, even ifthe interface is presented differently or slightly changed. ([View Highlight](https://read.readwise.io/read/01hktgz0tnm3mh19qbarw5143f))
- LAM's "recipe" is more observable. ([View Highlight](https://read.readwise.io/read/01hktgz785wde2y5nhx7r27wem))
- This means that once the demonstration isprovided, the synthesized routine runs directly on the target application without the needfor a busy loop of "observation" or "thoughts," and any technically trained human shouldbe able to inspect the "recipe" and reason about its inner workings. ([View Highlight](https://read.readwise.io/read/01hktgzr9txy1tqhgevyzjm1b0))
- creates a "conceptual blueprint" of theunderlying service provided by the application ([View Highlight](https://read.readwise.io/read/01hkth00z5spcpq365tgjnpwdb))
- the PL/FM community has focusedon symbolic techniques — solver technologies that rely on logical principles of induction,deduction, and heuristic search. ([View Highlight](https://read.readwise.io/read/01hkth24es8yyqnax89yv6nz0a))
- they suffer from a scalability limit ([View Highlight](https://read.readwise.io/read/01hkth2a1vatzkj03q59f9h2pb))
- recent innovations in the LM community are grounded in machine learning andneural techniques: while highly scalable, they suffer from a lack of explainability and comewith no guarantees of the output produced. ([View Highlight](https://read.readwise.io/read/01hkth2k2m7sk7p7vnmh2nk06h))
