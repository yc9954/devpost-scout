---
slug: "mini-blackhole"
url: "https://devpost.com/software/mini-blackhole"
title: "MiniB - Miniature Blackhole"
hackathon: "Snap AR Lensathon"
organization: "Snap Inc."
winner: true
words: 498
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# MiniB - Miniature Blackhole

> Get rid of ANYTHING whenever, wherever, forever with your own mini blackhole!

[Devpost](https://devpost.com/software/mini-blackhole) · hackathon [[Snap AR Lensathon]]

## Facets

**substrate** [[video_visual]]

**stack** aftereffects, blender, javascript, lensstudio, photoshop, reaper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mini blackhole

## Body

Inspiration Over the past hundred years, scientific discoveries have taught us a lot about the flexibility of the universe and ourselves. The proof of black holes (1971) illustrated that space and time are actually part of the same force, which challenges some of the basic assumptions we have about reality. Despite our linear human experience, time doesn’t have to move in a straight line. It can be bent. (?!?!) And, the 1964 breakthrough in brain science showed us that, despite previous assumptions, the brain is a very changeable organ. Through repetition, we can literally remap the structure of our brains. These two discoveries (along with my experiments in AR) got me thinking about the true nature of reality and our ability to affect it. So, I decided to create an accessible, convenient, cathartic experience: a mini-ritual to help people get rid of whatever is weighing them down. What it does MiniB is a miniature black hole that banishes things you'd like to get rid of. After placing the black hole in your space, you type whatever you'd like to erase, and it gets sucked into the swirling vortex, never to be seen again. How we built it I created some galactic starscapes using Midjourney, then brought them into Photoshop for tweaking. Nebula noise and glowing star animations were created in After Effects and the 3D elements were created in Blender. I created a series of VFX elements and particle systems to act as the swirling light in Lens Studio. Then, I customized the keyboard template to trigger parameters within those VFX systems. That way, when someone submits a phase, the blackhole responds. Challenges we ran into Creating the intro’s motion graphics (for multiple phone layouts) was a little challenging. As a 2D animator, I'm used to creating pretty advanced animations in AfterEffects, but I haven't really been able to recreate the same quality in LS natively (yet.) So, I created a sequence in AE and brought it in as a PNG animation, but I ran into a few aliasing and compression issues. Native text is better in the long run anyway, so I tried to recreate the animations I had made in AE using screen transforms, but I ran into alignment inconsistencies (on different phones) when I animated positions. Ultimately, I simplified the animations to resolve this. Accomplishments that we're proud of I’m proud of the core idea, the simplicity of the interaction, and the visual effects. What we learned I learned a ton about VFX and creating motion graphics within Lens Studio. What's next for Mini Blackhole I’d like to keep fine-tuning the visual elements and, ultimately, would like to create a voiceML version, so that people can simply speak words rather than typing them. Once the tech is available, I’d also like to connect it to AI, so that when a person says a word, a visual representation (either an image or a 3D model) of that word appears and is sucked into the void. <div