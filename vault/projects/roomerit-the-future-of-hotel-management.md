---
slug: "roomerit-the-future-of-hotel-management"
url: "https://devpost.com/software/roomerit-the-future-of-hotel-management"
title: "Roomerit | The Future of Hotel Management"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 604
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "substrate/structured_db"
---

# Roomerit | The Future of Hotel Management

> Roomerit is a QR-based hotel service platform that helps guests order anything they need from their room, while giving hotels an easy and affordable system to manage services, staff, and branches.

[Devpost](https://devpost.com/software/roomerit-the-future-of-hotel-management) · hackathon [[Frostbyte Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[health_clinical]] [[housing_homeless]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** cach, cloud, emailjs, express.js, nextjs, node.js, postgresql, qr4-qr-code, vercel

## How they structured the write-up

- the inspiration
- the solution
- technical implementation
- challenges faced
- accomplishments that we're proud of
- what's next for roomerit | the future of hotel management

## Body

logo part of system landing page part of system landing page login page login (page sample in dark mood) super Admin selcted hotel to show branch details or the whole hotel hotel summary of data , rooms and orders staff order page staff order page hotel admin summary of orders hotel admin home page hotel admin qr powered room creation with dynamic website created to earch room hotel admin creating users and assigning them rules hotel admin creating services and services item translated with 16v language hotel admin report analysis hotel admin guest page UI customization based on hotel theme's hotel admin home with Arabic translation guest page language selection guest quick order guest page previous orderes The Inspiration Roomerit started from a real problem I noticed in hotels in Makkah, especially during Umrah seasons. Many guests stay for a short time and need services quickly, but most hotels don't have a simple way for guests to order food, request cleaning, or ask for other services directly. In many cases, guests have to call reception or rely on slow communication, and building a full custom hotel ordering system is usually expensive for smaller hotels. The Solution That inspired me to create Roomerit as a subscription-based solution that hotels can use without high development costs. The idea was to make it easy for any hotel to provide a modern QR experience where guests can scan a code from their room, explore available services, place orders, track the status, and even message the hotel for special requests. Technical Implementation I built the project using the MERN stack with Prisma and a SQL database. The system is designed as a multi-tenant SaaS platform, meaning multiple hotels can use the same platform while keeping their data separated. I also implemented a full role-based structure, starting from the super admin who manages the platform, down to hotel admins, branch admins, staff members, and guests. Each hotel can customize its page with its own logo and theme colors, which makes the experience feel unique for every hotel. Challenges Faced One of the biggest challenges was handling permissions across different roles and branches, especially making sure each user can only access what they are allowed to. Another challenge was building a scalable subscription system with Stripe, where pricing depends on hotel size and room count. Deploying the full platform and making it production-ready also taught me a lot about real-world SaaS development. Accomplishments That We're Proud Of Building a fully functional multi-tenant SaaS platform from the ground up that solves a real-world problem. Successfully implementing a complex role-based permission system that ensures data isolation and security across different hotels, branches, and user types. Creating a customizable white-label solution where hotels can maintain their brand identity with their own logos and theme colors. Integrating a flexible subscription model with Stripe that scales based on hotel size and room count. Deploying a production-ready platform that demonstrates complete ownership of the development lifecycle—from database design to frontend dashboards and analytics. What's Next for Roomerit | The Future of Hotel Management The vision for Roomerit extends beyond just service ordering. Future plans include expanding into a comprehensive hotel management ecosystem with features like automated guest communications, predictive analytics for service demand, integration with popular PMS (Property Management Systems), and mobile apps for both guests and staff. We aim to incorporate AI-powered recommendations for personalized guest experiences, expand to multiple languages to serve international pilgrims, and eventually partner with hotels across other pilgrimage cities. The goal is to transform Roomerit into the go-to platform that bridges the gap between traditional hospitality and modern digital convenience. <div