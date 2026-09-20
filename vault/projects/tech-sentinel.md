---
slug: "tech-sentinel"
url: "https://devpost.com/software/tech-sentinel"
title: "Tech Sentinel"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 460
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
  - "domain/transportation"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Tech Sentinel

> Your all-in-one AI-powered cybersecurity shield.

[Devpost](https://devpost.com/software/tech-sentinel) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[security_privacy]] [[transportation]]
**substrate** [[video_visual]] [[web_dom]]

**stack** matplotlib, numpy, pandas, pil, python, scikit-learn, scipy, streamlit, virustotal

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tech sentinel

## Body

Inspiration Cybersecurity threats are constantly evolving, from phishing SMS to malware-laden files, malicious URLs, and network intrusions. We wanted to create a unified platform that empowers users—whether businesses or individuals—to detect, analyze, and respond to threats in real time, all in one place. What it does Tech Sentinel is an AI-powered, all-in-one cybersecurity dashboard. It provides: SMS Spam Detection: Instantly classify messages as spam or ham. Threat Detection (.arff): Analyze network datasets to detect intrusions. Image Steganography: Encrypt and decrypt secret messages in images. Live URL Scan (VirusTotal): Scan URLs for malicious content. PE File Scanner: Detect malware in executable files. File Hash Checker (VirusTotal): Verify file safety using SHA-256. Port Scanner: Check open/closed ports on hosts. PCAP Analyzer: Inspect network traffic packets in uploaded PCAP files. How we built it Frontend & UI: Streamlit for a clean, interactive dashboard. Machine Learning Models: SMS Spam Detection: TF-IDF + Random Forest Threat Detection: StandardScaler + ML classifier trained on .arff datasets PE File Malware Scanner: Custom classifier on extracted PE features External APIs: VirusTotal API for live URL/file scanning. Security: Password hashing, session management, encrypted image messages. Networking & Analysis: Python libraries like socket and scapy for port and packet analysis. Challenges we ran into Integrating multiple tools and models into a single cohesive dashboard. Handling file uploads and ensuring compatibility with different formats (ARFF, PCAP, PE files, images). Rate limits with VirusTotal API and waiting for scan results. Ensuring encrypted messages fit into image payload capacity. Safely storing and managing user authentication. Accomplishments that we're proud of We are proud to have built a single platform that unifies eight different cybersecurity tools, providing a comprehensive solution for threat detection and analysis. The platform enables real-time scanning for URLs and files using VirusTotal, while our custom machine learning models effectively detect SMS spam and PE malware. Additionally, we implemented secure image steganography with password-protected messages and designed an intuitive Streamlit interface that makes these advanced cybersecurity features accessible to users without technical expertise. What we learned Through this project, we learned how complex it can be to handle multiple file types and machine learning models within a single platform. We gained valuable insights into managing API limits and rate-limiting when integrating external services, as well as securing sensitive data such as passwords, API keys, and hidden messages. Furthermore, we refined techniques for feature extraction, encoding, and preprocessing to improve the accuracy of our cybersecurity ML models. What's next for Tech Sentinel Looking ahead, we plan to implement real-time network monitoring and alerts, add automated threat mitigation suggestions, and integrate additional malware and ransomware detection capabilities. We also aim to expand image steganography support for larger payloads and multiple file formats, while optimizing the platform’s performance and scalability for enterprise-level usage. <div