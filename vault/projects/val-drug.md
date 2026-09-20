---
slug: "val-drug"
url: "https://devpost.com/software/val-drug"
title: "VAL-DRUG"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 762
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# VAL-DRUG

> An AI-based App that can identify counterfeit drugs. The user just has to upload the back strip of the medicine and the app would decide whether the medicine is counterfeit or not.

[Devpost](https://devpost.com/software/val-drug) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** artificial-intelligence, azure, azure-ocr, cosmos-db, machine-learning, python, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for val-drug

## Body

Homepage User can upload or take an snapshot of the drug Valid Drug Counterfeit Drug Inspiration Counterfeit drugs can be harmful and may lead to serious side effects and when sold by unauthorized dealers can cause a huge loss in profit for the government. So it is imperative to develop a system for individuals to know if they are taking authentic drugs or not. Especially in India, there are very few systems that identify counterfeit drugs, and that too is not implemented to a large extent and is still in its basic stage. Not only in India, but this is also a serious problem in many countries. Counterfeit drugs comprise an increasing percentage of the US drug market and even a larger percentage in less developed countries. Counterfeit drugs involve both lifesaving and lifestyle drugs. In addition, the wholesale market involving numerous firms is a convenient target for counterfeit drugs. Trafficking in counterfeits can be extremely profitable; detection of counterfeits is difficult, and the penalties are modest. We wanted to develop something to address this problem for which not many solutions are built inspiring us to choose this topic What it does The system can identify whether the drug is counterfeit or not just with the help of the image of the back strip of the drug. The user can upload/take the picture of the drug and once the image is captured the image will be sent to the server where a series of checks is performed based on the text extracted from the image to verify the authenticity of the drug. These tests include comparing the composition of the drug, checking the batch number of the drug, checking if any of the text is wrongly printed, checking for the expiry date of the drug, and lastly ensuring whether the name and description of the drug are valid. If the uploaded image passes all these tests it would be declared valid or else it would be declared as counterfeit and the user would be provided with alternatives for the drug from the information stored in the database How we built it The OCR model is built on top of the azure OCR model. The authentic drug data is stored in COSMOS DB. The backend is built using a flask where we process the image and declare whether it's counterfeit or not. The entire backend is built using python and the frontend is built using Swift. We referred to a lot of documents to build the custom OCR model on top of the prebuilt OCR model catering to the needs of this particular application. We plan to replace the backend with Azure App Services as it would largely improve the access time Challenges we ran into The first challenge was to collect authentic data for this application. This was a huge challenge because there are lakhs of data and it took to a huge amount of time to scrap it from various sources. Each of us managed to collect about 1 lakh medicines each making the total count three lakh. The data collection phase was the major challenge in our opinion. Also using the extracted text from the medicine was hard as each manufacturer had their own way to list the data and it was challenging to write a common code that was able to identify the text pattern of various manufacturers. Also finally the various checks we perform required a lot of work on the logic part as it was important to classify the drug properly, even if we overlook a single field a valid drug may be classified as counterfeit, so this part a lot of work and effort Accomplishments that we're proud of We are proud of trying to solve a problem that has not been to that extent yet. We are happy that we were able to scrap a huge bulk of data for this application. We are proud of the fact that our product if implemented properly has the potential to solve a major problem in today's world. What we learned We learned a lot about azure and CosmosDB and various azure products used in this project. We learned how to handle a large amount and how to preprocess it properly. We also got to know some most commonly counterfeited drugs as a bonus while reading articles for building the application. What's next for VAL-DRUG 1.Building backend and deploying it using Azure App Services 2.Developing an android application for the same 3.Making the app work with big data by adding Azure pipelining to fasten the retrieval process <div