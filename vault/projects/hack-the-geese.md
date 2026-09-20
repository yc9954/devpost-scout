---
slug: "hack-the-geese"
url: "https://devpost.com/software/hack-the-geese"
title: "Hack The Geese"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 354
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Hack The Geese

> Make a bunch of new friends this weekend with 1-v-1 photo challenges! Get competitive, go social, and immerse yourself in the event like you've never imagined. Introducing Hack The Geese.

[Devpost](https://devpost.com/software/hack-the-geese) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]] [[video_visual]]

**stack** go, gpt3.5, javascript, next.js, typescript, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hack the geese

## Body

Inspiration At Hack the North, we found it tough to break the ice and balance coding with socializing. This personal challenge inspired us to create a project that makes it easier to make new friendships and get us all out of our social comfort zones. What It Does Here's how the game works: Scan your badge's QR code to log in. Find a (new) friend who you'd like to compete against. Receive a prompt, eg. "take a selfie with a person taller than you". Race to take a fun picture based on the prompt before the other player does. Win or lose, then you got to choose wether or not to rematch! How We Built It We built the websockets server using Go, it manages the game's state and updates the database when necessary. Our front end, include the custom duck generator, is built using Next.js and React. We used GPT-3.5 provided hackathon-relevant prompts, we used Prisma and PostgreSQL for the database, and we stored our images in Vercel Blob. Challenges We Ran Into First night: total system crash due to the websockets server not properly closing connections, fixed after many tireless hours.. thanks Sam. Fayd had to reimplement the broken QR scanner, twice! We weren't having much luck with those React components. Dieter struggled with coding unique duck colors... but after many bug fixes everything started working together. Accomplishments That We're Proud Of Getting to the event was tough for all of us. Sam flew overnight from California, Dieter drove 9 hours from Vermont, and Fayd had a 30-hour journey from India with layovers. But it was worth it! What We Learned We learned that making friends is just as crucial as writing good code. The journey from encountering problems to finding solutions showed us that anyone can overcome their fears. And yes, we also discovered that Canada has some really tasty snacks! What's next for Hack The Geese Making HTG more accessible to those outside of Hack The North to create new friendships and capture more moments so people have something more than just swag and a project to leave with <div