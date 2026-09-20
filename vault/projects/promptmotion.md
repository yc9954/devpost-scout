---
slug: "promptmotion"
url: "https://devpost.com/software/promptmotion"
title: "VibeMovie"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 1322
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/agriculture_food"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# VibeMovie

> Agentic & Conversational video editing!

[Devpost](https://devpost.com/software/promptmotion) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[agriculture_food]]
**substrate** [[geospatial]] [[transcript_audio]] [[video_visual]] [[web_dom]]

**stack** docker, express.js, gemini, javascript, node.js, react, remotion, typescript, vite, zustand

## How they structured the write-up

- 💡 inspiration
- 🎬 what it does
- 🛠️ how we built it
- 🚧 challenges we overcame
- 🏆 accomplishments that we're proud of
- 🎓 what we learned
- 🗺️ what's next for vibemovie

## Body

VibeMovie : An AI-Native Video Editor 💡 Inspiration The world of video editing is filled with powerful, professional-grade tools that are capable of producing cinematic masterpieces. However, this power often comes at the cost of complexity. Steep learning curves, cluttered interfaces with hundreds of buttons, and the manual nature of timeline-based editing can feel more like operating heavy machinery than engaging in a a creative act. We were inspired by the recent breakthroughs in conversational AI and asked ourselves: What if you could create a video just by describing it? We envisioned a tool that would remove the technical barriers and allow creators to focus purely on their vision. Instead of searching through menus to find the "fade" effect, you could simply ask: "Fade in the title text." Instead of manually scrubbing a timeline to find a scene, you could say: "Cut to the part where the rocket launches." This desire to make video creation as intuitive and fluid as a conversation was the core inspiration for VibeMovie. 🎬 What it does VibeMovie is an AI-native video editor that turns natural language into a rendered video. It works like a creative partner. A user can start with a raw video file, or even a blank canvas, and direct the entire editing process through a simple chat interface. 💬 Chat-Based Editing Users can ask the AI to perform a wide range of editing tasks, such as: "Add a title that says 'My Awesome Trip'." "Cut the first 5 seconds of the video." "Put a smooth fade-out effect at the end." "Make the text on screen red and larger." 📊 Live Visual Timeline While the user chats with the AI, a dynamic timeline provides a real-time visual representation of the video's structure. Users can see the clips, tracks, and their arrangement as the AI makes changes. 👉 Direct Manipulation Although AI-driven, the interface still allows for direct, hands-on adjustments. Users can drag clips to change their timing, trim their edges, or split them with a double-click. ✨ High-Quality Export Once the user is happy with the result, they can click the "Export" button to have the entire composition rendered into a high-quality MP4 video, with all the AI-generated edits, effects, and assets included. 🛠️ How We Built It VibeMovie is architected as a modern monorepo, with a powerful frontend engine that talks to an intelligent backend brain. The entire system is built around a single, declarative principle: video is just data. 🖥️ The Frontend: A Full-Featured Video Editor Engine We didn't just build a UI; we engineered a complete video editing engine from the ground up, designed to run entirely in the browser. The Core: The interface is built on React . At its heart it is a highly interactive, scalable, and draggable timeline component . This custom component uses @dnd-kit to provide users with the precise, intuitive drag-and-drop editing experience they expect from a professional tool. State Management: State is managed by Zustand . The entire video structure—every clip, text overlay, and transition—lives as a single, predictable JSON object. This is our "single source of truth." Live Preview: We use @remotion/player to provide a frame-accurate, real-time preview. It reads the JSON state directly from Zustand and renders the visual output, giving users instant feedback on every edit. 🧠 The Backend: The AI Director & Render Farm Our Node.js and Express server acts as the central intelligence and heavy-lifting powerhouse for the editor. The AI Bridge: It leverages the Google Gemini API to translate a user's natural language prompts into precise actions. We engineered a sophisticated prompt that teaches the AI how to read the incoming video JSON and rewrite it to apply the requested edits. The Render Engine: On export, the backend transforms into a powerful render farm. It uses @remotion/renderer to programmatically render the final composition into a high-quality MP4 file using a headless Chrome instance. 🌉 The Bridge: Our JSON-to-Video Compiler The secret sauce is how we connect everything. The entire video is represented as a declarative JSON object. We built a custom JSON compiler that dynamically maps this data structure into a tree of React components. Remotion then takes these components and renders them, frame by frame, into the final video. This architecture is incredibly powerful: whether the user drags a clip or the AI edits the vibe, they are both just manipulating a simple JSON object. 🚧 Challenges We Overcame 1. Teaching the AI to Edit Video Correctly Translating ambiguous human language like "make this cooler" into a precise JSON data structure was our biggest hurdle. Getting the AI to consistently output perfectly structured, nested JSON without a single misplaced comma was a massive prompt engineering challenge. Solution: We developed a multi-layered approach: advanced prompts with few-shot examples, a strict schema definition provided to the AI, and a robust validation layer on our backend to catch and sanitize any malformed AI output before it could break the editor. 2. Building a Performant, Interactive Editing Engine A video editor needs to feel fluid and instant. Building a performant UI with a draggable, scalable timeline that renders a live preview without lagging was a significant frontend engineering feat, especially as projects became more complex. Solution: This required a deep focus on React performance, meticulous state management with Zustand to prevent unnecessary re-renders, and leveraging battle-tested libraries like @dnd-kit to handle the complex interactive elements efficiently. 3. Mastering Server-Side Video Rendering Rendering a video on a server requires that the server have access to all the assets. However, blob: URLs for media uploaded in the browser are completely inaccessible to our backend rendering process. Solution: We engineered an on-demand asset pipeline . Just before rendering, the frontend identifies all local assets and uploads them to our server. The backend then remaps the paths in the JSON structure, ensuring the headless browser can find and composite every file into the final video seamlessly. 🏆 Accomplishments that we're proud of A Truly Conversational Interface We succeeded in creating an editor where complex actions can be triggered by simple, intuitive language. Watching the AI correctly interpret a command like "add a title and make it slide in from the bottom" and then seeing it reflected instantly on the timeline is a magical experience. The Hybrid Editing Model We're proud of the seamless integration between AI-driven editing and direct manual manipulation. The user is never locked into the AI's choices; they can always fine-tune the results by hand, offering the best of both worlds. The Server-Side Rendering Pipeline Building a fully automated, on-demand video rendering service on the backend was a significant technical achievement. It allows for high-quality, reliable exports without freezing the user's browser, which is a common problem with client-side video rendering. 🎓 What we learned Throughout this project, we learned that the future of creative software lies in abstracting complexity. The most powerful tool isn't necessarily the one with the most features, but the one that provides the most intuitive path from an idea to a result. Representing the entire video as a declarative JSON object was a revelation. It treated the video not as a monolithic file, but as a "script" that could be programmatically written, edited, and remixed. This approach makes it incredibly scalable and opens the door for even more powerful AI integrations in the future. 🗺️ What's next for VibeMovie This hackathon project is just the beginning. We're excited about the potential to expand on this foundation: Advanced AI Capabilities: Integrating more sophisticated AI models that can analyze video content (e.g., detecting scenes, identifying objects, generating transcripts) to perform even smarter edits. Real-Time Collaboration: Allowing multiple users to edit the same timeline, with the AI acting as a moderator and assistant. Template Library: Introducing a library of pre-built templates and effects that users can apply and customize through conversation. Expanding Media Support: Adding support for more complex media types, such as images, GIFs, and more advanced audio mixing. <div