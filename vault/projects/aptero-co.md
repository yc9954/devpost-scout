---
slug: "aptero-co"
url: "https://devpost.com/software/aptero-co"
title: "Aptero"
hackathon: "2019 Developer Circles from Facebook Community Challenge"
organization: "Facebook"
winner: true
words: 773
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/geospatial"
---

# Aptero

> Enterprise Collaboration and Call in Virtual Reality. With interactive VR spaces, we increase productivity in meetings with powerful interactive features (brainstorm, sketch, mind-maps, etc..)

[Devpost](https://devpost.com/software/aptero-co) · hackathon [[2019 Developer Circles from Facebook Community Challenge]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** javascript, oculus, react360, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aptero.co

## Body

Aptero, the whole story - Updated after being regional winners! https://www.aptero.co Inspiration When we saw the Oculus Go and Quest: cable free and completely portable VR hardware coming out, we instantly believed this was the future. In our previous workplaces, we were wasting everyday incredible amount of time to setup meetings and making sure everyone could join. We had remote colleagues dropping off, and often everyone was multitasking during meetings. VR can bring endless possibilities in the business world. That's why by combining the convenience of online meetings with the interactivity of face-to-face meetings, we can create virtual workspaces where you can collaborate, create and feel truly together with colleagues. Having won the regional part of this hackathon we benchmarked and learned about other solutions being made similar to our product, and we got inspired to create a company! We're focusing on new features that other existing solutions do not have yet. We already made some partnership with few other companies and are signing up our first beta clients to test our solution! What it does With Aptero, you'll have access to powerful meetings in interactive VR spaces, enabling remotely to review products and 3D models, brainstorm, sketch, mind-map, prototype and have team-building activities. The portable and easy to use oculus quest now allow anyone using Aptero to join a VR meeting from wherever you are, in the train, plane or just your office desk. With our new update v1.0.6 we now allow you to: Sticky notes that can be moved and written on Have a powerful speech to recognition notes !! Awesome feature that listen and recognise your speech, and automatically write your speech on your notes. No more need for VR keyboards. More than 120 languages possible on our speech recognition A whiteboard to discuss your drawings The ability to choose 3 different scenes: -- Conference room in the nature: perfect for teambuilding and big groups -- Penthouse office > perfect for business meetings -- Free space > perfect to stay focus on 3D Models you want to review (uploading a 3D model feature is coming soon) And much more :D How we built it We've built Aptero VR meetings using WEBRtc library to manage the sound and direct connection in order to create optimal chat rooms. We then used React360 for the front end, that connects to a nodeJS backend server managing and generating meeting rooms. The prototype is available on meeting.funnychain.co Every time users go into https://meeting.aptero.co , they create a new VR meeting room that can be shared to have an interactive VR space! Challenges we ran into The main challenge in building this prototype was keeping the application working in realtime with no lag or delay. We have tried a lot of different designs to keep the FPS high and to keep the audio streams stable. We also redesigned and customised our entire 3D scene in order to optimise it for the web (Originally the scene was 50mb and we striped it to a few mb). Our new environment scene takes only 2 MB and allows any device from any internet connection to join our meeting room and participate wherever they are. We believe connectivity and fluidity is very important for meetings. Accomplishments that we're proud of We are proud of the 3D paint feature developed in ApteroVR. This was very challenging and we ended up using an Octree design to implement this feature. Moreover, with our demo made for developer circles from Facebook, we've already have 2 potential clients eager to user our solution. We are very happy that some companies found our project interesting think that this product has a lot of potential. We are really proud to have developed this an application in such a short time. What we learned We learned how to modelize 3D models and also learned the utility of having a separate service worker in react360 to improve the performance. We also learned how to optimize a 3D application for the web. But in the second part of this hackathon we also learned how to improve these modelization, adapt it to the Oculus Quest and React360. We also learned the separate service worker in react360 to improve the performance. We also learned to optimize 3D applications for the web. What's next for Aptero.co The next technical big step for aptero.co is to add more features for meeting like screen sharing, file sharing and 3D model importation. Also, the next big step, business wise, is signing the next potential clients and we hope to get some firms to sign up as beta testers! Built With: javascript, oculus, react360, typescript, sketchup <div