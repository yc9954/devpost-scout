---
slug: "cast3d-scanner-for-medicinal-casts"
url: "https://devpost.com/software/cast3d-scanner-for-medicinal-casts"
title: "CAST3D - Scanner for Medicinal Casts"
hackathon: "Hack the North 2020++"
winner: true
words: 788
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "user/patient_family"
  - "substrate/video_visual"
---

# CAST3D - Scanner for Medicinal Casts

> Making a cast that will last

[Devpost](https://devpost.com/software/cast3d-scanner-for-medicinal-casts) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[health_clinical]]
**user** [[frontline_worker]] [[patient_family]]
**substrate** [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** arduino, google-spreadsheets, javascript, nodemcu, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cast3d - scanner for medicinal casts

## Body

The machine in all its glory Solidworks render Scanned Arm Partial cast print VF1 VF2 VF3 Inspiration With many previous fractures and injuries under my belt and an interest in 3D printing, the thought of developing a method of creating splints for those who are injured arises. Typically-used splint and cast materials are often quite heavy, lack water resistance, lack airflow, and a few other drawbacks. However, when searching through the 3D printing forums, a talented few constructed their own 3D printed casts. On the other hand of the talented few, there was little efficiency when attempting to scan one's arm, leg, etc… The most common method of scanning was photogrammetry using cameras. Most cameras used in these situations capture little to no depth and the process would take hours to perform without the right equipment. With the rise of LiDAR sensors, one common theme took hold, which was that of scanning objects. LiDAR has become very accessible at low costs. Taking into account all the factors listed, it seemed like the perfect opportunity to make an MRI-like machine that scans a patient's arm. What it does The CAST3D machine begins with the Alexa interaction, where the user data and information is collected. Once greeted, the machine takes a complete scan of the user’s injured arm and sends it to a technician's device. From there, the captured scan is processed to smooth down any discrepancies and to create the printable cast. Once done, the user has a printer-ready tailored 3D model to their distinct arm How we built it We first built an Alexa skill using voiceflow, that takes in new patient’s information, as well as updating a recurring patient's information. The skill collects the patient's first name, last name, email address, and phone number, this information then gets written into a google sheet that stores as well as dynamically updates this information. A google sheet script was made by coding in javascript which allowed for all of the email addresses that Alexa retrieves to be correctly formatted to emailaddress@mail.com . We then used the API blocks to connect to the Blynk server which turns on/off a virtual pin that connects to the NodeMCU via WiFi, the NodeMCU then sends a signal to the Arduino to turn on/off the relay which then tells the motors to move counter-clockwise until the scan is complete (1.52 mins). Once the scan is complete two more API integration blocks were used to allow voiceflow to connect to the Blynk server which turns on/off another virtual pin which is connected to the NodeMCU via WiFi, the NodeMCU then sends a signal to the Arduino to turn on/off the relay which then tells the motors to move clockwise back to their original position ready for another scan. Challenges we ran into We are into many different challenges both hardware and software. Software Issues: We initially had issues with the NodeMCU connecting to the Blynk server, we eventually just reset the board and it then worked. Many issues arose with voiceflow, we keep receiving errors for certain variables. Another issue with voiceflow was updating data for re-occurring patients. Hardware Issues: One of the first issues we came across was correctly sizing the belt for both wheels, even when we correctly measured the size for the belt, once the rotating arm reached the bottom too much slack within the belt occurred which did not allow for the rotation to continue. Another hardware issue that occurred was getting the NodeMCU board to communicate to the Arduino. Accomplishments that we're proud of It worked! After several hardware and software mishaps, we got the machine to operate smoothly enough to capture a clean arm scan. What we learned Making a system that combines hardware, software, and the interface can be quite challenging. Although it is always the hope that things work from the get-go. However, that was far from true. Troubleshooting on all levels of the system had to be completed on several occasions to better our device’s performance. Additionally, we learned to cooperate more as a team than as individuals. Both of us brought good ideas to the discussion table and a sense of individuality. On the other hand, we performed greatest when we combined those ideas and improved upon them. What's next for CAST3D - Scanner for Medicinal Casts Hopefully, sometime in the future, a CAST3D V2 comes about. Several design aspects need to be reconsidered for this device to be feasible for use in institutions. For example, opting for a more rigid material such as metal would have been a better option. Additionally, now that there is a better understanding of the hardware used, the goal is to prevent the time it requires to troubleshoot. <div