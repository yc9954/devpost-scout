---
slug: "self-care-for-devs-api"
url: "https://devpost.com/software/self-care-for-devs-api"
title: "The Caring Devs"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 957
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# The Caring Devs

> A collection of APIs dedicated to all fellow devs to take care of your well-being!

[Devpost](https://devpost.com/software/self-care-for-devs-api) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]] [[mental_health]]
**user** [[developer]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]]

**stack** flask, postman, python, slack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we’ve learned
- what's next for the caring devs

## Body

Inspiration Work healthily. Live happily. This simple motto is the inspiration behind The Caring Devs workspace. As developers, we make the world a better and more efficient place via technology - but at the expense of our health. We are constantly sitting down, exposing our eyes to screens and skipping meals. It is a common occurrence to find developers with muscle strains on their backs, necks, legs and even eyes. Many of us are also heavily addicted to caffeine and with the rising issue of burnouts in the tech community, we decided to take the first step. By building The Caring Devs workspace, featuring our very own Self Care for Devs API collection and the Nutritionix API collection, we hope to encourage fellow developers to start taking better care of their health before doing what they do best - building cool stuff for the world to see! What it does Self Care for Devs is a Slack Bot API that lets developers create and test their own self care bot easily. Any user can subscribe to services , which allows the bot to send notifications to remind the user to do these self care habits. These services are: Services Description quotes Sends a motivational quote every morning 7am. eye-care Sends notifications to take eye breaks every 30 minutes, with helpful tips on eye care. stretch Sends notifications to stretch once every hour, with helpful infographics to follow. water Sends reminder to drink water every 2 hours. memes Sends programming-related memes every 3 hours to brighten the day. nagging Sends reminders on random intervals about things like your posture, lighting on your setup, stand up occasionally, fun nutrition facts and eye breaks. Here's an overview of the routes of the API, which are used as slash commands to communicate with the self care bot: Slash Commands Description /help Returns list of all slash commands and their description /todo Returns list of the user's todos /todo [task] [HH:mm] Adds task and deadline time in HH:mm to the todo list /done [task] Marks task as completed, remove from todo list /subscribe [service] Receive notifications on the specified service /unsubscribe [service] Stop notifications from the specified service Nutritionix is the largest verified nutrition database. In the Nutritionix collection we’ve created, we have some of their most powerful endpoints powered by their natural language processing (NLP) algorithm to return useful nutritional facts. We’ve included this collection in our workspace as we believe it can be beautifully integrated with our Self Care for Devs Slack Bot API. How we built it The Self Care for Devs API is built using Slack API and Python Flask. Postman has been very useful during development including setting up mock servers for testing, organizing routes and putting it all together into a collection. After deploying our API, we have also set up a monitor for our collection to see how they perform daily, making sure no fatal errors are happening. Challenges we ran into The first challenge was making sure every team member was on the same page. Our team is compromised of people with various backgrounds (web developer, software engineer and data scientist) and we live in different parts of the world. So just getting started with the project was a small hurdle we had to overcome. We solve this by communicating more often and assigning our roles early on. Another challenge was that we had to learn how the Slack API works in order to build this Self Care for Devs Bot API. We also spent a lot of time researching on the different features and components of Postman, in order to learn more about it and be able to use it to enhance the project. Accomplishments that we're proud of Despite our team coming from diverse backgrounds, we are proud that we were able to overcome the challenges and complete this project smoothly together. Additionally, being able to create something that assists developers gives us a huge sense of accomplishment. "A healthy mind breeds a healthy body and vice versa" Zig Ziglar. In line with this quote, we are proud to develop something that points towards achieving the very same goal. What we’ve learned Because we come from different stacks in tech, we learn how to be open to each other's ideas and approach to executing those ideas. It is truly inspiring to get to know each other better through this hackathon! We also learn how to meander through all obstacles presented due to our geographical and skill differences. Allocating work, finding time for meetings, sharing resources efficiently took some time to figure out, but we were proud that we eventually cracked the code in making this project a smooth success. Most importantly, we learn a lot about what Postman has to offer. From its already strong API development tools to its workspaces, monitors and mock servers, we learned how to leverage the many components Postman has to offer to speed up our progress in this project. What's next for The Caring Devs In the future, we plan to add more slash commands to Self Care for Devs, making it into the ultimate self care/mental health companion for fellow devs. Perhaps adding some AI for the bot to be able to chat and make small talk with users. And maybe adding a journaling feature where users can record and share negative feelings with the bot to de-stress. There are indeed endless possibilities for The Caring Devs. We are thinking of expanding it further, beyond just having a Slack Bot. Maybe an app will be built as a follow-up. All in all, we are thankful that this hackathon has provided the opportunity to build something for the tech community while learning some new skills. <div