---
slug: "lingovision"
url: "https://devpost.com/software/lingovision"
title: "LingoVision"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 459
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# LingoVision

> LingoVision lets people read text of any language simply by blinking at it. We use an AdHawk MindLink glasses to capture and translate any text the user is looking at into speech of any language.

[Devpost](https://devpost.com/software/lingovision) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[finance_payments]] [[immigration_refugee]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** adhawk, firebase, google-cloud, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lingovision

## Body

Screenshot of Detection Inspiration We take our inspiration from our everyday lives. As avid travellers, we often run into places with foreign languages and need help with translations. As avid learners, we're always eager to add more words to our bank of knowledge. As children of immigrant parents, we know how difficult it is to grasp a new language and how comforting it is to hear the voice in your native tongue. LingoVision was born with these inspirations and these inspirations were born from our experiences. What it does LingoVision uses AdHawk MindLink's eye-tracking glasses to capture foreign words or sentences as pictures when given a signal (double blink). Those sentences are played back in an audio translation (either using an earpiece, or out loud with a speaker) in your preferred language of choice. Additionally, LingoVision stores all of the old photos and translations for future review and study. How we built it We used the AdHawk MindLink eye-tracking classes to map the user's point of view, and detect where exactly in that space they're focusing on. From there, we used Google's Cloud Vision API to perform OCR and construct bounding boxes around text. We developed a custom algorithm to infer what text the user is most likely looking at, based on the vector projected from the glasses, and the available bounding boxes from CV analysis. After that, we pipe the text output into the DeepL translator API to a language of the users choice. Finally, the output is sent to Google's text to speech service to be delivered to the user. We use Firebase Cloud Firestore to keep track of global settings, such as output language, and also a log of translation events for future reference. Challenges we ran into Getting the eye-tracker to be properly calibrated (it was always a bit off than our view) Using a Mac, when the officially supported platforms are Windows and Linux (yay virtualization!) Accomplishments that we're proud of Hearing the first audio playback of a translation was exciting Seeing the system work completely hands free while walking around the event venue was super cool! What we learned we learned about how to work within the limitations of the eye tracker What's next for LingoVision One of the next steps in our plan for LingoVision is to develop a dictionary for individual words. Since we're all about encouraging learning, we want to our users to see definitions of individual words and add them in a dictionary. Another goal is to eliminate the need to be tethered to a computer. Computers are the currently used due to ease of development and software constraints. If a user is able to simply use eye tracking glasses with their cell phone, usability would improve significantly. <div