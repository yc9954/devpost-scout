---
slug: "nourish-connect"
url: "https://devpost.com/software/nourish-connect"
title: "Med2Meals"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 902
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Med2Meals

> Replace medicine with alternative natural food 🥘

[Devpost](https://devpost.com/software/nourish-connect) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[agriculture_food]]
**user** [[legal_professional]]
**substrate** [[financial_record]] [[structured_db]]

**stack** bun, crossmint, express.js, fetch.ai, javascript, mongodb, next.js, node.js, postman, python, together.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for med2meals

## Body

Inspiration The inspiration for Med2Meals sprang from the universal truth that food is more than just sustenance; it's medicine, comfort, and a catalyst for connection. In today's fast-paced world, we've seen an increasing reliance on pharmaceutical solutions to health issues, often overlooking the holistic benefits of natural remedies and the healing power of human connection. This realization was compounded by the global pandemic, which highlighted the detrimental effects of isolation on mental and physical health. Med2Meals was born out of a desire to revive the ancient wisdom that food can heal and to harness the digital age's potential to bring people together over the healing power of meals. We envisioned a platform that not only encourages a natural approach to healing through diet but also fosters a sense of community and support among individuals facing health challenges. What it does Med2Meals connects individuals seeking natural dietary remedies for their health conditions with local chefs and home cooks who prepare and deliver home-cooked, healing meals. Users can input their specific health concerns or the type of medication they're aiming to supplement or avoid. The platform then suggests a variety of home-cooked recipes, each tailored to address those health issues with natural ingredients known for their healing properties. Beyond just providing recipes, Med2Meals offers a service where users can request these meals to be cooked and delivered by someone in their community. This feature aims to provide comfort through nourishing food while also opening the door to new friendships and a support network. The platform caters to a range of dietary preferences and health needs, ensuring that each user receives personalized care and nutrition. In essence, Med2Meals is more than a meal delivery service; it's a community-building tool that leverages the nurturing power of food to heal bodies and connect souls. How we built it Frontend Development : We utilized Next.js for the frontend to leverage its server-side rendering capabilities, ensuring a fast, and responsive user interface. Backend Infrastructure : Our backend is powered by Node.js and Express.js, forming a robust and scalable foundation. Integration of AI Technologies : We partnered with Together.ai to fine-tune and deploy Large Language Models (LLM) and Diffusion models tailored to our specific needs. These models are crucial for generating personalized meal recommendations and understanding user queries in natural language. AI Agents for Data Exchange : The seamless execution of LLM and diffusion models, along with data exchange between them, is facilitated by AI agents using fetch.ai. This innovative approach allows for real-time, intelligent processing and a highly personalized user experience. Blockchain Technology for Transactions : We employed Crossmint for blockchain ledger transactions between the user and chef. This ensures that every cooking opportunity a chef receives is cryptographically signed, providing a transparent and secure method to verify a chef's credibility through the NFTs they have minted. Database Management : MongoDB serves as our database management system, offering a flexible, scalable solution for storing and managing our data. API Documentation : The entire API documentation was meticulously maintained in a Postman Workspace. Development Tools : We adopted Bun as our package manager and JavaScript runtime. Bun's high performance and efficiency in package management and execution of JavaScript code significantly enhanced our development workflow, allowing us to build and deploy features rapidly. Challenges we ran into Customized Recipe Generation : We encountered difficulties in crafting the ideal few-shot prompts for Large Language Models (LLMs) to generate customized recipes, which was crucial for tailoring dietary solutions. Building AI Agents with Fetch.ai : The challenge of navigating Fetch.ai's occasionally misleading documentation was significant. However, the assistance from the Fetch.ai team was instrumental in overcoming these hurdles. Idea Pivot : Initially, we faced a setback with our original concept, which seemed too cliché after our initial pitch to judges. This led us to pivot to a more unique and impactful problem statement, which ultimately defined our project's direction. Accomplishments that we're proud of Successful Pivot : The decision to pivot our idea proved to be valuable. Moving away from a generic concept to tackle a unique problem statement has positioned us distinctively in the space. Diverse Technological Learning : Each team member embraced the challenge of learning new technologies, from AI agents and prompt engineering for LLMs to crypto signing. This diversity in learning has been one of our project's most enriching experiences. What we learned AI Agents : The project deepened our understanding of AI agents, enhancing our ability to deploy intelligent solutions. Fine-tuning LLMs : We gained valuable insights into the process of fine-tuning Large Language Models to meet specific project needs. Crypto Signing : The importance and application of crypto signing were key learnings, opening new avenues for secure data handling. Teamwork : The project underscored the indispensable value of teamwork in overcoming challenges and achieving collective goals. What's next for Med2Meals Speed Optimization : Currently, the process of fetching custom recipes using LLMs is slower than desired. Our immediate focus will be on improving the speed of this feature to enhance user experience. User Interface Improvements : We plan to refine the user interface to make it more intuitive and user-friendly, ensuring that our platform is accessible to everyone, regardless of their tech-savviness. Integration with Health Platforms : We are looking into integrating Med2Meals with existing health platforms and medical databases, to provide users with a seamless experience that bridges the gap between medical advice and dietary solutions. <div