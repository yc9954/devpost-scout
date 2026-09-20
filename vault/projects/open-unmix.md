---
slug: "open-unmix"
url: "https://devpost.com/software/open-unmix"
title: "Open-Unmix"
hackathon: "Global PyTorch Summer Hackathon"
organization: "Facebook"
winner: true
words: 813
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/transcript_audio"
---

# Open-Unmix

> End-to-end music demixing with PyTorch

[Devpost](https://devpost.com/software/open-unmix) · hackathon [[Global PyTorch Summer Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[scientific_research]] [[security_privacy]]
**user** [[researcher]]
**substrate** [[transcript_audio]]

**stack** pytorch, torchaudio, torchhub

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for open-unmix

## Body

end-to-end source separation with Pytorch The kind of results we obtain when demixing music Inspiration In our team at Inria, we are working on music unmixing . This means getting back the individual instruments from any stereo recording, like the vocals, the drums, the bass, etc. Music unmixing has many applications, especially for the music lovers that want to make covers of their favorite tracks! We've been working on it for quite a while now, and thanks to deep learning, great progress has been made in music unmixing and Pytorch is the framework we use daily for our research because it allows great flexibility, is powerful and is just a pleasure to work with. Recently, we published an MIT-license project called open-unmix that is fully written in torch and that brings state-of-the-art separation to our fellow researchers as well as to the (geeky for now) users. We are very happy with this recent release, but it had several drawbacks , that can be summarized as some signal processing parts were written in numpy , because torch does not (yet?) support complex algebra natively. However, we had the pleasure to see that the pytorch dev team takes audio very seriously and the whole torchaudio library now brings audio to pytorch users. Also, the amazing torch.hub makes it possible to load our models in one line of code. However, the process was still cumbersome, because not the whole pipeline was in pytorch, due to the numpy parts. What it does For the hackathon, we implemented in Pytorch the whole signal processing pipeline doing the delicate filtering of audio to get the actual separated waveforms. To do this, we exploited recently proposed features from torchaudio to go back to the separated signals directly and implemented the rest ourselves. As a result, we are happy to release a new torch.Module called the Separator , that: encapsulates everything needed to separate audio signals is differentiable, so that we can do training directly in the time domain! We believe this opens up very nice research directions. How we built it Open-unmix has been a very hard work to release, notably because we had to do some research on how to fight overfit and tune our models. Still, we were lucky we chose Pytorch for this because it significantly accelerated the whole process. Now, the torchfilters branch of Open-unmix , which is the object of this submission to the hackathon, exploits many remarkable features of Pytorch: torchaudio very effective dataloaders, inverse STFT and resampler. The flawless implementations of the classical BLSTM recurrent layers. Many off-the-shelf optimization algorithms and training tricks, as well as the straightforward way you implement training loops which you can debug. torch.hub is an extraordinary attempt at promoting reproducible research. Since it was pretty easy to setup, we added a hub support to our new Separator module. Challenges we ran into The hardest part of going end-to-end in Pytorch was to implement the complicated stereo Wiener filtering and Expectation-Maximization algorithms that are necessary to obtain state-of-the-art performance. While we made them all available for the users in a dedicated numpy toolbox , implementing the most delicate parts in torch was not easy. This is mainly because these all operations are performed on complex numbers, and torch does not yet support complex algebra natively. However, thanks to the way you build a Pytorch application, we could debug every part of it and optimize the code to finally even get smaller memory usage and faster computations than with the numpy version. Accomplishments that we're proud of We believe that the coolest part of our submission is that everything about the system is full-torch, which means we can benefit for the great production features that the Pytorch dev team has already created (notably torch.hub ) but also any other one that may come in the future. What we learned Pytorch is a community-based thing, and we are glad that the audio people got into it by creating the features of torchaudio . The take-home message for us is that taking action in this and contributing through our somehow narrow expertise on audio processing can have an impact in the larger plan of a big-sized project like Pytorch, and we are happy about it. What's next for Open-Unmix We hope that the end-to-end separation system we come up with through this submission will: raise some interest for this fascinating topic of source separation and what we believe are its extraordinary applications in terms of artistic creativity. raise new interesting research questions. In particular, having a module that's an end-to-end differentiable separator makes it possible to directly train models in the time domain. Then, if the objective is to plug some other process down the line of the Separator (such as lyrics recognition or polyphonic transcription networks), an end-to-end training may be imagined where separation is also trained on the way. <div