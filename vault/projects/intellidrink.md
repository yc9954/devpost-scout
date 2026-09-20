---
slug: "intellidrink"
url: "https://devpost.com/software/intellidrink"
title: "IntelliDrink"
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 505
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/sensor_telemetry"
---

# IntelliDrink

> Our project aims to help consumers of alcohol make responsible decisions by providing wearable biometric information based on their alcohol consumption and data driven decision making for bartenders.

[Devpost](https://devpost.com/software/intellidrink) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]] [[transportation]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[sensor_telemetry]]

**stack** python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for intellidrink

## Body

Wearable E-Ink Display Inspiration Our project falls under the category of health and safety. In 2019 alone, drunk driving took over 36,000 lives. Each time one of these tragedies occur, it could have been prevented if the drunk driver made better decisions. These deaths can all be preventable with technology aiding people in providing information and help with decision making. Our project aims to solve this crisis by providing information and data driven decision making to a consumer of alcohol. Information collected allows the bar goers to track the number of drinks they have consumed and their approximated blood alcohol content (BAC) level. These metrics allow the consumer to be more responsible and make more informed decisions. The product also provides information to bar tenders to help their customers have a safe and enjoyable night. What it does The customer shows up to the bar. At the door, they scan their ID insuring they are above the legal drinking age, as well as inputting their gender, weight, and payment method. The software assigns this information to a QR code which is displayed along with the metrics on an E-ink wearable display. When the customer want to order a drink, they scan the wrist band which adds the drink they ordered to their tab, updates the approximated biometrics. How we built it Using a Raspberry Pi, 3D printer, and e-ink display, the team made a wearable device that displays unique information relative to the user. a QR code that is used to count drinks, calculate BAC of the wearer, and pay for the tab at the end of the night. The Waveshare E-ink is a low cost reusable display we use on the wearable device. This and the electronics are house in a 3D printed casing and worn on the wrist. The display is driven by a Raspberry Pi zero (v1.1) and E-ink display driver. The code used is Python, using the Pillow API, the E ink library, and PiQRCodes The scanner uses a second Rasberry Pi Zero (v1.1) and communicates to the other Raspberry Pi via WiFi. Challenges we ran into Challenges we faced while creating this technology include: Coming up with a product idea. The team used their brainstorming skills Getting the Rasberry Pis to communicate Learning basics of Python for the newbies Limited hardware and tools Faulty hardware Accomplishments that we're proud of What we learned The team learned a lot about hackathons and coding during the 24 hours. Half the team had never done a hackathon. Half the team had little coding experience and learned Python, Pillow API, and debugging. What's next for IntelliDrink Future improvements include miniaturization of electronic components. This would provide a cleaner more intuitive design to the user. Software improvements include a more robust QR code reader, auditory feedback when scanning the QR code. Process improvements include asking the user how many drinks they have had so far, in case they are not starting at 0. We envision this project to be an option in every bar. <div