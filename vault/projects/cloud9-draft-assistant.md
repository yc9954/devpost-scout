---
slug: "cloud9-draft-assistant"
url: "https://devpost.com/software/cloud9-draft-assistant"
title: "Cloud9 Draft Assistant"
hackathon: "Sky’s the Limit - Cloud9 x JetBrains Hackathon"
organization: "Cloud9"
winner: true
words: 807
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Cloud9 Draft Assistant

> Real-Time Draft Intelligence Trained on Pro Play

[Devpost](https://devpost.com/software/cloud9-draft-assistant) · hackathon [[Sky-s the Limit - Cloud9 x JetBrains Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**substrate** [[structured_db]] [[web_dom]]

**stack** beautiful-soup, fastapi, jetbrains, junie, numpy, pandas, pycharm, python, pytorch, selenium, streamlit, xgboost

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cloud9 draft assistant

## Body

Banning Example Picking Example Inspiration I’ve been a fan of professional League of Legends since I started playing in 2016. While life has made it harder for me to grind ranked the way I used to, my passion for the esport has never faded, and I still closely follow the LCS and international tournaments. This project was inspired by co-streamers like IWillDominate and Caedrel, who seem to anticipate drafts as they unfold effortlessly. I remember one draft where Dom called each pick and ban by name before they happened. I wanted to explore whether that intuition could be captured in a system, one that could support professional teams during theorycrafting while also helping fans like me follow drafts at a high level without needing hundreds of hours of gameplay each season. What it does At its core, C9 Draft Assistant evaluates the current draft state and recommends the top five picks or bans, each paired with a concise, human-readable explanation. The primary signal comes from an AI model trained on Tier 1 professional draft data, learning what elite teams value at each stage of the draft. That score is then supported by data-driven heuristics such as current patch meta strength, champion synergies and counters, and player comfort. To keep recommendations realistic, the system also applies role-aware filtering so it avoids suggesting champions for roles that have already been filled. The result is a tool that feels intuitive to experienced viewers while remaining accessible to fans who want deeper insight into professional drafts. How we built it The project was built using Python as the core language. I used FastAPI for the backend and Streamlit for the frontend, with PyTorch and XGBoost handling the machine learning components. Data was gathered through a combination of Selenium and BeautifulSoup, pulling from sources such as GRID, gol.gg, and u.gg. For data processing and storage, I relied on pandas, NumPy, and a mix of CSV, Parquet, and JSON artifacts. Development was done in JetBrains PyCharm, with Junie used as an AI coding assistant throughout the build. I began by collecting and normalizing as much relevant draft data as possible, then trained the main drafting model on Tier 1 LoL drafts. From there, I incrementally layered in additional heuristics based on real match data and my own understanding of professional drafting, refining the system through iterative testing. Challenges we ran into The biggest challenge was data scale and complexity. I had never worked with a dataset as large or as nuanced as GRID’s, and the initial learning curve was steep. After spending significant time reading documentation and experimenting, I was able to extract useful information, but I’m confident there’s still untapped potential there. With more time, I would love to explore GRID more deeply and leverage it in more creative ways. Another major challenge was model training and evaluation. While I’ve followed AI research for a long time, this was my first time training a model entirely from scratch. Understanding how performance shifted with different data sizes and feature sets was both fascinating and difficult. To keep the signal clean, I chose to train primarily on Season 26 data, prioritizing relevance over volume to avoid teaching the model outdated metas. With more time, I would train multiple models across different patch windows and compare their performance empirically. Accomplishments that we're proud of I’m most proud that the model can produce coherent, professional-level drafts. The first time it banned Jayce in response to a Malphite ban, it genuinely felt like the system “understood” the game, and that moment made all the effort worth it. I’m also proud of what I was able to accomplish within the hackathon timeframe. I joined the competition late and was initially worried I wouldn’t finish in time, so seeing a fully functional system come together was incredibly rewarding. What we learned This project taught me a tremendous amount about data engineering, model training, and professional League of Legends drafting. I also significantly improved my general software engineering skills, particularly around project organization and system design. This was the first time I managed a project of this size entirely on my own, and while I made plenty of early mistakes, especially with file structure and architecture, I learned how to identify and fix those issues as the project evolved. What's next for Cloud9 Draft Assistant This project reignited my love for League of Legends and competitive play. Moving forward, I plan to expand the system with deeper team composition analysis, more advanced counter-pick modeling, and a cleaner, more intuitive frontend. I also intend to continue collecting Tier 1 draft data as the season progresses, allowing the model to improve over time and adapt more quickly to evolving metas. With more data and iteration, I believe this tool can become an even stronger bridge between professional insight and fan understanding. <div