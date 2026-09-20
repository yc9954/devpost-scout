---
slug: "learnscape"
url: "https://devpost.com/software/learnscape"
title: "LearnScape"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 583
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# LearnScape

> Project developed to make CNCF landscape easier and more accessible to beginners

[Devpost](https://devpost.com/software/learnscape) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[structured_db]]

**stack** alanai, css3, datree, docker, firebase, html5, javascript, node.js, react, stream, twilio

## How they structured the write-up

- 💡 inspiration -
- ⚙ what it does -
- 🔧 how we built it-
- 💪 challenges we ran into -
- 📌 accomplishments that we're proud of -
- 📚 what we learned -
- ⏭ what's next for -

## Body

CLI homepage CNCF chat getstream.io ask Alan the roadmap 📈 LearnScape 📈 💡 Inspiration - Going through the CNCF landscape and getting started with contributions gets overwhelming. We wanted to simplify the existing landscape for beginners and added a roadmap too for folks who want to learn more in the field of DevOps. This platform is developed such that it can guide new folks and learn concepts such as Docker and Kubernetes even if they contribute to this project because of the tools used in this project such as Docker, Datree, Alan AI, Firebase, getstream.io and Twilio. ⚙ What it does - Simplified CNCF LandScape where you can filter, search projects to contribute according to your tech stack Get your questions answered about DevOps by Alan AI Get your own personalised roadmap to reach your goal of DevOps Twilio will alert the project admins if there occurs any error in the server and server is about to shut down Get your brains working and join, network with other contributors of CNCF in the chat channel powered by getstream.io 🔧 How we built it- Developed an API to get all the projects in the database and specific project from large project data. The project id is given by the database. This API will also give you number of project provided in limit field and you can increment the page no to get the next limit frame data along all names of the projects. Check out the documentation of API here The fronted/client consumes this api in order to fetch the details of the several cncf projects and their information which can be needed by the beginner. We used Alan AI to develop a DevOps FAQ and roadmap section which could guide beginners on how to get started. Check out the Alan assistant implemented here For folks to get more involved and carry the conversations on the platform itself we used getstream.io to created a messaging channel where you could ask anything related to CNCF. Want to escape the chaos caused by server failure? Yes we can! by the use of Twilio . We used it to get notifications before a server goes down. //Twillio function here client.messages .create({ body: 'App crashing!!', from: '+15017122661', to: process.env.DEST_NUMBER }) .then(message => console.log(message.sid)); } Used Datree While starting the configuration it's essential to make sure that there is name specified for the deployment.Not having this might not raise errors by the native development kits (kubectl etc) but naming the deployment configurations while working with several clusters in a team is essential and cosidered a good practice. Check it here Used Google Dev Library's Firebase to host the react app. 💪 Challenges we ran into - We could not properly implement the API to frontend because of time constrictions and we tried to make use of each and every tool in a creative and unique way possible. This project has still lot of potential and improvements to make. 📌 Accomplishments that we're proud of - Although we were not familiar with most of the tools and tech we used to build it, we tried and learned on the go to make it possible. 📚 What we learned - We learnt about react and how to make use of all the tools according to the use case of our project even if they were different and sometimes caused a lot of trouble. ⏭ What's next for - Proper implementation of frontend to get all the projects from the API. <div