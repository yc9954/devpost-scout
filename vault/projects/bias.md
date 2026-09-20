---
slug: "bias"
url: "https://devpost.com/software/bias"
title: "BIAS"
hackathon: "Pinecone Hackathon: Jumpstart Real-World AI Applications"
organization: "Pinecone"
winner: true
words: 1222
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# BIAS

> Arguments extraction, analysis & more

[Devpost](https://devpost.com/software/bias) · hackathon [[Pinecone Hackathon- Jumpstart Real-World AI Applications]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, cohere, firebase, node.js, openai, pinecone, raiden.ai, vercel, zapier

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next
- credits

## Body

Dashboard view Project view Exploring analyzed arguments Browsing generated arguments clusters Deep search view Conversation view Debate simulation view Data export email PDF report generation email Inspiration The BIAS project stems from a belief in better-informed, potent and healthier debate and decision-making contexts, for everybody What it does Navigate the flow of information on issues you are interested in, with the help of AI : Automated analysis, extraction of arguments and counter-arguments from any source Support for webpages, documents, audio, video, youtube Browse analyzed and extracted arguments using a smooth and intuitive interface Arguments clustering for better discovery Source-backed conversational features to enquire more Agent-based debate simulations in a chatbot-like interface Data exports for further usage and analysis Detailed PDF report generations on issues of interest How we built it We used the following tools to build the BIAS projects: RAIDEN AI We signed up for this hackaton as a startup to put our infrastructure, RAIDEN AI , to use in a real-life application, and potentially generate interest in our platform from users (and investors) RAIDEN AI is used: To process, index and retrieve sources, in a project-scoped environment, with all the required features out-the-box (feature analysis, embeddings generations Pinecone indexing, ...), accessible with a single API call and no-config, in addition to automating adding sources from search queries in a single request To instantly deploy automation pipelines to production. Here we used 5 pipelines, all of which make use of LLMs : analyze-sources : extract arguments & counter-arguments related to given statement, from a source simulate-debate : agent-based debate simulation suggest-searches : on project creation, suggest search queries to be used for source retrieval cluster-title : generate titles for clusters of arguments report-generation : write a source-backed report related to the given statement PINECONE Pinecone is used to pretty much connect everything: Sources content blocks are indexed (using generated embeddings) alongside analyzed features as metadata, and project-scoped with namespaces. This allows for: Semantic search across projects Source-backed conversational chatbots Generation of a bibliography section when generating project reports Arguments & counter-arguments that are extracted from the source analysis pipeline are indexed in Pinecone as well. This allows for: Deep project search to be performed on atomic arguments in addition to source texts Relevant list for each argument : on the BIAS web platform, tapping an argument retrieves and displays list of closest arguments cards (both opposing and agreeing arguments) Generating clusters of arguments for a better exploration of topics Debate simulation : agents can make use of Pinecone as a memory bank to generate pertinent debate replies OPENAI We used: text-ada-002 to generate embeddings before storing them in Pinecone, for: sources text blocks analyzed arguments gpt-3.5-turbo-0613 in all pipelines to generate texts and objects We highlight the usage of the new functions addition, which makes workflows simply perfect for further automation. COHERE We use Cohere's classification feature in order to analyze each argument, in order to attribute it one of 3 labels: Optimistic Tone Pessimistic Tone Neutral Tone We believe the argument Tone feature will be useful further down the line in analyzing/shaping conversations related to pertinent topics, as the sentiment/tone of the message is as important as the reasoning dimension. ZAPIER Zapier is used to email users at the completion of 2 tasks, for which we believe users would like to preserve a copy: Data export - a CSV file Report generation - a PDF file This is accomplished in 3 steps : On processing completion : upload file to storage Catch Hook in Webhooks by Zapier : call webhook on upload completion, object with target user email and email content Send Outbound Email in Email by Zapier : configured on data from previous step We highlight the attachment feature of Send Outbound Email in Email by Zapier which lessens the time required by lengthy configurations for email attachments : A simple url string is supplied instead (the signed url of the data file uploaded on our storage), and the Zap takes care of the rest AWS Amazon Textract is used a one of the document extraction engines. It is especially useful in cases where documents have: Scanned formats; i.e. user take pictures of their notes and use them as source Non-standard structure; i.e. multi-column structures that do not follow a strict template VERCEL Using Vercel to deploy everything frontend related, whether in this project or any other: Instant deployment of our webapp, written in SvelteKit Instant subdomain configuration : bias.raiden.ai Challenges we ran into Conceptualizing the web platform interface : Required multiple design attempts and restarting from scratch before figuring out what to use Systems adapted to long processing times : As the processing tasks can be lengthy regarding the features we wanted to implement, there was a need to come up with models that emphasize intermittent updates; i.e. in Debate Simulation, instead of running the entire simulation and then displaying results, had to remodel the entire process, opted for a chatbot-like interface with step by step updates the same approach would be useful in future contexts where deep, nested processing is required by automations. i.e. prioritize the use of streams instead of responses on full completions Debate simulation : We needed to have opposing agents debate a given statement, using the analyzed arguments as context. Required lengthy testing of numerous sets of prompts to reach an acceptable model. Note : Challenges typically faced by teams according to Discord messages seemed to be related to document processing, extraction and storing/indexing in Pinecone. Using RAIDEN AI took care of all that without configuration needed. Accomplishments that we're proud of Built & deployed everything that was set to be accomplished in the BIAS project, both in backend and frontend, strictly within the 1 week hackaton. What we learned New tools to integrate in upcoming projects Approaches to modelling logical reasonning methods in a LLM context Better prompt techniques, especially in relation the GPT functions feature Insights on AI and development from discussing with other hackaton participants What's next for the BIAS project: Potential usage in education platforms: A start in responding to the discruption and vacuum created in education by recent AI developments. A new type of newsfeed: Can be deployed either as: an independent new type of platform, in which case, lengthy processes will be continuously running in the background and results presented as a news feed adapted to the users' areas of interest an integration with social media platforms (i.e. an augmentation of features such as twitter's community notes) a chatbot tailored to users' interests for RAIDEN AI: The BIAS project highlights promises outlined by the RAIDEN AI infrastructure in terms of speeding up the development of AI apps, through a zero-config Knowledge Base Layer and a very powerful API-first Automation Layer, to build + deploy + scale AI apps instantly We are looking for partnerships and investments for RAIDEN AI , reach out! If you happen to be in contact with the openAI team, please help reach back on quota increases requests we filled numerous times Credits Made for the BIAS BY RAIDEN AI team Try It Out You can try it out at bias.raiden.ai note : Login might be temporarily disabled to balance out incoming requests and credits usage. If it is the case, just let me know so i can open logins for you :) <div