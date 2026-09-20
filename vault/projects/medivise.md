---
slug: "medivise"
url: "https://devpost.com/software/medivise"
title: "Medivise"
hackathon: "Databricks Generative AI World Cup"
organization: "Databricks"
winner: true
words: 994
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Medivise

> Medivise tackles polypharmacy by streamlining medication management with OCR, drug to drug interaction and food interactions, and detailed reports for safer healthcare.

[Devpost](https://devpost.com/software/medivise) · hackathon [[Databricks Generative AI World Cup]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[general_public]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]

**stack** databricks, dbrx, fastapi, ios, kubernetes, langchain, mobile, mongodb, rag

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medivise

## Body

Architecture Key Functionalities Add Medications Easily Check Drug-Drug Interactions Monitor Food Interactions Automated Health Reports Inspiration Inspired by the growing challenge of polypharmacy, particularly among the elderly and those managing multiple health conditions, Medivise is designed to reduce the risk of adverse drug reactions (ADRs), which are a leading cause of hospital admissions and healthcare complications. Recognizing that over 40% of older adults in the U.S. take five or more medications, our app aims to provide a vital service by ensuring that all medications are managed safely and effectively, thereby decreasing the potential for harmful interactions and improving overall healthcare outcomes. What it does Here you can find the key features: Add Medications Easily: Quickly add medications by snapping a photo of your medication labels with your smartphone. Our OCR technology will automatically extract the text and fill in your medication details, simplifying the creation of your medication list. Check Drug-Drug Interactions: Ensure your safety by checking for potential drug interactions within the app. Whether you consult saved medications or enter new ones, Medivise helps you identify harmful drug combinations. Monitor Food Interactions: Stay informed about how certain foods may affect your medications. Medivise offers comprehensive details on food-drug interactions to help maintain an optimal diet that supports your treatment. Automated Health Reports: Generate detailed health reports automatically, including all your medication information in a PDF format. Share these reports with your doctor to enhance discussions during your medical appointments. How we built it To build Medivise for the hackathon, our team utilized a mix of advanced technologies and smart design choices aimed at addressing the specific needs of older users managing multiple medications. We developed a robust backend using MongoDB hosted on Google Kubernetes Engine (GKE) for scalable and secure data management. Our integration with Databricks (using DBRX and BGE) facilitated precise drug information retrieval, while MongoDB Vector Search was crucial for efficiently processing complex queries related to drug interactions. Specifically, we implemented a Retrieval-Augmented Generation (RAG) model that leverages content from "Stockley's Drug Interactions" book to power the drug-to-drug interactions feature, ensuring accurate and relevant information is always at the user's fingertips. On the front end, we chose Swift to develop the mobile application, focusing on creating a smooth and intuitive interface that is easy for older adults to navigate. FastAPI was used to build responsive, asynchronous API services that seamlessly connect our mobile interface with the backend, ensuring quick data processing and a fluid user experience. Although we did not conduct user testing due to the hackathon's constraints, each feature was designed with a clear focus on user-centered principles. Helm charts on GKE were employed to manage deployments effectively, guaranteeing that Medivise operates reliably, aiding users in safely managing their medications. This approach underscores our commitment to leveraging cutting-edge technology to enhance healthcare outcomes for those at greatest risk from polypharmacy. Challenges we ran into During the development of Medivise, we faced several significant challenges. Crafting a user-friendly interface tailored for older adults required meticulous attention to design simplicity and accessibility to ensure ease of use. Integrating a Retrieval-Augmented Generation (RAG) system to enhance the Databricks (using DBRX and BGE) API's capabilities posed another technical hurdle; we needed to effectively incorporate the extensive drug interaction data from "Stockley's Drug Interactions" into our system to provide reliable drug-to-drug interaction information. Additionally, building an infrastructure that could scale easily, leveraging Kubernetes, presented complexities in ensuring seamless scalability and robustness to handle varying loads without compromising performance. Accomplishments that we're proud of We are immensely proud of several key accomplishments with Medivise. Foremost, we successfully created an extremely user-friendly interface, specifically tailored for older adults, which simplifies the management of multiple medications and enhances accessibility. This focus on ease of use ensures that our app can be operated by individuals with varying levels of tech-savvy, making a real difference in their daily health management. Additionally, we integrated expert-driven, reliable content from "Stockley's Drug Interactions," empowering our app with a high level of accuracy through the innovative use of a Retrieval-Augmented Generation system. This blend of expert information and advanced technology allows Medivise to offer not just convenience but also confidence to its users in managing their medication safely and effectively. What we learned Our team used Kubernetes to scale generative AI for Medivise, efficiently managing resources and maintaining performance under different loads. We integrated the Databricks (using DBRX and BGE) API with Retrieval-Augmented Generation (RAG) techniques to improve the app's drug interaction data, enhancing reliability and utility. The project involved adapting AI functionalities for mobile platforms, ensuring smooth operation on smaller devices with a user-friendly interface. Overall, this experience expanded our technical skills and deepened our understanding of AI applications in healthcare. What's next for Medivise for Looking forward, Medivise has several exciting enhancements on the horizon to further improve its functionality and reach: Enhanced Interaction Analysis: We plan to extend the Retrieval-Augmented Generation (RAG) model to cover drug-to-food interactions. This will enable the app to provide even more comprehensive guidance on potential interactions, helping users manage their diets effectively alongside their medications. Web Application Development: To make Medivise more accessible, we aim to develop a web application that consumers can use to interact with the backend directly. This will provide an alternative to the mobile app, making the service available on a broader range of devices and platforms. Multilingual Support: We recognize the need to improve our app’s performance in languages other than English. Moving forward, we will enhance language support to ensure that Medivise delivers accurate and reliable functionality across various languages, expanding its usability worldwide. Advanced Splitting Techniques: Leveraging technologies like LangChain, we will improve our text splitting techniques. This will refine the app's ability to process and analyze text more accurately, particularly in handling complex inputs from OCR and user interactions. These improvements will not only enhance Medivise's current capabilities but also broaden its applicability and ease of use, making it an even more indispensable tool in healthcare management. <div