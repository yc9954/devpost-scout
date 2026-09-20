---
slug: "teachxr"
url: "https://devpost.com/software/teachxr"
title: "TeachXR"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 1042
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# TeachXR

> World's First AI Study Assistant in Extended Reality

[Devpost](https://devpost.com/software/teachxr) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[agriculture_food]] [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** cartesia, deepgram, gemini, javascript, mediapipe, ocr, react, singlestore, tailwind, vapi, xr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for teachxr

## Body

Home Page Sample use cases Inspiration Across the globe, a critical shortage of qualified teachers poses a significant challenge to education. The average student-to-teacher ratio in primary schools worldwide stands at an alarming 23:1! In some regions of Africa, this ratio skyrockets to an astonishing 40:1 . Research 1 and Research 2 As populations continue to explode, the demand for quality education has never been higher, yet the supply of capable teachers is dwindling . This results in students receiving neither the attention nor the personalized support they desperately need from their educators. Moreover, a staggering 20% of students experience social anxiety when seeking help from their teachers. This anxiety can severely hinder their educational performance and overall learning experience. Research 3 While many educational platforms leverage generative AI to offer personalized support, we envision something even more revolutionary. Introducing TeachXR—a fully voiced, interactive, and hyper-personalized AI teacher that allows students to engage just like they would with a real educator, all within the immersive realm of extended reality. Imagine a world where every student has access to a dedicated tutor who can cater to their unique learning styles and needs. With TeachXR, we can transform education, making personalized learning accessible to all. Join us on this journey to revolutionize education and bridge the gap in teacher shortages! What it does Introducing TeachVR: Your Interactive XR Study Assistant TeachVR is not just a simple voice-activated Q&A AI; it’s a fully interactive extended reality study assistant designed to enhance your learning experience. Here’s what it can do: Intuitive Interaction : Use natural hand gestures to circle the part of a textbook page that confuses you. Focused Questions : Ask specific questions about the selected text for summaries, explanations, or elaborations. Human-like Engagement : Interact with TeachVR just like you would with a real person, enjoying milliseconds response times and a human voice powered by Vapi.ai . Multimodal Learning : Visualize the concepts you’re asking about, aiding in deeper understanding. Personalized and Private : All interactions are tailored to your unique learning style and remain completely confidential. How to Ask Questions: Circle the Text : Point your finger and circle the paragraph you want to inquire about. OK Gesture : Use the OK gesture to crop the image and submit your question. TeachVR's Capabilities: Summarization : Gain a clear understanding of the paragraph's meaning. TeachVR captures both book pages to provide context. Examples : Receive relevant examples related to the paragraph. Visualization : When applicable, TeachVR can present a visual representation of the concepts discussed. Unlimited Queries : Feel free to ask anything! If it’s something your teacher can answer, TeachVR can too! Interactive and Dynamic: TeachVR operates just like a human. You can even interrupt the AI if you feel it’s not addressing your needs effectively! How we built it TeachXR: A Technological Innovation in Education TeachXR is the culmination of advanced technologies, built on a microservice architecture. Each component focuses on delivering essential functionalities: 1. Gesture Detection and Image Cropping We have developed and fine-tuned a hand gesture detection system that reliably identifies gestures for cropping based on MediaPipe gesture detection . Additionally, we created a custom bounding box cropping algorithm to ensure that the desired paragraphs are accurately cropped by users for further Q&A. 2. OCR (Word Detection) Utilizing Google AI OCR service , we efficiently detect words within the cropped paragraphs, ensuring speed, accuracy, and stability. Given our priority on latency—especially when simulating interactions like pointing at a book—this approach aligns perfectly with our objectives. 3. Real-time Data Orchestration Our goal is to replicate the natural interaction between a student and a teacher as closely as possible. As mentioned, latency is critical. To facilitate the transfer of image and text data, as well as real-time streaming from the OCR service to the voiced assistant, we built a robust data flow system using the SingleStore database . Its powerful real-time data processing and lightning-fast queries enable us to achieve sub-1-second cropping and assistant understanding for prompt question-and-answer interactions. 4. Voiced Assistant To ensure a natural interaction between students and TeachXR, we leverage Vapi , a natural voice interaction orchestration service that enhances our feature development. By using DeepGram for transcription, Google Gemini 1.5 flash model as the AI “brain,” and Cartesia for a natural voice, we provide a unique and interactive experience with your virtual teacher—all within TeachXR. Challenges we ran into Challenges in Developing TeachXR Building the architecture to keep the user-cropped image in sync with the chat on the frontend posed a significant challenge. Due to the limitations of the Meta Quest 3 , we had to run local gesture detection directly on the headset and stream the detected image to another microservice hosted in the cloud. This required us to carefully adjust the size and details of the images while deploying a hybrid model of microservices. Ultimately, we successfully navigated these challenges. Another difficulty was tuning our voiced assistant. The venue we were working in was quite loud, making background noise inevitable. We had to fine-tune several settings to ensure our assistant provided a smooth and natural interaction experience. Accomplishments that we're proud of Achievements We are proud to present a complete and functional MVP! The cropped image and all related processes occur in under 1 second , significantly enhancing the natural interaction between the student and TeachVR . What we learned Developing a Great AI Application We successfully transformed a solid idea into reality by utilizing the right tools and technologies. There are many excellent pre-built solutions available, such as Vapi , which has been invaluable in helping us implement a voice interface. It provides a user-friendly and intuitive experience, complete with numerous settings and plug-and-play options for transcription, models, and voice solutions. What's next for TeachXR We’re excited to think of the future of TeachXR holds even greater innovations! we’ll be considering* adaptive learning algorithms * that tailor content in real-time based on each student’s progress and engagement. Additionally, we will work on integrating multi-language support to ensure that students from diverse backgrounds can benefit from personalized education. With these enhancements, TeachXR will not only bridge the teacher shortage gap but also empower every student to thrive, no matter where they are in the world! <div