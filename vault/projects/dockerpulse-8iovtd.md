---
slug: "dockerpulse-8iovtd"
url: "https://devpost.com/software/dockerpulse-8iovtd"
title: "DockerPulse"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 354
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# DockerPulse

> DockerPulse is powerful tool designed to monitor and manage log data from multiple Docker containers. Additionally, it can send all updates and notifications to a connected Slack workspace app

[Devpost](https://devpost.com/software/dockerpulse-8iovtd) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[realtime_stream]]

**stack** bert, docker, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dockerpulse

## Body

Inspiration DockerPulse was inspired by products like k8sgpt.ai to make orchestration monitoring tool but mostly It was inspired by researches by Tien, Chin‐Wei, Zou, Zhuping who proposed techniques for anomaly detection in docker containers What it does DockerPulse is a powerful tool designed to monitor and manage log data from multiple Docker containers. It processes log data from these containers, parses them using Drain and Spell parsers, detects anomalies using a BERT-based neural network called LogBERT, and generates solutions for detected anomalies with GPT-3.5-Turbo. Additionally, DockerPulse can send all updates and notifications to a connected Slack workspace app. This entire system is wrapped in a user-friendly command-line interface (CLI) application, making it easy to schedule and automate log monitoring tasks with the help of cron jobs. How we built it Log Collection: DockerPulse collects logs from multiple Docker containers, making it easy to centralize and analyze your application's log data. Log Parsing: It uses the Drain and Spell parsers to extract structured information from log data, enabling more meaningful analysis. Anomaly Detection: DockerPulse employs LogBERT, a BERT-based neural network, to detect anomalies in the log data, allowing you to identify issues in real-time. Anomaly Solution Generation: When an anomaly is detected, DockerPulse leverages GPT-3.5-Turbo to generate solutions or recommendations to address the detected issue. Slack Integration: Connect DockerPulse to your Slack workspace app to receive notifications and updates about log data and anomalies directly in your communication platform. CLI Interface: DockerPulse offers a user-friendly CLI for easy interaction and scheduling of log monitoring tasks using cron jobs. Challenges we ran into Challenges we faced are as follows: Availability of time to research various techniques and their efficiencies Implementation of New Research related to version of BERT tailored for LogAnomaly Accomplishments that we're proud of Just that we were able to complete and learned about various researches and especially about ASCII art of DockerPulse What we learned We learned how to implement Drain and Spell parser from scratch. Some better coding practices What's next for DockerPulse We hope to move forward with more sophisticated models such as RNN based NN or Modified Residual Network <div