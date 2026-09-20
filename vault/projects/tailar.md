---
slug: "tailar"
url: "https://devpost.com/software/tailar"
title: "TailAR"
hackathon: "Snap AR Lensathon"
organization: "Snap Inc."
winner: true
words: 509
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "substrate/geospatial"
---

# TailAR

> Awaken the inner Tailor in you with TailAR SnapAR Lens

[Devpost](https://devpost.com/software/tailar) · hackathon [[Snap AR Lensathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**substrate** [[geospatial]]

**stack** bodytracker, lensstudio, meshbuilder, photoshop, programming

## How they structured the write-up

- inspiration 🤔
- what it does 🤷‍♂️
- how i built it ⚒️
- challenges i ran into 😶‍🌫️
- accomplishments that i'm proud of 🦚
- what i learned 🧑‍🏫
- what's next for tailar 🔮

## Body

Builder Logo Inspiration 🤔 Haha this is a funny story. So I was always amazed by all the custom clothing lenses and the type of dresses and fashion accessories, creators modelled were very inspiring especially DressX items ! They are the best ! Now I do know some bit of modelling but by default configuration xD and my interests, I'm more into programming. So I thought why not program a lens which lets users design their own fashion apparels and then try it on in realtime on the spot ? And thus TailAR was born ✨ What it does 🤷‍♂️ TailAR is an user-friendly lens and rather a complex one behind the scenes which lets users tailor their own body tracked items and try it on in real-time How I built it ⚒️ I had recently saw Max van Leeuwen's Mesh builder work on Twitter and thought I could use it here. So looked out for some resources over the Snap community and documentation and then built out a custom version of Mesh builder which would let me sew my custom clothing in world space. Then I took that mesh which was generated and mapped it on to the 3D body tracker. Challenges I ran into 😶‍🌫️ Main challenge was to get the Mesh builder work properly and the mapping part on the body tracker. Initially when I started, I was not able to figure out how to generate discontinued meshes and then combine it to form the final apparel mesh. But after 2-3 sleepless nights of hit and trails and studying the concept more in depth was able to crack it. Secondly without any reference sewing the experience in world space was a bit confusing, so I added in the body mesh object as a reference to design the clothing around it. Later in the final stages I replaced that with a tailor mannequin for consistency with the theme of the lens I was building around. Mapping part was rather twisted as well, getting the proper placement with occlusion was a bit of a brainwork I had to put into Accomplishments that I'm proud of 🦚 The moment I designed one Tshirt in VR, I thought what if we could design and try-on these apparels and accessories on the Fly without having any intermediate platform in between? The main accomplishment for me is to finally put that Idea to reality using SnapAR. It's indeed true. Dream it, Build it 💛 Building for masses; Even though this lens uses a complex background, it doesn't require any special hardware like LidAR or heavy processor. It will work on each and every device which supports Snapchat/Camerakit What I learned 🧑‍🏫 Advanced programming through Meshbuilder Dynamic Mesh generation 3D Mapping of Generated Clothing to Body Tracker What's next for TailAR 🔮 Extensive toolset and customization options Local Export & Import abilities through JSON encoding using Persistence Storing Mesh data and textures dynamically to the Lens Cloud Storage Connected experience where two or more users can collaborate to tailor the items together <div