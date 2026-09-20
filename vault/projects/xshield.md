---
slug: "xshield"
url: "https://devpost.com/software/xshield"
title: "xShield"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 1249
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/security_privacy"
  - "user/developer"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# xShield

> Introducing xShield,an AI-powered tool for easy code security and compliance analysis.Analyze entire repositories or commits for peace of mind. Fast, smart, and effortless security with a single click

[Devpost](https://devpost.com/software/xshield) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]] [[security_privacy]]
**user** [[developer]] [[educator_student]] [[legal_professional]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** aiworkbench, docker, javascript, langchain, llm, nvidia, python, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into & how we fixed it
- accomplishments that we're proud of
- what we learned
- what's next for xshield

## Body

Intro Infrastructure Pipeline Vulnerability Report Compliance Report Inspiration Whether you're a solo developer, part of an enterprise, or a student, everyone deserves secure code. As a software engineering student, I aimed to streamline the development-to-deployment process by tackling code issues early on. Inspired by large language models (LLMs), this project focuses on detecting and fixing vulnerabilities, ensuring data security, and verifying regulatory compliance before staging code for deployment. This approach helps developers and reviewers catch issues early, saving time and improving productivity while ensuring software compliance. Now solo developers and small teams can also have access to advanced AI tools for Code security checks and Compliance checks usually available only to enterprises through large security teams. For enterprises, this is especially useful since multiple software engineering projects can sometimes allow certain security issues to slip through. With this additional layer of security, companies can be more confident in their code security and compliance. What it does XShield scans your repository—either the entire codebase or just the latest commit—for vulnerabilities and compliance issues using an LLM Infrastructure. These scan can be executed through our web interface or via API calls integrated into your CI/CD pipeline using GitHub Actions. It generates a detailed report, enabling developers and reviewers to address issues before the code is deployed. Currently XShield offers multiple LLMs such as Hermes Llama 3 and GPT4 for users to choose for their code analysis. All of this is can be simply done in the xshield website, by simply putting the github repo url and a click of a button. XShield handles all the security and compliance checks and presents the user with an easy to read and manage report. Moreover, xShield is integrated with Static Application Security Testing tool such as (Bandit for Python) making its vulnerability and security detection more robust by giving the LLMs more context and additional layers of analysis. How we built it Handling large code repositories can be a challenge due to token limits in LLMs. To overcome this, we created a LangChain-based LLM pipeline where each code file is processed individually. The LLM generates a concise summary of each file’s functionality and dependencies. Once all summaries are complete, we combine them to build a compact representation of the entire repository. Next, we perform context analysis using the LangChain pipeline. The content of each file, along with its functionality and dependency map, is analyzed by the LLM to determine which other files are needed for a complete analysis. So when one file is being analyzed, all the related and dependant files are pulled by the LLM for a more comprehensive and contextual check. The LLM then provides a JSON response containing the relevant files for review. For vulnerability detection, xShield also uses a Static Application Security Testing tool to generate a security check report, to give to the LLM more knowledge about the issues that can be detected by existing tools. This static analysis tool runs independently on the user repository container giving the users the ability to implement any tool that fits their needs. Finally, the LLM processes this refined context to check for code vulnerabilities or data compliance. This LangChain-based flow allows us to scan entire repositories with improved accuracy and context-awareness. On the infrastructure side, we built XShield using Node.js microservices, each running in isolated containers. When a user subscribes their repository to the service, a new container is created on the fly with its own lightweight server. This ensures isolation and security for storing user code and sensitive data. The LLMs are also containerized, giving us the flexibility to use different models for security analysis based on client requirements. XShield is now developed and deployed using Nvidia AI Workbench. Since xShield is a multicontainer application we leveraged the compose feature of the AI Workbench to manage and run all of the services in different containers. To start the entire infrastructure, users just have to click on the start button in the compose section in the Environments menu. We recommend connecting AI Workbench to a cloud server with a high performance GPU such as Nvidia H100 since the AI Service uses local LLMs. Challenges we ran into & How we fixed it LLM's can sometimes be unpredictable, since we were dealing heavily with structured data, the llm's sometimes provided incorrect json response which ended breaking our web application during parsing. To encounter this issue, we used json fixing libraries and also more stable LLM's such as GPT4 to perform JSON fixing. This was a very effective solution to provide a stable and fluent experience. Initially we were manually deploying all the docker containers using shell scripts. This was a manual and tedious user experience. But through the valuable feedback of the judges, we were able to streamline this deployment by leveraging the compose feature of the AI workbench. We also had to redesign our application to support this new development and deployment using AI Workbench. Now our entire application is developed and deployed fully using Nvidia AI workbench and its compose feature. Accomplishments that we're proud of We successfully developed a robust, AI-driven code security and data compliance platform that combines LLM-based analysis with Static Application Security Testing (SAST) tools. This approach creates a comprehensive, adaptable security infrastructure for identifying and fixing security and data compliance issues that can support solo developers, teams, and enterprises alike. Our major achievements include overcoming the challenge of large code files and their dependencies by designing a custom LLM pipeline. This pipeline analyzes each file independently, builds a dependency map, integrates SAST reports, and provides a full-context security assessment. This method allows XShield to accurately and efficiently assess security vulnerabilities across complex codebases. Additionally, we’re proud of our integration with tools like Bandit, which enhances the LLM’s accuracy by adding detailed static analysis data. This fusion of SAST tools and LLM capabilities opens up exciting possibilities for improved security analysis, demonstrating a novel approach that leverages the strengths of both technologies. What we learned LLMs are incredibly versatile! They can do so much more than just answer queries. We discovered the unlimited potential of LLM pipelines when integrated with other services. While this demo showcases a simple implementation, larger and more specialized LLMs can detect vulnerabilities in insecure libraries b and even design patterns. We're proud of creating this LLM-based infrastructure, as it was a challenging yet rewarding experience. Special thanks to Docker containers and NVIDIA AI Workbench for making the deployment and setup process much easier! What's next for XShield While XShield offers robust security and compliance checks, there are several areas for improvement: Enhanced Policy Integration with RAG: We aim to integrate Retrieval-Augmented Generation (RAG) to allow more extensive policy files and handle complex security requirements. Larger Models and Fine-Tuning: We plan to incorporate larger language models and fine-tune them on Common Weakness Enumeration (CWE) datasets for deeper analysis and better-targeted security recommendations. Currently for this demo, we have integrated SAST tools to analyze python files effectively. In the future we would like to integrate multiple language SAST tools to provide a more robust security check experience or allow the users to use their SAST tool of choice. While users can modify the SAST tool by changing the containerTest repo, in the future we plan to make this process more intuitive and streamlined. Due to time constraints in the hackathon, our focus was primarily on integration and infrastructure. However, these improvements are on our roadmap to further enhance XShield’s performance and versatility. <div