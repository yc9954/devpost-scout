---
slug: "voicifying-quick-base"
url: "https://devpost.com/software/voicifying-quick-base"
title: "Voicifying Quick Base"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 992
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
---

# Voicifying Quick Base

> Use Quick Base to build Alexa Skills, Google Actions, chatbots, and more! Get request data analytics to use in pipelines to tie your other systems together and gather insights.

[Devpost](https://devpost.com/software/voicifying-quick-base) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**substrate** [[video_visual]]

**stack** .net, alexa, azure, botservice, c#, googleassistant, msteams, quickbase, slack, voicify

## How they structured the write-up

- inspiration
- what it does
- samples
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for voicify and quick base

## Body

Architecture Diagram webchat sample Slack bot sample Google Action Sample Voicify Quick Base integration listing Alexa Skill Sample sample_usage_chart Inspiration The core motivations for the hackathon was to address real problems: Connection, Responsiveness, Equity, and Security. I thought, "well hey, connectivity and responsiveness are exactly 2 of the problems I set out to help solve with Voicify - lets get these things working together". So I set out to let Quick Base and Voicify users easily spin up conversational experiences and apps using their existing Quick Base knowledge and tools. Create and manage conversations in tables, view conversational request data, visualize the data into charts to monitor usage, trigger pipeline events based on what people say or do with the skills and bots, and tons more! I also wanted to take the chance to teach others how to build enterprise software and integrate systems together, so I built the whole thing live on my twitch channel ! With my chat beside me, we were able to explore all the capabilities of Quick Base, figure out how we would get it working with Voicify, and then develop the integration step by step. What it does Voicify users can go to their integrations and add the Quick Base app integration. They simply need to supply a user token and the realm of their quick base domain. The integration then scaffolds a new Quick Base app with 2 default tables - one for content, and one for request data. Now with both the Voicify app and Quick Base app, users can deploy the app to any of the supported endpoints of Voicify including: Alexa Skills Google Actions Bixby Capsules IVR/Telephony systems SMS bots Slack bots Microsoft teams bots Facebook Messenger bots Embedded chat bots Custom voice assistants Any Azure bot channel and more! Then with the Voicify webhook pipeline setup, users can add new content in Quick Base and it will automatically be synced to Voicify and immediately available for end-users to ask about. For example: Whenever anyone interacts with the app, regardless of platform, Voicify will send the request information back to Quick Base where it can be visualized, trigger other pipelines, and more! Here's what that looks like: Check out Samples for some examples of how this is and can be used. Samples Below are a couple samples I built to demonstrate the flexibility of the integration and setup! Covid-19 Response App This is an app that was deployed to: Alexa Google Assistant Webchat but could also be deployed to any other channel Voicify supports. It allows users to ask about the current Covid-19 plan and what actions are being taken. Employee FAQ App This sample is deployed to: Webchat Slack Microsoft teams It allows employees to ask the bot about certain internal resources such as benefits packages, vacation policies, team members, and more. This also has a great example of when someone asks about benefits, it can send a request to an HR team to let them know what people are asking about. Quick Base Hackathon Resources App As a bonus example, I also deployed an app with resources related to the Hackathon itself! (pretty meta, I know) You can ask Alexa, Google, chatbots, and more about resources for the hackathon, due dates, inspiration, and more! Channel Screenshots Below are a few examples of the many places that these samples were deployed to! Google Assistant Alexa Slack Web chat How I built it This project was built by creating a middleware API using C#, .NET Core, and Azure App Service to act as a bridge between Voicify and Quick Base. Within this there are 3 primary functions: Configuration and Setup of the Voicify integration Webhook endpoint for Quick Base to send updates to records that then sync to the Voicify app Webhook endpoint for Voicify to send conversational request data to Quick Base I then created a few sample apps mentioned above using this setup and deployed them to different conversational and voice channels so users can interact with them! Here's what the entire architecture looks like between the two: Challenges I ran into The biggest challenge was not being able to automatically generate a pipeline from the REST API so that users could just one-click set the whole thing up from Voicify. Still, one manual process that most Quick Base users seem familiar with isn't too bad, and it can be easily extended to do SO much more. Accomplishments that I'm proud of I'm excited and proud of how easy this experience is for users to get up and running with a conversational interface. More and more, there is a need to provide an easier customer experience, keep connected with employees, and get users information as rapidly as possible. Together with Quick Base and Voicify, not only is it super easy for a user, customer, or employee to get access to the information they need, it's also super easy for the application user to create the experience. I'm also proud of this solution being a little bit "outside the box" of what Quick Base is normally used for. What I learned Mostly, I learned a ton about how Quick Base pipelines work and how they can be extended to easily tie internal systems together and make internal processes automated so easily. It was also a great opportunity to teach others about Quick Base and integration development by live streaming and publishing videos of the process. What's next for Voicify and Quick Base Tons of stuff! I'll be working on tighter integrations for letting Quick Base users implement more Voicify features without having to leave Quick Base, more app templates that include the optimal views for request analytics, and certain pipelines in place for different use-cases to optimize getting up and running. I'll also be working on finding some users who already use both Voicify and Quick Base to validate with more user testing, then add new features based on feedback. <div