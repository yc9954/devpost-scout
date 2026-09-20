---
slug: "notemd"
url: "https://devpost.com/software/notemd"
title: "NoteMD"
hackathon: "MongoDB AI Hackathon: Code for a Cause"
organization: "MongoDB"
winner: true
words: 507
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# NoteMD

> Enhancing the Healthcare, Experience One Patient at a Time

[Devpost](https://devpost.com/software/notemd) · hackathon [[MongoDB AI Hackathon- Code for a Cause]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[health_clinical]]
  <sub>weak: transportation</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[medical_record]] [[structured_db]]

**stack** express.js, json-web-token, llm, mongodbatlas, nextjs, openai-chat-completion-api, rag, railway, react, render, vector-search, vercel

## How they structured the write-up

- inspiration
- what i learned
- building the project
- challenges faced
- conclusion

## Body

Option for Doctor to select patient Patient profile showing assigned doctor Patient Mobile Dashboard Mobile dasboard Patient dashboar showing currently prescribed medication Desktop dashboard RAG in action! NoteMD: Enhancing Healthcare Experience Inspiration The average Doctors visit is a mere 15 minutes on a good day, and even less for busy doctors. NoteMD is designed to allow doctors to give healthcare services on the go, and allow patients to recieve healthcare services froom the go as well, All from the comfort of their devices. What I Learned Developing NoteMD was taught me how to do the following: Web Application Development: Insight into developing scalable and responsive web applications. Security Protocols: Implementation of JSON Web Tokens (JWT) to ensure data encryption and secure user authentication. Database Management: Utilized MongoDB Atlas for efficient data storage and retrieval, especially leveraging its vector search capabilities. Cloud Services Integration: Integration of AWS services to enhance the application's performance and reliability. Retrieval Augmented Generation (RAG): Application of RAG techniques to facilitate speedy access to medical records, enhancing user experience. Building the Project The development of NoteMD involved several key steps: Planning and Design: Defined the core features for both doctors and patients. Designed user-friendly interfaces to ensure seamless navigation. Backend Development: Set up a robust backend using Node.js and Express. Implemented MongoDB Atlas for data storage, ensuring scalability and security. Implemented a role-based authentication system allowing doctors to ha ev many patients but for each patient to only have one doctor Integrated AWS services to support vector search capabilities. Frontend Development: Developed a responsive frontend using React.js. Ensured real-time updates and interactions for scheduling and prescriptions. Security Implementation: Utilized JSON Web Tokens (JWT) to encrypt user data. Ensured that only authenticated users could access their respective data. Feature Integration: For Doctors: Provided functionalities to write prescriptions, schedule meetings, and follow up with multiple patients on the go. Enabled uploading and storing of medical documents, serving as context for vector searches. For Patients: Allowed viewing of available prescriptions and upcoming scheduled meetings with their assigned doctors. Enabled direct chat with medical records using Retrieval Augmented Generation, powered by MongoDB Atlas vector search on AWS for fast information retrieval. Challenges Faced Building NoteMD was not without its hurdles: Ensuring Data Security: Implementing robust encryption and authentication mechanisms to protect sensitive medical data was paramount and challenging. Integrating Advanced Search Capabilities: Leveraging vector search for efficient retrieval of medical records required in-depth knowledge and seamless integration with AWS and MongoDB Atlas. Balancing Functionality and Usability: Designing features that are both powerful for doctors and intuitive for patients demanded meticulous planning and user feedback. Scalability: Ensuring that the application could handle a growing number of users without compromising performance was a critical focus area. Conclusion NoteMD is more than just a web application; it's a step towards transforming the healthcare experience. By bridging the gap between doctors and patients, enabling efficient communication, and ensuring data security, NoteMD aims to make medical services accessible anytime, anywhere. Enhancing the Healthcare experience one step at a time! Try NoteMD today! <div