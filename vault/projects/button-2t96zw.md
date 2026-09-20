---
slug: "button-2t96zw"
url: "https://devpost.com/software/button-2t96zw"
title: "Button"
hackathon: "Amazon Sumerian AR/VR Challenge"
organization: "Amazon"
winner: true
words: 640
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/sensor_fusion"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Button

> A branded browser based VR escape room experience for the Oculus Rift and HTC Vive

[Devpost](https://devpost.com/software/button-2t96zw) · hackathon [[Amazon Sumerian AR-VR Challenge]]

## Facets

**mechanism** [[deterministic_policy]] [[sensor_fusion]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** amazon-sumerian, amazon-web-services, audacity, gimp-2.10.6, platinum-notes-4, wondershare-filmora

## How they structured the write-up

- welcome to button
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for button

## Body

Welcome to Button My Amazon Sumerian Hackathon entry for the 'Best VR App' category. Browser Requirements Firefox Version 60 and higher (built and tested in 64.0) Supported VR Headsets Oculus Rift / CV1 HTC Vive / Vive Pro To Start: Stand in the center of your VR space. Open the experience by clicking this link. Click the unmute icon in the lower right corner to enable audio. Click the VR icon in the lower right corner to start the experience. You will start in a very small closet-sized room. If you see a button, you should press a button. Controls: Teleport is disabled at the start - Listen for the audio cue that says, 'Teleport has been enabled' Oculus Touch Teleport - A/X button press HTC Vive / Vive Pro Teleport - Trackpad press There is no click/snap turning - turn your body. Buttons in the environment are activated by reaching out and touching them. A note on the 4th puzzle: Button was primarily developed and tested using an Oculus Rift and two front facing sensors about 5 feet apart in a small office. No rear / third sensor should be required to complete the 4th puzzle. It's all timing and technique. !!! Firefox Stability Note !!! If you run into glitching or freezing during gameplay... Close Firefox and wait about 30 seconds. Reopen Firefox. (one tab) Reload the experience. Inspiration "What could someone with little to no real-world coding or web development experience create and deploy using only the Sumerian Dashboard, the Sumerian tutorials, and assets included with Sumerian?" The Self-Imposed Rules: I could only use the Amazon Sumerian Dashboard to create my objects and entities in my VR environment. I could only use the Asset packs included with Amazon Sumerian. No custom / imported objects or models. I could not write any custom game or web code. Everything had to be done in the State Machine behavior system. Any code used had to come from examples in Amazon Sumerian tutorials, and the Amazon Sumerian Users Guide. What it does Button is a branded Web VR escape room puzzle experience for the Oculus Rift, HTC Vive, and Windows Mixed Reality headsets that provides four increasingly difficult puzzle challenges towards a final goal. How I built it Button was designed and built 100% in Amazon Sumerian. Audio and soundscapes were built using creative-commons licensed samples processed in Audacity, Platinum Notes 4, and Wondershare Filmora. A few custom textures for the end sequence were created using GIMP 2.10.6 Challenges I ran into I ended up sacrificing Google Daydream/Oculus Go VR headset support so I could use the 'VRController' component with the 'Daydream' controller ID to hack together a state-machine controlled rigid-body entity with a functional trigger collider. This was to work around a current bug with 'entity-with-rigid-body-collider' to 'entity-with-collider' trigger not functioning properly at the moment. Accomplishments that I'm proud of I am really happy with how the branded 'billboards' turned out at the end of the experience. I'm not a graphic designer by any means and this was my first attempt and making my own textures for use on entities. I'm also pleased with the sound effects and overall sound engineering. And I am very proud of my creative use of State Machine behavior logic I developed to implement puzzle functionality without having to write a single line of code. What I learned I discovered it is good practice to keep at least three project whiteboards (virtual) going: Overall start-to-finish storyboard. Entity and Logic System notes. Timeline with task breakdown. What's next for Button After the Amazon Sumerian Hackathon has concluded I plan to deploy Button as the official website for BrainFizz VR LLC - www.brainfizz.net - This will make BrainFizz VR LLC the first Virtual Reality company who's commercial website is only accessible via a 6DoF VR headset. <div