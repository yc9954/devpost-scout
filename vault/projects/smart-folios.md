---
slug: "smart-folios"
url: "https://devpost.com/software/smart-folios"
title: "Smart Folios"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 943
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/genomic_bio"
---

# Smart Folios

> Using AI to create highly personalized portfolios that meet financial goals unique to every investor.

[Devpost](https://devpost.com/software/smart-folios) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: benchmark_measured</sub>
**substrate** [[genomic_bio]]

**stack** android, firebase, ios, javascript, machine-learning, node.js, numpy, pandas, python, react, react-native, scikit-learn, scipy, stock-market-data

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart folios

## Body

Splash Screen with Login Your risk profile Welcome Screen to start new investment Tell us about your finances 1 Investment experience Tell us about your finances 2 Select your age and career Your investment goals Your goal details Portfolio View: Statistics Portfolio View: Assets selected Safety net Investment personalization loading Portfolio View: Statistics Tooltip My Folios Portfolio View: Annual returns percentage Portfolio View: Portfolio return vs benchmark Portfolio View: Drawdown and monthly returns Your portfolio preferences Thematic folios Portfolio View: Statistics Tooltip Home view with curated folios for beginner folios Popular folios Inspiration Traditionally, most self-serve investment platforms provided standard investment portfolios for the users to choose from. While many beginner investors are content with that, advanced investors usually tend to create custom portfolios by doing their own research or use premium financial advisory services. We believe that data-driven investment is the best form of investing and it should not be a privilege available only to the elite few. Hence, we built Smart Folios to create a free platform where anyone, regardless of their net worth, financial needs or experience, is able to get a highly customized portfolio that is tailor-made to suit their unique financial goals and risk tolerance with years of data to back that up. What it does Smart Folio allows investors of all age, career and experience levels, to quickly onboard and get a tailor-made mix of assets to meet their short and long term investment goals. Users can create as many custom portfolios as they want, by providing unique goals every time. For example, they can choose between a varying level of risks from low-risk-low-return to high-risk-high-return portfolios, select multiple investment themes like financial, blockchain and robotics, and provide actual expected returns on their money in a given duration. Smart Folio then uses its proprietary AI-based Asset Selection and Portfolio Optimizer to create a unique portfolio mix for the given input. There is no other investment platform that is able to meet such granular levels of investment goals and other constraints. Moreover, users can also choose to instead select among a hand-curated cluster of portfolios that are common and very popular and devised by experts in the market e.g. the well-known ‘Lazy Portfolio’. Our mission is to empower each and every individual to make the best use of their money and park it somewhere they would feel comfortable and not stressed about. How we built it At the core of our application is an AI-powered Portfolio Optimizer that reads the “Investment DNA” of our users which include details like current liquidity, risk tolerance, both long and short-term financial goals and even investment preferences. The optimizer crunches real-time market data of hundreds of Stocks, ETFs and Bonds and spits out a portfolio with a unique set of assets and weights. We then store this data into Firestore DB (from Firebase) using a Node-JS backend. For UI, we use React Native to create Android and iOS apps that help the user through onboarding and creating their dream custom portfolio. We also use our optimizer to come up with some hand-curated portfolio groups based on Expert Recommendations, which the users can also select from. Challenges we ran into The biggest challenge was to design a generic portfolio optimizer that can construct highly personalized portfolios meeting most of the targets and preferences set by the user. We had to deal with millions of data-points of daily market prices for hundreds of assets and train our ML models on them so they can construct a unique portfolio in real-time. This portfolio would have to meet a myriad of user objectives ranging from goals, experience, risk profile to preferences and optimize on a number of objectives such as maximizing return and Sharpe Ratio and minimizing volatility. We ran into several technical difficulties and important decision-making points while building this algorithm, which is so personalized but yet so generic and extensible. Accomplishments that we're proud of We did extensive research to come up with the novel machine learning model that powers our optimization engine. We are currently working towards a publication of the same. Our optimizer generated some incredible portfolios which pleasantly surprised us! For eg., a simple 3 asset portfolio with 32% VTI, 42% BND and 26% VXUS produced returns that were growing even at the time of recession when the standard SnP500 index fell. We came across several such smart portfolios. We successfully collaborated with a team of very diverse skill sets and geographical locations. One of our teammates is in India while the rest of us are located in the United States. What we learned Portfolio optimization is a hard problem but not an impossible one. By taking into account historical stock data for hundreds of assets including stocks, ETFs, and bonds, we are able to accurately create unique portfolios that can meet any financial constraints. With such a tool like ours in hand, our users can now make a better-informed decision about where to invest their money and be confident about it. What's next for Smart Folios In the future, we plan to add advanced features like Machine Learning-based Rebalancing Strategies that periodically adjust the assets in the portfolio based on the latest market data. We will also keep the user updated on the rebalancing done in their portfolio using alerts. We also believe everyone should have access to these advanced money-making strategies without having to pay a hefty fee. We want to enable the users to be able to automate their investments from our app by connecting their brokerage accounts. These future steps are aligned with our mission of financial inclusion and independence for everyone! iOS Build Link: https://rink.hockeyapp.net/apps/c0ed61be14d34a88b28bcdb27ac8b945 <div