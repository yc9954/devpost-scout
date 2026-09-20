---
slug: "adopting-genai-for-personalized-endorsements"
url: "https://devpost.com/software/adopting-genai-for-personalized-endorsements"
title: "Adopting GenAI for personalized endorsements"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 564
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/simulation_digital_twin"
  - "domain/retail_commerce"
---

# Adopting GenAI for personalized endorsements

> Revolutionizing e-commerce: Our platform uses GenAI to personalize ads for buyers, endorsing products recommended by Knowledge Graphs & allowing sellers to choose ambassadors for ads.

[Devpost](https://devpost.com/software/adopting-genai-for-personalized-endorsements) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[graph_reasoning]] [[simulation_digital_twin]]
**domain** [[retail_commerce]]

**stack** appwrite, elevenlabs, flask, mariadb, neo4j, nextjs, npm, openai, pytorch, react, tailwind.css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adopting genai for personalized endorsements

## Body

Inspiration Most social-media platforms support product endorsement by displaying advertisements on behalf of certified sellers. These advertisements lack target-audience knowledge and have limited area of creativity for the sellers. Such generic ads have a low probability of reaching the right audience. TLDR ; there are two main areas in tailored discovery to improve ad success: •⁠ ⁠Recommend specifc products to users based on user data •⁠ ⁠Allowing seller to choose an influencer for advertisement. What it does Our tailored discovery system is a two part AI service, where 1.⁠ ⁠ ⁠ Knowledge Graphs ⁠ helps sellers by endorsing their product in the form of a personalized advertizement, specifically to a users who are more likely to buy their products based on their activity/interactions on Tiktok. 2.⁠ ⁠ ⁠ GenAI ⁠ helps sellers to choose an influencer whose digital footprints are utilized to generate a personalized ad video, in a controlled manner. How we built it The system can be distributed in to 4 major parts: 1.⁠ ⁠ DataStore : We utilized Appwrite as our central datastore for app data and media storge. 2.⁠ ⁠ UI : We built our UI using Reactjs , Nextjs & tailwind.css . 3.⁠ ⁠ Product Recommendation : We created knowledge graphs in Neo4J based on likes, follows, posts, etc.. Then the LLM is given this graph as input to generate product reccomendations. 4.⁠ ⁠ Ad generator : After product is recommended, a deep fake video for the product is generated and sent to the frontend. Challenges we ran into There are several challenges we needed to address to make a stable prototype 1.⁠ ⁠Too many 'tiktoks' would cause homepage to load late. We had to implement pagination to solve this issue. 2.⁠ ⁠To demonstrate the effectiveness of knowledge graphs, we had to study user interaction patterns and evolve our graph using simulated data . 3.⁠ ⁠To save time, we had to plan effectively and decide what aspects of 'Tiktok' are necessary to replicate. 4.⁠ ⁠During ad-generation POC, we had to switch from diffusion models to GANs, and then lighter versions of GANs because of limited resources and data . This tolled us more to generate quality output. Accomplishments that we're proud of We successfully deployed a minimal and stable ⁠ standalone UI that replicates Tiktok behavior ⁠ modified with ads to products. 2.⁠ ⁠After populating our knowledge graph with enough data we observed ⁠ user-data driven product recommendation ⁠ that changes with latest-recorded user activity. 3.⁠ ⁠Using light-weight GANs, we successfully generated ⁠ personalized advertizements ⁠ which contains the AI generated video of a certified Tiktok influencer speaking a script at run-time tweaked with user-data What we learned 1.⁠ ⁠We learned UI technologies like Reactjs, NextJs and Tailwind CSS. 2.⁠ ⁠We learned how to utilize Neo4J for creating knowledge graphs. 3.⁠ ⁠Grasped the concepts of merging LLMs with knowledge graphs to generate reccomendation. 4.⁠ ⁠While brainstorming ideas for innovation in ads, we learned many aspects of UX design-science that is applied to regulate as well as enhance ad experience What's next for Adopting GenAI for personalized endorsements 1.⁠ ⁠Broader research is necessary for understanding revenue-model involved in making this live, and analyzing the performance of our model. 2.⁠ ⁠Better ML-models can be used to generate better quality videos. User data can be used to enhance these videos with different elements like background theme, weather effects, color palette, etc. <div