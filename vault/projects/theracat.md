---
slug: "theracat"
url: "https://devpost.com/software/theracat"
title: "Theracat"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1462
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/clinician"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
---

# Theracat

> A band and a plush cat that catch anxiety in how you move — and interrupt it before it peaks. There's no app to open, no waiting room. It's already on you, already watching, and it acts first.

[Devpost](https://devpost.com/software/theracat) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[health_clinical]] [[immigration_refugee]] [[mental_health]] [[scientific_research]]
**user** [[clinician]] [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[regulation_legal_text]]

**stack** anthropic-claude, arduino, bluetooth, elevenlabs, esp32, mpu6050, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for theracat

## Body

Machine learning feature input web ui for wristband data Key features distinguishing classes (plots) table of extracted features from input accelerometer waveform data Inspiration I(Wenqing) spent three years as a mental-health clinician, sitting with people in the grip of anxiety and panic attacks. Anxiety is the most common mental illness in the U.S.: about 40 million adults live with an anxiety disorder, and roughly 1 in 11 people has at least one panic attack a year. A panic attack is not "just stress." Your hands are shaking, you can't breathe, and you're certain you're about to die. It is one of the most frightening things a body can go through, and it contributes to nearly 11,000 suicide deaths in the U.S. every year. How do people cope today? Therapy genuinely works, but your clinician is not always in the room when the attack actually hits. Apps can help, but here is the cruel part: when you are shaking and choking on air, you do not have the capacity to unlock a phone, find the right app, and tap through a screen. The knowledge exists. The tools exist. What's missing is help in the moment itself. That's the gap we wanted to close. What if there were something that co-regulates you 24 hours a day, that you don't have to do anything to activate? Something that can feel when you're getting anxious and gently bring your body back down before the spiral peaks. That question became TheraCat. What it does TheraCat is a two-part companion: a wristband and a soft plush cat. The wristband quietly watches how you move. When it picks up the motion patterns associated with agitation and rising arousal, TheraCat acts first, before you have to do anything at all. TheraBot’s detection prototype is a minimal end-to-end pipeline for identifying simulated wrist-motion arousal from MPU6050-style accelerometer data. It generates synthetic three-axis acceleration signals for two states: Calm and Agitated. Calm motion is smoother and lower-variance, while agitated motion has higher variability, larger oscillations, sharper spikes, and more irregular wrist movement. The raw accelerometer stream is smoothed with a moving-average filter, split into overlapping sliding windows, and converted into standard motion features. These include standard deviation, skewness, kurtosis, FFT/PSD frequency features, and correlations between the X, Y, and Z axes. A lightweight classifier, such as a Random Forest, is then trained to distinguish Calm from Agitated windows and saved for reuse during inference. At inference time, each new accelerometer window passes through the same preprocessing, feature extraction, and model-prediction steps. The model outputs an agitation-probability score, which TheraBot can use as a trigger for a grounding intervention if elevated patterns persist across recent windows. Importantly, this prototype does not claim to detect rumination or diagnose anxiety; it detects an elevated wrist-motion arousal signature, consistent with the PRD’s framing. The primary intervention is touch. The band delivers slow, paced haptic breathing through a gentle motor on your wrist: a rhythm that contracts and releases, paced slower than your pulse, so your breath naturally follows it (long out, slow in). You don't have to read instructions or follow a screen. You just feel the rhythm and let your nervous system co-regulate with it. This is deliberate. In a panic attack the body can't really process advice, but it can feel safety, and somatic co-regulation works directly on the parts of the response (lowering arousal, raising HRV, quieting the fight-or-flight reaction) that words can't reach in that moment. On top of the haptics, the cat can speak. We used Anthropic's Claude to drive the reasoning and conversational logic, using ElevenLabs voice interaction, TheraCat can talk with you naturally, ask gentle safety check-in questions, and walk you through grounding skills like a physiological sigh or a paced breathing exercise when breath alone isn't enough. If risk language comes up in what you say, TheraCat steers you toward 988 crisis support. The plush cat is also expressive: two motors move its ears when you're stressed, so an invisible internal state becomes something you can see and hold. How we built it Under the hood, TheraCat is a simple sense → reason → act loop built from a few moving parts: Sense. The wristband runs on an ESP32 microcontroller with an MPU6050 6-axis accelerometer/IMU. It streams motion data continuously over Bluetooth Low Energy to the companion. A stress-classification model reads that accelerometer signal and decides when arousal is rising. We didn't guess at the thresholds: we warm-started the model from published, peer-reviewed work (Zhang et al., PeerJ 2016, which reported around 91.3% accuracy, and Quiroz et al., JMIR 2018, with 78%+ median accuracy), then designed it to adapt toward each person's own pattern, since every individual has a slightly different panic signature. Reason. When stress is detected, the system orchestrates the response. We used ElevenLabs for natural voice input and output, and a safety layer that screens for risk language and routes to 988 when needed. Act. The companion drives the hardware response: the haptic motor delivers the paced-breathing rhythm on the wrist, and two additional ESP32-controlled motors animate the cat's ears so the support is physical and visible. The whole thing ties accelerometer-based stress classification, BLE data streaming, motor control, voice I/O, and safety logic into one continuous loop, grounded in published anxiety and co-regulation research rather than vibes. Challenges we ran into Wiring up the hardware. Getting the ESP32, the MPU6050, and the motors talking to each other physically was harder than expected. We leaned on our coach to get the connections right. Connectivity. We started on Wi-Fi and kept hitting reliability issues, so we switched the whole data pipeline over to Bluetooth Low Energy, which was far more stable for a body-worn streaming device. Orchestrating it all. Stitching the sensing, classification, voice, and safety pieces into one coherent loop meant a lot of integration debugging. We used Claude heavily to debug and glue the pipeline together. The "how do you actually wear this" problem. Turning a breadboard prototype into something you can put on your wrist (and a cat you can hold) took some genuine creativity and improvisation. Accomplishments that we're proud of We got a working end-to-end prototype: motion in on the wrist, stress detected, and a real haptic-plus-voice response out, all in one loop. It's clinically grounded. The intervention design comes from three years of real clinical experience and from peer-reviewed research, not from a chatbot guessing what might feel nice. We built something that genuinely requires nothing from the user in their hardest moment, which was the whole point. The cat is expressive and embodied. Turning an invisible internal signal into moving ears and a held, warm companion made the support feel real. We built in safety from the start, including risk-language screening and a path to 988. What we learned Hardware is humbling. Embedded systems impose real constraints, and "it works on the bench" is a long way from "it works on a wrist." We learned a lot about BLE, sensor noise, and motor control under pressure. Touch is underrated. Digging into the somatic co-regulation literature (Zhang, PeerJ 2016 and Quiroz, JMIR 2018), reshaped how we thought about the intervention. The body responds to safety it can feel faster than to advice it has to interpret. Clinician plus engineers is a strong combination. Pairing lived clinical experience with embedded and ML skills meant the technical choices stayed anchored to what actually helps a person in crisis. Friction is the enemy. Every screen, tap, or step you remove matters enormously when the user is mid-panic. Designing for zero required action changed nearly every decision we made. What's next for Theracat TheraCat's next phase focuses on shrinking the system down and exploring two complementary product directions. With the support of Berkeley SkyDeck, we plan to prototype and pressure-test both paths before committing to a primary product line. Plan 1: Integrate everything into a smart band Consolidate the full experience onto the wrist by integrating the speaker and microphone directly into the band and miniaturizing the electronics. Rethink the calming mechanism. Instead of using a motor to tighten the band, develop a material or actuator that can genuinely contract and release, delivering breathing and grounding cues more naturally. Explore turning the band into a smart strap that replaces an ordinary Apple Watch or other smartwatch band, adding a panic-detection and intervention layer to everyday wearables. Plan 2: A personalized plush companion, especially for kids Offer a softer, more emotionally engaging form factor designed for younger users and families. Lean into creativity and personalization to make the companion feel unique to each child. Next steps with SkyDeck Validate the technical feasibility of the contracting band. Test the market fit of the plush companion. Decide which direction leads as the flagship product. Github: https://github.com/emilyLi2020/Theracat <div