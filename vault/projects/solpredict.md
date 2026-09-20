---
slug: "solpredict"
url: "https://devpost.com/software/solpredict"
title: "SolPredict"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 436
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "user/researcher"
  - "substrate/structured_db"
---

# SolPredict

> "Your AI-powered solubility companion. Instantly predict the solubility of any solute-solvent pair, streamlining research and unlocking the secrets of solution chemistry at the click of a button!"

[Devpost](https://devpost.com/software/solpredict) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**user** [[researcher]]
**substrate** [[structured_db]]

**stack** docker, fastai, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for solpredict

## Body

Inspiration The spark for SoluPredict was ignited by the quest to simplify the complex and often tedious task of determining solute-solvent solubility—a critical process in various industries, from pharmaceuticals to environmental science. Our team was inspired by the potential to harness AI to revolutionize how researchers and chemists approach solubility, aiming to convert hours of lab work into mere seconds of computation. What it does SoluPredict is an intuitive, AI-driven application that predicts the solubility of any given solute in a chosen solvent. It provides quick and reliable solubility data, which is crucial for formulating drugs, designing chemical processes, or assessing environmental impacts. By inputting the chemical structures or identifiers of the solute and solvent, users receive an instant solubility profile, saving valuable time and resources. How we built it We built SoluPredict using Docker to containerize our application, ensuring it can be seamlessly deployed and run on any platform. The backend leverages FastAI, which provides a deep learning framework that is both flexible and powerful, allowing us to train our AI model with a diverse dataset of chemical interactions. The front end is crafted for simplicity, making it accessible to users with varying levels of technical expertise. Challenges we ran into One of the significant challenges was curating a comprehensive and accurate dataset to train our model. Solubility data can be inconsistent, and gathering reliable information was a monumental task. Another challenge was optimizing the model for quick predictions without compromising on accuracy, requiring numerous iterations and fine-tuning. Accomplishments that we're proud of We are proud of developing a tool that democratizes access to solubility data, potentially accelerating research and development in multiple fields. Despite the challenges, our model achieves a high degree of accuracy and can provide solubility predictions in real-time. We are also proud of the robustness and scalability of SoluPredict, thanks to our use of Docker and FastAI. What we learned Throughout the development of SoluPredict, we learned that interdisciplinary collaboration is key to solving complex problems. Combining knowledge from chemistry, data science, and software engineering led to a product that could make a significant impact. We also learned the importance of user experience—making complex AI technology accessible and user-friendly. What's next for SolPredict Moving forward, we aim to expand SoluPredict's database to include more exotic and diverse chemicals, increasing its utility across various industries. We also plan to integrate predictive models for other properties like toxicity and reactivity, evolving SoluPredict into a comprehensive chemical prediction platform. Additionally, we look to foster a community where users can contribute data, further refining our AI models and pushing the boundaries of collaborative science. <div