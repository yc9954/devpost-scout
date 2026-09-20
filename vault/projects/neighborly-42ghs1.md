---
slug: "neighborly-42ghs1"
url: "https://devpost.com/software/neighborly-42ghs1"
title: "Neighborly"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 1121
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Neighborly

> Introducing Neighborly, THE platform for connecting with your neighborhood to responsibly borrow, lend, or trade everyday items! Need a tool, vehicle, or extra storage space? Look no further.

[Devpost](https://devpost.com/software/neighborly-42ghs1) · hackathon [[Atlas Madness]]

## Facets

**domain** [[developer_tools]] [[education]] [[labor_employment]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]] [[web_dom]]

**stack** bulma, docker, google-cloud, google-places, graphql, mongodb, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for neighborly

## Body

Architecture Diagram Inspiration The inspiration behind Neighborly came from a few different places. I live in a small-town suburb where everyone is pretty close, and we're always helping each other out. It's great to know that if I'm baking a cake and run out of sugar, I can run across the street and ask my neighbor to borrow a cup. My parents have had the idea for an app that allows you to lend and borrow things from people in your Neighborhood for a long time, and now that I've graduated school I found some more time to see if I could make that idea a fully-functional reality. I found Atlas Madness hoping to create a project I could put on my resume while job hunting, and with my newfound free time, Neighborly seemed like the obvious choice. While starting work, I recognized the potential value in the global sustainability that could be created from a platform that brings communities together through resource sharing. A tremendous amount of waste is created every year through buying and consumption, and sharing resources with your neighbors could help mitigate some of that impact. After all, there's no need for everyone on the block to have their own lawn mower if they only use it once a week anyway. What it does Neighborly is a web-based platform that enables users living in the same city or neighborhood to easily connect and responsibly share resources. The application allows users to create profiles, list items they are willing to lend, borrow, or trade, and browse available items. By providing a centralized hub for resource sharing, Neighborly streamlines the process of accessing items that may not be readily available or affordable for each individual in a community. How I built it Neighborly, at its core, is a basic CRUD app. I used create-react-app to initialize a frontend for the website and built pages and components using the Bulma CSS framework because it's lightweight, open source, and looks great out of the box. Though I initially was going to create a typical Express backend, I decided to go fully serverless in the nature of MongoDB Atlas. All backend processing is handled by Atlas Functions, some GraphQL custom resolvers, and a bit of Google Cloud Functions. I used the Realm web SDK to interact with my backend from React clients. The website is published to Github, where Google Cloud Build watches for pull requests to the deploy branch and then builds a Docker image, which is deployed to a Google Cloud Run instance. The GCR instance is available over a custom domain, beneighborly.xyz. Challenges I ran into User Metadata Management : This was my first time using Atlas app services to build anything. I spent quite a long time trying to define custom user metadata on sign-up, such as a user-provided name, or link to an avatar. User Creation functions worked for creating default values, but I could not pass custom data to them. After many hours of reading through the documentation, I ultimately decided to simply add metadata through a separate function that is run once on sign-up. Judging by the Mongo community forums, it seems other users were unclear on how to achieve this result as well. React State Management : Liklely due to a lack of clear understanding of how state is updated and managed in React, I found myself running into issues like infinite re-render loops pretty often. Ultimately, I probably should have opted for a more robust state management solution like Redux, but didn't find the time to do so. Styling Woes : I'll be very transparent: I don't love design. I find CSS styling and responsive tweaks to be really tedious and somewhat monotonous. I think the website looks alright, but certainly not the best it could have. Also, I feel that the time I spent managing stylistic choices detracted from the amount of features I wanted to add. Ultimately, I think I'm more comfortable with a backend focus, and next time I participate in a hackathon, I will probably seek a frontend designer to team up with. Accomplishments that I'm proud of For someone who worked alone, in his spare time, and with multiple technologies I have never used before, I feel I did a good job of creating an app that might be of real value to some people. After a few more minor tweaks, I'm going to tell my neighbors to sign up and begin the first sub-community within Neighborly. I'm glad to have created something that will see real-world use beyond testing and development, with the potential to create a more sustainable world for all of us. I'd say my greatest accomplishment was in what I learned while creating Neighborly. I got to experience hands-on what it's like to work with GraphQL (really cool language), MognoDB Atlas, and more of Google Cloud that I never knew existed. Most of my previous cloud application experience is within AWS, I have touched Firebase before but not too extensively. Learning all of these new technologies to use moving forward makes me proud! What I learned I learned that full-stack development is a tall order, and I see why the industry has shifted towards specialized roles like Frontend, Backend, and DevOps engineers. It's not realistic to assume the average software engineer will be able to keep up to date with all of the latest technologies on a large scale for the whole of an application's development. In general, I think I learned how valuable even just one other team member can be in creating an application from the ground up. What's next for Neighborly I am really passionate about what Neighborly can become, so I'm looking forward to adding more features even after the judging period is over and launching Neighborly in a production-ready manner. Some things I'd still love to add are: Messaging/transactions on-platform: Having an integrated messaging feature for reaching out about posts you're interested in would be great. Even better, if transactions can take place on-site, I could add something like the Stripe/Square API to allow users to put a temporary hold on a neighbor's card while they borrow a high-ticket item like a car. This would encourage users to treat their neighbors' belongings with respect, and always return them promptly. More specific localities for Neighborhood selection. e.g. I'd prefer to have Chelsea, Greenwich Village, and Tribeca all be separate Neighborhoods rather than users simply selecting "Manhattan". The smaller these communities are, the more open and collaborative they can become. Better mobile device support/responsiveness. This one's pretty obvious: the website is tough to use on small screens. It needs some CSS revamping. UX can be improved in general as well. <div