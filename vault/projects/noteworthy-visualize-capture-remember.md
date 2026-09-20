---
slug: "noteworthy-visualize-capture-remember"
url: "https://devpost.com/software/noteworthy-visualize-capture-remember"
title: "Noteworthy: Visualize, Capture, Remember."
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 934
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Noteworthy: Visualize, Capture, Remember.

> AI-powered lecture companion: Transforms speech into real-time visualizations, incorporates notes, and enhances learning with summaries, resources, and chatbot integration—effortless and efficient.

[Devpost](https://devpost.com/software/noteworthy-visualize-capture-remember) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** bash, gemini, html/css, javascript, ngrok, node.js, openai, p5.js, perplexity, playwrightapi, postman, python, react, zoomapi

## How they structured the write-up

- inspiration and what it does 🌟
- what we learned 💡
- how we built it 🛠️
- challenges we faced 🚧
- project impact 🌙
- why it stands out 🎉
- future directions 🔮🔜
- the future of learning starts now 🚀
- try us out! 📱

## Body

AI-Powered Lecture Companion: Redefining the Learning Experience 👩🏻‍💻🌲 Inspiration and What it Does 🌟 We've all been in lectures where the professor quickly sketches a vague diagram, expecting instant understanding, then erases the board while moving onto a completely new topic. Most students struggle to keep up, especially in technical subjects where visualizations are crucial . While we have had many text-to-speech and text-to-image integrations in educational resources, we rarely see speech-to-image transformations . Our team wanted to redefine this learning experience by building an AI-powered lecture companion that dynamically generates real-time visuals based on lectures. This tool also provides students with a comprehensive learning platform where their notes are efficiently stored and organized, as well as allowing students to access summaries, Q&As, chatbots, and other useful resources. What We Learned 💡 Throughout the development process, we discovered several key insights about multimodal communication, efficient information transmission, and integration of AI models: Reading APIs and understanding the unique offerings of each technology to develop innovative applications. Extensive verbal information could be represented with concise illustrations. Vertical integration of AI-based technologies requires a clear formal definition of expected inputs and outputs. Visual Learning Matters as students absorb information faster when concepts are accompanied by meaningful visuals. Personalized Learning Improves Retention as students benefit from a tool adaptive to their pace and note-taking style. Collaboration Enhances Education as the ability to share AI-generated notes and visuals fosters deeper discussions and understanding. How We Built It 🛠️ Our project utilizes cutting-edge AI technologies to create an intelligent, real-time assistive educational application. The development process unfolded through these innovative stages: 🔹Speech-to-Text Processing We engineered a speech recognition system by: Leveraging Zoom's powerful servers to capture and process audio in real-time . Utilizing data generated from Zoom’s WebSocket Technology for text extraction. Crafting a custom JSON-to-text converter that dynamically updates transcripts as lectures progress. 🔹AI-Generated Visuals We created lecture visualizations by: Analyzing speech transcripts to categorize word functions and highlight key concepts. Integrating Large Language Models (LLMs) to transform extracted data into structured visual prompts. Engineering prompts to receive strictly structured outputs redirected into further scripts. Standardizing the style of visual representations of concepts. Interfacing with OpenAI's API to generate P5.js code , enabling real-time sketch creation . Utilized client-server communication to switch between JS and Python. Implementing a dynamic rendering system that evolves visuals as the lecture unfolds. 🔹Intelligent Note-Taking We implemented a versatile digital workspace by: Designing an intuitive interface for seamless image insertion and manipulation. Creating a powerful multi-source merger capable of integrating diverse media types (chatbots, PDFs, etc.). 🔹AI Summaries & Resource Suggestions We enhanced learning opportunity through: Integrating Perplexity AI API to generate comprehensive summaries and power an intelligent Q&A system. Developing a sophisticated resource recommendation engine using Perplexity AI API for curated video, book, and article suggestions. Incorporating Gemini AI API to provide instant, context-aware answers to student queries. 🔹Collaboration, Sharing, and Organized Access We created a collaborative learning environment by: Designing an intelligent storage system that categorizes notes by course, lecture, and date. Seamlessly integrating Zoom's Calendar API to auto-populate the app with students’ calendar data. Developing a versatile note management system allowing anytime access, editing, printing, and sharing. Challenges We Faced 🚧 Building an advanced AI-powered tool in a limited timeframe posed several challenges: Evaluating the capabilities and limitations of each cutting-edge AI model and leveraging sample sets to make a final decision on an image-generation tool. Ensuring Visual Accuracy – Mapping abstract concepts to the right AI-generated diagrams was complex. Real-Time Syncing – Keeping students and professors on the same page without lags. Balancing Automation & Control – Allowing AI to generate content while keeping pace with professors’ lectures. Project Impact 🌙 Education should be accessible, engaging, and tailored to every student’s needs . Our tool: Supports Different Learning Styles – Visual, textual, and interactive elements enhance comprehension. Bridges the Gap for Struggling Students – Helps those who have difficulty keeping up with fast-paced lectures. Promotes Inclusive Learning – Works across devices, even for students without premium note-taking tools. Encourages Deeper Engagement – AI-generated questions and insights stimulate critical thinking, leveraging the best technologies available for student growth. Why It Stands Out 🎉 Our AI-powered lecture companion aligns perfectly with Zoom’s Education Grand Prize criteria : Creativity – A groundbreaking way to transform passive lectures into interactive learning experiences . One of the very few real-time speech-to-image education tools on the market! Technical Complexity – Integrates real-time AI speech processing, APIs, visual generation, chatbot integrations and multi-source syncing . Social Impact – Empowers students worldwide by making education more accessible, personalized, and engaging . It helps all students learn comfortably at their own pace. Future Directions 🔮🔜 Rendering Video and Images on the Same Platform Deploy the app as an extension in platforms like Zoom Apps and Microsoft Apps to seamlessly integrate video and image rendering during lessons and presentations. Utilizing Additional Tools for Diverse Illustration Styles Leverage tools like Mermaid AI to create structured flowcharts and diagrams, while integrating advanced models to visualize more complex topics, enhancing the learning experience. Implementing the React 360 Framework Explore how this platform can fit into a VR space by implementing the React 360 framework , providing a more immersive and interactive learning environment. The Future of Learning Starts Now 🚀 This is just the beginning. Our AI-powered lecture companion redefines how we learn, connect, and grow —ensuring that every student, no matter their learning style or background, has the tools they need to succeed in the classroom and beyond . Try Us Out! 📱 📹 GitHub: https://github.com/arushisharmaa/stanford-tree-hacks- 📹 Youtube Video: https://youtu.be/m_1f7-KvGmQ <div