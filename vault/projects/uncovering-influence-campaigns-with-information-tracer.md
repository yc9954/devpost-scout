---
slug: "uncovering-influence-campaigns-with-information-tracer"
url: "https://devpost.com/software/uncovering-influence-campaigns-with-information-tracer"
title: "Uncovering Influence Campaigns with Information Tracer"
hackathon: "Chirp Developer Challenge"
organization: "Twitter"
winner: true
words: 790
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Uncovering Influence Campaigns with Information Tracer

> Information Tracer is a real-time system to detect influence operations on Twitter and beyond. Our tool is used by researchers to investigate misinformation, spam accounts and bot campaigns.

[Devpost](https://devpost.com/software/uncovering-influence-campaigns-with-information-tracer) · hackathon [[Chirp Developer Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[media_journalism]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** bootstrap, d3.js, flask, google-cloud, javascript, mongodb, python, redis, twitter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for uncovering influence campaigns with information tracer

## Body

Visualization of a real-world, multi-platform influence campaign -- The Federalist [detected by Information Tracer] Visualization of a real-world, multi-platform influence campaign -- Todd Starnes [detected by Information Tracer] Visualization of a real-world, multi-platform influence campaign -- Red State [detected by Information Tracer] Visualization of a real-world, multi-platform influence campaign -- Breitbart [detected by Information Tracer] Visualization of a real-world, multi-platform influence campaign -- Life News [detected by Information Tracer] Visualization of a real-world, multi-platform influence campaign -- The Blaze [detected by Information Tracer] Visualization of a real-world, multi-platform influence campaign -- The Western Journal [detected by Information Tracer] Information Tracer Web Interface Information Tracer data pipeline Inspiration Hi my name is Zhouhan. I graduated from NYU Data Science PhD program on May, 2022. This project -- Information Tracer, was born out of my PhD thesis. My research has long focused on internet safety and anti-abuse. When pandemic started in 2020, I became increasingly worried about the spread of misinformation online, and started to build systems to help researchers visualize and contextualize how information spreads. Fast forward after graduation, I created Safe Link Network, a company dedicated to making the Internet safer and more connected. Information Tracer is the project I'm building now to detect fake news and other inauthentic behavior on Twitter and beyond. What it does Information Tracer is a real-time, cross-platform system to detect information operations such as disinformation or bot campaigns. We provide an infrastructure to enable users to choose metrics, set thresholds, and monitor potentially manipulated news content. We also apply advanced clustering algorithms to detect potentially coordinated actors across multiple platforms. Currently, our system takes a URL, hashtag or keyword as an input, then collects posts that mention the input from five social media platforms—Twitter, Facebook, YouTube, Reddit, and Gab. We provide both an interactive web interface and API endpoints to cater different use cases. How we built it I developed Information Tracer from scratch. The back-end is in Python. I use Twitter V2 API, Meta Crowdtangle API, Google YouTube data API and my own crawlers to collect data. I store data in MongoDB and custom file systems. On the server side, I use Python Flask to serve the webpage and API endpoints. For front-end, I use JavaScript, Bootstrap and D3js for visualization. To support real-time search, I use Redis to schedule jobs. I host my application on Google Cloud Containerized OS Instance. Challenges we ran into Data collection and data coverage. Among all platforms, Twitter V2 API is the most comprehensive and well-designed. We have difficulty collecting data from platforms such as Telegram and Whatsapp. Those platforms do not have developer-friendly API. Interface design. The intended user of our tool is researchers and fact-checkers. We realize that people have different technical backgrounds -- some want to use a web interface, while others want API endpoints. We need to make multiple interfaces to serve different needs. Accomplishments that we're proud of I presented Information Tracer and its real-world applications at MisinfoCon at DEFCON30 in 2022. The presentation is well received by the community! Here is a link about the conference. I was selected as 1 of 5 start-ups to compete in the NYC Media Labs AI and Local News Challenge in early 2022. I was awarded $7500 initial funding, and $5000 follow-up funding. Here is an tweet about me presenting at the Challenge. I presented Information Tracer at July 9 at the Computation + Journalism conference @BrownInstitute. Here is the conference information . On Twitter, Information Tracer has received positive feedback from professors and researchers . The tool is also used by journalists and activists to investigate online abuse . What we learned Information spreads across the Internet. Focusing on a single platform will limit our scope and understanding. Aggregating information across many platforms is very important and insightful. We are on the right track, but still have a lot to build. Some users prefer web interface, but others prefer API. As a result, we now support both Web and API access to our system. It is very important to talk to potential users to hear feedback. That is why we actively participate in challenges to receive as many feedback as possible. What's next for Uncovering Influence Campaigns with Information Tracer Keep sharing threat intelligence. We are reaching out to industry leaders. We have shared our research and results with multiple teams -- Machine Learning Health Team at Twitter, URL Integrity Team at Meta, and Jigsaw Team at Google. We plan to further our collaboration in the future. Research and development. We plan to use additional funding and resource to improve our system, including adding data source (other social media platforms), enriching our API endpoints, and exploring more clustering algorithms to identify coordinated actors. <div