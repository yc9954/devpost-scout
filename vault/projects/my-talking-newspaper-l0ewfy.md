---
slug: "my-talking-newspaper-l0ewfy"
url: "https://devpost.com/software/my-talking-newspaper-l0ewfy"
title: "My Talking Newspaper"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 630
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
---

# My Talking Newspaper

> Helping blind and visually impaired people to find and play talking newspapers, magazines and podcasts

[Devpost](https://devpost.com/software/my-talking-newspaper-l0ewfy) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[accessibility]]

**stack** amazon-alexa, amazon-dynamodb, amazon-web-services, javascript, lambda, love, node.js, s3, shell, sox

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for my talking newspaper

## Body

Example of a log from the game, where a user has helped a future user find their talking newspaper by an alternative name Use of ProgressiveResponse to transparently check for new items on each Newsession invocation A user has reported a TN with wrong details. I'll check that out. Another user has given an invalid name for a town. Use of multiple techniques to provide the most flexible way to ask for any item, and log or capture new or mispronounced items Inspiration There are over 500 talking newspapers and magazines in the UK, providing spoken-word local news and information to anyone who may be blind, partially sighted, or have any kind of print impairment. These cater to the almost 2 million people registered blind in the UK and are recorded by volunteers. Voices which become familiar to the listener. It's been described as having a friend read you the news every week. Information may include theatre guides, local interviews, listings for audio description at the local cinema, or council information. Editions are usually weekly or bi-weekly, and there are sometimes monthly magazines too. In ten years working with talking newspapers and technology for blind people, I realised there's a huge gap between the expensive proprietary complex audio players, and the simplicity of the potential of a voice user interface. What it does It's not just an audio player or yet another podcast player - it's a way for people to discover new content, support and local services. As well as a comprehensive listing of the UK's talking newspapers, And it has exclusive features not just specific to people with sight loss, but for everyone. For example, many like to listen at an increased playback speed. As far as I am aware, this is the only skill which does that. There's also intelligent time skip - if you request a point in time past the end of the track, it doesn't just stop like some players, but takes you to a point 30 seconds before the end of the track. How I built it With confusion, frustration, dedication, Slack, excitement and a lot of learning, late lights, lambda and love! Challenges I ran into During development, Lambda available on node updated to 8.10. I was able to re-factor my code to make much better but this was quite a change. For a period of some months in early 2018, all Alexa devices had an Audioplayer bug which meant that they could not seek to points in tracks longer than about 15 minutes This meant that I had to remove one of the key features of my skill, the ability to jump to any point in time. This is re-introduced with this new version. The AudioPlayer interface does not allow direct invocation once playing, and this required a lot of thinking around. Non-https audio is not allowed and there is no functionality to increase playback speed within the Audioplayer, so I built a complete AWS backend to pre-render and store copies of the files at normal and 1.5x playback speed on the AWS S3 services in London and Ireland, giving a much faster, more robust response on https endpoints. Accomplishments that I'm proud of The very positive reviews, even on the basic first version of the skill. The number of people using it. The positive feedback, support and enthusiasm for listeners. What I learned VUI, node, javascript, AWS, S3, SSML What's next for My Talking Newspaper With the recognition and publicity that a prize like this would give, this skill could grow worldwide. I also very much look forward to features which are currently US-only, like CanFulfillIntentRequest and PlaybackMode Intents, being made available outside the US, so I can improve and make my skill more easily accessible to more people. <div