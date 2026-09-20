---
slug: "p8hub-private-ai-hub"
url: "https://devpost.com/software/p8hub-private-ai-hub"
title: "P8Hub - Private AI Hub"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 942
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
---

# P8Hub - Private AI Hub

> P8Hub is an open-source project aimed at providing a private and simple platform for individuals and small teams to host and use their own AI services.

[Devpost](https://devpost.com/software/p8hub-private-ai-hub) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[vision_ocr]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]]

**stack** docker, docker-compose, fastapi, nextjs, sqlite

## How they structured the write-up

- what it does
- installation and demo
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for p8hub - private ai hub

## Body

Inspiration In an era where AI is transforming every aspect of our lives, I recognized the need for a private and easy-to-use platform where individuals and small teams could host and utilize their own AI services. The inspiration for P8Hub (Private AI Hub) came from the desire to make AI technologies accessible and private, democratizing them for all. What It Does P8Hub (Private AI Hub) is a platform that allows you to host and manage your own AI services. It's designed to work with Docker, providing container configurations to run a wide range of AI services, such as generative AI, computer vision, natural language processing, and AI for STEAM education. Host and manage AI Services with No Code . Everyone can use P8Hub . No matter whether you are a business leader, an AI engineer, a software engineer, a hobbyist, a student, or a STEAM teacher. Ensure privacy and security. No data is leaked to online services. Everything lies inside your docker containers, volumes, inside your local machine. Installation and Demo 3 simple steps to use: Install Docker , Python . Install P8HUb: pip install p8hub . Run the application: python -m p8hub.app and your private AI dashboard is online at http://localhost:5678 . Just open your browser to visit the admin dashboard. View Fullsize Image Docker Extension (Experimental): You can install this package as a Docker Extension with the following command: make install-extension Note: The backend currently needs machine port 18180 to serve the backend APIs and the UI through HTTP. This may lead to port conflict on your machine and is not recommended by the Docker team ( Read more ). View Fullsize Image How I Built It The foundation of P8Hub lies in Docker / Docker Compose container configurations. These containers house the different AI services, making deployment and scaling easy and user-friendly. I designed a simple and intuitive user interface to manage these services, view logs, and monitor performance. Technologies I've used: NextJS/Tailwind/Shadcn for the UI. FastAPI for the backend. Docker on Whales for docker interactions. Docker Compose for packaging and running AI services. The Architecture: View Fullsize Image The architecture of P8Hub consists of two main components: a FastAPI backend and a Next.js frontend. The backend and frontend communicate with each other via REST API. For ease of deployment, I build frontend into static files and serve them from the backend. The interaction with Docker (running, stopping, and monitoring services) is done via Python on Whales package. The Architecture of P8Hub Docker extension: View Fullsize Image The P8Hub Backend is now run as a Docker extension backend , and the frontend assets are still served through the backend. I created a simple Docker extension frontend with an IFrame to show the UI. Challenges I Ran Into Timing: I have only the last 9 days of the Hackathon to finish the product. It was very challenging for me in terms of time. AI service deployment: Each AI service has its own configuration and settings for the Docker Compose. I had to ensure that the Docker configurations were not only compatible with various AI services but also user-friendly for individuals with varying levels of technical expertise. Some projects need some modifications to run with Docker. I had some difficulties when creating the Docker extension. That is the reason for the above design: First, as my understanding, the recommended way of creating a frontend is to serve your static assets by Docker Desktop. I followed this tutorial to deploy my front end but it failed even when I could package it as static files. The reason is that NextJS bundled assets need some AJAX requests to load different parts, which seems not to be supported by the Docker extension. Second, the communication between the backend and frontend should be sockets or named pipes to avoid port conflict ( read more ). However, it takes time to reimplement all the APIs with all the protocols (I want to keep the HTTP for deployment without Docker Desktop). Maybe we can get back to implementing this part in the future. I still cannot find a way to open links with the browser from the Docker extension front end. Accomplishments That I'm Proud Of I developed a working project in a short time from scratch. It seems easy to use. This is my first Hackathon on DevPost. Cheer for the finishing line! This project is my first Docker extension. What I Learned The development of P8Hub taught us a lot about the challenges of integrating various AI services in a single platform. I learned how to use Docker to simplify the deployment of these services. It's also the first time I heard about the Docker extension and wrote an extension. What's Next for P8Hub - Private AI Hub The future of P8Hub is focused on expanding its capabilities and improving user experience. There are many things to improve from the first version of P8Hub: Support more AI services by adding more Docker container configurations. The applications were not selected carefully due to limited time. I think many more interesting AI applications can be integrated into P8Hub. Support more platforms and hardware . Currently, the applications on P8Hub were only tested on the Apple M1 chip. We can add support for NVIDIA GPUs and other platforms to optimize performance and usability. Improve Docker extension: We can work more on the Docker extension to eliminate the use of HTTP connections, which can avoid port collision and can be used when the extension is operated in constrained environments. Additionally, I aim to create an app editor to provide the capability of modifying or creating custom AI apps. <div