---
slug: "thetaform"
url: "https://devpost.com/software/thetaform"
title: "Thetaform"
hackathon: "Theta Network 2024 Hackathon"
organization: "Theta Labs"
winner: true
words: 634
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Thetaform

> The World's 1st Decentralized Terraform Cloud Provider, allowing you to deploy AI infrastructure on Theta EdgeCloud like a professional, using standard DevOps practices.

[Devpost](https://devpost.com/software/thetaform) · hackathon [[Theta Network 2024 Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]]

**stack** go, nextjs, terraform

## How they structured the write-up

- thetaform - a terraform provider for theta edgecloud!
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what's next for thetaform

## Body

Thetaform - A Terraform provider for Theta EdgeCloud! Thetaform landing page: https://thetaform.cloud Source code and install instructions: https://github.com/igorperic17/thetaform Personal dev blog: https://igorperic.dev Inspiration Having worked many years with AWS I appreciate the benefits of Infrastructure as Code (IaC) and what it brings to development teams. Setting up certain services is not an easy task using traditional cloud providers due to their bloated nature (IAM roles, permissions, storage services, VPCs, just to name a few). Having found out about Theta Edge Cloud I was impressed by how easy and straightforward it is to set up a dockerised AI service from a template, and yet it was so easy to customise by bringing your own container. As a Director of AI Research and Development at https://coretex.ai I was thinking about the possibility of integrating Theta Edge Cloud into our product suite. This partnership could have significant benefits to both of our user bases. I started thinking how would a team of ML or software engineers go about developing their AI models on Coretex and later deploying them on Theta Edge Cloud. I quickly realised Theta Edge Cloud misses a key component to be included in standardised DevOps practices in the industry - Infrastructure as Code (IaC) support. Since I have experience with Terraform and AWS, and there doesn't seem to be any Terraform provider for Theta... I decided to build one myself. :) What it does It lets you create Theta infrastructure in Terraform, so you can automate and secure usage of Theta Edge Cloud in your DevOps flow, allowing you to lower your cloud bill. You can: Programatically deploy AI model servers from a Theta library or your own Docker image Spin up/down Notebook servers from your Jenkins pipelines or GitHub actions, user Manage your Theta videos as infrastructure resources in your Terraform scripts ... and much, much more if I win this hackathon. :D How I built it The whole Terraform provider was developed locally in Golang from scratch. Since there is no official EdgeCloud CLI, I had to first build a client CLI library in Go which handles authentication and CRUD operations. While doing it reverse engineered the Theta EdgeCloud API by analysing network activity while using the web app, and "documented" the API in a Postman Collection. Most of the time I was fighting with properly marshalling requests and responses, but once the state management clicked I was flying! :) Challenges I ran into Reverse-engineering EdgeCloud API was not a walk in the park (it was changing during the hackathon) Lack of EdgeCloud infrastructure availability (machines were busy very frequently) Didn’t get to finish Video resource management, looking forward to get to it! Accomplishments that I’m proud of Finishing the submission on time! :D Running "terraform apply" feels different now, knowing exactly what happens under the hood... Learned a LOT and had fun while doing it! What I learned Go as a language Terraform provider development Theta ecosystem (even outside EdgeCloud - I tested and loved the Edge Node!) What's next for Thetaform My dream is to polish it, write mandatory unit tests and publish on the official HashiCorp provider repo! :) I’ll keep working on it and hopefully get in touch with EdgeCloud team to help them iron out some of the API functionalities, perhaps even release CLI as a standalone binary. I’ll definitely finish the Deployment Resource, and build the Video/Streaming Resource at least, but I have ideas for smart contract IaC as well (deploying ERC20 through TF, private key vault integration, key rotations, contract upgrades, etc). I truly believe in a future where DevOps Engineering teams choose Theta as one of their cloud providers over typical choices of AWS, Azure, GCP, Digital Ocean and others. And I believe building Theta Terraform provider is a step towards that future! <div