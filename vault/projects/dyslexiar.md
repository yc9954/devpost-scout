---
slug: "dyslexiar"
url: "https://devpost.com/software/dyslexiar"
title: "DyslexiA_R"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 1026
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DyslexiA_R

> An assistive technology iOS app that helps dyslexic individuals using optical character recognition and augmented reality

[Devpost](https://devpost.com/software/dyslexiar) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]]
**substrate** [[structured_db]] [[video_visual]]

**stack** ar, arkit, c, cloud, firebase, google, ios, ml, objc, ocr, swift

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for dyslexia_r

## Body

Analyze View Controller Convertible AR Dog Reading AR Autocorrect Inspiration Our team is a strong believer in the power of reading. Since childhood, we were the kids that would read under the cover late at night because we just loved the experience so much. From Agatha Christie to Harry Potter to Dale Carnegie, we've had a fascination with immersing in a good book. Discovering that some people - namely dyslexic individuals - face such a large obstacle to reading, astounded us. We wanted to do something about it, so we decided to help dyslexic people read and write fluently. What it does Dyslexia is the most common learning disability in the world and is characterized by difficulty in spelling, writing, and reading comprehension. Dyslexic individuals have trouble connecting letters to the sounds they make, and therefore have trouble reading. Despite the fact that dyslexia has nothing to do with intelligence, and is rather a result of neural hardwiring, there is negative stigma regarding the intellect of dyslexic individuals. To help dyslexic individuals cope with some of the challenges posed by dyslexia, we created DyslexiA_R - an assistive technology app that uses machine learning to recognize words and display augmented reality models. DyslexiA_R performs three major tasks: helping dyslexic individuals read, write, and visualize their progress. The introductory page of the app contains directions for how to use the 3 features of the app. The UI design of the app is optimized to making the user experience as smooth as possible for dyslexic people. We use gif images to demonstrate correct app usage, and speech buttons to speak directions. Users can sign into the app using fingerprint scanning instead of passwords written in small font - which may be a challenge to dyslexic people The first feature is reading assistance. Users can resize the scanning box by pinching, and position it over the text they want help reading. By clicking the speech button, the user can hear the text being spoken. Under the hood, a machine learning algorithm parses the text inside of the scanning box using optical character recognition. Once the algorithm has classified the text, a text to speech framework will speak the text. If the user clicks the AR button, the same optical character recognition will first recognize the text, detect a nearby surface using Apple’s AR kit, and and then project a model of the word in augmented reality. We use echoAR to provide the AR models. Since dyslexic people usually understand better using visuals rather than text, these AR models will assist them during reading. At any time the user can press the cancel button to dismiss the speech or AR model The second feature is writing assistance. Dyslexic individuals often have trouble spelling, so we created an autocorrect algorithm to assist them while writing. While writing, the user can resize the scanning box to fit the desired text. Then, press the scan button. Now, we use a combination of optical character recognition and a custom autocorrect model to display possible words the user intended to write. The user can hear the different options by clicking the speech button, and then select the correct word. This word will be projected in augmented reality onto a detected piece of paper. The user can now trace the word and continue writing. Over time the dyslexic user may develop muscle memory for the way certain letters are written. The last feature is progress analysis. In this screen, we show users some helpful statistics regarding their progress: most misspelled words and weekly progress of how many words practiced. The raw data is stored on a secure Cloud Firestore database using Google Cloud, and is collected as the user utilizes features of the app. Dyslexia can be a challenging disorder to face, but we hope our assistive technology iOS app alleviates some of the obstacles and improves users’ ability to read and write fluently. How I built it We built the main iOS application on XCode using Swift. We used UIkit to create simple UI, SwiftUI to create more advanced animated UI, and ARkit to render various augmented reality models. The augmented reality models were provided by echoAR. We trained a machine learning model to recognize and classify text. Our model architecture follows the state of the art in OCR: the input image is fed through a convolutional neural network and then an LSTM. Finally the CTC algorithm with beam search is applied to extract the characters. Our UI is completely centered around dyslexic individuals, so we don't have tiny text that may be hard to read. We use animated images and speech buttons. For speech buttons, we use the AVFoundation framework. We store data regarding reading/writing progress on a Cloud Firestore database using Google Cloud. The iOS application also uses an auto-suggest algorithm that determines the most likely intended word, and then provides the correct spelling. The auto-suggest algorithm was written in C and Obj-C and is extremely efficient, using an O(word length) trie and a dynamic programming Levenshtein distance calculator. Challenges I ran into The augmented reality was reallly tricky, but we used some pro debugging skills to figure out what the heck was going wrong. The auto-suggest algorithm was also very challenging to write, and even importing it into a Swift iOS project took a lot of head-scratching. The machine learning optical character recognition was of course difficult to use with new data. Accomplishments that I'm proud of We tried really hard to make an app that can actually help people in need. By using ML, OCR, AR, and other pretty advanced coding tools, we were able to create a working prototype. We all probably learned more during the hackathon than most university lectures :). I guess we really learned the importance of hands-on experience as well What I learned Optical character recognition, machine learning, augmented reality to name a few tools. But the most important - we learned how to make tech for the good of others. What's next for DyslexiA_R Hopefully, we can continue refining the app, improve our machine learning and auto-correct, and then publish it on the app store <div