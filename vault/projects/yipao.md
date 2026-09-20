---
slug: "yipao"
url: "https://devpost.com/software/yipao"
title: "Moresales"
hackathon: "Google Cloud Vertex AI Agent Builder Hackathon"
organization: "Google"
winner: true
words: 1052
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Moresales

> Revolutionizing bussiness intelligence with AI-driven SQL interactions. Simplify complex queries and enhance database efficiency effortlessly

[Devpost](https://devpost.com/software/yipao) · hackathon [[Google Cloud Vertex AI Agent Builder Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** astro, dialogflow, fastapi, gemini, google-cloud-sql, javascript, mysql, openapi, pypi, python, react, sql, vertexai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moresales

## Body

Yipao Logo Yipao Framework Inspiration The inspiration for moresales stemmed from the frustration of managing and querying large SQL databases. Many businesses struggle with data analysis, often spending countless hours trying to derive meaningful insights from their data. We envisioned a solution that would not only simplify this process but also leverage the power of AI to enhance query efficiency and accuracy. What it does moresales is a revolutionary open-source Python library developed in this hackathon ( https://pypi.org/project/moresales/ ) that facilitates AI-driven interactions with SQL databases. It allows users to generate and execute SQL queries dynamically using natural language, essentially enabling users to chat with their databases. This chat functionality transforms moresales into a personal data analyst for each user, providing tailored insights and making data interaction more intuitive and accessible. moresales integrates seamlessly with Google services ensures that users can leverage the full power of Google's advanced AI technologies, enhancing the efficiency and accuracy of their data operations. moresales's ability to retrieve, analyze, and visualize data effortlessly makes it a powerful tool for businesses aiming to harness the full potential of their data. How we built it moresales was developed using a combination of advanced technologies and a carefully designed architecture to ensure robust performance and seamless functionality. The development process is illustrated in the following scheme: Dialogflow and Vertex AI Agent Builder Integration: Users interact with moresales through Dialogflow, which processes natural language inputs. Dialogflow sends these inputs to Vertex AI Agent Builder, where prompt rewriting occurs to refine and optimize the queries. Decision Making: The refined queries are then passed through a decision-making module that determines the appropriate action: initializing a connection, documenting the database, or performing inference. moresales Core Functionality: moresales connects to the SQL database and executes SQL queries dynamically. It supports various operations such as initialization ( INIT ), documentation ( DOCUMENT ), and inference ( INFERENCE ). moresales's API facilitates these interactions, ensuring seamless communication between the AI components and the database. Vectorstore and Retrieval-Augmented Generation (RAG): moresales integrates with vector databases through the Vectorstore, enhancing the retrieval process. The RAG model, powered by Google Generative AI (Gemini), is used to augment and improve the accuracy of data retrieval and query responses. Execution and Information Retrieval: Once the SQL query is generated, it is executed on the database. The results are then processed and returned to the user, providing precise and actionable insights. This architecture allows moresales to leverage the strengths of Google Cloud services, delivering a powerful and efficient tool for data analysis. The iterative development and rigorous testing ensured that moresales meets the highest standards of performance and reliability. Challenges we ran into Challenges we ran into We encountered several challenges during the development of moresales. One significant issue was working with Dialogflow, as we had not used it previously. However, we soon discovered that Dialogflow is a powerful tool for natural language processing, which greatly enhanced our project's capabilities. Another challenge involved the API certification process to ensure the agent could use it through OpenAPI. Initially, this presented some difficulties, but by following detailed tutorials and leveraging community resources, we were able to resolve these issues effectively. Overcoming these obstacles not only improved our technical skills but also reinforced the robustness of moresales's architecture. Accomplishments that we're proud of We are immensely proud of several key accomplishments in the development of moresales. First and foremost, we successfully created a tool that significantly simplifies data analysis by enabling natural language interactions with SQL databases. This breakthrough allows users to manage and query their data intuitively, making advanced data analysis accessible to everyone. Additionally, our seamless integration with Google Cloud services, such as Vertex AI and Dialogflow, showcases the powerful synergy between moresales and leading AI technologies. This integration not only enhances moresales's performance but also leverages the full potential of AI to deliver precise and actionable insights. Furthermore, our team overcame substantial technical challenges, demonstrating resilience and a commitment to innovation. The positive feedback from initial users has validated our vision, and seeing moresales in action, solving real-world data problems, is a testament to the hard work and dedication of our team. We believe moresales has the potential to revolutionize data analysis, and we are excited about the future possibilities it holds. What we learned Throughout the development of moresales, we gained invaluable lessons in teamwork and project management. We learned how to collaborate more effectively as a team, particularly under tight deadlines, ensuring that each member's strengths were leveraged to achieve our common goal. Constant testing and iterative improvements became integral to our workflow, helping us to quickly identify and resolve issues. We also embraced the challenge of exploring new technologies, such as Dialogflow and the intricacies of AI-driven SQL interactions. The process of creating a Python library from scratch was an enlightening experience, teaching us the nuances of software development and library management. Additionally, we recognized the importance of fostering an open-source community, understanding that collaboration and community engagement are key to the growth and success of any project. These lessons have not only enhanced our technical skills but also prepared us for future endeavors in the tech industry. What's next for moresales The future of moresales is incredibly promising. We plan to continue enhancing the library by expanding its capabilities and integrations. One of our primary goals is to deepen moresales's integration with Google Cloud services, leveraging the latest advancements in AI and machine learning to provide even more powerful and efficient data analysis tools. This includes further utilizing Vertex AI, Dialogflow, and other Google Cloud technologies to enhance moresales's performance and user experience. In addition, we aim to broaden moresales's real-world applications by integrating it with various business intelligence platforms and industry-specific solutions. This will allow businesses to seamlessly incorporate moresales into their existing workflows, providing them with unparalleled data insights and operational efficiencies. We are also working on adding more features, such as support for additional SQL dialects, enhanced natural language processing capabilities, and more robust security measures to ensure data integrity and privacy. Our vision for moresales extends beyond just a tool; we aim to build a thriving open-source community around it. all acknowledgements for this work go to Facilpos, and this product was developed by Facilpos. Youtube -> https://www.youtube.com/c/facilpos/videos Facebook -> https://www.facebook.com/facilpos/ Instragram -> https://www.instagram.com/facil_pos/ <div