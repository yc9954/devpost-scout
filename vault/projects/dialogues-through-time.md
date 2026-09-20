---
slug: "dialogues-through-time"
url: "https://devpost.com/software/dialogues-through-time"
title: "Dialogues Through Time"
hackathon: "Microsoft AI Classroom Hackathon"
organization: "Microsoft"
winner: true
words: 873
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "user/developer"
---

# Dialogues Through Time

> An immersive educational game that reimagines learning history through interactive AI conversations with historical figures.

[Devpost](https://devpost.com/software/dialogues-through-time) · hackathon [[Microsoft AI Classroom Hackathon]]

## Facets

**mechanism** [[runtime_tool_creation]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** azure, c#, llm, python, redis, unity

## How they structured the write-up

- abstract
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dialogues through time

## Body

Gameplay Snapshot Project architecture diagram PS: To all newcomers exploring this project, we’re no longer hosting the project due to the associated costs. However, we’d love for you to check out our demo video to see it in action! Abstract Embark on a groundbreaking journey through history with "Dialogues Through Time." This innovative educational game combines immersive storytelling, interactive AI-driven dialogues, and stunning visuals to offer a unique learning experience. Inspiration History is such an interesting field. But it unfortunately does not get the love that it deserves most of the time. One can not directly experience historical events, which can make learning it more difficult. We thought about how one doesn't have to dread learning history when they could just talk to the person, whom they are learning about. Given the theme of the hackathon, we decided to proceed with the idea of transforming the learning experience of history from something dull into something fun and engaging. Kryštof has extensive expertise in AI application development, while Bennett brings experience as a skilled 3D artist and game developer to the table. Seeing how well our skills complement one another for what is needed for this project, we started work right away once we put our ideas for the project down on paper on a chilly Thursday evening after our university lecture. What it does The player is introduced to a multidimensional entity that seeks to understand humanity. The entity sends the user in time with the goal to learn from prominent historical figures whose legacies impacted our current world greatly, albeit in different ways. The player then shares his/her findings with the entity at the end, which will test if he/she learned well. How we built it At the core of Dialogues Through Time is our LLM Constraining System. This innovative technology allows us to guide the AI with a json tree, ensuring it behaves according to predefined parameters while retaining the dynamic nature of Large Language Models. This ensures a consistent and relevant educational experience. During the development of our LLM Constraining system we came across the ability of AI to generate these constraints procedurally itself. For instance, the knowledge tests in dialogues through time are based on previous interactions and are dynamically created by the AI, offering a personalized learning journey for each player. This system is not only useful for our education game but also has extreme potential for the creation of AI procedurally generated experiences that are constrained to specific predefined rules. Our game harnesses the power of GPT-4, deployed via Azure OpenAI Service, for complex tasks, and GPT-3.5-turbo for lighter operations. This integration ensures a smooth, intelligent, and responsive gaming experience. The backbone of our game is a FastAPI backend, hosted on Azure WebApp Service. This setup offers robust integration, easy CI/CD setup linked with GitHub, facilitating rapid, efficient development cycles. To manage game states, dialogues, and chat histories, we've utilized Azure Redis Data Service. Its lightweight nature, coupled with Azure's powerful hosting solutions, ensures a seamless experience for numerous players simultaneously. Challenges we ran into One of the challenges we faced was maintaining the reliability of AI responses while adhering to established rules and staying in character for an optimal educational experience. Striking the right balance was crucial to avoid the AI behaving in unwanted ways or losing track of its original goal. Our LLM Constraining made working with the large language model much easier, guiding it to the optimal learning experience. Another challenge involved offering variations in experiences while simultaneously preserving the general structure and direction of the conversation. Fortunately, this approach proved effective in achieving the desired outcomes. Additionally, connecting the frontend with the backend posed a hurdle that we successfully overcame. The solution involved implementing the FastAPI Python module, Azure OpenAI deployment and integrating the Azure Redis data service to ensure seamless communication and functionality between the two components. Accomplishments that we're proud of Despite the educational game being still being in its early stages of development, we are extremely happy with the effectiveness of the constraining system. Furthermore, we are pleased that the envisioned aesthetics were successfully achieved, and the models and animations were completed ahead of the deadline. What we learned I personally learned that while it is important to work together with someone to complete such a project, it is equally important with who you team up with. Teaming up with Kryštof really allowed me to continue with my frontend development with a peace of mind, knowing that the backend is well take care of, which it was. -Bennett I've picked up a lot about what the Azure Cloud brings to the table for development – it really speeds up and adds a safety net to the whole development process and makes iteration fast. -Kryštof What's next for Dialogues Through Time We think that the most logical path would be to develop this game further by adding more characters, improving the design and adding more interactivity, in order to achieve the goal of building a revolutionary history learning platform. We are already thinking of creative ways to make the history learning even more creative and fun, for example by guiding Leonardo Da Vinci to draw a new painting with you. <div