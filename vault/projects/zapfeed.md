---
slug: "zapfeed"
url: "https://devpost.com/software/zapfeed"
title: "Zapfeed"
hackathon: "TiDB Future App Hackathon 2024"
organization: "PingCAP"
winner: true
words: 800
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Zapfeed

> Transform Feedback into Actionable Insights

[Devpost](https://devpost.com/software/zapfeed) · hackathon [[TiDB Future App Hackathon 2024]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[retail_commerce]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** nextjs, openai, tailwindcss, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zapfeed

## Body

Inspiration The inspiration for Zapfeed came from observing the challenges businesses face in managing and interpreting customer feedback. Many companies gather feedback through various channels, but often struggle to analyze this data effectively and convert it into actionable insights. The idea was to create a tool that not only simplifies the feedback collection process but also leverages advanced technologies like AI and vector search to enhance the analysis. We aimed to empower businesses to understand their customers better, make informed decisions, and ultimately improve customer satisfaction. Our passion for customer-centric solutions and the potential of AI in transforming data into insights drove us to develop Zapfeed. What it does Zapfeed is a SaaS platform designed to help businesses collect, analyze, and act on customer feedback efficiently. The key features include: Feedback Collection: Users can easily gather feedback through customizable widgets that can be embedded on their websites. Intuitive Dashboard: The dashboard provides a visual overview of feedback metrics, including sentiment analysis, total feedback, and trends over time. AI-Powered Analysis: Utilizing OpenAI's GPT models, Zapfeed offers an AI chatbot that can answer queries based on feedback data, providing contextual insights. Vector Search Capabilities: By integrating TiDB's vector search technology, Zapfeed allows users to find relevant feedback quickly, enhancing the discovery of patterns and themes. How we built it We built Zapfeed using a modern tech stack that includes: Frontend: We utilized Next.js for building a responsive and dynamic user interface. This framework allows for server-side rendering and fast loading times, enhancing user experience. Backend: We integrated Next.js with TiDB Serverless for storing data & its vector search capabilities. AI Integration: We leveraged OpenAI's GPT models for natural language processing, allowing users to interact with the chatbot for feedback analysis. Deployment: The application is deployed on Vercel, ensuring fast and reliable access for users. Challenges we ran into Throughout the development of Zapfeed, we encountered several challenges: Data Integration: Integrating TiDB Serverless and ensuring smooth data flow between the frontend and backend required careful planning. We had to optimize our data schema and queries to leverage vector search effectively. AI Response Accuracy: Achieving accurate and relevant responses from the AI chatbot was a challenge. We had to refine our prompts and ensure that the AI had enough context to provide meaningful insights based on user queries. Customization Complexity: Allowing users to customize their feedback widgets while maintaining a user-friendly interface was difficult. We needed to strike a balance between extensive customization options and ease of use. Testing and Debugging: Ensuring the application worked seamlessly across different devices and browsers required extensive testing. We faced issues with responsiveness and had to iterate on our designs to ensure compatibility. Accomplishments that we're proud of We are proud of several accomplishments with Zapfeed: Successful Integration: We successfully integrated TiDB Serverless with vector search technology, allowing for fast and efficient querying of feedback data, which is a unique feature in our market. AI Chatbot Functionality: The AI chatbot can now effectively analyze feedback and provide relevant insights, showcasing the power of AI in improving customer understanding. User-Friendly Interface: We developed an intuitive dashboard that simplifies the complexity of data analysis, making it accessible to users with varying technical backgrounds. Customization Capabilities: Our customizable widgets allow users to tailor their feedback collection methods to fit their brand identity, which enhances user engagement. What we learned The development of Zapfeed taught us valuable lessons: Importance of User Feedback: Gathering feedback from potential users during the development process helped us refine our features and user interface. Understanding user needs is crucial for creating a successful product. Iterative Development: We learned that building a product is an iterative process. Regular testing and feedback loops allowed us to identify issues early and adapt our approach as needed. Leveraging New Technologies: Exploring and implementing technologies like TiDB and OpenAI's GPT gave us insights into the potential of combining traditional databases with AI and vector search. What's next for Zapfeed Looking ahead, we have several exciting plans for Zapfeed: Enhanced AI Capabilities: We aim to further improve our AI chatbot by training it on a broader dataset of feedback to enhance its contextual understanding and response accuracy. Mobile Application: Developing a mobile version of Zapfeed to allow users to manage feedback on the go is a key priority. This will make our platform even more accessible. Advanced Analytics Features: We plan to introduce advanced analytics tools, such as predictive insights and trend forecasting, to help businesses anticipate customer needs and behaviors. Integration with More Platforms: Expanding our integration capabilities with popular platforms like Shopify and WordPress will broaden our user base and enhance functionality for e-commerce businesses. User Community and Support: Establishing a user community for sharing best practices and support will help foster engagement and continuous improvement based on user feedback. <div