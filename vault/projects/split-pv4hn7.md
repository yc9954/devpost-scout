---
slug: "split-pv4hn7"
url: "https://devpost.com/software/split-pv4hn7"
title: "Split"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 395
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# Split

> Response Driven Generative Emailing. Powered by AI. We enable users to optimize their communication by learning from their emailing habits, tones, and emotional inclinations.

[Devpost](https://devpost.com/software/split-pv4hn7) · hackathon [[UC Berkeley AI Hackathon]]

## Facets


**stack** flask, google, hume, llamaindex, pandas, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for split

## Body

Inspiration We wanted to develop an easy-to-use workflow that allowed users to generate personalized emails with the assistance of AI, while retaining the user’s unique writing style and emotion inflections. What it does Our product learns from your previous emails and trains a custom LLM that will draft emails that sound like you, not like a robot. It learns from your writing style and how you respond to specific people. Then, it generates emails from user prompts that match that style. How we built it We used the Google API to parse through a user's old emails and develop a LlamaIndex LLM built on OpenAI's text-davinci-003. Then, we use Hume AI to understand the user's tone and emotion in their emails, and associate it with specific subjects and recipients so future emails can be fine-tuned to fit the user's emailing habits. Challenges we ran into It was quite difficult to get all of the different aspects of our model working together in unison, especially establishing the connection between the parsed emails and Hume emotion tags to the LlamaIndex model. We had to experiment with many different tools and prompt styles to get an accurate email generation. However, with a lot of dedication and troubleshooting, we were able to develop a working model to demonstrate our concept and its potential functionality. Accomplishments that we're proud of We are particularly proud of how we were able to train the model based on a user's previous emails, as this is the functionality that sets us apart for a plain LLM or other email productivity plugin. What we learned We learned how rewarding it was to train our own LLM using LlamaIndex. Base LLMs like ChatGPT are already so powerful, so the functionality of training a custom LLM based on your own data unlocks endless possibilities. What's next for Split We hope to completely integrate the code and workflow into a Google plugin or extension so users can easily implement it into their daily emailing. We want to ensure the privacy and security of the user’s data, so we want to experiment with methods to reduce how much data is sent to third-party services like OpenAI. We also want to dedicate further development to the emotion training, as this could boost the effectiveness of our product and add to our main value proposition of personalized, user-specific email generation. <div