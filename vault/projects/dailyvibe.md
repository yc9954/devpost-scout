---
slug: "dailyvibe"
url: "https://devpost.com/software/dailyvibe"
title: "Dailyvibe"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1422
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "domain/transportation"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Dailyvibe

> Once a day, Dailyvibe lets you choose between 4 emojis to describe how you are feeling. Your vibe is then displayed on a world map, anonymously, alongside people from all over the world.

[Devpost](https://devpost.com/software/dailyvibe) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[disaster_emergency]] [[labor_employment]] [[mental_health]] [[transportation]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** ai, azure, azure-content-moderator, azure-face-recognition, azure-map, azure-translation, express.js, git, github, nextjs, nginx, openapi, postgresql, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dailyvibe

## Body

Introducing Dailyvibe The first ever sketch of Dailyvibe Dailyvibe See what people are saying, and where they're saying it, at a glance. Once a day, Dailyvibe lets you choose between 4 emojis to describe how you are feeling. Your vibe is then displayed on a world map, anonymously, alongside people from all over the world. This service has been made possible leveraging the multiple capabilities of the Azure Cognitive Services . Share your vibe on www.dailyvibe.org now. Inspiration During the pandemic, many people are forced to stay by themselves for long periods of time, which often leads to people feeling disconnected and alone. We thought that if people could quickly get a sense of how other people around the world are feeling, they might feel more connected. Knowing that other people are going through similar things can help reassure us that we are not alone. We wanted a quick, anonymous way for people to share their feelings and see how others are doing. We think that Dailyvibe fits that purpose. What it does Dailyvibe allows users to upload how they feel once a day about what is happening in the world and optionally attach a comment. Their (anonymous) vibe and comment will then be visible on the world map. They can also see how everyone else is feeling and what they have to say. All of the day's vibes are aggregated and a global daily vibe is displayed. Users can also choose to take a selfie, and have the system guess their vibe, rather than manually selecting how they feel (the images are not stored or displayed publicly in any way). How we built it Overview We built the site using Next.js, a React.js framework, and TypeScript. We used PostgreSQL as database and everything is working seamlessly using Nginx as a web server secured with SSL from Let's Encrypt running on an Azure Virtual Machine . Azure Cognitive Services use cases This project has been focused on leveraging the Azure Cognitive Services as far as possible. We chose them to because they fit our use case well and worked out of the box, which saved a lot of time which would otherwise have been spent on gathering data, training models, and deploying them. 1) Face Using Face allowed us to add a smart feature to the site where users can upload a selfie and have the system guess how they feel. The selfies uploaded are not saved in the database and only used to get the vibe inference 2) Translator As we wanted the platform to be accessible for all, we use Translator to detect the languages of comments posted by users and translate them into English or other languages. Users can then use the translate feature of their browser to translate all comments at once in the language of their choice. The original comments are still saved in the database for future use. 3) Content Moderator To remove any hate speech and insult and provide the user a 100% safe experience on Dailyvibe, the messages are sent to Content Moderator to flag any profanity or personally identifying information, and comments which are flagged are disabled. 4) Text Analytics (Work in Progress) In the future, we are considering adding several other Azure Cognitive Services. For example, we could use Text Analytics to extract any popular topics that users are commenting about. Once the site has been running for a while, we can also start to analyze how vibes change over time and what kinds of patterns or trends exist. Anomaly Detector could be used to identify any sudden changes in vibe. Misc Azure Services use cases 1) Azure Map Azure Map is a key component of Dailyvibe. It makes it a breeze to integrate and display the user's vibe across the globe. 2) Azure Virtual Machine Dailyvibe is hosted on an Azure Virtual Machine (Standard B1ms) with the following specs: Operating system: Linux (ubuntu 18.04) Size: Standard B1ms (1 vcpus, 2 GiB memory) Location: West US 2 Challenges we ran into First of all, it was our challenge to make a solution that could actually help people in this pandemic. By the process of ideation, we started designing our service with the problem of people's loneliness in lockdown using Azure AI technology. Tech wise, the main challenge was to seamlessly integrate the AI capabilities in the system. It was not a matter of "using AI" to use AI, but to think first on what great features would improve the user experience on Dailyvibe and how can we leverage AI within the Azure ecosystem to move forward. We had great ideas, right in the beginning the project, to use the Text Analytics capabilities in order to extract topics from the vibe's comment, similar to what Twitter is doing on it's trending section. Unfortunately, after several tries, we couldn't get the result we expected as we need more daily vibe data to extract correct information. This is only a postponement as we will resume and provide this feature in a near future when we have data to do so. Dailyvibe is open to everybody, so despite the fact that it was created for a hackathon, we had to try hard to make it live and accessible for all. Accomplishments that we're proud of We are proud to have created a place where people around the world can share their feelings everyday and in every environment in both web and mobile. Big thanks to Microsoft for their Azure platform as all their products were integrated smoothly and we believe we are as proud to have build Dailyvibe with them that they will be to be part of this journey. Dailyvibe isn't perfect of course, but it is the beginning of something special. Creativity always brings light to darkness. We have brought all of our abilities, in design, engineering, AI, psychology and much more, to do good and try to solve a bigger issue, and for this, damn right we should be proud. What we learned We found that using pre-made AI services greatly simplifies and speeds up the development process. These services can always be swapped out for custom trained models later if necessary. AI is now becoming part of our daily life, but we are still facing obstacles. For a lot of people, AI is a black box and there is a boundary between AI engineers and the rest of the team, and the same is true for designers. What we learnt during this hackathon is to break the walls between the different disciplines by involving everyone on each step of the creation. As you can see on our Miri board at https://miro.com/app/board/o9J_lSkOotc=/ , everyone co-existed and shared their ideas and knowledge from ideation to production deployment to co-create Dailyvibe. Dailyvibe is all about community, sharing and wellbeing, meaning that people should perceive Dailyvibe as their new AI assisted self-care routine. For that we learned and experienced branding and marketing to better capture people's interest. As we also wanted to spread awareness about Dailyvibe, we learned how to run a basic Ad campaign using Twitter and Linkedin. It is in everyone's abilities to bring change and happiness to the world. Our goal with Dailyvibe is humble and simple, and if we can at least improve someone's life and state of mind with Dailyvibe, then it is already a victory. What's next for Dailyvibe We're hoping that more people start using Dailyvibe, as the quality of the user experience largely depends on the amount of people posting vibes and comments. Dailyvibe opportunities are endless. When the traffic will be sufficient, we will be able to gather a considerable number of data concerning the mental health of people from all over the world. We have then the ambition to partner with a Data Marketplace Specialist like Snowflakes ( https://www.snowflake.com ) to provide Dailyvibe data to other tools and institutions through the Dailyvibe API. On top of that, we want to provide a way for people to report comments. Our AI implementation already moderates comments before submission, but having a way for the community to also moderates the comments is on our roadmap. We also want to make Dailyvibe available for the missing countries where Azure Map is not available in order to really provide a safe place for people to share their emotions worldwide. One of our objectives is to expand the Dailyvibe platform with our twitter account @dailyvibedotorg to keep the good vibes flooding and keep our users updated on what is coming soon. <div