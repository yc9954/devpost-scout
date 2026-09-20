---
slug: "akash-cosmos-omnibus-evolution"
url: "https://devpost.com/software/akash-cosmos-omnibus-evolution"
title: "Akash Cosmos Omnibus evolution"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 839
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Akash Cosmos Omnibus evolution

> Extends support for running Cosmos SDK powered validator nodes on the Akash network

[Devpost](https://devpost.com/software/akash-cosmos-omnibus-evolution) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** bash, docker

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for akash cosmos omnibus evolution

## Body

web tool thornode localhost rpc docker logs of thornode panacea rpc running on akash Inspiration Traditional cloud providers come with a lot of advantages. One of them is renting hardware resources on demand for a given period of time without needing to hassle about maintaining them, keeping them safe from attackers, redundancy and so on. However the issue with cloud providers such as AWS, GCP or Azure is they are centralized and managed by a centralized organization. This doesn't make them as a valid running environment for Web 3.0 where applications have the objective to become as decentralized as possible and become immune to power outages or infrastructure problems. It defeats the purpose of having a decentralized application if most of its nodes run on a single cloud provider and when that cloud provider has some downtime the decentralized network used by our app is susceptible to stake majority attacks. Or it could even face downtime for projects still found in its inception that have a small number of nodes. This is not just a theory. Its something that happened and it will still continue to happen in the future. Akash comes as a decentralized cloud application solution. For me this represented an opportunity to try learn its internals and get familiar to it. I also helped the Cosmos ecosystem get more support on having a decentralized infrastructure that runs in different parts of the world, and on different providers. What it does The cosmos-omnibus project allows you to run validator nodes for different chains that use the Cosmos SDK. It does so by defining a Dockerfile that is generic and suitable to build projects derived from tendermint. On every new release of the project (cosmos-omnihub) on github a github worflow will create new docker images from those Dockerfiles for each subproject in its repository and it will store them on ghcr.io docker image repository. From there the images can be used to deploy a validator node on the akash network. Similar to running the images on the Akash network you could also run it on any other environment. So the repository also serves as collection of instructions on how to build a multitude of blockchain validators. How we built it In the project I extends support for 3 different projects: panacea, thorchain and cyber. To test their functionality I had to create some docker-compose files and run the validators locally from the docker-compose files. The nodes are built from source, which means they are authentic. There is no way to use an altered version of a binary, linux package or a an altered Docker image from different third parties. So part of the challenge was to get accustomed with this projects. Panacea is a project developed by medibloc and it allows to store medical data of the patients in a decentralized way. Thorchain is a decentralized exchange that enables swap of assets such as Ethereum, Bitcoin and Binance Coin. The validator node is just a small piece in the whole stack ran by the decentralized exchange, but having support for validator nodes will help the network to become stronger and safer. Cyber (bostrom) is a project that it is still in its inception and has the purpose of building a consensus system that behaves similar to a search engine. It proposes to solve the issue of having a central authority that is acting as crawler of the web (e.g. Google Search) Challenges we ran into panacea was pretty easily to add suport for as it worked right away with initial Dockerfile found in the cosmos-omibus project for panacea I also added a SNAPSHOT json file which contains the URL to the SNAPSHOT file. This can be used to speed up the synchronization of the chain. Used filebase(dot)com as a storage for the snapshot.json file. thorchain however required me to add some new functionality to the repository: possiblity to add some third party requirements to an image (apt packages dependencies) extra build arguments passes as environment variables to make install support for golang 1.17 (most of the projects from cosmos-omnibus run on golang 1.16, however some newer projects also require golang 1.17. the methods I used to enable golang 1.17 allows easy customisations and can be applies to use different versions of golang) override variables in config.toml files (more specifically the P2P seeds) by inline replacement I also had to make the PR for the chain-registry repo as there was no support for it yet bostrom required to also run golang 1.17 and I had to pass extra argument on start to run without GPU support because akash network is not supporting that at the moment. Accomplishments that we're proud of I was able to enable support for multiple validator nodes What we learned to build cosmos-sdk validators from source using the akash network the deploy applications on a decentralized cloud What's next for Akash Cosmos Omnibus evolution extend support for new chains contributing also to the chain-registry repository to add missing cosmos sdk projects maintaining existing projects <div