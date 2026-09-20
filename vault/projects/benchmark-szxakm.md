---
slug: "benchmark-szxakm"
url: "https://devpost.com/software/benchmark-szxakm"
title: "BENCHMARK"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 721
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/cross_origin_web"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# BENCHMARK

> Overwhelmed by projects and hobbies? BENCHMARK is a simple, 100% private dashboard to track your tasks and progress. Runs offline in your browser, with zero setup needed.

[Devpost](https://devpost.com/software/benchmark-szxakm) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[cross_origin_web]] [[structural_withholding]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]] [[web_dom]]

**stack** css3, html5, javascript, localstorage, vanilla

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for benchmark

## Body

Inspiration As students, we are constantly juggling a mix of academic projects, personal hobbies, and creative ideas. We tried using complex project management tools, but found they were often bloated with features we didn't need, required an internet connection, and raised concerns about data privacy. We were inspired to create a tool that was the exact opposite: a beautiful, simple, and powerful tracker that respects your privacy, works completely offline, and gets out of your way so you can focus on what matters—building and creating. What it does BENCHMARK is a single-page application that helps you track your creative projects and hobbies with zero fuss. It features: A Dynamic Dashboard: View all your projects as clean, responsive cards. Complete Tracking: Each project has its own task list and a progress log for notes and milestones. Light & Dark Modes: Instantly switch themes to suit your preference. Powerful Search & Filtering: Quickly find projects by name or filter your view by status (Active, On Hold, Completed). 100% Privacy & Offline Use: BENCHMARK uses your browser's localStorage, meaning your data never leaves your computer and the app works perfectly without an internet connection. Data Portability: You can export a full backup of your data to a JSON file and import it back anytime, making it easy to move between devices. Zero Installation: It's a single HTML file that runs in any modern browser. No setup required. How we built it We made a deliberate choice to build BENCHMARK without any frameworks to prove that a powerful and modern application can be created with just the fundamentals. The entire application is a single HTML file. We used Vanilla JavaScript for all the logic, including DOM manipulation, event handling, and managing the project data. All data is saved and retrieved from the browser's localStorage API, which acts as our simple, private database. The user interface was styled with modern CSS, leveraging CSS Grid for the responsive dashboard layout and CSS Variables to implement the light and dark themes efficiently. The result is a highly portable, dependency-free application that is incredibly fast and requires zero installation. Challenges we ran into The biggest technical challenge was managing the application's state and keeping the UI perfectly in sync with the data in localStorage without a framework like React or Vue. Without a virtual DOM, we had to be very intentional about how the screen was updated after every change (adding a project, checking off a task, etc.). We solved this by creating a single, powerful render() function that is responsible for redrawing the entire project list based on the current data array. This approach, while simple, required careful logic to ensure that event listeners were correctly re-attached after each render and that the user's search and filter selections were always respected. Accomplishments that we're proud of We are incredibly proud of building a feature-rich, modern application in a single file with zero dependencies. This was a core goal and a significant technical achievement. We're also very proud of the clean, intuitive UI/UX, especially the seamless light/dark mode and the powerful, instant search functionality. Finally, implementing the full data export/import feature was a major accomplishment, as it gives users complete ownership and control over their data, which is a principle we strongly believe in. What we learned This project was a deep dive into the power of core web technologies. We learned just how much can be accomplished with Vanilla JavaScript and modern CSS without reaching for a heavy framework. We gained a much deeper understanding of the localStorage API, data serialization with JSON, and the importance of writing modular, maintainable JavaScript code even in a single-file project. Most importantly, we learned that prioritizing user privacy and simplicity can lead to a more elegant and effective product. What's next for BENCHMARK BENCHMARK has a solid foundation, and we see a clear path for future enhancements based on user feedback. Our immediate next steps include: Project Deadlines: Adding a simple date field for project deadlines. Tagging System: Implementing a tagging system to allow for more flexible project organization and filtering. Advanced Sorting: Adding options to sort projects by creation date or last updated time. PWA Conversion: Exploring packaging BENCHMARK as a Progressive Web App (PWA) to give it a more native, installable experience on both desktop and mobile devices. <div