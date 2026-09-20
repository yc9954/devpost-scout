---
slug: "digispotter"
url: "https://devpost.com/software/digispotter"
title: "DigiSpotter"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 446
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DigiSpotter

> Your new electronic gym partner, who remembers what set you're on unlike your real one and uses state-of-the-art Computer Vision to correct your form.

[Devpost](https://devpost.com/software/digispotter) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[structured_db]] [[video_visual]]

**stack** arkit, firebase, ios, swift, swiftui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for digispotter

## Body

logo workout selection screen tracking in action Inspiration The inspiration for DigiSpotter came from within our team members, who recently started going to the gym in the past year. We agreed that starting out in the gym is hard without having a personal coach or gym partner that is willing to train you. DigiSpotter aims to solve this issue by being your electronic gym partner that can keep track of your workout and check on your form in real time to ensure you are training safely and optimally. What it does DigiSpotter uses your phone's camera to create a skeletal model of yourself as you are performing an exercise and will compare it across various parameters to the optimal form. If you are doing something wrong DigiSpotter will let you know after each set. It can detect errors such as suboptimal range of motion, incorrect extension, and incorrect positioning of body parts. It also counts for you as you are working out, and will automatically start a rest timer after each set. All you have to do is leave your phone in front of you as if you are taking a video of yourself working out. The results of your workout are saved to your account in the app's database to track improvements in mobility and general gym progress. How we built it We created this app using Swift for the backend and SwiftUI for the frontend. We are using ARKit for iPhone to help us create our position tracking model for various positions in the body as running natively drastically increases the performance of the app and the accuracy of the tracking. Using our position tracking model, we can calculate the relative angles of body parts and determine their deviation from an optimal angle. Challenges we ran into ARKit is designed more for creating virtual avatars from motion capture data and not interpreting movement between relative body parts, and such in order to create a skeleton that fits our needs we needed to make many changes from any other tracking library. Accomplishments that we're proud of We are able to calculate deviation from an optimal squat and relay the information to the user. What we learned All of us were completely new to developing for iOS so we had many challenges attempting to figure out the conventions of Swift and how we can interact with our app. What's next for DigiSpotter We would like to add as many exercises as we can to the App and we want to further expand how much historical data we can collect so our users can have a more detailed view of how they have improved over time. <div