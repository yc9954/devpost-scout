---
slug: "crocosign"
url: "https://devpost.com/software/crocosign"
title: "CrocoSign"
hackathon: "Dropbox Sign AI-Powered Agreements Hackathon"
organization: "Dropbox"
winner: true
words: 438
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "user/legal_professional"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# CrocoSign

> CrocoSign is the cross platform app that helps entrepreneurs, individuals and small businesses keep a paper trail seamlessly with the power of AI generated agreements and cute UI.

[Devpost](https://devpost.com/software/crocosign) · hackathon [[Dropbox Sign AI-Powered Agreements Hackathon]]

## Facets

**domain** [[labor_employment]] [[legal_justice]]
**user** [[legal_professional]] [[small_business]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** android, dart, firebase, flutter, gpt, ios, material-ui, web

## How they structured the write-up

- 🌟inspiration 🌟
- 🚀 what it does 🚀
- 🛠️ how we built it 🛠️
- 🤔challenges 🤔
- 🏆accomplishments 🏆
- 🧠 what we learned 🧠
- 🐊what's next for crocosign🐊

## Body

🌟Inspiration 🌟 CrocoSign is designed for entrepreneurs, individuals, and small businesses who need a hassle-free way to create clear paper trails, especially when starting out. Many entrepreneurs initially rely on oral contracts with peers or other businesses, which while are legally binding, are very challenging to enforce. That's where CrocoSign comes to the rescue! 🚀 What it does 🚀 CrocoSign bridges the gap between verbal agreements and written contracts. Early-stage product development often involves critical agreements that can lead to problems later on if not properly documented. In these situations, verbal agreements are insufficient, and hiring a lawyer may not be practical due to cost and time constraints. With the power of AI and Dropbox Sign, it is as easy as vaguely describing the agreement details, and CrocoSign does all the rest. Everything from the document generation and editing phase, up to managing the signers and facilitating the signing process. 🛠️ How we built it 🛠️ Flutter & Dart for Client side application The application was built with Flutter in order to target multiple platforms (Android, iOS and Web) entirely during the duration of this hackathon (more specifically, the last one week and a half of it); Figma & Inkscape for UI/UX design The UI design and logo were made using Figma and Inkscape. Certain assets such as the loading indicators were taken from the free library of lotties online and edited accordingly; Firebase for persistence layer (Firebase Storage for document storage, Firebase Realtime Database for user data and Firebase Auth for user authentication); GPT 3.5 for text generation. 🤔Challenges 🤔 Time constraint issues prevented me from polishing the web interface the way I wanted; Embedded signing, due to added complexity in deployment process (different impact for Android and Web), was replaced with non-embedded signing; Managed to overcame some framework limitations in regards to pdf file processing, resulting in developing my own widgets from scratch to accomplish this goal. 🏆Accomplishments 🏆 Aside from points mentioned above, I was able to complete the generation flow and get consistent results with GPT3.5 Made a contract with my flat mate in regards to when I am required to walk their dog. I am no longer bound by verbal agreements! 🧠 What we learned 🧠 PDF manipulation in Flutter; this is a topic I was especially interested in, but didn't have time to explore; Dropbox Sign is very simple to use - as long as you do not use Dio in Flutter (encountered an interesting issue which I will be detailing in my feedback report) 🐊What's next for CrocoSign🐊 The Nile 🐫 .. and possibly Google Play and a pricing plan! <div