---
slug: "airflip"
url: "https://devpost.com/software/airflip"
title: "AirFlip"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 946
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# AirFlip

> Flip documents effortlessly with the power of ML and speech recognition.

[Devpost](https://devpost.com/software/airflip) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** css3, firebase, html5, javascript, json, ola, python, react, speechapi, tensorflow, tfjs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for airflip
- business viability

## Body

Logo for AirFlip. Homepage--pretty empty right? Well, not anymore! Sheet music of Megalovania (doodoodoo doo) displayed here. Even better :O Camera with markers that showcase face and gesture detection for flipping pages. Inspiration Musicians. People with disabilities that impair their ability to use devices. Workers who rely on swiping seamlessly through instructions on their devices. Students who are too lazy to scroll through online textbooks to do their homework. All of these people require an alternate way to scroll through documents aside from using their fingers to interact with their touchpad, mouse, or keyboard. This is how the idea for AirFlip was invented. What it does AirFlip's core principle is to give users more seamless methods of flipping through documents without the need to touch their device (aside from opening the platform and document of course). When taken to the homepage for the first time, users can upload a PDF document that will pop up on the page. From there, they can either stick with the normal, mundane controls of how PDF navigation works nowadays--clicking buttons or specifying a specific page-- OR use the unique features our application provides! Our primary feature allows the user to flip the document by simply using a head or hand gesture in the direction they want to turn the page; the platform will use your camera and a machine learning algorithm that detects in real-time when gestures are made. Another feature involves the user speaking a specific word that will turn the document page for them; for instance, to turn to the next page, users can say "next" or "right," and a speech recognition library will recognize their words and do the deed for them! How we built it The user interface is built with React, and our machine learning model was trained using Tensorflow and is based on the pre-trained Movenet model. Tensorflow.js and Ola npm libraries were used to relay real-time video information between the frontend and our model for gesture detection. Lastly, we used the Web Speech API to develop our speech recognition feature. Challenges we ran into Git merge conflicts; losing progress with code a few times; tireless debugging at night; the common struggles that most developers and hackathon-ers face, we faced as well. However, to go into more detail, the main struggle for us was ensuring that our platform's video footage was properly being relayed to our ML model in real-time. It was quite a hassle working with React hooks, backend requests, and asynchronous (async-await) functions to get our scripts to recognize the real-time video footage, let alone even the component itself since it would render after the scripts were running. Changing up our ML model's dimensions and matrix calculations to pair with the data the video footage provided was also something puzzling that kept us going at night; oftentimes, the dimensionalities of our data and matrices just wouldn't match up. We faced other lesser issues, but nothing compared to the gruesomeness of full-stacking everything together. Accomplishments that we're proud of Despite all of the bugs and struggles that tried to let us down, we persevered and finished with a product that we were all proud of. All of the main features we initially brainstormed for this project were successfully implemented, and we even had time to come up with a few minor features nearing the end of our hacking time (e.g. the normal controls of PDF navigation) to add icing on the top! What we learned We learned that neural networks are surprisingly effective at what they do--we did not expect them to correctly identify certain positions from pose data (the positions of the user’s ears, chin, etc.) on the first try, but they worked like magic. In addition, it is more difficult than it may first seem to ensure interoperability among different modules in a software project. What's next for AirFlip Our future mission is to improve two aspects of our project: the architecture and the model. Our project is still in the MVP stage and the neural network, despite its decent performance, could still use some improvement, while the architecture of the project still needs improvements. The next step for the neural network would be to migrate into a production-level model using industry tools like TensorFlow or PyTorch to ensure maintainability, evolvability, and scalability. In terms of architecture, our goal is to improve our state management. Business Viability This idea has lots of potential to turn into a successful tech venture. One route we could go is to turn our project into a document-editing and storage platform like Google Drive or PDF-editing tools with an incredibly unique toolset of ML-based features. Machine learning in document platforms can be used in a variety of ways, not just for gesture detection and speech recognition for navigation but also (as an example) for sorting files using unsupervised learning. A source of revenue for this idea would be to incorporate pricing plans, with more plans offering more extensive sets of features like more storage and better ML performance. Another potential route for this project is to turn it into a tech platform that helps automate any mundane task like scrolling through a PDF using ML, more specifically gesture detection and speech recognition. Again, our main source of revenue would most likely come in the form of pricing plans that offer more robust features as you climb in price. Near the end of the hackathon, our team realized that gesture detection and speech recognition have countless uses outside of our app, especially with regards to making services more accessible to everyone. No matter which route we follow, AirFlip will bring a significant impact to the world. <div