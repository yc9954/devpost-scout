---
slug: "refnet-c04g9n"
url: "https://devpost.com/software/refnet-c04g9n"
title: "RefNet"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 1084
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# RefNet

> RefNet is an all-in-one platform to search, visualize, and analyze research papers with AI-powered insights, citation graphs, notes, and seamless exports — making literature review faster and smarter.

[Devpost](https://devpost.com/software/refnet-c04g9n) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[scientific_research]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** cedar, css3, d3.js, flask, javascript, openalex, python, react, tailwindcss

## How they structured the write-up

- our inspiration
- what refnet does
- how we built it
- challenges building refnet
- accomplishments that we’re proud of
- what we learned
- what’s next for refnet

## Body

RefNet's Landing Page Scholary article recommendations based on search references using OpenAlex Interactive Graph with floating sticky notes MLA citation feature with 3 different types of export features CedarOS manipulating the frontend Our Inspiration As student researchers working in different labs, one thing we all shared was the dread of doing literature reviews. Digging through papers, figuring out who cited who, tracking research trends, and then manually putting citations into a manager always felt like a time sink that slowed down actual research. We wanted to make a tool that would let us spend less time juggling PDFs, reference managers, and citation networks — and more time thinking about the science itself. RefNet was born from that frustration: a platform to search, visualize, and analyze research papers in one place, making literature review not just easier, but actually kind of fun. What RefNet does RefNet is a comprehensive research paper search and citation network visualization platform built for researchers, by researchers. It takes the scattered, tedious parts of the research workflow and brings them together into one seamless system. Here’s what you can do with RefNet: 1. Powerful Search & Import Search OpenAlex’s massive academic database by title, authors, keywords, or fields. Sort and filter results by citations, relevance, or publication date. Import saved graphs from JSON files to pick up right where you left off. 2. Interactive Graph Visualization (D3.js) Explore citation networks where nodes = papers and edges = citations. Node size reflects citation count, color reflects publication year, and arrows show citation direction. Select papers to highlight their connections, drag nodes to rearrange, zoom/pan, and dynamically expand graphs with reference/citation depth controls. 3. Cedar OS for Direct Frontend Manipulation with AI Cedar OS is a floating AI research assistant that lives directly on your graph. Unlike static “chat-with-a-paper” tools, it’s fully integrated with both the frontend and backend, serving as a dynamic bridge between your research context and intelligent analysis. How it works: Mastra-Powered AI Backend: Cedar OS connects to a Node.js server orchestrated by Mastra, which integrates with GPT-4o. Mastra acts as the “conductor,” feeding Cedar OS context about your selected papers, the graph structure, and even your notes. Direct Frontend Manipulation: Cedar OS isn’t just text. It can highlight nodes, rearrange graph layouts, and even add newly discovered papers directly to your network. When the AI suggests a bridging paper or related work, you see it appear right in the visualization. Context Awareness: Every query Cedar handles is scoped to your current graph state. It knows which papers are selected, how they connect, and what themes are emerging. What Cedar OS can do for you: Single Paper Deep Dive: Summarize methodology, findings, and key contributions. Comparative Analysis: Compare multiple papers side-by-side, highlighting differences in approach, datasets, or conclusions. Pattern Recognition: Spot recurring methods, research gaps, or influential authors across your graph. Intelligent Note Integration: Cedar OS can pull in your whiteboard notes, rephrase them, and even link them back to papers in your graph for richer context. In short, Cedar OS turns RefNet from a passive visualization into a living research partner. It understands your graph, reshapes it with new discoveries, and helps you see not just what exists, but what matters. 4. Notes & Whiteboard Environment Create, drag, resize, and color-code text boxes right on the graph. Use 16+ predefined colors for categorization and modern glassy overlays to organize your thoughts. Persistent styling makes it easy to keep track of research themes. 5. Export Made Simple JSON for full graph state (this gives you the ability to save graphs and share them with collaborators). BibTeX for selected papers (direct reference manager compatibility for platforms like Zotero). PNG high-quality screenshots of your annotated graph for presentations. Review Paper PDF of selected nodes with references to sources, used to build general knowledge on a subject using GPT-powered summarization. How we built it Our stack combines performance, scalability, and seamless user experience: Frontend: React 18, D3.js for graph visualization, Tailwind CSS, and Cedar OS overlay. Backend: Flask API to fetch and process OpenAlex data, with NetworkX powering graph analysis. AI Backend: Node.js with Mastra orchestrating GPT-4o for intelligent analysis and paper discovery. Data Source: OpenAlex API, giving us access to millions of up-to-date academic papers. Data Flow: User searches → Flask fetches & structures OpenAlex data → Frontend builds papers. Graph expands via citation networks processed in NetworkX → rendered with D3.js. Selected papers → Mastra backend → GPT-4o → Cedar OS surfaces insights and manipulates the graph. Export tools handle JSON/BibTeX/PNG/PDF workflows. Challenges building RefNet Citation graph scale: Some papers had thousands of references. We had to carefully design depth/limit controls to keep graphs usable. Real-time performance: Rendering large graphs in D3.js while supporting drag, zoom, and dynamic expansion took careful optimization, preventing excessive loading times. AI context handling: Making GPT-4o “understand” not just single papers, but their relationships in the graph, required custom orchestration in our Mastra backend. Frontend-AI connection: Teaching Cedar OS to not only talk but also act (highlight nodes, expand the graph) was a new design challenge that pushed us into territory beyond normal chatbot integrations. Hybrid Deployment: Deploying the Flask + Mastra backend on AWS EC2 while hosting the React frontend on Vercel created challenges in networking, CORS configuration, and API gateway routing. We had to carefully balance performance, scalability, and security across two platforms to ensure smooth cross-service communication. Accomplishments that we’re proud of Built a smooth, interactive graph explorer that makes navigating thousands of citations intuitive. Integrated AI-powered Cedar OS that directly manipulates the graph, bridging chat and visualization. Created a one-click export workflow that plays nicely with Zotero, BibTeX, and common citation styles. Designed a whiteboard-like notes system so researchers can contextualize findings as they explore. Enabled sharing JSON versions of graphs with other researchers to foster collaborative research. What we learned Literature review is less about “finding papers” and more about understanding connections. AI becomes exponentially more useful when it’s embedded in context, not siloed off. Researchers need tools that adapt to them — that means intuitive controls, instant feedback, and seamless data flow. What’s next for RefNet Collaboration Mode: Real-time shared graphs so lab teams can explore literature together. Custom Citation Styles: Beyond MLA, allow users to define their lab’s or journal’s style. More AI Features: Automatic paper summarization into slides, clustering papers by methodology, and multilingual support. Agentic Cedar OS: Let Cedar actively drive research sessions — dynamically expanding graphs, clustering papers, and surfacing recommendations without explicit prompts. <div