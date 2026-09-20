---
slug: "dcloud"
url: "https://devpost.com/software/dcloud"
title: "dCloud"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 1085
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/legal_justice"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# dCloud

> Are you tired of online data leaks and big companies owning your data? At dCloud we provide cloud storage without compromising your ID & preferences while keeping our services fully decentralized.

[Devpost](https://devpost.com/software/dcloud) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**domain** [[legal_justice]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[video_visual]]

**stack** android-studio, cmake, golang, javascript, react-native, visual-studio, xcode

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dcloud

## Body

macOS Wallet Screen macOS Swap function TestFlight install dWeb Screen (BTFS Dashboard) dCloud Settings Inspiration Since the arrival of Web 2.0, the concentration of computational power in the hands of a few entities has been evident, this mostly as a result of centralized servers convenience and ease of use. Decentralized systems and P2P had an important lag of adoption mainly due to the lack of economic incentives for the software industry. The arrival of Block-chain technology removes confidence in a P2P network from the equation and in turn offer incentives to participants who act honestly within it. Although projects such as IPFS / Filecoin offer decentralized storage while preserving the user's privacy still depend on high-performance centralized servers as access points (gateways) and network nodes, going back to the paradigm of depending on a few High performance Nodes (owned by a few big names in the industry) to maintain it. dCloud’s mission is to bring Full and self-contained mobile/desktop BTFS network nodes focusing on providing the versatility and ease of use of a centralized cloud storage app and at the same time providing security, privacy and storage persistence through a decentralized economy comprised of interconnected BTFS hosts and renter nodes using BTT as a medium of exchange. What it does dCloud serves different use cases, some are already available and some are future developments: Cloud storage backup (Available) Long term files backup like family photos, important files, etc. Temporary big files sharing (Available) Files which are not possible to share on popular apps like email, whatsapp, telegram, etc Mobile auto-backup file system (similar to iCloud - Currently not available) Low IT budget companies storage solution. (Currently not available) dWeb creator & browser (similar to IPFS hosted sites - Currently not available ) ## How we built it dCloud idea was born back in 2020 from community feedback on BitTorrent telegram chat, after the BTFS v1 main net release we all wanted to have decentralized dropbox-like mobile app in which you can easily backup your data without giving away your freedom, privacy and big bags of money. When BTFS v1 airdrops began some advanced users from the TRON SRs and Devs discord channel took the lead and started to create host nodes on servers, laptops and even Raspberry Pis (which, based on experience end up being the hosts favorite setup) . We all shared ideas on how to make nodes more energy efficient and improve the overall node stability to get more contracts and thus more $BTT. More and more people were interested on having their own nodes to enjoy the airdrops coming from BitTorrent team, thus, users with high cost servers started to get burn due to a higher competition with smaller and more energy efficient nodes. A clear path was paved favoring small nodes over big servers. Fairness and decentralization is possible with BTFS. October 2020. BTFS was compiled and executed for the first time on a physical Android device using Termux terminal emulator, this gave us the confidence on the portability capabilities of BTFS and the architecture proposal of dCloud was born: OS Bootstrap → dCloud devs (Built separately per OS) BTFS binaries → BitTorrent React Native (GUI) → dCloud devs (Android + iOS shared code) By separating dCloud code like this we’ll be able to reduce the developing effort. BitTorrent team delivers the binaries, dCloud team devs focuses on implementing them to the specific OS environment and code a single Graphical Interface for both major mobile platforms: Android and iOS. Mid 2021. Android OS bootstrap is completed and basic GUI is developed for BTFS v1, however we faced major roadblocks to make the app available on Google Play due to Peer to Peer code restrictions by Google Play policies, so the development switches the effort towards improving the app instead of complying with Google Play. Feb 2022: After thousands of code lines and tons of passion dCloud is a reality (not perfect yet but working towards it). We have released a BTFS v2 compatible app and proudly can say it is now in a proof of concept stage. Basic UI functions for Android are implemented as well as out-of-the-box FULL BTFS v2 node features. dCloud Github repo has been released as Free & Open Source since May 2021 and will continue like this forever. We believe that keeping a FOSS will boost dCloud development in the future and will encourage further ramifications and use cases for both BTFS and dCloud. Being a FOSS project does not imply it won’t have a revenue stream, it just means anyone can collaborate to improve it or to build on top of it. May - October 2022: Even tough we have been building on a lower profile several updates were introduced in dCloud, including but not limited to: Code homologation between iOS & Android (Removal of third party dependencies in Android version) UI improvements Upload feature in App included Storage duration modification option Added support for BTFS 2.2.1 BTFS shared library updated to BTFS 2.2.1 plus compiling options optimized for size reduction Challenges we ran into Prepare the go-btfs code for mobile: Compiling and configuring a project in Xcode and Android Studio to use the btfs shared libraries became the hardest thing due to the almost non existent documentation online. Up to date applying to official App Stores has been also a hard topic due to the legal documentation needed by Apple to deploy (Crypto projects need extra legal requirements and we are still in the process of getting it). For Android the limitation resides in peer to peer communication code restrictions. We found a way to workaround this by modifying the go-btfs p2p calls. Accomplishments that we're proud of Winning the Web3 community votes during the first TRON hackathon as well as 1st prize from judges. Having several stars and forks in our Gihub repository The project has received several recognitions by the TRON/BTT community in our social media. This gives us the motivation to keep working on improving the app :) What we learned Mobile releases are OK, however we need to increase our reach to touch as much audience as possible User experience is important We need to improve our ramp-up and know-how for users willing to use dCloud and BTFS in general. What's next for dCloud Renter user Experience (GUI) -> 2022 | Hackathon S3 Android version simplicity improved -> 2022 | Hackathon S3 Google Play Introduction -> 2022 | Hackathon S3 macOS and Windows release -> 2022 | Hackathon S3 <div