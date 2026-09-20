---
slug: "promanage"
url: "https://devpost.com/software/promanage"
title: "Promanage"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 557
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Promanage

> Organizing all your projects efficiently and easing collaboration.

[Devpost](https://devpost.com/software/promanage) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** cli, express.js, firebase, firestore, gcp, heroku, node.js, postman, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for promanage

## Body

auth CLI Dashboard profile info project edit env Inspiration One of the most important things to take care of when working on coding projects is how efficiently we can manage the development cycles of the project. Most of us here have tons of projects that are not fully developed even though it has the potential to be big. Effective collaboration is another important attribute of a successful project. What it does Promanage is your one stop for managing all your projects no matter where you are. It allows you to have a portfolio-inspired interface to show you all your projects that you've worked on along with their current status. This way you can have a good overview of your current developer status. With seamless integration with github, it also allows you to import your project details from github without any hassle at all. Environment management, promanage, along with the help of promanage-cli helps you share your environment variables with your entire team without any issues. The setup allows you to maintain a global environment configuration per project, which you and your team can take help of by either downloading from the website or by running the the promanage get command using the cli. How we built it The application mainly consists of three sub applications: The website : We build the entire application setup mainly using javascript and only javascript. For the website, we used ReactJS for the frontend while hosting it on firebase-hosting. We implemented our authentication services via firebase via google and github providers. For styling and making our designs look good, we used material-ui for the styling. Backend : The backend is a NodeJS server using the express framework to handle the api requests to various endpoints. We used firestore for the database services, to maintain different configurations per user. We hosted this NodeJS server on the heroku cloud platform. Command line application : We created an interactive cli using nodeJS as a npm package which is globally available in the name of promanage-cli . We used third party libraries such as chalkJS and inquirer to make it interactive and visually pleasing for the users when using it. Challenges we ran into Authenticating users on the cli using google services connected to the same firebase project as the web. Accomplishments that we're proud of We managed to build a full stack application with a pretty decent looking frontend within a short period of time. It was also the first time we worked with a cli-based application so getting that to work and being able to publish it is an accomplishment on its own. What's next for Promanage Our vision for promanage is something bigger than what it currently is. We believe to morph promanage into that one spot where, developers all around come to, to visualize and analyze their projects, keep track of their tasks in each project, build a portfolio out of their projects and much more. One of the initial ideas, even though we didn't end up implementing was a drag and drop feature to generate starter codes for different tech stacks you work on (the ui for it is implemented in the codebase tab). We believe it would be useful in many ways and would help devs be more productive and focus more on the actual coding than managing projects. <div