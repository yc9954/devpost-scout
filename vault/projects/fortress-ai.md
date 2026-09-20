---
slug: "fortress-ai"
url: "https://devpost.com/software/fortress-ai"
title: "Fortress AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 604
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/security_privacy"
---

# Fortress AI

> Autonomous AI Cybersecurity for SMEs

[Devpost](https://devpost.com/software/fortress-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[security_privacy]]

**stack** celery, docker, etherscan, fastapi, kubernetes, next.js, postgresql, redis, socket.io, timescaledb

## How they structured the write-up

- inspiration
- security vs automation
- real-time performance
- multi-agent coordination
- making enterprise security accessible

## Body

FortressAI Project Story Inspiration Cybersecurity has become increasingly difficult for small and medium enterprises. While large organizations can afford dedicated security teams, most SMEs cannot maintain 24/7 monitoring, threat detection, incident response teams, or expensive enterprise security infrastructure. This problem became more evident when looking at the cybersecurity landscape in Hong Kong. In 2025 alone, cyber incidents increased significantly, with phishing attacks, ransomware campaigns, data breaches, and wallet-draining attacks disproportionately affecting SMEs. We asked ourselves a simple question: What if cybersecurity could defend itself? This idea became FortressAI. Instead of building another dashboard that generates alerts for humans to review later, we wanted to build an autonomous cybersecurity guardian capable of detecting, simulating, responding to, and logging threats automatically. What We Built FortressAI is an AI-powered autonomous cybersecurity platform designed specifically for small and medium enterprises. The platform provides proactive security without requiring organizations to maintain dedicated security teams. FortressAI operates through two primary modes: Demo Mode Simulates real-world cyber attacks and autonomous responses for training, testing, and demonstrations. Guardian Mode Provides real-time protection for businesses and blockchain users by monitoring networks, endpoints, and digital assets continuously. The platform combines: Autonomous threat detection AI-powered attack simulation Automated incident response Compliance logging Blockchain wallet security Real-time monitoring dashboards Our goal was simple: Enterprise-grade security without enterprise-level costs. How We Built It We built FortressAI as a multi-agent architecture where different AI agents specialize in specific security tasks. Recon Agent Continuously scans infrastructure for: Open ports Misconfigurations Exposed services Vulnerabilities Suspicious assets Tools used include: Network scanning pipelines External asset discovery Threat intelligence integrations Simulation Agent Once risks are identified, the system performs AI-assisted security simulations. These simulations include: Phishing detection Red-team testing Threat validation Attack scenario generation Machine learning models help classify threats and improve detection accuracy. Response Agent Once threats are confirmed, FortressAI automatically responds. Response capabilities include: Threat isolation Tunnel deployment Network segmentation Kill switches Blocking malicious infrastructure Maintaining business continuity This allows threats to be contained within seconds. Log Agent All activities are recorded through immutable logging systems. This provides: Compliance evidence Audit trails Regulatory reporting Incident history The architecture combines: FastAPI backend services Next.js monitoring dashboards Containerized deployment Machine learning pipelines Cloud infrastructure Automated orchestration systems Deployment was designed to be simple enough for SMEs while remaining scalable. Challenges We Faced Building autonomous cybersecurity systems introduced several difficult challenges. Security vs Automation Automating security responses introduces risk. We had to ensure automated actions could respond quickly without causing operational disruption. Real-Time Performance Threat detection is only valuable if response times remain extremely fast. Optimizing scanning, inference, and automated remediation pipelines required significant tuning. Multi-Agent Coordination Creating multiple agents that work together reliably required careful orchestration and communication mechanisms. Making Enterprise Security Accessible Enterprise security tools are often complex and expensive. We needed to design a system that reduces complexity while preserving security capabilities. What We Learned Throughout development we learned several important lessons. Security systems must move from reactive to proactive defense AI becomes more powerful when specialized agents collaborate SMEs require simpler security experiences rather than more features Autonomous systems require strong observability and transparency Most importantly: The future of cybersecurity is not more alerts. It is autonomous defense. Future Vision FortressAI represents more than a security tool. Our vision is to build an autonomous security infrastructure layer capable of protecting organizations continuously with minimal human intervention. We imagine a future where: Businesses deploy security in minutes rather than months Threats are resolved automatically Compliance becomes continuous Security becomes accessible to every organization regardless of size Our mission is simple: Transform cybersecurity from reactive defense into proactive, self-healing protection. <div