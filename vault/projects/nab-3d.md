---
slug: "nab-3d"
url: "https://devpost.com/software/nab-3d"
title: "Nab 3D"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 725
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Nab 3D

> Nab any object straight out of the real world and into your browser. Video to 3D web component -- all in one line of code.

[Devpost](https://devpost.com/software/nab-3d) · hackathon [[TreeHacks 2024]]

## Facets

**domain** [[civic_government]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** api, bun, cloudflare, ffmpeg, git, javascript, react, swift, three.js, vite, webassembly

## How they structured the write-up

- inspiration
- functionality
- how did we build nab 3d?
- challenges faced
- what we learned
- what's next?

## Body

Title slide! Existing workflows suck. Nab's new workflow. Nab's stack. Some of our scans! Nab 3D Inspiration Nab streamlines the process of bringing real-world objects into the digital sphere by utilizing video transformations, photogrammetry, providing a custom API to host and display them. Sophia is well acquainted with photogrammetry, having used it to create models of locations around Seattle. But the process is nothing short of terrible : Take 30 - 250 images of your object. Manually find and run a good photogrammetry model (or spend 10-20 hours 3D modeling your object on Blender) Process and export .glb Edit model in Blender and re-export Import .glb to project and set up a scene with Three.js (which usually takes at least 20+ lines of complicated, buggy 3js code) And, you have to repeat the entire process all over again for each model you want to add! Functionality Nab 3D, however, introduces a web component that does all of this in one line of code— in a matter of seconds. It revolutionizes this intricate process: It's as easy as... 1. Input a video of the object. 2. Paste our web component URL in your website. With Nab 3 D The user does not have to touch a single line of Three.js or deal with any aspect of the photogrammetry/modeling process! How did we build Nab 3D? Filled with excitement for the photogrammetry process, we dove headfirst into development. The idea of creating 3D models from videos was incredibly captivating. Yet, as we immersed ourselves in our project, we found ourselves unsure of exactly how to realize the idea. So, midway through the hackathon, we decided to pause and reassess our value proposition. With the growing importance of 3D modeling in e-commerce, our mission became clear: make 3D modeling accessible. We want Nab 3D to truly stand out as a user-friendly solution in the world of 3D modeling. We used Bun, React, Vite, and Three.js for frontend, Cloudflare for the database, Apple Object Capture API/Swift for backend, and FFmpeg for video parsing. Challenges faced We spent the first half of the hackathon building our app around Autodesk’s Reality Capture API and fighting authorization bug after authorization bug, only to realize that you can't use their API until you contact their associates — weekdays only! We struggled to find another photogrammetry API and ended up using Apple’s Object Capture API with Swift— a language none of us had developed in before. Although each and every part of our pipeline had its own set of roadblocks, almost to the point of pivoting, we think sticking with the idea paid off. What We Learned Besides learning classic soft skills like ideation and resilience, we also had an opportunity to learn completely new skills, frameworks, and even languages. In fact, two of us were beginners in any kind of web dev/JavaScript, one of us had never touched APIs and databases before, and all of us had never worked in Swift and Bun before (even though a large part of our app ended up being written in Swift!). Everyone on the team is coming out of this hackathon with not only an entirely new stack but also new friends and hilarious sleep-deprived memories. Our team members have spent countless hours ripping our hair out trying to bring 3D scans of objects into the web. For something this relevant to the future of e-commerce, advertising, and media (especially considering the rise of AR), it was surprising how slow and laborious the process was. We realized that the process did not need to be this painful – in fact, it could be simplified down to one line of code, served by an API with the help of photogrammetry. What's next? 3D e-commerce, advertising, & media are coming – and Nab's goal is to make that world accessible to everyone. Furthermore, photogrammetry lends itself to the demand for an easy-to-use scan to 3D asset pipeline, which will grow as AR/VR becomes a dominant technology and focus for advertising. The global 3D e-commerce market size was USD 11.11 Billion in 2023, with a projected 40.0% compound annual growth rate in 2024-2030. We plan to further develop this idea, with anything as big as a foray into AR/VR or as specific as potential implementations in food marketplaces like Doordash, or small businesses on Etsy. Thanks for reading! <div