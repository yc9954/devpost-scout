---
slug: "browserhelp"
url: "https://devpost.com/software/browserhelp"
title: "BrowserHelp"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 795
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "substrate/web_dom"
---

# BrowserHelp

> BrowserHelp allows full voice control of your Chrome Browser, making the web more accessible

[Devpost](https://devpost.com/software/browserhelp) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[voice_speech]]
**domain** [[accessibility]]
**substrate** [[web_dom]]

**stack** amazon-alexa, amazon-web-services, chrome, css, html, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- how do i get started
- supported phrases
- what's next for browserhelp

## Body

Install the Alexa skill and Chrome extension, login with Amazon, and you're good to go! BrowserHelp : Control your Chrome browser via voice interactions Inspiration A large part of our interaction with the world nowadays comes from surfing the web. This requires constant interaction with keyboard and mouse, posing a large problem for those who are not able to do this due to physical impairments or disabilities. BrowserHelp attempts to tackle this problem by offering an alternative, a natural voice interaction with your Amazon Echo device to give you complete control over your Chrome Browser What it does After installing the Alexa skill and companion Chrome extension, you can navigate the web and perform all of your basic browser interactions without having to lay a finger on your keyboard or mouse! Searching with Google, scrolling, tab management, navigating to arbitrary links on a page and moving through your history are some examples, but you can also set your preferred news site and up to 3 favourites for easy access How I built it BrowserHelp consists of three components: The BrowserHelp Alexa Skill, backed by a Node.JS Lambda function The BrowserHelp Chrome extension A NodeJS server, needed to: Form a bridge between the HTTP-based requests from Lambda functions, and the websocket connections needed by the Chrome extension Facilitate Login with Amazon when setting up the Chrome Extension User interaction and conversation flow is handled within the Lambda function, which uses Account Linking to identify different users. Actions to be performed are sent from Lambda function to the server via a secure connection, together with a hashed user identifier. The Chrome extension, once installed, uses Login With Amazon via the server to acquire and store the same hashed identifier. After this, server and extension establish a dedicated and secure socket.io channel for that hash through which all communication for that user runs. The extension then performs requested actions using a mix of Chrome APIs and injected content scripts. Challenges I ran into The only scalable way of keeping a Chrome extension in sync with the actions it needs to perform, is by using websockets and the Publisher-Subscriber (PubSub) pattern. This does not, however, work well with the stateless architecture of Lambda functions, which cannot keep a websocket connection alive. The most scalable way I could find was relaying all of the lambda function requests to a server, which creates dedicated websocket channels for users to which their Chrome extension can subscribe Free-form text input, as needed for searching any website or adding any input in a page, is still quite a challenge using Alexa. As a (hopefully) temporary solution, I decided to use the Web Speech API to interpret search queries Accomplishments that I'm proud of BrowserHelp is my first project going into production, and it's incredibly gratifying to finish a project and seeing it usable by people from all over the world Receiving incredibly positive feedback from multiple users during beta testing and while live, and hearing about ways in which BrowserHelp is used I couldn't have thought about before Despite Amazon's strict certification process, coming up with a unique use case for Alexa that's different from most Alexa skills which just stick to the voice-based interaction with your Echo How Do I Get Started Visit browserhelp.me to install the Alexa Skill and Chrome Extension. After installing the skill, enable Account Linking for that skill via either the Alexa app on your phone or the Alexa web app. When you've installed the companion Chrome Extension, Alexa BrowserHelp , you will be prompted to login via Login With Amazon. Log in using the same account details as used for installing the Alexa Skill. Once this is complete, a message will appear telling you you can now close the tab and start using the skill, or setup your favourite websites and news site via the options page You are now ready to start using the skill by saying "Alexa, start BrowserHelp". Alternatively, try "Alexa, ask Browserhelp to scroll down" or one of the other supported phrases listed below. Supported Phrases Try some of the following sample utterances: Search with Google Show News Highlight links Open Link {x} Remove highlighting Open favourite {1/2/3} Help Navigate {back/forward} Scroll {up/down} {Open/close} tab Press Enter Reload page Open {Youtube/Google/Facebook/Twitter/Hacker News} What's Next for BrowserHelp Offer custom integration and specific voice commands for large platforms such as Youtube or Facebook Inject Web Speech API for filling in any form and search box on the page, in the same way as currently done for highlighting and selecting links Extend commands. Commands present in the next version include: Dictate Page List Bookmarks Open Bookmark {x} Log In Press {Tab/Backspace/Spacebar/Up/Down/Left/Right} Use Input {1/2/3} Setting a single or repeated timer for any of the existing commands <div