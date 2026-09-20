---
slug: "carbonz"
url: "https://devpost.com/software/carbonz"
title: "CarbonZ"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 489
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# CarbonZ

> Digital MRV for a sustainable ecosystem

[Devpost](https://devpost.com/software/carbonz) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[finance_payments]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** ai, amazon-web-services, chainlink, machine-learning, nextjs, polygon, python, quicknode, solidity, spaceandtime

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learnt
- what's next for carbonz

## Body

Ensuring Digital Measuring, Reporting and Verification for a sustainable ecosystem Inspiration Digital Monitoring, Reporting, and Verification (MRV) of greenhouse gas emissions remain a crucial tool in ensuring we have a sustainable planet. This was what brought about the CarbonZ project (a new product developed by Chemotronix during the hackathon) which combines IoT, AI, and Blockchain technologies to provide a comprehensive solution for offsetting carbon emissions. By leveraging IoT devices equipped with sensors, we monitor and track environmental parameters to accurately measure carbon emissions. Our advanced calibration strategy, powered by AWS, ensures precise data interpretation. What it does With the collected data, our AI algorithms convert raw sensor values into real-time CO2 concentration readings, enabling individuals and organizations to monitor their carbon footprint easily and accurately. Additionally, we leverage Blockchain technology to facilitate seamless and transparent carbon offsetting, empowering users to take proactive steps toward environmental sustainability. The data from the IoT device is also analyzed using A.I such that stakeholders can forecast carbon emissions and take actions to gradually reduce it. How we built it We built an IoT device that tracks carbon emissions in the atmosphere using the ESP8266 board and sensors such as MQ7, MQ9, MG811, and MQ5, among others. We then leveraged AWS to deploy a regression machine-learning model to calibrate the IoT device's raw sensor data. We also leveraged Space and time as a decentralized data warehouse to store data using the SQL endpoints. To offset carbon emissions, we leveraged Quicknode to create an ERC20 token as tokenized carbon credits, and chainlink was used to automate several functions in the smart contract. Challenges we ran into Spaceandtime was quite difficult to navigate, but we found our way by following the tutorials available. Combining several technologies was also very tedious, but we were able to divide tasks efficiently as a team to achieve our goals within the stipulated timeline of the project. Accomplishments that we're proud of Developing a unique blend of IoT, A.I, and Blockchain technologies to address the issue of carbon emissions Creating an IoT device with a unique ID registered on the blockchain. This enables users and companies to track their carbon emissions, which can be a complex and challenging process. Storing carbon emissions data on a decentralized data warehouse (SpaceandTime) instead of traditional cloud storage. Leveraging AWS to build and deploy a Machine learning model for sensor calibration. What we learnt Technical skills: We learned about the Chainlink and Space and Time ecosystems, as well as the Quicknode. we also learned about platforms such as AWS and how several services can support our product. Other skills: We had to combine several new technologies and this was only possible through good collaboration and persistence, we learned the value of good communication and collaboration. What's next for CarbonZ We are looking forward to initiating and partnering with climate-friendly projects while implementing an effective platform for digital measurement, reporting, and verification of projects globally. <div