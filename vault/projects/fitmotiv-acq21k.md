---
slug: "fitmotiv-acq21k"
url: "https://devpost.com/software/fitmotiv-acq21k"
title: "Fitmotiv"
hackathon: "Hack the North 2020++"
winner: true
words: 948
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Fitmotiv

> Synchronized fitness app that motivates you to be more active and build deeper connections with your friends.

[Devpost](https://devpost.com/software/fitmotiv-acq21k) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[mental_health]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** azure, cockroachdb, google-cloud, ibm-cloud, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fitmotiv

## Body

App Screens Home, Analytics, Leaderboard Workouts, Invites, Live Video Call, Summary Inspiration Two challenges that arose as a result of COVID-19 are social isolation and decreased physical activity. Today, 1 in 4 Canadians live alone and long term loneliness can lead to an increased risk of depression, stress, insomnia and even heart disease. With lockdowns in place and loss of motivation, COVID-19 has resulted in a drastic decrease in physical activity on a global level. At the same time, we're also losing connection with our friends and other people we would have met frequently. What it does Studies have shown that exercising together leads to higher motivation, better performance and decreased stress. Fitmotiv is a mobile application that connects people by working out together virtually. Product Features: Preset Workouts - Is today leg day? Or perhaps you want those washboard abs. Fitmotiv comes with preset workouts tailored to your fitness needs. Guided Workouts - Exercise in sync without fumbling with your phone. Fitmotiv automatically displays each exercise with a timer so that you can focus on sweating. Invite Friends - Invite up to three friends to motivate and hold each other accountable. Leadership Board - Compete with friends for the longest workout streak. Personal Dashboard - Review key fitness metrics to see how you’re doing. Voice Commands - During your workout, simply talk to the app and it will perform a function for you. “Mute”, “Pause Workout”, “Turn Off Video” and many more. During rest times, the users can chat with each other and reconnect with their friends for spontaneous conversations! How we built it Our app is mostly built for the IOS platform using Swift, while a part of our app is its own microservice, built using Node/Express JS, hosted on Heroku. Within the app, we integrated Vonage API for collaborative workout sessions via video call, Azure Cognitive Speech Services for hands off voice control (muting mic, turning off video) and IBM NLU API to detect the emotions throughout the workout sessions. We also used Google Cloud to where we implemented authentication and Machine Learning. We also experimented with Pose estimation with Tensorflow, however, due to time constraints we decided to leave it off for now. Challenges we ran into In terms of technical challenges, it took a huge amount of time to integrate audio streams from Azure Speech Services to work with IBM NLU while handling any errors gracefully so as to not invoke voice commands incorrectly. Developing the Swift app was challenging as well since only one team member had access to the Xcode IDE. Most of the APIs we worked with were for the first time and it took us some time to understand their documentation and implementation methods. However, with the help of mentors and sponsors, we were able to implement everything we planned to. Accomplishments that we're proud of It was a huge challenge to be working remotely but despite the roadblocks we are really proud of finishing our MVP adhering to a great UI/UX design, conducting live workout sessions between friends and integrating 4 unique APIs into our implementation. This was an important problem that we all deeply cared about. The pandemic in general has caused a lot of instability in our lives and it's impacting us negatively in terms of our physical wellness and mental health. We hope Fitmotiv encourages more people to exercise more often and at the same time reconnect with your friends. Ultimately, leading to a happier and healthier you! What we learned Hemant - As a novice frontend developer, I learned more advanced HTML/CSS to be able to customize the vonage video calling UI to fit our needs. I also dove deep into Azure Cloud for the first time. Sai - As the mobile developer, I built the iOS app and integrated the various APIs we needed. It was my first time using some of these API’s and it was interesting to see how different products can be combined to build out an impactful project. Swarup - As a full-stack developer for the project, I learned about the various APIs and tools like Vonage and Azure, and the great many features on these APIs. I also learned about some more in-depth concepts related to Express. Winnie - As the UX/UI designer, I learned that it is important to constantly get feedback to iterate on the design. We uncovered a lot of opportunities for improvement from speaking to mentors and conducting usability testing with representative users. What's next for Fitmotiv We built the minimum viable product during this 36 hour hackathon. There are several additional features that we would like to pursue next. For example, we would like to add the functionality to work out with people outside of your friend’s list and create the opportunity to make new connections. This would allow us to bring more people together and help foster connections with interesting people around the world. Another example is we would like to build a feature that can detect movement and count the number of times you complete an exercise which is the Pose Estimation. This could be used as an interesting feature in which users can challenge each other to achieve the highest number of push ups in 60 seconds or hold the longest plank or any other exercise. We would also like to flesh out the IBM NLU API integration, adding features to dynamically adjust workout plans based on detected user sentiment patterns. Imagine yourself with Fitmotiv: No more sedentary lifestyle. Look at that 92 Days Workout Streak! Best Shape of Your Life, regardless of Quarantine/Social Distancing. Deeper Connections with Friends. Workouts are Finally Enjoyable! Overall, a Happier and Healthier you. <div