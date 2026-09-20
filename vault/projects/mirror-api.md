---
slug: "mirror-api"
url: "https://devpost.com/software/mirror-api"
title: "MirrorAPI"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 337
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# MirrorAPI

> Compare Your API Versions with Confidence

[Devpost](https://devpost.com/software/mirror-api) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mirrorapi

## Body

Select API endpoints and send request to both Receiving responses from both API versions Displaying conflicts between JSON responses Sign In Page MirrorAPI Inspiration We were inspired by the Statefarm Challenge and NVIDIA Challenge to implement our skills in API version control and documentation to solve a high impact problem all developers face regularly when working with APIs. What it does Our application requests the user for two API endpoints that are compared and contrasted to determine the changes that we will be making to the codebase. Then, we use Nvidia's Nemotron Agentic AI model to perform Retrieval-Augmented Generation, automatically generating a well-defined report that provides well-founded and detailed insights on API design changes. How we built it We built it using Next.js and TypeScript for the front end and the API differences tool and used OAuth for employee authentication. We used FastAPI and Python for communicating with the Nemotron model. Challenges we ran into We faced our first major hurdle when creating detailed API documentation whilst maintaining industry compliance. Traditional LLama models were not delivering reports that were up to par. Therefore we found a solution by leveraging the power of NVIDIA Nemotron models known for their superior reasoning capabilities and long term context retention. Accomplishments that we're proud of We are proud of our front end, which was based on the sponsor challenges we chose, and we are also proud of how we used NVIDIA Nemotron to produce comprehensive yet easy-to-understand reports for employees to read and understand the APIs used in their codebase better. What we learned We learned countless industry best practices when it came to API design and version control. Additionally, we had a chance to implement deterministic algorithms for API consensus and use Advanced ML and Agentic AI models. What's next for MirrorAPI We're planning to implement this use case into professional CI/CD workflows. We are also in the process of adding real-time algorithms that propagate changes through the entire codebase upon an API update for full and precise automation. <div