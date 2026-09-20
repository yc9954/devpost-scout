---
slug: "live-coding-circle"
url: "https://devpost.com/software/live-coding-circle"
title: "LiveCoding Circles"
hackathon: "2018 Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 399
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# LiveCoding Circles

> Because everybody can learn to code, we provide a tool to reach it no matter where you are

[Devpost](https://devpost.com/software/live-coding-circle) · hackathon [[2018 Developer Circles Community Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** bot, css, customer-sdk, docker, facebook, heroku, html, javascript, messenger, nodjs, pty, ruby, socket.io

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what's next for live-coding-circle

## Body

Simultaneous And Screenshot Full Featured Console Inspiration Every communities has experts and people who want to learn code or improve their skills but they can't always can be in the same place, at the same time or dont have posibilities to pay for formal education, so we developed LiveCoding Circles as a tool to bring knowledge to people, building learning groups (circles) from different regions, places or realities expanding the reach of the developer circles. Today, the technology enable to many people to overcome economic difficulties, empowering them professionally, thanks to the internet and democratization of knowledge today is posible escape from a local reality into a new world of opportunities Programming skill provides us not only a technical tool but also it allowing us to integrate with the emerging technologies and move from being simple users to creators of solutions What it does LiveCode Circles provides a tool to take education anywhere, without having a high performance computer or a complex development environment, Just having an Internet connection you could practice and learn from tutors or study groups, being able to discuss ideas. Live Editor Full Featured Terminal And more features Root access on Terminal Multiple Languages support Full featured chat Copy & Paste support on terminal A docker container by snippet How I built it We build using Customer Chat SDK to develop the chat room experience into the live coding editor. Each snippet is supported by a Docker container, where the user could be free to use an full feature bash terminal We are spawning child process to provide a terminal thought a pty connection with the docker container. We made an small hack with Messenger Bot for act as a chat room manager. Challenges Use Customer Chat SDK (Beta) for first time. Provide a full feature terminal for run your snippets online. Find a new way to use Messenger Bot to connect people. Achieve a perfect code edition synchrony using websockets Build many of docker images for each language supported What's next for live-coding-circle Stream directly in a Facebook live video ( I couldn't finish this feature before the deadline :c ) Video & Audio streaming to improve the experience Show in the browsers the website result Record a session and publish the video in the site Multiple files support Snippets Collection Statical Analysis using linters Build IDEs plugins to provide this features too <div