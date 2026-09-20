---
slug: "sleep-sounds"
url: "https://devpost.com/software/sleep-sounds"
title: "Ambient Noise"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 1014
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/transportation"
  - "substrate/code_repository"
---

# Ambient Noise

> High-quality ambient sound loops on Amazon Alexa to help you fall asleep faster, sleep better, relax, and focus.

[Devpost](https://devpost.com/software/sleep-sounds) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[developer_tools]] [[labor_employment]] [[transportation]]
**substrate** [[code_repository]]

**stack** alexa-skills-kit, amazon-alexa, amazon-dynamodb, amazon-web-services, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for ambient noise

## Body

Some of the sounds of Ambient Noise Ambient Noise in the Alexa Skill Store Sample of the sound name variation parser Lambda function invocation pattern (traffic bursts at night) Inspiration A few months ago I was welcomed with a new upstairs neighbor in my apartment complex. No big deal, right? Unfortunately for me, my new neighbor had a tendency to walk very loudly and adopted a dog shortly after moving in that insisted on barking for an hour every morning at 5am. As someone who really enjoys a solid night of sleep and thinks of mornings as the bane of existence, you can probably imagine my daily frustration. After a couple weeks of unsuccessfully trying to let my body adapt to the noise, I decided it was time to put my Echo Dot on my bedside to good use... What it does To drown out my neighbor's (and her dog's) noisy morning routine I developed a "Rain Sounds" Skill consisting of a 1-hour loop-able track of rainshower background noise. After using the Skill for a couple weeks with considerable success, I published it to the Alexa Skill Store and was met with unexpected rapid growth and many positive reviews. It turns out that I wasn't the only one who thought Alexa would be a great ambient noise device! I responded to a swarm of reviews and emails asking for more sounds, leading me to develop and publish over a dozen individual ambient noise Skills . But what about the folks who wanted to use all my sounds? To help them avoid the potential pain of (up until recently) being required to enable each Skill before you can use them and assisting in the discovery of all the available ambient noises I had to offer, I decided to build a Skill capable of playing all the sounds from one simple prompt. Enter the consolidated "Ambient Noise" Skill . How I built it The Ambient Noise Skill is built upon the Node.js Alexa Skills Kit Audioplayer Example for AWS Lambda as a baseline for building proper Alexa audioplayer responses and persisting user data with DynamoDB. Since most folks listen to these ambient noises while they sleep, it was vital for the Skill to never abruptly switch sounds and to be able to handle an influx of traffic during nighttime hours. To address these concerns, I modified the example project to disable the concept of a "playlist" in favor of looping a specified track and used AWS Lambda to run my project's code. Additionally, I used incrementing values in the user's DynamoDB record to keep track of how many times each sound has been played and when the user was last active in order to personalize the Skill's speech and playback behavior in the future. All in all, it's not a horribly complex Skill, but a lot of thought went into creating a great, reliable user experience - and when it comes to voice applications, that's half the battle! Challenges I ran into Although Ambient Noise is a relatively simple Skill, I ran into a particular challenge of slot-only utterances not always being recognized properly. Sometimes I would say a sound but Alexa would act like she didn't hear anything, and other times the result was simply inaccurate. But hey, let's be honest: NLP (Natural Language Processing) is hard. While I'm sure the smart folks at Amazon are working every day to improve Alexa's interpretation of human speech, I needed an immediate solution. To resolve the issue, I created another intent (appropriately called "soundOnlyIntent") which had only one sample utterance attached to it: {Sound} . That's right - by isolating the utterance to its own intent Alexa was able to build a better language model. Ta-da! Problem solved! Accomplishments that I'm proud of When it comes to Voice User Experiences (VUX), ensuring that your Skill can react correctly to users' requests is extremely important. Humans phrase things in a myriad of ways and natural language processing (NLP) doesn't always translate a user's speech into a perfectly-matching Skill Slot Value. To account for this, I did two things. First, I added an utterance to allow a user to get a list of supported sounds, allowing them to hear an example of what the Skill expects them to say. But more importantly, I created a function to take in a potential slot value, cast it into lowercase-only characters, then cross-check it against a list of manually-made variations based on different ways that I could envision myself talking to the Skill. The result was over 130 variations of ways to say 13 different sounds . What I learned When first making this Skill I didn't have a firm grasp of how state handling was performed in the Node.js Alexa Skills Kit Audioplayer Example. While some Skills need to keep a detailed track of a user's state to be able to resume a complex interaction if they were to leave and come back, this Skill was quite the opposite: using multiple states actually made the Skill much more complicated than it needed to be. This forced me to learn how state handling is implemented in the ASK Node.js library so that I could reliably strip down the audioplayer example project my code was built upon to only use a single state. Not only did this process result in a lean codebase for Ambient Noise , but it also gave me the knowledge to build complex stateful Alexa Skills in the future. What's next for Ambient Noise Listening to user feedback and watching for unhandled requests from users' commands are vital to making a 5-star Skill. I'll be monitoring user feedback closely - both in reviews and via direct emails from users - to see what sounds I should add next. Additionally, I'll be using the analytics I've set up with VoiceLabs to watch for different variations of spoken names of sounds which I did not account for so I can improve the Skill's ability to play the right sound no matter what alternative name a user may have for it. <div