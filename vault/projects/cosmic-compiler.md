---
slug: "cosmic-compiler"
url: "https://devpost.com/software/cosmic-compiler"
title: "Cosmic Compiler"
hackathon: "Build Beyond Hackathon"
organization: "BuildBeyond"
winner: true
words: 457
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Cosmic Compiler

> One Compiler to rule them all

[Devpost](https://devpost.com/software/cosmic-compiler) · hackathon [[Build Beyond Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[educator_student]]
  <sub>weak: frontline_worker, researcher</sub>
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]
  <sub>weak: financial_record</sub>

**stack** esbuild, express.js, farmermotion, lucidereact, monacoeditor, node.js, react19, tailwindcss, typescript, vite

## How they structured the write-up

- inspiration

## Body

Problem Statement Students often face difficulties while programming, especially when debugging errors or working with programs provided in laboratory manuals. They frequently have to switch between a code editor, AI chatbot, and lab manual—copying and pasting code between different tools. This interrupts the coding workflow and makes programming tasks more time-consuming. We identified this problem from our own experience as students and aimed to create a single environment that brings these activities together. Solution Overview Cosmic Compiler is an AI-powered, multi-language coding environment that combines code editing, code execution, AI assistance, debugging, and file processing in one platform. Users can upload lab manuals and other supported files, extract relevant programming content, load it into the editor, run the code, and use the AI assistant to create, explain, debug, and improve their programs. The overall workflow is: Upload File → Extract Code → Edit → Run → Debug with AI → Improve Key Features AI Coding Assistant — helps create, explain, debug, and improve code. Multi-Language Compiler — supports Python, C, C++, Java, JavaScript, and HTML/CSS. AI Code Fixing — analyzes code and compiler errors and suggests fixes. Lab Manual Extraction — extracts relevant programs from uploaded documents. Multiple File Support — works with PDF, Word, Excel, CSV, and text files. AI Code Review — allows users to review suggested changes before applying them. Integrated Terminal & Run History — view program output and previous executions. Live HTML Preview — run and preview HTML/CSS/JavaScript directly within the environment. Technologies Used Frontend: React 19, TypeScript, Vite, Tailwind CSS, Monaco Editor, Framer Motion, Lucide React Backend: Node.js, Express, TypeScript/tsx, esbuild AI: Google Gemini, with optional Groq support Document Processing: PDF, Word, Excel/CSV, and text document parsers Code Execution: Python 3, GCC, G++, Java/Javac, and Node.js Target Users College students learning programming Programming beginners who need AI-assisted guidance Students working on programming laboratory assignments Students who frequently work with lab manuals and programming exercises Educators and academic labs looking for a unified programming environment Inspiration As a student, I often face challenges while programming. When I encounter an error or need help improving my code, I usually have to copy the code from the editor, paste it into an AI chatbot for correction or suggestions, and then return to the code editor to apply the changes. Similarly, while working on programming laboratory assignments, I often need to open lengthy lab manuals, find the required program, copy the code, and paste it into the code editor. This repetitive process takes time and interrupts the coding workflow. These challenges inspired me to build Cosmic Compiler, an AI-powered compiler with an agentic coding assistant that can help users create, correct, update, delete, and extract code from lab manuals within a single coding environment. <div