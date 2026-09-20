---
slug: "silas-avery-yong-kang"
url: "https://devpost.com/software/silas-avery-yong-kang"
title: "DataNexus"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1004
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# DataNexus

> DataNexus enables everyone to control and monetize their data and provides data seekers with invaluable alternative data sources to fuel our data-hungry world.

[Devpost](https://devpost.com/software/silas-avery-yong-kang) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]] [[web_dom]]

**stack** chainlink-functions, hardhat, next.js, nft.storage, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for datanexus

## Body

Data Listings Dashboard My Data Listings Providing Data User Account OVerview Inspiration Problem Companies are hungry for alternative data sources that can provide a competitive edge. At the same time, individuals want to finally control and monetize their data. This creates an opportunity for a mutually beneficial data marketplace. There's currently no platform that lets people sell their information directly to companies in a secure, profitable way. Solution DataNexus bridges the gap between companies seeking alternative data sources and individuals looking to monetize their personal information. Our platform allows data seekers to specify their needs, prompting users to contribute relevant personal data to a collective pool. This highly secure, encrypted, and decentralized data pool becomes a rich source of nuanced insights once merged. DataNexus provides access to detailed, individualized information that could enhance the predictive abilities of AI models at scale. And unlike traditional data brokers, our platform ensures each participant is fairly compensated while fully protecting privacy through encryption. By forging connections between data demand and supply in a secure, transparent, and decentralized manner, DataNexus pioneers a new data marketplace – one that finally puts power back into the hands of individuals. Our solution transforms how data is traded in the digital age. What it does Our platform enables seamless, secure data transactions between purchasers and providers. Purchasers create Data Listings detailing their desired data. Providers then sell their data by sending encrypted API Data keys to the Listing contract. This triggers a chain of automated steps: The DataListing contract decrypts the provider's API key using a Functions script. It fetches the provider's API data and encrypts it with the purchaser's key. The encrypted data is posted to IPFS for the purchaser to access. This workflow allows providers to share access without ever exposing their API keys. Purchasers can only view the data they purchased. The entire transaction happens securely on-chain. How we built it We built DataNexus with Chainlink Functions and the NFT.storage HTTP API. We developed two smart contracts, DataListing.sol and DataListingFactory.sol, and used a hybrid RSA /AES encryption scheme to protect providers' data and API keys. DataListings Are owned by purchasers, who fund the contract and set the data source, number of data points, and price per data point Store the public keys used to encrypt provider data and API keys, as well as an encrypted gist URL containing the private key used to decrypt provider API keys Contain a Functions script to securely transfer provider data to purchasers Store IPFS CIDs containing encrypted provider data Functions Script Decrypts the providers API key and fetches their data Generates an AES key and encrypts provider data Posts encrypted data to IPFS using the NFT.storage API Return the IPFS CID to the DataListing DataListingFactory Creates DataListings and transfers purchaser funds to their new listing Keeps track of DataListings and their owner/purchaser Challenges we ran into Posting data to IPFS Posting data to IPFS in chunks - Due to the 2KB size limit on Function requests, we had to split data into multiple chunks before uploading to IPFS. This added complexity to managing the uploads. Duplicate requests overloading NFT.storage - Our Function DON nodes making duplicate requests to NFT.storage for IPFS uploads occasionally resulted in errors. We had to implement retries with backoff to handle this. Temporary API key ban from testing - While testing our system, one of our API keys was temporarily banned due to too many requests from our Function nodes. We had to obtain new keys and implement better request throttling. Encrypting with purchaser's public key - We wanted to encrypt data with the purchaser's public key to avoid them needing to manage an extra decryption key. However, the Functions toolkit lacks cryptography libraries to do this securely. Data size/encryption Data size limitations with RSA encryption - Our initial encryption with RSA keys limited data packets to 256 bytes, which was insufficient. We switched to AES encryption to handle larger packet sizes. Our script now generates an AES-GCM key, used to encrypt the API response, then encrypted with the purchaser key and posted to IPFS with the data Frontend Integration Import issues with Functions toolkit - We could not import the Functions toolkit into our frontend codebase, preventing us from easily managing subscriptions, consumers, and secrets. We did not have time to re-implement this functionality. Google Verification For privacy reasons, Google requires apps to go through a verification process before allowing access to user data through Gmail. Since this is just a hackathon project, we haven't gone through that process yet. If you'd like to help us out by providing access to your email data for testing purposes, feel free to DM one of the team members to get your email address whitelisted. We appreciate your understanding that collecting user data responsibly is a priority. Let us know if you have any other questions! Accomplishments that we're proud of We successfully built an MVP that allows users to securely sell their data through Chainlink Functions and IPFS. The threshold encryption scheme we implemented provides a high level of security for sensitive user information. Overcoming the limitations of making external API requests from Functions was a technical challenge we are proud to have solved. What we learned Through developing DataNexus, we gained valuable experience with Chainlink Functions - their capabilities, limitations, and best practices. We explored innovative techniques like threshold encryption to handle secure key management. Integrating external APIs posed some difficulties that taught us a lot about how to design serverless architecture. What's next for DataNexus In the future, we plan to integrate more data sources beyond just Google Fitness to provide users with more options for selling their data. We want to build our own IPFS pinning service to replace the current NFT.storage solution. To improve the purchaser experience, we will explore cryptographic methods to provide access to purchased data without requiring the storage of a private key. Overall, we aim to build on what we've learned to scale up DataNexus into a fully decentralized data marketplace. <div