---
slug: "web3wheels"
url: "https://devpost.com/software/web3wheels"
title: "Web3Wheels"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1273
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/transportation"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Web3Wheels

> A decentralized autonomous Uber service using blockchain and AI. Mint, own, and trade car NFTs. Real-time data and smart contracts ensure transparency, efficiency, and seamless use.

[Devpost](https://devpost.com/software/web3wheels) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[finance_payments]] [[transportation]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** chainlink, ether, express.js, fastapi, gymnasium, hardhat, leaflet.js, nextjs, node.js, openzeppelin, python, rainbowkit, react, shadcn

## How they structured the write-up

- what inspired us
- what it does
- how we built it
- challenges we faced
- accomplishments that we're proud of
- what we learned
- what's next for web3wheels
- chainlink usage

## Body

Logo Components On-chain and Off-chain components Data Flow Smart contracts Use case diagram GIF Visual of partially trained coordinator and taxi agents. blue-taxis, green-passengers, red-picked up passengers, Area: Manhattan, NYC GIF Visual of partially trained coordinator and taxi agents. blue-taxis, green-passengers, red-picked up passengers GIF Visual of partially trained coordinator and taxi agents. blue-taxis, green-passengers, red-picked up passengers GIF Visual of partially trained coordinator and taxi agents. blue-taxis, green-passengers, red-picked up passengers GIF Visual of partially trained coordinator and taxi agents. blue-taxis, green-passengers, red-picked up passengers GIF Visual of partially trained coordinator and taxi agents. blue-taxis, green-passengers, red-picked up passengers Command line output of Taxi behavior during training Training summary What Inspired Us We have been inspired by the challenges faced in the current transportation landscape, where centralized platforms often lead to monopolization, maximum price threshold, and a lack of transparency. Our vision has been to develop a solution that democratizes vehicle ownership and management, offering a fairer, more inclusive model that leverages the latest advancements in blockchain and AI technologies. We aim to ensure that as the autonomous vehicle industry emerges, it does not remain dominated by centralized platforms. Instead, we seek to open up the space for every individual, fostering a more equitable and competitive environment. What it does User Categories & Vision Car Shop : Role : The car shop is responsible for minting cars and making them available for purchase. In future iterations, these real-world car shops will be verified by Chainlink oracles using institutional online data, ensuring a trusted environment. Function : Car shops mint cars with 0km, ensuring lifetime tracking from the start. Car Owner : Role : Car owners purchase cars from the car shop using their Web3 wallet. They can buy full or fractional ownership of a car. Function : After purchasing a car, the owner sets the autonomous car’s strategy, such as maximizing revenue by picking up customers. The car operates autonomously, learning and optimizing its strategy over time based on real-time data and past experiences. Owners can track the car’s movements live on the app and view daily performance metrics like mileage, customer count, and revenue. Owners will be able to resell their cars to the car shop or other buyers, further promoting a dynamic market. Passenger : Role : Passengers use the app to call a car with a single click. They get matched with the nearest, fastest, or cheapest available car. Function : Payment is made directly from the passengers' Web3 wallets to the car owners' wallets, ensuring a smooth and transparent transaction process. What it currently does Minting Dynamic Car NFTs Chainlink implementations (data feeds, automation, anyAPI call) Buying and selling functions for car ownership Daily end-of-the-day update of dynamic car NFTs Frontend website with map integration Integration of the frontend and smart contracts (mint NFTs, car shop, dashboard etc.) Backend with AI API and AI model inference Reinforcement Learning with AI coordinator (made from deep neural network) All functions are implemented in the backend (creation of cars, public API) Future work to be done Fractional ownership of NFTs CCIP integration AI backend hosting on decentralized compute infrastructure Decentralized database/datastorage Customized taxi agent strategy setting Improve integration of the backend with the smart contract Autonomous integration of the payment between passenger and the car (proof of concept) AI training with larger dataset (weather, traffic conditions, fuel/power level) How We Built It The development of Web3Wheels involved several key components: Blockchain and Smart Contracts : Hector spearheaded the implementation of smart contracts for vehicle minting, ownership transfers, and transactions in the blockchain domain, guaranteeing secure and transparent processes. His contributions extended to the Chainlink implementation, ideation process, and documentation. AI and Route Planning : Dave integrated AI algorithms for real-time data analysis, optimizing route planning. The implementation is built using tensorflow in Python, taking advantage of reinforcement learning packages like stable_diffusion3. We created an environment of real city streets using Open Street Map, and generated Taxi and Passenger classes to populate the environment. The AI Coordinator provides coordination between Taxi's to pick up the right passenger by providing destination targets to each Taxi. The AI component uses a actor-critic model for deep reinforcement learning. Frontend Development : Mihir developed the user interface using NextJS, TailwindCSS, Shadcn, Wagmi, Viem and RainbowKit allowing users to interact with the blockchain backend and view simulations on Leaflet Open Street Map. And using the Dextools API for price conversion in the dashboard. This technology stack provides a modern, responsive, and user-friendly experience. AI, Backend, and AI API : Berkay initiated the project by setting up the AI repository and establishing reinforcement learning as the machine learning paradigm. He developed single agent training environments in Python using Gymnasium, converting maps into MultiDiGraphs with NetworkX for route finding and optimization. These environments were designed to explore and maximize agent rewards. After handing over the AI component to Dave, Berkay focused on developing the backend in Node.js. He created a simulation environment to organize vehicles and passengers and simulate vehicle movements. Additionally, Berkay implemented an AI API using FastAPI to connect the AI models with the backend, ensuring seamless integration and real-time updates. Team Organisation, Graphics and Video production : Mario composition of team with key skills to make the project happen. Setting up regular team meetings, agenda & workflow. Creation of branding, story telling, video production etc. Challenges We Faced Building a good reward function for RL-training Setting up a training environment for MARL ( Multiagent Reinforcement Learning) Compatibility of the compiler versions of the smart contracts Limited number of online resources on resolving issues about smart contracts Map integration and dynamic car, passenger markers on the map Loading time of map data from OpenStreetMap Api and converting it into MultiDiGraph Different time zones (Hector was barely awake during meetings ;)) Accomplishments that we're proud of Distribution of the responsibilities and the tasks / good work split Workflow and consistency in development and meetings Regular, organized documentation and meetings Team commitment Building a proof of concept in a short period for a complex idea/product What we learned Dave : Using stable_baselines3 for a reinforcement learning agent was a first for me. It took multiple iterations to get the environment defined correctly. It was a pleasure to get the Taxi agents to pick up passengers finally after hours of training on a personal GPU. Berkay : Learning JavaScript and Node.js has been crucial for my transition into the web3 space, and utilizing NetworkX for map graph conversion and route finding provided efficient and effective results. It was a pleasure to work on reinforcement learning again, which is my preferred machine learning paradigm. Hector : I delved into the Chainlink platform, expanded my knowledge of Solidity and Hardhat, explored the applications of Dynamic NFTs, and gained insights into emerging projects like Scroll, Celo, and others. This experience broadened my expertise in blockchain development and exposed me to innovative solutions and platforms within the blockchain ecosystem. Mihir : I learned to seamlessly integrating frontend and smart contract using wagmi hooks. Integrating leaflet map in the frontend with draggable markers. Optimizing the build using next js prerendering and partial rendering features. What's next for Web3Wheels While fully self-driving cars are not in the immediate future, we believe the concept of personal income-generating agents would be a game changer for general public ownership of AI revolution. Rather than speculating on NVIDIA stock, people can own and manage their own mini businesses that leverage the latest AI technology and use blockchains with Chainlink for decentralized and trust-minimized coordination. Chainlink usage Datafeed: PriceConverter.sol#L22 | DynamicNFTCar.sol#L150 Chainlink anyAPIcall: CarEodDataConsumer.sol#L54 Chainlink automation: Chainlink Upkeep | CarEodDataConsumer.sol#L47 <div