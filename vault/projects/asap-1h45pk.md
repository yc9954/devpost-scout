---
slug: "asap-1h45pk"
url: "https://devpost.com/software/asap-1h45pk"
title: "ASAP Knowledge Navigator"
hackathon: "Accelerate App Development with GitHub Copilot"
organization: "Microsoft"
winner: true
words: 5965
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "user/government_staff"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ASAP Knowledge Navigator

> Empowering industries with AI-driven insights through Retrieval Augmented Generation (RAG), simplifying complex tasks like Kubernetes diagnostics and SEC filings into actionable strategies

[Devpost](https://devpost.com/software/asap-1h45pk) · hackathon [[Accelerate App Development with GitHub Copilot]]

## Facets

**mechanism** [[benchmark_measured]] [[graph_reasoning]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: human_in_the_loop</sub>
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]] [[legal_justice]] [[media_journalism]] [[security_privacy]] [[supply_logistics]] [[transportation]]
**user** [[developer]] [[frontline_worker]] [[government_staff]] [[patient_family]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[regulation_legal_text]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** aifabric, aks, azure, c#, gpt-4o, kubernetes, semantickernel, service

## How they structured the write-up

- overview of projects
- inspiration
- what it does
- project components
- challenges we ran into
- what we learned
- what's next for asap knowledge navigator
- strategic validation of asap knowledge navigator
- - risk (continued): over-reliance on semantic search accuracy; mitigated by continuous refinement of prompt engineering, incorporating human-in-the-loop validation, and diversifying data used for vectorization.
- technologies used in asap knowledge navigator

## Body

ASAP-AzureKubernetesService-log-analyzer-RAG report on Kubernetes "ProviderFailed" error in ACI, including diagnostics and logs. GitHub issue #14 in ASAPKnowledgeNavigator: Failed Kubernetes pod "eraser-virtual-node-aci-linux-ks96c" with no container statuses. GitHub repository for GitHubActionTriggerCLI within ASAP Knowledge Navigator, showing project files and README. GitHub Issue: Pod failure analysis in progress. ASAP Knowledge Navigator: Resources overview with running containers and projects. ASAP Knowledge Navigator: .NET garbage collection metrics over 5 minutes. ASAP Knowledge Navigator: AI-powered EDGAR filing search and insights for TSLA. "ASAP Knowledge Navigator: TSLA's AssetsCurrent graph and risk factor insights." GitHub repository view of the ASAPKnowledgeNavigator project, showing the main project structure and README. First page of Tesla, Inc.'s 10-K annual report for 2023 (PDF), showing standard SEC filing information. sec-edgar tool in action: Retrieving TSLA's CIK and downloading its 2023 10-K report. GitHub repository view of SEC-RAG-Navigator-db within ASAP Knowledge Navigator, showing project structure and README. SEC-RAG-Navigator-db help output, showing available commands like create-container and knowledge-base-search. SEC-RAG-Navigator-db initializing connection to Azure Cosmos DB and retrieving database/container information. SEC-RAG-Navigator-db processing Tesla's 10-K PDF, adding pages as knowledge base items to Cosmos DB. SEC-RAG-Navigator-db performing semantic search for "Risk Factors" in Cosmos DB, returning relevant document excerpts. ChatService in SEC-RAG-Navigator-db summarizing "Risk Factors" from Tesla's 10-K (pages 121, 45, and 39). GitHub issue: ACI provider pod failure analysis and review. Connects to your Kubernetes cluster for log retrieval and AI-powered analysis. GitHub Action triggers to post AI-driven findings as repository issues. Review Kubernetes pod analysis results posted as GitHub issues. Kubernetes pod configuration for AI-driven log analysis GitHub Copilot generates and refactors Kubernetes analysis code. AI-powered Kubernetes log analyzer for seamless AKS integration.Automated log collection and intelligent analysis for Kubernetes clusters. Automated log collection and intelligent analysis for Kubernetes clusters. GPT transforms log data into actionable insights for anomaly detection. ASAP SEC-RAG Navigator: AI-driven solution for SEC filing analysis Core features: SEC filing management, AI-driven insights, and natural language querying. SEC-RAG Navigator Workflow: Data retrieval to actionable insights. Fetch latest Tesla 10-K filing via EDGAR. Upserting Tesla 10-K into Cosmos DB. EDGAR Research Assistant leveraging .NET 9 and Azure ASAP Knowledge Navigator: Revolutionizing Knowledge Retrieval and Insight Generation with RAG Transforming industries by delivering actionable insights through Retrieval-Augmented Generation (RAG) , simplifying complex challenges such as Kubernetes diagnostics and SEC filings into intelligent strategies. Overview of Projects ASAP Knowledge Navigator is a comprehensive initiative composed of three primary projects, each targeting specific challenges and applications: ASAP SEC-RAG-Navigator: Command-Line Tools Tools to streamline SEC EDGAR filings retrieval, analysis, and management using RAG and advanced AI. ASAP Knowledge Navigator - .NET 9 Aspire Project A robust .NET 9-based platform offering intuitive user interfaces and natural language search capabilities for SEC filings. ASAP-AzureKubernetesService-Log-Analyzer-RAG: Command-Line Tools Tools focused on Kubernetes pod failure detection, analysis, and issue resolution through semantic log analysis and RAG techniques. Inspiration The ASAP Knowledge Navigator project was created to showcase how Retrieval-Augmented Generation (RAG) can transform knowledge retrieval and insight generation across various industries. From streamlining the analysis of regulatory filings such as SEC EDGAR to simplifying technical operations like Kubernetes management, this versatile tool proves its value in diverse applications. By combining RAG with Azure's robust infrastructure, the platform leverages scalable computing power, seamless integration capabilities, and enterprise-grade security to tackle complex challenges with advanced AI. This combination ensures efficient, actionable solutions tailored to specific industry needs. EDGAR and Kubernetes are just two examples of the many ways ASAP Knowledge Navigator can make a meaningful impact. Addressing Common and Domain-Specific Challenges Through AI and Automation The ASAP Knowledge Navigator tackles diverse challenges by leveraging its core strengths of automation, AI-driven insights, and optimization to address both common and domain-specific pain points. Whether streamlining SEC EDGAR filings analysis or simplifying Kubernetes management, the platform demonstrates its adaptability across industries. For SEC EDGAR filings, ASAP Knowledge Navigator showcases its strength in managing complex financial and regulatory data. It automates manual data extraction, reducing time and effort for analysts. With AI-powered analysis, the platform simplifies the interpretation of financial information, while real-time updates keep users informed about regulatory changes. In contrast, for Kubernetes, the platform addresses the technical complexities of system operations. It automates the detection and resolution of pod failures, minimizing downtime and enhancing reliability. Additionally, it streamlines configuration and management with AI-driven insights and optimizes resource utilization to lower costs. The platform also bolsters security by implementing best practices and leveraging AI to identify and mitigate potential threats. What ties these use cases together is the platform’s ability to automate repetitive tasks, generate actionable insights, and optimize processes. At the same time, it tailors its solutions to the unique needs of each domain, whether addressing the regulatory complexities of SEC filings other the technical intricacies of Kubernetes. This versatility showcases how ASAP Knowledge Navigator effectively adapts to diverse industries while maintaining its core value of efficiency and precision. Addressing SEC EDGAR Filings Pain Points: Manual Data Extraction: ASAP Knowledge Navigator automates data extraction, saving time and effort. Complex Financial Data: AI-powered analysis simplifies the understanding of complex financial data. Staying Updated with Regulatory Changes: The platform provides real-time updates on SEC regulations and filings. Addressing Kubernetes and SEC Pain Points Complex Configuration and Management: ASAP Knowledge Navigator simplifies Kubernetes management through automation and AI-driven insights. Pod Failures and Troubleshooting: The platform automates the detection and resolution of pod failures, reducing downtime. Resource Utilization and Optimization: AI-powered optimization techniques help improve resource utilization and reduce costs. Security and Compliance: The platform incorporates security best practices and leverages AI to identify and mitigate threats. What It Does How ASAP Knowledge Navigator Leverages RAG for Enhanced Knowledge Retrieval ASAP Knowledge Navigator employs Retrieval-Augmented Generation (RAG) to elevate knowledge retrieval and insight generation. It combines the strengths of advanced retrieval techniques with the generative capabilities of large language models (LLMs). This synergy allows ASAP Knowledge Navigator to go beyond traditional knowledge retrieval methods, offering a more intelligent and comprehensive approach to information access and analysis. Instead of simply retrieving documents based on keywords, ASAP Knowledge Navigator utilizes RAG to understand the context and intent behind user queries. This enables the platform to: Access and synthesize information from diverse sources: RAG enables the platform to connect to various data repositories, including internal documents, databases, and external knowledge sources. This provides a comprehensive view of information, enabling more holistic analysis. Deliver precise and relevant answers: By retrieving contextually relevant information from a vast knowledge base, ASAP Knowledge Navigator minimizes errors and inaccuracies, ensuring reliable and trustworthy insights. This reduces the risk of misinformation. Generate personalized responses: RAG allows the platform to consider user preferences, needs, and context, tailoring responses and recommendations for a more personalized experience. This increases user satisfaction. Provide deeper understanding and insights: By grounding AI responses in factual information and identifying relationships within data through contextual data enrichment and knowledge graphs, ASAP Knowledge Navigator facilitates more insightful analysis and decision-making. This contextual understanding helps the AI models generate more accurate and relevant responses. Furthermore, by enhancing prompts with relevant context from the knowledge graph, ASAP Knowledge Navigator ensures that the AI models have the necessary information to generate precise and insightful answers. Reduce hallucinations and improve accuracy: By validating AI-generated responses against a knowledge model, ASAP Knowledge Navigator ensures the reliability and trustworthiness of information. This minimizes the risk of AI "hallucinations" or generating factually incorrect information. AI-Driven Analytics with ASAP Knowledge Navigator ASAP Knowledge Navigator leverages AI-driven analytics to provide users with deeper insights and more efficient analysis capabilities. This approach is particularly valuable in complex domains like Kubernetes diagnostics and SEC EDGAR filings analysis. By applying AI algorithms and machine learning models, ASAP Knowledge Navigator can: Identify patterns and anomalies: AI-driven analytics can detect subtle patterns and anomalies in data that might be missed by traditional analysis methods. This enables proactive identification of potential issues and risks. Predict future trends: By analyzing historical data and identifying trends, AI algorithms can provide insights into future trends, enabling organizations to anticipate challenges and opportunities. Automate data analysis: AI can automate various data analysis tasks, such as data cleaning, normalization, and feature extraction. This frees up human analysts to focus on higher-level tasks. Generate actionable insights: AI-driven analytics can translate complex data into actionable insights, providing users with clear and concise recommendations for decision-making. ASAP Knowledge Navigator for SEC EDGAR Filings Analysis Analyzing SEC EDGAR filings can be a time-consuming and complex task. ASAP Knowledge Navigator can streamline this process by: Automating the retrieval and processing of EDGAR filings: This eliminates the need for manual searches and data extraction, saving time and resources and allowing analysts to focus on higher-level tasks. Extracting key information and identifying trends: ASAP Knowledge Navigator can analyze filings to identify relevant data points, such as financial performance, risk factors, and corporate governance information. This provides a comprehensive view of a company's financial health and operations. Financial Performance Metrics: Automatically extracts and analyzes key financial data, including revenue, profit margins, earnings per share (EPS), and other relevant indicators. Risk Factors: Identifies and categorizes potential risks disclosed in the filings, such as market risks, competitive risks, regulatory risks, and operational risks. Management Discussion and Analysis (MD&A): Processes and summarizes management's perspective on the company's financial condition, results of operations, and future prospects. Corporate Governance Information: Extracts details about the company's board of dir