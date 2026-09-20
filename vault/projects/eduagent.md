---
slug: "eduagent"
url: "https://devpost.com/software/eduagent"
title: "EduAgent"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 1329
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# EduAgent

> Many advanced topics are only taught through dense media such as textbooks. Using Agentic AI, our team created a platform that takes text, and transforms it into an easy-to-understand, simple video.

[Devpost](https://devpost.com/software/eduagent) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** claude, crewai, html, lmnt, python, radio, tex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- 1. contentextractoragent
- 2. lessonplanneragent
- 3. manimagent
- 4. lmntnarratoragent
- 5. videocomposeragent
- 6. qualitycheckeragent
- orchestrating the pipeline: crew
- why it works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eduagent

## Body

Inspiration Inspiration Simply put, we were inspired by 3Blue1Brown. Grant Sanderson of 3Blue1Brown taught complex mathematical and scientific topics intuitively through targeted, minimalist animations. Our team comes from a wide array of technical backgrounds (including applied mathematics, computer science, data science, and data theory). While tools like Manim (The image generation tool that Sanderson uses in 3Blue1Brown) are powerful, they require significant programming expertise. Our goal was to build a system that allows educators and students to generate these high-quality, explanatory videos simply by providing a topic or a block of text, making advanced learning more accessible to everyone. What it does EduAgent is an automated video generation pipeline that transforms a user's text-based prompt into a short, animated educational video. A user can input a concept (e.g., "The Pythagorean Theorem," "How does a 4-stroke engine work?"), and the system will: Research and Script: Break down the topic into a logical, easy-to-understand video. Generate Visuals: Create corresponding Python code for the Manim animation library to visualize each part of the script. Synthesize Voice: Produce a natural-sounding voiceover that reads the script. Compile: Render the animations, sync them with the audio, and deliver a final, polished MP4 video file. The result is a concise, graphically-rich video that explains the core concepts of the prompt, ready for use in classrooms, presentations, or online learning. How we built it Educational Video Generation Pipeline: Powered by Specialized Agents The system employs a carefully designed pipeline that uses six specialized agents to transform raw educational content into engaging, high-quality videos. Each agent is responsible for a specific task in the process, ensuring that the final product is both educational and visually captivating. The agents work together seamlessly, guided by a central orchestrator known as the Crew . Here’s a breakdown of each agent in the pipeline: 1. ContentExtractorAgent The first step in the process is content extraction. The ContentExtractorAgent analyzes and extracts relevant information from input files, such as PDFs, images, and other educational documents. This agent is critical for identifying key content to be used in the video, such as text, diagrams, and graphs, which will later be incorporated into animations and voice narrations. By converting static information into usable data, this agent serves as the foundation for the entire process. 2. LessonPlannerAgent Once the content is extracted, the LessonPlannerAgent steps in to organize and structure the educational material into a cohesive lesson plan. This agent takes the raw content and arranges it into a logical sequence, ensuring that the flow of the lesson is engaging and pedagogically sound. The lesson plan outlines what concepts to cover, in what order, and what visuals or examples should be included, providing a roadmap for the rest of the pipeline. 3. ManimAgent The ManimAgent is responsible for bringing the lesson plan to life with high-quality mathematical and educational animations. This agent generates precise, dynamic visuals using Manim , a powerful mathematical animation library. Whether it's illustrating complex mathematical formulas or visualizing scientific concepts, the ManimAgent ensures that the visualizations are not only accurate but also engaging for learners. The animations are designed to match the educational content outlined by the LessonPlannerAgent , providing a clear and compelling way to visualize abstract concepts. 4. LMNTNarratorAgent No educational video is complete without clear, high-quality narration. The LMNTNarratorAgent uses LMNT's cutting-edge voice engine to generate audio narration for the video. The voiceover is crafted to align with the lesson plan and animations, ensuring that the spoken content matches the visuals and helps reinforce key points. The LMNTNarratorAgent also ensures that the narration is clear, engaging, and professional, making it an essential part of the overall learning experience. 5. VideoComposerAgent Once the animations and audio narration are ready, the VideoComposerAgent takes over to combine these elements into a polished final video. This agent arranges the animations and narration in the correct sequence, synchronizing them to create a seamless viewing experience. The VideoComposerAgent also handles transitions between scenes, background music, and any other visual elements required to produce a high-quality educational video. The result is a well-structured, visually engaging, and informative video that is ready for distribution. 6. QualityCheckerAgent The final step in the pipeline is quality assurance. The QualityCheckerAgent rigorously reviews the finished video to ensure that it meets both technical and educational standards. This agent checks for any issues with video quality, audio clarity, and synchronization between the visuals and narration. It also ensures that the content is pedagogically effective, verifying that the video achieves its educational goals. If any issues are detected, the video is sent back for adjustments, ensuring that only the highest-quality educational videos are delivered. Orchestrating the Pipeline: Crew The entire pipeline is managed by Crew , an orchestrator that ensures each agent performs its task in the correct order. The orchestrator tracks the completion of each step and moves the process forward only when the previous step is successfully finished. This systematic approach ensures that the pipeline runs smoothly, with each agent contributing its specialized capabilities to produce the final educational video. Why It Works This specialized-agent system is designed to maximize efficiency and quality. Each agent is fine-tuned to handle a specific task, allowing for expert-level execution at each stage of the pipeline. By using this modular approach, the system can generate high-quality educational content while maintaining flexibility and scalability for a variety of subjects and formats. This well-organized pipeline leverages the power of specialized agents working together, ensuring that the final product is not only visually appealing but also pedagogically effective and tailored to the needs of the learner. Challenges we ran into Building an automated end-to-end video pipeline presented several significant challenges: Agent Hallucination and Code Quality: Early tests with other models resulted in frequent generation of non-functional or buggy Manim code. We overcame this by switching to Claude , which proved far more reliable in generating correct and complex code from natural language prompts. We also implemented a strict validation and error-handling step in our compiler. Temporal Synchronization: Aligning the timing of the voiceover with the on-screen animations was a major hurdle. We solved this by having the Scriptwriting Agent embed timing cues and animation triggers directly into the script, which the Animation Code Agent then used to pace the visual scenes. Maintaining Context Between Agents: Ensuring the Animation Agent understood the intent of the script written by the Scripting Agent was difficult. We developed a structured JSON format for inter-agent communication, which included not just the text but also metadata about the desired tone, visual elements, and pacing. Accomplishments that we're proud of We are incredibly proud of successfully creating an automated "text-to-video" pipeline for educational content. Specifically, we're proud of the modular agentic architecture, which is easily extensible, generating a complex proof-of-concept video, explaining the "Introduction to Derivitives" in calculus (a topic that requires precise visual and narrative coherence) and the quality of the final output (which features clean animations, clear narration, and great synchronization with minimal user intervention). What we learned This project was a deep dive into the practical applications of agentic AI workflows. Our key takeaway is that agent specialization is super important. Using multiple, specialized agents is far more effective than relying on a single Agent. Each agent can be fine-tuned for its specific task, leading to a higher-quality result. What's next for EduAgent We see a bright future for EduAgent and have a clear roadmap for expansion: Subject-Specific Agents: We plan to develop agents trained for specific domains, such as a History Agent that can generate animated maps and timelines, or an Art History Agent capable of analyzing and annotating famous artworks. User Customization: Allow users to choose different animation styles, voices, languages, and levels of detail (e.g., "Explain this for a 5th grader" vs. "Explain this for a college student"). Interactive Feedback Loop: Implement a feature where users can provide feedback on a generated video (e.g., "that part was confusing"), which the system can use to automatically regenerate a better version. <div