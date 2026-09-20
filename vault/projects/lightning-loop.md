---
slug: "lightning-loop"
url: "https://devpost.com/software/lightning-loop"
title: "Lightning Loops"
hackathon: "BitRate: Machine Learning & Music Series"
winner: true
words: 344
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
---

# Lightning Loops

> A networked musical instrument you play by drawing in 3D space, trained on 164 MIDI recordings of me playing piano.

[Devpost](https://devpost.com/software/lightning-loop) · hackathon [[BitRate- Machine Learning - Music Series]]

## Facets

  <sub>weak: provenance_signing</sub>
  <sub>weak: education</sub>
  <sub>weak: video_visual</sub>

**stack** javascript, linode, magenta, magenta.js, magentajs, node.js, python, three.js

## Body

I have some experience using applied ML with 2D graphics, but this was my first time using non-image-based training data. As source material, I used 164 MIDI recordings of myself playing piano in high school and undergrad. I first attempted to split out the melody tracks with midi-miner, but wasn't able to get usable output. Fortunately, enough of the samples were sufficiently cleaned up (or else my playing was evidently close enough to the specified time signature to count as quantization) that preprocessing wasn't necessary. With my data ready, I picked two of Magenta's examples to concentrate on: AI-Duet and Piano Genie. For AI-Duet, I wasn't able to put together a pipeline that produced a working final result, but I was able to successfully train and deploy models for Piano Genie. Piano Genie creates complex note output from simple input, by default 88 keys out from eight in; this was appealing to me because, as a performer, I'd retain control over timing, while the model would get to decide the pitch. The Piano Genie sample training script was my first time working with a script that ran continously until stopped, rather than using a fixed number of epochs. To resolve this, I ended up training two models, one on CPU and one on GPU, for eight hours each, then testing both. The GPU-trained version effectively having a much longer training time, it reproduced a lot more material from the sample set, a result that I liked better for this project. Almost finished, I ran into a snag: I also needed to create a separate Python environment with different dependencies to convert the Piano Genie checkpoint into the final output format. With no documentation for this step that I could find, I discovered the requirements by trial and error. With the model working, I finally wired it into a multiplayer 3D drawing application I built in three.js, using the 2D angle between start and end point to select my eight keys. The result is a fascinating "third hand" for live piano playing while drawing. <div