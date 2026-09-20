---
slug: "gambit-y0j7mu"
url: "https://devpost.com/software/gambit-y0j7mu"
title: "Pawn Up"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 531
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/legal_justice"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Pawn Up

> Pawn Up: Your Personal AI Chess Coach—Analyze, Train, and Master Chess on Your Own Time.

[Devpost](https://devpost.com/software/gambit-y0j7mu) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]] [[legal_justice]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** chroma, css3, docker, flask, gemini, git, github, groq, html5, javascript, llama, node.js, oauth, python

## How they structured the write-up

- about the project

## Body

Analyze with AI Home Connect with Lichess Search thousands of games with Vector Search Upload Games Choose Puzzles Arch About the Project We are a bunch of amateur players who love playing chess, but over time we noticed that our improvement has become stagnant. Like many college students, we neither have the time nor the financial means to invest in professional coaching to take our game to the next level. This frustration sparked the idea behind Pawn Up —a project built to help players like us break through the plateau and improve their chess skills in their own time, without expensive coaches or overwhelming resources. What Inspired Us As passionate chess players, we struggled with finding affordable and effective ways to improve. Chess can be an expensive hobby if you want to seek professional help or guidance. The available tools often lacked the depth we needed or came with hefty price tags. We wanted something that would provide personalized feedback, targeted training, and insights that anyone could access—regardless of their financial situation. How We Built It We started by integrating Lichess authentication to fetch a user's game history, allowing them to directly analyze their own performance. With Groq and Llama3.1 , we leveraged AI to categorize mistakes, generate feedback, and suggest relevant puzzles to help users train and improve. We also levergae ChromaDB for vector search features and Gemini pro and Gemini embedding Our project features four key components: Analyze : Fetches the user's last 10 games, provides analysis on each move, and visualizes a heatmap showing the performance of legal moves for each piece. Users can also interact with the game for deeper analysis. Train : Using AI, the system analyzes the user's past games and suggests categorized puzzles that target areas of improvement. Search : We created a vector database storing thousands of grandmaster games. Users can search for specific games and replay them with detailed analysis, just like with their own games. Upload : Users can upload their own chess games and perform the same analyses and training as with the Search feature. What We Learned Throughout the development of Pawn Up , we gained a deeper understanding of AI-powered analysis and how to work with complex game datasets. We learned how to integrate chess engines, handle large amounts of data, and create user-friendly interfaces. Additionally, we explored how LLMs (large language models) can provide meaningful feedback and how vector databases can be used to store and retrieve massive datasets efficiently. Challenges We Faced One of the main challenges we encountered was making the AI feedback meaningful for players across various skill levels. It was crucial that the system didn’t just provide generic advice but rather tailored suggestions that were both practical and actionable. Handling large amounts of chess data efficiently, without compromising on speed and usability, also posed a challenge. Building the vector database to store and search through grandmaster games was a particularly challenging but rewarding experience. Despite these hurdles, we’re proud of what we’ve built. Pawn Up is the solution we wish we had when we first started hitting that plateau in our chess journeys, and we hope it can help others as well. <div