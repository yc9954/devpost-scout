---
slug: "unimate-7s9kn2"
url: "https://devpost.com/software/unimate-7s9kn2"
title: "UniMate"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 451
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# UniMate

> Your ultimate university companion.

[Devpost](https://devpost.com/software/unimate-7s9kn2) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** cloudservice-render, css, deeplearning, frameworks-flask, html, javascript, languages-python, naturallanguageprocessing, neuralnetworks, others-machinelearning, platforms-render, vectorization

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Query-Answer Chatbot Interface Query-Answer Inspiration Since when I join my university(1st Year) I felt difficulties in finding the places in the university like library, hostel, canteens etc. because university is big .So for the guidance I need to ask my seniors and others So I thought to make a chatbot to help my further upcoming junior mates so that they will not get through the same problem. What it does It basically answers the queries of 1st year students. It can answer the following queries: 1."Hi", "Hello", "Hey", "Good morning", "Good afternoon", "Good evening", 2."What is the syllabus for my course?" 3."Where can I find my timetable?" 4".What subjects will I study?" 5."Who is my mentor?" 6."Where is the library?", "Can you tell me the location of library?", "Where is library located?" 7."How can I access the gym?" 8."Where is gym?" 9."Where is the cafeteria?" 10."Are there study rooms available?" 11."What programming languages will I learn?" 12."Who are the professors for my department?" 13."Is there a lab for my domain?" 14."Can I get domain related project guidance?" 15."What clubs can I join?", "Is there a music club?" 16."Are there sports facilities?" 17."How do I participate in cultural events?" 18."Where is the hostel?" 19."What are the hostel rules?", "Is there a curfew for hostels?" 20."How can I report maintenance issues?" 21."How do I pay my fees?" 22."Are there scholarships available?" 23."Can I get a fee receipt?" 24."I feel sick", "Who do I contact in an emergency?" 25."How do I report harassment?" 26."Bye", "Goodbye", "See you later", "Thanks, bye" How we built it We built it using following concepts: A. Natural Language Processing 1.Tokenization : word_tokenize Stemming : Porter Stemmer Vectorization : Bag of words B. Neural Network 1.Artificial Neural Network C. Deep Learning 1.Activation Function : ReLU(For hidden layer) Softmax(For Output layer) 2.Loss Function : CrossEntropyLoss 3.Optimizer : Adam D. Machine Learning 1.Model Creation(ANN) 2.Output prediction E. Flask + HTML + CSS 1.For Front End F. Javascript 1.For interactivity G. Hosting 1.render.com ## Challenges we ran into 1.Low Accuracy in the beginning(73% in beginning to 99% final) 2.Misalignment of data(Wrong Prediction) 3.Deployment ## Accomplishments that we're proud of Getting almost close to 100 % accuracy with net zero loss after 600 epochs for our existing dataset make us feel proud. ## What we learned We learned a lot of things from data cleaning to deployment. Mostly we learned in training part how to achieve higher accuracy. ## What's next for UniMate Actually we are trying to embed the features of generative AI in our existing chatbot so that it can answers any queries. In short we want to change it from predefined model to LLM based model as soon as possible. <div