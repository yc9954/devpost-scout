---
slug: "cinance"
url: "https://devpost.com/software/cinance"
title: "Fundation"
hackathon: "Hackonomics 2025"
organization: "hackonomics"
winner: true
words: 896
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/labor_employment"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Fundation

> Fundation: Build your gaming empire, master the market

[Devpost](https://devpost.com/software/cinance) · hackathon [[Hackonomics 2025]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[labor_employment]]
**substrate** [[structured_db]] [[web_dom]]

**stack** c#, html, next.js, react, tailwindcss, typescript, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for fundation

## Body

Hire a Staff Get Income Make a new Game Gameplay Game Over Inspiration Our journey with Fundation began from a shared passion for two distinct yet fascinating worlds: finance and game development. We've always been captivated by the intricate systems of economic simulations and the creative freedom of tycoon games. The idea sparked from a desire to merge the strategic depth of managing financial assets with the engaging, iterative process of building a game studio from the ground up. We wanted to create a game that wasn't just about making money, but about understanding the dynamics of investment, market trends, and risk management, all wrapped in a fun, accessible package. What it does Fundation is a finance-themed game development tycoon game where players build and manage their own game studio. The core loop involves hiring employees, each with unique Tech and Design skills. Players then develop and publish games, strategically balancing their team's combined expertise. The game simulates market reception based on this balance: a well-balanced team leads to successful games, gaining popularity and followers, while an imbalanced team results in poor outcomes and a loss of followers. Beyond game development, players must navigate financial decisions, manage budgets, and potentially invest in company upgrades to grow their empire. How we built it Fundation was built as a multi-faceted project, consisting of both a game and a dedicated showcase website. For the game, we utilized Unity as the main game engine and C# for the logic language. We focused on developing a robust system for employee management and stat aggregation. Each employee object stores their individual Tech or Design values, which are summed up for active employees when a game is published. The crucial part was implementing the balance calculation. We devised a formula to determine the imbalance percentage between total Tech and Design stats. This percentage then dictates the game's quality tier (Excellent, Good, Poor, Very Poor). Based on this tier, we apply a popularity multiplier to a base popularity value, determining the actual popularity earned. Finally, this popularity directly influences the gain or loss of followers through a set conversion rate, driving player progression. Our showcase website was developed using the Next.js framework, alongside libraries like Tailwind CSS and React. This dual-component approach allowed us to not only build a functional game but also to effectively present our work to a wider audience One of the primary challenges was balancing the core stat system. Initially, it was either too easy to achieve perfect balance, making the game feel repetitive, or too punishing, leading to rapid player frustration. We spent significant time tweaking the imbalance percentage thresholds and the popularity multipliers for each game outcome tier to create a challenging yet rewarding progression curve. Another significant hurdle was ensuring the finance theme truly shone as the main concept. While the game development loop was engaging, integrating meaningful financial decisions that felt central to progression, rather than just an afterthought, proved complex. We wrestled with how to make investment opportunities, market fluctuations, and budgeting compelling without overwhelming the player with overly complex spreadsheets or abstract economic models. The goal was to make financial strategy as impactful as team management, which required careful design of revenue streams, expenditure points, and risk-reward scenarios within the game's economy. Finally, visualizing the impact of employee stats in a clear and intuitive way for the player presented its own set of difficulties. Early iterations made it hard for players to understand why their games succeeded or failed. We had to refine our UI feedback to prominently display the "Game Outcome" (e.g., "Very Poor!") and explicitly show the popularity gained/lost and follower changes Accomplishments that we're proud of What we learned This project taught us the immense importance of iterative design and rigorous playtesting, especially when dealing with numerical systems like stats and economies. What looks good on paper often needs significant adjustment in practice. We learned to prototype quickly, gather feedback, and be willing to completely overhaul mechanics that weren't serving the game's core loop. We also gained valuable experience in topics such as Financial Management because one of our main challenges in developing Fundation was the game balancing system, and in order to give our players a balanced playthrough we need to understand the Financial contect in Fundation and combine it with real world scenario, as for the Technological side, we learned more on Game Optimization, because in the making of Fundation we ran into multiple instances of game crashing because of unoptimized mechanics resulting in game creashes and heavy load, we learned many techniques so that our game are more optimized now. More broadly, it reinforced the idea that simplicity often leads to greater depth; a few well-tuned mechanics can be far more engaging than many complex, underdeveloped ones. What's next for Fundation For the future of Fundation, we envision expanding the game's depth with features like employee training and skill growth, allowing players to further specialize their team. We also plan to introduce market trends and genres, where certain game types are more popular at different times, adding another layer of strategic decision-making. Deeper investment opportunities beyond just studio upgrades, such as market trading or acquiring rival studios, are also on our roadmap to truly lean into the finance theme. Ultimately, we aim to make Fundation a rich, replayable simulation that appeals to both strategy and tycoon enthusiasts <div