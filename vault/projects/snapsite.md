---
slug: "snapsite"
url: "https://devpost.com/software/snapsite"
title: "SnapSite"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 248
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "user/general_public"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SnapSite

> An AI design tool that builds a website with a photo! Snap a photo of text describing the website and it builds it. This overcomes funding, time and technical skills with just a snap of a photo.

[Devpost](https://devpost.com/software/snapsite) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**user** [[general_public]]
  <sub>weak: small_business</sub>
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, anysca, gpt, python

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for snapsite

## Body

Inspiration Building a website for someone who is non technical is tough and small businesses agree. Over 30% of SMBs in the US alone still don’t have a website and this stat is after the rise of quick step web design firms like Wix.com. SMBs highlight limited funding, time constraints and technical complexities as the barriers to entry in building a website. We wanted to change that! Enter SnapSite. What it does Snapsite creates a website through a snap of a photo! Capture any text and let our AI engine design a stunning website for you. Select from a wide selection of styles and modify your website to reflect your brand. How we built it We used AWS API to extract text from image (OCR). We then took the extracted text to feed it to our python code and the GPT 4 API to generate the website. Challenges we ran into GPT 4 is not a good UX designer It’s hard to deploy image to text model given multiple file types to consider Accomplishments that we’re proud of We have a working prototype and excited to spend more time on it to make it better What we learned how to deploy your own model! GPT 4 takes about 10 minutes to generate a website which is too long for a consumer What’s next for SnapSite This is just the beginning! So, Everything! :smile: to become the goto AI website generating tool for SMBs and individual users worldwide! <div