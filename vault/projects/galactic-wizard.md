---
slug: "galactic-wizard"
url: "https://devpost.com/software/galactic-wizard"
title: "Galactic Wizard"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 485
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Galactic Wizard

> Tokenize...Anything

[Devpost](https://devpost.com/software/galactic-wizard) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** albedo, javalin, javascript, kotlin, sqlite, stellar, svelte

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for galactic wizard

## Body

View created tokens Buy Tokens Create Tokens Claim Tokens Inspiration I was inspired by the Stellar Quest badges, I thought it was really cool that you are able to easily create tokens that can represent anything, And then trade those tokens. What it does This project is based on one of the challenge proposed by Stellar, specificcaly: "Combine Stellar and IPFS, Filecoin or Torrent for an NFT wizard" Galactic Wizard is a web app that allows people to easily create tokens to represent anything. To create tokens, an issuing and distribution account are used. The token is created by the issuing account and then sent to the ditribution account to be distributed. Galactic Wizard allows you to create normal tokens and NFTs (Unique Tokens). Aside from the normal options of an asset (token), Galactic Wizard also allows you to associate data with a token. This is done by adding data to the issuing account, which is possible on stellar, and interpreting this value as being associated with the token. Normally you would only be able to upload a small amount of data, but Galactic Wizard allows you to add files by first uploading the file on ipfs and storing the ipfs hash on the stellar blockchain. Another special options is the ability to add a description to the token, this can then be used to give more information about what the token is and what it represents. Additionally you can also specify how you want to distribute the tokens. Currently you can place a sell offer on the Stellar Decentralized Exchange to sell your token for US Dollars or you can reserve the tokens for a specific stellar address. Galactic Wizard also allows you to view the created tokens, claim tokens that are reserved for you and buy tokens that are being sold on the Stellar decentralized exchange. How I built it To build the view of the front-end I used js , svelte and carbon components . To build the logic of the front-end I used the 'stellar-sdk , js-ipfs , js and albedo` For the back-end I used kotlin , javalin , ktorm , sqlite and moshi . The back-end keeps track of the tokens created using Galactic Wizard so the client can easily request that informatin. The information about the tokens is stored in a sqlite database. Challenges I ran into Dealing with really small numbers Using javascript. Dealing with multisignature transactions Accomplishments that I'm proud of I am proud that I used the knowledge I gained from Stellar Quest to build an application that is usefull and functional. What I learned I learned a lot about the options of using nft and tokens on Stellar. What's next for Galactic Wizard Add ability to auction tokens. Optimise fetching of ipfs images. Add ability to host a stellar.toml file. Add ability to choose curreny when selling a token. host frontend on ipfs <div