---
slug: "contract-ml"
url: "https://devpost.com/software/contract-ml"
title: "Contract ML"
hackathon: "Dropbox Sign AI-Powered Agreements Hackathon"
organization: "Dropbox"
winner: true
words: 988
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/retrieval_grounding"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Contract ML

> An AI-Enabled tool to help small and medium scale businesses efficiently author, review and sign business contracts.

[Devpost](https://devpost.com/software/contract-ml) · hackathon [[Dropbox Sign AI-Powered Agreements Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[retrieval_grounding]]
**domain** [[legal_justice]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** ai, dropbox, gatsby, gcp, generativeai, machine-learning, palm, palm-api, react

## How they structured the write-up

- inspiration
- what does it do
- how it uses generative ai (large language models)
- challenges and fixes
- how contract ml is built
- responsible ai and reliability considerations
- interesting learnings
- what's next for contract ml

## Body

Contract ML home page Architecture and supported flows for contractml AI Assisted Contract Review. The PaLM api is used to review contract pages Dropbox sign api used to enable multiparty document signing Inspiration For many small and medium scale businesses or individuals, the process of creating contracts for their services or reviewing contracts they are presented with can be a daunting task. This is especially true for those who are not familiar with legal jargon and the process of contract creation. To address this, Contract ML aims to provide a tool that can help users rapidly create and review contracts. This is done by leveraging state of the art AI models and best-in-class UX to assist in the process of contract creation and review. What Does It Do Contract ML offers value across several features: Automated Contract Review (with Human in the loop). Highlights important terms or issues in a contract that the user should double check before signing. Multiparty Contract Signing with multiple parties powered by DropBox Sign . Utilizes the DropBox sign API to allow users to sign contracts with multiple parties. AI-Assisted Contract Authoring [in progress]. A work flow that supports users in creating their own contracts customized to their service or business needs. Contract Gallery [in progress]: A collection of contracts that users can use as a starting point for their own contracts How it Uses Generative AI (Large Language Models) ContractML utilizes state-of-the-art Large Language Models (LLMs) in it's two high level workflows. Specifically, Iapply the PaLM Generative AI model in : AI-Assisted Contract Review: An LLM scans each page of a contract and identifies critical actionable terms or issues the user should double-check before signing. This assists in ensuring that all necessary points are addressed and reduces the likelihood of misunderstandings or legal issues arising from the contract. AI-Assisted Contract Authoring (in progress): This feature revolutionizes the user experience for crafting business or service contracts. The user can take the following steps: Describe the contract they need. ContractML Author tool conducts a web search to find relevant data or contracts (retrieval) to serve as a basis for the new contract. The system provides a plan to the user containing suggested high-level components for the contract. The user is offered an interface to edit or modify the proposed plan. ContractML generates the content for each section and merges all parts into a comprehensive contract. The user can edit or review the generated contract and download it in a variety of formats (e.g., pdf, markdown, etc). Challenges and Fixes PDF Data Extraction: Extracting data clearly with minimal noise from a pdf is crucial to obtaining high quality results from the AI model. To address this, I explored several libraries such as pypdf2, pdfminer, etc and also front end pdf parsing libraries such as pdfjs. Ultimately I found pdfjs to be more controllable and where possible we rely on its parsing capabilities but fall back to a server based solution on failure (pypdf2). Prompt Engineering: Writing the correct prompts that make the Generative Model helpful required systematic evaluation of multiple prompts. For example, it was critical to specify the output format of the generated text (e.g., markdown), specify the verbosity ask the model to also generate rationale for its suggestions. DropBox Sign Api Caching: During evalaution and test, it was critical to make multiple requests to the dropbox sign api both to understand its behaviours, debug errors, run automated tests and to improve the user experience. To address this, I implemented a caching layer that allows us to cache the results of the api calls and replay them during testing. This allows us to run tests without incurring the cost of making multiple api calls. How Contract ML is Built Contract ML is built using the following technologies: Frontend: React and GatsbyJS Backend: FastApi Hosting and Infrastructure: Google Cloud Platform (Firebase firestore for database, Firebase Auth for authentication and access control, VertexAI PaLM model for AI assisted contract authoring and review, Cloud Run for hosting the backend API) Document Signing: DropBox Sign API Responsible AI and Reliability Considerations To ensure the AI assistance offered by ContractML is consumed in a responsible manner, the following considerations were prioritized: Human in the loop User Experience: The user is always in control of the process and can choose to accept or reject the AI suggestions. The user is also able to modify the AI generated content to suit their needs. Addressing Hallucination and Quality Control: LLMs are susceptible to generation content that may not be factual or grounded in existing referennceable documents which could lead to poor decision making. To address this ContractML does the following Task decomposition: The LLM model is tasked with reviewing contracts on a page by page basis. This simplifies the task and reduces the likelihood of hallucination. UX checks: The interface provides the user with a clear indication of the AI generated content, the possibility of errors, the need to double check and allows them to modify it as needed. Interesting Learnings Working on this project involved learning about the following: Prompting techniques for reliable LLM generation for contract authoring and review Best practices for UX design for AI assisted workflows Working with the PalM LLM Api via VertexAI Working with the DropBox Sign API (rest endpoints and embedded signing api flow) What's next for Contract ML Contract ML will invest in additional quality and safety checks to ensure that the AI assistance offered is of the highest quality and reliability. Options include: Contract Gallery: Build out tooling for a community driven contract gallery where users can share their contract templates with others. Feedback loop: The system will be able to learn from user feedback to improve the quality of the AI assistance offered. Improved Document Authoring: Improve the UX for document authoring Assembly high quality contract review datasets that can be used to train domain-specific models for hight quality contract review <div