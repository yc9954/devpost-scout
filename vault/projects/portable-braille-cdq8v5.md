---
slug: "portable-braille-cdq8v5"
url: "https://devpost.com/software/portable-braille-cdq8v5"
title: "Portable Braille"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 470
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/education"
  - "domain/labor_employment"
---

# Portable Braille

> Educational device that encourages young visually impaired people to learn and practice Braille in order to increase chances for future employment and expand general literacy level of the community.

[Devpost](https://devpost.com/software/portable-braille-cdq8v5) · hackathon [[TreeHacks 2025]]

## Facets

**domain** [[accessibility]] [[education]] [[labor_employment]]

**stack** arduino, bluetooth, braille, c, esp32, ios, rayban|meta

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for portable braille

## Body

Components to combine in limited size PortableBraille Capturing stream video from RayBan|Meta glasses to Jetson Orin Nano for facial expression recognition Inspiration Literacy level of Blind and Visually impaired community even in United States is lower than 10%. And the reason is simple - Braille (tactile text) is not affordable and not accessible today. I follow Haben Girma - the first deaf-blind person graduated Harvard Law school. She is a brilliant person, wrote books, influencer and advocates for people with disabilities rights. I saw how efficient she is in communications with people. However, she needs a special person who assists her by typing speech of her interlocutors, so it can be converted to Braille format and Haben can read it in tactile format. I believe that she could do even more if there is a device that could do handle it, keeping her communication private and without relying on assistance. What it does For visually impaired people the device allows users to read and write text on the phone privately, texting, surfing web, swiping Instagram, and of course learn and practice reading and writing. It is the first device that encourages blind users to improve their reading skills in most delightful ways - communication with loved ones and friends. Also device allows to "read" face expressions while talking to people, by face expression recognition using RayBan|Meta glasses and doing computing on the Jetson Orin Nano. It is the only solution today that doesn't require connection to internet and work even faster than BeMyEyes (powered by OpenAI). For deaf-blind users convert all speeches to text, and then converts it to tactile Braille and render in on the device, so user doesn't need an assistant. How we built it We 3d-printed an enclosure of the device on the 3d printer. Soldered Li-Po battery to battery-management-System module for correct charging/discharging and powered the microcontroller and Step-up boost DC-DC converter to power up braille module, which needs 200V for operating. Braille module gets data from microcontroller. There is a keypad of at least 6 buttons for typing braille combinations. Keypad also connected to the microcontroller. Microcontroller syncs with a phone over Bluetooth Low Energy. We hacked RayBan|Meta glasses in analog way to connect in to Jetson Orin Nano. Challenges we ran into Education Open Accomplishments that we're proud of First really portable braille display that fits a pocket It encourages to practice reading Connected different platforms, even closed, to each other Allows blind and visually impaired individuals to receive and follow contemporary AI trends: not to listen but to read audio messages. What we learned how to power the hardware device with AI connect different platforms altogether still learning... What's next for Portable Braille test the device with more users to collect more feedback explore if this project can transform to a Product <div