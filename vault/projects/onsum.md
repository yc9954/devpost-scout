---
slug: "onsum"
url: "https://devpost.com/software/onsum"
title: "OnSum"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 869
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/patient_family"
---

# OnSum

> Hong Kong is aging fast, and elderly parents are often alone while children work. OnSum schedules their meds and appointments, reminds them gently in Cantonese, and alerts family if one's missed.

[Devpost](https://devpost.com/software/onsum) · hackathon [[Youth Code x AI]]

## Facets

**domain** [[developer_tools]] [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[supply_logistics]]
**user** [[patient_family]]

**stack** ai-sdk/openai, class-variance-authority, clsx, css, deepseek-api, eslint, geist-fonts, lucide-react, next.js, nvidia-api, opencode, postcss, react, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for onsum

## Body

Logo Inspiration OnSum began with a concern that many of us in Hong Kong share. This is a city that is aging faster than almost anywhere on earth, and within a few decades nearly one in three Hongkongers will be elderly. Behind that statistic are real people: parents who spend their days alone in small flats while their children work long hours to keep up with the cost and pace of this city. We did not have to look far for inspiration. We saw it in our own families, in grandmothers who eat dinner alone and fathers who insist they are fine so their children will not worry. Those children love their parents deeply, but long work hours, their own families, and physical distance make it hard to be present. They cannot be there at three in the afternoon to check whether a parent has taken their medication. So they worry, and when something is forgotten, the guilt stays with them. We built OnSum to address that worry directly. The name carries the Cantonese idea of 安心, meaning peace of mind, which is what we most wanted to give back to families who feel stretched too thin. What it does OnSum is designed to be simple for the elderly to use. Family members add a parent's medications, appointments, and daily tasks to a shared calendar, and an AI companion handles the rest. It reminds the parent through a simple chat, speaking in Cantonese and in familiar words, and confirms that each task has been done. If something important is missed, the family is notified right away. Our guiding belief was that the elderly should not have to learn another complicated app; they should only have to talk to a kind, patient assistant, while the more complex management stays on the caregiver's side. How we built it Building it meant designing for two very different users at once. We created two surfaces over a single shared system: a family dashboard where adult children manage the calendar and view how their parent's day is going, and an elderly chat room that is large, calm, and easy to use. Between them sits a reminder engine that tracks each scheduled time, sends a message at the right moment, waits for a reply, and escalates to the family only when necessary. Every reminder, whether a daily medication or a clinic visit weeks away, flows through the same structure so that nothing is missed. Challenges we ran into The hardest challenges were rarely technical. Teaching the agent to sound human, warm without being childish and persistent without nagging, took far more care than any line of code. We worked through questions of tone in Cantonese, how to follow up when a parent does not reply without making them feel watched, and how to decide what counts as urgent enough to alert a busy child at work. Accomplishments that we're proud of OnSum is more than a reminder app. It is a way to keep caring for the people who raised us even when work and distance make it difficult to be present. We are proud that no parent using it has to feel forgotten, and that no child has to choose between their work and their parent's health. We built a system that keeps families connected across the distances this city imposes, and that made it worth the effort we put into it. What we learned We learned that good caregiving technology is mostly about restraint: knowing when to speak gently, when to wait, and when to do nothing and leave a family to itself. The real work was not in the code but in the care, in how a single message is received by someone who is lonely, and in earning enough trust that a worried child can feel reassured. What's next for OnSum Looking ahead, we want OnSum to grow in two directions: becoming more agentic, and becoming voice-first. Today, OnSum reminds and confirms. Next, we want it to act. Our goal is a companion that takes on the small logistical tasks of caregiving, including booking a taxi to a clinic appointment, helping arrange a prescription refill before the medicine runs low, learning a parent's habits and adjusting how it checks in, and coordinating between siblings so nothing is missed. The aim is to move from a tool that remembers to one that helps, reducing the mental load on families so they can spend their limited time with their parents rather than on logistics. The second direction is voice-first. Many of Hong Kong's elderly did not grow up with screens, and typing will always be a barrier no matter how large the text. Their most natural way to communicate is speech. We want OnSum to be something a grandmother can talk to in Cantonese, replying out loud, asking questions, and never needing to touch a device. For seniors with poor eyesight or limited hand mobility, voice is not just a convenience; it is what makes the technology usable for them at all. Together, these directions point to the same goal: an OnSum that listens, understands, and reliably takes care of what needs to be done for the families who depend on it. <div