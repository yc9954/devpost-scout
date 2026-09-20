---
slug: "agreefast-for-docusign"
url: "https://devpost.com/software/agreefast-for-docusign"
title: "Agreefast for Docusign"
hackathon: "The Docusign Hackathon: Unlocked"
organization: "Docusign"
winner: true
words: 1352
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Agreefast for Docusign

> We revolutionize your Docusign workflows with AI insights, obligation and event tracking, seamless compliance enhanced by chat with envelopes, and Trello integration for eased deadline management.

[Devpost](https://devpost.com/software/agreefast-for-docusign) · hackathon [[The Docusign Hackathon- Unlocked]]

## Facets

**mechanism** [[cross_origin_web]] [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[labor_employment]] [[legal_justice]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[web_dom]]
  <sub>weak: structured_db</sub>

**stack** azure, chrome, cloudflare, docker, docusign-connect, docusign-esignature-api, express.js, fastapi, langchain, mongodb, neo4j, nextjs, ollama, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- technologies used and user flow
- what we learned
- what's next for agreefast for docusign

## Body

Landing Page Agreefast Smart Dashboard with QuickSign Chrome Extension Individual Key Event Detail Captured Party-specific Obligation List Agreefast Envelope Chatbot QuickSign - Choose Organisation Stage QuickSign - eSignature Session Link Generation Stage Agreefast Trello Power-up Agreefast Constructed Knowledge Graph Agreefast Trello Power-up Experience - Demo Invitation Agreefast Chrome Extension - User Experience Flow Agreefast and Docusign integration - User Experience Flow Swagger for API Documentation Agreefast for Docusign Inspiration Agreefast was inspired by the common struggles many businesses face with complex legal agreements. Often, users are overwhelmed by lengthy contract terms, unclear obligations, and the fear of being trapped in unfavorable terms. We wanted to build a solution that simplifies this process by providing clarity, insights, and smart tracking without adding extra work for users. With Docusign's widespread adoption and seamless workflow, we aimed to integrate with it to enhance its effectiveness, preventing agreement traps at both the pre-signing and post-signing stages. What it does Agreefast integrates seamlessly with Docusign, providing users with AI-driven insights into agreements. It automatically analyzes the terms of contracts, calculates a Compliance Obligatory Score , our custom-made metric, to gauge the number of obligations in the agreement and the level of importance it has on keeping the agreements compliant and in force, and provides a list of obligations for each party involved. This helps users manage their contracts more effectively, ensuring they stay on track. Additionally, 'Agreefast' extracts key events and timelines from signed agreements and allows users to add them to their device calendar. With the Trello Power-Up , users can track upcoming events, view completed events, and manage tasks directly from their Trello board using just the envelope ID from Docusign. How we built it Agreefast was built using a combination of AI-driven natural language understanding to analyze contract language and identify obligations and timelines, along with seamless integration into Docusign's ecosystem via webhook URLs leveraging the Docusign Connect technology and Docusign eSignature API . We used a variety of web technologies, including cloud services from Azure and OpenAI for storage and AI processing respectively, JavaScript for the browser extension, and Trello’s API to ensure smooth integration. Detailed technologies are highlighted below. The platform is designed to be user-friendly, operating without requiring complex authentication from the end-users, and following the simple workflow of Docusign. Challenges we ran into Data Accuracy : Extracting and interpreting legal terms from agreements accurately was a challenge. We had to fine-tune our AI model and prompts to ensure it could effectively identify obligations and key clauses by undertaking richer LLM usage. Integration Complexity : Integrating with Docusign and ensuring that the webhook, calendar features, and Trello Power-Up worked seamlessly without introducing friction for the user required detailed attention. User Experience : Ensuring that the platform remained simple and user-friendly while delivering powerful features was a balancing act. Our goal was to make sure the user experience felt as seamless as Docusign itself. This played a huge role in how our dashboard was designed. Accomplishments that we're proud of Zero Authentication Hassles : 'Agreefast' operates without requiring additional user authentication, rather is grounded on using emails to prove user identity, maintaining the simplicity of the much appreciated Docusign workflow. Rich AI Insights : Our platform provides valuable insights into agreements, including a compliance score and a comprehensive list of obligations for each party involved. Envelope Chatbot : The powerful chatbot experience that is freshly prepared for each envelope is also something we believe our users will be thrilled about. Post-Signing Tracking : We’re proud to offer features that help users keep track of critical events after the agreement is signed, such as adding such identified events directly to their calendars and using Trello to manage tasks. Seamless Trello Integration : The Trello Power-Up is a standout feature that allows users to effortlessly track their agreements right on their own boards, by simply entering the envelope ID. Technologies used and User Flow Docusign Connect for seamlessly integrating the envelopes before and after signing into our platform. Docusign eSignature API for enabling the QuickSign feature on 'Agreefast' which helps users sign envelopes quickly right from within our platform. Docusign Navigator was also experimented with and 'Agreefast' is built to readily support Docusign Navigator when the Upload Agreement API is made publically available as mentioned in the Docusign Developer documentation. NextJS for the React based frontend web application OpenAI API for LLMs Ollama API for embedding models. Langchain for orchestrating the AI workflow Socket.io for the AI chat interface Unstructured for processing the documents to gather meaningful information Trello power-up SDK for building the UI and functionalities and the Trello REST API for populating the events and reminders onto the boards Neo4j for storing the knowledge graphs constructed from the envelopes. amqplib for consuming and producing to the message queues from the Node.js workers and pika for the Python workers in order to enable an asynchronous workflow for time consuming tasks via RabbitMQ . Microsoft Azure and Cloudflare for cloud deployment and application security. API Documentation with Swagger We have a well documented Swagger API documentation provision done for our entrypoint API server which can be experienced at Swagger for Agreefast API Server Microservice/Codebase Description ai_service Consumes from RabbitMQ upon detecting new Docusign envelope sent, to make AI inferences and prepare the knowledge graph for driving the Agreefast Envelope Chatbot backend Hosts the Docusign Connect POST webhook and enables interaction with 'Agreefast Dashboard' and Trello Power-up. Helps enable the QuickSign feature by integrating with Docusign eSignature API chat_service Works on key inference phase when the chatbot is queried by the user on the frontend. Exposes API endpoints to be integrated to 3rd party services like WebEx or Slack if required chrome_extension Helps new users leverage Docusign Connect to link to Agreefast and quickly open the relevant Agreefast Dashboard from the Docusign Agreement Signing Page frontend Agreefast Dashboard and landing page built with NextJS for a seamless dashboard user experience trello-powerup-html Hosts Trello Power-up specific integration assests to populate details captured from envelope into Trello boards Endpoint Method Description /api/envelope/:id/getActivationStatus GET Returns the activation status of the specified envelope. /api/envelope/:id/activate GET Activates the specified envelope and notifies recipients via email. /api/envelope/:id/deactivate GET Deactivates the specified envelope. /api/envelope/:id/getObligationScore GET Fetches the compliance obligatory score for the specified envelope. /api/envelope/:id/getObligations GET Retrieves the obligations associated with the specified envelope. /api/envelope/:id/getSignedDate GET Fetches the signed date for the specified envelope. /api/envelope/:id/getAgreements GET Retrieves the agreements associated with the specified envelope. /api/envelope/:id/getIcsData GET Retrieves ICS data for the specified envelope. /api/envelope/:id/chat POST Sends user questions to the chat service for the specified envelope and retrieves the response. /api/envelope/:id/aiProcessingComplete POST Marks the AI processing for the specified envelope as complete and sends notification emails. What we learned User Feedback is Key : Engaging with some potential users during development helped us understand their true needs, such as the importance of keeping everything within the existing Docusign workflow. Integration Details Matter : The most precise and key details in integration (like syncing timelines to calendars and Trello) had a large impact on user satisfaction and the overall effectiveness of the platform. Simplicity Drives Adoption : Keeping things easy to use while offering advanced features was crucial. This instantly intrigued interest in our potential users when we asked for their feedback. What's next for Agreefast for Docusign We’re excited to continue refining Agreefast by expanding its capabilities: Custom AI Models : We plan to allow users to choose their own model of choice for each envelope to let them choose what's best for their usecase. Extending the Envelope Chatbot : To provide a much accelerated value, we are exploring options to expose the Agreefast chatbot into users' workplace messaging apps like Slack, Cisco Webex, Discord, Microsoft Teams, etc. More Integrations : We’re exploring integration with other platforms and tools in the contract / project management space to provide even greater value. Enhanced AI Capabilities : We plan to improve our AI models to provide even deeper insights into contract terms and obligations. User Personalization : Adding personalized features to allow users to customize their dashboard and notifications based on their preferences. <div