---
slug: "hot-spot-4961jt"
url: "https://devpost.com/software/hot-spot-4961jt"
title: "Hot Spot"
hackathon: "Garuda Hacks 2020"
winner: true
words: 654
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Hot Spot

> An app that keeps the community safer by heatmapping patient history and analyzing the risk of infection for every location.

[Devpost](https://devpost.com/software/hot-spot-4961jt) · hackathon [[Garuda Hacks 2020]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[elder_child_care]] [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** css, express.js, google-maps, heroku, html, javascript, mongodb, mongoose, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hot spot

## Body

Hot Spot Logo A heat map of sample data. Red = Do not go near! The dashboard where hospitals/health officials can input data Registration page for hospitals, including an interactive map Brief summary of Hot Spot, as seen on the live app Inspiration We were inspired by the world’s slow recovery from the COVID-19 pandemic. As people are starting to go outside again, whether necessary or not, there needs to be a system for citizens to know the risks of certain locations. Simply knowing the number of people at a location is not enough; COVID-19 has been shown to remain airborne on various surfaces for extended periods of time. We wanted to create an app that could allow everyone to view the risk of infection on a convenient heatmap, which would allow people to notice patterns and determine which locations are safe to visit. What it does Hot Spot provides users with a live-updated heat map that shows the infection risk of various locations. Data is uploaded by hospitals and health officials about the locations that infected patients/high risk patients have visited recently, as well as how long they spent at that location. Using high-accuracy geolocation API, entries about each patient’s location history and time spent can be easily added and stored in a global database. Hot Spot then compiles this data such that the user can view any location on earth and select a location to view its risk factor. Hot Spot has several implications in helping to stop the pandemic. First of all, it allows the elderly/highly susceptible population to step outside while avoiding the regions of highest risk. Secondly, non-infected people can also check in with Hot Spot so they can stay informed and safely enter the public while avoiding infection (or re-infection). Users can also check locations that they have been to recently, and if the heatmap indicates that that location is high-risk, the user can self-quarantine in order to prevent further transmission. We believe Hot Spot has the potential to track and stop the transmission of COVID-19 on both a municipal and global scale. How we built it Hot spot is a web app backed by a Node.js server using the Express.js framework. Data from users is sent to the server and stored in a MongoDB database. Addresses and longitude/latitude data was converted using an external Geolocation API. The frontend was created using React and coded in Javascript. The maps on the website used the Google Maps Javascript AP Challenges we ran into The challenges we ran into mostly consisted of small debugging issues. However, there was one larger problem when we tried to host our app on Herokuapp.com; we had all our backend files stored in the "backend" folder, but they had to be in the root directory or else it wouldn't work. Accomplishments that we're proud of We are extremely proud of Hot Spot overall as it has the potential to make a difference in everyone’s worlds. In particular we are proud of the aesthetic user interface of our app and the global functionality using geolocation API (converting addresses to longitude-latitude). What we learned We learned a lot about the full stack development experience. Having to handle all the frontend and backend ourselves, we now have more experience on developing apps and how to maximize workflow. We’ve gained a good deal of experience working with various technologies and APIs, including geocoding APIs, Google Maps APIs, and theming using Bootstrap What's next for Hot Spot Next steps for Hot Spot could include an automated verification system to verify hospitals and health officials, so that manual account creation is not necessary. Hot Spot could also implement some AI to recognize infection patterns and make more accurate risk assessments. It would also be useful for Hot Spot to be integrated with location services like Google Location History, which would aid hospitals in creating a location history for a patient. <div