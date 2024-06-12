# AutoGen Update: Complex Tasks and Agents

![rw-book-cover](https://i.ytimg.com/vi/KuX_dkqr7UY/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGE4gXihlMA8=&rs=AOn4CLAgKMn8jX-Z4DPP4Gn3uZLc2LzssA)

## Metadata
- Author: [[Microsoft Research]]
- Date: 2024-06-04
- Full Title: AutoGen Update: Complex Tasks and Agents
- Category: #articles
- Summary: The text discusses using multi-agent workflows to complete complex tasks efficiently. Researchers have made progress in achieving state-of-the-art performance by employing a team of four agents. They are developing a platform called AutoGen to facilitate this approach and are aiming to introduce new agents that can self-improve and handle more complex scenarios.
- URL: https://youtube.com/watch?v=KuX_dkqr7UY&si=VBu6y7jmWwwB3yqp

## Highlights
- if we take a look at  the following example from the GAIA benchmark   for General AI Assistants, it reads, “How many  nonindigenous crocodiles were found in Florida   from the years 2000 through 2020?” Well, to solve  this task, we might begin by performing a search  
  and discovering that the U.S. Geological Survey  maintains an online database for nonindigenous   aquatic species. If we access that resource,  we can form an appropriate query, and we'll get   back results for two separate species. If we open  the collection reports for each of those species,   we'll find that in one instance, five crocodiles  were encountered, and in the other, just a single   crocodile was encountered, giving a total of  six separate encounters during those years. So  
  this is an example of a complex task, and it has  certain characteristics of tasks of this nature,   which is that it benefits strongly from planning,  acting, observing, and reflecting over multiple   steps, where those steps are doing more than just  generating tokens. ([View Highlight](https://read.readwise.io/read/01j04pb6mk1vq0rgqhz6kpr64n))
- we're betting on using   multi-agent workflows as the vehicle to get us  there. ([View Highlight](https://read.readwise.io/read/01j04pc98afc41hm9y0zsbgvfe))
- agents  are a very, very powerful abstraction over things   like task decomposition, specialization, tool use,  etc. Really, you think about which roles you need   on your team, and you put together your team of  agents, and you get them to talk to one another, ([View Highlight](https://read.readwise.io/read/01j04pd3686psqzdkbe10s7pn1))
- we are   producing a platform called AutoGen, which is open  source and available on GitHub. And I encourage   you to check this out at the link below. ([View Highlight](https://read.readwise.io/read/01j04pdgd5dpgk9wtq6dhheqv0))
- It consists of  a general assistant, a computer terminal that can  
  run code or execute programs, a web server that  can browse the internet, and an orchestrator to,   sort of, organize and oversee their work. ([View Highlight](https://read.readwise.io/read/01j04pedvz87rf8rwd7nfg5yxd))
- we are able to more than double the   performance on the hardest set of questions, the  Level 3 questions, which the authors of that work  
  describe as questions for a perfect general  assistant, requiring to take arbitrarily long   sequences of actions ([View Highlight](https://read.readwise.io/read/01j04ph3xms16hcqbvvskx59ph))
- So this is the loop or the plan that they  are following. So it begins with the question   or the prompt, and then we produce a ledger,  which is like a working memory that consists of  
  given or verified facts; facts that we need to  look up, for example, on the internet; facts that   we need to derive, perhaps through computation;  and educated guesses. ([View Highlight](https://read.readwise.io/read/01j04pj1bcmp0zajs6r62kn6dq))
- give the language models space to speculate   in a constrained environment without some of the  downstream negative effects of hallucination. So   once we have that ledger, we assign the tasks to  the independent agents, and then we go into this   inner loop, where we ask first, are we done? If  not, well, are we still making progress? As long  
  as we're making progress, we'll go ahead and we'll  delegate the next step to the next agent. But   if we're not making progress, we'll note that  down. We might still delegate one other step,   but if that stall occurs for three rounds, then  we will actually go back, update the ledger ([View Highlight](https://read.readwise.io/read/01j04pk6ffm2n7rwwmqnda9snq))
- come up with a new set of assignments for the  agents, and then start over. ([View Highlight](https://read.readwise.io/read/01j04pkb6gx199vn4ahx2nv1cq))
