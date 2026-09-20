---
slug: "volunteer-options-alexa-skill"
url: "https://devpost.com/software/volunteer-options-alexa-skill"
title: "Volunteer Options Alexa Skill"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 394
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Volunteer Options Alexa Skill

> Volunteer Options helps people find interesting opportunities to volunteer in their community.

[Devpost](https://devpost.com/software/volunteer-options-alexa-skill) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** alex-skills-kit, node.js, rest-api, sessions

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- accomplishments
- what i learned
- whats next for the volunteer options alexa skill

## Body

Echo Show Mode on HD Fire Tablet running Volunteer Options Details Screen Inspiration Volunteering has been a rewarding experience for me. It can be fun, educational, helps you meet new people and gives you a good feeling. I've seen volunteering help my retired parents stay more active. There are many great organizations out there that just wouldn't exist without volunteers. When the Amazon Alexa Tech for Good Challenge popped up, it seemed to me there might be a way Alexa could help people discover and connect with various volunteer organizations. What it does Volunteering Options is meant for someone who wants to volunteer but doesn't know where to look. Just say "Alexa, Open Volunteer Options" and she'll prompt you for your zip code and then find up to 20 organizations nearby who can use volunteers. Volunteers come in many flavors, coach, teacher, EMT, fire personnel, rescue, relief workers, ski patrol, crossing guards, mentors, food shelf staff and so much more. Some opportunities are short some can last a lifetime. Give Volunteer Options a try and see what you can find! How I built it I knew that google maps seemed to be able to provide some information about volunteer organizations. With a little research I was able to find RestApi calls that provide a list of volunteer organizations based on a GPS location. Two additional APIs were required, one to determine GPS location based on zip code and another to get detailed information about each organization. Challenges Interestingly the API finds organizations based on GPS coordinates, so a challenge was to first translate a zip to latitude, longitude and then to process the list. Another challenge, would it be easier to ask for a user's permission and automatically determine their zip code? (I rejected this idea since a user may want to find volunteer options for a specific location, so the prompt for zip is more flexible and still plenty easy to use). Accomplishments This was a short-term Hackathon, done in my spare time, so I was happy just to produce an Alexa skill with potential to connect talented and willing volunteers with deserving organizations. What I learned I learned more about intents, node callbacks and google apis. Whats Next for the Volunteer Options Alexa Skill I could add a City intent or ask the user permission to automatically determine the user's location. <div