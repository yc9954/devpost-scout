---
slug: "atlascode"
url: "https://devpost.com/software/atlascode"
title: "Techdocs"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 1237
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Techdocs

> Code Documentation, Redefined: Where AI Meets Clarity!

[Devpost](https://devpost.com/software/atlascode) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** azure, azure-sql-database, clarifai, docker, fastapi, huggingface, langchain, python, python-package-index, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for techdocs

## Body

techdocs CLI LLM Streamlit Application Inspiration OUR LAZINESS IS THE SOLE MOTIVATION FOR TECHDOCS Techdocs really started as a passion project due to our indolent nature towards documenting our own codebases. We are currently working as core backend-microservice developers for an open-source organization - Heritians at our University. Here is our story about how Techdocs was born: Currently, we are the only devs working on the project but now that we have recruited 20+ new students it is inevitable to document our code to increase code readability. At the time of recruitment, our codebase already consisted of 6+ directories and 4k+ lines of code. For the new recruits, understanding our codebase ASAP is imperative. Documenting the code manually is not a possibility because, well, we are lazy and we hate to document. As we both are very well-versed with LLMs our thought was, why don't we automate this boring documentation thing once and for all? And there we have it. What it does Techdocs is a PyPI package capable of automatically generating documentation for Python codebases via CLI . Techdocs generate the docstrings in place by analyzing the structure, logic, and functionality of code by leveraging Abstract Syntax Tree (AST) for .py files. It leverages the power and efficiency of Large Language Models (LLMs) along with carefully crafted API design to accomplish the task. How we built it Techdocs can be broadly classified into 3 major components: Backend/API : This API is where all the magic happens. It acts as a brain for our product. Developed using FastAPI , our API is catered to achieve minimum user-perceived latency. Our API hosts WizardLM-70B - a fine-tuned version of the Llama-2 model for downstream tasks like Code Understanding, and Code Generation. Deployment: The API is linked with Huggingface spaces via a simple .yml workflow. It then uses the power of DOCKER to containerize the API module, hosting it on Hugginface's servers . This way, our public endpoints are exposed and our CLI tool can use them however the user intends. LLM Tools Used: The API uses the WizardLM-70B model served on Clarifai's servers . Integration of Prompt Engineering, user inputs and model inference are done with the help of Langchain . Deployed API Link: https://caffeinecrew-techdocs.hf.space/docs CLI/PyPI Package : This is the main interface with which users can interact with our product. The tool is a PyPI package which makes it easier to install and use in any Python project. To prepare the package tools like build , twine , setuptools , and argparse have been used. Here are a few things you can do with the CLI tool. $ techdocs >👋 Hi there! Welcome to techdocs. Here are some cool things you can do: 💫 try out a demo with our new GUI 🚀 and explore how to use the CLI: ➡️ https://techdocs.streamlit.app/ 💫 signup here to get an API key 👤: $ techdocs signup -u <username> -p <password> -e <email> 💫 use the line below to issue a new API key 🗝️: $ techdocs apikey -u <username> -p <password> 💫 use the CLI to generate documentation for your project 📚: $ techdocs generate -k <api_key> -u <username> -p <password> -d <directory> PyPI package: https://pypi.org/project/techdocs/ Web App : Note that the web app is only intended as a demo. To unleash the full power of Techdocs , please refer to the CLI usage. We used Streamlit to create a user-friendly web app that allows users to upload their code block and get the documentation in a proper format. We have mentioned clear instructions on the instructions page. The home page of our app has all the details of our Techdocs projects along with its Architecture. Challenges we ran into API Deployment Issues: Our very first API design consisted of keeping the entire WizardLM-70B model locally on Huggingface's servers. However, the size of the model exceeded the free tier available there. Furthermore, inferencing from a model available on a local disk was extremely time-consuming. To get docstrings of a single function it would take a few minutes. To tackle these mentioned issues, we shifted to Clarifai's API for our LLM. As the model is constantly kept on a dedicated server, the inferencing time was reduced by 90% from the original approach. Our inference time was reduced from a few minutes to under 10 seconds . This step, however, added an external dependency for our API deployment. Before going for Hugginface Spaces, the original plan was to deploy the API on Vercel Cloud. However, we were not able to deploy it on Vercel due to this newly added dependency - the 'Clarifai' package, as it exceeded the free tier resources that Vercel grants. To solve this issue, we decided to sync our GitHub repo to Huggingface Spaces via a .yml workflow and then deploy the API there by using our DOCKERFILE . Without the docker support from Huggingface Spaces, we could not have deployed our API anywhere! Docker was our saviour. CLI development: Unlike the infamous click package for building CLIs, the package we used argparse , does not provide a built-in way to create subcommands. Adding subcommands by adding sub-parsers and binding appropriate function definitions was a nightmare. But we aced it eventually! Sending Verification emails for new signups: Our API is deployed on Huggingface spaces which blocks all the SMTP relay ports and hence it was very hard to send verification emails. To mitigate this issue, we had to buy a separate domain and relay the SMTP servers on that domain. This email server is deployed separately on Vercel Cloud. Accomplishments that we're proud of Firstly, all the documentation you see in this project is created by using Techdocs . No code documentation is done manually :) We have developed a PyPI package so contributors all around the world can contribute and make this product better. We strongly believe, in the power of open-source projects! PyPI package allows easy access to all users. What we learned The use of Langchain was crucial here. This open-source tool has so much potential and is very handy in developing LLM products. It is cool! DOCKER images are way better than using other deployment platforms. This was the very first project where we actually used docker to deploy our product. Designing UI is a heck of a task. What's next for Techdocs Currently, Techdocs can only generate documentation for Python programming language. Our plan is to expand our product to a spectrum of popular programming languages to help developers across the globe with documentation tasks. We plan to hire experts from different programming languages so that we can extend the support and build native packages for those languages. Being final-year undergrad students, we are looking for decent funding so we can achieve this task. As of now, our product suffers majorly in terms of privacy and integrity. As we have mentioned earlier, we are using a third-party Clarifai package for hosting our LLM. This creates a big question about user code integrity and privacy. To cater to this issue, we are constantly exploring new quantized and light versions of possible LLMs that we can employ for this task. This will eliminate the need for third-party APIs. We plan to integrate such lightweight models into our PyPI package itself so that none of the user's code will be sent anywhere, and all the documentation generation will take place on the user's device itself. <div