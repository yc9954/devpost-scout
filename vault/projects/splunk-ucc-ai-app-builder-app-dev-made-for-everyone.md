---
slug: "splunk-ucc-ai-app-builder-app-dev-made-for-everyone"
url: "https://devpost.com/software/splunk-ucc-ai-app-builder-app-dev-made-for-everyone"
title: "Splunk UCC AI App Builder - App dev made for everyone"
hackathon: "Splunk Agentic Ops Hackathon"
organization: "Splunk"
winner: true
words: 573
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Splunk UCC AI App Builder - App dev made for everyone

> Describe a Splunk add-on in plain English; an AI agent inside Splunk using the Splunk Agent SDK, builds it with ucc-gen, validates with AppInspect, and self-corrects until the package ships clean.

[Devpost](https://devpost.com/software/splunk-ucc-ai-app-builder-app-dev-made-for-everyone) · hackathon [[Splunk Agentic Ops Hackathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[geospatial]] [[web_dom]]

**stack** mcp, python, react, splunk, splunkai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for splunk ucc ai-assisted app builder

## Body

Inspiration Building a production-ready Splunk add-on is a slog: understanding globalConfig, how inputs stream data, scaffolding with ucc-gen , packaging it, run AppInspect, read the failures, fix, repeat. I've been doing that loop by hand for years - its tiring; so we taught an agent to do it, and put it inside Splunk where the data, tools, and AI already live. What it does Splunk UCC AI-Assisted App Builder is a full add-on IDE that runs natively inside Splunk . You describe what you need in plain English and a tool-calling AI agent authors the globalConfig.json , creates the boilerplate app, orchestrates the app-specific code for your usecase, then drives a self-correcting build loop : ucc-gen build -> AppInspect -> read the findings -> auto-fix the source -> re-run, until the package is AppInspect-clean and shippable . It also has a wizard, a Monaco file editor, live GitHub import/export, and a one-place Configuration tab for the AI provider - all without leaving Splunk. How we built it A native Splunk (UCC) app with the standalone React IDE embedded and its API over Splunk REST endpoints. The agent leverages the Splunk Agent SDK ( splunklib.ai ) , in a clean isolated subprocess, calling 7 builder tools also registered on the Splunk MCP Server for use outside the app . The verification oracle is AppInspect (a Splunk Developer Tool) and ucc-gen (the official UCC framework) - the same official tooling Splunk ships. A unified Configuration page (encrypted in storage/passwords ) allows custom external AI services for the AI assistant to leverage. GitHub Actions CI builds, validates and tests it — including the official splunk/appinspect-cli-action and a live Splunk-in-Docker integration run. Challenges we ran into Splunkd's shared interpreter pollutes imports across apps - solved by spawning the Agent SDK in a pristine subprocess. Python version split : persistent REST handlers run 3.9, but the Agent SDK stack needs cp313 - fixed with python.required = 3.13 and a pure-python urllib3 pin. AppInspect packaging hygiene for compiled, vendored AI deps (aarch64 when developing on Silicone Mac, .keep files, permissions, reload triggers). CSRF on the embedded SPA's proxy calls (Splunk Web needs both X-Splunk-Form-Key and X-Requested-With ). Stopping the agent from looping on a no-op fix (a no-progress breaker + a URL-encoding bug in the project reset). Accomplishments that we're proud of A genuinely usable IDE running inside Splunk on the Splunk Agent SDK - not a mockup. Natural language -> AppInspect-clean add-on in ~40 seconds (e.g. a working Equine Energy API add-on, clean in 3 self-correcting iterations). Uses three Splunk AI/developer capabilities together: MCP Server , AppInspect (Developer Tools) , and the Agent SDK . Fully open source (with a generated license inventory) and CI-green , including a live Splunk-in-Docker integration test. What we learned How to drive the Splunk Agent SDK ( splunklib.ai ) end-to-end, register app functions as Splunk MCP Server tools, and use AppInspect as a deterministic verification oracle for an agent loop, plus the real-world constraints of running modern AI dependencies inside Splunkd's runtime. What's next for Splunk UCC AI-Assisted App Builder Have the builder generate the CI/CD it was built with - emit a GitHub Actions pipeline (official AppInspect + Splunkbase publish) for every add-on it creates. Route the main IDE's assistant through the Agent SDK so the polished UI is powered natively by splunklib.ai . Multi-account AI providers, deeper UCC feature coverage (alert actions, OAuth, custom commands), and one-click Splunkbase packaging. <div