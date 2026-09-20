---
slug: "change-scribe"
url: "https://devpost.com/software/change-scribe"
title: "Change Scribe"
hackathon: "Accelerate App Development with GitHub Copilot"
organization: "Microsoft"
winner: true
words: 1132
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Change Scribe

> An AI-powered VS Code extension that automatically generates semantic changelogs from code changes and commits, saving hours of documentation time while ensuring clear communication of code changes

[Devpost](https://devpost.com/software/change-scribe) · hackathon [[Accelerate App Development with GitHub Copilot]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[structured_db]]

**stack** azureopenai, gemini, git, openai, typescript, vsce, vscode

## How they structured the write-up

- inspiration
- the early days
- the evolution
- github copilot: the game changer
- azure openai: the testing ground
- what's next

## Body

Inspiration As a developer juggling multiple large projects simultaneously, working in teams with different coding styles in a fast-paced environment, I faced a common challenge: maintaining clear, up-to-date documentation of code changes. Lost in the flow, I often hesitate to stop and document each change. By the time I’m done, there’s a mountain of changes that are hard to recall or prioritize. Important updates end up missing, or I have to spend extra time retracing my steps. Working in teams with different coding styles and priorities, I’ve seen how this lack of clear documentation can lead to confusion, missed deadlines, and even code conflicts. I’ve also seen how this lack of transparency can lead to frustration and wasted time. This is a common issue for many developers, especially in fast-paced environments. Traditional changelog maintenance is time-consuming and often overlooked in the rush to complete features. This pain point inspired Change Scribe - an AI-powered VS Code extension that automatically generates semantic changelogs from git commits, ensuring teams stay informed about codebase evolution without manual documentation overhead. The Early Days The initial version of Change Scribe, then called "Literate," focused on basic changelog generation using OpenAI's GPT models. It supported both OpenAI and Azure OpenAI services, featuring: Basic git commit parsing with commit message extraction Simple changelog generation in Keep a Changelog format Limited format support with fixed sections Basic error handling for API and git operations Progress indicators for generation, saving, and committing While functional, it lacked the robustness needed for diverse development environments and changelog formats. It had a hard time handling complex commit messages and changelog formats. It also faced performance issues with large repositories or commit histories. A core limitation was that it had basic git integration without detailed change tracking. The Evolution During the hackathon period, Change Scribe transformed from a basic changelog generator into a comprehensive development tool. This evolution was driven by user feedback, technological advancements in LLM capabilities, and the need for more flexible documentation tools in modern development workflows. Key features added during the hackathon period include: Expanded LLM provider support (Gemini, Groq, SambaNova) Enhanced changelog format handling (Conventional and Keep a Changelog) Improved git change tracking Robust error handling Type-safe implementations Better documentation The extension evolved from a simple changelog generator to a sophisticated development tool, capable of handling various commit styles and changelog formats while maintaining semantic meaning. GitHub Copilot: The Game Changer The development of Change Scribe began with a simple idea: automate changelog generation using AI. What started as a basic VS Code extension evolved into a sophisticated tool supporting multiple LLM providers and changelog formats, and is a true display of the powerful combination of GitHub Copilot and VS Code in modern software development. As we evolved from version 0.7.0 to 0.11.3 in a matter of days, this AI-powered pair proved invaluable. When implementing complex features like multi-provider LLM support, Copilot's context-aware suggestions significantly accelerated development. It understood the VS Code extension API patterns and suggested appropriate implementations. While integrating Git functionality, Copilot provided ready-to-use code snippets for diff parsing and change tracking, saving hours of documentation consultation. VS Code's built-in TypeScript support, combined with Copilot's type suggestions, ensured type safety across the codebase. When working with multiple LLM providers, Copilot suggested comprehensive interfaces and type definitions, reducing potential runtime errors. The extension's changelog merging logic was particularly challenging. Copilot helped craft regex patterns for section detection and suggested efficient algorithms for content merging. When implementing format-specific features, it provided template structures for both Conventional and Keep a Changelog formats. Testing was streamlined as well. I used Copilot to generate comprehensive test cases based on function signatures and documentation. It understood Jest's syntax and VS Code's testing infrastructure, suggesting edge cases I hadn't considered. Error handling, often an afterthought, became robust as Copilot suggested potential failure points and appropriate error messages. For API integrations, it provided complete error handling patterns specific to each LLM provider. Documentation, typically time-consuming, was accelerated as Copilot generated detailed JSDoc comments and README updates based on code changes. In fact, I went back and redocumented the entire project using Copilot. It maintained consistency in documentation style and suggested relevant examples. This synergy between GitHub Copilot and VS Code transformed what would have been weeks of development into just 2 days, while maintaining high code quality and comprehensive testing. The result is a more robust, well-documented, and maintainable extension that serves its users better. Azure OpenAI: The Testing Ground Throughout the development of Change Scribe, Azure OpenAI Service played a pivotal role as both a development tool and a core service. As we built and tested the extension's multi-provider LLM support, Azure OpenAI Service served as our primary testing ground, offering several advantages over other providers. Initially, we leveraged Azure OpenAI's GPT-3.5-turbo model to test different prompting strategies for changelog generation. The service's detailed logging and monitoring capabilities proved invaluable in understanding how different git commit formats were being processed and how the generated descriptions could be improved. This testing phase helped us refine our prompt engineering significantly. The development process particularly benefited from Azure OpenAI's deployment flexibility. We created multiple deployments with different models and configurations, allowing us to test the extension's behavior across various scenarios. This helped us identify and fix edge cases in our changelog generation logic, especially when dealing with different commit message formats and changelog styles. Azure OpenAI's robust error handling and rate limiting features helped shape our extension's resilience. We encountered and learned to handle various API-related challenges, from token limits to concurrent request management. This experience led to implementing better error handling across all LLM providers supported by the extension. The service's consistent API response times and reliability were crucial during our testing phase. We processed thousands of commit messages through different prompt configurations, helping us optimize the extension's performance and response handling. The detailed usage metrics helped us understand patterns in changelog generation requests and optimize our token usage. Security testing was another area where Azure OpenAI proved valuable. We tested different authentication methods and API key management strategies, ultimately implementing a secure and flexible configuration system that works across different LLM providers while maintaining Azure-level security standards. This extensive testing with Azure OpenAI Service shaped Change Scribe into a more robust, reliable, and efficient extension. The insights gained influenced not just the Azure OpenAI integration, but the entire architecture of our LLM provider system, resulting in a more maintainable and scalable solution. What's Next Looking forward, I plan to: Add support for custom changelog templates Implement AI-powered commit message improvement Add changelog visualization features Integrate with CI/CD pipelines Support team-specific documentation styles Enhance multi-language support Change Scribe aims to continue evolving, making changelog maintenance effortless while ensuring clear communication of code changes across development teams. <div