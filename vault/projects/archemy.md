---
slug: "archemy"
url: "https://devpost.com/software/archemy"
title: "ARchemy"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 507
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# ARchemy

> Did you ever want to learn alchemy, but you were limited by the laws of physics? Well, fret no more. With the help of AR-chemy, you can be a wizard and change the world. Kinda.

[Devpost](https://devpost.com/software/archemy) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** ar, cloudflare, gpt, python, snap3d, spectacles, sql, sqlite, typescript

## How they structured the write-up

- 💡 inspiration
- ⚙️ what it does
- 🧱 how we built it
- ⛈️ challenges we ran into
- 🥇 accomplishments that we're proud of
- 🧪 what we learned
- 🚀 what's next for archemy

## Body

💡 Inspiration Our team really enjoyed playing games like Little Alchemy, and Infinite Craft, where we get to take basic building blocks and challenge the limits of our imagination. But we wanted to take this to the next level. What if instead of clicking pixels on a screen with a mouse, we move these building blocks into the real world? What if we could spawn anything from a toaster, to a dragon, to a transformer right before our eyes, all with the use of our fingertips? Well, you can achieve all of this through ARchemy. ⚙️ What it does ARchemy is an augmented reality crafting game that lets players combine elemental building blocks to create new ones in real time. Using Snap Spectacles and Snap3D, players can pick up, merge, and transform objects around them into entirely new creations. Whether it’s fusing a chair with fire to make a “throne of flames” or combining a duck with a car to make a “quackmobile,” the possibilities are endless. The experience blends physical gestures with immersive AR visuals so you feel like a true digital alchemist. 🧱 How we built it We used Snap Spectacles and Lens Studio as the foundation for the AR experience. Snap3D powered our object generation pipeline, while a backend service managed caching and retrieval of previously generated 3D assets for speed and efficiency. We also connected to an external LLM (GPT) service to help interpret user prompts and guide object generation, ensuring creative and unexpected combinations. ⛈️ Challenges we ran into Optimizing 3D asset generation/retrieval. An issue with the Snap3D API was its slow 3D object generation. The app generates lots of different objects and so we wanted a way to cache previously generated 3D assets and quickly load them from storage. We tried two approaches: storing objects in memory, and storing the objects in an external database and querying them with a dedicated backend server. 🥇 Accomplishments that we're proud of Our team has never worked with AR and so it was very rewarding to learn how it worked. Additionally, we are proud of the fact that we dove into Snap's developer ecosystem, working with the Snap3D API, remote gateway LLM services, and Lens Studio. 🧪 What we learned We learned how to integrate multiple technologies into one seamless experience, from AR technology to efficient backend services. We also gained experience in optimizing system performance through caching 3D objects. On the design side, we learned how important neat component design (modularity, event driven architecture) is to scaling the project. 🚀 What's next for ARchemy We want to expand ARchemy into a multiplayer experience, so friends can collaborate or compete to create the most imaginative objects in shared AR worlds. We also plan to improve the object generation pipeline with better caching and fine-tuned AI models, as well as expand the “crafting tree” to support thousands of possible combinations. In the future, we envision ARchemy evolving into a platform for creativity, education, and entertainment, helping people explore the boundary between imagination and reality. <div