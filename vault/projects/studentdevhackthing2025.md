---
slug: "studentdevhackthing2025"
url: "https://devpost.com/software/studentdevhackthing2025"
title: "BackOnTrack"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 1211
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# BackOnTrack

> Stay Focused With Friends

[Devpost](https://devpost.com/software/studentdevhackthing2025) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** claude, css, html, javascript, neon-database, react, sql, typescript, v0.dev, vercel, whereby-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for backontrack
- ai tools disclosure

## Body

Inside a classroom. This is the members tab, and other options such as study sessions and notes are on the sidebar A look at a class dashboard. You can see classes Aryan is part of as well as the option to join and create classes. A look inside a study session, where you can see Aryan and Ronit on call, as well as a study session timer. Our AI Tutor, a wrapper of Grok. It is instructed to ask students follow up questions, to test for understanding. Inspiration All of us struggled to get our work done on our own. Any time we had a question, finding an answer felt nearly impossible: no one around could help, and opening the internet was always a gamble that the next three hours would disappear into social media. On top of that, we constantly forgot due dates, important meetings, and class notes, which only piled on more stress. Night after night, we found ourselves scrambling to finish assignments at 11:59, not because we lacked dedication, but because we were continually falling victim to the distractions built into the online world. What it does We created Back On Track as a collaborative study platform to help students stay organized and learn together. On the website, users start by creating an account. Then they have the option to join classes using a class code, or create a new class. Members in a class can view and upload notes, assignments, and calendar events, and also chat with an AI tutor. But the most important feature of Back On Track is how they can create and join group study sessions together. Users can start a group study session with a timer and invite their classmates, and they will be able to talk to each other in a video call. Alternatively, they can create a solo study session so they can study by themselves with a timer. Together, these features make it easier for students to stay focused, stay connected, and get their work done. How we built it We built our website by first outlining our idea, goals, and key features, which helped us create our first HTML prototype using Claude by Anthropic. After a few iterations with Claude and UI/functionality edits, we had a clean single-file codebase to upload into v0 by Vercel. From there, v0 generated a fully functioning React app that we deployed to Vercel. Once v0 applied our basic UI, we began the backend with an email-based account system, a database linking class data to users, and a full video communication setup. We started with email and database work using v0 and initially used Supabase. The issue was that Supabase wouldn’t reliably connect usernames to account IDs in a way our UI could retrieve and display. We solved this by switching to Neon, which let us use SQL storage instead of Supabase’s Members API. After rebuilding the backend from our base code, we updated the UI to a modern black and white theme. Next, we added the note-sharing system using Azure Blob so students can upload class notes. For video calling, we first tried Agora’s API, but it failed due to restrictions we couldn’t bypass. We then switched to WhereBy’s API, which worked smoothly and came with free credits. Finally, for the AI chatbot in each class, we integrated GrokAI’s API since it works well with Vercel and gave us ten dollars in free credits. Challenges we ran into Overall we faced many challenges from arguing with each other to major technical problems. Our major problem was with SupaBase, our backend storage database where all of our data was stored for our website. This gave us many problems as we were not able to fetch the username from userID no matter how many times we reformatted the database tables and rewrote the code. Eventually, we found Neon as an alternative and fully switched to Neon which completely fixed our problems. Our next challenge was with the video call API where we first used Agora’s API but switched to WhereBy’s API as it allowed us to implement it better in our UI and backend. Then the final challenge we faced was arguments among ourselves. When working in a group there are always disagreements over what to implement, how to go about it, and who needs to do what. But again, we managed to make compromises, create an effective system for work distribution, and move past our issues. I think we’re all proud of our final product. Accomplishments that we're proud of Our app is fully functional and ready to be deployed in schools. We have designed the app to be able to support more changes in the future which will allow us to deploy the application in our own school. Working together as a group and overcoming our problems such as figuring out the SupaBase error and replacing it with Neon. We went from a broken presence system to a fully stable class-wide collaboration flow within four hours after switching databases. This project allowed us to learn from each other and increase our knowledge by just collaborating and developing with each other. What we learned We would say the biggest technical topic we learned was on how to better debug. One of the biggest reasons why we were struggling a lot on bugs at the beginning was because none of us properly utilized the console logs. However, as we progressed through the hackathon, we started using the logs, and it made our bug fixing much faster. The logs were also how we fixed our bug regarding the online status of users, as we realized WebSocket and Vercel often ran into issues when implemented together. This was discerned from errors returned from the logs. Overall, we learned how to better use the logs and will for sure be using them in the future to debug. Additionally, we learned so much on how to collaborate effectively from setting up Github and using branches, pushing, and pulling to effectively allow us to work together. At first, we were a mess when it came to organizing tasks, but we learned to distribute the tasks in a way where we were working together and working as effectively as possible. So the best skill that we learned was how to collaborate among each other and overcome arguments(we had a bunch) by creating compromises which ultimately made our project way better. What's next for BackOnTrack Our group really believes Back On Track has the potential to be turned into something beyond a hackathon project, and we want to continue developing this project. We are playing with a few more ideas, such as turning the web application into an app, and allowing schools to become more involved in the process, such as allowing teachers to create classrooms for students. We also have plans to present our platform to our school because we believe it can be helpful to students. Overall, we hope to keep working on BackOnTrack and making it a better experience for anybody that decides to use it. AI Tools Disclosure We used Claude to generate the frontend code for the UI, and then had v0.dev generate the backend. We also used ChatGPT occasionally to help us debug any errors. <div