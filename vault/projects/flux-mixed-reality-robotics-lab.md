---
slug: "flux-mixed-reality-robotics-lab"
url: "https://devpost.com/software/flux-mixed-reality-robotics-lab"
title: "Flux - Mixed Reality Robotics Lab"
hackathon: "Meta Quest Presence Platform Hackathon 2024"
organization: "Meta"
winner: true
words: 578
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "user/educator_student"
---

# Flux - Mixed Reality Robotics Lab

> Flux is a Mixed Reality Robotics Lab for the Quest where you can write Arduino code, connect electrical components, simulate circuits, and build and prototype robotics projects - all in one app.

[Devpost](https://devpost.com/software/flux-mixed-reality-robotics-lab) · hackathon [[Meta Quest Presence Platform Hackathon 2024]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**user** [[educator_student]]

**stack** c#, javascript, node.js, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flux - mixed reality robotics lab

## Body

Inspiration Outside of VR and game development, our team has always been passionate about robotics and how great it is as a beginner-friendly tool for teaching and learning coding. We wanted to bring the culture of making and tinkering, and extend it in Mixed Reality. We thought that we can create a platform that makes learning and experimenting with robotics more accessible and engaging. What it does Flux is a circuit simulator and robotics prototyping tool all in one app. Users can choose from a variety of electrical components and connect them to create projects from a blinking LED to a fully functioning Robotic Arm. These components can then be connected to a virtual Arduino microcontroller, which can be programmed and compiled in-app to control their functions. With an integrated environment for coding, building, and testing, Flux streamlines the process of learning and experimenting with robotics and electronics. How we built it The central aspect of Flux is the microcontroller simulation, which is actually handled externally with a locally hosted Node.js server. This server performs the compilation and actual running/simulation of the code. The Unity representation of the microcontroller then communicates with this server to determine the values of output pins and to monitor those of the input pins. These signals are then relayed through connecting wires around the circuit, allowing users to create dynamic projects and applications. Challenges we ran into With the ambitious scope of the project and its technical nature, we struggled to manage our hackathon time and schedule effectively. Setting proper limits on the features we wanted to introduce was challenging, as there were so many exciting possibilities to explore. We also didn't have enough time to make the demo more accessible to someone with not much experience with circuits, as it should have been the goal since the potential of the app is more on education. Our current demo is mostly showcasing the platforms features as a simulation instead of as an educational tool. Accomplishments that we're proud of One of our earliest accomplishments is that we're able to make the external microcontroller simulation work at all, as the rest of our project was hanging on it. What we learned We re-learned a lot of circuits and robotics topics we haven't touched in a long time and got to know what it takes to simulate those in an app. What's next for Flux - Mixed Reality Robotics Lab Built-in simulated microcontroller - this part was originally out of scope and we had to rely on integrating and adapting an existing solution outside of the application. Ideally though, this is something that is already built-in and runs within the application itself. Beginner Tutorials/Demos - we wanted this platform to be a good tool for teaching robotics and programming to complete beginners. given the engaging and spatial nature of VR and MR, we believe there's a lot of potential with regards to education on this platform. In-App Modelling/Building - we envision this platform as tool where people can prototype and test builds that they can actually assemble in real life. Having a basic modelling tool to create bodies, enclosures or frames that they could 3d print and use in a real life version of their projects would work great for this goal. Multi-User Collaboration - being able to prototype together with other people and play around with your builds is something exciting albeit an ambitious feature that we would want to see one day <div