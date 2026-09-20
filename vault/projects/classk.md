---
slug: "classk"
url: "https://devpost.com/software/classk"
title: "Classk"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 462
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
---

# Classk

> Classk is a mission-based platform where students help each other, earn points for completed missions, and compete on leaderboards within their major, turning collaboration into a game.

[Devpost](https://devpost.com/software/classk) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
  <sub>weak: developer_tools</sub>
**user** [[educator_student]]
  <sub>weak: structured_db, web_dom</sub>

**stack** css, flask, flask-login, flask-sqlalchemy, flask-wtf, html, javascript, jinja, python, sqlalchemy, sqlite, werkzeug

## Body

Classk Logo Inspiration Classk was created to solve a common problem: campus life can feel disconnected. Students lose items, need help, want study partners, and organize events—but everything is spread across different platforms. We wanted a single place where students could collaborate easily and enjoyably. Inspired by gamified systems like Duolingo and Stack Overflow, we asked: What if helping people on campus felt as engaging as leveling up in a game? That idea shaped a mission-based platform that turns everyday student needs into rewarding challenges. Organizing students by major adds community structure without limiting cross-campus collaboration. What It Does Classk gamifies student collaboration through missions. Students can create, accept, and complete missions in categories like Help, Lost & Found, Study Groups, and Events. Completing missions grants points (20–60 depending on category and difficulty), and every 100 points increases the user’s level. Leaderboards show top contributors by group, category, and total points. Event missions include ratings and comments, and each user has a profile displaying their stats, levels, and mission history. Admins can moderate missions, adjust points, and review group-level analytics. How We Built It We began with the database design around users, missions, groups, and ratings. Using Flask with blueprints and the factory pattern, we organized the backend into clear modules. SQLAlchemy handled relationships and optimized queries, which became essential as the platform scaled. On the frontend, we built a custom design system featuring glassmorphism and smooth animations. One of the most challenging components was our fully custom dropdown, built with vanilla JavaScript to handle animations, dynamic initialization, and proper stacking without relying on native elements. Point balancing was refined through testing to keep progression rewarding. The admin dashboard was developed last to maintain design consistency and provide moderation tools. Challenges We faced SQLAlchemy N+1 query issues, cross-browser UI inconsistencies (especially with backdrop-filter ), secure file upload handling, and dynamic field initialization timing. We also improved mission visibility logic so users can explore both group-specific and campus-wide missions. What’s Next Upcoming improvements include CSRF protection, password reset functionality, mission notifications, full-text search, WebSocket-based real-time updates, a badge system, mobile apps, and integrations with campus systems. We also plan to introduce sponsor partnerships and campus collaborations . At the end of each month, the top users in each mission category will receive real rewards—such as free products, gift bundles, or multi-month subscriptions provided by sponsors. On-campus, students will be able to redeem their points for food, event tickets, or other student services , creating a real-world connection between helping others and earning tangible benefits. AI Tools Disclosure We used ChatGPT during ideation, debugging, and refining code structure, and Cursor as an AI-assisted coding tool to speed up development. All core features, logic, and design decisions were fully reviewed and implemented by us. <div