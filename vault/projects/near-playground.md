---
slug: "near-playground"
url: "https://devpost.com/software/near-playground"
title: "Near Playground"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 618
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/structured_db"
---

# Near Playground

> Near Playground is a browser-based editor that allows developers to write, compile, test and call Near Rust and AssemblyScript Smart contracts in the browser.

[Devpost](https://devpost.com/software/near-playground) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[education]] [[supply_logistics]]
**user** [[developer]] [[educator_student]] [[general_public]]
**substrate** [[structured_db]]

**stack** javascript, near, node.js, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for near playground

## Body

Main page Projects Page Writing smart contract in Rust Writing smart contract in AssemblyScript Testing smart contract in Rust Rust project NPGManifest.json file AssemblyScript project NPGManifest.json file Calling view method in smart contract written in Assembly Script Inspiration While participating in the Chainlink Fall Hackathon I spent a lot of time using the Remix IDE to write smart contracts, so I decided to build something similar for Near. What it does Near Playground (NPG) is a developer tool that allows users to write, test, compile, deploy, and call Near smart contracts in the browser. NPG allows users to develop smart contracts in both Rust and AssemblyScript. NPG also allows the user to export the smart contract project by clicking the download button available in the file explorer. How we built it Near Playground can be dived into 3 parts: frontend, smart contract, backend. Frontend The frontend was built using Javascript, Vue.js, Vuetify, CodeMirror, and NEAR-API-JS. We used Vue.js and Vuetify to build the User Interface, and CodeMirror to build the code editor. NEAR-API-JS is being used to authenticate the user by interacting with the Near wallet, deploying, and calling smart contracts. Smart contract I wrote a smart contract in AssemblyScript named contract manager that allows users to keep track of the smart contract projects that he is working on. Whenever the user creates a project in Near playground a function in the contract manager is called in order to add the new smart contract id, name, type(programming language, Rust/AssemblyScript), and owner (user account id). Backend The backend was built with Node.js and express. The backend allows users to run unit tests, compile contracts using both NEAR-SDK-RS and NEAR-SDK-AS with just a click of a button in the UI. Near Playground comes with two starter templates for both languages. The Rust starter template is the counter example provided by Near, and the AssemblyScript template which is a CRUD smart contract written by me that allows users to manage a students database. Inside each template there is a file named NPGManifest.json . This file is where the user needs to declare the functions that his smart contract has in order to be able to call it. Here is the NPGManifest.json file for the AssemblyScript template: { "viewMethods": [ { "name": "getStudents", "args": [] }, { "name": "filterByJSKnowledge", "args": [ { "name": "knowsJavaScript", "type": "boolean", "default": false } ] } ], "changeMethods": [ { "name": "addStudent", "args": [ { "name": "id", "type": "string", "default": "" }, { "name": "name", "type": "string", "default": "" }, { "name": "age", "type": "int", "default": 0 }, { "name": "gpa", "type": "float", "default": 0 }, { "name": "knowsJavaScript", "type": "boolean", "default": false } ] }, { "name": "removeStudent", "args": [ { "name": "id", "type": "string", "default": "" } ] } ] } In the file above we declared the functions that the smart contract has, as well as the arguments that each function takes in the args field. The allowed arguments types are : string, boolean, int, and float . Challenges we ran into On some rare occasions Near testnet RPC server would throw a 500 internal server error while I was working on the project Accomplishments that we're proud of I am proud that I was able to learn the basics of writing a Near smart contract and build such a large project in less than 3 weeks. What we learned I learned how to write, test, compile, and call Near AssemblyScript, and Rust smart contracts. I learned how to build a browser-based code editor and a file explorer. What's next for Near Playground Add code linting for both Rust and AssemblyScript. Add more starter templates Dockerize the application Release NPG to the public <div