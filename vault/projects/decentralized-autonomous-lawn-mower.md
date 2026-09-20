---
slug: "decentralized-autonomous-lawn-mower"
url: "https://devpost.com/software/decentralized-autonomous-lawn-mower"
title: "Decentralized Autonomous Lawn Mower"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 692
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Decentralized Autonomous Lawn Mower

> Robotics as a decentralized service powered by Chainlink

[Devpost](https://devpost.com/software/decentralized-autonomous-lawn-mower) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** brownie, chainlink, diode, externaladapters, gazebo, ipfs, open-zeppelin, ros, solidity, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for decentralized autonomous lawn mower

## Body

Perimeter WebApp Inspiration Services are usually centralized and sensitive to censorship. What if you get banned from a common service such as delivery? Blockchain technology can help with this issue. We were already developing an autonomous robot for lawn mowing and we thought about how it can be more efficient by sharing it between neighbors so you can pay just for your actual usage and the robot can still be in use and efficient most of the time. Moreover, this can be accomplished in a trustless and autonomous way by paying via smart contracts. What it does We have built a decentralized autonomous robot for lawn mowing. More specifically, there is a website where you can query this service and pay for it. Also, on the robot there are various algorithms that can do the autonomous lawn mowing. For now, a single path/perimeter can be done for lawn mowing but in the future the user can input the coordinates of its perimeter for a customized lawn mowing. In this first step, the robot is simulated. The robot offers also a service to take snapshot with its cameras. These images are minted and available in the user's wallet. How we built it Robot The robot is simulated using Gazebo for the dynamics. Also the ROS (Robot Operating System) framework was used to create all the robot internal services (nodes) and communicate between them. A boustrophedon optimal path planner is used to plan the path to follow inside a given perimeter. We will not go too much into details since this part was done before the Hackathon. Mowing Service The robot has a flask server running where we can query the different services available. It exposes a websocket port where we can connect to it via ros3djs from the website. The robot launches an http server where the website's port is exposed using the Diode Network. Then from the website any user can connect to the robot by querying the websocket url of the robot. To do that, we used an external adapter that sends a request to the robot's api so we can know which url to connect to. Once we are connected, we can launch a mission which is a smart contract function for payment. It also sends the request to the robot to start mowing the grass. Snapshot Service The robot also has a camera on it so it can incidentally also take snapshots for the user to keep them. With the help of an external adapter we can send a request to the robot api to take snapshot using its camera. It will then publish it to IPFS for decentralized storage. The smart contract will receive the IPFS url of the image from the external adapter after the request has been completed. Next, the image is minted in a smart contract using the url acquired previously. The user will therefore have all the snapshots taken with this decentralized robot directly in his wallet. Challenges we ran into We had some issue with external adapters to return us strings. Accomplishments that we're proud of We are proud to have a functional demo and that we managed to put everything together as this was our first experience with web3 world. What we learned Coming from a robotics background, we learned a lot during this projects as it was our first time playing with smart contracts and frontend development. Some of the stuff we learned includes: Solidity External Adapters IPFS and Web3 Storage NFT Chainlink Brownie Diode network Javascript, HTML and CSS for frontend development ros3djs framework What's next for Decentralized Autonomous Lawn Mower Moving forward, we would like to make this project a reality by connecting this system to a real robot instead of a simulated one. Also, in order for this decentralized autonomous lawn mowing service to work, more development is needed to ensure precise lawn mowing in a more realistic scenario and with arbitrary perimeters to mow. Improvements on the planning algorithm are needed to ensure its reliability. We would also like to develop a mobile application as its more user friendly and convenient for this type of service. <div