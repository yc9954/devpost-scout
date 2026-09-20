---
slug: "stream-gift"
url: "https://devpost.com/software/stream-gift"
title: "vodsaver by stream.gift Team"
hackathon: "Theta Network 2024 Hackathon"
organization: "Theta Labs"
winner: true
words: 626
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# vodsaver by stream.gift Team

> Permanently save VODs / past live-streams from major streaming platforms via Twitch

[Devpost](https://devpost.com/software/stream-gift) · hackathon [[Theta Network 2024 Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]] [[web_dom]]

**stack** bash, ethersjs, express.js, javascript, nextjs, particle-network, react, thetajs, yt-dlp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- instructions
- challenges we ran into
- accomplishments we’re proud of

## Body

Market opportunity Diagram of how a VOD is processed (Also available on pitch deck) EDIT: We've moved all of our integrations for Theta Edge Cloud to vodsaver.com , which is a standalone tool to download VODs from Twitch & Kick. Inspiration Many streaming platforms & vast majority of streamers participate accepting donations & fundraising initiatives to support their creators. In 2023 alone, Twitch streamers raised over $400 million in crowdfunding efforts . However, many of these payment methods go through third party intermediaries, and as a result deal with transaction disputes, high fees from chargebacks, fraudulent donations, transaction delays, and many other issues with traditional financial payments. Furthermore, past/recorded live-streams are limited by current storage solutions on streaming platforms. Twitch only offers to save your VOD for 7 days (you can pay a monthly subscription to extend it to 30 days) before deleting permanently. What it does Introducing stream.gift , a streaming service that allows streamers on platforms like Twitch & Kick to crowdfund and receive donations via cryptocurrency & TFUEL. Viewers can donate to their favorite streamers in crypto and have their donation be read on stream. In addition, with integration via Theta Edge Cloud , stream.gift features vod-saver , a permanent storage solution for streamers past livestreams & VODs, and ease of access for saving one - just paste your temporary video URL and start uploading to the Cloud immediately. In our video demonstration, we demonstrate the use-case of both features/products, and the UX of navigating stream.gift as a streamer. How we built it stream.gift is built with TypeScript, Next.js 14 (frontend), and Express (Backend). For sending tips/donations, it’s a simple sendTransaction method via ethers to send TFUEL. Upon sending, we have an event listener on the backend, which listens for incoming transactions, which is triggered upon receiving. We also check whether the sending address owns a Theta Name Service, which will be read on-stream instead of the address if found. Streamers can login to Twitch via Particle Network. For vod-saver , we leverage Theta Edge Cloud and the provided video services API . We also utilize yt-dlp tool to retrieve direct video links from streaming platforms and transcode them to be available for Theta Edge Cloud. We have a 24-core dedicated server currently for encoding & compressing these videos, however we have been experimenting with NVENC encoding & compression (GPU based) in anticipation of the rendering services soon to be released by Theta Edge Cloud. Instructions See our video demonstration here . Written instructions are provided in the description as well. Challenges we ran into Finding a balance between the user/streamer experience and the developer he VODs was a challenge. We consulted with multiple engineers about the services to be integrated. We first considered downloading the VOD via yt-dlp, then uploading to an S3 bucket to be transcoded via URL to Theta Edge Cloud. We realized this was an extra step, so we decided to make the video URL path upon downloading resolvable on our server locally, so we can send this link from our end to Theta Edge Cloud to transcode. We had some challenges integrating Thetaboard’s Theta Name Service into our donation service, however we consulted with their discord team and we have integrated Theta Name Service into donations. Accomplishments we’re proud of Started building streaming solutions in May 2024 Won award @ Sui Overflow for a different streaming product We created & started development of vodsaver Created a full concept implementation for Theta Network for stream.gift Created a video-on-demand solution for streaming platforms via Theta Edge Cloud (Compatible with Twitch, Kick) Address & target a huge market with our product, and a continued step towards on-chain tooling for streamers. stream.gift GitHub stream.gift Full YouTube Demo Resources may be updated <div