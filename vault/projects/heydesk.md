---
slug: "heydesk"
url: "https://devpost.com/software/heydesk"
title: "SupportDesk"
hackathon: "TiDB AgentX Hackathon 2025"
organization: "TiDB"
winner: true
words: 1066
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# SupportDesk

> SupportDesk is an Agentic customer support platform that lets companies provide instant assistance via chat, manage tickets efficiently, and deliver 24/7 support without a large team.

[Devpost](https://devpost.com/software/heydesk) · hackathon [[TiDB AgentX Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** azure-openai, c#, rag, react, semantic-kernel, tidb-cloud

## How they structured the write-up

- what i learned
- how i built it
- what makes heydesk stand out
- challenges i faced
- the impact
- technical innovation
- tidb account email :

## Body

Knowledge-base Agents Landing Dashboard support portal Customer support is broken. Traditional ticketing systems are clunky, knowledge bases are hard to navigate, and customers often wait hours or days for responses. I envisioned a future where support is intelligent, proactive, and truly helpful - where AI agents don't just respond with canned answers, but actually understand context, search through knowledge bases intelligently, and provide meaningful solutions. Every customer interaction should feel like talking to your most knowledgeable team member- someone who knows your product inside and out, remembers previous conversations, and can instantly find the right information to solve any problem. What I Learned Building an agentic AI support platform solo taught me that context is everything . I learned that: Vector search alone isn't enough - you need to combine it with full-text search for comprehensive knowledge retrieval Multi-step workflows require careful orchestration between different AI services User experience drives adoption - even the most powerful AI is useless if customers can't easily interact with it Real-time communication through SignalR enables truly conversational support experiences Solo development requires wearing many hats - from database design to UI/UX to DevOps SDK development is crucial when official tools don't exist - I had to build a complete .NET SDK for TiDB Vector Search from scratch, Learnt alot about indexes and embeddings. How I Built It SupportDesk leverages TiDB Cloud's powerful vector and full-text search capabilities through a custom-built .NET SDK that I developed specifically for this project. Core Architecture Frontend : React + TypeScript with TanStack Router for seamless navigation Backend : .NET 9 with Entity Framework Core for robust data management Database : TiDB Cloud with vector embeddings and full-text search Custom SDK : TiDB.Vector.NET - A complete .NET SDK I built from scratch AI Integration : Azure OpenAI for intelligent responses and Exa AI for web search Real-time : SignalR for live chat and notifications The Custom TiDB Vector SDK Since there was no official .NET SDK for TiDB Vector Search , I built one from scratch: TiDB.Vector.NET . This SDK provides: Fluent Builder Pattern : Intuitive API for setting up vector stores Built-in AI Integration : OpenAI and Azure OpenAI support out of the box Advanced Filtering : Collection and tag-based filtering for multi-tenant applications RAG Capabilities : Simple AskAsync method for question-answering with source citations Type Safety : Full C# type safety with parameterized SQL queries Performance Optimized : Leverages TiDB's HNSW indexes and JSON optimization The Agentic Workflow Knowledge Ingestion : Websites and documents are automatically processed and embedded using my custom SDK Intelligent Search : When customers ask questions, the system performs both vector similarity search and full-text search across the knowledge base Context-Aware Responses : AI agents analyze search results, conversation history, and customer context to provide personalized responses Continuous Learning : Every interaction improves the system's understanding of customer needs Key Features Multi-tenant Architecture : Each organization has its own knowledge base and support portal Intelligent Ticket Routing : AI automatically categorizes and routes tickets to appropriate agents Real-time Chat : Customers can chat with both AI and human agents seamlessly Knowledge Base Management : Easy document ingestion from URLs, file uploads, or direct text input Agent Dashboard : Comprehensive tools for human agents to manage tickets and conversations What Makes HeyDesk Stand Out 1. Custom TiDB Vector SDK First-of-its-kind : No official .NET SDK existed for TiDB Vector Search Production-ready : Built with enterprise features like multi-tenant filtering Open source : Available to the community at TiDB.Vector.NET Performance optimized : Leverages TiDB's advanced vector indexing capabilities 2. True Agentic AI Architecture Multi-step workflows : Combines vector search, full-text search, and LLM reasoning Context-aware responses : AI remembers conversation history and customer context Intelligent routing : Automatically escalates complex issues to human agents Continuous learning : System improves with every interaction 3. Developer-First Approach Modern tech stack : Built with latest .NET 9, React 19, and TypeScript Type safety : End-to-end type safety from database to UI Real-time capabilities : SignalR for instant communication Docker-ready : Complete containerization for easy deployment 4. Enterprise-Grade Features Multi-tenancy : Complete isolation between organizations Scalable architecture : Handles thousands of concurrent users Security : JWT authentication, CORS protection, and data isolation Monitoring : Built-in health checks and status monitoring Challenges I Faced Building a Custom SDK : Creating a complete .NET SDK for TiDB Vector Search from scratch was incredibly challenging. I had to reverse-engineer the vector search capabilities, understand TiDB's SQL syntax for vector operations, and build a fluent API that developers would love. Solo Development Complexity : Building a full-stack application with multiple services, real-time features, and AI integration as a solo developer required careful planning and prioritization. Database Integration Complexity : Getting TiDB Cloud's vector search to work seamlessly with my .NET backend required deep understanding of TiDB's vector data types and indexing strategies. CORS and Deployment Issues : Deploying a full-stack application with separate frontend (Vercel) and backend (Digital Ocean) services required extensive CORS configuration and health monitoring. Real-time Communication : Implementing SignalR for live chat while maintaining security and proper authentication across different user types (customers vs. agents) was challenging. AI Response Quality : Ensuring AI responses are contextually relevant and helpful required fine-tuning prompt engineering and search result ranking algorithms. User Experience Design : Creating an intuitive interface that works for both customers (simple support portal) and agents (complex dashboard) while maintaining consistency was a significant design challenge. Time Management : Balancing feature development, testing, deployment, and documentation as a solo developer required efficient workflows and clear priorities. The Impact HeyDesk transforms customer support from a reactive, ticket-based system into a proactive, intelligent conversation platform . Organizations can now: Reduce response times from hours to seconds with AI-powered instant responses Improve customer satisfaction through context-aware, personalized support Scale support operations without proportionally increasing human agent workload Build comprehensive knowledge bases that actually get used and improved over time Leverage cutting-edge vector search through a custom-built .NET SDK Technical Innovation The TiDB.Vector.NET SDK I built represents a significant contribution to the .NET ecosystem: First .NET SDK for TiDB Vector Search Production-ready with enterprise features Open source and community-driven Performance optimized for high-scale applications Type-safe with full IntelliSense support *HeyDesk represents the future of customer support - where AI and human agents work together seamlessly to provide exceptional customer experiences through intelligent, context-aware conversations. TIDB Account Email : dev.manasseh@gmail.com <div