---
slug: "classcast"
url: "https://devpost.com/software/classcast"
title: "ClassCast"
hackathon: "EducateHacks 2024"
organization: "EducateHacks"
winner: true
words: 576
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ClassCast

> Connecting parents with their child's education.

[Devpost](https://devpost.com/software/classcast) · hackathon [[EducateHacks 2024]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** axios, jwt, nextjs, postgresql, postman, prisma, react, typescript

## How they structured the write-up

- reason why i made this project
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for classcast

## Body

ClassView Page Login Page (Redirects to a login form depending on which option you select) Onboarding (Registration) Form Educator Portal Create Update Modal Reason why I made this project Parents usually find it difficult to be completely connected to their kid's education. When asking how their school day was, they usually find a response like "fine", or "good", without ever connecting or understanding what their children are learning and how they are growing in the classroom. What it does ClassCast acts like a "connection" between the classroom and parents. Teachers are able to broad-"cast" events happening in the classroom via an "update board". They can also tag images so parents get a better idea of what is happening, and can feel more immersed and connected with their child. That way, parents can stay up-to-date with their child's education and see the progress that their child is making. How I built it The project was built using Typescript and NextJS for the frontend, and utilizes Prisma ORM + PostgreSQL for the database and an API built using NextJS server actions. The project features secure JSON Web Token based authentication, and all data is encrypted in order to prioritize security. I also used Postman for testing my API endpoints. Timeline of creating ClassCast: 03/05 Night Created the project (and project structure) Wrote database schemas Finished account creation and authentication endpoints 03/06 Morning Created frontend for authentication (signup and login) Created Parent and Educator Portal Pages Wrote backend logic for class creation and joining (Created first GitHub commit) 03/06 Afternoon Created frontend for Creating and Joining classes Crafted UI for the ClassView page 03/06 Evening Wrote update creation endpoints in backend Created frontend for viewing and creating updates Added image upload functionality (Final GitHub Commit) Challenges I ran into One challenge that I ran into was managing users. With the database schema which I had written, Parents and Educators were two separate types of accounts (they each had their own tables). This meant that it was hard being able to merge them (in situations like joining classes, since classes would have a combination of Parents and Educators in them). I solved this by added relations to my database, and writing separate API endpoints for parents and educators in order to make it easier to work with. Another challenge which I faced was being able to store images. I did not want to use something like S3 or Cloudinary (as I wanted it to be simple), and I had limited storage in my database, which makes it difficult (especially if images are large). I solved this by compressing the image and storing it as a string (which the DB can easily handle). Then, when the client receives the Image, it would be decoded and presented. Accomplishments that I'm proud of A big accomplishment that I'm proud of was being able to finish the project on time and present a working MVP. I was also able to tackle the challenges (listed above), and I still emerged with a working solution. What's next for ClassCast Due to the short timeframe of the hackathon, I was not able to implement some security-related things (related to authentication). That would definitely be something that I am looking to improve in the future. Also, due to the short timeframe, I was unable to add parent comments to the update board. That would also be a feature that I would be interested in adding later on. <div