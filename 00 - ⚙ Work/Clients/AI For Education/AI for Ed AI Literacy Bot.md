### Project Scope
- **Objective**: Develop an interactive, chapter-based AI literacy education bot.
- **Target Audience**: Students aged 7-18, with tailored experiences for two age groups: 7-12 (family-assisted) and 13-18 (independent or teacher-assisted).
- **Platform**: Web-based solution, built and hosted on Vercel/Replit.
- **Key Features**: Interactive learning modules, voice-to-text and text-to-voice capabilities, data privacy adherence.

### Deliverables
1. **Functional AI Education Bot**:
   - Interactive, tailored learning experiences.
   - Chapter-based structure covering different AI literacy skills/topics.

2. **Hosting and Deployment Setup**:
   - Setup on Vercel/Replit, ensuring scalability and performance for high user traffic.
   - Use the Claude API 

3. **Documentation and Training Materials**:
   - User guides for different age groups.
   - Technical documentation for future maintenance and updates.

### Milestones and Timeline
1. **Conceptualization and Design (January - February)**:
   - Define detailed functionalities and user journey.
   - Complete initial design mock-ups and bot architecture.

2. **Development (March - Mid)**:
   - Develop core functionalities and user interfaces.
   - Finalize curriculum
   - Create Prompts

3. **Testing (Mid March-April)**:
   - Conduct internal and user acceptance testing.
   - Refine and debug based on feedback.

4. **Deployment and Launch (April 19th)**:
   - Final deployment and go-live on AI Literacy Day.

### Budget

Initial Server costs; Jan/Feb - zero.
Setup servers in march to have one month of resolving any issues This makes for approx 2 month of running at scale 
- 2 x $4k = $8k Plus $13-$17k Total budget: $21-$26K ND Costs Then ~$4k monthly running costs.
### Risks and Mitigation Strategies
- **Technical Challenges**: Regular reviews and testing to ensure quality.
- **User Engagement**: Iterative testing with target groups to refine user experience.

Some initial thoughts:

- I would not self host any LLM - inviting too many problems IMO
- LlMA needs to be trained on your own dataset - again, the massive problems this is inviting, you need really big money and time to do this properly.

What I meant, was what we do in app dev world is we

- vectorize data - v01 of app - raw, regular data augmented retrieval - this is alpha app
- have a "training period" where SMEs go QA system and vote for good questions - v02- this beta app

1.- have a small, friendly set of users/SMEs now go again in system and Supervote answers 2- setup classifiers that can aid in the filtration of the above data What this does

1. Supervoted answers now get saved in a "master" datasource
2. classifiers will filter data, if no answer found in master, it waterfalls into v02 of datasource

if that fails, then you pull data from v01 of datasourc

3. if all three fail, 1) ask for clarification or 2) have a specialized prompt - e.g. ProfSynapseHelperAgent that talks to an LLM

Now this is ready for release:

- release app that pulls ONLY from vectorstore - no hallucinations
- you can have a an agent that can monitor realtime interactions - users that consistently go past 2nd datasource either 1) AgentHelper steps in and/or 2) it gets flagged so a teacher/instructor can help user in realtime.

So, you finetune you AI Application overall, not the model. In above scenario, it allows teams like you guys to start with a low cost. Once data is ready for preview, scaling up on platforms like ND is just a matter of planing 1-2 months ahead. The helper agent needs to contextually switch between 2-3 scenarios (user needs guidance on how to ask questions in the given context, or user needs to be flagged)