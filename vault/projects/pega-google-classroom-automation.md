---
slug: "pega-google-classroom-automation"
url: "https://devpost.com/software/pega-google-classroom-automation"
title: "Pega-Google Classroom Automation"
hackathon: "The HCL-Pega Pathbreaker Hackathon"
organization: "HCL"
winner: true
words: 420
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
---

# Pega-Google Classroom Automation

> The application consists of around 9 REST-FUL Integrations services circling around the primary features like classroom creation, retrieve classrooms, posting announcements and much more.

[Devpost](https://devpost.com/software/pega-google-classroom-automation) · hackathon [[The HCL-Pega Pathbreaker Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[mental_health]]
**user** [[educator_student]]

**stack** google-classroom-api, google-cloud, pega

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for pega-google classroom automation

## Body

Inspiration With the COVID Pandemic, Organizations struggle to find a solution to deliver learning digitally . In every industry learning has always been the key source for both technical and mental heath development. Currently industries face the lack of educating their employees about best practices which includes mental health, technical development, soft skills and even best body postures while working. This application tries to solve the issue by easily automating with Google classroom and have a teacher-student based learnings What it does This Application can be primarily used on LMS Portals by various organizations mainly with Pega Applications built for need of education/learning etc The Application's primary motive is centered on “Teacher” to manage their students, assignments and classrooms however “Student” can view their classrooms. Some exciting features of this application are 1) Create Classroom: Google accounts with “Teacher” profiles can create classroom easily entering the classroom name and description 2) Create Course Work: Google accounts with “Teacher” profiles can create assignments for classrooms and also view the student submissions 3) Manage Classrooms: Google accounts with “Teacher” profiles can manage their classrooms a. Post Announcements : Add new announcements to a classroom b. View Students: All the enrolled students will be listed 4) Student Classrooms: Feature for “Student” profiles to view their classroom, can be extended and developed further How I built it The Application was built in Pega version 8.6 and on theme-cosmos v03.01. The use cases were structured into flow diagrams and accordingly case types were created to serve purpose of each use case. All the REST integration rules like data transforms and datapages required for establishing a connections are maintained in separate ruleset -ClassroomIntegrations:01-01 . Created Authentication profile with related scopes and the latest OAuth2.0 is used for authorization Challenges I ran into I faced challenges on authorization part where every user needs to give access to their classroom/google account Faced challenges on refresh tokens and access tokens, came up with many errors Accomplishments that I am proud of To create a complete REST-FUL Application to handle over 9 integration services To handle errors effectively and debugging them That it was really a good learning experience What I learned I, primarily learned on time management and planning of items Having worked solo, understood the importance of a team and how good a team should be Got more exposure on the Rest APIs in general What's next for Pega-Google Classroom Automation Planning on making it more student friendly as well Improve UX and more apt error management <div