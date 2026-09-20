---
slug: "hyper-immersive-panorama"
url: "https://devpost.com/software/hyper-immersive-panorama"
title: "Hyper Immersive Panorama"
hackathon: "Google’s Immersive Geospatial Challenge"
organization: "Google"
winner: true
words: 612
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/elder_child_care"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Hyper Immersive Panorama

> Use facial detection to take a look around exciting destinations.

[Devpost](https://devpost.com/software/hyper-immersive-panorama) · hackathon [[Google-s Immersive Geospatial Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[elder_child_care]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** google-places, javascript, jquery, php

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hyper immersive panorama

## Body

MediaPipe Face landmark detection used for natural camera control. Ever wanted to see the view from the peak of MT Everest? Inspiration The concept of virtually immersing oneself in a location before physically visiting it holds immense potential and offers numerous benefits, especially in today's interconnected and digitally advanced world. Here are some key points of inspiration: Accessibility for People with Mobility Limitations: Virtual immersion can be a game-changer for individuals with mobility issues, including the elderly or those with disabilities. It allows them to experience and explore places that might be physically inaccessible, breaking down barriers and providing a sense of freedom and exploration. Affordability and Economic Constraints: Traveling can be expensive, and not everyone has the financial means to visit distant or exotic locations. Virtual immersion offers an affordable alternative, enabling users to experience the wonders of the world without the associated costs of travel. Educational Value: Students and educators can benefit greatly from virtual immersion. It can be used as a dynamic teaching tool, providing a deeper understanding of geography, history, and culture by virtually transporting students to locations around the globe. Travel Planning and Preview: For potential travelers, virtual immersion can serve as a preview tool, helping them to plan their trips more effectively. They can scout locations, understand the layout of landmarks, and get a feel for a destination, which can enhance their actual travel experience. What it does Hyper Immersive Panoramas detect the users orientation of their head using facial detection and the web camera. The real time facial orientation is then used to allow the user to look left, right, up or down, in the virtual 3D environment. We also add ambient audio and the ability to walk around using the forward and back keys on the keyboard. How we built it For the base mapping and rendering we used Cesium JS and Google Photorealistic 3d Tiles to make a realistic world environment. For the facial recognition we leveraged Media Pipe Face Landmark Detection to apply the facial position to camera movement instructions in Cesium. We then built a simple web based application to showcase how one could quickly setup navigation and audio of several different locations right inside a web browser. Challenges we ran into Media Pipe despite outputting many different facial landmarks did not provide an overall pitch, roll, and yaw of the users head. Luckily we found this brilliant work by Susanne Thierfelder that helped us get closer to our goal of using head movement to control the camera. 🙏 Some of the Google Cesium examples on the Google Developer docs were using an outdated library and we had to upgrade to V 1.111 to be able to control the sky and other environment aspects. Accomplishments that we're proud of Overall the experience is very natural. We tried to create a neutral zone where the camera does not move, and the more you look left the faster the camera moves. Overall this approach worked much better then trying to continuously update the orientation of the camera to the head, which was more jerky and glitchy. It is easy for others to update the locations and build their own experience. What we learned Working with Cesium JS API was impressive how many different controls were available for moving, zooming, and panning the camera. Coding 3D web experiences can be pretty confusing at times to not end up upside and backwards. What's next for Hyper Immersive Panorama Would love to be able to also add dynamic layers for things like cycling, mountain biking and skiing trails, so you can see where you have been or others have been like with Strava Heat Maps. <div