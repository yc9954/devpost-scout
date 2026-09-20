---
slug: "broomies"
url: "https://devpost.com/software/broomies"
title: "Broomies"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 708
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Broomies

> Easily assign chores, track monthly performance, and split expenses effortlessly with our roommate-friendly solution, Broomies! It's finally time to say goodbye to all of your household conflicts!

[Devpost](https://devpost.com/software/broomies) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** cockroachdb, go, react-native, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for broomies

## Body

Broomies landing page/login. Home page with a roommate leaderboard for the current month, and quick access to the user's chores. Displays all chores that are randomly assigned to roommates for the week, and can be viewed by each roommate. These are a list of chores that can only be seen by the user. Completion is indicated by the toggles. Every roommate gets notified whenever a chore is assigned, and whenever a chore is completed. Roommates have the option to view completed chores and give them anonymous ratings. Create and assign a chore for your roommates. Give assigned chore a description, choosing the days that it cycles through weekly, and selecting the difficulty level. Finance tool for keeping track of everyone's expenses throughout the month. Every transaction is recorded and can viewed by each roommate. Add a transaction. Inspiration Oftentimes, roommates deal with a lot of conflicts due to differences in living habits and aren't comfortable sorting things out by confronting one another. This problem creates unwanted tension between individuals in the household and usually ends up leading to a poor living experience. What it does Broomies is a mobile app that creates a fun environment to help roommates assign chores for one another, anonymously. Assigned chores can be seen by each roommate, with a separate tab to view your own assigned chores. Once a chore is created by a roommate, it randomly cycles weekly to ensure nobody gets repeated chores. Completing chores on time gives roommates points that get tallied up per month. There is also a way to track expenses with a built-in financing tool to record each transaction a roommate has made for their household. At the end of each month, the monthly sum gets split based on roommate performance, and the top roommate(s) get to pay the least. How we built it Our project utilizes a React Native Frontend with a Go backend and CockroachDB as our db. All our front-end components are designed and implemented in-house. Currently, the app is hosted locally, but in the future, we plan to host our backend on Google cloud, and hopefully publish a polished version on the app store. Finally, we used Git and Github for version control and collaboration tools. Challenges we ran into This was our first time developing a mobile application and working with CockroachDB. A big challenge was adjusting and understanding the nuances of mobile development Figuring out an equitable method for distributing points that rewarded doing chores but didn't promote sabotaging your roomies took much polling from fellow hackers Our app covered a lot of features, and we would often run into bugs involving chore management and transaction splitting Accomplishments that we're proud of We are really proud of managing to create a full-stack, functioning mobile app as not only first-time mobile developers, but CockroachDB users as well. Entering the hackathon, our goal was to create something that would make any part of our life easier, and we believe Broomies does just that. We are proud to build an app that we hope to actually use in the future. We are really proud of the overall design and theme of Broomies, and how effectively we were able to translate our designs into reality What we learned The power of design, both in components and in data structures. Before we started, we took the time to plan out our data structures and relationships, this helped us flesh out a scope for our project, and effective divide work amongst the team. Lots of experience working on new technologies: From IOS and React Native, to leveraging CockroachDB Serverless in quickly turning an idea into a prototype How to effectively ideate: Going into the hackathon, not having a good idea was our biggest concern, but once we learned to let go of finding "The One" hackathon idea, and instead explored every possible avenue, we were able to flesh out ideas that were relevant to our life. What's next for Broomies After fleshing out user management and authentication, we want to deploy the Broomies app on the App store, as well as host our backend on Google Cloud. Also, we want to add the ability to react/respond to task completions, so your roomies can evaluate your tasks. <div