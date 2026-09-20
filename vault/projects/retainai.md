---
slug: "retainai"
url: "https://devpost.com/software/retainai"
title: "RetainAI - The Intelligent Solution to Keep Your Top Talent"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 1006
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# RetainAI - The Intelligent Solution to Keep Your Top Talent

> RetainAI crafts customized employee retention strategies, empowering companies to minimize turnover, enhance engagement, and retain their top performers.

[Devpost](https://devpost.com/software/retainai) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[retrieval_grounding]]
**domain** [[civic_government]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** llama, llama-index, nvidia, python, scikit-learn, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for retainai

## Body

Inspiration Employee turnover is a significant financial burden, with estimates suggesting that it costs U.S. businesses approximately $1 trillion annually. This staggering figure encompasses both direct and indirect costs associated with losing employees and the subsequent need to replace them. Moreover, the span of control can be up to 12-15 employees per manager, making it incredibly difficult to track employee sentiment and implement effective retention strategies. With this problem in mind, I decided to build RetainAI. What It Does RetainAI is an NVIDIA AI Workbench project with a Streamlit front-end, serving as a web app for managers. The app allows a user to upload their own data in CSV and PDF formats, or use a sample dataset. Once uploaded, the app runs ML model, and displays a dashboard with employees and their predicted attrition probability. This probability is calculated using a Random Forest Classifier model trained on uploaded employee data such as tenure, compensation, promotion frequency, performance scores, etc. As a result, a manager can see which employees on their team are at high risk of attrition. But it doesn't end there—managers can also generate personalized retention strategies for individual employees. These strategies are created by GenAI and reference proprietary data in CSV, including employee details, performance reviews, benefits enrollment, engagement surveys, and unstructured PDF documents such as industry trends and company benefits. The model generates a comprehensive retention strategy, which managers can easily download as a PDF for future reference. Another key feature of RetainAI is a chat mode. A manager can ask questions about their entire team (not just individual employees). For example, one might ask, "Which employees are not satisfied with work-life balance?" or "Which employees performed poorly in the Q3 performance review?" The chat mode is driven by llama-3.1-70b-instruct model and reference proprietary employee data. How We Built It The project is built entirely in the NVIDIA AI Workbench. First, I generated fictional employee data, similar to what can be found in any modern human capital management system. Once the data was generated, I built a simple Random Forest Classifier model that predicts an employee's attrition probability based on various features. The model was tested on a new set of employees used in the demo. Employees with an attrition probability above 0.5 are considered at risk. Afterward, I developed a Llama-Index workflow that orchestrates multiple LLM calls, retrieving different pieces of information. I used local vector db to store the embeddings of sample PDF documents with industry trends and employee benefits. The model used for embeddings is NV-embed-qa-4 by NVIDIA. Next, llama-3.1-70b-instruct hosted as NVIDIA NIM is used to answer questions and retrieve relevant information. Below is a brief overview of each step of the workflow and a shortened version of the prompts: Analyze Compensation: How does the current salary of this employee compare to the industry benchmark? Consider the employee's starting and current salary. How does the salary growth compare to industry standards? Analyze Reviews: Based on the performance reviews, what are the employee's key strengths and areas for improvement? How do the performance reviews align with the attrition risk? Analyze Benefits: Are there any benefits that the employee is not utilizing? Are there additional benefits that could improve employee satisfaction and retention? Analyze Surveys: What are the key factors affecting employee engagement and satisfaction? Are there any areas for improvement based on the survey responses? Synthesize Responses: Based on the analysis of compensation, performance reviews, benefits enrollment, and engagement survey responses, provide a comprehensive retention recommendation for the employee. To enhance the app and offer more flexibility, I added the ability to upload custom CSV and PDF files instead of relying solely on the sample dataset. The uploaded data must match the structure of the training data to ensure prediction accuracy. For this, I built a field-mapping interface with semi-automated fuzzy matching. For example, if a user-uploaded CSV has a column labeled "Employee Name," it will automatically map to the required "Full Name" field. Users can also manually map fields if names differ significantly. Additionally, I introduced a chat mode using Streamlit’s chat functionality and the llama-3.1-70b-instruct model hosted on NVIDIA’s API Catalog. I used llama-index as the LLM framework to provide context, integrating employee snapshots through ChatMessage, MessageRole, and PromptTemplate for context-aware chat experience. Finally, I built a Streamlit front-end that allows users to interact with the app and launch it directly from the AI Workbench. See the detailed walkthrough video on YouTube - here Challenges We Ran Into One of the challenges was generating a fictional employee dataset that would make sense and reflect real-world data. I spent some time adding logic to the data generation script and refining it. The second challenge was building the prediction model. Since I had limited experience with traditional ML models, I faced difficulty in choosing the right model and verifying its accuracy. Accomplishments We're Proud Of I'm proud to have built this working prototype in a relatively short time while using technologies that were new to me. With some additional work, I believe this app has the potential to become a scalable stand-alone product. What We Learned I learned how to use NVIDIA AI Workbench, which was new to me. It was very easy to get up and running on my Mac. Additionally, I learned about traditional ML models such as the Random Forest Classifier and Survival Analysis. I also used NVIDIA NIM for the first time. What's Next for RetainAI I have a lot of ideas for the next steps, but they will mostly be driven by feedback. Some obvious ideas include: Deployment and hosting of the app Ability to use locally hosted LLMs Adding more advanced document parser like LlamaParse for complex PDFs Providing functionality to connect to user data (e.g., Snowflake, AWS, Databricks, or popular HCM systems) Improving the accuracy of attrition predictions Enhancing the output of retention strategies, either by prompt engineering or fine-tuning the model Adding the ability to perform RAG (retrieval-augmented generation) over different user files (e.g., internal policy, industry trends, compensation benchmark reports) <div