---
slug: "donorfu"
url: "https://devpost.com/software/donorfu"
title: "DonorFu"
hackathon: "2018 Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 420
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# DonorFu

> Connecting potential donors with facebook group posts requesting blood donations.

[Devpost](https://devpost.com/software/donorfu) · hackathon [[2018 Developer Circles Community Challenge]]

## Facets

**substrate** [[geospatial]]

**stack** aws-lambda, dialogflow, facebook-graph, messenger, messenger-platform, mongodb, nginx, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for donorfu

## Body

bot Inspiration The inspiration for this idea came when we had need of blood for our friend. We found so many groups on facebook distributed over different areas. Some groups were highly active and thus cluttered with requests that did not correspond to the location targeted by the group. Others were dormant and requests were unanswered. We got into thinking there should be a solution to manage these groups and match potential donors with specific posts. What it does DonorFu is a facebook messenger bot leveraging access to groups approved by admins to match posts with registered potential donors. Group admins log in and add specific groups whose posts are then processed and matched with donors for sending them notifications in messenger itself. The donors can follow the link to the post in the notification to declare their willingness to donate. Additionally, they can check their eligibility before contacting the poster. The eligibility check is just a basic set of questions and has no association with proper checkups done on site before donation. How we built it We have built a bot connecting Dialogflow NLU engine with Facebook messenger platform APIs. We are using Facebook Groups API to get access to posts in groups that are added to our app by their admins. Facebook Login is used for getting permission to access group posts. Then our app can access group posts which can be managed in the bot itself due to Account Linking with the bot. We are using cloud functions for listening to Messenger platform webhooks and process posts. Google maps API is used to check the vicinity of locations. Challenges we ran into We faced many challenges while building this which made our journey interesting. We learned to build a complex manual facebook login flow along with account linking for the messenger. Another challenge was using Facebook test users with Messenger bot as there is no clear way to add the bot to a page created by test user. Accomplishments that we're proud of We were able to extract blood group and location and match them with donor details with good accuracy. Created a seamless way for managing groups, getting notifications, sign up for notifications, all within the same ecosystem using a conversational interface. What's next for DonorFu DonorFu can easily be extended for other kinds of donations such as organ donations. On a higher level, this kind of mechanism for matching users with groups posts can be applied to other areas where both parties reap benefits. <div