---
slug: "heyoh-camera"
url: "https://devpost.com/software/heyoh-camera"
title: "Heyoh camera for Mac"
hackathon: "PyTorch Annual Hackathon 2021"
organization: "Facebook"
winner: true
words: 374
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Heyoh camera for Mac

> Bring real-life gestures to your video calls with heyoh virtual camera

[Devpost](https://devpost.com/software/heyoh-camera) · hackathon [[PyTorch Annual Hackathon 2021]]

## Facets

**mechanism** [[vision_ocr]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]]

**stack** coreml, gcp, python, pytorch, pytorchlightning, swift

## How they structured the write-up

- what it does
- inspiration
- how we built it
- challenges we ran into
- what's next for heyoh camera

## Body

GIF Github Project Page - Download & Install What it does Heyoh is a Mac virtual camera for Zoom and Meets. You don't have to look for buttons with awkward reactions anymore. Heyoh augments the live video by recognizing hand gestures and smiles and shows effects to highlight them to other video participants. Heyoh works with any video device, either physical or virtual, and since we do everything on your computer - your video calls and data always stay safe. Inspiration As engineers who work remotely, we spend a LOT OF TIME on video calls, talking to people all over the world. Adopting this lifestyle has become more common nowadays, but some pain points still have not been solved. We want to make this experience a little bit better. How we built it Heyoh camera Heyoh virtual camera is built as a CoreMediaIO DAL plugin for macOS. We use Swift, and custom-tailored PyTorch model converted to CoreML to utilize Metal and NeuralEngine (M1 Macbook) under the hood. We resize frames to 256x128 and inference them one by one with additional post-processing and smoothing (1€ Filter) of the predictions. This allows us to comfortably operate at 24+ FPS on a base model 2018 Macbook Air. Heyoh camera app repository Detection model Our goal is to build a lightweight though powerful enough model to provide the best user experience and not cause any disruptions to a regular video call experience. Our detection model is inspired by CenterNet with few modifications from segmentation_models_pytorch and is built on top of a pre-trained MobileNet V2 backbone from torchvision . Finally, our training pipeline is organized with PyTorch Lightning. Heyoh Object Detection / Tracking pipeline Challenges we ran into Video calls are already consuming a lot of processing power on the device. Heyoh virtual camera has to work under very strict conditions, so it feels seamless to the user and helps communication. We spent a lot of effort optimizing and tailoring model architecture to fit those requirements. Worth mentioning that DAL plugins are not a very well-documented part of the Apple ecosystem. It took us some trials and errors to make it work well. What's next for heyoh camera Adding more gestures Adding virtual backgrounds Making better AR effects <div