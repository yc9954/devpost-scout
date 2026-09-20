---
slug: "greengold"
url: "https://devpost.com/software/greengold"
title: "greengold"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 1070
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "user/small_business"
---

# greengold

> Greengold is an environmental and climate focused green-minded project built on the Celo blockchain.

[Devpost](https://devpost.com/software/greengold) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]] [[small_business]]

**stack** celo, solidty, web3

## How they structured the write-up

- challenge 🏆
- what is greengold? 💚💛
- inspiration 💡
- what it does ❓
- how does it work? ⚙
- how we built it 🔨
- challenges we ran into 💪
- accomplishments that we're proud of 😎
- what we learned 📘
- what's next for greengold ⏱

## Body

Challenge 🏆 🏆 Green Track on the Celo's Make Crypto Mobile Hackathon What is greengold? 💚💛 💎 Greengold is an environmental and climate focused green-minded project built on the Celo blockchain. Inspiration 💡 🌎 Pollution and global warming are really hot topics nowadays. The top leaders of countries make sessions to handle this situation. In this situation people think blockchain is equal to wasting resources, pollution and a big cause of global warming. That’s why we wanted to create a project that would help blockchain to turn a little greener. 🗜 We are freelancer deep learning developers with a strong interest in cutting edge technologies like blockchains and smart contracts. 🌿 Our vision is a world where people are eco-friendly and they use smart contract technology to reduce energy consumption and CO2 footprints to create a healthier and better environment. What it does ❓ 📐 Greengold helps to measure and calculate the energy consumption and the carbon footprint of different human activities from travelling by airplane, through training a deep learning model till commuting with a gasoline-powered or an electric car. ⏳ Users can start and stop a measurement anytime they want about any activity. A measurement based on time or the spent resources. For example they can measure the carbon footprint of commuting or to work with a computer for 6 hours. How does it work? ⚙ ⚙ As it was mentioned earlier, users can measure and calculate the energy consumption and the carbon footprint of their activities. Requirements: ✅ Celo wallet ✅ Users should know the power consumption of their own devices. However, we made an old-fashioned web2-based API service to provide some data. ✅ Furthermore, for the calculation the smart contract needs the proper ratio of energy production. We also provide this data on a country level. Steps: ⏰ Time-based measurement: 🟢 set up the device (name, energy consumption) 🟢 start a measurement 🟢 stop a measurement 🟢 get result 🔬 Consumption-based measurement: 🟢 set up the device (name, energy consumption) 🟢 set the consumed resources 🟢 get result Features already implemented: 🟩 constructor (string memory sentence) payable 🟩 function addParentDevice (string calldata message, string calldata name, uint8 status, uint8 consumptionType, uint defaultCPU) onlyAdmin(message) external 🟩 function getParentDeviceById (uint id) onlyExistingParentDevice(id) external view returns (ParentDevice memory) 🟩 function getParentDevices () external view returns (ParentDevice[] memory) 🟩 function changeParentDevice (string calldata message, uint id, string calldata name, uint8 status, uint8 consumptionType, uint defaultCPU) onlyAdmin(message) onlyExistingParentDevice(id) external 🟩 addUserDevice (string calldata customName, uint customCPU, uint parentDeviceId) onlyExistingParentDevice(parentDeviceId) external 🟩 function getUserDevices () external view returns (UserDevice[] memory) 🟩 function changeUserDevice (uint id, string calldata customName, uint customCPU, uint parentDeviceId) onlyExistingUserDevice(id) onlyExistingParentDevice(parentDeviceId) external 🟩 function startTimeMeasure (uint userDeviceId) onlyExistingUserDevice(userDeviceId) external 🟩 function getTimeMeasures () external view returns (TimeMeasure[] memory) 🟩 function stopTimeMeasure (uint measureId) onlyEnoughFee() onlyLivingTimeMeasure(measureId) external payable 🟩 function addUnitMeasure (uint unitCount, uint userDeviceId) onlyEnoughFee() onlyExistingUserDevice(userDeviceId) external payable 🟩 function getUnitMeasures () external view returns (UnitMeasure[] memory) 🟩 modifier onlyAdmin (string memory sentence) 🟩 modifier onlyEnoughFee () 🟩 modifier onlyExistingParentDevice (uint id) 🟩 modifier onlyExistingUserDevice (uint id) 🟩 modifier onlyLivingTimeMeasure (uint id) How we built it 🔨 🧱 There was more steps of the building process. First we figured out what to do and how to implement it. Because smart contracts and on-chain data storage are focused on efficiency we had to figure out how to manage and store data as optimized as possible. There we decided to use old world web services at the user endpoint of our solution. In the future it can get replaced with oracle services. We created the data structure of the project and we decided how to store the data in the smart contract. By building the Solidity code we implemented the classical CRUD data management process for each data type. The functions in the contract are organized by variables and tasks instead of being alphabetically organized. There are four key variables; the array of the predefined parent devices, mappings for time based measurements, for unit based measurements and for the devices added by the users. The key of the mappings is the address of the users. All key data containers are public. It can be changed in the future if needed but we want to show the transparency of our system. Challenges we ran into 💪 💪 Celo infrastructure is great, we didn’t have any challenges with it. On the other hand it was much more challenging to unify the old world web and web2 solutions with the future-proof web3 technology since static consumption data must be accessible to help the whole process. There are different ways to handle this requirement; the solution we implemented now is just one of the possible ways. It would need more time to examine the advantages and disadvantages more deeply. Since we plan to continue with greengold, we definitely would spend the needed time to make experiments. Accomplishments that we're proud of 😎 😎 deployed a smart contract: Celo Alfajores Test Network: 0x6F035e0e7de9e30a9Ae8C60142E2D0A1E49A9fd5 😎 created an API service to help users to reach necessary energy-related data for the measurement: https://hyperrixel.com/hackathon/greengold/ 😎 web based user interface: https://hyperrixel.com/hackathon/greengold/demo/ What we learned 📘 🧠 We learned a lot about Celo’s infrastructure and we learned a lot about carbon footprints of different activities. It is really hard to work on this topic since day by day we get to know new ways how humankind destroys the resources of our planet. What's next for greengold ⏱ 🚀 We want to turn our idea into a prosperous service. There are some community and general features that we definitely want to integrate into our solution. Blockchain and smart contract developers are a great community. We think the future should be built on communities. Fighting against pollution and making the world a better place need a lot of devotion. Building social-related projects like challenges between users turn hard tasks into fun. We show a way to save our environment but we are open to cooperate with other developers and communities to build better projects. During the hackathon we deployed a smart contract to make the first step on a long and green journey on the Celo blockchain. 🟩 storing results in NFT certificates 🟩 make energy reduction challenges between the users 🟩 establish a new discussion and movement within the blockchain community about the environmental impact of daily activities and how blockchains and smart contracts can help to make daily life more eco-friendly <div