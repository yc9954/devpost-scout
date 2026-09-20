---
slug: "instacanva"
url: "https://devpost.com/software/instacanva"
title: "instaCanva"
hackathon: "Canva AI and Integrations Hackathon"
organization: "Canva"
winner: true
words: 819
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# instaCanva

> Instant Ideas! Instant Designs!

[Devpost](https://devpost.com/software/instacanva) · hackathon [[Canva AI and Integrations Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[legal_professional]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[video_visual]]

**stack** canva-connect-api, flask, gemini, python, sendigrid, twilio

## How they structured the write-up

- instacanva ⚡: seamlessly bringing canva to whatsapp

## Body

instaCanva ⚡: Seamlessly Bringing Canva to WhatsApp instaCanva is an innovative WhatsApp bot that allows users to manage their Canva designs directly from WhatsApp, combining the ease of messaging with the powerful design capabilities of Canva. With instaCanva, you can create, upload, and export Canva designs without ever leaving WhatsApp, streamlining your design process and making it more accessible. Inspiration ✨: The inspiration for instaCanva came from a personal milestone—reaching 200 designs on Canva. As a huge fan of Canva, I realized the growing need for a more accessible way to manage an increasing number of designs on the go. This need, combined with the rising prevalence of APIs and AI in modern applications, led me to team up with a fellow Canva enthusiast to create a solution that integrates Canva’s capabilities into WhatsApp. The idea is rooted in the belief that future applications will increasingly build on existing platforms to enhance productivity and efficiency, much like InstaCanva does. How We Built It instaCanva was built using the following technologies: Python for the backend logic. Flask as the web framework to handle requests. Twilio & Sendgrid for WhatsApp & Email messaging integration. Canva Connect API for design management and authentication. Google Gemini AI for natural language processing to handle user commands. The development process involved integrating these technologies to create a seamless experience for users, from authenticating their Canva accounts to managing their designs via WhatsApp. Challenges: Building instaCanva presented several challenges: Lack of Resources: We found very few tutorials on developing applications that integrate with Canva, especially for developers. OAuth Implementation: Implementing secure OAuth authentication with Canva proved to be a complex task. File Handling: Sending and receiving files from WhatsApp through Twilio to Canva involved intricate handling of media files, which was initially buggy. Complex Codebase: The early stages of development were plagued with numerous if-else statements, leading to a buggy and inefficient codebase. Despite these challenges, we persevered, learning and adapting as we progressed. The experience highlighted the importance of solid code optimization, which is a priority for our future development. Current Capabilities 💥: instaCanva offers the following features: Authentication with Canva: Securely authenticate your Canva account via OAuth2. Upload Assets: Directly upload images and other design assets from WhatsApp to your Canva account. Create Designs: Instantly create new Canva designs by providing a title through WhatsApp. List Designs: Search for and list your existing Canva designs using keywords. Export Designs: Export Canva designs in PDF format and receive them directly on WhatsApp. Natural Language Processing: Leverages Google Gemini AI to understand and process user commands in natural language. Accomplishments That We're Proud Of Despite the challenges, we are proud of several key accomplishments: Successfully integrating Canva’s API with WhatsApp through Twilio. Creating a functional MVP that allows users to manage their Canva designs directly from WhatsApp. Overcoming initial technical hurdles with OAuth and file handling to create a seamless user experience. What We Are Learning 🤗 Throughout this project, we are continuously learning: The importance of careful planning when integrating multiple APIs, especially when dealing with authentication and file transfers. How to optimize and refactor code to improve performance and maintainability. The value of persistence and adaptability in overcoming technical challenges and resource limitations. Future Roadmap: We have ambitious plans to enhance instaCanva, including: Optimizing Code: Refactoring the code to reduce complexity and improve performance before moving to production. Direct WhatsApp API Integration: Enhancing communication by hitting the WhatsApp API directly for faster responses. Enhanced Security: Improving profile and session security, as well as data privacy measures. Additional Canva Features: Integrating advanced Canva functionalities like template customization, text editing, and image manipulation directly from WhatsApp. Multi-format Export: Expanding export options to include formats like PNG and JPEG. Advanced NLP: Improving the natural language processing capabilities for more accurate and intuitive user interactions. Cross-Platform Integration: Exploring integration with other platforms to extend InstaCanva’s utility. Analytics and Reporting: Implementing features to track user interactions and provide insightful reports for continuous improvement. Development Status: instaCanva is an actively developing project. We are continually working on enhancing its features, optimizing its performance, and incorporating user feedback. The current MVP demonstrates the core functionalities, and we plan to release regular updates as we build towards a fully-featured product. 3 main keywords to use currently when testing the MVP upload -- This will import or send your assets/files to Canva connect -- Connect your Canva account to instaCanva download or get me or export -- This downloads and retrieves the query parametered file. To try our magic bot in Twilio Sandbox: send join moon-reach to +14155238886 📌 Conclusion: instaCanva represents a forward-thinking approach to application development by leveraging existing platforms to create new efficiencies. As Canva enthusiasts, we are excited about the potential of instaCanva to revolutionize how users interact with Canva and look forward to receiving feedback from the judges to help us refine and perfect this innovative tool. <div