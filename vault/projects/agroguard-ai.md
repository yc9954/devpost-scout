---
slug: "agroguard-ai"
url: "https://devpost.com/software/agroguard-ai"
title: "AgroGuard AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 469
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# AgroGuard AI

> AgroGuard AI: Simple Dashboard to help farmers monitor their fields

[Devpost](https://devpost.com/software/agroguard-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[labor_employment]] [[security_privacy]]
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** c++, css, html, javascript, typescript

## How they structured the write-up

- dashboard preview
- the problem this solves
- how the system works
- alerts and notifications
- technology used
- project structure
- designed for farmers
- future improvements
- contributing
- purpose
- license

## Body

🌾 AgroGuard AI Smart Field Monitoring and Intrusion Alert System AgroGuard AI is an IoT based field monitoring system built for farmers. It provides live sensor readings, instant alerts, and a simple dashboard so farmers can understand what is happening in their field without technical knowledge. The goal is simple. Protect crops, prevent losses, and give farmers peace of mind. Dashboard Preview The dashboard shows live temperature, humidity, rain status, gas detection, and intrusion alerts in one place. The dark theme is designed for clarity and outdoor visibility. The Problem This Solves Farming fields are often left unattended for long hours. Common issues include Sudden rain damaging crops Harmful gas buildup Intruders or animals entering fields at night No easy way to monitor conditions remotely AgroGuard AI connects the field to the internet and keeps the farmer informed at all times. How the System Works Hardware The field unit is built using a NodeMCU ESP8266 and multiple sensors. DHT11 for temperature and humidity Rain sensor Gas sensor Laser and LDR based intrusion detection OLED display for local status Buzzer for on site alerts WiFi connection using a hotspot Cloud Backend The backend runs completely on Cloudflare. Cloudflare Workers handle API requests D1 database stores the latest sensor readings KV storage stores notification subscriptions Telegram bot sends instant alerts Dashboard The dashboard is a progressive web app. Live sensor cards Real time temperature and humidity graph Mobile friendly layout Simple language suitable for farmers Alerts and Notifications Notifications are triggered when any sensor value changes or when an intruder is detected. Alerts are delivered through Telegram bot messages On field buzzer Dashboard updates This ensures the farmer is informed even when not actively checking the dashboard. Technology Used Hardware ESP8266 NodeMCU DHT11 Rain sensor Gas sensor LDR and laser module Backend Cloudflare Workers Cloudflare D1 Cloudflare KV Frontend HTML Tailwind CSS Chart.js Notifications Telegram Bot Web Push Project Structure AgroGuard AI firmware folder contains ESP8266 Arduino code worker folder contains Cloudflare Worker backend public folder contains dashboard files assets folder contains images and screenshots Designed for Farmers This project follows a farmer first approach. Simple language Clear visual indicators Works on low end phones Minimal interaction required Offline friendly dashboard Future Improvements Planned upgrades include Voice alerts in Hindi GSM support for areas without WiFi Historical data analysis Smarter intrusion detection Crop specific insights Contributing Contributions are welcome. Whether it is improving the UI, optimizing sensor logic, adding language support, or improving documentation, every contribution helps. Purpose Technology should support the people who feed the world. AgroGuard AI is built to protect crops, farmers, and livelihoods using affordable and scalable technology. License This project is licensed under the MIT License. ⭐ If you like this project, give it a star. It supports open source learning and real world impact. <div