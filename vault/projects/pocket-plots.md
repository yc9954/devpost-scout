---
slug: "pocket-plots"
url: "https://devpost.com/software/pocket-plots"
title: "Pocket Plots"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1176
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Pocket Plots

> Making land ownership accessible and affordable to all

[Devpost](https://devpost.com/software/pocket-plots) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[on_device_local]] [[simulation_digital_twin]]
**domain** [[climate_energy]] [[finance_payments]] [[legal_justice]] [[retail_commerce]] [[supply_logistics]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** checkbook, convex, gradio, huggingface, materialui, natural-language-processing, netlify, nltk, numpy, pandas, python, react, scikit-learn, tailwind

## How they structured the write-up

- 💡 inspiration
- ⚙️what it does
- 🛠️ how we built it
- 🤔 challenges we ran into
- 😎 accomplishments that we're proud of
- 🧠 what we learned
- 🔎 what's next for pocket plots

## Body

Logo 💡 Inspiration Generation Z is all about renting - buying land is simply out of our budgets. But the tides are changing: with Pocket Plots, an entirely new generation can unlock the power of land ownership without a budget. Traditional land ownership goes like this: you find a property, spend weeks negotiating a price, and secure a loan. Then, you have to pay out agents, contractors, utilities, and more. Next, you have to go through legal documents, processing, and more. All while you are shelling out tens to hundreds of thousands of dollars. Yuck. Pocket Plots handles all of that for you. We, as a future LLC, buy up large parcels of land, stacking over 10 acres per purchase. Under the company name, we automatically generate internal contracts that outline a customer's rights to a certain portion of the land, defined by 4 coordinate points on a map. Each parcel is now divided into individual plots ranging from 1,000 to 10,000 sq ft, and only one person can own a contract to each plot to the plot. This is what makes us fundamentally novel: we simulate land ownership without needing to physically create deeds for every person. This skips all the costs and legal details of creating deeds and gives everyone the opportunity to land ownership. These contracts are 99 years and infinitely renewable, so when it's time to sell, you'll have buyers flocking to buy from you first. You can try out our app here: https://warm-cendol-1db56b.netlify.app/ (AI features are available locally. Please check our Github repo for more.) ⚙️What it does Buy land like it's ebay: We aren't just a business: we're a platform. Our technology allows for fast transactions, instant legal document generation, and resale of properties like it's the world's first ebay land marketplace. We've not just a business. We've got what it takes to launch your next biggest investment. Pocket as a new financial asset class... In fintech, the last boom has been in blockchain. But after FTX and the bitcoin crash, cryptocurrency has been shaken up: blockchain is no longer the future of finance. Instead, the market is shifting into tangible assets, and at the forefront of this is land. However, land investments have been gatekept by the wealthy, leaving little opportunity for an entire generation That's where pocket comes in. By following our novel perpetual-lease model, we sell contracts to tangible buildable plots of land on our properties for pennies on the dollar. We buy the land, and you buy the contract. It's that simple. We take care of everything legal: the deeds, easements, taxes, logistics, and costs. No more expensive real estate agents, commissions, and hefty fees. With the power of Pocket, we give you land for just $99, no strings attached. With our resell marketplace, you can sell your land the exact same way we sell ours: on our very own website. We handle all logistics, from the legal forms to the system data - and give you 100% of the sell value, with no seller fees at all. We even will run ads for you, giving your investment free attention. So how much return does a Pocket Plot bring? Well, once a parcel sells out its plots, it's gone - whoever wants to buy land from that parcel has to buy from you. We've seen plots sell for 3x the original investment value in under one week. Now how insane is that? The tides are shifting, and Pocket is leading the way. ...powered by artificial intelligence Caption generation Pocket Plots scrapes data from sites like Landwatch to find plots of land available for purchase. Most land postings lack insightful descriptions of their plots, making it hard for users to find the exact type of land they want. With Pocket Plots , we transformed links into images, into helpful captions. Captions → Personalized recommendations These captions also inform the user's recommended plots and what parcels they might buy. Along with inputting preferences like desired price range or size of land, the user can submit a text description of what kind of land they want. For example, do they want a flat terrain or a lot of mountains? Do they want to be near a body of water? This description is compared with the generated captions to help pick the user's best match! Chatbot Minute Land can be confusing. All the legal confusion, the way we work, and how we make land so affordable makes our operations a mystery to many. That is why we developed a supplemental AI chatbot that has learned our system and can answer questions about how we operate. Pocket Plots offers a built-in chatbot service to automate question-answering for clients with questions about how the application works. Powered by openAI, our chat bot reads our community forums and uses previous questions to best help you. 🛠️ How we built it Our AI focused products (chatbot, caption generation, and recommendation system) run on Python, OpenAI products, and Huggingface transformers. We also used a conglomerate of other related libraries as needed. Our front-end was primarily built with Tailwind, MaterialUI, and React. For AI focused tasks, we also used Streamlit to speed up deployment. We run on Convex We spent a long time mastering Convex, and it was worth it. With Convex's powerful backend services, we did not need to spend infinite amounts of time developing it out, and instead, we could focus on making the most aesthetically pleasing UI possible. Checkbook makes payments easy and fast We are an e-commerce site for land and rely heavily on payments. While stripe and other platforms offer that capability, nothing compares to what Checkbook has allowed us to do: send invoices with just an email. Utilizing Checkbook's powerful API, we were able to integrate Checkbook into our system for safe and fast transactions, and down the line, we will use it to pay out our sellers without needing them to jump through stripe's 10 different hoops. 🤔 Challenges we ran into Our biggest challenge was synthesizing all of our individual features together into one cohesive project, with compatible front and back-end. Building a project that relied on so many different technologies was also pretty difficult, especially with regards to AI-based features. For example, we built a downstream task, where we had to both generate captions from images, and use those outputs to create a recommendation algorithm. 😎 Accomplishments that we're proud of We are proud of building several completely functional features for Pocket Plots . We're especially excited about our applications of AI, and how they make users' Pocket Plots experience more customizable and unique. 🧠 What we learned We learned a lot about combining different technologies and fusing our diverse skillsets with each other. We also learned a lot about using some of the hackathon's sponsor products, like Convex and OpenAI. 🔎 What's next for Pocket Plots We hope to expand Pocket Plots to have a real user base. We think our idea has real potential commercially. Supplemental AI features also provide a strong technological advantage. <div