---
slug: "hockey-updates-an-alexa-skill-with-audio-updates"
url: "https://devpost.com/software/hockey-updates-an-alexa-skill-with-audio-updates"
title: "Hockey Updates, an Alexa skill with audio updates"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 862
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/web_dom"
---

# Hockey Updates, an Alexa skill with audio updates

> The Hockey Updates skill uses Polly to let Alexa communicate when an NHL game starts or someone scores.

[Devpost](https://devpost.com/software/hockey-updates-an-alexa-skill-with-audio-updates) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[web_dom]]

**stack** amazon-alexa, amazon-dynamodb, amazon-lambda, amazon-polly, amazon-web-services, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built alexa's audio updates
- challenges i ran into
- what i learned
- what's next for hockey updates

## Body

Inspiration My family adore Alexa. My 4 year old daughter is particularly smitten with her. She’s always asking Alexa to tell a joke, set a timer or... At this stage, Alexa is practically family. The sole issue is that she only speaks when spoken to - which is not how we communicate with each other - at all. Unfortunately, Alexa doesn't support native push notifications, yet . In an effort to give Alexa a voice of her own, I came up with the audio updates pattern (which forms the basis of my Hockey Updates skill). What it does The Hockey Updates skill uses Polly (the AWS text to speech service) to let Alexa initiate communication with us when she has something to say (e.g. when an NHL game starts, or someone scores). The result isn't quite to the level of native push notifications, as you have to ask Alexa to open a skill before she'll start providing updates, but it's pretty close! I've decided to call this the audio updates pattern (yes, I'm terrible at naming things). There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors. How I built Alexa's audio updates The hockey part of this skill is pretty run of the mill. What's cool are the audio updates. This quasi-notification functionality is essentially a loop with an if condition. To give a brief synopsis, Alexa plays a filler track (using her AudioPlayer feature), and when the track is almost finished, she checks if there’s an event to play to the user. If there is new audio, she queues that, alternatively, she queues the filler again. When the queued audio is played and almost finished, she checks again for a new event, and so on. The audio updates flow (which manages user state, generates and queues audio) is roughly as follows: Either an IntentRequest or an AudioPlayer.PlaybackNearlyFinished request triggers a Lambda function The function retrieves the user's data from DynamoDB (user table), providing the user's Alexa ID as the key The function calls a 3rd party API endpoint (in my case, the NHL schedule feed) If there's a new event to process for the user, the function calls DynamoDB (eventAudio table) with the event ID (to retrieve S3 URL, if one exists) If a new audio file is required (i.e. not present in the eventAudio table), the function generates a message and sends the SSML to Polly The function uploads the Polly response to S3 as an MP3 file The function updates the eventAudio DynamoDB table with the new event ID and S3 URL The function also updates the user’s data in the DynamoDB user table (to set the new event ID as the user's current event ID) The S3 URL is sent back to the Alexa service for queueing Challenges I ran into This pattern raises a number of new and interesting challenges from a VUI perspective. For example: Filler If there haven’t been any events in a while, how does the user know whether Alexa is still providing audio updates? I decided to play a filler track (the quiet sound of a hockey practice) to let the user know that Alexa is running in the background. Similarly, the absence of the filler track makes it clear that Alexa has stopped processing audio updates (after a user has cancelled them, or the game has finished). Intro Before jumping straight into the audio updates, I decided that Alexa should play an intro track. The intro track sets the expectation for the types of content the user will expect to hear whilst the skill is running. I also wanted to take this opportunity to remind the user that they can cancel the audio updates at any time. I felt that acknowledging the user’s control over the notifications was important, so as to belay any fears that Alexa might blurt out an update when the user wasn’t home. What I learned Whilst this pattern looked great on paper, I wasn’t positive if Alexa would support it in practice. Thankfully, she does. Moreover, my design for the events backend was overly engineered (with scheduled jobs to generate the event audio files). As luck would have it, I ran out of time to build the backend I had drawn up and tried just-in-time event audio creation instead. To my surprise Polly was lightening fast. As a result, Alexa only generates audio files when she needs them, saving function execution time and object storage costs. Also, it turns out you can’t emulate a goal siren using Polly, no matter how hard you try ! <speak><prosody rate="x-slow" volume="x-loud"><say-as interpret-as="expletive">discombobulated</say-as></prosody></speak> What's next for Hockey Updates Unfortunately, (at the time of writing) the hockey season is about to come to a close; and whilst I'd like to augment Polly's updates with actual game audio, there's probably more value in creating new skills which leverage the audio updates pattern. If you've been looking for a notification mechanism for Alexa, I hope this write-up has proved useful in some way. If you have any questions or feedback, please feel free to reach out to me on Twitter . Until next time... Alexa, stop. . <div