---
slug: "fork-on-the-road"
url: "https://devpost.com/software/fork-on-the-road"
title: "Fork On The Road"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 665
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Fork On The Road

> Try "Alexa, ask Fork On The Road" and the fork will help you make a decision. Alexa Skill that uses dynamic 3D.

[Devpost](https://devpost.com/software/fork-on-the-road) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**mechanism** [[runtime_tool_creation]]
**domain** [[developer_tools]] [[supply_logistics]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** alexa, api-gateway, apl, chrome, javascript, lambda, node.js, puppeteer, s3, three.js, unity

## How they structured the write-up

- "alexa, ask fork on the road"
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for fork on the road
- demo video

## Body

Adding Food Choices Picked Pizza Adding Things To Do Picked Movies Landing Alexa Skill Icon "Alexa, ask Fork On The Road" Review on Amazon Geek out on GitHub Inspiration A friend of mine told me about the Amazon Multimodal Contest, #AmazonAlexaMultimodalChallenge, and I thought I'd take a stab at making my first Alexa Skill. While researching the Amazon Presentation Language I looked for inspiration in my daily life to guide my direction. One evening, my family and I were trying to decide on what movie we would watch. This sparked the idea of a fun and interactive decision maker. Thus was born, "Fork On The Road". What it does The skill is invoked with "Alexa, ask Fork On The Road". Users are asked to add up to four things for the fork to choose from. Users can also remove items they've added. While users are adding things, an animation of the fork bounces in the intersection of two roads. A full 3D scene is used to present items in a fun and unique way, with items placed as dynamic 3D extruded text. When there as at least 2 items the user can "Spin the Fork". When the fork is choosing, it bounces up and spins around, slowly stopping on the path it would like you to take. A final screen presents the forks decision using another dynamic 3D scene. This skill works responsively across all Alexa products ranging from speech-only to TV. "Your destiny awaits. Enjoy!" How I built it This project was created using several different technologies. It primarily uses open-source and Amazon platforms. The key technology is Amazon's APL. The APL is designed using several layers of APL Components, including APL Video, that are sequenced with SendEvent Commands and Document Directives. Document transforms, game logic and speech response is managed using the ASK SDK for Node.js running on Lamba. Skill configuration for invocations, utterances, intents, lambda, etc, are maintained and deployed through a Skill Manifest and the ASK CLI. Resources and Assets come from two different sources. Static files are hosted on S3 with a Cloudfront instance on top. Dynamic assets, like the dynamically generated 3D scene, are requested from a Lambda service with API Gateway routing requests. This dynamic asset service uses a Headless Chrome Node API called Puppeteer to load a website, take a screen capture, and send it back to the Alexa device with a "image/png" header. The captured website uses Three.js to dynamically construct a scene based on the variables in the request and composes elements such as extruded text. Animations were also scripted in Three.js and then captured, cropped and embedded in the APL. The 3D scene was first composed in Unity to get the look and feel correct and then exported. Finally, the fork's sound effect was composed in Sony Acid Pro using a couple of layered sounds and exported to the appropriate MP3 specs using Audacity. Enlarge Image Enlarge Image Challenges I ran into The Amazon APL is off to a great start but the games visual sequences will most likely be easier to accomplish once there are more APL Commands and Component options. Accomplishments that I'm proud of I really enjoyed figuring out the dynamic asset service as this opened up a slew of opportunities for unique visual experiences. This type of feature can be used in many different ways to provide a composited image to provide visual data. For instance, the Size or Atmosphere graphs in Amazon's Sample Space Explorer Skill. What I learned Lots! In the past I've done very light research into Alexa Skills but this was a full-blown exercise to see how far I could push the APL's user-perceived visual interface. What's next for Fork On The Road The big item on my list is the ability to change the 3D environments to things like a winter wonderland or desert scene. Ideally this would be done with a menu system that uses the TouchWrapper Component. Demo Video Watch it here <div