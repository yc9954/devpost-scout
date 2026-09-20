---
slug: "domaingpt"
url: "https://devpost.com/software/domaingpt"
title: "DomainGPT"
hackathon: "Web3 and AI Unstoppable Hackathon | Unstoppable Domains & AWS"
organization: "Unstoppable Domains"
winner: true
words: 676
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# DomainGPT

> Streamline your blockchain domain management with our Telegram bot, offering real-time domain availability checks, comprehensive statistics, and top holder insights—all at your fingertips.

[Devpost](https://devpost.com/software/domaingpt) · hackathon [[Web3 and AI Unstoppable Hackathon - Unstoppable Domains - AWS]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]]

**stack** duneapi, python, python-telegram-bot, telegram, unstopabledomainapi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for domaingpt

## Body

Unstoppable Domain Bot for Telegram Inspiration The inspiration for this project came from the growing popularity and adoption of blockchain domains. I saw a need for a user-friendly tool that could help both domain enthusiasts and professionals manage and explore blockchain domains effortlessly. Leveraging the widespread use of Telegram, I aimed to create a convenient solution that integrates seamlessly with the Unstoppable Domains ecosystem. What it does The Unstoppable Domain Bot for Telegram provides several key functionalities: Domain Availability Check : Users can check if a specific domain name is available for purchase and get a direct link to buy it if it is. Domain Statistics : The bot provides comprehensive statistics about registered domains and subdomains, including a breakdown by top-level domain (TLD). Top 10 Domain Holders : Users can view the top 10 domain holders, including the number of domains they own. List Domains : The bot generates a list of all domains associated with a given domain owner and provides the result in a CSV file. User Count : Displays the total number of users who have interacted with the bot. Help Command : Provides a detailed list of available commands and instructions on how to use them. How I built it Setting Up the Bot : I initialized a Telegram bot using the python-telegram-bot library and configured it with the necessary token and command handlers. Integrating APIs : I integrated the Unstoppable Domains API to check domain availability and retrieve owner information. I used the Dune Analytics API to fetch domain statistics and top domain holder data. Developing Features : Implemented various commands like /check , /udstats , /top10 , and /list to handle different user requests. Added inline query support to allow users to interact with the bot in any chat. User Data Management : Created a mechanism to track user interactions and maintain a count of unique users. Testing and Optimization : Conducted rigorous testing to ensure smooth operation and accurate responses. Optimized the code for better performance and user experience. Challenges I ran into API Rate Limits : Managing API rate limits and ensuring the bot could handle multiple requests without exceeding these limits was challenging. I implemented efficient error handling and retry mechanisms to address this. Data Processing : Processing and presenting data from multiple sources in a concise and user-friendly manner required careful planning and implementation. User Interaction : Designing a user-friendly interface and handling various user inputs, including edge cases, posed challenges that I tackled through iterative testing and feedback. Security : Ensuring secure communication and handling of API keys and user data was paramount. I followed best practices to safeguard the bot and its users. Accomplishments that I'm proud of Successfully integrating multiple APIs to provide comprehensive domain management functionalities. Creating a user-friendly and efficient Telegram bot that simplifies blockchain domain management. Achieving a smooth and responsive user experience through thorough testing and optimization. Receiving positive feedback from initial users and seeing real-world use of the bot. What I learned Blockchain Domains : Deepened my understanding of blockchain domains, their registration, and management. Telegram Bot Development : Gained expertise in building and deploying a Telegram bot, handling user interactions, and integrating various functionalities. API Integration : Enhanced my skills in integrating multiple APIs and processing data efficiently. User Experience : Learned the importance of creating a user-friendly interface and providing clear, concise responses to user queries. What's next for DomainGPT Enhanced Features : Adding more functionalities such as domain price tracking, auction alerts, and advanced search filters. User Feedback : Continuously gathering user feedback to improve the bot's features and usability. Multi-Language Support : Expanding the bot's capabilities to support multiple languages to cater to a global audience. Community Engagement : Engaging with the blockchain domain community to promote the bot and collaborate on new features. Security Enhancements : Continuously improving the security measures to protect user data and ensure secure communication. I am excited about the future of DomainGPT and its potential to make blockchain domain management more accessible and efficient for everyone. <div