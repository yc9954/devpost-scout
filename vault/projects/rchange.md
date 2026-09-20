---
slug: "rchange"
url: "https://devpost.com/software/rchange"
title: "Rchange"
hackathon: "Hack the North 2019"
winner: true
words: 397
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/video_visual"
---

# Rchange

> AR Currency Converter

[Devpost](https://devpost.com/software/rchange) · hackathon [[Hack the North 2019]]

## Facets

**substrate** [[video_visual]]

**stack** dart, flask, flutter, python, xe

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for rchange

## Body

Inspiration Many travelers struggle with the currency change when they are in a country of different currency. It is especially visible in Europe where eastern europeans, with their own currencies, travel to west, where the main currency is Euro. The see the bunch of numbers on the menu of the shop or restaurant, and they try to convert it into their own currency to have a better view point about how much they are spending, but they cannot calculate each and every calculation of conversion in their respective minds or cannot just search each one of them on the internet. We as a team come up with a solution to this. What it does Rchange, is an AR based mobile application with which you just have to point your camera towards the restaurant’s menu and boom! The currency is converted into the one of your choice, not only one number, but all the prices which were on the camera are pointed to the currency of your choice. How we built it We built the AR based mobile application using Flutter because it enabled us to make a beautiful UI in a short time. Furthermore, Flutter enables us to make the app available on multiple platforms in the future. Designing was done in Figma, because of its amazing workflow and team libraries. We used the XE CD api to list and convert all currencies. Backend was written using Python and Flask. To get the latest currency values to convert we used XECD Client which provides a simple Pip library . Challenges we ran into The hardest part was making the AR work. Finding and parsing text in a still image is fairly easy thanks to the abundance of tools for this. Find and parsing text live in a viewfinder is a lot harder. We were able to find a way to do this using Firebase ML Vision offline OC.. What we learned It was the first time working with AR. We learned how to use AR in flutter and used a relatively low level custompainter API to draw the overlay. What's next for Rchange We’d like to leverage the XE API’s historical data as well as prices analysed by Rchange in order to provide an API that allows users to: Predict price fluctuation in specific locations To get acquainted with local prices for products or services offered <div