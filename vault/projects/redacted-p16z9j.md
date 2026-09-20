---
slug: "redacted-p16z9j"
url: "https://devpost.com/software/redacted-p16z9j"
title: "Hex"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 561
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "substrate/structured_db"
---

# Hex

> Hex is your personal assistant for buying a home.

[Devpost](https://devpost.com/software/redacted-p16z9j) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[on_device_local]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]] [[housing_homeless]]
**substrate** [[structured_db]]

**stack** adobe-illustrator, core-ml, express.js, figma, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for hex

## Body

Inspiration The housing market is tough as it is for new families looking to buy their first house. It just gets tougher if you don't have the right knowledge in your corner. It's extremely important to be informed throughout the home buying process, using all available tools and resources to find your home and make an investment that sets your family up for future financial success. With Hex, it's easy to go deeper than what's on the surface of a home listing. Hex aggregates data from numerous sources and utilizes innovative technologies, including computer vision, LiDAR, and generative AI to provide homeowners with the insights needed to find their home. What it does Hex helps homebuyers track information about houses they tour, first by taking a full 3D scan of the interior using hardware you already have in your pocket. Then, Hex synthesizes this data along with other relevant data about the property, to provide an estimated home value, room count, and fully interactive 3D models of each room's floor plan, making it easy to review and compare homes after tours. How we built it The application is written for iOS devices using SwiftUI. We utilized Apple's RoomPlan SDK, which takes advantage of on-device LiDAR sensors to generate an accurate 3D plan of the interior floor plan and detect other features present within a space such as furniture. We wrote an Express.js web server to facilitate all interactions with external APIs and data sources, so the iOS app only needed to interface with our web server to get all needed data. We trained an machine learning model off a dataset of DFW housing prices in the last year in order to accurately estimate home values. Initially, we planned to use TensorFlow and run predictions on a server, but using Create ML and exporting the model as a Core ML package in order to run predictions on-device allowed us to have a better user experience. We used Pandas in a Jupyter Notebook to clean the data before training the model. Finally, we leveraged the OpenAI API to support the Hex Insights feature. Challenges we ran into Since not all our team members have Macs, we utilized Swift Playgrounds on an iPad to develop some of the views and logic in the mobile app. While this was not ideal, it worked great for our usecase and integrated seamlessly back into our main project. How to apply ML well We spent a lot of time investigating how we could support homeowners with data and provide insights that are truly valuable to the user. Designing for mixed-reality Designing for the AR room scanning interface was a challenge as none of us had done this before. We wanted to deliver a user experience that felt natural and polished, since this is also a . This required investigating different design patterns and relying on Apple's Human Interface Guidelines to provide an experience that is familiar and intuitive for users. Learning the tech stack All of us worked with technologies that we weren't as familiar with, so a sizable portion of the hackathon was spent getting familiar with Swift/SwiftUI, the OpenAI API, and machine learning tools. What's next for Hex Better support for multi-room scanning Android support Highlight rooms on the 3D model Detect issues with structural integrity and other things which may fly under the radar <div