---
slug: "vct-hackathon-5bx0nj"
url: "https://devpost.com/software/vct-hackathon-5bx0nj"
title: "VCT Team Builder"
hackathon: "VCT Hackathon: Esports Manager Challenge"
organization: "Amazon"
winner: true
words: 625
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/geospatial"
---

# VCT Team Builder

> If your VCT Manager doesn't use this tool, they're TROLLING.

[Devpost](https://devpost.com/software/vct-hackathon-5bx0nj) · hackathon [[VCT Hackathon- Esports Manager Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[geospatial]]

**stack** amazon-web-services, aws-bedrock, aws-cognito, cloudformation, github-actions, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vct-hackathon
- thank you!

## Body

VCT-Team-Builder-App-Teaser Inspiration Our team aimed to go beyond just creating a simple chat interface. We leveraged data, AI and our understanding of human-computer interaction to provide an edge by enhancing a manager’s productivity through visual insights and interactivity. This approach allows for more informed decision-making, backed by accurate complex data retrieval and analysis, and transforms them into actionable insights and strategies at a glance. What it does The Team Builder tool helps a VCT Manager form teams comprising of known pro-players in the VCT scene based on 2023 and 2024 data. The Team Builder provides a digital assistant that leverages the power of Machine Learning and Large Language Models to suggest the optimal winning team combination, assign roles, evaluate players and team contribution and suggest strategies based on the chosen players. It also provides the ability to customise the team itself and do a deep-dive analysis on each player's attributes and stats. How we built it Using AWS Bedrock Converse capability we built an LLM-driven Agentic RAG application that is able to retrieve data provided by Riot (and external 3rd party data) and provide a high quality response. It leverages dynamic few-shot prompting methods so it performs at high levels of accuracy without affecting speed. We also leveraged machine learning to enhance the quality of outputs by finding trends and patterns of teams stats that result in winning rounds. We designed the front end application so that a VCT Manager could interact with the digital assistant whose insights can be supported by interactive visuals. Challenges we ran into Transforming existing VCT data into formats for LLM retrieval requires significant investment into functional and industry capabilities. Providing many examples in a prompt for increased accuracy resulted in low speed. We faced throttling issues, and had we not experienced these issues, we would used a more powerful model that would have generated higher quality answers, however we opted to use a medium-range model that still works quite well. Accomplishments that we're proud of We are proud of the way our team worked together to brainstorm ideas, solutions and workarounds for the challenges we faced. We believe we stretched the goals to develop a high performing application that is designed with the end-user's needs in mind. Our digital assistant performs with high accuracy and the Team Builder Score surfaced amazing insights that the digital assistant can leverage to provide useful suggestions. What we learned Using an IaC approach with AWS Cloud Formation templates made the process quicker and more structured, enabling enhancements to the application to happen rapidly. We found dynamic few-shot prompting to be a suitable approach to combat the performance challenges because: enables many examples to be provided so that LLM is accustomed to a variety of scenarios. Minimise the impact of having long prompts with many examples reducing accuracy and speed. This is because few-shot prompting generates embeddings on the examples and only the most relevant examples to the query are used as examples in the prompt. What's next for vct-hackathon We believe there is so much potential to do further analysis, ML and to further develop the LLM-powered Digital Assistant using AWS technology with the end goal to help a VCT manager and Team Coach plan strategies (for example: looking at map control analysis, building a Performance Dashboard to monitor current team progress and play styles, and utilise Scrims data (practice match data) that would be in high demand for all VCT esports managers once fully designed and developed. Thank you! The VCT Team Builder team would like to thank AWS, Devpost and Riot Games for allowing us to learn and participate in such an engaging competition. We definitely learned a lot and grew in technical knowledge as well as friendship points :) <div