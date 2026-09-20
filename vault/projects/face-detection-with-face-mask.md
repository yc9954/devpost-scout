---
slug: "face-detection-with-face-mask"
url: "https://devpost.com/software/face-detection-with-face-mask"
title: "Wikang Wagi (Winning Language)"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 989
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Wikang Wagi (Winning Language)

> A language learning tool that extracts, translates, and reads Filipino text to English

[Devpost](https://devpost.com/software/face-detection-with-face-mask) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** azure, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for wikang wagi

## Body

Inspiration My 5-year old son is more fluent in English than my native language ( Filipino ). My project's name, Wikang Wagi , actually came from one of his books currently used at school. I like that phrase, which literally means "Winning ( wagi ) Language ( wika )". I think it embodies the goal of my solution, which is to help kids or anyone to "win" or be successful in learning Filipino and at the same time promote my native language. What it does I developed a webapp that will allow anyone to take a picture (using a webcam or phone's camera) of any Filipino text or passage and let it read to you its English translation along with the text regions found. The user can then hover or click on the highlighted region and a popover will show the corresponding translation. The webapp is responsive so it should work in desktop, laptop, phone, tablet, or any device with a browser and a camera. How I built it In summary, these are the Azure products I've used: Static Web App Function Cognitive Services - Computer Vision (OCR) Cognitive Services - Translator (Text Translate) Cognitive Services - Speech (Text to Speech) I used both JavaScript (for UI) and Python (for API backend) to write the codes along with some nice 3rd party libraries to help me build the camera feature. The UI is hosted as a Static Web App that uses Python Function as its API. The UI makes use of Speech SDK to provide the text-to-speech feature while in the Function implementation, both the Read API (to extract text from images) and Translator REST (to translate Filipino to English) were used. Also in the backend, I added OpenCV module as well to do additional image preprocessing (eq. resize image, convert to grayscale, blur, etc.) to increase text extraction accuracy if needed. I think this kind of approach is good and scalable since it can easily allow me to add more Cognitive Services or even custom ML package in the future. Challenges I ran into I have some Machine Learning background but I'm primarily a JavaScript developer working on an ERP platform product at work, and my ML skill is not applicable there plus I haven't tried using the Camera API in an actual website yet. It took me a while to get a hang of making a camera UI especially the part of sending the file blob from browser, then backend will handle and process it, and then finally send it back to the browser. I'm not that good in designing a user interface from scratch as well so I just went with a simple and clean UI then focus on the main features first and ease of use. Unfortunately, I started late for this event and was not able to provide a fancy and nice looking UI (which I can do given more time). Note that using any of the Azure SDK was a breeze and I find no challenge there, thanks to its good and easy to follow documentation along with lots of sample codes! Accomplishments that I'm proud of It is my first time to use Azure products and to be honest, I find that the overall development workflow of using the 5 products I tested and together with VS Code, was very seamless and way better that what I experienced in AWS products. Again, the camera integration is something that I've done for the first time during this event and I think it will help me a lot moving forward when playing and testing Computer Vision + ML in my side projects. Most importantly, hearing my son said "Dad, that's cool!", was the greatest reward in all of this and I'm sure he'll enjoy his Filipino study time now. What I learned A lot! I wish Azure can offer monthly free credits (just like AWS) to hobbyist like me to further experiment the other Azure products especially those ML related that I want to further test :) Due to lack of time, I was not able to try the part where I can design my own CNN, do model training/testing, then deploy/host it. My initial project idea of creating a custom model that can identify your name with and without face mask would benefit from that setup. What's next for Wikang Wagi I wish I have more time to do these things below but I think someone can actually build a business/product around this, which is basically a kind of an eLearning service. Here are the features that I have in mind: My son always asks "What's the English of ( insert Tagalog word )?" so adding more text processing after text extraction to find words or group of words and then allow translation of those individually. Potential UX would be something like tapping the word or phrase then it will show a popover of the English translation. Support reverse translation (from English to Filipino). Unfortunately, Speech Text-to-Speech does not support Filipino yet. Support for all supported languages in Translator Integrate to an online dictionary ( https://dictionaryapi.com ) to offer more learning opportunity and understanding. If the translated word or phrase is incorrect, provide a way to set the right or better translation. That can be done by providing a database and add a new logic on when to query from DB or use the Azure service. Perhaps, these manually entered translations can be used by Azure as additional training data that can improve the overall performance of the Translator service. Have a collection of commonly forgotten words and provide a flashcard to strengthen memory. My favorite and the one I currently use is Anki ( https://apps.ankiweb.net ) so an automated integration to that if possible would be great. Offer a free and premium tier since anyone can spam the usage of this service and could cost a huge bill on my part! <div