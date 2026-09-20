---
slug: "txt2bot"
url: "https://devpost.com/software/txt2bot"
title: "txt2bot"
hackathon: "Wix Make-A-SaaS Hackathon"
organization: "Wix"
winner: true
words: 904
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# txt2bot

> txt2bot is an easy-to-use customer support platform that provides business owners with a plethora of tools to streamline support such as an advanced chatbot, AI-assisted FAQ system, and chat analytics

[Devpost](https://devpost.com/software/txt2bot) · hackathon [[Wix Make-A-SaaS Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[civic_government]]
**user** [[small_business]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** amazon-web-services, aws-lambda, gpt3.5-turbo, openai, textract, velo, wix, wix-crm, wix-data, wix-media-manager

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for txt2bot

## Body

Inspiration Chatbots are a prominent feature of many popular websites ranging from governments to startups. Ideally, knowledge-based chatbots should save users time and companies money as users get faster responses and companies need fewer support resources. In practice, however, chatbots have often proven to be mediocre at best, spitting out irrelevant responses or shackling users to a fixed conversation flow and failing to address their issue. Furthermore, they are usually only within reach of large enterprises and corporations, leaving out small enterprises. This situation inspired our product, txt2bot, which combines a GPT-powered, fully configurable knowledge-based chatbot with other powerful features such as natural language triggers, FAQ organisation, algorithm-based semantic search and user analytics , all in a very simple user interface, putting a powerful support system within reach of small businesses . What it does txt2bot includes the following powerful features: Knowledge Base & Index - a one-stop hub for business owners to import and upload documents which they want our system to process. Uploaded information can be utilised by every module of txt2bot. Configurable Knowledge-based Chatbot - combining both rule-based and natural language chatbot technology, txt2bot's chatbot can be embedded into business owners' websites to provide swift support. Chatbot Triggers - business owners can setup triggers using natural language to perform actions such as sending an email, forwarding correspondence or making HTTP requests for added flexibility when rules match a user's message. User Feedback - business owners and their users can provide feedback to the chatbot to help it improve over time. Frequently Asked Questions Builder - business owners can migrate their FAQ pages to txt2bot to take advantage of our knowledge index and search features. Chatbot conversations provide insight into the questions which users are actually answering, helping business owners address users' concerns better. Analytics & Insights - business owners can view analyses of user-chatbot interactions and better tune their knowledge base and support system to help users out. How we built it Built on Editor X and Wix's robust global cloud infrastructure, our app uses: Wix's Content Manager and wix-data APIs for efficient storage of business owners' knowledge and user messages Wix Realtime APIs to enable high-performance chat functionality Wix Secrets APIs to securely store API and session secrets to improve security Wix Web Modules to seamlessly connect frontend and backend code Wix HTTP Functions to connect with external services Wix Datasets and wix-data to rapidly build data manipulation user interfaces with little code Wix Storage to track temporary user sessions On top of this, we also use the following external APIs and services: Amazon Web Services AWS Textract - to extract written text from user-uploaded documents (functionality is work in progress) AWS Lambda - connecting to AWS Textract AWS EC2 - running gpt4all as an alternative to using the OpenAI API (work in progress) OpenAI GPT 3.5 Turbo - our search function selects relevant portions of the knowledge base and feeds these into GPT 3.5 Turbo to generate natural-sounding responses to user's queries Embeddings - to generate text embedding vectors which help in measuring how words are related to each other Challenges we ran into Performance Many of txt2bot's operations manipulate text embedding vectors - which are long arrays containing high dimensional representations of text. Functions such as search rely on being able to promptly retrieve and calculate the similiarity between vectors; while calculations were not an issue, storing and retrieving the multi-megabyte long indices was. Initially, we retrieved the entire list of documents, user messages and vectors from the database via wix-data every time; while wix-data is fast, our retrieval code was simply too inefficient. Hence, we began caching vectors and messages in files instead, since they often need to be loaded in entire batches at once, improving performance noticeably. Optimising External API Requests At first, our requests to the OpenAI embeddings API were done sequentially, but this proved too slow. While parallelising them took a bit of work, it drastically sped up the document indexing process. Accomplishments that we're proud of Prompt engineering While the GPT family of language models has come very far, it is still not trivial to create a general prompt which produces a good response given the wide range of possible user questions and messages. We spent a fair amount of time studying prompt engineering techniques to strike a balance between providing enough information and preventing the models from outputting false data. Consequently, our prompts allow txt2bot's knowledge-based chatbot to provide, by our testing, reasonably good responses to a majority of questions. Rapidly iterating on user feedback We were able to iterate rapidly on user feedback on aspects such as design and user experience, adding entirely new features such as search-as-you-type, based on user feedback. What we learned This is the first time we have built an entire SaaS almost solely on the Editor X platform, and we learnt a lot about its astonishing capabilities and features, such as how convenient Velo Web Modules are, and how to avoid repetitive boilerplate code by using Editor X's low-code features like datasets and repeaters. What's next for txt2bot We would like to improve our prompts to produce better results more often. We are considering implementing a version of txt2bot which uses less external APIs (like OpenAI), for more privacy-concious businesses. This version would be powered by gpt4all, a collection of open-source chatbot models, training data, and code, and would likely run on a cloud provider. <div