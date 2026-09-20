---
slug: "blcokrok"
url: "https://devpost.com/software/blcokrok"
title: "Memecoooins"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 729
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "user/government_staff"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Memecoooins

> $50, A WALLET OF RANDOM MEMECOINS, AND 24 HOURS TO CHANGE YOUR FATE

[Devpost](https://devpost.com/software/blcokrok) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**user** [[government_staff]]
**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** blockchain, postgresql, sveltekit, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- business model
- challenges we faced
- accomplishments
- what we learned
- what’s next for memecoooins

## Body

Inspiration Memecoooins is inspired by the chaos and excitement of meme coins, where tokens can skyrocket by 10x, 100x, or crash just as fast. We wanted to turn that thrill into a simple, fun experience. For just $50, you get a shot at riding the highs and lows of the meme coin market without needing to be a crypto expert. With real-time updates and the chance to hit big or laugh at the chaos, Memecoooins makes investing entertaining, unpredictable, and easy to enjoy. What It Does Memecoooins makes crypto investing simple and fun. Here's how it works: You pay $50 and get access to a mystery crypto wallet loaded with a random mix of meme coins. The wallet is securely managed for you, so you don’t need to worry about private keys or setup. Watch your portfolio in real time as it updates hourly, showing how the value of your coins is soaring or crashing. When you're ready, you can redeem your wallet, gain full control of it, and decide to hold onto your coins or cash them out. How We Built It Technology Stack SvelteKit : Handles both frontend and backend with server-side rendering (SSR) , API routes, and reactive UI. PostgreSQL with Prisma : Ensures efficient data management and scalability. Blockchain Integration : Solana Blockchain : Creates wallets and processes transactions securely. Raydium API : Allocates random meme coins through token swaps. CoinGecko API : Tracks live token prices to update the dashboard in real-time. Stripe : Processes user payments. Clerk : Manages user authentication and sessions. Workflow Login & Purchase : Users log in via Clerk and pay $50 through Stripe . Wallet Creation : A Solana wallet is created and funded with $45 USDC . Random Meme Coins : Meme coins are randomly allocated via the Jupiter API . Dynamic Dashboard : Users track their wallet’s value with hourly updates powered by CoinGecko API . Cash Out Anytime : Users can redeem their wallet, convert coins to USDC, and withdraw their balance (minus a 10% profit share ). Business Model Service Fee : $5 from every wallet covers operational costs. Profit Sharing : We take a 10% cut of profits when wallets are redeemed. This aligns our success with the users'. Challenges We Faced Custodial vs. Non-Custodial Accounts Balancing user experience with compliance was tricky: Non-Custodial : Users control their wallets but limit our ability to manage funds. Custodial : Easier fund management but requires KYC, increasing user friction. Our Solution: The Gift Card Model We adopted a hybrid approach: Wallet Creation : Solana wallets are created on behalf of users without KYC. Crypto Allocation : Meme coins are purchased and stored securely in the wallet. Ownership Transfer : Users receive full control of their wallet and private keys during redemption. Fiat Conversion : KYC is only required for converting crypto to fiat, simplifying the onboarding process for casual users. Operational Challenges Transaction Fees : High fees and minimum swap amounts consumed initial funds quickly. Payment Issues : Cards were flagged by fiat-to-crypto platforms like Ramp and MoonPay during testing. We’re exploring solutions such as prepaid crypto cards and verified business accounts to resolve these issues. Hourly Price Updates Updating coin prices hourly was tough: Initial Problem : Vercel’s free tier limits cron jobs, leading to timeout errors. Solution : Switched to GitHub Actions for scheduled updates, ensuring smooth performance. Accomplishments Successfully integrated Solana for secure wallet creation and token allocation. Built an engaging, real-time dashboard using the CoinGecko API . Designed a hybrid wallet system that balances compliance and ease of use. Solved tough challenges creatively, like the gift card model and GitHub Actions cron jobs . What We Learned Balancing security, compliance, and user experience in crypto platforms is complex. Simplifying the onboarding process required innovative thinking. Real-world testing revealed unexpected issues, but overcoming them strengthened the platform. What’s Next for Memecoooins Deploy Real Crypto Transactions : Complete testing to ensure smooth functionality before live deployment. Enhance User Engagement : Add leaderboards, social sharing features, and gamification to boost excitement. Prizes Considered Wakaba Prize PearAI (YC24) Prize Best Overall Yay :3 Best UI/UX Most Kawaii Most Likely Meme Startup Would Blow Up on TikTok (WBUOT) Lowkey Actually Kind of Good (LAKOG) This Project is Awesome (TPIA) Most CVRVEY Website I’m Just a Girl Money Money Money I Laughed. (New Hackers Prize) MEOW~ <div