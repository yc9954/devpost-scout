---
slug: "nearkick"
url: "https://devpost.com/software/nearkick"
title: "Nearkick"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 330
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Nearkick

> Decentralized kickstarter web application.

[Devpost](https://devpost.com/software/nearkick) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[video_visual]] [[web_dom]]

**stack** croncat, ipfs, near-sdk, nginx, react, rust

## How they structured the write-up

- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for nearkick

## Body

Welcome page All projects page Project page Dashboard (mobile view) What it does Nearkick is a decentralized application that allows you to create and kickstart your own projects. The goal is to create a platform that allows anyone to create and kickstart their own projects and anyone to fund them. When supporters of a project reach the goal, the project will be marked as completed. All the supporters will be added to a list of supporters of the project. Later they can verify that they are a supporter of the project. If the project is not funded by the marked deadline, the supporters will be refunded the amount they have contributed. The project will be closed and the supporters will be notified. How I built it Front end is written in React which is bundled and hosted on a Nginx server I used CSS to style and make website responsive for all device sizes Smart contract is written in Rust along with the Near SDK dependency To upload and show images I am using IPFS I am using https://cron.cat/ to autonomously check status of project funding when the end date arrives Challenges I ran into This is my first time writing a smart contract and creating a decentralized application using the Near protocol so I needed to learn about them first I needed a way to store project images, but I didn't want to create my back end server where I upload images since it defeats the purpose of decentralization. I discovered IPFS and learned how it works and I integrated it into my web application What I learned Rust language syntax and features How web applications interact with smart contracts How to make cross-contract calls What is IPFS and how it works How to edit videos :) What's next for Nearkick I need to create a mainnet version of the web application Add additional features that will help users when creating and supporting projects Create Nearkick mobile application <div