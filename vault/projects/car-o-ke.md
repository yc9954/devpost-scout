---
slug: "car-o-ke"
url: "https://devpost.com/software/car-o-ke"
title: "CAR-O-KE"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 399
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
---

# CAR-O-KE

> The first and only karaoke app for autonomous vehicles

[Devpost](https://devpost.com/software/car-o-ke) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[transportation]]

**stack** amazon-alexa, byton, dialogflow, musixmatch, nextjs, react, spotify

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i'm proud of
- what i learned
- what's next for car-o-ke

## Body

Select songs by mood Menu Page Song search Singing Analytics & Social Karaoke Experience Inspiration Byton's prompt challenged us to think about how would we spend time in an autonomous vehicle with a 49" shared experience display. Karaoke was among the first things that came to our mind as it's not only a fun group activity but also very well-aligned with what we already do in cars. At the same time, autonomous vehicle with cutting edge technologies such as Byton could bring karaoke to the next level. What it does Caroke is the first and only karaoke app specifically designed for autonomous / semi-autonomous vehicles. The features includes Auto suggestions: Just like Spotify for Karaoke on wheels, Caroke suggest songs for you to sing according to passengers preference, ambience, and location. Smart voice coaching: Caroke analyses your singing for you to see if you're out of tune and provide overall score for your sining. Voice Recognition: Start a song by just saying. Caroke understands you just like your favorite smart assistants such as Amazon Alexa. Record and Playback: Keep the fun memories of you and everyone in the car. Social: Have more fun together with personalized vocal tracks for everyone in the car. How we built it We mocked Byton's in-car experience of our app in a Web Application built with React. The voice recognition uses Web Speech API and Dialog Flow. Karaoke data (lyrics and tone) is from a UltraStar Deluxe song collection by razzertronic. We built our custom karaoke simulator with a pitch recognizer component inspired by PitchDetect by cwilso. Challenges we ran into We would love to use Alexa as in real Byton cars do but we cannot use it in web apps, so we used Dialog Flow instead. Pitch detection is pretty challenging in environment such as javascript. Accomplishments that I'm proud of Made a potentially reusable karaoke simulator First time designed for a screen this wide What I learned Learned a whole lot about pitch detection Learned how to design for Shared Experience Displays Learned to prototype voice user experiences with Web Speech API which we found to be quite agile and would alternative to go straight into building a full-blown Alexa Skill. What's next for CAR-O-KE We'll see how our Byton challenge go. We're also interested in open sourcing our karaoke components to make it easier for people to prototype karaoke experiences. <div