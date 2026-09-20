---
slug: "sustainable-ethical-shopping-extension"
url: "https://devpost.com/software/sustainable-ethical-shopping-extension"
title: "Wonderful Stew"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 654
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/climate_energy"
  - "domain/retail_commerce"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Wonderful Stew

> A web extension which reviews items in your shopping cart and recommends more ethical and sustainable options.

[Devpost](https://devpost.com/software/sustainable-ethical-shopping-extension) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[climate_energy]] [[retail_commerce]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** chrome, cloud, css, extension, firebase, firestore, google, html5, javascript, react, webpac

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wonderful stew

## Body

Initial prototype After further development Inspiration Wonderful Stew was inspired by personal interest in having a tool to help find the most sustainable and ethical product available on a given ecommerce site. What it does Figma: Using Figma and its Smart Animate function, we designed a clean and effective user interface for a Wonderful Stew extension and external website. The extension itself displays a product from your shopping cart, its ethical/sustainable rating, and a better alternative. It conveys only the most important information and makes use of text blocking to emphasize sustainable alternatives. The ‘Learn more’ button links to our website, which contains additional information about our metrics and sources. Both the extension and website employ carousel functionality to display pertinent information per product. Extension: In its current state, the extension displays a basic example of what might be in a user’s cart if the extension was fully connected to a web scraping service. This is accomplished using a couple of React components that use static resources already in the repo. An example ethicality rating and picture is displayed, which would be obtained from our Firstore database once it was coupled to our user interface. A substitute product’s data would also be obtained from the database and displayed on a card below, which a sample of is displayed in green. Website: When you click the learn more button through the extension, it would lead the user to a webpage with further information comparing the two products. The products would be compared with variables such as ethical rating, amount of emissions, etc. This website will source data through the Firebase database, which grabbed information from ethicalconsumer.org. Database: To create our database of information, we employed the use of Google Firebase, specifically Cloud Firestore. This is an extremely helpful space to build a scalable database across devices. The format of the database contains two main components: the collection and the document. The Collection is a broad category which contains all of the relevant documents. Using these you can build an ever-growing tree of entries into your database. For our project, we wanted to store relevant information for various products which could be pulled and used in our extension when the customer is checking out. So, we began drawing the tree to our specific product. Knowing that our database would contain MANY more products of varying types, we made sure to lay out an organized pathway starting with the broadest category: food. Then, we worked our way through different sub categories, making our branch more specific, until we landed at our product. An important thing to note is that as we move through the tree, we ALWAYS alternate between collection and document. How we built it To build the extension interface, we used webpack and React, as well as Chrome extension boilerplate we found on GitHub. To build the website, we used Github pages and some HTML and CSS. To build the database, we created a new Firestore project and manually entered the collections, documents, and fields. Challenges we ran into Working with new technologies, React components & containers are relatively new frameworks to learn. Accomplishments that we're proud of For many of us, this was our first Hackathon, so we are proud to have created a project surrounding an idea that we are passionate about and feel that has real world applications. Beyond learning to collaborate virtually, we are proud to have practiced new technologies and pieced together pieces to form a basic iteration of our project. What we learned Everything :) The whole hackathon was a learning process :) What's next for Wonderful Stew Carousel interface Connection to Firestore database Web scraping to populate database automatically Web scraping to read data in user’s cart Expand our tree, and even add a new base category like clothing Add web scraping capabilities in the future so that our database can be self-sustaining, and be expanded exponentially <div