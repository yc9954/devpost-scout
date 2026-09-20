---
slug: "pixie-ai-dw8l0h"
url: "https://devpost.com/software/pixie-ai-dw8l0h"
title: "Pixie AI"
hackathon: "Databricks Generative AI World Cup"
organization: "Databricks"
winner: true
words: 871
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/developer"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/regulation_legal_text"
---

# Pixie AI

> AI Copilot for Nurses

[Devpost](https://devpost.com/software/pixie-ai-dw8l0h) · hackathon [[Databricks Generative AI World Cup]]

## Facets

**domain** [[developer_tools]] [[education]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[developer]] [[educator_student]] [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]] [[medical_record]] [[regulation_legal_text]]

**stack** databricks

## How they structured the write-up

- inspiration
- what it does
- how to use it
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pixie ai
- team details

## Body

frontend architecture sample usage of databricks genai sql query Inspiration Nurses in hospitals manage multiple patients daily and overwhelming workloads in high-stress environments. They often have to care for more patients than recommended, which leads to increased medical errors, burnout, and even patient mortality. For instance, a single additional patient per nurse can raise the likelihood of patient mortality by 7% and significantly increase nurse burnout rates​ (Penn LDI)​. What it does 𝗣𝗶𝘅𝗶𝗲 𝗔𝗜 directly tackles this urgent issue. [Note: this tool is not for triage; it’s designed for patients who have been hospitalized for several days.] Our innovative solution revolutionizes how nurses prioritize patient care. By integrating seamlessly with hospital systems, Pixie AI reduces the manual strain on nurses through a proactive approach: 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝗖𝗵𝗲𝗰𝗸-𝗜𝗻𝘀: Before each check-in, Pixie AI contacts patients via bedside intercoms, posing standardized questions. We made sure the AI sounds as natural and fast as possible. These interactions are recorded and analyzed for emotional and health cues (patient's mood, condition, note, etc), helping to prioritize care needs. 𝗦𝗺𝗮𝗿𝘁 𝗥𝗮𝗻𝗸𝗶𝗻𝗴 𝗦𝘆𝘀𝘁𝗲𝗺: Using tone analysis & sentiment analysis for the responses, our system evaluates the urgency of each patient's situation, ranking them to ensure nurses attend to the most critical cases first. 𝗥𝗲𝗮𝗹-𝗧𝗶𝗺𝗲 𝗨𝗽𝗱𝗮𝘁𝗲𝘀: Nurses and doctors can check the order of their visit anytime. We prioritize patients who need urgent help first. Nurses receive pushed alerts when there are emergencies via emails & SMS. Similarity search: Nurses and doctors can search similarity using Databrick ai_similarity() PDF View : Doctors and Nurses can view patient's history with their PDF medical records. Pixie AI enhances patient safety and empowers nurses, allowing them to deliver more personalized and effective care. This leads to better patient outcomes and reduced stress and burnout among nursing staff. Nurses and doctors can also save tons of time on checkups, doing paperwork to instead focus more on the patients. With Pixie AI, hospitals can ensure that their most valuable resources—nurses—are supported, respected, and optimized. We expect a 40% reduction in the time nurses spend on routine checks and paperwork. This allows for more focused patient care, potentially enhancing outcomes and reducing staff stress. Imagine a future where hospital care is not only reactive but proactive, with AI seamlessly ensuring that patient care is timely and precise. That's a future with Pixie AI. How to use it Setting Up: Clone this repository Create environment settings: cp .env.example .env Fill in the required environment variables in the .env file. Make sure you have all the required keys and secrets. Instructions: To run chat, go to backend , click on run.sh In the backend folder, run the Streamlit UI: make run All PDF records will be saved in records folder. All QR code will be saved in qr_code folder. How we built it Pixie AI was built with the goal of optimizing nurses' workflow in hospitals. We wouldn't make it without Databricks LLM model. The model is used to: Summarize conversations and detect if they need help. Determine patients' priority, response sentiments. Search similar cases with similarity search. As a POC, we want to keep it simple for both users and developers. We use HumeAI to build the chat interface faster. The patients' information, conversations, and records are saved in Databricks SQL clusters. Lastly, we put a lot of effort in UX design to make sure doctors, patients, and hospitals can use it without knowing much about programming. Challenges we ran into One of the main challenges we faced was ensuring the accuracy and reliability of voice recognition in noisy hospital environments. Additionally, integrating with various hospital information systems posed technical hurdles due to diverse software platforms and data privacy regulations. Accomplishments that we're proud of We are particularly proud of Pixie AI’s ability to significantly reduce the workload on nurses by automating the initial patient check-in process. Our system has demonstrated a high level of accuracy in voice recognition and sentiment analysis, leading to improved patient prioritization and care. Additionally, the positive feedback from nursing staff about the usability and effectiveness of our system has been incredibly rewarding. What we learned Throughout the development of Pixie AI, we learned the importance of close collaboration with end users—nurses—in the design process. Their insights were invaluable in making the system practical and effective. We also gained a deeper understanding of the complexities involved in integrating AI technologies with existing healthcare protocols and systems. What's next for Pixie AI Looking ahead, we plan to expand Pixie AI’s capabilities to include more languages and dialects, making it accessible to a broader range of healthcare facilities worldwide. We are also exploring additional AI features, such as predictive analytics, to anticipate patient needs before they arise. Moreover, ongoing partnerships with healthcare providers will be crucial for continuous improvement and wider adoption of Pixie AI. At the core, Pixie AI is about saving medical processes time, and let doctors have more freedom to care for their patients. Team details Members: Stephanie Nguyen & Chris Le Email Address (of each participant): tien.nguyen@columbia.edu and locvicvn1234@gmail.com Company/Organization you guys work for/represent: We are college students. We go to Columbia University & Augustana College Country: United States Industry prize you are going for: Healthcare and Life Sciences <div