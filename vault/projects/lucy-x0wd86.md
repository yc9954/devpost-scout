---
slug: "lucy-x0wd86"
url: "https://devpost.com/software/lucy-x0wd86"
title: "Lucy"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 486
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Lucy

> Military personnel will utilize Lucy to identify potential threats during field operations.

[Devpost](https://devpost.com/software/lucy-x0wd86) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]] [[voice_speech]]
**substrate** [[structured_db]] [[video_visual]]

**stack** arduino, chromadb, deepgram, groq, lmnt, python, spotrobot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lucy

## Body

Inspiration We are tinkerers and builders who love getting our hands on new technologies. When we discovered that the Spot Robot Dog from Boston Dynamics was available to build our project upon, we devised different ideas about the real-world benefits of robot dogs. From a conversational companion to a navigational assistant, we bounced off different ideas and ultimately decided to use the Spot robot to detect explosives in the surrounding environment as we realized the immense amount of time and resources that are put into training real dogs to perform these dangerous yet important tasks. What it does Lucy uses the capabilities of Spot Robot Dog to help identify potentially threatening elements in a surrounding through computer vision and advanced wave sensing capabilities. A user can command the dog to inspect a certain geographic area and the dog autonomously walks around the entire area and flags objects that could be a potential threat. It captures both raw and thermal images of the given object in multiple frames, which are then stored on a vector database and can be searched through semantic search. This project is a simplified approach inspired by the research "Atomic Magnetometer Multisensor Array for rf Interference Mitigation and Unshielded Detection of Nuclear Quadrupole Resonance" ( https://link.aps.org/accepted/10.1103/PhysRevApplied.6.064014 ). How we built it We've combined the capabilities of OpenCV with a thermal sensing camera to allow Spot Robot to identify and flag potentially threatening elements in a given surrounding. To simulate these elements in the surroundings, we built a simple Arduino application that emits light waves in irregular patterns. The robot dog operates independently through speech instructions, which are powered by DeepGram's Speech to Text and Llama-3-8b model hosted on the Groq platform. Furthermore, we've leveraged ChromDB's vector database to tokenize images that allow people to easily search through images, which are captured in the range of 20-40fps. Challenges we ran into The biggest challenge we encountered was executing and testing our code on Spot due to the unreliable internet connection. We also faced configuration issues, as some parts of modules were not supported and used an older version, leading to multiple errors during testing. Additionally, the limited space made it difficult to effectively run and test the code. Accomplishments that we're proud of We are proud that we took on the challenge of working with something that we had never worked with before and even after many hiccups and obstacles we were able to convert our idea in our brains into a physical reality. What we learned We learned how to integrate and deploy our program onto Spot. We also learned that to work around the limitations of the technology and our experience working with them. What's next for Lucy We want to integrate LiDar in our approach, providing more accurate results then cameras. We plan to experiment beyond light to include different wave forms, thus helping improve the reliability of the results. <div