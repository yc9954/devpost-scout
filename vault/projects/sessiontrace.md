---
slug: "sessiontrace"
url: "https://devpost.com/software/sessiontrace"
title: "SessionTrace"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 828
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# SessionTrace

> Never lose track of where you left off

[Devpost](https://devpost.com/software/sessiontrace) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[graph_reasoning]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[health_clinical]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]

**stack** .net, c#, claude-code, copilot, esbuild, github, javascript, json, logitech-actions-sdk, logitech-options+, mx-creative-console, mx-master, node.js, npm

## How they structured the write-up

- inspiration
- the core idea
- extending to hardware
- how we built it
- challenges we faced
- what we learned
- vision beyond this project

## Body

Inspiration Our inspiration came from ourselves. Every developer has experienced that moment, including us. It is late. You are deep into debugging. You switch branches. You fix something unrelated. You step away. When you return, you cannot remember the exact state you were in when everything made sense. Or you hand off work to a teammate and later realize you cannot reconstruct what the project looked like at that moment. We realized something important: Developer context is one of the most valuable resources in software development. Git tracks code changes. But nothing tracks session state: Which files were open Where the cursor was What branch you were on What errors were present What decisions were captured as notes We wanted to build the session tracer every developer wishes they had. The Core Idea SessionTrace is a Logitech Options+ Plugin and VS Code extension that allows developers to save rich snapshots of their entire working session with a single shortcut. Each snapshot captures: Open file tabs Cursor positions Git context and branch Changed files Live diagnostics (errors and warnings) Custom notes & reminders Attached code selections It also includes built-in reminders with priority levels, so developers can track what matters directly alongside their session history. Developers can later resume any snapshot and instantly restore their workspace to that exact state. Through a unified Panel and searchable timeline view, they can: Browse session history Review notes Manage reminders Generate AI summaries Generate teammate handoffs Draft PR descriptions Instead of reconstructing context manually, developers restore it instantly. If we think about productivity as: $$ \text{Productivity} = \frac{\text{Focused Work Time}}{\text{Total Work Time}} $$ Then every minute spent reconstructing context reduces productivity. SessionTrace reduces that reconstruction time toward zero. Extending to Hardware We asked a bigger question: What if saving and restoring context could be physical? We extended SessionTrace to Logitech hardware using: MX Creative Console MX Action Ring By integrating SessionTrace with these devices, we turned them into physical control surfaces for developer memory. With hardware: One button press saves a full session snapshot Another loads a previous checkpoint A key generates an AI summary A dial rotates through contextual actions A button drafts a pull request A button adds a reminder Instead of opening command palettes or searching through menus, developers act directly. The hardware becomes the bridge between thought and execution. How We Built It VS Code Extension SessionTrace was built in: TypeScript (strict mode) Using only VS Code APIs Zero third-party dependencies Bundled with esbuild for fast activation Key systems include: Filesystem-based session storage in .sessiontrace/ Git context detection via VS Code Git API (CLI fallback) Diagnostic snapshots via vscode.languages.getDiagnostics() AI generation via vscode.lm.selectChatModels() (GitHub Copilot) Timeline-based session memory panel Snapshots are stored per user, versioned, and organized for long-term reliability. Logitech Plugin On the hardware side, we built a plugin using the Logitech Actions SDK in C# . The plugin: Registers custom hardware actions Maps hardware triggers to SessionTrace commands Handles cross-platform behavior (Windows and macOS) Sends OS-level shortcut events to VS Code Includes configuration and logging This created a seamless bridge: Hardware Button → Logitech SDK → SessionTrace Command → Context Restored No modification of VS Code internals. No firmware changes. No invasive integrations. Just clean, focused extension + hardware control. Challenges We Faced 1. Cross-Platform Reliability We had to carefully handle: Windows vs macOS filesystem differences Git detection edge cases Workspace identity resolution Extension lifecycle behavior Ensuring consistent behavior across operating systems required disciplined testing. 2. Bridging Two Worlds The VS Code extension is written in TypeScript. The Logitech plugin is written in C#. This meant working in two very different development models: Event-driven extension host APIs Logitech’s hardware action registration model OS-level keyboard simulation We had to think clearly about responsibility boundaries: Extension handles state and logic. Plugin handles physical triggers. 3. Context Is Subtle Capturing context is not the same as summarizing code. We learned that restoring: Open files Cursor locations Diagnostics Branch state Notes is far more powerful than generating a summary alone. True developer productivity is not just about automation, it is about restoring mental state. What We Learned Through this project, we learned that: Restoring context is more valuable than navigating faster. Hardware can meaningfully reduce cognitive friction. Physical interaction reduces micro-interruptions. Developer memory is an underserved problem space. SessionTrace demonstrates how Logitech’s ecosystem can assist developers by transforming the MX Creative Console and MX Action Ring into interfaces for preserving and acting on knowledge. Vision Beyond This Project Our vision goes beyond SessionTrace. This project shows how Logitech hardware can become a universal control layer for software. Saving state, triggering AI, and restoring context should not be limited to one IDE. It could work across: IDEs Design tools Project managers Data science notebooks 3D modeling software Writing environments Any application where meaningful moments matter SessionTrace is just the first proof of concept. The larger idea is this: Hardware should not just control tools. It should preserve and restore knowledge. <div