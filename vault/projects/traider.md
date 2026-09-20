---
slug: "traider"
url: "https://devpost.com/software/traider"
title: "traider"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1234
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# traider

> Trade smarter not harder! Upgrade your financial literacy with traider

[Devpost](https://devpost.com/software/traider) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** fast-api, figma, google-search-api, nvidia, openai, perplexity, v0, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for traider

## Body

Portfolio Page Homepage Simulation in Action Financial Calculator Leaderboard Setup Inspiration Finance isn’t a subject commonly taught thoroughly in schools, yet it plays a crucial role in everyone’s lives. Many people, especially students, grow up without exposure to financial concepts, making it challenging for them to navigate real-world financial decisions. This lack of financial knowledge can lead to overwhelming debt, poor savings habits, and financial stress. In our lives, we have seen that these knowledge gaps in finance can cause enormous hurdles when entering college, internships, or the corporate world as young adults struggle to manage their growing debt and earnings. What it does traider is an educational platform that provides beginner investors with mock trading simulations and instantaneous AI-powered feedback for their trades. Scraping REAL historical and current stock data from Yahoo Finance, traders can engage with accurate market data and place their trades over a user-specified simulation duration beginning at a specified start date. Unlike models trained on outdated datasets, our product offers real, relevant market and economic data based on the stock ticker and current date in the simulation, which we then synthesize with NVIDIA to supplement young traders with more robust information to fuel their financial decision-making. This allows users to make informed trades using accurate and up-to-date market information. Our product stands out from other trading simulations in that it allows students to pick any timeframe in the past to put their trading skills to the test. Further, our supplemental market events information provides a more detailed painting of the financial landscape during the simulation, encouraging informed investing. Our dynamic and colorful data insights allow students to examine takeaways, while our AI-powered feedback for each executed trade promotes healthy learning and detailed mistake analysis. The leaderboard and financial calculator features offer a social and educational playground for students to explore the world of trading while gamifying finance like never before. How we built it Frontend: Next.js Tailwind Vercel/v0: We ran multiple versions of v0 to fine-tune and perfect out front end while asking for abstract animations for the background and generated complex containers for the simulator page Shadcn: Awesome built-in Next.js UI library which provided interactive graphic cards for buttons and pop-outs Figma Canva Radix UI Lucid React Backend: NVIDIA: We used NVIDIA and NVIDIA Cloud Compute to test the model. We used NVIDIA bev dev on a T4 GPU Cloud Instance to run a Jupyter notebook through Ubuntu Linux to fine-tune Lama 70b on financial prediction data Vercel Hosting Fast API Perplexity: We used it for the AI stock trading feedback simulator OpenAI: Used NVIDIA llama-70B to generate responsive and instantaneous feedback on stock exchanges. Additionally, provided a section for students to ask questions about the stock market and other financial questions Google Search API: Scrape relevant market and economic events given a stock ticker and a date. Once we scanned financial news websites for economic data, we passed it through NVIDIA using llama 70B to get the best possible market consensus on a stock ticker and synthesize that information to display to users. This enhanced their decision-making process as they decided on how to place trades. Challenges we ran into Finding an accurate LLM to provide users feedback on their trades Providing a layout for the various data visualizations in an aesthetically pleasing and non-overwhelming manner Handling massive amounts of stock data from Yahoo Finance and parsing through it to calculate daily portfolio values with complex mathematical calculations Picking up new technology and integrating with databases with which we have no prior experience, such as Convex Handling the dynamic animations on the homepage Combining the v0 code with preexisting code and integrating the frontend with the backend Real-time data handling: stock and trading information datasets led to rate limits we faced when making our API calls Finding a logo that would encompass our product. We spent a lot of time ideating different designs on Figma Accomplishments that we're proud of Backend: We were excited to be able to integrate and leverage AI models, such as Perplexity and Llama 70B, NVIDIA Brev, and cloud computing, for numerous features of our trading simulation. These included providing young investors instantaneous feedback on their trades, parsing through and summarizing market data with Google Search API and Llama 70B, and offering an AI-powered chatbot that answers users' questions and concerns regarding finance and trading. We were also proud to utilize a database technology that was new to us, Convex, to store user information. Through Clerk, we could also set up secure user authentication through Google sign-in. Additionally, we leveraged the Yahoo! Finance API to consolidate and display financial stock data for any time frame the user needed, allowing the user to see detailed stock information, such as high, low, open, close, volume, and more. These complex calls and technology integrations allowed for a seamless user experience and analytical trading dashboard. Frontend: We are proud of our dynamic homepage UI and the detailed and analytical simulator page UI. Their seamless and intuitive interfaces make them easy to use for our young target audience. We paid close attention to the color scheme, ensuring that it aligns with our brand identity and creates a visually cohesive and inviting interface. The result is a user-friendly design that is both functional and appealing, providing an enjoyable experience for users of all experience levels. Additionally, the components we are most proud of are the Homepage for its nifty abstract animations, which make the page more exciting. The home page’s color palette is also bright, giving it a more vibrant feel since it is marketed towards students to encourage them to learn more about finance. Another page we are proud of is the trading simulation and portfolio analytics page. The UI is attractive and enhances the theme. Many of the boxes and the pop-out form offer interactive and dynamic components. We were also proud to be able to offer various features on our page in just 36 hours of coding, from financial calculators to a leaderboard to data visualizations regarding portfolio analytics. We thoroughly enjoyed building this engaging product and integrating the technical backend with an appealing front end. What we learned Through developing this project, we learned about the complexity of designing scalable backend architectures, handling real-time data processing, and optimizing system performance. We learned the importance of efficient database structuring to maintain data integrity while ensuring fast retrieval. Additionally, we also deepened our understanding of financial market mechanics, from order execution to portfolio management, and the challenges involved in simulating a fair and realistic trading environment. Most importantly, we gained valuable experience working collaboratively and iterating design choices to build the most reliable user-centric platform. What's next for traider Next mission for traider is to bring it to the real market with users of all age groups who are students to try our product out. We also plan on implementing more robust features, such as fine-tuning an LLM on trades and historical stock data to provide more tailored insights to users, developing a more social aspect of the platform to allow young investors to share their accomplishments with their networks, and integrating voice-based AI-powered chat support for our younger client base. We would also aim to build AI-generated weekly quizzes and maintain performance metrics and streaks to keep our users rewarded and engaged on a daily. Additionally, we would love to implement cryptocurrency in our platform. <div