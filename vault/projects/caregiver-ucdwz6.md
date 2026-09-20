---
slug: "caregiver-ucdwz6"
url: "https://devpost.com/software/caregiver-ucdwz6"
title: "Caregiver"
hackathon: "DeveloperWeek 2025 Hackathon"
organization: "DevNetwork"
winner: true
words: 1203
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Caregiver

> Caregiver is an AI-powered assistant for assisted living facilities, automating event tracking, resident insights, medical queries, and SMS alerts—plus a fun AI-powered memory game to engage residents

[Devpost](https://devpost.com/software/caregiver-ucdwz6) · hackathon [[DeveloperWeek 2025 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[accessibility]] [[elder_child_care]] [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, docker, html, hugging-face-spaces, hugging-face-transformers, javascript, oracle-apex, python, redis, sql, twilio

## How they structured the write-up

- project story: caregiver – ai for assisted living facilities
- how we built caregiver:
- challenges we ran into:
- what we learned
- the impact of caregiver:
- next steps – how we can improve caregiver:
- conclusion:

## Body

System Diagram Medical Ai Assistant Question: What events are happening this week which would help cancer patients? Medical AI Assistant Question: How can i help cancer patients? Ai Powered Memory Game Example Dental Information Graphs on Oracle Apex Disability Information Graphs on Oracle Apex Mental Distress Information Graphs on Oracle Apex Home page tables on Oracle Apex Project Story: Caregiver – AI for Assisted Living Facilities About the Project Assisted living facilities often struggle with managing resident data, tracking events, and engaging residents in meaningful activities. Many of these tasks rely on manual processes, making them time-consuming and inefficient. Our goal was to create a smart, AI-powered solution that automates these processes while improving the quality of care for residents. Inspiration We wanted to apply AI in a practical way to help real-world communities. Assisted living facilities often lack efficient digital solutions, and we saw an opportunity to use conversational AI, vector search, and automation to make administrators' jobs easier while also benefiting residents with interactive cognitive activities. How we built Caregiver: ● AI-Driven Medical Assistance: Utilizes large language models (LLMs) via Hugging Face Transformers to answer complex medical queries and provide contextual, accurate information. This allows administrators to ask questions related to general health (e.g., treatment options for cancer, exercises for osteoporosis) as well as facility-specific inquiries (e.g., event details, resident health statistics). ● Dual-Purpose Redis Database: Acts as both a key-value store to maintain conversation history (ensuring that the chatbot interactions remain contextually aware) and as a vector database to support efficient retrieval of relevant data based on vector searches. ● Oracle APEX Frontend: The user interface is built on Oracle APEX, which is synchronized with a relational SQL database. This setup allows for dynamic data visualizations and an interactive dashboard that administrators can use to monitor resident health and facility operations. ● Interactive Memory Game: Provides an engaging cognitive exercise for residents. In this game, an LLM simulates a person from a specific year. Users ask questions to gather hints (e.g., inquiries about popular music or historical events), and then they attempt to guess the hidden year. ● Twilio SMS Notifications: Integrates with Twilio’s API to send daily SMS notifications. These messages alert administrators to upcoming events and important updates at the facility, ensuring they stay informed in real time. Challenges we ran into: ● Data Integration – Collecting, Cleaning, and Structuring Health Data: We sourced and processed data from the Healthy Aging dataset, which included statistics on mental distress, disabilities, and dental health trends. Before we could use this data in Oracle APEX, we had to clean and format it. This involved handling missing values, standardizing categorical data, and optimizing SQL queries to support efficient real-time visualization. We also worked on structuring the dataset for fast retrieval and meaningful insights, ensuring our dashboards accurately represented real-world aging trends. ● Vector Search Optimization – Fast and Accurate Retrieval of Event and Resident Data: Our AI chatbot relies on Redis as a vector search database to quickly retrieve relevant facility events, resident statistics, and medical insights. To achieve this, we embedded facility event descriptions using SentenceTransformers and tested various distance metrics (cosine similarity, Euclidean, Manhattan) to optimize search accuracy. Additionally, we had to fine-tune Redis vector index parameters to balance query speed and retrieval precision, ensuring fast and relevant chatbot responses. ● Oracle APEX Customization – Building an Interactive and Engaging Frontend: Oracle APEX is a low-code platform, but making it visually appealing and highly interactive required extra effort. We used custom JavaScript and CSS overrides to enhance the design, ensuring that dashboards were both responsive and mobile-friendly. Additionally, we optimized SQL queries to prevent slow dashboard performance, fine-tuned data visualizations for readability, and embedded external components like the AI chatbot and memory game, allowing seamless interaction between the frontend and backend. What we learned ● Selecting the Right AI Model for Healthcare Applications: We used DeepSeek-R1-Distill-Qwen-1.5B, a distilled model optimized for reasoning, math, and complex problem-solving. Unlike many AI models, DeepSeek-R1 was trained using reinforcement learning (RL) without supervised fine-tuning (SFT), allowing it to self-improve over time. This model provided fast and reliable responses, making it a strong choice for healthcare-related AI applications. However, while DeepSeek-R1 is not inherently HIPAA-compliant, its open-source nature allows for self-hosted deployments, ensuring better data privacy control in real-world medical use cases. ● Using Oracle APEX for Data Visualization and Frontend Development: Oracle APEX provided a low-code environment that made it easy to build interactive dashboards tracking resident health trends. While APEX was useful for structured SQL-based visualizations, it had limitations in design flexibility. To improve the UI, we implemented custom JavaScript and CSS overrides, making the dashboard more visually engaging. Another challenge was ensuring real-time data retrieval, which required SQL query optimization to avoid slow dashboard performance. Additionally, integrating external components such as the AI chatbot and memory game required additional API configuration. ● Hosting and Developing APIs on Hugging Face: Hugging Face Spaces allowed us to deploy our backend API and integrate AI models efficiently. The platform offered built-in GPU support and simplified model hosting, but running larger models like DeepSeek-R1 required significant computational resources, making long-term deployment costly. While Hugging Face is excellent for quick prototyping, for production deployment, self-hosting on cloud platforms like AWS, Azure, or Oracle Cloud would be more cost-efficient and secure. ● Deploying and Using Models on Hugging Face: We experimented with multiple AI models before selecting DeepSeek-R1-Distill-Qwen-1.5B for its strong reasoning and data interpretation capabilities. Hugging Face allowed us to easily switch between models, but we found that embedding retrieval-based AI using Redis significantly improved performance. The combination of vector databases (Redis) and AI models (DeepSeek-R1) enhanced context-aware chatbot interactions, ensuring responses were accurate and relevant. The Impact of Caregiver: ● Caregiver successfully integrates AI-powered assistance, real-time event tracking, and data-driven insights to improve the management of assisted living facilities. By combining conversational AI, vector search technology, and automated notifications, the system enhances operational efficiency while providing valuable medical and facility-related information. The addition of an interactive memory game also helps engage residents in cognitive exercises, making Caregiver a holistic solution for administrators and residents alike. ● Through this project, we demonstrated how AI and automation can address real-world challenges in assisted living facilities. By leveraging DeepSeek-R1-Distill-Qwen-1.5B for natural language understanding, Redis for fast vector searches, and Oracle APEX for interactive dashboards, Caregiver provides accurate, real-time insights that improve decision-making for facility administrators Next Steps – How We Can Improve Caregiver: ● Enhancing AI Model Performance: Fine-tune DeepSeek-R1-Distill-Qwen-1.5B on a medical-specific dataset to improve accuracy for healthcare-related inquiries. ● Expanding AI Capabilities: Integrate multi-modal AI to allow administrators to process images, medical charts, and reports in addition to text-based queries. ● Improving Frontend User Experience: Further customize Oracle APEX by adding more dynamic UI elements, improved mobile responsiveness, and additional interactive tools for administrators. Conclusion: Caregiver demonstrates how AI can enhance assisted living facility management by providing real-time insights, automated event tracking, and interactive cognitive tools. By integrating DeepSeek-R1-Distill-Qwen-1.5B, Redis vector search, and Oracle APEX dashboards, the system streamlines operations while improving resident engagement. Moving forward, optimizing AI performance, ensuring HIPAA compliance, and scaling deployment will be key steps toward making Caregiver a viable real-world solution. <div