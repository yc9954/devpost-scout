---
slug: "metallisense-oti3f0"
url: "https://devpost.com/software/metallisense-oti3f0"
title: "MetalliSense"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 776
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "user/developer"
---

# MetalliSense

> AI-powered real-time alloy optimization for smarter foundry operations.

[Devpost](https://devpost.com/software/metallisense-oti3f0) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: cross_origin_web, sensor_fusion</sub>
**user** [[developer]]

**stack** javascript, mongodb, node.js, python, react.js, restapi, scikit-learn

## Body

Logo Login page DashBoard Grades Specifications MetalliSense AI INSPIRATION: Modern foundries depend on precise control of chemical composition to produce metals with the required strength, durability, and quality. Even a small deviation in alloy composition can lead to scrap, re-melting, wasted materials, and increased energy consumption. Traditionally, metallurgists analyze spectrometer readings and decide manually how much alloy should be added to correct the composition. While this process relies on valuable expertise, it can be time-consuming and may vary across operators or shifts. At the same time, industrial environments generate large amounts of real-time data from sensors and spectrometers. We were inspired by the idea of using Artificial Intelligence and Industry 4.0 technologies to turn this data into actionable insights. This led to the creation of MetalliSense AI, an intelligent system designed to assist metallurgists by analyzing real-time composition data and recommending precise alloy corrections while keeping humans in control. WHAT IT DOES: MetalliSense AI is an AI-powered decision-support system for alloy optimization in foundries. The system continuously monitors chemical composition data and compares it with the target metal grade. When deviations are detected, the AI engine calculates the optimal alloy additions required to bring the composition back within specification. Key capabilities include: Real-time monitoring of chemical composition Detection of deviations from target metal grades AI-generated alloy correction recommendations Human-in-the-loop approval and override system Complete logging and traceability of decisions Instead of automating the process entirely, MetalliSense acts as a smart assistant for metallurgists, helping them make faster and more accurate decisions. HOW WE BUILT: We built MetalliSense AI using a modular Industry 4.0 architecture that reflects how real industrial systems operate. Frontend Dashboard: A web interface that displays real-time chemical composition data Shows deviations from the target grade Presents AI-generated recommendations Allows engineers to approve or override decisions Backend Service: Acts as the central orchestrator of the system Handles communication between the frontend, AI engine, and data sources Manages workflow and logging Industrial Data Integration Layer A spectrometer simulator streams real-time composition data Mimics industrial communication used in real foundries AI RECOMANDATION ENGINE: Analyzes chemical composition data Computes optimal alloy additions needed to minimize deviation The core calculation used by the system is: 𝐷𝑒𝑣𝑖𝑎𝑡𝑖𝑜𝑛=𝑇𝑎𝑟𝑔𝑒𝑡𝐶𝑜𝑚𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛−𝑀𝑒𝑎𝑠𝑢𝑟𝑒𝑑𝐶𝑜𝑚𝑝𝑜𝑠𝑖𝑡𝑖𝑜𝑛 Using this deviation, the AI model estimates how much alloy should be added to correct the composition while respecting practical metallurgical constraints. CHALLENGES WE RAN INTO: One of the biggest challenges was simulating realistic industrial conditions without access to real foundry equipment. To solve this, we built a spectrometer simulator capable of generating continuous chemical composition data streams. Another challenge was designing a system where AI could provide recommendations without removing human authority. Industrial environments require safety and accountability, so we implemented a human-in-the-loop workflow where engineers must approve or override AI suggestions. Managing real-time communication between multiple system components—frontend, backend, AI service, and simulator—also required careful coordination to ensure smooth data flow. Finally, alloy optimization is not purely mathematical; it involves real metallurgical constraints such as element interactions and maximum addition limits. Incorporating these constraints into the recommendation logic was a complex but important task. Accomplishments that we're proud of: We are proud of building a system that closely resembles real industrial architectures used in smart factories. Key accomplishments include: Designing a complete AI-driven alloy optimization workflow Implementing a real-time data monitoring dashboard Creating a modular architecture that can easily integrate with real hardware Maintaining transparency and traceability for every decision made by the system Demonstrating how AI can assist experts rather than replace them Most importantly, the project demonstrates how modern technologies can improve both industrial efficiency and sustainability. WHAT WE LEARNED: This project taught us valuable lessons about both software engineering and industrial systems. We gained experience in designing distributed systems that process real-time data streams and integrate multiple services. We also learned how critical explainability and transparency are when deploying AI in industrial environments. Another key lesson was that successful industrial AI systems must prioritize human-centered design. Instead of replacing experts, AI should support them by providing insights that help them make better decisions. Working on this project also deepened our understanding of Industry 4.0 concepts, including smart manufacturing, digitalization, and data-driven process optimization. WHAT'S NEXT FOR METALLISENSE: MetalliSense AI has strong potential for future development and real-world deployment. Possible next steps include: Integrating with real spectrometer hardware in industrial foundries Implementing machine learning models trained on historical alloy data Adding cost optimization for alloy additions Connecting with ERP and manufacturing execution systems Building a digital twin of the foundry process for advanced simulations Our long-term vision is to transform MetalliSense into a smart manufacturing platform that helps foundries optimize production, reduce waste, and operate more sustainably. <div