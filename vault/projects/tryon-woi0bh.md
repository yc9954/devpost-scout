---
slug: "tryon-woi0bh"
url: "https://devpost.com/software/tryon-woi0bh"
title: "TRYON"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 404
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/video_visual"
---

# TRYON

> Try before you buy – virtually using GenAI. Our app lets users try on clothes using just their image, all processed locally for complete privacy and instant results.

[Devpost](https://devpost.com/software/tryon-woi0bh) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[health_clinical]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[video_visual]]

**stack** ai, hp, python, studio, transformers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tryon

## Body

Inspiration Shopping online often lacks the personal touch of trying on clothes. Many users hesitate to purchase because they’re unsure how the outfit will look on them. At the same time, concerns over data privacy make uploading personal images to the cloud a non-starter. We wanted to solve this by offering a fast, private, and fun virtual try-on experience—right from the user’s device. What it does TryOn allows users to virtually try on clothes using their own photo, without uploading any personal data to external servers. The application uses a body segmentation model to isolate the user’s silhouette and a powerful inpainting diffusion model to realistically overlay the selected clothing item. All processing happens locally on the user's device, ensuring full privacy. How we built it We combined: A body segmentation model to accurately detect and segment the user's figure GenAI - An inpainting diffusion based model generative AI model to generate a realistic try-on image by seamlessly blending the garment with the user's photo A locally hosted inference pipeline, optimized to run on standard consumer devices without requiring internet or cloud support A simple, intuitive user interface that lets users upload their image, select a clothing item, and preview the try-on instantly Challenges we ran into Deployment hurdles — setting up the application for local use involved troubleshooting vague error messages and failure logs. Lack of clear diagnostics made it difficult to pinpoint issues during runtime, which significantly slowed down the initial deployment process. Managing memory and compute constraints for real-time local inference, compared to just hosting FASTAPI. When not hosting API endpoint I can offload and spin up models based on requirements but here all endpoints that is needed to run the solution should be up and running, which does not help in GPU constraint situations. Accomplishments that we're proud of Successfully deploying a fully offline virtual try-on system Maintaining a high standard of visual realism while keeping the app lightweight Enabling complete user privacy—images never leave the device Making it easy and intuitive for anyone to try on clothes virtually -Registered the model on AI Studio What we learned Gained hands-on experience in registering and managing models in AI Studio, which helped streamline model versioning and deployment Learned to leverage HP AI Studio to assist with deploying the virtual try-on pipeline What's next for TRYON Include a text to image search that allows users to search through different clothing items <div