---
slug: "devorbit-dmp8u3"
url: "https://devpost.com/software/devorbit-dmp8u3"
title: "DevOrbit"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 510
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# DevOrbit

> The ultimate space for developers to network, collaborate, share and work together!

[Devpost](https://devpost.com/software/devorbit-dmp8u3) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** drizzleorm, nextjs, postgresql, socket.io, tailwindcss, three.js, typescript

## How they structured the write-up

- 💡 the idea
- ✨ what it does
- 🛠️ how we built it!
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- ✨ what's next for devorbit!

## Body

DevOrbit 🚀 DevOrbit is the ultimate space for developers to pair program, share code snippets, and work together. Whether you're looking to work on a project, brainstorm new ideas, or just have a random chat about your favorite tech topics, DevOrbit has got you covered. It's where magic happens—think of it as your coding spaceship. 💡 The Idea The idea behind DevOrbit was to create a space where developers from around the globe can connect and collaborate based on their interests. I find myself to be very efficient when I code alongside some hardworking folks on my idea, it keeps me going and sometimes even gives rise to new ideas during chat. So yes, that is kinda the idea behind DevOrbit. ✨ What it does DevOrbit provides devs with the following features: SignUp/SignIn 🔐 : Social login using Google is used. Room Creation and Joining : Easily create or join rooms to collaborate with others. Tags based room filter 🔍 : Search for rooms using tags on tech the room is using. Video Meetings 🎥 : Video meetings with screen sharing, pinning, picture-in-picture mode, etc. Chat 💬 : Communicate with other participants in real-time using Socket.io. Excalidraw : Each room has its own Excalidraw whiteboard session that in-room users can make use of. Room Info Box : Handy information about the current room. Task Management 📝 : Stay organized with a task list feature. Timer ⏱️ : Keep track of your sessions with a built-in timer. 🛠️ How we built it! Started out by roughly sketching the idea on an Excalidraw board with all the features and how and where it will go in the application. Then used the following technologies to implement the idea: Next.js for server-side rendering and static site generation. TypeScript for type-safe code. Tailwind CSS for the style. Socket.io for real-time chat functionality. getStream.io for video meetings and screen sharing. PostgreSQL for database management. Drizzle ORM for simplifying database operations. Excalidraw for real-time drawing and diagramming. Google OAuth for secure user authentication. three.js for the landing page animation. 🚧 Challenges we ran into Establishing the Socket.io connection for the chat functionality threw a lot of errors, and I had to spend a lot of time debugging. 🏆 Accomplishments that we're proud of Successfully integrating video meetings in the application. Implementing the chat functionality (this took quite a lot of debugging and time lol). Creating a common collaborative drawing board with Excalidraw for each room. 📚 What we learned Learned a lot about the backend part of applications and used PostgreSQL and Drizzle ORM for the first time, and it was really fun. Learned about Socket.io and using it in a Next.js application. And lastly, patience lol (debugged errors related to chat functionality for 3 days straight T_T). ✨ What's next for DevOrbit! Frontend deployment on Vercel is done, but there is still the deployment of the backend to be done, and I am planning on using Heroku to do so. There is still some optimization stuff to do and changing the logo of the application. <div