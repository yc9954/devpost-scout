---
slug: "slap-kw7rd8"
url: "https://devpost.com/software/slap-kw7rd8"
title: "Slap"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 1033
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
---

# Slap

> Need something that helps you stay focused during studying/work? Use this slap machine to wake you up if you are about to fall asleep!

[Devpost](https://devpost.com/software/slap-kw7rd8) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[sensor_fusion]]

**stack** arduino, blynk

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for slap
- tracks (but also anywhere you see fit)

## Body

physical parts circuit physical parts + circuit code 1 code 2 code 3 code 4 Inspiration All of us have run into this problem: trying to finish an assignment or study for an exam but finding yourself losing concentration or falling asleep. We need a solution to solve this issue! What it does This device uses a gyroscope attached to a headband to measure the tilt of your head. If the sensor detects that your head is no longer upright, but instead, leaning forward and downward (which means that you are falling asleep!), it activates the motor and the speaker. The motor is connected to the hand, and is rotated 90 degrees to slap the person, before rotating back to its original position. The speaker plays the audio clip “Wake up, you filthy animal!”. This process is in a loop, sp as long as your head remains tilted downward, you will keep getting slapped and called a filthy animal. The device also allows another user to use an app to control the rotation of the hand. How we built it Gyroscope (MPU6050): We made a program that prints out the acceleration and rotation angle of the sensor. After testing different angles, we found an acceleration that resembles the position of the head when a person is falling asleep, and set that as our indicator. Speaker (ISD1820 + 0.5 W 8 Ω loudspeaker): We used the ISD1820 module to record a message “Wake up, you filthy animal!” and connected it to the speaker. We tested this separately to begin with by connecting it to an ultrasonic sensor so that the sound would play if an object was within 10 cm of the sensor (Lab 2). Servo Motor (MG996R): For the motor, we first tested it using code from Lab 3 on the SG90 micro servo motor (torque of 1.80 kg-cm) found in our standard Arduino kit with a paper cutout of a hand. We then transferred our logic onto the MG996R servo motor which has a much larger torque (9.4 kg-cm) and can rotate a real-life sized hand. IoT (Blynk + Feather V2): We used a similar design as the one we did in Lab 4. Blynk is able to control the rotation of the motor (thus the movement of the hand). This allows a second person to be able to slap the individual by controlling the rotation of the hand on their phone (because we all need responsible friends that look out for us like that). Challenges we ran into We spent a long time figuring out how to connect Blynk to our product and ran into multiple issues. At first, there seemed to be issues with the Feather V2 board itself, as running the basic “Blink” program did not seem to make the red light flash. We also ran into issues with the hotspot, as it kept saying that the device was offline. This ended up being a Mac issue, so we tried on a Windows laptop instead. However, there were problems with ESP32 itself on this laptop, as it kept saying that esp32tool.exe does not exist. A software update was able to eventually resolve this issue, so that we were able to get the device to be online and control the servo motor using the Blynk console. We also ran into a challenge of how to attach the hand to the motor, as it was quite heavy (almost 200 g). We were originally going to attach the motor to the end of the hand that had a place for an attachment to be mounted to a desk clamp, however, the weight was unbalanced and so the hand was unable to stay upright. We resolved this issue by instead keeping the clamp attachment on the hand, and attaching the motor with hot glue closer to the hand’s wrist so that it could stay balanced. Having the clamp attachment already glued to the other end of the hand helped since it acted as a counterweight such that we did not need to move the motor even further up the hand (i.e. closer towards the fingers). Accomplishments that we're proud of Overall, we’re incredibly proud of being able to create a fully functioning prototype with all components incorporated together (including a realistic hand) and not just a proof of concept. We’re proud of being able to finally connect our prototype with Blynk, as it took multiple feathers, laptops, software updates, and hotspots to finally work. We’re also proud of being able to make a prototype with the motor actually connected to the hand, instead of using a piece of paper as suggested by others to only show a proof of concept, as this showed an ability to overcome an engineering challenge. What we learned We gained a deeper understanding of input and output signals. In the process of combining all parts together, we had to tweak the code and the circuit so that one part can react to the change in another part. In this way, we were able to get a better understanding of computer logic and how to incorporate multiple components in formulating our design on an Arduino. What's next for Slap A more accurate threshold for the gyroscope sensor. As for now, if acceleration-x reaches a certain value, the motor will be activated. But ideally, we will have a more accurate measure threshold that can detect if the user is falling asleep more accurately, and that would need more experimentation with the gyroscope sensor in order to figure out more accurate acceleration and rotation values. A more refined attachment of the hand to the motor. Currently, it is attached using hot glue on a piece of styrofoam as the platform, which can easily break. Ideally, we can get a drill and a shaft to attach to the motor and securely attach the hand to it. A louder speaker. Currently, we have a 0.5 W speaker, which doesn’t produce much sound. We can increase the volume by soldering on an additional component (a PAM8403 module) which acts as a sound amplifier. Tracks (but also anywhere you see fit) best overall yay most likely meme startup WBUOT most iq points lost IJAG <div