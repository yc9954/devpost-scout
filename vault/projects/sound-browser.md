---
slug: "sound-browser"
url: "https://devpost.com/software/sound-browser"
title: "Sound Shop"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 433
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/video_visual"
---

# Sound Shop

> A music video browsing application featuring online shopping interface

[Devpost](https://devpost.com/software/sound-browser) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[immigration_refugee]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** alexa, amazon, android-studio, cloudinary, java, javascript, node.js, sony, tivo, visa

## How they structured the write-up

- overview
- background
- how we built it
- capitol360 hackathon

## Body

Safe Browser Chrome extension Safe Browser Chrome extension Welcome to Sound Shop Overview Sound Shop is a music video browsing application for Fire TV , which includes a shopping interface for purchasing products featured in the videos. Users can conveniently and safely navigate a set of customizable auto-generated playlists and select content to play. Users can then browse products featured in the selected content and purchase products through the app. Background Music videos comprise an important part of the video streaming industry and are the consistently the most viewed content on streaming giants such as YouTube and Vimeo, which provide free viewing to users in exchange for watching advertisements to provide revenue. This often creates a clumsy user experience as viewers are repeatedly presented with ads that don't relate to the content. Sound Shop aims to create a more seamless user experience, while still generating revenue for musicians, by presenting users with the opportunity to purchase products found in the content they are viewing as well as the musician's branded merchandise. In addition products can be purchased directly through the TV app using the Visa checkout system, making the shopping experience as effortless as possible. In addition the Sound Shop supports Alexa powered voice commands for searching and video player controls when run on a Fire TV that is paired to an Alexa enabled device. The app may also feature videos for important social causes, for instance, Searching by Sony Pictures . Playlists can be created with the help of the Safe Browser Chrome extension to ensure contents appropriate for all ages, and the FireTV platform provides a safe environment for browsing content, reducing the need for accessing less secure web browser content. You can find a demo video for the Safe Browser Chrome extension HERE How We Built It Sound Browser is an Android TV application built with Java using Android Studio . The playlists are generated using TiVo's playlist creator , which creates playlists based on various styles and themes. Content and metadata are retrieved using Rovi Music API with platform optimized media provided by Cloudinary's image and video management services. Purchases are confirmed using the Visa checkout API. The Safe Browser Chrome extension is a JavaScript extension that utilizes Google's list of banned search terms to check lyrics pages for inappropriate content before adding them to a playlist. To run the extension follow the instructions for setting Chrome to developer mode and load the extension file that can be found HERE Capitol360 Hackathon You can find more information about the Capitol360 Hackathon and the creation of Sound Shop HERE <div