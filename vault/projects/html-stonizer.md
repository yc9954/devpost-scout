---
slug: "html-stonizer"
url: "https://devpost.com/software/html-stonizer"
title: "HTML stonizer - carve information in stone"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 515
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# HTML stonizer - carve information in stone

> Carve important financial data, predictions, or quotes in stone. The API notarizes HMTL fragments in the Blockchain so that you can prove that an information was available at a specific point in time.

[Devpost](https://devpost.com/software/html-stonizer) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[media_journalism]]
**substrate** [[financial_record]] [[web_dom]]

**stack** algo-sdk, algorand, amazon-web-services, nestjs, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges i ran into
- accomplishments that we're proud of
- what we learned
- what's next for html stonizer

## Body

Inspiration Liars, misappropriations, and fake news everywhere! The Web will surely be a better place without them. You can debunk and do fact checking on top news, but what guarantees other contents around the web? We are tired of accessing information over the internet without anchors. Anybody can write something and then modify the content: Who can guarantee that a financial report was not modified since its publication? What can assure that a prediction of the Bitcoin trend was not tampered? How can we verify that someone had an idea before someone else? What it does The HTML stonizer API downloads a static webpage, and notarizes the requested fragment of HTML in the Algorand blockchain so that it will be immutable forever. The API returns a code (the ID of the blockchain transaction) that can be inserted in the webpage to mark it. Another endpoint is able to look for marks in a page and verify the content against the blockchain. The verification API will answer to the following questions: Is some fragment of this page stonized ? Has the fragment been modified? When was it first notarized? How we built it We built the API in Node using the NestJS framework and the library algo-sdk to interact with the Algorand Blockchain. Scraping and analysis of pages are powered by Puppeteer, Axios and Cheerios (for dynamic exploration of pages with a jQuery-like API). The whole application is dockerized and a simple Terraform script is provided to allow the installation on an AWS EC2 instance. Challenges I ran into During the development we discovered many difficulties in scraping the page, since many websites are dynamically loaded. We chose to use cheerios to manipulate the pages and the nodes after the download. Since the API was containerized and Puppeteer needed to use the Headless Chrome core to scrape the web pages correctly, we also experienced difficulties to put the whole set of required libraries into the container: We found the correct set of dependencies by using old documentation and via a trial and error approach. Accomplishments that we're proud of We are proud to put a step further in making the web a safer place. What we learned We improved our knowledge about Algorand permissionless Blockchain. Furthermore we learned how to reduce the friction in the usage and testing of the API by means of a Chrome Extension (published on the chrome extension store). What's next for HTML stonizer We envision several cool features that we will make the API more and more useful: Possibility to overcome the limitation of notarization payload size (1Kb), e.g. by using hashing techniques Add the possibility to delegate the authorization to the API in order to notarize private pages (e.g. enterprise websites with trade secrets or other private pages with sensible data) Possibility to discover similarities in a webpage (fingerprinting) to create plagiarism detectors Plugins for popular CMS (e.g. Wordpress, Joomla, Drupal) so that content creators can notarize a fragment of a post directly through the editor Add notarization to the Chrome extension UI (html-stonizer-chrome-extension) Create extensions for other browsers <div