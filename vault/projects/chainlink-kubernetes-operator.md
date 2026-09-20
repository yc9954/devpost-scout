---
slug: "chainlink-kubernetes-operator"
url: "https://devpost.com/software/chainlink-kubernetes-operator"
title: "Chainlink Kubernetes Operator"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 772
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Chainlink Kubernetes Operator

> Deploying tons of Chainlink Oracle Nodes and their jobs can be cumbersome and error prone. Kubernetes container orchestration and its operator pattern streamlines everything and lets us scale.

[Devpost](https://devpost.com/software/chainlink-kubernetes-operator) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[video_visual]]

**stack** amazon-web-services, cloudformation, eks, golang, kubernetes, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainlink kubernetes operator
- prizes

## Body

Chainlink Operator UI after jobs being automatically added Custom ChainlinkJob resources in the AWS EKS cluster When these resources are deployed to a Kube cluster, the node gets automatically launched correctly When this ChainlinkJob resource is deployed to the cluster, the operator automatically adds it to the corresponding Oracle node. I used AWS for running my kubernetes cluster and development purposes Inspiration I've been a DevOps/SRE engineer for the past 5 years and have constantly witnessed how easy orchestrating different services at enormous scale is with Kubernetes. It is one of my favorite technologies to use in the industry and I decided to build my project around that. I always wanted to learn how to build my own Kubernetes Operators and this was the perfect chance! What it does The chainlink-kubernetes-operator implements a Kubernetes Operator that can manage Chainlink Oracle nodes and their jobs in a Kubernetes cluster based on declarative Kubernetes resources. Instead of running nodes manually and inserting jobs via the Chainlink Operator UI, we can now deploy custom resource to our Kubernetes cluster and the Kubernetes operator will take care of all the arrangements. I have implemented the Kubernetes Operator and two types of custom resources. A "ChainlinkNode" resource and a "ChainlinkJob" resource. When a user deploys a "ChainlinkNode" resource into a Kubernetes cluster, the operator will spin up all the required deployments and services in one of the nodes attached to the cluster. This happens automatically behind the scenes, abstracted away from the user. Furthermore, to add Jobs to the created chainlink nodes, we can deploy the "ChainlinkJob" resource, which will automatically add the described job to the described instance. This makes it extremely easy to manage even hundreds of Chainlink nodes and their jobs with no risk of human error in their deployment. The deployments also become very resilient, as Kubernetes will always make sure they are running correctly and any crashes are automatically corrected. How we built it I built the operator using the Kubernetes operator-sdk . It created the boilerplate code for a basic operator, which I then extended to handle both of my custom Chainlink related resources. The operator can be built into a docker image and deployed into any Kubernetes cluster alongside its custom resource definitions. For testing purposes, I also set up a full CloudFormation template for setting up a full-fledged AWS Elastic Kubernetes Service cluster up in the AWS Cloud. I also used Amazon ECR (Elastic Container Registry) for storing all my versions of the operator while I was developing it. The GitHub repository contains scripts in the scripts folder for deploying the full cluster, building and pushing the image and deploying the operator to the cluster. Challenges we ran into I had not built Kubernetes Operators before, nor worked with AWS CloudFormation so it was a huge learning experience for me. The biggest issues I had were with adding jobs automatically to chainlink nodes once the ChainlinkJob resource was deployed into the cluster. I had to figure out how to interact with the Chainlink Node API, authenticate my client, and then POST the job details to have it activate itself on the node. This was especially difficult because the Kubernetes Operator I was building had to do all the web requests and it was hard to debug while running it inside Kubernetes. Accomplishments that we're proud of I really feel I managed to make running Chainlink Nodes and Jobs inside kubernetes clusters much more simple than before. Kubernetes is the de facto container orchestration system and I believe there are many more who would like to run Chainlink Oracle nodes inside Kubernetes. What we learned I learned how to use various AWS services, including EKS, ECR, CloudFormation and EC2 much better than before. I also learned how to build new Kubernetes Operator projects and increased my skills in Golang, which is nowadays very prevalent in DevOps/SRE tools. I also learned how to set up the full Chainlink job functionality including operator and consumer contracts and how the operator node interacts with smart contracts to bring off-chain data on-chain. What's next for Chainlink Kubernetes Operator I want to clean up the repository a bit and publish this as an open-source project for anyone to contribute to. The Kubernetes Operator pattern suits Chainlink Operator Nodes and their jobs especially well and I hope to see the project grow. I will certainly keep working on it. My biggest dream would be having the Chainlink Kubernetes Operator as part of the official Chainlink repository one day. Prizes I have applied for the AWS $10k credits prize, and for that my domain is https://lemonking.xyz <div