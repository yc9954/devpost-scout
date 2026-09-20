---
slug: "express-drone-care"
url: "https://devpost.com/software/express-drone-care"
title: "Express Drone Care"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 978
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
---

# Express Drone Care

> Delivering physician-ordered medical prescriptions and lab tests in minutes from any medical record.

[Devpost](https://devpost.com/software/express-drone-care) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]]

**stack** arduino, autodesk-fusion-360, electronics, microcontroller, openai, python, react, servo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for express drone care

## Body

Extracted fields Payload attached to battery pack Payload + battery pack attached to full drone Drone in flight Inspiration The inspiration for Express Drone Care came from the growing need for safe and efficient delivery of medical prescriptions and lab tests to patients, especially during the COVID-19 pandemic. We recognized the growing use of telehealth and digital clinics providing both synchronous and asynchronous interactions to interact with patients. We also realize the potential of drones to address the full stack delivery of telehealth services for providers and set out to create a solution that would provide fast and reliable delivery to patients' homes without increasing physician responsibilities. What it does Express Drone Care can take in a general medical record from a provider, understand and extract the relevant patient, prescription/lab test, and delivery information from the medical record, and surface this information to a drone operator who would be at a central location to fill the prescription and send the drone out for autonomous flight. User journey: Physician uploads medical record to our drag and drop portal We send the medical record to our server We use our custom ChatGPT script to extract the relevant information about the patient Prescription/lab test, and delivery We send the information back to the portal to surface to the drone operator (in the future) to program the autonomous drone flight Drone operator loads prescription/lab test into our custom payload Drone delivers payload to patient’s delivery address. How we built it Hardware: We used the ANAFI Ai drone from Parrot. We custom laser cut the payload “claw” out of acrylic and connected an Arduino Nano to the drone to control the claw’s I/O and mechanism. We discovered the ANAFI drone runs linux and can give and receive serial commands. Because we can control external peripherals (microcontrollers, etc), we created a small peripheral device out of a microcontroller, LEDs, buttons, and servo motor controller on a custom proto board to use in a mechanical assembly later. Mechanical assembly: due to tight time constraints (3D printing is too slow), we were only left with laser cutting which led to design challenges (constrained to 2D objects). With this, we used compliant mechanisms to retrofit onto the drone’s curvature and body, accommodating numerous constraints (space, weight, air flow, staying clear of propellers, reliability, diverse set of payloads). We also wrote small calibration software to make sure motors go into correct positions and firmware to communicate with drone. Software: We built our frontend using React/Typescript and Ant Design. We set up a Node JS server on the backend to handle local API requests. We used custom prompt schemes in ChatGPT from OpenAI to extract the relevant information from the medical record for prescription/lab test delivery. We send a POST request from our frontend to our primary endpoint ‘/upload’ to process the medical record. We had a custom prompt sequence that included setting initial context, querying the name, prescriptions/lab tests, and addresses to extract across a general set of medical records. We then sent the extracted and formatted data to our Node server to re-surface back to the client for a drone operator to program the drone’s autonomous flight and know which prescription/lab tests to include in the payload. Challenges we ran into Due to safety constraints with regards to flying drones outside of Treehacks' drone cage, we were not able to show a test flight of sending the drone to a patient's home. Therefore, we decided to split the project into two halves: Create a provider portal to upload a medical record, then use NLP to extract relevant patient, prescription, and delivery information from the medical record to surface to a drone operator. Build a native drone attachment to carry the medical prescription/lab test and directly integrate with the drone's firmware to drop the test at a specified time (e.g., when the drone reaches the patient's home). We also ran into several rate limit and inconsistent response challenges with ChatGPT. To resolve the rate limit issues, we added an error checking mechanism to flag if we need to re-log in to ChatGPT or start a VPN. To improve response accuracy, we created a custom function to check for valid answers (e.g., delivery address should start with an integer). Hardware is always hard, but especially more difficult with drones, including: ANAFI simulator package hardware dependent on having an NVIDIA graphics card which no one on our team had. Building hardware (design, fabrication, assembly) in this small of a time frame is difficult (ie. resort to laser cutting). This also led us to only have essentially one shot at getting the hardware right. Drone payload: ensure it was light and customized enough to minimize impact on drone flight. Accomplishments that we're proud of Added additional system to existing drone and figured out a way to mount the payload mechanism without mounting points prebuilt on to the drone. Improving ChatGPT’s reliability for our use case through prompt engineering Full stack software design to integrate across client, server, and drone Working on a complex drone application within the time and space constraints What we learned Mechanical design was a great exercise in thinking about what is actually necessary and minimally viable in this very tight time span vs. over-engineering Learned a ton about Parrot’s simulation software was created and the nuances of building a drone company (TLDR: it’s hard) which was super interesting to hear about Nuances of ChatGPT and prompt engineering What's next for Express Drone Care Because each drone and battery pack are independent parts, we can load up each drone with a different type of payload in the future. We also intend on creating an API to directly integrate into other EHRs and health systems. No physician upload necessary → automatically screen after visit summaries Automatically program full flight path for drone (no manual work for drone operator) <div