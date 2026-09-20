---
slug: "code-explorer"
url: "https://devpost.com/software/code-explorer"
title: "Code Explorer"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 1039
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Code Explorer

> This app allows you to ask questions and get answers regarding your code provided the folder location of your code.

[Devpost](https://devpost.com/software/code-explorer) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** codellama, docker, langchain, neo4j, ollama, streamlit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for code explorer

## Body

App Diagram Inspiration I've always found ChatGPT to be useful when developing my own coding projects. However, one feature this application was missing for me was the ability to reference my source code files. So I decided to build my own application that allows you to select the folder in which your code project is located and what programming language you are using. Then you can ask the chatbot any questions regarding your codebase and it'll be able to refer to your own code. An example use case where the Code Explorer chatbot could be useful: "Provided the source code, please update CatQuery.py to query the cat dataset using pagination, referencing the code in the DogQuery.py file which already contains code for querying the dog dataset using pagination, and show the resulting code." What it does This app allows you to ask questions and get answers regarding your code provided the folder location of your code and the programming language you are using. It utilizes a RAG-based AI framework to provide additional context about your code files to an existing LLM model. It supports a variety of programming languages such as *.swift, *.py, *.java, *.cs, etc . This tool can be useful for learning/debugging your code projects such as Xcode projects, Android projects, AI applications, web dev, and more. How I built it Here is a diagram of how the application works. Step 1: The user first picks the location where their code files are located The user also selects the programming language of the files they are interested in The user selects the "Process files" button on the UI The documents are loaded and chunked The chunks are embedded into vectors and stored in a vector database Step 2: A QnA chain is created which allows the user to talk to the chatbot in a question-and-answer style. The chatbot will reference the vector database when answering the coding question, ergo referencing the original source code files. You can talk to this chatbot directly and much more accurate and technical answers. A separate Agent chain is created which uses the QnA chain as a tool. You can think of it as an additional layer on top of the QnA chain which allows you to communicate with the chatbot more casually. Under the hood, the chatbot may ask the QnA chain if it needs help with the coding question, which is basically an AI discussing with another AI about the user's question before returning the final answer. In testing, the agent appears to summarize rather than give a technical response as opposed to the QA agent only. Langchain was used to orchestrate the chatbot pipeline/flow Step3: The user first selects whether they want to use the standalone QnA chain (enable "Detailed Mode") or the Agent chain (disable "Detailed mode") When the user asks a question, the appropriate chain is used to return the final answer that is displayed in the chat window Docker Services: pull-model : Downloads the specified LLM model to use (default: codellama:7b-instruct ). The reason codellama:7b-instruct was used was because it was based on the llama2 model which performs similar to OpenAI's LLM model, but trained with additional code context, and then fine-tuned to receive and respond in human language which makes it better at responding when asked about code related questions. llm : Ollama LLM self-hosting service that can host the LLM model/embedding that was pulled. database : Neo4j database. It is used to store and retrieve the vector embeddings of the code files. bot : Main application built with the Streamlit UI framework. The user will be able to interact with the application from this service. Challenges I ran into This was my first time getting into the world of LLM-based development. I thought this hackathon would be a good opportunity to learn and apply the tools used in this software space like Docker, Neo4J, LangChain, Ollama, and more. I've mostly been an app developer, but AI has always been an intriguing topic to get into. The GenAI stack was a big help to get me started. Retaining memory in Langchain was tricky with the QnA chain, and didn't seem to work well. The only around that was to use an Agent chain which could retain the chat history. However, there were drawbacks to this approach since it wouldn't give as technical of an answer, which is why it can be optionally set with the "Detailed mode" toggle in the sidebar. Streamlit reruns the entire Python script whenever the user interacts with a widget (e.g. submit text in a chat, click button, etc.). So I had to be mindful of this and store all widget values in the session state and ensure that resources such as the vector store reference and the memory in the Agent chain would still be retained by marking them as cached resources with Streamlit's @st.cache_resource . This way the application would run as expected. On Ubuntu Linux, I found that referencing the host.internal.docker DNS didn't work when using the Docker CE only. This seemed to only be a feature of Docker Desktop which I then installed and the DNS was able to be resolved properly. Accomplishments that I'm proud of I'm excited that I got to try LLM-based development for the first time and was able to build a minimal viable product that can actually be useful for myself and hopefully, anyone else who might find this tool useful as well. What I learned I learned what Ollama, Neo4j, and Langchain were. I'd never heard of them before, but now I have a good grasp on how I can use them to further develop this project and/or start a new LLM-based project. I also learned some new Docker configurations when setting up my docker-compose and Dockerfiles such as the ability to watch for file changes for automatic rebuilds and managing an internal network between all these services. What's next for Code Explorer I'll look more into Langchain's agents and see if I can improve the responses it retrieves from the QnA chain to provide more in-depth and technical answers to the user's questions. I may switch to a full-fledged UI framework such as ReactJS or ASP.NET in the future. <div