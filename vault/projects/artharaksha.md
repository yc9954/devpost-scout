---
slug: "artharaksha"
url: "https://devpost.com/software/artharaksha"
title: "ArthaRaksha"
hackathon: "Google Cloud Vertex AI Agent Builder Hackathon"
organization: "Google"
winner: true
words: 6487
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/revocation_withdrawal"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/general_public"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# ArthaRaksha

> When Gen-AI Rescues You from Financial Fraud and Creates Social Impact

[Devpost](https://devpost.com/software/artharaksha) · hackathon [[Google Cloud Vertex AI Agent Builder Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[revocation_withdrawal]] [[vision_ocr]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]] [[elder_child_care]] [[finance_payments]] [[legal_justice]] [[retail_commerce]] [[scientific_research]] [[security_privacy]] [[supply_logistics]]
**user** [[developer]] [[general_public]] [[researcher]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** agent-builder-agent, agent-builder-agent-context, agent-builder-dataset, agent-builder-grounding, agent-builder-tools, google-agent-builder, google-cloud, google-cloud-function, google-cloud-run, google-gemini, google-gemini-1.0, google-gemini-1.5-pro, pub/sub, python

## How they structured the write-up

- project demo links
- about the project
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for artharaksha
- conclusion
- created by

## Body

Screenshot of App Results Screenshot of App Results Screenshot of App Results Screenshot of App Results Screenshot of App Results Screenshot of App Results Technical Architecture Project demo Links First Link: Main demo link - Main Demo link SecondLink: Technical deep-dive link and Architectural Workflow. Walkthrough of ArthaRaksha in action through functionality and code - Second Demo link About the Project This project focuses on building a prototype resembling a Fraud Protection agent that can help ordinary citizens, especially those who are less aware and emerging digital users against scam calls and texts. Such people may include senior citizens, teenagers with recent digital bank accounts, people from rural parts becoming the emerging digital banking customer segment, people who are not very conversant with English or not so tech savvy etc. though recent reports suggest that well informed individuals in senior private and public sector roles have also fallen for such frauds. This prototype Fraud Protection agent, named ArthaRaksha, is intended to be at the user’s service 24x7 in his / her native language through its mobile app version. The prototype is built using Vertex AI's Agent Builder and is powered by Google Cloud Platform and Google latest Large Language and Multi-modal languages such as Gemini 1.0 and Gemini 1.5 pro. The prototype can transcribe and translate native language speech and text, summarize the event, identify the possibility of fraud, analyze a potential fraud, categorize as per RBI (Reserve Bank of India) fraud classification guidelines and help generate incident report of the potential fraud as per the inputs needed by cybercrime departments with pre-filled parameters (powered by Google’s Gen-AI LLM and MLM models underneath) and finally submit the incident with just one ‘click’ through automated API integration to the agencies and also to banks (if applicable). Inspiration The inspiration for this project came from personal experiences: In one case, one of the prototype developer’s aunt received a fraud call concerning my cousin with the ultimate intent to siphon off money. The caller claimed that the developer’s cousin was in trouble and demanded immediate payment for supposed legal fees. Although the developer's aunt did not fall for the scam, the experience left a lasting impact on the family, highlighting the urgent need for effective fraud detection mechanisms. In another incident, the other prototype developer’s mother received a fraudulent call from a bank that attempted to steal personal information under the garb of KYC renewal for an existing joint account. This joint account has the family’s lifelong savings linked to it. When we researched further, we found a recent report by the Indian Cybercrime Coordination Centre in Mar'2024 outlining that digital financial frauds impact on direct individual banking users amounted to a staggering ₹40,000 crore over the last two years, that's approx. 4.8 Billion US Dollars. At the same, time, the number of such fraud calls have grown by more than 110% in the last 2 years in India. Cybercrime, especially financial fraud, poses a burgeoning and rapidly expanding threat in India, impacting millions of individuals and unsuspecting digital banking users. This alarming situation underscored the increasing prevalence of phone scams and motivated us to develop a solution to help detect and mitigate such fraudulent activities. Generative AI powered ArthaRaksha App prototype built upon the Google Cloud VertexAI Agent Builder platform is an attempt to demonstrate the possibility to complement the relentless efforts of Indian govt, RBI, and banking players in dealing with the herculean, rapidly mutating fraud patterns of scammers. With a collective efforts of all legitimate financial players in India, ArthaRaksha can be powered by a fraud detection and processing platform owned by RBI and contributed to by all interested and legitimate banking players (similar to working models such as those powered by NPCI (UPI), NSDL (for ecommerce marketplace), Digilocker, or upcoming inter operable payment system of RBI). This way, such an underlying model can be continuously trained on newest fraud data and patterns across languages and be up to date not only with latest fraud detection patterns but also new fraud awareness protection, response, and control mechanisms developed by both RBI / Govt agencies and banking and other financial players. Customized versions of the App can be built and deployed by legitimate financial institutions such as banks whereas the underlying platform, data, and model may be contributed to by all financial players, RBI, and Government financial and cybercrime detection agencies. The app intends to bridge the gap between the genuine, dedicated, and independent initiatives by law enforcement agencies, RBI, banks etc. and their adoption as part of a banking user’s daily life. Adoption is best when the interaction with sophisticated backends are hidden to make it a layman’s app in his hand-held device. Financial fraud methods are similar to viruses and follow viral evolution patterns - they mutate fast and if the protection system is not fast enough to respond, damage is done at a mammoth scale by the time controls are put in place. The ability envisioned through the solution is to embed a much needed “real-time”, trusted analysis capabilities for fraud call and text content providing users with an immediate warning (in some cases, even before a fraud call is terminated) and to reduce the reaction times of the protection, control, and reporting systems in place. What it does Generative-AI powered ArthaRaksha App prototype built upon the Google Cloud VertexAI Agent Builder platform is an attempt to demonstrate the possibility of complementing the relentless efforts of the Indian govt, RBI, and banking players in dealing with the herculean, rapidly mutating fraud patterns of scammers. With the collective efforts of all legitimate financial players in India, ArthaRaksha can be powered by a fraud detection and processing platform owned by RBI and contributed to by all the interested and legitimate banking players, telecom players etc. (similar to working models such as those powered by NPCI (UPI), NSDL (for ecommerce marketplace), Digilocker, or upcoming inter-operable payment system postulated by RBI). This way, such an underlying model can be continuously trained on the newest fraud data and patterns across languages and be up to date not only with the latest fraud detection patterns but also new fraud awareness protection, response, and control mechanisms developed by both RBI / Govt agencies and banking and other financial players. Customized versions of the App can be built and deployed by legitimate financial institutions such as banks whereas the underlying platform, data, and model may be contributed to by all financial players, RBI, and Government financial and cybercrime detection agencies. The app intends to bridge the gap between the genuine, dedicated, and independent initiatives by law enforcement agencies, RBI, banks etc. and their adoption as part of a banking user’s daily life. Adoption is best when the interaction with sophisticated backends is hidden or invisible to make it a layman’s app in the user’s hand-held device. Financial fraud methods are similar to viruses and follow viral evolution patterns - they mutate fast and if the protection system is not time-sensitive and agile enough to learn and respond, the damage is already done at a mammoth scale by the time users realize that they have been conned and agencies get a hold of fraud methods. The ability envisioned through the solution is to embed a much needed “real-time”, trusted analysis capabilities for fraud call and text content empowering users with an immediate warning (in some cases, even before a fraud call is over) and to drastically improve the reaction times of the protection, control, and reporting systems in place. How we Built it Step 1: Research and Data Collection The first step involved extensive research into the characteristics of fraud calls. We collected data from various sources, including publicly available datasets of scam call recordings and transcripts. Below are example datasets that were used: RBI published publicly available documents were used to benchmark category of frauds https://www.rbi.org.in/financialeducation/RajuandATM.aspx A BigQuery scam call dataset was used that was publicly available: https://github.com/7shiny786/ArthaRaksha/blob/main/Data/ScamCalls_SM_Scam%20Call_1.mp3 Few audio calls simulating real fraud calls were made - they are available in github as example calls and used in the prototype flow. Bank / ecommerce clients' names that were used to make the call look real scam calls made by scammers. These are not real scam calls and has no relation with the bank name or ecommerce company name taken in the scam calls. https://github.com/7shiny786/ArthaRaksha/blob/main/Data/ScamCalls_SM_Scam%20Call_2.mp3 Since the RBI document was a collection of text, images, text blended within images, and a lot of customer formatting that is commonly seen in marketing materials, OCR was used to extract useful context related to fraud example and their categories and the processed document was used as input as data store for grounding. Step 2: Designing the Architecture We designed the system architecture on Google Cloud platform and integrated different Google Cloud services to bring the solution to life . A schematic representation of the technical architecture is attached here: https://github.com/7shiny786/ArthaRaksha/blob/main/Technical_Architecture/ArthaRaksha-Technical_LLD.png to enable readers to easily correlate with the below explanation. The architecture includes: Data Ingestion and storage : Google Cloud storage has been used as the predominant data storage component. Call (audio) record file are stored at https://github.com/7shiny786/ArthaRaksha/blob/main/Data/ScamCalls_SM_Scam%20Call_2.mp3 Scam documents including text files and transcribes are stored at https://github.com/7shiny786/ArthaRaksha/blob/main/Data/transcripts_SM_Scam%20Call_1_transcript_66553c59-0000-222f-8ea3-582429cdbdc8.json VertexAI Agent Builder used tool Datastore for the purpose of retrieving data chunks (called snippets) when requested to be grounded to specific datasets for certain questions (for example, fraud categorization). The underlying storage for Datastore is Google Cloud storage. The cleansed RBI guideline is stored at https://github.com/7shiny786/ArthaRaksha/blob/main/Data/RBIDoc_DataStore.docx Staging area has been used to store temporary files generated as part of the conversation flow. This serves as kind of working memory for the application for a specific session. Such files are stored at https://github.com/7shiny786/ArthaRaksha/blob/main/Data/StagingArea_Content/ScamSMS_scam_text_Translation_1_SM.txt Application Stack: Front-end: The user interface part is simple, intuitive, and currently built and deployed over Slack. This is the point at which user will interface with the ArthaRaksha and current implementation which is only a prototype may be replaced with interfaces built over open-source frameworks such as Vue.JS (vue-chatbot), Reach.js (with chatfuel), RASA etc.. Alternatively one may choose to go for managed services for developers such as Kommunicate, Microsoft Bot, Botanic or integrated with ready to use customer facing agents that are already well adopted such as Whatsapp, Telegram, facebook messenger or Google’s ‘Dialog Flow’. There are immense opportunities to differentiate an Artharaksha offering in the front-end and financial players such as banks or authorized fraud protection partners of RBI / Government may like to integrate ArthaRaksha’s capabilities through existing applications. Back-end: This is the layer that is currently being showcased through the Vanilla App’s Slack i