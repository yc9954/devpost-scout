---
slug: "farmware-omy1wa"
url: "https://devpost.com/software/farmware-omy1wa"
title: "Farmware"
hackathon: "Zero to One Hackathon by Convex"
organization: "Convex"
winner: true
words: 545
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/disaster_emergency"
  - "domain/scientific_research"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Farmware

> Using satellite imagery to provide historical soil moisture readings for farmers.

[Devpost](https://devpost.com/software/farmware-omy1wa) · hackathon [[Zero to One Hackathon by Convex]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[disaster_emergency]] [[scientific_research]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]

**stack** convex, leaflet.js, next.js, nextauth, react, shadcn, tailwind

## How they structured the write-up

- inspiration
- how we built it
- tech stack:
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for farmware

## Body

Inspiration Sabih: I wanted to use free and open satellite imagery for an agricultural or environmental purpose. I had another real-time wildfire tracking idea but that was too complex. Using established methods on how to use satellite imagery to meaurse soil moisture was more feasible. To read more about the way we used satellite imagery, check out this article . How we built it The European Space Agency has a variety of satellites orbiting the Earth. We used one called Sentinel-2 . It gave us a decent resolution as well as a pleasing revisit time of just 5 days. We access all the captured images through their Sentinel Hub API . For background, a satellite image contains more than just what you see. It captures the RGB wavelengths and more. What the human eye sees is just a portion of the possible wavelengths energy can be.. The sensors on a satellite like the Sentinel-2 capture different portions of wavelengths . These different wavelengths can be used in various ways such estimating soil moisture. Or even estimating nutrient levels. But this is a lot more complex based on our research so it was out of scope for our MVP. We used Convex to make the API calls to Sentinel Hub and store images in file storage. The frontend then pulls the stored images to show the user the final soil moisture image. We also used Convex for image caching for when the user requests previously requested images. Tech Stack: Frontend framework: Next.js + React Serverless backend: Convex Deployment: Vercel Component library: Shadcn Styling: Tailwind Map library: Leaflet Challenges we ran into The project required a lot of upfront research. We had to figure out which satellite(s) to use. We then had to figure out how to estimate soil moisture. We used Clickup to keep our notes organized and for commenting feedback. We also researched how feasible it is to calculate nutrient levels. It is not as straightforward as soil moisture and requires more sophisticated machine learning methods which we read about in research papers. Tech wise, replicating my teammate's Convex deployment locally was a challenge. I eventually figured it out. It was due to environment variables. Team wise, coordination between different time zones was a bit tough. We didn't have that many overlapping hours. I (Sabih) was in Canada, Ghiridar is in India, and Wenn is in Australia. Sentinel-2 wasn't the only one orbiting the Earth. ;) Accomplishments that we're proud of Making a functional tool for farmers was satisfying. Working together as a team was also nice. I thought we were a talented team who put in the work together! What we learned Planning at the beginning is very important. It determines the course of the rest of the project. Communication as well. Frontload as much information when doing a handoff. This reduces back and forth. And when replicating a teammate's deployment, make sure to include all steps. Or take a video of setting it up from scratch. What's next for Farmware Integrate nutrient level estimation. Fertilizer is composed of 3 main parts, NPK. N is nitrogen. P is phosphorus. K is potassium. We will have to read research papers and test out different methods to see what is most feasible to achieve this. <div