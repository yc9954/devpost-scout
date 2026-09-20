---
slug: "buidlsmart"
url: "https://devpost.com/software/buidlsmart"
title: "BuidlSmart"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 973
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# BuidlSmart

> A no-code smart contract builder

[Devpost](https://devpost.com/software/buidlsmart) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[web_dom]]

**stack** hashpack, hedera, ipfs, next, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for buidlsmart

## Body

Inspiration As per May 2020 statistics, blockchain technology is still not mainstream in most industries. In fact, blockchain technology is least adopted in important sectors like healthcare and education. Taking healthcare as an example, 21% of the healthcare industry is still considering the use of blockchain yet there is no apparent plan for the same. The main reason for this is the lack of information and education on blockchain technology. If we look closely, the inception of programmable cryptocurrency came with Ethereum in 2015, almost 7 years ago, so it's fair to say that blockchain technology is still relatively new. As such things are constantly evolving in this domain and it is hard for developers to learn and use the technology effectively. In our endeavor to solve this problem and increase the accessibility of blockchain technology, we decided to create BuidlSmart . What it does BuidlSmart is simple and easy to get started with. First, you log into BuidlSmart with your Hashpack wallet and connect to the website. Once logged in, a user needs to create a new application. An application is simply put, a smart contract. After creating an application, a user can do multiple actions, like create an object or a function. An object is similar to a struct in solidity where each object has some fields associated with it. After creating an object, one can create a function in order use the created object, like mutating data to create objects or reading objects stored on the blockchain. All this can be accomplished from the user interface. Once a user has created the objects and functions they require, they can go ahead and compile the contracts and deploy it to the Hedera testnet directly from the website. No need to run tedious commands or software. If building and deploying your smart contracts wasn't enough, the user can even test the deployed contract directly from the website, without having to write a script or code for the same. This is extremely useful for people who have absolutely zero knowledge of programming. How we built it We used the following technologies to build Debook: React.js : React.js was a no-brainer for us to choose since all of our teammates have experience in building React.js applications and the Hedera documentation had great support for React.js so it made the development experience very easy too. On top of that, React.js is very fast and efficient, so our end result was also fast and efficient. Solidity : To actually build a decentralized application, we had to use a programming language compatible with the Hedera blockchain which was Solidity, therefore using it was a necessity in order to create the product, though with that said, we were quite comfortable in using Solidity to create our contracts even though we faced some minor errors here and there. Next.JS : As said before, our application had to be fast and we wanted performance, so we went with Next.JS, which is a framework for building React.js applications. Next.JS had quite a lot of features including custom serverless API routes which was important for our use case since we had to compile the user's smart contracts to EVM binary which could only be done on the server side, hence this was a game changer for us. Hedera Smart Contract Service : While we used Next.JS and Solidity to build our application for the blockchain, we actually had to deploy somewhere. That's where Hedera's smart contract service comes in. Smart contract service allowed us to deploy our application to the Hedera blockchain and use the Hedera Hashgraph SDK to execute functions in our smart contract. Challenges we ran into While building the project, we ran into multiple challenges. The first one was dealing with Solidity structs and arrays. It was a minor issue that we were able to resolve in a day or two. The next issue we faced was with Hedera. Although integrating our contracts with Hedera was pretty seamless, Hedera had a restriction on the size of the contract file on the Hedera File Service. This was a problem because we had to upload our smart contract in someway or another. After extensive research through StackOverflow and the documentation, we were able to resolve the error by dividing our file into chunks and uploading each chunk to the file service, then appending the multiple chunks. It worked and our application ran smoothly. Accomplishments that we're proud of We are proud of being able to use Hedera technology in our application without any major issues, as well as the Hashpack library for authentication and management. We are also proud of building a small engine that can convert a json representation of objects and functions to full-fledged solidity code. The main accomplishment really only was being able to bring together the entire project in a short duration of time. What we learned During the hackathon, we learnt a lot of new and amazing things about blockchain and Solidity. We discovered exciting new language features while building our application's smart contracts and we used Hedera's smart contract service for the first time, which was a totally new experience for us. Learning and building on Hedera was certainly exciting as deploying the contracts to the Hedera blockchain and using the sdk was relatively easy, and it has also convinced us to use Hedera in the future. What's next for BuidlSmart In the future, we would like to change our approach of building applications to use flowcharts or block diagrams to ensure a shorter learning curve for the end user and improved accessibility while creating smart contracts. We would also like to expand the application functionality by allowing users to create functions which can delete objects, since currently a user can create functions to read or write objects, but not to remove an object. <div