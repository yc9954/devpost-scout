---
slug: "foodsense-enwz2m"
url: "https://devpost.com/software/foodsense-enwz2m"
title: "Food Sense - Meal Journal"
hackathon: "RevenueCat Ship-a-ton"
organization: "RevenueCat"
winner: true
words: 839
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# Food Sense - Meal Journal

> Food Sense is a meal journal that tracks what you eat and how you feel. Discover which foods trigger symptoms, and easily log, analyze, and share data with your dietician.

[Devpost](https://devpost.com/software/foodsense-enwz2m) · hackathon [[RevenueCat Ship-a-ton]]

## Facets

**domain** [[health_clinical]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** firebase, pdfkit, revenuecat, swift, swiftcharts, swiftdata, swiftui

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for food sense - meal journal

## Body

Inspiration About eight years ago, I began noticing that certain foods made me feel uncomfortable. I read a book by Novak Djokovic , where he described experiencing similar issues after meals. He started analyzing what he ate and how he felt afterward, and based on his observations, he changed his diet. This dietary change significantly improved his performance, which was incredibly inspiring for me, both as an individual and as a tennis player myself. I decided to do the same for myself, noting down each food I ate and how I felt afterward. Through these notes, I discovered that creamy pastas made me feel bad, so I stopped eating them. Last year, I consulted a dietician about my diet. During the consultation, I logged what I ate, when I ate, and how I felt at the end of the day, then sent her a weekly report as a PDF. It was hard to track what I ate throughout the day. Should I note it on my laptop, tablet, or phone? I started logging on my tablet using handwriting, but when I sent it, it seemed complicated. Next time, I typed it using a keyboard, but that took time. I realized I could use an app like this, so I built one. What It Does With this iOS app, users can log what they eat and how they feel. They can track their feelings at different points, such as while eating and a few hours later. Users can track their eating habits, identify foods that trigger symptoms, and export their logs as a PDF to share with a healthcare professional or dietician. How I Built It I used SwiftUI as the UI framework for this project, SwiftData for local data storage, and Firebase for Google Analytics to track user demographics and interactions. I used Swift Charts to visually display metrics, PDFKit to export data as PDFs, RevenueCat to manage in-app subscriptions and RevenueCat Paywalls to remotely configure paywall view. Challenges I Ran Into I used new technologies for this project, which came with a learning curve. The most frustrating challenge, however, was dealing with iOS 18-related bugs during the Shipaton. Accomplishments That I Am Proud Of I work full-time, so I had to work on this project after my shifts for Shipaton. I’ve always wanted to create this app myself, and releasing it in almost a month felt amazing. I’m proud of myself for sticking with it, even though there were days when I took a break to rest and recharge. I realized that it's normal not to work at full capacity every day, and sharing both the productive moments and the times when I needed rest helped keep me grounded. What mattered most was focusing on progress over perfection and managing my time effectively. Sharing my journey daily on X (Twitter) kept me accountable, and even though there were moments when I almost lost hope, I stayed the course. That’s what I’m most proud of 🙌. What I Learned Besides the new technologies I mentioned, like PDFKit, SwiftData, and SwiftCharts, I also learned how my motivation works. By consistently doing something every day, even if it's just a small task, I can stay motivated. Through this project, I realized the importance of testing future releases of iOS versions such as iOS 18 beta and fixing issues as needed. This was also my first time sharing my progress while building in public, and it turned out to be far less stressful than I feared. Instead of receiving harsh criticism, people offered constructive feedback and have been supportive from day one. Even when I struggled to decide on navigation for some screens, they provided guidance, which was a valuable learning experience for me. What's Next for Food Sense - Meal Journal I definitely want to integrate AI into the app to help users better understand their bodies. For example, the app might suggest, “You feel bloated after meals that contain dairy. You may be sensitive to lactose.” This would be incredibly useful for both myself and others. Additionally, I plan to introduce more visually appealing charts and analyses, and allow users to log other symptoms, like allergies, so they can better understand their reactions. To make the data even more meaningful, I want to access menstrual cycle data from Apple Health. Hormonal changes during the menstrual cycle can affect appetite and cause symptoms, making it important to consider in tracking food and feelings. To make logging easier, I’m also planning to add default meal names, so users won’t have to type everything after each meal. Moreover, I plan to add reminder notifications to prompt users to log their meals. I’m also considering adding a screen with helpful resources and guides for those following specific diets, like FODMAP, gluten-free, or lactose-free. To enhance the user experience, I want to incorporate more animations into the interface, making the app more engaging and interactive. I hope this app will help users better understand their bodies and encourage them to make positive lifestyle changes. <div