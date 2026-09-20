---
slug: "berlin-s-potsdamer-platz-between-utopia-and-dystopia"
url: "https://devpost.com/software/berlin-s-potsdamer-platz-between-utopia-and-dystopia"
title: "Berlin’s Potsdamer Platz between utopia and dystopia."
hackathon: "ARCore Geospatial API Challenge"
organization: "Google"
winner: true
words: 882
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Berlin’s Potsdamer Platz between utopia and dystopia.

> Explore one of the most iconic and history-rich squares of Berlin, discover some of the innovation it's been driving, and risk a peek into the future. Do you want to live in a utopia or dystopia?

[Devpost](https://devpost.com/software/berlin-s-potsdamer-platz-between-utopia-and-dystopia) · hackathon [[ARCore Geospatial API Challenge]]

## Facets

  <sub>weak: climate_energy, transportation</sub>
**substrate** [[geospatial]]
  <sub>weak: video_visual</sub>

**stack** arkit, blender, realitycomposer, realitykit, scavengar, swift, xcode

## Body

Birds eye perspective of the experiences geo coordinates Historical photos anchored to a skyscraper Dystopia scene Dystopia scene Utopia scene Quiz Checkpoint Building Geometry debug mode; meshes with a simple shader that colorises each fragment with the associated normal Exported block of the building geometry within Apples Reality Composer Utopia Scene – Windmill and Plants Berlin’s Potsdamer Platz between utopia and dystopia Potsdamer Platz has been one of Berlin's most important squares for over 150 years. It is rich in history and has been the nucleus for some of the city's most significant innovations that still shape the urban life of Germany's capital today. If there would be only two words to describe the iconic square, they would be change and innovation. Looking into the years ahead, it is a necessity to hold ourselves responsible to these important words and their meaning. Thus, we want to expand an AR experience that unlocks stories from the past and provides an outlook on what our world might look like in the years to come. To create an impactful immersive story, we combined a variety of digital and interactive elements. After scanning a QR code, users are greeted and guided through the first part of the experience by a narrator. It’s important to underline the AR experience works without downloading an app which is achieved by leveraging the AppClip framework. To increase engagement, we’ve been implementing tasks and trivia elements while guiding users alongside relevant physical structures, like Europe's first traffic light. The audio-narrated story of local discovery ends with a choice users have to make. They are prompted with the decision to enter one of two scenarios – a utopia or a dystopia. Whereas until this point, the theme of the AR experience is a scavenger hunt that leverages geospatial transforms of the Geospatial API, the second part is less guided and focuses on advanced location-based features like building geometry and occlusion. These features allow us to alter the physical reality and risk an outlook on how the future might look like. In addition to placing and attaching interactive 3D scenes on the geometry around the user, we’ve been adding post-processing effects, custom shaders, and spatial audio to amplify immersion when it’s most important in the AR story – increasing the emotional involvement when users are faced with the decision how we want to live in the years ahead. The main idea behind Potsdamer Platz AR is to combine new ways of non-linear storytelling with local discovery and emotional messaging about climate change with a clear call-to-action. It addresses a broad audience and does not require any technical expertise to use, making it accessible to all ages. Aiming for a smooth UX, we created a coaching overlay that intuitively guides through the localization process while navigational elements have been implemented to navigate users through the experience. Challenges we’ve been facing: Facade Geometry is available but by default cannot be queried for a specific location or exported thus, we built a little tool to export a snapshot of geometry at the currents user location as a USDZ. We processed facades (computing the normals) to use within Apple’s RealityComposer to decorate the scene with custom 3D models. This workflow came with new challenges as RealityComposer would clip the drawing distance for objects with this huge physical size (couple hundred meters). We fixed it by scaling down the model to 10%, creating our scene and everything within it. Back in Scavengar we scaled it up but also adjust the rotation to fit RealityKits and ARKits coordinate system. Building geometry blocks within the geospatial API currently don’t have a stable identifier (UUID) – it changes each time you use the API, so we needed to get creative to use our exported geometry and anchor it back onto the facade. We came up with the following workaround: When exporting the geometry, we also store the current coordinate for the selected facade block. Next we loop through all the facades within a frame and compare their coordinates distance to the one from our exported block. For the smallest distance we can safely assume it belongs to our target facade and associate it with our custom anchor, which get’s updated on every frame with the facade transform. We’re proud of having created an AR experience that combines native app performance and high quality visuals, while keeping the accessibility of a WebAR experience. The geospatial API allowed us to not only enable pinpoint precision and automatic localization, but helped to bring the level of immersion to another level with building geometry. The latter one was specifically challenging to get right, as we built our own tool to export the geometry up front, to have full control over the whole scene even when concepting and composing the 3D assets up front. Having all building blocks in place, the concept is built for high scalability, enabling us to spread the existing experience to multiple locations around the globe with only slight adjustments to make. We’d love to extend the project and focus a lot more on content creation, striving for higher visual quality by building custom 3D assets. We’d like to explore these opportunities with city councils, tourism boards and cultural institutions to make cities come to life, creating interactive stories for good. <div