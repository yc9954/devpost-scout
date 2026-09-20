---
slug: "phoneburner"
url: "https://devpost.com/software/phoneburner"
title: "PhoneBurner"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 814
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# PhoneBurner

> Boost the productivity of your sales team by power dialing and tracking prospect lists all in monday.com .

[Devpost](https://devpost.com/software/phoneburner) · hackathon [[monday apps challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** api, css, graphql, html5, php, rest, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for the phoneburner app and our team

## Body

Inspiration Over the last couple of months our team has begun utilizing a power dialing tool internally for our sales team. This has helped autonomously boost productivity when it comes to lead and prospect outreach. Due to the overwhelming success we had found while utilizing such a program made us ask "Why is no one providing a tool within the monday.com platform?". Without much hesitation our integrations team got right to work and developed an app that solved just that. After weeks of market research at CarbonWeb ( https://carbonweb.co/home ) we partnered with one of the best power dialing programs on the market, PhoneBurner ( https://www.phoneburner.com/ ). Having this partnership has allowed us to integrate all the amazing power dialing capabilities right into monday.com. What it does The application itself contains a plethora of monday.com features including a template, board view and several integrations. Workspace Templates Dialing Session Template Allows user to have a fully automated power dialing experience within a native monday.com board. Sales Process funnel To be used in sync with the Dialing Session Template this basic sales funnel should give a full sales experience. Board View Dialing Session View This view allows user’s to begin a dialing session within a classic monday.com expiernece. The users begin a dialing session within PhoneBurner based on a group selection. Integrations Call Status Tracking Call status tracking includes two integrations that allow us to change a status within monday.com based on if the call was answered or not answered. Disposition Tracking Disposition tracking also includes two integrations that will allow us to either write an update or change a status based on a specific PhoneBurner disposition hit within a dialing session. Database Sync The Database Sync allows users to sync contacts from PhoneBurner to monday.com and also update them when they change inside a user’s board. Last Called Date Last call date is a singular integration that allows the last called date to come into monday.com in order to track when a contact was last dialed. In addition to the above, we have already had many more feature requests that we will continue to work toward in our developer build as the production build proceeds down its user acceptance testing phase! How we built it We have spent over a year now working within the PhoneBurner platform and understanding users needs not to mention that our own team has been using monday.com for nearly four years now. So when it came to the features needed we were ready to get coding. We were able to build these out using Graphql , rest, php and some other tricks in our hat that allows us to have a streamlined and automated power dialing session for the users. To us the most important part was the users not having to feel like they were a coder meaning that it had to be a drag and drop situation with a one time auth. This is when we ran into some challenges we had to overcome connecting into the PhoneBurner platform itself. Challenges we ran into Like we stated before we want the app to be as streamlined as possible and for this to take place we would need to have a simple way to authorize monday.com to PhoneBurner one time without a continual expiration period. We worked on a cron job system that would allow us to automatically re-auth after the expiration date and do all of this before the user ever even notices. Besides development challenges, the hardest challenges were the outward facing client process. Because of our main goal of a streamlined process we had to work extra diligently on not only the sales team, but also the onboarding team and support team. We had to expand our resources and knowledge base to support such a large flow of users. Accomplishments that we're proud of Something that we are incredibly proud of is being able to fulfil the needs of an official app launch. We were able to not only research and develop out the app but also fully sell, onboard and support the app we have built. The app itself is a game changer in the way of turning monday.com into a CRM as it adds one more level of CRM functionality. I feel that we are continuing to grow the monday.com platform and its goal of ideal users by launching such a powerful dialer. What's next for the PhoneBurner app and our team On the agenda is to continue and develop out the monday.com platform with our other application ideas along with supporting the PhoneBurner app. We plan to soon launch the v1.1 which will have several updated features that have been requested from the initial stages of our Alpha testing. We are also beginning our Beta testing phase in May this year. If you are interested in joining the Beta please signup below! <div