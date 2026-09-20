---
slug: "flipside-rz9i1v"
url: "https://devpost.com/software/flipside-rz9i1v"
title: "Flipside"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1277
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/media_journalism"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Flipside

> News reimagined: Swipe to see every side of the story.

[Devpost](https://devpost.com/software/flipside-rz9i1v) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]] [[media_journalism]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, deep-learning, fetch.ai, fine-tuning, firebase, flask, html, huggingface, intersystems, iris, javascript, large-language-model, llama-index, newsapi

## How they structured the write-up

- inspiration
- what flipside does
- key features
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flipside

## Body

System Design: Mailman Agent System Design: Rabbithole Mode System Design: Subscriptions System Design: Chrome Extension Rabbithole Mode Complete Article Flipside Mode News Feed Inspiration The way we consume news is often one-dimensional, confined within our own echo chambers without even knowing how to find opposing viewpoints. Don't you want to know what the other side thinks? As bot-infested and hate-speech-filled social media platforms become primary news sources, students fall victim to misinformation and hidden agendas. We must prevent the spread of extremism to our generation by providing students with a safe space to stay informed. Our mission is not just to redefine the news experience, but to bring people together by fostering understanding and discourse between polarized groups. What Flipside does Flipside breaks through echo chambers and creates a safe space for students to discover the world through multiple lenses. Glide through bite-sized news stories in a sleek interface. Start with an AI-generated, unbiased article, then swipe right to explore contrasting viewpoints sourced from real people on online forums, Twitter posts and YouTube comment sections. If the story captures your imagination, enter the 'Rabbithole' and deepen your understanding through a guided conversation with our purpose-built AI agent that provides personalized and safe answers. Key Features 1. Bite-sized News: Swipe up and down to scroll through story summaries, swipe left/right to dig deeper into a story that catches your eye. Kinda like Tinder 👀 2. Explore Narratives: Read thoughts, reactions and opinions on any story sourced from Reddit, Twitter and YouTube. A place for every perspective. 3. Enter The Rabbithole: Ever been down a Wikipedia rabbit hole? Yeah, it's pretty addicting. Our rabbit hole features an AI-generated wiki fine-tuned on the topic with a trove of real-time information on the news story. You can also chat with a personalized AI agent to learn more. 4. Subscribe to Stories, not Sources: Keep yourself out of the echo chamber by following news stories instead of sources. As soon as there's an update to your favorite news story, we'll send you a notification. How we built it 1. Automatic Data Curation: Our Mailman Agent This agent is the crux of our app. It’s tasked to periodically fetch latest news to keep our app on top of the headlines while also notifying users if they might be interested in the update. Our Fetch AI agent uses time and geolocation to fetch the top headlines from the NewsAPI and process it through our extensive Together.ai GenAI content generation pipeline and publish it on our app. During this process, it uses llama_index from InterSystems IRIS to generate keywords through a RAG model, fed into Twitter Search API and webscrapers to extract relevant discussions. All data is automatically stored on and retrieved from Firebase Firestore. 2. Flipside Mobile App We build our platform using React Native and Swift for iOS. We used complex gesture handling to enable an intuitive and addictive swipe & scroll based user experience. We set up a Flask server to communicate with the various systems deployed. On top of this, we built a beautiful UI to ensure user experience was exactly how we imagined it. 3. Rabbithole Mode This agent provides the seamless replies in the Rabbithole mode. The agent is tasked to complete a whole AI pipeline to curate the best reply semantically to the context and accurately to the query. We utilized Fetch.ai’s versatile AI agent framework in Python to retrieve requests from our React Native app containing our query and a Together AI fine-tuned model. This is further processed using llama_index integration with the IRIS container by InterSystems for a RAG model powered by our context file and query intertwined with an engineered prompt. We utilize certain criteria such as query relevance, frequency, distinctiveness and contextual relevance. These keywords are fed into NewsAPI to retrieve the most similar articles which are added as context to generate valid reliable information. 4. Vector Search We utilize a semantic SQL vector search powered by InterSystems at the heart of our prediction tasks throughout the app. There were two main tasks with this foundation: 1. Subscriptions : We maintain a database of subscribed articles of each user. We take in a new article fetched by our Mailman Agent powered by Fetch.ai and generate embeddings of the fetched article and all subscribed articles using HuggingFace’s all-mpnet-base-v2. We then calculate a normalized vector dot product, sorted in decreasing order, and choose the top 5 users above a 0.75 threshold. This informs us that these users are most-likely to be interested in the new updates and we send them a notification. 2. Flipside Companion : We utilize the same process in our Chrome Extension to give a bit-sized summary of the article while providing the different narratives of the current article by choosing the top two articles from our database, ordered by a vector dot product (SQL semantic search) by InterSystems of the current article and our database. 5. Prompt Engineering: The Magic Challenges we ran into Jaisal: AI agents, vector databases, and the world's most powerful LLMs; one would assume that swiping would be the easiest feature to implement - wrong. Why React why? Why did this take 8 hours to build? Robby: I spent quite a while trying to get an LLM to respond to my prompts accurately. In my exasperation, I asked it to take a deep breath and then it started working! Ayaan: Found a weird bug while implementing the InterSystems IRIS SQL Search and spent 4 hours with the InterSystems team to figure out this never-seen-before bug! Anant: Going from a sleep-deprived midterm week to a sleep-deprived hackathon weekend :) Accomplishments that we're proud of Ayaan: I'm so proud of Robby for taking ownership of some of the most tedious and technically difficult tasks we had, plus for being a fantastic group DJ. Robby: I'm so proud of Ayaan for debugging one of our most complex modules, and as we hit enter in the terminal to test it...his laptop died! Jaisal: I'm so proud of Anant for coming up with great ideas for Flipside's features, combined with some really catchy names to make our project memorable. Anant: I'm so proud of Jaisal for managing to build out the entire UI, creating the technical outline for our app and doing so much more while helping the rest of us through our first hackathon. Truly incredible. What we learned 36 hours is a LOT of time wow... We actually built one of our most complex projects yet - even calling it full stack won't cut it. We learnt the important balance of compromise: with dozens of ideas we had to prioritize the ones which were important (healthy arguments!), settle for imperfect implementations, and think about the tech, the business, the moral implications, and most importantly, the user experience. These are all skills that we don't get the practice in our daily lives. So, Treehacks was the perfect place to get exposed to what we would say is a more realistic representation of the real world. And we developed newfound appreciation for each other. The heart-to-heart conversations you have on 2 hours of sleep go a long way. What's next for Flipside News on the go : We already have AI generated images (did you notice? :P). Next it's time for AI podcasts, weekly summaries and rabbithole-y stories - all automatically and perfectly generated. Highlight and Reply: A lot of users are refering to a small piece of text within the article when the make comments. Why not add the option to quote pieces of text? See which parts are interesting to others. Kind of like the YouTube "Most Watched Part" feature. <div