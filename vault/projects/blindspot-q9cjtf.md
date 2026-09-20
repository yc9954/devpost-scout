---
slug: "blindspot-q9cjtf"
url: "https://devpost.com/software/blindspot-q9cjtf"
title: "Blindspot"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 684
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/media_journalism"
  - "substrate/structured_db"
---

# Blindspot

> In today’s digital age, misinformation erodes trust and democracy. Blindspot, a gamified app, empowers users to spot fake news, sharpen critical thinking, and enhance media literacy.

[Devpost](https://devpost.com/software/blindspot-q9cjtf) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]] [[media_journalism]]
**substrate** [[structured_db]]

**stack** flask, langchain, newsapi, nextjs, openai, python, react, typescript

## How they structured the write-up

- 💡 inspiration 💡
- ⚙️ what it does ⚙️
- 🛠️ how we built it 🛠️
- 😣 challenges we ran into 😣
- 🎉 accomplishments we are proud of 🎉
- 📚 what we learned 📚
- ⏭️ whats next ⏭️

## Body

💡 INSPIRATION 💡 We wanted to solve a pressing global problem. While we were going through the brainstorming phase, a member on our team read an article titled “Recognizing Fake News Now a Required Subject in California Schools”, which inspired the idea of a gamified app to discern fake news. In today’s digital age, the sheer volume of information at our fingertips can be overwhelming. With the rise of social media and the constant flow of news, it has become increasingly challenging to distinguish between credible information and misinformation. Fake news not only spreads rapidly but also has the potential to influence public opinion, incite unrest, and undermine trust in legitimate sources, ultimately threatening our democracy. We built Blindspot in order to solve this problem by training young adults to distinguish between fake and real news. ⚙️ WHAT IT DOES ⚙️ Blindspot is a game that presents the user with a series of news articles-- some articles are fake, others are real. Articles are presented one at a time, and each time, the player's goal is to determine whether the article they are reading is fake or real. As the user advances in this game, fake articles will feel increasingly real, making the game more difficult. 🛠️ HOW WE BUILT IT 🛠️ Our frontend is built with Next.js, React, and TypeScript. In the backend, we connected a Python Flask API with OpenAI’s GPT-4o using LangChain to generate fake articles to show to players. We also use the NewsAPI to fetch real articles to provide a mix of real and fake. 😣 CHALLENGES WE RAN INTO 😣 It turns out, it's incredibly difficult to find a dataset of high-quality recent news articles. With the recent push in AI, massive proprietary datasets of high-quality content are heavily paywalled, and even APIs are heavily rate-limited. As such, we had to get creative to find content that is convincing. We also found that modern LLMs are safeguarded pretty heavily, so convincing one to generate high-quality fake news was a challenge. Through much prompt engineering, we were able to get the models to generate very realistic & convincing fake news (scary!), where often times even our own team had a <80% accuracy rate! 🎉 ACCOMPLISHMENTS WE ARE PROUD OF 🎉 Initially, we had several ideas that we wanted to implement, but we were able to combine them in a way that made our final idea (Blindspot) better than any of the initial ones. Many of our team members were unfamiliar with TypeScript, but we were able to ramp up quickly enough in order to help with the frontend. Despite the time constraints, we are also proud that we were able to successfully connect the backend to the frontend in a short amount of time. The game is also addictively fun/hilarious to play! Our team enjoyed plenty of good laughs while building the app. 📚 WHAT WE LEARNED 📚 We learned to collaborate effectively as a team. Before this occasion, we were strangers, but within a day, we merged our varied ideas, allocated tasks based on individual strengths, implemented frontend and backend code, and integrated them to develop an MVP. A few team members were new to LLM models. Through this hackathon, we discovered the remarkable potential and user-friendliness of these models in crafting exceptional products. ⏭️ WHATS NEXT ⏭️ Blindspot is set to revolutionize how users engage with news and enhance their media literacy. We plan to introduce daily or weekly challenges to keep users engaged and returning to the app regularly. To further involve our community, we’ll allow users to submit articles they encounter for verification and inclusion in the game, making the experience more interactive and user-driven. A multiplayer mode will enable users to compete in real-time to identify fake news, adding a competitive edge to the learning process. We’ll also provide advanced analytics, giving users detailed insights into their performance and highlighting areas for improvement. Additionally, we’ll include in-depth educational modules on media literacy, the psychology of misinformation, and fact-checking techniques, ensuring users are equipped with the knowledge to navigate the complex media landscape effectively. <div