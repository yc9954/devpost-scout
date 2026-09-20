---
slug: "blockify-x2owt7"
url: "https://devpost.com/software/blockify-x2owt7"
title: "Blockify"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 759
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Blockify

> Empowering Artists with Blockchain: Seamless Royalty Payments and Ownership Control Through Spotify Integration.

[Devpost](https://devpost.com/software/blockify-x2owt7) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]]

**stack** blockchain, move, node.js, react.js, spotify, sui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blockify

## Body

Inspiration The project was inspired by looking at the challenges that artists face when dealing with traditional record labels and distributors. Artists often have to give up ownership of their music, lose creative control, and receive only a small fraction of the revenue generated from streams. Record labels and intermediaries take the bulk of the earnings, leaving the artists with limited financial security. Being a music producer and a DJ myself, I really wanted to make a product with potential to shake up this entire industry for the better. The music artists spend a lot of time creating high quality music and they deserve to be paid for it much more than they are right now. What it does Blockify lets artists harness the power of smart contracts by attaching them to their music while uploading it and automating the process of royalty payments which is currently a very time consuming process. Our primary goal is to remove the record labels and distributors from the industry since they they take a majority of the revenue which the artists generate from their streams for the hard work which they do. By using a decentralized network to manage royalties and payments, there won't be any disputes regarding missed or delayed payments, and artists will have a clear understanding of how much money they are making from their streams since they will be dealing with the streaming services directly. This would allow artists to have full ownership over their work and receive a fair compensation from streams which is currently far from the reality. How we built it BlockChain: We used the Sui blockchain for its scalability and low transaction costs. Smart contracts were written in Move, the programming language of Sui, to automate royalty distribution. Spotify API: We integrated Spotify's API to track streams in real time and trigger royalty payments. Wallet Integration: Sui wallets were integrated to enable direct payments to artists, with real-time updates on royalties as songs are streamed. Frontend: A user-friendly web interface was built using React to allow artists to connect their wallets, and track their earnings. The frontend interacts with the smart contracts via the Sui SDK. Challenges we ran into The most difficult challenge we faced was the Smart Contract Development using the Move language. Unlike commonly known language like Ethereum, Move is relatively new and specifically designed to handle asset management. Another challenge was trying to connect the smart wallets in the application and transferring money to the artist whenever a song was streamed, but thankfully the mentors from the Sui team were really helpful and guided us in the right path. Accomplishments that we're proud of This was our first time working with blockchain, and me and my teammate were really proud of what we were able to achieve over the two days. We worked on creating smart contracts and even though getting started was the hardest part but we were able to complete it and learnt some great stuff along the way. My teammate had previously worked with React but I had zero experience with JavaScript, since I mostly work with other languages, but we did the entire project in Node and React and I was able to learn a lot of the concepts in such a less time which I am very proud of myself for. What we learned We learned a lot about Blockchain technology and how can we use it to apply it to the real-world problems. One of the most significant lessons we learned was how smart contracts can be used to automate complex processes like royalty payments. We saw how blockchain provides an immutable and auditable record of every transaction, ensuring that every stream, payment, and contract interaction is permanently recorded and visible to all parties involved. Learning more and more about this technology everyday just makes me realize how much potential it holds and is certainly one aspect of technology which would rule the future. It is already being used in so many aspects of life and we are still discovering the surface. What's next for Blockify We plan to add more features, such as NFTs for exclusive content or fan engagement, allowing artists to create new revenue streams beyond streaming. There have been some real-life examples of artists selling NFT's to their fans and earning millions from it, so we would like to tap into that industry as well. Our next step would be to collaborate with other streaming services like Apple Music and eliminate record labels to the best of our abilities. <div