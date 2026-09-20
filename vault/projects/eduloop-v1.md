---
slug: "eduloop-v1"
url: "https://devpost.com/software/eduloop-v1"
title: "Eduloop v1"
hackathon: "United Hacks V5"
organization: "Hack United"
winner: true
words: 848
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Eduloop v1

> Eduloop is an offline communication, resource sharing and club-advertisement intranet for schools that cannot afford to supply all its students with internet access.

[Devpost](https://devpost.com/software/eduloop-v1) · hackathon [[United Hacks V5]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css, express.js, html, javascript, multer, node.js, socket.io

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eduloop v1

## Body

messaging demo basic UI Selecting username for that session when a task is added, the icon shows a little red exclamation mark to show that there is work due. task management file sharing image sharing Inspiration I’ve always had a strong passion for learning, so much so that a few years ago I called my country’s Ministry of Education to try to suggest improvements! Though that initiative was shut down, it sparked a deeper desire in me to help fix issues in the education system. When I started learning Computer Science and networking in A-Level, I saw an opportunity to do something practical: build a tool that could actually help improve communication and student life in my school and beyond my school. That’s how Eduloop was born - a solution to real problems I see daily. What it does Eduloop v1 is a local, offline, web-based communication and task management platform for students. It features: Real-time group chat rooms (e.g. General, Announcements, Club Promo, Memes) File sharing with support for images and documents A built-in Task Tracker for students to manage assignments and due dates A sidebar for switching channels and a responsive layout for easier use on different devices It works entirely over a local network, so even students without mobile data or internet access can still participate if they're connected to school network. To access it students connect to the local area network and type in the IP address of the server in their browsers How we built it I started with a basic Node.js + Socket.IO chat tutorial to set up client-server communication. From there, I: Created a custom chat interface in HTML/CSS Built separate chatrooms using socket.io’s join() and leave() logic Added a username system so students know who sent what Implemented file uploads using Express and Multer (for things like photos, PDFs, etc.) Designed and built a Task Tracker using JavaScript DOM manipulation Tweaked the UI to look clean and usable for school environments (kept it in dark mode too) All of this was done using the iterative method of program development, while learning more about networking and web development along the way. Challenges we ran into Honestly, every single stage of development was a challenge. Even setting up the package.json was difficult. This is my first full stack project using Javascript, HTML and Css. I have to admit, the process took a lot out of me, especially since I'm in the middle of exams. I leveraged AI, a lot of documentation and my brain. But most specifically the biggest challenges were: File handling (which used a whole other tutorial): I had to learn how to store uploaded files safely on the server and serve them via URL — not something I had done before. Syncing features across chatrooms: Making sure features like the Task Tracker didn’t interfere with the chat logic across rooms required careful DOM and event management. I had to create a new rule in windows defender that allowed node.js to send and receive information for the device over the network. I also discovered that phone hotspots have a feature that allows devices to connect to it but not commincate with eachother. Accomplishments that we're proud of I'm proud of the fact that I dared to follow through with this project. I built a functioning, usable real-time, scalable chat app with file sharing and tasks from the bottom up with only AI and documentation to guide me. I learned server-side JavaScript and backend routing without prior experience. (and that's saying a lot) What we learned I've learned that in this day and age, you're not going to be hand-writing every function or iteration, instead to speed development time leverage the tools that you have such as AI, not as a complete cruch but as a helper. (If you don't know what your code does then there's something wrong). Furthermore, how socket.io rooms work, and how to build local real-time applications. How to use multer for file uploads and express.static() for serving content Better HTML/CSS layout and responsive design strategies That building a useful product requires constant testing and iteration and that it’s okay to break things and fix them! What's next for Eduloop v1 I have big plans that at first include small aspects such as: Adding notifications for when files or homework is shared. Improving my media queries to improve compatabilty. Save tasks and chats in a persistent database such as SQlite Let only teachers post assignments or announcements in designated channels Add AI tools to summarize chatrooms or help students manage tasks better or help with homework Furthermore to scale the project, I want to add file compression on media being sent. I believe that Eduloop could really help people all over my country, Zimababwe. In rural areas, I would like to have the server preloaded with resources that student parents can access, as only they usually have phones. Then similar to how an sms can be sent to mulitple devices, I want to use that sam elogic to sync and update all eduloop servers country wide! <div