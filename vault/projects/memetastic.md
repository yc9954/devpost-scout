---
slug: "memetastic"
url: "https://devpost.com/software/memetastic"
title: "MemeTastic"
hackathon: "Elastic Weekend with Code for Cause"
organization: "Code for Cause"
winner: true
words: 1270
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# MemeTastic

> Summon and Search Dank Memes Anywhere and Anytime!

[Devpost](https://devpost.com/software/memetastic) · hackathon [[Elastic Weekend with Code for Cause]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[general_public]]
**substrate** [[code_repository]] [[document_pdf]] [[web_dom]]

**stack** android, axios, dart, elasticsearch, flutter, github-actions, google-cloud, javascript, kibana, ngrams, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for memetastic

## Body

Major App Screens All App Screens (2 /2) All App Screens (1 / 2) Inspiration It all started with an urge to build a full-stack application without using firebase + firestore and after exploring elasticsearch and kibana I knew that I can scrape some data and store it in the cloud-hosted elasticsearch which can then be used for a variety of purposes. Finally, I decided on scrapping memes (because everyone loves them) and discovered that the Reddit API is public, started experimenting with node.js , and voila I succeeded. It took the rest of the day and a sleepless night for me to figure out how to ingest that data into elasticsearch , first by hosting it locally and then into the cloud, and then the next one and a half day to build the frontend for which I chose Flutter because one, I was already familiar with it, two, it gives better looking and faster (as in building the application) results than the native android code using kotlin and three, I have almost 0 experience with react-native . What it does The Flutter application summons a random meme from the top 100 memes on the memes subreddit. The backend uses elasticsearch to achieve this and then the frontend displays it with a clean UI. A user can also search for any meme using any string , given that I have implemented the ngram analyzer, the user will automatically be prompted with various suggestions on the basis of the string they enter. Finally, the user can also share these memes with anyone. How I built it The project is divided into three major parts (hence, two GitHub repositories and elasticsearch running on Google Cloud). The Backend The backend is written with node.js and javascript (uses axios and elasticsearch packages) and it runs every thirty minutes using a CI/CD pipeline created on GitHub Actions . Every thirty minutes, it scraps the URL and the title of the top 100 memes from the memes subreddit using the public Reddit API and ingests this data into elasticsearch which can then be confirmed and visualized using kibana . This keeps the frontend application always up-to-date with the popular memes to keep the user engaged. The Frontend The frontend is written with dart and flutter that provides a smooth, minimalistic UI and a great UX. It pulls in the top 50 memes (to make the process quick) from elasticsearch every time the user clicks next and then randomly chooses one meme to display, which can also be shared anywhere. The user is first welcomed with a welcome screen and can then generate memes by clicking the next button, there are proper arrangements to address any errors in the process of loading search results or loading memes. For the search, a user can type in any string and all the results containing that string will be listed out (this is achieved by using ngrams in elasticsearch and was set up using kibana ). Clicking on any of the results redirects the user to the home screen and loads up that particular meme! Everything in the frontend is production-ready, be it the splash screen, the app icon, app name, or the main drawer, and has been released on my GitHub . Elasticsearch This has been hosted on the Google Cloud and while most of the working is done using my backend (which can be visualized using kibana ), the ngrams were set up directly from kibana using the documentation. Challenges I ran into I had no team and had to work with the backend and frontend simultaneously. Apparently there are very few resources on elasticsearch with flutter and absolutely 0 official documents, most of the StackOverflow questions are also answered incorrectly and I had to go deep in the web to read small articles and had to try things on my own. I used a third-party flutter package called elastic_client which had no documentation, their documentation consisted only of a few examples for specific cases, I had to read the code of that package to figure out how to get it working. Implementing the search functionality using ngrams in Flutter was even tougher because of no resources. This was my first project where I built the backend (I am not well versed with the backend), as well as the frontend. Building everything with the time limit was another task, I finished with the code a few hours before the deadline. One of the reasons for this is my ongoing classes which go on for almost the whole day to cover up the second semester's syllabus and the extra assignments, because our batch entered the first year late (pandemic), the other two reasons being no teammates and Google Summer of Code community bonding time. Honestly, I am good with building the frontend functionalities but not good with designing the UI and UX, through this hack I learned a lot about designing too. Working with node.js and javascript was also tough because I am a newbie with the MERN stack. While working I also realized that some of the code written in the documentation was not working (I might open an issue and PR for the same but I might be wrong) and hence had to try some code and some StackOverflow answers on my own. And finally, learning the ELK stack in such a short time was a big task in itself. Accomplishments that I'm proud of I am really proud that I learned and used an industry-level product (the ELK stack) and integrated it into my application in a very short time. Writing all the code in a very short amount of time. Succesfully entering into my first Hackathon with a good project. Getting familiar with and writing backend code as well as improving my understanding of GitHub Actions . Designing something (the UI and the UX) for the first time in my life. Building a production-ready full-stack application with such a powerful tech stack (which is ready to be published on the play store and will be available for the apple app store with a few minor tweaks). Testing out my code thoroughly (only manually) and looking for all the edge cases. And finally, reading a lot of documentation and coming up with ideas of improving them or adding the missing documentation. What I learned I learned a lot of new stuff, listing them below - How to work with node.js and javascript . Using ELK stack. Using ELK stack with Flutter . Reading the source code and a lot of documentation for Flutter packages. Designing smooth and minimal UI. Building a user-centered UX and taking care of every possible edge condition which might result in an error. How to successfully deploy the backend using GitHub Actions and then integrating it together with the frontend. A lot of YAML and JSON syntax. What's next for MemeTastic Adding more features like browsing memes through categories, dark mode, more searching options will be my top priorities. I will most probably also enter this as a project in small open-source programs to let beginners learn about Flutter + ELK + node.js together. And finally, I will be releasing this to the play store so that everyone can enjoy some good memes with a single click. Note: I will be entering this as a DevOps project too because I used a CI/CD tool ( GitHub Actions ). I am a complete beginner in DevOps and I hope that if this can't be considered a DevOps project it won't cause any other issue except being disqualified from that particular space. <div