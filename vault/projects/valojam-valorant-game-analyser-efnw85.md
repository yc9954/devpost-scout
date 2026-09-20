---
slug: "valojam-valorant-game-analyser-efnw85"
url: "https://devpost.com/software/valojam-valorant-game-analyser-efnw85"
title: "Valojam-Valorant Game Analyser"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 502
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/educator_student"
---

# Valojam-Valorant Game Analyser

> Use Valojam, get better at Valorant!

[Devpost](https://devpost.com/software/valojam-valorant-game-analyser-efnw85) · hackathon [[Funathon]]

## Facets

**domain** [[developer_tools]] [[legal_justice]]
**user** [[educator_student]]

**stack** jupyternotebook, matplotlib, numpy, python, scikit-learn, selenium, time, valking.gg

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that we're proud of
- what we learned
- what's next for valojam-valorant game analyser

## Body

Inspiration Having more than hundreds of hours of game time in FPS and Campaign games, I have first person experience with how hard it can be to get better at a game and defeat one’s competition. People tend to watch YouTube tutorials and professional e-sports players play in hope of improving. Improvement is dependent upon one’s game statistics and not how one tries to play. A good player would have good game statistics if they play their way and not try to imitate a different and more or less experienced player. There had to be a way for players to get personalized AI generated insights about their gameplay and easy to follow, slow-paced instructions as to what they would have to do improve at the game at a reasonable pace. This led to me creating Valojam. What it does This project comprises of a supervised machine learning model in which, Kill/Death (KD) ratios of past Valorant matches of a player are mined from an online source and stored in a list. A second list is then created with elements going from 1 through the number of elements in the initial list with the KDs. A regression line is then plotted after the model is trained using this data. Based on this regression line, an expected KD (x) is inferred which is then showed to the player. The player is then encouraged to have a KD greater than “x”. If the player manages to get a KD higher than “x”, the model would be retrained and a slightly higher KD would be inferred. This would encourage the player to show a slow-paced yet gradual improvement in the game. If, in case the player gets a KD lower than “x”, the retrained model would display a lower expected KD which would be more convenient for the player to achieve. This approach in improving the performance of a player would be more effective because of the minute, slow-paced and not-complex goals. How we built it I built it using the IDE Jupyter Notebook and python as the programming language. Challenges I ran into I ran into multiple challenges ranging from slightly to decently complex. Debugging the code was the primary problem which occurred minutely during the phase of me building the project. Apart from debugging, finding reliable sources to mine data was an issue I overcame in the initial phases of me building the project. Accomplishments that we're proud of Successfully building the project and having it work as per planned is the main accomplishment I am proud of. This project was presented in multiple national level competitions by my mentor and was appreciated by the Delhi Govt. What we learned Carrying this project out familiarized me with new libraries such as selenium and improved my thinking abilities, thanks to working with python. I also extensively learned managing my time better. What's next for Valojam-Valorant Game Analyser Upon granting of legal permission by the owner of valking.gg , I plan to commercialize this project. <div