---
slug: "good-samaritan-29zp5x"
url: "https://devpost.com/software/good-samaritan-29zp5x"
title: "Good Samaritan - Vision Pro Assisted First-Aid Care"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 781
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/health_clinical"
  - "user/frontline_worker"
---

# Good Samaritan - Vision Pro Assisted First-Aid Care

> Allowing bystanders to provide informed first-aid care to those experiencing medical emergencies with the assistance of mixed reality (looking years in advance when the tech is commonplace).

[Devpost](https://devpost.com/software/good-samaritan-29zp5x) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[disaster_emergency]] [[education]] [[health_clinical]]
**user** [[frontline_worker]]

**stack** applevisionpro, mediapipe, opencv, python, realitydeepcomposer, swiftui, terraapi

## How they structured the write-up

- the problem:
- the solution:
- what we are proud of, and how we built it:
- business model:
- the team (4 people, 4 schools represented):
- next steps:
- challenges we ran into:
- what we learned:

## Body

The Problem: Inspired by our teammates' lack of knowledge in first aid administration, we address a gap in emergency medical response time for remote and underserviced locations. Currently, it takes 7 minutes for emergency medical services (EMS) to reach the scene, with the time in rural areas doubling to 14 minutes. For critical medical emergencies, such as cardiac arrest, every minute the chances of survival decrease by 10% making immediate intervention necessary. This is where the most crucial element to save lives comes in: the bystander. In fact, the intervention of bystanders can triple the chances of survival in instances of cardiac arrest. Here is where another issue arises. Only 6 out of 10 people feel comfortable even attempting to perform CPR for someone in cardiac arrest. This stems from only 3.5% of people in the United States being trained in first-aid procedures such as cardiac arrest, and an irrational fear the bystander will inflict further damage to the victim. The Solution: The report below follows the assumption that in the next 5-10 years VR technology will be readily adopted into everyday life, by everyone. Strides in hardware will make the technology as sleek as a pair of glasses, and as common as a smartphone. Our novel VR and AI-based pipeline equips bystanders with the knowledge and visual guidance to perform life-saving procedures with confidence and precision. At Treehacks, we focused on creating guidance for a situation where a bystander witnesses someone seizing, which eventually escalates into cardiac arrest. Using Good Samaritan, the device passively detects a medical emergency and guides the bystander on how to care for the victim until emergency medical services arrive on the scene in order to give the victim the best chances of survival. We provide in-depth, real-time visuals that detail: Real-time data streamed from a Fitbit of the victim to monitor vitals (TerraAPI) Facilitate proper “log-roll technique” to move an injured person The correct safe orientation for someone having a seizure so they don’t choke on their saliva The proper supporting of the head and neck to prevent paralysis Instruction for proper CPR with visuals on the victim’s body for where to place hands, what pace to perform compressions at, and when to give mouth-to-mouth breaths A live progress bar displaying the time until emergency medical services arrive on the scene This immersive experience ensures that, without immediate professional help, the affected individuals receive the best possible care, increasing their chances of survival and recovery. What we are proud of, and how we built it: Wow, we created a novel dynamic application that has the potential to save millions of lives in the future. We programmed computer vision-based models using MediaPipe and OpenCV to perform pose detection and joint detection. We then performed linear transformations in a 3D vector space to identify and anchor the points in the Apple Vision Pro’s virtual space using real-time video from our computer vision script built onto VisionOS. Business Model: $14.6 Billion Market Cap -Work with public health departments to include the app in rural or underserved areas. The government could fund the deployment of the app as part of their mandate to improve public health infrastructure. -Work with emergency services to integrate the app into their response protocols, providing first responders with additional information or assisting in situations where they can't reach the scene immediately. -Apply for government grants aimed at technological innovations that improve public safety and health. -Educational Programs: Integrate the app into educational programs, such as school safety initiatives or community health workshops, funded or supported by local or national government agencies. The team (4 people, 4 schools represented): Ray- Stanford, specializes in AI and product structure Shutaro- Columbia, specializes in immersive technologies Shloak- UCLA, specializes in vision Yash- Georgia Tech, specializes in medicine Next Steps: This is one tangible application for Good Samaritan, though in the future we plan to have similar guiding procedures for: -Anaphylactic shock -Lacerations where bleeding must be managed -Stroke -AED’s -Other emergency medical complications that benefit from the interference of a bystander Challenges we ran into: Our expertise lay in Unity; however, Apple Vision Pro was only accessible with Unity Pro ($2,000), so we pivoted to and learned Swift. We ran into errors while translating CV’s 2D data into a 3D environment; we made use of anchoring techniques to pin the z-dimension while using the xy-dimension from CV. What we learned: A ton! Applying CV’s 2D data into a 3D space, programming VR and AR on the Apple Vision Pro, and using Swift UI to develop VisionOS applications! Our pipeline is built ground up and novel—we figured it out along the way with little documentation to lean on! <div