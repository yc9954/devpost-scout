---
slug: "amethyst-wy3mjf"
url: "https://devpost.com/software/amethyst-wy3mjf"
title: "Amethyst"
hackathon: "Kore.ai Botathon"
organization: "Kore.ai"
winner: true
words: 1035
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Amethyst

> Don't let anyone to Dull your Sparkle

[Devpost](https://devpost.com/software/amethyst-wy3mjf) · hackathon [[Kore.ai Botathon]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]]
**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** api, bootstrap, html5, kore.ai, mock-response, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for amethyst

## Body

Flow of Amethyst Inspiration The thing that inspired us to choose the e-commerce domain was that, personally, I struggled a lot while talking to the chatbots. In terms of e-commerce bots, it just answers the very basic questions, and we can't get to talk to the bot like a normal conversation. Most of them are not user-friendly. The e-commerce bot frequently ** fails to allow us to shop for products** as we do in the applications. The problem that screwed up the user was that he or she couldn't able to shop the products and couldn't add the products to their cart to shop later in their virtual assistants . What it does So, we came up with the concept with the additional features—the virtual assistant named Amethyst—as a solution. It is an e-commerce bot that mainly relies on the area of personal care, and we created a brand called "Amethyst," which is a brand composed of skin care products and hair care products. We usually propose that if the user logged in to his or her account, he or she would see the following features, and we used an existing database. So the login credentials are listed below. Login credentials: 1:- Username: noah01 Password:12345678 email/gmail: noahhwilliams01@gmail.com Login credentials: 2:- username: aahana08 Password:12345678 email/gmail: aahanadesai03@gmail.com My Orders In "My Orders," it'll be subdivided into the categories of "check order status" and "go to cart." On the check order status page, it'll encounter the authentication of the user, so we don't have to login again and again in the same session. For example, if the username Noah01 logs into the account, he will see the order status of any current or previous orders in the database of his account, which is accessible via the mock API, and if the user gets into the "Go To Cart" button, he'll see the products that he added to the cart, or if the cart is empty, it will return that the cart is empty and redirect to the main menu. Shop Products In "Shop Products," it'll list the products that are available under the brand Amethyst. It includes skin care products and hair care products containing amethyst. If the user navigates the above-mentioned menu, he'll encounter the "buy now" and "add to cart" options. If the user clicks on the "Buy Now" menu, it'll ask for a payment method consisting of COD and UPI . He can choose his payment methods. and the shipping address, mobile number, and order details are fetched and stored in the mock API. If the user buys something, it'll be reflected in my orders. If the user clicks "Add to Cart," the product is added to the cart and he redirected to the cart, where we can buy the product in the cart or remove the product from the cart . Ordered Queries In the ordered queries, we can get help for the order-related queries, and it'll be subdivided into 3 options to choose from, including Cancel Order, Re-Order, and Return Order . We can cancel the order that was placed in the cancel order task, and we can reorder the items we brought in the reorder task. We can get the refund amount in the return order, or we can exchange an order for that amount, which is all reflected in the database. Non-Ordered Queries The non-ordered queries are there to help with the non-order-related queries. It will include the following options: Zipcode Availablity If the user enters a zip code like 600040, 30174, or 10003, it'll return the city and show whether we can ship to that city or not. Cart directs to the user's cart. Customized Products In the customized product, it'll consist of the skin care analysis and the hair care analysis. In the skin care analysis, it'll consist of a skin care quiz, and with that quiz, he or she will get customized skincare products. in the skin care analysis It'll consist of a skin care quiz, and with that quiz, he or she will get the customized products for hair care. After Buying the product the user will receive the mail regarding the order How we built it We built this VA on the Kore.ai XO platform, which provided us with a great interface for new users, and we use the built-in API for login and Zipcode availability, with the cart and order details being updated in the system. It can be found at the API URLs listed below: link link link link link link The email was sent to the responding users' emails using Node.js , which was hosted. Challenges we ran into The difficulty we encountered was that we couldn't complete the cart on the dialogue task, which included removing items from the cart and buying products from the cart, which was so challenging to provide both functionalities in the same dialog, but we overcame it with better solutions. They, like all other existing ecommerce bots, do not have the ability to add or remove items from the cart, but our bot can do that, and it'll do all the functionalities that were mentioned above, including the zipcode check. Accomplishments that we're proud of We established the cart in the bot which is Reflective in the Database. Accomplished the zipcode availability. We can track and check the status of orders. we can Re-order, Cancel order and Return order. Customizing Products for Users. Shopping Products. What we learned We learned how to interact with virtual assistants and how they function outside of the user interface. We learned about how to integrate APIs and learned about Node.js. includes entity extraction as well as, -Machine Learning (ML) -Fundamental Meaning (FM) -Knowledge Collection/ Knowledge Graph (KG) -optimizing intent recognition and training ML engines What's next for Amethyst The scope of amethyst is to set up a membership check for all the users and invoke the stock details in the upcoming session. We are also trying to establish the AWS server domain to store the image on the server and integrate the machine learning algorithms, which really work in real-time, to obtain the skin and hair ages in real-time. The web enabled version of bot can be found here: https://amethyst.drcstudio.co.in/ <div