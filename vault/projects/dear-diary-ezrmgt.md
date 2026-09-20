---
slug: "dear-diary-ezrmgt"
url: "https://devpost.com/software/dear-diary-ezrmgt"
title: "Dear Diary"
hackathon: "BitRate: Machine Learning & Music Series"
winner: true
words: 685
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Dear Diary

> Turn your journal into music

[Devpost](https://devpost.com/software/dear-diary-ezrmgt) · hackathon [[BitRate- Machine Learning - Music Series]]

## Facets

**domain** [[disaster_emergency]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** emotion, firebase, magenta, natural-language-processing, nextjs, react, typescript, vercel

## How they structured the write-up

- why use it?
- how it works
- what is exciting and useful about this project?
- challenges we ran into, what we learned, and what we're proud of
- what's next for dear diary
- areas for future research and technological developments in the community
- contact
- acknowledgments

## Body

DearDiary.ai Start screen Social sharing About us Turn your journal into music Why use it? We want you to journal and to feel better. Studies show that journaling increases mindfulness and alleviates stress, anxiety, and depression. We also want you to create music. Like journaling, the mental health benefits of creating music are well-documented . And music is awesome. How it works Sentiment Analysis As you type each word, we perform sentiment analysis using the popular natural language processing library VADER.js. This returns a prediction score from -1.0 to +1.0, that we interpret as a sentiment along the spectrum of negative to neutral to positive. Music Creation using Magenta We use Google’s Magenta MusicVAE pre-trained model to interpolate between two pre-composed melodies—one happy, one sad—created by our teammate Devin Lane who has a background in music composition and education. As you type, our app creates new music that lives in the latent space of the emotion spectrum between happy, neutral, and sad based on our sentiment analysis. Visuals and a e s t h e t i c We opt for minimal and calming design because we want people to freely express their thoughts and feelings. We animate an SVG tree with leaves and birds by covering parts of the image with white squares that we dynamically remove as the user types. Playfulness and Creativity We build in Easter eggs to encourage playfulness and creativity. The music changes with punctuation, special characters, upper case, and deleting. Try strong emotion words to see what you can create! Playback and social sharing We save entries using Google Firestore for realtime persistence so that users can save, share, and replay the exact song they create. We integrate "share to Twitter" and "share as a link" functionality. What is exciting and useful about this project? Artistic and musical considerations : Expanding the boundaries of user-generated art informed by AI trained on creative musicians' compositions. Music education and empowerment : more people feel that—yes—they can create music. Mindfulness, mental health, emotional awareness : A soothing, engaging return to the self. A recharge in the deluge of a storm. Coping during 2020 : Traumatic events abound—COVID-19, reckoning with social and racial justice, natural disasters, political division—we offer a moment to come into deeper awareness with your emotions. This radical self-compassion is an important step in societal transformation. Challenges we ran into, what we learned, and what we're proud of NLP sentiment score is a limited metric for gauging emotion of text. We were hoping to find a multi-dimensional emotion library, but there are only a few available and they're all paid services. It would be a great open source project to build an detailed emotion NLP API that runs in the browser and is accessible to scrappy teams. Music : writing melodies that were contrasted enough to convey different emotions, yet similar enough to create musically-satisfying interpolations. Lots of trial and error with very dissonant AI interpolations between the compositions. Playback : Engineered advanced custom diffing solution to playback exact melody snapshot of user activity and implemented state management system to accurately play back each note character by character. Browser compatibility : Extensive testing and bug resolution for Chrome, Firefox, Safari, MacOS, Windows, and iOS. What's next for Dear Diary Increase dialogue with mental health professionals for maximum emotional benefit and enjoyment for users Increase dialogue community of users who are musically timid, yet curious Increase dialogue with general users for next directions Offer new sound design and melodies Offer journal entry saving and user accounts as well as new sharing integrations Improved visuals using generative AI Areas for future research and technological developments in the community Improved multi-dimensional emotion ranking libraries ImprovRNN often produced results we found not musical Integrate MIDI to Tone.js and Magenta.js Improved documentation to match the quality of the examples Create audio plug-ins for DAWs like Logic and Reaper Contact Stephen Haney – https://twitter.com/sdothaney Suyash Joshi – https://twitter.com/suyashcjoshi Devin Lane – https://twitter.com/gentle_return Acknowledgments Jazz Keys: https://jazzkeys.plan8.co/ Magenta-js: https://github.com/magenta/magenta-js Tone.js: https://tonejs.github.io/ Google Melody Mixer Journal Tree Excellent tutorial on MusicVAE Fantastic tutorial on Magenta-js in general <div