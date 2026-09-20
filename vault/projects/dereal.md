---
slug: "dereal"
url: "https://devpost.com/software/dereal"
title: "DeReal"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 1102
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# DeReal

> A social app prompting you to share spontaneous moments. Earn rewards with on-chain Social Scores and enjoy gamified streaks—all in a seamless, user-friendly experience.

[Devpost](https://devpost.com/software/dereal) · hackathon [[-REDACTED- Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
**user** [[general_public]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** aurora, blockchain, next.js, node.js, shadcn, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that i'm proud of
- what's next for dereal

## Body

Landing Home page Profile Page Ad/banner creation De Real Userflow and Revenue strategy Inspiration The main inspiration comes from the motivation to build a consumer-centric app that could on-board users on web3 platforms, while also making it engaging. I've seen a lot of products bloom, but most are infra-related, social products need some refinement in the web3 space and I believe that a little support from the right people and a big push from my side can result in something good. The product had some small verification from people, so I am already continuing it. What it does DeReal is a decentralized social media platform encouraging users to share spontaneous, real-life moments by sending random daily prompts to capture and post photos. It promotes authenticity and transparency while rewarding user engagement through an on-chain Social Score, incentives, and gamified features like streaks. DeReal leverages blockchain technology to manage user incentives and data ownership securely, providing a seamless and user-friendly experience. The platform monetizes through paid promotions and ads, offering advertisers access to authentic user engagement. Users can post photos with captions, and hashtags, on-chain. The relevant data is stored on IPFS, while the hashes are maintained in the smart contract's state. Apart from the regular posts, some special events pop up randomly, with a 2-minute timer to allow the user to click a quick photo and post it. Posting the events leads to extra points for the users as engagements, meaning their incentives would be better. A small highlight on the ads and paid promotions is that anyone can fill out a form with the relevant details, which will then be displayed to the users. How we built it DeReal is built by combining modern web development technologies with blockchain integration to create a seamless and user-friendly experience. Here's how: Frontend Development: Used Next.js for building a responsive and dynamic user interface, along with Tailwind CSS, and Shadcn for styling to ensure a clean and modern design. Chain Integration: Integrated with the Aurora blockchain platform to leverage its high throughput and scalability. This allowed me to deploy smart contracts efficiently. Also, the cheap gas fees and the fact that is posts the tix on Near Chain is Simplifying User Experience: Implemented Aurora Pass for seamless wallet management, enabling automatic wallet creation and abstracting blockchain complexities from the users. This works only on Mainnet thought. On-Chain Social Score: Developed smart contracts in Solidity to calculate and manage users' Social Scores on-chain, incentivizing engagement and interaction within the platform. Random Prompts Feature: Built a backend service to send random prompts to users throughout the day, encouraging them to capture and share spontaneous moments. Gamification Elements: Added features like streaks and badges to reward consistent participation, enhancing user engagement through gamified experiences. Paid Promotions and Ads: Integrated an advertising platform where businesses can submit ads via a form, choosing from one-time payments or subscription models, which are then displayed to users in a non-intrusive manner. Data Handling and Privacy: Ensured user data is handled securely, giving users control over their data-sharing preferences and rewarding them for participation. Challenges we ran into Blockchain Integration and User Experience Complexity Abstraction: One of the main challenges was integrating blockchain features without overwhelming users with technical details. We needed to ensure that interactions like wallet creation, transactions, and on-chain activities were seamless and intuitive. Gasless Transactions Limited Support on Aurora Network: Implementing gasless transactions to remove barriers for non-crypto-savvy users was a significant challenge. Tools and SDKs that facilitate gasless operations, such as the Dynamic SDK and paymaster models, currently do not support the Aurora network. This limitation meant I couldn't leverage existing solutions to abstract gas fees away from users on this platform. Complexity Remains: Without native support for gasless transactions on Aurora, the complexity of handling transaction fees remained an obstacle. Users still needed to manage gas fees, which adds friction to the user experience and could deter mainstream adoption. Random Prompt Feature Efficient Scheduling: Building a backend service to send random prompts throughout the day required creating an efficient and scalable scheduling system. Monetization Strategy Implementation Advertising Platform Development: Creating a system where advertisers could submit ads, choose payment models, and track performance involved building comprehensive backend and frontend solutions. User Experience Balance: Integrating ads in a way that didn't disrupt the user experience required thoughtful design and placement strategies. Security Concerns Smart Contract Security: Protecting against vulnerabilities in smart contracts required thorough testing, code audits, and adherence to best practices. User Engagement and Retention Feature Prioritization: Deciding which features to develop first to provide the most value and keep users engaged was a strategic challenge. Feedback Integration: Gathering user feedback and iterating on the platform without significant delays demanded an agile development process. Time Constraints Hackathon Deadline: Building a fully functional MVP within the limited time frame of the hackathon required efficient time management and prioritization of core features. Accomplishments that I'm proud of Seamless Blockchain Integration: Successfully abstracted blockchain complexities for a user-friendly experience. Aurora Pass Wallet Management: Implemented automatic wallet creation and secure management. Dynamic Social Scoring: Built an on-chain Social Score system to incentivize engagement. Gasless Transaction Exploration: Investigated solutions despite limited support on Aurora for gasless transactions. Random Prompt System: Developed a scalable backend for random prompts to capture real-life moments. Advertising Platform: Created a flexible paid promotions system with multiple payment options. Gamification Features: Added streaks and badges to enhance user engagement and retention. *User-Focused Design: Prioritized user experience and simplicity throughout the development. Meeting Hackathon Deadline: Delivered a fully functional MVP within the hackathon timeframe. ## What we learned User-Centric Blockchain Design: Simplifying blockchain interactions is key for mainstream adoption. Importance of Privacy and Control: Users value data privacy and transparency, making it crucial for trust. Challenges of Gasless Transactions: Lack of network support for gasless models on Aurora presents obstacles. Iterative Development Value: Agile iterations and feedback loops greatly enhance product quality and user experience. What's next for DeReal This is the most important part: Building a better ad system. I wanted to build an ad contract that could track on-chain user activity and maintain a data set for them. Using it other companies as well as social platforms could pull ads on their dapps, to generate revenue and enable users to pay for gas fees by watching ads. Improvement towards the Random Prompt timer: Currently it's working on a centralized server that triggers it, in the future I want to build a fully trustable Random Number generator. Advanced Gamification: Improve the streaks algorithm and make it work better. This will help with user calculating their payout. <div