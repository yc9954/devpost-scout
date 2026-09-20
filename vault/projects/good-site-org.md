---
slug: "good-site-org"
url: "https://devpost.com/software/good-site-org"
title: "Good-Site.org"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 557
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/web_dom"
---

# Good-Site.org

> A Chrome extension that helps you understand your privacy. Finds the privacy policy of any website and uses AI to give you the main points, with just the click of a button.

[Devpost](https://devpost.com/software/good-site-org) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** chrome, css, express.js, extension, gpt-4o, html, javascript, node.js, oauth, tiktokloginkit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for good-site.org

## Body

Inspiration Growing up, my dad always emphasized the importance of reading any contract before agreeing to it. In today's digital age, where data and privacy are valuable commodities, it's more crucial than ever to understand privacy policies. However, putting this into practice is challenging, as most privacy policies exceed 2,000 words and span multiple pages. While researching this idea, I discovered an interesting statistic: it would take the entire US population 53.8 billion hours to read their privacy policies each year. That's equivalent to over 76 work days per person, solely dedicated to reading privacy policies. No one can afford to do that. So, I realized the only way to combat the issue would be a browser extension that reads privacy policies for users and categorizes the main points into pros and cons. Source What it does Good-Site.org is a Chrome browser extension that summarizes the privacy policy of any website with the click of a button. All it takes is for you to be on a website and click the "Summarize Privacy Policy" button on the extension and it finds the privacy policy of the website, and summarizes it into Pros and Cons using GPT-4o. How I built it To create the Chrome extension, I utilized Chrome's Manifest V3 platform and wrote the code in JavaScript. The Good-Site.org website was built using Express.js, with HTML pages styled using Tailwind CSS. To add a personalized touch to the extension, I integrated TikTok's Login Kit. For summarizing privacy policies, I leveraged OpenAI's GPT-4o API. Challenges I ran into As this was my first time creating an extension, the task seemed pretty daunting. However, after realizing that it primarily involved JavaScript (a language I've worked with for years), the project seemed more feasible. While integrating TikTok's Login Kit into the Good-Site.org website was relatively straightforward, connecting the authentication system from the website to the extension required some additional effort. Midway through development, I realized that in order for the extension to be intuitive, users should be able to click the extension button on any page of a website, not just the privacy policy page. This meant I needed to find the privacy policy link from the current page. Fortunately, most websites include a link to their privacy policy in their footer, which is present on every page. Throughout the process, I tested the extension on a specific website. However, after finishing the extension, I discovered that the privacy policy parser didn't always work as expected, since some privacy policies have different formats. So, I had to spend significant time to refine the parser to ensure it works across all websites. Accomplishments that I'm proud of Creating an extension Integrating third party authentication into an extension Dynamically populate UI with AI response What I learned This project provided me with valuable knowledge and skills. I learned how to create browser extensions and connect them to different websites. Additionally, I gained experience in using AI responses to dynamically populate tables. Furthermore, I acquired skills in utilizing TikTok's APIs and developer tools. Overall, this project has been an enriching learning experience that has expanded my technical capabilities. What's next for Good-Site.org Looking ahead, I am excited to gather user feedback, iterate on the extension's features, and explore new ways to promote transparency and awareness in the ever-evolving landscape of online privacy. <div