---
slug: "mycareerpath"
url: "https://devpost.com/software/mycareerpath"
title: "MyCareerPath"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 420
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# MyCareerPath

> MyCareerPath- Your Path, Your Way. Generates a study plan tailored to your preferences. Say goodbye to searching resources and the frustration of preparing timetables with this personalised assistant.

[Devpost](https://devpost.com/software/mycareerpath) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[disaster_emergency]] [[education]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** bedrock, claude

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mycareerpath

## Body

Project outline Inspiration We as students and working professionals often struggle to prepare a study schedule and gather relevant resources for interview preparation and self study. Our struggles and a quote by the Prime minister of India, "Turn disaster to opportunity" (translated) inspired us to develop an application to address the concern. What it does The application browses the web to identify relevant study resources (videos, blogs, or books) based on the user's interest and generates a roadmap suggesting all the resources with their URLs to study every day/week/month as per the total available time mentioned by the user. Additionally, the application features a section for relevant quizzes and interview preparation MCQs for the user to test his knowledge. How we built it We followed the principles of Prompt Engineering and designed few shot prompts for the LLM based on the given inputs. Prompts were customised to 'common sense' logic based on the time available. For example, a user can never complete 5-6 different resources inside a day. For such scenarios, prompts were designed to suggest only the resources a human brain can comprehend in the short timeline such as a 6-7 hour YouTube video or a crash course available as a blog. Challenges we ran into No challenges were reported in regard to the AWS infrastructure. Designing the prompt to customise to user demands on timeline was challenging. Designing LLM instructions to address roadmaps as short as q day/1 week and as long as 52 weeks/1 year required lots of brainstorming and analysis. Accomplishments that we're proud of We were able to customise prompts to an extent to create customised roadmaps. We experimented on a number of prompts to create roadmaps for 1 day, few days/weeks, and even for a year. What we learned The biggest learning from the project is that developing Generative AI applications is not restricted to prompt engineering or understanding the strengths and limitations of LLMs. Communication and constructive feedback is very important. It was virtually impossible to design the most optimal prompt without gathering insights and reviews from potential users. What's next for MyCareerPath In the future, the app can be extended to students (currently it focuses on working professionals). The app shall be able to create roadmaps for preparing for competitive exams such as UPSC, JEE, GRE, GMAT, CAT etc. It shall also be used to create a timetable for students appearing in their high school examinations. Here the model would take into consideration the strong and weak subjects of the student. <div