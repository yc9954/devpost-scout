---
slug: "digital-patient-care-system-5-0-dpcs-5-0"
url: "https://devpost.com/software/digital-patient-care-system-5-0-dpcs-5-0"
title: "Digital Patient Care System 5.0 (DPCS 5.0)"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 871
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# Digital Patient Care System 5.0 (DPCS 5.0)

> DPCS 5.0 is a smart healthcare ecosystem designed to monitor, analyze, and respond to patient health in real time

[Devpost](https://devpost.com/software/digital-patient-care-system-5-0-dpcs-5-0) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
  <sub>weak: provenance_signing</sub>
**domain** [[health_clinical]]
  <sub>weak: developer_tools, elder_child_care</sub>
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]
  <sub>weak: medical_record</sub>

**stack** c++, docker, edge-ml-models-blockchain:-ethereum/ganache, esp-idf, fastapi, firmware, flask, github-actions-(ci/cd), grpc, javascript-(react), kafka-/-redpanda-apis-&-protocols:-rest, kubernetes-(cloud)-cloud-services:-aws/gcp/azure-(kafka, merkle-root-anchoring-smart-contracts-other-tools:-grafana-(dashboards), mqtt-over-tls

## Body

Overview Cam 2 Practical Front Side circuit Back Side Flow Chart 🌟 Inspiration The inspiration behind DPCS 5.0 stemmed from observing how many patients, particularly in rural and remote areas, suffer due to the late detection of health emergencies. Chronic illness management remains largely manual in many parts of the world, and the cost of continuous monitoring devices remains prohibitively high. Our vision was to create a system that is affordable, secure, and highly reliable. We wanted to combine the power of edge computing, artificial intelligence, and cloud technology into a single healthcare platform that could alert caregivers instantly, provide doctors with valuable long-term insights, and still respect the privacy of patients. ⚡ What it does Digital Patient Care System 5.0 acts as a full-stack health monitoring and alert system. A wearable device built on ESP32 continuously collects critical vital signs such as ECG, heart rate, oxygen saturation, body temperature, galvanic skin response, sweat pH, and motion. This data is securely transmitted to a Raspberry Pi edge gateway, which runs its own MQTT broker, performs real-time anomaly detection, and can trigger SMS alerts in case of emergencies. At the same time, the gateway stores data locally for 30–90 days, ensuring resilience even without internet connectivity. Data is also synchronized with the cloud, where machine learning pipelines refine anomaly detection models, a blockchain client anchors health data for tamper-proof trust, and long-term trends are stored in a scalable time-series database. The patient portal shows only today’s vitals in a privacy-first manner, while the doctor portal provides access to historical records, AI-driven anomaly detection, and deep analytics. 🛠️ How we built it The system was built in multiple layers. On the device side, we wrote ESP32 firmware that integrates with sensors and transmits the data using MQTT secured with TLS encryption. For offline resilience, the ESP32 also caches data on a microSD card. On the edge layer, the Raspberry Pi hosts Mosquitto as a secure MQTT broker, Kafka for durable message streaming, InfluxDB for short-term storage, and Python-based machine learning scripts for anomaly detection. A GSM module (SIM7600) was integrated for sending SMS alerts even when internet connectivity is unavailable. On the cloud side, we deployed a Kafka cluster to act as the global data backbone, TimescaleDB and InfluxDB for long-term time-series storage, and object storage for raw data. A blockchain client anchors Merkle roots of health data to ensure trust and immutability. Finally, we built web portals for patients and doctors using React for the frontend and FastAPI for the backend, connected securely to the cloud services. 🚧 Challenges we ran into Building DPCS 5.0 was full of technical and practical challenges. Streaming ECG data in real time without losing packets required deep optimization of both network protocols and buffering mechanisms. Implementing TLS on the ESP32 was a challenge due to limited memory and processing power, but it was essential for securing patient data. Synchronizing data between the Raspberry Pi edge node and the cloud without duplication or loss required designing a robust messaging system with Kafka. Another challenge was designing dashboards that provided enough information for doctors to make decisions while maintaining strict privacy for patients. Managing the power consumption of the wearable nodes was also critical, as continuous monitoring could quickly drain batteries if not optimized. 🏆 Accomplishments that we're proud of Despite the challenges, we are proud that we built a fully functional end-to-end prototype. The system successfully collected data from wearable ESP32 devices, transmitted it to the Raspberry Pi, performed anomaly detection locally, and triggered SMS alerts through the GSM module. We anchored blockchain proofs of patient health data, ensuring trust in medical records. Our web portals provided a dual experience: the patient view was privacy-focused, showing only today’s vitals, while the doctor view offered long-term analysis and AI-based alerts. We also achieved offline resilience by enabling 30–90 days of data storage on the Raspberry Pi, ensuring monitoring even during internet outages. 📚 What we learned Throughout this project, we learned the importance of designing healthcare systems with edge computing in mind. Real-time anomaly detection at the edge dramatically reduces response time compared to cloud-only systems. We also realized that privacy and security must be integrated into the design from day one, with features like TLS encryption and blockchain-based integrity verification. Another key learning was that healthcare systems must be resilient, especially in environments with unreliable connectivity, so local storage and SMS backups are vital. Finally, we learned that scalability changes everything: the architecture that works for one patient must be modular enough to scale to thousands or even millions. 🚀 What’s next for DPCS 5.0 Looking ahead, we plan to enhance DPCS 5.0 with predictive AI models capable of detecting early signs of diseases before they become critical. We aim to integrate smartwatches, medical-grade devices, and hospital IoT systems into the platform, creating a unified healthcare ecosystem. The doctor portal will be expanded with telemedicine features, enabling doctors to consult patients remotely in real time. We also plan to conduct pilot deployments with hospitals and real patients to validate the system in real-world conditions. Ultimately, our goal is to scale DPCS 5.0 into a global healthcare IoT platform that empowers patients, assists doctors, and saves lives. <div