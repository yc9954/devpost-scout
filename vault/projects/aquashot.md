---
slug: "aquashot"
url: "https://devpost.com/software/aquashot"
title: "Aqua Shot"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 792
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/web_dom"
---

# Aqua Shot

> Spray your friends, and make NFT's that we'll send! Interact with and cherish memories with creators through physical interactions that turn into NFTs.

[Devpost](https://devpost.com/software/aquashot) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[web_dom]]

**stack** aptos, c++, ipfs, opencv, pinata, python, react, teensy, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aquashot

## Body

Mockups of our product box for placement and planning. CAD model of our tapered nozzle and base to increase distance and accuracy. Judy's genuine reaction to our NFT captured memory. Custom electronics board with Teensy 4.0, MOSFETs for pump and LED control, power distribution, and servo output headers. Our 2-tiered setup before we added water. Inspiration This project was inspired by our curious naïveté in integrating interdisciplinary technologies… and the desperate need to wake up a certain friend incapable of waking up to any traditional alarm. Every Thursday at 5am, everyone but him within a 2 room radius would wake up to his alarm. We were drawn to the use of water as a potential alternative to a traditional alarm. Thinking beyond an alarm, we found an opportunity to use robots to augment livestreams and strengthen the bond between content creators and consumers. As users donate to control the robot and interact with a creator, they receive NFTs of moments that can be cherished far into the future. We came to see a use case in the realm of virtual human interactions. Particularly, we focused on how to foster a more meaningful connection between streamers and their audience, which platforms such as Twitch are constantly trying to find innovations in. By getting people more involved in the moments, we are able to create not only those interactions, but also create an in-person anchor point for the people, representing key components streaming sites have yet to utilize: the warmth and intimacy that real-world interactions and memories can provide. What it does Users pay using Aptos for a water turret to spray water at somebody’s face. The user interacts with the website we made, which has integration for Aptos' Petra wallet, as well as a livestream showing what a creator is doing. We mounted a separate webcam on a turret, which uses facial recognition to track people, and aims the water nozzle at their face. When someone donates through the site, the pump activates, and a recording of the moment is made into an NFT and sent back to the user's wallet. Overall, the interaction between our hardware and software (Web3 integration, CV, motor controls) is what drives the user experience. How we built it We designed and fabricated the aqua shooter (our water-spraying turret-targeting robot) using 3D printing, laser cutting, soldering, and manual fabrication using various other tools. We used many libraries and programming languages to program the various parts of our project. We used Typescript, HTML, Python, and C++ programming languages, along with the most notable packages we used being React for the website, Aptos SDK for Aptos integration, OpenCV alongside the face_recognition package for face tracking, and Pinata-python for uploading videos to IPFS. Challenges we ran into The biggest challenge was integrating the software and hardware. With complex software and hardware components, we had to find ways to bring them all together at the last moment. Some of these included the installing of different software packages, the design of complex small parts, and finally the integration of everything after we had tested each individual component of the project and needed to tune it. Overall, the unpredictable results, or lack thereof, from these different components interacting was stress-test for communication, planning, and technical precision. Accomplishments that we're proud of In a project with so many different parts, we are proud that we could integrate many different disciplines together and successfully come up with this unique system that brings both joy and utility to its users. What we learned We learned many aspects in Aptos, OpenCV, and robotics through this compiled fun project! In addition, we learned how to integrate these very different disciplines into a complete project, ensuring precision on all fronts before piecing together the puzzle. What's next for AquaShot Although we were only able to create one new avenue of physical interaction, we hope to continue expanding the ways that meaningful physical interactions can be included in virtual interactions. While this project’s goal was a mix of futuristic technologies for fun shenanigans, we look to bring these tools forward for the purpose of bridging the connectivity gap between the physical and virtual worlds. Indeed, the Aqua Shot should not be seen as a standalone, but rather an example feature of what the product could include. In addition, there remains the possibility for an entirely new type of investment/trade market. On one hand, streamers will opt in on these technologies due to promises of higher donation revenue. On the other, viewers will be actively placing bets on moments and memories that will stand as valuable to the community, making them active entertainers as well. As a result, we envision an entirely new type of engagement in entertainment and human relationships. <div