---
slug: "txt2app"
url: "https://devpost.com/software/txt2app"
title: "Txt2App"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 886
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/web_dom"
---

# Txt2App

> Txt2App: Turn any idea into a fully functional mobile app, powered by LLM and Nvidia AI Workbench.

[Devpost](https://devpost.com/software/txt2app) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[legal_professional]]
**substrate** [[web_dom]]

**stack** cuda, fastapi, llm, nvidia-ai-workbench, ollama, python, react, react-native

## How they structured the write-up

- how to run:
- everything is fully explained step by step in our github:

## Body

Diagram Main UI App simulation building the APK Working on a Real device! Txt2App: Turn any idea into a fully functional mobile app, powered by LLM and Nvidia AI Workbench. Fastlinks: How to run: If you wish to run the Workbench on your machine follow this: TUTORIAL HERE Hi!, if you are a judge and want to review the code and the Nvidia Ai Workbench Container here are the links: Blog Post : Click here Nvidia Ai Workbench Container : inside HERE Video Demo : OPEN VIDEO Introduction: In an increasingly technology-driven world, the ability to develop mobile apps shouldn't be reserved for expert programmers only. Nvidia CEO Jensen Huang has highlighted the need to focus on learning prompt engineering rather than traditional programming, noting: "It is our job to create computing technology such that nobody has to program. And that the programming language is human." 1 LLMs provide the ability to process natural language input and text generation (not limited to natural language), which is an indispensable tool to achieve this goal. 2 The Nvidia AI Workbench offers a robust environment for the creation, training and optimization of container-based artificial intelligence models. Above all, it allows the use of resources both on the local machine and on external servers, facilitating rapid development from ready-to-work environments, thus accelerating development times. 3 Problem: Developing mobile applications presents several challenges: 4 Code Complexity : Mobile app programming involves writing and debugging code, which can be difficult without strong technical expertise. Diversity of frameworks, versions, and platforms : Ensuring that an application works optimally on different devices requires managing multiple versions and configurations, which can complicate the development process. UI/UX Design : Designing a good UI/UX that meets the expectations of users, who are already accustomed to established and current design patterns, can be an even more challenging task than developing the app's own backend. Current Solutions: Flutter Flow: This solution provides tools for interface design, but does not provide any AI capabilities. https://www.flutterflow.io/product Appypie: This text to app solution allows you to create applications with just a text prompt, however it requires a subscription, is closed source, and the demo provided by the page does not provide evidence of the use of AI. https://www.appypie.com/ UI Bakery: Although this page better demonstrates AI-based interface design, it does not provide any functionality to the app, only generating base designs. https://uibakery.io/ Solution: Introducing Txt2App , Huang's promise becomes a reality, accessible to everyone, democratizing application development and opening up new possibilities for technology creation thanks to Nvidia Ai Workbench and LLMs (Generative AI). Diagram and Summary: The general diagram of our solution is as follows, this is a summary of the services, but we will detail them later. Google Cloud VM: We are using a Google VM with the following features. OS: Ubuntu 24.04 LTS. GPU: Nvidia Tesla T4 (16Gb). RAM: 65 Gb. HDD: 500 Gb. vCPU: 10 cores. Nvidia AI Workbench: The Nvidia toolkit is used to perform rapid development and deployment of our application. https://docs.nvidia.com/ai-workbench/user-guide/latest/overview/introduction.html Ollama Server: We use the Ollama server service to run the LLM models used in the project. LLM Model: Deepseek Coder V2. https://ollama.com/library/deepseek-coder-v2 ReactJS: This was the web framework to create the project's UI, we used pure ReactJS without any additional framework. Main UI: This is the main interface of the project where the text window and the App preview are displayed. App Preview: This interface pre-renders the app for the user to test before converting it to APK. React Native: App Builder: Android Native Build is used to convert React code into Android native code. Fastapi: We use this framework to create the complete API of our application. Static Website: This section of the API is used as a server to display the UI from the browser. API: This section communicates the UI with the generation, preview and build services. Everything is fully explained step by step in our github: https://github.com/altaga/Txt2App Commentary: Txt2App is a groundbreaking solution designed to revolutionize the way mobile applications are developed. Leveraging the power of large language models (LLM) and Nvidia's AI Workbench, Txt2App enables users to turn any idea into a fully functional mobile app with ease. This innovative tool lowers the barriers to app development by automating many of the complex, technical tasks that traditionally require extensive programming knowledge. Whether you're an entrepreneur with a vision or a business looking for custom solutions, Txt2App simplifies the journey from concept to deployment. Empowering Users with Cutting-Edge AI By integrating Nvidia's AI Workbench, Txt2App harnesses cutting-edge machine learning models to interpret natural language inputs and generate corresponding app features. This means users can describe their ideas in plain text, and Txt2App will handle the heavy lifting of coding, UI/UX design, and backend infrastructure. This fusion of LLM and AI-driven technology drastically reduces development time, while ensuring that the final product meets high performance and functionality standards. A New Era for App Development Txt2App marks a significant shift in how applications are conceptualized, created, and delivered. It democratizes app development, making it accessible to non-technical users without compromising on the quality or complexity of the applications produced. As the world becomes increasingly mobile-centric, Txt2App opens doors for individuals and businesses to innovate and adapt swiftly, fostering a more inclusive and dynamic app ecosystem. References: https://www.forbes.com/sites/timbajarin/2024/03/20/nvidias-ceo-on-the-democratization-of-coding/ https://ai.meta.com/blog/meta-llama-3/ https://docs.nvidia.com/ai-workbench/index.html https://www.netguru.com/blog/mobile-app-challenges <div