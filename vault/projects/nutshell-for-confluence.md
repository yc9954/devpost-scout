---
slug: "nutshell-for-confluence"
url: "https://devpost.com/software/nutshell-for-confluence"
title: "Nutshell for Confluence"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 438
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
---

# Nutshell for Confluence

> Unlock the knowledge from your video recordings and automatically create documentation, training material, and meeting notes.

[Devpost](https://devpost.com/software/nutshell-for-confluence) · hackathon [[Codegeist Unleashed]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[document_pdf]] [[transcript_audio]]

**stack** confluence, forge, google-cloud, javascript, openai, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nutshell for confluence

## Body

Inspiration Often I found myself wasting time watching long videos at work. Catching up on missed calls, or searching through training videos for bits of information. The information I needed was buried between minutes 12:07 and 14:03. Good luck using the confluence search for it! What it does We unlock the knowledge of the videos in confluence pages, by transcribing and organizing what is being sad. How we built it The app was constructed using Atlassian Forge, with the technology stack encompassing JavaScript (JS), Python, Google Cloud Platform, and OpenAI. It harnessed the capabilities of Atlassian Forge, enabling frontend components to invoke remote endpoints and interact with the Confluence API. The app's workflow involved the retrieval and processing of videos attached to Confluence pages. After extracting audio and generating summaries, the processed videos were deleted, and the Confluence page was updated with the summary, timestamps, and topic details. Challenges we ran into The foremost obstacle was the handling of large video files, which initially proved too resource-intensive for the Atlassian Forge environment, necessitating the use of remote capabilities on an external server. Integrating external APIs, including those from Google Cloud Platform and OpenAI, presented another hurdle due to the complexities associated with differing data formats, authentication, and API endpoints. Additionally, the team had to navigate a learning curve to grasp the intricacies of Atlassian Forge, understanding both its limitations and the range of possibilities it offered. Accomplishments that we're proud of We are proud of the final product, "Nutshell for Confluence." It's a game-changer for Confluence users, as it allows them to access video content efficiently, read transcriptions, and find critical information quickly without watching lengthy videos. The app is a productivity booster and a time-saver. What we learned We became familiar with the limitations and capabilities of Atlassian Forge, enabling us to make informed decisions about its usage. Moreover, we discovered the flexibility of Forge functions, which can be employed for rendering on both the frontend and backend, offering diverse implementation options. Interacting with external APIs, such as those from Google Cloud Platform and OpenAI, became a part of our expertise. We also honed our skills in optimizing video processing, including audio extraction and summary generation What's next for Nutshell for Confluence We hope to release our app in the Atlassian Marketplace and use our technology to do other cool things! We want to offer different text outputs for users to choose from, for example, the full transcription in different languages, different summary lengths, and different text formats. We also hope to extend the functionality beyond video and include PDFs, Confluence Pages, and other document types. <div