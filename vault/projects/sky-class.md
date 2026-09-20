---
slug: "sky-class"
url: "https://devpost.com/software/sky-class"
title: "Sky Class"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 642
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Sky Class

> Sky Class enables anyone to create a class and offer voice-interactive content through any Alexa device.

[Devpost](https://devpost.com/software/sky-class) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** c#-asp.net-web-api

## How they structured the write-up

- inspiration:
- what it does:
- how i built it:
- challenges i ran into:
- accomplishments that i'm proud of:
- what i learned:
- what's next for sky class:

## Body

List of classes My Account page Content slides and options Student management page File upload management Editing a content slide Inspiration: I built this to provide voice activated learning for the visually impaired (I have some blind people playing my other Alexa skill and have been thinking about the ways this technology can change their lives), but this skill is for anyone who wants to provide their content to specific groups of people. Students, people in their study group, family, friends, church groups, corporate training, customer service surveys, interactive user manuals. Sky Class is the gateway to voice-interactive learning. What it does: Sky Class is a way for anyone to create a class, with content delivered by Alexa. Using my website, myskyclass.com, you create an account, then create a class, and drag and drop bundles of content called slides. Each slide is Alexa saying something. You can add whatever you want her to say, including the new SSML markup. I’ve made adjustments to automatically slow the rate at which she delivers sentences to make it easier to follow her. You can add prompts to each slide. A prompt is how you respond to that information, like a menu of options. Then depending on their selection, it takes them to another slide. You control the structure of the content using the web site, connecting one piece of information to another. The student, at home on their Alexa device, chooses their path through your content using voice commands. The slide of content doesn’t just have to be Alexa speaking, though; it can be an MP3 file that you upload through the site, that automatically streams. So you can include full lectures in your class, sound tracks, corporate training, bedtime stories, verbal instruction to your kids, or instructions for the babysitter, so they know about meals, bedtime, and emergency contact. When your class is all ready, you provide the registration code to your students. Students create their own account at the web site and enter the code, and they are automatically added to your class. When they launch Sky Class, they have access to your class, and to any other classes they have registered for. As the teacher, you can see all the people who have registered for your class and how much of your content they’ve visited. You can use your own registration code and join your own class as a student, to try it out. And it gets even cooler. You can create quizzes that they take while using the skill, and their scores are tallied and you can see and download the results. You can have the skill tell them their score or you can just keep it to yourself. You can also post a message for a specific student that is delivered only to that student when they launch Sky Class. And you can deliver document files of any kind by email, by attaching them to any slide. The student just says, Email me more information, and an email is automatically sent with the document attached. Or think about corporate clients listening to a sales presentation and then asking for more information to be sent to them. How I built it: C#, this is a Windows web service that talks directly to the Amazon cloud. Challenges I ran into: I ran out of time implementing amazing features. But there is plenty here for v. 1.0. Accomplishments that I'm proud of: The web interface is pretty slick in light of how quickly this came together. The ability to upload, manage, and deploy streaming MP3 content is what will make this skill immensely useful to people and organizations. What I learned: Amazon's technology is going to change the world. What's next for Sky Class: Even more improvements for the web interface, to make it easier for people to set up their content. <div