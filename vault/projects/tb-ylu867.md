---
slug: "tb-ylu867"
url: "https://devpost.com/software/tb-ylu867"
title: "TuBoleto - Pay public transit IRL with NEAR & Aurora"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 1042
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/developer"
  - "substrate/financial_record"
---

# TuBoleto - Pay public transit IRL with NEAR & Aurora

> 80% of people in Latam commute in public transit on a daily basis, making it great for crypto adoption. Minimal fees are key for micropayments. For us DeFi can make public transit free altogether.

[Devpost](https://devpost.com/software/tb-ylu867) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** android, android-activity-recognition, android-location, android-webview, dart, ethers.js, firebase, firebase-analytics, firebase-auth, firebase-crashlytics, firebase-functions, firebase-hosting, firebase-remote-config, firebase-storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tuboleto - pay public transit irl with near & aurora

## Body

Inspiration We believe that the best way to push web3 and DeFi is to embed into people’s habits and pain points to completely change their IRL traditional economy experience and turn those pain points into opportunities. We dreamed of making Lima commuters be able to see when the next bus was coming. We now show more than 1K buses GPS real time data. We dreamed of people paying for public transportation with their phones, banks met with us and then tried to do it on their own, we now make it possible in 500 buses. We now want to make public transportation free and believe this will drive all of the above. That is our goal. What it does This first step is just allowing the use of crypto as a means of payment for public transit. How we built it We knew that user experience was going to be key in order to drive user adoption between commuters so we started thinking about the simplest and most seamless way for our users to add money to their TuBoleto balance and pay for their bus ride. And also, all of this had to be done without changing the current fare model (which is distance based) and without significant infrastructure investment so the bus companies here in Lima would be on board. We needed to identify the specific bus vehicle the user is using without deploying complex in-bus devices and without requiring the user to own the latest high-end smartphone. So we used in-bus QR codes. For the distance based fare model we decided to use the user’s GPS, other sensors and machine learning to identify where the user got on the bus and where he got off. This would reduce user input and so achieve an easier experience as the only things required to ride the bus was to have enough balance and read the QR code. For the part of adding balance we needed to be compatible with the non-crypto wallets that already have widespread use here in Lima but also start with our plan of driving crypto adoption in order to later be able to grow an economy sustainable enough to make public transport free. We believe tapping into the NEAR ecosystem is a fantastic fit. On top of having almost non-existent transaction fees -key for micropayments- we haven’t been able to find a more friendly wallet than the NEAR wallet, it has an easy onboarding for new-to-crypto users as it allows them to skip the step of storing/backing-up a passphrase and uses an email instead. We believe it is brilliant and we know our users value it. We also love the fact that it has Aurora built on top which gives the opportunity to tap into the growing EVM developer ecosystem. In the technical part we knew our target market device of preference was android and we also had a lot of experience building for it (we build TuRuta, now +500K registered users, after all) but we didn’t want to rule out the possibility of expanding to IOS in the mid-term and try to reduce the effort on that part. We did our fair amount of research on hybrid frameworks and built some prototypes before using flutter. So we decided to use flutter for building the UI. Challenges we ran into The main challenge we ran into was the fact (we came to realize) that many android device manufacturers don’t closely follow the official android APIs and OS processes policies. This caused TuBoleto to behave differently on many devices, having issues ranging from sensor information (GPS) and activity recognition APIs being very inaccurate to our app being suddenly killed by the OS. We had to add some manufacturer-specific patches that helped in many cases. We also had to increase the user input in situations where we require it & on the devices we need to. We are continuously improving in this area. Accomplishments that we're proud of Around 500 buses are already connected, we have made a partnership with a bus dealership in Peru and we are going to be doubling our bus number in the next month and a half. We are also proud of organically appearing on the news and having banks and other financial institutions now being the ones calling us now. What we learned We learnt a lot of things: Automatic detection of where the user got off the bus is not going to be perfect from day one but with some fine tuning it can be good enough with some manual user input and some random inspections (from our human personnel) to detect and prevent cheating. This is closely monitored and the model is getting better and better. Based on talking to our users we have learnt that needing to memorize the 12 words to prevent losing their funds is a big ask, and many times a no-go, as they are used to passwords. This is why we believe the NEAR Wallet can be expected to thrive in new-to-crypto user bases like ours. Many of our users are open and enthusiastic about DeFi and Web3 although it’s important to know that when we interview them about it we don’t necessarily refer to it as Web3 but at the functionalities. We focus on understanding their current problems and needs. We then validate with them if the effort required from them is feasible for them and we validate that the solutions we propose actually solve their problems. This gives us many lessons. What's next for TuBoleto - Pay public transit IRL with NEAR & Aurora Our next steps with regards to the use of this means of payment are basically defining whether or not we would use NEAR/aETH, a stable coin (like nUSDO or aUSDO) to reward users. Evaluate if we shall generate another token in which case we have to define the tokenomics, specially ways to earn the token (like rewarding good user behavior, that is users who keep their sensors on and so provide useful information to the community) and promote its usage and create real sustainable value. Anyhow we have tests in place and many stealth experiments with regards to this and we are in continuous conversations with our public transit users. <div