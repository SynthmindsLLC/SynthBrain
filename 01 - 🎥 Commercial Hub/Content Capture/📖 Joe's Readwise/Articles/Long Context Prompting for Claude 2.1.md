# Long Context Prompting for Claude 2.1

![rw-book-cover](https://www-images.anthropic.com/production/images/Neuroscience_Social.png?w=1200&h=630&q=82&auto=format&fit=crop&dm=1701835335&s=bd32b759166bf1515b633748ae36a18d)

## Metadata
- Author: [[Anthropic]]
- Date: 2023-12-06
- Full Title: Long Context Prompting for Claude 2.1
- Category: #articles
- Summary: Claude 2.1 is a state-of-the-art model with a 200K token context window, and it performs well on real-world retrieval tasks across longer contexts. However, the model can be reluctant to answer questions based on an individual sentence in a document if that sentence is out of place. By using a minor prompt update, such as adding a sentence to direct the model to look for relevant sentences first, Claude's performance significantly improves. This approach also enhances Claude's performance on single sentence answers within context. The team behind Claude is continuously training and improving the model based on community feedback and experimentation.
- URL: https://www.anthropic.com/index/claude-2-1-prompting

## Highlights
- Claude 2.1 is trained on a mix of data aimed at reducing inaccuracies. This includes not answering a question based on a document if it doesn’t contain enough information to justify that answer. We believe that, either as a result of general or task-specific data aimed at reducing such inaccuracies, the model is less likely to answer questions based on an out of place sentence embedded in a broader context. ([View Highlight](https://read.readwise.io/read/01hh0zerbr7jmp8w21gf6nhqsc))
- Claude 2.1 is much more reluctant to answer when a sentence seems out of place in a longer context, and is more likely to claim it cannot answer based on the context given. ([View Highlight](https://read.readwise.io/read/01hh0zfh0e69qk4k0emmkje0dk))
- When running the same evaluation internally, **adding just one sentence to the prompt resulted in near complete fidelity throughout Claude 2.1’s 200K context window**. ([View Highlight](https://read.readwise.io/read/01hh0zg2n1ztq023aprw9t8csj))
- *Here is the most relevant sentence in the context:”* ([View Highlight](https://read.readwise.io/read/01hh0zga4djhs3kk9f3ff8mkkg))
- Essentially, by directing the model to look for relevant sentences first, the prompt overrides Claude’s reluctance to answer based on a single sentence, especially one that appears out of place in a longer document. ([View Highlight](https://read.readwise.io/read/01hh0zgq427z4xpjmgng7tfymr))
- the revised prompt achieves 90-95% accuracy ([View Highlight](https://read.readwise.io/read/01hh0zh1dknjm6r9qgqmn3kvfw))
