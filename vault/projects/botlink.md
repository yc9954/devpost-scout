---
slug: "botlink"
url: "https://devpost.com/software/botlink"
title: "BoTLINK"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 1291
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# BoTLINK

> BoTLINK is a platform that NFTizes offline assets and connects blockchains with the Internet of Things, powered by Polygon, Solana and Chainlink

[Devpost](https://devpost.com/software/botlink) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[supply_logistics]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** express.js, helium, ipfs/filecoin, lorawan, micropython, nft.storage, node.js, polygon, pycom, react, rust, solana

## How they structured the write-up

- welcome to botlink, the blockchain of things powered by chainlink.
- introduction and problem statement
- our solution
- at a glance
- how it's built
- what's next for botlink

## Body

Diagram Landing page Navigation through the BoTLINK webpage FYU of BoTLINK NFT of an offline asset Real IoT device used! Check our video for the live demo! Welcome to BoTLINK, The Blockchain of Things powered by Chainlink. BoTLINK is a platform that NFTizes offline assets and connects blockchains with the Internet of Things. Live: https://botlink.site/ Introduction and Problem Statement IoT comes with several use cases in different sectors, however, its wider application is caught sometimes behind security concerns over data storage or on the device itself. Will combining it with blockchain be the answer to all its woes? Our answer is yes, as the projects trying to tackle these problems surely reflect. But they all come with their set of drawbacks that must be tackled along the way. Blockchain can Bring to the table Decentralization of data, added Security, which is perhaps one of the greatest woes of IoT. Transparency: as anyone would be able to check the blockchain at any time. Autonomy, as the Blockchain reinforces machine to machine economies through a token. And reduced costs as there are already great projects around with huge infrastructure. Because the global M2M economy is projected to have annual revenues of at least $1.5 trillion by 2030, solving these automation problems is of major social importance. NFTs provide provable control over any type of digital asset, including the “digital twins” of any object or process in the physical world, including IoT tracked assets. Because cryptography makes the reliability of blockchains provable, NFT holders can be confident that their ownership of the underlying non-fungible asset is secure. Further, smart contracts enable an NFT seller to place conditions on a token-holder’s rights such as in supply chain as our demo provides. Not only that it can be expanded to almost any industry available as almost every single one of them makes use of a warehouse and has to track parts and shipments to be made, and all of that can be tokenized. Warehousing is a very large expense for a manufacturing company, and inaccurate inventory can have a big impact on profitability. Conventional databases are well-known for user-entry errors, but inventory recorded as a blockchain entry can only exist in one place, and its digital identity moves with the physical item. Databases frequently have a single point of failure—like reliance on one vendor or one cloud provider—and a single unexpected event can cause a cascade of supply chain disruptions. Our Solution NFTizing offline assets and joining IoT with Blockchain, but without the downside. Namely the Solana blockchain with its speed and ease of development and the huge infrastructure of the Helium Network with its more than one hundred and eighty thousand LoRa Hotspots around the world. In addition to that we are incorporating Polygon as it is a better alternative to mint and host NFT while at the same time combining it with IPFS/Filecoin for the data storage, retrieval and management of smart contracts. Of course we need to secure this assets with verifyable randomness, so we will be using the Chainlink VRF for that. Importance of VFR according to Chainlink's documentation: "Chainlink VRF is a Verifiable Random Function that provides smart contracts and NFTs with a secure source of randomness backed by a cryptographic proof. The cryptographic proof serves as an audit trail proving the RNG operated in a tamper-proof manner. The cryptographic proof is then validated on-chain before delivering the random number to the consuming NFT contract, helping guarantee only truly random values are consumed. The strong security properties of Chainlink VRF help ensure neither the oracle, users, or developers can manipulate or predict the random number generated, resulting in NFTs that are assigned provably rare attributes and NFT collections distributed in a verifiably fair and unbiased manner." With this we aim to provide several services to businesses and enterprises such as provenance and asset tracking in a new, effectively secure way. At a glance This is the landing page of our NFT "marketplace", imagine it as a platform such as SAP where you would manage your fleet of offline assets, tracking, sensor data and so forth. In the device section after going through Metamask you'll get a look at your fleet of devices, from which you can choose to assigned to an NFTized asset to track it along a certain path that can be predetermined through a smart contract (in which the release can also be automated). Here you can see how an NFTized asset looks at a glance in the webpage, you can also see the IoT data feed, the Solana link where that data is uploaded to and also the Polygon scan of said NFT with its information and metadata. For more on the MVP you can check our main video to further our insight on the development of this project and to see IoT devices in real time action! How it's built Each of the IoT devices are connected to the Helium Network. They send the information through LoRaWAN to the network, once it gets there it is sent directly to our integration (an API) which works as a WebHook, this request reaches our NodeJS Express server. It then processes each of the hook calls and sends them to the solana blockchain through the Solana CLI, which is installed and configured on the server to communicate with the devnet directly. System's Architecture: All communication with the server and the website is done through API Management to facilitate scalability when server requests become larger. Services used: Chainlink VRF, to add Verifiable Randomness to NFTs, quite important when managing IoT devices. https://chain.link/education/nfts Helium Network - LoraWAN Main Service. https://www.helium.com/ Solana Cli - Interaction with Solana to catch IoT datafeeds and record them in the blockchain. https://docs.solana.com/cli Polygon - To mint NFTs via smart contracts and the main backend and have EVM compatibility. https://polygon.technology/ Alchemy - All smart contract information such as metadata and some variables are managed through Alchemy. https://www.alchemy.com/layer2/polygon Moralis - We Respek da pump so a lot of our front end uses Moralis' APIs. - https://moralis.io/ Much More Documentation and Codebase at: https://github.com/EddOliver/BoTLINK What's next for BoTLINK The project is still in its early stages, we perhaps went a little bit too far with the number of blockchain that we are employing, but every single one is doing in this project what it does best. Solana for cheap and fast transactions for the Helium IoT data feed, Polygon for lowering the cost of minting NFTs, Filecoin/IPFS for NFT and data storage and retrieval and Chainlink supporting Verifiable Randomness for those NFTs. We know that the it has quite a lot of points of failure because of this and we plan to keep on Developing to reduce them. Despite saying that we think we have THE bridge between Solana and Helium, regarding IoT. The impact regarding the Solana ecosystem is huge, as it merges the ideals of a Nasdaq-speed blockchain architecture with the enourmous infrastructure that the Helium Network has with its more that 230,000 Longfi hotspots around the world and solves the woes that IoT normally has without a blockchain implementation. Lastly I would like to say that NFTizing is a gamechanger for IoT. Because the global M2M economy is projected to have annual revenues of at least $1.5 trillion by 2030, solving these automation problems is of major social importance. Blockchains using smart contracts give real-time visibility and the opportunity to intervene earlier into operations gone astray. Blockchains also increase resiliency and lower costs because smart contracts are structured, auditable documents that can take the place of expensive trusted intermediators and enforcement costs. As the Metaverse progresses we will start NFTizing EVERYTHING and this project is a good starting point in our opinion. Hopefully you like it! <div