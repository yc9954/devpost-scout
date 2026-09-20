---
slug: "tube-uni"
url: "https://devpost.com/software/tube-uni"
title: "Tube Uni"
hackathon: "Google AI Hackathon"
organization: "Google"
winner: true
words: 726
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Tube Uni

> Create a personal podcast on any topic, with a customized duration. Do something useful with your commute, dummy!

[Devpost](https://devpost.com/software/tube-uni) · hackathon [[Google AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]] [[transportation]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** gemini, google, google-moderator, google-storage, maps, next.js, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tube uni

## Body

do something useful with your daily commute! choose commute route or time, and any topic you can think of hold on for a minute or two and just start listening... Inspiration Commuting every day, both of us found ourselves staring at people, just waiting for the journey to end. This tends to make the commute feel longer than it actually is. In theory, you could read a book or watch a video, but concentrating in a moving vehicle is challenging, making audio a more practical option. However, finding suitable content for short rides is difficult. You might consider listening to an episode of your favorite podcast or an audiobook, but these rarely match the length of your commute, forcing you to stop midway through an episode. Many public transportation trips last only between 5 to 20 minutes, hardly justifying the effort to start something new. As a result, you end up either staring at people, which can feel awkward, or cycling through the same old music playlists. Surely, there must be a more enjoyable and productive way to pass the time. What it does We created a simple web app designed to make the most of short commutes. it was built around the London Tube, but it's applicable to any city and any transport method of a short commute. Just select your start and end stations, or simply input your travel time. Then, choose a general knowledge topic, either from your own ideas or from one of the suggested topics, and that's it! The app will quickly generate a custom podcast on your chosen topic, tailored to the length of your commute. How we built it We utilized various Google APIs to develop our application. Key among these was Gemini , which allowed us to create the context, structure, and text for our podcasts. Additionally, we integrated Google's Maps , Moderation , Storage and Text To Speech APIs. Our podcast content is grounded in information fetched from Wikipedia. The application itself is built with Next.js and deployed on Vercel for smooth accessibility. Challenges we ran into Generated content length - Gemini tends to keep answers short (500-800 words), even if we asked for longer text (1000 words+). This is a known issue with LLMs. We came up with the outline + paragraph generation strategy, to overcome it and reach podcasts lengths of up to 20 minutes. Long audio generation - The regular Google TTS API is limited to shorter lengths. We had to use the beta LongAudioSynthesize API to generate podcasts of up to 20 minutes. Accomplishments that we're proud of Amos and I have been eager to collaborate again for a while now. Despite facing challenging circumstances during this hackathon - with Amos traveling to London and myself, Liza, adjusting to the demands of new motherhood - we were determined to make it work. Remarkably, we not only overcame these obstacles but also integrated the unique backdrop of London into our project's concept seamlessly. What we learned Language models are hard to trust with regard to new information, news, or opinionated content. There will be solutions and new ways to mitigate that, but in the meantime, they're actually really good with evergreen content, which can also be easily grounded. This is why this concept makes really good use of what language models are already pretty good at today. It allows people to harness their power for something useful that can be used every day, and it actually feels like magic. Creating a crafted podcast on any topic with endless duration options can only be achieved at scale with LLMs, so it's really exciting to us. What's next for tube uni Currently, this is a side project for both of us. After some ideation, we decided to work on this idea specifically for this hackathon. We're proud of the MVP we've built and have both used it ourselves a few times. This is what made us believe this concept can actually become very popular. It can also be extended to other content materials, including children, students and professionals. If you can ground the content with enough source material, it can be a very useful way to learn things in a time with an ever-shortening attention span. Winning this hackathon can give us the attention and support to make this more than just a side project. <div