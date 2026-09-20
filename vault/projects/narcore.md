---
slug: "narcore"
url: "https://devpost.com/software/narcore"
title: "Narcore"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 424
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
---

# Narcore

> An AI undercover agent to detect and intercept online drug advertising.

[Devpost](https://devpost.com/software/narcore) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[human_in_the_loop]]
  <sub>weak: finance_payments, mental_health</sub>
  <sub>weak: sensor_telemetry</sub>

**stack** browserbase, claude-code, docker, javascript, llama, next.js, nomic, react, redis-stack, shadcn/ui, stagehand, tailwind

## Body

As technology and social media have become more advanced, law enforcement agencies must keep up. Nowadays, drug dealers market their product not on the dark web or secretive forums, but out in plain sight on their social media pages. Apps designed to connect individuals with algorithms focused on curating your "For You" page ended up creating the perfect environment for dealers to market their product to the masses. And it's not as simple as searching up narcotics-related keywords such as drugs. Criminals are adapting by publishing public posts with captions and instead of saying "I'm selling weed," they make use of slang like "restockd PRODUCT. hmu for PUFF 🍃". Law enforcement agencies have their drug enforcement divisions dedicating valuable time to searching for these kinds of posts. Narcore was created to help law enforcement officials by using multiple Browserbase instances to scrape through synthetic feeds on a virtual machine. If their caption indicates illegal substance advertising, Narcore flags the specific post and provides it to law enforcement agencies for a human-in-the-loop to review through Narcore's dashboard. If the post is deemed as substance distribution, Narcore can get into contact with the seller and assist law enforcement by arranging meets and inquiring about what substances they're selling, information that will allow law enforcement officials to obtain a warrant to shut down their operations. Narcore is first seeded using known keywords from national datasets such as the Drug Enforcement Agency's Drug Slang Code Words and Substance Abuse and Mental Health Services Administration's glossary. Narcore then employs Nomic AI to track the semantic drift of these decoy terms. When innocent words like "blueberry" start suddenly appearing alongside drug-related signals like "M30," "delivery," or the leaf emoji and the human-in-the-loop deems this as illegal activity, Narcore encodes this information for future scans. Narcore deletes these terms after 30 days or once they are not being actively used. Finally, to ensure Narcore doesn't flag posts that contain keywords only by coincidence, a risk-scoring algorithm is implemented by taking multiple factors into evaluation, such as: Frequency of high-risk text, Redirects to encrypted messaging platforms, Payment markers A post is flagged once the risk threshold is exceeded, and Narcore then generates a Lead Summary Report , including: The account's public handle and platform Detected code words And metrics from the risk-scoring evaluation This report is then available to law enforcement and social media platforms for their review, and if approved, Narcore will agentically reach out to the distributor posing as a buyer to provide crucial information to accelerate their takedown. <div