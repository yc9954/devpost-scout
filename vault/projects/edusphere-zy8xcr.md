---
slug: "edusphere-zy8xcr"
url: "https://devpost.com/software/edusphere-zy8xcr"
title: "EduSphere"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 1060
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# EduSphere

> EduSphere: Where learning meets leisure. Elevate education with collaborative hubs, innovative chat features, real-time interaction, and entertainment!

[Devpost](https://devpost.com/software/edusphere-zy8xcr) · hackathon [[HackSwift 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
  <sub>weak: government_staff</sub>
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** clerk, livekit, mapbox, nextjs, openai, postgresql, prisma, rapidapi, shadcn, socket.io, spotifyapi, tailwindcss, uploadthing

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for edusphere

## Body

Chat interface Music player ,Random Jokes and Game Zone Interface In chat Q/A,Next Reply and ChatSummary Interface TODO/Note and live news Interface Summariser and Plagiarism Detector Interface Inspiration In today's rapidly evolving educational landscape, the demand for comprehensive and efficient tools to navigate digital learning environments has never been more pressing. As students and educators grapple with the challenges of collaboration, communication, and academic integrity, there arises a need for innovative solutions that not only address these issues but also optimize time efficiency. EduSphere is born out of this necessity, driven by the vision to revolutionize the way we learn and teach in the digital age. Our platform embodies the spirit of inclusivity, agility, and effectiveness, providing a robust ecosystem where students and educators can thrive. What it does EduSphere is an all-encompassing web application meticulously crafted to meet the diverse needs of students and instructors within educational environments. At its core, the platform revolves around hubs, acting as collaborative spaces where users can form channels based on shared interests or courses. These channels enable users to organize discussions based on specific topics, courses, or interests, ensuring streamlined communication and collaboration. Whether it's a text channel for asynchronous discussions, an audio channel for real-time voice communication, or a video channel for face-to-face interaction, EduSphere provides the flexibility to accommodate various communication needs within a single hub. Within these hubs, users have access to a rich array of features designed to elevate learning experiences and foster active engagement. A standout feature of EduSphere is its robust group chat functionality, enabling seamless communication and idea exchange among users. Beyond typical chat platforms, EduSphere integrates innovative tools like chat summarization and mood analysis, in chat Q/A where users can ask questions based on chat. Furthermore, an integrated language translator ensures inclusivity by breaking down language barriers and facilitating participation in discussions regardless of users' linguistic backgrounds, a next reply suggesting to the user what to reply next in ongoing chat,a feature to explain chat, and a text-to-audio converter in chat. For those seeking real-time interaction, EduSphere offers both group and individual audio/video calling capabilities. Additionally, a map locator feature enhances connectivity by allowing users to pinpoint friends' locations and calculate distances, facilitating convenient meetups and collaborations. In addition to its educational utilities, EduSphere places a strong emphasis on leisure and entertainment. The Entertainment Zone boasts a curated music player and provides live updates on cricket scores, news, quotes, jokes, and weather information, catering to a wide range of interests. Moreover, the game zone offers a refreshing mental break, offering a variety of single and multiplayer games, including educational variants that seamlessly integrate learning and leisure. EduSphere's organization and productivity tools are equally robust. The Management section empowers students to efficiently organize tasks, assignments, and notes, while the code editor facilitates coding practice and assignment submission. Furthermore, a plagiarism checker ensures academic integrity in instructors' evaluations. The platform also features an AI-powered "Ask Anything" feature, enabling users to instantly seek answers to queries. This comprehensive suite of features culminates in a platform that expertly balances learning and leisure, enriching the educational experience for all users. By consolidating various functionalities into one seamless platform, EduSphere not only saves time but also offers a cohesive and efficient user experience. How we built it Frontend Frameworks/Libraries: Next.js: A React-based web framework. Tailwind CSS: A utility-first CSS framework. React Quill: A rich text editor built with React. Zustand: A state management library for React. Shadcn 2.Authentication/Authorization: Check Authentication: Likely referring to an authentication system. 3.API Integration: Hugging Face: Provides NLP models and services. Open AI. RapidAPI: A platform for discovering and connecting to APIs. Spotify API: API for integrating Spotify functionality. 4.Media Handling: MUX: A platform for streaming video. Uploadthing. 5.Real-time Communication: LiveKit: A platform for building real-time video and audio experiences. Socket.io: A library for real-time web applications. 6.Data Handling: Mapbox: Provides mapping and location services. JSDOM: A JavaScript implementation of the DOM and HTML standards. Challenges we ran into Developing an app using Socket.io, a real-time communication library, presents several challenges. Firstly, the complexity of implementing real-time features such as chat or live updates requires a deep understanding of asynchronous programming and event-driven architecture. Scalability is another concern, as the server must efficiently handle increasing numbers of concurrent connections as the user base grows. Ensuring error handling and resilience is crucial to maintain app responsiveness and reliability under adverse conditions like network issues or server crashes. Cross-browser compatibility adds complexity, requiring thorough testing across different browsers to identify and address compatibility issues. Handling state and data synchronization among clients and servers further complicates development, necessitating mechanisms for conflict resolution and data consistency. Finally, testing and debugging in a real-time environment can be challenging due to the asynchronous nature of communication, requiring comprehensive testing strategies to ensure correct functionality under various scenarios. Despite these challenges,with careful planning and teamwork we were able to complete the project on time with all the features we thought to build Accomplishments that we're proud of One of our proudest accomplishments is the seamless integration of real-time communication features using Socket.io. With EduSphere, students and educators can engage in instant messaging, live updates, and notifications, fostering collaboration and enhancing learning experiences. What we learned We learn many new things about nextjs, RapidAPI and many more while building the application. We also learned to work with a team and complete the task in a given time. What's next for EduSphere Expanding EduSphere to include a comprehensive internship/job searching feature is a strategic move to further empower students in their professional journey. With this addition, students can browse and apply for internships, submit short assignments as part of the application process, and even participate in online interviews directly through the platform. This integrated approach streamlines the internship application process, providing students with a centralized platform to manage their career aspirations efficiently. Furthermore, introducing an online learning feature enhances EduSphere value proposition for both students and educators. Educators can upload various courses covering a wide range of subjects and topics, enriching the learning experience for students. The platform's search functionality allows students to discover and enroll in courses tailored to their interests and career goals.. By offering a diverse selection of courses and resources, EduSphere becomes a comprehensive educational ecosystem that supports students throughout their academic and professional journey, promoting continuous learning and growth. <div