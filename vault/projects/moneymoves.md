---
slug: "moneymoves"
url: "https://devpost.com/software/moneymoves"
title: "MoneyMoves"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 695
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# MoneyMoves

> Personalized stock insights scraped from your favourite websites.

[Devpost](https://devpost.com/software/moneymoves) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, beautiful-soup, express.js, next.js, numpy, pandas, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moneymoves

## Body

Logo Inspiration In today's fast-paced world, the average person often finds it challenging to keep up with the constant flow of news and financial updates. With demanding schedules and numerous responsibilities, many individuals simply don't have the time to sift through countless news articles and financial reports to stay informed about stock market trends. Despite this, they still desire a way to quickly grasp which stocks are performing well and make informed investment decisions. Moreover, the sheer volume of news articles, financial analyses and market updates is overwhelming. For most people finding the time to read through and interpret this information is not feasible. Recognizing this challenge, there is a growing need for solutions that distill complex financial information into actionable insights. Our solution addresses this need by leveraging advanced technology to provide streamlined financial insights. Through web scraping, sentiment analysis, and intelligent data processing we can condense vast amounts of news data into key metrics and trends to deliver a clear picture of which stocks are performing well. Traditional financial systems often exclude marginalized communities due to barriers such as lack of information. We envision a solution that bridges this gap by integrating advanced technologies with a deep commitment to inclusivity. What it does This website automatically scrapes news articles from the domain of the user's choosing to gather the latests updates and reports on various companies. It scans the collected articles to identify mentions of the top 100 companies. This allows users to focus on high-profile stocks that are relevant to major market indices. Each article or sentence mentioning a company is analyzed for sentiment using advanced sentiment analysis tools. This determines whether the sentiment is positive, negative, or neutral. Based on the sentiment scores, the platform generates recommendations for potential stock actions such as buying, selling, or holding. How we built it Our platform was developed using a combination of robust technologies and tools. Express served as the backbone of our backend server. Next.js was used to enable server-side rendering and routing. We used React to build the dynamic frontend. Our scraping was done with beautiful-soup. For our sentiment analysis we used TensorFlow, Pandas and NumPy. Challenges we ran into The original dataset we intended to use for training our model was too small to provide meaningful results so we had to pivot and search for a more substantial alternative. However, the different formats of available datasets made this adjustment more complex. Also, designing a user interface that was aesthetically pleasing proved to be challenging and we worked diligently to refine the design, balancing usability with visual appeal. Accomplishments that we're proud of We are proud to have successfully developed and deployed a project that leverages web scrapping and sentiment analysis to provide real-time, actionable insights into stock performances. Our solution simplifies complex financial data, making it accessible to users with varying levels of expertise. We are proud to offer a solution that delivers real-time insights and empowers users to stay informed and make confident investment decisions. We are also proud to have designed an intuitive and user-friendly interface that caters to busy individuals. It was our team's first time training a model and performing sentiment analysis and we are satisfied with the result. As a team of 3, we are pleased to have developed our project in just 32 hours. What we learned We learned how to effectively integrate various technologies and acquired skills in applying machine learning techniques, specifically sentiment analysis. We also honed our ability to develop and deploy a functional platform quickly. What's next for MoneyMoves As we continue to enhance our financial tech platform, we're focusing on several key improvements. First, we plan to introduce an account system that will allow users to create personal accounts, view their past searches, and cache frequently visited websites. Second, we aim to integrate our platform with a stock trading API to enable users to buy stocks directly through the interface. This integration will facilitate real-time stock transactions and allow users to act on insights and make transactions in one unified platform. Finally, we plan to incorporate educational components into our platform which could include interactive tutorials, and accessible resources. <div