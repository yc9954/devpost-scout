---
slug: "brailled"
url: "https://devpost.com/software/brailled"
title: "Brailled"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 728
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
---

# Brailled

> Digital Braille Display + a mobile app that uses Azure AI services to convert digital text/printed text/speech to Braille thus, empowering cognition through AI.

[Devpost](https://devpost.com/software/brailled) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: video_visual</sub>

**stack** arduino, azure, bluetooth, dart, flutter

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for brailled

## Body

Speech OCR Text Create text file record audio Select text files Speech recognition Speech text from image OCR OCR Inspiration My mom is an expert in teaching kids with differential abilities, through her I got to know about the struggles of the visually impaired, the greatest gut-wrenching moment was when I came to know that there are 253 million people who are visually impaired, most of them are in my country India, and the solutions for their education such as Digital Braille Displays cost thousands of dollars, too much for someone living in a developing or undeveloped country to afford, and for this reason, they are one of the most deprived section of society when it comes to a very basic thing such as education, this motivated me to use whatever skills I had to develop a solution that should be affordable and practical. What it does There are two parts to it, Hardware and Software, the hardware is a custom-designed and prototyped digital braille cell that is made up of 6 electromagnetic actuators that are driven through a Darlington transistor array via an Arduino Uno, that communicates via a mobile app through Bluetooth that has been developed through flutter and makes use of azure cognitive services to convert digital text/Printed Text/Speech to braille and speech so that a visually impaired person could understand and educate. How I built it It all started with an idea to build a cheap braille cell, but then it did not take long enough to realize that source of content that needs to be converted to braille is just as important, this is when the idea of a mobile application came into the picture that would connect to the braille display through Bluetooth and use Azure Cognitive services that convert the traditional type of stored educational content such as digital text, printed text, and speech to braille. The Bluetooth communication between the braille display and the mobile is serial communication, transmits the data in bytes and that byte is manipulated to PORTB of ATMEGA328 Challenges I ran into The biggest challenge was making the app, I am more of a hardware guy and had not even touched app development, and now I had to create quite a complex app within a short amount of time, had never made a single API call in my life and now I had to make complex multipart POST requests to communicate with the Azure cognitive services, and all this while being a one-man team. it was quite hard but when the things actually fit together and worked as intended, the maker spirit inside me felt the joy I cannot describe. Accomplishments that I'm proud of Successfully created a hardware braille solution that is way cheaper than any competition, that is from thousands of USD to less than 20. Successfully created an app that uses Azure cognitive services to convert the content in the desired format and communicates via a digital braille display. An array of linear actuators controlled by a mobile application in real-time, I have not seen this before anywhere else, so I had to create a custom format in which the data is sent from phone to the device via Bluetooth. The most important achievement is when I took it to Akshat, who is 100% visually impaired by birth and is now preparing for law school admissions, when he read through the braille display for the first time, he smiled with satisfaction, that smile was everything for me, all the sleepless nights I spent was now worth it, and that smile was the biggest achievement. What I learned The things I have learned is this past month are almost nuts, from being a microcontroller and a hardware lover to, wetting my feet in the world of app development and knowing how easy it is to implement and integrate features similar to human-level cognition to a software application. I learned the beauty of giving back to the people in need, it was not about donating money, but giving time and attention to solving a problem that 253,000,000 people face and the rest of the world just ignores heartlessly. What's next for Brailled Improving exception handling Extending language preferences, the Azure cognitive services support almost every major language and that's awesome. Spending more time with the visually impaired students to get their feedback and improve. <div