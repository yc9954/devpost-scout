---
slug: "perwer"
url: "https://devpost.com/software/perwer"
title: "PERWER"
hackathon: "Africa Deep Tech Challenge 2025"
organization: "Africa Deep Tech Foundation"
winner: true
words: 780
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/health_clinical"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
---

# PERWER

> PERWER IoT System lets you remotely monitor power, optimise solar usage, cut running costs, get smart AI predictions and analyse data for your Mini Grids and Cell Towers.

[Devpost](https://devpost.com/software/perwer) · hackathon [[Africa Deep Tech Challenge 2025]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[education]] [[health_clinical]]
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]]

**stack** 3dblender, 3dprinting, arduinoide, c, c++, chatgpt, css, html5, javascript, json, machine-learning, onrender, perplexity, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next for perwer

## Body

Perwer Solar Panel PERWER Inverter Perwer Generator PERWER Dashboard Inspiration It all began During my Internship in University when I was flipping through a Business Day NG newspaper and saw how much IHS and other telecom companies were spending on diesel, especially with fuel prices skyrocketing. In 2016 as per another report I read through research, IHS reportedly spent 2.6 billion Naira every month on diesel. By 2023, even with Project Green in place, that figure had risen to over 31.2 billion Naira annually. It was shocking. I thought, There has to be a smarter way to power these towers and manage Batteries used in Solar Systems and Mini-grids. Solar looked like a great alternative, but then came the issue of batteries. They were expensive, hard to manage, and failed often without proper monitoring. That headline stuck with me. Later, I talked to a friend who had worked on mini-grid systems and had run into similar challenges. That’s when we both realized something important. If we could solve this power management problem, we could help telecom towers run more efficiently, reduce costs, and even improve connectivity for rural communities. And just like that, the idea for PERWER started to take shape. And the Africa Deep Tech Challenge Made us revisit the Challenges, What it does PERWER is a smart, ultra-low-power system that makes mini-grids and telecom towers more reliable, affordable, and sustainable. It monitors temperature, power flow, battery health, and fuel usage, sending real-time updates to a dashboard. With built-in AI, it predicts faults, optimizes solar and battery performance, and enables predictive maintenance, reducing downtime, cutting fuel costs, and extending system lifespan. Even in remote areas, PERWER keeps energy systems running smoothly while lowering emissions. How we built it PERWER is built using a blend of reliable, affordable, and locally repairable components. At its core are ESP32 microcontrollers paired with voltage dividers, ACS712 current sensors, DS18B20 temperature sensors, and optional LoRa modules for extended communication, also LED for Onsite Display. Dual connectivity through GSM and Wi-Fi ensures the system remains operational even in areas with weak network coverage. On top of the hardware, an AI layer powered by a regression model analyses real-time data to accurately predict battery health and state of charge, enabling proactive maintenance. All insights are delivered through a simple, responsive dashboard built on Supabase with a custom frontend, providing seamless access to critical power metrics. Challenges we ran into It wasn’t a smooth journey. The sensors gave noisy signals at first. Some components overheated. GSM connections were unreliable in the field. Fitting everything into tight tower enclosures was a headache. We fixed each problem step by step. We added capacitors to clean up signal noise, upgraded to higher-rated resistors, calibrated the ESP32’s ADC, and redesigned the hardware layout to fit better in compact spaces. We also had to switch the ML model from Random Forest to Regression for better Accuracy. Accomplishments we’re proud of We now have a working system. that can help reduce site visits, prevents outages and saves money. The AI model predicts battery health with 98 percent accuracy and the system uses less than 2 watts of power. Everything is built with parts that can be sourced locally, and it doesn’t need advanced skills to maintain. What we learned Building PERWER meant testing not just the hardware, but also the software under real-world conditions. In the lab, components like the ESP32, sensors, and power circuits looked solid, but only field trials revealed issues such as sensor drift, power noise, heat buildup, and connectivity drops. On the software side, testing was equally critical: our AI regression model for predicting battery health needed validation against real operating data, while the Supabase-powered dashboard and communication stack were stress-tested under weak GSM/Wi-Fi signals. Iterating on both hardware and software in the field allowed us to simplify designs, harden enclosures, refine algorithms, and optimize data handling. Every cycle of testing made PERWER smarter, tougher, and more accurate, ensuring it truly works in the harsh, resource-constrained environments it was built for. What’s next for PERWER We are ready to scale. Our immediate focus is on expanding field deployments, providing simplified installation kits, and training local technicians for maintenance and support. From powering cell towers to schools, clinics, and rural communities, our goal is to roll out PERWER across hundreds and soon thousands of sites across Africa. By proving resilience in the toughest environments, we can ensure reliable energy that connects and empowers millions of people. The next phase is to launch PERWER as a startup, raise growth capital, and scale operations positioning it as the go-to solution for monitoring and optimizing power across Africa’s telecom towers and mini-grids. <div