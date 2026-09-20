---
slug: "thermohalo-ai-firearm-detection-84vpze"
url: "https://devpost.com/software/thermohalo-ai-firearm-detection-84vpze"
title: "ThermoHalo - AI Firearm Detection"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 1376
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# ThermoHalo - AI Firearm Detection

> ThermoHalo uses AI-powered thermal imaging to detect concealed weapons at school entrances. Safe, FERPA-compliant, and built on affordable $200 cameras to protect kids.

[Devpost](https://devpost.com/software/thermohalo-ai-firearm-detection-84vpze) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[human_in_the_loop]] [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[accessibility]] [[climate_energy]] [[education]] [[legal_justice]] [[mental_health]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** computervision, rf-detr, roboflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for thermohalo - ai firearm detection

## Body

Examples of images that were captured (far left, middle right) and the annotated versions that the model trained on (middle left, far right A selfie taken with the thermal imaging system that demonstrates how individual privacy is preserved by ThermoHalo. A Confusion Matrix of the predictions that ThermoHalo makes, the red labeled frames are mistakes, and the green are accurate predictions An alert occurs when a firearm is detected in n or more consecutive frames A flowchart showing ThermoHalo’s multilayer verification system Inspiration After numerous shooting threats made national headlines at our school, Memorial High School, my brother and I spent months living in constant fear. We brought extra textbooks to class not to read, but as makeshift shields. We carried things we could grip if the worst happened. The hallways we once walked freely through started to feel like narrow exits, and names like Uvalde and Sandy Hook echoed constantly in our minds. But this isn't just our story. It's the reality for millions of students, educators, and families across the country. School violence and threats, whether real or hoaxes, disrupt learning, damage mental health, and erode trust in the institutions meant to nurture the next generation. We built ThermoHalo because schools should be places where curiosity and community thrive, not places where fear has a home. Rather than restricting lawful gun ownership or relying on purely reactive measures, we wanted a proactive, technology-driven way to raise the alarm before a shooting can even start. What it does ThermoHalo uses AI-powered thermal imaging to detect concealed firearms at school entrances and walkways. When someone carrying a concealed weapon enters the camera's view, the system flags the thermal signature of the gun against the body's heat and triggers a multi-layer verification process before any response is deployed. The verification system works in three stages. First, the AI only raises an alert if a firearm is persistently detected across multiple consecutive frames, cutting down on false positives. Second, a front-end staff member reviews the thermal image and physically observes the flagged individual for suspicious behavior. Third, if both the AI and the human reviewer agree there's a threat, a single button press sends an alert, complete with camera footage, to a school resource officer or police. This triple-layered approach means multiple levels of personnel confirm a threat before law enforcement is ever deployed. Critically, ThermoHalo achieves all this while respecting privacy: thermal imaging naturally obscures facial features and skin color, capturing only heat signatures, and the system runs locally rather than sending data to a hackable cloud. How we built it We started by examining existing concealed-weapon detection technologies, X-ray scanners, metal detectors, and millimeter-wave imaging, but each had dealbreakers: prohibitive costs (tens to hundreds of thousands of dollars per unit), health risks from repeated radiation exposure, or bulky equipment requiring trained staff. Our goal became a system that was safe, affordable, efficient, and minimally intrusive. We chose thermal imaging paired with AI because it can safely reveal the cold metal frame of a firearm without emitting harmful radiation. Prior lab work at the Birla Institute of Technology and Science and the University of Kufa had proven this concept, but only with $20,000 cameras. Our key insight was to use computer vision and machine learning to extract meaningful patterns from low-cost hardware instead, learning generalized anomaly patterns rather than relying on expensive, high-resolution sensors. We began with a $450 FLIR One Pro, but its poor sensitivity (~70 mK) and low 160×120 resolution produced blurry, unusable images. We switched to a $200 TOPDON TC002C Duo with nearly double the sensitivity (40 mK) and a crisp 512×384 resolution. We then captured images of people concealing a CZ 75 P-01 handgun in various poses, placements (waistband, pants pockets, hoodie pockets), body shapes, clothing, and environments, and annotated them in Roboflow by drawing bounding boxes around both the guns and the people. For the model itself, we built an automated multi-layer verification pipeline around our detection model, connecting real-time predictions to a human-in-the-loop alert system that culminates in a one-click notification to law enforcement. Challenges we ran into Our biggest technical hurdle was the model architecture. Our initial approach used YOLOv8, a standard choice for real-time object detection, but it struggled badly with the low-contrast nature of thermal data. Because YOLO divides images into a fixed grid and analyzes cells in relative isolation, it kept missing the "soft" edges that concealed handguns create, producing a high rate of false negatives as the weapon blurred into the body's heat signature. After weeks of plateaued progress, we pivoted to the RF-DETR model. Thanks to its Global Attention Mechanism, RF-DETR analyzes spatial relationships across the entire image, so it learned that a cool spot near a human waistband isn't a random artifact but a high-probability threat. This shift from local grid-based detection to global spatial reasoning was our single most important breakthrough. Getting there took thirteen iterations. We spent countless hours hunting "blind spots", like subjects turning sideways so the gun was only partially visible, and fixed them by continuously feeding the system new data from diverse environments, from sun-drenched entryways to crowded, climate-controlled hallways. We also collected footage of benign metal objects like phones, keys, and water bottles so the model would stop false-alerting on them. We also had to confront hard limitations. Heavy winter clothing blocks the cold thermal signature of a gun from reaching our camera, and thermal equilibrium means a firearm sitting in a warm pocket gradually "warms up" and becomes harder to detect. We added heavier-clothing data to versions 10 through 13, which produced marginal gains, but we honestly acknowledge that heavy-layer performance remains below the threshold for reliable field deployment. Beyond the technical work, we navigated a genuinely complex legal and ethical landscape, designing around the Fourth Amendment and Kyllo v. United States (placing cameras only in public areas), FERPA compliance (collecting no personally identifiable information), and potential sources of algorithmic bias across different body shapes and clothing. Accomplishments that we're proud of ThermoHalo achieved a 98% mAP@50 score , meaning that in 98% of cases the system correctly found a concealed gun and pinpointed its precise location on screen. We kept false positives below 4% and false negatives below 5%, and we measured a time-to-detection of under one second from the moment a person enters the frame. Beyond the metrics, we're proud that we built a system that takes privacy and ethics seriously from the ground up rather than as an afterthought, using thermal imaging that obscures identity, local on-device processing, and a triple-verification process specifically designed to prevent a student from ever being wrongly searched in front of their peers. We're most proud that we turned a frightening personal experience into something built to protect other students from feeling the same fear. What we learned Our biggest takeaway was the power of AI working together with humans to identify threats, rather than replacing human judgment. We learned how to design a system that is simultaneously legally sound, ethically responsible, and technically resilient, and how those three demands constantly shape one another. Technically, we learned why architecture choice matters enormously: the jump from YOLO's local grid reasoning to RF-DETR's global spatial attention was the difference between a system that didn't work and one that did. We learned the value of stress-testing against real-world messiness, and we gained a real appreciation for the physics underlying our problem, from thermal resistance to thermal equilibrium, and how those constraints define what's actually possible. What's next for ThermoHalo - AI Firearm Detection Looking ahead, we want to improve ThermoHalo's adaptability to diverse school environments, including larger campuses and crowded spaces, by refining the AI model. We aim to expand the system's contextual understanding so it can more reliably distinguish benign objects from concealed handguns while continuing to drive down false positives. We also plan to explore advanced privacy-preserving techniques like on-device inference and federated learning to further reduce data transmission and strengthen student privacy. Working alongside school personnel and safety experts, we want to optimize the multi-layered verification process and keep the system ethically responsible, legally compliant, and operationally effective. Ultimately, our goal is to scale ThermoHalo into a deployable product and company that protects America's schools and saves lives. <div