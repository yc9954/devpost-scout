---
slug: "mypetpal-qbwgc9"
url: "https://devpost.com/software/mypetpal-qbwgc9"
title: "MyPetPal"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 833
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
---

# MyPetPal

> An AI-powered iOS app that reduces screen time and helps users stay focused.

[Devpost](https://devpost.com/software/mypetpal-qbwgc9) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]]
  <sub>weak: web_dom</sub>

**stack** css, geminiapi, html, javascript, react-native, screentimeapi, supabase, swift, typescript

## How they structured the write-up

- mypetpal usage
- what inspired us
- our biggest challenge
- the future for mypetpal

## Body

MyPetPal usage MyPetPal is an iOS app that limits excessive screen use while helping users to manage their time effectively and staying focused. The app features a daily report on users’ screen time usage, displaying the user’s most used apps and screen time throughout the day. In addition, it also features a task scheduler that leverages Gemini’s AI API to verify task competition, keeping users accountable for their productivity. MyPetPal introduces a gamification aspect, where the user is tasked with taking care of a pet. The pet’s mood and health dynamically respond to the user’s behavior, declining with extended distraction and improving as the user remains focused and productive. Together, these features tackle the growing problem of screen-time addiction and its correspondence with lacking productivity in both teenagers and adults. What inspired us The idea of MyPetPal stemmed from our and our community’s experience with screen-time addiction and its effects on a multitude of issues, namely productivity. Growing up in a highly academic area, grades and academics were emphasized, but effective time management and productivity skills were never taught. As a result—under constant stress from school work—we and our friends realized that we would spend excessive amounts of time on our phones through social media apps like Tiktok and Instagram, as a means of procrastination. With this in mind, we tried everything to limit distractions: we downloaded many popular screen-time managing apps like Opal to stay on task, but none seemed to work because of one key element: accountability. At the start of our sophomore year, we came up with a simple trick to help us stay productive for hours on end and get our work done before our friends even got home: the timelapse; we came up with a system where as soon as we got home from school, we would schedule dedicated work sessions, timelapsing the entire process and sending the videos to each other after. Slowly, we would end up timelapsing our entire after-school life: work, then take a break, work, then eat, work, then eat dinner—what started as a way to keep ourselves accountable turned into a system that fundamentally reshaped how focused we were after school. This timelapse method did two things: it kept us from procrastinating since we had to start recording right before each session, and it kept us off our phones—something we had struggled with extensively in the past. This method captures the essence of the benefits of accountability, and how accountability is the key element behind success. However, as our schedules started to not align due to varying extracurriculars, our system that was once so perfect would eventually fall apart: with no one to send the timelapse to, there was no motivation to start the timelapse in the first place, eventually leading to the destructive cycle of “doomscrolling” on social media. This sparked the inspiration for MyPetPal: what if there was a way to maintain that same sense of accountability and focus, but without depending on others’ schedules? After surveying 120+ students at our school, we set out to solve two key productivity issues: excessive screen time and low motivation to start work. Our biggest challenge The biggest technical challenge we faced while developing MyPetPal was implementing Apple’s Screen Time API. Apple places a heavy emphasis on security throughout their software, which makes the API highly secure, leading to limited access and complicated implementation. Documentation wasn’t helpful either: code examples were far too general for our use case, and the framework explanations were unclear, forcing us to spend several hours experimenting and troubleshooting. Additionally, we were unfamiliar with this framework, having no experience with it previously, so integrating it with React Native and Swift required extensive trial and error. This was by far our greatest setback, stretching across weeks and slowly chipping away at our motivation. Despite these difficulties, we were able to uncover a GitHub repository called “ScreenBreak” that used the exact same framework for a similar purpose. By analyzing their code, we were able successfully, enabling a core feature of our app. The future for MyPetPal If we were to create a 2.0 version of the app, we would focus on enhancing both user motivation and social connectivity. To encourage users to stay off devices, we would expand the gamification system by introducing a currency system, where coins can be obtained through days of consistent productivity. Currency could be spent to customize their pets to customize their pets-including changing their appearance, adding accessories, unlocking new animations-making the app experience more engaging and rewarding. To introduce a social aspect, we would implement calendar syncing, where users could participate in focus sessions, making it easier for users to coordinate with friends, participate in group challenges, and track progress together. We would also add analytics and insights, giving users productivity patterns to identify areas needed for improvement and enabling a leaderboard system for healthy competition. Overall, the version 2.0 would foster a more immersive and social-driven experience that would strengthen our motivation and engagement. <div