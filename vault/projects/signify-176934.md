---
slug: "signify-176934"
url: "https://devpost.com/software/signify-176934"
title: "Signify"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 1037
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Signify

> Where signs speak louder.

[Devpost](https://devpost.com/software/signify-176934) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** django, javascript, mediapipe, openai, opencv, python, pytorch, react-native, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for signify

## Body

GIF Figma Prototype GIF Architecture Persona Value Proposition Figma Screen 1 - Home Figma Screen 2 - Upload Figma Screen 3 - Loading Figma Screen 4 - Generated Text Figma Screen 5 - Edit Page Inspiration We were inspired to create Signify to leverage generative AI in empowering underprivileged people. We wanted to highlight an often-overlooked issue that affects a significant number of people. In today's content creation landscape, we discovered that sign language users encounter far greater challenges in communicating with their audience compared their speaking counterparts. This led us to questions such as, "What makes them different from non-sign language content creators? Is their content limited? Are people interested in sign language content creators because they are different?" We found out that content creators who primarily use sign language struggle to connect with a broader audience, as most people do not understand sign language. This places the burden on the creator to invest more time and effort in making their videos accessible with closed captions. For those unable to do so, their hard work is limited to an audience that understands sign language, significantly restricting their reach. Our goal was to find a solution that enables sign language content creators to operate on an equal footing with their non-sign language counterparts. What it does Signify empowers deaf and sign language content creators by providing a tool to translate Word-Level American Sign Language (WLASL) into text, generating subtitles for their videos. Additionally, it can incorporate personalized speech into the video, enhancing accessibility and engagement for a broader audience. How we built it Our application processes videos to recognize and transcribe sign language into text, which is then enhanced and optionally synthesized into the user's voice. The process begins with dissecting the video into individual frames using OpenCV. Each frame is then analyzed using MediaPipe to detect 21 human hand landmarks, represented as 3-dimensional vectors for each landmark. These vectors are flattened into a one-dimensional array suitable for machine learning models. The flattened landmark vectors are fed into a PyTorch model that predicts the word associated with each frame. After several seconds, the generated string of words is sent to a language model (OpenAI in our case) to enhance the text by adding proper punctuation and refining the overall structure. Optionally, users can synthesize their own voice by recording several voice notes, which help us capture the structure of their voice. Using Tacotron2, a voice synthesizing model, we create a voice file that mimics the user's voice. This synthesized voice, along with subtitles, is then synchronized with the video according to the timestamps from which they were derived. The sign language to text model is built using PyTorch and trained with data we have created for this project. Challenges we ran into One of the main challenges we faced was finding the appropriate dataset for our model. While there are many datasets for American Sign Language (ASL) that use fingerspelling, which means spelling each individual letter to form a sentence, datasets for Word-Level American Sign Language (WLASL) are either non-existent or too complex to incorporate into our project. Many of these datasets contain hundreds of gigabytes of training data, which are inseparable from each other, and pose a physical barrier for our team to train such a model with only laptops and a few weeks. Additionally, we realized that our speech synthesizer model requires a powerful GPU to produce a custom voice within a reasonable time frame. Based on our testing, it took us an hour to generate a fully customized voice from the generated text. As a result, we decided to make use of an existing model, Google’s TTS, to ensure this functionality would still be available for users. Accomplishments that we're proud of We are particularly proud of training our own model capable of detecting Word-Level American Sign Language and converting it into text. Being composed almost entirely of year 1 students, this project has also been our first step into machine learning and AI in practice. Furthermore, the incorporation of many different libraries and tools in the computing world has also trained us in putting them together into a cohesive fullstack project. This accomplishment enables sign language creators to produce content more effectively for their community. Additionally, our integration of personalized speech synthesis enhances the accessibility and appeal of their videos, bridging the gap between sign language users and the broader audience. What we learned We discovered that sign language content creators often don't receive as much audience engagement as their speaking counterparts. They often need to take extra steps to educate their audience about sign language, and their content options are limited. For example, they can't participate in trends involving music, such as dancing or reaction videos, as easily. Additionally, we observed a lack of initiatives for the sign language and disability community in the modern world. This has inspired us to consider future projects that would help people with disabilities enjoy the world in the same way that others do. In regards to the technical aspects of the project, we learned that developing and training our own AI model requires a lot of time and resources. If given the proper hardware and time, we are sure that we would be able to develop a model that can deliver results at faster speeds with even better accuracy. Other than that, we were also shocked to discover that there were so many open source tools out there for anyone willing to create an AI-related project. Many of the tools we used were free and had extensive documentation for beginners. There has never been a better time to start a project. Go wild and explore all the numerous possibilities with all the tools of the internet at your disposal. What's Next for Signify Our goal is to develop a sign language-to-speech model that tailors a unique voice for each user, incorporating facial landmark detection and significant movements to capture emotions. Additionally, we aim to create a real-time converter, enabling sign language users to live stream with spoken English, similar to other streamers. Furthermore, we hope to expand our libraries to include other sign languages to provide this service for more parts of the world. <div