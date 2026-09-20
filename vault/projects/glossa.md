---
slug: "glossa"
url: "https://devpost.com/software/glossa"
title: "Glossa"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 912
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "substrate/video_visual"
---

# Glossa

> Glossa is your all-in-one language assistant that helps you learn and get better at writing and speaking English. Come, enrich your language learning experience.

[Devpost](https://devpost.com/software/glossa) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[education]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** azure, azure-cognitive-services, python, streamlit

## How they structured the write-up

- inspiration 💪🏻
- what it does 🤖
- how we built it 🔨
- challenges we ran into 🙅🏻‍♂️
- accomplishments that we're proud of and what we learned 🎖️
- what's next for glossa 🔜

## Body

Home Page Main Page Text to Text Translation Page Image OCR Page Image OCR functionalities in action What's this called? Page Image Captioning + News How "j" say it? Page Spelling Fix + Pronunciation features in action Chatbot Page Chatbot in action Azure Services Used LUIS app Page Training Intents in LUIS Testing chatbot performance in LUIS Mobile View Website Mobile View Functionalities in action in Mobile View Inspiration 💪🏻 The inspiration for this project is my dad's educational experience 🎓. He studied in an English medium school for the first time only when he graduated from secondary to higher secondary school. His primary language until then was Tamil and he shared with me how difficult it was for him to pick up English, as a dictionary/language translation book 📒 was the only means of translation for him. Receiving captions for images or vocal pronunciations of words were distant dreams at that time. Let us think about this, today, even though English is the most spoken language in the world (considering native and non-native speakers together), there are millions of people, especially in developing countries who still do not possess Basic English proficiency. This is limiting their growth and hence, with today’s technological advances, I wanted to help by building something useful for them. I believe Glossa with all the features it provides can help people all across the world 🌍 learn a language like English and excel in their lives. What it does 🤖 Glossa is an Azure-powered responsive web application that helps non-native English speakers learn as well as use English for their day-to-day activities. Glossa can be used to learn other languages as well. Glossa has 5 main features. You can watch the Youtube video describing its functionalities here 🎥. Brief Overview of Features: 📋 1) Text to Text Translation : Translate text from one language to another , get synonyms if available and listen to the pre-configured voice outputs. 2) Image OCR : Upload an Image and get its text extracted in the language of your choice. 3) What's this called? : Image Captioning + News - Upload an Image, get its textual description in the language of your choice and be able to search content related to it. 4) How "j" say it? : This feature helps you get better at writing and speaking English. Type an English sentence, get the spellings corrected and receive the pronunciation for the same. 5) Chabot : Interactive chatbot that helps solve your queries. These features make Glossa your all-in-one language assistant that helps you learn and get better at writing and speaking different languages. How we built it 🔨 Glossa is a responsive web application built using Python and Streamlit - Open source Python library. The functionalities are powered by Azure Cognitive Services. You can have a look at the code here 💻. Feature Wise Service Description: ⚒️ Description of the various pages have been shared in the 'What it does' section ☝🏻️ 1) Text to Text Translation Page : Azure services used here are the Translator and Text-To-Speech Cognitive Services APIs. 2) Image OCR Page : Azure services used here are the Optical Character Recognition and Translator Cognitive Services APIs. 3) What’s this called? Page : Azure services used here are the Computer Vision ‘Analyze an Image API’ and the Bing Search API. 4) How "j" say it? Page : Azure services used here are the Bing Spellcheck and Text-To-Speech APIs. 5) Chatbot Page : Built using the LUIS (Language Understanding) cognitive services API. Challenges we ran into 🙅🏻‍♂️ I am fortunate to be able to access many resources to easily learn what I want to learn but this is not the case for many people across the world. Hence, I had to put myself in their shoes, understand their pain points and accordingly develop a solution that could cater to their needs. This took a lot of time but I am happy with what I have been able to build for them. Initially, the Text-To-Speech API worked only on my local machine and not when deployed but I was later able to fix this by spending some time and thoroughly studying the API Reference docs. Now the feature works when deployed as well 😄. Accomplishments that we're proud of and What we learned 🎖️ The fact that I was able to build an End to End solution that could potentially help millions of people excites me. On the technical side of things, I had to create the web app in such a way that it was responsive 📱, had good UI while ensuring that all the features worked as intended. I am happy that I was able to accomplish these goals. This was the first time that I used a Cloud Platform ☁️. Using Azure was great. It has a clean UI and well-structured layout which makes it easy to use and keep track of various services. Using Azure Cognitive Services was a good experience, thanks to the Quickstarts 🚄 provided for numerous programming languages and code labs. Had to check the API Reference Docs for a few functionalities and they were really well documented and easy to use. What's next for Glossa 🔜 Recent advances in Natural Language Processing (NLP) enable us to implement exciting functionalities like Passage Summarization and Grammar Correction . Features like these could further enrich the language learning experience and I look forward to integrating them into the future versions of Glossa. <div