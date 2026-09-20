---
slug: "karo-trj4av"
url: "https://devpost.com/software/karo-trj4av"
title: "Karo: Social Task Manager"
hackathon: "RevenueCat Ship-a-ton"
organization: "RevenueCat"
winner: true
words: 720
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
---

# Karo: Social Task Manager

> Delegate tasks to anyone from your contacts. We get it to them if they aren't on the app (via WhatsApp/Messages) and like a great assistant, the app follows up and reminds them to complete the tasks!

[Devpost](https://devpost.com/software/karo-trj4av) · hackathon [[RevenueCat Ship-a-ton]]

## Facets

**domain** [[disaster_emergency]]

**stack** ai, amazon-ec2, amazon-web-services, core-data, golang, postgresql, revenuecat, s3, swift, swiftui, twilio, uikit, whatsapp, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for karo

## Body

Social task manager - delegate tasks and let Karo make sure it reaches them and they are reminded. We let you know when its completed! Delegate tasks to anyone, add deadlines, assets and more! Collaborate with groups. Similar to how messaging apps create groups. No friction and effortless! Not on Karo? We will send them the task to them on WhatsApp or by text and make sure they are reminded to complete it. Inspiration My mom & wife send tasks over iMessage/WhatsApp. These tasks get lost with the other conversations that take place around it. Either they forget what they have delegated, or the receiver forgets what was assigned to them. Everytime we would try to use a shared task manager, it ended up failing. They were either complicated or technical. That’s why Karo came about—the first social task manager letting you assign tasks to anyone in your contacts, form groups, and collaborate effortlessly with all familiar interactions people have learnt from the messaging apps they use everyday! What it does Send tasks to anyone in your contacts! A task manager disguised as a chat-like app to make task delegation people centric. The person assigned the task doesn't even need the app to complete it. We send the tasks to people not on the app by WhatsApp or by text. Karo also takes up the role of a great assistant, reminding the assigned user to complete the task and notifies the sender about the actions taken on the tasks! How we built it In technical terms: iOS UIKit SwiftUI RevenueCat Backend GoLang Hosted on AWS (EC2, S3) Twilio for SMS WhatsApp Business Design Figma Challenges we ran into We struggled initially to find the balance between clearly being a task app while keep the experience of a chat/messaging app. Our early beta would just look like a chat app and users used it incorrectly and after a long of tweaking - we are really glad people now use it like an actual task manager without getting confused. This is the first of its kind app that makes tasks delegation people centric instead of traditional group like collaboration. This was really challenging and glad we finally got it right! The next major challenge was getting SMS services to work because of US laws compliances and getting approval from Meta to use the WhatsApp business API. Accomplishments that we're proud of Completing the feedback loop! Our users love this. When you delegate a task and the moment they complete it and check off the task, they're notified. We can't tell who loves it more - the person checking off the task or the person getting notified about their delegated task being completed!!! Shipping the bare minimum the app needed in order to start succeeding. We probably planned for 5 to 7 more features before we thought we'd launch, but stripping out anything that wasn't important for the v1 was a great decision. Adopting the blinkist paywall design - this is just so good and can't wait to experiment more on this Making it to the App Store iOS 18 feature lists Organically getting featured on TechCrunch, 9to5Mac, MacRumors and AppAdvice to name a few! What we learned Ship the earliest possible version of your app to users to test as soon as possible to avoid making biased and incorrect decisions! Do not keep adding one more thing you need for a perfect launch. If your launch is perfect and flooded with features, you launched too late. Twilio is expensive! To overcome this, we moved more of the load on WhatsApp and SMS as a fallback for countries where users would What's next for Karo We want Karo to be the way friends and families delegate tasks to one another so the entire process becomes extremely efficient while keeping it fun and gamified! Alongside that businesses that use messaging apps as a way to function would find it a no-brainer to adopt Karo! Apart from that we have the roadmap planned for the next 2 months. September: Paywall experiments Free Trials vs Paid upfront intro offer App Clips Android app Recurring reminders Accessibility support October: Email login support Prepare for holiday season Offers + Paywalls Templates & themes Marketing heavily on socials (only organic for now) Apple Watch support Mac app support <div