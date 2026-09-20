---
slug: "nexarch-ukoica"
url: "https://devpost.com/software/nexarch-ukoica"
title: "NexArch"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 413
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
---

# NexArch

> Build to Scale Together

[Devpost](https://devpost.com/software/nexarch-ukoica) · hackathon [[Frostbyte Hackathon]]

## Facets

**domain** [[developer_tools]]
  <sub>weak: developer</sub>
**substrate** [[sensor_telemetry]]
  <sub>weak: code_repository, structured_db</sub>

**stack** azure, azurevm, fastmcp, gemini, langchain, langraph, next.js, pydantic, python, redis, temporal.io

## Body

As Now a days software systems grow, and their real production architecture mostly becomes unclear. Teams no longer know how requests actually move through services, databases, and APIs. This actually makes it hard to find bottlenecks, fix performance issues, as well as decide how the system should be improved. Present time tools show logs and metrics, however they do not explain the system’s structure or guide about the architectural decisions. Nexarch solves this by understanding applications from how they run in production. By using our lightweight SDK, Nexarch observes live request flows, service connections, and performance behaviour without accessing source code or sensitive data. From this runtime information, it automatically rebuilds workflow of better architectural design based on the system’s actual architecture and highlights problem areas. Nexarch then generates multiple improved architecture designs with workflow's options which actually focused on performance, cost, or low-risk changes. Each of the generated option is compared using clear metrics like speed, reliability, cost, and complexity. This helps teams make confident, data-backed architecture decisions faster, even helps to make a better production ready scalable system. Atlast user will get to know some interesting information about there whole architecture and workflow pipelines, so that there system never get messed up and work as production ready. It is actually a better system visibility platform, which reduce manual analysis, lower risk during changes, and continuous clarity as applications evolve so that in future if anything new came up which can help, then developers can evolve there architecture and workflow based on it. Chaleenges: We have built MCP servers for each type of functionality so that we can implement them with LangGraph for non-linear, asynchronous workflows. While doing this, it was quite frustrating because our computational costs increased significantly, and we also hosted the backend on a cloud virtual machine. However, we managed these challenges and designed an efficient workflow for our platform. We then developed an SDK that allows users to directly access our services by integrating it into their applications. For this, we used MCP servers along with features like tracking and key-based cryptography, which took considerable time because we learned these new technologies in a single night and still managed to build a scalable product. Finally, we deployed the backend on the cloud with a custom domain at https://api.modelix.world and the frontend at https://run-time.in . For deployment, we used Azure Cloud App Service and Virtual Machines, which required additional time and effort, especially for SSL configuration and setup. <div