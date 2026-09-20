---
slug: "izmjs-devtools"
url: "https://devpost.com/software/izmjs-devtools"
title: "IZMjs Devtools"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 447
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# IZMjs Devtools

> Imagine you write your code and you click a button to generate the API documentation of the whole project. This exactly what you can do and a lot more when using the IZMjs devtools.

[Devpost](https://devpost.com/software/izmjs-devtools) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** express.js, javascript, mongodb, node.js, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for izmjs devtools

## Body

Inspiration During the development of NodeJS projects, it was always hard for me to keep the API documentation updated with the code. Also, going back and forth between the IDE and Postman distracts me a lot. This is why I thought about a solution that keeps me concentrated on the IDE, and generates the postman documentation without even leaving the code editor. What it does The project has two parts: IZMjs framwork : It helps developers to: Build their projects in a modular and maintainable way Reuse their existing modules just by cloning them as submodules or even just by copying and pasting them to the modules folder Manage the ACL in a very simple way Code faster using predefined snippets Comes with pre-developed modules: Chat module : Allow developers to add realtime chat system without adding a single line of code. It can be configured with redis to support multi-servers. Files module : Used to support files management. The files will be uploaded in GridFS and very rich with features like: uploading, downloading, listing and sharing files. Apps module : If you need to perform server to server communication, just create an application, give it permissions and use the generated clientId/secretKey to execute any allowed request you have on your project DataBrowser module : This module allows developers to interact with the database in a visual mode And much more... The devtools : It helps developers to: Perform boring tasks like: Restarting the server, creating new modules... Translating server messages Exploring the controllers In a graphical mode Generating/synchronizing the Postman documentation and environment variables from the code Defining the projects settings using the settings editor To document their requests (The form of the body, the tests to be executed...) without leaving the code editor. Check an example here Navigate through the code by using the links generated in Postman: In the capture above, clicking the ok link will open for you the code of the ok function How we built it The code was built using NodeJS, Express, and MongoDB on the server. Postman API was used for synchronizing the documentation with Postman. Challenges we ran into Thanks to Postman API and the JSON schema , the task was a lot easier . Accomplishments that we're proud of Now, using IZMjs and the devtools: I can generate the documentation from the code I can synchronize my code with an existing Postman collection I can navigate through my code using the generated documentation What's next for IZMjs Devtools I am planning to: Migrate all the projects to typescript Enhance the devtools by adding more features like: Defining routes Data modeling Defining tests In a graphical way <div