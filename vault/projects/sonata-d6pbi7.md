---
slug: "sonata-d6pbi7"
url: "https://devpost.com/software/sonata-d6pbi7"
title: "Sonata - Share Music Videos"
hackathon: "Theta Network 2023 Hackathon"
organization: "Theta Labs"
winner: true
words: 758
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Sonata - Share Music Videos

> Music video social platform powered by Theta Video API. Featuring ThetaPass NFT-gated content and subscription capabilities from Square. Follow users, watch their videos. Sonata will empower creators.

[Devpost](https://devpost.com/software/sonata-d6pbi7) · hackathon [[Theta Network 2023 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[legal_professional]]
**substrate** [[financial_record]] [[video_visual]]

**stack** dart, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sonata

## Body

Login screen Video upload screen showing how users can enable ThetaPass NFT content gating, and even Square's Subscription API Showing a user's profile page Live music video in action Live music video in action Invoice that subscribers receive in their email Inspiration Sonata is a music video sharing platform and mobile app that allows creators to share original works with their fans, followers, and subscribers. It uses the Theta Video API to upload and store videos on the decentralized Theta Network. Users can restrict their videos to be shown only to subscribers (powered by Square) or Theta NFT holders. What it does Mobile App Sonata is a mobile app available for iOS and Android. It's still in beta stages, but provides the ability for users to sign up for an account, start following other users, as well as upload video to the Theta Network. There is a public video feed for all trending videos. Users can also decide to only share their own original content with subscribers or particular NFT holders. Theta Video API The Theta Video API provides a fast and perfect solution to host video on the platform that is much cheaper than traditional cloud storage. Watch the demo video to see how easy it is to upload a video from your phone. All video content for Sonata is uploaded and stored using the Theta Video API. NFT Gated Content Users can also specify a Theta NFT ID and when uploading a new video, the "NFT holders only" switch can be enabled that only allows people who are owners of that particular NFT to see the video. This feature uses ThetaPass to force the user to login and verify their ownership of the NFT. Sonata can add utility for NFT creators looking to bring more perks to holders of their collections. Subscription-Only Content The Subscribers-only feature leverages the Square Subscriptions API to allow users to subscribe on a monthly basis to any other user. For demo purposes, the subscription plan created for each user is a $5/month plan. Once subscribed, users can see exclusive content. For demo purposes, the app accepts a Square access token and a location ID, but the quickest way to test it is to leave those fields blank in your profile and use the app's provided credentials. Navigating to a user's profile and tapping on the Subscribe button will trigger multiple Square API calls: Create customer -> Create Subscription Plan -> Create Subscription Once the subscription is created, you will receive an email to pay the $5/mo invoice. The app shows how video creators can monetize their content quickly and easily using the Square Subscriptions API. How we built it Sonata was built using Flutter to simultaneously build a mobile app for iOS and Android platforms. It uses Firebase to store user information and authentication. It uses the Theta Video API to upload content, ThetaPass JS library for proving NFT ownership, and the Square Subscriptions API for creating customers, subscription plans, and tying those customers to created subscriptions. Challenges we ran into The Theta Video API was surprisingly easy to integrate, but The ThetaPass library was difficult to implement because it is only available in JavaScript. I used the ThetaDrop Connect example to work from. I set up a third party server to host this React app and embedded it as a browser view within the app. The user has to manually enter the NFT ID to verify ownership. The React app uses a Firebase library to register ownership (if the user does in fact own the NFT), which allows NFT-holder only video to be watched back on the app. Accomplishments that we're proud of Sonata (beta version) is available NOW for free for all Android devices on Google Play: https://play.google.com/store/apps/details?id=com.contrabandinteractive.sonata We are currently working on getting the beta live on the Apple App Store. We can provide TestFlight access to any judge who wants to try it out. The iOS version of the app is working and ready for testing, but we must pass Apple's certification process to distribute the app on the App Store. What we learned I learned a lot about the Theta ecosystem. I also learned a lot about Square's developer offerings that seem to get better every year. What's next for Sonata I see a niche in the social media market for an app such as this that caters to musicians and independent music creators to share their works. I'd like to see how big this app can grow after I spend more time on refinements. <div