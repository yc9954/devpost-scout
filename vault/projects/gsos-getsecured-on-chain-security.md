---
slug: "gsos-getsecured-on-chain-security"
url: "https://devpost.com/software/gsos-getsecured-on-chain-security"
title: "GETSecured PolygonSECURE Edge Network"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 493
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# GETSecured PolygonSECURE Edge Network

> An AI-Based fully-automated on-chain vulnerability scanner for Polygon Edge with an off-chain automated source code vulnerability scanner for developers.

[Devpost](https://devpost.com/software/gsos-getsecured-on-chain-security) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]]

**stack** angular.js, edge, golang, polygon, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for getsecured network

## Body

Off-chain static vulnerability assessment Bytecode of the smart contract getting deployed Repository of vulnerable source code AI/ML Training Data KNN Classifier ML Model Polygon Edge Integration Inspiration PLEASE watch the final demo here Off-chain vulnerability scanner: https://www.youtube.com/watch?v=PzDGnh7UHNo On-chain vulnerability scanner Part 1 - architecture review and code walkthrough: https://youtu.be/TSa5Nc0LpLo Polygon Edge on-chain security scanning demo with the AI-based vulnerability scanner module: https://www.youtube.com/watch?v=26pSuBrognE Cybersecurity is one of the fundamental principles of any blockchain solution. Unfortunately, we are seeing a lot of data breaches these days where malicious users are managed to hack the smart contracts or exploit some weakness or security vulnerabilities to gain access to others' money and steal it. A lot of such incidents could have been easily avoided if we mandate that developers can only deploy the code in the network if the code doesn't have any major vulnerabilities. Hence I thought of building this CUSTOMIZED VERSION OF POLYGON-EDGE where the code can ONLY be deployed if there is no vulnerability . If the code has any major vulnerability, it will stop the deployment and throw an error back to the developer that the code is not suitable for the deployment What it does I have created a CUSTOMIZED VERSION OF POLYGON-EDGE integrated with my AI model that can do a real-time , on-chain detection of vulnerable code that is being deployed on the polygon edge network and rejects the deployment if there is any vulnerability. How we built it First I have consolidated various bad and vulnerable source code samples and compiled them to create a repository of vulnerable bytecodes that belongs to vulnerable solidity code. Then I created a machine learning model using the GoLearn library. It is a KNN classifier knn.NewKnnClassifier("euclidean", "linear", 2) which is trained with various bad code samples i.e. the comp[iled bytecode repository and has the ability to classify a smart contract code as a good code or d code. Then I integrated that model into the Polygon Edge network golang source code inside func (e *Eth) SendRawTransaction(input string) (interface{}, error) to validate the code at runtime when the code is getting deployed using remix and metamask. Once the polygon-edge code is compiled and running, if I try to deploy a bad code, it will not detect the vulnerability and reject the deployment. But, if the code is good then it will allow the deployment. Challenges we ran into The first challenge was to learn and understand the polygon edge architecture and the code base. The second was to create the vulnerable codebase repository Third, creating the machine learning model using golearn and then finally integrating it with Polygon-edge network source code. Accomplishments that we're proud of Managed to create a complete working prototype with machine learning and polygon-edge What we learned Learned golang programming language, machine learning using golang and obviously polygon-edge What's next for GETSecured Network We would like to launch this as a full-fledged tool to help the entire development community. <div