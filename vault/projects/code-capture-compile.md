---
slug: "code-capture-compile"
url: "https://devpost.com/software/code-capture-compile"
title: "CodeCapture"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 691
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/structured_db"
---

# CodeCapture

> An application that allows you to code without typing

[Devpost](https://devpost.com/software/code-capture-compile) · hackathon [[Azure AI Hackathon]]

## Facets

  <sub>weak: vision_ocr</sub>
**domain** [[education]]
**user** [[educator_student]] [[general_public]]
**substrate** [[structured_db]]

**stack** azure, computer-vision, csharp, mysql, ocr, python, serverless, twilio, xamarin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what's next for codecapture

## Body

Inspiration While in recent times, the world has started moving towards pro-CS education, the fact is that buying computers is a distant dream for most students and educational institutions across the globe even today. In most developing countries, which account to over 85% of the world , the ratio of CS students versus the number of computers available is highly skewed and most students are still learning programming via pen-and-paper. At the same time, however, the number of people who own mobile phones has significantly increased. Statistically speaking, 4 out of 5 people have access to smartphones versus only 2 out of 5 to computers . Smartphones simply are more accessible than computers. Bridging this gap between pen-and-paper coding and coding on a computer by using a technology that people already own can bring a significant difference in the adoption of Computer Science education today. What it does CodeCapture is a web application that aims to ease coding education for individuals that have limited to no access to personal computers and computer labs at school or college using pen-and-paper and their smartphone. CodeCapture allows you to simply take a picture of your hand-written code, extract it, and run it in your browser . With CodeCapture, you will be able to code without typing. Built around this amazing functionality is an all-inclusive mobile-first learning platform. With facilities such as customized programming courses for students and educators, code testing and assessment facilities, and virtual classrooms, CodeCapture shall offer an unparalleled online CS education experience. CodeCapture will also feature a plethora of curated learning content for all users (individual and institutional) as well as a safe space to connect with the learner’s community and share their work. With CodeCapture, YOU DO NOT NEED TO TYPE TO CODE! How we built it While developing our product, we had to ensure that our solution, while fulfilling the consumer’s need, also remains highly fault-tolerant, scalable, and available. Therefore, we made our system design decisions in order to ensure a robust product. Azure Cognitive Services is our product’s hero, enabling us to take code from paper to mobile. While text extraction facilities have been available in the market for a while, this is a first-of-its-kind use-case. We utilized ReactJS as our primary technology for the consumer-facing side of the product to ensure better performance. Azure Static Web Apps as a tool also enhances scalability and offers high availability. We chose to forgo a traditional back-end and instead use a serverless architecture via Azure Functions with .NET for all our infrastructural work to ensure maximum scalability and lower cost. For our database needs, considering our structure, we chose Azure Database for MySQL due to its high availability. Our storage has been enabled by Azure Blob Storage in order to ensure high availability, accessibility and security of stored information. In order to facilitate compilation of code, we are using an Azure VM where compilers are installed, where a custom-built Python API is utilizing the system resources to manage the code compilation. Thus, we are pushing the boundaries of traditional coding education platforms in order to stand out and disrupt the market, both in terms of idea and execution. Accomplishments that we're proud of The CodeCapture Web App Prototype was accepted by Code.org to be featured in the Hour of Code 2020 . It was featured on hourofcode.com for the Computer Science Education Week 2020 . The CodeCapture Mobile App was featured in the Student Showcase at .NET Conf 2020 . The CodeCapture Web App was selected as the National Winner in the Education category at the Microsoft Imagine Cup 2021 India Championship The CodeCapture Web App won the Popular Choice Prize at the Microsoft Azure AI Hackathon What's next for CodeCapture We have a lot of plans to scale CodeCapture to an even greater extent. Using this amazing product as our foundation, we intend to build an all-inclusive learning platform. With facilities such as virtual classrooms, curated learning content, instructors' upskilling, and learners' community, CodeCapture shall offer an unparalleled online mobile-first classroom experience. We aim to empower youth to be future ready by making coding education accessible to all <div