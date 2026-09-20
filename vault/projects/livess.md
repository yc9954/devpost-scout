---
slug: "livess"
url: "https://devpost.com/software/livess"
title: "Livess"
hackathon: "GRID Esports DataJam 23"
organization: "GRID Esports"
winner: true
words: 492
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# Livess

> Live E-Sport Stats for Opera GX

[Devpost](https://devpost.com/software/livess) · hackathon [[GRID Esports DataJam 23]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**substrate** [[geospatial]]

**stack** figma, grid.gg, react, tailwind, typescript

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for livess

## Body

Live E-Sports Stats Sidepanel shows live matches Team Stats show kills, deaths, assists for both team. Player colors change according to average kills/deaths. Player Stats show player and weapon stats. If you want, you can see live match statistics in the bottom bar of the page. If you want, you can see live match statistics in the sidebar of the page. What it does Livess is an Opera GX add-on that allows viewing live CS:GO match data. Using the Grid platform, Livess shows live match, team and player statistics to the user. How we built it 1) First, I downloaded the test data and backend files provided by Grid. 2) Then I analyzed the incoming data using Postman. 3) I designed the pages and components of the application I will develop with Figma. 4) I developed the components by creating a simple react application with Vite. 5) Then, I turned the application I developed into an add-on using CRXJS Vite Plugin. Challenges we ran into The size of each message in the data sent by the Grid was very large. Additionally, there was no documentation explaining the fields in this data. First of all, I created Interfaces by taking samples from the data I examined with Postman. I collected the values that the fields can take (for example, weapon names, event types, map names) by creating a simple application. Additionally, where I had difficulty, I asked questions to the officials in the Discord group. I am no stranger to browser extensions, I have developed extensions for Chrome before. But this was the first time I had to develop it for opera. Fortunately, the process was very similar for both of them. I needed to transmit the data coming through the socket to different units in the add-on (For example, sidebar and content). These units work in isolation from each other and communication is provided via messaging protocol. CRXJS Vite Plugin establishes a common state mechanism for these units. In this way, I can access the data I updated using Redux from both the sidebar and popup sections. Accomplishments that we're proud of I designed and developed an Opera GX add-on that visualizes data coming through Websocket. What we learned Thanks to this hackathon, I was introduced to the Grid platform. This is the first time I have developed an add-on for Opera GX. In this process, I discovered new tools and libraries to implement the project. What's next for Livess There are some features that I designed in the project but could not develop (e.g. triggers). I can complete them. I can add new features to the Trigger section. (For example, if player X gets 5 kills, donate or turn on some music or change the color of the RGB lamp in my room.) By adding location information to the data, I can integrate the mini map and generate alarms based on location information. Performance improvements and bug fixes Design improvement <div