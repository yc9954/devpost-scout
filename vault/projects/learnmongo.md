---
slug: "learnmongo"
url: "https://devpost.com/software/learnmongo"
title: "LearnMongo"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 404
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/structured_db"
---

# LearnMongo

> An AI powered learning platform for mongoDB

[Devpost](https://devpost.com/software/learnmongo) · hackathon [[Atlas Madness]]

## Facets

**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** django, google-cloud-run, mongodb-atlas, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for learnmongo

## Body

Restaurant query Inspiration There are online courses that you can take to learn about MongoDB. They provide in depth tutorials on how to use it and its inner-workings and they're really helpful. It's great to see all the knowledge you need to perform a task, but sometimes it's really nice to just play around with a system to get a foot in the door. What it does LearnMongo takes a simple self-learning approach. When a user visits a page, they will be asked for a query. The purpose for this app is to teach the very basics so all you need to do is type what you want and the integrated AI will spit out a query for you. It will also run that generated query on a sample MongoDB Atlas database to get you the sample data you requested. How we built it We used MongoDB Atlas to host our sample database The server was developed with Django using pyMongo to communicate with the database We used the Google Cloud Platform to: Generate queries with Vertex AI (code-bison@001 model) Build our container when updated with Cloud Build Deploy LearnMongo with Cloud Run Challenges we ran into A big challenge we faced was working with the AI. We needed a prompt that would generate correct pyMongo code that would execute at runtime. Getting everything set up and deploying properly. We had trouble working with GCP permissions that slowed development whenever something new came up. Accomplishments that we're proud of Many of these technologies that we used for this project were foreign to us when we started. We were able to take our time to read documentation and play around with them until we understood how they worked. We also started late in the timeline so everything was all gas, no brakes until the end and we were able to work well under our time constraint. What we learned We learned a lot more about GCP services. We didn't have much experience in cloud platforms before this, so it was fun to explore what GCP had to offer. A lot of tasks that would normally take a long time are integrated very well into the platform so we were able to learn very quickly. What's next for LearnMongo There is still more work needed on prompt generation and possibly training our own model instead of using an untuned one to write more accurate code. <div