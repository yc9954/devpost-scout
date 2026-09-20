---
slug: "academe-agbixc"
url: "https://devpost.com/software/academe-agbixc"
title: "Academe"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 770
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/video_visual"
---

# Academe

> Academe is a platform for students to share and receive advice and educate each other on various academic matters such as the college application process, high school experience, and more.

[Devpost](https://devpost.com/software/academe-agbixc) · hackathon [[Funathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[video_visual]]

**stack** aws-amplify, aws-dynamodb, expo-cli, javascript, react-native, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for academe

## Body

Profile & Friend Screens Main Screens Inspiration As a high school student myself, I struggled with discovering what my passions are. For too long, I feel like I'm lagging behind others for not knowing what my passions are. When I did try something new, I feel overwhelmed by the lack of guidance and instructions. For example, I wanted to learn how to develop a simple mobile app for my clubs at school. However, I was overwhelmed and frightened by the journey that I needed to take to develop it. I didn't know where to start and I didn't even know if it was possible. Luckily, after countless hours of research, I found a group online that helped me on my journey. This online group inspired me to create Academe. I realized that I wasn't the only one struggling to learn something new. I've encountered hopelessness numerous times during my learning, and I realized that too many people have quit trying. By creating a community with Academe, I can help connect students with mentors and help them receive guidance on whatever they want to learn. What it does Academe aims to provide a platform for students to develop their passions and explore academic matters that aren't available in school or anywhere else. Current websites and apps give general advice to these students that are vague and unhelpful. Our platform is a unique way for students to connect with those who have experienced and overcame the problems they're facing. Academe is inclusive to everyone because it generates a community filled with people wanting to help each other in their learning. Our app performs similarly to popular apps such as Discord and Slack. Users are able to join school-specific servers that their teachers created for discussions regarding homework, class material, and more. Users are also able to create their own private groups for purposes like clubs, group projects, and more. They are also able to join public servers, hosted by college students who acts as mentors that will answer and guide student problems and decision-making for their academic problems. Inside these servers, there are multiple channels (messaging platforms) based on different conversations. This enables an organized method for messaging. Moreover, users are able to direct message their friends and find friends. How we built it I created this app using a Javascript and TypeScript framework called React Native. I used Expo Client to run my app on my emulator and my real phone. For my backend, I used AWS Amplify and its User Pool DynamoDB to store user accounts for login and sign-up. I used its graphQL Appsync API to store, fetch, mutate, and update user data like their name, what servers they're in, and more. Also, I used AWS Storage S3 to store image and audio data. In my code, I created components like list items and buttons for data mutations and I created screens to create the frontend. Each screen usually has two parts in the file’s code: half of it fetches data from my backend, and the other half displays this data to create the frontend of my app. Challenges we ran into One of the most challenging aspects of creating the app was setting up the backend structure. It had the most mistakes because there were plenty of outcomes that we did not expect to happen. Sometimes the logic did not work out and we had to restart the backend entirely. Moreover, the frontend was one of the most time consuming parts of the app. There were several edge cases where the styling was not working properly and hurt the user experience. Overall, we were able to overcome these challenges! Accomplishments that we're proud of Being able to submit a working prototype of the app is my biggest accomplishment! What we learned Over the course of the hackathon, I learned a lot about CSS and styling after hours spent on tutorials on how to achieve certain stylings. I also learned a lot about GraphQL and backend data prototyping . Most importantly, I learned how to work under pressure and create a functioning app by the end of a hackathon. What's next for Academe Our next goal is to contact volunteering and tutoring organizations from multiple universities to appoint moderators for each academic subject they want to advise on. Each individual or group of willing moderators will be evaluated for their experience and interests. This evaluation will determine what servers they can run. After this, we will host weekly lectures at local high schools and colleges to spread the awareness about our problem and our solution to solve it. <div