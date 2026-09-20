---
slug: "clarifina"
url: "https://devpost.com/software/clarifina"
title: "Clarifina"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 1164
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/security_privacy"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Clarifina

> Financial literacy done smart, together.

[Devpost](https://devpost.com/software/clarifina) · hackathon [[ShellHacks 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[security_privacy]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** amazon-web-services, axios, cloudwatch, express.js, figma, firebase, javasc, node.js, openai, s3, textract, typescript

## How they structured the write-up

- inspiration
- what does the project do?
- how was the project built?
- challenges
- accomplishments
- what we learned
- future iterations for clarifina

## Body

Inspiration We are hunting down the feeling of uncertainty when reading financial documents. Our team understands how difficult it can be to understand complex documents. As college students, the big financial jargon can be daunting. Additionally, many of our teammates are from families whose first-language is not English - for them, too, this task can quickly lead to an overwhelming confusion of words. The situation is exacerbated for underrepresented individuals. Due to the lack of understanding for financial documents individuals are turned away from pursuing their business pursuits or end up making a poor decision. The current market does not have a streamlined way for individuals to be able to better understand their financial matters. We sought to create a platform to centralize the process in improving the community’s financial literacy by providing guidance & document summaries. What does the project do? Our web application is revolutionizing the way users take control of their financial futures by offering personalized recommendations and tailored financial advice like never before. We’ve created a one-stop hub where financial literacy becomes not just accessible, but empowering. Whether users are navigating tricky financial terminology or seeking guidance on complex financial projects, our platform provides expert insight with the user’s unique financial history and demographic profile at the core of every recommendation. With our intuitive PDF upload feature, users can upload documents they need help deciphering, and our system doesn’t just analyze—it highlights key sections and offers easy-to-understand, personalized definitions of the most complex terms. But we didn’t stop there. Our AI-powered recommendations go beyond generic advice, delivering insights that are custom-fit to each user’s background and financial circumstances, helping them make smarter, more informed decisions. By centralizing financial education into a seamless, user-friendly experience, we're not just improving financial literacy—we're building the financial confidence that drives lasting change in our communities. How was the project built? This web application was built using a robust backend architecture powered by AWS and Firebase, combined with a modern frontend designed in TypeScript and CSS. Leveraging AWS services like S3 for document storage and Textract for extracting text via machine learning, the system seamlessly processes user-uploaded documents. A Lambda function, triggered via API Gateway, handles uploads, initiates Textract processing, and returns structured JSON outputs, all while maintaining CORS functionality. The backend also integrates IAM roles to secure access across S3, Textract, and Lambda, with Cloudwatch for real-time monitoring and logging. On the user management side, Firebase Auth handles authentication, while Firestore stores user data and documents in a well-structured database. Additionally, OpenAI’s models like GPT-4o provide personalized financial analysis and advice based on demographic data. Node.js and Express.js power server-side operations, handling HTTP requests and routing efficiently. The frontend was developed in TypeScript, styled with CSS, and designed using Figma for a smooth user experience, integrating tools like Axios, PDF Viewer, and Highlight for enhanced interactivity and document display. Challenges To preface, none of our teammates have been exposed to the majority of backend tools used in our project (AWS, Lambda, Textract, Firestore, Express.js, Axios, Typescript). Overcoming this major learning curve meant an in-depth conversation with the team on our strengths, weaknesses, & current interests in learning. Our team was completely unaware of how to transfer from Cognito (AWS’ authentication service) to Firebase Authentication (Google’s service). The SDK’s from the two platforms have different APIs, making the authentication, session verification, and user management difficult as significant refactoring was necessary. Another challenge was saving the users session into their user dashboard. It was difficult to return to an exact session & redisplay that screen from the database where the suggestions, chats, as well as PDF annotations were saved. Frontend wise, it was difficult to create smooth transitions onto the page & then create a logical flow of Typescript components. There was a constant need for rerouting as well as a process with trial & error to position the elements/create smooth transitions. Accomplishments We are beyond proud of your ability to preserve through a very daunting task and execute accordingly on it. We spent hours before beginning our project researching our target aduice’s main motivation for participating in the web-app. In that timeframe, we also planned into detail what the flow of our application would look like - even having the opportunity to wireframe with Figma. Due to this process of test-driven development, we were able to reduce the amount of time it took to create certain aspects. Our number one accomplishment in the backend was being able to integrate every component together to create the document analyzer. Using our API from the gateway, our document was accessed on S3 with our lambda function, which used Textract to turn the text into a JSON file, which in turn was processed by OpenAI's GPT, storing both the pdf and the JSON within our Firestore database, associated with each user's individual account from the authentication. On the user side, they simply clicked a line and would get a definition and an analogy that accounted for their demographics. Frontend's biggest accomplishment was being able to design the elements on Figma & bring that vision to life. Our team self-curated figures to use on the pages, too. It was an amazing opportunity to see how the design of different elements completely changes the user’s experience as well as their perception of which elements to click. When we finally established the design for the page to scan documents, we were overjoyed because of the amount of little details that mattered into the overall functioning of the page. For example, adding pulsating effects to draw the user’s eyes to an important fact. What we learned The biggest thing we learned was how to be resourceful together as a team but also individually. As a team we had to truly work with each other's strengths and present ourselves in a vulnerable state to admit our weaknesses. By playing off what had a knack as well as our own interests in learning something new, we were able to incorporate our group member’s interests and passions into this project. Individually, we were able to learn how to look for specific articles/videos/comments online and synthesize that information to become what we have created. Understanding that the answer cannot be found in one location, but rather a harmony of several became a huge growth point in this hackathon. Future Iterations for Clarifina In the future, we would love to tailor our responses more towards underrepresented communities. This would include training models to identify biases in the information we are presenting. Moreover, we’d like to incorporate a section that would present opportunities for those individuals based on the demographic data we collected. To help a wider audience of individuals, it would be neat to include a translating option to convert the document uploaded into another language. As an additional feature, we could also provide our personalized answers in that language, too. For the scanning capabilities, we would like to implement individual words as well as summary paragraphs. <div