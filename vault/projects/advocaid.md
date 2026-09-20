---
slug: "advocaid"
url: "https://devpost.com/software/advocaid"
title: "AdvocAID"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 727
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AdvocAID

> AdvocAID, a web app with a GPT-2 and sentiment analysis model, provides personalized AI-generated feedback and tips for women to help build confidence, self-advocacy, and overcome workplace barriers.

[Devpost](https://devpost.com/software/advocaid) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** bootstrap, css, custom-api-routes, flask, google-fonts, gpt-2, html, hugging-face-transformers-api, javascript, jsonl, python, pytorch, scikit-learn, textblob

## How they structured the write-up

- my inspiration
- what advocaid does
- how i built advocaid
- use of machine learning
- challenges i faced
- accomplishments i’m proud of!
- what i learned
- what's next for advocaid

## Body

My Inspiration I often wondered why so many talented, highly qualified women face greater challenges climbing the ranks in the workplace, as opposed to their male counterparts. I realized it stems from societal norms that tell women to be complacent in their position and avoid speaking up for themselves, while fostering assertiveness and confidence in men. This imbalance not only holds women back from their full potential, but perpetuates workplace inequality, furthering the gender gap in professional settings. So, I developed AdvocAID—a platform to empower women and to help them advocate for themselves, and achieve the success they rightfully deserve. What AdvocAID does AdvocAID is a web app designed to help women in the workplace improve their self-advocacy skills. It utilizes a custom-trained GPT-2 model to generate personalized feedback based on real-world workplace scenarios. Through sentiment analysis, AdvocAID evaluates the confidence level of users' responses and provides actionable advice on how to assert themselves more confidently while maintaining professionalism. The app also features expert advice from women who have navigated similar workplace challenges, providing users with relatable role models and motivational insights. How I Built AdvocAID I used a GPT-2 pre-trained model for natural language processing, fine-tuning it on a custom dataset of workplace scenarios covering topics like salary negotiations, workload discussions, and work-life balance. During training, I optimized hyperparameters such as learning rate and batch size to enhance the model's ability to generate actionable and context-aware feedback. For sentiment analysis, I integrated TextBlob to assess user input and classify confidence levels. I built the backend using Flask to load the fine-tuned model, handle user inputs, and provide AI-generated feedback via API routes. Lastly, I created an intuitive, user-friendly front-end with HTML, CSS, and JavaScript, incorporating interactive features like a scenario carousel and expert advice videos to ensure a seamless user experience. Use of Machine Learning In this project, I applied the concepts of machine learning through a custom-trained GPT-2 model. This model was fine-tuned on workplace conversations to generate personalized feedback that helps users assert themselves more confidently. Sentiment analysis via TextBlob helps assess the tone of user responses, allowing the app to gauge the user’s confidence level and provide tailored advice. The combination of these AI tools ensures that feedback is both personalized and constructive, empowering women to refine their communication skills in real time. Challenges I Faced One of the biggest challenges in developing AdvocAID was finding a dataset that met my specific needs. I found that existing datasets on workplace interactions and conversations lacked the detail and focus required for empowering women and their confidence. To address this, I created a custom dataset by drawing from personal interactions, advice from experts online, and related datasets. This process required extensive research, organization, and refinement to ensure the data was both diverse and relevant to real-world workplace scenarios, but I’m proud I got it to work! Accomplishments I’m Proud Of! I’m super proud of being able to successfully train my custom GPT-2 model! After extensive tuning of the hyperparameters, I optimized the model to generate feedback that was both accurate and actionable. One of the highlights was reducing the epoch loss to an ideal 0.2, indicating the model was learning efficiently and adapting well to the data. This achievement validated the effort put into creating my custom dataset and fine-tuning the training process, paving the way for AdvocAID’s functionality. What I Learned Through this project, I learned a lot about natural language processing, machine learning model fine-tuning, and sentiment analysis. I also gained valuable insights into creating a web application from scratch, including both the back-end development with Flask and front-end design with HTML/CSS/JS. Working with the GPT-2 and sentiment analysis model and fine-tuning it to generate relevant workplace advice was a challenging yet rewarding experience. Most importantly, I learned the power of using technology to address social issues and empower women in meaningful ways. What's Next for AdvocAID In the future, I plan to expand AdvocAID by adding more workplace scenarios and incorporating additional AI-driven features, such as voice tone analysis to provide insights into how users can modulate their speech for greater impact. Additionally, I aim to integrate video analysis to evaluate body language and movements, offering a comprehensive understanding of nonverbal communication. These enhancements to the app’s sentiment analysis will focus on delivering more detailed feedback tailored to users’ specific needs. <div