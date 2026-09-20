---
slug: "tradeoff-c24mwv"
url: "https://devpost.com/software/tradeoff-c24mwv"
title: "TradeOff"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 968
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# TradeOff

> Stock market simulation game where students race to beat the market.

[Devpost](https://devpost.com/software/tradeoff-c24mwv) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]]

**stack** api, cerebras, dynamodb, english, graphite, javascript, python, react, tailwindcss

## How they structured the write-up

- 💭 inspiration
- 🎓 what it does
- ⚙️ how we built it
- 🚧 challenges we ran into
- 💪accomplishments that we're proud of
- 📖what we learned
- 🔮 what's next for tradeoff

## Body

💭 Inspiration Financial literacy remains a critical gap for many people, especially young adults entering the investment world. Traditional learning methods often feel abstract and disconnected from real market dynamics. We were inspired to create an engaging, risk-free environment where users could develop genuine investment skills through hands-on experience. The idea came from recognizing that the best way to learn investing isn’t through textbooks, but through practice, without the fear of losing real money. We wanted to bridge this gap by combining gamification with real-world market simulation, making financial education both accessible and exciting while showcasing the powerful tools and opportunities available through RBC’s investment platform. 🎓 What it Does TradeOff is an interactive stock market simulation game specifically designed to empower students to achieve their life goals through smart investing. Players begin by setting personalized financial milestones, whether it’s saving for their first car, funding that dream graduation trip, or building an emergency fund and the game creates customized investment scenarios to help them reach these targets. The platform features a realistic trading environment where students can practice going long or short on various holdings, guided by a dynamic news feed that influences stock prices in real-time. This mimics actual market conditions and teaches players how external events impact investment decisions, building crucial financial literacy skills without any real-world risk. What sets TradeOff apart is its seamless integration with RBC InvestEase’s philosophy of making investing accessible and confidence-building. As students play and learn, they discover how early and consistent investing can accelerate their path to achieving real-life goals. The game demonstrates InvestEase’s user-friendly approach to portfolio management, automated investing features, and goal-based investment strategies. ⚙️ How We Built It We built our user interface using React.js with Tailwind CSS, creating an intuitive and responsive design with candles and the news functionality as well. RBC API Integration: We integrated RBC’s Portfolio Simulation & Market Sandbox API to provide authentic portfolio return calculations and realistic market behaviour. Our backend combines Python and JavaScript to handle complex financial calculations, including sophisticated order book management and interpolation logic for accurate portfolio returns. This dual-language approach allowed us to leverage Python’s financial computation strengths while maintaining JavaScript’s web integration capabilities. Database: We implemented Amazon DynamoDB as our primary database solution, efficiently managing our order book data, game state persistence, and user portfolio tracking. The NoSQL structure perfectly accommodates the dynamic nature of trading data and user interactions. Real-time updates: We utilized DynamoDB Streams to enable instantaneous stock market data updates, ensuring that price movements and market events are reflected immediately across all user sessions, creating an authentic trading experience. Hardware Deployment: We deployed our application on QNX hardware, showcasing the platform’s capabilities in running modern web applications and demonstrating the versatility of embedded systems in financial applications. Development Workflow: We accelerated our development process using Graphite’s AI-powered code review platform, which helped us maintain code quality while enabling rapid iteration and feature deployment through streamlined pull request management. News Feed: As for the news feed, we used Cerebras Inference API calls to generate fake stock market news that seemed authentic to add authenticity and depth for the project. Having low latency was crucial for this point. 🚧 Challenges We Ran Into Implementing the core order book logic proved more intricate than anticipated. We had to balance realism with educational value, ensuring the simulation was complex enough to teach real concepts while remaining accessible to beginners. Market Simulation Authenticity: Achieving realistic stock market behaviour through randomization was particularly challenging. We needed to create price movements that reflected genuine market dynamics, incorporating volatility clustering, momentum effects, and news-driven price actions, while maintaining educational clarity. The interpolation logic for portfolio returns required careful calibration to ensure mathematical accuracy. 💪Accomplishments that We're Proud Of Built a full-stack financial simulation in under 36 hours. all while balancing workshops, interviews, activities, and attending every food event. Integrated RBC’s Portfolio Simulation & Market Sandbox API, delivering realistic portfolio returns and market behaviour. Created dynamic, AI-powered news feeds with Cerebras API, simulating authentic market events that influence gameplay. Implemented real-time market updates with DynamoDB Streams, ensuring all players see instant market movements. Deployed on QNX hardware, demonstrating the adaptability of our app across embedded systems. Collaborated and team bonded as four Western students, iterating quickly, solving challenges, building and losing sleep together. 📖What We Learned We deepened our understanding of Amazon Web Services, particularly DynamoDB’s capabilities and best practices. We also learned to leverage DynamoDB Streams for real-time applications opened our eyes to the power of event-driven architectures in modern web development. API Integration Expertise: Working with RBC’s financial APIs taught us valuable lessons about handling external data sources, managing authentication, and building robust error handling. These skills are directly applicable to professional software development. Collaborative Development: Using Graphite’s platform enhanced our understanding of modern development workflows, code review processes, and the importance of maintaining clean, reviewable code even under tight deadlines. We learned how AI-powered tools can accelerate development without sacrificing quality. 🔮 What's Next for TradeOff We envision TradeOff evolving into a comprehensive financial education ecosystem with exciting new features and capabilities: Enhanced Asset Universe: Expanding beyond traditional stocks to include bonds, ETFs, mutual funds, cryptocurrencies, commodities, and sector-specific investments. This would give students exposure to diverse asset classes and modern portfolio theory in action. Advanced Trading Features: Implementing options trading, margin accounts, dividend reinvestment programs, and international markets to provide comprehensive investment education covering both basic and sophisticated strategies. Industry-Specific Scenarios: Creating specialized simulation modules for different sectors (technology, healthcare, energy, ESG investing) with industry-specific news feeds and market dynamics, helping students understand sector rotation and thematic investing.- Multiplayer Tournament System: Introducing multiplayer modes where students can challenge each other, join investment clubs, and compete in friendly tournaments and long-term portfolio challenges with real scholarship incentives. <div