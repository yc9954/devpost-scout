---
slug: "bytesense"
url: "https://devpost.com/software/bytesense"
title: "BYTEsense"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 809
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# BYTEsense

> Taste Life, Byte by Byte!

[Devpost](https://devpost.com/software/bytesense) · hackathon [[Hack the North 2023]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]]
**substrate** [[structured_db]]

**stack** cohere, css3, flask, html5, javascript, openai, python, replit, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we are proud of:
- what we learned:
- what’s next for bytesense:

## Body

Logo! Dashboard Preview Inspiration Among our group, we noticed we all know at least one person, who despite seeking medical and nutritional support, suffers from some unidentified food allergy. Seeing people struggle to maintain a healthy diet while "dancing" around foods that they are unsure if they should eat inspired us to do something about it; build BYTEsense. What it does BYTEsense is an AI powered tool which personalizes itself to a users individual dietary needs. First, you tell the app what foods you ate, and rate your experience afterwards on a scale of 1-3 - The app then breaks down the food into its individual ingredients, remembers how your experience with them, and stores them to be referenced later. Then, after a sufficient amount of data has been collected, you can use the app to predict how NEW foods can affect you through our "How will I feel if I consume..." function! How we built it The web app consists of two main functions, the training and the predicting functions. The training function was built beginning with the receiving of a food and an associated rating. This is then passed on through the OpenAI API to be broken apart to its individual ingredients through ChatGPT's chatting abilities. These ingredients, and their associated ratings, are then saved onto an SQL database which contains all known associations to date. Furthermore , there is always a possibility that two different dishes share an ingredient, but your experience is fully different! How do we adjust for that? Well naturally, that would imply that this ingredient is not the significant irritator, and we adjust the ratings according to both data points. Finally, the prediction function of the web app utilizes Cohere's AI endpoints to complete the predictions. Through use of Cohere's classify endpoint, we are able to train an algorithm which can classify a new dish into any of the three aforementioned categories, with relation to the previously acquired data! The project was all built on Replit, allowing for us to collaborate and host it all in the same place! Challenges we ran into We ran into many challenges over the course of the project. First, it began with our original plan of action being completely unusable after seeing updates to Cohere's API, effectively removing the custom embed models for classification and rerank. But that did not stop us! We readjusted, re-planned, and kept on it! Our next biggest problem was the coders nightmare, a tiny syntax error in our SQLite code which continuously that crashed our entire program. We spent over an hour locating the bug, and even more trying to figure out the issue (it was a wrong data type.). And our final immense issue came quite literally out of the blue, previously, we utilized Cohere's new Coral chatbot to identify ingredients in the various input, but, due to an apparent glitch in the responses - we got our responses sent over 15 times each prompt - we had made a last minute jump to OpenAI! Once we got past those, most other things seemed like a piece of cake - there were a lot of pieces - but we're happy to present the finished product! Accomplishments we are proud of: There are many things that we as a team are proud of, from overcoming trials and tribulations, refusing sleep for nearly two days, and most importantly, producing a finished product. We are proud to see just how far we have come, from having no idea how to even approach LLM, to running a program utilizing TWO different ones. But most importantly, I think we are all proud of creating a product that really has potential to help people, using technology to better people's lives is something to be very proud of doing! What we learned: What did we learn? Well, that depends who you ask! I feel like each member of the team learnt an unbelievable amount, whether it be from each other or individually. For instance, I learnt a lot about flask and front end development from working with a proficient teammate, and I hope I gave something to learn from too! Even more so, throughout the weekend we attended many workshops, ranging from ML, to LLM, Replit, and so many others, that even if we didn't use what we learnt there in this project, I have no doubt it will appear in a next! What’s next for BYTEsense: All of us in the team honestly believe that BYTEsense has reached a level which is not only functional, but viable. As we keep on going all that is left is tidying up and cleaning some code and a potentially market ready app could be born! Who knows, maybe we'll be a sponsor one day! But either way, I am definitely using a copy when I get back home! <div