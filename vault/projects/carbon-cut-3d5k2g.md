---
slug: "carbon-cut-3d5k2g"
url: "https://devpost.com/software/carbon-cut-3d5k2g"
title: "Carbon Cut"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1155
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Carbon Cut

> Your one-stop shop for climate action and impact.

[Devpost](https://devpost.com/software/carbon-cut-3d5k2g) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
**domain** [[climate_energy]] [[finance_payments]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chroma, css, fast-api, git, github, google-cloud, google-maps, html, javascript, nextjs, openai, python, react, render

## How they structured the write-up

- 🌟 inspiration
- 💡 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for carbon cut

## Body

Main dashboard for the User to check how their carbon emission is Carbon Footprint calculator for individual Link takes to RAG model of planet where you can interact and understand better how you impact the planet RAG model of the Planet Real Feedback and Pain Points from different users when we discussed our idea Item checker uses tag image or barcode number to give us information about how carbon efficient is the product Check how sustainable is your item and provide recommendations to do better Calculate carbon credit awarded to each user on decreasing their carbon emission. Search bar to find restaurants which are eco-friendly and sustainable Sustainable restaurant search based on the location typed. Providing transportation options and how using the one which is sustainable and not time consuming would be helpful. Carbon cut: Your one-stop shop for climate action and impact. 🌟 Inspiration Studies show that many people know about climate change and sustainable behaviors, but not as many people adjust their actions accordingly. This is largely due to inconvenience and the perception of no environmental impact. People know that climate change is bad, but they don’t know where to start. We want to bridge the gap between knowledge and action, making it easy for people to foster sustainable behaviors in their everyday lives. 💡 What it does Our website, Carbon Cut, assesses a person’s carbon footprint and offers personalized recommendations on how to make the most impact with the least effort. We want to emphasize that individuals are NOT the problem, but they CAN be part of the solution . By taking the effort of research out of their hands and quantifying their impact, Carbon Cut answers users’ two most prevalent pain points. We also have established the groundwork to implement credits, rewarding users for their sustainable choices. They will be able to use these credits for discounts on partner brands, such as (ideally!) Cotopaxi, Patagonia, Reformation, and other sustainable brands. These environmental features are: Item checker: You can upload a photo from the tag that contains the details of any product (mostly clothes) and it will assign a grade to your item based on the carbon impact it has. Sustainable Restaurants : You can input any location you want, and it will display you a map with the most sustainable restaurants near you in a map, with their name and location Transportation Tracker : Just select the origin and destination of your travel and it will display you the most sustainable solution to arrive at that place Furthermore, in order to create more consciousness about the environment, we have a chatbot in which you can "talk" to some of the priority places of the planet, such as the Amazon Rainforest, Northern Great Plains, the Coral Triangle, among others. You can ask whatever you want to these places as if they were a person 🛠️ How we built it In the creation of Carbon Cut, we began with research and brainstorming. Literature showed that high prices, perception of no environmental impact, greenwashing, inconvenience, and social image were among the biggest barriers to sustainable action. Thus, we established features to address many of these challenges and sought out feedback from other hackers (Doc link posted with all feedback and iterations). The resounding consensus of the 8 hackers we surveyed was that inconvenience and perception of no environmental impact were the two most prevalent barriers to action. With that reassurance in mind, we tailored our website to emphasize impact and optimize convenience. From a technical perspective, the front end was made using HTML, CSS, and Next.Js. The backend was made by creating an API using FastAPI. The Item Checker was made using Computer Vision (Optical Character Recognition) and a custom few-shot LLM built on gpt-3 The Restaurants feature was made using Google Places API The Routes feature was made using Google Routes API The Planet LLM is a Retrieval Augmented Generative Model trained with data from WWF, using a Vector Database from Chroma with dozens of documents 🚧 Challenges we ran into All's well that ends well. With that being said, no hackathon is complete without its challenges. We had 2 main challenges. Firstly, we had some issues when deploying our Chroma Vector Database, due to different dependencies and it being too heavy to be deployed on Render, so we used Google App Engine for the RAG model. Secondly, we also had some issues when deploying the image-to-text model, since we used Pytesseract and the model needed to install a file on our computer, which couldn't be done in the deployed instance, hence we had to change the way we identified the text in any image. 🏆 Accomplishments that we're proud of We are proud of our team. Coming from universities in Pennsylvania, Florida, and Mexico, we formed our team on Slack and met at the TreeHacks orientation. From that moment on, we maintained open communication, kept a strong work ethic, and shared many laughs. We are also proud of the progress we have made on Carbon Cut in 36 hours and the potential it holds to shape the lives of many people. One hacker, who preferred to remain anonymous, said of Carbon Cut, "When you see carbon footprint used in marketing it's always very condemning. It’s nice to see something focused on action." Another noted, in our first round of user pain point research, that inconvenience was one of their major barriers and that they would use a website such as Carbon Cut, "especially if it showed me how much impact it would have." Thanks to our multi-disciplinary team and the thoughtful responses of our fellow hackers, Carbon Cut now features a dashboard that quantifies impact in a variety of ways, from percent change to trees planted to Olympic-sized swimming pools of water saved. Through the use of social math, we are proud that Carbon Cut can be used, understood, and enjoyed by a wide range of users. 📚 What we learned This project was an exercise in all of our skills, including our ability to learn! We tackled Carbon Cut with an army of old and new skills, and even some that we learned at the various TreeHacks workshops. From Next.js to RAG Models to generative UI (shoutout to Guillermo Rauch from Vercel!), this weekend was nothing short of an exercise in experiential learning. 🔮 What's next for Carbon Cut Next up for Carbon Cut is increased precision carbon tracking, partnerships, and credits. We hope to continually improve our carbon emissions tracking and keep personalized recommendations modern and up-to-date with current technologies. Additionally, we plan to establish credits to reward users for choosing sustainable alternatives. These credits will be redeemable for discounts towards partnered sustainable brands, such as Cotopaxi and Patagonia. Lastly, as always, Carbon Cut is here to help you . If you have any requests or ideas on how to improve Carbon Cut, please don't hesitate to reach out! <div