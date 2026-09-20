---
slug: "direct-8z7o32"
url: "https://devpost.com/software/direct-8z7o32"
title: "Direct"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 291
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
---

# Direct

> AI meets Travel: Direct empowers the user with the culmination of human knowledge to seamlessly handcraft a perfect vacation.

[Devpost](https://devpost.com/software/direct-8z7o32) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[structured_db]]

**stack** featureform, mindsdb, mongodb, pinecone, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for direct

## Body

Inspiration Direct started with a vacation and the lack of a suitable travel app. We recognized a hole in travel itinerary assistance, which is the unutilized power of user input. In seeking a method to avoid the stress of repeatedly scouring the internet for various tickets and matching timings, we landed with Direct. What it does Compared to current players in the industry, like Expedia, we work with the user to make a perfect travel itinerary. Carrying the disruptive momentum of OpenAI's LLM technology, we integrate GPT-4 into our application to effectively scour the internet for the best itineraries and prepare numerous alternatives, allowing the user send messages describing their needs and preferences to refine their vacation plans. How we built it We utilize MindsDB and Featureform to effectively process and store large amounts of itinerary data for quick recall. During runtime, we query a Pinecone vector database for relevant itinerary data and grab pre-processed GPT-4 summarizations from MindsDB to use as context for a final GPT-4 response request. Challenges we ran into Understanding how to integrate MindsDB into our application while keeping in mind runtime drawbacks was quite difficult. Accomplishments that we're proud of We were able to streamline the entire data pipeline using Featureform, from capturing data through webscraping to the vector embeddings in Pinecone. We are also really happy about our seamless user interface on the frontend. What we learned We learned about how multiple databases could connect with each other to efficiently query prepared datasets. What's next for Direct We envision a highly flexible and scalable travel application. After continuing to incorporate more locations and produce self-growing datasets, we see paths in cooperating with tourism-related corporations and working with users to make an even better app! <div