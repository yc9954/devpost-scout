---
slug: "project-cd41lvjbiorw"
url: "https://devpost.com/software/project-cd41lvjbiorw"
title: "Backtracc"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 764
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Backtracc

> Backtracc reminds you of forgotten valuables when you leave rideshare vehicles because forgetting items in strangers' cars isn't fun.

[Devpost](https://devpost.com/software/project-cd41lvjbiorw) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[video_visual]]

**stack** cloudflare, express.js, pinata, python, raspberry-pi, samba-nova, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for backtracc

## Body

Inspiration Search up ‘lost items’ on r/uber, and you’ll find countless stories people losing valuable possessions to Uber rides and other similar services. We all lose things at some point, but retrieving your stuff is usually a pain. Imagine this: you are very excited about your family vacation, and you decide to take an Uber to get to the airport. Once you get to the check-in gate, looking for your ID, you suddenly remember that you left your wallet in the Uber. Frantically, you try to get a hold of your driver, and the vacation is ruined as you wait for Uber to return your wallet - your flight has taken off without you and your family. You begrudgingly call another Uber to get you home. From the driver's standpoint, Dan's father does drive an Uber for a living. There have been many instances of customers leaving phones, sunglasses, wallets, purses, and even trash behind them. This system benefits the driver by preventing them from needing to return the items to the original owners and wasting fuel to get there. It also entices the customers to keep the place clean. What it does Our project helps Uber drivers and riders by notifying both parties when items are left behind after their rides. Once a ride is completed, which we know when riders are no longer detected, we use a camera to check if there are any items left behind. If there are items left behind, our system will keep a log of it and will also send a notification instantly to the rider and driver as soon as possible. How we built it We ultilized 3 ultrasonic sensors to detect human presence in each back seat. The ultrasonic sensors are connected to a Raspberry Pi Pico W. When human presence is gone, the Raspberry Pi Pico W will notify the Raspberry Pi 4 over USB serial communication. From that Raspberry Pi 4, we use a webcam that is connected to take a picture of the current scene and send it to our central server for processing. In our central server, we will first send the image along with a prompt to Samba-Nova server to utilize their hosted LLama3.2-VisionInstruct-11B model in order to detect what items are left behind. If there are items left behind, the image will be stored on Pinata with key-value data to track information about the driver, rider, and the items detected. We will also let the most recent customer know about the items that they left behinds by showing the output of the Llama3.2 model from Samba-Nova and show them the image stored on Pinata by using a mobile push notification. Challenges we ran into Hardware is difficult - there are a lot more moving pieces needed to make this project work than we originally thought, between all the peripherals connected to the microcontroller, to the 3 different codebases (frontend, backend, car-hub, embeeded) we wrote in 3 languages (TypeScript, Python and C++). Accomplishments that we're proud of We used Terraform to deploy our frontend and manage our DNS on Cloudflare. This actually worked really nicely and was even faster than using the UI to manage the deployments once the config was set up. Making updates to DNS records was a breeze via Terraform. We also designed and 3D printed a clamping enclosure for the car-hub hardware using Onshape, a cloud-based CAD software. We protected our main branch and only merged into main via pull requests, which, while technically being the correct way of doing things, was definitely a first for us in a hackathon setting. It allowed us to stay on the same page even as we focused on different components on the project. What we learned Terraform We had never used Terraform before, so we learned that for the first time here! Vision LLMs Prompt engineering is a challenge and this was a huge focus for us. Measure twice, cut print once! Since we had to model around a lot of existing components, we had to make a lot of precise measurements to make the case work. What's next for Backtracc Collaborate with ride sharing services to automatically penalize riders for leaving trash behind Design a custom PCB for the hardware, enabling us to make it more compact. Add authentication to the system, enabling this solution to be deployed in the real world to fleets of drivers Aggregate analytics on lost items, including peak lost item times and most commonly lost items Add hardware to track lost items in other locations in a vehicle, such as the trunk <div