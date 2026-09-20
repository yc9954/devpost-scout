---
slug: "scavene"
url: "https://devpost.com/software/scavene"
title: "Scavene"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 753
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
---

# Scavene

> Enhance your NEAR smart contract security with Scavene, the audit tool that detects vulnerabilities and ensures best practices.

[Devpost](https://devpost.com/software/scavene) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]

**stack** ai, ci/cd, githubaction, langchain, python, rag

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scavene

## Body

landing page scavene on github action marketplace vulnerability report action process #1 action process #2 Inspiration The increasing use of smart contracts is undeniable, and their ability for autonomous execution offers significant advantages, such as reduced costs and increased efficiency. Furthermore, smart contracts provide a decentralized system granting users greater control and eliminating third-party manipulation risk. However, despite these benefits, the efficacy and security of smart contracts are intrinsically linked to the quality and precision of their underlying code. Even seemingly small weaknesses in smart contract logic can pose major risks if exploited by malicious actors. For example, a major cyberattack incident on Binance BNB Bridge in October 2022 resulted in a loss of $566 million due to a smart contract bug. These incidents underscore the critical need for robust blockchain security. Therefore, mitigating the risk of such attacks is important to ensure the security and integrity of smart contracts. One crucial measure is conducting thorough smart contract audits. Such audits not only enhance security but also reassure investors and users that the contract will function as intended, thereby reducing the risk of future threats and cyberattacks. However traditional smart contract audits, while valuable, can be costly and time-consuming, potentially creating a barrier for early-stage projects. Furthermore, the continued introduction of new vulnerabilities requires constant awareness. As a result, continuous auditing is highly desirable, as it ensures that all code is thoroughly tested for security prior to release. For these reasons, I created Scavene, with the goal of making smart contract audits accessible and effective for everyone, regardless of project size or stage. What it does Scavene uses an AI-powered smart contract auditor that is specifically built for NEAR smart contracts. It uses language models and a knowledge library to automatically scan code for vulnerabilities, security concerns, and deviations from standard practices. As a result, Scavene provides insight that allows developers to detect and resolve any issues quickly and efficiently. Furthermore, it connects smoothly with existing development workflows via GitHub Actions or may be operated locally. How we built it Scavene was built using Python for easier interaction and native support with Large Language Models (LLMs). Currently, it only supports OpenAI and Anthropic models. However in future development, it will include support for custom and local models, for flexibility and customization. Furthermore, to improve model accuracy and provide more context, Scavene uses Retrieval Augmented Generation (RAG). This technique employs a knowledge base of NEAR-specific vulnerabilities, which is accessed via FAISS (vector store) and embedding mechanism, allowing the model to give a more targeted and relevant analysis. Challenges we ran into During the development of Scavene, one of the primary challenges was maintaining and improving the quality of the audit results. Smart contract security is a domain where accuracy is important, and finding the right balance between detection sensitivity and precision is complex and challenging. The process of tuning the AI model needs constant iteration and adjustment to ensure it can effectively identify potential vulnerabilities while minimizing false positives. False positives were also a persistent challenge. While it's better for a security tool to be overly cautious, too many false alarms can reduce the tool's practical utility and user trust. The other challenge was testing scavene in more advanced and complex smart contracts. Advanced smart contracts often incorporate sophisticated logic and AI is usually bad at complex tasks. This highlighted the need for continuous learning and adaptation of the system to handle more complex scenarios. Accomplishments that we're proud of Using RAG and knowledge base to improve its audit result Integrate this tool with GitHub action to run automatically on the repo We’re currently testing this tool with the smart contract developer to get their insight and feedback about this tool What we learned A major lesson learned came when I implemented Retrieval-Augmented Generation (RAG), which significantly enhanced the model context awareness. Another important lesson was that model fine-tuning is gradual, even a 1% improvement matters significantly in security auditing, as it could mean detecting an additional vulnerability that might prevent substantial financial losses. What's next for Scavene Enhancing our knowledge base with new vulnerability patterns, security issues, and best practices Developing more advanced report and visualization tools for audit results Continuously improving the current model fine-tuning and supporting another model (local and custom) Expand support for another blockchain smart contract In the future, I aim to add another feature, not just auditing, but also creating, deploying, and reviewing. From there, Scavene can be a hub for developers to interact with smart contracts. <div