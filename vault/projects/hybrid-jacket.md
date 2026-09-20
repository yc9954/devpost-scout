---
slug: "hybrid-jacket"
url: "https://devpost.com/software/hybrid-jacket"
title: "Hybrid Jacket"
hackathon: "Snap AR Lensathon 2022"
organization: "Snap Inc."
winner: true
words: 868
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Hybrid Jacket

> A next level haute couture virtual fashion experience. By combining the AR try on feature with an engaging World AR experience, users are fully immersed in the world of virtual fashion design.

[Devpost](https://devpost.com/software/hybrid-jacket) · hackathon [[Snap AR Lensathon 2022]]

## Facets

**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** blender, codenodeforshaders, javascript, marvelousdesigner, photoshop, substancepainter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hybrid jacket

## Body

Hybrid Jacket - Overview Hybrid Jacket - Nude Hybrid Jacket - Rainbow Hybrid Jacket - Plastic Inspiration The rooms and environment of the experience and more specifically the jacket design was inspired by reusable physical materials and recyclable plastic items. We tried to translate these items into the virtual world by adding different kind of fabrics with organic, non symmetrical shapes and adding semi transparant and reflective shading. The idea is to show how you can create haute couture (virtual) fashion from basically anything by using your own creativity and imagination based on real world items. Virtual fashion is a sustainable and playful way of discovering design opportunities and realising a way of sending out a message into the world based on your own creativity and imagination. What it does We wanted to go beyond a fashion try on by creating a more immersive and dynamic experience. By adding both a world and selfie feature, users are fully immersed into the mind of the designer. On opening the Lens, users see three portals. They can switch through the portals by a 2D UI. Once a portal is chosen, users are invited to step in and explore the room where the jacket is showcased. When users are inside the portal, a call to action is shown to switch cam to try on the jacket from that specific room. While trying on the jacket they can switch between the three versions by using the 2D icon UI. They can also choose to switch back to world view and explore the other portals. How we built it Jacket design Modeling the jacket in Marvelous Designer Low poly version in Blender Backing normal maps from high poly to low poly in blender Making 3 different style and texture in blender+photoshop Rooms Designing the rooms in blender. Choosing materials and texture that fit the styles of the jackets; Adding lights to create the perfect ambience and mood, different for each room. Joining all the materials in one single texture for each room. Baking lights and shadows Designing the portals Adding the skybox for the "sand room" Adapting the occluder box for each room and the skybox Adding dynamics details inside Lens Render each room to a separate Render Target Project each Render Target on the portal planes so they don't visually intersect even though in real life they shouldn't be able to Code to check the user entering a room and displaying the room behind the portals Challenges we ran into From a creative perspective, the biggest challenge for this experience was to realise a smooth user experience while switching between rear and front cam. As this can always cause some drop off, we really needed to maintain the users attention. We did a lot of testing with random users to see if we could capture and maintain their attention and if the UI of switching between the camera's was clear. We wanted users to navigate back to the portals to try on a different version which seemed too much of an effort for some users. We think we solved this by giving users the option to keep switching versions on both front and rear cam. This gives them more freedom in choosing wether or not to go back to the rear cam in order to try on a different version of the jacket. From a technical perspective it was a challenge to come up with a solution for the portal rooms overlapping but only the room you are in being visible. Furthermore for the portals it was quite some coding to create the tech that displays the room from the portal door without having anything behind the door. Regarding the 3D, obviously the poly count was challenge, backing the light in the rooms and creating the plastic and transparent material. Accomplishments that we're proud of We are super proud on the experience we created as we wanted to go beyond a "standard" virtual try on. We really think we managed to have users step in to the mind of the designers and discover which environment they like the most in order to choose a try on and play with the different designs in a very dynamic and interactive way. We are also proud on being able to realise a smooth user experience with a realistic looking environment and garments within the available file size and maintaining our projected visual quality. What we learned Most of all, we once again learned a proper Lens needs a lot of work, time, dedication, imagination and creativity. We first saw this as a side project but eventually went all in and ended being fully invested in the project. Only then can it turn out great and have an actual impact on both the users, their community and everyone experiencing it, either by themselves or seeing it as a shared content. What's next for Hybrid Jacket Showing it to the world and giving everybody the opportunity to express themselves with the version fitting their identity the best and hopefully realising some awareness about the idea behind the Lens. Furthermore, if well received, we would love to create a full collection with multiple models. looks and environments.8U <div