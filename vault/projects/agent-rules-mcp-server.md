---
slug: "agent-rules-mcp-server"
url: "https://devpost.com/software/agent-rules-mcp-server"
title: "Agent Rules MCP Server"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 612
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Agent Rules MCP Server

> Your coding development rules, instantly accessible

[Devpost](https://devpost.com/software/agent-rules-mcp-server) · hackathon [[Code with Kiro Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** githubapi, kiro, mcp, node.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agent rules mcp server

## Body

Inspiration Every developer faces the same problem: managing coding rules across different AI tools . When you switch between Cursor, Kiro, or other AI coding tools, you lose all your coding rules, style guides, and instructions. Your workspace gets messy with duplicate files, and keeping everything consistent is hard work. I had this problem when working on different projects with different AI tools. Then I thought: What if we could store all rules in GitHub and get them when needed? This would remove the need to manage local files and let teams easily share their coding rules. What it does Agent Rules MCP Server changes how developers handle coding rules by: Store Rules in One Place : Keep all your coding rules and instructions in one GitHub folder Get Rules When Needed : Pull specific rules without filling up your workspace Support Many File Types : Works with .md , .mdc , .chatmode.md , .prompt.md , and .instructions.md files Easy Setup : Works right away with public repositories, no GitHub token needed The server gives you two main tools: get_rules : Get rules for specific topics (e.g. "react", "security", "typescript") list_rules : See all available rule topics with descriptions How we built it I used Kiro's Specs feature a lot to plan and design the project. Working with Kiro helped me: Plan the MCP server structure Figure out how to connect with GitHub Design how to process rules Set up error handling Built with TypeScript using: MCP SDK : To work with AI coding tools GitHub API : To get files from GitHub Used Kiro's helpful features: Specs Feature : I made the specifications using specs mode Autopilot Development : Let Kiro handle boring coding tasks Live Debugging : Worked with the AI to solve problems Challenges we ran into The biggest problem was getting the MCP server to work with Kiro. The server failed because MCP doesn't support complex JSON Schema features like oneOf and anyOf . This was annoying because the server worked fine by with other AI IDEs but it doesn't work when with Kiro. After getting feedback, I worked with the AI to fix and redesign the schema to use simpler patterns that follows MCP Server documentations. Another problem was dealing with GitHub's API limits. The solution? A smart backup system that switches to getting files directly from GitHub when the API limit is reached, so you can always access your rules. Accomplishments that we're proud of Made the MCP server work completely with Kiro after fixing the schema problems. This needed good understanding of both MCP limits and how Kiro works. Built a strong backup system that removes the need for GitHub tokens in most cases. This makes the tool available to everyone without needing to manage API keys. Created a this MCP that "just works" developers can start using their own coding rules right away without making local rules folder in workspace. What we learned Found out what MCP's JSON Schema can and can't do, and learned to work within these limits while keeping all features working. This knowledge helps with building future MCP servers. Learned to use Kiro's advanced tools: Specs : For planning features step by step Steering : For keeping coding standards the same across the project Working Together : Using Kiro as a debugging partner, not just a code writer Learned good ways to use GitHub's API, including handling rate limits and getting content in ways that work well even with lots of users. What's next for Agent Rules MCP Server Building a collection of community-made steering/rules/instructions covering: Framework rules (React, Vue, Angular, etc) Language best practices Security guidelines Performance tips <div