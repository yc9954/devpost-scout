---
slug: "test-project-2a4vxf"
url: "https://devpost.com/software/test-project-2a4vxf"
title: "Lockdown Exams"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 652
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Lockdown Exams

> Giving students exams at home while discouraging cheating.

[Devpost](https://devpost.com/software/test-project-2a4vxf) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** c#, expo.io, react-native, sqlite

## How they structured the write-up

- the problem
- our idea
- the solution
- the technical details
- what was achieved during this hackathon
- the required resources to finish this idea
- the impact during and after the covid crysis
- future ideas
- video note

## Body

The problem So now that everybody is in lockdown, most of the students are worried about their schedule regarding education, not necessarily because they would not study, since studying from home is no big deal as long as you have the required tools for your activity, but because there is currently no reliable way to test their knowledge in online exams and assuring that there was no cheating done. Our Idea That's why we thought at "LockdownExams", system that tries as much as possible to discourage cheating while taking online exams. In order to show you how we do that, we prepared a little description: The solution The whole system is formed from 3 applications: a phone app, a desktop app and a webserver. The student will log in on the desktop app with the credentials provided by his/her university, and there a list of the exams that he needs to take will be displayed (a time frame in which those exams are available could also be added). The student clicks on an exam, a test is done on his webcam to see that he has one and it works, if that's the case , then an image with a qr code is opened, he uses the phone app to scan that qr code and the exam is started. Now, his desktop app is locked in full screen, his phone is locked on the app screen and the webcam started the recording. There will be filters for things like: the student leaving from the pc, the sound of a different keyboard, the student starting to talk etc. and these actions will be marked as a note with timestamp on the current recording. Once he finishes the exam, the recording is uploaded to the web server in order to be reviewed later (since there will be thousands of hours worth of view time, that is why we add the notes on the timeframe of the video.) The technical details The desktop app will be written in C# using windows forms, and in order to prevent the student leaving the fullscreen view, certain key combinations (alt+tab, ctrl + tab etc.) will be disabled. For the access to the webcam and the filters, we will use AForge . The phone app will be made using react native and expo.io and the webserver will be nginx with the scripting done in PHP using the Laravel Framework . The database for storing student/teacher related data will be MySql What was achieved during this hackathon Well, the whole idea is really complex, but still we are proud that we managed to finish the first part where we can scan a qr code with the phone and a test is opened (although all the data there is hardcoded and we cheated a little bit by connection the pc and phone on the same wireless network) The required resources to finish this idea That is one of the most beautiful things in programming, apart from a computer and time, there is not much needed The impact during and after the COVID crysis During the crisis, this app will help students to stay safe in self isolation without worrying about postponing their academic schedule. After the crisis, if the validation process proves to be viable enough, a lot of flexibility will be added for the students (some of them are working and having extra projects, so allowing them to take the exam during a wider time frame would be a relief for a lot of them) Future ideas In order to try and make the exam as same as before, the phone app could have an option to make a photo and upload that to a specific exercises, that way, complex problems could be given, not only multiple choice type of questions. Video Note Unfortunately we don't know video editing, but we found one that explains our idea very close <div