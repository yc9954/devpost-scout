---
slug: "lockerism"
url: "https://devpost.com/software/lockerism"
title: "Lockerism"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 475
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# Lockerism

> Redefining Secure Data Analytics with Homomorphic Encryption and Blockchain Technology

[Devpost](https://devpost.com/software/lockerism) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[privacy_tech]] [[structural_withholding]]
**domain** [[developer_tools]]
**substrate** [[structured_db]]

**stack** fastapi, metamask, next.js, python, zksync

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lockerism

## Body

Inspiration We drew our main inspiration from the ongoing news and fears that users have surrounding their private information. This also boils back to our own team's personal fears as well about our data security and potential data leaks during computations. What it does Lockerism applies HE to the data passed to the model for recommended profiles output that have similar content to those the user has interacted with, making up the stimulated FYP. It also untilises zero knowledge proofs on blockchain to verify the usage of the content-based filtering model on the data at little cost. Lockerism uses a 2 pronged approach whereby HE is used for data privacy and the blockchain component is used to verify the model. How we built it Our main tech stack uses Next.js for the frontend and Flask with RESTFul APIs for the backend along with ML. We also used Metamask as our Web3 service provider with xkSync Era for the zero knowledge proofs. ** Development Tools VSCode (IDE): Used for writing and managing code. Postman (API Testing): Used for testing and verifying API endpoints. ** APIs Used Internal APIs: Developed within the project to handle video recommendations and health checks. **Assets Used TikTok User Profiles Dataset: Sourced from Kaggle https://www.kaggle.com/datasets/manishkumar7432698/tiktok-profiles-data?resource=download This dataset contains profiles of TikTok users used to train the recommendation model. ** Libraries Used ** Backend Libraries Flask: A lightweight WSGI web application framework in Python used for building the backend server. numpy: A fundamental package for scientific computing with Python, used for numerical operations. pandas: A data manipulation and analysis library for Python, used for handling and processing the dataset. scikit-learn: A machine learning library for Python, used for training the recommendation model. ** Frontend Libraries NextJS: A React framework for building server-side rendered and static web applications. MUI Components: A popular React UI framework that provides pre-designed components for building user interfaces. ethers: A library for interacting with the Ethereum blockchain and its ecosystem. web3: A JavaScript library for interacting with the Ethereum blockchain, used for integrating blockchain functionality. Challenges we ran into The main challenge that we had was integrating all the blockchain elements into our existing ML model and frontend in a seamless manner. Accomplishments that we're proud of Overall, we are proud to have built a project that aligns with our passion in blockchain and has a use case that we all feel is impactful as well. What we learned Our main takeaways would be to stick to our interests and passions because that would really be the fuel for our project and proved to be what made us stick out till the end. What's next for Lockerism One additional feature that we thought about having was to integrate differential privacy mechanisms to provide an additional layer of privacy. This would align strongly with our use case as well. <div