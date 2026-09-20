---
slug: "sagacity"
url: "https://devpost.com/software/sagacity"
title: "Sagacity"
hackathon: "Hack the North 2019"
winner: true
words: 420
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Sagacity

> An application that takes pictures of fragmented written notes and converts them into high quality, readable and organized notes

[Devpost](https://devpost.com/software/sagacity) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, google-cloud-vision, html, javascript, mongodb, natural-language-processing, node.js, python, tensorflow

## How they structured the write-up

- motivation
- the problem we saw
- what exactly does it do?
- who is it intended for?
- how it was built

## Body

Banner Image Banner logo Thumbnail Image Demo Screenshot Motivation For most (new) university students find it challenging to take clear, concise and organized notes while understanding and interpreting the contents of a lecture. This often leads to fragmented thoughts captured in the form of unorganized blurbs of text. Unfortunately, having to pay attention to the information being put forward in a lecture comes at the cost of assimilating the information in the notes. Simply in order to assist us in our daily lives, we built an application that allows us to focus on learning (while taking terrible notes) by taking away the need to constantly format the way we write. We can stay disorganized (as long as all relevant information is transcribed) and simply allow the application to generate high-quality, readable and concisely formatted notes. The problem we saw Sagacity was developed to counter a daily issue that students face — note-taking. As the standards for education around the world continuously rise, the difficulty of notetaking does as well. Students are fed more information, at a faster rate than ever before. Rather than valuing the quality of their notes, students are forced to write rudimentary and fragmented notes in order to keep up with the fast pace of modern-day education. Thus, the students are forced to either make quick, scribbled notes to keep up, or make higher quality notes and fall behind. What exactly does it do? Sagacity is a web-based application that streamlines the note-taking process by digitizing disorganized hand-written notes by turning them into clearly formatted and structure notes. We use state-of-the-art OCR and NLP technologies in order to translate the handwriting to text and generate text around the keyword and related sentences found within the document. Who is it intended for? High school and post-secondary students are the target audience for this service. Whether they wish to simply organize their notes digitally, clean up cryptic notes to allow for easier comprehension, or anything in-between. How it was built This application used text detection models from the Google Cloud Platform as well as robust OCR to convert the handwriting in the image into text. All of the extracted data/metadata is put into a data structure that resembles a tree (slightly more complicated implementation, but we won't go into it here) after which all the detected text is put into a state-of-the-art NLP model (uses new recurrent network architectures as well as unsupervised learning) used to generate text around the key phrases while accounting for related sentences . <div