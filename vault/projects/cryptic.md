---
slug: "cryptic"
url: "https://devpost.com/software/cryptic"
title: "Cryptic"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 361
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "substrate/video_visual"
---

# Cryptic

> Secure your images. One click. One lock. One Cryptic.

[Devpost](https://devpost.com/software/cryptic) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[privacy_tech]]
**substrate** [[video_visual]]

**stack** blob, bolt, css, encryption/decryption, html5, modern-ui-**javascript-(vanilla-js)**-?-core-logic-for-ui, typescript, vite

## How they structured the write-up

- 🚀 inspiration
- 🔐 what it does
- 🛠️ how we built it
- 🧱 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for cryptic

## Body

🚀 Inspiration With growing concerns about digital privacy and the unauthorized use of personal media, we wanted to create a simple yet secure way for anyone to encrypt and share their images safely. Cryptic was born from the idea of empowering users with client-side encryption in a fast, accessible, and user-friendly way—no servers, no signups, just secure image sharing. 🔐 What it does Cryptic lets users encrypt their images directly in the browser, converting them into .cryptic files that can only be decrypted through the app. The platform supports multiple image formats, drag-and-drop upload, batch processing, and optional password protection. Users can then decrypt these files when needed, ensuring privacy and control over their visual content. 🛠️ How we built it We used: HTML5, CSS3, and JavaScript for a responsive and interactive front end AES-256 encryption for secure client-side encryption and decryption Drag-and-drop APIs and FileReader for seamless uploads Custom JavaScript logic for file validation, encryption, decryption, and download functionality Basic image preview and progress indicators to improve UX 🧱 Challenges we ran into Implementing AES-256 encryption without relying on external libraries was tricky, especially ensuring consistency between encryption and decryption. Managing batch processing while keeping the UI responsive was challenging with larger files. Developing the project from single prompt Dealing with file size limits and maintaining performance on slower machines. 🏆 Accomplishments that we're proud of Achieved secure encryption entirely in-browser , without uploading to any server. Created a clean and intuitive interface that works seamlessly on both desktop and mobile. Implemented support for multiple file types and batch processing with clear feedback and error handling. Embedded a real sense of data ownership and privacy for users. 📚 What we learned The depth and complexity of implementing secure cryptographic systems on the front-end. How to improve user experience through subtle feedback mechanisms like progress bars and file previews. The importance of balancing security, performance, and usability in privacy-focused tools. 🔮 What's next for Cryptic Add cloud storage integration with end-to-end encryption Implement QR-based file sharing or encrypted download links Include image compression before encryption to reduce file size Build a mobile-first PWA version for offline encryption on the go <div