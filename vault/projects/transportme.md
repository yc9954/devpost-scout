---
slug: "transportme"
url: "https://devpost.com/software/transportme"
title: "TransportMe"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 648
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/geospatial"
---

# TransportMe

> TransportMe will help you find the closest bike rental, scooter, or station by texting the location to your phone.

[Devpost](https://devpost.com/software/transportme) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[climate_energy]] [[developer_tools]] [[education]] [[housing_homeless]] [[transportation]]
**user** [[educator_student]] [[general_public]]
**substrate** [[geospatial]]

**stack** amazon-alexa, amazon-lambda, multicycles, nexmo, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for transportme

## Body

Inspiration As an university student, I often find myself oversleeping and rushing to get to class. As I prepare in the morning, I don't have time to look for the closest bike whether it be switching between rental bike apps or looking around physically! I needed a quick and easy way to locate nearby bikes/scooters without using my hands. Not only will this skill help university students alike, it can entice others to use bikes instead of cars which can mitigate air pollution and ultimately, global warming. It is estimated that a typical US car produces 300 gCO2/passenger-km whereas a bike only produces 65 gCO2/passenger-km[1]. That's about 78.3% less pollution for using bikes! This skill is meant to make finding bikes/scooters more convenient and hands-free so that customers are willing to choose environmentally friendly transportation. It's a win win! What it does TransportMe tells you the closest bike or scooter within a 1.25 mile radius of a given location. It will ask for a location to search in which can be an address or a partial address. You can say find bikes , find scooters , find stations , or find provider . We currently support 10 providers: Bike: Jump, Lime, Ofo, Spin, Pony, Byke, Mobike Scooter: Bird, Spin Station: Donkey, Nextbike It can also use your device's location by adding near me at the end of the command. It will notify you how far the vehicle is and will send a link of the location to your phone. If a station is searched, it will say the number of available vehicles. Lastly, to make it more user friendly, you can say repeat to make Alexa repeat what she previously said. How I built it Using third party APIs, I used Node.js to convert addresses to geolocations (latitude, longitude) that can then be used to make POST requests to find the location of the vehicle. Fortunately, the APIs of the providers are open to the public although it took some time to go through the documentation and understand how to use each one effectively. By utilizing parallel programming inherent in Node.js, I created an algorithm to find the desired vehicle/provider efficiently. Challenges I ran into The main challenge I ran into was understanding how to use ASK SDK v2 which has an incomplete documentation. It lacks examples on how to build responses with methods such as addElicitSlotDirective and addDirective . It doesn't even describe what those methods do. However, I was able to figure it out by looking at ASK SDK v1 examples. Accomplishments that I'm proud of I am proud of creating a tool that can potentially help others and the environment at the same time! This skill can easily become a skill that students and metropolitan cities can use daily, especially if rental bikes/scooters are easily accessible. (Also being able to get to class on time is a plus.) What I learned Since this was my first time using Node.js and building an Alexa skill, I definitely learned a lot. Some of the things I learned was how AWS Lambda is used, calling external APIs to create a product, and how to deal with the asynchronous behavior of Node.js. What's next for Transportme Due to a lack of time, I was unable to add support for other countries. The APIs I'm using can also be used in Europe and the Asia pacific. I will be adding support for UK, Germany and Singapore soon. I will also try to include more providers. For Alexa devices with screens, it would be cool to show a map with pins of current location and the vehicle's location. I would also like add an option to choose the closest x number of vehicles if the user wants to find multiple vehicles. References [1] Thorpe, Daniel. “Climate Impacts of Biking vs. Driving.” The Keith Group, Harvard University, 20 June 2016, keith.seas.harvard.edu/blog/climate-impacts-biking-vs-driving. <div