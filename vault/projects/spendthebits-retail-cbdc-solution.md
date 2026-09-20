---
slug: "spendthebits-retail-cbdc-solution"
url: "https://devpost.com/software/spendthebits-retail-cbdc-solution"
title: "SpendTheBits Retail CBDC Solution for regional banks & MSB's"
hackathon: "Ripple CBDC Innovate "
organization: "Ripple"
winner: true
words: 625
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "user/legal_professional"
  - "substrate/financial_record"
---

# SpendTheBits Retail CBDC Solution for regional banks & MSB's

> Our retail CBDC portal is tailor-made for regional banks & MSBs to easily send cross-border payments, manage corresponding ledgers, and provide their end users a platform for remittance requests.

[Devpost](https://devpost.com/software/spendthebits-retail-cbdc-solution) · hackathon [[Ripple CBDC Innovate]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[immigration_refugee]]
**user** [[legal_professional]]
**substrate** [[financial_record]]

**stack** django, postgresql, react-js, redis, typescript, websockets, xrpl

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spendthebits retail cbdc solution for small regional banks
- links and logins for test by judges

## Body

Transactions Dashboard for MSB / Bank Remittance List Outward Exchange Rate Offer for cross-currency settlement Slab Based Fee Structure KYC Screen with transaction limit monitoring Inspiration We support Ripple's collaboration with central banks, aiming to establish CBDC frameworks. Our focus is on creating an accessible layer beneath this framework, empowering smaller financial institutions to leverage CBDC capabilities, including affordable cross-border remittances through Ripple's system. What it does The system consists of two portals: An institutional portal for initiating and approving cross-border payments, featuring foreign exchange rates, personalized end-customer limits based on their KYC level, and robust customer ticket support for both banks and end-users. A web portal tailored for customers of regional banks, facilitating the submission of cross-border remittance requests. The remittance process can be finely tuned in accordance with the customer's KYC level. The portal incorporates real-time AML checks and maintains an audit history to ensure a secure and risk-conscious experience. ( Ongoing) How we built it Our aim was to develop a robust, real-time, and secure cross-border payment system for institutions. This system seamlessly integrates with existing platforms like SWIFT, while channeling all financial data through the portal. Over the past two years, we've diligently crafted this technology, maintaining a strong partnership with XRPL. Our dedicated global team of eight collaborates daily to refine our product, leveraging the XRP Ledger backend. The CBDC Retail Portal was conceived exclusively for the Ripple CBDC Innovate hackathon, and we're eagerly anticipating the judges' feedback on our creation. Challenges we ran into We encountered several challenges during the development of this portal, including: Multi-signing across diverse languages and frameworks: Integrating multiple signers across different programming languages (e.g., JavaScript and Python) presented significant coordination and compatibility hurdles. Complex fee structure for financial institutions across various currencies: Implementing a slab-based fee approach that caters to diverse currencies while ensuring accuracy and transparency posed a notable challenge. Creating intuitive dashboards and reports: Designing dashboards and reports that align with the preferences and needs of financial institutions, providing a comprehensive and actionable overview, required careful consideration and iteration. Dynamic multi-role platform: Establishing a multi-role platform with real-time configurable role permissions tailored to each bank's specific requirements demanded intricate development to ensure flexibility and security. Accomplishments that we're proud of Dynamic Role and Permission Model: We successfully developed a flexible role and permission system, allowing banks to configure various roles with specific permissions according to their unique requirements. The complexity of making this system both dynamic and controllable was a challenging yet rewarding achievement. Professional and User-Friendly Remittance Flow: We designed a professional and user-friendly process for a complex task like remittance. By integrating the power of blockchain with a well-crafted web portal, we've created a seamless experience, offering the best of both worlds. Empowering End Users: Our platform enables end users to create their own remittance requests, which can be automatically or manually approved by the bank based on the customer's KYC levels. This feature enhances user autonomy while maintaining security and compliance standards, depending on the customer's KYC levels. What we learned Deep understanding of the various features offered by XRP Ledger Playing around with xrpl-py, xrpl-js libraries. What's next for SpendTheBits Retail CBDC Solution for small regional banks Integrate more payout partners for different countries for delivering the end money faster to the beneficiary . We are in talks with Apaylo, Fortress Trust , Mozrt (WireFX), and other partners for the same. Integrate more FX rate providers for more options to users. Integrate oracle based FX for more trust. Links and logins for test by judges Demo Bank of Canada Link : https://portal-demo-bank-of-canada-xmney.netlify.app/ Username : sushanta+20@spendthebits.com Password : STBpassword12@ Passphrase : sh8sAN4MUNpyVoMP3vTv1h4i7b8SF Demo Bank of India Link : https://portal-demo-bank-of-india-xmney.netlify.app/ Username : sushanta+r@spendthebits.com Password : STBpassword12@ Passphrase : snHxHJPdF2VW2HkUp2MN48CCqNdgE <div