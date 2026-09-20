---
slug: "runbook-rabbit-let-rovo-be-your-jira-agent-s-new-assistant"
url: "https://devpost.com/software/runbook-rabbit-let-rovo-be-your-jira-agent-s-new-assistant"
title: "Runbook Rabbit - Let Rovo be your Jira agent's new assistant"
hackathon: "Codegeist 2024"
organization: "Atlassian"
winner: true
words: 501
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
---

# Runbook Rabbit - Let Rovo be your Jira agent's new assistant

> Reads your companies runbooks for your Jira agents. Depending on the issue's fields and comments it highlights the relevant sections in your handbooks. Entirely runs on Rovo and Jira Automations 🔒.

[Devpost](https://devpost.com/software/runbook-rabbit-let-rovo-be-your-jira-agent-s-new-assistant) · hackathon [[Codegeist 2024]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]]
**substrate** [[document_pdf]]

**stack** forge, react, react-query, rovo, trpc, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for runbook rabbit

## Body

Highlights the relevant parts of your runbook Summarizes the next steps Adjustable to every need via Jira Automations Inspiration Runbooks as process documentation are a cornerstone of ITSM, guiding teams through complex workflows and edge cases. Yet, no app tightly integrates these resources with Jira Service Management . Runbook Rabbit changes that. It makes runbooks actionable and accessible directly within Jira . Most importantly the app: Runs on Atlassian (no egress!) ✅ Is a powerful extension to Atlassian Rovo ✅ What it does Runbook Rabbit leverages Atlassian Rovo to read and interpret your runbooks (or playbooks / agent documentations), dynamically integrating them into Jira Service Management. It links specific runbooks to projects and request types, analyzes context when issues are updated or commented on , and suggests actionable next steps . But the app doesn't stop there! It also highlights the relevant text sections the human agent should read when proceeding with the ticket. ✍️ This keeps the human in the loop and helps the agent understand which parts of the handbook were the basis for the AI-generated summary. How I built it I built Runbook Rabbit on Forge , and it runs entirely on Atlassian servers. Using Jira Automations and Atlassian Rovo , the app reads issue fields and updates, matches them against the corresponding runbook, and delivers real-time insights to agents. The configuration is straightforward, allowing admins to define in which projects and issue types Runbook Rabbit operates. Via Jira Automations one can configure when the runbooks should be analyzed. In my tests this worked best with: The issue create event The comment created event Field update events for fields that are mentioned in the runbook. Fun fact: I built this app on a backpacking tour through Laos 🇱🇦 & Thailand. 🇹🇭. So the use case from the video is actually accurate. Challenges I ran into Obviously, I had to spend a couple of hours finding the right prompts to deliver accurate results. After numerous tests, I’m proud that Runbook Rabbit provides reliable results even for complex runbooks . Its ability to highlight the sentences from the runbook that were considered helps the agent notice when Rovo misses any important parts. Accomplishments that I'm proud of The text highlighting also works when complex formatting, like tables or lists with bullet points or ordered lists, is used. To make this possible, I utilized Atlassian’s adf-utils package, which offers traversal methods for the Atlassian Document Format (ADF). What's next for Runbook Rabbit The next features are already in the pipeline! 👨🏻‍💻 What’s planned next is an analysis feature that allows managers to check which parts of the handbooks have been highlighted most often over a certain period. I believe this could enable admins to improve their Jira configurations and company processes by providing insights on which topics their agents spend the most time with . I'm looking forward to using @forge/sql for this use case. 👀 Let me know, what you think. Thank you for reading this! 🐰 Cheers, Julian <div