---
slug: "job-search-kbm7z2"
url: "https://devpost.com/software/job-search-kbm7z2"
title: "Job Search"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 662
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/web_dom"
---

# Job Search

> Find the perfect job through Alexa and get results sent to your cell!

[Devpost](https://devpost.com/software/job-search-kbm7z2) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[web_dom]]

**stack** amazon-web-services, ask-sdk, conversationsapi, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for job search

## Body

Job Search splash intro/outro Phone number prompt Job type query screen Job found view Inspiration The process of job searching can be tedious and slow, we wanted to create something which speeds up this process and makes it more intuitive. By searching through voice, the user avoids having to navigate a website, click tiny check boxes and scroll through annoying drop down menus. We also found that when searching online, jobs can get lost in a clutter of emails and tabs, so we wanted to avoid this by sending messages to the user by SMS. What it does Job Search will query you for these four parameters: Job type Location Salary Full time or part time Once these details have been given, Job Search will find jobs meeting those criteria and then prompt you for your cell number, it will then send you a text message to your cell with the job results! How I built it We developed the skill mostly in the Alexa developer console, using the interface provided by the Conversations API. We created lots of dialogs to handle the skill flow and we built an API definition for the job search, which is managed through an AWS lambda function, written in NodeJS deployed through the ASK-CLI. We also created utterance sets in the console which represented different ways users could interact with the skill, these utterance sets were built off the values in our interaction model, which contained both custom slot types (our job list slot) and then built-in slots such as AMAZON.PhoneNumber. The views were built using APL, we mostly used features available in 1.0, for the audio in skill we used APLA. We used the SerpAPI to perform our job search, and then the Twilio node package to send our SMS messages. Challenges I ran into We initially found debugging difficult since the interactions within the conversations API weren't hitting our lambda endpoint, but we found that following the advice offered by the Amazon office hours via Twitch really helped us find the best approach. We initially had trouble finding an appropriate Job Search API, since the public job searching API's were too specific, offering information which was far too granular for most users, i.e. API's purely for careers in engineering. Eventually we found the Search Engine Results Page API (SerpAPI), which supported a wide range of jobs. Accomplishments that I'm proud of We're proud of the way we planned out the flow of the skill, thinking about different ways users may approach searching for certain parameters, for example, when gathering phone numbers we came across the following friction points: User says number wrong User gives invalid number User gives number in varying lengths Solutions We built an intent which allows the user to edit misheard numbers, so this flow... Alexa : Please read out your phone number User : 800 499 Alexa : 800 495 User : No that's 800 499! Alexa : OK, that's 800 499 ...Is possible! We used NPM packages which validate phone numbers based on region We save the previous utterances in a session variable and concatenate them on each user request. What I learned In testing we found that the flow users take in a skill is rarely linear and they will often deviate off the "happy path" to change something or add a new parameter. The conversations API has taught us to have a more lateral mindset when it comes to developing skills. What's next for Job Search We'd like to further enhance our conversational flow, building more dialogs to ensure that we have an excellent coverage of all potential conversational paths. We'd like to expand the breadth of parameters that job search can accept to allow for more intelligent job searching, We also wanted to add more API's that provide more depth in certain careers. To enable permissions to request and access user email addresses, so we can send emails about jobs that match the users criteria. <div