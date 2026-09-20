---
slug: "snap-cart"
url: "https://devpost.com/software/snap-cart"
title: "Snap Cart"
hackathon: "Square + Google AI Hackathon"
organization: "Square"
winner: true
words: 634
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/small_business"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Snap Cart

> A quick and cost effective POS solution for small businesses

[Devpost](https://devpost.com/software/snap-cart) · hackathon [[Square - Google AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]] [[supply_logistics]]
**user** [[small_business]]
**substrate** [[video_visual]] [[web_dom]]

**stack** cloud-run, inventoryapi, javascript, mongodb, paymentsapi, react, tensorflow.js, vertexai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snap cart

## Body

Upload Images to train Using Snap Cart Inspiration Snap Cart was born out of a desire to share the innovative shopping experience pioneered by Amazon Go Stores. Amazon Go's checkout-free technology has set a new standard for convenience and efficiency in the world of retail. Our aim is to provide small businesses with a quick and cost effective solution that streamlines setup time and enhances customer experience. Snap Cart can even help ease the challenges associated with labeling handmade items that are not barcode-friendly. We were inspired by the idea of transforming the way people shop, making it seamless and accessible to small businesses in our communities. We wanted to offer them a competitive edge against larger retail chains and e-commerce giants by providing an affordable, user-friendly platform that integrates cutting-edge technology. What it does Cutting-Edge Technology: Snap Cart leverages Square APIs and AutoML with Google’s Vertex AI API, combining the power of cloud-based payment processing and advanced image classification technology. This synergy allows customers to shop effortlessly while enabling store owners to streamline their operations. Easy Product Training: Snap Cart offers an intuitive interface for store owners to train their own AI model to fit their business. Using a user-friendly dashboard, retailers can upload product images and provide price information, making the system well-prepared to recognize all of a business’ products. Seamless Customer Experience: Customers simply need to show a product to the camera, and press “add to cart” once the AI recognizes it. Snap Cart's intelligent image recognition technology identifies the product almost instantly, streamlining the checkout process and eliminating the need for barcode scanning or manual input. Inventory Management: Snap Cart provides a real-time inventory tracking system, enabling store owners to monitor stock levels efficiently. When an item is recognized at the checkout, the system automatically updates inventory records, ensuring that stores can restock and manage their inventory with ease. How we built it We constructed a brand new web application using a MERN stack. We utilize Square’s Catalog and Inventory APIs to allow for automatic inventory management and the Payments API to handle card payments. We leveraged Google Vertex AI APIs to streamline the setup and training of each model and Tensorflow.js to classify images on the browser for decreased latency. We used Tailwind CSS to create the UI for our application. Set up CI/CD with Google Cloud Run using Docker to containerize each service. Challenges we ran into Request timeouts were a big problem that we found fairly late into development. Cloud Run only allows requests to take up to 1hr before timing out and training the model usually takes around 2 hours. To solve this, we needed to utilize request polling to make sure that the model is exported after it is trained. It was difficult to create a UI that looked nice and was also responsive. Dealing with the camera layout was difficult as it didn’t seem to play nice with Tailwind. Accomplishments that we're proud of This is the first time that we have all worked on an end-to-end web application together. It can cost small businesses valuable money to create barcodes for their products, so we are very happy to be able to provide a simple and easy alternative. Successfully utilizing Google AI and Square API for the first time, our team achieved a valuable and enriching learning experience. What we learned We learned essential collaboration skills and time management Gained important skills with popular technologies What's next for Snap Cart Have the product automatically be added to the cart when recognized by the AI Currently to view a store’s inventory, you need to go into the seller dashboard on Square’s website. We would like to implement our own version of that so that the seller doesn’t need to navigate away from the page. <div