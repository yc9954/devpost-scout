---
slug: "letmetalktohuman-ai"
url: "https://devpost.com/software/letmetalktohuman-ai"
title: "Letmetalktoahuman AI"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 479
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Letmetalktoahuman AI

> Our project's voice agent interacts with redundant customer service bots, quickly navigating through automated systems to connect users with real human agents through call forwarding.

[Devpost](https://devpost.com/software/letmetalktohuman-ai) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: cross_origin_web</sub>
**substrate** [[code_repository]] [[document_pdf]] [[web_dom]]

**stack** html, node.js, react, react-router-dom, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for letmetalktohuman ai

## Body

this is the user form to get inputs to use in the VAPI system Inspiration We often encountered challenges navigating automated call systems, which left us spending excessive time on hold and feeling frustrated. These experiences made us realize how much valuable time was being wasted when we could have been focusing on more productive tasks and we were left angry and wondering if there was a better way to optimize telecommunication systems. This frustration inspired us to develop a solution that streamlines the process, minimizing wait times and improving the overall customer experience. What it does The system includes a form where clients can enter their name, phone number, and a brief description of their issue, such as requesting a refund or returning an item. Once submitted, the VAPI system automatically places a call to the provided number. A virtual assistant then guides the client through a series of questions to better understand their problem with the VAPI system answering the questions based off the description given. The VAPI setup even handles the wait time on the client's behalf, ensuring they’re connected directly to the appropriate support agent without unnecessary delays. How we built it We implemented the solution using React.js for the front-end interface and VAPI for handling the automated calls. The form submission triggers the VAPI system, which initiates and manages the call flow. For version control and collaboration, we hosted the project on a GitHub repository, utilizing GitHub Actions for continuous integration and automated testing to ensure a smooth deployment process. We used llama within Groq as the LLM as we saw significant difference in response time when using groq vs openai. This setup allowed us to efficiently manage code updates and track changes while leveraging VAPI’s capabilities to handle real-time interactions with clients. Challenges we ran into We encountered challenges managing different branches, as the primary branch frequently stalled during the process. Accomplishments that we're proud of We were able to integrate the front end with the VAPI connector after clicking the submit button which took time, but we were persistent in solving the problem. What we learned We explored various functionalities within the React ecosystem, gaining a deeper understanding of tools and techniques available to enhance our applications. For instance, we learned about the @media query, which allows us to create responsive designs by applying different styles based on screen size and device characteristics. Additionally, we became proficient in utilizing VAPI to manage automated calls, including how to implement its features for efficient interaction with clients. This knowledge has equipped us to build more dynamic and user-friendly applications. What's next for Letmetalktohuman AI We aim to implement a feature that recognizes and performs specific dial tones, as these are a common part of phone interactions. This feature will enhance the user experience by allowing the system to respond to different inputs appropriately. <div