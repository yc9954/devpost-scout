---
slug: "scup-smart-checkup"
url: "https://devpost.com/software/scup-smart-checkup"
title: "SCUP: Smart Checkup"
hackathon: "The Worthy Web App Challenge"
organization: "Progress"
winner: true
words: 1400
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/general_public"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/medical_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SCUP: Smart Checkup

> Smart telemedicine platform, based on IoT devices that provide Vital signs and historical values.

[Devpost](https://devpost.com/software/scup-smart-checkup) · hackathon [[The Worthy Web App Challenge]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[health_clinical]]
**user** [[clinician]] [[general_public]] [[legal_professional]] [[patient_family]]
**substrate** [[code_repository]] [[medical_record]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, arduino, aws-iot, react

## How they structured the write-up

- introduction, inspiration and problem
- solution
- made with several kendoreact components!
- how we built it
- real world alpha test
- step by step trial
- what's next for scup
- final commentary
- references:

## Body

login Screen Sensor monitor historical Oxygen saturation Thimble ECG sensor Thermometer Real Consultation V1.1 DISCLAIMER: This application is used for demonstrative and illustrative purposes only and does not constitute an offering that has gone through regulatory review. It is not intended to serve as a medical application. There is no representation as to the accuracy of the output of this application and it is presented without warranty. Introduction, inspiration and Problem The Current COVID-19 pandemic changed everything. From the way we do business, congregate, transport and most specially the way we go to the doctor and take care of our health. This made Telemedicine one if not the way to move forward regarding simple patient care. So we decided to research what kind of solutions we are adopting. Telemedicine software allows doctors to interact with patients via online video, which has been traditionally useful for practices with dispersed rural populations, including gaining access to specialists beyond what is locally available. Sometimes telemedicine software is offered as a standalone platform, but these days it's not unusual to find it also provided within existing medical practice management (PM) software. Even standalone telemedicine platforms will often easily integrate with other medical software, such as for Electronic Health Records (EHR) or to make it easier to work with patient histories, making it easier to diagnose or treat medical conditions. (1). But, that's the main problem. The sophistication of a system does not matter if few people are using it (at sometimes prohibitive costs) and it has no reach to zones where it was intended to operate. Also, most systems are way too cumbersome to use, have very old UI's and are not adaptable to modern needs. To validate these past hypotheses we decided to do some field research and ask Medical Doctors first hand, several questions, regarding their use of Telemedicine platforms and the way we can improve them. We made a series of interviews with Medical Doctors, you can find the full documentation in this repository: https://github.com/altaga/Scup/tree/main/Interviews We have to add that these tests were performed with Doctors just from Mexico City, where telehealth solutions are almost non-existent or have not reached the numbers that are needed today. And this is where we see the main problem. Most doctors were using Zoom or Teams for their telemedicine needs! Yes, that is indeed the current state of affairs regarding telehealth, at least in Mexico. We also spoke with several MD's in the US and most of them were doing the same. Despite the fact that we have several, very sophisticated systems they have not reached mass market , are too hard to use and do not provide useful data. And that's the second problem, the current meeting apps do not meet the healthcare needs regarding just taking Biometrics or following up patients. But, what if we can change that? Solution SCUP is a Smart telemedicine platform, based on IoT devices that provides Vital signs and historical values. This to transform the way telemedicine is provided and solve the biggest problem in relation to distance check-ups, which is taking biometrics. Our current version consists of an Oxygen Saturation Thimble, an ECG sensor and a contactless Thermometer that can send real time information to a web application. This allows distance consultations and follow ups to become more seamless and to grab real biometrics and vital signs while doing them. Here is our current development: Click on the image please as markup cannot embedd videos. Made with several KendoReact components! For a thorough list of the components check this part of our github: https://github.com/altaga/SCUP-WWAC#app-ui We have to take into consideration that this has also been made for mobile and is a modernized form of old telemedicine which has quite a lot of applications out there. How we built it This is the main diagram of the system: Through several cloud services we can get important biometric data from the patient. First through MQTT and AWS IoT we are collecting the sensor data that is sent through an AWS API to a Database. Then though another couple API's we are using that data and filling the required slots on our webapp. The devices are developed by us using off the shelf components and are mostly 3D printed. The temperature Sensor and the Oxygen Saturation Thimble are very self-explanatory as they are just wireless (WiFi powered) and only send their data to the Database. The ECG sensor is much more complicated as we continue developing a past project: https://www.hackster.io/386896/ehm-electrocardiography-holter-monitor-06a4f3 The innovation we are bringing to the table regarding this sensor is the use of Dry electrodes and integration into everyday clothing, making it indeed much easier to use and very comfortable. Real World Alpha Test This is perhaps the most important part of the project as we decided to test it with real doctors in a real* clinical setting. *We avoided attending emergency and terminal patients and chose patients without many symptoms. The Alpha Test involved 9 medical doctors from different areas to use the SCUP’s Application. They also got the opportunity to see in action the wireless medical devices. All of them spent time in the application with a patient. Some of them recreate a normal medical consultation. The rest of them use the application as an experiment of the new technology. In the end, all of them were amused with the software. They haven't seen any Telemedicine software like this one and were surprised about the devices. They gave us valuable feedback. Which we used to improve the UI and the medical reports in order to make it useful and user friendly. The testers also gave us ideas about the next devices we could integrate to SCUP’s Application. We are thinking of expanding this to 50 MDs for our Beta test and continue testing, while exploring business models for the IoT devices and applications. Here is a compilation of the most important aspects of said Alpha test: Click on the image please as markup cannot embed videos. Step by Step trial Check our Github for step by step instructions on how to run the environment and addon. As this application requires the physical devices to work, we have prepared a virtual device simulator that you can find in our Github. in addition with Step by step instructions on how to use it: https://github.com/altaga/SCUP-WWAC#simulator-tab We are always up for a live demonstration of our projects, if you are a judge of this contest please contact us via Devpost! What's next for SCUP Testers gave us ideas about the next devices we could integrate to SCUP’s Application. We are thinking of adding blood pressure smart devices. It is the last primary measure for vital signs and there are some other medical devices we can continue adding. By now the public's emotions towards telemedicine is that it is somewhat useless (in some regards) and not well focused. We are thinking of expanding this to 50 MDs for our Beta test and continue testing, while exploring business models for the IoT devices and applications. We will show telemedicine is no longer science fiction, by continuous testing and improvement within the medical community. Final Commentary This is perhaps the first telehealth application of this kind to have potential to reach mass market and become a part of a Doctor's repertoire. Most medical Doctors, even in the US and Europe, not to mention developing countries (such as Mexico) are NOT using determined applications for their telehealth needs, but the common meeting applications such as Teams or Zoom. We are just using an add-on that aims to overcharge their capabilities with biometric reading and patient follow ups, which is the way to go. It's much easier to adopt many more users this way than to expect them to learn to use a new application from scratch. We envision a future in which Healthcare is invisible and seamless, where you are getting the attention of experts but only engage if necessary. Using Machine learning and IoT to monitor symptoms to a condition with every process improving so it becomes error-free. With emphasis on the preventive side and with the patient as the point of care, YOU become the point of care. References: (0) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4193577/ (1) https://www.techradar.com/best/best-telemedicine-software (2) https://doxy.me/en/ (3) https://www.amchealth.com/ (4) http://swymed.com/software-cloud-server/ (5) https://www.teladochealth.com/ (6) https://www.mendfamily.com/ (7) https://www.advancedmd.com/patient/telemedicine-software/ (8) https://www.acetiam.eu/acetiam-solutions/telemedicine/ (9) https://mdlnext.mdlive.com/ (10) https://physicianvisit.com/ (11) https://www.thera-link.com/pricing/ (12) https://www.theraplatform.com/ (13) https://www.sofiasalud.com/ (14) https://www.ncbi.nlm.nih.gov/books/NBK207146/ (15) https://telemedicine.arizona.edu/blog/7-telemedicine-concerns-and-how-overcome-them <div