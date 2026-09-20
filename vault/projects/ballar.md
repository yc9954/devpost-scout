---
slug: "ballar"
url: "https://devpost.com/software/ballar"
title: "BallAR"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1258
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# BallAR

> Unite AR and electro-stimulation to perfect your beer pong game.

[Devpost](https://devpost.com/software/ballar) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[education]]
**substrate** [[geospatial]] [[video_visual]]

**stack** arduino, esp32, gemini, lensstudio, snapchatspectacles, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ballar

## Body

Aim Fire! Hardware Diagram Software Workflow Inspiration While our hackathon team is less Greek Life and more Geek Life, we recognize the utility, hilarity, and surprising difficulty of the game ‘Beer Pong’. This party game requires precise hand-eye coordination, inter-team collaboration, and strategic planning. It is also frequently played in dim conditions and under various forms of impairment, meaning that participants can use all the help they can get. With that in mind, we developed BallAR, an augmented reality (AR) tool developed on Snap Spectacles paired with electro-stimulation pads so users can practice their aim, receive assistance during matches, and even have our experience flex their beer-pong muscles for them. What it does BallAR has a physical and an AR component. The physical component is centered around electro-stimulation sensors that are actuated via an Arduino, relay module, and ESP 32 module. When the user wishes to launch the ball, the electro-simulation sensors hooked up to the user’s arm will actuate certain sensors in a timed fashion through the relay module. The AR component is built for Snap Spectacles. The primary functionality of this experience is to create a spatial UI that draws an optimal ping-pong ball shot from the user’s hand to a single red solo cup. The user’s hand is tracked via the Snap Lens Studio Interaction Manager, which serves as one end of the ideal trajectory. The other end is defined differently based on the two primary modes, single-cup and multi-cup. In single-cup mode, the user can click a spatial button to take a photo for Gemini to analyze. Using the returned XY coordinate and the Z depth coordinate created by the depth mapping during the photo, we can define a 3D coordinate that represents the endpoint of a ping-pong ball’s ideal trajectory. In multi-cup mode, the user is able to place and adjust a predefined triangular object representing the 10-cup arrangement of a Beer Pong game. This object maps onto flat surfaces initially, but after placement can be physically moved to any location in 3D space, depending on the user. The user can then dynamically select a cup to aim for, which will serve as the next target. Finally, the AR component also connects to the electrostimulation component via BLE, and offers a few levels of protection when it comes to the initiation of said component. Because the stimulation has the potential to adversely affect the user, we placed high priority on ensuring that the experience would be difficult to accidentally trigger. Before anything could begin, our electrostimulation UI was locked behind the acknowledgement of a successful connection from both parties (Snap Spectacles and ESP32 Microcontroller). After this, a safety button would be enabled, which needs to be fully pressed in order to enable the electrostimulation fire button, which would in turn, after being pressed, reenable safety and hide the fire button. How we built it The snap lenses send a message over bluetooth to the Arduino. This causes the Arduino to activate certain muscles with the electric sensors. To better develop a user’s ability to throw consistently we have a relay module to time the moment we actuate the user’s muscles. This timing ensures that we are able to separate the general throwing motion from the motion we use to release the ball. The user interface and cup detection was developed through Lens Studio in TypeScript. We used the Gemini API to allow us to detect the beer pong cups and use a lightweight trajectory analysis algorithm to derive a realistic trajectory for the user to aim for. The algorithm for this trajectory was inspired by research conducted around the optimal trajectory for basketball free throws. We followed a similar methodology where given the initial positions and target positions, we perform a series of frame translations to arrive at a 2D projection, fit a parabolic arc, and translate it back into the world frame which the glasses operate in. The arc was derived from conducting a series of video analysis to analyze the trajectory of the ball observed in a simulated game of beer pong. Challenges we ran into From the very start, BallAR was defined by overcoming challenges and rethinking plans. Our team’s initial concept was a Basketball trainer in AR (we aim to see the Golden State Warriors immediately after this hackathon). However, two factors led to us reconsidering: first, we found an existing Snap Spectacles Basketball trainer experience. Second, after testing with our electrostimulation technology, we found that the amount of electricity required to launch a basketball (via activating the tricep and wrist muscles) would cause irritation and discomfort. However, after brainstorming, we were able to pivot and buy some red solo cups and halloween themed ping-pong balls to pursue a different iteration of BallAR! Furthermore, we, alongside all of CalHacks, quickly came into contact with connectivity problems onsite. A poor initial internet connection led to a mass adoption of hotspot activity, which in turn decreased internet quality. The prisoner’s dilemma was in full force, and our team decided that the best solution would be to purposefully avoid the transmission of large amounts of data over wireless networks within our project. Our systems were built to be as independent as possible, with only an images’ worth of an API call and a small string sent via BLE necessary for a single runthrough of BallAR. This kind of redundancy and system safety was a novel but interesting challenge as we prototyped our experience. Accomplishments that we're proud of BallAR, despite its funny use case, combines the areas of anatomy, electrical engineering, firmware development, physics, game design, and augmented reality development for a smooth, cohesive experience. This project demonstrates our team’s ability to pull together knowledge from various sources of personal experience and learn new skills quickly, putting together several self-contained but mutually reinforcing components. Our ability to rapidly and successfully integrate our initial independent work (as compared to prior hackathon experiences) indicates not only that we understood one another as we converged and diverged, but also that we understood the project and its overall goals– a critical skill in school and in society. What we learned Broadly, this hackathon made our team realize the critical importance of connectivity both in terms of our project scope and our ability to iterate and develop. Unstable internet, while not crippling, in practice greatly limited the API and toolcalling ability of our project, as we wished to offer a live demo during judging. Our team learned to brainstorm around such fundamental challenges, and quickly developed a habit of using AI not within our experience, but instead to augment our research to overcome the problems we were seeing. Beyond internet issues, our team was able to learn tremendous amounts of seemingly disconnected information in order to apply it to our final product. From anatomy (an understanding of musculature was necessary for proper electrostimulation) to physics (the algorithm used for ping-pong ball targeting needed to be grounded in reality) to stateful programming (AR design is much like game design, in that sense). We grew in all these fields, either directly learning or indirectly hearing about difficulties overcome. What's next for BallAR BallAR, at the moment, is a very one-size-fits-all experience. Individuals can customize left-and-right handedness, but we offer no way to calibrate aspects such as average ball velocity or electrostimulation sensitivity within the experience itself. While our team was able to avoid this problem during demos by manually adjusting, in the future we could add further customizability to both the AR and stimulation components of our experience. <div