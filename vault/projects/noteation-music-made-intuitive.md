---
slug: "noteation-music-made-intuitive"
url: "https://devpost.com/software/noteation-music-made-intuitive"
title: "Noteation: Music made Intuitive"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 702
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Noteation: Music made Intuitive

> A powerful sheet music reader and annotator that automatically changes pages using AdHawk eye tracking technology and computer vision techniques

[Devpost](https://devpost.com/software/noteation-music-made-intuitive) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** adhawk, cockroachdb, flask, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for noteation: music made intuitive

## Body

The UI pages Our app in use at a piano The glasses and app side by side Inspiration Every musician knows that moment of confusion, that painful silence as onlookers shuffle awkward as you frantically turn the page of the sheet music in front of you. While large solo performances may have people in charge of turning pages, for larger scale ensemble works this obviously proves impractical. At this hackathon, inspired by the discussion around technology and music at the keynote speech, we wanted to develop a tool that could aid musicians. Seeing AdHawks's MindLink demoed at the sponsor booths, ultimately give us a clear vision for our hack. MindLink, a deceptively ordinary looking pair of glasses, has the ability to track the user's gaze in three dimensions, recognizes events such as blinks and even has an external camera to display the user's view. Blown away by the possibility and opportunities this device offered, we set out to build a hands-free sheet music tool that simplifies working with digital sheet music. What it does Noteation is a powerful sheet music reader and annotator. All the musician needs to do is to upload a pdf of the piece they plan to play. Noteation then displays the first page of the music and waits for eye commands to turn to the next page, providing a simple, efficient and most importantly stress-free experience for the musician as they practice and perform. Noteation also enables users to annotate on the sheet music, just as they would on printed sheet music and there are touch controls that allow the user to select, draw, scroll and flip as they please. How we built it Noteation is a web app built using React and Typescript. Interfacing with the MindLink hardware was done on Python using AdHawk's SDK with Flask and CockroachDB to link the frontend with the backend. Challenges we ran into One challenge we came across was deciding how to optimally allow the user to turn page using eye gestures. We tried building regression-based models using the eye-gaze data stream to predict when to turn the page and built applications using Qt to study the effectiveness of these methods. Ultimately, we decided to turn the page using right and left wink commands as this was the most reliable technique that also preserved the musicians' autonomy, allowing them to flip back and forth as needed. Strategizing how to structure the communication between the front and backend was also a challenging problem to work on as it is important that there is low latency between receiving a command and turning the page. Our solution using Flask and CockroachDB provided us with a streamlined and efficient way to communicate the data stream as well as providing detailed logs of all events. Accomplishments that we're proud of We're so proud we managed to build a functioning tool that we, for certain, believe is super useful. As musicians this is something that we've legitimately thought would be useful in the past, and granted access to pioneering technology to make that happen was super exciting. All while working with a piece of cutting-edge hardware technology that we had zero experience in using before this weekend. What we learned One of the most important things we learnt this weekend were the best practices to use when collaborating on project in a time crunch. We also learnt to trust each other to deliver on our sub-tasks and helped where we could. The most exciting thing that we learnt while learning to use these cool technologies, is that the opportunities are endless in tech and the impact, limitless. What's next for Noteation: Music made Intuitive Some immediate features we would like to add to Noteation is to enable users to save the pdf with their annotations and add landscape mode where the pages can be displayed two at a time. We would also really like to explore more features of MindLink and allow users to customize their control gestures. There's even possibility of expanding the feature set beyond just changing pages, especially for non-classical musicians who might have other electronic devices to potentially control. The possibilities really are endless and are super exciting to think about! <div