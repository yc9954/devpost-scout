---
slug: "dotify"
url: "https://devpost.com/software/dotify"
title: "Dotify"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 559
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Dotify

> Bringing the world to your fingertips.

[Devpost](https://devpost.com/software/dotify) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
**domain** [[accessibility]] [[health_clinical]] [[housing_homeless]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[video_visual]] [[web_dom]]

**stack** arduino, c++, cad, css, gemini, html, javascript, python, servo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for dotify

## Body

Dotify Dotify ⠙⠕⠞⠊⠋⠽ Inspiration Imagine walking into a grocery store and realizing that nearly every package is silent to your sense of touch. In the United States, unlike public signage covered by the ADA, there is no universal requirement for Braille on food products. Prescription drugs have some best-practice guidelines, but for everyday items like milk, soda, or cereal, Braille is virtually nonexistent. As a result, millions of visually impaired Americans rely on workarounds like QR codes, talking label devices, or smartphone apps just to identify something as simple as a can of soup. Labels, the most basic gateway to information, remain out of reach. Dotify was created to close this gap. It translates the visual world into concise, meaningful messages at the click of a button – and automatically prints out the corresponding Braille. What it does Dotify is an AI-powered portable device that captures an image, understands its content, and prints out a short label/sticker that can be read by touch. This is a super easy way to make shops, households, and other places in our community more accessible for the visually impaired. Capture: The user points the device at an object or scene and takes a picture. Understand: The image is processed by our software and analyzed through the Google Gemini API, which generates a concise text description (e.g., "a blue ceramic mug with a flower on it" ). Translate: The Arduino receives this description and converts it into Braille character data. Feel: Servo motors actuate pins to emboss the Braille dots, and a DC motor advances the paper for the next character. How we built it Dotify combines hardware, software, and AI into a single mechatronic system: Power System: 4×AA batteries powering the Arduino, motor driver, and six servos. Arduino UNO R4: The “brain” of the device, managing servo motions and motor timing. Google Gemini API: Web app takes photo and interprets visual data into descriptive text. Micro Servos (x6): Actuate Braille pins to emboss dots. DC Motor + Motor Driver: Feeds paper consistently between letters. 3D-Printed Housing: Keeps all components aligned in a compact, functional case. Challenges we ran into Mechanical precision: Aligning servo motors to press Braille pins accurately required several 3D-printed iterations. Motor control: Without PWM on the motor driver pin, we had to use fixed-duration timing for consistent paper spacing. System integration: Coordinating the website, AI API, and Arduino required a robust communication protocol to avoid data corruption or delays. Accomplishments that we’re proud of Built a functional Braille label printer using low-cost, off-the-shelf parts. Created a full end-to-end pipeline, from image recognition → AI description → Braille translation → physical embossing. Demonstrated the potential of AI and hardware to deliver accessible, real-world assistive technology. What we learned How to design and prototype a complex mechatronic device. Hands-on experience with software-hardware communication and servo control. How having a clear mission for the product is just as important as planning out technical details. The fact that we were solving real human problems definitely fueled us throughout the Hackathon. What’s next for Dotify Miniaturization & portability: Shrink the prototype into a pocket-friendly form factor. Multi-cell Braille display: Expand to a 10–12 cell line for faster reading of full words. On-device AI: Use tinyML models to perform object recognition without internet. Community feedback: Partner with visually impaired users to improve usability and design. <div