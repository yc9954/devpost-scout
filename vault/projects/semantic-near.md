---
slug: "semantic-near"
url: "https://devpost.com/software/semantic-near"
title: "Semantic Near"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 697
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/transportation"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Semantic Near

> Perform Semantic Search over all the posts of any user on the decentralized Near Social network.

[Devpost](https://devpost.com/software/semantic-near) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[transportation]]
**substrate** [[video_visual]] [[web_dom]]

**stack** docker, faiss, near, nearsocial, nextjs, openai, python, react, tailwind, typescript, vercel

## How they structured the write-up

- background & architecture
- build
- improvements
- acknowledgement & disclaimer

## Body

SemanticNear Perform Semantic Search over all the posts of any user on the decentralized Near Social network. Website here . Github here . Background & Architecture The Near Social Network is a fully decentralized social network that lives entirely on the NEAR blockchain. As usage of the platform grows and becomes a more prominent source of news and media consumption in the future, tools such as Semantic Search are required to help parse this information. Because all data is stored on-chain, the contracts are optimized to minimize storage. Thus, although a user may have made hundreds of posts over time, only a single post is stored in the smart contract state at any given time. When a new post is made, the old post is deleted to free storage and the new post replaces it. Thus, recreating the entire chain of user posts requires traversing the blockchain history to analyze each block and fetch the current post for the user at that block. Building an indexer would be the best solution for this problem, but due to resource & time constraints, we opt for a different solution. A user inputs a Near Social account id along with a semantic search query. We use the Pagoda Enchanced API to then grab all the blocks that the account ID of interest has had any interaction in. We then query the SocialDB Contract (which contains all the state of Near Social) to reconstruct the chain of posts the user has made. These posts are then passed into our backend server, which is written in python & uses FastAPI as the web framework. With the posts in hand, we use NLTK to slice up the text into smaller chunks composed of complete sentences. This will allow us to identify the most relevant chunks of text. We calculate the word embeddings for each of our chunks – the embeddings come from OpenAI's Embedding Model . With embeddings in hand, we compute a similarity search using Facebook Research's FAISS library against the user-inputted semantic search query. In order to capture surrounding context, we also retrieve neighboring textual chunks (the +/- 1 chunks that surround the relevant chunks we have found). We then return these results to the user. For deployment, we deploy a docker container on AWS ECS using Fargate as our compute engine to autoscale compute resources depending on website load. Our container fleet sits behind an Elastic Load Balancer that provides SSL termination. Build Backend For our backend code we use a Makefile for our build process and Poetry as our dependency manager for Python. Install poetry, change directories into the server folder, and then run poetry install to install all dependencies. Note that we require python 3.9.13 and that the Rust Compiler must be installed on your machine in order to build certain dependencies. An OpenAI API Key is required for the project, and must be available in the environment as OPENAI_API_KEY . You can run export OPENAI_API_KEY=<your key> in your current shell or add the key to your .zshenv file. Afterwards, run make setup to configure your environment to run our application. To run the server run make server . To build a docker image for the server run make docker-build-local . To create a docker container based on the image run make docker-run-local . Frontend Our frontend is built using React , Next.js , and Tailwind CSS . To run our web app locally, change directories into the frontend directory and run yarn install to install all dependencies. Then run yarn dev . Improvements This is an early prototype and there are many improvements to be made. A cleaner integration with Near Social would allow a user to login into their account and select multiple users to conduct a semantic search on. In it's final form, this may look like a Near Social Widget that allows a user to effectively parse information through their feed via blazing-fast semantic search. The word embeddings of a user's feed can be computed & caches before hand, and websockets can be used to allow for real-time search results. Acknowledgement & Disclaimer This is a prototype and has not been thoroughly battle-tested. <div