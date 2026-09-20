---
slug: "comfort-care"
url: "https://devpost.com/software/comfort-care"
title: "Comfort Care"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 438
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Comfort Care

> Comfort those with COVID-19

[Devpost](https://devpost.com/software/comfort-care) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[transcript_audio]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** amazon-web-services, css, django, ec2, figma, html, php, python, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for comfort care?

## Body

Enter Comfort Code Add Audio Add Music Rearrange Content Preview Memories and Messages Inspiration COVID-19 has awoken a harsh reality that no one should face. With the risk of infection being so high, hospitals are limiting visitation. Those stricken with COVID-19 potentially face dying alone with no one at the bedside and little to no comfort in their final moments. After seeing countless news articles and speaking with healthcare professionals we sought to change that. What it does Comfort Care allows family members to easily upload and share pictures, videos, audio recordings, and even their loved one’s favorite music. Once it’s uploaded their loved one or a health care provider can access a slideshow of the shared memories to leave by the patient’s bedside. How we built it We started by laying out what a user flow would look like. We wanted to make things as simple as possible for both the family of a patient and health care providers to use while also remaining HIPAA compliant and secure. We settled on a code-based system. The API generates a code that essentially becomes the identifier for that patient. Families can then login with that code and upload photos and videos from their device (stored securely in S3). If they wish to record a message for their loved one, they can do so directly in their browser and it will be uploaded and saved and played over the slideshow of images. Families can then choose songs from their Spotify that their loved one would enjoy. From the health care provider side, the code can be shared from the family and the presentation can begin on a device that sits in the room next to the patient. The player is built within a web browser so it can be universally accessible from any device (either hospital provided or family provided). Challenges we ran into We ran into a lot of challenges around how to make this the best possible experience for a family. Families put into this position are under a lot of stress and they feel helpless. We wanted to find a way to help families regain some of their control while also providing the best experience for a sick patient. Accomplishments that we’re proud of We made something that could help millions of people. What we learned That the magnitude of this problem is even larger than we initially thought. What's next for Comfort Care? We’d like to expand upon the app’s features and allow for audio/video calling and being able to connect patients with spiritual leaders to receive last rites and comfort in their final moments. <div