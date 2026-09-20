---
slug: "mentation"
url: "https://devpost.com/software/mentation"
title: "Mentation"
hackathon: "MongoDB AI Hackathon: Code for a Cause"
organization: "MongoDB"
winner: true
words: 1212
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/mental_health"
  - "substrate/structured_db"
---

# Mentation

> Lana is an AI friend/therapist, tracking emotions, keeping a diary, affirming love, & learning from you to become your digital twin. Accessible in Hindi & English, Mentation offers well-being for all.

[Devpost](https://devpost.com/software/mentation) · hackathon [[MongoDB AI Hackathon- Code for a Cause]]

## Facets

**mechanism** [[benchmark_measured]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[mental_health]]
**substrate** [[structured_db]]

**stack** apprunner, aws-sdk, axios, bedrock, boto3, cognito, docker, eventbridge, hugging-face, hugging-face-transformers, i18nnext, lambda, mongodb, next.js

## How they structured the write-up

- inspiration ⭐️
- how we built it 🧑‍💻
- challenges we ran into 🥊
- accomplishments we’re proud of 🏆
- what we learned 🙇‍♂️
- what’s next for mentation ⏭️

## Body

Get to know 'Mentation' What we're driven by is the poor Awareness, Accessibility, and Affordability of mental health support. These are the technologies used. SignIn/SignUp Dark Mode SignIn/SignUp Light Mode Get to know the user Dark Mode Get to know the user Light Mode First Chat Screen Dark Mode First Chat Screen Light Mode Chats Dark Mode Chats Light Mode Stats Dark Mode Stats Light Mode Emotion Calendar Dark Mode Emotion Calendar Light Mode Daily Logs Dark Mode Daily Logs Light Mode Breath Dark Mode Breath Light Mode Inspiration ⭐️ Mentation was born from a familiar moment: we saw a friend, nervously avoid the word "therapist" around her parents, fearful it would ignite the family debate. This highlighted and reminded us of the obstacles many in India still face like financial limitations, societal pressure, and a general uncertainty about when and how to seek support. For many, mental health remains taboo, causing them to conceal their struggles, sometimes even from themselves. Hence, the idea of a pocket-friendly pocket friend came to us. that is the therapist/friend bot. Inspired by the therapeutic power of journaling, which helps track emotions, and monitor personal growth, we added a diary feature for self-reflection, alongside analytics to visualize progress and look at the bigger picture. Building on these insights, another compelling idea emerged: what if this bot, which is capable of understanding and tracking a person’s major life events and emotions, could over time become their digital twin? By learning how users respond to specific situations and remembering their unique reactions, the bot could evolve into a digital friend that truly understands, reflects, and supports the user. An empathetic "clone" that grows alongside them. How We Built It 🧑‍💻 Mentation combines AWS’s advanced services, frontend and backend technologies, and machine learning models, all optimized for scalability and flexibility. Ideation and Research: We examined user needs by speaking with friends, reviewing mental health trends, consulting a psychologist, and identifying gaps in accessible support. Prototyping and NLP Development: We designed conversational flows and trained NLP models to accurately recognize emotional cues with empathy. To optimize performance, we benchmarked various NLP and AWS Bedrock models, exploring approaches like custom LLM training as an alternative to Bedrock and offloading emotion detection to a dedicated model. These prototypes and experiments helped us identify the most effective setup for our needs. Crafting UX and User Flow: After rounds of discussions and feedback we mapped an intuitive user journey with a clean, minimal, and friendly interface, keeping each feature accessible and purposeful. Making the user flow on the application as smooth as possible. Frontend & Backend: Frontend & Backend: Built using Next.js for both frontend and API, with TypeScript ensuring type safety. Authentication is secured with AWS Cognito, Google Auth, and JWT. MongoDB serves as the database, while Tailwind CSS, ShadCN components, and i18nNext enable a seamless, multi-language user experience. Machine Learning and Model Integration: Our architecture uses AWS SageMaker to manage embedding models, leveraging Hugging Face integrations. The main LLM is AWS Bedrock's LLaMA 70B, selected for its robust capabilities, while MiniLM was chosen for embeddings for its balance of speed and quality. A SageMaker Notebook was used to customize MiniLM's container entry point, allowing deployment on a SageMaker serverless endpoint. System Architecture: Our serverless architecture relies on SageMaker endpoints on Lambda, App Runner for deploying the app, and MongoDB for cost-effective storage. AWS EventBridge handles automated tasks, and Bedrock enhances chatbot capabilities. Iterative Prototyping: Early prototypes focused on chatbot functionality, evolving to include diary entries and resource-based responses. Testing different models for translation and cultural accuracy was crucial, especially for Hindi. Challenges We Ran Into 🥊 Building Mentation brought significant challenges: Technical Learning Curve: Returning to ML after a gap, we re-learned model training concepts. Tools like SageMaker and vector search required time and AWS credits, especially on SageMaker notebooks. AWS Service Limitations: AWS Bedrock has been down for our account since November 9th, but we experimented and found that the same bedrock model was available in north Virginia, got access to that, and modified the code to make it work, which delayed testing and improvements. SageMaker deployment limitations also led us to rely on CPU instances and lightweight models. The custom container size exceeded Fargate’s 12 GB limit, adding complexity to our goal of a serverless setup. Hackathon Time Constraints: Discovering the hackathon close to the deadline, coupled with a work trip, compressed our timeline, limiting our testing capabilities. One of the biggest challenges was optimizing our model architecture. As this was our first major ML project, we dedicated significant time and effort to exploring and benchmarking various solutions to find the best fit. Initially, we tested a segregated workload setup, assigning different models for specific tasks (e.g., main LLM, a separate model for suicide detection). However, practical constraints, including compatibility issues and resource limitations, eventually led us to consolidate our approach around AWS Bedrock. While this required pivoting after investing time and credits, it gave us a streamlined, scalable solution and provided invaluable learning experiences in navigating model integration challenges. Accomplishments We’re Proud Of 🏆 Despite these hurdles, we’re proud of several achievements: Model and Vector Search Deployment: Deploying a custom script and models on SageMaker and fine-tuning vector search for relevant responses was a major milestone. Google SSO Integration: Successfully adding Google Single Sign-On was a great learning experience and provided a seamless login experience. AWS Journey: Building this project on AWS was both challenging and rewarding. Coming from a GCP background, we initially found AWS’s UI complex and its documentation somewhat overwhelming. However, working with services like App Runner, EventBridge, and the AWS SDK pushed us out of our comfort zones and expanded our skills significantly. We’re proud of overcoming our initial hesitation and successfully navigating AWS’s ecosystem to meet our project goals and optimize costs—a journey we may not have pursued otherwise but one that proved invaluable. What We Learned 🙇‍♂️ This hackathon was a valuable learning experience: Technical Skills: We gained hands-on experience in deploying apps on AWS, training models on SageMaker, and implementing custom endpoints, as well as embedding generation and similarity indexing. Project Management: We learned the importance of time and resource management, balancing exploration with implementation. We also recognized the need for clear documentation for future use. Efficient Development: Testing different models, embedding setups, and serverless configurations showed us how to prioritize approaches based on performance and user experience. What’s Next for Mentation ⏭️ Looking forward, we plan to: Scale Infrastructure: Transition from App Runner to EKS for better scalability and cost efficiency. Expand Language Support: Add support for more Indian (Regional) languages with improved translation models. Enhance User Customization: Enable users to personalize Lana’s personality to cater to diverse communication styles. Therapist Export Feature: Offer an "export therapist's" notes option for users to convert their chats into comprehensive and relevant notes for therapists or other mental health professionals. “Share Your Lana” Feature: Develop Lana’s digital clone feature, central to our vision for Mentation. Enhanced Personalization: Capture user data on onboarding for a tailored experience, helping Lana become an even better match. Comprehensive Testing: Conduct extensive testing on AWS Bedrock’s integration once operational for stability across functionalities. Simplify Tool Experience: Ensure accessibility and equity across varied demographics to make Mentation widely useful. <div