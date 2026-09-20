---
slug: "recycling-trashcan-ar-map"
url: "https://devpost.com/software/recycling-trashcan-ar-map"
title: "Recycling Trashcan AR Map"
hackathon: "Google Maps Platform Hackathon"
organization: "Google"
winner: true
words: 1293
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Recycling Trashcan AR Map

> Guide students towards the closest recycling trashcan location on campus by an AR map app (Geospatial API and Terrain anchors). It's more immersive experience than 2D GMaps with 360 photos+videos.

[Devpost](https://devpost.com/software/recycling-trashcan-ar-map) · hackathon [[Google Maps Platform Hackathon]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** arcore, geospatialapi, kotlin, terrainanchors

## How they structured the write-up

- background
- companion website
- augmented reality map thoughts
- how i built it
- api usage
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for recycling trashcan ar map

## Body

Newer version feature graphic Help students find the closest recycling trashcan location on campus Background The California State University Fresno campus has many recycling trash cans which allow selective waste disposal. Not every trashcan is selective though. My goal is to help students find the closest location to increase trash recycling rates, decrease landfill mass, and contribute to sustainability. This project aligns with the Fresno State Sustainability Club 's mission and the campus's sustainability efforts . (Note that I'm not a university employee, I'm just a fan of the club). Companion website At first a website was born which uses the Google Maps JavaScript API and shows the possible recycling locations on a "traditional" Google Map via the Marker API. The student has to pick the closest pin, and then they can see 360 photos and 360 videos of the particular trash can location. The 360 photo uses a custom fork of Google VR view for Web and the website is open source . Augmented Reality Map thoughts Handheld devices could provide a much more immersive experience than inspecting 2D maps while on the go. Clicking on pins and exploring monoscopic 360 photos and videos are fun but a native app could be more helpful for the students. An outdoor AR (Augmented Reality) map mobile app would be desirable to guide the students as seamlessly as indoor AR maps work. For example, the BWSS ARMap ( source code ) helps tech event attendees to find classrooms at a local tech venue. However my indoor AR map works with an image activation and then places the AR anchors relative to the image. The exact position and orientation of the activation images are crucial. As usual with AR or VR objects the augmented billboards (in case of the BWSS AR map the objects are billboards) are susceptible to drifting caused by sensor error accumulation as the user naturally moves. If the activation image is displaced or the orientation was modified just a tiny bit, that would have resulted in noticable object displacement especially when we talk about distances as large as a campus. The Fresno State Sustainability Club would have to produce a variety of AR Map activation images and post those onto the trashcans. That's a lot of administrative work and is prone to error. On top of that there's no guarantee that the trash cans or the images would stay in place. The campus recycling trash cans are outdoors (so we know the trash can GPS locations) and with the help of A-GPS technologies or dual-band GPS modules, the student's location is also relatively precise. I was not able to provide a technologically sound solution to gauge the initial orientation and drifting of the student's phone. In the 2020 fall, an end of a blog post and a teaser video hinted that Google was researching a solution I needed. How I built it At the Google IO 2022 the Geospatial API was announced. The API utilizes several technologies under the hood: ARCore’s AI algorithms Street View data Google Earth 3D models Google's Visual Positioning System (VPS) This finally made it possible to implement a concept of the desired AR Map mobile app ( source code , demo video ) which is now also featured on the top of the companion website. API Usage The website uses Google Maps JavaScript API. The mobile application uses both the Geospatial API (with Terrain Anchors) and Google Maps SDK for Android (the bottom portion of the app). The two together hopefully will help the student to better see possible locations. The initial mobile application concept was using the Geospatial API, however I started to use the Terrain Anchors in September. Recent changes (released 2022 November 12th) include the following API usages: Customized 2D Map markers to be green recycling arrow symbols Customized 3D Map markers to be downward pointing green arrows instead of traditional red map pins (lower vertex count hopefully will be beneficial for performance) Utilizing the Marker API so students can click on the 2D markers The Info Window shown by the marker click allows the student to see the 360 photo / video web page of the particular location with an additional click Challenges I ran into The elevation levels provided by the Geospatial API were off by a good 30 yards so the pins were hovering high up in the air. First I employed a hard-coded constant offset to compensate for the elevation problem. The locations of the trash cans were hard coded. Some trashcans would be already moved. To modify the locations shown by the concept app a new app release was needed. I only mapped the trashcans in the science area of the campus, I need to cover the whole campus. Accomplishments that I'm proud of I tested the feasability of the API with a concept app. The underlying building blocks (ARCore, Street View, Earth 3D Models, VPS) worked nicely. The Terrain Anchors allowed the treatment of the elevation offsetting issue in September. The latest November release greatly improved the user experience (customized markers, objects, seamless usage flow - no click needed on the 2D map to populate the anchors), the application - website synergy and the maintainability of the mobile app. What I learned Elevation can be problematic, but fortunately Terrain Anchors came to the rescue while I was trying various workarounds. I had to refactor the app to pull the locations from an online location (with a hard-coded fallback in case the user would be offline), so this way the trash can locations can be updated/corrected without a new app releases. This dynamic location download and update makes the app universal and usable for multiple guidance purposes and at multiple locations in the future (may require more marker image customization). I need to profile and tune the app to make sure there are no memory leaks or other performance problems to help with mid-range or low-range phones. A lot of students use Apple devices (iPhone, iPad), it'd be great to support those platforms. I either need to create a native iOS ARCore port of the app or see if Unity would cover all the needed features. What's next for Recycling Trashcan AR Map The project is open source. One of the next challenges will be to port the applications to native iOS or Unity to cover multi platform. Looking at the broader picture: this app can be a basis for not only recycling trashcan location AR Maps, but essentially any outdoor AR Map. I can guide the students also to various campus buildings using different markers. Even now the latest version of the app is able to distinguish multiple mapped areas and able to choose between them based on which one is closer to the student. Other campuses (see a participant interested in the comments) could already issue a Pull Request to me with new mapped areas serving other campuses. Companion 360 photos or videos are not required for an extension. Further plans: Make the app's offerings accessible from the official Fresno State Bulldog Genie assistant application. Extend the app's capability to guide students to campus building, the building could use traditional red map pins to distinguish them from the green arrow recycling trashcan locations. Create a gamification version where students get rewards based on how many recycling trashcan locations they visit. (Note: this would need user authentication, some form of back-end (such as Firebase), and significant privacy policy change.) Create a gamification version where we would count how many pieces of recycling trash is disposed into which trashcans. Students could earn rewards (such as Fresno State Sustainability water bottles). (Note: this would need user authentication, some form of back-end (such as Firebase), and significant privacy policy change.) <div