---
slug: "hi-u5pk3l"
url: "https://devpost.com/software/hi-u5pk3l"
title: "Chatbot for Class"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 637
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# Chatbot for Class

> Let's bring Wit.ai chatbot to classroom! A teacher's guide for making basic chatbot with students. Provided Covid-19 safety guide bot as an example.

[Devpost](https://devpost.com/software/hi-u5pk3l) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]

**stack** airtable, docusaurus, facebook-messenger, javascript, node.js, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- facebook products used
- challenges we ran into
- accomplishments that we are proud of
- what we've learned
- what's next

## Body

GIF Chatbot in action! Thumbnail! Inspiration "Chatbot for class" was created to help teachers who want to experience the chatbot technology with class. A way to experience basic AI model training Designed for beginners in tech so a wide range of readers could understand and follow the steps Used Covid-19 safety guidelines since it is a topic that every student is familiar with What it does The tutorial: Shows basic setup for the Facebook and Wit.ai App Walks through the Node.js code and shows the sections which are easily adjustable by the reader Brief explanation of model training and NLP The bot itself: Gives a quiz based on the user input. The bot will remember the user's previous answers and give follow up questions. How we built it Throughout the writing of this tutorial, we always tried to think in a reader's viewpoint. The reader persona that we created is a teacher who teaches at Middle/High school and has basic or little knowledge of the technology that we have used. For the Covid-19 chatbot that we created, we basically used Wit.ai to get the utterances of the user. We have trained the model to understand the utterances mentioned below and figure out the intent of getting safety information. Is going to the gym safe? Is it safe to hike? Will working out outdoors make me sick? After training, The bot will ask one of the follow up questions such as: How possible you and people around you will wear a mask? How crowded the place will be? How enclosed the space will be around you? The bot will give the safety information according to user's input. We used CDC official "Daily Activities and Going Out" safety guide for the answers. Facebook Products Used Messenger Platform Wit.ai Facebook for Developers Docusaurus And Facebook Messenger to communicate and work on the article. Since we need to keep the previous message for a follow up question, we used Airtable to store the quiz progress. For privacy reasons, the data is going to be deleted after session expires. We don't store user input data permanently. Challenges we ran into The biggest challenge was to find a right basic scenario for the bot, which will be a clear example what custom input Wit.ai can efficiently process and learn from. To solve this, we've remodeled the dialogue scenario a number of times to find input, best suitable to demonstrate Wit.ai capabilities and its ease of use. Accomplishments that we are proud of We are proud that we have created a tutorial which can make a good impact for teachers who want to bring technology to the classroom. We hope our tutorial inspires teachers and students who are willing to know more about Wit.ai, Node.js coding and basics of NLP. Also, we are grateful that we were able to work as a team despite of 13 hour timezone difference. We synced up a call almost every week to keep on track. It was really meaningful to meet and collaborate with developers in another country through this Hackathon. What we've learned We've learned a lot about Wit.ai and Facebook Messenger Platform capabilities. Also, it was a good chance to discover possibilities with technologies like Glitch and Airtable, make a great use of them and understand them better. Furthermore, we also had a great time doing research on conversational interface design patterns and gradually improving our tutorial to better cover this topic. What's next We want to keep improving "Chatbot for Class" by making it able for readers to add a new intent in Wit.ai and customize the quiz. Also, we are looking forward to making this tutorial more accessible and understandable by showing this to people who have a basic or little knowledge of technologies that we have used and getting feedback from them. <div