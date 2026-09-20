---
slug: "wheezer-418n3w"
url: "https://devpost.com/software/wheezer-418n3w"
title: "Wheezer"
hackathon: "Intel Hacks 2017"
organization: "Intel"
winner: true
words: 471
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
---

# Wheezer

> A lung function testing device for asthmatics

[Devpost](https://devpost.com/software/wheezer-418n3w) · hackathon [[Intel Hacks 2017]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]

**stack** 3dprinting, adafruit, android-studio, arduino-101, diptrace, matlab, seeedstudio, sm5812

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wheezer

## Body

Inspiration Asthma affects approximately 1 in 12 people in the US (AAAAI, 2001). The most significant measurement for quantifying asthma severity is the pulmonary lung function test. One such function test includes spirometry, which is used to assess the lung volume and exhalation rate of the patient. Without health insurance, these tests can cost over $200 per visit (Healthcare Bluebook). Our goal is to design a low-cost device for spirometry testing that can accurately assess the patients lung capacity and flow rate during exhalation. What it does Our device measures the exhalation flow rate via the pressure drop through a venturi. Based on the venturi dimensions, the fluid density, and the pressure drop, the flow rate can be calculated and integrated for the total lung capacity. This information is plotted on a digital display on the device and is also transmitted via bluetooth to a connected android device. The following values are used to characterize the lung function: FVC -- Forced vital capacity. FVC is the total amount of air exhaled during the test. FEV -- Forced Expiratory Volume, which measures how much air you can exhale during a forced breath. FEV1 -- The amount of air exhaled may be measured during the first second. How we built it The instrument was designed using fluid mechanics to design the venturi based on our size constraints and selected differential pressure gauge. The venturi was then modeled and printed using a MakerBot. An Arduino101 is used to communicate with the differential pressure gauge and plots the results on the digital display. It also transmits the data via bluetooth to a connected android device for real-time plotting and analysis. Challenges we ran into Challenges included syncing the arduino clock with the android device for accurate integral calculation of the total lung capacity. We also had issues with losing low-flow data due to pressure gauge sensitivity at very low deltaP. Accomplishments that we're proud of We are exceptionally proud that our device correlates well with the professional spirometry testing and shows repeatable results. The peak flow rates and total lung volume correlated well, but the greatest differences were at low flows toward the end of the exhalation. What we learned During testing, we discovered difficulty measuring low flow rates, which is an inherent flaw of flow measurement with a venturi. Other flow measurement devices should be considered to capture lower flow rates. What's next for Wheezer It is possible that future iterations of Wheezer could also include a parallel measurement using a hot-wire anemometer to cover the low flow range while the venturi covers the upper range. Future iterations of Wheezer will also be able to save the patients data to their phone to track lung strengthening or deterioration over time. The instrument will also be redesigned for greater portability and convenience in maintenance. <div