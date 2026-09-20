---
slug: "containerized-online-bandit-experimentation-cobe-platform"
url: "https://devpost.com/software/containerized-online-bandit-experimentation-cobe-platform"
title: "Containerized Online Bandit Experimentation (COBE) Platform"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 717
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/scientific_research"
  - "user/developer"
  - "user/researcher"
  - "substrate/video_visual"
---

# Containerized Online Bandit Experimentation (COBE) Platform

> A containerized experimentation platform built to monitor online controlled experiments learned under contextual bandit policies in real-time.

[Devpost](https://devpost.com/software/containerized-online-bandit-experimentation-cobe-platform) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[measured_ablation]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[scientific_research]]
**user** [[developer]] [[researcher]]
**substrate** [[video_visual]]

**stack** django, docker, gunicorn, jquery, nginx, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for containerized online bandit experimentation (cobe) platform

## Body

Average Rewards for Control and Treatment Groups in Simulated User Feedback Learning Probabilities via CB Training Screenshot of the Control Group Landing Page Screenshot of the Treatment Group Landing Page Inspiration Having recently joined Shutterstock as a Data Engineer on the Experimentation Enablement Team, my inspiration for this project came from the pain points many internal teams face when implementing, executing, and monitoring controlled experiments. This calls for AI/ML driven solutions that addresses questions like "What if the chosen variation post A/B test degrades in performance over time?". Many companies with an experimentation-first culture can highly benefit from utilizing online controlled experiments supported by contextual bandit systems to personalize the user experience by adjusting and optimizing future decisions based on the data collected from each observation. The current process of setting up, running, and monitoring these experiments is often time-consuming and requires specialized knowledge, and currently, no open source solution to support online controlled experiments exists. This led me to develop a containerized platform that can streamline and automate these processes, making it more accessible and efficient for experimenters and data scientists. What it does The Containerized Online Bandit Experimentation (COBE) Platform is a comprehensive and user-friendly tool for building, running, and monitoring online controlled experiments. It is built on top of a contextual bandit framework, making it suitable for various applications such as online A/B testing and personalized recommendation systems. The platform streamlines and automates the process of experimentation by providing a user-friendly interface to set up experiments and deploy them in real-time. It also offers a dashboard for monitoring and analyzing experiment performance, allowing for quick insights and decision-making. How we built it The platform is built using containerization to respect the experimentation process by isolating all variants from each other. Using containerization also enables ease of deployment and scalability of the infrastructure. Additionally, the platform is designed to be modular and customizable, allowing users to choose and integrate different components and tools according to their needs and preferences. Particularly for this MVP, we utilized various technologies and languages, including Python, Docker, and NGINX, to build and optimize the platform's performance and functionality. We also incorporated contextual bandits policy trainer container to simulate the user experience and provide personalized recommendations. Challenges we ran into One of the main challenges we faced during the development process was designing and implementing a scalable and efficient infrastructure for the platform. These aspects are imperative to fully support the full suite of experimentation methods. We had to optimize the platform's resource usage while ensuring it could handle these experiments simultaneously. Another challenge was integrating different tools and components into the platform, as there were compatibility and configuration issues to overcome. Accomplishments that we're proud of We are proud to have developed a platform that can streamline and automate the process of setting up and running online controlled experiments in a fairly reproducible manner. We were able to utilize a user-friendly interface and dashboard for non-technical users to easily run experiments, customize visualizations, and monitor performance. We also incorporated advanced features such as personalized recommendations and real-time analytics, making the platform more dynamic and robust. What we learned During the development process, we learned the importance of a modular and scalable approach in designing and building a complex platform such as the COBE platform. We also gained a deeper understanding of contextual bandit policies and their applications in online experiments. Through integrating different technologies and tools, we learned how to optimize and enhance the platform's performance and functionality. Additionally, we learned about the importance of building a containerized solution to address challenges commonly faced in experimentation. What's next for Containerized Online Bandit Experimentation (COBE) Platform We have the following developments lined up for the future of our COBE platform: Incorporating additional contextual bandit algorithms with an ability to tune parameters to improve the platform's recommendation capabilities and provide more accurate insights and suggestions. Expanding the platform's capabilities to handle more variations of experimental design, including A/B/n Testing, AA Testing, etc. Fully utilize Weights and Biases capabilities to create an improve experience for experimenters and data scientists. Implementing automated testing and validation processes to ensure the platform's reliability and accuracy. Integrating a user feedback system to gather insights and improvements from users to continuously enhance the platform's functionality and user-friendliness. <div