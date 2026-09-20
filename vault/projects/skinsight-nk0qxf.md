---
slug: "skinsight-nk0qxf"
url: "https://devpost.com/software/skinsight-nk0qxf"
title: "Skinsight"
hackathon: "United Hacks V5"
organization: "Hack United"
winner: true
words: 328
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Skinsight

> Ai for skincare

[Devpost](https://devpost.com/software/skinsight-nk0qxf) · hackathon [[United Hacks V5]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** expo.io, google-cloud, react-native, supabase, vertex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skinsight

## Body

Inspiration We had both gone through significant skin transformations, with experience dealing with expensive dermatologist appointments and the never ending search for a good, personalized, science backed skincare routine What it does Snap three quick pics and Skinsight scores your skin with a couple metrics, then spits out a structured analysis, routine, and reasoning/approach. How we built it Expo Go for the front end Gemini-2.5 + a tiny Flask edge function for image crunching Supabase for auth + storage Figma so the UI doesn’t look 2010 celsius energy Challenges we ran into figuring out how to get the model to send out a structured json output for us to parse into our ui finding out how to scrape skincare product listings, and then manually cleaning that data up general bugginess of moving all our users' data around as they navigate through the onboarding while trying to avoid too much ux friction. maintaining security of data even though users aren't yet authenticated, and then securely moving data once users are authenticated. Accomplishments that we're proud of Shipped an almost fully functional onboarding to our app in 2ish days with a pretty sleek UI/UX and a strong market analysis creating the KNN semantic search engine for skincare products, we had never done something like it before What we learned how to give LLMs the ability to call tools that we made. The reasoning behind why we should use edge functions for this as a production app productivity stagnates after an all nighter What's next for Skinsight most of the functionality for the actual app once the user passes the onboarding still needs to be done. we set up the ui mostly for each of the pages (home, routine, and settings screens) but they arent integrated with the supabase backend or the necessary weather apis to provide the functionality we envision. We made significant progress, but theres still a lot left to go for Skinsight to become the real deal. <div