---
slug: "chatedu-mt379l"
url: "https://devpost.com/software/chatedu-mt379l"
title: "ChatEDU"
hackathon: "Microsoft Generative AI Hackathon"
organization: "Microsoft"
winner: true
words: 1261
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# ChatEDU

> Copilot for students that learns and works with them, not for them.

[Devpost](https://devpost.com/software/chatedu-mt379l) · hackathon [[Microsoft Generative AI Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** azure, nextjs, openai, react

## How they structured the write-up

- inspiration
- what is chatedu
- technical architecture
- potential impact
- next steps

## Body

Welcome to ChatEDU Home Page Subject Landing Page Knowledge Graphs Model the Interconnectedness of Topics Multimodal Knowledge Files are Analyzed with Azure AI to Build Knowledge Graphs Knowledge Files Update the Knowledge Graphs and can be Viewed In in the App Learning Agents Quiz Students on their Knowledge Students can Upload Images for Explanations Learning Agents Provide Image Responses Agents Provide Hints on Difficult Questions Tasks are Summarized after Completion ChatEDU: A Second Brain for Students Inspiration Four Undergraduates Exploring the Educational Potential of Generative AI Background Jason Hedman Computer Science and Applied Math Web Developer Vasco Singh Computer Science and Applied Math Web Developer JP Higgins Computer Science and Education Prompt Engineer Jake Underwood Computer Science, Data Science, Engineering Science, and Engineering Management Product Manager We are four computer science undergraduates from Vanderbilt University. Over the last year, our team has explored the educational applications of generative AI while taking courses at Vanderbilt’s Data Science Institute and engaging with its Initiative on the Future of Learning & Generative AI . Our Vision From our experience, students primarily use generative AI to automate tasks such as completing homework or writing essays. We’ve identified inherent limitations in this approach: Automating assignments circumvents the learning process, resulting in knowledge gaps Generative models lack contextual understanding of a student's curriculum or learning progress Siloed chat interactions fail to maintain a student's personalized knowledge profile, which is crucial for tailoring guidance We envision a future where students push beyond automation and utilize a generative AI as a copilot that works and learns with them, not for them . What is ChatEDU Overview ChatEDU is a multimodal educational tool that leverages generative AI to create a second brain for students. Knowledge Graphs: structured models of academic subjects that enable exploration of interconnected topics Knowledge Profiles: dynamic records of individual learning data, including progress and strengths, tailored to Knowledge Graph structures Task-Based Learning Agents: intelligent agents that guide students through their prompted learning objectives Interactive Learning Pathways: multimodal sessions crafted by Learning Agents, integrating text, audio, and images, and personalized in real-time to each student’s Knowledge Profile By continually refining its understanding of the student's knowledge, ChatEDU enhances its effectiveness over time, offering a revolutionary approach to personalized, multimodal education. Knowledge Graphs In ChatEDU, Knowledge Graphs are structured models of academic subjects where nodes represent topics and edges map their dependencies and connections. These graphs form the foundation for crafting personalized Knowledge Profiles and enable our Learning Agents to navigate interconnected topics, guiding students toward their learning objectives. Multimodal Knowledge Files Students upload Knowledge Files that are analyzed to extract topics and connections and update the Knowledge Graph. These files can be plain text, images, videos, or PDFs. We then use Azure Video Indexer, Azure Document Intelligence, and GPT 4 Vision to determine the sentiment of the media. Task-Based Learning Agents Students then prompt our Task-Based Learning Agents with a learning objective, such as understanding a topic better or solving a problem. The agent then traverses the relevant knowledge graph, identifies the path to achieving the objective, and guides the student through a learning session to achieve their objective. Interactive Learning Pathways Interactive Learning Pathways combine text, audio, and images to create a multimodal learning experience. Learning Agents guide students through these pathways customized to each student's unique Knowledge Profile. As students explore the Learning Pathway, the Agent engages them by asking questions, explaining concepts, and providing relevant examples. These pathways adapt to the student's Knowledge Profile changes, ensuring personalized, efficient, and impactful learning experiences. Dynamic Knowledge Profiles After each learning session, the Learning Agent analyzes the student’s comprehension, assessing their understanding of each topic. This data forms the basis of the student's Knowledge Profile , which captures their progress, strengths, and knowledge gaps. As a result, future interactions with the student are tailored to their individual understanding, providing targeted guidance and support. Summary: Adaptive Second Brain for Students ChatEDU serves as a Second Brain for students by providing personalized, interactive learning experiences. Students upload Knowledge Files (lectures, notes, assignments) as videos, images, PDFs, or plain text We analyze the files with Azure AI services to extract relevant topics and connections, which are added to a Knowledge Graph Students then prompt Task-Based Learning Agents with learning objectives, such as preparing for an exam or completing a problem-set Agents identify the relevant components of the Knowledge Graph and create an Interactive Learning Pathway Students ask and answer questions, receive instruction, and progressively work toward their learning objectives Agents analyze and assess the student's progress, strengths, and areas for improvement, creating a Dynamic Knowledge Profile With continued use, the system refines its understanding of the student's knowledge, improving its effectiveness over time. Technical Architecture Microsoft Services OpenAI GPT-4 Vision: generate knowledge graphs, task plans, learning assessments and analysis, image descriptions, and interactive chat experiences Azure Cosmos PostgreSQL: store knowledge graphs, knowledge profiles, learning objectives, and more Azure AI Document Intelligence: extract text and images from PDFs Azure Video Indexer : extract transcripts, keywords, topics, and sentiment from user-uploaded videos Azure Blob Storage : store user-uploaded videos, images, and PDFs Azure AD: authenticate users with Microsoft and other OAuth providers Azure Static Web Apps: host and serve the front-end and API routes Extra Services React: component library for creating stateful, flexible user interfaces Next.js: web framework for server-side rendering of pages and creation of API routes Vercel AI SDK: modular react hooks for offering rich chat experiences Potential Impact Education A recent study by IDC, commissioned by Microsoft , underscores the transformative role of AI in higher education. It reveals that nearly all (99.4%) of the 509 U.S. higher education institutions surveyed believe AI will be crucial to their competitiveness over the next three years. ChatEDU will enhance student competency by tailoring learning experiences to their unique needs, ensuring mastery of concepts, and adapting to their evolving understanding. We plan to pilot an enterprise version for higher-ed institutions, offering insights into their students' diverse learning needs and providing an engaging, digital-native supplement to in-class learning, making education more interactive and personalized. AI Community ChatEDU is pioneering the creation of knowledge graphs for academic subjects, a concept that has been extensively researched in higher education but has not yet been implemented. Large language models make this vision a reality. By transforming unstructured educational materials into structured, interconnected knowledge graphs, we aim to push the boundaries of educational methodologies. Beyond the Target Community Knowledge Profiles can incredibly benefit students as they transition into their careers. The comprehensive data on their skills and knowledge can aid in onboarding into new companies by providing a clear picture of their strengths and areas for growth. Furthermore, these profiles can guide the development of new skills and help students explore practical applications of their education in real-world scenarios. Next Steps Implementation in Classrooms We are extending our collaboration with Vanderbilt's Data Science Institute and its Initiative on the Future of Learning & Generative AI to beta-test our platform in multiple classrooms. Additionally, we are working with Vanderbilt's renowned Peabody College of Education and Human Development to ensure our product aligns with modern educational practices and policies. Technical Improvements Our hackathon work will lay the framework for our grand vision of creating an educational copilot that improves learning outcomes for all. We are exploring graph databases such as Neo4j to develop more effective knowledge graphs. These enable us to add semantic meaning to edges and optimize the traversals of our Learning Agents. Additionally, we are experimenting with Autogen to add further structure to our multi-agent system. <div