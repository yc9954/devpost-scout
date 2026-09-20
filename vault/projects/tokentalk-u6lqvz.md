---
slug: "tokentalk-u6lqvz"
url: "https://devpost.com/software/tokentalk-u6lqvz"
title: "TokenTalk"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 904
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TokenTalk

> Anonymous chat system

[Devpost](https://devpost.com/software/tokentalk-u6lqvz) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: developer_tools</sub>
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** anonymous, authentication, css3, firebase, firebase-(firestore, firebase-hosting, hosting), html5, imgbb-api, javascript-(es6+), lucide, tailwind-css

## Body

here is a preview of my project Inspiration In a digital world where our conversations are saved and stored forever, we were inspired to create a space for communication that is truly private and temporary. We wanted to build the opposite of apps like WhatsApp or Discord; we wanted to create a "digital secret note" that self-destructs. The core inspiration for TokenTalk was to build a chat application where you can have a quick, secure, and private conversation that leaves no trace. What it does TokenTalk is a full-featured, ephemeral web-based chat application. Here's what it does: Creates Ephemeral Chat Rooms: Users can instantly create either a 1-to-1 Direct Message or a Group Chat. Sets Time Limits: Every room has a mandatory timer (from 5 minutes to 24 hours). When the timer expires, the room, all its messages, and all its files are permanently deleted. Uses Secure Access Codes: Rooms are private and only accessible via a unique, 4-character random code. Full Chat Features: It's a modern chat app with real-time features like: Message Unsend, Edit, and Reply: Users have full control over their messages. File & Image Sharing: Users can share images and files. Auto-Deleting Files: All uploaded files are automatically scheduled for deletion from the hosting service when the chat room expires, ensuring complete privacy. Real-time Indicators: Shows "user is typing..." and "user has joined/left" notifications. Group Admin System: The creator of a group is the admin and can kick members. If the admin tries to leave, they are forced to assign a new admin to keep the group going. How we built it We built TokenTalk with a "vanilla-first" approach, focusing on a lightweight app without heavy frameworks. Frontend: The entire application is built with HTML5, CSS3, and modern Vanilla JavaScript (ES6+ Modules). We used Tailwind CSS (via CDN) for the UI, Lucide Icons for the icons, and a lightweight emoji-picker library. Backend (BaaS): We used Firebase as the "engine" for the entire app. Firestore: Provides the real-time, NoSQL database for all messages and room data (timers, member lists, admin status). Firebase Anonymous Authentication: Cleverly gives each user a unique, temporary ID without them needing to sign up or log in. Firebase Hosting: We used this to deploy the final, live website to the world. File Storage (API): To keep the project 100% free and private, we used the imgbb API. Our code uploads files directly to their service and, most importantly, uses its API to set an automatic expiration date on the file that matches the chat room's timer. Challenges we ran into We faced several significant challenges that taught us a lot: Finding a 100% Free File Storage: This was our biggest hurdle. Firebase Storage required upgrading to a paid plan. We pivoted to Cloudinary, which was complex, and finally settled on imgbb, which perfectly met our three requirements: it was free, had a simple API, and supported auto-deletion of files. Managing Complex State in Vanilla JS: Building features like message replies, admin-transfer logic, and real-time typing indicators without a framework like React is very challenging. We had to design a robust global state object and use Firestore's onSnapshot listeners to keep everything in sync without bugs. The Dark/Light Theme "Flicker": Our theme toggle caused a "flash of light mode" when the page loaded. We solved this by implementing an industry-standard fix: adding a tiny, blocking script to the HTML that runs before the page renders to apply the correct theme instantly. Deployment & Caching: After deploying new versions, we couldn't see our changes. This forced us to learn about and debug firebase.json configurations and the importance of browser caching (and how to bypass it with a hard refresh). Accomplishments that we're proud of True Ephemerality: Our proudest feature. Not only are the chat messages deleted, but all uploaded files are also automatically deleted by the imgbb API after the chat expires. This delivers on our core promise of total privacy. Building a Feature-Rich App with Zero Frameworks: We are incredibly proud of building a complex, real-time application with message replies, editing, and file sharing using only Vanilla JavaScript. It proves the power of modern web fundamentals. A Complete Admin System: We successfully designed and implemented a robust admin system for groups, including kicking members and safely transferring the admin role, which required careful database logic. What we learned This project was a massive learning experience. We learned how to fully leverage Backend-as-a-Service (BaaS) platforms like Firebase to handle tasks (real-time chat, auth, hosting) that would normally require a custom server. We learned how to read documentation and integrate third-party APIs (like imgbb) to solve specific problems. We learned how to manage a complex application state in Vanilla JS, a skill often hidden by modern frameworks. We learned the entire deployment pipeline, from firebase init to debugging live production issues like browser caching and domain setup with Cloudflare. What's next for TokenTalk We have a clear roadmap for TokenTalk's future: Freemium Model: We plan to add a "TokenTalk Pro" subscription (using Stripe or Razorpay) that allows for longer chat durations, larger member limits, and password-protected rooms. Custom Backend: Our ultimate goal is to migrate from Firebase to our own custom backend using Python (FastAPI and WebSockets). This will give us 100% control over the data and allow for even greater privacy and more advanced features. Native Mobile Apps: We would love to expand TokenTalk to iOS and Android. <div