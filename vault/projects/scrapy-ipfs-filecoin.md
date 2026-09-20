---
slug: "scrapy-ipfs-filecoin"
url: "https://devpost.com/software/scrapy-ipfs-filecoin"
title: "scrapy-ipfs-filecoin"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 429
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# scrapy-ipfs-filecoin

> Scrapy IPFS Filecoin provides scrapy pipelines and feed exports to store scraped items into IPFS and Filecoin using services like Web3Storage, LightHouse, Estuary, Pinata, and Moralis.

[Devpost](https://devpost.com/software/scrapy-ipfs-filecoin) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**substrate** [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** estuary, filecoin, ipfs, lighthouse.storage, moralis, pinata, python, scrapy, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for scrapy-ipfs-filecoin

## Body

Python package Github Repository Logo Inspiration Scrapy is an open-source and collaborative framework for extracting the data you need from websites. It has supported storage such as File system, FTP, Amazon S3, and Google Cloud Storage but it has no support for IPFS & Filecoin storage. Also, I did not find any official support for decentralized storages like IPFS & Filecoin. So feeling the need for decentralized storage like IPFS & Filecoin storage support for scrapy I am inspired to add support for IPFS & Filecoin storage to upload images and other files and the scraped result in the format supported by scrapy. What it does It provides support for decentralized storage like IPFS & Filecoin storage (i.e Images & File pipelines and Feeds export) to scrapy so that the images & other files and scraped output can be uploaded to IPFS & Filecoin using different services. How I built it I explored scrapy documentation regarding Files & Images Pipelines and Feed exports to understand and inherit it to support storage for IPFS & Filecoin. Then I explored documentation of different services facilitating the storing of files like Web3.Storage, Estuary, LightHouse.Storage, Moralis and Pinata. Then I created clients for each of them to upload files and then created Files & Images Pipelines to upload files to IPFS & Filecoin utilizing the clients. Then I create Feeds export to export the output of scrapy scraping utilizing the clients. Challenges I ran into It was challenging to understand the scrapy flow for pipelines and feeds export to store the files and scraping output to IPFS & Filecoin. I studied the documentation & code and finally understood the flow. And another challenge was integrating the different services supporting IPFS & Filecoin into it. After all, I overcome the challenge and finally came with the support for IPFS & FIlecoin to scrapy using different services. Accomplishments that I am proud of I am proud of being able to add decentralized storage support like IPFS & Filecoin storage for scrapy to upload files and scraped results in different formats using different services. What I learned I was dedicated to adding support for IPFS & Filecoin storage to scrapy which is a popular python scraping framework. So in doing so I learned about the scrapy pipelines and feed exports and also the different services available to store files to IPFS & Filecoin. What's next for scrapy-ipfs-filecoin Scrapy-IPFS-Filecoin will continue to be optimized so that it becomes better and bug-free and also add support for other additional services to store files to IPFS & Filecoin. <div