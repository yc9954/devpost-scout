---
slug: "identifi-46wsv8"
url: "https://devpost.com/software/identifi-46wsv8"
title: "identiFi"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 710
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# identiFi

> Your Digital Identity Reinvented. Create Once, Identify Everywhere

[Devpost](https://devpost.com/software/identifi-46wsv8) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** chainlink, ethers, ipfs, polygon, solidity, tailwindcss, typescript

## How they structured the write-up

- inspiration 💡
- what it does ⚙️
- how we built it 🛠️
- configuration
- smart contract overview
- storing images on ipfs
- challenges we ran into 🚧
- accomplishments that we're proud of 🏆
- what we learned 📚
- what's next for identifi 🚀

## Body

landing page Example of Polygon Cardona Contract that represents a uploading files and documents Snippet of code using Chainlink VRF Inspiration 💡 The current digital identity landscape is often fragmented and insecure, making it challenging for users to manage and verify their identities across different platforms. identiFi was inspired by the potential of blockchain technology to create a unified, secure, and verifiable digital identity solution that empowers users to manage their identities seamlessly. What it Does ⚙️ identiFi introduces a revolutionary approach to digital identity management by leveraging blockchain technology to ensure privacy, security, and authenticity: Decentralized Identifiers (DIDs): Create and manage unique DIDs on the blockchain. Identity Verification: Submit identity documents for verification by trusted third parties. User Profile Management: Update personal details and manage credentials easily. Cross-Platform Support: Access and use the app across different devices and platforms. Security Measures: Strong security measures including encryption and secure key management. Social Media Integration: Share your verified digital identity on various social media platforms. Profile Editing: Easily update and manage your digital identity profile. How We Built It 🛠️ identiFi is developed using the latest in blockchain and decentralized storage technology: Blockchain Backend: Developed using Solidity, smart contracts on Ethereum provide a secure and decentralized backend for identity management. Chainlink VRF: Used to generate unique DIDs for users. IPFS: All user images are stored on IPFS to ensure decentralized and secure storage. Monobean: Utilized for batch transactions, ensuring efficient and cost-effective operations. Polygon Cardona Testnet: The application was deployed to polygon cardona Testnet Prerequisite Nodejs Installed Git Installed npm Installed Hardhat Installed Metamask (or any other Ethereum wallet) Chainlink VRF setup (with LINK tokens) IPFS setup Configuration To deploy to a test or main network, update the configurations located in hardhat.config.js to use a private key and, optionally, deploy to a private RPC like Infura. require('@nomiclabs/hardhat-waffle'); const privateKey = 'xx'; const projectId = 'xx'; module.exports = { "zkEVMCardonaTestnet": { url: 'https://polygon-zkevm-cardona.blockpi.network/v1/rpc/public', accounts: [privateKey], }, }, solidity: { version: '0.8.4', settings: { optimizer: { enabled: true, runs: 200, }, }, }, }; Smart Contract Overview The main contract, IdentiFi , manages user profiles, DIDs, and credentials. Key Functions createUser: Creates a new user profile and requests a new DID using Chainlink VRF. editUser: Edits an existing user profile. getUserByUsername: Retrieves user information by username. getUserByAddress: Retrieves user information by address. addJob: Adds a job to the user's profile. getJobs: Retrieves jobs associated with a user. setVisibility: Sets visibility preferences for user profile information. getVisibility: Gets visibility preferences for user profile information. batchCreateUsers: Batch creates multiple user profiles using Monobean. Storing Images on IPFS User images are uploaded and stored on IPFS. This ensures that images are stored in a decentralized manner, enhancing security and accessibility. Challenges We Ran Into 🚧 Blockchain Integration: Integrating with Ethereum and ensuring seamless smart contract functionality was complex and required extensive debugging. Chainlink VRF: Implementing and managing Chainlink VRF for generating unique DIDs was challenging due to the need for precise configuration and handling of LINK tokens. IPFS Storage: Ensuring that user images were securely uploaded and accessible via IPFS presented several challenges related to decentralized storage. User Experience: Creating an intuitive and user-friendly interface for managing digital identities while maintaining strong security measures was a balancing act. Accomplishments That We're Proud Of 🏆 Successfully deployed smart contracts on Ethereum and integrated Chainlink VRF for unique DID generation. Implemented secure and decentralized storage of user images on IPFS. Developed a robust and user-friendly interface for managing digital identities. Overcame significant technical challenges related to blockchain integration and decentralized storage. What We Learned 📚 Gained in-depth knowledge of blockchain technology and its applications in digital identity management. Learned to integrate Chainlink VRF for generating unique identifiers. Enhanced our understanding of decentralized storage solutions like IPFS. Improved our skills in smart contract development and deployment on Ethereum. What's Next for identiFi 🚀 Mainnet Deployment: Deploy identiFi on the Ethereum mainnet for broader adoption. Enhanced Features: Add more features such as multi-factor authentication and biometric verification. Partnerships: Collaborate with organizations and platforms to expand the ecosystem of verifiable credentials. Scalability: Improve the scalability and performance of the platform to handle a larger user base. User Feedback: Continuously gather user feedback to refine and enhance the platform. cardona-zkevm.polygonscan: https://cardona-zkevm.polygonscan.com/address/0xc791B6446F02fDCA0CBaa075BD3d513624D2c2F8 <div