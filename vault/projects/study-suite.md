---
slug: "study-suite"
url: "https://devpost.com/software/study-suite"
title: "Study Suite"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 524
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/transcript_audio"
---

# Study Suite

> Research shows students learn 20% more content through the active recall method. Our project converts lectures into quizzes that help student retain and understand the information they learn best.

[Devpost](https://devpost.com/software/study-suite) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[runtime_tool_creation]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[transcript_audio]]
  <sub>weak: structured_db</sub>

**stack** database, fetch.ai, llm, model, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for study suite

## Body

Inspiration Inspired by a shared vision for transformative education, our team is embarking on a project to enhance learning from recorded lectures. We believe that integrating interactive quizzes will foster active participation, deepen understanding, and improve retention for students. Through this initiative, we aim to revolutionize the learning experience by empowering students to engage with the material in a more dynamic and effective way. What it does Through a series of meticulously designed agents, we facilitate every step of the process. Initially, our system effortlessly transforms video content into detailed lecture transcripts, ensuring accessibility and clarity. Next, these transcripts are seamlessly converted into interactive quizzes, engaging students in active learning. Our quiz auto-grader feature streamlines assessment, providing instant feedback and allowing students to revisit incorrect responses for further understanding. Moreover, our system offers valuable suggestions, pinpointing timestamps for review based on quiz mistakes, and recommending related lectures to deepen comprehension. By integrating these functionalities, we aim to optimize learning outcomes and empower students to navigate their educational pursuits with confidence and efficiency. How we built it Agents is the whole idea of the project, so we needed a way to create responsive agents,and make them communicate with each other. Our project was constructed with a sophisticated blend of cutting-edge technologies. Leveraging Fetch.ai 's framework, uagents, we orchestrated a network of AI agents to execute various tasks seamlessly. For the conversion of video to text transcripts, we harnessed the power of advanced APIs dedicated to this purpose, ensuring accuracy and efficiency in the process. Additionally, we integrated Language Model APIs, such as LLM's, to dynamically generate quizzes from the extracted transcripts, enabling personalized and contextually relevant assessment content. Through the strategic amalgamation of these tools and frameworks, we engineered a robust and adaptable system that streamlines the creation of interactive learning materials while harnessing the capabilities of artificial intelligence to enhance the educational experience for students. Challenges we ran into Undertanding the different ways agents, protocols, and delta v communicate is our main struggle. We needed to understand the concepts from the network including Context, Protocol, Mailbox, and other things. Accomplishments that we're proud of We're proud to have created an end-to-end pipeline using AI agents, leveraging cutting-edge technologies to enhance the learning experience. Our seamless integration of advanced tools transforms video content into detailed transcripts and generates personalized quizzes, resulting in a dynamic and engaging platform. This accomplishment showcases our commitment to innovation and our dedication to empowering students with effective educational solutions. What we learned Throughout this project, we've learned to harness Fetch.ai's uagents for building interactive AI agents and effectively utilize the latest text generation APIs. This journey has honed our skills in deploying uagents for seamless communication and collaboration while also mastering the capabilities of text generation APIs to dynamically create learning materials. This experience has broadened our technical expertise and highlighted the transformative potential of AI in education. What's next for Study Suite Different format of questions like - Truth or False and even open ended questions add more agents to increase the functionality of the agents. Integrating wispr with the app to make a just voice integrated agent. <div