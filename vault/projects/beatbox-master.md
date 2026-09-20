---
slug: "beatbox-master"
url: "https://devpost.com/software/beatbox-master"
title: "Beatbox Master"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 1189
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Beatbox Master

> Alexa shows you her beatbox skills and teaches you about beatboxing!

[Devpost](https://devpost.com/software/beatbox-master) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**domain** [[education]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** amazon-dynamodb, apl, apla, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for beatbox master

## Body

Skill Icon Inspiration Beatbox Master was one of the first skills I built for Alexa, way back in 2017 (I think!). At the time the response from Alexa in the UK if you asked her to beatbox was 'I'm not really cut out for beatboxing' and I thought I should do something about that. The first version of the skill just used Alexa ssml content, leveraging the phoneme tag to replicate bass drum, hi-hat and snare, and produced something just about recognisable as beatboxing. I progammed in several beatbox patterns, and the skill would chain these up - some combinations worked better than others of course. In 2019 I updated the skill to use different Polly voices, but essentially it was the same mechanism - and more of a novelty than anything genuinely musical. It was all fun though, and played on the inherent ridiculous nature of an AI-type persona trying to be 'street'. My big frustration was that it wasn't possible to make Alexa keep time - I just had to rely on using TTS loops that by virtue of repetition kind of gave a sense of rhythym. APL made it possible to deliver multiple commands on a schedule... but would only work for users on screen devices, so would not help the majority of users. So Alexa was beatboxing... but not very well! In late 2019 I started a conversation with the School Of Beatbox (based in London) about using Beatbox Master, which had picked up a small following of users, to offer an aural history of beatboxing, alongside audio beatboxing lessons. So we could help people learn to beatbox... but we still couldn't teach Alexa to stay in time. Fast forward to summer 2020 when APL for Audio (APLA) was announced. Woohoo! Suddenly the skill I'd imagined all those years ago might actually be possible... What it does Using APLA means Alexa can now deliver time synchronised beatboxing - and so can her Polly friends. To add to the fun we've sampled up some real human beatboxers, and used the same mechanism to play audio files along to the same beatbox patterns. We've put together an audio history of beatboxing, to give users an understanding of beatbox culture, and this is offered up alongside new beats and voices as the skill is used. School Of Beatbox are providing a set of audio beatbox lessons, and they should be available shortly... I have a development version with the first set of lessons in, but we're not going to make this feature live until we've got the full set of 30 or so lessons available. How I built it The first thing was a to build an APLA sequencer - not the 'sequencer' APLA item, but the kind of sequencer you might use on a hardware/virtual drum machine or synth. Once that was done, I plugged in the Alexa phonemes and we were away... hey presto, Alexa could beatbox properly! (well, at least she stays in time...) Next up I needed to choose some friends for her to beatbox alongside - due to the challenges mentioned below, some of the voices I'd used in previous versions didn't really work any more so I went through all the available Polly voices and picked those that seemed best suited. Either because they sounded most authentic or had a certain style. Audio beatboxers was the next step - and naturally I was the guinea pig. A quick recording session later and I'm lisetening to my own voice beatboxing better than i ever could! School of Beatbox and a few friends contributed, and we've built four audio-file based beatboxers who each have their own style and 'specials' that they use alongside the standard bass drum, hi-hat and snare. The skill uses APL to deliver visuals alongside the audio - again there were more challenges, but we've got a set of images that display in time with the beats (more on that below!). The APLA is delivered via APL execute commands to achieve this. Finally I added a dynamic frame-based surround that mimics a PA system at a beatbox contest... the bigger the screen, the more speaker cones in the sound system! Challenges I ran into The beta nature of APL for Audio has provided a few challenges. Initially I found that my sequencer system needed a volume boost - the more tracks I used, the quieter the output. The volume boost needed wasn't consistent across ssml and audio-file output, or across audio-only and screen devices - so I had four different levels of volume boosting. Following one update to APLA I almost blew my speakers - the audio only devices were suddenly REALLY loud and I had to reach for the voume knob... a few weeks later the APLA delivered via APL commands followed suit. Another challenge was the visuals - my plan was to have the skill to show the beat patterns on screen, and highlight the active beat so users could follow the beat progression and practice along to this. However, the delay introduced whilst the APLA document is rendered means I was not able to get it in sync. I ended up using images that change in the appropriate beats-per-minute (BPM)... they don't necessarily start bang on the beat, but the effect is close enough. The delay in rendering the APLA was another challenge itself - I used crowd noises to cover this, on audio-only devices the APLA is rendered when the response begins, so the crowd noise is delivered via SSML output whilst this happens. On screen devices because the APLA document is executed as part of the APL it is not rendered until the command is executed. I had to add an APL media player item and play the crowd noise mp3 on that whilst the APLA renders. The render length for APLA also changes depending on the content - audio files are faster than SSML, so the beatboxer starts before the crowd stop cheering. Some Polly voices are slower to render than others, so I chose those with good render times (which meant no US beatboxers!) and Alexa herself is slowest of all... so there is a bit of a pause before she starts. Perhaps she is nervous :-) Accomplishments that I'm proud of I have found myself nodding my head along to some of the beats generated. Hopefully you'll find the same - and maybe will also find yourself quietly beatboxing whilst waiting for the kettle to boil! What I learned I learned a lot about the (current) restrictions of APL for Audio. It is still awesome compared to what was previously possible, but hopefully performance and effects will improve in the coming months. I also enjoyed making the submission video - it is done in the style of a YouTube Drum Machine/Synth review - hence the plants and desktop toys. If nobody else gets that reference, it at least made me smile :-) What's next for Beatbox Master Beatboxing lessons are coming soon! APL for Audio is the focus for this submission, but hopefully subscriptions for the lessons will make the effort worthwhile! <div