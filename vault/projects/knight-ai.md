---
slug: "knight-ai"
url: "https://devpost.com/software/knight-ai"
title: "Knight AI"
hackathon: "Airia AI Agents Hackathon"
organization: "airia"
winner: true
words: 846
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Knight AI

> See something suspicious? Knight AI instantly analyses websites, emails, and social media for phishing and scams, flags the threat, explains why it's dangerous, and tells you exactly what to do.

[Devpost](https://devpost.com/software/knight-ai) · hackathon [[Airia AI Agents Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[runtime_tool_creation]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
  <sub>weak: supply_logistics</sub>
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** airia, anthropic, chrome-extensions-(manifest-v3), express.js, haiku, html, javascript, mongodb, node.js, virustotal, whois

## How they structured the write-up

- inspiration
- what we built
- how we built it
- challenges
- what we learned
- what's next

## Body

Phishing attempt in website blocked Phishing attempt blocked in gmail Knight AI chat for detected threat Knight AI chat for another detected threat Live threat analysis in extension Potential Threat sample Safe mail sample Phishing attempt blocked sample Knight AI Threat log Knight AI: Your AI Powered Cybersecurity Companion Inspiration Every year, cybercrime costs the world $10.5 trillion , which is more than the global drug trade combined. In 2023 alone, the FBI received over 880,000 cybercrime complaints , with phishing being the most reported crime for the third consecutive year, accounting for 298,000 cases . Over 3.4 billion phishing emails are sent every single day, and nearly 1 in 3 people will click a malicious link without realising it. What makes this worse is that these attacks no longer arrive as obvious spam. They come as a Facebook message from someone you know whose account was hacked, a convincing Netflix login page hosted on Firebase, or a job offer email that looks completely legitimate. The average person has no way to tell the difference. Existing security tools either block threats silently or flash a red warning with no explanation. Neither approach helps the user understand what happened or what to do next . People click through warnings they don't understand, or panic over ones that turn out to be false alarms. We built Knight AI because the missing piece isn't just detection; it's explanation . We wanted to build a tool that not only catches the threat but talks you through it, answers your questions, and tells you exactly what to do. What We Built Knight AI is a Chrome browser extension that acts as a real time AI security shield. It automatically analyses websites, emails, and social media messages the moment you open them without any manual scanning required. For every threat detected, Knight AI flags the risk level and explains why it's dangerous in plain language. Not sure what it means? Just ask — you can chat directly with the AI to get a clearer explanation and find out exactly what to do next. Every warning and Dangerous detection is automatically saved to a built-in threat log that you can easily filter by platform, status, and keyword. This ensures you always have a full history of what Knight AI caught. The log updates live as new threats are detected and can be exported as a CSV at any time. How We Built It We built Knight AI as a full stack system consisting of a Chrome extension that extracts structured content from the browser, a Node.js backend that handles caching and routing, and an AI analysis engine. This engine is powered by Claude Haiku running on the Airia platform and is equipped with VirusTotal and WHOIS tools for real threat intelligence. Challenges Content Extraction from Emails and Social Media Gmail, Outlook, and Facebook Messenger all presented unique scraping challenges. Email clients nest message content inside complex, dynamically generated page structures that change frequently, so we had to find stable patterns that would reliably extract the required contents. Facebook Messenger was the hardest. The entire frontend is deliberately obfuscated with no meaningful class names or structure to rely on. Getting clean message text from these platforms is incredibly difficult. Prompt Engineering and Tool Selection Getting the AI to make the right decisions consistently, such as which tools to call, when to skip them, and how to respond across different content types, required a level of precision we didn't anticipate. Every content type has different rules. For example, a website needs a full URL scan, while a suspicious email needs a content and domain check. The hardest bug to fix was the AI treating a user's simple follow up question as a new threat to analyse. This triggered expensive security tool calls just because the page URL was visible in the background context. It took several iterations to find the right wording to make the AI reliably distinguish between "analyse this" and "answer my question about what you already analysed." We came away with a clear lesson. Prompt engineering at this level is indistinguishable from software engineering. Vague instructions produce inconsistent behaviour just as surely as a bug in code. What We Learned Building this project taught us that real world data extraction is incredibly hard. Modern frontends are not built to be scraped, and reliable extraction requires deep knowledge of browser rendering. We also quickly realised that prompt engineering is essentially debugging, as ambiguous instructions cause real, traceable bugs just like code defects. Above all else, we learned that users need context, not just warnings. Explaining the threat to a user is just as valuable as detecting it in the first place. What's Next Looking ahead, we are excited to expand Knight AI's capabilities. We plan to add support for WhatsApp Web and Instagram DMs, along with a feature that automatically reports threats to official authorities. We are also working on a mobile browser extension. Eventually, we want to launch a team dashboard designed for organisations to monitor threats across all their employees. <div