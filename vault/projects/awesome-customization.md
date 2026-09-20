---
slug: "awesome-customization"
url: "https://devpost.com/software/awesome-customization"
title: "Awesome Customization"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 389
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Awesome Customization

> Awesome Customization is a workspace that shows how you can dynamically pull images, videos, and other media from awesome APIs to create customizable user experiences.

[Devpost](https://devpost.com/software/awesome-customization) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** api, javascript, postman

## How they structured the write-up

- inspiration 🤓
- what it does 🏭
- how i built it 🏗️
- challenges i ran into 🙄
- accomplishments that i'm proud of 🍾
- what i learned 📓
- what's next for awesome customization ⏭️

## Body

Unsplash Visualize GIF Unsplash API Search Mini Demo Inspiration 🤓 I was inspired by Kyle Calica's demo: "Visualizing Open Brewery Data with Bootstrap" . His demo gave me a lot of ideas on how I could make an API response a bit more interesting than just some nicely formatted JSON. The Postman Visualizer takes API development a step further and allows me to demonstrate how the response data from an API can be used. What it does 🏭 The Awesome Customization workspace: Provides a number of API collections that pull media resources from APIs around the web that can be used to create customizable user experiences. Shows how to use each of the APIs and set up the different authorization types. Visualizes the output so that developers and creators have a better understanding of the data being returned and how it can be used. How I built it 🏗️ I built everything in the Postman web interface and used the browser developer tools to debug and tweak the visualizations. I also read a lot of API docs! Challenges I ran into 🙄 I had little trouble understanding how to manage secrets/keys in a workspace I intend to make public. I wanted to make sure I wasn't going to accidentally share all my secrets and keys with the world. I ended up using variables and just setting the "Current Value" which doesn't get sent to the server. I had trouble getting YouTube videos to embed in the output visualization. I think it is an iframe related issue. I output the embed tags instead so folks can see how the embed tags are generated. Accomplishments that I'm proud of 🍾 I was excited to see actual images in the visualization output. I think this provides further validation of the API output. What I learned 📓 I learned about postman features I had never touched: Workspaces Pre-request Scripts (helpful for the Gravatar email hash) Test scripts Visualize How to use variables for Authorization How to use several APIs including: ** Creative Commons ** GIPHY ** Google Fonts ** Gravatar ** Pixabay ** The Noun Project ** Unsplash ** YouTube What's next for Awesome Customization ⏭️ There are likely many more APIs that can provide some awesome customizations. Freesound has an API that would be cool for creating a dynamic sound-board. 🔊 <div