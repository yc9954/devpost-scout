---
slug: "skin-ai-zlwdsy"
url: "https://devpost.com/software/skin-ai-zlwdsy"
title: "DermaDetect"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 708
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/developer"
  - "user/government_staff"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DermaDetect

> DermaDetect leverages AI for accessible skin health checks, focusing on affordability and privacy for underserved populations.

[Devpost](https://devpost.com/software/skin-ai-zlwdsy) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[developer]] [[government_staff]] [[patient_family]]
  <sub>weak: clinician</sub>
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** clerk-oauth, convex, flask, framer-motion, infobip-twillio-like, intel-cloud, keras, llm, matplotlib, numpy, opencv, pandas, predictionguard, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dermadetect

## Body

GIF Demo (click to play) Application diagram Technical diagram Landing page (light) User Home (light) Result page (light) SMS Alert sent to user's physician Landing page (dark) User Home (dark) Mobile Ready SMS - 2 Inspiration DermaDetect was born out of a commitment to improve healthcare equity for underrepresented and economically disadvantaged communities, including seniors, other marginalized populations, and those impacted by economic inequality. Recognizing the prohibitive costs and emotional toll of traditional skin cancer screenings, which often result in benign outcomes, we developed an open-source AI-powered application to provide preliminary skin assessments. This innovation aims to reduce financial burdens and emotional stress, offering immediate access to health information and making early detection services more accessible to everyone, regardless of their societal status. What it does AI-powered analysis: Fine-tuned Resnet50 Convolutional Neural Network classifier that predicts skin lesions as benign versus cancerous by leveraging the open-source HAM10000 dataset. Protecting patient data confidentiality: Our application uses OAuth technology (Clerk and Convex) to authenticate and verify users logging into our application, protecting patient data when users upload images and enter protected health information (PHI). Understandable and age-appropriate information: Prediction Guard LLM technology offers clear explanations of results, fostering informed decision-making for users while respecting patient data privacy. Journal entry logging: Using the Convex backend database schema allows users to make multiple journal entries, monitor their skin, and track moles over long periods. Seamless triaging: Direct connection to qualified healthcare providers eliminates unnecessary user anxiety and wait times for concerning cases. How we built it Machine learning model TensorFlow, Keras: Facilitated our model training and model architecture, Python, OpenCV, Prediction Guard LLM, Intel Developer Cloud, Pandas, NumPy, Sklearn, Matplotlib Frontend TypeScript, Convex, React.js, Shadcn (Components), FramerMotion (Animated components), TailwindCSS Backend TypeScript, Convex Database & File storage, Clerk (OAuth User login authentication), Python, Flask, Vite, InfoBip (Twillio-like service) Challenges we ran into We had a lot of trouble cleaning and applying the HAM10000 skin images dataset. Due to long run times, we found it very challenging to make any progress on tuning our model and sorting the data. We eventually started splitting our dataset into smaller batches and training our model on a small amount of data before scaling up which worked around our problem. We also had a lot of trouble normalizing our data, and figuring out how to deal with a large Melanocytic nevi class imbalance. After much trial and error, we were able to correctly apply data augmentation and oversampling methods to address the class imbalance issue. One of our biggest challenges was setting up our backend Flask server. We encountered so many environment errors, and for a large portion of the time, the server was only able to run on one computer. After many Google searches, we persevered and resolved the errors. Accomplishments that we're proud of We are incredibly proud of developing a working open-source, AI-powered application that democratizes access to skin cancer assessments. Tackling the technical challenges of cleaning and applying the HAM10000 skin images dataset, dealing with class imbalances, and normalizing data has been a journey of persistence and innovation. Setting up a secure and reliable backend server was another significant hurdle we overcame. The process taught us the importance of resilience and resourcefulness, as we navigated through numerous environmental errors to achieve a stable and scalable solution that protects patient data confidentiality. Integrating many technologies that were new to a lot of the team such as Clerk for authentication, Convex for user data management, Prediction Guard LLM, and Intel Developer Cloud. Extending beyond the technical domain, reflecting a deep dedication to inclusivity, education, and empowerment in healthcare. What we learned Critical importance of data quality and management in AI-driven applications. The challenges we faced in cleaning and applying the HAM10000 skin images dataset underscored the need for meticulous data preprocessing to ensure AI model accuracy, reliability, and equality. How to Integrate many different new technologies such as Convex, Clerk, Flask, Intel Cloud Development, Prediction Guard LLM, and Infobip to create a seamless and secure user experience. What's next for DermaDetect Finding users to foster future development and feedback. Partnering with healthcare organizations and senior communities for wider adoption. Continuously improving upon data curation, model training, and user experience through ongoing research and development. <div