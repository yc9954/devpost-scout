---
slug: "empower-hack-2-0-project"
url: "https://devpost.com/software/empower-hack-2-0-project"
title: "Scholarship Probability Model"
hackathon: "Empower Hacks 2.0"
organization: "Project: Empower"
winner: true
words: 679
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# Scholarship Probability Model

> Our Scholarship AI Probability Model leverages neural networks to analyze academic profiles and financial data, providing actionable insights to optimize scholarship applications.

[Devpost](https://devpost.com/software/empower-hack-2-0-project) · hackathon [[Empower Hacks 2.0]]

## Facets

**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]]

**stack** matplotlib, numpy, pandas, python, scikit-learn, tensorflow

## Body

Our model's accuracy and loss graphs. Inspiration Our team was motivated to develop the Scholarship AI Probability Model after recognizing the financial hardships faced by first-generation college students, who often struggle with the high costs of higher education. Many students apply for scholarships but are unsure how to optimize their chances of acceptance. We saw an opportunity to leverage advanced AI techniques to address this issue by creating a model that predicts the probability of receiving a scholarship based on a student's academic profile and other relevant factors. Our goal was to develop a tool that could provide actionable insights and enhance the scholarship application process for those in need. What it does Our Scholarship AI Probability Model uses a neural network to estimate the likelihood of a student receiving a scholarship. The model is structured with three layers: an input layer, a hidden layer, and an output layer. The output layer employs a Sigmoid activation function, which converts the model’s output into a percentage representing the probability of scholarship success. To enhance the model’s accuracy, we implemented dropout techniques to prevent overfitting and normalized the data for stable training. The model evaluates various inputs, such as GPA, demographic information, and income level, and uses a point system to rank student profiles based on historical scholarship data. By summing the points and comparing them to past recipients, the model generates a probability score indicating how likely the student is to receive a scholarship. How we built it We built the Scholarship AI Probability Model using Python, employing libraries such as NumPy for mathematical functions and TensorFlow/Keras for implementing the neural network. We researched and found datasets with 100,000 rows, based on available scholarship data and infographics. The model was trained over 50 epochs to maximize accuracy and minimize processing time. Our team conducted extensive research on neural network architectures and activation functions to determine the best configuration for our specific use case. Developing the point system and integrating it with the neural network was a complex task that required both programming and theoretical knowledge from our research. Challenges we ran into One of the main challenges was creating a synthetic dataset that accurately reflected the parameters and trends we wanted to analyze, given the absence of a fitting public dataset. Additionally, fine-tuning the neural network to prevent overfitting while maintaining accuracy was challenging. We also faced difficulties in determining the optimal combination of layers, units, and activation functions for our model. Despite these challenges, our team persisted through multiple iterations and adjustments to refine the model's performance. Accomplishments that we're proud of We are proud of overcoming the technical challenges associated with developing and validating our model. Creating a functioning proof-of-concept with a synthethic dataset was a significant achievement, demonstrating that our neural network can effectively predict scholarship probabilities. We are also pleased with our ability to integrate complex concepts into a practical tool that has the potential to support students in their scholarship applications. This accomplishment stands as a testament to our team’s dedication and problem-solving skills. What we learned Throughout this project, we gained valuable insights into neural network design and implementation, including the importance of data normalization and dropout techniques to prevent overfitting. We also learned about the complexities of designing and evaluating a model with synthetic data and the challenges of translating theoretical concepts into practical applications. Effective collaboration and time management were crucial, especially given the multifaceted nature of the project and the need to balance research, development, and documentation. * What's next for the Scholarship Probability AI * Looking ahead, our team plans to enhance the model's accuracy and realism by acquiring and integrating a more accurate and comprehensive public datasets. We aim to explore advanced neural network architectures and optimize the point system for greater precision. Additionally, we are considering developing a user-friendly app to streamline the input process and improve accessibility for applicants. By addressing these areas, we hope to further refine the model and increase its impact on helping students secure the financial aid they need for higher education. <div