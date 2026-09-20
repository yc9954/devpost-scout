---
slug: "jarvis-mhfy78"
url: "https://devpost.com/software/jarvis-mhfy78"
title: "Agent Ricky"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 841
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Agent Ricky

> Monitoring the Health and Safety of First Responders and Military Personnel

[Devpost](https://devpost.com/software/jarvis-mhfy78) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[disaster_emergency]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** brev.dev, dain, python, tensorflow, terraapi, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- 1. biometric and geolocation data collection
- 2. heart rhythms neural network classification
- 3. data processing
- 4. custom dain-powered ai alerts agent
- 5. custom dain-powered ai visualization agent
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agent ricky

## Body

Inspiration Our team wanted to use this opportunity at TreeHacks to create something bigger than ourselves, something that serves others. Who better can we serve than the first responders and the military personnel who have devoted their lives to protect and serve us every day? These first responders and military personnel must respond quickly because they are placed in very delicate situations. Thus, we realized that, we needed an AI that can be proactive and create real-time decision-making. Unlike rule-based automation or passive AI that waits for user input, agentic AI goes beyond this traditional AI by enabling autonomous decision-making in critical situations where speed and efficiency are very important. What it does Agent Ricky is a custom AI agent tailor-made for first responders and military personnel to monitor the status, safety, and health of soldiers, squadrons, and first responders in training and in action. It is essentially another member of the team. Live biometric and geolocation data collection enables Agent Ricky to detect abnormalities and dangers in real time by providing data for a series of health metrics. These health metrics are then utilized by a custom DAIN-driven AI agent to provide timely alerts, statistics, and information that could prove to be the key to save many lives. How we built it Languages: Python · TypeScript Frameworks and Tools: DAIN · Terra API · Nvidia Brev.dev · TensorFlow 1. Biometric and Geolocation Data Collection Originally, we began with the goal of using Terra's PPG waveform data to aid an AI agent in recognizing arrhythmia in order to monitor heart health. However, once we implemented a prototype system, we thought of other data that is pertinent to first responders and military personnel that could also be analyzed, monitored, and reported through the same system. As such, the data collection step now involves collection of a variety of biometric and geolocation data. 2. Heart Rhythms Neural Network Classification PPG waveform data provided by Terra API allowed us to train a keras sequential neural network from scratch using Nvidia's Brev.dev. The neural network is designed to differentiate between regular, irregular, and atrial fibrillation (afib) heart rhythms and provides crucial data for the health of first responders and military personnel. 3. Data Processing We took a different approach for processing other important biometric and geolocation data. For example, we calculated important metrics such as respiratory rate, SpO~2~, HRV, stress estimation, sleep quality, pulse wave analysis, and peak detection. These calculations could then be used for detecting alarming conditions. In addition, the preprocessed data can also be passed to the AI agent for visualization purposes. 4. Custom DAIN-powered AI Alerts Agent DAIN is a custom SDK that allows us to build custom AI agents on top of LLMs to communicate with them in an efficient manner. We designed a DAIN-powered AI service the provides timely alerts to keep safe. It takes in the variety of detected regularities or irregularities in biometric and geolocation data and determines if an alert is necessary to notify leaders and supervisors of. 5. Custom DAIN-powered AI Visualization Agent We also designed a DAIN-powered AI service that provides important visualization information to help leaders stay better informed about training and combat situations. For example, respiratory rates or location over time can prove to be crucial information. Challenges we ran into One area that we spent a significant time in was learning how to use DAIN and all its possibilities. Although DAIN draws on the power of LLMs to create AI agents, DAIN's functionality and SDK is quite different from any LLMs we had previously worked with. However, after poking and prodding our way through documentation and experimentation, we discovered the interesting potential of DAIN. Learning through the demo services, the UI manipulation, and background processes took a lot of experimentation, but also offered a novel learning experience in creating and launching AI services. Accomplishments that we're proud of Creating our own Agentic AI that has the potential to make a real impact. Coming into the Hackathon, agentic AI systems were novel to all our team members. Yet, hackathons are the best places to explore new topics, new ideas outside of comfort zones. As such, we are really proud that we, 4 strangers, not only met each other, but synergized into a cohesive unit that collectively explored agentic AI through DAIN's products. In addition, together we were able to build Agent Ricky, an agentic AI system that has the ability to provide first responders and military personnel and their leaders with the crucial information to keep them safe in training, service, and combat. What we learned The next powerful wave of AI may come from Agentic AI that leverages the abilities of LLMs to more effectively and efficiently perform specific, precise, and detailed tasks. What's next for Agent Ricky The potential of Agent Ricky only grows the more data there is available. With an expanded user base and many more data points, we see Agent Ricky as having real potential in greatly improving the safety of first responders and military personnel. <div