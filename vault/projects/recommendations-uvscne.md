---
slug: "recommendations-uvscne"
url: "https://devpost.com/software/recommendations-uvscne"
title: "Recommendations for Confluence"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 1208
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Recommendations for Confluence

> Recommend interesting conferences, trainings etc. to your coworkers. Populate them with rich content or attachments. Categorize them with spaces or labels. Search them all over your Confluence. Learn.

[Devpost](https://devpost.com/software/recommendations-uvscne) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** confluence, custom-content, forge, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for recommendations
- famous last links

## Body

The recommendation hub Create a recommendation with a rich description Add a macro for certain recommendations on a wiki page Recommendation details with the ability to add comments Inspiration Life-long learning is a thing - not just in our company. Often, colleagues share valuable trainings, cool conferences they attended or interesting books they read. They do this on several systems and channels, and many of these tips are often forgotten quickly or go under in the deluge of messages. On the other hand, people often need an agenda to learn something new. Colleagues want to extend their skills and new employees want to build up key knowledge to do their job. That's why we had the idea to centralize sharing and finding these educational recommendations. And what would be a more appropriate tool to use than our knowledge base, namely Confluence? So we made different attempts to reach our goal in the past, but nothing we tried fully met our requirements. That's when we decided to develop our own "education hub" - the idea of the Recommendations app was born. Our mission is to create a marketplace for tried and tested educational material. What it does Our app adds the ability to easily create (short) notes to describe any kind of educational recommendations. Such a note has a title, a rich description and can have attachments. It also resides in an appropriate Confluence space and can be categorized with a label. People searching for recommendations can filter by space and label or search for explicit keywords or authors. This the "pull" part. We also want to proactively notify colleagues who watch certain spaces or labels, so that they are immediately informed about new things they're interested in (the "push" part). Recommendations should be a living document (as is a wiki). Users can like or comment on them to share their opinions about the resource with their colleagues. Use cases I want to share a conference called "DevOps Week". I create a recommendation in the TECH space and label it with "devops" and "conference". Every techie who is interested in devops or conferences in general, will hear about it. Another use case is the onboarding process of new employees. Let's say we have a new developer in our Forge app team. We would label every important basic stuff with "newbie" and the fitting key word label "forge-dev". So on her first day, she directly has an agenda of what to read. Beside conferences and training, you might want to maintain a book list or set up an expert search. How we built it We developed the app in a team of two people who normally work on Confluence DataCenter apps. To build our app we used Forge, as this might be future proof and let us develop fast. To have as much freedom as possible we used the Custom UI approach to build our frontend. We added a hub ( globalPage ) with all the required functions of creating and filtering recommendations. To access the information where it's needed, we developed three macros to create, search and display recommendations on Confluence pages. A recommendation is a so called Custom Content which is a special content type (similar to a page or comment). The main advantage is that it is stored in Confluence and can be found via the normal Confluence search. Challenges we ran into As mentioned we do work with Atlassian on-premise apps, but normally not in the cloud / Forge environment. So the tech stack (ReactJS, Forge and Confluence Cloud API) was kind of new to us. This was challenging at first, because things behave quite differently than in on-premise development. But after we had set up our skeleton (which was quite easy with the documentation!) and read through some ReactJS articles, things quickly improved. Working with Custom Content was the next big challenge. Although there is some documentation, a rich code example would have helped at this point. Thankfully, the community helped us out and we could take a look at a working example (props to Fabian Siegel's CQL search POC for custom content ). As the feature is relatively new in Forge we noticed some teething problems, and sometimes we weren't sure whether we made a mistake or if there was a bug / missing feature in the API (see the feedback ticket FRGE-888 ). For example, we managed to attach uploaded images to a recommendation, but did not find a working way to display them. Sending notifications is an integral part of our vision, but sadly this has not been implemented yet in Forge. This would be our major feature request to the Forge team. On a UX level, we tried to make creating and finding recommendations as easy as possible. We want people to share their tips in the right place without having to search for the appropriate space or label, so we thought hard about the chosen Forge modules and the best configuration of these app parts. That's why we used the hub and macro approach both - all at one place (hub) and all information in the right place (macro). For the macros, it would be really nice to have a space and label picker in UI Kit for the macro configuration. Accomplishments that we're proud of We made it work :) We set up a Forge app and can use Custom Content. We tried nearly every feature described in the documentation and are able to say what worked and what didn't - this will also help us in future Forge apps. Particularly difficult was the handling of attachments and labels, but eventually most of it worked. Many of our goals have been completed and the app is in a usable state. We didn't want to create a "throw-away" prototype and think we can continue developing after the hackathon. That is why we submitted it to the Atlassian marketplace. What we learned We learned much about the Forge and cloud environment. Especially about the life cycles and deployment process. The Confluence cloud APIs were another interesting field, which sometimes had its pitfalls. Apart from Atlassian part, we familiarized ourselves with ReactJS. We have mostly used Vue.js in our current on-premise projects, so it was interesting to see similarities and differences. The Atlassian component library made styling very easy and is a great place to see what's currently possible within Forge. Last but not least, we learned that the Atlassian Developer Community is a great place with nice people. Most questions were answered lightning-fast by another user or Atlassian staff - thanks for that! What's next for Recommendations As stated in the Codegeist blog article "perfect is the enemy of done", things like UI/UX improvements can be done after the deadline. Adding metadata to recommendations, like ratings or due dates (e.g. for conferences), might be the next feature. We will also observe the Forge changelog for new features we were missing so far. This includes features like reactions (apart from simple likes) and notifications. Of course we have many more ideas how to extend our app. We will wait for feedback from users and see what's most important to develop next. Famous last links Forge feedback ticket: https://ecosystem.atlassian.net/browse/FRGE-888 Marketplace listing: https://marketplace.atlassian.com/apps/1229448/recommendations-for-confluence <div