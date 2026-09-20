---
slug: "infrablocks"
url: "https://devpost.com/software/infrablocks"
title: "InfraBlocks"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 842
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
---

# InfraBlocks

> Making cloud services what they were meant to be — simple.

[Devpost](https://devpost.com/software/infrablocks) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** cedar-os, nextjs, openai, radix-ui, react, tailwindcss, typescript, xyflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for infrablocks

## Body

Example Service Architecture InfraBlocks Inspiration Not so long ago, developers had to be part-time system administrators, managing physical servers in a data center. The cloud was a revolutionary promise: forget the hardware, and focus on your code. It was meant to make a developer's life simpler, allowing anyone to deploy an application with a few clicks. This was the dream—powerful infrastructure that was easy to use, accessible, and designed to accelerate innovation, not hinder it. However, that initial dream of simplicity has become lost in a sea of complexity. Today's cloud platforms have evolved into sprawling ecosystems where a single task requires navigating hundreds of specialized services. The barrier to entry has become immense, with developers needing to spend 60-80 hours and hundreds of dollars on certifications just to grasp the fundamentals. We've simply traded the complexity of racking physical servers for the equally daunting complexity of digital configuration. We believe the cloud's original promise is worth fighting for. That’s why we built InfraBlocks. Our mission is to cut through the noise and restore the simplicity that was lost. We are here to fulfill the dream the cloud first offered, making powerful infrastructure intuitive and accessible so that developers can get back to what they do best: building the future. What it does InfraBlocks is a visual, web-based tool that transforms complex cloud infrastructure management into a simple drag-and-drop experience. Users can visually construct their desired architecture by selecting and connecting service "blocks"—representing everything from virtual machines and databases to serverless functions. The magic happens when you press 'Deploy'. InfraBlocks automatically generates the necessary Infrastructure as Code (IaC) and provisions the resources on your chosen cloud provider. Furthermore, our integrated AI agent, Rex , takes simplicity to the next level. You can describe your needs in plain English, and Rex will automatically generate the corresponding block diagram for you, making deployment faster and more accessible than ever. How we built it We integrated Warp as our primary development environment, which was instrumental in building InfraBlocks. Its powerful, modern terminal streamlined our entire workflow, from managing the Next.js frontend to executing complex Terraform commands. Most importantly, Warp's agentic features provided the fine-grained control we needed to efficiently develop and debug our AI agent, Rex , consolidating our toolchain and saving significant development time. Frontend : We built a responsive and interactive user interface using Next.js with TypeScript for type safety and scalability. The UI components were crafted with Tailwind CSS and Radix UI for a modern and accessible design. Backend & IaC : The core of our provisioning engine is powered by Terraform . It allows us to reliably and consistently manage infrastructure across different cloud providers. AI Agent (Rex) : Rex is built on OpenAI's powerful language models and integrated using the Cedar-OS serves as the bridge between human intent and system execution, allowing Rex to not just suggest infrastructure changes but directly manipulate the application’s state. This enables real-time updates on the canvas, where blocks can be added, connected, or modified instantly based on user input. The framework enforces structured reasoning and consistency, ensuring that AI-generated infrastructure is valid, deployable, and aligned with best practices. Challenges we ran into Our two biggest hurdles were mastering Terraform and navigating Git merge conflicts . With Terraform , it wasn't just about learning the syntax; it was about deeply understanding underlying cloud architecture concepts, such as networking, security groups, and IAM roles. This forced our team to rapidly upskill in fundamental cloud engineering principles to ensure our generated infrastructure was robust and secure. Simultaneously, as multiple team members contributed code, resolving Git merge conflicts became a frequent challenge. It required us to establish a disciplined workflow and a clear branching strategy to integrate new features without disrupting existing code. Accomplishments that we're proud of We are incredibly proud of creating a fully functional visual editor that successfully translates a user's block diagram into deployable Terraform code. Integrating our AI agent, Rex, to intelligently generate these diagrams from a simple text prompt was a major milestone that truly brings our vision of a simplified cloud to life. Seeing a complex infrastructure stack get provisioned with a single click is a truly rewarding experience. What we learned This project was a deep dive into the world of Infrastructure as Code and cloud architecture. We not only learned the intricacies of Terraform but also gained valuable insights into how different cloud services interact. Building a project of this complexity also strengthened our skills in full-stack development, from creating a sophisticated frontend with Next.js to managing complex state on the backend. What's next for InfraBlocks The journey is just beginning. Our future roadmap includes: Multi-Cloud Support : Expanding beyond our initial provider to include GCP and Azure. More Blocks : Adding a wider variety of services to our library, including more advanced networking and machine learning components. Smarter Rex : Enhancing our AI agent to understand more complex requests and provide cost-optimization suggestions. Collaboration Features : Allowing teams to design and manage their infrastructure together in real-time. <div