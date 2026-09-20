---
slug: "call-prep-agent"
url: "https://devpost.com/software/call-prep-agent"
title: "Call Prep Agent"
hackathon: "Agentforce Virtual Hackathon"
organization: "Salesforce"
winner: true
words: 492
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Call Prep Agent

> We work in an increasingly virtual world. Running from meeting to meeting with customers, prospects, partners. The Call Prep Agent helps us prepare by quickly researching and learning about attendees.

[Devpost](https://devpost.com/software/call-prep-agent) · hackathon [[Agentforce Virtual Hackathon]]

## Facets

**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** apex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for call prep agent

## Body

Call Prep Example Deep research example Pre-Call Briefing Doc Example Inspiration We work in an increasingly virtual world. All of us can relate to the feeling of running from meeting to meeting whether it be with customers, prospects or partners -- often being invited to meetings with unfamiliar faces and not knowing what their background is or what perspective they come with. There's never enough time to fully prepare. In a perfect world, we'd have an assistant build a digital brief for us with photos and bios of each meeting attendee and with deeper research at our fingertips. What it does We've built the Call Prep Agent on Agentforce to help with exactly this challenge. With the Call Prep Agent, we can simply ask the agent to help us prep for a specific meeting or for the entire day. The agent will gather bios, profile pics, locations for each meeting of interest. And with a simple prompt, we can drill far deeper by having the agent analyze web research, gather linkedin profile details and summarize contact interaction logs from Salesforce. And lastly, the agent can output all of that information to a briefing document that we can then use to collaborate and prepare jointly with teammates. How we built it The agent runs on Agentforce for Employees and includes a single topic called Call Prep that includes a set of actions that perform the following: Get Meetings -- retrieves meeting information from Google Calendar Build Meeting Attendee UI -- presents a rich UI with meeting and attendee information Web Research -- Research a given attendee across the web using the Perplexity.ai API Get Contact Interactions -- Retrieve and summarize contact interaction logs for the attendee from Salesforce Get LinkedIn Profile -- Retrieve and summarize a users's LinkedIn profile in detail via a data provider API (Nubela ProxyCurl) Analyze Meetings -- Answer questions spanning multiple meetings Create Pre-Call Briefing Doc -- Output a meeting of interest as well as all research gathered during the agent conversation into a new Google Doc (integrated via the Google Drive and Google Docs API) Challenges we ran into We just wish we had more time. We'd love to do so much more with this agent. Accomplishments that we're proud of We're particularly proud of the rich text UI we were able to render inside the Agentforce chat panel. This took some clever HTML rendering. Also super happy we were able to generate the Google Doc output. What we learned We crammed a bit towards the end. Wish we had started work on the project weeks ago. What's next for Call Prep Agent We'd love to polish it up and get it onto the agent exchange. We'd love to significantly polish the document output with pretty formatting. Given time constraints, we just got a barebones document output working for now. We'd absolutely love to replicate the experience on slack with a slackbot and headless agent API integration. <div