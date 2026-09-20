---
slug: "memri"
url: "https://devpost.com/software/memri"
title: "Memri"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 725
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/developer"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Memri

> Helping memories become immersive experiences, where every moment of nostalgia transforms into vivid digital stories to view.

[Devpost](https://devpost.com/software/memri) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[developer]] [[patient_family]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** gemini, react, three.js, vast-ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for memri

## Body

Home (Globe Page) Memory Lane (Bubble World Page) Logo (Memri Branding) Inspiration Our inspiration for this project comes from dementia patients who struggled during early stages of treatment to view the link between a photo and a memory. This is one of the struggles of recall declines in memory which is often why memory degrades. Our initial idea was focused on aiding those with dementia with memory recall and piecing it all together into experience. However we then came to realisation that memory degradation effects all of us. In our day to day lives brain fog and memory issues is a real trouble that causes even the simplest of actions to become a monolithic nightmare. How many of us go downstairs and lose track of what we were meant to do because of a distraction. This modern day issue has an affect on us and our experiences in life. Making the memories we hold dear fall away and slowly become less and less noticeable in our lives, even if we try to keep them. What it does Memri stores all events as a geographical pin which the user can drop on any location of the globe. Every memory is stored on a map with a pin that contains every picture and description of the events. We convert these pictures and descriptions of each event into their own shareable scene of an immersive memory experience which can be sent across to friends and family to relive these memories as if they were vividly there. How we built it We used Three.js to render the earth models, provided by a 3D Modeller @omega and we used a node server to receive memories and process them into a backend json file. These memories were then stored along with each of their respective images. When a user clicks on the memory through the flow (Adds a memory, clicks onto the pin on the map to go into the memory lane world and scrolls through the memory lane timeline to find the memory they want to relive), the image/images and description of the memory is then sent to gemini which creates a brief about the Scene then a prompt which is sent to TRIPO AI (fallback to use Gemini and a Local Three.js Builder, this works by taking a html primitive Shapes Gemini composition from the image and representing it in the scene as a diorama), to create a scene replicating the memory which is able to segment the objects in the photo and individually generate them into a scene which the user can then explore. Once it is generated the scene is loaded into the scene experience to view by the user. Challenges we ran into 3D Models were very hard for us to create, we know that a main part of the user experience is what they visually see so we needed to find a better 3d model for each of the components. Additionally as backend developers creating frontend is relatively hard. We learnt many skills along the way and enjoyed the creation process, we are grateful to be able to submit this project to help the health of people. Accomplishments that we're proud of We created Memri with not much technical skills to us which would be relevant to the project, learning all of the programming techniques mostly during the period of the hackathon. It was extremely challenging but we got there and are proud of the accomplishments we made during this event. What we learned We learnt that memory is more than just a picture or video, but something which should be immersive. Media on its own is unable to do that, but experiences like ours can. We are not able to feel ourselves without the memories that made us who we are, it is only right that we cherish them and make them permanent. What's next for Memri Memri will go through deeper research to become a better treatment and solution to early cases of dementia. Becoming a part of their therapy and potentially aiding with treatment for later stages by adaptive recall techniques. We aim to also make memri a solution to general forgetfullness and overall a way for people to relive the experiences they have forgotten or reminisce on; We aim to provide everyone a story to read with their loved ones. <div