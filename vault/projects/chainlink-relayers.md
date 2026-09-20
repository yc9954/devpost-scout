---
slug: "chainlink-relayers"
url: "https://devpost.com/software/chainlink-relayers"
title: "Chainlink Relayers"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 878
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
---

# Chainlink Relayers

> Decentralised, trust minimised meta-transaction relays as a Chainlink service.

[Devpost](https://devpost.com/software/chainlink-relayers) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]]

**stack** foundry, solidity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for chainlink relayers

## Body

Relayers App Dashboard Inspiration To create a high-quality, adaptable relay service, similar to Chainlink Keepers to simplify meta-transaction relays, allow clients to pay in Link and provide a familiar user experience. Existing solutions inspired me to leverage the high-quality Chainlink decentralised oracle network validator set to create a streamlined Chainlink service. What it does Chainlink Relayers uses a decentralised oracle network (DON) to relay meta-transactions in a highly-reliable. trust-minimised way. The user and developer experience is made simple by keeping the implementation similar to Chainlink Keepers. It removes the requirement for forwarder contracts as with other meta-transaction services and reduces trust by using a DON. Relayers allows a 'user' of a DApp to sign a message containing the information of the relay they wish to request which is then relayed by the ON so that transactions can be paid for by the relay 'client'. Client contracts will be submitted for relay and funded via the Relayers App which will abstract away interaction with the Registrar contract in an almost identical way to Keepers. Relayers provides a solution which is adaptable, allowing for custom logic to detail conditions for whether a 'user' request for Relay is accepted or denied based on the given parameters. An example for this would be: allowing a finite number of transaction relays per user for a given function whilst limiting the global maximum number of transaction relays across all users i.e. "only the first 100 to mint go free". This is handled by the client in the Relay compatible contract and by setting the checkData parameter upon registering the contract for Relay, to specify the selector of the function(s) to check users against. How I built it Adapted the existing Keepers contracts to ensure the UX was familiar Developed a Registrar contract for Relay clients to submit and fund their Relay compatible contracts. Developed a Registry contract to provide instructions to the Relayers, the oracle network nodes, for how to execute and manage Relays. *Developed an interface for Relay contracts to inherit from to ensure compatibility with the Registry for Relay via the Relayers. Challenges I ran into The main challenge when building this service was determining if the current Chainlink core code could be made compatible for Relayers. I attempted initially to use the existing core adapters to create a job specification but will need to dig further into how this could work or if extra functionality needs to be added. Limited time! I wasn't able to complete everything before the deadline but I am excited to see if anyone is interested in the project and can offer some guidance to create the finished service. Accomplishments that I'm proud of Take on a project with no prior knowledge on my own despite many setbacks and unknowns Being able to understand and adapt the Keepers code to create a streamlined service Despite the service currently not being end to end completed, I came from knowing very little about Chainlink and no experience of smart contract development before the hackathon, so being able to create the service architecture is a big achievement. I started the Hackathon 2 weeks into the start date as I found out about it late. I have had many personal setbacks including a family bereavement, which was my main motivation to start the hackathon to make him proud, and became unwell in the final week so was unable to create an end to end product. Despite this I view my submission as a success to have something to submit despite my personal situation. I also want to say a massive thank you to all the organisers of this event for giving me this opportunity, particularly Patrick who, through his many many tutorials, I have learnt almost everything I know from. What I learned That making a Relayers service is more complicated than I initially anticipated. It is made more complex by the inability to simulate the requirement for a job run by checking the on-chain state to signal when a user has requested a relay transaction. You cannot listen for events as with a direct request job as that would require a transaction, defeating the purpose of the relay. I originally looked at using an RPC wrapper, similar to the CCIP reference implementation, to transmit relay requests but could not determine how to connect to an oracle network without understanding the core Chainlink client code - something that I will be looking at next. I learned a lot for this hackathon - Solidity, Foundry, using signed data types and understanding and using the EVM. What's next for Chainlink Relayers Create an end to end service by connecting with an oracle network Build an App front-end for clients to submit contracts for user relays. The design for this front end is added at the top of this page and is similar to Keepers, in design and programmatically, to create a familiar and simple yet highly adaptable and reliable service. Create unit tests for the main contracts. Since the functionality is similar to Keepers, the unit tests will be similar. Given the time limit and personal circumstances, I could not create >150 unit tests, as is the case with Keepers, as porting and adapting all these tests will be a large undertaking. <div