---
slug: "row"
url: "https://devpost.com/software/row"
title: "ROW"
hackathon: "EOSIO Hackathon: Beyond Blockchain"
organization: "Block.one"
winner: true
words: 936
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# ROW

> Recoverable Online Wallets expand on WebAuthn for use and brings social recovery that empowers communities to secure themselves without trusting any intermediaries.

[Devpost](https://devpost.com/software/row) · hackathon [[EOSIO Hackathon- Beyond Blockchain]]

## Facets

**mechanism** [[provenance_signing]]
**user** [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** c++, css, eosio.cdt, eosjs, gcp-compute-engine-(vm), haproxy, html, javascript, react, typescript, ubuntu, webauthn, webflow, webpack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for row

## Body

ROW logo Inspiration Recoverable Online Wallets, or ROW, is a vision of making blockchain UIs mostly disappear, without introducing trust. With emphasis on low mental costs of users actions, instead converting authentication into a series of (mindless) steps. Account recovery mimics how people get into their house once they get locked. It relies on a multisig of trusted contacts. We believe systems like this would sooner or later replace passwords/otps, phone numbers/emails as ANY security factors, and even replace security coded and KYCas a (easy to phish) recovery procedures. Google cloud securing or at least hosting billions of people accounts could really use the system that removes the current security holes, by making their current webauthn offering including Titan security Keys the focus and disable the insecure fallback methods. What it does ROW consists of smartcontract and webapp without any persistent storage. It uses webauthn to sign transactions and to authenticate. It adds devices under account and saves KeyIDs in the smart-contract, thus eliminating the need for the server. Also removes the risk of the server losing the KeyIDs, which previously meant forever lost key and credentials- which allows the system to run solely on the webuthn keys. ROW takes 2 approvals (multisig) for usage - SYS token transfer in our demo. Usually one device is your PC tpm/enclave, and the other is a phone tpm/enclave. ROW can support any combination of webauthn keys, including external keys like Yubikey and Titan. It removes the need for passwords, emails, mnemonics, etc. In the future owner recovery UI will be added to manage the trusted friends multisig. 2/4 multisig, with 2 current devices and 2 trusted contacts. How we built it First we studied webauthn and FIDO standard to make sure we can safely keep all cryptographic guarantees if we modify it and make KeyIDs public. After determining that we did the compatibility tests with different operating systems and version to make sure we can support enclaves instead of just Yubikeys (external FIDO devices) Then we took EOSIO WebAuthn Example Web App and modify it into webapp hosted on the Google Cloud Platform and demo accessible on the rowauthn.com . We build the simple responsive UI that groups actions together, and an advanced one (click on a tab on the top) that allows us to troubleshoot and test each action on its own. In parallel we were developing the smartcontract . Other than storing multiple KeyIDs under the account, we decided to make it into a full multisig contract. The main reason for that is that we can easily approve using other contracts, which will for instance add support for RSA. Microsoft Windows unfortunately requires RSA when webauthn is used. Our contract still allows users to interact with other smart contracts with their own accounts. Challenges we ran into Bugs in EOSIO frameworks: https://github.com/EOSIO/eosjs/issues/853 https://github.com/EOSIO/eosio.cdt/issues/1075 Before we had finished basic logics of ROWwebapp to retrieve WebAuthn public key and signature we ran into the issue of how to mimic WebAuthn signature to test the contract. It took us some time to get online and offline tools to create the ECDSA signature for curve P-256 and then serialize the public key and signature in EOSIO format. Due to the non-existence of some tools i.e. a tool to convert the public key in hex format to EOSIO string format (PUB_R1_xxx, SIG_R1_) we had to write additional python scripts to achieve this: https://gist.github.com/smlu/021103bcc1da9c621998980a31086ce9 We also had troubles with publishing the contract to the EOSIO blockchain through other tools than cleos . As it turned out there are no publicly available tools for this. Primary goal was to use https://blocks.io to publish the contract but the app doesn’t support serializing contract ABI to binary format. So we had to build the ABI serializer to be able to upload the contract through blocks.io. Accomplishments that we're proud of We believe we made the first full webauthn authentication that fully lives on a blockchain, and doesn’t require the user to trust a server. That makes it self contained, and fully resilient even against inside attackers! We also believe it's the first multisig using webauthn on a blockchain. Whole process (Webauthn signi, serialization data, parsing the key, etc) is running on the client side (in browser). At the last minute we also managed to add RSA onchain validation which adds support for houndert of millions of Windows 10 devices! With some additional work we believe we can fully remove the need for recovery codes and mnemonics in a very user friendly way. What we learned We learned that; we can safely save KeyID on the blockchain without compromising FIDO security. To trick browsers into talking with row.webapp, the site needs to be hosted on https with valid certificate. Windows Microsoft doesn’t expose the P-256 cryptographic curve, so RSA on-chain validation needed to be added to support all Microsoft Windows 10 devices. What's next for ROW Build super simple flutter mobile and desktop apps, only so users can get notifications for second factor via Google Firebase integration- they can keep using the website only if they prefer no installation. Build out an user friendly “recovery UI” for trusted contacts Add account creation/migration functionality Integrate its UI into UAL, so more dapps and portals can easily integrate the ROW as a signer. Interview potential customers outside of the crypto space to figure out how to best leverage 2 factors for authentication. Onchain or offchain? What kind of tooling can they easily interface with? Build it into existing webauthn tooling. Integrate with get Set transaction payer to make transaction proposing free. Find a business case or else. <div