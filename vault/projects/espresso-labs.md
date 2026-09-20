---
slug: "espresso-labs"
url: "https://devpost.com/software/espresso-labs"
title: "Espresso Labs"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 484
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Espresso Labs

> Espresso Labs is building Gary, a voice-first digital assistant that helps busy people close loops faster by automatically tracking their obligations

[Devpost](https://devpost.com/software/espresso-labs) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**domain** [[developer_tools]]
  <sub>weak: transportation</sub>
**user** [[developer]]

**stack** elevenlabs, lovable, make.com, openai, postgresql, python, railway, react, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for espresso labs

## Body

Inspiration How much time is spent doing the work around the work? Most of us are plugged into so many incoming channels these days, like github, slack, email etc. Our time is spent reviewing and responding to messages instead of on the tasks that deeply energise us. Our mission is to help every one of us have the time to focus on the work they truly enjoy. We are aiming to do this by giving everyone access to an intelligent personal secretary. What it does We focused our initial efforts on building a highly personalised intelligent secretary for software developers. Imagine walking into work and having a consolidated view of all that's on your agenda presented to you in a pleasing way instead of being overwhelmed scrambling to catchup on yesterday's events or worse if you've been on PTO. The secretary will take information from all different inbound channels like slack, github, email and more, and provide an update via conversation. It can also take and note actions for you to handle at a later date, integrating with calendar, todoist and more for this. How we built it Developed a backend that could retrieve relevant context from all the various channels the user is plugged into. Used ElevenLab's conversational agent to manage the conversation flow with the user. We gave it access to tools to interact with the backend and third-party websites. Used Make.com to create webhooks that could speed up integration with third-party websites. We used this to plug into OpenAI to help our secretary review and summarise github PRs. Developed a sophisticated dashboard UI with React that consolidates all the information the user needs to manage their tasks and excel at their job. This collects information from the call with their secretary and the other inbound sources. Challenges we ran into We had challenges fulfilling our broad vision. So we decided to focus on software developers to start We had challenges controlling the flow of the conversation with the agent. This required careful design of the prompts. We had challenges integrating with various external tools in the given time. We decided to use of Make to help us orchestrate flows with third-party tools. Accomplishments that we're proud of An intuitive and comprehensive dashboard that connects information from the conversation between the secretary and captures actions to be taken. The user can also take actions from here. An awesome conversation flow which already feels like it would 10x the enjoyment and productivity of the everyday software engineer. Coming together as a team of strangers and putting out a great product in such little time. Big kudos team! What we learned We've levelled up our prompt engineering skills significantly How to highly leverage the conversation UI and tool use How to use a host of new tools and tie them altogether What's next for Espresso Labs The opportunities are many. Wait and see. <div