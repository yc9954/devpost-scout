---
slug: "pytorch-information-extraction"
url: "https://devpost.com/software/pytorch-information-extraction"
title: "Pytorch for Information Extraction on Image Documents"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 201
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Pytorch for Information Extraction on Image Documents

> Learn Pytorch by building an information extraction system for student-id cards from scratch

[Devpost](https://devpost.com/software/pytorch-information-extraction) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** docusaurus, opencv, pytorch

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pytorch-information-extraction

## Body

Inspiration In 2019 I did my academic internship on machine learning What it does I extracts information from students-id(s) within images. How I built it I built the project using object detection, instance segmentation, image classification and image alignment. Challenges I ran into I had two main difficulties while developing the project and writing this tutorial: My personal computer has no GPU, so I had to rely on Google Colaboratory to train my models. Also, due to the issue of everything licenced under the MIT licence, I had to create my own datasets for the project. Accomplishments that I'm proud of I'm really proud to have developed and implemented a methodology for information extraction from scratch using my best machine learning library, Pytorch. Mostly because Information Extraction is real has been a real challenge in the discipline of computer vision for so many years now. What I learned I've mostly learned how to optimize my Pytorch code. I also learned a few tricks for developing Information Extraction Systems. What's next for Pytorch-Information-Extraction What comes next for this tutorial is surely the following: Make the detection module more robust to truncated documents. Develop and train a custom OCR engine using Pytorch. <div