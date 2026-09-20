---
slug: "art-museum"
url: "https://devpost.com/software/art-museum"
title: "Art Museum"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 728
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Art Museum

> Go to the museum. With your voice.

[Devpost](https://devpost.com/software/art-museum) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**user** [[general_public]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** airtable, alexa, alexa-conversations, amazon-dynamodb, amazon-web-services, apl, apl-a, art-institute-of-chicago-public-api, jovo, lambda, node.js, rekognition, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for art museum

## Body

inspiration The genesis of this skill dates back a few years to AWS re:invent 2018. The Art Institute of Chicago had recently released a treasure trove of Creative Commons images (and audio tour snippets!) from their collection, which inspired a prototype at the Alexa hackathon that year. It was super fun to make and well received, but the idea never made it past that proof of concept. what it does Art Museum is a voice first art museum. It lets you traverse a vast art collection with simple language. As a starting place, you can go broad: “I want to see a painting”.“Show me another one like that”. And as you explore the collection, you can drill down. “Show me paintings from France”. “Show ones with horses in them”. “Bring me to sculptures from India.” “Actually, show one from Germany”. Each item is accompanied by a short form audio segment from the museum tour, bringing rich context to each piece as you view it. how we built it Of course none of this would be possible without the Art Institute of Chicago – a world class museum with a world class API (shout out to Nikhil Trivedi, the museum’s Director of Web Engineering & Experience Design for his guidance along the way!). Their catalog is vast, so the first thing we did was filter records that were in the public domain AND included bonus audio content. This left us with hundreds of records, but much more manageable than the full catalog. The API is full of rich information about each piece, but as with any voice project, the content is never just plug and play. To make this work, Katy and I built our own API in front of theirs, essentially designing a layer of conversational metadata to supplement their records so they would seamlessly integrate with our Alexa Conversations sample dialogs and custom slot values. We spent a ton of time on this, ultimately landing on category, origin, and detail as our three parameters. How would someone actually ask for a painting? They’d probably describe it! So we ran the catalog of images through AWS Rekognition to bring some additional descriptive tags into the mix. Our dataset is a blend of existing metadata from their API, some supplemental descriptive tags from Rekognition and of course a lot of elbow grease to smooth it all out. APL for Audio was also clutch. In the past you would have to mix the ambient museum audio into the dialogue lines, which is time consuming and often impractical. APL-A allowed us to mix a randomized assortment of ambient museum sounds to add some gallery vibe during the speech prompts. It also allowed us to serve the museum clips at full fidelity (would have been a shame to crunch them for SSML). The other linchpin was Alexa Conversations – which we utilized for dialog management, context carryover and state management. Building that scaffolding by hand with intents and session attributes is possible but it would be really hard and flimsy. Outsourcing the state management piece took a huge burden off the development process. challenges we ran into That being said, Alexa Conversations is crazy! It truly is a new paradigm for skill building – and it took a TON of experimentation with different model structures to achieve the experience we were hoping for. We had to scrap everything and start over four or five times. And each training data experiment can take many hours to design, build, debug, and observe. So working with this technology is a commitment. I’d have break through moments where I thought I’d figured something out, then 5 minutes later I’d have no idea what was happening. Major shoutout to the Alexa Conversations team for rolling up their sleeves and getting in the trenches with us the last few weeks and especially all this weekend. Their collaboration and partnership is why us and so many others made it to the finish line. accomplishments that we’re proud of Katy and I have always been excited about the intersection of short form media and voice. We’ve explored this with other projects by creating the media and building an experience around it. With Art Museum, we took an existing collection of media and made it more accessible. what We learned A lot. what's next for Art Museum Hopefully a lot. <div