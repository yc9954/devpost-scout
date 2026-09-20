---
slug: "ecgo"
url: "https://devpost.com/software/ecgo"
title: "ECGo"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 829
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# ECGo

> Mobile ECG with Wi-Fi capabilities that makes AI-powered diagnoses and stores data on a remote server.

[Devpost](https://devpost.com/software/ecgo) · hackathon [[TreeHacks 2025]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]

**stack** c, esp32, influxdb, opacity, python, pytorch, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ecgo

## Body

(Pardon the very basic video - we worked straight to the wire to bring this project to fruition!) Inspiration Both our team members come from families working in the medical device industry, and we know firsthand how important critical medical devices are for saving lives around the world. Our project aims to solve the lack of portable ECG machines on hand in developing regions or crisis-stricken areas, where such devices (and the doctors needed to operate them) are incredibly expensive or simply unavailable. What it does ECGo takes a three second sample of your heartbeat using attached electrodes. It then forwards this sample to a remotely hosted database, from which an AI model is able to run an arrhythmia diagnosis on the test data. This information is then sent back to the user, along with a sample ID they can use to access their data in the future from our web application. How we built it The heart (get it?) of the hardware on this project consists of an ESP32 microcontroller, which uses its built-in ADC to read values from an AD8232 heartbeat filtering IC. This data is then displayed on two 0.96" OLED screens controlled over I2C. The user can also use a joystick to pan and zoom the ECG waveform displayed on the screen. For safety, both the microcontroller and IC are powered by AA batteries to avoid any potentially dangerous power connections. On the software side, the ESP32 must be connected via Wi-Fi to some network which allows it to make HTTP requests. We use these requests to write data to an InfluxDB database, and also read the AI model's diagnosis out from the same database. Each sample is randomly assigned an ID from 0-10000 for use with the web interface. The front-end software is a simple streamlit app, which uses Python to query the database for user data and displays the resulting data. The server uses a CNN Transformer which we pretrained on open-source ECG data. It also interfaces with the InfluxDB database by checking it periodically for a new series of data, and writes its inference to the database when it finds new data. Challenges we ran into One early challenge with the hardware bringup was the fact that my OLED screens were manufactured with a single I2C address, meaning that there would be no way to use two screens to display different data. To fix this we had to desolder a small surface mounted resistor and shift it to a different pin, which was quite a challenge. Otherwise, noise was (and is) a big issue with the project; we do our best to avoid being in areas with tons of electromagnetic interference when taking detailed samples. Testing the model was also a challenge, since we don’t have a good way of measuring an irregular heartbeat with our electrodes. The model did report a positive diagnosis of arrhythmia for incredibly noisy environments, which have more irregular signals, and a negative diagnosis for a regular heartbeat. We explored the web3 track and experimented with placing an AI-powered agent on the application also assists with interpreting their test results and giving medical suggestions. However, this was rather difficult to integrate in the limited time we had left and so in the final product we left it off. Accomplishments that we're proud of As a team of only two (one hardware/firmware and one software/AI), we are very proud of having a successful final product with so many different features and complexities. We’re very happy with the way the hardware fabrication went, from prototyping to the final PCB soldering without any major hiccups. Furthermore, the entire data flow of chip -> HTTP -> Database -> Model -> Database -> HTTP -> chip is surprisingly reliable and effective. What we learned This project was a new experience for both of us when it comes to integrating our areas of technical expertise with each other, as interactions between embedded systems and AI on such a close level are less common in our normal work. Technically, we both learned a lot about working with time-series data and InfluxDB. Working through the aforementioned integration gave us both a better understanding of how to work with diverse inputs and outputs that we don’t usually see. What's next for ECGo ECGo is not just about arrhythmia diagnosis - this paradigm of an inexpensive, mobile device for use in the field in conjunction with more powerful AI diagnostics and support in a remote server has great potential to us in bringing healthcare to areas around the world with less access to technology or medical personnel. The next future steps are to further develop the diagnostic capabilities and improve the ECG filtering, and then adapt the device to be even more technology-free by moving the patient query onto the ESP32 as well, making the relatively inexpensive hardware component the only item we need on-hand to perform the whole suite of diagnostic, data storage, and recommendation. <div