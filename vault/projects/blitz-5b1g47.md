---
slug: "blitz-5b1g47"
url: "https://devpost.com/software/blitz-5b1g47"
title: "Blitz"
hackathon: "2018 Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 1062
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "user/small_business"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Blitz

> Blitz is an instant business networking app connecting freelancers and creators.

[Devpost](https://devpost.com/software/blitz-5b1g47) · hackathon [[2018 Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]] [[small_business]]
**substrate** [[structured_db]] [[video_visual]]

**stack** expo.io, firebase, javascript, react-native, redux

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what we improved in the last 14 days :)
- what’s next for blitz

## Body

Inspiration As self-employed designers, developers and creators, we are all active in various startup networks, co-working spaces, and events. Although we may have plenty of contacts in our respective industries, getting to know people, especially from different professional backgrounds, is often quite difficult. Events are always a chance game, time-consuming and not on point. We realized that many of us are missing out on interdisciplinary networking, skill-exchange or basic feedback on ideas. As a result, a lot of potentially great projects never happen. When traveling to a new city, freelancers need the opportunity to make the right connections fast, enter new circles, and join industry events and hackathons. We were longing for a simple, time-efficient, skill-based, purpose-driven network that is instant and on point and empowers freelancers to collaborate, help each other out and kick-start projects, across industries, interests, and countries. What it does Blitz is a skill-based, instant business networking app connecting creators from various backgrounds and fields. A Blitz is a shoutout that is active for 24 hours only, like an insta-story. It connects you to freelancers across industries that are close to you, but it can open up relationships all over the world. With Blitz, you can directly build your network with other creators in your area, no matter which city you are in. This is especially powerful when traveling and entering new circles, professional networks and industry events. Sending out a Blitz is simple: All you need to do is select who you want to meet by industry background (Designer / Developer / Product / Business / Marketing / Content), select an intent (Coffee / Skillsharing / Event / Project) and add a short message at the length of a tweet - and your Blitz will appear in the discovery of other creators. Once you reply to the most interesting responses, you have been successfully connected and can start chatting. One important thing: All Blitzes are anonymous - in discovery mode, only user names and avatars will be displayed - the real names, profile pictures, and gender will only be revealed, once users have been matched. Like this, we want to avoid harassment and emphasize a strictly professional and skill-oriented community, with a culture of collaboration in mind. Our vision is to bring together the collective intelligence of thousands of European and international creators and empower them to focus on doing the work they love and perform at their best. How we built it Blitz is a react-native app with a firebase backend. Since we wanted to keep using the create-react-native/expo build tools, we had to jump through some hoops to achieve certain things. Turns out firebase-web-sdk doesn’t work well right now with react-native/expo, so we had to move all database calls to firebase cloud functions. Notifications are handled through expo as well to avoid ejecting the project and lose hot-reloading. All in all, the experience of developing a native app just using javascript was refreshing and less painful than expected. Challenges we ran into The main challenge was creating this app from scratch in 2 months. This included finding a concept, creating the UI/UX, and developing a react-native prototype for Android and iOS simultaneously, including the backend. Another challenge was: Blitz shouldn’t be a dating app, and we want to prevent our users from misusing it as such. While on dating apps, most of decision-making is determined by pictures, we needed to translate the action for networking, while omitting pictures and focussing strictly on the skills of our users. In the absence of visual cues like profile pictures, real names and gender, the styling was tricky and we couldn’t rely on what makes other dating apps successful. Accomplishments we’re proud of Hacking together a React-Native Android/iOS app in 6 weeks without prior knowledge of React-Native. (Max) Coming up with a vision as a team, radically reducing it, executing it within just 8 weeks, testing it and it works! (Lisa) Designing and adapting the user flow and interface in a new environment for Android and iOS (Mathias) What we learned React-Native (Max) / switching from Sketch to Adobe XD & that hacking is quick, dirty and totally different from my usual work with corporate clients (Lisa) / Quickly reacting to concept adaptions, ignoring the urge to make screens pixel perfect and implementing them in our UI/UX design. (Mathias) What we improved in the last 14 days :) We added two important new Features: The new REPORT Feature allows users to report inappropriate content/messages, explicit behavior (such as sexual harassment or abusive language, or making people uncomfortable in other ways), spam/fake profiles and bad offline behavior (during a personal meeting or event). The feature is accessible in Discovery Mode (Feed) / Messages and the Public Profile. Since we are not allowing pictures, before matches have been made, the reporting refers primarily to text. Reporting is an important feature for us at Blitz to ensure professionalism among our users and quality within our app. When inappropriate users are reported by enough people, they will be banned from our app, and no one else will be subjected to their behavior any longer. The new UNMATCH Feature allows users to dissolve matches and will be accessible in Messages, as well as the Profile View. Users can unmatch other users for the same reasons as they can report them (see above), and then the contact and previous messages will disappear. Unmatch is an important feature in order to allow our users to simply change their mind and sort out their contacts, end inappropriate conversations, or if they have simply matched somebody by mistake. Moreover, we have made some visual improvements and did some bug fixing. What’s next for Blitz • Polishing UX/UI • New SHARING Feature – share profile to other users within Blitz and suggest connections / external social shares • Strong Focus on Community: Grow User Base, Community Building • Create a more positive (less aggressive) Brand-Image • User-Centric Approach: Incentives/Rewards to drive User Engagement (Users who help others out) • Inclusiveness: Anonymity Aspect (investigate more anonymity layers, sharing of private information), Implement more Languages, Accessibility features, Light version for emerging markets • User Privacy / Data Handling • User Ratings /Categories of Expertise / Quality Management • Automation Processes • Marketing, Communication, Release Strategy • Start live Beta > Apple Store, Google Play Store • Strategic Partners, Cooperations, Advisors <div