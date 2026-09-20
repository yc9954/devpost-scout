---
slug: "find-your-inner-potato"
url: "https://devpost.com/software/find-your-inner-potato"
title: "Find your inner potato"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 249
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Find your inner potato

> Every person is unique, just like a potato. Are you big, small, cooked or fried? Raw maybe? Or not a potato at all, just pretending to be one. Find out your true potato here!

[Devpost](https://devpost.com/software/find-your-inner-potato) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**mechanism** [[runtime_tool_creation]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, bedrock, partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for find your inner potato

## Body

Inspiration I got the idea from a dutch website called "tostiszijnnetmensen.nl" (people are like grilled cheese sandwiches). It's quite old and static, but quite entertaining and random. I was wondering if I could get the same effect but with dynamically generated and personalized it further. What it does It finds out what kind of potato you are and creates a cool shareable image for linked-in. How we built it Challenges we ran into Soooo many. I thought this was easy. First of all, linking context between different inputs and outputs was very difficult to interpret. Also, various models seemed quite buggy and answered themselves in a chat. Anthropic always starts with an annoying sentence restating your question as some kind of disclaimer, which ruins customer experience. Also the time it takes to generate an image is not really user-friendly for dynamic apps. The reproducability of images is also hard. You sometimes want to tell a story about the same person, so you need similar images of that person. This is almost impossible unfortunately. Accomplishments that we're proud of Made the bot random enough to be funny sometimes. It was hard since quite often it outputs predictable or unfunny text which is 'too logical'. By first letting it create a completely random scene, and only then trying to match it with user input, we got better responses. What's next for Find your inner potato A bit linked-in campaign of course :) and maybe a talk on an AWS event. <div