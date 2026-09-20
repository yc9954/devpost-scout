---
slug: "pair-and-aid-parental-aid"
url: "https://devpost.com/software/pair-and-aid-parental-aid"
title: "PAIR AND AID - Parental Aid"
hackathon: "Garuda Hacks 2020"
winner: true
words: 897
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# PAIR AND AID - Parental Aid

> One-click for a slick care for your child's health and education.

[Devpost](https://devpost.com/software/pair-and-aid-parental-aid) · hackathon [[Garuda Hacks 2020]]

## Facets

**domain** [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** api, azure, bubble, certbot, express.js, node.js, pm2, postgresql, ubuntu

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pair and aid - parental aid
- tracks this project is intended for

## Body

Inspiration Every parent wants the best for their children and we understand how struggling parents nowadays could be to care for their children. In a wider scale, a country's future depends on the quality of the younger generation. We develop 'Pair and Aid' to help Indonesian children to be healthier, happier, and more well-prepared to fight for their dreams, via peer tutoring, alumni network, and health monitoring. Peer tutoring Children speak with their own language and it's often hard to understand by adults. Through peer learning and support group, we believe that they can achieve better and more sustainable learning curve, in a more convenient learning atmosphere. Moreover, having experience in teaching their peers can boost children's confidence and train their problem-solving skills, which both will be useful for their future. Alumni network The path to the future is sometimes uncertain and intimidating. We'd like to reduce children's anxiety by creating a communication media, connecting them to the previous alumni from their schools. This way, alumni can share 1) their experience, 2) the challenges that they faced, and 3) well-targeted advice for the children who will follow on their path. Health calculator To be successful in the future, children need to be healthy and physically fit. We provide a health calculator to take into consideration the risks they possess now and customised lifestyle-based intervention that they could follow. What it does Our web application is divided into four main features, which are listed below: STUDY BUDDY - a peer to peer based learning platform where one could find a peer tutor based on their expertise and level of education, this is supported by an inbuilt messaging platform and dynamic link to collaborative whiteboard using Miro. FRIENDS FOREVER - a social platform where one could connect with seniors and alumni of their school. HEALTH CALCULATOR - the idea is to build a model which could stratify contemporary health status and estimate future metabolic risk. Due to limited time, we provide in the app prototype a health monitoring tool in the form of BMI calculator where both children and adults can submit the data needed (sex, weight, height, age) which then will return as BMI score, BMI classification (underweight, normal, overweight, obese), and finally customised lifestyle-based recommendations according to the BMI classification. While adults BMI scores are according to the Asia Pacific standard, children BMI classification is based on WHO growth standard (age- and sex-matched percentiles). KNOW YOU BETTER - a tool to let children understand themselves (under development), will mainly include relevant psychological tests. How I built it Our web application is built using components listed below: Bubble - used to build the front end of the application. App logo and design are integrated into our app using Bubble Design feature. Implement UI flow using Bubble Workflow feature and associated logical flow functionalities. Connected to Node.js below using Bubble's builtin REST API connector plugin. Used the builtin database for account management and managing associated user data. Used the builtin deployment feature to generate a production-ready app. Node.js - used to build the API service utilized by some functionalities inside our Bubble app. Supported by Express.js for routing and structured using MVC (Model-View-Controller) design pattern. Used Sequelize ORM for connection to the underlying PostgreSQL database. Used pm2 as the process production manager. Used certbot to generate certificate and Node.js builtin HTTPS library to provide TLS-secured API endpoints. PostgreSQL - used for storing converted CSV data that is utilized as a basis for BMI calculation in our Health Calculator service. Azure - used to host our API service (virtual machine) and PostgreSQL database (Azure Database for PostgreSQL). Challenges I ran into Below is the list of challenges that we ran into: Remote team work involving 1 team mate based in Australia and another team mate residing in the UK. This time difference was the biggest challenge, especially in coordinating meetings and working schedules. Not too specific problem scopes leading to many potential ideas to explore further. Our team spent quite a long time to shortlist the most feasible idea. No assigned mentor to guide us during the process. Too limited time to execute the idea into a real-life setting prototype. Accomplishments that I'm proud of We’re proud that as a team we could invent this novel idea together as an one-stop app that comprehensively address children’s needs and assist parents to help their children achieving their dreams. Moreover, in only 36 hours, we can effectively work together as a team although not all of us reside in the same geographical locations. We’re pleased with the outcome that we’ve achieved so far and we believe the complete execution of this idea would be beneficial for both children and parents. What I learned Good organisational skills and tasks delegation among team members. Time management, specifically in breaking it down and deciding task priorities. Learning several new applications, especially bubble.io, loom. What's next for PAIR AND AID - Parental Aid Here are things that we like to improve upon: Further development to “Know-you better” feature by incorporating the relevant psychological tests into the app. More input to databases in all four main services. Testing the app to the potential users and getting feedback to improve the app even more. Tracks this project is intended for Best Health Hack Best Education Hack Bubble: Best No-Code Hack using Bubble.io Best use of Microsoft Azure <div