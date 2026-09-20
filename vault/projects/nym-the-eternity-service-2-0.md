---
slug: "nym-the-eternity-service-2-0"
url: "https://devpost.com/software/nym-the-eternity-service-2-0"
title: "Nym, The Eternity Service 2.0"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 537
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
---

# Nym, The Eternity Service 2.0

> A client that exemplifies how to send a file via the Nym network. The destination address can be a nym-file-service-provider, which will save a copy of the file locally.

[Devpost](https://devpost.com/software/nym-the-eternity-service-2-0) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[finance_payments]]

**stack** antd, electron, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nym, the eternity service 2.0

## Body

NYM Inspiration GUI development is one of my hidden passions and I wanted to try out the Nym challenge. Also I have some previous experience in privacy driven systems. So this is why i picked it as one of my projects for the HACKATOM. It was a bit of a challenge to use the testnest, but in the end I liked it because it was something new I wanted to learn. Also a friend suggested I pick up this challenge. He like the privacy-anonymity topic. He helped me a bit with the development, especially enabling the app as a desktop application. What it does A client that exemplifies how to send a file via the Nym network. The destination address can be a nym-file-service-provider, which in turn will save a copy of the file locally. The file is encrypted on the client, and stored like that. The client can come at any time to ask for the file by it hash. He can download files and delete them. Because the files are encrypted using a key stored only on the client nobody else will be able to see the content of the file. Also the anonymity aspect of the NYM network cannot identify the owner of the file. Even if somebody else guesses the hash of the file and downloads it he won't be able to decrypt it. How we built it The application is written in React with Typescript. Can be run as a browser app or a desktop app using the Electron framework. The client was tested on the Milhon NYN tested (v0.11.0) running a nym-client built from source, v0.11.0. A separate nym-client instance must be run for the file-service-provider and another one for the nym-file-uploader-client. Each one will listen on different ports in case they run on the local machine. The configuration of the server-provider that is used by the current client can be done from src/config/Config.s. In the same place you can configure the nym-client used by the client. The messages sent between the client and the service-provider are binary messages. The encryption algorithm used for the files is AES-CTR 128. The hashing is done using an md5 sum. The metadata about the files is stored in the browser localStorage. Challenges we ran into The nym-clients disconnects from the time to time and is required restarts. This also implies I need to restart from time to time the file-service-provider. So as a consequence the development was slower. Accomplishments that we're proud of Obtained a functional app that can be easily extended both on desktop and in the browser. What we learned Encryption mechanism in client side applications. Sending raw binary data via sockets which is the most efficient way of transferring data. No more overhead caused by JSON encoding. Decoding base58 addresses from binary data. Overall working a bit more with low level data. What's next for Nym, The Eternity Service 2.0 Support for public files Support for larger files, split content in chunks Creating a protocol that identifies what are the operations supported by a running service provider. Make it extensible Embed payment systems Connect service providers with external file storage systems, maybe distributed blockchain storage such as Storj, Sia, etc <div