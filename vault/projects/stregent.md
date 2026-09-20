---
slug: "stregent"
url: "https://devpost.com/software/stregent"
title: "stregent"
hackathon: "GitLab AI Hackathon"
organization: "GitLab"
winner: true
words: 709
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# stregent

> Stregent lives in your pipeline. Build. Deploy. Fix. Talk to it anytime whatsapp like a senior dev. Powered by Claude in gitlab duo. It never sleeps so you can. Not reactive, its proactive!.

[Devpost](https://devpost.com/software/stregent) · hackathon [[GitLab AI Hackathon]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** gitlab, mcp, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i faced
- what i learned
- what's next for stregent

## Body

stregent Inspiration As developers, we've all been there — you spend hours debugging, finally hit deploy, and walk away to grab lunch or head home. Then your phone buzzes. The site is down. The pipeline failed. And you're nowhere near your laptop. The frustration isn't just the failure itself — it's the context switching. Opening your laptop, logging into GitLab, finding the failed job, reading the logs, figuring out the fix. All of that mental overhead when you should be resting. I wanted to build something that collapses that entire workflow into a conversation on WhatsApp — the app every developer already has open. What it does StregEnt (Stress-Free Agent) is an autonomous CI/CD monitoring agent built on the GitLab Duo Agent Platform. When a pipeline fails in your project: The StregEnt Flow (running natively on GitLab Duo) detects the failure and sends you a WhatsApp notification instantly You open WhatsApp and ask StregEnt what went wrong StregEnt investigates — fetching pipeline status, job logs, and error details using custom GitLab MCP tools You say "ask Claude to fix it" — StregEnt creates an issue and mentions the Claude Agent on GitLab Duo Claude Agent analyzes the codebase, writes the fix, and creates a merge request You say "merge it" — StregEnt merges the MR and your pipeline goes green All of this from WhatsApp. No laptop required. How I built it StregEnt has two main components: StregEnt Flow — A custom YAML-defined flow on the GitLab Duo Agent Platform. It runs on GitLab's managed infrastructure and uses the run_command tool to make a POST request to a webhook server when triggered, sending a WhatsApp notification to the developer. The flow is triggered by a CI job that fires on_failure and mentions the flow's service account in an issue comment. StregEnt Client — A WhatsApp bot built with whatsapp-web.js and TypeScript. It connects to a custom FastMCP server ( glabs_server ) that exposes GitLab REST API tools — pipelines, job logs, issue creation, issue comments, and merge request merging. The agent loop is powered by Gemini 2.5 Flash via the OpenAI-compatible endpoint, with Redis for conversation history persistence. The two components work together: the Flow handles proactive notification, the Client handles interactive investigation and delegation. Challenges I faced SRT Proxy blocking outbound HTTP — GitLab's Sandbox Runtime blocked all external HTTP requests from within flows by default. The fix was using a custom Docker image ( node:20 ) in agent-config.yml which bypasses SRT, allowing the run_command tool to execute curl requests freely. Pipeline failure trigger not available — The ai_flow_trigger_pipeline_hooks feature flag is disabled by default on GitLab.com, meaning flows can't automatically trigger on pipeline failure events. The workaround was using a CI job with when: on_failure that creates an issue and mentions the StregEnt flow service account — achieving the same result through GitLab's existing event system. Token limits on free tier LLM providers — Tool call responses from GitLab (especially job logs) are large. Groq's free tier TPM limits were too tight for agentic tool use with conversation history. Switching to Gemini 2.5 Flash via its OpenAI-compatible endpoint solved this — higher limits, faster responses, zero code changes needed beyond the base URL and API key. WhatsApp notification spam — The StregEnt Flow was calling curl multiple times due to agent retry behavior. Fixed with a simple in-memory lock on the Express webhook server that ignores duplicate requests within a 60-second window. What I learned How to build and deploy custom flows on the GitLab Duo Agent Platform How the Anthropic Sandbox Runtime works and how to configure custom execution environments for flows That WhatsApp-first interfaces are genuinely powerful for developer tooling — the feedback loop is faster than any dashboard How to wire MCP tools to an agentic loop without using a framework — just a clean tool call loop with conversation history What's next for StregEnt Deploy the webhook server to Railway for a persistent URL (no more ngrok) Enable pipeline failure trigger when the feature flag becomes generally available Add a merge_request approval flow so Claude can request human sign-off before merging Open source glabs_server as a standalone GitLab MCP server for the community Expand notification channels beyond WhatsApp — Telegram, SMS, email <div