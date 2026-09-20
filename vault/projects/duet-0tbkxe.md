---
slug: "duet-0tbkxe"
url: "https://devpost.com/software/duet-0tbkxe"
title: "Duet: Brainwaves -> Live Music"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 824
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/immigration_refugee"
  - "domain/mental_health"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Duet: Brainwaves -> Live Music

> Creativity is inherent, but expressing it is hard. Duet reads live brainwaves via EEG and uses AI to generate evolving soundscapes that reflect your emotions, giving voice to your inner symphony.

[Devpost](https://devpost.com/software/duet-0tbkxe) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[immigration_refugee]] [[mental_health]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[structured_db]]

**stack** emotiv, gemini, next.js, python, ruby, singlestore, sonicpi

## How they structured the write-up

- about the project

## Body

Duet's music generation revolutionizes how we approach music therapy. We capture real-time brainwave data using Emotiv EEG technology, translating it into dynamic, personalized soundscapes live. Our platform, backed by machine learning, classifies emotional states and generates adaptive music that evolves with your mind. We are all intrinsically creative, but some—whether language or developmental barriers—struggle to convey it. We’re not just creating music; we’re using the intersection of art, neuroscience, and technology to let your inner mind shine. About the project Inspiration Duet revolutionizes the way children with developmental disabilities—approximately 1 in 10 in the United States—express their creativity through music by harnessing EEG technology to translate brainwaves into personalized musical experiences. Daniel and Justin have extensive experience teaching music to children, but working with those who have developmental disabilities presents unique challenges: Identifying and adapting resources for non-verbal and special needs students. Integrating music therapy principles into lessons to foster creativity. Encouraging improvisation to facilitate emotional expression. Navigating the complexities of individual accessibility needs. Unfortunately, many children are left without the tools they need to communicate and express themselves creatively. That's where Duet comes in. By utilizing EEG technology, we aim to transform the way these children interact with music, giving them a voice and a means to share their feelings. At Duet, we are committed to making music an inclusive experience for all, ensuring that every child—and anyone who struggles to express themselves—has the opportunity to convey their true creative self! What it does: Wear an EEG Experience your brain waves as music! Focus and relaxation levels will change how fast/exciting vs. slow/relaxing the music is. How we built it: We started off by experimenting with Emotiv’s EEGs — devices that feed a stream of brain wave activity in real time! After trying it out on ourselves, the CalHacks stuffed bear, and the Ariana Grande cutout in the movie theater, we dove into coding. We built the backend in Python, leveraging the Cortex library that allowed us to communicate with the EEGs. For our database, we decided on SingleStore for its low latency, real-time applications, since our goal was to ultimately be able to process and display the brain wave information live on our frontend. Traditional live music is done procedurally, with rules manually fixed by the developer to decide what to generate. On the other hand, existing AI music generators often generate sounds through diffusion-like models and pre-set prompts. However, we wanted to take a completely new approach — what if we could have an AI be a live “composer”, where it decided based on the previous few seconds of live emotional data, a list of available instruments it can select to “play”, and what it previously generated to compose the next few seconds of music? This way, we could have live AI music generation (which, to our knowledge, does not exist yet). Powered by Google’s Gemini LLM, we crafted a prompt that would do just that — and it turned out to be not too shabby! To play our AI-generated scores live, we used Sonic Pi, a Ruby-based library that specializes in live music generation (think DJing in code). We fed this and our brain wave data to a frontend built in Next.js to display the brain waves from the EEG and sound spectrum from our audio that highlight the correlation between them. Challenges: Our biggest challenge was coming up with a way to generate live music with AI. We originally thought it was impossible and that the tech wasn’t “there” yet — we couldn’t find anything online about it, and even spent hours thinking about how to pivot to another idea that we could use our EEGs with. However, we eventually pushed through and came up with a completely new method of doing live AI music generation that, to our knowledge, doesn’t exist anywhere else! It was most of our first times working with this type of hardware, and we ran into many issues with getting it to connect properly to our computers — but in the end, we got everything to run smoothly, so it was a huge feat for us to make it all work! What’s next for Duet? Music therapy is on the rise – and Duet aims to harness this momentum by integrating EEG technology to facilitate emotional expression through music. With a projected growth rate of 15.59% in the music therapy sector, our mission is to empower kids and individuals through personalized musical experiences. We plan to implement our programs in schools across the states, providing students with a unique platform to express their emotions creatively. By partnering with EEG companies, we’ll ensure access to the latest technology, enhancing the therapeutic impact of our programs. Duet gives everyone a voice to express emotions and ideas that transcend words, and we are committed to making this future a reality! Built with: Emotiv EEG headset SingleStore real-time database Python Google Gemini Sonic Pi (Ruby library) Next.js <div