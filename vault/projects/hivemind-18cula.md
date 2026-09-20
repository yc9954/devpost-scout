---
slug: "hivemind-18cula"
url: "https://devpost.com/software/hivemind-18cula"
title: "HiveMind"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1307
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# HiveMind

> HiveMind: Your Second Brain for Smarter Learning.

[Devpost](https://devpost.com/software/hivemind-18cula) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[structured_db]] [[transcript_audio]]

**stack** api, chromadb, flask, gemini, intersystems, nextjs, perplexity, python, sonar, streamlit, superbase, three.js, typescript, vector-embedding

## How they structured the write-up

- problem
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hivemind

## Body

HiveMind Problem Education is one of the most powerful tools for personal and professional growth, yet the way knowledge is imparted remains largely standardized and inflexible. Many students struggle with course material because traditional learning methods fail to cater to individual learning needs. Some students grasp concepts quickly, while others require additional time and explanation, leading to gaps in comprehension that affect academic performance and long-term retention. Moreover, collaboration and peer learning opportunities are often limited, leaving students to navigate their academic struggles alone. Some students grasp concepts effortlessly and can help their peers, but there is no structured way to connect them. Our goal is to change this by creating an intelligent, AI-driven educational platform that adapts to each student’s needs, making learning more effective, engaging, and inclusive. Inspiration The idea for HiveMind was born from observing the disparity in student learning experiences, and have a framework based system to collectively improve everyone in the class week by week, leaving no one behind. We created a system that fosters collaborative learning environment, collective growth and collective improvement until everyone in the class is on same level of understanding and comprehension. What it does HiveMind is an AI-powered educational platform that enhances student learning through continuous collective growth through peer learning sessions. By seamlessly integrating with online learning environments, the platform analyzes student responses and categorizes them into different levels of understanding. This classification enables the system to provide tailored support, ensuring that students who need extra help receive it, while those who have mastered concepts can reinforce their knowledge by guiding others. The platform assesses student performance through AI-driven quizzes and assignments, determining their comprehension levels. Based on this analysis, students are placed into one of four learning hubs: those requiring foundational support, those needing additional clarification, those who have a strong grasp of concepts, and those who have achieved mastery. This hub is made up of a right balance of 4 students and this matching is done by the custom algorithm. The system then facilitates peer matching, allowing students with higher scores to assist those in lower scores. Additionally, Its seamless integration with existing learning platforms ensures that students receive real-time feedback and targeted support without disrupting their educational workflow. How we built it HiveMind was developed using a combination of advanced web technologies, machine learning frameworks, and 3D visualization tools. Our backend, built with Python, manages data processing, user authentication, and AI-driven assessments. We implemented custom algorithms to evaluate student performance, generating meaningful insights that adapt to their learning needs. The frontend, developed with TypeScript, Three.js, and Next.js, provides an intuitive interface where students can track their progress through an interactive 3D brain visualization. To enable real-time peer matching and vector-based assessments, we incorporated vector embeddings using IRIS Vector database, and Perplexity Sonar API reasoning that analyze student responses and categorize them accordingly. These embeddings are stored efficiently to facilitate quick retrieval, ensuring smooth transitions between different learning levels. Once the peers are matched, they will go through a Zoom session which is monitored by an AI agent which evaluates the progress of the student as well as the hub. Throughout the development process, we optimized the platform for scalability, ensuring that HiveMind could accommodate a growing number of users without performance bottlenecks. The integration of AI, real-time analytics, and peer-to-peer networking allowed us to create a seamless experience that enhances student engagement. Challenges we ran into One of the biggest challenges we faced was merging the 3D dashboard into our existing system, which already included vector embeddings and a peer-to-peer network. This led to numerous Git merge conflicts, causing unexpected issues that disrupted our workflow. With time running out, we had to make a critical decision—to start fresh with a new GitHub repository in the final hours of development. This shift required us to carefully migrate existing functionalities while ensuring that all components remained fully functional. Rendering the 3D brain visualization was another major hurdle. Achieving a balance between performance and visual appeal proved difficult, as real-time interactions required optimized rendering techniques. We experimented with various configurations in Three.js, adjusting parameters to ensure smooth animations and intuitive navigation. Additionally, maintaining compatibility across different devices added another layer of complexity, as rendering performance varied based on system specifications. Despite these challenges, our team remained persistent, debugging issues, restructuring code, and finding creative solutions to ensure that HiveMind functioned as intended. Overcoming these obstacles reinforced our teamwork and problem-solving skills, making the final product even more rewarding. Accomplishments that we're proud of Building HiveMind was an ambitious challenge, and we are proud of what we have achieved so far. One of our biggest accomplishments is successfully implementing an AI-driven assessment system that evaluates student comprehension in real-time. Our machine learning models accurately categorize students based on their understanding, enabling tailored learning experiences that adapt dynamically to individual needs. We also developed a structured peer-matching system that facilitates collaboration between students at different knowledge levels, fostering a strong sense of community and support within the platform. Another major achievement is our intuitive , which provides students with a clear and interactive representation of their learning progress. By integrating AI-driven insights with visually appealing analytics, we have transformed the way students perceive their academic journey. Additionally, our backend infrastructure is optimized for scalability, ensuring that HiveMind can handle a growing number of users without compromising performance. Successfully integrating the platform with online learning tools while maintaining a seamless user experience was a significant milestone that highlights our technical expertise and problem-solving abilities. What we learned Throughout the development of HiveMind, we encountered numerous challenges that pushed us to think critically and innovate. One of the most valuable lessons we learned was the importance of real-time processing in educational platforms. Immediate feedback is crucial for student engagement, and optimizing our AI models to deliver quick yet accurate assessments requires extensive experimentation and fine-tuning. We also gained a deeper understanding of the complexities involved in integrating AI-driven tools with existing educational platforms. Ensuring compatibility with learning management systems, designing efficient data pipelines, and maintaining user privacy were all critical considerations that shaped our development process. Furthermore, we realized that while AI can enhance learning, human interaction remains an essential element of education. This insight reinforced our belief in combining AI-driven recommendations with peer-based learning to create a balanced and effective system. From a user experience perspective, we learned the significance of designing interfaces that encourage participation without overwhelming students. Keeping the UI simple yet powerful was a challenge that required iterative testing and feedback. Understanding the psychology of learning and motivation helped us refine our platform to make it more engaging and beneficial for students. What's next for HiveMind HiveMind is only at the beginning of its journey, and we have exciting plans for its future. One of our key next steps is integrating the platform with Zoom, enabling real-time transcription and AI-powered suggestions during class discussions. This feature will enhance virtual learning by providing students with relevant questions, summaries, and recommendations, making online education more interactive and insightful. We also aim to enhance our adaptive learning models to provide even more personalized learning paths. By refining our AI algorithms, we can ensure that each student receives targeted resources and exercises tailored to their specific needs. Another major focus is incorporating gamification elements, such as achievement badges, leaderboard rankings, and interactive challenges, to keep students motivated and engaged throughout their learning journey. In the long term, we plan to expand HiveMind’s reach by forming partnerships with universities, online learning platforms, and EdTech companies. By integrating our system into large-scale educational environments, we can impact a wider audience and help bridge learning gaps across diverse student populations. Our vision is to make education more personalized, collaborative, and accessible, ensuring that every student has the tools they need to succeed. <div