---
slug: "needu"
url: "https://devpost.com/software/needu"
title: "Needu"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 663
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "substrate/code_repository"
  - "substrate/transcript_audio"
---

# Needu

> Safety Feature for the loved ones

[Devpost](https://devpost.com/software/needu) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[disaster_emergency]]
**substrate** [[code_repository]] [[transcript_audio]]

**stack** android, firebase, firebasecloud, flutter, ios, javascript, kiro

## How they structured the write-up

- the story behind needu
- what needu does
- the technical architecture
- the development journey
- what this means
- what's next
- personal reflection

## Body

SOS page Profile Page User Auth Page Phone OTP verification page NeedU — Silent Safety System for the loved ones Hold. Record. Share. A fast, privacy-minded silent SOS for forced abductions and violent situations. Built with Flutter + Firebase. The Story Behind NeedU In moments of extreme danger, every second counts. I've witnessed emergency situations where victims couldn't call for help—their phones taken, their voices silenced, their movements restricted. These heartbreaking realities sparked a burning question: What if there was a way to cry for help without making a sound? That's how NeedU was born—a silent guardian that help in such situations What NeedU Does NeedU is a lightweight silent SOS app designed for the most critical moments. With just a 3-second press-and-hold , it: 🔴 Silently triggers an emergency protocol 🎙️ Records 30 seconds of background audio 📍 Captures your exact location 📱 Alerts up to 3 emergency contacts via SMS 🔒 Works in the background —no need to keep the phone active Built for situations when you can't speak, can't move freely, or can't risk being discovered reaching for help. The Technical Architecture Core Features Built Hold-to-Trigger SOS with animated countdown and visual particles Haptic feedback and confirmation systems for silent operation Background audio recording with iOS & Android optimization Secure chunked uploads to Firebase Storage Multi-platform authentication (Phone OTP, Email/Password, Google Sign-In, Apple Sign-In) Phone verification ensuring SOS alerts reach real emergency contacts Design Philosophy Privacy-first approach : Your data stays secure and encrypted Intuitive design system : AppColors, AppTypography, AppTheme, and SizeConfig Persistent user data : SharedPreferences locally + Firestore cloud backup Lightweight architecture : Fast response times when milliseconds matter The Development Journey Inspiration Every time I heard about someone trapped in a dangerous situation—unable to call for help, their voice silenced by fear or force—I felt a deep responsibility to act. Emergency situations don't wait for perfect conditions. Victims need a way to reach their loved ones even when traditional methods fail. NeedU represents hope in the darkest moments. Building with Kiro This project marked my first experience with Kiro, and it transformed my development workflow. Despite initial debugging challenges with this emerging platform, Kiro's capabilities became clear— it significantly boosted my productivity and helped bring this vision to life faster than traditional development approaches. The learning curve was steep, but the results speak for themselves. Overcoming Challenges Debugging complexity : Working with a new platform meant navigating uncharted territory SMS integration hurdles : Implementing reliable SMS functionality while adhering to carrier protocols Background processing : Ensuring the app works seamlessly even when users can't interact with their device Cross-platform compatibility : Making sure the SOS system works reliably on both iOS and Android The SMS functionality remains our biggest technical challenge—the system is built but not yet sending alerts to emergency contacts. This is our highest priority. What This Means NeedU isn't just an app—it's a lifeline. Every feature was designed with one question in mind: "Will this help someone get home safely?" The Impact Vision Faster emergency response : Alerts sent in under 10 seconds Silent operation : No visible or audible indicators that could escalate danger Location accuracy : Precise GPS data for emergency responders Audio evidence : Critical context for understanding the situation What's Next Immediate Priorities Complete SMS integration —making sure alerts actually reach emergency contacts 2 Wallet Mangement —So that users can view over free tier. Store deployment —getting NeedU into users' hands through app stores User experience refinement —every interaction must be intuitive under stress Code optimization —ensuring rock-solid reliability Long-term Vision NeedU will evolve into a comprehensive safety ecosystem, potentially integrating with emergency services, supporting multiple communication channels, and providing peace of mind to families worldwide. Personal Reflection Building NeedU taught me that meaningful technology requires more than code —it demands empathy, persistence, and an unwavering commitment to user safety. Working with Kiro showed me how emerging tools can accelerate innovation when we're building something that truly matters. <div