---
slug: "waffle-vsb70j"
url: "https://devpost.com/software/waffle-vsb70j"
title: "Waffle"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 447
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Waffle

> Chat with relevant topics instantly - semantic proximity messaging.

[Devpost](https://devpost.com/software/waffle-vsb70j) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[financial_record]] [[geospatial]]

**stack** convex, next.js, react, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for waffle

## Body

Inspiration Inspired by the classic internet chatrooms meeting the timeless in-person marketplace of ideas you encounter at events. What it does When you send a message on waffle, it makes similar messages more visible to you and shrinks irrelevant content so that you can focus on threads that you are interested in chatting about. Meanwhile, you can remain aware of other conversation and can dial into it by joining in in real-time. How we built it Waffle leverages OpenAI API's high-powered LM's to embed messages into vectors which represent their meaning. We used thinkmap.ai to quickly and iteratively plan out our direction and required steps. Our MVP was a tool you could put a thesis statement and an essay into and it would colorize the sentences based on their relevance to the thesis statement, making sure you will stay on track. We brainstormed ideas of how to use the underlying vector encodings to add more meaning than just pure text. We used Convex to handle the synchronization for our chat service, which requires making embeddings and computing their cosine similarity dynamically, which we had no problems with using their service. Challenges we ran into It was challenging at first to understand which convex hooks to use, but once we got it working we had no issues with sync'ing. We also found it challenging to think of practical and novel ideas in such an open-ended hackathon, and are proud that we came to our solution. Accomplishments that we're proud of Formed a team and shipped an innovative AI product in one day, as we only participated in the in-person hackathon. What we learned We learned that the tools you use during development can drastically reduce headaches about data and separation of concerns. We learned that it's much more cost-effective and less saturated market to work with LM embeddings rather than pure generation, and the information is meaningful. What's next for Waffle We want to try storing a user's location in the conversation space based on their entire message history rather than simply the most recent message, and see how that would change the product. Currently user id's are stored in browser only, so while nobody can access your account, if you clear your cookies you will not be able to log back in. We could add more robust authentication. We want to create a map of the conversation space based on a lower-dimension representation of the sentence embeddings. Clusters could be labeled with k-means clustering and users could jump in at clusters in order to jump off with a topic they are interested in starting from a birds-eye-view. Team: Miles Wiesenthal Eli Richmond Lyne Tchapmi Luis Arevalo <div