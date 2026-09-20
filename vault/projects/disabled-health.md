---
slug: "disabled-health"
url: "https://devpost.com/software/disabled-health"
title: "Disabled Health"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 842
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/scientific_research"
  - "user/social_worker"
  - "substrate/video_visual"
---

# Disabled Health

> Providing tech accessibility and health information for the disabled.

[Devpost](https://devpost.com/software/disabled-health) · hackathon [[Funathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[accessibility]] [[scientific_research]]
**user** [[social_worker]]
**substrate** [[video_visual]]

**stack** cvzone, gtts, nltk, opencv, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for disabled health

## Body

Disabled Health Logo Inspiration The prevalence of injury amongst disabled children is over four times as likely as that of a child without disabilities. Over half of the injuries dealt to disabled children occur at home, and around half of those injuries are caused by falling. These alarming statistics inspired me to create this app. AI technologies such as Siri don’t have readily available medical information; thus, it becomes incredibly hard to treat damages done at home, especially when the injury happens unexpectedly. 62% of adults with disabilities say that they own a computer, while 81% of adults without disabilities say that they own a computer. This gap comes from the fact that it is incredibly hard to use computers if you are disabled, even with the new technology to help aid this problem. I wanted to create this app so that disabled people can help treat their injuries faster and have an easier time navigating technology. What it does Disabled Health has 4 main uses. The first one is a health assistant, which is the app's focus. It provides on-the-go medical information which you can access. The second part is a voice assistant, which was mainly added so that you can entirely rely on Disabled Health, instead of relying on other sources such as Siri or Google Home. The third is a virtual keyboard, where you can type using a window on your computer, by simply putting your index and middle finger together in front of a webcam. The fourth is a virtual mouse, where you can move your cursor using a window on your computer. You can move your mouse using your pointer finger and click by moving your thumb out. Both the virtual keyboard and the virtual mouse work outside of the application, and thus it has real-world usage. The health assistant uses an intents.json file to read data and then uses the module NLTK to stem the words inputted, and then the application utilizes a neural network and machine learning algorithms to convert your inputted string to a probability of it being a specific tag which is read in the intents.json file. If the probability is high enough, it returns an answer to your question. The voice assistant is almost the same, except it uses deep speech to understand what you are saying, and then converts it to a string. The virtual mouse and keyboard both use media pipe and OpenCV to scan the webcam for the indexes of your fingers (photo provided in the demo video), and, for the mouse, upscales the camera intake and uses the pointer finger's top index as the center of the cursor. Overall, Disabled Health uses AI, machine learning, deep speech, and neural networks to function. How we built it I built this application using PyCharm, and lots of youtube videos learning about deep speech. Challenges we ran into Package control was by far the largest technical difficulty I faced when programming "Disabled Health." To put it in perspective, specific module versions were incompatible with other modules, which would in turn destroy the code. Many of the modules I used had a plethora of issues in their newest release, and thus, the documentation and the skills I received from working with these modules were useless as I had to relearn another version of that module for the app to work. Modules such as PyAudio were not even possible to install on my system, and thus I had to find the original wheel file to install it. Overall, finding the right package versions, testing out my program and its runtime on these versions, and then implementing new code into these versions was a huge problem. Something would always break along the way until I found the perfect balance of package versions within my app. Accomplishments that we're proud of I am so proud of this app, how far we have come while making it, and hopefully, the lasting impact that it will create. I have also submitted this application to the congressional app challenge and hopefully will win that along with this hackathon. What we learned We learned machine learning, AI, and deep learning through modules such as NLTK, tensorflow, and gTTS. What's next for Disabled Health I would love to implement Tkinter for a GUI. Although my app is user-friendly, I could make it much more user-friendly if I had a nicer GUI with more vibrant colors and an easier-to-use run process. I have been working on a research paper for NLTK and Tensorflow compilation algorithms based on the intent.json file size for epochs, and have come across the fact that the process is entirely linear for normal file sizes; thus, I would love to implement this into my GUI by creating settings to change the amount of data in the intents.json file just by the click of a button to make the process dynamic. TKinter offers a lot of GUI functionality for Python, and I am also looking into creating a flask application or a django application for Disabled Health. <div