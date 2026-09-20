---
slug: "sunshare-2fnis4"
url: "https://devpost.com/software/sunshare-2fnis4"
title: "sunshare"
hackathon: "TRON Grand Hackathon - HackaTRON Season 7"
organization: "TRON DAO"
winner: true
words: 868
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/financial_record"
---

# sunshare

> sunshare aims to provide individuals with a transparent and secure way to share files

[Devpost](https://devpost.com/software/sunshare-2fnis4) · hackathon [[TRON Grand Hackathon - HackaTRON Season 7]]

## Facets

**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[financial_record]]

**stack** amazon-web-services, btfs, bun, harthat, node.js, react, redis, remix, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sunshare

## Body

Homepage Upload page Create a Share form Download page Download page | Decryption key prompt Sunshare architecture Inspiration Sunshare draws inspiration from established file-sharing platforms while addressing their limitations. Like WeTransfer, it embraces a clean, user-friendly approach to file sharing with time-limited access. From MEGA, it takes the crucial principle of client-side encryption, ensuring true privacy for users' data. However, Sunshare goes further by combining these proven concepts with decentralized storage and transparent, blockchain-based pricing, creating a solution that prioritizes both user privacy and pricing clarity in ways its predecessors couldn't. What it does Sunshare offers a pragmatic approach to secure file sharing with transparent, user-friendly pricing. While traditional platforms often leave users uncertain about how their data is being used and analyzed, sunshare provides a clearer alternative. Built on BTFS decentralized storage and featuring client-side military-grade encryption, the platform ensures your files remain private and distributed. The straightforward pay-as-you-go model means you only pay for what you upload – smaller files cost less, putting you in control. All pricing calculations are handled through a public smart contract, making the whole process transparent and verifiable. This combination of technologies and fair pricing allows you to share files while maintaining control over both your data and costs, without the opacity of traditional centralized storage solutions. How we built it Sunshare's architecture is built on multiple layers that work together seamlessly to provide secure and decentralized file sharing. The user interface is crafted using React.js and Remix, creating a responsive and intuitive frontend experience that makes file sharing accessible to everyone. Behind this, a backend powered by Node.js and Bun handles the core application logic and file processing. Files are stored on a BTFS (BitTorrent File System) Node, leveraging decentralized storage to ensure data resilience and accessibility without relying on traditional centralized servers. The pricing and payment infrastructure is managed through a Solidity smart contract deployed on the BTTC blockchain and using the BTFS Price oracle, which transparently handles all transaction logic and cost calculations. Challenges we ran into I faced many challenges during the development of sunshare. The biggest one was learning and interacting with BTFS being totally new to the tool. I had to deep dive into the (not so well written) documentation to understand how the BTFS Network and BTFS Node were working. Furthermore, as I am building this project alone, I had to do everything from scratch. Some areas were under my domain of expertise (backend & frontend development), but others were not (BTFS & smart contract development); therefore, I had to push myself out of my comfort zone to deliver sunshare. Accomplishments that we're proud of I am proud that I managed to solve all the challenges mentioned above. On top of that, I am also proud of getting back to the habit of coding for fun and building projects on my own during my free time rather than coding solely for companies. What we learned On the technical side, I have learned more about how web3 projects work, especially all the interactions with smart contracts in a web3 application. Moreover, I now understand how decentralized file storage such as BTFS works under the hood and how to leverage such tools to make production projects. But, more important than learning new technical skills, I have learned about myself. I have learned that I can embrace the habit of coding for fun (or at least on my own projects) every day. I can have an idea and make it happen, all by myself. No matter what the outcome of this hackathon is, I leave it as a better entrepreneur. What's next for sunshare I have a lot of ideas for sunshare. Here's a draft roadmap I have if the project wins a prize: Make sunshare production ready : The server is currently just one instance and wouldn't be able to cope with a suddent spike of uploads. Resumable uploads : Currently, if an upload goes wrong because of a network outage, it will not be able to resume. The idea would be to store metadata about the upload progress on sunshare's servers to be able to resume them later. No Limit Uploads : Inspired by mega.nz, I would like to add no limit uploads. I am currently facing some limitations regarding the maximum size of uploaded files with the BTFS API used to store files chunk by chunk. Sunbytes voucher price refinement : I am planning to refine the voucher price calculator smart contract to show parameters used for share price computation more accurately. It implies adding much more parameters to the price computation than is currently implemented, such the sunshare's servers business, the number of recipients ... Cross browser download : Downloading on sunshare is currently not available on non-chromium browsers for technical limitations, but I want users to be able to download shares in whatever browser they use. Web2 Payment : As I would like to make sunshare mainstream, I feel that requiring a crypto wallet to pay for uploads will be a hurdle. A lot of people haven't been introduced to Web3 yet. The idea would be to allow users to pay for uploads through a web2 payment gateway such as Stripe. <div