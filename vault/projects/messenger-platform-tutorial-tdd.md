---
slug: "messenger-platform-tutorial-tdd"
url: "https://devpost.com/software/messenger-platform-tutorial-tdd"
title: "Messenger Platform Tutorial (TDD Approach)"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 570
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
---

# Messenger Platform Tutorial (TDD Approach)

> A 2 in 1 tutorial, learners will learn about the messenger platform & get familiar with Test Driven Development by using pre-made red state tests for each lesson.

[Devpost](https://devpost.com/software/messenger-platform-tutorial-tdd) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**user** [[educator_student]]

**stack** bash, docker, express.js, facebook-messenger, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for messenger platform tutorial (tdd)

## Body

RED X Green TESTS TDD Inspiration First of all, I am personally attached to the messenger platform as I am one of the participants (and luckily winners) of the MEA Bots For Messenger Challange held back in 2017, it was an awesome experience from all perspectives. On the other hand, I do believe that Test Driven Development is underserved when it comes to tutorials, hence I thought it would be a cool idea to mix and match both concepts. I believe the TDD approach will help learners learn faster since they have micro-goals to achieve that in hand will serve the whole end goal of the tutorial, also it will make the tutorial more interactive and fun. What it does This tutorial cover the whole life cycle of a message in 5 different lessons. A life cycle typically looks like this 👇 "The conversation life cycle starts when a user sends message to your chatbot, the message received in the platform's servers and delivered to you through the Webhooks you have implemented (Lesson_1 & Lesson_2) . In your webhooks, you will parse the webhook event (Lesson_3) , build your app logic (Lesson_5) , and then send the message back through the platform's API (Lesson_4) . Finally, the platform will deliver the messages to your user on your behalf." The goal in each lesson is for learner to write some code to move tests from red state to green state , hence finish one part of the application. After finishing all the lessons & sub lessons, the learner will have a complete chatbot in his/her hand now and have learned the main concepts the interactive way. How I built it Used javascript, shell scripts & docker to provide users with this tutorial experience. In order to make it easier for the learner to run each lesson's test and be super focused on moving them from red state to green state (TDD Approach), I have developed a shell script lesson runner specifically for this tutorial. Challenges I ran into The overall learning experience and how to make it both fun and interactive. Accomplishments that I'm proud of Having learners experience a double benefit from this tutorial. (learning about the messenger platform from one hand & getting familiar with TDD on the other hand) What's next for Messenger Platform Tutorial (TDD) I am planning to make it a 3 in 1 tutorial by adding Wit.ai to produce a real-life chatbot example. [Global Round] | New Lessons Added For the Global Submission I have added 3 more lessons to my tutorial. As planned I have introduced Wit.ai to the tutorial to make it a 3 in 1 tutorial. The idea behind introducing Wit.ai is the versatility of the platform's built in NLP feature and the ability of Natively supporting customized Wit.ai App from within the platform. This feature is the one that I like the most from the platform as it have saved me a lot of time in integrating Wit.ai in my old projects, hence, I thought that including it in my tutorial would give an extra value to the tutorial followers, as it will show them how they can easily & implicitly add wit.ai support to their chatbots. The 3 added lessons are: 1- Built-In Nlp Feature as lesson 6. 2- Customizing Wit.ai and use it in the chatbot as lesson 7. 3- Appendix lesson on setting up the Facebook App. <div