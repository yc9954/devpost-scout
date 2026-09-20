---
slug: "api-based-latex-cluster"
url: "https://devpost.com/software/api-based-latex-cluster"
title: "API based LaTeX Cluster"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 567
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/document_pdf"
---

# API based LaTeX Cluster

> The developed LaTeXCluster connects LaTeX nodes around the world and provides an API for developers, enabling them to quickly and easily implement applications with complex LaTeX functionality.

[Devpost](https://devpost.com/software/api-based-latex-cluster) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** angular.js, docker, imagemagick, latex, mysql, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for api based latex cluster

## Body

Inspiration LaTeX is a software system for document preparation in professional fields. Examples are science and engineering, economics, linguistics or musicology or fields with e.g. non-Latin scripts or complex math expressions. Unfortunately, the process of installing, handling and compiling LaTeX documents is still associated with a lot of knowhow and working effort which prevents and slows down many development projects. Easy access to LaTeX environments would leverage massive benefits for various application areas. What it does To solve the problem described above, an API based LaTeX cluster concept was developed in this hackathon project. This allows developers to use a distributed server network of LaTeX nodes and compile LaTeX documents through an API. The LaTeX environments (so called LaTeX Cluster Nodes) can be hosted on different servers and be accessed by a HTTPS API. They can also be managed by an access server (so called Cluster Manager Server) which implements the API to a set of LaTeX Cluster Nodes. How we built it The LaTeX environments were encapsulated in a Docker running Ubuntu and equipped with a developed NodeJS wrapper that connects the HTTPS API with LaTeX commands. This also includes automatic preprocessing (e.g. code injection in LaTeX templates or setting compilation parameters like format) and code preparation. In addition to the LaTeX environment, further packages like imagemagick have also been integrated to further increase functionality and flexibility. After the request, the nodes then return the compiled document in the desired format. If you want to address multiple nodes or integrate load balancing an interconnected Cluster Manager Server is an appropriate solution. For this purpose, a nodejs server or nginx can be used. Challenges we ran into The compilation of user LaTeX code is demanding, so that no security vulnerabilities may occur. Therefore the integration of numerous validity checks and authorization concepts was necessary. In total, a stable software version was achieved during the hackathon. Accomplishments that we're proud of Addressing LaTeX commands by an API in own applications e.g. within web servers or browser applications was not easily possible and such an open source LaTeX Cluster with the explained functionality did not exist until now. An important building block was the wrapper approach, which opens the LaTeX world for API users. You can now also host your own LaTeX cluster nodes or connect them with a Cluster Manager Server. In particular, I was able to solve the problems that arose in the area of pre-processing, communication and execution of the LaTeX cluster nodes. I am convinced that this will enable and accelerate many usecases of developers. With the API, developers are empowered to quickly and elegantly implement applications with LaTeX functionality. What we learned During the hackathon, I learned about the architecture and challenges of a scalable computing cluster that can be accessed via an API and how valuable automated testing with Postman is in such a software project. What's next for API based LaTeX Cluster Further development of a Cluster Manager Server for managing and selection of specific LaTeX Cluster Nodes (e.g. by geographic location or uptime) Expanding the cluster network to more servers around the world by reaching out to the LaTeX community. Feel free to watch my short video summary . If you have any further questions about the concept or the operation, please do not hesitate to contact me. Thanks for your interest and see you at the Postman Galaxy Conference. <div