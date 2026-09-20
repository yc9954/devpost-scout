---
slug: "condensis"
url: "https://devpost.com/software/condensis"
title: "Condensis"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1161
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# Condensis

> Condensis offers AI-generated notes to students who struggle with note-taking, helping promote accessible education. Our multimodal language model can synthesize notes from any lecture video.

[Devpost](https://devpost.com/software/condensis) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[education]] [[finance_payments]]
  <sub>weak: labor_employment</sub>
**user** [[educator_student]]
**substrate** [[transcript_audio]]
  <sub>weak: sensor_telemetry, structured_db, video_visual, web_dom</sub>

**stack** chatgpt, checkbook.io, figma, google-cloud, google-text-to-speech, gpt-3, openai, opencv, python, react, retool, whisper

## Body

List of lecture notes Home page List of courses Lecture 3 notes About page Checkbook.io API in use Slide detection graph Finding a problem Education policy and infrastructure tend to neglect students with accessibility issues. They are oftentimes left on the backburner while funding and resources go into research and strengthening the existing curriculum. Thousands of college students struggle with taking notes in class due to various learning disabilities that make it difficult to process information quickly or write down information in real time. Over the past decade, Offices of Accessible Education (OAE) have been trying to help support these students by hiring student note-takers and increasing ASL translators in classes, but OAE is constrained by limited funding and low interest from students to become notetakers. This problem has been particularly relevant for our TreeHacks group. In the past year, we have become notetakers for our friends because there are not enough OAE notetakers in class. Being note writers gave us insight into what notes are valuable for those who are incredibly bright and capable but struggle to write. This manual process where we take notes for our friends has helped us become closer as friends, but it also reveals a systemic issue of accessible notes for all. Coming into this weekend, we knew note taking was an especially interesting space. GPT3 had also been on our mind as we had recently heard from our neurodivergent friends about how it helped them think about concepts from different perspectives and break down complicated topics. Failure and revision Our initial idea was to turn videos into transcripts and feed these transcripts into GPT-3 to create the lecture notes. This idea did not work out because we quickly learned the transcript for a 60-90 minute video was too large to feed into GPT-3. Instead, we decided to incorporate slide data to segment the video and use slide changes to organize the notes into distinct topics. Our overall idea had three parts: extract timestamps the transcript should be split at by detecting slide changes in the video, transcribe the text for each video segment, and pass in each segment of text into a gpt3 model, fine-tuned with prompt engineering and examples of good notes. We ran into challenges every step of the way as we worked with new technologies and dealt with the beast of multi-gigabyte video files. Our main challenge was identifying slide transitions in a video so we could segment the video based on these slide transitions (which signified shifts in topics). We initially started with heuristics-based approaches to identify pixel shifts. We did this by iterating through frames using OpenCV and computing metrics such as the logarithmic sum of the bitwise XORs between images. This approach resulted in several false positives because the compressed video quality was not high enough to distinguish shifts in a few words on the slide. Instead, we trained a neural network using PyTorch on both pairs of frames across slide boundaries and pairs from within the same slide. Our neural net was able to segment videos based on individual slides, giving structure and organization to an unwieldy video file. The final result of this preprocessing step is an array of timestamps where slides change. Next, this array was used to segment the audio input, which we did using Google Cloud’s Speech to Text API. This was initially challenging as we did not have experience with cloud-based services like Google Cloud and struggled to set up the various authentication tokens and permissions. We also ran into the issue of the videos taking a very long time, which we fixed by splitting the video into smaller clips and then implementing multithreading approaches to run the speech to text processes in parallel. New discoveries Our greatest discoveries lay in the fine-tuning of our multimodal model. We implemented a variety of prompt engineering techniques to coax our generative language model into producing the type of notes we wanted from it. In order to overcome the limited context size of the GPT-3 model we utilized, we iteratively fed chunks of the video transcript into the OpenAI API at once. We also employed both positive and negative prompt training to incentivize our model to produce output similar to our desired notes in the output latent space. We were careful to manage the external context provided to the model to allow it to focus on the right topics while avoiding extraneous tangents that would be incorrect. Finally, we sternly warned the model to follow our instructions, which did wonders for its obedience. These challenges and solutions seem seamless, but our team was on the brink of not finishing many times throughout Saturday. The worst was around 10 PM. I distinctly remember my eyes slowly closing, a series of crumpled papers scattered nearby the trash can. Each of us was drowning in new frameworks and technologies. We began to question, how could a group of students, barely out of intro-level computer science, think to improve education. The rest of the hour went in a haze until we rallied around a text from a friend who sent us some amazing CS notes we had written for them. Their heartfelt words of encouragement about how our notes had helped them get through the quarter gave us the energy to persevere and finish this project. Learning about ourselves We found ourselves, after a good amount of pizza and a bit of caffeine, diving back into documentation for react, google text to speech, and docker. For hours, our eyes grew heavy, but their luster never faded. More troubles arose. There were problems implementing a payment system and never-ending CSS challenges. Ultimately, our love of exploring technologies we were unfamiliar with helped fuel our inner passion. We knew we wanted to integrate Checkbook.io’s unique payments tool, and though we found their API well architectured, we struggled to connect to it from our edge-compute centric application. Checkbook’s documentation was incredibly helpful, however, and we were able to adapt the code that they had written for a NodeJS server-side backend into our browser runtime to avoid needing to spin up an entirely separate finance service. We are thankful to Checkbook.io for the support their team gave us during the event! Finally, at 7 AM, we connected the backend of our website with the fine-tuned gpt3 model. I clicked on CS106B and was greeted with an array of lectures to choose from. After choosing last week’s lecture, a clean set of notes were exported in LaTeX, perfect for me to refer to when working on the PSET later today! We jumped off of the couches we had been sitting on for the last twelve hours and cheered. A phrase bounced inside my mouth like a rubber ball, “I did it!” Product features Real time video to notes upload Multithreaded video upload framework Database of lecture notes for popular classes Neural network to organize video into slide segments Multithreaded video to transcript pipeline <div