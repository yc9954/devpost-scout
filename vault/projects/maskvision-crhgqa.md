---
slug: "maskvision-crhgqa"
url: "https://devpost.com/software/maskvision-crhgqa"
title: "MaskVision"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 514
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MaskVision

> Protecting people through intelligent, real-time face mask detection.

[Devpost](https://devpost.com/software/maskvision-crhgqa) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**substrate** [[structured_db]] [[video_visual]]

**stack** dataset, keras, machine-learning, numpy, python, streamlit, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maskvision

## Body

Deep learning based detection- Person not wearing mask Deep learning based detection- Person wearing mask Landing Page Image upload Inspiration MaskVision began with a simple question that stayed with me during the pandemic: how can we help people stay safe in public settings without putting the entire responsibility on manual monitoring? I saw how inconsistent mask usage could be, and how challenging it was for public places to encourage compliance in a gentle, scalable way. I wanted to explore whether technology could quietly assist in this process. That curiosity became the inspiration behind MaskVision . What it does MaskVision analyzes an uploaded face image and predicts whether the person is wearing a mask. It provides a clear label and a confidence score so the user understands how certain the system is. The goal is to make the experience simple and immediate: upload a photo, and get a result within seconds . How we built it The project uses a binary image classification model trained on a dataset of masked and unmasked faces. The images were resized , normalized , and prepared for training. The model was then integrated into a Streamlit application, where I focused on creating a clean and accessible interface . CSS overrides were used to improve the appearance beyond Streamlit’s defaults. The prediction flow, image display, and feedback messages were all refined to feel intuitive for users. Challenges we ran into Several unexpected issues appeared during development. Getting consistent predictions across images with different lighting , angles , and backgrounds required a lot of experimentation. Streamlit’s layout system also created challenges when aligning components and styling them consistently. Technical details like model loading paths , image preprocessing differences , and preparing a proper 3:2 thumbnail for submission took more time than expected. These small obstacles added up, but each one pushed the project forward. Accomplishments that we're proud of I’m proud that MaskVision became a complete and functional tool rather than just a trained model. Building a full pipeline—from data preparation to UI design and deployment —felt rewarding. The final interface is smooth , and the predictions are presented clearly . I’m also proud of how much the project evolved from the original idea. Seeing it come together into something coherent and usable is an accomplishment on its own. What we learned This project taught me how important the full development process is, not just the modeling part . I learned how to balance accuracy with usability and how design choices affect how people experience an AI tool. I also learned to iterate quickly , troubleshoot unexpected issues, and adapt when things didn’t work the first time. The experience strengthened my understanding of both machine learning and practical deployment . What's next for MaskVision Future improvements include adding support for live webcam detection expanding the dataset to improve robustness identifying partial or incorrect mask usage I also want to explore deploying MaskVision as an API so it can be integrated into other systems. The main goal is to continue refining it into a reliable, real-world tool for safety awareness . <div