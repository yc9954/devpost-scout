---
slug: "billboards"
url: "https://devpost.com/software/billboards"
title: "Billboards"
hackathon: "Google Photorealistic 3D Maps Challenge"
organization: "Google"
winner: true
words: 528
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Billboards

> Introducing Billboards that lets companies place 3D billboards on Google 3D Maps. Boost your brand's virtual presence and engage customers in a novel way with immersive, location-based advertising.

[Devpost](https://devpost.com/software/billboards) · hackathon [[Google Photorealistic 3D Maps Challenge]]

## Facets

**mechanism** [[cross_origin_web]]
**user** [[general_public]]
**substrate** [[geospatial]] [[video_visual]]

**stack** blender, gcp, google-maps, google-maps-3d, nextjs, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for billboards

## Body

Inspiration The world of Blade Runner 2049 was my inspiration. Wanted to build a 3d world with large and immersive ads. What it does Billboard lets companies add billboards, hot air balloons, blimps etc., with their ads, campaigns etc. Companies can upload their campaign images and place the billboards in strategic locations. They can highlight their location by adding eye catching ads. In admin page companies can create their campaigns in billboards, blimps etc. It has a split panel with left side being used by the company to place the billboards, adjust direction, change the images, and publish them. In the right side they can see the realtime preview of the billboards they are adding. 3 types of billboards are available, and these can be placed in the ground or on top of buildings. Balloons that floats high above the ground, keeps rotating and catches the attention of users. Blimp that flies continuously above an area showing larger ads. In the main page the users/consumers can navigate through the map looking at various ads and campaigns. How we built it It is a Next.js hosted Google Cloud Run. It has two areas, the main page and the admin page. In the admin page the left side is a basic flat map where the user places the billboard. A polygon is drawn to show location and area of the billboard. At the same time the 3d billboard will be displayed in the 3d map in right side. The billboards are placed with altitude mode set as "RELATIVE_TO_MESH" so that it can be placed in ground or over a building. I created all the 3d models from scratch in blender. One major issue I faced is I have to show the image the user uploads in the 3d image (my original idea was to display videos but currently it is not possible). Now there is no option for this in the 3d maps neither there was a WebGL support. So I created there models in a way that the image texture can be replaced via a python script. So when a company upload a image a copy of the original .glb file taken and the image texture is replaced via python script and new .glb file is created. The glb files are stored in Google Cloud Storage. The details of the billboard type, position, orientation etc are stored in Firestore. Created some crude animations like the balloon rotation and blimp flying in a circle by simply updating the position and orientation in short intervals. Challenges we ran into As mentioned before generating the dynamic .glb was a bit challenging which I eventually succeded. Building the 3d models where a bit challenging as well especially the lighting as default materials where shown darker, sometime simply black at an angle. Had to find some good emission values and some node editing to achieve a brighter model. Accomplishments that we're proud of I was able to complete this at a very short period of time as I just took up the project over this weekend. What's next for Billboards To look at feasibility of building it as complete project and publishing online. <div