---
slug: "pay-your-daddy"
url: "https://devpost.com/software/pay-your-daddy"
title: "Lumo"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 657
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Lumo

> Lumo: Split expenses instantly, no upfront payments. Empowering seamless, real-time cost-sharing for everyone—fast, fair, and hassle-free. 💸⚡

[Devpost](https://devpost.com/software/pay-your-daddy) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[retail_commerce]] [[security_privacy]]
**user** [[small_business]]
**substrate** [[code_repository]] [[financial_record]]

**stack** angular.js, axios, javascript, mongoose, typescript

## How they structured the write-up

- why we built this
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lumo?

## Body

Loading Page Home Page Adjust your monthly pledge Choose which members from the group that will cover the costs Choose which group you are paying for Shared credit card to pay Why we built this Unbanked and some underbanked individuals who lack access to traditional financial services face significant challenges in managing shared expenses such as rent, utilities, and groceries. These individuals are forced to rely on informal pooling like collecting physical cash or digital P2P payment tools like Zelle, PayPal, and Splitwise, which all facilitate post-transaction reimbursements. However, these methods are unreliable, as they depend on timely repayments, leaving the individual who fronts the payment vulnerable to delayed or unfulfilled reimbursements. For those already struggling with cash flow, this delay creates more financial strain. We believe that enabling real-time, equitable splitting of group expenses without requiring upfront payments from a single individual is crucial in serving unbanked and underbanked people. What it does Lumo enables people to split purchases in real-time at the point of purchase, unlike traditional P2P payment methods like Venmo, Zelle, PayPal, Apple Pay, and Splitwise, which require one person to pay upfront and rely on post-transaction reimbursements. Lumo directly divides payments among participants by charging the cards the users put on file. By integrating with existing payment methods like prepaid cards and ACH, Lumo provides an inclusive solution for unbanked and underbanked individuals, empowering them to manage shared expenses transparently and equitably. How we built it Lumo was built using a modern TypeScript stack, with React and Vite on the frontend, styled with Tailwind CSS , and managed with Zustand for real-time state handling. The backend leverages Node.js and Express , with MongoDB for data storage and Stripe for secure payment processing. We integrated AI tools like Bolt and Cursor to streamline development and optimize our codebase. By combining these technologies, we created a scalable, efficient solution for real-time expense sharing. Challenges we ran into One major challenge was obtaining POS access on Stripe for Apple Pay with Apple Cash , as both platforms require special permissions that take over 48 hours to secure—something we couldn't achieve within the hackathon's timeframe. Consolidating funds in real-time was difficult due to the absence of a standard protocol. We had to create a custom solution to synchronize multiple payment sources seamlessly, ensuring that payments could be split equitably without delays. Balancing security, efficiency, and user experience while integrating diverse payment methods required significant troubleshooting and fine-tuning. Accomplishments that we're proud of We're incredibly proud of developing a fully functional MVP that successfully handles real-time transactions. Despite the tight timeframe, we managed to integrate secure payments and achieve actual transaction processing, demonstrating the feasibility of our solution. What we learned This project deepened our understanding of the financial services landscape , especially the challenges faced by unbanked and underbanked individuals in managing group expenses. We gained insights into the reliance on informal systems and the gaps in existing payment infrastructures. Navigating technical barriers, like the limitations of single-source payment systems, taught us the importance of designing solutions that are both accessible and scalable . Additionally, working with new technologies enhanced our technical skills while tackling real-world problems, sharpening our ideation, problem-solving, and user-focused design capabilities. This experience reinforced the value of teamwork in creating a meaningful, inclusive solution. What's next for Lumo? We plan to expand Lumo by integrating with existing POS systems like Square to retrieve itemized receipts and merchant details in real-time, allowing users to split specific, pre-approved items instead of the entire bill. In the future, we aim to incorporate ML/AI features that can intelligently assign personalized items to each user based on past preferences and even exclude common items they've historically opted out of. Additionally, we want to market Lumo to the college-age demographic —a group we relate to personally, as we've all experienced the hassle of tracking shared expenses for groceries, dining, and group activities, especially when reimbursements are delayed. <div