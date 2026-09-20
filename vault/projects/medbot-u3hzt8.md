---
slug: "medbot-u3hzt8"
url: "https://devpost.com/software/medbot-u3hzt8"
title: "care.ai"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 502
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
---

# care.ai

> For go-to assistant for everything in primary healthcare

[Devpost](https://devpost.com/software/medbot-u3hzt8) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[developer]] [[patient_family]]
**substrate** [[code_repository]]

**stack** amazon-web-services, c++, fastapi, firebase, intel, intel-cloud, java, machine-learning, monsterapi, postman, python, reflex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for care.ai

## Body

Inspiration Care.ai was inspired by our self-conducted study involving 60 families and 23 smart devices, focusing on elderly healthcare. Over three months, despite various technologies, families preferred the simplicity of voice-activated assistants like Alexa. This preference led us to develop an intuitive, user-friendly AI healthcare chatbot tailored to everyday needs. What it does Care.ai, an AI healthcare chatbot, leverages custom-trained Large Language Models (LLMs) and visual recognition technology hosted on the Intel Cloud for robust processing power. These models, refined and accessible via Hugging Face, underwent further fine-tuning through MonsterAPI, enhancing their accuracy and responsiveness to medical queries. The web application, powered by the Reflex library, provides a seamless and intuitive front-end experience, making it easy for users to interact with and benefit from the chatbot's capabilities. Care.ai supports real-time data analytics and critical care necessary for humans. How we built it We built our AI healthcare chatbot by training LLMs and visual recognition systems on the Intel Cloud, then hosting and fine-tuning these models on Hugging Face with MonsterAPI. The chatbot's user-friendly web interface was developed using the Reflex library, creating a seamless user interaction platform. For data collection, We researched datasets and performed literature review We used the pre-training data for developing and fine-tuning our LLM and visual models We collect live data readings using sensors to test against our trained models We categorized our project into three parts: Interactive Language Models: We developed deep learning models on Intel Developer Cloud and fine-tuned our Hugging Face hosted models using MonsterAPI. We further used Reflex Library to be the face of Care.ai and create a seamless platform. Embedded Sensor Networks: Developed our IoT sensors to track the real-time data and test our LLVMs on the captured data readings. Compliance and Security Components: Intel Developer Cloud to extract emotions and de-identify patient's voice to be HIPAA Challenges we ran into Integrating new technologies posed significant challenges, including optimizing model performance on the Intel Cloud, ensuring seamless model fine-tuning via MonsterAPI and achieving intuitive user interaction through the Reflex library. Balancing technical complexity with user-friendliness and maintaining data privacy and security were among the key hurdles we navigated. Accomplishments that we're proud of We're proud of creating a user-centric AI healthcare chatbot that combines advanced LLMs and visual recognition hosted on the cutting-edge Intel Cloud. Successfully fine-tuning these models on Hugging Face and integrating them with a Reflex-powered interface showcases our technical achievement. Our commitment to privacy, security, and intuitive design has set a new standard in accessible home healthcare solutions. What we learned We learned the importance of integrating advanced AI with user-friendly interfaces for healthcare. Balancing technical innovation with accessibility, the intricacies of cloud hosting, model fine-tuning, and ensuring data privacy were key lessons in developing an effective, secure, and intuitive AI healthcare chatbot. What's next for care.ai Next, Care.ai is expanding its disease recognition capabilities, enhancing user interaction with natural language processing improvements, and exploring partnerships for broader deployment in healthcare systems to revolutionize home healthcare access and efficiency. <div