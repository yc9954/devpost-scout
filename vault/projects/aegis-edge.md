---
slug: "aegis-edge"
url: "https://devpost.com/software/aegis-edge"
title: "Aegis Edge"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 373
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/formal_verification"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/patient_family"
  - "substrate/sensor_telemetry"
---

# Aegis Edge

> Zero-trust autonomous triage for networked medical hardware. Localized frontier intelligence detects sensor tampering and patches embedded firmware in real time, without ever leaving the device.

[Devpost](https://devpost.com/software/aegis-edge) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[formal_verification]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[health_clinical]] [[security_privacy]]
**user** [[patient_family]]
**substrate** [[sensor_telemetry]]

**stack** arduino, c, flipper, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for aegis edge

## Body

Landing Page Device Graph Dashboard Agentic Patch Fix Red Team Blue Team Inspiration Hospitals, forward operating bases, and SCADA plants can't ship sensor data to the cloud, HIPAA, denied-comms, air-gaps. So when an attacker spoofs a sensor on the wire, no SOC ever sees it. We wanted to build the immune system for that gap: an on-prem model that patches firmware faster than an adversary can rewrite the attack. What it does Aegis Edge is an air-gapped autonomous defense for embedded hardware. A Python bridge streams telemetry from an Arduino-driven ventilator, detects sensor tampering, asks a local 70B-param LLM to derive a virtual-sensor patch in Arduino C++, and reflashes the UNO over USB, all without leaving the LAN. How we built it Hardware: ELEGOO UNO R3 ventilator rig: DC fan, pressure pot, LCD1602, buzzer, HX1838 IR receiver. Attacker: Flipper Zero running a custom aegis_attacker.fap that fires a signal at the ventilator Bridge: Python + pyserial reading 115 kbaud JSON, anomaly detector on a rolling window. Brain: local LLM (Ollama) emitting strict, parser-clean C++. Reflash loop: arduino-cli compile + upload invoked as a subprocess. Frontend: live three.js dashboard for the demo. Accomplishments that we're proud of End-to-end recovery in under a few seconds: attack → detect → generate → flash → vent breathing again. A fully untethered attacker. The Flipper sits on the table; the vent alarms when you aim it. Zero-shot virtual sensors that actually track ground truth using only pressure and fan PWM. The whole pipeline runs offline. No outbound packets, ever. What we learned Physical-layer attacks change the threat model entirely; software defenses have to assume the wires are lying. Local frontier models are finally fast and good enough to sit in a real-time control loop, not just a chat window. The unsexy infra (udev rules, executable bits, serial framing) is what actually ships demos. What's next for Aegis Edge Multi-sensor fusion: derive any dropped channel from the survivors, not just temperature. Signed firmware so the reflash itself can't be hijacked. A formal verification pass on LLM-emitted patches before they hit the MCU. Port beyond AVR, STM32, ESP32, and eventually real medical-grade controllers. Field trials with a defense or healthcare partner where the air-gap is the product, not the demo. <div