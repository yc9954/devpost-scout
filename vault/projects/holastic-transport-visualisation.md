---
slug: "holastic-transport-visualisation"
url: "https://devpost.com/software/holastic-transport-visualisation"
title: "HoloAstic Transport Visualization"
hackathon: "Junction 2016"
winner: true
words: 810
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
---

# HoloAstic Transport Visualization

> Bringing UPM's transport visualization to the next level - to increase customer loyalty!

[Devpost](https://devpost.com/software/holastic-transport-visualisation) · hackathon [[Junction 2016]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]]

**stack** axure, bluemix, git, microsoft-hololens, sketch, unity, visual-studio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for holoastic transport visualization

## Body

Inspiration We will bring the way of visualization to the next level and help UPM differentiating from the competition by using latest 3D technology with Mixed Reality. We were inspired by the possibilities of Microsoft HoloLens , 3D models in Virtual Reality and new ways of interaction between humans and machines. We are convinced, by using the HoloAstic Transport Visualization (HoloAstic = HoloLens + Fantastic) UPM will save money and increase customer loyalty by improving delivery reliability. The daily work on tracking orders is easier to understand and options for decision making are vastly improved. We have calculated a rough business case, and can show that our solution will save more than** 1.2 Million € annually**. Our solution includes two extensions to the HoloAstic Transport Visualization to create a complete ecosystem: Solution Module 1: Transport Prediction - A calculation engine Solution Module 2: Delivery Tracker - A simple mobile app for truck drivers What it does We are using the transport data from IBM Bluemix , enhancing it with additional transport information and external data and our solution visualizes the data on a 3D world map. The world map is showing ALL ongoing transports and orders of UPM. An indicator (RED, GREEN) shows critical transports. By using voice commands, the user is able to choose one customers and reduce the data according to his selection. In addition gesture and speech enables the user to drill down to a specific order / transport. Detailed information (product, grade, estimated time of arrival, ...) is shown to get more insights. Alternative transport methods are shown if applicable and simulations are calculated how Estimated Time to Arrival can be kept. In addition a UPM employee can invite q customer to join the session. Customer and UPM employees will be able to collaborate and deciding on the best alternatives to reach the original estimated time of arrival. In our use case, there are multiple alternatives - truck, ship and train. By clicking on the alternative route, the data will be transferred back to be Back-End. Our Solution consist of the following parts Main Solution: consists of full 3D visualization showing a top down view of all UPM transports Module 1: transport prediction will merge real time data and historical data to calculate exact arrival times Module 2: the delivery tracker, a mobile app, allows drivers to update the delivery status in real time. How we built it First we analysed the available data and discussed the different data models with UPM and Bluemix experts. Then we created paper prototypes to design the flow necessary to visualize the data. Finally we design all necessary 3D models (earth, truck, ship, train) and made them interactive. In parallel we have integrated the Bluemix APIs to include original UPM data directly in our solution. Technology used was: Microsoft Hololens, Cross Platform Development Tools, SketchUp, Unitiy 3D, Git, Visual Studio, C#, ... Challenges we ran into Collaboration: We had challenges to share our code with GIT. Solved. Data model: The data was not very easy to understand. Some adaptions were necessary to make the data usable. Complexity of 3D models. It took us a lot of time to create 3D models and then reduce the complexity of all models to ensure good performance. Availability of WLAN: As we have an online application transferring a large amount of data, it was sometimes very hard to get it running because WLAN was N/A. UI/UX Design: We invested a lot into the interaction between Human and the 3D Models. This is why our UX Designer tested several ways in prototypes before we started implementation. Our biggest concern, related to presentation is the weak WLAN which might cause performance problems. Accomplishments that we're proud of The whole solution created by our team. We did not expect to get it running within the short time. We managed to divide the roles in the team very clearly and work effective. Back-End, Front-End, Visuals, UX, Preparation of Pitch, ... HoloAstic Transport Visualization is is the very first solution on Microsoft HoloLens that allow easy analysis of transport status and logistics for the paper industry, specially customized to UPM needs. It is also possible to run the HoloAstic Transport Visualization on different devices like Mobile, Desktop - cross platform What we learned Teambulding, UPM’s business and logistic processes and to make a simple visualization for it. What's next for HoloAstic Transport Visualization We need to extend the use case. Of course it was not possible to make all data in all variants available in the Hololens Solution in such a short time. Extend the use case with new scenarios Increase amount of dynamic data and the visualization of it Increase customer collaboration capabilities Add additional calculations and predictions for transports Add Decision Support functionalities Remote Guidance with Skype or other tools (e.g. with Truck driver, loading, ...) <div