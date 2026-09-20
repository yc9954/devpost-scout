---
slug: "communites-against-corona"
url: "https://devpost.com/software/communites-against-corona"
title: "Communities Against Corona"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 752
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/elder_child_care"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Communities Against Corona

> Covid-19 has led to the scarcity of essential items such as toilet-paper and water. This website provides a platform for people to help their communities by offering their extra resources to others.

[Devpost](https://devpost.com/software/communites-against-corona) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[elder_child_care]]
**user** [[general_public]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** bootstrap, css, firebase, google-maps, html5, javascript, jquery

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for communities against corona

## Body

map map on mobile Sample marker How the user is able to add markers Marker management Inspiration Covid-19 has introduced many problems to the general public. One important problem that we have failed to address is the issue with the scarcity of essential items. I too have experienced this issue when my family couldn't buy items used daily such as toilet paper as they were out of stock because of irrational fear. Senior citizens are heavily affected by this issue and may not be able to find the resources they need on their own. What it does Communities Against Corona is a responsive website that is designed to create a platform for communities to reach out to each other and help them by offering extra resources they might have such as toilet paper, water, food, etc. Users of the website can place markers on the map and can indicate what resources they are able to provide. They can also add a label to the markers with information such as their name, phone number, address and a short description. Users can modify their markers and see that their changes are deployed in real-time to all users currently logged in. How I built it For the front-end of the website, I utilized HTML5, CSS, and Javascript. I also specifically used the bootstrap CSS library to create and modify the UI and look of the website. For the backend, I used Firebase to handle all the requirements. I used firebase google authentication to authenticate and manage the users. Furthermore, I used Firebase realtime database to store the location and show the markers in real-time to the users. To create the map and place the markers, I used the google-maps javascript API. I also used google maps geocoding API to convert user-inputted addresses to latitude and longitude. Finally, I deployed the website to the internet using Firebase hosting. Challenges I ran into I ran into many challenges along the way and often found my self frustrated. This was my first time dabbling with firebase, databases and user authentication. One challenge I ran into was that when I tried to access the firebase user it would show up as null. I had to use firebase's onAuthState function to access the user. This function would run when the user logged in and made sure that the code wouldn't run when the user wasn't logged in yet. Another challenge I ran into was that after I created the markers, there wasn't a way for me to modify the markers and delete them. To approach this problem, I had to create a global array of the marker objects and had to store a unique id in the marker object. This allowed me to find the specific marker when the database was modified and deploy the changes accordingly. Another difficult challenge that I came across was that my website was not working on certain browsers such as safari. This led to me learn more about browser compatibility and I hate to restructure the code without needing async and await functions that were causing errors in safari. Accomplishments that I'm proud of I am very proud that I was able to finally finish a project. My personal connection with this project has helped me persevere through my obstacles. I am also proud that I was able to figure out firebase realtime databases as this was the first time I used a database whatsoever. Most importantly, I'm proud that I took the initiative to help out my community and the people I interact with and love. What I learned I learned a lot about HTML5, CSS, and Javascript. I also learned about plugins such as Jquery and Bootstrap. Furthermore, I learned a lot about cloud and realtime databases and user authentication and management. This project has also taught me how to adapt when my code isn't working and has given me knowledge on how to complete a project from its initial stage to deployment. What's next for Communities Against Corona My goal is to get this website to the hands of many people as possible. To truly make a change, this website needs to be more exposed. I hope to talk with my city officials to come with a plan so that my website can help my community. I also want to be able to work with an organization as more volunteers are needed to transport the resources to people who can't freely travel such as seniors or people with high-risk conditions. <div