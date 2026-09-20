---
slug: "ar-voice-control-and-ml-hand-sign-ninjutsu-battle-simulator"
url: "https://devpost.com/software/ar-voice-control-and-ml-hand-sign-ninjutsu-battle-simulator"
title: "AR Voice ML Ninjutsu Battle Simulator"
hackathon: "Hack the North 2019"
winner: true
words: 698
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AR Voice ML Ninjutsu Battle Simulator

> Our project bridge the gap between science fiction and reality, bring anime characters to life. Users get to reenact their favourite scenes and justus from the anime Naruto with their anime figures!!

[Devpost](https://devpost.com/software/ar-voice-control-and-ml-hand-sign-ninjutsu-battle-simulator) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[simulation_digital_twin]] [[voice_speech]]
**substrate** [[structured_db]] [[video_visual]]

**stack** augmented-reality, css3, flask, hologram, html5, javascript, keras, machine-learning, python, react, tensorflow, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for ar voice control and ml hand sign ninjutsu battle simulator

## Body

Hologram display Hand sign detection Voiceflow part 1 Voiceflow part 2 Naruto hand signs Inspiration Simply put, our project bridge the gap between science fiction and reality. We are a group of anime fans who dreamed of anime characters coming to real life since our childhood. In the past 3 days, we made our dreams come true. Our AR battle simulator projects hologram on our favourite anime characters to bring them to life. We achieved two main goals: projecting hologram to bring our anime protagonist to live; casting Japanese ninjutsu in hologram form through ML Hand Sign Recognition. These used to be only items that exists in anime classics such as Naruto (an anime about Japanese Ninjas) , Yugioh (an anime about a card game that can summon virtual/real monsters), but today we brought them from the 2D display to the 3D world. A small step for 4 anime fans, a giant leap for the anime community. In addition, the anime industry is a huge untapped market in the west. According to Hollywoodreport, the revenue of the anime industry in 2017 was 19.1 billion USD. The industry is full of figure collectors that are more than willing to pay for innovative anime merchandise. Not only is our project a major breakthrough for the anime community, it is also potentially extremely profitable. What it does The battle simulator is a game where two players brawl off in the battle of Naruto ninjutsu hand signs. Each player has an anime figure. When ninjutsu is cast, the effect is projected on the anime figure as a hologram. The machine learning model can identify 12 unique hang signs from the anime Naruto and different anime cards. Each ninjutsu consists of multiple hand signs. Hologram demo: https://drive.google.com/file/d/1wP-MFGF_UKBkN2Uv-KxRyxEyveSBHZ3z/view?usp=sharing Hand sign demo: https://drive.google.com/file/d/1PSYILYJyG9ejJosRWk2ShaHvN29rtybN/view?usp=sharing Full live demo: https://drive.google.com/file/d/178inYQhvB55_E9wC00r53HRkvtmSWTgP/view?usp=sharing How WE built it We constructed the battle dome and hologram projector using cardboards, coloured paper, and monitor display. We build the machine learning model using Keras and tensorflow. We trained the model with custom dataset with 15k images gathered during the hackathon (it took a long time). At the same time, we also worked on creating a front and backend connection to host the animations and hold the game logic. We utilized flask for the backend and used react for the frontend. Challenges WE ran into With flask being single threaded (python in general) it was difficult for us to maintain or plan for multiple thread usages, something node would do great. However, tensorflow and keras has such a great python community that we chose to stick with it. Accomplishments that WE are proud of We set out a grand vision at the beginning of Hack the North to build a hologram AI battle dome. The objective was difficult and grand in nature; however, we were able to achieve it in the end. It is more than a minimum viable product, it represents the hard work and the constant trial and error during the 36 hours of Hack the North. What WE learned We learned to decrease the scope of the project when time and resource constraints are major issues. Machine learning, text to speech, web development, and hologram. Needless to say, we were ambitious. It is as if we are building 4 projects side by side instead of one. We learned that to achieve this grand vision, we had to decrease the scope of the project and use helpful APIs to do different components. We decreased the number of consecutive hand signs from 5 to 2; we used an API called Voice Flow to build the voice controller instead of building it from scratch. All of these discussions helped us to achieve our end goal. What's next for AR Voice Control and ML Hand Sign Ninjutsu Battle Simulator The next step for the AR Voice Control and ML Hand Sign Ninjutsu Battle Simulator is to build a version of it that works for a smartphone. We already prototyped the hardware for the hologram display, all that is left is an innovative idea for the software components. After that is done, the product is ready to find early adopters from the anime fans and other markets. <div