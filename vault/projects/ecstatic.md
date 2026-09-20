---
slug: "ecstatic"
url: "https://devpost.com/software/ecstatic"
title: "Ecstatic"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 1053
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Ecstatic

> analyze and enhance your videos, practice presentations and get exact reviews, and much more!

[Devpost](https://devpost.com/software/ecstatic) · hackathon [[AWS Graviton Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]]
**substrate** [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** amazon-ec2, flask, graviton, ibm-watson, moviepy, natural-language-processing, opencv

## How they structured the write-up

- inspiration
- what it does
- the ux workflow
- how we built it
- how filters work
- how confidence tracker works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ecstatic

## Body

welcome screen select from options enhance feature's home screen [upload video] video processing final results Analyse feature's homescreen analyse feature's result ec2 instance dashboard Inspiration Videos are a very important part of life, even more in this totally digitalized world. People capture moments, for fun and entertainment, and for many of us, its either partially or totally related to work. Also, since the world has seen a really new level of digital revolution in each and every field, people are more dependent on technology than ever, which in fact, is actually good! We wanted to help out people who'd want to do nice things with the videos they capture, or maybe the people who are into public speaking and are tryna to transition into the digital mode, literally anyone we feel, because everyone's a creator in some way or the other! We were very fascinated when we imagined if there could be a way to enhance video qualities, because generally its the other way round. Downgrading something is easier than enhancing it. Moreover, we never really could find anything that would rate your presentations and speeches based on technical grounds, and if there is something, the features are really scattered and not-to-the-point. Also we were intrigued by the processor capabilities of graviton based EC2 instances, so we wanted to try something that would be heavy on the processor and see for ourselves if its efficient enough. These were the inspirations we had! What it does Ecstatic lets you do a lot. For the major part, its subdivided into two main sections:- Enhance Videos It lets user upload their video, probably a low quality one so that ecstatic can enhance them, and then the work starts to happen behind the scene. The audio is extracted first, and then the video is broken down frame-by-frame. And then through the help of python libraries like MoviePy and OpenCV, each and every frame is enhanced using filters such as median blur, gaussian blur. Then at last, the frames are joined again and the audio is added as well and the output file is ready to be downloaded by the user! Once the final video is ready, the script performs a cleanup and deleted all the files taken from user! Analyze Speeches/Presentations In this section, user just need to start recording [they should give mic and camera access to the browser] and then they can continue the speech or presentation like a rehearsal. Ecstatic would then perform various things, including- Speech to text, which in turn performs grammar check and tells the score. Vocabulary index, which analyses how good was users vocabulary and usage of words. Confidence, if the user seemed confident enough while delivering their content. Tone analyser, using the audio extracted. Pace of speech, by dividing the total words spoken by total time taken. The UX workflow How we built it As the basic framework for our app, we used python's flask library. The webpages are made and designed using HTML5 and CSS3 To enhance videos, we used OpenCV that breaks it down into frames. To extract the audio and apply filter to frames, we used MoviePy library and the same was used to join frames as well as to add back the audio. To analyse speeches, we used Javascript's speech recognition to get the transcript, facemesh library to check face's position to calculate confidence score, grammar checker to check grammar and give score based on mistakes. The whole flask application is deployed on graviton based EC2 instances. How filters work Let's take gamma color correction filter into consideration:- It follows this one formula where the non-negative real input value Vm is raised to the power gamma and multiplied by the constant A to get the output value Vout. In the common case of A = 1, inputs and outputs are typically in the range 0–1. How Confidence Tracker works So, we looked into basic symptoms for lack of confidence while giving a public speak. We found out that people become specifically more shaky or just so still when they're nervous in front of public. So we defined parameter based on that. The app used ml15 facemesh and makes a facemesh out of the person's face, then it looks up into the face movement, a subtle periodic movement determines confidence and hence is given the maximum confidence points. On the other hand, if the face movement is way too much, or is way too less, thats a determining factor for low confidence index. if(moveCount*165/count >90){ final = (90-moveCount/count); } else{ final = raw + 5; } Challenges we ran into We ran into many kinds of challenges. One major challenge was that half of our team was totally new to flask and python, and none of our teammates were familiar with EC2 instances. So deploying it was of course challenging. Also, getting everything to work properly and efficiently was indeed challenging. We faced some minor issues throughout as well, like finding right filters to enhance frames, making the app responsive for all screen sizes, letting JavaScript interact with python variables, making the grammar check work as it was requiring java dependencies on runtime, deriving acceptable algorithms to determine the confidence parameters, and a few more! Accomplishments that we're proud of We're proud of what we were able to achieve throughout this whole hackathon. We made something that's pretty much helpful and works well without making any false promises. We are also happy that we were successfully able to deploy it on graviton based EC2 instances provided by AWS. What we learned The whole hackathon was a learning quest, we must say, we learned a load of things, including- deploying on EC2 Recognizing the powers of graviton, Using flask efficiently, Recognizing the powers of OpenCV library, Editing videos [for our demo video part], debugging and working with teammates efficiently, writing good code and using good git practices. What's next for ecstatic We would love to add more features to ecstatic, such as letting user upload pre recorded video for analysis, enhance live video in real time, increasing the accuracy, identifying the kind of filter needed to enhance the images in advance, and more! We would also like to market it a bit to let people know and try it out and in turn get their feedback! <div