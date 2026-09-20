---
slug: "skibidi-yamdjw"
url: "https://devpost.com/software/skibidi-yamdjw"
title: "My Skibidi Girlfriend Simulator"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 899
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# My Skibidi Girlfriend Simulator

> My Skibidi Girlfriend Simulator is an interactive experience where you brainrot with a CS major virtual girlfriend. Have conversations and meet the love of your life, now with #kawaii music <3

[Devpost](https://devpost.com/software/skibidi-yamdjw) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css, express.js, google-cloud, html, javascript, node.js, openai, python

## How they structured the write-up

- inspiration meme boom
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skibidi girlfriend simulator
- tracks we're submitting to:

## Body

This project was created by two girls named Grace. Inspiration meme boom The Skibidi Girlfriend Simulator was inspired by the growing interest in AI-driven virtual companions and interactive experiences. With advancements in voice recognition and conversational AI, we wanted to explore how users could engage in natural conversations with a virtual character. This project aimed to provide a fun, immersive experience while utilizing modern AI technologies like GPT-3 and Google's Speech-to-Text and Text-to-Speech APIs. The idea of creating a digital "girlfriend" that responds to voice commands and provides personalized interactions sparked our creativity to incorporate code with something visual, and that drove the project forward. meme boom What it does The Skibidi Girlfriend Simulator allows users to interact with a virtual girlfriend. Users can chat with the simulation by entering text into the chat box. The text is then sent to OpenAI's GPT-3, which generates a skibidi-fied response. The simulator creates an interactive and dynamic conversation where the virtual girlfriend responds in real time, simulating a natural text conversation. There's also #kawaii #uwu BGM. Unfortunately, we were unable to get the text-to-speech integrated in the allotted time but we do have scripts for transcribing speech and turning text to audio. How we built it The project is composed of both a frontend and a backend that work together to create a seamless experience: Frontend (HTML, CSS, JavaScript): A visually engaging interface with a pink theme and interactive elements, including a microphone for voice input. The background image and a transparent "girlfriend" GIF were placed on the screen to make the experience more immersive. JavaScript was used to manage the microphone recording, send audio data to the backend, and handle playback of the AI-generated responses. Backend (Node.js with Express, Python): The backend handles several tasks, including receiving audio files, transcribing them into text using the Speech-to-Text API, sending that text to GPT-3 for generating a response, and then converting that response into audio with the Text-to-Speech API. The server was set up to communicate with Google Cloud services and OpenAI's GPT-3 API. APIs Used: Google Speech-to-Text API: To convert the user’s spoken input into text. OpenAI GPT-3: To generate human-like responses based on the transcribed text. Google Text-to-Speech API: To turn the generated text responses into audio for playback. The main character art/gifs were completely hand-drawn by Grace Jin! Challenges we ran into Browser Compatibility: One of the main challenges was ensuring the audio playback worked for all browsers. API Integration: Integrating and configuring multiple APIs was difficult! 3. Real-Time Interaction: Creating smooth and realistic real-time interaction between the user and the virtual girlfriend was tricky. Ensuring that responses were timely, contextually relevant, and dynamic posed several design challenges. Accomplishments that we're proud of Successfully integrated multiple technologies to create a working interactive system. Overcame challenges related to CORS and server issues, and OS and browser compatibility to ensure the application was usable across devices. Developed an immersive user interface with visually appealing elements, such as a pink theme, a transparent GIF of the "girlfriend," and smooth interaction transitions. What we learned We had a great time creating and building this project! Here are some of our many takeaways from this weekend: API Integration: We gained a deep understanding of integrating various APIs, including how to use Google Cloud's services (Speech-to-Text and Text-to-Speech) and how to work with OpenAI's GPT-3 API. Cross-Browser Functionality: Handling microphone access and ensuring compatibility with various browsers taught us the importance of testing and debugging cross-browser functionality. User Experience Design: We learned how to create an interactive and visually appealing experience while balancing design with functionality. Real-Time Processing: Managing real-time processing of audio data, sending it to the backend, processing the data, and delivering an immediate response was a valuable experience in asynchronous programming. What's next for Skibidi Girlfriend Simulator The project has a lot of potential for further development: Speech Recognition: Since we were unable to get the speech-to-text and text-to-speech working, that is our next priority. We want to give users the option to have actual conversations. Expanded Conversation Options: We aim to expand the virtual girlfriend’s dialogue to cover more diverse and engaging conversation topics. Fine-tuning the responses from GPT-3 could also help enhance the naturalness of the interactions. Emotion Recognition: Adding a layer of emotion recognition to interpret the user’s tone or sentiment could make the conversations feel even more personalized. We created versions of the gif to reflect the girlfriend's emotions, and have yet to add them into the gameplay. Additional Features: We plan to integrate more interactive features, such as dynamic responses based on user input, changing backgrounds, and even more advanced AI behaviors for the virtual girlfriend. The goal is to continue evolving the Skibidi Girlfriend Simulator into a more sophisticated and engaging virtual companion for users, combining the power of AI with interactive technology. We'd also love to create more partner options and increase the levels of brainrot. Tracks We're Submitting To: best overall yay :3 (or worst project 🤷‍♀️) (IJAG) I’m Just A Girl (we are just two girls) UX/UI most kawaii (WBUOT) would blow up on tiktok (WPPOIL) would piss people off on linkedin i’m just a chill guy i laughed. (new hackers prize) (we have both been to less than five hackathons) most iq points lost build a tool that distracts you when ur trying to be productive (TPIA) this project is awesome <div