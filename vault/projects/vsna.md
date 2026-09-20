---
slug: "vsna"
url: "https://devpost.com/software/vsna"
title: "VSNE"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 1082
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# VSNE

> Your Personalized Career Mentor – Guiding Your Path to Success, One Step at a Time!

[Devpost](https://devpost.com/software/vsna) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** api, codebuff, css, flask, github, gmail, javascript, linkedin, openaiapi, python, react, sqlalchemy, sqlite, vite

## How they structured the write-up

- inspiration
- tracks we're going for
- what it does
- for the backend
- for the frontend
- team

## Body

Home page Dark mode Home Page Light mode Home Page 2 Light mode User Profile page Dark mode User Profile Page 2 Dark mode User Profile Page Light mode User Profile Page 2 Light mode Spinning cat on the user profile page Roadmap Page Light mode Roadmap page Dark mode Chat with Sage page Dark mode Chat with Sage in action Dark Mode Chat with Sage Light mode Codebuff being used by Sab Codebuff being used by Ewa Home page on mobile device Side bar mobile device User input page on mobile device Spinning cat vid on mobile device Roadmap on mobile device Chat with sage page on mobile device Inspiration The inspiration behind the VSNE Career Mentor Bot came from our desire to create a project that could help others navigate career paths. The name VSNE itself combines the initials of each team member, symbolizing collaboration and unity. The name of the bot is Sage. Tracks we're going for Most Technically impressive - Modal Beginner track Best personal project (CodeBuff) Statsig Grand Prize, Best overall project Magic Loops Generative UI/UX Nethenoob spinning cat Bill Zhang Conversational AI Prize Education and AI What it does The VSNE Career Mentor Bot -Sage- is designed to serve as a personalized career mentor for students and professionals. She helps users navigate the complex world of career development by providing insights, resources, and suggestions. Sage uses AI to offer tailored advice, such as resume tips, job search strategies, and skill-building recommendations. She also provides access to career-related data, such as internships, job postings, and professional profiles from platforms like LinkedIn, enabling users to make informed decisions about their career paths and guides users toward their ideal career paths, offering tailored roadmaps and resources. How we built it Frontend: React, Vanilla CSS Backend: Flask, SQLAlchemy AI/ML: OpenAI API for conversational intelligence Database: SQLite Additional Tools: HTML, CSS, JavaScript Frontend hosting: Vercel for React app. Backend hosting: Vercel for Flask, API, and Database. Challenges we ran into - OpenAI API : This gave us a lot of problems and we couldn't deploy it. But it runs locally. Integration complexity : Integrating AI components into the project, especially for personalized career advice, posed some challenges. Ensuring that the OpenAI API could provide valuable, context-aware responses was an ongoing task. Data scraping limitations : Scraping LinkedIn profiles and internship data required careful handling to avoid potential violations of privacy policies and technical limitations with web scraping tools. Frontend-backend communication : Syncing the frontend and backend seamlessly, especially with the real-time interactions between the bot and the user, required extensive testing and troubleshooting. Ensuring accessibility and cross-browser compatibility : Testing the bot across different devices and browsers while maintaining a consistent user experience was time-consuming but important for the app’s success. Deploying : Deploying the project on vercel was tricky since it was Sab's first time and we ran into many problems but luckily we did it as it is important for the app to be deployed. Accomplishments that we're proud of Seamless AI integration : The team was able to integrate the OpenAI API effectively, allowing the bot to provide relevant and personalized career advice. Responsive and accessible design : The bot’s frontend is responsive and user-friendly across devices, with accessibility features that ensure a broad range of users can engage with the app. Real-time career data : The ability to scrape and display real-time data from LinkedIn and other platforms for users was a major accomplishment, adding significant value to the bot’s functionality. Smooth UX/UI : The project team created an intuitive and enjoyable experience for users, with smooth animations and a clean design that made interactions with the bot straightforward. How to run it locally Clone the repository git clone https://github.com/Nicsims98/Career_mentor_bot.git Change directory to the project folder cd Career_mentor_bot NOTE: Make sure to do this for both the frontend and backend terminal first before the other commands. For the backend Inside the Career_mentor_bot directory, go to code-for-sage folder, and then src folder. cd code-for-sage Create a virtual environment in a terminal: python -m venv venv source venv/bin/activate # on Mac/Linux venv\Scripts\activate # on windows Install dependencies: pip install -r requirements.txt Set up environment variables (create a .env file) echo "FLASK_ENV=development">.env echo "DATABASE_URL=sqlite:///sage.db">>.env Initialize the database flask db init flask db migrate flask db upgrade Run the Flask application python app.py For the frontend In another terminal, Install dependencies(node.js) npm install Run the front end npm run dev The project should run on http://localhost:5173 Deployed link The link : https://vsne-career-mentor-bot.vercel.app/ What we learned AI integration : Nic learned how to effectively use the OpenAI API for personalized user interactions and how to refine responses to be more context-aware. Frontend development techniques : Ewa learned how to improve accessibility, implement hover effects, and create a responsive, interactive UI for both laptops and mobile phones. Additionally, ensuring smooth animations and transitions added to the app’s overall user experience. Backend challenges : The backend team (Sab and Vee) learned more about optimizing Flask to handle API requests efficiently (Sab), web scraping for real-time career data, and sending the personalized recommendations to users emails (Vee). Collaborative development : The team learned how to divide tasks effectively based on each member’s strengths, as well as how to communicate and troubleshoot together as a unit. What's next for VSNE The next steps for the VSNE Career Mentor Bot include: Expand AI capabilities : The team plans to enhance the AI’s advice to cover more career areas, including specific industries and niches. Add more integrations : Integrating with more career platforms, like job boards, and adding additional features, such as automated resume reviews, will be part of the upcoming phases. Mentorship Matching : Mentor matching based on career goals. Internship Finder : Find potential internships for user to apply to. Team Vee: Web scraping for internships and LinkedIn profiles for users recommendations. Sab: Backend development, database management and integration between all components. Nic: AI integration and Flask API development for Sage. Ewa: Frontend development and design. That order forms VSNE ✨✨ Note Even after the extra 1 hour, the chat box refused to work😮‍💨. We couldn't channel our inner sigma😞 ......But it works locally so you can do that if you really want to chat with sage🤓. You know since she's so nice.. and caring... Words can't describe.🤗 But do you still need to chat with her much when the rest of our project is a WWWWW🔥 We're gonna fix it after judging ends 💯 <div