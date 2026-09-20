---
slug: "birdbot-computer-vision-that-enables-citizen-science"
url: "https://devpost.com/software/birdbot-computer-vision-that-enables-citizen-science"
title: "BirdBot - Computer Vision That Enables Citizen Science"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1281
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# BirdBot - Computer Vision That Enables Citizen Science

> BirdBot is an avian wildlife camera that helps environmentally conscious professionals contribute to science using the power of artificial intelligence.

[Devpost](https://devpost.com/software/birdbot-computer-vision-that-enables-citizen-science) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[finance_payments]]
**user** [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** adaptive-cards, adaptive-expression, bot-framework, composer, custom-vision, luis, power-automate

## How they structured the write-up

- inspiration
- what is birdbot?
- how we built birdbot
- challenges we ran into
- our current accomplishments
- what we learned

## Body

Bird Species Randomizer - Horned Grebe Bird Species Randomizer - Black-Bellied Plover Bird Species Randomizer - Canvasback Bird Species Identification - European Starling - TensorFlow Lite Bird Species Identification - Blackcapped Chickadee - TensorFlow Lite Inspiration The founder of BirdBot, Tyler Odenthal, developed the idea when asking his mom about potential AI projects. After pitching a couple of failed ideas, his mother eventually asked. "Can you make me an AI that tells me about the birds at my bird feeder?" After some extensive research, Tyler realized that trail and bird cameras use very outdated technology. Knowing an AI bird camera was possible, he assembled a team of AI experts and ornithology advisors. In late 2020, they started working diligently towards an AI camera that can monitor and teach people about birds. You can find more information on the project here at Bird.Bot | Bird.Bot/AiModel What is BirdBot? BirdBot is a machine learning product (e.g., IoT & chatbot) that helps environmentally conscious professionals contribute to science using the power of artificial intelligence. Wildlife research and conservation rely heavily on data collection. Citizen scientists have played a huge role in data set aggregation throughout history. The issue with citizen science is consistency. If there is no human to monitor a location, that animal population goes unnoticed. BirdBot uses AI to capture bird metrics that a human might otherwise miss if they are not around. Some of these features being general bird species, presence and absence data, on-screen bird count, predator detection, and more. These features allow environmentally conscious people to create wildlife camera networks that they can actively monitor. This data may prove critical for ornithology research and wildlife research in general as the network and dataset grow. Mary Ellen Hannibal , once said, "Science needs more eyes, ears, and perspectives than any scientist possesses." Technology allows for the expansion of that scientific potential. It is up to those who invent these technologies to give real definitions and true incentives for their use. At BirdBot we believe that our team can help solve the conservation incentive problem through the use of well-defined goals and emerging technologies such as AI and blockchain. Our planet is currently experiencing the Sixth Mass Extinction, as published by the National Academy of Science and many others. This extinction event is called the Holocene Extinction and it is due to how humans live on this planet. This isn't a problem that one person can solve, and it will take effort from everyone. If more people are incentivized to care, learn and protect the wildlife around them. I believe we can help promote a culture of conservation and help save this planet. How We Built BirdBot Python Scripts We built BirdBot by leveraging Python to scrape images of birds from Google. Then we designed a TensorFlow model to clean the datasets for only bird photos and sorted them by species. This method, in combination with pre-existing datasets; allowed us to build a highly accurate object detection model for bird species identification. Microsoft Custom Vision AI After collecting the photo dataset and cleaning it, we were able to upload the bird photos to Microsoft Custom Vision AI. Each iteration we would add more bird species to the custom vision AI data set. After various iterations we have achieved accuracy across 30 different bird species. Now that we have a model with a significate amount of accuracy and tags, we can work on the bot portion of BirdBot. CustomVision.AI - Photo: Custom Vision AI Prediction Dashboard Microsoft Composer and Bot Framework For the bot portion of the project our team leveraged Microsoft Composer and Bot Framework. Composer made developing a bot in the Microsoft ecosystem exceptionally easier. As we are able to spend less time figuring out coding / syntax and more time on developing the architecture of the bot. This allowed our team to make and integrate various features such as a routing menu, adaptive cards, natural language processing (LUIS) and the integrations with Microsoft Custom Vision AI. We are able to leverage the Custom Vision AI model that we created to analyze photos being sent to an Azure Bot Service, such as BirdBot. Through the Composer Trigger below, we are able to detect when a user sends a photo to the bot and route that message to the Custom Vision AI Prediction endpoint. After the vision AI makes a prediction, the bot takes the top prediction result and queries another database to gather information on the predicted bird species. When the data is all collected, the bot will trigger an adaptive card with the top predicted bird species. Microsoft Composer - Photo: Microsoft Composer - BirdBot - GitHub: BirdBot GitHub Microsoft Adaptive Cards This is what one of the adaptive cards may look like after a successful prediction. Adaptive Card Designer - Photo: Adaptive Card Prediction - BirdBot Testing Hardware After implementing Custom Vision AI into a chatbot, we started to make progress on hardware/IoT devices that can support TensorFlow Lite. For those interested in rapid development of object detection models, Custom Vision AI might be for you as you can export your trained models as a TensorFlow Lite model. You will however have to implement your own code to run the TensorFlow Lite model and I recommend this tutorial by EdjeElectronics: Run TensorFlow Lite on a Raspberry Pi We also had the opportunity to work with the Azure Precept Dev Kit, and are currently in the process of evaluating. Here is what the current hardware and set up looks like. Microsoft Azure Dev Kit Microsoft Azure Dev Kit CORAL + Raspberry Pi + Camera Hardware Challenges We Ran Into Tagging datasets and making sure the data is high quality can be a tedious challenge. It took a lot of innovation to tag thousands of photos in a high-quality manner. Some of this innovation was around utilizing other existing bird models like YOLO to identify the object from a layer one perspective ("Bird"), then we give a more refined layer two tags ("American Goldfinch"). We also brought on advisors specialized in ornithology so we could always validate species questions and features. Identifying features and training for potential tag conflicts is how a model can be sustained long term as more objects are added. To identify these features, we needed to bring on ornithology subject experts. Our Current Accomplishments Accepted to the Fundable Accelerator Program Early Access to Azure Precept Studio Potential Partnerships with Alveus Sanctuary , American Eagle Foundation , and Urban Bird Treaty What we learned Innovation is not a straight line. Throughout the project, we have had many ideas of what we wanted to do with BirdBot. Even to this day, we will debate what the real value of an AI wildlife camera might be. We honestly don't know. Researchers don't use AI in the field currently to gather metrics at a scale that BirdBot may be able to do. We have had our Ph.D. advisors tell us that developing a refined AI metric for wildlife monitoring might be hard. Even if it is hard, it hasn't deterred us from the idea of using AI to help humans monitor the world around us. Everyone on the team believes in what BirdBot potentially can do for research. So much that if the metrics and standards for AI wildlife monitoring don't exist, we will make them. Research applications have probably been our biggest learning experience because it will be our biggest challenge in providing real-world value to Citizen Science initiatives. What's next for BirdBot - Computer Vision That Enables Citizen Science Hopefully Raise Some Money. Partner with Major Conservation Organizations. Create One of the World's Largest Wildlife Camera Networks. <div