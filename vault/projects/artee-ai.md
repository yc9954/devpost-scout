---
slug: "artee-ai"
url: "https://devpost.com/software/artee-ai"
title: "ARTEE.AI"
hackathon: "Global PyTorch Summer Hackathon"
organization: "Facebook"
winner: true
words: 1223
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ARTEE.AI

> Endless AI-Generated Tees

[Devpost](https://devpost.com/software/artee-ai) · hackathon [[Global PyTorch Summer Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[agriculture_food]] [[finance_payments]] [[immigration_refugee]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** google-cloud, javascript, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for artee.ai
- some extra url's

## Body

Me with some printed tees Designs list Preview and buy Design example StyleGAN examples Inspiration Creativity may be the ultimate moonshot for artificial intelligence. Already AI has helped write pop ballads, mimicked the styles of great painters and informed creative decisions in filmmaking. That’s no different than with AI and design. So while AI will replace designers, it will replace the designers of today, not the designers of tomorrow. AI will become a design partner and tool that designers can use to meet ever-evolving workplace demands. But what if we can create a product which will revolutionize the whole industry. For example the t-shirt industry, two hundred billion business, with $10 billion global market of custom printed tees. Modern users like "scroll" design - social nets, dating apps, etc. already provide you with endless content. So all you have to do is flip through and choose what you like. So we created an endless store of AI-generated t-shirt designs and integrated it with custom on-demand t-shirt printing service. What it does Endless store of AI-generated T-Shirt designs which can be purchased and delivered worldwide. Pytorch deep learning framework is used to built state-of-the-art generative model (StyleGAN), trained on modern art. Some additional customization is applied to expand user's experience: Caption generation Print borders generation Pixelation How I built it Generative model A high-quality generative model is the heart of our product. So we started with research in this direction. t is obvious that the quality will depend on two things - algorithm and data. As an algorithm we decided to use StyleGAN ( original NVIDIA's repo link ), since it generates high-resolution images (1024 x 1024) and it was proved that it works for different domains (tons of this[soemthing]doesnotexists sites). As a dataset, we used subset of wikiart styles and The Museum of Modern Art dataset . We have removed low-quality images, crop non-square images and it gave us a final dataset of about 40.000 images. T-Shirt printing Creating custom t-shirt printing manufactory is a big deal, so we started looking for someone who had already done it for us. The ideal candidate should have a simple integration, ideally some REST API, so we can send our design and get a printed t-shirt. There are several such companies, but for now we decided to use teemill.com because they have very high-quality printing, simple integration with API, worldwide delivery and they also do all payment/delivery process for us, so we don't need to collect and process any data from the customer. After this t-shirt is printed and delivered to the customer in a couple of weeks max. Extra customization Now we have some generated artwork, but it's not enough to print it on a t-shirt. We need to pre-process generated image to fit the teemill API format, generate previews, generate image captions. We also experimented with borders (we extract top-N most common colors from an image and add a border of the random size of color which is equal or contrastive to one of top colors). We also experimented with pixelation of the initial image. Website We used a poster store template from the website-builder tilda.cc . It does not support showing unique t-shirts each time (you should define all your goods on Tilda website), but Tilda allows us to run custom HTML/javascript on their side. So we get a list of unique designs from our API and show them on website. If a user wants to purchase a t-shirt we generate teemill.com page URL using our API and redirect. On Teemill page, user can specify all the necessary information and order t-shirt. Backend We use google cloud products as a backend for our store. We don't want to generate designs on the fly, because it is expensive to have GPU instance always up. Instead of this we pre-generate hundreds of thousands of designs with all required meta and store them on google cloud storage. Also, we have a google cloud firestore database with information about products. So we try not to show t-shirts which have already been ordered. f our database runs out we will just generate new designs. We have two API endpoints: get_products - returns the list of 12 t-shirts with all required meta get_product_url - generate URL for custom teemill product, so a user can order t-shirt Both endpoints use google cloud functions, so we have fully serverless and scalable architecture. Product Launch We launch our product on producthunt.com and collected 116 upvotes. This allowed us to be on the producthunt main page, which gives us several thousands of users next days after launch. We didn't run any bots or advertising campaigns, just called a couple of friends and then producthunt users upvote us. So it is a quite good result for such a product. Challenges I ran into Creating such a "algorithms" (from a technical point of view - site/backend/model) is quite simple if you know what to do. But it is much more difficult to launch the product: It should generate high-quality designs - pytorch model did it for us; It should produce results with great variability - again, pytorch model and large artwork database; It should be user-friendly - Tilda and teemill helps us; It should be stable and scalable - google cloud works well; We need to find some users - friends, and sites like producthunt can help to find first users. Accomplishments that I'm proud of In a few weeks we have created not another "This X Does Not Exist" or "AI Generated X", but real product which can already be used (and is being used by our customers) --- we have about 40 t-shirts ordered as for now (~10 by me and my friends, rest from producthunt users / other sources). We have about 4000 unique user sessions (from producthunt and other PR activities), so the purchase rate is about 1% which is quite OK for businesses like the fashion industry. We have some positive feedback: "This is the biggest disruptive product idea I have seen on ProdutHunt by far in the fashion industry. Way to go." "A cool and disruptive leveraging of the possibilities of the generative field. Really cool." "Great idea and a wonderful application of Deep Learning." What I learned From the production side, I learned a lot about deep learning deployment, distributed training, creating of serverless apps, site construction. I also learned how to launch a product. From the science side, I learned about generative models, caption models, training of GAN's. What's next for artee.ai We need to dive deep into social media for our product PR. It is useless to make a product that no one needs. We also have ideas about other design patterns for t-shirt product: Rectangle designs; Seamless borders; Full t-shirt prints; Texts on prints. Moreover, we have many ideas for other areas: posters, postcards, mugs, pillows --- there is tons of API's for custom products. On the other hand, we did a deep analysis of the t-shirt/fashion industry and we can collaborate with major manufacturers (like Nike or H&M) to create custom collections which will become popular. Some extra URL's artee.ai - main website github - github project page producthunt - producthunt project page teemill - teemill store page youtube - full demo video (from rules we have only 3 minutes limit for video) <div