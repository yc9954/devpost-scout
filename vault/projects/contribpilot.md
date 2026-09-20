---
slug: "contribpilot"
url: "https://devpost.com/software/contribpilot"
title: "ContribPilot"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 831
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
---

# ContribPilot

> Finding an open source issue is easy. Contributing successfully is hard. ContribPilot bridges that gap with personalized guidance powered by Gemini and GitLab MCP.

[Devpost](https://devpost.com/software/contribpilot) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]]

**stack** fastapi, gemini, gitlab, google-cloud, mcp, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for contribpilot

## Body

UI Inspiration As a computer science student, I’ve always wanted to contribute more to open source projects, but I repeatedly ran into the same problem: finding an issue is easy, actually contributing is hard. Most beginners struggle with understanding unfamiliar repositories, figuring out contribution guidelines, setting up the project locally, and knowing where to start. Existing tools can recommend issues, but they rarely help contributors understand what comes next. I built ContribPilot to bridge that gap. Instead of just finding beginner-friendly issues, I wanted an agent that could understand a repository, read its documentation, and generate a personalized roadmap that guides a developer from issue selection all the way to opening a Merge Request. What it does ContribPilot is an AI-powered open source contribution coach built with Gemini, Google Cloud, and GitLab MCP. A user provides their skills and interests, and ContribPilot: Finds beginner-friendly GitLab issues Ranks opportunities using BM25-based relevance scoring Retrieves repository context such as README and CONTRIBUTING files Explains issues in plain language Estimates difficulty and required skills Generates a repository-specific implementation plan Guides users through setup, development, testing, and Merge Request creation Instead of receiving a list of links, users receive a complete contribution roadmap tailored to the repository they selected. How we built it I built ContribPilot using Gemini, Google Cloud Agent Builder, and GitLab MCP. At the core of the project is the GitLab MCP integration, which gives the agent access to GitLab repositories, issues, merge requests, and project data through MCP tools. ContribPilot uses these MCP capabilities to search for contribution opportunities, retrieve issue details, and understand repository context. To make the experience more useful for new contributors, I built an additional backend layer around the GitLab MCP integration. This layer handles GitLab OAuth, repository context retrieval, issue ranking, and contribution-specific analysis. When a user asks for help contributing to open source, the agent: Uses GitLab MCP tools to discover and retrieve contribution opportunities. Retrieves repository context such as README files, contribution guidelines, and project documentation. Analyzes the repository and issue requirements. Generates a personalized implementation plan tailored to that repository. The agent itself runs on Google Cloud using Gemini and Agent Builder, while the supporting services are deployed on Cloud Run. OAuth credentials are stored securely using Google Secret Manager. Challenges we ran into One of the biggest challenges was GitLab OAuth and repository access. GitLab’s OAuth mcp scope works well for issue discovery, but repository file endpoints behave differently. Public repositories could be accessed without additional permissions, while private repositories required broader scopes. I had to design the repository context retrieval logic to handle these cases gracefully. Another challenge was token management. GitLab access tokens expire after a short period of time and refresh tokens are rotated after every refresh. I implemented automatic token refresh logic and added synchronization mechanisms to prevent multiple requests from trying to refresh the same token simultaneously. I also ran into issues integrating MCP with Google Agent Builder. Some MCP tool schemas contained fields that Agent Builder rejected with INVALID_ARGUMENT errors. I ended up normalizing tool schemas and removing unsupported fields before registration while applying defaults server-side. Accomplishments that we're proud of I’m most proud of building an agent that goes beyond issue discovery and helps users understand how to successfully contribute to open source projects. Most contribution tools stop after recommending issues. ContribPilot continues the workflow by analyzing repository documentation, contribution guidelines, and project context to generate practical implementation plans tailored to a specific repository. I’m also proud of successfully integrating GitLab MCP into a real-world workflow. Rather than using MCP as a simple demo integration, ContribPilot uses GitLab MCP capabilities as a core part of the contribution discovery and repository analysis process. Finally, I’m proud that the project combines Gemini, Google Cloud Agent Builder, GitLab MCP, OAuth, and repository analysis into a complete agent experience that addresses a problem many developers face when trying to make their first open source contribution. What we learned Building ContribPilot taught me a lot about MCP, OAuth, cloud deployment, and agent architecture. I learned how to design MCP tools that work reliably with AI agents, how OAuth token refresh workflows behave in production environments, and how to deploy agent-based applications using Google Cloud Run and Secret Manager. I also learned that building a useful agent requires much more than connecting an LLM to an API. The quality of the workflow, tool design, and context retrieval has a huge impact on the usefulness of the final experience. What's next for ContribPilot My next goal is to expand ContribPilot beyond GitLab by adding GitHub integration so users can discover and contribute to open source projects across both platforms. I also plan to improve the backend architecture so it can handle significantly more users and larger workloads while maintaining fast response times. Finally, I want to add a complete authentication and user management system so contributors can save their progress, revisit contribution plans, and track their open source journey over time. <div