---
slug: "fantom-adventure-rpg"
url: "https://devpost.com/software/fantom-adventure-rpg"
title: "Fantom Adventure RPG"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 1351
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/labor_employment"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Fantom Adventure RPG

> An RPG game, reflecting how I (player) first get into the Fantom world, accompanied by a Fantom pet, raise and train them, and bring them along to adventure in the Fantom World!

[Devpost](https://devpost.com/software/fantom-adventure-rpg) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]] [[labor_employment]]
**user** [[developer]] [[legal_professional]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** amazon-web-services, ftmscan, github, photoshop, remix, solidity, unity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for fantom adventure rpg

## Body

Key Art for the game Game: https://www.fantomadventurerpg.xyz Collection: https://paintswap.finance/marketplace/fantom/collections/fantom-adventure-rpg---pet/nfts https://paintswap.finance/marketplace/fantom/collections/fantom-adventure-rpg---equipment/nfts Game vibe starto! Inspiration I'm a passionate gamer and indie game developer who is considering developing in Web3 recently. My friend then introduced me to the Fantom blockchain, highlighting its speed and cost-effectiveness. With the aim of harnessing Fantom's fast and cost-effective potential to the fullest extent, together with my expertise, I immediately decided to create a game that could fully operate on the blockchain itself. Next, I need to research the advantages of a blockchain game, why people need it, and most importantly, how to attract players. Ultimately, I aim to establish the following project mission: Immutable Game Mechanics that cannot be cheated and are fair to everyone. Security with no single point of failure, particularly addressing concerns about hackers compromising the server. Decentralized development involving the community, where the code is publicly available for anyone to build upon and expand. Attracting players with engaging gameplay and rewarding items as NFT collections, offering players true ownership of in-game assets. After conducting further experiments on the transaction speed, I discover that the transaction receipt return from the block takes around 3 seconds. This speed is deemed satisfactory for a non-real-time game, as typically animation or transitions are used to mask the delay in turn-based web2 games (which can be up to 3 seconds) to prevent players from experiencing lag. As a result, I have made the decision to develop a blockchain RPG game with animation graphics that will serve as a mask for transaction delays. (After confirming that no similar game utilizing this approach on the Fantom blockchain, making this project a unique and exciting addition to the ecosystem) What it does An RPG adventure game that will include an evolving main storyline to keep players engaged. Players will discover, train, and form a bond with their own Pets (ERC721 NFTs). They can then battle tomb guardians alongside their pets to earn equipment (ERC1155 NFTs) for the main characters. The core game loop: Requires a minimum of 1 transaction per day, with an average of 5 transactions. Involves exploring the Tomb and encountering random powerful Guardians that drop unique NFT equipment upon defeat. Strategy: Emphasizes low complexity but in-depth gameplay. Allows players to strategize their team composition based on pet weakness, skills, and character equipment to optimize equipment farming with minimal transactions. WARNING: To cater to the hackathon, the game balancing has been significantly tuned and sped up, taking into consideration that judges may have limited time and cannot spend hours or days playing and evaluating a game. How I built it I began by writing a Game Design Document (GDD) within a limited timeframe. The GDD serves as a standard guide for game development, from conceptualization to production. Next, I started to learn Solidity. With my coding skills, I found it relatively manageable to grasp. I relied on resources like https://cryptozombies.io/ , trial and error, and sought assistance from the Fantom community for more challenging code aspects. This included addressing the 24kB contract size limitation and preventing contract exploitation by other parties. Following that, I created Key Art and game assets using Adobe Photoshop, which were then integrated into Unity. As a Unity developer, this process proved to be relatively straightforward. Finally, the most time-consuming aspect was establishing the connection between smart contracts and the Unity game. Initially, I utilized web3.js, but due to time constraints, I ultimately transitioned to the ChainSafe SDK. Still, countless bugs are to be fixed, for 2 weeks! Somehow help ChainSafe to fix their bug… Was thinking to fall back to web3.js if there’s no time constraint. Throughout the development process, I actively sought feedback and engaged the community in voting for their preferred themes. It's worth mentioning that the key art itself was inspired by one of my followers, @AllThingsFantom. Challenges I ran into One significant challenge was the time constraint. Developing a game within 50+ days is a real challenge, especially considering my previous best record of 10 months. However, a prototype is possible, which means the submission will be a prototype/Open Alpha version. Another challenge I faced was the size limitation of the smart contract. This limitation posed difficulties in incorporating game logic. I had to find innovative ways to optimize for gas and contract size, which added multiple layers of complexity compared to a traditional web2 game. I vividly recall feeling overwhelmed and even posted a tweet on Twitter expressing that my mind was flooded with Public, Private, Internal, External, and more words. It felt like my brain was being reshaped to adapt to these new considerations. Additionally, the Chainlink SDK was not specifically tailored to accommodate complex blockchain game. It appeared to be designed primarily for games focused on minting and reading NFTs. As a result, I had to make modifications and encountered some bugs during the transition from V1 to V2 midway through my development process. Accomplishments that I'm proud of Mastered Solidity and gained proficiency in writing smart contracts. Successfully bridged the gap between web2 and web3 technologies. I acquired the knowledge and skills necessary to integrate these two worlds. Overcame and resolved the ChainSafe bug, increasing the stability and reliability of the game. Developed a playable prototype that aligns closely with my initial vision. It's incredibly fulfilling to see my imagination come to life in a functional and interactive form. Through active engagement and feedback, I fostered a supportive community of players and enthusiasts who share my passion for the game. They even offer me help at no charge. I really love the community and very much appreciate it. Conducted extensive playtesting and received positive feedback from the community (I can't sleep for a day due to the positive excitement), validating the gameplay mechanics and overall enjoyment factor of the prototype. Demonstrated resilience and adaptability in navigating the challenges of game development within a limited time frame, showcasing my ability to meet deadlines and deliver results. Lastly, I learned to use AWS services by myself! What I learned Nothing can stop my imagination and dedication! Fantom is truly a joy to work with—fast, affordable, and incredibly fun to explore! I'm grateful for the supportive and friendly Fantom community who never hesitate to lend a helping hand. Writing a smart contract wasn't as daunting as I initially thought. I gained a solid understanding of how blockchains function and delved into concepts like RPC and its purpose. Along the way, I fully embraced and absorbed myself in crypto terms like SAFU, HODL, and more. What's next for Fantom Adventure RPG For me, the prototype marks just the beginning, representing a mere 20% of the entire journey. The remaining 80% is dedicated to bringing this game to its complete and polished form, as I strive to realize my long-held dream of founding my own gaming studio. Winning the prize would not only validate the value of this project but also provide the means to turn my dream into a reality. I intend to reinvest the prize money to establish my studio and expand the team by hiring 2 additional developers (game artist + unity dev), allowing us to take the game to new heights! In the short term: My top priority is to continuously enhance the game's stability, addressing any existing bugs in the front end and bridging components. This will not only help uncover potential technical challenges but also leave a strong impression on the judges. I am eager to incorporate sounds and background music (BGM) into the game, aiming to have them implemented in time for the judge's review. Additionally, I have plans to elevate the quality of the story arts, ensuring they captivate players and further enhance their gaming experience. Looking ahead to the long term: The next phase involves transitioning into full-scale production, refining the game and bringing it to completion. Use web3.js for more stability. Need to create my own Unity library. Building a passionate and engaged FARPG community, fostering a strong connection with players. Explore monetization strategies to sustain the growth of my studio (if I have one). Thank you for your support! <div