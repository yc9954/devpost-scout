---
slug: "community-canvas-magic-snoo"
url: "https://devpost.com/software/community-canvas-magic-snoo"
title: "Community Canvas: Magic Snoo"
hackathon: "Fun and Games with Devvit Web"
organization: "reddit"
winner: true
words: 711
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
---

# Community Canvas: Magic Snoo

> Bringing communities together, one pixel at a time. A persistent, collaborative canvas where redditors create shared artwork and leave their mark.

[Devpost](https://devpost.com/software/community-canvas-magic-snoo) · hackathon [[Fun and Games with Devvit Web]]

## Facets

  <sub>weak: developer_tools</sub>
  <sub>weak: geospatial, structured_db, video_visual</sub>

**stack** devvit-web-platform, express.js, node.js, react, redis, tailwind, typescript

## Body

An image of a colored mural Inspiration: Reddit's history is filled with legendary social experiments, and none is more iconic than r/place. It proved that communities could create incredible art from the simplest of tools. I was inspired by that spirit of collaboration and wanted to build an experience that any subreddit could use to create its own "r/place moment," turning a simple game into a lasting piece of community history. What it does: Community Canvas is a fully persistent, collaborative art application built for Reddit communities. Launch and Paint: Users launch the app directly from a Reddit post. They can choose a color and click any shape on the canvas to paint it. Persistent Storage: Every color change is saved on the server. When you close and re-open the app, or even refresh the page, the community's artwork is still there, exactly as it was left. User Attribution: The app proudly displays the username of the last person to contribute, giving users a real sense of ownership and recognition for their part in the creation. How I built it: This project was built from the ground up using the modern Devvit Web stack, creating a true full-stack application. Front-End: The user interface is built with React and TypeScript . To keep the code clean and maintainable, the front-end was structured using modern React patterns. The interactive mural itself was encapsulated in its own component ( MagicSnoo.tsx ), turning a complex SVG into a reusable and manageable piece of the UI. All client-side logic including fetching data, managing state, and handling optimistic updates was abstracted into a custom hook ( useCanvas.ts ). This separation of concerns kept the main App.tsx component incredibly clean and easy to understand. Back-End: The server is powered by Node.js and Express , handling API requests for saving and loading data. Database: All canvas data is made persistent using Redis , as provided by the Devvit platform. Platform: The entire experience is seamlessly integrated into Reddit using the Devvit Web Platform . Challenges I ran into: The development journey was a true lesson in perseverance! I started with the excellent Devvit Web React template, which provided a solid foundation. The real challenge was in transforming its simple "counter" example into a complex, full-stack, multi-user application. This required deconstructing the template's default server logic and rewriting it from scratch to handle our specific needs: saving and loading entire objects of canvas data, fetching user information, and handling multiple API endpoints. I had a massive learning curve in understanding the specific way Devvit's server environment works with Redis where I learned that data is stored as strings and must be manually parsed with JSON.stringify and JSON.parse was a huge breakthrough. Every step was a deep dive into the Devvit stack, turning a simple starting point into a completely new and powerful application. Accomplishments that I am proud of: I am incredibly proud that this is not just a simple front-end prototype. It's a complete, full-stack application that was architected with clean, modern React patterns. Overcoming the technical challenges to design and build a robust client-server architecture with a clear separation of concerns on the front-end was a huge accomplishment. More than anything, I am proud that the final product is a polished, stable, and genuinely fun experience that is ready for a real community to enjoy. What I learned: This hackathon was an incredible learning experience. I learned how to take a starter template and fundamentally reshape it to fit a new, more complex vision. I gained a deep, practical understanding of the entire Devvit Web architecture, from writing server-side Express routes and managing Redis storage to connecting everything to a responsive React front-end using custom hooks. Most importantly, I learned that even the most stubborn bugs can be solved with methodical debugging and a refusal to give up. What's next for Community Canvas: Magic Snoo The "Community Canvas" is built to be an engine. The next step is to create a whole library of different Snoo murals and other designs that communities can choose from. I envision this becoming a weekly event in subreddits, where members vote on the next canvas and work together to complete it, creating a new tradition and a gallery of community-made art. <div