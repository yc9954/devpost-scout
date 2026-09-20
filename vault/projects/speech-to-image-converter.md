---
slug: "speech-to-image-converter"
url: "https://devpost.com/software/speech-to-image-converter"
title: "Speech to Image Converter"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 790
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Speech to Image Converter

> See what you speak

[Devpost](https://devpost.com/software/speech-to-image-converter) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[voice_speech]]
**domain** [[education]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[financial_record]] [[video_visual]]

**stack** api, cuda, nvidia, python, pytorch, workbench

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for speech to image converter

## Body

Inspiration I am inspired to participate in this project because of my passion for AI and its potential to transform the way we interact with machines. Working on speech-to-image conversion using Nvidia's AI workbench and APIs allowed me to explore innovative solutions that can enhance accessibility and creativity in various fields, such as art and education. Additionally, it was the best way to get hands-on experience with Nvidia’s cutting-edge technologies, which I believe enhanced my understanding and skills in AI. Hackathons like these also provide an opportunity to collaborate with employees and engineers from Nvidia and tackle real-world challenges, which fueled my drive to contribute to meaningful advancements in technology and get to work with probably the best computer scientists across the globe. What it does This project titled Speech-to-image Converter aims to generate images based on audio/speech as input by leveraging the benefits of Nvidia's AI workbench. The project can be used in various applications such as storytelling. How we built it The Speech-to-Image Converter is an advanced generative AI system that allows users to create real-time images from spoken or audio descriptions. While existing generative AI applications such as speech-to-text and text-to-image converters are well-established, little attention has been given to the direct conversion of speech into images. This project aims to bridge that gap by developing a seamless solution using NVIDIA's AI Workbench to convert audio inputs into visual content. For example, if a user says, Lion in a Jungle in 4K the application transcribes the audio and instantly generates a high-resolution image of a lion in the jungle. This provides an intuitive way to transform verbal ideas into visuals, offering new creative opportunities. To achieve this use case, I made use of two existing AI architectures. One was openAI's whisper to transcribe the audio from the user into text. As part of the 2nd module a stable diffusion model was used through Nvidia's API to convert text into images and thus we get an overall application that converts speech to images. This application was created and tested on Nvidia's AI workbench. Challenges we ran into Faced, with quite a lot of issues, some of the important ones can be described below: ** AI workbench installation failure* : This was the 1st issue I had to encounter and I was unable to complete the installation of the AI workbench, however, I had a debug session with colleagues from Nvidia and we found that the virtualization in the bios mode was disabled and after enabling it, I was able to install the workbench. **Availability of GPUs : As a student getting access to GPUs was difficult. We do have Google Colab that comes with inbuilt GPUs but Nvidia's AI workbench does not work with Google Colab. Additionally, LLMs like stable diffusion need GPU, to overcome this drawback I used Nvidia's inbuilt APIs from Nvidia's API catalog that in the end still makes use of stable diffusion without actually needing a GPU locally. **Huge disk space : A couple of times I encountered issues where the images of my docker were occupying more than 70 GB of my disk space and I was running out of memory, we did not have a fix for it but as a workaround, we tried reinstalling the docker after which this issue was not seen. **Compatibility issues *: I also encountered a lot of compatibility issues when installing certain libraries that were not aligned with the containers on which the libraries were to be installed. Accomplishments that we're proud of 1) This is my first ever hackathon and it is also a challenging hackathon, I'm proud I was able to get a working version of the application by making use of the workbench as described in the problem statement. 2) Did not give up despite many hurdles and happy to have been in contact with brilliant colleagues from Nvidia. What we learned 1) Ask for help when needed. 2) Never give up, your solution might just be around the corner. 3) Hands-on experience with CUDA, GPU and Nvidia workbench. What's next for Speech to Image Converter The following ideas can be thought of for further improvement. 1) Currently we are using Nvidia's API from the catalog to generate an image from text, instead of doing that it would also be nice to train and use a stable diffusion model directly, with this approach we could also generate our images of ourselves. For example "Raghu in space" this would then give an image of me in space. 2) The idea could further be extended for videos, i.e. to generate videos based on audio inputs. 3) We could also try to create our emojis and memes as part of an extension to this project. <div