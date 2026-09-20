---
slug: "3dreal"
url: "https://devpost.com/software/3dreal"
title: "3dReal"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 825
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# 3dReal

> Your memories, but realer

[Devpost](https://devpost.com/software/3dreal) · hackathon [[TreeHacks 2024]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** ai, figma, firebase, nerf, nvidia, xcode

## How they structured the write-up

- inspiration
- what it does
- how it works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for 3dreal

## Body

GIF A rendered selfie GIF BeReal Integration concept - using bluetooth to locate nearby friends to then give a 3dReal option our logo Inspiration Metaverse, vision pro, spatial video. It’s no doubt that 3D content is the future. But how can I enjoy or make 3d content without spending over 3K? Or strapping massive goggles to my head? Let's be real, wearing a 3d vision pro while recording your child's birthday party is pretty dystopian. And spatial video only gets you so far in terms of being able to interact, it's more like a 2.5D video with only a little bit of depth. How can we relive memories in 3d without having to buy new hardware? Without the friction? Meet 3dReal, where your best memories got realer. It's a new feature we imagine being integrated in BeReal, the hottest new social media app that prompts users to take an unfiltered snapshot of their day through a random notification. When that notification goes off, you and your friends capture a quick snap of where you are! The difference with our feature is based on this idea where if you have multiple images of the same area ie. you and your friends are taking BeReals at the same time, we can use AI to generate a 3d scene. So if the app detects that you are in close proximity to your friends through bluetooth, then you’ll be given the option to create a 3dReal. What it does With just a few images, the AI powered Neural Radiance Fields (NeRF) technology produces an AI reconstruction of your scene, letting you keep your memories in 3d. NeRF is great in that it only needs a few input images from multiple angles, taken at nearly the same time, all which is the core mechanism behind BeReal anyways, making it a perfect application of NeRF. So what can you do with a 3dReal? View in VR, and be able to interact with the 3d mesh of your memory. You can orbit, pan, and modify how you see this moment captures in the 3dReal Since the 3d mesh allows you to effectively view it however you like, you can do really cool video effects like flying through people or orbiting people without an elaborate robot rig. TURN YOUR MEMORIES INTO THE PHYSICAL WORLD - one great application is connecting people through food. When looking through our own BeReals, we found that a majority of group BeReals were when getting food. With 3dReal, you can savor the moment by reconstructing your friends + food, AND you can 3D print the mesh, getting a snippet of that moment forever. How it works Each of the phones using the app has a countdown then takes a short 2-second "video" (think of this as a live photo) which is sent to our Google Firebase database. We group the videos in Firebase by time captured, clustering them into a single shared "camera event" as a directory with all phone footage captured at that moment. While one camera would not be enough in most cases, by using the network of phones to take the picture simultaneously we have enough data to substantially recreate the scene in 3D. Our local machine polls Firebase for new data. We retrieve it, extract a variety of frames and camera angles from all the devices that just took their picture together, use COLMAP to reconstruct the orientations and positions of the cameras for all frames taken, and then render the scene as a NeRF via NVIDIA's instant-ngp repo. From there, we can export, modify, and view our render for applications such as VR viewing, interactive camera angles for creating videos, and 3D printing. Challenges we ran into We lost our iOS developer team member right before the hackathon (he's still goated just unfortunate with school work) and our team was definitely not as strong as him in that area. Some compromises on functionality were made for the MVP, and thus we focused core features like getting images from multiple phones to export the cool 3dReal. There were some challenges with splicing the videos for processing into the NeRF model as well. Accomplishments that we're proud of Working final product and getting it done in time - very little sleep this weekend! What we learned A LOT of things out of all our comfort zones - Sunny doing iOS development and Phoebe doing not hardware was very left field, so lots of learning was done this weekend. Alex learned lots about NeRF models. What's next for 3dReal We would love to refine the user experience and also improve our implementation of NeRF - instead of generating a static mesh, our team thinks with a bit more time we could generate a mesh video which means people could literally relive their memories - be able to pan, zoom, and orbit around in them similar to how one views the mesh. BeReal pls hire 👉👈 <div