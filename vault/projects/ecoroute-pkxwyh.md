---
slug: "ecoroute-pkxwyh"
url: "https://devpost.com/software/ecoroute-pkxwyh"
title: "EcoRoute"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1203
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/transportation"
  - "user/developer"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# EcoRoute

> EcoRoute is a navigation app that prioritizes the environment and takes into account transport modes (cars, bikes, public transit, rideshare) to recommend the vehicle with the least carbon emissions.

[Devpost](https://devpost.com/software/ecoroute-pkxwyh) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]] [[health_clinical]] [[transportation]]
**user** [[developer]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** css, figma, heroui, mapbox, next.js, react.js, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ecoroute

## Body

Home/Login Screen Settings Page Favorite Places Stats Page Favorite Transportation Maps Page Inspiration The inspiration for creating EcoRoute came from noticing a gap between the way people travel and our ongoing fight to reduce carbon emissions. Navigation apps today are centered around getting to your location as fast as possible but don’t consider the environmental cost of these actions. Millions of people drive short distances every day, when this same distance could be travelled by bike or public transport. While these individual choices may seem small, they quickly add up leading to a large impact on our planet. Currently, road travel is a significant contributor to global carbon emissions with ⅕ of all emissions stemming from vehicles. I was also motivated to make a navigation app that was more engaging. Current navigational apps are quite dull and boring and make travel a task when in reality it could turn into a fun mission. That’s why when I started to develop this app, I made sure to include features like stats, achievements and favorite places, which helps to gamify travel but also show users how small actions can add up to meaningful impact. What it does EcoRoute is a navigation app that helps users reduce their carbon footprint by prioritizing sustainable travel over speed and convenience. It compares transportation options such as cars, bikes, public transit, and rideshares and recommends the route with the lowest carbon emissions. For example, if a user has to get from their home to their office, the app will recommend the user to use public transport to get to their office to avoid traveling by themselves in a car which would have a greater environmental impact compared to traveling in a shared bus. The app includes features like saved vehicles and places, sustainability stats, and achievements that track CO₂ savings and miles traveled to encourage eco-friendly habits. Users can also customize preferences, such as avoiding highways or prioritizing the lowest emissions route. Built with React.js and powered by the MapBox API, EcoRoute makes eco-conscious travel simple, engaging, and accessible for everyday users. How we built it I first used Figma to design my app, and made sure to include a color scheme and mockups for each page so that it would be easier for me when I started actually developing the app. While creating the Figma design, I used Icons8 to find isometric icons for the application buttons which matched the overall design perspective I was going for for this map. When developing the app, I used HeroUI components to make the button components and establish a clear user interface throughout the app. All of the pages and components were made in React.js with lots of CSS used for styling throughout. The map, navigation instructions, and search box interface were provided by calling the MapBox API. Finally, I deployed and tested my app using Next.js. Challenges we ran into One of the biggest challenges I faced while developing EcoRoute was integrating the MapBox API into the app. Mapbox required careful setup to display real-time routes and properly calculate emissions. Getting the API to accept dynamic inputs like starting and ending points while still handling customization such as bike routes, public transport, and more was challenging. I also had to ensure that the data returned from MapBox could be combined with my own CO₂ emission calculations in a way that was accurate and seamless for users. Another challenge came from managing the user interface. Since I wanted EcoRoute to feel stylish, accessible, and engaging, I spent a lot of time experimenting with React.js components and CSS styling. Designing consistent buttons, layouts, and color schemes wasn’t always straightforward, especially since I used HeroUI and Icons8 resources alongside my own styling. Ensuring that every page looked cohesive and easy to use required extensive iteration. Sometimes, components didn’t align correctly or design aspects clashed with navigation flow, and fixing these bugs took patience. Additional limitations included restricted API support. Uber X Share does not offer ride-sharing endpoints, preventing direct integration of shared rides, and MapBox lacks full public transit routing and real-time bus or train data. Accomplishments that we're proud of I’m proud of building a fully functional navigation app that prioritizes sustainability over speed by comparing transportation modes and recommending the lowest-emission route. EcoRoute turns carbon-conscious travel into something practical and engaging through features like sustainability stats, saved vehicles, and achievements. I’m also proud of designing and developing the entire app independently from Figma prototypes to a polished React.js interface and successfully integrating the MapBox API for real-time routing while layering in custom CO₂ calculations. This project demonstrates my ability to combine technical skills, user-centered design, and environmental impact into a single, working solution. What we learned While debugging issues that I ran into while building the app, from functionality to logic errors, I had to stay patient and persevere through these challenges. For example, I spent a long time reading through the HeroUI documentation to better understand what role each component played in an app’s design. I also had to pay attention to the syntax used to incorporate these elements and then I had to carefully replicate it in my own code. Similarly I went through MapBox’s developer guides and experimented with their sample demos of their API’s to figure out how to handle routing and dynamic inputs. Additionally watching YouTube Videos and developer forums was extremely useful and seeing how other people approached similar problems showed me how I can learn from what others have done and apply it to my own programs. Another lesson I learned from the importance of iteration. Initially, my app had a very basic structure but throughout the development process, I had to refine and update key features like favorite places, stats, and more based on what I thought would work best for the user. This helped me learn the importance of user experience and how it’s fundamental to an app. Even small adjustments like adjusting where a button was or how the carbon savings were displayed made a huge difference to how a user could interact with the app. What's next for EcoRoute For a 2.0 version of EcoRoute, I would focus on adding real-time public transit data by integrating APIs from agencies like AC Transit to show live routes and transit lines. I would also aim to incorporate the UberX Share API to support seamless ridesharing. I would expand social and community features by allowing users to compare weekly CO₂ savings with friends, adding leaderboards, and supporting sustainability activities like community tree planting to increase engagement. Support for electric vehicles would also be improved by integrating EV charging stations, estimated charging times, and more refined carbon calculations that account for traffic congestion and dynamic route changes. Unlike the current version, EcoRoute 2.0 would recalculate recommendations mid-route rather than only before a trip begins. Additionally, I would introduce machine learning–based personalization to adapt recommendations based on user habits, such as preferred distances for biking or transit use in certain conditions. Finally, I would release EcoRoute on iOS and Android and expand accessibility through partnerships with local cities, such as integrating youth bus passes directly into the app, making EcoRoute more practical and impactful. <div