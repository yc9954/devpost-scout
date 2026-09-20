---
slug: "danger-zone-fm7xal"
url: "https://devpost.com/software/danger-zone-fm7xal"
title: "Danger Zone"
hackathon: "Snap AR Lensathon"
organization: "Snap Inc."
winner: true
words: 588
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Danger Zone

> Enter the cockpit of an F18 Super Hornet and try to race your way through a twisting valley under 45 seconds.

[Devpost](https://devpost.com/software/danger-zone-fm7xal) · hackathon [[Snap AR Lensathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** glsl, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for danger zone

## Body

helmet texturing Intro screen terrain rendering Inspiration This Lens was heavily inspired by the 2022 film "Top Gun: Maverick" (specifically, this scene ). I also happen to live in San Diego, where both films were made, and the real-life location of the original Navy TOPGUN Academy . So though I've never flown in a fighter jet, I frequently see (and hear!) them flying overhead, and can't help but wonder what it'd be like to be inside one... What it does "Danger Zone" places you--and optionally, a friend--in the cockpit of an F18 Super Hornet in a race against time to navigate your way through a twisting valley in under 45 seconds. The Lens opens with the ability to customize your pilots' call signs (200+ pre-selected or type your own) and helmet designs (12), as the Range Control guides you via radio. Tilt your head(s) to bank the jet, attempting to stay as close as possible to the path on your Heads Up Display , which will determine the jet's airspeed. How we built it This is by far one of the most detailed Lenses I've built in terms of bringing together 3D modeling / texturing, SFX, VFX, shader design, camera positioning, and more. There are little details that might get overlooked on first pass like a harness and oxygen hose that are rigged, environment reflections on the jet and helmet visor, and condensation vapor along the wings. It took about 6 weeks to create. The heart of this Lens is a shader that dynamically constructs a valley behind the jet, using ray marching to carve a valley out along the path of a curve. There are also shaders used for the HUD, clouds, vapor along the wings, and the dynamic call signs on the helmets. About half of the 9MB the Lens size is stored in Remote Assets to speed initial loading. The Range Control's voice was recorded by me using Voice.AI , and will even provide thematic hints like flipping the camera ("check your six") or finding a face("we have no visual"). I used Substance Painter to texture the helmet designs. Blender was utilized to adjust and rig models for the jet, helmet, oxygen hose, seatbelt. I gathered around 200 real call signs from this website . Challenges we ran into The multitude of shaders is quite compute-expensive, especially on older devices, so I dynamically adjust the Render Target resolution and level of detail based on the speed of the device. I also had to synchronize the scripted logic of the camera position and rotation with the shader, as well as synchronize the camera positions for the HUD and terrain shaders. It was quite challenging to create a smooth dynamic path that could easily be passed to a shader with a single vec4 array with a max size of 32. I ended up duplicating some code between shader and script to create a parametric Catmull-Rom Spline . Another tricky aspect was rasterizing the dynamic call sign text to a curved UV texture. This required carefully fitting and warping the UV coordinates of the text texture to align with the helmet designs. Accomplishments that we're proud of I like that the Lens feels intense, almost like a rollercoaster. What we learned I learned quite a bit about ray marching, shader camera positioning, SDFs , and became more skilled at some tools like Blender and Substance Painter What's next for Danger Zone I'd love to work with Paramount in some official capacity, but I'm not holding my breath! <div