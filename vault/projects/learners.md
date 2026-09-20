---
slug: "learners"
url: "https://devpost.com/software/learners"
title: "Learners"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 437
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "user/educator_student"
  - "user/general_public"
---

# Learners

> Empowering global knowledge through remote mentoring

[Devpost](https://devpost.com/software/learners) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[developer_tools]] [[housing_homeless]]
**user** [[educator_student]] [[general_public]]

**stack** docker, gcp, helm, javascript, kubernetes, letsencrypt, php, symfony

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for learners

## Body

Explore other interests Mentors that will fit you (based on your interests) Searching for mentors (with OpenSSL as their skills) Contacting a mentor (booking a mentoring session) User profile User settings Become a mentor page (add skills and hobbies) Inspiration Learners is going to be launched for the community in response to the global crisis caused by the Covid-19 pandemic, to enable remote knowledge sharing and mentoring within a manageable and friendly environment. Since many countries are asking their citizens to #StayHome and #WorkFromHome , we believe that Learners can provide what's needed to make knowledge more accessible in times of isolation, social distancing and quarantine. What it does Learners is a social platform connecting people around the world willing to share (mentors) and receive (mentees) knowledge about interesting subjects within a manageable and friendly environment. How it works Mentors are users with skills/tags added to their profiles, able to share their knowledge and skills Mentees are all users with or without skills/tags, able to look for mentors and to book coaching sessions Session are sessions booked on mentors (with additional availabilities) by mentees How we built it The Learners back-end API is built with Symfony wrapped up in a Docker container, and its CI/CD pipelines are pointing to the GCP GKE staging and production clusters. The front-end is built with VueJS and its CI/CD pipelines are pointing to Firebase and a production hosting. Challenges we ran into The implementation of a state-of-the-art authentication flow is an ongoing challenge. We have now implemented a native authentication system with some limitations. After debating the different alternatives we decided to stick with Auth0 ( https://auth0.com ) . We are expecting to release the new authentication system in the next version. The implementation of a video conference service is also an ongoing challenge. The users have currently to agree on which tool they use for their remote virtual mentoring sessions (we recommend Hangouts for now) . We expect to release our own video conference service in the next version. Accomplishments that we're proud of We are proud that we built the platform following SOLID principles and programming best practices. Also that we were able to design a complex multi-tenant architecture to make workspaces available for our users. We are expecting to release the workspace functionality soon. What we learned We learned something new: humanitarian-driven-programming . Which means programming driven by humanitarian principles in times of crisis. What's next for Learners We are currently programming non-stop to finish the above-mentioned functionalities. We aim to release this tool to the global community in the best condition. Made with ❤ in Paris <div