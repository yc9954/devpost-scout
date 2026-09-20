---
slug: "the-healing-power-of-telling-your-story"
url: "https://devpost.com/software/the-healing-power-of-telling-your-story"
title: "The Healing Power of Telling Your Story"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 662
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
---

# The Healing Power of Telling Your Story

> They share their journey to champion hope.

[Devpost](https://devpost.com/software/the-healing-power-of-telling-your-story) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[patient_family]]

**stack** amazon-comprehension, amazon-translation, aws-api-gateway, aws-cognito, aws-lambda, aws-rds, dart, flutter, mysql, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for the healing power of telling your story
- try it out

## Body

Inspiration Many diseases are treatable but not curable. Living with such disease is an ongoing learning experience for patients and families. They share their journey to champion hope. What it does This application is a platform giving patients and parents needed tool to share their stories and reach out to the community. There is many portals & community support the same idea. However all those platforms only support local community, where patient only contact with others who talk the same language. Using AWS AI services we enhance the idea to build bigger community not limited to nation or language. Patient Stories from Around the World. User can see all other users post, seeing the recent posts first. User can add his posts. Posts can contains patient story, milestones in his journey, feedback (about certain hospital, clinic, doctor,..), asking for advise or share his experience with others. Add comments to other posts, give a hand, advise, lesson learned or at least supportive words Search in other stories to get posts talked in certain topic. How I built it It is mobile application developed by Flutter (cross mobile development platform). For user registration and authentication I used AWS Cognition Stories saved in AWS RDS mysql DB To extract keywords from stories, Amazon Comprehension is used. Those keywords are used to facilitate user search Translation between Arabic, English & french is done using Amazon Translation. Translation is done for stories and extracted keywords. Challenges I ran into Application in current phase support 3 languages: Arabic, French & English. Architect solution that can give good performance while translating user posts from his original language to the other 2 languages and how user can search using his languages in posts (from all language) and return to him immediately. This can be achieved by Extract keywords from the post (in case of English & french or by translating Arabic post to English then extract the keywords) Translating the post & keywords to the other 2 languages Then when user inquire the timeline (or inquire based on search query), data will be retrieved quickly as translation done once while adding Accomplishments that I'm proud of From business perspective: I'm very proud to do anything that can support not curable patient even if help is a small thing. In first days of disease discovery, patient want a lot of information not from Doctors but from other patient has the same disease. They want to hear from them, ask them and feel they are not alone. After while this same patient, will always feel that he wants to help new patients and give him advise and support. From technical perspective: Although AWS provide SDK and resources (for android, iOS, JS,...), but almost nothing for flutter community. So I build a flutter package aws_ai that can be used by flutter developers to integrate with AWS AI services such (Rekognition, Translation,..). This package will help flutter developer to integrate with AWS AI services easily, which means more & more flutter users will use AWS AI services and generate a lot of great ideas. Package can be found here What I learned It is my first flutter project, my first flutter package. First time to use AWS Translation, Comprehension & Rekognition (although I didn't use rekognition in this project but I learn about it while implementing the flutter package). But the most challenging part for me was using Signature Version 4 Signing Process in calling AWS APIs in flutter package. What's next for The Healing Power of Telling Your Story It will be a long Journey, for example : Categorize stories based on disease type. So each user can join certain community. Get more user information such as countries, town, age,.. Some disease is related to user children, so I want both father & mother can add posts to the same child Update GUI titles based on user language Show number of comments on each post Add notifications Try it out Download it <div